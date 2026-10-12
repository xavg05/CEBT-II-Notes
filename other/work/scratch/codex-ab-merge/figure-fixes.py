from pathlib import Path
import pymupdf
root=Path(__file__).resolve().parents[4];scratch=Path(__file__).parent
p=pymupdf.open(root/'sources/Advanced Biotech/Lecture5.pdf')[16]
p.get_pixmap(matrix=pymupdf.Matrix(4,4),clip=pymupdf.Rect(662,24,846,413)).save(str(scratch/'AB-17-melt-curve.png'))
script=scratch/'merge.py';s=script.read_text();s=s.replace('shutil.copy2(AB/path,OUT/path)',"shutil.copy2(Path(__file__).with_name('AB-17-melt-curve.png') if path=='figs/AB-17-melt-curve.png' else AB/path,OUT/path)");script.write_text(s)
(root/'out/work/reviews/AB-U4a.md').write_text('# AB-U4a cross-review\n\nOwner: claude (existing short notes).\n\nAB-17 links `figs/AB-17-melt-curve.png`, but that image contains amplification and standard-calibration curves. Its caption describes melting and derivative plots. Correct figure is the right-hand plot pair on Lecture5 page 17. The new Codex merged qPCR deliverable uses a verified replacement crop; the original short note and figure are untouched.\n\nStatus: original short-note finding remains for its owner.\n')
print('Saved replacement crop and ownership-safe review.')
