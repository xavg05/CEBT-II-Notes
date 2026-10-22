"""Publish separately authored SEP notes in source order, with continuous labels.

Canonical drafts retain local labels and transcription traceability. No merges.
"""
from pathlib import Path
from urllib.parse import unquote,urlsplit
import re,json,hashlib,shutil,tempfile
from PIL import Image

ROOT=Path(__file__).resolve().parents[3]
from check_inline_math import check_files
check_files(p for base in [ROOT/'other/work/drafts', ROOT/'other/work/archive/reviewed-units'] for p in base.rglob('*.md'))
WORK=ROOT/'other/work';SCRATCH=WORK/'scratch/separations'
DRAFT=WORK/'drafts/Separations II';READ=ROOT/'notes/Separations II'
EXPORT=ROOT/'other/obsidian/CEBT-II Notes/Separations II'
TITLES={1:'Introduction and absorption',2:'Drying of solids',3:'Membrane separations',4:'Adsorption and chromatography'}
MATH=re.compile(r'(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$')
FIGREF=re.compile(r'!\[([^\]]*)\]\(\.\./figs/([^\)]+)\)')
def github(text):
    def convert(m):
        if m[1] is None:return '$`'+m[2]+'`$'
        formula=m[1].strip();tags=re.findall(r'\\tag\{(\d+)\}',formula)
        assert len(tags)<=1
        label='\n**Equation ('+tags[0]+')**\n' if tags else ''
        return label+'\n```math\n'+re.sub(r'\\tag\{\d+\}','',formula).strip()+'\n```\n'
    return MATH.sub(convert,text)
def folder(u):return f'{u:02d} - {TITLES[u]}'
def write_pair(rel,text):
    for base,native in [(READ,False),(EXPORT,True)]:
        p=base/rel;p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(text if native else github(text),encoding='utf-8', newline='\n')
    files.append({'path':str((READ/rel).relative_to(ROOT)).replace('\\','/'),'obsidian':str((EXPORT/rel).relative_to(ROOT)).replace('\\','/')})

notes=[];files=[];figure_map={};equation=0
for u in TITLES:
    drafts=sorted((DRAFT/f'U{u}').glob('U*-*.md'))
    assert drafts,f'No drafts for U{u}'
    for p in drafts:
        text=p.read_text(encoding='utf-8');title=text.splitlines()[0].removeprefix('# ').strip()
        title=re.sub(r'^(?:U\d+-\d+|SEP-\d+)\s*[:—-]\s*','',title)
        n=len(notes)+1;filename=f'SEP-{n:02d} - {title}.md'
        assert not any(c in filename for c in '<>:"/\\|?*'),filename
        local=list(map(int,re.findall(r'\\tag\{(\d+)\}',text)))
        assert local==sorted(set(local)),(p,local)
        mapping={k:equation+i+1 for i,k in enumerate(local)}
        text=re.sub(r'\\tag\{(\d+)\}',lambda m:'\\tag{'+str(mapping[int(m[1])])+'}',text)
        # References to labels remain prose and retain original local meaning.
        def ref(m):
            key=int(m[2]);assert key in mapping,(p,m[0])
            return m[1]+' ('+str(mapping[key])+')'
        text=re.sub(r'\b([Ee]quation|[Ee]q\.)\s*\((\d+)\)',ref,text)
        equation+=len(local)
        text=re.sub(r'^# .+$',f'# SEP-{n:02d}: {title}',text,count=1,flags=re.M)
        def figure(m):
            old=m[2]
            if old not in figure_map:
                desc=re.sub(r'^u\d+-(?:\d+-)?','',old,flags=re.I)
                figure_map[old]=f'SEP-{n:02d}-{desc}'
            return '!['+m[1]+'](../figs/'+figure_map[old]+')'
        text=FIGREF.sub(figure,text)
        notes.append({'number':n,'unit':u,'title':title,'filename':filename,'draft':str(p.relative_to(ROOT)).replace('\\','/'),'text':text})

reviewed=all((SCRATCH/f'U{u}/review-passed').exists() for u in TITLES)
status='Author verification and independent cross-review are complete.' if reviewed else 'Author verification is complete; independent cross-review is in progress.'
for i,item in enumerate(notes):
    u=item['unit'];nav='[Subject index](../README.md) · [Topic overview](README.md)'
    def target(other):return other['filename'] if other['unit']==u else '../'+folder(other['unit'])+'/'+other['filename']
    if i:nav='[Previous](<'+target(notes[i-1])+'>) · '+nav
    if i+1<len(notes):nav+=' · [Next](<'+target(notes[i+1])+'>)'
    write_pair(Path(folder(u))/item['filename'],nav+'\n\n<!-- note-content:start -->\n'+item['text'].rstrip()+'\n<!-- note-content:end -->\n\n'+nav+'\n')

