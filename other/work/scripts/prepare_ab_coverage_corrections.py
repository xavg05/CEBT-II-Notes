"""Prepare exact reviewed corrections; mutate owned notes only with user authority.

Default execution validates all targets and writes a reviewable manifest only.
Use --apply-user-authorized only after the user grants the AGENTS ownership exception.
"""
from pathlib import Path
import argparse, ast, json, re, runpy

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'other/work/scratch/coverage-audit-20261014'
parser = argparse.ArgumentParser()
parser.add_argument('--apply-user-authorized', action='store_true')
parser.add_argument('--extend-reviewed', help='Workspace-relative JSON of reviewed consistency corrections')
args = parser.parse_args()
previous = OUT/'ab-correction-batch.json'
if previous.exists() and json.loads(previous.read_text(encoding='utf-8')).get('authorized_application'):
    if args.extend_reviewed:
        assert args.apply_user_authorized, 'The ownership exception must cover applying the reviewed extension.'
        batch = json.loads(previous.read_text(encoding='utf-8'))
        namespace = {'re':re, 'MATH':re.compile(r'(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$')}
        tree = ast.parse((ROOT/'other/work/scripts/build_notes.py').read_text(encoding='utf-8'))
        pure = ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ['compatible','github']],type_ignores=[])
        exec(compile(pure,'<publisher-formatters>','exec'),namespace)
        formatter = namespace['github']
        proposal_path = (ROOT/args.extend_reviewed).resolve()
        assert proposal_path.is_relative_to(ROOT)
        pending = {}
        known = {entry['id'] for entry in batch['replacements']}
        for change in json.loads(proposal_path.read_text(encoding='utf-8')):
            if change['id'] in known:
                continue
            pub = ROOT/change['published']
            targets = [(ROOT/change['canonical'],False),(pub,True),(pub.parent/'Complete section.md',True)]
            targets += [(ROOT/'other/obsidian/CEBT-II Notes'/p.relative_to(ROOT/'notes'),False) for p,gh in targets[1:]]
            record = {'id':change['id'],'old':change['old'],'new':change['new'],'targets':[]}
            for p,gh in targets:
                old,new = (formatter(change['old']),formatter(change['new'])) if gh else (change['old'],change['new'])
                text = pending.get(p,p.read_text(encoding='utf-8'))
                assert text.count(old)==1,(change['id'],p,text.count(old))
                pending[p] = text.replace(old,new)
                record['targets'].append(p.relative_to(ROOT).as_posix())
            batch['replacements'].append(record)
        for p,text in pending.items():
            p.write_text(text,encoding='utf-8')
        batch['files'] = len({target for entry in batch['replacements'] for target in entry['targets']})
        previous.write_text(json.dumps(batch,indent=2,ensure_ascii=False),encoding='utf-8')
    runpy.run_path(str(ROOT/'other/work/scripts/verify_ab_coverage_corrections.py'), run_name='__main__')
    raise SystemExit(0)
changes = json.loads((OUT/'review/ab-proposed-corrections.json').read_text(encoding='utf-8'))
structure = 'other/work/archive/reviewed-units/Advanced Biotechnology/08 - Protein structure - determination and prediction.md'
ab25 = next((ROOT/'notes/Advanced Biotechnology').rglob('AB-25 - *.md'))
canonical_text = (ROOT/structure).read_text(encoding='utf-8')
replacements = [
    ('AB-25-NMR', next(x for x in canonical_text.splitlines() if x.startswith('**NMR** abandons')),
     '**NMR** measures nuclear-spin resonances from an ensemble of protein molecules tumbling in solution. Chemical shifts, through-space interactions and scalar couplings provide structural restraints without an ordered crystal. Its observables are ensemble and time averaged; it does not image one isolated molecule.'),
    ('AB-25-ensemble', next(x for x in canonical_text.splitlines() if x.startswith('5. The result is an **ensemble**')),
     '5. The result is an **ensemble** of structures compatible with the restraints. Spread can reflect incomplete restraints or modelling uncertainty as well as flexibility; establishing dynamics requires suitable experimental observables rather than model spread alone.'),
    ('AB-25-size', next(x for x in canonical_text.splitlines() if x.startswith('**Why cryo-EM does better')),
     '**Why cryo-EM does better with large particles.** Alignment requires recognising a particle’s orientation from a noisy projection. Larger particles generally provide more distinguishing features and stronger contrast. Smaller particles are harder to align reliably. Around 100 kDa is a useful practical scale for this comparison, rather than a universal lower size limit; achievable performance depends on specimen, contrast, symmetry, detector and reconstruction method.'),
]
for ident, old, new in replacements:
    changes.append(dict(id=ident, canonical=structure, published=ab25.relative_to(ROOT).as_posix(), old=old, new=new))
