"""Build the subject/topic reading tree and its portable Obsidian counterpart.

Inputs are reviewed native Markdown units in other/work/archive/reviewed-units/.
This publisher does not renumber equations or alter scientific explanations.
"""
from pathlib import Path
import hashlib,json,re,shutil,zipfile,tempfile
from urllib.parse import unquote,urlsplit
import pymupdf

ROOT=Path(__file__).resolve().parents[3]
from check_inline_math import check_files
check_files(p for base in [ROOT/'other/work/drafts', ROOT/'other/work/archive/reviewed-units'] for p in base.rglob('*.md'))
WORK=ROOT/'other/work'
READ=ROOT/'notes'
EXPORT=ROOT/'other/obsidian/CEBT-II Notes'
MATH=re.compile(r'(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$')
SUBJECTS=[('Equilibrium Thermodynamics','ET',12,43),('Advanced Biotechnology','AB',17,57)]
manifest={'subjects':[],'files':[],'figures':{}}

def compatible(s):
    return re.sub(r'\\operatorname\{(Cov|Var|Re)\}',r'\\mathrm{\1}',s).replace('i<j',r'i\lt j')
def github(s):
    def render(m):
        if m[1] is not None:
            expression=compatible(m[1].strip())
            labels=re.findall(r'\\tag\{(\d+)\}',expression)
            assert len(labels)<=1
            label='\n**Equation ('+labels[0]+')**\n' if labels else ''
            expression=re.sub(r'\\tag\{\d+\}','',expression).strip()
            return label+'\n```math\n'+expression+'\n```\n'
        return '$`'+compatible(m[2])+'`$'
    return MATH.sub(render,s)
def safe(s):
    return re.sub(r'\s+',' ',re.sub(r'[<>:"/\\|?*]',' - ',s)).strip(' .')
def expressions(s):return [(m[1] if m[1] is not None else m[2]).strip() for m in MATH.finditer(s)]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def demote_body(s):
    # Small notes have one H1; retain the unit conclusion as H2 in its final note.
    return re.sub(r'^(#{3,6}) ',lambda m:m[1][1:]+' ',s,flags=re.M)
def marker(content):return '<!-- note-content:start -->\n'+content.rstrip()+'\n<!-- note-content:end -->\n'
def write_pair(rel,content):
    for parent,native in [(READ,False),(EXPORT,True)]:
        p=parent/rel;p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(content if native else github(content), encoding='utf-8', newline='\n')
    ex=expressions(content)
    cost=sum(x.count('{')+1 for x in ex)
    assert cost<2000,(rel,cost)
    manifest['files'].append({'path':str((READ/rel).relative_to(ROOT)),'obsidian':str((EXPORT/rel).relative_to(ROOT)),'expressions':len(ex),'math_cost':cost})

for name,prefix,unit_count,small_count in SUBJECTS:
    base=WORK/'archive/reviewed-units'/name
    units=sorted(base.glob('[0-9][0-9] - *.md'))
    assert len(units)==unit_count,(name,len(units))
    index=[f'# {name}\n\n[All subjects](../README.md)\n\nRead the numbered topics in order. Each topic has an overview, its small notes and a complete-section version. Figures are shared in this subject’s `figs/` folder. Equation numbers continue through the subject.\n']
    if prefix=='AB':index.append('Gene regulation is externally supplemented; synthetic condensates is the optional final topic.\n')
    entries=[];numbers=[];tags=[];used_images=set()
    for i,p in enumerate(units):
        native=p.read_text(encoding='utf-8');title=native.splitlines()[0][2:]
        folder=f'{i+1:02d} - {safe(title)}'
        source=native.split('\n',1)[1].strip()
        source=re.sub(r'\]\(figs/','](../figs/',source)
        matches=list(re.finditer(r'^## Section (\d+): (.+)$',source,re.M))
        assert matches,p
        overview=source[:matches[0].start()].strip()
        small=[]
        for j,m in enumerate(matches):
            number=int(m[1]);numbers.append(number)
            body=source[m.end():matches[j+1].start() if j+1<len(matches) else len(source)].strip()
            content=f'# Section {number:02d}: {m[2]}\n\n'+demote_body(body)+'\n'
            filename=f'{prefix}-{number:02d} - {safe(m[2])}.md'
            small.append((number,filename,content))
            # Every paragraph and equation is retained, changing only heading depth.
            canonical=source[m.start():matches[j+1].start() if j+1<len(matches) else len(source)].strip()
            def no_headings(s):return re.sub(r'^#{1,6} ', '',s,flags=re.M).strip()
            assert no_headings(content)==no_headings(canonical),(p,number)
        topic_rel=Path(name)/folder
        nav='[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)'
        for j,(number,filename,content) in enumerate(small):
            links=[nav]
            if j:links.insert(0,f'[Previous](<{small[j-1][1]}>)')
            if j+1<len(small):links.append(f'[Next](<{small[j+1][1]}>)')
            navigation=' · '.join(links)
            write_pair(topic_rel/filename,navigation+'\n\n'+marker(content)+'\n'+navigation+'\n')
        complete=f'# {title}\n\n{source}\n'
        assert expressions(complete)==expressions(native),(p,'math preservation')
        write_pair(topic_rel/'Complete section.md',nav+'\n\n'+marker(complete)+'\n'+nav+'\n')
        topic=[f'# {i+1:02d}. {title}\n\n[Subject index](../README.md) · [Complete section](<Complete section.md>)\n',overview,'','## Small notes','']
        topic.extend(f'- [{prefix}-{n:02d}: {content.splitlines()[0].split(": ",1)[1]}](<{filename}>)' for n,filename,content in small)
        if i:topic.extend(['',f'[Previous topic](<../{i:02d} - {safe(units[i-1].read_text(encoding="utf-8").splitlines()[0][2:])}/README.md>)'])
        if i+1<len(units):topic.extend(['',f'[Next topic](<../{i+2:02d} - {safe(units[i+1].read_text(encoding="utf-8").splitlines()[0][2:])}/README.md>)'])
        write_pair(topic_rel/'README.md','\n'.join(topic)+'\n')
        index.append(f'- [{i+1:02d}. {title}](<{folder}/README.md>) — {prefix}-{small[0][0]:02d}–{prefix}-{small[-1][0]:02d}')
        entries.append({'number':i+1,'title':title,'folder':folder,'canonical':str(p.relative_to(ROOT)),'notes':[filename for n,filename,content in small],'note_numbers':[n for n,filename,content in small]})
        tags.extend(int(x) for x in re.findall(r'\\tag\{(\d+)\}',native))
        for image in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',native):
            assert image.startswith('figs/') and '..' not in image,image
            old=base/image
            for dest in [READ/name/image,EXPORT/name/image]:
                dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(old,dest)
                assert digest(old)==digest(dest)
            manifest['figures'][str((READ/name/image).relative_to(ROOT))]=digest(old)
            used_images.add(image)
    assert numbers==list(range(1,small_count+1)),(name,numbers)
    assert tags==sorted(set(tags)),name  # Removed examples may leave gaps in preserved labels.
    write_pair(Path(name)/'README.md','\n'.join(index)+'\n')
    manifest['subjects'].append({'name':name,'prefix':prefix,'sections':entries,'small_notes':small_count,'equations':len(tags),'figures':len(used_images)})

