# Separations II explanation cross-review — 15 October 2026

Reviewer: independent Codex reviewer. Author of proposals: coordinator. Reviewed all 43 JSON entries in other/work/scratch/all-subject-explanations/sep-proposals.json against the entire corresponding native short note, including its assumptions, equations, examples and neighbouring prose. Read SEP-U1–U4 production/source records. Source rereading was unnecessary for these explanation-only additions: no new graph reading, numerical data or ambiguous source equation is introduced.

No study note or proposal edited. Own only this report. This is a proposed-change scientific/style review, not a claim that final exports or applied passages have been checked.

## Result

Two concrete corrections requested before scientific sign-off; all remaining new passages are scientifically consistent with the assumptions in their actual notes. Optional consolidation is also recommended in notes listed below. Python verified every replacement anchor occurs exactly once in its target, with 43 distinct target paths.

### 1. SEP-30: crossflow reduces concentration difference, not the gradient required for a specified diffusive flux

Proposed sentence:

> Raising crossflow instead increases the film coefficient and reduces the concentration gradient needed to return the same solute load.

This confuses concentration gradient with film-integrated concentration difference. At unchanged diffusivity, Fick's law fixes the gradient required for a specified diffusive flux. Increased crossflow shortens the film and reduces wall enrichment, without necessarily reducing the local gradient for the same return flux. In the fully rejected steady film, the wall return gradient magnitude is J_V C_w/D_B and follows the local flux balance; a change in C_w can change that local load, but cannot justify the unconditional gradient wording.

Concrete replacement:

> Raising crossflow instead increases the film coefficient, so a smaller wall-to-bulk concentration difference can return the same retained-solute load.

This explains the intended mechanism using the quantity that k_f actually multiplies. No equation or number needs changing.

### 2. SEP-39: avoid assuming a large unused fraction without specifying the front width

Proposed sentence:

> Much of the downstream capacity is then partially used or unused, even though the bed would capture more solute if poor outlet quality were allowed.

A low breakthrough limit does not guarantee that a large fraction of capacity is unused. A long bed with a short mass-transfer zone can have high utilisation at a low outlet limit. The point is partial utilisation within the front, whose fraction of the bed depends on its length and shape.

Concrete replacement:

> Capacity within the downstream mass-transfer zone remains partly unused, even though the bed would capture more solute if poorer outlet quality were allowed.

The next sentence correctly says earlier breakthrough can reflect a broader front as well as lower total capacity. Preserve that distinction.

## Scientific checks by note

| Notes | New explanation checked against actual context |
|---|---|
| SEP-01 | Operating balance versus equilibrium versus local rate; solvent choice and interfacial area affect different factors. No fictitious rate supplied by stage equilibrium. |
| SEP-02 | Flow paths and internals; vacuum pressure budget distinct from contact effectiveness. |
| SEP-03 | Henry-coordinate conversion and fixed-temperature ideal-dilute total-pressure effect; molecular affinity not confused with mole-fraction slope. |
| SEP-04 | Fixed-duty solvent loading and driving force; minimum flow remains a limiting infinite-contact requirement. Existing nonlinear-equilibrium/interior-pinch qualification preserved. |
| SEP-05 | Common-flux resistance addition requires conversion of concentration drops; numerical examples support different dominant films. |
| SEP-06 | D/delta scaling conditional on fixed film and hydrodynamics; individual coefficients not identified by one combined measurement. |
| SEP-07 | Reciprocal-force slice cost; HTU–NTU split only under constant prefactor and selected operating path. |
| SEP-08 | Log mean derived from reciprocal linear force; equal-force limit regular; curved profiles require more than endpoints. |
| SEP-09 | Equilibrium-stage multiplicative recurrence versus continuous local integration; both counts produce same height with different height measures. |
| SEP-10 | Gas loading/liquid holdup feedback and quadratic chart ordinate; diameter changes flow per area in transport calculation. |
| SEP-11 | Pinch loading not operating loading; convergence verifies chosen interpolation rather than physical data. |
| SEP-12 | Conserved dry-solid denominator; latent energy inventory does not set rate. |
| SEP-13 | Fixed-H fixed-P heating leaves vapour partial pressure unchanged; percentage-saturation and RH conversion distinguished. |
| SEP-14 | Sensible/latent redistribution and incoming-liquid enthalpy; saturation family requires energy selection. |
| SEP-15 | Equal H,P gives equal dew point despite different initial temperature; cooling below dew changes humidity and requires liquid outlet. |
| SEP-16 | Stable competition of heat supply and evaporation demand; wet bulb versus adiabatic saturation remains conditional transport analogy. |
| SEP-17 | Critical-moisture supply/demand mismatch distinct from equilibrium endpoint; rising solid temperature when latent demand falls. |
| SEP-18 | Dry-gas ratio controls humidity rise, not drying time; countercurrent gas/solid pairing fixes operating-line sign. |
| SEP-19 | Minimum of fitted external/internal branches under specified closure; crossing must lie on trajectory; distinct logarithmic slow limits. |
| SEP-20 | Specified cocurrent example remains wet branch; changing gas pairing changes transition while material coefficients remain fixed. Ideal moisture-time equality does not guarantee equal thermal history. |
| SEP-21 | Conservation path selects rate-family points; reciprocal integration weights slow regions rather than averaging rates. |
| SEP-22 | Added surface heat divided between increased evaporation and changed convective heat supply; variable surface reference curves driving-force path. |
| SEP-23 | Sorption and diffusion multiply in constant-property dense transport; common thickness scaling leaves ideal selectivity unchanged. |
| SEP-24 | Internal recycle distinct from net recovery; incomplete solute retention breaks concentration-ratio/VCR equality. |
| SEP-25 | True versus apparent rejection reference concentrations; retained-solute convection requires different balance from linear permeating-component series resistance. |
| SEP-26 | Permeate partial-pressure feedback and physical root; local enrichment relative to local retentate does not ensure enrichment relative to original inlet. |
| SEP-27 | Collected composition and area have different weights; common-reference volumes express common amount basis. |
| SEP-28 | Product derivative retains total-flow loss and composition change; local versus collected permeate roles match stated support-mixing model. |
| SEP-29 | C_p affects diffusion and convective removal; solvent/solute velocity-scale ratio interpreted within dilute linear closure. |
| SEP-30 | Return diffusion and exponential accumulation correct; crossflow sentence requires correction 1 above. |
| SEP-31 | Osmotic equilibrium cancellation of pressure/activity; permeance reduces excess hydraulic requirement, not equilibrium threshold. |
| SEP-32 | Parametrising pressure by flux enforces wall polarisation before osmotic evaluation; curvature and gel limit agree with specified measured relation. |
| SEP-33 | Coupled salt/solvent inventory; recycle changes local feed state without removing net salt inventory. |
| SEP-34 | Constant rejection still permits varying local permeate concentration; integral uses local flux; equipment threshold distinct from operating margin. |
| SEP-35 | Cyclic working capacity is inventory difference; finite times prevent equilibrium capacity guaranteeing productivity. |
| SEP-36 | Finite-site saturation and reciprocal-error magnification; no new numerical assertion. |
| SEP-37 | Closed-batch depletion and increasing equilibrium counterpart shrink driving force; agitation affects rate rather than capacity under fixed equilibrium conditions. |
| SEP-38 | Actual endpoint concentration enters isotherm; inadmissible root and original-balance check distinct from kinetics. |
| SEP-39 | Integrated input-minus-output is captured inventory; unused-fraction wording requires correction 2 above. Existing fluid-storage qualification remains authoritative. |
| SEP-40 | Swing positions relative to isotherm bend govern capacity; pressure/composition, purge and cycle preparation distinct. |
| SEP-41 | Phase preference versus inventory retention; integrated detector area versus peak timing/height. |
| SEP-42 | Width-normalised plate metric and Gaussian conversion; van Deemter optimum equates marginal changes, constant A term does not shift it. |
| SEP-43 | Differential retention and identical-partitioning limit; unequal-width definition versus later-width design approximation. |

