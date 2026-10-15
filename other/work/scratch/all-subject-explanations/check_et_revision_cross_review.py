import json
import pathlib
import re

root = pathlib.Path(__file__).resolve().parents[4]
base = root / 'other/work/scratch/all-subject-explanations'
manifest = json.loads((base / 'before-revision/manifest.json').read_text(encoding='utf-8'))
proposals = json.loads((base / 'et-proposals.json').read_text(encoding='utf-8'))
rows = []
for entry in proposals:
    path = entry['path']
    before = (base / 'before-revision' / manifest[path]).read_text(encoding='utf-8')
    current = (root / path).read_text(encoding='utf-8')
    expected = before
    for edit in entry['edits']:
        old = edit['old'].replace('\r\n', '\n')
        new = edit['new'].replace('\r\n', '\n')
        assert expected.count(old) == 1, (entry['note'], 'anchor not unique')
        expected = expected.replace(old, new, 1)
    assert expected == current, (entry['note'], 'actual differs from proposals')
    assert re.findall(r'\\tag\{[^}]+\}', before) == re.findall(r'\\tag\{[^}]+\}', current)
    assert re.findall(r'!\[[^\]]*\]\([^)]*\)', before) == re.findall(r'!\[[^\]]*\]\([^)]*\)', current)
    rows.append({'note': entry['note'], 'edits': len(entry['edits']), 'applied_exactly': True})
assert len(rows) == 43
result = {'notes': len(rows), 'edits': sum(x['edits'] for x in rows), 'applied_exactly': True, 'equation_tags_and_figures_preserved': True, 'per_note': rows}
(base / 'et-independent-cross-review-validation.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k != 'per_note'}))
