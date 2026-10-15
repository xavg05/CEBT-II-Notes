# Reaction Engineering explanation cross-review — 15 October 2026

**PASS: all 21 applied RE short-note revisions reviewed independently. No consequential finding remains.** Also checked the coordinator's SEP-30 and SEP-39 corrections in their actual native notes, and the global guidance in PLAN.md §7 and CLAUDE.md.

This reviewer proposed the ET changes, not the RE changes. Read every actual RE native short note in full context, compared the saved originals with `re-proposals.json`, and checked the applied text. The scope is the explanation revision; the existing original-PDF scientific review and numerical evidence remain in force for unchanged material. No study note was edited in this task.

## Exact change and preservation checks

`other/work/scratch/all-subject-explanations/verify_re_cross_review.py` independently reconstructs each revision from its immutable saved original using `before-revision/manifest.json`. All 21 applied files exactly match that reconstruction. Equation tags, display equations and figure links are unchanged in all 21. Reproducible results are in `RE-explanation-cross-review-20261015-checks.json` alongside this report.

## Scientific and explanation review

| Notes | Independent check | Result |
|---|---|---|
| RE-01 | Species balance includes transport; extent normalisation and rate basis are distinct transformations. | PASS |
| RE-02 | Incremental consumption divided by local volume-specific rate has volume units; PFR advantage is restricted to the stated increasing reciprocal-rate comparison. | PASS |
| RE-03 | Dividing ideal-gas flows by inlet values separates mole change, temperature and pressure. Expansion at fixed conversion reduces concentration and increases first-order size. | PASS |
| RE-04 | Heat-capacity flow has W/K units, not J/K. Dividing adiabatic temperature and conversion gradients cancels the local extent rate; wall heat introduces a rate-dependent term. | PASS |
| RE-05 | Serial waiting times add by convolution. Fixed total mean gives variance proportional to inverse tank count; adding unchanged tanks changes the mean as well. No finite cascade is assigned a hard minimum time. | PASS |
| RE-06 | Linear first-order consumption commutes with concentration averaging; nonlinear CSTR/PFR maps do not commute although passive-tracer convolution does. | PASS |
| RE-S3-01 | Preparation, chemical activation and accessibility are separate constraints; additional sites/area do not guarantee selectivity. Matches the existing zeolite and metal examples without adding unsupported performance values. | PASS |
| RE-S3-02 | Fixed-metal-mass coarsening reduces exposed area; clean feed reverses competitive coverage but does not by itself redisperse sintered metal. Exothermic regeneration can compound damage. | PASS |
| RE-S3-03 | Adiabatic paths conserve sensible plus chemical enthalpy; interstage exchanger changes temperature at fixed conversion. Reversible exothermic net rate can improve on cooling near equilibrium, despite a smaller forward constant. | PASS |
| RE-S3-04 | Average survival differs from survival at average age. Fixed tank count and length-scaled tank count are separate interventions; the text retains wetting, dispersion and effective-rate limitations. | PASS |
| RE-S3-05 | Sequential pathway fluxes must satisfy steady intermediate balances, with stoichiometry respected. Rate, accessible area and product yield remain distinct. | PASS |
| RE-S4-01 | Occupied/vacant ratio gives the Langmuir normalisation. Low-pressure slope identifies capacity times affinity, rather than both independently. | PASS |
| RE-S4-02 | Taking the nonnegative root of pair-site equilibrium produces square-root pressure dependence; shared normalisation gives competitive displacement. | PASS |
| RE-S4-03 | BET column fractions require occupancy weighting. Slope plus intercept isolates monolayer volume; area is probe-accessible rather than an active-site count. | PASS |
| RE-S4-04 | Concave capillary pressure lowers liquid chemical potential and equilibrium vapour pressure; flat limit and film/core distinction are correct. Isosteric slope holds loading fixed. | PASS |
| RE-S5-01 | Fast reversible steps can carry a small net throughput near equilibrium; exact zero throughput is not inferred. Two occupied fractions versus one explain LH/ER denominators under stated inventories. | PASS |
| RE-S5-02 | Logarithmic pressure derivative is a local fractional slope, not signed consumption. The redox-site fraction adjusts so reduction and restoration fluxes match. | PASS |
| RE-S6-01 | Pore-concentration and total-area conventions put geometric penalties in effective diffusivity once. Molecular/wall collision combination has the correct pressure limits. | PASS |
| RE-S6-02 | Normalisation leaves the reaction/diffusion modulus. Integrated reaction equals boundary flux; zero centre gradient is compatible with nonzero centre reaction. Pellet size comparison holds kinetics/diffusion/surface concentration fixed. | PASS |
| RE-S6-03 | Multiplication by concentration derivative supplies the first integral of the pellet equation. Stronger chemistry steepens surface gradient while shortening penetration; film balance closes on the same surface concentration. | PASS |
| RE-S6-04 | Reaction elimination yields the Prater concentration–temperature relation under constant coefficients. Thermal stability explanation is explicitly confined to the reduced model and distinguishes a bound from a predicted rise. | PASS |

