# AB-U15 cross-review — AB-57

Verdict: **PASS. No required corrections found.**

Reviewed read-only: out/AB/AB-57-synthetic-dna-rna-condensates.md and out/work/progress/codex-ab57-lecture16-20261009.md. Opened all five existing cropped PNGs. No new PDF rendering/reading, no edits to AB-57, figures, progress, ownership board or plans. Parent handles KaTeX and integration. The reported orphan “third offered choice” is already absent from the version reviewed.

## Equations and assumptions

1. DeltaG = DeltaG_standard + RT ln Q; at equilibrium Q=K and DeltaG=0, giving K=exp(-DeltaG_standard/RT). Dimensionless activity-based K explicitly stated; individual association correctly distinguished from a phase boundary.
2. Production-minus-first-order-loss balance dN/dt=s-lambda*N correct with fixed production and common constant hazard.
3. At steady state Nss=s/lambda, so Nss/s=1/lambda. For an exponential survival distribution, integration of survival yields the same mean lifetime; independently checked by Simpson quadrature. Steady state and first-order loss are explicit assumptions.
4. Separating the loss-only ODE yields exponential cohort survival N=N0*exp(-t/tau), with the correct sign and initial condition.
5. Setting survival to 1/2 yields half-life=tau*ln(2), not tau. Effective loss including cell-division dilution is correctly qualified as residence time rather than pure chemical degradation lifetime.

The numerical lifetime inference is conditional on one continuously active polymerase per plasmid, negligible initiation delay, complete transcripts counted one-for-one as nanostars, and steady-state first-order removal. Those assumptions are explicitly stated; elongation speed alone is not treated as initiation frequency. No molecular degradation lifetime is claimed from the gels or puncta.

## Independent example calculations

Transcript transit time: 250 nt / (250 nt/s) = 1.00 s.
Production under the stated occupancy: 25 / 1.00 = 25.0 nanostars per cell per second.
Effective loss constant: 25 / 30000 = 0.0008333333333333334 s^-1.
Mean lifetime: 1200 s = 20.0 min.
Half-life: 831.7766166719343 s = 13.862943611198906 min (13.9 min rounded).
Steady-state residual: zero; half-life survival fraction: 0.5.
All agree with the note. Results come from this reviewer's independent script, not the owner's saved outputs.

| Sequence, 5 prime to 3 prime | Reverse complement, 5 prime to 3 prime | Length | GC fraction | Self-complementary |
|---|---|---:|---:|---|
| CGATCG | CGATCG | 6 | 66.7% | Yes |
| GGGGCCCC | GGGGCCCC | 8 | 100.0% | Yes |
| CAGATCTG | CAGATCTG | 8 | 50.0% | Yes |
| CCGATGCG | CGCATCGG | 8 | 75.0% | No |
| CGCG | CGCG | 4 | 100.0% | Yes |

All five table rows match. The GGGGCCCC choice is explicitly an initial design judgement at comparable conditions, not a calculated melting or phase-separation temperature; folding, alternative association, concentration, geometry and bond exchange are appropriately qualified.

## Structure and figures

Title follows Section 57 convention. Exactly seven required H2 sections in order; local equation tags are 1 through 5. No source-PDF/lecturer narration, wikilinks or callouts. All five relative image links resolve to valid PNGs, and all five images were visually opened. Captions and surrounding text explain the scaffold, domains, transcription/capture, RNA designs and gel distinction. Source citations and retrieval limitations live in shared progress rather than deliverable narration.

## Review limits and reproducibility

Bounded review uses shared progress to establish source coverage; it does not independently certify every research claim against the inaccessible publisher pages, revisit source PDFs, or perform parent-owned KaTeX rendering. No current blocker or required owner action.

Independent script: out/work/scratch/codex-AB57-cross-review-20261009/review.py
Results: out/work/scratch/codex-AB57-cross-review-20261009/independent-results.json
