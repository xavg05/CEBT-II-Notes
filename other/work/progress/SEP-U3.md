# SEP-U3 membranes: author production record

Owner: codex. Twelve source-order short drafts complete under `other/work/drafts/Separations II/U3/`. All 51 original pages read visually in batches 1–20,21–35,36–51; every page also individually opened at original-scan-derived resolution. No source pages omitted. Root confirmed absorption pilot passed before drafting. Independent cross-review is pending; this is not a reviewed-unit claim.

Coverage/transcription and corrections: `other/work/ocr/Separations II/U3.md`. Page-to-draft mapping is complete. Handwritten additions and printed equations/data included; highlight-only marks not individually replicated. Original scans remain unchanged. Twelve titles cover mechanisms/structure, equipment/modes, metrics/resistances, binary gas, gas estimate, gas integration, liquid rejection, polarisation/gel, osmosis, coupled whey design, continuous plants/fouling, RO differential design.

Python: `other/work/scratch/separations/U3/verify.py`; results `results.json`; all five supplied numerical examples recomputed, including the source integration mesh and refined integration. Added osmotic-pressure estimate, parameterised whey table, RO refined area. Unit checks and limits explicitly in notes. Gas mesh refinement changes area from ~12433 to12443m², so notes report ~1.24e4m². RO arithmetic area51.1609 requires18 whole modules, whereas integration under same ideal assumptions50.9024 permits17. This is an accuracy-dependent threshold, not a universal source correction.

Figures: nine original colour crops in `notes/Separations II/figs/u3-*.png`. Every initial crop opened; coordinate scaling error identified and fixed by converting displayed1334×1888 boxes to native1653×2338; final crops reopened. `figure-crops.json` records display-coordinate boxes; the script supplies native conversion. Ambiguity-table boxes use displayed coordinate basis as documented. No AI figures generated.

## External sources actually opened and read

- ETH Zurich, *Membrane Separations* (2016), https://ethz.ch/content/dam/ethz/special-interest/mavt/process-engineering/separation-processes-laboratory-dam/documents/education/RCS_2020/Membranes/Classes/Membrane_course_HS2016.pdf . Successfully retrieved text on first open and subsequently opened sections on gas driving forces, polarisation and AppendixA. Later screenshot requests failed with cache-miss; visual screenshot is not claimed. Used as independent conceptual/equation support, not copied prose.
- Lamm and Jarboe, *Chemical Engineering Separations: A Handbook for Students*, membranes chapter, https://eng.libretexts.org/Bookshelves/Chemical_Engineering/Chemical_Engineering_Separations:_A_Handbook_for_Students_(Lamm_and_Jarboe)/01:_Chapters/1.06:_Membranes . Read gas diffusion/sorption, film resistances and RO chemical-potential equations; supports coefficient/units distinctions.
- Cui, Jiang and Field, *Fundamentals of Pressure-Driven Membrane Separation Processes*, Elsevier textbook sample chapter, https://booksite.elsevier.com/samplechapters/9781856176323/9781856176323.pdf . Actually read classification, retention, film model and polarisation versus fouling sections; supports mechanism and limitations.

MIT Cooney lecture resource page and its PDF were opened but PDF extraction yielded one line and screenshots not used: do not claim its teaching content consulted. MIT *Fundamentals of desalination* URL failed to retrieve: not used.

## ETH gas-model evidence preserved for review

Retrieved text lines2763–2821, PDF zero-based80–81 (PDF indices81–82), AppendixA. Paraphrase: the co-current asymmetric hollow-fibre model assumes constant properties, isothermal operation and fixed pressures. Its porous support has negligible hydraulic resistance but keeps locally emerging gas compositions from mixing inside that support. This permits different local interfacial and collected permeate mole fractions; the former is set by local retentate conditions. Overall and differential component balances subsequently distinguish those quantities. Original source short excerpt,14words: “No mixing of permeate fluxes of different compositions occurs inside the porous supporting layer”.

This resolves a missing assumption in the supplied handout's quadratic-yi design. Drafts clearly state it, and explain that directly contacting a shared mixed permeate channel requires its actual composition in the pressure driving force instead. Root's later failed ETH open does not invalidate the worker's successfully read text, but no ETH screenshot is claimed.

## Author-certain source corrections and qualifications

- Printed VCR denominator corrected by handwritten retentate and steady balance.
- No-polarisation wall concentration is approximately bulk, not printed Cw<Cf.
- Printed gas outletx=.005 corrected to.05 from95%nitrogen and quadratic/data.
- Distinguish overall stage cut from oxygen component recovery.
- Graph composition gaps are not pressure driving forces without pressure weighting.
- Osmotic opposition decreases solvent flux; it can increase salt passage via wall enrichment.
- Gel pressure includes osmotic opposition; high-concentration ratios useg/L, notM.
- RO retentate exponent−.995, not printed−.005.
- Secondary diagram is retentate staging, not permeate polishing despite handwriting shorthand.
- Salt target.25g/L treated as example design specification, not complete drinking-water guarantee; historical energy claims omitted from universal statements.

No unresolved consequential handwriting ambiguity. Root independently blind-read p40 polynomial and example data before seeing author transcription; agreement recorded in OCR record.