index=['# Separations II','',f'These {len(notes)} short notes cover the four supplied filled handouts: absorption, drying, membranes, and adsorption including chromatography. Read in order, keeping the shared `figs/` folder with the topics.','',status,'','Short notes remain separate; complete-section versions await your chosen merge groups.','', '## Topics','']
for u,title in TITLES.items():
    group=[x for x in notes if x['unit']==u]
    overview=[f'# {u:02d}. {title}','','[Subject index](../README.md)','',status,'','## Short notes','']
    overview += [f'- [SEP-{x["number"]:02d}: {x["title"]}](<{x["filename"]}>)' for x in group]
    if u>1:overview+=['',f'[Previous topic](<../{folder(u-1)}/README.md>)']
    if u<4:overview+=['',f'[Next topic](<../{folder(u+1)}/README.md>)']
    write_pair(Path(folder(u))/'README.md','\n'.join(overview)+'\n')
    index.append(f'- [{u:02d}. {title}](<{folder(u)}/README.md>) — SEP-{group[0]["number"]:02d}–{group[-1]["number"]:02d}')
index+=['','## Scope and conventions','','The supplied set contains 141 PDF pages, including handwritten explanations and completed equations. Original scans, page coverage, source corrections, external references and verification are recorded in the production work files. Coverage of these handouts does not establish that additional problem sheets or other course material have been supplied.','',f'Equation labels run continuously from 1 to {equation}. Estimates from graphs remain approximate; assumptions distinguish simplified calculations from more detailed models.']
write_pair(Path('README.md'),'\n'.join(index)+'\n')

cache=SCRATCH/'figures';cache.mkdir(exist_ok=True)
for old,new in figure_map.items():
    source=READ/'figs'/old
    if source.exists():shutil.copy2(source,cache/old)
    source=cache/old;assert source.exists(),old
    for dest in [READ/'figs'/new,EXPORT/'figs'/new]:
        dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,dest)
        assert hashlib.sha256(source.read_bytes()).digest()==hashlib.sha256(dest.read_bytes()).digest()

def validate(base):
    links=0;images=set()
    for p in sorted(base.rglob('*.md')):
        s=p.read_text(encoding='utf-8')
        assert '[[' not in s,p
        if p.name.startswith('SEP-'):
            headings=['Overview','Intuition','Derivation','Motivation and explanation','Link to other topics','Conclusion']
            positions=[s.index('## '+h) for h in headings];assert positions==sorted(positions),p
            assert not re.search(r'\b(?:lecture|lecturer|handout|PDF|slide)\b',s,re.I),p
            assert not re.search(r'\b(?:TODO|TBD|unreadable|uncertain transcription)\b',s,re.I),p
        cleaned=MATH.sub('',s) if base==EXPORT or 'Vault' in str(base) else re.sub(r'```math[\s\S]*?```','',s)
        for m in re.finditer(r'(!?)\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))\)',cleaned):
            target=m[2] or m[3]
            if urlsplit(target).scheme or target.startswith('#'):continue
            dest=(p.parent/unquote(target.split('#')[0])).resolve();assert dest.exists(),(p,target)
            links+=1
            if m[1]:images.add(dest)
    for p in images:
        with Image.open(p) as im:im.load();assert im.width and im.height
    return {'files':len(list(base.rglob('*.md'))),'links':links,'used_figures':len(images)}

result={'files':files,'notes':len(notes),'equations':equation,'figures':figure_map,'reviewed':reviewed,'reading':validate(READ),'obsidian':validate(EXPORT)}
published_tags=[]
for item in notes:
    s=(EXPORT/folder(item['unit'])/item['filename']).read_text(encoding='utf-8')
    published_tags+=list(map(int,re.findall(r'\\tag\{(\d+)\}',s)))
assert published_tags==list(range(1,equation+1))
with tempfile.TemporaryDirectory(prefix='sep-portable-') as temp:
    relocated=Path(temp)/'Vault/Courses/Separations II';shutil.copytree(EXPORT,relocated)
    assert validate(relocated)==result['obsidian']
result['portable_relocation_pass']=True
for item in json.loads((SCRATCH/'source-manifest.json').read_text(encoding='utf-8')):
    assert hashlib.sha256((ROOT/item['source']).read_bytes()).hexdigest()==item['sha256']
result['source_hashes_unchanged']=True
(SCRATCH/'publish-validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8', newline='\n')
(SCRATCH/'note-manifest.json').write_text(json.dumps([{k:v for k,v in x.items() if k!='text'} for x in notes],indent=2),encoding='utf-8', newline='\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['files','figures']},indent=2))
