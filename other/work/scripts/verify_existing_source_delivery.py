"""Ensure earlier source-reviewed PDC/SEP drafts survived current publication."""
from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT/'other/work/scratch/coverage-audit-20261014'
EXPORT = ROOT/'other/obsidian/CEBT-II Notes'
def body(p):
    return p.read_text(encoding='utf-8').split('<!-- note-content:start -->\n', 1)[1].split('\n<!-- note-content:end -->', 1)[0].rstrip()

pdc = json.loads((ROOT/'other/work/scratch/pdc/note-manifest.json').read_text(encoding='utf-8'))
for entry in pdc['notes']:
    target = next((EXPORT/'Process Dynamics and Control').rglob(entry['filename']))
    draft = ROOT/'other/work/drafts/Process Dynamics and Control'/entry['filename']
    assert body(target) == draft.read_text(encoding='utf-8').rstrip(), target

sep = json.loads((ROOT/'other/work/scratch/separations/note-manifest.json').read_text(encoding='utf-8'))
equation = 0
figure_map = {}
for entry in sep:
    text = (ROOT/entry['draft']).read_text(encoding='utf-8')
    local = list(map(int, re.findall(r'\\tag\{(\d+)\}', text)))
    mapping = {k: equation+i+1 for i,k in enumerate(local)}
    text = re.sub(r'\\tag\{(\d+)\}', lambda m: '\\tag{'+str(mapping[int(m[1])])+'}', text)
    text = re.sub(r'\b([Ee]quation|[Ee]q\.)\s*\((\d+)\)', lambda m: m[1]+' ('+str(mapping[int(m[2])])+')', text)
    equation += len(local)
    text = re.sub(r'^# .+$', f'# SEP-{entry["number"]:02d}: {entry["title"]}', text, count=1, flags=re.M)
    def figure(m):
        old = m[2]
        if old not in figure_map:
            desc = re.sub(r'^u\d+-(?:\d+-)?', '', old, flags=re.I)
            figure_map[old] = f'SEP-{entry["number"]:02d}-{desc}'
        return '!['+m[1]+'](../figs/'+figure_map[old]+')'
    text = re.sub(r'!\[([^\]]*)\]\(\.\./figs/([^\)]+)\)', figure, text)
    target = next((EXPORT/'Separations II').rglob(entry['filename']))
    assert body(target) == text.rstrip(), target

pages = {}
for unit, total in [(1,33),(2,34),(3,51),(4,23)]:
    transcript = (ROOT/f'other/work/ocr/Separations II/U{unit}.md').read_text(encoding='utf-8')
    recorded = set(map(int, re.findall(r'^\| (\d+) \|', transcript, re.M)))
    assert recorded == set(range(1,total+1)), (unit, recorded)
    pages[f'SEP-U{unit}'] = total
result = {'pdc_notes_preserve_source_reviewed_drafts':len(pdc['notes']), 'sep_notes_preserve_source_reviewed_drafts':len(sep), 'sep_page_index_coverage':pages, 'sep_equation_labels':equation, 'sep_used_figure_names':len(figure_map)}
(OUT/'existing-delivery-validation.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps(result, indent=2))
