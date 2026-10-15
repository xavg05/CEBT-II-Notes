# AB-U6 coverage and precision findings — 14 October 2026

Reviewer: Codex. Owner of original short notes: claude. These findings are recorded rather than applied, in accordance with AGENTS.md. AB-25 and the corresponding complete section/native editions contain the same wording.

## 1. NMR ensemble averaging — correction required

The AB-25 intuition paragraph incorrectly says NMR abandons averaging across molecular copies. Solution NMR measures a bulk ensemble of molecules; what it dispenses with is an ordered crystal or individually aligned particle images. NMR supplies resonance-based structural restraints, with observables averaged over the appropriate ensemble and timescales. This is an added explanatory error, not missing mathematical lecture content.

Concrete replacement for the NMR intuition paragraph:

> **NMR** measures nuclear-spin resonances from an ensemble of protein molecules tumbling in solution. Chemical shifts, through-space interactions and scalar couplings provide structural restraints without an ordered crystal. Its observables are ensemble and time averaged; it does not image one isolated molecule.

The existing sentence describing spread of the calculated structural ensemble already acknowledges weak restraints, but should additionally avoid equating model spread with measured motion. Proposed replacement:

> The result is an **ensemble** of structures compatible with the restraints. Spread can reflect incomplete restraints or modelling uncertainty as well as flexibility; establishing dynamics requires suitable experimental observables rather than model spread alone.

Evidence actually opened and read: [RCSB PDB primary deposition and original paper abstract for 2NR2](https://www.rcsb.org/structure/2NR2), especially ensemble-averaged NMR restraints and under/over-restraining. The Nobel advanced-information PDF was attempted but returned 403 and was not used.

## 2. Cryo-EM size limitation — qualify wording

AB-25 states that below about 100 kDa a particle is too faint to align and calls this a lower size limit. The source gives a broad preference for larger proteins and complexes, not a universal hard cutoff. Preserve the course's useful scale without treating it as a theorem.

Concrete replacement:

> Smaller particles generally produce weaker images and are harder to align reliably. Around 100 kDa is a useful practical scale for this comparison, rather than a universal lower size limit; achievable performance depends on specimen, contrast, symmetry, detector and reconstruction method.

## Ownership and publication

Apply replacements to the canonical reviewed unit and regenerate both small-note and complete-section editions together. Do not directly patch one generated copy and leave the other three inconsistent. No notes were edited as part of this report. These findings must remain visible in the overall readiness report until resolved by the owner or explicitly authorised by the user.

## Closure — 15 October 2026

The user explicitly authorised the initial three findings and the full reviewed Biotechnology batch. The coordinator applied these replacements to the canonical unit and all four reading/export copies, together with two adjacent NMR/dynamics qualifications identified by the independent reviewer. Exact preservation checks pass. The independent review's final closure is recorded in `AB-01-47-source-coverage-20261014.md`; the findings above are retained as history and are no longer awaiting ownership permission.
