# Independent cross-review: Process Dynamics and Control U1–U4

Reviewer: Codex review agent, independently assigned by the author. Date: 12 October 2026.

Scope: canonical drafts PDC-01–12 in `other/work/drafts/Process Dynamics and Control/`; Ch1 PDF pages 1–10 and Ch2 pages 1–15 visually inspected through existing rendered montages. Read CLAUDE.md, AGENTS.md, relevant PLAN.md entries and ownership board. No canonical note or board edits made.

## Decision

**Scientific review passed. No blocking scientific or numerical errors found.** Publisher rendering and portable export validation remain the author’s responsibility; this review does not claim an Obsidian runtime check.

## Re-derivation and validity checks

- PDC-01: sensible-energy balance and target heating demand are consistent with fixed liquid holdup and equal flow. Feedforward cancellation is exact only under the explicitly stated model, fixed target and instantaneous heating. Feedback/regulator/servo distinctions are correct.
- PDC-02: reflux-drum accumulation has the correct signs. All five measurement–valve pairings agree with the figure. Inferential temperature measurement is correctly qualified by composition and pressure sensitivity.
- PDC-03: expanding the extensive solute and sensible-energy storage and substituting the volume balance correctly cancels direct outlet terms. Reaction heating uses the correct exothermic sign. Coolant closure and avoidance of double-counting reaction enthalpy are correct.
- PDC-04–05: inert and reacting tank balances, integrating-factor step solution, reacting gain and pole, changing-volume product rule, volume history and finite-pulse jump balances all re-derived. The concentration cancellation for proportional withdrawal is physically consistent, including the no-feed/no-reaction limit.
- PDC-06: thermal capacitance divided by conductance gives the sensor time constant with seconds as its units. Heater-to-temperature and feed-temperature transfer functions have the same pole and correctly different dimensional gains.
- PDC-07: mass balance plus enthalpy discharge gives m dT/dm = (gamma−1)T, hence temperature and pressure power laws. Absolute temperature, constant heat capacities, fixed volume and consistent internal-energy/enthalpy reference shifts are correctly handled. The distinction between a state relation and a time history is clear.
- PDC-08: subtracting the actual steady operating state gives the perturbation ODE. Laplace initial-value term is retained with its correct coefficient, then removed only to define zero-state transfer function. Other inputs are held at zero for individual MIMO elements.
- PDC-09–10: step partial fractions, impulse-area units and resulting output jump, exact fractional settling time, integrator level ramp and pipe time-shift transformation all checked. BIBO versus zero-input stability of the integrator is distinguished correctly.
- PDC-11: eliminating the two tank states produces the stated characteristic polynomial; natural frequency, damping ratio and quadratic roots are correct. Positive passive lags imply zeta >= 1. Negative damping and undamped BIBO instability are correctly identified.
- PDC-12: distinct-root solution satisfies r(0)=r_dot(0)=0; repeated-root solution has the required polynomial factor. Differentiating the underdamped solution gives the stated sine expression; first peak and full-period same-side envelope decay reproduce overshoot and decay ratio. Negative-gain use of magnitudes and restrictions to constant numerator/no zeros are sound.

All time constants and pole units, gain dimensions, extensive balances, relevant zero-reaction/no-input limits and stated model restrictions were checked. Equations tagged continuously 1–42 across these notes.

## Numerical verification

Every numerical example independently recomputed using Python math expressions, without reusing the author’s verification outputs. Results saved in `PDC-U1-U4-independent-numbers.json` alongside this review. All printed values agree at their stated rounding. Examples include heating duties 1.260/1.470 MW; pulse concentration 2.727272727 mol m^-3; gas discharge temperature 227.357484977 K; pipe delay 25.132741229 s; second-order peak time 36.275987285 s, overshoot 0.163033535 and decay ratio 0.0265799335.

## Figure and prose checks

Opened all five linked source crops: PDC-01 heated-tank feedback, PDC-02 distillation loops, PDC-03 cooled CSTR, PDC-11 damping regimes and PDC-12 overshoot/period. Labels, controller pairings, axes and peak definitions agree with the notes, and crops are readable. Subject figure targets exist. Relative links are intended for published topic folders, not the draft staging directory; validate final placement when publishing.

All twelve files include the required seven sections. No lecture/PDF/lecturer references, wikilinks or callouts appear. Prose stands independently of the source, and missing CSTR variable assignments and reference-energy reasoning are supplied rather than left blank. External-source retrieval provenance is outside this review’s scope and must remain documented by the author.

## Nonblocking improvement

PDC-06, before Eq. (18): state the heated-liquid assumptions explicitly in that note: perfect mixing, constant liquid properties, no reaction, negligible environmental heat loss and mixer work. Its physical model and formulas are correct, and the later explanation mentions insulation/heat loss, but placing the assumptions beside the balance better meets CLAUDE.md’s standalone requirement.

Optional editorial only: the PDC-09 worked example could label gain as output units per input unit and unit impulse area as one input-unit-second, making its already-correct impulse units especially explicit.

## Author resolution

12 October 2026: explicit heated-tank assumptions added before Eq. (18) in PDC-06 and republished. Both independent scientific reviews now pass; rendering and portability checks are recorded in the production record.
