# SEP-U1 author production record

Owner: codex. Status: written and author-verified; independent scientific review pending. No publication/index/board changes made by unit author.

All 33 PDF pages visually inspected as original colour scans, in bounded batches. The handwriting pilot p9–12 passed legibility after root blind-reading. Coverage/transcription/ambiguity evidence: `other/work/ocr/Separations II/U1.md`. Figures are original-scan crops, not recreated images.

## Proposed short-note map

| Draft | Title | PDF pages |
|---|---|---|
| U1-01 | Separation choices and continuous contacting | 1–5 |
| U1-02 | Absorption-column equipment | 6–8 |
| U1-03 | Gas–liquid equilibrium conventions | 9 |
| U1-04 | Operating lines and pinch limits | 10–13 |
| U1-05 | Two-film resistances and overall coefficients | 13–17 |
| U1-06 | Film models and coefficient measurement | 18–19 |
| U1-07 | Packed-column height and transfer units | 20–21 |
| U1-08 | Evaluating NTU and logarithmic driving forces | 22–24 |
| U1-09 | HETP and theoretical-stage relationships | 24–26 |
| U1-10 | Packed-column hydraulics and diameter | 27–29 |
| U1-11 | Designing an ammonia absorber | 29–33 |

Administrative learning aims condensed in U1-01; no source content pages omitted. Boundary pages shared where a section starts halfway down the page. Question-number annotations are administrative and omitted. Stage sketch presented as conceptual example, not a calculated three-stage design. Small notes remain separate.

## External sources actually read

- [NPTEL absorption introduction](https://archive.nptel.ac.in/content/storage2/courses/103103035/module4/lec1.pdf), full 6 pages: U1-01/02 equipment and solvent-selection explanations.
- [NPTEL process design, column selection](https://archive.nptel.ac.in/content/storage2/courses/103103027/module7/lec1/1.html): U1-02 holdup, vacuum, cleaning, foaming and side streams.
- [NPTEL interphase transfer](https://archive.nptel.ac.in/content/storage2/courses/103103035/module3/lec7.pdf), 3 pages: U1-03/05 equilibrium conventions and interfacial equilibrium reasoning.
- [LearnChemE stripping summary](https://learncheme.com/quiz-yourself/interactive-self-study-modules/stripping-columns/stripping-columns-summary/): U1-04 operating line below EL and gas-flow influence. Avoided page's inconsistent wording/units by independent derivation.
- [NPTEL differential packed design](https://archive.nptel.ac.in/content/storage2/courses/103103035/module4/lec2.pdf), full 4 pages: U1-04/07 balance, solute-free flows and non-dilute correction.
- [Iowa State Lamm/Jarboe gas–liquid transfer handbook](https://eng.libretexts.org/Bookshelves/Chemical_Engineering/Chemical_Engineering_Separations:_A_Handbook_for_Students_(Lamm_and_Jarboe)/01:_Chapters/1.02:_Mass_Transfer_in_Gas-liquid_Systems): U1-03/05/06 conventions, diffusion/film laws and coefficient bases; actually read content beyond navigation.
- [NPTEL wetted-wall and packed transfer correlations](https://archive.nptel.ac.in/content/storage2/courses/103103035/module3/lec4.pdf), 6 pages: U1-06 empirical diffusivity-exponent limitations.
- [NPTEL transfer-unit design](https://archive.nptel.ac.in/content/storage2/courses/103103035/module4/lec3.pdf), 5 pages: U1-07/08/11 integration procedure and overall HTU. External example contains typos; no external example numbers copied.
- [Iowa State absorption and stripping handbook](https://iastate.pressbooks.pub/chemicalengineeringseparations/chapter/absorption-and-stripping/): U1-09 stage-equivalent framework, U1-10 stage-height/diameter distinction and service-dependent flooding fractions. Equations in this page are rendered images; source HETP formula independently rederived from the original readable handout.

These provide cross-checks and brief explanations; the detailed derivations use the supplied handout and independent balances, not reproduced external prose. No unread retrieved source claimed.

## Author verification

`other/work/scratch/separations/U1/check_u1.py` computes every numerical worked answer, resistance shares, slope limits, HETP and hydraulic illustrative geometry. `numerical-validation.json` preserves inputs/results. Ammonia piecewise analytic quadrature agrees with refined Simpson to better than 1e-6 in NTU; positive driving force checked across interpolation interval. Equations rederived from balances/flux matching; units and zero-resistance, zero-driving-force and parallel-line limits checked.

Nine PNG crops were individually opened after correcting displayed-to-native coordinate scaling. Files: `notes/Separations II/figs/u1-{contacting-stages,packed-column,tray-column,operating-forces,pinch,film-profiles,pressure-drop,hydraulic-chart,ammonia-equilibrium}.png`. Relative paths in drafts intentionally match future topic publication, not work-file location.

Corrections to report: missing pressure dimensions in handwritten Henry units; incorrect inverse-coefficient wording; missing length in handwritten Sherwood relation; stripping pinch sets maximum L/G at fixed L; NTU depends on flow ratio through OL; K4 ratio is square of velocity fraction; ammonia data supply packed volume, not height. Using unrounded pressure data and converged curved-equilibrium quadrature gives NTU17.6229916, volume13.0098m³, rather than coarse-table19.355/14.2884m³ or rounded straight-line14.8201m³. Final notes present physical/model approximations without mentioning the source handout.

No consequential unresolved handwriting. Main limitations retained: dilute constant-flow at5% ammonia, effective reactive-solute equilibrium data, approximate gas-side control, empirical hydraulic chart, missing area for actual height. Independent review and final KaTeX/export/link checks remain root-owned.