for i, entry in enumerate(json.loads((OUT/'review/ab25-adjacent-corrections.json').read_text(encoding='utf-8')), 1):
    entry.update(id=f'AB-25-adjacent-{i}', published=ab25.relative_to(ROOT).as_posix())
    changes.append(entry)
seq = 'other/work/archive/reviewed-units/Advanced Biotechnology/04 - Sequencing II - long reads and applications.md'
ab14 = next((ROOT/'notes/Advanced Biotechnology').rglob('AB-14 - *.md'))
for label, old, new in [
    ('amplification', '| Amplification | cloning | PCR + bridge PCR | **none** | **none** |', '| Amplification | sufficient template required; cloning in shotgun workflows | PCR + bridge PCR | **none** | **none** |'),
    ('preparation', '| Preparation | per-fragment cloning | 1–2 days | minutes | circularisation |', '| Preparation | purified template; separate clone preparation for shotgun libraries | 1–2 days | minutes | circularisation |'),
]:
    changes.append(dict(id='AB-14-table-'+label, canonical=seq, published=ab14.relative_to(ROOT).as_posix(), old=old, new=new))

MATH = re.compile(r'(?<!\\)\$\$([\s\S]*?)(?<!\\)\$\$|(?<!\\)\$((?:\\.|[^$])*?)(?<!\\)\$')
def github(s):
    def convert(m):
        if m[1] is None:
            return '$`'+m[2]+'`$'
        formula = m[1].strip()
        tags = re.findall(r'\\tag\{(\d+)\}', formula)
        label = '\n**Equation ('+tags[0]+')**\n' if tags else ''
        return label+'\n```math\n'+re.sub(r'\\tag\{\d+\}', '', formula).strip()+'\n```\n'
    return MATH.sub(convert, s)

pending = {}
manifest = []
for change in changes:
    pub = ROOT/change['published']
    targets = [(ROOT/change['canonical'], False), (pub, True), (pub.parent/'Complete section.md', True)]
    targets += [(ROOT/'other/obsidian/CEBT-II Notes'/p.relative_to(ROOT/'notes'), False) for p, gh in targets[1:]]
    entry = {'id': change['id'], 'old': change['old'], 'new': change['new'], 'targets': []}
    for p, gh in targets:
        old, new = (github(change['old']), github(change['new'])) if gh else (change['old'], change['new'])
        text = pending.get(p, p.read_text(encoding='utf-8'))
        assert text.count(old) == 1, (change['id'], p, text.count(old))
        pending[p] = text.replace(old, new)
        entry['targets'].append(p.relative_to(ROOT).as_posix())
    manifest.append(entry)

(OUT/'ab-correction-batch.json').write_text(json.dumps({'authorized_application': args.apply_user_authorized, 'replacements': manifest, 'files': len(pending)}, indent=2, ensure_ascii=False), encoding='utf-8')
if args.apply_user_authorized:
    for p, text in pending.items():
        p.write_text(text, encoding='utf-8')
print(json.dumps({'applied': args.apply_user_authorized, 'exact_replacements': len(manifest), 'validated_files': len(pending)}))
