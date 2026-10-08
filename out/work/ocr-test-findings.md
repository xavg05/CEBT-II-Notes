# OCR / PDF-reading test — findings

Test date: 2025-10-08. Read-only; no notes written.

## Corpus
32 PDFs in sources/ (16 Advanced Biotech, 16 Equilibrium Thermodynamics).
**None is scanned** — all have embedded fonts and a text layer (pdffonts non-empty for all 32).
No Separations II PDFs present yet.

Worst text layers (chars/page from pdftotext):
  Lecture14.pdf          59 ch/pg  (sparse: figures only, not garbled)
  20TLect3.pdf          166 ch/pg  (maths garbled)
  20TLect5.pdf          333 ch/pg  (equations fragmented; used for this test)
  20TLect1.pdf          204 embedded fonts (heavy symbol-font subsetting)

## Tools
pdfinfo pdftotext pdffonts pdftoppm   OK (poppler, /opt/homebrew)
tesseract 5.5.3 / leptonica 1.87.0    OK
ImageMagick montage + magick          OK (newly available; was missing at plan time)
PyMuPDF 1.28.2                        OK (scratch venv; system python also has fitz)
ocrmypdf                              NOT INSTALLED (not needed — nothing is scanned)

## OCR accuracy, 20TLect5.pdf rendered at 250 dpi
Transcripts: p4-04.txt, p6-06.txt, p13-13.txt

PERFECT (plain prose, sans-serif body text):
  "Note:  Gibbs energy of mixing negative, so mixing is spontaneous"
  "Chemical potential of mixing larger for more dilute species"
  "(i) Infinite dilution ebulliometry"
  "Boil pure component 2 and measure"
  "Add a small amount of 1.  Reboil at same T.  Measure AP and Ax"   <- DP/Dx lost

CONCRETE ERRORS (p6):
  mu_1          -> "fy"           Greek mu not recognised at all
  mu_1^IM       -> "M,”"          superscript IM -> comma + quote
  mu_1^ex       -> "p"            whole term collapsed to one letter
  mu_2          -> "Hy"
  mu_2^IM       -> "Lb""
  ln 0.3        -> "1n0.34"       l->1, space lost, AND digit corrupted 0.3 -> 0.34
  0.7^2         -> "0.7*"         exponent -> asterisk
  0.3^2         -> "0.3*"
  J mol^-1      -> "Jmol"" / "Jmol”"   superscript -1 -> quote mark
  G_1, G_2      -> "G,"           every subscript -> comma
  S_1 dT        -> "S,dT"
  minus sign    -> em-dash "—"

CONCRETE ERRORS (p4 — a figure, axis labels only):
  Entire plot (4 curves) produced 6 orphan tokens:
    "q)", "(Jmol)", "37 Jmol"", "—446 Jmol"", "—483 Jmol"
  LOST COMPLETELY: axis label G, x-axis x_1, and all three curve labels
    (DG^ex, DG^mix, DG_IM^mix). Numbers survive but are unattributable to curves.

CONCRETE ERRORS (p13 — text + partial derivatives + P-x-y diagram):
  P = P_2^SAT   -> "P =P,""
  (dP/dx_1)_T|_{x2=0} -> "( oP" / "pat OX, r" / "LST"   derivative fully destroyed
  Delta P, Delta x    -> "AP", "Ax"                     Greek Delta -> "A"
  x_1, y_1 axis label -> "X,Y,"
  Diagram (L, L+V, V regions, two P^SAT points, tangent) -> nothing usable

## Read-tool page limits
  pages "1-20"   OK  (20 pages returned in one call)
  pages "21-25"  OK  (5 pages)
  pages "22-42"  FAILS: "Page range exceeds maximum of 20 pages per request"
  pages "3,4,6"  FAILS: "Invalid pages parameter ... Give one page or one range, not a list"
So: max 20 pages per call, contiguous range only.

## Verdict
- OCR is reliable for plain prose only.
- Every equation, subscript, superscript, Greek letter and sign was corrupted.
- One error was NUMERICALLY silent-but-fatal: ln 0.3 -> 1n0.34.
- Figures, graphs and axis labels are not recoverable by OCR at all.
- Tesseract adds nothing over pdftotext here, since nothing is scanned.

## Proposed workflow for the real run
1. Survey with pdfinfo + a PyMuPDF montage (5 across, ~330 px) to find unique slides
   and skip build-up duplicates.
2. Read prose from the page images with the Read tool, max 20 contiguous pages per call.
3. Read every equation, number and axis label from the page image. Never from
   pdftotext and never from tesseract.
4. Re-derive each equation and recompute every number in Python before use.
5. Crop figures with PyMuPDF at Matrix(4,4), then open each PNG to verify.
