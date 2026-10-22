# RE-U2 independent cross-review — 22 October 2026

Reviewer: codex. Original author and note owner: claude. Scope: RE-07–12, source section 2, all six canonical drafts and both publication editions. The initial review of commit 1958ec0 was read-only. Xavier's follow-up explicitly authorised Codex to correct these Claude-owned canonical drafts and close the review. Those corrections and the final evidence are recorded below. No source PDF or historical snapshot was changed.

## Verdict

**Final verdict: PASS.** The three original findings, the recommended heat–mass-transfer clarification, the pressure convention and one additional rounding issue are corrected in the canonical inputs and both editions. Equations 21–37 were re-derived, all 14 source pages rechecked visually, and all ten figures opened individually. The author verification script and 50 independent checks pass. RE-U2 and its independent cross-review row are now **reviewed** on BOARD.

## Original findings and correction rationale — now closed

### 1. RE-08: twice the initial slope applies to normalised time

Location: `RE-08 - Reaction-controlled shrinking particles.md`, Motivation and explanation, paragraph below the conversion figure; reading edition line 80.

The paragraph correctly explains that each curve uses its own completion time, but then displays the dimensional derivative and says it starts at twice the film-controlled slope. The dimensional initial slopes are `3/tau_rxn` and `1.5/tau_film`, whose ratio is `2 tau_film/tau_rxn`. The factor of two is guaranteed only for derivatives with respect to each curve's own dimensionless time. For example, completion times of 100 s and 10 s give reaction and film initial slopes 0.03 and 0.15 per second, respectively: the ratio is 0.2, not two.

Replace the final sentence of that paragraph with:

> The reaction-controlled curve rises faster initially against its own normalised time because a constant receding speed removes the large outer shell first. The initial dimensionless slopes `dX/d(t/tau_c)` are 3 for reaction control and 1.5 for film control. Their dimensional slopes are `3/tau_rxn` and `1.5/tau_film`, so their ratio also depends on the separate completion times.

Use ordinary native maths delimiters when integrating this text. No equation or numerical-result correction is needed.

### 2. RE-10: changing geometry requires more than changing exponents

Location: `RE-10 - Shrinking-core regimes and combined resistances.md`, final paragraph of Motivation and explanation; reading edition line 96.

The opening statement suggests the plate and cylinder results follow by changing the spherical `2/3` and `1/3` exponents. This works for the simple reaction-front geometry relation but not generally for product-layer diffusion. A cylindrical shell obeys `r dC/dr = constant`, giving logarithmic shell resistance. For a long cylinder with negligible end effects, integration yields

$$
\frac{t}{\tau_{\mathrm{cylinder}}}=X+(1-X)\ln(1-X),
$$

with the product interpreted by its limiting value at complete conversion. It cannot be obtained just by replacing the exponents in the spherical diffusion expression. A slab instead gives a quadratic layer-growth relation.

Minimal replacement for the opening sentence:

> The same balance method can be repeated for flat plates and cylinders, but the area and diffusion resistance must be re-derived for each geometry. The spherical formulas cannot generally be transferred by changing their exponents alone; cylindrical product-layer diffusion introduces a logarithm.

This is an overstatement added in the note, rather than an error in the source's instruction to derive other geometries separately. The independent Python check integrates the cylindrical resistance and verifies the logarithmic expression at three conversions.

### 3. RE-12: individual complete conversion is not a universal reactor requirement

Location: `RE-12 - Reactors for solid reagents.md`, first sentence of Overview and first sentence of Conclusion; reading edition lines 10 and 72.

Both passages say the reactor must give **every** particle at least its complete-reaction time. That is the condition for complete conversion of every identical particle under the model, not a requirement for a specified average conversion. It conflicts with this note's valid 99% plug-flow designs, which all use less than the complete-reaction time, and with its exponential-RTD model, which retains a nonzero fraction of early departures at every finite mean time.

Suggested Overview opening:

