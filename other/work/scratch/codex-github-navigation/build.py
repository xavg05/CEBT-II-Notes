"""Publish existing approved unit merges; preserve original production snapshots."""
from pathlib import Path
import hashlib,json,re,shutil,subprocess
from final_support import reviewed,protect_labels,restore_labels,figure_source,relocated_source,corrections

ROOT=Path(__file__).resolve().parents[4]
WORK=Path(__file__).parent
MATH=re.compile(r'(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$')
SUBJECTS=[('Equilibrium Thermodynamics','equilibrium-thermodynamics','ET'),('Advanced Biotechnology','advanced-biotechnology','AB')]
MAX_COST=600
MAX_CHARS=16000
old_manifest=json.loads((WORK/'manifest.json').read_text()) if (WORK/'manifest.json').exists() else {'subjects':[]}
old_pages={page['path'] for subject in old_manifest['subjects'] for page in subject['pages']}

def maths(s):return [(m.group(1) if m.group(1) is not None else m.group(2),m.group(1) is not None) for m in MATH.finditer(s)]
def cost(s):return sum(x.count('{')+1 for x,display in maths(s))
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def slug(s):return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
def demote(s):return re.sub(r'^(#{1,5}) ',lambda m:'#'+m[1]+' ',s,flags=re.M)
def bare_formula(s):return re.sub(r'\\tag\{\d+\}','',s)

def github(s):
    def replace(m):
        def compatible(value):return re.sub(r'\\operatorname\{(Cov|Var|Re)\}',r'\\mathrm{\1}',value).replace('i<j',r'i\lt j')
        if m.group(1) is not None:
            expression=compatible(m.group(1).strip())
            tags=re.findall(r'\\tag\{(\d+)\}',expression)
            assert len(tags)<=1
            label='\n**Equation ('+tags[0]+')**\n' if tags else ''
            expression=re.sub(r'\\tag\{\d+\}','',expression).strip()
            return label+'\n```math\n'+expression+'\n```\n'
        assert '`' not in m.group(2),m.group(2)
        return '$`'+compatible(m.group(2))+'`$'
    return MATH.sub(replace,s)

def partition(body):
    blocks=body.split('\n\n');chunks=[];current=[]
    for block in blocks:
        proposed='\n\n'.join(current+[block])
        boundary=block.startswith('## Section ') and len('\n\n'.join(current))>7000
        if current and (cost(proposed)>MAX_COST or len(proposed)>MAX_CHARS or boundary):
            chunks.append('\n\n'.join(current));current=[]
        assert cost(block)<=MAX_COST and len(block)<=MAX_CHARS,('Oversized indivisible paragraph',block[:100])
        current.append(block)
    if current:chunks.append('\n\n'.join(current))
    if len(chunks)>1 and len(chunks[-1])<1600:
        combined=chunks[-2]+'\n\n'+chunks[-1]
        if len(combined)<=MAX_CHARS and cost(combined)<=MAX_COST:chunks[-2:]=[combined]
    assert '\n\n'.join(chunks)==body
    return chunks

manifest={'subjects':[],'originals':{},'references':[],'figures':{},'limits':{'math_cost':MAX_COST,'body_characters':MAX_CHARS}}
protected=[Path(p) for p in subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().split('\0') if p and (p.startswith(('sources/','out/ET/','out/AB/','out/merged/')) or p in ['CLAUDE.md','AGENTS.md','out/PLAN.md'])]
protected=[relocated_source(ROOT/p).relative_to(ROOT) for p in protected]
manifest['originals']={str(p):digest(ROOT/p) for p in protected}
manifest['review_corrections']=corrections()

