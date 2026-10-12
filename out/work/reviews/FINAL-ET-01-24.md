# Final independent scientific review: ET-01–24

Reviewed by Codex; completed 2026-10-12. Scope: the first six archived Equilibrium Thermodynamics merged units, covering short notes ET-01–24. This is an independent review of the existing explanations, derivations, examples, assumptions and figures, not a fresh page-by-page audit of every source PDF. No archived notes or final deliverables were edited by this reviewer.

**Outcome:** review complete, with 22 exact corrections supplied in `out/work/scratch/final-et-01-24/corrections.json`. Final publication must apply these corrections and rerun its rendering/link checks before marking the delivery ready. Every replacement occurs exactly once, including when all replacements are applied sequentially in memory; there are no overlapping replacements.

## Scientific checks completed

- Foundations: Gibbs differential, chemical potential as partial molar Gibbs energy, Euler extensivity and Gibbs–Duhem; pure-fluid enthalpy departure from the Maxwell relation; partial-molar reconstruction and binary tangent relations; ideal-gas and ideal-solution chemical potentials and mixing energy. Corrected the Gibbs departure to subtract the ideal-gas volume before integration.
- Fugacity: finite-pressure chemical-potential integration, ideal-gas subtraction and the low-pressure reference limit; liquid Poynting correction and ideal-mixture limit; pressure/volume virial conversion and Peng–Robinson fugacity. Replaced the undefined expression involving `ln[f(P)/f(0)]` by a valid finite lower pressure before taking a limit. The sign of the integral determines residual Gibbs energy; it does not determine the local volume departure at the final pressure.
- Activity coefficients: pressure dependence from partial-molar excess volume; the identities $\mu_1^{ex}=g^{ex}+(1-x_1)g^{ex\prime}$ and $\mu_2^{ex}=g^{ex}-x_1g^{ex\prime}$; binary Margules and Redlich–Kister differentiation; dilute-limit vapour-pressure slopes; fusion-equilibrium relation including the heat-capacity correction.
- Models: van Laar from the stated vdW mixing rules, regular-solution volume fractions and solubility parameters, Flory–Huggins lattice solvent activity and criticality, Wilson and NRTL chemical potentials, and UNIFAC combinatorial terms. Independent finite differences of total/excess Gibbs energy reproduce the stated Margules, van Laar, Wilson, NRTL and Flory–Huggins chemical potentials (largest residual about $1.4\times10^{-10}$ in dimensionless units). vdW reduction algebra agrees to below $6\times10^{-16}$ in the test cases. These numerical derivative checks complement the derivation review; they are not a general proof for every parameter set.
- Phase rule and interfaces: variable/constraint counts for ordinary equilibrium and selective membranes; osmotic equilibrium and its dilute limit; Laplace pressure from interfacial work, Kelvin equation from chemical-potential equality, and boiling-point elevation from solvent activity. Pure solvent against solution has three independent variables; four applies when both sides have independently variable compositions.

Independent recalculation uses `verify.py`; reproducible output is in `independent-results.json` and `numerical-output.txt`. Model derivative/algebra checks and a counterexample to the incorrect local interpretation of fugacity are in `derivation-checks.py` and `derivation-results.json`.

## Numerical examples and corrections

All quantitative examples in this scope were independently recalculated from their stated inputs: ice driving force, vdW departures/inversion temperature, ethanol–water mixture and contraction, water Poynting factors and humidity chemical potential, nitrogen virial fugacity, steam-table integration and PR, activity pressure dependence, Margules tables and parameter fitting, nitrogen–methane VLE, dilute-pressure slope inference, freezing depression and glycol eutectic, regular-solution/FH activities, Wilson/NRTL fitting and curvature, UNIFAC combinatorial values, osmosis, Kelvin droplets and boiling bubbles.

Material findings:

1. The whiskey calculation uses a 40:60 ratio of pure-liquid volumes before mixing. This differs from ordinary ABV, which uses final beverage volume. Define it as an illustrative ethanol–water mixture to preserve the graph-based example and its approximately 3% contraction.
2. Steam integration with the printed coarse table gives $I=-5018.34477$ J mol$^{-1}$, $\phi=0.40792075$ and $f=203.96038$ bar. Publish approximately −5018, 0.408 and 204. The coarse/fine difference is about 0.3%, rather than 3%. PR gives $\kappa=0.87323619$, rounded to 0.873.
3. Rounded infinite-dilution activities 0.509 and 0.288 give Wilson $\Lambda_{12}=2.54353407$ and $\Lambda_{21}=0.74175278$, rounded to 2.544 and 0.742.
4. Redlich–Kister does not impose zero excess entropy or positive deviation. Distinguish the particular regular-solution/vdW derivations from flexible empirical models. Clarify that temperature-dependent FH parameters can represent LCST behaviour and that Wilson extrapolation is contingent on its parameter fit.
5. Constant fusion entropy and enthalpy require the stated negligible liquid–solid heat-capacity difference. Freezing-derived solvent activity predicts osmosis at another temperature only with the corresponding dilute or temperature-independence assumption.
6. Bubble superheat estimates hold surface tension at its 100°C value. Updating only saturation pressure with steam tables does not validate that approximation at large superheat; retain the example while stating its limit.

Remaining differences in examples are compatible with the stated rounding or graph-estimate precision. Nanometre-droplet continuum/incompressibility limits and constant latent-heat/ideal-vapour approximations remain explicit. No extra unresolved scientific finding remains in this review scope after the supplied corrections are applied.

## Figures and external sources

All 13 referenced figures in this scope were opened and visually inspected in four contact sheets (`figures-1.png` through `figures-4.png`) during the interrupted review. Their mathematical meaning and nearby explanatory use were checked. Final relocated-image links and full rendered equations belong to the publication check.

Sources actually opened/read during completion, 2026-10-12:

- [MIT 3.012: Models of the chemical potential](https://ocw.mit.edu/courses/3-012-fundamentals-of-materials-science-fall-2005/db26fd8bd9421c3659931bccdd605328_lec11t.pdf): partial-molar Gibbs energy, Gibbs–Duhem, finite-pressure ideal-gas reference and solution activity. Equation pages 3 and 5 were also opened as screenshots.
- [NIST TDE: Redlich–Kister activity-coefficient model](https://trc.nist.gov/TDE/TDE_Help/Redlich-Kister-AC-Model.htm) and [model parameter temperature dependence](https://trc.nist.gov/TDE/TDE_Help_4_0/ActivityCoefficientModels.htm): polynomial excess Gibbs energy and temperature-dependent coefficients support the excess-entropy correction.
- [IAPWS IF97 release](https://iapws.org/technical-guidance/release/IF97-Rev): water/steam property formulation, region limits and saturation calculations.
- [IAPWS surface-tension release, PDF](https://iapws.org/documents/release/Surf-H2O.download): temperature-dependent surface tension and tabulated change from 58.91 mN/m at 100°C to 39.95 mN/m at 190°C support the bubble-example validity limit.

An older NIST help URL was inaccessible; the working NIST pages above were used. The IUPAC Gold Book fugacity URL returned HTTP 403 and was not used as a consulted source.