> Complete conversion of an individual particle under fixed conditions requires contact lasting at least its complete-reaction time. Reactor design instead starts from the required average conversion and the solid residence-time distribution, together with reagent supply and heat transfer.

Suggested Conclusion opening:

> Choose the contact time and solid residence-time distribution to meet the required average conversion. Complete conversion of every identical particle requires no departures before the complete-reaction time; narrow distributions achieve high average conversion with less holdup.

Retain the existing correct RTD integral, coefficients and 99% comparisons.

## Additional heat–mass-transfer clarification — now applied

RE-11 Motivation says both transfer coefficients scale with `1/d`. That is exact for constant `Sh = Nu = 2`; with forced-convection correlations they scale as `[2 + a sqrt(Re)]/d`. The intended cancellation concerns the **ratio** of the coefficients under the adopted `Sh approximately Nu` approximation. If the distinct Schmidt and Prandtl corrections are retained, their ratio has a weak Reynolds-number dependence and the surface temperature need not be exactly size independent. The note already introduces the heat–mass analogy as an approximation, so its main result is valid within that approximation. Tightening the explanatory sentence would make its limits clearer.

## Source coverage and per-note checks

All 14 original pages were visually read using the existing page renders; pages 8 and 11 were additionally opened individually for the dense spherical-shell and evaporation equations. All ten cropped figures were opened in a labelled review montage and checked against the source: shrinking particle, particle conversion, shrinking-core sequence and profile, core conversion, and the five reactor arrangements. No missing substantive source subtopic was identified.

| Note | Source | Independent finding |
|---|---|---|
| RE-07 | pp1–4 | Stoichiometric film supply and moving boundary give the stated radius-squared law and time. Units and size scaling pass. The gas/solid concentration ratio is consistent with air at one atmosphere; explicitly stating that pressure would improve the illustrative estimate. |
| RE-08 | pp4–5 | Extent-based surface rate, reaction lifetime and integrated film-plus-reaction time pass, including non-unit stoichiometry. Correct the normalised-versus-dimensional slope statement. |
| RE-09 | pp6–9 | Core/surface boundary values, conserved inward shell flow, sign, factor six, conversion relation and early-time square-root behaviour pass. Singular initial-rate and sharp-front limitations are explained. |
| RE-10 | pp9–10 | Fixed-radius film time, combined local resistances, integrated additivity and the layer/reaction crossing pass. Correct the geometry transfer statement. |
| RE-11 | pp11–12 | Liquid balance, latent-heat demand, conductivity/diffusivity units and Clausius–Clapeyron closure pass within the stated dry-gas, dilute, quasi-steady heat–mass-analogy model. Suggested qualification of coefficient size scaling above. |
| RE-12 | pp12–14 | All five equipment types are covered. Segregated RTD averaging, plug-flow limit and mixed-solids asymptotes pass. Correct the universal full-conversion requirement in Overview and Conclusion. |

The source's conductivity-symbol correction on p12 is sensible: the coefficient multiplying the temperature difference is gas thermal conductivity. Figures and equations do not refer readers back to the lecturer, slides or source PDF.

## Independent verification evidence

`other/work/scripts/crossreview_re_u2.py` was written independently of the author's SymPy/SciPy script. Its final 50 checks use pure-Python quadrature, root solving, boundary values and conservation, including all calculated values stated in prose, their displayed rounding, normalised slopes and the plug-flow times. Results are in `RE-U2-cross-review-numbers-20261022.json`. Empirical inputs and correlation validity ranges are identified as inputs rather than represented as derived observations.

