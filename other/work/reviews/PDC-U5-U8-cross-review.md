# Independent cross-review: PDC-U5–U8 (PDC-13–22)

Reviewer: independent Codex review agent, 12 October 2026.

Status: **passed; no required scientific corrections**. Notes and shared board were not edited.

## Scope and method

Read AGENTS.md, CLAUDE.md and relevant PLAN.md units. Opened and read every canonical draft PDC-13–22. Visually inspected chapter 2 pages 16–32 through page images/montages and all five linked figure crops. Independently reconstructed the balance equations, transform algebra and limiting behaviour; reran every numerical example with Python standard-library calculations. Results are preserved in `PDC-U5-U8-independent-numbers.json`. Checked that equation tags are consecutive 43–71, figure filenames exist in the delivery figures folder, and the notes contain no lecture/slide/lecturer references or wikilinks.

This review checks science, content and figure legibility; final publication link resolution and KaTeX/portable-export rendering belong to the publishing validation.

## Findings by unit

- **U5 / PDC-13–14:** pipe transit, equal-lag partial fractions, causal shift, signed superposition and signal duplication are correct. Geometry gives 25.132741 s rather than the rounded 25 s source value; the note clearly retains that precision. The 125 s response is 0.263752790 K. The heater/feed cancellation respects compatible units and identical lag paths.
- **U6 / PDC-15–16:** coupled irreversible CSTR equations and row/column convention are correct; reaction cancels in the total-species balance. At 100 s the A/B deviations are 0.432332358/0.199788200. Boiler mass/internal-energy storage and stream enthalpies correctly eliminate steam flow. Recomputed B = 1836312.61 kJ m^-3 and all four coefficients match; simultaneous heat compensation gives zero inventory drift and one unit steam-flow increase. Fixed pressure, coexistence of phases, integrator and algebraic feedthrough limitations are explicit. Conversion of heat-column coefficients from kW to W is correct.
- **U7 / PDC-17–19:** repeated-pole inversion, conjugate residues, BIBO versus free-response stability, cancellation caution and properness are sound. Independently multiplied the degree-six factors and recombined the claimed impulse transform at five real/complex points; all passed. The inverse-response minimum is at 0.405465108 s with output -1/3. The final-value theorem conditions correctly inspect the output transform, and the worked endpoint is 0.2. The unstable counterexample correctly rejects an otherwise finite G(0).
- **U8 / PDC-20–22:** Taylor terms, second-order reaction derivative, tank restoring coefficient and transformed-state output linearisation are correct. The tank implicit integral matches independent bisection and direct RK4 integration: nonlinear h(1000) = 2.131978614 m versus linear 1.964326007 m. Mixer baseline 3.96 volume percent is the exact balanced value and must be retained rather than silently replaced with rounded 4 percent. Percentage-point valve convention gives K_v = 0.038416 and K_B = 0.98. Triple-lag partial fractions and all reported final/transient values pass.

## Figures

Opened PDC-13-pipe-and-tanks, PDC-16-boiler, PDC-17-pole-map, PDC-21-linear-and-nonlinear-level and PDC-22-three-tank-mixer. All crops are readable and relevant; no equation fragments are mistaken for figures. The repeated -1 pole is explicitly explained because it overlays on the pole map. The nonlinear tank chart is correctly described as qualitative; numerical precision comes from balances, not graph extraction.

## External consultation and independence

The author reports reading these APMonitor/BYU Dynamics and Control resources. This reviewer independently opened/read their relevant sections too:

- [Transfer Functions](https://apmonitor.com/pdc/index.php/Main/TransferFunctions): transform assumptions, series and parallel combination, endpoint interpretation.
- [State Space Models](https://apmonitor.com/pdc/index.php/Main/StateSpaceModel): input/output matrix dimensions and direct feedthrough.
- [Controller Stability Analysis](https://apmonitor.com/pdc/index.php/Main/StabilityAnalysis): denominator-root stability and final-value limitations. Its broad cancellation statement was not accepted as internal-stability evidence; PDC-17–18 correctly give the stronger warning.
- [Model Linearization](https://apmonitor.com/pdc/index.php/Main/ModelLinearization): equilibrium Taylor expansion and local validity.

Notes use independently developed physical explanations and derivations; no external worked example is copied. Supplemental pages contain some notation typos, but the notes use the correctly re-derived expressions. Michigan CTMS pages reported inaccessible by the author are not treated as used sources. Author consultation record is `other/work/progress/PDC-chapters1-2.md`.
