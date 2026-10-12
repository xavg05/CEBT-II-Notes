# Reaction Engineering II — opening batch, 12 October 2026

Owner: codex. Unit RE-U1 is written, with author verification complete. Independent cross-review is pending; it must not be labelled reviewed. No complete-section merge is authorised.

## Source use

- `other/sources/Reaction Engineering II/CEBT II reaction engineering 1.pdf`, all eight pages: rendered and read visually in two overview montages; page 7 also opened individually. Equations were read from page images, not trusted from the extracted text.
- All five available PDFs inventoried to locate later topic boundaries. Only section 1 was fully read for production. Extracted text is a locator, not verified OCR. No source PDF was changed.
- Original figures cropped using PyMuPDF at 4× scale: section 1 p5 reciprocal-rate plots and p7 cascade RTDs. Both final crops opened and inspected; early incomplete crops replaced before publishing.

Opened and read supplementary primary university sources:

| Notes | Source | Use |
|---|---|---|
| RE-01 | [Fogler, Mole balances](https://public.websites.umich.edu/~elements/6e/01chap/summary.html) | Species-rate sign and catalyst-mass basis; distinction between rate and concentration derivative |
| RE-02 | [Fogler, Conversion and reactor sizing](https://public.websites.umich.edu/~elements/6e/02chap/summary.html) | Conversion, reciprocal-rate plot and reactor design framework |
| RE-03 | [Fogler, Stoichiometry](https://public.websites.umich.edu/~elements/6e/04chap/summary.html) | Flow stoichiometric table and concentration–conversion closure |
| RE-04 | [Fogler, Nonisothermal design](https://public.websites.umich.edu/~elements/6e/11chap/summary.html) | Enthalpy balance structure, heat-capacity flow and adiabatic coupling |
| RE-05 | [Fogler, Residence-time distributions](https://public.websites.umich.edu/~elements/6e/16chap/summary.html) | Pulse tracer, moments and ideal-reactor distributions |
| RE-06 | [Fogler, Predicting conversion from RTD](https://public.websites.umich.edu/~elements/6e/17chap/summary.html) | Segregated mini-batch interpretation; maximum mixedness as a distinct closure |

An attempted IUPAC Gold Book page (`https://goldbook.iupac.org/terms/view/T06534`) returned HTTP 403. It was not used or cited as evidence. No external text or figures were copied into the deliverables.

## Content and qualifications

Six standalone small notes in the subject's first topic; matching native Obsidian copy. Native author text is retained in `other/work/drafts/Reaction Engineering II/`. Equation labels 1–20 are provisional continuous numbers for the written batch, identical in both editions.

- Added an explicit ideal-gas stoichiometric closure because section 1 requires deriving concentration from conversion when density changes, but does not supply that derivation.
- Added worked numerical examples to the sparse introductory material; they are illustrative, not claimed as source examples.
- Clarified section 1 p8 terminology: macromixing describes bulk-flow/RTD behaviour, while segregation and maximum mixedness concern molecular mixing. A generic ideal-reactor network is not automatically the maximum-mixedness model for its RTD.
- Kept the energy balance's reaction-rate and reaction-enthalpy normalisations consistent; no confirmed equation typo was corrected in section 1.
- Section 2 is missing. Sections 7 and 8 are also absent. Later short-note numbering remains provisional until section 2's scope is known. The course is not complete.

## Verification and reproduction

Portable Python 3.13.7, PyMuPDF 1.28.2 and Pillow 12.3.0 were installed under ignored `other/work/tools/` because the current Windows environment had no usable Python. KaTeX and marked are installed locally under that same ignored tools folder. The historical two-course builder is unchanged; running it rewrites the all-subject indexes, so preserve/re-add the Reaction Engineering index entries if rebuilding the older subjects.

Run from the repository root:

```powershell
& ./other/work/tools/python/python.exe -X utf8 other/work/scripts/verify_re_u1.py
& ./other/work/tools/python/python.exe -X utf8 other/work/scripts/publish_re.py
node other/work/scripts/check_re_math.mjs
```

- All example numbers recomputed in Python. Separate Simpson integrations verified cascade RTD normalisation, mean, variance and first-order survival for N=1, 4 and 10; checked species-balance residuals and limiting cases. Units and sign conventions checked by derivation.
- Eight pages per edition (six notes plus two indexes); all 54 internal links per edition resolve. Both figures decode, and mirror bytes match.
- Native subject copy relocated into a temporary `Vault/Courses/` directory and its links revalidated. User's vault and Obsidian app were not accessed.
- 341 mathematical expressions parsed in each edition by KaTeX with no failures. Mathematical content and all 20 numbered equation labels match between the editions. All page costs stay below the existing GitHub math budget.
- Every generated page opened by the validation script; all six content notes also rendered through headless Chrome into a local 13-page PDF. All 13 rendered pages visually inspected in four montages: text, formulas and both figures readable. PDF pagination is a scratch preview, not a deliverable.

Evidence: `other/work/scratch/codex-reaction-engineering/{inventory,publish-validation,numerical-validation,math-validation}.json`. Render artifacts are ignored. No GitHub browser runtime rendering or Obsidian runtime check is claimed.