- Numerical integration of the combined moving-boundary resistance balance gives **2100.0150991148093 s**, agreeing with the integrated sum of the three limiting contributions.
- Product-layer and reaction curves cross at normalised time **0.5**, conversion **0.875**. The early-time layer expansion is consistent with `t/tau = X^2/3`.
- The droplet model gives **289.3529300609058 K** (**16.202930060905828 degrees C**) and an evaporation-rate ratio **0.16491705399990297** against the same-property gas-temperature estimate.
- Direct integration in core-radius coordinates gives the mixed-solids 99% mean times **49.66610812851698**, **24.79973210764684** and **19.77346881946236** times the respective completion times. The large-mean survival coefficients are **0.5**, **0.25** and **0.2**.
- All six canonical bodies exactly match the native publication bodies. Reading/native full text agrees after mathematical-format conversion. All **108** relative links across these twelve note copies resolve; all **20** image references/files across the two editions decode, representing ten distinct figures. Labels **21–37** are correct and continuous.
- After correction and republication, the all-RE KaTeX checker parses **1125** native expressions with no failure and confirms mathematical parity across both editions. The inline-maths guard passes across **680** current publication/canonical files.
- Original source SHA-256: `a164aa88e59221e17ec581a81ab95117909b8c55f1171b2e2a2ad9ccc134c5f7`, unchanged. No live Obsidian or GitHub runtime check is claimed. A fresh run of `publish_re_all.py` independently relocates the current RE export and validates its links and figures successfully.

## Sources actually opened

