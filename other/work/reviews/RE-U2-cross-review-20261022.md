# RE-U2 independent cross-review — 22 October 2026

Reviewer: codex. Author and note owner: claude. Scope: RE-07–12, source section 2, all six canonical drafts and both publication editions. Reviewed commit 1958ec0 and the current corrected files. No Claude-owned study note or source PDF was edited.

## Verdict

**Review complete; three corrections required before RE-U2 can be marked reviewed.** The principal equations, source coverage and calculated results pass. The three findings concern statements that overgeneralise otherwise correct results. The BOARD unit remains **written**, with this report linked for owner correction. One additional low-priority clarification is recommended below.

## Required corrections

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

## Recommended clarification, not an additional blocking finding

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

`other/work/scripts/crossreview_re_u2.py` was written independently of the author's SymPy/SciPy script. Its 42 checks use pure-Python quadrature, root solving, boundary values and conservation. Results are in `RE-U2-cross-review-numbers-20261022.json`.

- Numerical integration of the combined moving-boundary resistance balance gives **2100.0150991148093 s**, agreeing with the integrated sum of the three limiting contributions.
- Product-layer and reaction curves cross at normalised time **0.5**, conversion **0.875**. The early-time layer expansion is consistent with `t/tau = X^2/3`.
- The droplet model gives **289.3529300609058 K** (**16.202930060905828 degrees C**) and an evaporation-rate ratio **0.16491705399990297** against the same-property gas-temperature estimate.
- Direct integration in core-radius coordinates gives the mixed-solids 99% mean times **49.66610812851698**, **24.79973210764684** and **19.77346881946236** times the respective completion times. The large-mean survival coefficients are **0.5**, **0.25** and **0.2**.
- All six canonical bodies exactly match the native publication bodies. Reading/native full text agrees after mathematical-format conversion. All **108** relative links across these twelve note copies resolve; all **20** image references/files across the two editions decode, representing ten distinct figures. Labels **21–37** are correct and continuous.
- The existing independent all-RE KaTeX checker parses **1125** native expressions with no failure and confirms mathematical parity across both editions. The inline-maths guard passes across **680** current publication/canonical files.
- Original source SHA-256: `a164aa88e59221e17ec581a81ab95117909b8c55f1171b2e2a2ad9ccc134c5f7`. The review does not modify it. No live Obsidian or GitHub runtime check is claimed; portable relocation from the author's relabelling run is historical author evidence, not a fresh independent run here.

## Sources actually opened

- The supplied 14-page section-2 PDF, read visually as described above.
- [NPTEL/IIT Bombay problem set 10, Q10.3](https://archive.nptel.ac.in/content/storage2/courses/103101001/downloads/Problems/ProblemSet_10/ProblemSet_10.html): same-size shrinking-core particles under reaction control, excess gas and mixed-solid residence times. Used to check the assumptions of the solids RTD application, not as a copied derivation.
- [NISTIR 6783, section 6.5, PDF p27](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir6783.pdf#page=27): paired Sherwood/Nusselt correlations, water/air Schmidt and Prandtl values, saturation and droplet energy coupling. Opened the relevant PDF page visually. Conservation signs were independently derived rather than copied from extracted text.
- [Xu, Sun and Khaleel, original paper abstract](https://arxiv.org/abs/1808.01029): quasi-static product-layer diffusion is an assumption of the standard model, with restricted validity. Only the abstract was used; this is not represented as a full-paper read.

The IslandScholar cylindrical-model paper returned 403, and the CFDEM raw PDF endpoint was unsupported by the browser. Neither inaccessible text was used. The cylindrical correction follows the independent shell-balance derivation and quadrature above.

## Owner closure checklist

Apply the three required corrections to canonical drafts and regenerate both editions, preserving equation labels. Optionally tighten RE-11 and state the pressure in RE-07's illustrative density ratio. Recheck the changed sentences and edition parity; then Codex can verify closure and change the main RE-U2 row to reviewed. Until then its author-verified written status remains accurate.