## Style and integration

Every passage addresses its topic, preserves established notation, and avoids source/lecturer references or a new heading template. New explanations mostly add the intended causal or algebraic connection. The shared heading anchor places additions just before Motivation and explanation, within the end of Derivation, which is acceptable for a derivation interpretation. Some passages explicitly introduce a later worked example; consider moving those particular sentences beside that example during integration if flow is awkward.

The following existing notes already state nearly the same point as part of the proposed addition. Prefer replacing or consolidating the corresponding old prose rather than retaining both versions:

- SEP-15: derivation already states initial temperature does not set dew point at fixed H,P and describes the changed balance after condensation. Keep the new comparison between two initial samples; trim the matching old explanatory sentences.
- SEP-17: existing Motivation already explains that critical moisture depends on imposed demand and that stronger gas-side drying can exhaust supply earlier. Preserve the new explicit contrast with equilibrium moisture and remove repeated demand wording.
- SEP-24: new VCR paragraph substantially repeats the derivation and later worked-example caveat about permeating protein. One explanation after the balance is enough.
- SEP-25: new first paragraph expands precisely the inequality already explained after rejection definitions. Use the more causal new paragraph there and remove the old explanatory duplicate.
- SEP-36: reciprocal-error paragraph repeats the reason following equation 155. Consolidate into the new more complete explanation.
- SEP-38: new first paragraph is close to Intuition's existing final-equilibrium intersection argument. Replace the shorter Intuition wording with the expanded explanation or trim the repeated part.
- SEP-41: distinction of phase-volume inventory and concentration preference already appears immediately after equation 168. The new migration consequence is useful; avoid repeating the same inventory explanation verbatim in two places.

These are concise-edit recommendations, not additional scientific failures. Other repeated terms such as driving force, local rate and equilibrium are appropriate because they are applied to distinct mechanisms.

No new numerical examples were introduced, so no arithmetic was changed or recomputed for this proposal review. Original worked-example verification remains in the production records. No new source data, diagrams or claims require rereading ambiguous handwriting. Final maths rendering, figure links and export consistency remain publication checks, and the actual applied changes require a closure read after the two corrections.

## Applied-correction closure

Reopened the actual native SEP-30 and SEP-39 notes after coordinator application. SEP-30 now says crossflow permits a smaller wall-to-bulk concentration difference for the same retained-solute load. SEP-39 now describes partly unused capacity within the downstream mass-transfer zone without claiming it must be a large bed fraction. Both scientific findings are closed. The coordinator also consolidated repeated explanation in SEP-15/24/25/36/38; those were style recommendations. Scientific cross-review passes for the proposed SEP additions with the applied corrections; publication rendering and mirror checks remain separate.
