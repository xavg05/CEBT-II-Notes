# Independent review of AB teaching recovery — 22 October 2026

Reviewer: Codex ET recovery agent, separate from AB author. Scope: all additions in the 15 changed corrected canonical AB units, including all 37 recovered blocks; unaffected notes checked against the author's 57-note disposition. Historical comparison uses parent of removal commit 77f9703. Publication checks remain the parent agent's separate task.

The recovery passes scientific review. Both minor AB-40 wording corrections below are closed in the canonical unit and recovery script; the owner reran the 69-check verifier successfully. Content restores mechanisms, statistical assumptions, controls, phase-volume bases and model interpretation rather than renaming exercise sections. The prenatal-screening mechanism and figure are restored in AB-15; the deleted Phred and coverage definitions return in AB-12 and AB-10. Gene-regulation supplementation and condensates optional scope remain qualified.

I read the canonical additions and the author verification code, and ran `verify_ab_teaching_recovery.py`: all 69 numerical and sequence checks pass. I independently followed the derivations in their actual context:

- Uncovered-base probability follows Bernoulli sampling and its Poisson limit; nominal average coverage is distinguished from depth at a particular site. The consensus tail is correctly stated as a conservative bound; wrong calls are grouped, ties counted as failures, alignment and independence required.
- The chromosome-dosage numerator and total-DNA normalisation use the same diploid-genome-equivalent fraction. Subtracting the euploid baseline yields a small signal proportional to placental fraction; binomial fraction variance gives inverse-square depth scaling. This is a screening model, not a clinical performance threshold or a direct fetal karyotype. Placental origin and possible discordance are explicit.
- Thermodynamic concentration effects, nearest-neighbour step counting, reverse-complement geometry, synthesis yield, clone screening, fluorescence occupancy, SELEX odds and strand-displacement saturation are mathematically consistent with the stated assumptions.
- Threshold variance propagation requires independence and otherwise covariance; exponentiation gives multiplicative uncertainty. RT-qPCR controls distinguish extraction, reverse transcription, sample adequacy and contamination rather than treating a negative as proof of absence.
- Filtration area scaling, centrifuge acceleration and sigma convention, transformed homogeniser fitting, recovery/concentration tradeoffs, precipitation inventory and resin loading all use compatible bases. AB-40's pressure target is explicitly an extrapolation requiring validation.
- The no-leak positive-feedback model has a stable zero state; its lower positive root is unstable and upper root stable, so basal expression and initial conditions matter. Dual reporters distinguish shared from independent contributions under matching assumptions. Dilution timing describes a decay segment rather than a full period.
- Cell-free release-factor deletion requires a charged suppressor tRNA and termination route. RNA mass recovery counts acceptable target population. Minimal-cell counts are historical annotation data. Compartment geometry alone does not establish autonomous cellular function. Transcript lifetime inference states steady state and its polymerase-occupancy model.

Two minor findings sent directly to the owner:

1. AB-40 said "4.4 would fall short" although 4.4 is the real-valued target. State that four whole passes fall short and round up to five.
2. AB-40's "Extrapolating to much higher pressure would not be:" lacks its complement. State that it would not be justified without validation.

No note owned by the AB author was edited by this reviewer. Figure paths are checked by the verification script; image visual checks and both-edition parity are coordinated separately. No clinical accuracy or runtime Obsidian validation is claimed.
