"""Publish only Codex's Reaction Engineering short notes; never merge them.

Run with the portable Python in other/work/tools/python on Windows.
The historical two-course publisher remains untouched.
"""
from pathlib import Path
import hashlib, json, re, shutil, tempfile
from urllib.parse import unquote, urlsplit
import pymupdf

ROOT = Path(__file__).resolve().parents[3]
from check_inline_math import check_files
check_files(p for base in [ROOT/'other/work/drafts', ROOT/'other/work/archive/reviewed-units'] for p in base.rglob('*.md'))
SUBJECT = 'Reaction Engineering II'
TOPIC = '01 - Foundations for heterogeneous reactor modelling'
DRAFT = ROOT / 'other/work/drafts' / SUBJECT
READ = ROOT / 'notes' / SUBJECT
EXPORT = ROOT / 'other/obsidian/CEBT-II Notes' / SUBJECT
MATH = re.compile(r'(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$')

def github(text):
    def render(m):
        if m[1] is None:
            return '$`' + m[2] + '`$'
        formula = m[1].strip()
        tags = re.findall(r'\\tag\{(\d+)\}', formula)
        assert len(tags) <= 1
        label = '\n**Equation (' + tags[0] + ')**\n' if tags else ''
        return label + '\n```math\n' + re.sub(r'\\tag\{\d+\}', '', formula).strip() + '\n```\n'
    return MATH.sub(render, text)

files = sorted(DRAFT.glob('RE-*.md'))
assert len(files) == 6
tags = []
manifest = []
def pair(rel, content):
    for base, native in [(READ, False), (EXPORT, True)]:
        p = base / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content if native else github(content), encoding='utf-8')
    cost = sum((m[1] or m[2]).count('{') + 1 for m in MATH.finditer(content))
    assert cost < 2000
    manifest.append({'path': str((READ/rel).relative_to(ROOT)), 'obsidian': str((EXPORT/rel).relative_to(ROOT)), 'math_cost': cost})

for i,p in enumerate(files):
    text = p.read_text(encoding='utf-8')
    tags.extend(int(t) for t in re.findall(r'\\tag\{(\d+)\}',text))
    nav = '[Subject index](../README.md) · [Topic overview](README.md)'
    if i:
        nav = f'[Previous](<{files[i-1].name}>) · ' + nav
    if i+1 < len(files):
        nav += f' · [Next](<{files[i+1].name}>)'
    pair(Path(TOPIC)/p.name, nav + '\n\n<!-- note-content:start -->\n' + text.rstrip() + '\n<!-- note-content:end -->\n\n' + nav + '\n')
assert tags == sorted(set(tags))  # Preserve remaining labels after example removal.

overview = f'# Foundations for heterogeneous reactor modelling\n\n[Subject index](../README.md)\n\nStart with assumptions and rate conventions, then build material and energy balances. Residence-time distributions and molecular mixing explain why real flow can give different conversion from ideal models.\n\nThe six short notes cover the opening section. Author verification is complete; independent cross-review is pending. Equation labels 1–20 continue across this first batch. A complete-section merge awaits the requested grouping.\n\n'
overview += '\n'.join(f'- [{p.stem.split(" - ",1)[0]}: {p.stem.split(" - ",1)[1]}](<{p.name}>)' for p in files) + '\n'
pair(Path(TOPIC)/'README.md', overview)
pair(Path('README.md'), f'# {SUBJECT}\n\nRead topics in teaching order. Keep the shared `figs/` folder with the notes when copying this subject.\n\n- [01. Foundations for heterogeneous reactor modelling](<{TOPIC}/README.md>) — RE-01–06, written; independent cross-review pending.\n\nFurther topics are planned. The source for section 2 (fluid–solid reactions with a solid reagent) is missing, as are the gas–liquid and fermenter sections. This is an initial batch, not a complete course.\n')

for p in (READ/'figs').glob('RE-*.png'):
    target = EXPORT/'figs'/p.name
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(p,target)
    assert hashlib.sha256(p.read_bytes()).digest() == hashlib.sha256(target.read_bytes()).digest()

def validate(base):
    links = 0
    for p in base.rglob('*.md'):
        text = p.read_text(encoding='utf-8')
        for m in re.finditer(r'(!?)\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))\)',text):
            target=m[2] or m[3]
            if urlsplit(target).scheme or target.startswith('#'):
                continue
            dest=(p.parent/unquote(target.split('#',1)[0])).resolve()
            assert dest.exists(), (p,target)
            links+=1
            if m[1]:
                pix=pymupdf.Pixmap(str(dest))
                assert pix.width>0 and pix.height>0
    return {'files':len(list(base.rglob('*.md'))),'links':links}

result={'reading':validate(READ),'obsidian':validate(EXPORT),'files':manifest,'equations':tags}
with tempfile.TemporaryDirectory() as tmp:
    relocated=Path(tmp)/'Vault/Courses'/SUBJECT
    shutil.copytree(EXPORT,relocated)
    assert validate(relocated)==result['obsidian']
result['portable_relocation_pass']=True
(ROOT/'other/work/scratch/codex-reaction-engineering/publish-validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='files'},indent=2))
