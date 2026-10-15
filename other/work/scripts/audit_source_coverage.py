"""Build a reproducible source/reading inventory; text matches are diagnostics, not proof."""
from pathlib import Path
import hashlib, json, re
import pymupdf

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'other/work/scratch/coverage-audit-20261014'
OUT.mkdir(parents=True, exist_ok=True)
records = []
for subject in sorted((ROOT / 'other/sources').iterdir()):
    if not subject.is_dir():
        continue
    notes = sorted(p for p in (ROOT / 'notes' / subject.name).rglob('*.md')
                   if re.match(r'^(ET|AB|RE|SEP|PDC)-\d+', p.name))
    note_text = {str(p.relative_to(ROOT)): p.read_text(encoding='utf-8') for p in notes}
    sources = []
    for pdf in sorted(subject.glob('*.pdf'), key=lambda p: [int(x) if x.isdigit() else x for x in re.split(r'(\d+)', p.name)]):
        doc = pymupdf.open(pdf)
        pages = []
        for i, page in enumerate(doc):
            value = page.get_text()
            pages.append({'page': i + 1, 'text': value})
        sources.append({'pdf': str(pdf.relative_to(ROOT)), 'sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(), 'pages': pages})
    record = {'subject': subject.name, 'notes': note_text, 'sources': sources}
    records.append(record)
    (OUT / (subject.name + '.txt')).write_text('\n\n'.join(
        f"SOURCE {s['pdf']} PAGE {p['page']}\n{p['text']}" for s in sources for p in s['pages']), encoding='utf-8')
(OUT / 'inventory.json').write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps([{'subject': r['subject'], 'pdfs': len(r['sources']), 'pages': sum(len(s['pages']) for s in r['sources']), 'short_notes': len(r['notes'])} for r in records], indent=2))
