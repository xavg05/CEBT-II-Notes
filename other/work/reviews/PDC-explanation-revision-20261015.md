# PDC explanation revision: independent review, 15 October 2026

Reviewer: Codex review agent, independent of the revision author. Scope: the working-tree changes to all 22 canonical PDC drafts. This is a review of the explanatory revision, not a fresh audit of unchanged source equations or original figure crops.

## Findings

The changes improve causal understanding rather than adding generic summary paragraphs. They follow disturbances through physical storage and removal, distinguish gain from response speed, explain the purpose of baseline subtraction and normalisation, and interpret example numbers against their own endpoints. PDC-04 now supplies the missing bridge from the balance to standard form and from its coefficients to physical behaviour. The existing headings, equation tags and note format remain intact.

Two wording corrections were reported to the author and both were fixed and re-read:

1. **PDC-12, added first-peak explanation:** calling the overshoot the exponential envelope at that instant is imprecise. The full normalised transient envelope is `exp(-a t)/sqrt(1-zeta^2)`, whereas the first peak excess is `exp(-a t_p)` because the sine vanishes and the cosine is -1. At damping 0.5 these are 0.188255 and 0.163034 respectively. Explain the substitution at the peak, or call it the exponential decay factor.
2. **PDC-21, added outflow-slope explanation:** make “taking its reciprocal” explicitly refer to the outflow slope, not the preceding time constant. The gain is the inverse slope; the time constant is area divided by slope.

No new equation or numerical error was found. Other notable distinctions are correct: changing flow is a bilinear input–state effect while a prescribed new fixed flow still yields a linear lag; reacting concentration memory differs from fluid residence time; a cascade's initially flat response does not create a finite dead interval; a right-half-plane zero is not a growing mode; equilibrium endpoint agreement alone does not verify a nonlinear transient.

## Independent verification

New arguments were re-derived from the balances and product/Taylor rules, including outlet-flow cancellation in concentration balances, the gas-vessel cooling term, first-order storage/removal ratios, summed A/B conservation, boiler coefficient signs, local second-order reaction slope, gravity-outflow slope and equilibrium curvature, and the three-tank valve product terms.

Python was run with `other/work/tools/python/python.exe` using independent standard-library calculations. Results include:

| Check | Independent result |
|---|---|
| Heated-tank heat-capacity flow | 42000 W/K |
| Inert/reacting tank 95% times | 299.573227 s / 149.786614 s |
| Inert/reacting tank initial slopes | Both 0.0300 mol m^-3 s^-1 |
| Lag progress after two time constants | 86.4664717% |
| Damping 0.5: first peak, overshoot, same-side decay ratio | 36.2759873 s; 0.163033535; 0.0265799335 |
| Critical step at one time constant | 0.264241118 |
| Coupled A/B deviations after 100 s | 0.432332358 / 0.199788200 |
| Boiler B and feed-to-steam gain | 1836312.61 kJ/m^3; -0.0173880797 |
| Boiler matched feed/heat change | Inventory drift < 3e-19 m^3/s; extra steam 1 kg/s |
| Inverse-response initial slope / minimum | -2; -1/3 at 0.405465108 s |
| Local second-order reaction gain and time | 1/3; 33.3333333 s |
| Gravity tank linear / nonlinear level after 1000 s | 1.96432601 m / 2.13197861 m |
| Gravity-tank independent RK4 value substituted into implicit solution | Returns 1000.000000000014 s |
| Three-tank progress at one / three individual time constants | 8.03013971% / 57.6809919% |
| Three-tank linear / exact final composition | 4.34416% / 4.34262948% |

The independent RK4 check used a 0.1 s time step. Units and limiting cases of the added interpretations are consistent. Machine-readable numerical evidence is preserved in `PDC-explanation-revision-20261015-numbers.json` beside this review.

## Instruction changes and disposition

The revised CLAUDE.md explanation standard and PLAN.md section 6.3 were reviewed after they were written. They preserve the established seven-section style, provide reproducible causal and algebraic criteria, distinguish the scalar storage/removal interpretation from more general dynamics, and require per-topic interpretation rather than copying tank language. They explicitly retain equation labels, existing scope, provenance, cross-review and separate publication variants. The plan's per-unit criteria match the improvements present in the 22 drafts. No conflicting or incorrect instruction was identified.

Both wording findings are closed in the canonical drafts. The explanatory revision passes this independent scientific and instructional review. Publication, figure opening, maths rendering and portable-export checks remain the author's separate delivery checks; this record does not claim an Obsidian runtime inspection.
