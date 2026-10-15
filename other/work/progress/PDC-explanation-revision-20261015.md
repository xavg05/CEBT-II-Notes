# PDC explanation revision — 15 October 2026

Author: Codex. Authorised scope: improve all supplied-source PDC notes using Xavier's preferred PDC-04 explanation, preserve the established style, and update PLAN.md and CLAUDE.md so the method can be repeated. All 22 canonical drafts and both published editions are revised. Independent scientific/instructional cross-review passed after two wording fixes. No complete-section merge was requested.

## What the example improves

The useful difference is explanatory connection: it traces physical causes, explains the purpose of algebraic operations, separates speed from endpoint, and interprets numerical values against the actual experiment. Existing notes had correct equations and useful intuition but sometimes compressed these bridges into a short reason line. Revisions integrate the missing connections into the existing sections instead of adopting the conversational example's headings or expanding every note identically.

| Note | Gap addressed |
|---|---|
| 01 | Follow colder feed through energy storage, measurement and heating; interpret heat-capacity flow and feedforward's fixed-target assumption. |
| 02 | Explain actuator choice by tracing inventory and separation effects; show why an inventory imbalance needs corrective withdrawal. |
| 03 | Explain outlet-flow cancellation physically and what constitutive closure must determine. |
| 04 | Explain standard-form normalisation, integrating factor, reacting baseline, total removal, Damköhler limits, poles, residence time and numerical settling fractions. |
| 05 | Explain why inlet composition changes concentration but well-mixed withdrawal does not directly; interpret pulse concentration as a weighted average. |
| 06 | Identify thermal capacity/conductance and explain shared poles but different input gains; interpret a sensor driven by a gradual tank response. |
| 07 | Expand the energy product derivative to expose the cooling term; distinguish a state relation from its time history and from reversible discharge. |
| 08 | Separate coordinate change from actual initial-state assumptions; connect the transform denominator back to storage and removal. |
| 09 | Explain exponential remaining distance, initial tangent and why impulse and step have different endpoints. |
| 10 | Explain the absent restoring term and persistent memory; compare ramp, curved rise and transported step. |
| 11 | Explain second-order coefficient normalisation, envelope/frequency and why mechanical inertia can oscillate while passive sequential mixing cannot. |
| 12 | Explain transient weights from initial conditions and peak ratios from the final-value reference line. |
| 13 | Trace front arrival and sequential storage; distinguish an initially flat tangent from another finite waiting interval. |
| 14 | Explain compatible units and signal meanings; distinguish cancellation of dynamics from cancellation of endpoints. |
| 15 | Interpret each matrix column as an experiment and use conserved A+B to explain different concentration memories. |
| 16 | Explain boiler coefficient signs, lack of inventory restoration and the physical approximation behind algebraic steam feedthrough. |
| 17 | Explain decay versus polynomial weighting, slow visible modes and why a weak unstable mode eventually dominates. |
| 18 | Compare pathway initial slopes with final strengths; distinguish inverse response, immediate feedthrough and transport delay. |
| 19 | Explain why zero-frequency evaluation recovers a static balance only after settling is established; separate gain from timing. |
| 20 | Show which Taylor/product terms cancel, remain or are neglected; connect dynamic gain to the equilibrium tangent. |
| 21 | Interpret outflow slope as restoring strength and explain local time/gain trends and finite-step endpoint curvature. |
| 22 | Explain increased inlet and outlet contributions to valve sensitivity, downstream product terms and repeated sequential memories. |

## Source and scientific verification

Read all 22 canonical notes and the original production/cross-review records. Reopened both supplied PDFs, rendered all 42 pages into seven six-page montages and visually inspected them; used text extraction for locating prose. Existing source equations, figures, scope and corrections are retained. Original PDFs were not modified. The new interpretations were independently derived from the existing balances and response formulas.

Supplementary university teaching pages actually opened and read for this revision:

- [BYU/APMonitor feedback introduction](https://apmonitor.com/pdc/index.php/Main/FeedbackControl): measurement–controller–actuator causality.
- [Balance equations](https://apmonitor.com/pdc/index.php/Main/PhysicsBasedModels): extensive accumulation and stream terms.
- [First-order systems](https://apmonitor.com/pdc/index.php/Main/FirstOrderSystems): separate gain, lag and transport delay; use the independently derived response rather than the page's mistyped inverse transform.
- [Transfer functions](https://apmonitor.com/pdc/index.php/Main/TransferFunctions): zero-state input/output and block relationships.
- [Second-order systems](https://apmonitor.com/pdc/index.php/Main/SecondOrderSystems): damping and normalised responses.
- [State-space models](https://apmonitor.com/pdc/index.php/Main/StateSpaceModel): stored states and direct feedthrough.
- [Stability analysis](https://apmonitor.com/pdc/index.php/Main/StabilityAnalysis): modes and stability, qualified by the existing hidden-mode and final-value cautions.
- [Linearisation](https://apmonitor.com/pdc/index.php/Main/ModelLinearization): equilibrium slopes and neglected higher-order terms.

No external passage was copied into the study notes. These sources supplement reasoning rather than replace balance derivation. The original production record contains the earlier, broader source list.

Reran the existing Python numerical/ODE/partial-fraction verification in `other/work/scratch/pdc/verify.py`. Independent review separately recomputed added values and checked signs, conservation, units, limits and Taylor expansions. [Independent review](../reviews/PDC-explanation-revision-20261015.md) and [numerical evidence](../reviews/PDC-explanation-revision-20261015-numbers.json) record the checks. Two findings were corrected: first-peak excess is the exponential decay factor after substituting the peak phase, and level gain is explicitly the reciprocal of the outflow slope.

The common 95% criterion gives inert/reacting PDC-04 settling times 299.573/149.787 s. The supplied conversational example's approximate “finished” times were not adopted as an exact or shared criterion. Added equal initial slopes explain why a faster concentration relaxation does not require a larger initial slope in this experiment.

## Publication and rendering

- Published only PDC through `other/work/scripts/publish_pdc.py`. Fixed its implicit Windows text encoding by explicitly reading/writing UTF-8; this preserves punctuation and maths in navigation and indices.
- Verified 31 Markdown files per edition: 22 notes, eight topic indices and one subject index. All 234 local links per edition resolve; all ten figures decode and match across editions. Relocated the native export into a temporary independent folder and reran link validation successfully.
- `other/work/scripts/check_pdc_explanation_revision.mjs` checks exact draft/native content, equivalent reading/native formulas, KaTeX compilation and resulting HTML formula counts. All 963 maths expressions per edition pass; all 71 numbered labels remain in continuous order. Existing numbered results retain their labels.
- Headless Chrome rendered the full set into a local 72-page review PDF, with all 22 note openings and all ten source figures present. Visually inspected the rendered note openings, the expanded PDC-04 pages, and every existing figure in a contact sheet. The local render is a verification artifact, not a requested merged delivery. An initial sandboxed Chrome attempt failed; the approved external run succeeded.
- No Obsidian application runtime or GitHub website runtime was opened. Rendering checks use local KaTeX/HTML/Chrome, and portability checks use relocated Markdown and links.

Machine-readable edit, rendering and publication evidence lives in `other/work/scratch/pdc-explanation-revision/` and `other/work/scratch/pdc/publish-validation.json`. The historical generator `other/work/scratch/pdc/write_notes.py` must not overwrite the revised canonical drafts. PLAN §6.3 and CLAUDE §3 document the reusable authoring and review criteria.
