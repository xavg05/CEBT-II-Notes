"""Whole-publication link, label, source-preservation and portable-export checks."""
from pathlib import Path
from urllib.parse import unquote,urlsplit
import re,subprocess,json,tempfile,zipfile,hashlib,os
from PIL import Image
ROOT=Path(__file__).resolve().parents[3]
BASE='8b0c67f'
READ=ROOT/'notes';NATIVE=ROOT/'other/obsidian/CEBT-II Notes'
LINK=re.compile(r'(!?)\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))\)')
def check(base,baseline=False):
 count=0;figures=set();pages=0;labels=0
 for p in base.rglob('*.md'):
  text=p.read_text(encoding='utf-8');pages+=1
  if baseline and p.name!='README.md':
   rel=p.relative_to(ROOT).as_posix()
   old=subprocess.run(['git','show',BASE+':'+rel],capture_output=True,encoding='utf-8')
   if old.returncode and p.name.startswith(('ET-','AB-')):
    ident=p.name.split(' - ',1)[0]
    candidates=subprocess.check_output(['git','ls-tree','-r','--name-only','-z',BASE,'--',str(p.parent.relative_to(ROOT)).replace('\\','/')],cwd=ROOT).decode('utf-8').split('\0')
    previous=[x for x in candidates if Path(x).name.startswith(ident+' - ')]
    if len(previous)==1:old=subprocess.run(['git','show',BASE+':'+previous[0]],capture_output=True,encoding='utf-8')
   if old.returncode==0:
    oldlabels=re.findall(r'\\tag\{(\d+)\}',old.stdout)
    newlabels=re.findall(r'\\tag\{(\d+)\}',text)
    assert [x for x in newlabels if x in oldlabels]==oldlabels,(p,'existing labels shifted')
    labels+=len(oldlabels)
  # Do not treat mathematical notation such as an interval as a Markdown link.
  prose=re.sub(r'```math[\s\S]*?```|(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$|(?<!\\)\$`[^`]*?`\$|(?<!\\)\$(?:\\.|[^$])*?(?<!\\)\$','',text)
  for m in LINK.finditer(prose):
   target=m[2] or m[3]
   if urlsplit(target).scheme or target.startswith('#'):continue
   dest=(p.parent/unquote(target.split('#',1)[0])).resolve()
   assert dest.exists(),(p,target)
   count+=1
   if m[1]:figures.add(dest)
 for p in figures:
  with Image.open(p) as im:im.verify()
 return {'pages':pages,'links':count,'referenced_figures':len(figures),'preserved_existing_labels':labels}
result={'reading':check(READ),'native':check(NATIVE,True)}
sources=[]
for line in subprocess.check_output(['git','ls-tree','-r',BASE,'--','other/sources'],cwd=ROOT).decode('utf-8').splitlines():
 meta,rel=line.split('\t',1)
 if rel.startswith('"'):rel=json.loads(rel)
 p=ROOT/rel;expected=meta.split()[2]
 actual=subprocess.check_output(['git','hash-object','--',str(p)],cwd=ROOT).decode().strip()
 assert actual==expected,(p,'source changed')
 sources.append(rel)
result['unchanged_original_sources']=len(sources)
# Validate the export in an unrelated directory and compare ZIP contents bytewise.
archive=ROOT/'other/obsidian/CEBT-II-Obsidian.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(NATIVE.rglob('*')):
  if p.is_file():z.write(p,p.relative_to(NATIVE.parent))
temporary=tempfile.TemporaryDirectory(prefix='cebt-teaching-recovery-')
if os.name=='nt':
 # The repository deliberately uses descriptive names; exercise a relocated
 # tree through Windows' extended-path API rather than hitting MAX_PATH.
 resolved=Path(temporary.name).resolve()
 assert resolved.name.startswith('cebt-teaching-recovery-') and resolved.parent==Path(tempfile.gettempdir()).resolve()
 temporary.name='\\\\?\\'+str(resolved)
with temporary as tmp:
 dest=Path(tmp)/'Vault/Courses'
 with zipfile.ZipFile(archive) as z:
  assert z.testzip() is None
  z.extractall(dest)
 relocated=dest/'CEBT-II Notes'
 checks=check(relocated)
 assert checks['pages']==result['native']['pages']
 assert checks['links']==result['native']['links']
 for p in NATIVE.rglob('*'):
  if p.is_file():assert p.read_bytes()==(relocated/p.relative_to(NATIVE)).read_bytes()
 result['portable_relocation']=checks
result['zip_sha256']=hashlib.sha256(archive.read_bytes()).hexdigest()
(ROOT/'other/work/progress/teaching-recovery-publication-validation-20261022.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