Python spot checks independently reproduce the expansion-versus-constant-flow sizing direction, rate cancellation in the adiabatic path, fixed-mean variance direction, nonlinear map order, broader-RTD surviving fraction, competitive site conservation, BET parameter inversion, LH logarithmic slope by finite difference, Bosanquet limiting behaviour, spherical flux versus integrated consumption, surface/overall effectiveness and Prater bound. They check the new explanations against the existing example equations; no new values were added to the study notes. Exact machine outputs are in the JSON record.

The added prose is specific to the actual equations and examples and fits existing Motivation and explanation sections. Some concepts intentionally reinforce earlier intuition, but the additions supply causal or algebraic connections rather than a generic checklist. They do not turn the missing RE source sections 2, 7 or 8 into implied coverage or alter the provisional RE-S identifiers.

## SEP corrections and instruction consistency

- **SEP-30 PASS.** The actual note now says that at complete rejection no solute exits through the membrane, while convection to the wall is balanced by diffusion back to bulk. This follows directly from setting permeate concentration to zero in its signed film balance. Its exponential explanation correctly attributes the shape to concentration-proportional convection versus gradient-proportional diffusion. The existing osmotic sentence refers to opposing **solvent** flux, while distinguishing increased solute passage. No contradiction remains.
- **SEP-39 PASS.** The actual note now identifies partly unused capacity *within the downstream mass-transfer zone*, rather than asserting a fresh bed region beyond a front already at the outlet. The complement of the outlet fraction integrates retained inventory; a breakthrough threshold is not total saturation. The unchanged unused-equivalent-length formula remains explicitly approximate and distinct from geometric zone width.
- **PLAN.md §7 / CLAUDE.md PASS.** Both apply the same physical/algebraic/observational explanation standard across all subjects while preserving existing style, current corrected text, authorised complete-section groupings and equation numbering. PLAN states that the prior PDC push prerequisite was met before beginning; ownership revision authority is tied to the user's explicit instruction. AB-U13 supplementation, optional AB-57, missing RE/PDC sources and no-new-merge boundaries remain explicit. Synchronisation, independent review, Python verification, UTF-8 publication and honest runtime limitations are consistent between the two instruction files.

## Primary sources actually opened for this independent review

- [Fogler, Diffusion and reaction in porous catalysts](https://public.websites.umich.edu/~elements/6e/15chap/summary.html): read pellet-balance, dimensionless-profile, effectiveness and transport/kinetics explanatory text. The page presents much of its algebra as images; the new algebra was independently rederived from the actual native notes rather than treated as verified by unviewed web images.
- [Fogler, Predicting conversion from RTD](https://public.websites.umich.edu/~elements/6e/17chap/summary.html): read segregation, mixing-model and model-selection discussion.
- [Fogler, Catalysis and catalytic reactors](https://public.websites.umich.edu/~elements/6e/10chap/summary.html): read step-inventory and catalyst/coverage explanations.
- [Fogler, Nonisothermal reactor design](https://public.websites.umich.edu/~elements/6e/11chap/summary.html): read energy-balance and operation-path discussion.

These corroborate the review rather than provide new numerical datasets. The proposal review's additional source log is in `RE-explanation-proposals-20261015.md`; this report does not claim to have independently opened every source listed there.

Final mathematical rendering, image opening, both-format publication/portability, and GitHub delivery checks remain the coordinator's responsibility. This PASS covers the actual RE applied explanation changes and the explicitly listed SEP/instruction checks, not a new full PDF audit or Obsidian runtime test.
