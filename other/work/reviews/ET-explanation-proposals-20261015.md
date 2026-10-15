# Equilibrium Thermodynamics explanation proposals — 15 October 2026

Scope: read-only review of every native short note, ET-01–43, in `other/obsidian/CEBT-II Notes/Equilibrium Thermodynamics/`. No notes, sources, production instructions or other agents' files were changed. This reviewer owns the proposal JSON, its scratch generator and this review record.

Read CLAUDE.md, PLAN.md, BOARD.md and the previous records `FINAL-ET-01-24.md`, `FINAL-ET-25-43.md` and `ET-source-coverage-20261014.md`. The last record documents visual coverage of all 247 original source pages; this revision reuses that established reading. No proposed explanation requires resolving an ambiguous original equation or extracting another figure.

The proposals are in `other/work/scratch/all-subject-explanations/et-proposals.json`, generated reproducibly by `make_et_proposals.py` in the same folder. There is one entry per short note, with the specific gap and exact unique old/new anchors. Each adds one or two topic-specific paragraphs where the reasoning is needed. Existing headings, numbered results, source scope and numerical examples are preserved. The additions do not introduce numerical answers; mathematical identities are algebraic consequences of the existing equations.

## Review focus and findings

| Notes | Connection made explicit |
|---|---|
| ET-01 | Independent component transfers make each chemical-potential difference vanish; stationarity differs from stable equilibrium. |
| ET-02 | Maxwell substitution turns thermal expansion into compression entropy; the constant-enthalpy differential explains throttling sign. |
| ET-03 | Euler reconstruction uses final-environment partial molar volumes rather than volumes carried unchanged through mixing. |
| ET-04 | Product-rule cancellation avoids counting amount changes twice; opposite slopes do not imply opposite pure-reference deviations. |
| ET-05 | Real-minus-ideal subtraction holds composition fixed; volume contraction constrains a derivative rather than the whole excess Gibbs energy. |
| ET-06 | More inert gas can raise equilibrium water partial pressure while lowering its gas mole fraction. |
| ET-07 | Shared reference cancels to give the logarithmic fugacity-ratio driving force; rate needs separate transport physics. |
| ET-08 | Local compressibility controls an increment, while fugacity accumulates an area; their endpoint values cannot be substituted for one another. |
| ET-09 | Dense supercritical crossover is continuous; good integrated fugacity does not imply equally good endpoint density. |
| ET-10 | Activity includes dilution as well as the activity coefficient; the sign of the latter is not a unique molecular-force diagnosis. |
| ET-11 | Differentiating total rather than molar excess energy includes both size and composition changes; pure-end excess zero allows finite dilute non-ideality. |
| ET-12 | Differentiating the total-amount denominator produces the common minus-excess-energy term; consistency does not validate pairwise assumptions. |
| ET-13 | Oxygen enrichment relative to Raoult differs from enrichment relative to the liquid: argon remains more volatile here. |
| ET-14 | Smaller additions reduce chord bias but amplify absolute pressure error; the limiting slope is a difference of contributions. |
| ET-15 | Separate temperature and dilution linearisations; the existing ideal-model discrepancy isolates these approximations. |
| ET-16 | The higher candidate freezing temperature is encountered first; closed-sample composition differs from remaining-liquid composition. |
| ET-17 | A common denominator cancels pure terms and reveals the square; equal cohesive energies remove only the energetic departure. |
| ET-18 | Chain count differs from segment occupancy; solvent addition changes both volume fractions and produces the linear activity term. |
| ET-19 | Boltzmann weights are relative probabilities that must be normalised, explaining the local-composition denominators. |
| ET-20 | Additive excess-energy pieces give additive logarithms and multiplicative activity coefficients; energetic and size limits differ. |
| ET-21 | Referencing one phase explains the independent constraint count; conservation fixes amounts separately. |
| ET-22 | Reference cancellation leaves opposing pressure/mixing energies; reverse-osmosis concentration changes the opposing osmotic pressure. |
| ET-23 | Laplace pressure is not surrounding vapour pressure; critical-radius stability assumes a fixed vapour reservoir. |
| ET-24 | The compressed phase differs between bubbles and droplets; nucleation superheat differs from bulk solute elevation. |
| ET-25 | Eliminating a phase amount gives the lever rule; feed composition equals liquid at bubble point and vapour at dew point. |
| ET-26 | Normalising the unknown phase produces distinct bubble/dew equations; pure-vapour correction is a separate approximation. |
| ET-27 | Stable-liquid thermodynamic factor distinguishes an azeotrope from a spinodal zero; azeotropic enrichment vanishes. |
| ET-28 | Shared denominator motivates the auxiliary ratio; two component constraints at one azeotrope fix a chosen model, not every curve. |
| ET-29 | Hypothetical reference is not a physical phase; changing convention preserves measurable fugacity. |
| ET-30 | Pressure comparisons require stating whether methane partial pressure or feed composition is fixed. |
| ET-31 | Unit dilute coefficient incorporates interactions into Henry's constant rather than removing them. |
| ET-32 | Identical copies trivially satisfy fugacity equality; real criticality requires disappearing density as well as composition differences. |
| ET-33 | Fixed overall composition allows changing phase compositions during retrograde condensation; an open reservoir then changes composition too. |
| ET-34 | Splitting the logarithm explains why the constant shifts standard potential while the concentration factor stays in the coefficient. |
| ET-35 | Stoichiometric chemical-potential addition explains geometric averaging and ionic activity powers. |
| ET-36 | Negative mixing Gibbs energy does not prove homogeneous stability; the common tangent compares global alternatives. |
| ET-37 | Heating reduces the dimensionless penalty even at fixed contact energy; LCST requires a different temperature dependence. |
| ET-38 | Activity compensates concentration partitioning; feed amount changes phase fractions rather than endpoints. |
| ET-39 | Conserved small fluctuations cancel first-order energy changes, explaining local curvature versus distant-phase alternatives. |
| ET-40 | Mobility and thermodynamic driving force are separate; a negative concentration coefficient still carries matter down chemical potential. |
| ET-41 | A sub-unity exponent raises a positive sub-unity factor without preventing its critical vanishing. |
| ET-42 | Phase amounts can change at fixed three-phase compositions; exhausting a layer removes a constraint. |
| ET-43 | Pure-major-component limits apply to different liquids; equilibrium steam ratio excludes operating losses and incomplete equilibration. |

