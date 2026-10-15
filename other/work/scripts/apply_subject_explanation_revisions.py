"""Apply reviewed per-note revisions while preserving current scientific corrections.

Native short notes, existing complete sections and canonical publisher inputs are
edited together. This deliberately does not invoke historical full-tree publishers.
Run once per subject; exact anchors and pre-write validation prevent silent drift.
"""
from pathlib import Path
import argparse, hashlib, json, re

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'other/work/scratch/all-subject-explanations'
NATIVE=ROOT/'other/obsidian/CEBT-II Notes'
READ=ROOT/'notes'
SUBJECTS={'et':('Equilibrium Thermodynamics',43),'ab':('Advanced Biotechnology',57),
          're':('Reaction Engineering II',21),'sep':('Separations II',43)}
MATH=re.compile(r'(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$')
pending={}; originals={}; records=[]

def read(p):
    if p not in originals: originals[p]=p.read_text(encoding='utf-8')
    return pending.get(p,originals[p])

def compatible(s):
    return re.sub(r'\\operatorname\{(Cov|Var|Re)\}',r'\\mathrm{\1}',s).replace('i<j',r'i\lt j')

def github(s):
    def render(m):
        if m[1] is None:return '$`'+compatible(m[2])+'`$'
        f=compatible(m[1].strip());tags=re.findall(r'\\tag\{(\d+)\}',f)
        assert len(tags)<=1
        label='\n**Equation ('+tags[0]+')**\n' if tags else ''
        return label+'\n```math\n'+re.sub(r'\\tag\{\d+\}','',f).strip()+'\n```\n'
    return MATH.sub(render,s)

def tags(s):return re.findall(r'\\tag\{(\d+)\}',s)

def edit(text,edits,p,heading_shift=False):
    for e in edits:
        old,new=e['old'],e['new']
        if text.count(old)!=1 and heading_shift:
            def promote(t):return re.sub(r'^(#{1,5}) ',lambda m:'#'+m[1]+' ',t,flags=re.M)
            old,new=promote(old),promote(new)
        assert text.count(old)==1,(str(p),old[:200],text.count(old))
        text=text.replace(old,new,1)
    return text

def section_edit(p,number,edits):
    text=read(p)
    sections=list(re.finditer(r'^## Section (\d+): .*$',text,re.M))
    idx,= [i for i,m in enumerate(sections) if int(m[1])==number]
    start=sections[idx].start();end=sections[idx+1].start() if idx+1<len(sections) else len(text)
    original=text[start:end]
    revised=edit(original,edits,p,heading_shift=True)
    pending[p]=text[:start]+revised+text[end:]

def main():
    args=argparse.ArgumentParser()
    args.add_argument('--subjects',nargs='+',choices=list(SUBJECTS),default=list(SUBJECTS))
    selected=args.parse_args().subjects
    for ident in selected:
        subject,count=SUBJECTS[ident]
        stamp=OUT/f'{ident}-applied.json'
        assert not stamp.exists(),f'{ident} already applied; edit current text directly for follow-up fixes'
        proposal=json.loads((OUT/f'{ident}-proposals.json').read_text(encoding='utf-8'))
        assert len(proposal)==count and len({x['path'] for x in proposal})==count
        actual={p.relative_to(ROOT).as_posix() for p in (NATIVE/subject).rglob('*.md')
                if re.match(r'(ET|AB|RE|SEP)-',p.name)}
        assert {x['path'] for x in proposal}==actual,(ident,'Incomplete short-note coverage')
        for item in proposal:
            p=ROOT/item['path'];original=read(p)
            revised=edit(original,item['edits'],p)
            assert tags(original)==tags(revised),(p,'Numbered equations changed')
            pending[p]=revised
            if ident in ('et','ab'):
                complete=p.parent/'Complete section.md'
                number=int(re.search(r'(?:ET|AB)-(\d+)',p.name)[1])
                section_edit(complete,number,item['edits'])
                topic=p.parent.name[:2]
                archive,=(ROOT/'other/work/archive/reviewed-units'/subject).glob(topic+' - *.md')
                section_edit(archive,number,item['edits'])
            else:
                if ident=='re':
                    draft,=(ROOT/'other/work/drafts'/subject).glob(p.name)
                else:
                    n=int(re.search(r'SEP-(\d+)',p.name)[1])
                    unit=1 if n<=11 else 2 if n<=22 else 3 if n<=34 else 4
                    local=n-(0 if unit==1 else 11 if unit==2 else 22 if unit==3 else 34)
                    draft,=(ROOT/'other/work/drafts'/subject/f'U{unit}').glob(f'U{unit}-{local:02d} - *.md')
                pending[draft]=edit(read(draft),item['edits'],draft)
            records.append({'note':item['note'],'path':item['path'],'gap':item['gap'],'edits':len(item['edits'])})
    # Publish only modified native files. Preserve their existing navigation and grouping.
    for p,text in list(pending.items()):
        if p.is_relative_to(NATIVE):
            target=READ/p.relative_to(NATIVE)
            read(target)
            pending[target]=github(text)
    for p,text in pending.items():
        assert '\ufffd' not in text,(p,'Invalid text encoding')
        if not p.is_relative_to(READ):assert tags(originals[p])==tags(text),(p,'Tag preservation')
        assert text.count('<!-- note-content:start -->')==originals[p].count('<!-- note-content:start -->'),p
    # Snapshot uncommitted source corrections before changing any study file.
    snapshot=OUT/'before-revision'
    snapshot.mkdir(parents=True,exist_ok=True)
    snapshot_manifest={}
    for p,text in originals.items():
        relative=p.relative_to(ROOT).as_posix()
        saved=snapshot/(hashlib.sha256(relative.encode('utf-8')).hexdigest()[:20]+'.md')
        snapshot_manifest[relative]=saved.name
        if not saved.exists():
            saved.parent.mkdir(parents=True,exist_ok=True);saved.write_text(text,encoding='utf-8')
    prior=snapshot/'manifest.json'
    manifest=json.loads(prior.read_text(encoding='utf-8')) if prior.exists() else {}
    manifest.update(snapshot_manifest)
    prior.write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding='utf-8')
    for p,text in pending.items():p.write_text(text,encoding='utf-8')
    for ident in selected:
        subject,_=SUBJECTS[ident]
        changed=[{'path':p.relative_to(ROOT).as_posix(),
                  'before':hashlib.sha256(originals[p].encode('utf-8')).hexdigest(),
                  'after':hashlib.sha256(t.encode('utf-8')).hexdigest()}
                 for p,t in pending.items() if subject in p.parts]
        (OUT/f'{ident}-applied.json').write_text(json.dumps({'subject':subject,'notes':[r for r in records if r['path'].startswith((NATIVE/subject).relative_to(ROOT).as_posix())],'files':changed},indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps({'subjects':selected,'short_notes':len(records),'files_updated':len(pending)},indent=2))

if __name__=='__main__':main()
