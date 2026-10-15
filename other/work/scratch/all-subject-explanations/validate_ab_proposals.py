import json
import pathlib
import re

root = pathlib.Path(__file__).resolve().parents[4]
entries = json.loads((root / 'other/work/scratch/all-subject-explanations/ab-proposals.json').read_text(encoding='utf-8'))
results = []
for entry in entries:
    original = (root / entry['path']).read_text(encoding='utf-8')
    changed = original
    for edit in entry['edits']:
        old = edit['old'].replace('\r\n', '\n')
        new = edit['new'].replace('\r\n', '\n')
        assert changed.count(old) == 1, (entry['note'], old)
        changed = changed.replace(old, new, 1)
    assert re.findall(r'\\tag\{[^}]+\}', original) == re.findall(r'\\tag\{[^}]+\}', changed), entry['note']
    assert re.findall(r'!\[[^\]]*\]\([^)]*\)', original) == re.findall(r'!\[[^\]]*\]\([^)]*\)', changed), entry['note']
    results.append({'note': entry['note'], 'edits': len(entry['edits']), 'characters_added': len(changed)-len(original)})
assert len(entries) == 57
assert len(set(e['path'] for e in entries)) == 57
output = {'notes': len(entries), 'edits': sum(r['edits'] for r in results), 'all_unique_anchors': True, 'numbered_equations_and_figure_links_preserved': True, 'characters_added': sum(r['characters_added'] for r in results), 'per_note': results}
(root / 'other/work/scratch/all-subject-explanations/ab-proposal-validation.json').write_text(json.dumps(output, indent=2)+'\n', encoding='utf-8')
print(json.dumps({key: val for key, val in output.items() if key != 'per_note'}))
