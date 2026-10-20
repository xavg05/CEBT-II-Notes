"""Publish PDC canonical short notes to GitHub and portable Obsidian editions.

This scoped publisher leaves existing courses untouched and creates no merges.
"""
from pathlib import Path
from urllib.parse import unquote,urlsplit
import re,json,shutil,tempfile,hashlib,zipfile
import pymupdf
ROOT=Path(__file__).resolve().parents[3]
WORK=ROOT/'other/work';SUBJECT='Process Dynamics and Control'
DRAFT=WORK/'drafts'/SUBJECT;READ=ROOT/'notes'/SUBJECT
EXPORT=ROOT/'other/obsidian/CEBT-II Notes'/SUBJECT
META=json.loads((WORK/'scratch/pdc/note-manifest.json').read_text(encoding='utf-8'))
TOPICS={1:('Control objectives, variables and dynamic modelling','Choose the control objective and process boundary, identify variables, then close the dynamic balances.'),2:('Physical balances and first-order dynamics','Derive mixing, reaction and thermal dynamics from stored mass and energy. Keep variable volume and finite pulses explicit.'),3:('Transfer functions and elementary responses','Subtract a steady baseline, transform zero-state balances, and distinguish self-regulating lags, integrators and transport delay.'),4:('Second-order dynamics and damping','Connect two dynamic states to a pole pair, then derive damping regimes, step response and measurable oscillation features.'),5:('Combining process elements','Multiply series responses, sum signed contributions, and treat branches as copies of information.'),6:('Multiple-input multiple-output models','Use matrix rows for outputs and columns for inputs. Verify coupled balances by checking conserved totals.'),7:('Poles, zeros, stability and steady-state gain','Interpret free modes and forced-response shape separately, then check final-value conditions before computing steady gain.'),8:('Linearisation around an operating point','Expand nonlinear balances at a consistent equilibrium and compare the local model with exact finite-step behaviour.')}
MATH=re.compile(r'(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$')
def github(text):
 def render(m):
  if m[1] is None:return '$`'+m[2]+'`$'
  formula=m[1].strip();tags=re.findall(r'\\tag\{(\d+)\}',formula);assert len(tags)<=1
  label='\n**Equation ('+tags[0]+')**\n' if tags else ''
  return label+'\n```math\n'+re.sub(r'\\tag\{\d+\}','',formula).strip()+'\n```\n'
 return MATH.sub(render,text)
def folder(u):return f'{u:02d} - {TOPICS[u][0]}'
manifest=[]
def pair(rel,text):
 for base,native in [(READ,False),(EXPORT,True)]:
  p=base/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text if native else github(text),encoding='utf-8')
 manifest.append({'path':str((READ/rel).relative_to(ROOT)),'obsidian':str((EXPORT/rel).relative_to(ROOT))})
notes=META['notes'];tags=[]
for i,item in enumerate(notes):
 p=DRAFT/item['filename'];text=p.read_text(encoding='utf-8');tags.extend(map(int,re.findall(r'\\tag\{(\d+)\}',text)))
 u=item['unit'];nav='[Subject index](../README.md) · [Topic overview](README.md)'
 def target(other):return other['filename'] if other['unit']==u else '../'+folder(other['unit'])+'/'+other['filename']
 if i:nav=f'[Previous](<{target(notes[i-1])}>) · '+nav
 if i+1<len(notes):nav+=' · '+f'[Next](<{target(notes[i+1])}>)'
 pair(Path(folder(u))/item['filename'],nav+'\n\n<!-- note-content:start -->\n'+text.rstrip()+'\n<!-- note-content:end -->\n\n'+nav+'\n')
assert tags==list(range(1,META['equations']+1))
reviewed=(WORK/'scratch/pdc/review-complete').exists()
status='Author verification and independent cross-review are complete.' if reviewed else 'Author verification is complete; independent cross-review is in progress.'
index=[f'# {SUBJECT}\n\nRead the eight topics in order. These notes cover the supplied introduction and linear-system dynamics, with physical explanations and derivations. Keep the shared `figs/` folder with the topic folders.\n',f'{status} Equation labels continue through PDC-01–22. Short notes remain separate; complete-section versions await your requested grouping.\n','## Topics\n']
for u,(title,intuition) in TOPICS.items():
 group=[x for x in notes if x['unit']==u]
 overview=f'# {u:02d}. {title}\n\n[Subject index](../README.md)\n\n{intuition}\n\n{status} These short notes remain separate pending a requested merge group.\n\n'
 overview+='\n'.join(f'- [PDC-{x["number"]:02d}: {x["title"]}](<{x["filename"]}>)' for x in group)+'\n'
 if u>1:overview+=f'\n[Previous topic](<../{folder(u-1)}/README.md>)'
 if u<8:overview+=f'\n[Next topic](<../{folder(u+1)}/README.md>)'
 pair(Path(folder(u))/'README.md',overview+'\n')
 index.append(f'- [{u:02d}. {title}](<{folder(u)}/README.md>) — PDC-{group[0]["number"]:02d}–{group[-1]["number"]:02d}')
index+=['','## Source coverage and remaining material','','The supplied chapters 1–2 contain 42 PDF pages. The full visual scan and supplementary-source record are in [the production record](<../../other/work/progress/PDC-chapters1-2.md>). Later sections on feedback controller design, advanced control and whole-plant control have not been supplied. This is the complete available-source batch, not a complete course.']
# Keep portable index self-contained: external production-record relative links are omitted.
read_index='\n'.join(index)+'\n';pair(Path('README.md'),read_index.replace('The full visual scan and supplementary-source record are in [the production record](<../../other/work/progress/PDC-chapters1-2.md>). ','The full visual scan and supplementary sources are recorded with the repository production files. '))
for p in (READ/'figs').glob('PDC-*.png'):
 target=EXPORT/'figs'/p.name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,target)
 assert hashlib.sha256(target.read_bytes()).digest()==hashlib.sha256(p.read_bytes()).digest()
def validate(base):
 count=0;images=set()
 for p in base.rglob('*.md'):
  content=p.read_text(encoding='utf-8');assert '[[' not in content,p
  if p.name.startswith('PDC-'):
   assert all('## '+h in content for h in ['Overview','Intuition','Derivation','Motivation and explanation','Link to other topics','Conclusion']),p
   assert not re.search(r'\b(lecture|lecturer|handout|PDF|slide)\b',content,re.I),p
  link_content=MATH.sub('',content) if base==EXPORT or 'Vault' in str(base) else re.sub(r'```math[\s\S]*?```', '',content)
  for m in re.finditer(r'(!?)\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))\)',link_content):
   target=m[2] or m[3]
   if urlsplit(target).scheme or target.startswith('#'):continue
   dest=(p.parent/unquote(target.split('#',1)[0])).resolve();assert dest.exists(),(p,target);count+=1
   if m[1]:images.add(dest)
 for p in images:
  pix=pymupdf.Pixmap(str(p));assert pix.width>0 and pix.height>0
 return {'markdown_files':len(list(base.rglob('*.md'))),'links':count,'figures':len(images)}
result={'reading':validate(READ),'obsidian':validate(EXPORT),'equations':len(tags),'manifest':manifest}
with tempfile.TemporaryDirectory(prefix='pdc-portable-') as tmp:
 relocated=Path(tmp)/'Vault/Courses'/SUBJECT;shutil.copytree(EXPORT,relocated)
 assert validate(relocated)==result['obsidian']
result['portable_relocation_pass']=True
(WORK/'scratch/pdc/publish-validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='manifest'},indent=2))
