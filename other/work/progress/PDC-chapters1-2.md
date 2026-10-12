# Process Dynamics and Control: chapters 1–2 production record

12 October 2026. Author: Codex. PDC-U1–U8 written and independently cross-reviewed. Deliverables: 22 short notes in eight chronological topic folders, 71 continuous equation labels, ten visually checked PDF figure crops, topic/subject navigation and the native Obsidian mirror. Short notes remain separate; no complete-section merge was requested. PLAN.md and CLAUDE.md were not changed.

## Source scan and coverage

Both original PDFs remain unchanged in `other/sources/Process Dynamics and Control/`. All 42 pages were rendered and visually scanned, including text, equations, diagrams and exercise spaces. Text extraction was used for locating content, not as an equation authority. Overview montages and individual pages are retained locally in `other/work/scratch/pdc/`; crop coordinates are recorded in `crops.json` there.

| Unit | Source PDF indices | Final notes and scope |
|---|---|---|
| PDC-U1 | Ch1 p1–10 | PDC-01 control objectives/feedback/feedforward; PDC-02 distillation loop interpretation; PDC-03 CSTR variables and model closure |
| PDC-U2 | Ch2 p1–5 | PDC-04 inert/reacting tank lags; PDC-05 variable volume and finite pulse; PDC-06 thermocouple/heated liquid; PDC-07 gas discharge and reference energy |
| PDC-U3 | Ch2 p5–11 | PDC-08 deviation variables/zero-state transfer functions; PDC-09 steps/impulses; PDC-10 integrators/dead time |
| PDC-U4 | Ch2 p11–15 | PDC-11 standard second order and pole regimes; PDC-12 full step derivation, overshoot, period and decay ratio |
| PDC-U5 | Ch2 p16–19 | PDC-13 pipe/two-tank series model; PDC-14 summation, subtraction and signal duplication |
| PDC-U6 | Ch2 p20–23 | PDC-15 MIMO convention and A→B CSTR; PDC-16 boiler mass–energy matrix |
| PDC-U7 | Ch2 p23–27 | PDC-17 poles/repeated/complex modes and degree-six example; PDC-18 zeros/properness/inverse response; PDC-19 final-value theorem/gain |
| PDC-U8 | Ch2 p27–32 | PDC-20 Taylor linearisation and reaction order; PDC-21 draining tank, transformed state and implicit exact solution; PDC-22 three-tank mixer and valve response |

Shared boundary pages introduce the next topic without duplicating explanations. Chapter 1's course administration and book list are omitted from study notes. The basic thermostat mechanism is included with feedback intuition. The available chapters cover introduction and process dynamics; chapter 1 lists later feedback-controller, advanced-control and plant-design sections, but their PDFs are absent. PDC-U9–U11 remain unclaimed and awaiting source. This delivery does not claim complete course coverage.

## Blank spaces and initiative

- Ch1 p8: the empty variable-identification table is replaced by an explicit, qualified CSTR assignment with input/output/state distinctions, plausible measurements and coolant model closure. The assignment states its assumptions rather than claiming a universal measured/unmeasured answer.
- Ch2 p1–2: the mixed-tank and reacting-tank solutions include the integrating-factor derivation and physical gain/time-constant interpretation.
- Ch2 p5: gas-vessel energy-reference questions are answered using consistent offsets in internal energy and enthalpy.
- Ch2 p11–15: the two-tank elimination and second-order step/overshoot/decay exercises are derived, including initial conditions.
- Ch2 p17: series order, delay and inverse transform questions receive qualified explanations and the causal shifted response.
- Ch2 p30: the local level gain, transformed-state exercise and implicit exact nonlinear solution are completed and numerically compared.
- Added numerical examples supply concrete checks where only a conceptual model was given. Added inverse-response example shows why zeros matter; it is not copied from an external source.

## Corrections and qualifications

1. Second-order time scale τ is not the oscillation period. Natural angular frequency is 1/τ; the undamped period is 2πτ.
2. An ideal integrator is not BIBO or asymptotically stable, but its zero-input state is neutral rather than exponentially growing. Undamped oscillators also fail BIBO stability. These distinctions prevent conflating several uses of “unstable”.
3. Zero initial state deviations do not require a step input or its derivative to remain zero at 0+. The initial-state transform contribution is displayed before defining the zero-state transfer function.
4. Rational physical input–output models can be proper with equal numerator/denominator degrees and direct feedthrough. The blanket strict-properness claim would exclude the ideal boiler steam-flow row.
5. Pole–zero cancellation does not establish internal stability. Zeros can hide modes from a particular input/output path; their effects on transient weighting and inverse response are explained.
6. The final-value theorem requires settling/nondecaying-mode checks on the complete output transform. A finite G(0) alone is insufficient.
7. Boiler coefficient recomputation gives feed-to-steam coefficient −0.0173881, consistently rounded to −0.0174, rather than the inconsistent −0.0176 diagram label. Heat-column units are explicitly kW versus W.
8. Pipe geometry gives 25.132741 s transit; the notes retain this instead of the coarsely rounded 25 s value.
9. The three-tank specified flows and 2% dilute feed balance at 3.96%, rather than exactly 4%. Retaining that equilibrium gives valve gain 0.038416 and exact cancellation of the steady term. Percentage points and volume-percent/fraction conventions are distinguished.
10. PDC-06's heated-liquid assumptions were made explicit beside the balance following independent review.