- The supplied 14-page section-2 PDF, read visually as described above.
- [NPTEL/IIT Bombay problem set 10, Q10.3](https://archive.nptel.ac.in/content/storage2/courses/103101001/downloads/Problems/ProblemSet_10/ProblemSet_10.html): same-size shrinking-core particles under reaction control, excess gas and mixed-solid residence times. Used to check the assumptions of the solids RTD application, not as a copied derivation.
- [NISTIR 6783, section 6.5, PDF p27](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir6783.pdf#page=27): paired Sherwood/Nusselt correlations, water/air Schmidt and Prandtl values, saturation and droplet energy coupling. Opened the relevant PDF page visually. Conservation signs were independently derived rather than copied from extracted text.
- [Xu, Sun and Khaleel, original paper abstract](https://arxiv.org/abs/1808.01029): quasi-static product-layer diffusion is an assumption of the standard model, with restricted validity. Only the abstract was used; this is not represented as a full-paper read.

The IslandScholar cylindrical-model paper returned 403, and the CFDEM raw PDF endpoint was unsupported by the browser. Neither inaccessible text was used. The cylindrical correction follows the independent shell-balance derivation and quadrature above.

## Authorised correction log and final closure

| File | Applied change | Reason |
|---|---|---|
| RE-07 | State one atmosphere for the illustrative carbon/oxygen density ratio. | Its numerical oxygen concentration needs an explicit pressure. |
| RE-08 | Give initial dimensionless slopes 3 and 1.5, then distinguish the dimensional slopes using their separate completion times. | Closes finding 1 without changing either limiting equation. |
| RE-10 | Require geometry-specific area and resistance derivations; explicitly mention the cylindrical logarithm. | Closes finding 2; no incorrect transfer by exponent substitution remains. |
| RE-11 | Qualify size independence in Overview, Intuition, Motivation and Conclusion; explain cancellation of the coefficient ratio and the special stagnant-gas inverse-diameter limit. | Applies the recommended clarification consistently through the note. |
| RE-12 | Make the design requirement a target average conversion; reserve the no-early-exit condition for complete conversion of every identical particle. | Closes finding 3 consistently in Overview and Conclusion. |
| RE-12 | Report the three 99% plug-flow times as approximately 0.990, 0.785 and 0.881 times the corresponding completion times. | Fresh prose-number checking found that 0.7845565 rounded through 0.785 could produce the old 0.79 by double rounding. Direct consistent three-decimal reporting removes that issue. |
| RE publisher | Change the topic-02 status string to completed independent cross-review and use the Windows extended-path interface for relocation. | Rebuilding retains the closed review status and tests descriptive long filenames successfully. |

Only `publish_re_all.py` was used. Equations throughout RE remain labels **1–110**, with **21–37** belonging to this unit; no in-text references require remapping. Five canonical files changed, with RE-09 requiring no correction. Both publication formats were regenerated from the corrected canonical text.

### Equation-by-equation independent derivation record

| Label | Re-derived balance or mathematical step | Units/limit check |
|---|---|---|
| 21 | Film flux is coefficient times bulk-minus-surface concentration; integrate over the current sphere area. | Molar flow; zero concentration difference gives zero supply. |
| 22 | Differentiate solid inventory `4 pi rho_m r^3/3`, equate consumption to `nu_A/nu_B` times fluid supply and cancel current area. | Receding speed has length/time units and negative sign. |
| 23 | Insert `k_g=D/r`, integrate `-r dr` from initial radius to zero, retaining the stoichiometric ratio. | Completion time scales as radius squared divided by diffusivity, multiplied by the concentration ratio. |
| 24 | Divide the integrated radius-squared law by the completion time and convert the remaining volume fraction into conversion. | Initial radius and conversion are recovered; final conversion is one. |
| 25 | Multiply the extent rate per area by `nu_A`, use bulk concentration in the fast-film limit and balance shrinking inventory. | Constant negative radial speed; no extra `nu_B` is appropriate for extent-based kinetics. |
| 26 | Integrate constant radial speed, set zero radius to define completion time, then cube the radius fraction. | Reaction completion time is proportional to initial radius. |
| 27 | Eliminate surface concentration between film delivery and first-order surface consumption; integrate the sum of local resistances. | Each isolated-resistance limit is recovered; full completion times add. |
| 28 | Integrate steady spherical diffusion twice to `a/r+b`, then impose zero core concentration and bulk concentration at the exterior. | Both boundary values and nonnegative intervening concentration pass. |
| 29 | Differentiate the profile and multiply by `4 pi r^2 D_e`. | Same inward molar flow at every shell radius; spherical-shell resistance is positive. |
| 30 | Balance core inventory against the incoming molar flow; integrate `r_c^2/R-r_c`, evaluate at initial radius and normalise. | Factor six, radius-squared lifetime, zero initial time and complete-conversion endpoint pass. |
| 31 | Repeat the extent-based surface-consumption balance at the receding core with negligible transport resistance. | Core recedes linearly; fixed exterior size does not alter its reaction-controlled radius law. |
| 32 | Use fixed exterior area in the film supply; divide constant molar consumption by initial solid inventory. | Conversion is linear until completion; lifetime has time units. |
| 33 | Add film, spherical-layer and core-reaction local concentration drops at the same molar flow, then integrate the moving boundary. | Independently integrating the local balance gives 2100.0150991148093 s at the test conversion, agreeing with the three integrated contributions. |
| 34 | Balance the loss of liquid inventory against outward vapour delivery from the saturated interface. | Negative shrinking speed; zero vapour driving force gives zero evaporation. |
| 35 | Equate positive latent-heat demand to gas-side heat supply and use the explicitly adopted equal-Sh/Nu coefficient ratio. | Both sides have power/length units; the surface is cooler than the dry bulk gas. |
| 36 | Integrate `d ln(P_sat)/dT = DeltaH_vap/(R T^2)` at constant vaporisation enthalpy. | Pressure ratio is dimensionless and becomes one at equal temperatures. |
| 37 | Weight each identical particle's surviving fraction by its exit-age density; completed particles contribute zero beyond completion time. | Dimensionless average; delta and exponential RTD limits reproduce the plug- and mixed-solid results. |

The author's `verify_re_s2.py` was rerun successfully using `RE_PYLIB=other/work/scratch/re-s2/pylib` and the portable Python 3.13.7 interpreter. Local scratch dependencies: SymPy 1.14.0, NumPy 2.5.4, SciPy 1.18.1 and mpmath 1.3.0. No dependency files are committed. The symbolic identities, SciPy root/integration checks and the independent 50-check calculation all pass. The unchanged author output is `other/work/progress/re-s2-verification.json`.

Final whole-RE publisher results: **27 notes**, **110** strictly increasing labels from 1 through 110, **241 links** and **20 image references** per edition, and **portable relocation PASS**. The topic README now records completed review. No open RE-U2 scientific, numerical, figure, reference or publication finding remains.
