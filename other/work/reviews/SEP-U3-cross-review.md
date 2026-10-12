# SEP-U3 independent cross-review

Reviewer: Claude, independent of the U3 author (Codex). Date: 12 October 2026.

Result: **PASS — no blocking findings.** One minor clarity edit applied (below).

## Evidence

- Original scans read for every worked example: p19 (gas design data and quadratics), p34 (NaCl polarisation), p40 and p42 (whey ultrafiltration), p49–50 (RO design). Literal readings agree with the author's transcription record, including the source errors it lists: printed outlet x = 0.005 (should be 0.05), RO exponent −0.005 in the C3 line (−0.995; the printed C3 = 49.9 g/L confirms), and "≈ 17" modules from 51.17 m² by arithmetic mean.
- Independent script `other/work/scratch/separations/review-U3/independent.py` (written from the scans; does not read author code or results). Results in `results.json`. The gas differential design is integrated with RK4 in x, a different scheme from the author's mesh.
- All 12 drafts read in full; quadratic rearrangement (U3-04), differential gas balance (U3-06), film-model integration (U3-08), osmotic-pressure derivation (U3-09), coupled UF parametrisation (U3-10), local RO elimination (U3-11) and RO concentration/area integrals (U3-12) re-derived.

## Numerical agreement

| Example | Independent | Draft |
|---|---|---|
| Gas quadratics | 4y²−22.36y+10.45, 4y²−16y+2.5; yi 0.514753 / 0.162883 | agrees |
| Endpoint gas area | S 0.550520; J 2.67792e−5 / 5.73099e−6; A 11 475 (arith) / 13 663 m² (log) | agrees |
| Differential gas design | S 0.529133, ȳ 0.350491, A 12 443 m², O2 recovery 0.887 | agrees |
| NaCl polarisation | Re 1.5, Sc 625, Sh 6.38757, kf 3.40670e−5 m/s, Cw 0.114382 M, Rtrue 0.973772 | agrees |
| Ideal osmotic pressure 0.1 M NaCl | 4.875 bar | agrees |
| Whey UF | Π(10) 0.043909, Π(400) 6.544 bar; J* 103.584 LMH; ΔPG 6.95833 bar; 36 LMH → Cw 36.0403 g/L, ΔP 0.304067 bar; table row 60 LMH 0.6486 bar | agrees |
| RO | C3 49.9109, C2 0.207875 g/L; net 26.4435 / 14.2777 bar; A 51.1609 m² → 18 modules; integrated 50.9024 m² → 17 | agrees |

Note: the source's Sh = 6.37 is close to the exact-1/3 value (6.388), not the 0.33-exponent value (6.25); this does not affect the drafts, which use the exact exponent.

## Edit applied

- U3-12 worked example step 1 now states Q1 = 333.333 m³/day, which the step used without giving a value.

## Figures and style

All nine `u3-*.png` crops opened in a montage: each shows the intended construction legibly and matches its adjacent prose. A small fragment of unrelated text at the foot of `u3-11-feed-bleed.png` is harmless. All drafts have the seven required sections, defined symbols, local sequential equation tags, prose-only links and no source/lecturer references.
