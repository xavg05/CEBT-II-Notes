"""Refresh only changed RE/PDC bodies, preserving current navigation and labels.

The historical RE section publisher renumbers all display formulas. Match the
unchanged formula identities instead, so new explanatory equations stay unnumbered.
"""
from pathlib import Path
import re,json,subprocess,collections
ROOT=Path(__file__).resolve().parents[3]
MATH=re.compile(r'(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$')
def github(text):
 def render(m):
  if m[1] is None:return '$`'+m[2]+'`$'
  f=m[1].strip();tags=re.findall(r'\\tag\{(\d+)\}',f)
  assert len(tags)<=1
  label='\n**Equation ('+tags[0]+')**\n' if tags else ''
  return label+'\n```math\n'+re.sub(r'\\tag\{\d+\}','',f).strip()+'\n```\n'
 return MATH.sub(render,text)
def key(s):return re.sub(r'\s+','',re.sub(r'\\tag\{\d+\}','',s))
files=[]
for subject in ['Reaction Engineering II','Process Dynamics and Control']:
 for p in sorted((ROOT/'other/work/drafts'/subject).glob('*.md')):
  previous=subprocess.run(['git','show','HEAD:'+p.relative_to(ROOT).as_posix()],capture_output=True,encoding='utf-8')
  if previous.returncode:continue
  text=p.read_text(encoding='utf-8')
  if text==previous.stdout:continue
  native,= (ROOT/'other/obsidian/CEBT-II Notes'/subject).rglob(p.name)
  current=native.read_text(encoding='utf-8')
  if p.name.startswith('RE-S'):
   labels=collections.defaultdict(list)
   for m in MATH.finditer(current):
    if m[1] is not None:
     tag=re.search(r'\\tag\{(\d+)\}',m[1])
     if tag:labels[key(m[1])].append(tag[1])
   def tagged(m):
    if m[1] is None:return m[0]
    candidates=labels.get(key(m[1]),[])
    return '$$'+m[1].rstrip()+('\n\\tag{'+candidates.pop(0)+'}' if candidates else '')+'$$'
   text=MATH.sub(tagged,text)
   assert not any(labels.values()),(p,labels)
  before,rest=current.split('<!-- note-content:start -->',1)
  _,after=rest.split('<!-- note-content:end -->',1)
  content=before+'<!-- note-content:start -->\n'+text.rstrip()+'\n<!-- note-content:end -->'+after
  oldtags=re.findall(r'\\tag\{(\d+)\}',current);newtags=re.findall(r'\\tag\{(\d+)\}',content)
  assert [x for x in newtags if x in oldtags]==oldtags,(p,oldtags,newtags)
  native.write_text(content,encoding='utf-8')
  read=ROOT/'notes'/subject/native.relative_to(ROOT/'other/obsidian/CEBT-II Notes'/subject)
  read.write_text(github(content),encoding='utf-8')
  files.append(read.relative_to(ROOT).as_posix())
(ROOT/'other/work/progress/re-pdc-teaching-publication-20261022.json').write_text(json.dumps(files,indent=2),encoding='utf-8')
print(f'Published {len(files)} RE/PDC note pairs; preserved navigation and current labels.')
