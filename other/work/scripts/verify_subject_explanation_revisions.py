"""Preservation, canonical synchronisation, links and portable-export checks."""
from pathlib import Path
from urllib.parse import unquote,urlsplit
from collections import Counter
import hashlib,json,re,shutil,tempfile
from PIL import Image

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'other/work/scratch/all-subject-explanations'
NATIVE=ROOT/'other/obsidian/CEBT-II Notes'
READ=ROOT/'notes'
baseline=json.loads((OUT/'baseline.json').read_text(encoding='utf-8'))
snapshots=json.loads((OUT/'before-revision/manifest.json').read_text(encoding='utf-8'))
changes=[r for ident in ['et','ab','re','sep'] for r in json.loads((OUT/f'{ident}-applied.json').read_text(encoding='utf-8'))['notes']]
assert len(changes)==164
MATH=re.compile(r'(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$')
def text(p):return p.read_text(encoding='utf-8')
def body(s):return s.split('<!-- note-content:start -->',1)[1].split('<!-- note-content:end -->',1)[0].strip()
def norm(s):return re.sub(r'^#{1,6} ','',s,flags=re.M).replace('](../figs/','](figs/').strip()
def tags(s):return re.findall(r'\\tag\{(\d+)\}',s)
def section(s,number):
    found=list(re.finditer(r'^## Section (\d+): .*$',s,re.M))
    idx,=[i for i,m in enumerate(found) if int(m[1])==number]
    return s[found[idx].start():found[idx+1].start() if idx+1<len(found) else len(s)]
canonical=[]
for item in changes:
    p=ROOT/item['path'];current=text(p)
    before=text(OUT/'before-revision'/snapshots[item['path']])
    assert tags(current)==tags(before),p
    assert re.findall(r'!\[[^\]]*\]\([^)]*\)',current)==re.findall(r'!\[[^\]]*\]\([^)]*\)',before),p
    assert re.findall(r'^#{1,6} .*$',current,re.M)==re.findall(r'^#{1,6} .*$',before,re.M),p
    assert current!=before,p
    subject=p.relative_to(NATIVE).parts[0]
    if subject in ['Equilibrium Thermodynamics','Advanced Biotechnology']:
        n=int(re.search(r'(?:ET|AB)-(\d+)',p.name)[1])
        complete=text(p.parent/'Complete section.md')
        assert norm(body(current))==norm(section(body(complete),n)),(p,'Complete section divergence')
        archive,=(ROOT/'other/work/archive/reviewed-units'/subject).glob(p.parent.name[:2]+' - *.md')
        assert norm(body(current))==norm(section(text(archive),n)),(p,'Canonical section divergence')
        canonical.append(str(archive.relative_to(ROOT)))
    else:
        # Same explanation paragraphs must occur in publisher input despite local tags/titles.
        if subject=='Reaction Engineering II':draft,=(ROOT/'other/work/drafts'/subject).glob(p.name)
        else:
            n=int(re.search(r'SEP-(\d+)',p.name)[1]);u=1 if n<=11 else 2 if n<=22 else 3 if n<=34 else 4
            local=n-(0 if u==1 else 11 if u==2 else 22 if u==3 else 34)
            draft,=(ROOT/'other/work/drafts'/subject/f'U{u}').glob(f'U{u}-{local:02d} - *.md')
        proposal=next(x for x in json.loads((OUT/(('re' if subject=='Reaction Engineering II' else 'sep')+'-proposals.json')).read_text(encoding='utf-8')) if x['path']==item['path'])
        for e in proposal['edits']:assert e['new'] in text(draft),(draft,'Canonical explanation absent')
        canonical.append(str(draft.relative_to(ROOT)))
source_pdfs=[p for p in baseline if p.startswith('other/sources/') and p.endswith('.pdf')]
for name in source_pdfs:assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==baseline[name],name

def links(base):
    count=0;figures=set()
    for p in base.rglob('*.md'):
        s=text(p);assert '\ufffd' not in s,p
        s=MATH.sub('',s) if base!=READ else re.sub(r'```math[\s\S]*?```|\$`[^`]*`\$','',s)
        for m in re.finditer(r'(!?)\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))\)',s):
            target=m[2] or m[3]
            if urlsplit(target).scheme or target.startswith('#'):continue
            dest=(p.parent/unquote(target.split('#',1)[0])).resolve()
            assert dest.exists(),(p,target)
            count+=1
            if m[1]:figures.add(dest)
    for p in figures:
        with Image.open(p) as im:im.load();assert im.width and im.height
    return {'files':len(list(base.rglob('*.md'))),'links':count,'figures':len(figures)}
results={'short_notes_revised':len(changes),'per_subject':dict(Counter(x['note'].split('-')[0] for x in changes)),
         'existing_complete_sections_synchronised':29,'canonical_files_checked':len(set(canonical)),
         'source_pdfs_unchanged':len(source_pdfs),'reading':links(READ),'native':links(NATIVE)}
for p in READ.rglob('*.png'):
    q=NATIVE/p.relative_to(READ)
    assert q.exists() and p.read_bytes()==q.read_bytes(),p
with tempfile.TemporaryDirectory(prefix='ce-') as temp:
    dest=Path(temp)/'v';shutil.copytree(NATIVE,dest)
    assert links(dest)==results['native']
results['relocation_pass']=True
(OUT/'publication-validation.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