Two small existing prose issues would otherwise conflict with the new distinctions, so exact additional edits are supplied without changing any result or number:

- ET-35: the reported 3.6% departure is that of the **mean activity coefficient**, not of the complete NaCl activity, which contains its square. Change the noun and comparison reference; retain the existing number.
- ET-36: the zero-curvature root is the loss of **local stability**, rather than the equilibrium onset of two-liquid coexistence. Explicitly distinguish spinodal from binodal.

## Sources actually opened and read

All were retrieved successfully on 15 October 2026. These are corroborating primary teaching/model sources; the prose additions are independent explanations and algebraic consequences of the reviewed native equations, rather than copied passages or new borrowed numerical datasets.

- [MIT 3.012, Models of the chemical potential](https://ocw.mit.edu/courses/3-012-fundamentals-of-materials-science-fall-2005/db26fd8bd9421c3659931bccdd605328_lec11t.pdf), pp. 3–10: partial-molar/Gibbs–Duhem structure and reference-state formulation. Supports ET-01, 03–05, 07, 10–12 and reference reasoning throughout.
- [Howard DeVoe, Thermodynamics and Chemistry, second edition v10](https://www2.chem.umd.edu/thermobook/v10-screen.pdf): opened sections on partial-molar intercepts (9.2.3), surface work (5.7), freezing and osmotic measurements (12.2), and binary phase diagrams including azeotropes, partial miscibility and retrograde behaviour (13.2). Corroborates physical distinctions in ET-02–06, 14–16, 21–27, 29–33, 42–43; established equations and numerical examples remain the direct basis of the additions.
- NIST TDE model definitions: [Redlich–Kister](https://trc.nist.gov/TDE/TDE_Help/Redlich-Kister-AC-Model.htm), [Margules](https://trc.nist.gov/TDE/TDE_Help_4_0/Margules-AC-Model.htm), [van Laar](https://trc.nist.gov/TDE/TDE_Help_4_0/VanLaar-AC-Model.htm), [Wilson](https://trc.nist.gov/TDE/TDE_Help_4_0/Wilson-AC-Model.htm), [NRTL](https://trc.nist.gov/TDE/TDE_Help_4_0/NRTL-AC-Model.htm), [UNIQUAC](https://trc.nist.gov/TDE/TDE_Help_4_0/UNIQUAC-AC-Model.htm), [UNIFAC](https://trc.nist.gov/TDE/TDE_Help_4_0/UNIFAC-AC-Model.htm) and [parameter temperature dependence](https://trc.nist.gov/TDE/TDE_Help_4_0/ActivityCoefficientModels.htm). Read the actual linked definition pages, including the expressions for excess Gibbs energy, rather than relying on search snippets. Supports ET-11–12, 17–20, 27–28 and model/reference usage later. NIST's UNIFAC page identifies the method and parameter output; it is not a derivation of the combinatorial model.
- [MIT 3.020, lecture 21 transcript](https://ocw.mit.edu/courses/3-020-thermodynamics-of-materials-spring-2021/1bgnBRUCdZ4iTNWZbkl7cEzMOMJLrirk9_transcript.pdf), pp. 1–6: conserved independent transfers, tangent intercepts, common tangent and phase-weighted Gibbs energy. Supports ET-36–39. [NIST lever-rule description](https://www.ctcms.nist.gov/~kattner/solidifc/lever.html) also read for the separation of phase equilibrium and phase-fraction balances (ET-16, 21, 25, 38, 42).
- [DTU Electrolyte Thermodynamics compendium](https://backend.orbit.dtu.dk/ws/files/131770579/ElectrolyteCompendium.pdf), sections 4.3–4.4, pp. 17–18: dilute-reference normalisation and simultaneous molality activity/standard-potential changes. Supports ET-31, 34–35.
- [Kamgar et al., Mutual diffusion in concentrated liquid solutions: A new model based on cluster theory, Cambridge author manuscript](https://api.repository.cam.ac.uk/server/api/core/bitstreams/011354f3-868f-403c-99d5-346254aee70d/content), pp. 1–3: thermodynamic-factor versus mobility distinction and critical-region empirical exponent. Supports ET-40–41. No refit of the original experimental diffusion data is claimed.

## Verification and limits

- Generator verifies every native file exists, every exact insertion anchor occurs once, and all 43 notes are covered once. Additional ET-35/36 clarifications have unique anchors too.
- Independently followed the added algebra: constant-enthalpy differential, same-reference fugacity subtraction, total-versus-molar derivative, quotient derivative for pairwise excess energy, logarithmic reference conversion, activity-factor multiplication, lever-rule elimination and fluctuation cancellation. Units and fixed-variable requirements checked against the native equations.
- No new rounded numerical answer is introduced, so no new numerical example is being asserted without Python. The existing example values retain the previous independent verification described in the historical audits; they were not all recomputed in this explanation-proposal task.
- These are proposals only. Final publication must apply them to the proper canonical edition, propagate existing complete sections and the GitHub/native mirrors, validate math/figures/navigation, and perform the independent revision review required by AGENTS.md. This record does not claim those later actions, an Obsidian runtime check, or a new original-PDF audit.
