"""Close the AB and ET cross-review corrections of the 2026-10-15 explanation revision.

Edits the native short note, its existing complete section and the canonical
reviewed unit together, then republishes those native files to the reading
edition. Refuses to run if a reading file has drifted from its native source.
"""
from pathlib import Path
import json, re, sys
sys.path.insert(0, str(Path(__file__).parent))
import apply_subject_explanation_revisions as A

ROOT, NATIVE, READ, OUT = A.ROOT, A.NATIVE, A.READ, A.OUT
AB = NATIVE/'Advanced Biotechnology'
corrections = json.loads((OUT/'et-cross-review-corrections.json').read_text(encoding='utf-8'))
corrections += [
    {'path': (AB/'07 - DNA nanotechnology/AB-21 - Structural DNA nanotechnology and DNA origami.md').relative_to(ROOT).as_posix(),
     'note': 'AB-21', 'gap': 'Absolute equilibrium claim conflicts with the added annealing-timescale qualification.',
     'edits': [{'old': 'Cooling slowly from above $T_m$ keeps the system equilibrated, so it escapes these **kinetic traps**.',
                'new': 'Cooling slowly from above $T_m$ can allow incorrect contacts to exchange and help the system escape these **kinetic traps**.'}]},
    {'path': (AB/'15 - Gene regulation and synthetic circuits/AB-51 - Stochastic gene expression and noise.md').relative_to(ROOT).as_posix(),
     'note': 'AB-51', 'gap': 'Pulse-smoothing statement lacked its reference regime.',
     'edits': [{'old': 'A short promoter pulse produces some messages, but a long-lived protein pool changes only a little during that pulse.',
                'new': 'Around a steady expression level, a promoter fluctuation short compared with protein lifetime has little time to change protein abundance relative to its sustained effect: it produces some messages, but the long-lived protein pool changes only a little during that pulse.'}]},
]

native_touched = set()
for item in corrections:
    p = ROOT/item['path']
    subject = p.relative_to(NATIVE).parts[0]
    A.pending[p] = A.edit(A.read(p), item['edits'], p)
    native_touched.add(p)
    number = int(re.search(r'(?:ET|AB)-(\d+)', p.name)[1])
    complete = p.parent/'Complete section.md'
    A.section_edit(complete, number, item['edits']); native_touched.add(complete)
    archive, = (ROOT/'other/work/archive/reviewed-units'/subject).glob(p.parent.name[:2]+' - *.md')
    A.section_edit(archive, number, item['edits'])

for p in native_touched:
    target = READ/p.relative_to(NATIVE)
    assert A.read(target) == A.github(A.originals[p]), (target, 'reading edition drifted from native')
    A.pending[target] = A.github(A.pending[p])
for p, text in A.pending.items():
    assert '�' not in text and A.tags(A.originals[p]) == A.tags(text), p
    p.write_text(text, encoding='utf-8')
record = [{'note': c['note'], 'path': c['path'], 'gap': c['gap'], 'edits': len(c['edits'])} for c in corrections]
(OUT/'cross-review-corrections-applied.json').write_text(json.dumps(
    {'notes': record, 'files': sorted(p.relative_to(ROOT).as_posix() for p in A.pending)}, indent=2, ensure_ascii=False), encoding='utf-8')
print(json.dumps({'notes': [c['note'] for c in corrections], 'files_updated': len(A.pending)}, indent=2))