## External sources actually opened and read

All explanations and examples are independently written and balances are re-derived. These BYU/APMonitor teaching resources were consulted for supplementary framing and checks, not treated as flawless equation authorities. Only relevant explanations within each topic were used; some web equations have typos, so results were checked against the physical balances and independent mathematics.

| Source | Use |
|---|---|
| [Dynamic Model Introduction](https://apmonitor.com/pdc/index.php/Main/DynamicModeling) | U1 boundaries, states, input categories and constitutive closure |
| [Process Control Introduction](https://apmonitor.com/pdc/index.php/Main/FeedbackControl) | U1 sensors, actuators, feedback and information-flow interpretation |
| [Feedforward Control](https://apmonitor.com/pdc/index.php/Main/FeedforwardControl) | U1/U5 disturbance compensation and model dependence |
| [Balance Equations](https://apmonitor.com/pdc/index.php/Main/PhysicsBasedModels) | U2 extensive storage and changing-volume balance checks |
| [First Order Plus Dead Time](https://apmonitor.com/pdc/index.php/Main/FirstOrderSystems) | U2/U3 gain, time constant and separation of lag from delay |
| [Transfer Functions](https://apmonitor.com/pdc/index.php/Main/TransferFunctions) | U3/U5 transform definitions, series/parallel combination and zero-state interpretation |
| [Second Order Systems](https://apmonitor.com/pdc/index.php/Main/SecondOrderSystems) | U4 standard form, equal/unequal lags and damping/step-response comparison |
| [State Space Models](https://apmonitor.com/pdc/index.php/Main/StateSpaceModel) | U6 matrix dimensions, state/input/output distinction and feedthrough |
| [Controller Stability Analysis](https://apmonitor.com/pdc/index.php/Main/StabilityAnalysis) | U7 pole interpretation and final-value cautions; broad cancellation wording was not adopted |
| [Linearization of Differential Equations](https://apmonitor.com/pdc/index.php/Main/ModelLinearization) | U8 equilibrium Taylor expansion and operating-point validity |

Michigan CTMS introduction pages were attempted but unavailable (fetch/access errors); they were not used. Two guessed APMonitor introductory URLs also failed; the valid DynamicModeling and PhysicsBasedModels pages above were subsequently opened through their actual links.

## Verification and publication

- Author numerical script: `other/work/scratch/pdc/verify.py`; results: `numerical-verification.json`. Every numerical example recomputed in Python. Standard-library RK4 independently checks analytical second-order, two-lag and three-lag response curves at multiple times. The nonlinear tank implicit solution matches direct integration. Degree-six factorisation and impulse partial fractions were recombined at real and complex points. Units and physical limits checked throughout.
- Independent cross-reviews: [U1–U4](../reviews/PDC-U1-U4-cross-review.md) and [U5–U8](../reviews/PDC-U5-U8-cross-review.md), with their independent Python results beside the reports. Both passed. The one assumptions clarification is incorporated.
- Scoped publisher: `other/work/scripts/publish_pdc.py`. Canonical native Markdown stays in `other/work/drafts/Process Dynamics and Control/`; main notes use GitHub-compatible maths and the export uses native dollar maths. All original equations and prose are preserved between editions, with equation labels 1–71.
- 31 Markdown files per edition: 22 notes, eight topic indexes and one subject index. All 234 internal navigation/figure links per edition resolve; all ten used figures were opened visually, recropped where needed, decoded and copied byte-identically. Required section order and standalone prose checks pass.
- KaTeX/Markdown check: `other/work/scratch/pdc/render.mjs` parses every publication file and renders 844 expressions in each edition without errors; expression counts agree. HTML previews are local scratch outputs. `render-validation.json` records results.
- An actual Chrome launch was attempted for screenshot/runtime layout checks, but sandbox restrictions on Chrome's crashpad/Mach service prevented it. The failed attempt is retained in `browser-attempt.json`. No browser screenshot or Obsidian runtime verification is claimed. Static Markdown/KaTeX validation, visual figure checks and export relocation are complete.
- The full subject export was copied to a different temporary `Vault/Courses/` location and validated again; its navigation and figure links remain intact. The local all-subject Obsidian ZIP was regenerated from the current export and checked after extraction. Archive checks are recorded in `archive-validation.json`.

## Delivery paths

- [Main reading index](<../../../notes/Process Dynamics and Control/README.md>)
- [Native Obsidian index](<../../obsidian/CEBT-II Notes/Process Dynamics and Control/README.md>)

Copy the whole subject folder, including its shared `figs/`, into the vault. No vault files were changed. Later course sections require their sources, and merges await the user's specified groups.
