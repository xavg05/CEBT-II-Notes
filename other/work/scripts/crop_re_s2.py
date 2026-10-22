"""Crop RE-07 to RE-12 figures from the section 2 source PDF (rectangles in PDF points)."""
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / 'other/sources/Reaction Engineering II/CEBT II reaction engineering 2 - reactions of solids.pdf'
FIGS = ROOT / 'notes/Reaction Engineering II/figs'
CROPS = [
    (2, (70, 70, 480, 432), 'RE-07-shrinking-particle.png'),
    (5, (140, 452, 456, 706), 'RE-08-shrinking-particle-conversion.png'),
    (6, (68, 386, 512, 548), 'RE-09-shrinking-core-sequence.png'),
    (7, (140, 92, 454, 300), 'RE-09-shrinking-core-profile.png'),
    (10, (140, 66, 456, 320), 'RE-10-shrinking-core-conversion.png'),
    (12, (204, 436, 395, 660), 'RE-12-falling-particle-reactor.png'),
    (13, (80, 92, 508, 240), 'RE-12-moving-belt-reactor.png'),
    (13, (106, 288, 498, 420), 'RE-12-rotary-kiln.png'),
    (13, (165, 472, 400, 678), 'RE-12-fluidised-bed.png'),
    (14, (214, 112, 388, 318), 'RE-12-fixed-bed.png'),
]
doc = pymupdf.open(SRC)
for page, rect, name in CROPS:
    pix = doc[page - 1].get_pixmap(matrix=pymupdf.Matrix(4, 4), clip=pymupdf.Rect(*rect))
    pix.save(FIGS / name)
    print(name, pix.width, pix.height)
