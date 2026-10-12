"""Independently check preserved scientific prose, all active links, and relocation."""
from pathlib import Path
import hashlib,json,re
from urllib.parse import unquote,urlsplit
import pymupdf

ROOT=Path(__file__).resolve().parents[3]
WORK=ROOT/'other/work'
manifest=json.loads((WORK/'LAYOUT-MANIFEST.json').read_text())
def content(p):return p.read_text().split('<!-- note-content:start -->\n',1)[1].split('\n<!-- note-content:end -->',1)[0].strip()
def prose(s):return re.sub(r'\s+',' ',re.sub(r'^#{1,6} ','',s,flags=re.M)).strip()
preserved=0
for subject in manifest['subjects']:
    name=subject['name']
    for unit in subject['sections']:
        canonical=(ROOT/unit['canonical']).read_text()
        native=ROOT/'other/obsidian/CEBT-II Notes'/name/unit['folder']
        complete=content(native/'Complete section.md')
        assert complete.replace('](../figs/','](figs/').strip()==canonical.strip(),unit['canonical']
        first=re.search(r'^## Section \d+:',canonical,re.M)
        overview=canonical.split('\n',1)[1][:first.start()-len(canonical.split('\n',1)[0])-1]
        # Reconstruct all scientific sections from the small-note content alone.
        reconstructed='\n\n'.join(content(native/p) for p in unit['notes'])
        original_sections=canonical[first.start():]
        assert prose(reconstructed).replace('](../figs/','](figs/')==prose(original_sections),(name,unit['folder'])
        preserved+=len(unit['notes'])

links=0;missing=[]
active=[ROOT/p for p in ['README.md','AGENTS.md','CLAUDE.md','PLAN.md','other/README.md','other/work/README.md','other/work/LAYOUT.md','other/work/FINAL-DELIVERY.md','other/obsidian/README.md']]
active+=list((ROOT/'notes').rglob('*.md'))+list((ROOT/'other/obsidian/CEBT-II Notes').rglob('*.md'))
for p in active:
    for m in re.finditer(r'!?\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))\)',p.read_text()):
        target=m[1] or m[2]
        if urlsplit(target).scheme or target.startswith('#'):continue
        dest=p.parent/unquote(target.split('#',1)[0]);links+=1
        if not dest.exists():missing.append((str(p.relative_to(ROOT)),target))
assert not missing,missing
for rel,sha in manifest['figures'].items():
    p=ROOT/rel;assert hashlib.sha256(p.read_bytes()).hexdigest()==sha
    pix=pymupdf.Pixmap(str(p));assert pix.width and pix.height
for item in json.loads((WORK/'scratch/reorganize-layout/preservation.json').read_text()):
    p=ROOT/item['new'];assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'],item['new']
assert not (ROOT/'out').exists() and not (ROOT/'sources').exists()
assert not list(ROOT.glob('**/merged'))
result={'scientific_small_notes_preserved':preserved,'complete_sections_preserved':sum(len(s['sections']) for s in manifest['subjects']),'active_local_links':links,'missing_links':missing,'identical_decoded_subject_figures':len(manifest['figures']),'scientific_and_source_files_preserved':len(json.loads((WORK/'scratch/reorganize-layout/preservation.json').read_text())),'no_out_or_merged_directory':True}
(WORK/'LAYOUT-PRESERVATION.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
