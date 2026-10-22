# Independent ET teaching recovery review — 22 October 2026

Reviewer: codex AB recovery agent, separate from the ET author.

Result: PASS after two editorial findings were closed by the owner. This review covers the changes to all twelve canonical ET units and all 43 per-note recovery decisions. Publication parity, equation rendering and portable-export validation are coordinated separately by the parent agent.

Read the complete canonical diff and the per-note retention/omission record against the historical worked-section deletion. The recovered additions preserve the important distinctions: driving force versus nucleation, chemical potential versus concentration, excess volume versus the value of excess Gibbs energy, entropy versus energetic non-ideality, local volume versus accumulated fugacity, equilibrium compositions versus phase amounts, binodal versus spinodal and background molecular transport versus collective thermodynamic restoration. Numerical grids and repetitive substitution steps were reasonably condensed while keeping their teaching conclusions. Existing scientific qualifications remain.

Independently re-derived Gibbs–Duhem cancellation for the excess-volume model; conversion of density virial coefficients into pressure-series fugacity; solvent activity from ice equilibrium; Flory–Huggins solvent activity and critical conditions; symmetric common-tangent/binodal and spinodal conditions; asymmetric equal activities and lever rule; Kelvin scaling; phase-rule changes when a phase disappears; and molality/mole-fraction standard-state conversion. No scientific blocker found.

Ran the independently written `other/work/scripts/crossreview_et_recovery.py`: 19 numerical invariants/comparisons pass, including the restored coarse supercritical-steam table integral. Small differences from the author's stored numbers arise from using the exact gas constant rather than 8.314; they do not change the reported precision. Evidence: `et-teaching-independent-numerics-20261022.json`.

Opened and visually inspected the seven restored ET figures in `other/work/scratch/ET-recovery-crossreview-figures.png`: Margules activity curves, oxygen–argon mixing-energy sketch, water phase diagram, osmometer, pentane–propanal azeotrope sketch, isobutane–furfural common tangent/spinodals and nitrobenzene–hexane diffusion. Captions and added interpretations agree with the visible axes/features; graph/schematic values remain qualified. This was a file-image inspection, not an Obsidian runtime check.

Closed findings:

- ET01 said the supercooling relation was below, although it had been inserted above. Owner corrected the direction reference.
- ET09 retained a worked-example section title. Owner removed the six existing worked-example title prefixes across ET09/13/16/28/30/38; the parent coordinates generated filenames and navigation.

The owner additionally restored the ET09 tabular volumes needed for its retained numerical-method discussion and the ET16 thermal inputs needed for its retained eutectic comparison, with author numerical verification expanded accordingly.
