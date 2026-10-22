"""Relabel and publish all Reaction Engineering II short notes (RE-01 to RE-27).

Supersedes publish_re.py (section 1) and publish_re_supplied.py (provisional RE-S3 to RE-S6
identifiers). Idempotent: renames provisional drafts and figures if still present, writes explicit
equation labels into the canonical drafts, then rebuilds the GitHub reading edition and the native
Obsidian mirror. No complete-section merges are created.

Set RE_ROOT to run against a copy of the repository (dry run).
"""
from pathlib import Path
import hashlib, json, os, re, shutil, tempfile
from urllib.parse import unquote, urlsplit
import pymupdf

ROOT = Path(os.environ.get('RE_ROOT') or Path(__file__).resolve().parents[3])
SUBJECT = 'Reaction Engineering II'
DRAFT = ROOT / 'other/work/drafts' / SUBJECT
READ = ROOT / 'notes' / SUBJECT
NATIVE = ROOT / 'other/obsidian/CEBT-II Notes' / SUBJECT

RENAME = {f'RE-S{s}-{n:02d}': f'RE-{i:02d}' for i, (s, n) in enumerate(
    [(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 4),
     (5, 1), (5, 2), (6, 1), (6, 2), (6, 3), (6, 4)], start=13)}
FIGURES = {
    'RE-S3-03-staged-beds.png': 'RE-15-staged-beds.png',
    'RE-S3-05-transport-pathway.png': 'RE-17-transport-pathway.png',
    'RE-S4-03-bet-isotherms.png': 'RE-20-bet-isotherms.png',
    'RE-S4-04-pore-hysteresis.png': 'RE-21-pore-hysteresis.png',
    'RE-S5-01-rate-maximum.png': 'RE-23-rate-maximum.png',
    'RE-S5-02-temperature-effects.png': 'RE-23-temperature-effects.png',
    'RE-S6-02-pellet-profiles.png': 'RE-25-pellet-profiles.png',
}
TOPICS = [
    ('01 - Foundations for heterogeneous reactor modelling', range(1, 7),
     'Rate conventions, ideal reactor balances, changing gas volume, coupled energy balances, residence-time distributions and molecular mixing.'),
    ('02 - Fluid–solid reactions with a solid reagent', range(7, 13),
     'Shrinking-particle and shrinking-core kinetics under film, product-layer and reaction control; droplet evaporation; reactors for solid reagents.'),
    ('03 - Catalyst materials and deactivation', range(13, 15),
     'Catalyst families, preparation and zeolites; sintering, poisoning, coking and attrition.'),
    ('04 - Catalytic reactors and nonideal flow', range(15, 17),
     'Catalytic reactor types, staged adiabatic beds and tanks-in-series flow models.'),
    ('05 - Industrial catalysts and transport pathways', range(17, 18),
     'Ethylene oxide, methanol and ammonia oxidation; the transport and surface-step sequence.'),
    ('06 - Adsorption equilibria', range(18, 20),
     'Physical and chemical adsorption; Langmuir, dissociative and competitive isotherms.'),
    ('07 - Porous-solid characterisation', range(20, 22),
     'BET surface area, capillary condensation and isosteric enthalpy.'),
    ('08 - Surface mechanisms and apparent kinetics', range(22, 24),
     'Langmuir–Hinshelwood and Eley–Rideal rates; apparent orders, activation energies and oxide redox cycles.'),
    ('09 - Diffusion in porous catalysts', range(24, 25),
     'Molecular, Knudsen and surface diffusion; effective diffusivity.'),
    ('10 - Isothermal diffusion and reaction', range(25, 27),
     'Pellet profiles, Thiele modulus and effectiveness; disguised kinetics and external films.'),
    ('11 - Thermal effects in catalyst pellets', range(27, 28),
     'Coupled heat and mass balances, the Prater bound and multiple steady states.'),
]
RATE_MAX_ANCHOR = 'Its B order is $1-\\theta_B$ when other partial pressures are fixed.'
RATE_MAX_TEXT = (
    '\n\n![Langmuir–Hinshelwood rate and coverages against the pressure of A](../figs/RE-23-rate-maximum.png)\n\n'
    'The plot holds temperature and $P_B$ fixed and raises $P_A$ from zero. The solid curve is the rate; the dashed '
    'curves are the coverages $\\theta_A$ and $\\theta_B$. The rate rises while extra A mainly fills vacant sites, peaks '
    'where $\\theta_A=\\tfrac12$, and then falls because further A displaces the B it needs as a partner. Its vertical '
    'axis is a common illustrative scale for rate and coverage, so only the shapes and the position of the maximum carry meaning.'
)
MATH = re.compile(r'(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$')
TAG = re.compile(r'\\tag\{(\d+)\}')


