# Reaction Engineering II — relabel plan and quality findings, 22 October 2026

Author: claude. Requested by Xavier: write the section 2 notes now that the source has arrived, relabel the provisional notes into one consistent scheme, and check note quality.

Codex was running the user-authorised teaching-content recovery over RE drafts at the same time. Claude waited for its commit (b72139e) and then ran `publish_re_all.py`. Checks: 27 notes; labels 1–110 strictly increasing with no gaps; 241 links and 20 images per edition; KaTeX parses 1,125 expressions with edition parity; inline-maths check passes; portable relocation passes; all 21 existing notes match their pre-relabel text apart from headings, labels and figure names (plus the RE-23 rate-maximum figure). Results: `other/work/progress/re-relabel-validation.json`. Codex's recovery also cleared all six stale worked-example references listed below.

## Section 2 (new, Claude-owned)

Source: `other/sources/Reaction Engineering II/CEBT II reaction engineering 2 - reactions of solids.pdf`, 14 pages, all read visually.

| Note | Source pages | Equations |
|---|---|---|
| RE-07 Shrinking particles under film control | 1–4 | 21–24 |
| RE-08 Reaction-controlled shrinking particles | 4–5 | 25–27 |
| RE-09 Shrinking core with product-layer diffusion | 6–9 | 28–30 |
| RE-10 Shrinking-core regimes and combined resistances | 9–10 | 31–33 |
| RE-11 Droplet evaporation with coupled heat and mass transfer | 11–12 | 34–36 |
| RE-12 Reactors for solid reagents | 12–14 | 37 |

Additions beyond the source (all derived and checked in `other/work/scripts/verify_re_s2.py`, results in `other/work/progress/re-s2-verification.json`): quasi-steady justification ($\rho_m/C$ ratio), series film + reaction time for a shrinking particle (27), three-resistance additivity for the shrinking core (33, checked by numerical integration), early-time $X\approx\sqrt{3t/\tau_c}$, crossing of layer and reaction curves at $t/\tau_c=0.5$, $X=0.875$, droplet surface-temperature estimate, $\mathrm{Sc}/\mathrm{Pr}$ cube-root ratio, and segregated mean conversion (37) for plug and mixed solids.

Source corrections: p12 says "$\Delta H^{\mathrm{vap}}$, $D$ and $k$ are approximately independent of temperature"; $k$ should be the gas thermal conductivity $\lambda$. p1 "shrink as it reactor" is a typo for "reacts". Neither affects equations.

Figures (cropped with `other/work/scripts/crop_re_s2.py`, each opened and checked): RE-07-shrinking-particle, RE-08-shrinking-particle-conversion, RE-09-shrinking-core-sequence, RE-09-shrinking-core-profile, RE-10-shrinking-core-conversion, RE-12-{falling-particle-reactor, moving-belt-reactor, rotary-kiln, fluidised-bed, fixed-bed}.

External sources actually read: CSJM University Kanpur CHE-S402 fluid–particle kinetics slides (after Levenspiel ch. 25), Wikipedia "Wet-bulb temperature" and "Rotary kiln".

Status: author-verified; independent cross-review pending.

## Relabel map (applies after the recovery commit)

| Provisional | Final | Figure renames |
|---|---|---|
| RE-S3-01 | RE-13 | |
| RE-S3-02 | RE-14 | |
| RE-S3-03 | RE-15 | RE-S3-03-staged-beds → RE-15-staged-beds |
| RE-S3-04 | RE-16 | |
| RE-S3-05 | RE-17 | RE-S3-05-transport-pathway → RE-17-transport-pathway |
| RE-S4-01 | RE-18 | |
| RE-S4-02 | RE-19 | |
| RE-S4-03 | RE-20 | RE-S4-03-bet-isotherms → RE-20-bet-isotherms |
| RE-S4-04 | RE-21 | RE-S4-04-pore-hysteresis → RE-21-pore-hysteresis |
| RE-S5-01 | RE-22 | |
| RE-S5-02 | RE-23 | RE-S5-01-rate-maximum → RE-23-rate-maximum; RE-S5-02-temperature-effects → RE-23-temperature-effects |
| RE-S6-01 | RE-24 | |
| RE-S6-02 | RE-25 | RE-S6-02-pellet-profiles → RE-25-pellet-profiles |
| RE-S6-03 | RE-26 | |
| RE-S6-04 | RE-27 | |

Topic folders keep their numbers; section 2 fills the empty `02 - Fluid–solid reactions of solid reagents`. Equation labels: section 1 keeps 1–20; section 2 uses 21–37; sections 3–6 are numbered continuously from 38 in teaching order (they had no in-text equation references, so this changes no prose).

## Quality findings in existing notes (for Codex's recovery, not edited by Claude)

1. Stale references to deleted worked examples: RE-02 "The worked comparison", RE-03 "In the worked expansion example", RE-05 "In the worked fit", RE-06 "In the nonlinear worked network", RE-S3-04 "The worked results compare those model choices", RE-S4-02 "The worked comparison consequently distinguishes…". Codex's recovery diff already addresses RE-06 and RE-S3-04; check the rest.
2. `figs/RE-S5-01-rate-maximum.png` was cropped but never linked. It shows the Langmuir–Hinshelwood rate maximum against $P_A$ with $\theta_A$, $\theta_B$; it belongs beside the $\theta_A=\tfrac12$ maximum derivation in RE-S5-02 (RE-23). The relabel script places it there.
3. Section 3–6 notes lack ID headings (`# Catalyst materials and preparation` instead of `# RE-13: Catalyst materials and preparation`); sections 1 and all SEP/PDC notes include IDs. The relabel script adds them.
4. Overview openers in sections 3–6 use "Assume X." rather than the "Assumed: X." prerequisite line used in section 1 and the other subjects. Cosmetic; left for the owner.
5. Subject and topic READMEs still describe section 2 as missing and the identifiers as provisional. The relabel publisher rewrites them.
