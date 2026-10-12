# SEP-U2: Drying of solids

Owner codex; date 12 October 2026. Author verification complete; independent scientific review pending. Publication and final numbers controlled by coordinator.

## Reading and coverage

- All 34 original colour page images read individually before drafting, overview batches PDF 1–20 and 21–34.
- Transcription and page-to-note traceability: other/work/ocr/Separations II/U2.md.
- Eleven short notes under other/work/drafts/Separations II/U2/, source order:
  1. equipment/wet solids (p1–2);
  2. humidity and chart conventions (p3–7);
  3. humid enthalpy/adiabatic saturation (p8–11);
  4. dew point (p12);
  5. wet bulb/transfer analogy (p13–19);
  6. moisture and periods (p20–24);
  7. countercurrent operating line/minimum gas (p25–27);
  8. analytical times (p27–29);
  9. cocurrent arrangement (p29);
  10. graphical integration (p30–31);
  11. other solvents/nonadiabatic (p32–34).
- Boundary pages shared only where they contain several distinct topics. No source pages omitted.

## Validation and corrections

other/work/scratch/separations/U2/verify.py and numerical-validation.json: all numerical examples computed in Python, including chart-based input calculations, separate saturation/enthalpy checks, positive residence-time integrals, exact transition, co-/countercurrent endpoint checks and quadrature convergence.

Cloth example: minimum gas 66.6667 kg/kg; actual 80; wc=.212; wet branch 13.34165 h; falling 1.50283 h; total 14.84449 h; gas outlet H=.0136. The additional cocurrent model has crossing w=.02 below target and remains fully wet through target, total 14.33408 h. All-constant ideal co-/countercurrent integrals coincide given identical gas endpoints; local driving force does not stay constant.

Corrections are kept distinct from literal transcription:

- H/H* is percentage saturation; conventional relative humidity uses partial pressures.
- Humid heat varies with H; exact energy balance stated before dilute constant-s slope shortcut.
- p22 dry carrier density, not vapour density.
- p23 handwritten latent-heat division at top wrong; lower filled equation correct.
- p25 blanket constant local driving force false; clarified with p29 and original integral.
- p31 printed integration sign corrected to positive reciprocal-rate area.
- p30 supplied rate graph stops w=.5, cannot complete source w=.9 path from that figure alone; numerical graph-method example explicitly generated from separate analytical model.

Root independently blind-read original p5,p23,p27,p31; readings and dimensional/balance resolution recorded in transcription.

## Figures

Ten source scan crops under notes/Separations II/figs/u2-*.png; every crop visually opened after extraction. Original scan coordinate scaling retained in verification script. All links use ../figs/ ready for topic-folder publication; draft work-tree itself intentionally has no duplicate figures.

## Sources actually opened

- [ASHRAE Handbook: Psychrometrics, SI](https://handbook.ashrae.org/Handbooks/F25/SI/F25_Ch01/F25_Ch01_si.aspx): ideal-gas definitions, distinct percentage-saturation/RH measures, moist-air enthalpy, adiabatic-saturation and dew-point constraints. Actual source read; no copied prose.
- [NPTEL drying introduction](https://archive.nptel.ac.in/content/storage2/courses/103103027/module4/lec1/1.html): independent discussion of material/gas/equipment dependence and limits of raising surface-transfer demand.
- [NPTEL drying mechanisms](https://archive.nptel.ac.in/content/storage2/courses/103103027/module4/lec1/2.html): free/bound/unbound/equilibrium moisture terminology and internal transport modes.
- [NPTEL dryer design notes](https://archive.nptel.ac.in/content/storage2/courses/103103027/pdf/mod4.pdf): equipment classification and conserved-basis material/energy balances. Its own direct/indirect description has a wording typo; adopted definitions independently follow the primary handout and energy boundary.

Scope qualification: the supplied nonadiabatic section only states additional modelling requirements, without full equations/example. Final note adds a clearly assumed lumped energy model and a specified conceptual calculation; not presented as a fully specified industrial design.
