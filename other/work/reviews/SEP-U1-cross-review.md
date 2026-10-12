# SEP-U1 independent cross-review

Reviewer: independent of the U1 author (check script started by a Codex subagent, completed and signed off by Claude). Date: 12 October 2026.

Result: **PASS — no blocking scientific, numerical or coverage findings.** No edits to U1 drafts were required.

## Evidence

- Independent script `other/work/scratch/separations/review-U1/independent.py` (does not import author code); results in `independent-results.json`. The ammonia equilibrium table was transcribed from the original page independently of the author record.
- Original scans re-read for the ammonia design (p29, p32, p33): data table, xB* ≈ 0.067 handwritten estimate, straight-line Az = 14.8 m³ and trapezium NTU = 19.35 / Az = 14.3 m³. Confirmed the handout's height formula contains A, so the supplied data fix packed volume Az, not Z; the draft's treatment is correct.

## Numerical agreement

| Check | Independent | Draft |
|---|---|---|
| Gas molar density 293 K, 110 kPa | 0.0451532 kmol/m³ | agrees |
| Absorber/stripper pinch | Lmin 1.8, Gmin 0.45, L/G 2.222 | agrees |
| Two-film shares CO2/NH3/SO2 | 0.474 %, 91.7 %, 35.7 % gas-side | agrees |
| Linear NTU/HETP example | NTU 4.15888, Z 2.49533 m, n 3.41902, HETP 0.729837 m | agrees |
| Hydraulic sizing | U 1.10 m/s, D 1.07587 m, K4 fraction 0.3025 | agrees |
| Ammonia design | x* 0.06652, Lmin 0.0375075, L 0.0483847 kmol/s, xB 0.0515659 | agrees |
| Ammonia NTU (piecewise-analytic vs log-Simpson) | 17.6229916 / 17.6229916 | agrees |
| Packed volume | 13.0098 m³ (endpoint log-mean 13.999; coarse table 19.355 → 14.288) | agrees |

## Structure and style

All 11 drafts contain the seven required sections in order, prose-only links, no wikilinks, and no source/lecturer references. All linked `../figs/u1-*.png` targets exist; crops were opened by the author and the ammonia-equilibrium crop was checked against p30 here.
