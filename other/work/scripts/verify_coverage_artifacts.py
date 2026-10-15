from pathlib import Path
import json,hashlib,re
import pymupdf
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'other/work/scratch/coverage-audit-20261014'
inventory=json.loads((OUT/'inventory.json').read_text(encoding='utf-8'))
sources=0
for subject in inventory:
    for source in subject['sources']:
        p=ROOT/source['pdf']
        assert hashlib.sha256(p.read_bytes()).hexdigest()==source['sha256'],p
        sources+=1
figures=0
for p in (ROOT/'notes').rglob('*.png'):
    rel=p.relative_to(ROOT/'notes');native=ROOT/'other/obsidian/CEBT-II Notes'/rel
    assert native.exists(),p
    assert hashlib.sha256(p.read_bytes()).digest()==hashlib.sha256(native.read_bytes()).digest(),p
    pix=pymupdf.Pixmap(str(p));assert pix.width>0 and pix.height>0
    figures+=1
new=json.loads((OUT/'re-publication.json').read_text(encoding='utf-8'))
tags=[]
for item in new['entries']:
    p=ROOT/item['obsidian'];text=p.read_text(encoding='utf-8')
    body=text.split('<!-- note-content:start -->\n',1)[1].split('\n<!-- note-content:end -->',1)[0]
    original=(ROOT/item['draft']).read_text(encoding='utf-8').rstrip()
    def normalise_display(s):
        return re.sub(r'\$\$([\s\S]*?)\$\$',lambda m:'$$'+re.sub(r'\\tag\{\d+\}','',m[1]).strip()+'$$',s)
    assert normalise_display(body)==normalise_display(original),(p,'science preservation')
    assert not re.search(r'\b(slides?|lecturer|lecture PDF)\b',body,re.I),p
    for heading in ['Overview','Intuition','Motivation and explanation','Worked example','Link to other topics','Conclusion']:
        assert '## '+heading in body,(p,heading)
    tags.extend(int(x) for x in re.findall(r'\\tag\{(\d+)\}',body))
assert tags==list(range(21,94)),tags
result={'unchanged_original_pdfs':sources,'decoded_identical_figures_per_edition':figures,'new_notes_preserve_drafts':len(new['entries']),'new_equation_labels':tags,'required_headings_and_standalone_prose_pass':True,'portable_native_relocation_pass':new['relocated_native_links_pass']}
(OUT/'artifact-validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='new_equation_labels'},indent=2))