def read(p):
    return p.read_text(encoding='utf-8').replace('\r\n', '\n')


def write(p, text):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding='utf-8', newline='\n')


def github(text):
    def convert(m):
        if m[1] is None:
            return '$`' + m[2] + '`$'
        expr = m[1].strip()
        tags = TAG.findall(expr)
        assert len(tags) <= 1, expr
        label = f'\n**Equation ({tags[0]})**\n' if tags else ''
        return label + '\n```math\n' + TAG.sub('', expr).strip() + '\n```\n'
    return MATH.sub(convert, text)


# 1. Rename provisional drafts and figures.
for old, new in RENAME.items():
    for p in DRAFT.glob(old + ' - *.md'):
        p.rename(p.with_name(new + p.name[len(old):]))
for old, new in FIGURES.items():
    src, dst = READ / 'figs' / old, READ / 'figs' / new
    if src.exists():
        src.rename(dst)

notes = {}
for p in sorted(DRAFT.glob('RE-[0-9][0-9] - *.md')):
    notes[int(p.name[3:5])] = p
assert sorted(notes) == list(range(1, 28)), sorted(notes)

# 2. Normalise headings, figure names and equation labels in the canonical drafts.
label = 0
for n, p in sorted(notes.items()):
    text = read(p)
    title = p.stem.split(' - ', 1)[1]
    lines = text.split('\n')
    assert lines[0].startswith('# '), p
    lines[0] = f'# RE-{n:02d}: {title}'
    text = '\n'.join(lines)
    for old, new in FIGURES.items():
        text = text.replace(old, new)
    if n == 23 and 'RE-23-rate-maximum.png' not in text:
        assert RATE_MAX_ANCHOR in text, 'rate-maximum anchor missing'
        text = text.replace(RATE_MAX_ANCHOR, RATE_MAX_ANCHOR + RATE_MAX_TEXT, 1)
    if n <= 12:
        # Sections 1 and 2 carry reviewed explicit labels; keep them.
        tags = [int(t) for t in TAG.findall(text)]
        assert all(t > label for t in tags), (p.name, tags, label)
        label = max(tags, default=label)
    else:
        # Sections 3 to 6: every display equation is labelled, continuing the subject sequence.
        assert not re.search(r'(?<![\\\w$])\((?:2[1-9]|[3-9]\d|1\d\d)\)', MATH.sub('', text)), \
            f'{p.name}: prose equation reference would need remapping'

        def number(m):
            global label
            if m[1] is None:
                return m[0]
            label += 1
            body = TAG.sub('', m[1]).rstrip()
            return '$$' + body + f'\n\\tag{{{label}}}' + '$$'
        text = MATH.sub(number, text)
    write(p, text.rstrip() + '\n')

# 3. Publish both editions.
for base in (READ, NATIVE):
    for p in base.rglob('RE-*.md'):
        p.unlink()
entries = []
for folder, ids, blurb in TOPICS:
    paths = [notes[i] for i in ids]
    for k, p in enumerate(paths):
        nav = '[Subject index](../README.md) · [Topic overview](README.md)'
        if k:
            nav = f'[Previous](<{paths[k - 1].name}>) · ' + nav
        if k + 1 < len(paths):
            nav += f' · [Next](<{paths[k + 1].name}>)'
        content = nav + '\n\n<!-- note-content:start -->\n' + read(p).rstrip() + '\n<!-- note-content:end -->\n\n' + nav + '\n'
        write(NATIVE / folder / p.name, content)
        write(READ / folder / p.name, github(content))
        entries.append({'id': p.name[:5], 'path': str((READ / folder / p.name).relative_to(ROOT)),
                        'obsidian': str((NATIVE / folder / p.name).relative_to(ROOT))})
    number_, title = folder.split(' - ', 1)
    first, last = paths[0].name[:5], paths[-1].name[:5]
    overview = f'# {number_}. {title}\n\n[Subject index](../README.md)\n\n{blurb}\n\n'
    if number_ == '02':
        overview += 'Author verification is complete; independent cross-review is pending.\n\n'
    overview += '## Short notes\n\n' + '\n'.join(
        f'- [{p.name[:5]}: {p.stem.split(" - ", 1)[1]}](<{p.name}>)' for p in paths) + '\n'
    for base in (READ, NATIVE):
        write(base / folder / 'README.md', overview)

