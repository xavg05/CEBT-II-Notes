"""Cache original-resolution scans and four-page overview montages; never modify PDFs."""
from pathlib import Path
import hashlib, json
import pymupdf
from PIL import Image, ImageOps, ImageDraw

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'other/work/scratch/separations'
records = []
for unit, source in enumerate(sorted((ROOT / 'other/sources/Separations II').glob('*.pdf')), 1):
    dest = OUT / f'U{unit}'
    dest.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(source)
    pages = []
    for i, page in enumerate(doc):
        target = dest / f'p{i+1:03d}.png'
        images = page.get_images(full=True)
        if len(images) == 1 and len(page.get_image_info()) == 1:
            pix = pymupdf.Pixmap(doc, images[0][0])
            if pix.colorspace and pix.colorspace.n > 3:
                pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
            pix.save(str(target))
            method = 'embedded scan'
        else:
            page.get_pixmap(dpi=200, annots=True).save(str(target))
            method = 'page rendering'
        pages.append({'page': i+1, 'image': str(target.relative_to(ROOT)), 'method': method})
    for start in range(0, len(pages), 4):
        sheet = Image.new('RGB', (1400, 2040), 'white')
        draw = ImageDraw.Draw(sheet)
        for k in range(min(4, len(pages)-start)):
            im = Image.open(dest / f'p{start+k+1:03d}.png').convert('RGB')
            im = ImageOps.contain(im, (700, 990))
            x, y = (k % 2)*700, (k // 2)*1020
            sheet.paste(im, (x, y+30))
            draw.text((x+12, y+8), f'U{unit} PDF page {start+k+1}', fill='black')
        sheet.save(dest / f'montage-{start+1:03d}-{min(start+4,len(pages)):03d}.png')
    records.append({'unit': unit, 'source': str(source.relative_to(ROOT)), 'sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'pages': pages})
    doc.close()
(OUT / 'source-manifest.json').write_text(json.dumps(records, indent=2), encoding='utf-8')
print(json.dumps([{'unit': r['unit'], 'pages': len(r['pages']), 'sha256': r['sha256']} for r in records], indent=2))
