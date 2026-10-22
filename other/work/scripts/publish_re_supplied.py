"""SUPERSEDED by publish_re_all.py (final RE-01–27 numbering); do not run.

Publish the supplied sections 3–6 using provisional section identifiers; no merges."""
from pathlib import Path
import re,json,shutil,hashlib,tempfile
from urllib.parse import unquote,urlsplit
import pymupdf

ROOT=Path(__file__).resolve().parents[3]
from check_inline_math import check_files
check_files(p for base in [ROOT/'other/work/drafts', ROOT/'other/work/archive/reviewed-units'] for p in base.rglob('*.md'))
SUBJECT='Reaction Engineering II'
DRAFT=ROOT/'other/work/drafts'/SUBJECT
READ=ROOT/'notes'/SUBJECT
NATIVE=ROOT/'other/obsidian/CEBT-II Notes'/SUBJECT
OUT=ROOT/'other/work/scratch/coverage-audit-20261014'
TOPICS=[
 ('03 - Catalyst materials and deactivation',['RE-S3-01','RE-S3-02']),
 ('04 - Catalytic reactors and nonideal flow',['RE-S3-03','RE-S3-04']),
 ('05 - Industrial catalysts and transport pathways',['RE-S3-05']),
 ('06 - Adsorption equilibria',['RE-S4-01','RE-S4-02']),
 ('07 - Porous-solid characterisation',['RE-S4-03','RE-S4-04']),
 ('08 - Surface mechanisms and apparent kinetics',['RE-S5-01','RE-S5-02']),
 ('09 - Diffusion in porous catalysts',['RE-S6-01']),
 ('10 - Isothermal diffusion and reaction',['RE-S6-02','RE-S6-03']),
 ('11 - Thermal effects in catalyst pellets',['RE-S6-04']),
]
MATH=re.compile(r'(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$')
def github(text):
    def convert(m):
        if m[1] is None:return '$`'+m[2]+'`$'
        expr=m[1].strip();tag=re.search(r'\\tag\{(\d+)\}',expr)
        label=f'\n**Equation ({tag[1]})**\n' if tag else ''
        return label+'\n```math\n'+re.sub(r'\\tag\{\d+\}','',expr).strip()+'\n```\n'
    return MATH.sub(convert,text)
entries=[];equation=20
# RE-01 source-coverage addition, retaining its existing navigation and equation labels.
first=next(DRAFT.glob('RE-01 - *.md'))
first_body=first.read_text(encoding='utf-8').rstrip()
first_folder='01 - Foundations for heterogeneous reactor modelling'
for base,native in [(READ,False),(NATIVE,True)]:
    target=base/first_folder/first.name
    previous=target.read_text(encoding='utf-8')
    before=previous.split('<!-- note-content:start -->',1)[0]
    after=previous.split('<!-- note-content:end -->',1)[1]
    target.write_text(before+'<!-- note-content:start -->\n'+(first_body if native else github(first_body))+'\n<!-- note-content:end -->'+after,encoding='utf-8')
for folder,ids in TOPICS:
    paths=[next(DRAFT.glob(i+' - *.md')) for i in ids]
    for i,p in enumerate(paths):
        body=p.read_text(encoding='utf-8')
        def number(m):
            global equation
            if m[1] is None:return m[0]
            equation+=1
            return '$$'+m[1].rstrip()+f'\n\\tag{{{equation}}}'+'$$'
        body=MATH.sub(number,body)
        nav='[Subject index](../README.md) · [Topic overview](README.md)'
        if i:nav=f'[Previous](<{paths[i-1].name}>) · '+nav
        if i+1<len(paths):nav+=f' · [Next](<{paths[i+1].name}>)'
        content=nav+'\n\n<!-- note-content:start -->\n'+body.rstrip()+'\n<!-- note-content:end -->\n\n'+nav+'\n'
        for base,native in [(READ,False),(NATIVE,True)]:
            dest=base/folder/p.name;dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_text(content if native else github(content),encoding='utf-8')
        entries.append({'id':ids[i],'draft':str(p.relative_to(ROOT)),'path':str((READ/folder/p.name).relative_to(ROOT)),'obsidian':str((NATIVE/folder/p.name).relative_to(ROOT))})
    overview='# '+folder.split(' - ',1)[1]+'\n\n[Subject index](../README.md)\n\n'
    overview+='Read the short notes in order. Section-based identifiers are provisional while the missing solid-reagent material awaits its source. The notes remain separate.\n\n'
    overview+='\n'.join(f'- [{ident}: {p.stem.split(" - ",1)[1]}](<{p.name}>)' for ident,p in zip(ids,paths))+'\n'
    for base in (READ,NATIVE):(base/folder/'README.md').write_text(overview,encoding='utf-8')

index='# Reaction Engineering II\n\nThe supplied material covers foundations and catalytic reaction engineering: sections 1 and 3–6. Section 2 (solid reagents), section 7 (gas–liquid reactors) and section 8 (fermenters) are still missing. This is therefore not the complete course.\n\n'
index+='- [01. Foundations for heterogeneous reactor modelling](<01 - Foundations for heterogeneous reactor modelling/README.md>) — RE-01–06.\n'
index+='- 02. Fluid–solid reactions with a solid reagent — awaiting source.\n'
index+='\n'.join(f'- [{folder.split(" - ",1)[0]}. {folder.split(" - ",1)[1]}](<{folder}/README.md>) — '+', '.join(ids)+'.' for folder,ids in TOPICS)+'\n\n'
index+='RE-S3, RE-S4, RE-S5 and RE-S6 identify source sections, not final chronological note numbers. Equation labels continue after RE-06. Keep the shared `figs/` folder when copying the subject.\n'
for base in (READ,NATIVE):(base/'README.md').write_text(index,encoding='utf-8')
for p in (READ/'figs').glob('RE-S*.png'):
    dest=NATIVE/'figs'/p.name;dest.parent.mkdir(exist_ok=True,parents=True);shutil.copy2(p,dest)
    assert hashlib.sha256(p.read_bytes()).digest()==hashlib.sha256(dest.read_bytes()).digest()
    pix=pymupdf.Pixmap(str(p));assert pix.width and pix.height
def links(base):
    count=0
    for p in base.rglob('*.md'):
        text=MATH.sub('',p.read_text(encoding='utf-8'))
        text=re.sub(r'```math[\s\S]*?```|\$`[^`]*`\$','',text)
        for m in re.finditer(r'!?\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))\)',text):
            target=m[1] or m[2]
            if urlsplit(target).scheme or target.startswith('#'):continue
            assert (p.parent/unquote(target.split('#',1)[0])).exists(),(p,target)
            count+=1
    return count
result={'new_short_notes':len(entries),'equation_start':21,'equation_end':equation,'reading_links':links(READ),'native_links':links(NATIVE),'entries':entries}
with tempfile.TemporaryDirectory() as tmp:
    dest=Path(tmp)/'Vault/Courses'/SUBJECT;shutil.copytree(NATIVE,dest)
    assert links(dest)==result['native_links']
result['relocated_native_links_pass']=True
(OUT/'re-publication.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='entries'},indent=2))