index = ('# Reaction Engineering II\n\n'
         'These 27 short notes cover the six supplied sections: reactor-modelling foundations, reactions of solid reagents, '
         'catalysts and catalytic reactors, adsorption, surface kinetics, and diffusion and heat effects in catalyst pellets. '
         'Read in order, keeping the shared `figs/` folder with the topics.\n\n'
         'Short notes remain separate; complete-section versions await your chosen merge groups.\n\n## Topics\n\n')
for folder, ids, _ in TOPICS:
    number_, title = folder.split(' - ', 1)
    span = f'RE-{ids[0]:02d}' + (f'–{ids[-1]:02d}' if len(ids) > 1 else '')
    index += f'- [{number_}. {title}](<{folder}/README.md>) — {span}\n'
present = {int(t) for p in notes.values() for t in TAG.findall(read(p))}
gaps = [i for i in range(1, label + 1) if i not in present]
gap_note = (' Labels ' + ', '.join(map(str, gaps)) + ' are unused because earlier example material was removed.'
            if gaps else '')
index += ('\n## Scope and conventions\n\n'
          'Sections 7 (gas–liquid reactors) and 8 (fermenters) are named in the course outline but have not been supplied, '
          'so this is not yet the complete course.\n\n'
          f'Equation labels run continuously from 1 to {label} in teaching order.{gap_note} '
          'Rates state their species, sign and basis; values read from graphs are approximate.\n')
for base in (READ, NATIVE):
    write(base / 'README.md', index)

# Root indexes: replace the subject bullet only.
bullet = (f'- [Reaction Engineering II](<Reaction Engineering II/README.md>) — 11 topics, RE-01–27; '
          'supplied sections 1–6. Sections 7 and 8 await sources.')
for p in (ROOT / 'notes/README.md', ROOT / 'other/obsidian/CEBT-II Notes/README.md'):
    if p.exists():
        text = read(p)
        text, count = re.subn(r'^- \[Reaction Engineering II\]\(.*$', bullet, text, flags=re.M)
        assert count == 1, p
        write(p, text)

# Figures: mirror notes/figs exactly for RE images.
for p in (NATIVE / 'figs').glob('RE-*.png'):
    if not (READ / 'figs' / p.name).exists():
        p.unlink()
for p in (READ / 'figs').glob('RE-*.png'):
    dest = NATIVE / 'figs' / p.name
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(p, dest)
    assert hashlib.sha256(p.read_bytes()).digest() == hashlib.sha256(dest.read_bytes()).digest()


# 4. Validate.
def validate(base):
    links = images = 0
    for p in base.rglob('*.md'):
        text = read(p)
        stripped = re.sub(r'```math[\s\S]*?```|\$`[^`]*`\$', '', MATH.sub('', text))
        assert 'RE-S' not in text, (p, 'provisional identifier remains')
        for m in re.finditer(r'(!?)\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))\)', stripped):
            target = m[2] or m[3]
            if urlsplit(target).scheme or target.startswith('#'):
                continue
            dest = (p.parent / unquote(target.split('#', 1)[0])).resolve()
            assert dest.exists(), (p, target)
            links += 1
            if m[1]:
                pix = pymupdf.Pixmap(str(dest))
                assert pix.width and pix.height
                images += 1
    return {'markdown_files': len(list(base.rglob('*.md'))), 'links': links, 'images': images}


all_tags = []
for n, p in sorted(notes.items()):
    all_tags += [int(t) for t in TAG.findall(read(p))]
assert all_tags == sorted(set(all_tags)), 'equation labels not strictly increasing'
for e in entries:
    g, o = read(ROOT / e['path']), read(ROOT / e['obsidian'])
    assert re.findall(r'\*\*Equation \((\d+)\)\*\*', g) == TAG.findall(o), e['id']
used = {m for p in READ.rglob('RE-*.md') for m in re.findall(r'figs/(RE-[^)>\s]+\.png)', read(p))}
unused = sorted(p.name for p in (READ / 'figs').glob('RE-*.png') if p.name not in used)
assert not unused, unused

result = {'notes': len(entries), 'equation_labels': [all_tags[0], all_tags[-1], len(all_tags)],
          'reading': validate(READ), 'obsidian': validate(NATIVE)}
with tempfile.TemporaryDirectory() as tmp:
    moved = Path(tmp) / 'Vault/Courses' / SUBJECT
    shutil.copytree(NATIVE, moved)
    assert validate(moved) == result['obsidian']
result['portable_relocation_pass'] = True
out = ROOT / 'other/work/progress/re-relabel-validation.json'
write(out, json.dumps({**result, 'entries': entries}, indent=2, ensure_ascii=False))
print(json.dumps(result, indent=2, ensure_ascii=False))
