from pathlib import Path
import json
import pymupdf
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[3]
out = root / 'other/work/scratch/codex-reaction-engineering'
out.mkdir(parents=True, exist_ok=True)
inventory = []
for source in sorted((root / 'other/sources/Reaction Engineering II').glob('*.pdf')):
    doc = pymupdf.open(source)
    texts = [page.get_text() for page in doc]
    (out / (source.stem + '.txt')).write_text('\n\n'.join(f'PAGE {i+1}\n{t}' for i,t in enumerate(texts)), encoding='utf-8')
    inventory.append({'file': source.name, 'pages': len(doc)})
    print(source.name, len(doc), 'pages')
    for i,t in enumerate(texts):
        lines = [x.strip() for x in t.splitlines() if x.strip() and not x.strip().isdigit()]
        print(i+1, ' | '.join(lines)[:260])
    if source.stem.endswith(' 1'):
        images = []
        for i,page in enumerate(doc):
            pix = page.get_pixmap(matrix=pymupdf.Matrix(1.4,1.4))
            pix.save(out / f'L1-p{i+1:02d}.png')
            images.append(Image.open(out / f'L1-p{i+1:02d}.png').convert('RGB'))
        for start in range(0,len(images),4):
            tile_w, tile_h = images[0].size
            montage = Image.new('RGB',(tile_w*2,tile_h*2),'#bbbbbb')
            for j,im in enumerate(images[start:start+4]):
                montage.paste(im,((j%2)*tile_w,(j//2)*tile_h))
            montage.save(out / f'L1-montage-{start+1}.png')
(out / 'inventory.json').write_text(json.dumps(inventory,indent=2),encoding='utf-8')