for name,folder,prefix in SUBJECTS:
    files=sorted((ROOT/'out/merged').glob(name+' *.md'))
    assert len(files)==(12 if prefix=='ET' else 17)
    dest=ROOT/'notes'/folder;(dest/'figs').mkdir(parents=True,exist_ok=True)
    source=[reviewed(p) for p in files]
    normalised=json.loads(subprocess.check_output(['node',str(WORK/'normalise.mjs')],input=json.dumps(source).encode(),cwd=ROOT))
    offsets=[];counter=0;sections={}
    for i,s in enumerate(source):
        tags=[int(n) for n in re.findall(r'\\tag\{(\d+)\}',s)]
        assert tags==list(range(1,len(tags)+1)),(files[i],tags)
        offsets.append(counter);counter+=len(tags)
        for sec in re.findall(r'^## Section (\d+):',s,re.M):sections[int(sec)]=i
    units=[];pages=[];full=[f'# {name} — complete Obsidian edition\n\nAll teaching units in order. Equation numbers run continuously through this subject. For GitHub, use the [linked reading sections](README.md).\n']
    for i,(p,original,s) in enumerate(zip(files,source,normalised)):
        title=s.splitlines()[0][2:];unit_number=i+1;offset=offsets[i]
        s,protected_labels=protect_labels(s)
        saved={}
        def cross(m):
            sec=int(m.group('sec'));n=int(m.group('eq'));target=sections[sec]
            assert 1<=n<=len(re.findall(r'\\tag\{(\d+)\}',source[target])),(p,sec,n)
            val=m.group('lead')+str(offsets[target]+n)+m.group('end')
            key=f'CROSSREFERENCEPLACEHOLDER{len(saved)}END';saved[key]=val;return key
        for pattern in [r'(?P<lead>Section (?P<sec>\d+),? (?:equation|eq\.) ?\(?)(?P<eq>\d+)(?P<end>\)?)',r'(?P<lead>(?:[Ee]quation )?\()(?P<eq>\d+)(?P<end>\) of Section (?P<sec>\d+))']:
            s=re.sub(pattern,cross,s)
        segments=[];cursor=0
        tags_count=len(re.findall(r'\\tag\{(\d+)\}',original))
        def renumber_prose(prose):
            def change(m):
                n=int(m[1])
                if 1<=n<=tags_count:
                    manifest['references'].append({'source':str(p.relative_to(ROOT)),'old':n,'new':offset+n,'context':prose[max(0,m.start()-75):m.end()+75]})
                    return '('+str(offset+n)+')'
                return m[0]
            return re.sub(r'\((\d+)\)',change,prose)
        for match in MATH.finditer(s):
            segments.append(renumber_prose(s[cursor:match.start()]))
            segments.append(re.sub(r'\\tag\{(\d+)\}',lambda m:r'\tag{'+str(offset+int(m[1]))+'}',match[0]));cursor=match.end()
        segments.append(renumber_prose(s[cursor:]));s=''.join(segments)
        for key,value in saved.items():s=s.replace(key,value)
        s=restore_labels(s,protected_labels)
        assert [bare_formula(x) for x,d in maths(original)]==[bare_formula(x) for x,d in maths(s)]
        assert [d for x,d in maths(original)]==[d for x,d in maths(s)]
        body=s.split('\n',1)[1].strip()
        for ref in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',s):
            ref=ref.strip('<>');a=figure_source(p.parent/ref);b=dest/ref
            assert a.is_file(),a
            b.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(a,b)
            assert digest(a)==digest(b)
            manifest['figures'][str(b.relative_to(ROOT))]=digest(a)
        chunks=partition(body);unit_pages=[]
        file_title=p.stem.split(' - ',1)[1]
        for j,chunk in enumerate(chunks):
            filename=f'{unit_number:02d}-{j+1:02d}-{slug(file_title)}.md'
            page={'path':str((dest/filename).relative_to(ROOT)),'unit':unit_number,'part':j+1,'title':title,'chunk':chunk,'cost':cost(chunk)-len(re.findall(r'\\tag\{(\d+)\}',chunk)),'expressions':len(maths(chunk)),'tags':[int(n) for n in re.findall(r'\\tag\{(\d+)\}',chunk)]}
            unit_pages.append(page);pages.append(page)
        full.append(f'## {unit_number:02d}. {title}\n\n'+demote(body)+'\n')
        units.append({'source':str(p.relative_to(ROOT)),'title':title,'number':unit_number,'pages':unit_pages,'tags':[int(n) for n in re.findall(r'\\tag\{(\d+)\}',s)]})
    for k,page in enumerate(pages):
        links=['[Subject index](README.md)']
        if k:links.insert(0,f'[Previous]({Path(pages[k-1]["path"]).name})')
        if k+1<len(pages):links.append(f'[Next]({Path(pages[k+1]["path"]).name})')
        nav=' · '.join(links)
        text=f'# {page["title"]} — reading {page["unit"]:02d}.{page["part"]}\n\n{nav}\n\n<!-- reading-content:start -->\n'+github(page['chunk'])+'\n<!-- reading-content:end -->\n\n'+nav+'\n'
        (ROOT/page['path']).write_text(text)
    complete='\n'.join(full)
    assert [int(n) for n in re.findall(r'\\tag\{(\d+)\}',complete)]==list(range(1,counter+1))
    (dest/'complete-obsidian.md').write_text(complete)
    for unit in units:
        reconstructed='\n\n'.join(page['chunk'] for page in unit['pages'])
        assert len(maths(reconstructed))==sum(page['expressions'] for page in unit['pages'])
    status=('All 12 units have completed final content review, numerical checks and correction integration. See the [final delivery record](../../out/work/FINAL-DELIVERY.md) for scope and evidence.' if prefix=='ET' else 'All 17 units have completed content review and correction integration. **Unit 15 is externally supplemented** because the original course material was thin. Unit 17 is optional; preliminary research remains identified in its text. See the [final delivery record](../../out/work/FINAL-DELIVERY.md) for scope and evidence.')
    readme=[f'# {name}\n\n[All subjects](../README.md) · [Repository home](../../README.md)\n\n{status}\n\n## Read on GitHub\n\nFollow the sections in order. Each page uses protected inline LaTeX and fenced math blocks, with a conservative per-page math budget. Equation numbers appear immediately above the formulas, continue across pages and match the complete edition.\n']
    for unit in units:
        readme.append(f'### Unit {unit["number"]:02d}: {unit["title"]}\n')
        for page in unit['pages']:
            headings=re.findall(r'^## (.+)$',page['chunk'],re.M)
            caption='; '.join(headings) if headings else 'Continuation of derivation and examples'
            if page['tags']:caption+=f' — equations {page["tags"][0]}–{page["tags"][-1]}'
            readme.append(f'- [{unit["number"]:02d}.{page["part"]}: {caption}]({Path(page["path"]).name})')
        readme.append('')
    readme.extend(['## Complete single-file edition for Obsidian','','[Download/read the complete Obsidian edition](complete-obsidian.md). It contains the whole subject, including every derivation, example and figure reference, using standard `$...$` and `$$...$$` delimiters. Copy this file together with this subject’s `figs/` folder into your vault. **The full file exceeds GitHub’s cumulative math budget; use the reading sections above for browser reading.**','','Production and review records are retained in [out/](../../out/). Original individual notes, source PDFs and archived unit merges are preserved.'])
    (dest/'README.md').write_text('\n'.join(readme)+'\n')
    manifest['subjects'].append({'name':name,'folder':folder,'prefix':prefix,'equations':counter,'expressions':len(maths(complete)),'units':[{**unit,'pages':[p['path'] for p in unit['pages']]} for unit in units],'pages':[{k:v for k,v in page.items() if k!='chunk'} for page in pages]})
(ROOT/'notes/README.md').write_text('# Notes\n\n[Repository home](../README.md)\n\n- [Equilibrium Thermodynamics](equilibrium-thermodynamics/README.md) — 12 reviewed teaching units.\n- [Advanced Biotechnology](advanced-biotechnology/README.md) — 17 reviewed teaching units, including optional condensates.\n- [Copy-ready Obsidian folders](../out/obsidian/README.md).\n\nEach subject has linked GitHub reading sections, its own figures, and a complete single-file Obsidian edition. Preparation and review records live in [out/](../out/). Reaction Engineering II and Process Dynamics and Control source PDFs are now available; their production planning has not yet been done.\n')
for path,sha in manifest['originals'].items():assert digest(ROOT/path)==sha,path
current_pages={page['path'] for subject in manifest['subjects'] for page in subject['pages']}
for stale in old_pages-current_pages:(ROOT/stale).unlink()
(WORK/'manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'subjects':[{'name':s['name'],'pages':len(s['pages']),'equations':s['equations'],'expressions':s['expressions'],'max_cost':max(p['cost'] for p in s['pages'])} for s in manifest['subjects']],'preserved_original_files':len(manifest['originals']),'copied_figures':len(manifest['figures'])},indent=2))