root_index='# CEBT-II Notes\n\n- [Equilibrium Thermodynamics](<Equilibrium Thermodynamics/README.md>) — 12 topics, 43 small notes.\n- [Advanced Biotechnology](<Advanced Biotechnology/README.md>) — 17 topics, 57 small notes.\n\nStart with a subject, then its numbered topics. Use the topic’s small notes for step-by-step reading or its complete-section version for everything together.\n'
(READ/'README.md').write_text(root_index+'\n[Obsidian copy](../other/obsidian/README.md) · [Plan](../PLAN.md) · [Review records](../other/work/FINAL-DELIVERY.md)\n', encoding='utf-8', newline='\n')
(EXPORT/'README.md').write_text(root_index+'\nCopy this entire `CEBT-II Notes` folder into your vault. Keep each subject’s topic folders and shared `figs/` together. No plugin or importer is needed.\n', encoding='utf-8', newline='\n')
(EXPORT.parent/'README.md').write_text('# Obsidian edition\n\n[Open the notes](<CEBT-II Notes/README.md>). Copy the whole `CEBT-II Notes` folder into your vault, or copy one subject folder with all its topic folders and `figs/`.\n\nThis mirrors the main notes layout and uses standard inline/display math. The local ZIP `CEBT-II-Obsidian.zip` is generated from this folder.\n\n[Repository home](../../README.md) · [Main notes](../../notes/README.md)\n', encoding='utf-8', newline='\n')

def validate(folder):
    links=0;images=set()
    for p in folder.rglob('*.md'):
        for m in re.finditer(r'(!?)\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))\)',p.read_text(encoding='utf-8')):
            target=m[2] or m[3]
            if urlsplit(target).scheme or target.startswith('#'):continue
            dest=(p.parent/unquote(target.split('#',1)[0])).resolve();assert dest.exists(),(p,target)
            links+=1
            if m[1]:images.add(dest)
    for p in images:
        pix=pymupdf.Pixmap(str(p));assert pix.width and pix.height
    return {'markdown_files':len(list(folder.rglob('*.md'))),'links':links,'figures':len(images)}
results={'reading':validate(READ),'obsidian':validate(EXPORT),'subjects':[{k:v for k,v in sub.items() if k!='sections'} for sub in manifest['subjects']]}
archive=EXPORT.parent/'CEBT-II-Obsidian.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(EXPORT.rglob('*')):
        if p.is_file():z.write(p,p.relative_to(EXPORT.parent))
with tempfile.TemporaryDirectory(prefix='cebt-new-layout-') as temp:
    dest=Path(temp)/'Vault'/'Courses';dest.mkdir(parents=True)
    with zipfile.ZipFile(archive) as z:assert z.testzip() is None;z.extractall(dest)
    assert validate(dest/'CEBT-II Notes')==results['obsidian']
results['zip_relocation_pass']=True
results['archive_sha256']=digest(archive)
results['max_page_math_cost']=max(x['math_cost'] for x in manifest['files'])
(WORK/'LAYOUT-MANIFEST.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n', encoding='utf-8', newline='\n')
(WORK/'LAYOUT-VALIDATION.json').write_text(json.dumps(results,indent=2)+'\n', encoding='utf-8', newline='\n')
print(json.dumps(results,indent=2))
