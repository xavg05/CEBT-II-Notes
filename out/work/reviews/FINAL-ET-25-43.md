# Final independent scientific review: ET-25–43

Reviewer: independent Codex subagent, 12 October 2026. Scope: merged units 07–12, all prose and formulas in Sections 25–43 of `notes/equilibrium-thermodynamics/complete-obsidian.md`, checked against the archived merges for exact corrections. Read AGENTS.md, CLAUDE.md, PLAN.md and BOARD before review. No original or delivery notes edited.

Status: scientific review complete; 27 corrections supplied for parent application. Recheck their application before marking delivery reviewed. Component-label corruption in the existing complete edition is a separate global publishing defect already assigned to the parent. No unresolved scientific blocker remains after the listed corrections are applied.

## Findings

Exact old/new text, archived source filenames, reasons and severity are in `out/work/scratch/final-et-25-43/corrections.json`. The correction script validates each old substring occurs exactly once in its archived merge. Corrections do not overlap.

High severity:

- Section 34: worked example simultaneously assigns gamma*=gamma#=1 to the same finite-concentration solution. Exact standard-state conversion forbids this. Use one ideal mole-fraction solution, gamma*=1, gamma#=0.9910729, a#=0.4955365, a*=0.00892709, and unchanged ideal solvent activity 0.9910729. Standard chemical potentials differ by RT ln(M_s m°).
- Section 32: equal compositions alone do not identify criticality. An azeotrope has equal compositions but distinct phase densities; the trivial equal-root EOS flash solution exists away from criticality. Correct criticality explanation to require convergence of density and composition and the second/third variation stability conditions.

Medium severity:

- Normalise molality and ionic activities by standard molality everywhere; define mean ionic molality.
- Distinguish spinodal local stability from binodal equilibrium splitting and positive curvature from global stability.
- Qualify critical-locus topology to the simple binaries considered rather than all binaries.
- Explain that homogeneous bulk chemical-potential formulas omit gradient free energy in diffuse interfaces.
- Specify van Laar parameters and reject trivial equal-composition roots in LLE solving.
- Distinguish pure methane fugacity coefficient from its partial coefficient in nitrogen-rich gas.
- Separate dilute Debye–Hückel screening/salting-in from high-salt protein salting-out.
- Handle exactly heteroazeotropic overall composition: both liquid layers can finish vaporising together at T*.
- Replace unsupported “under 0.1%” mutual-solubility statement with the actual immiscible-limit assumption.
- Clarify that vanishing mutual diffusivity does not mean vanishing molecular self-diffusion. The 0.64 exponent represents coupled critical fluctuations and hydrodynamic transport; simple arithmetic averaging of Gamma is a heuristic, not its derivation.

Low severity:

- Spinodal at −10 °C rounds to 0.341, not 0.342.
- NaCl limiting-law coefficient at m=0.01 with alpha=1.171 rounds to 0.889, not 0.890.
- Give reproducible NIST Antoine inputs for steam distillation.
- Remove unsubstantiated specific attribution of the regular-solution azeotrope error to benzene pi electrons.

## Independent derivations

- Sections 25–26: equal fugacities, component balances, lever rule and y=Kx derive phase amounts; integrate d ln f=V dP/RT for Poynting factor; sum modified Raoult equations for bubble pressure and reciprocal dew pressure.
- Sections 27–28: differentiate total bubble pressure and apply Gibbs–Duhem to factor its derivative; derive azeotropic x=y and Margules candidate composition; divide van Laar log-gamma equations, invert algebraically and verify fitted activities and predicted P/y.
- Sections 29–31: gas/liquid fugacity equality gives ideal solubility and gamma=xideal/x; take the dilute-limit slope to obtain H=gamma-infinity*f-liquid; change reference to derive gamma*=gamma/gamma-infinity; integrate van't Hoff temperature form.
- Sections 34–35: exact molality/mole-fraction conversion with shifted standard potential gives gamma# relation; add ionic chemical potentials to derive stoichiometric product activities and geometric mean gamma; electroneutrality reduces weighted squared charges to |z+z−| in the mean limiting law. Debye–Hückel's Poisson/Boltzmann derivation is explicitly beyond course depth; its stated result and dimensions were checked.
- Sections 36–39: differentiate g=sum x mu at fixed T,P and use Gibbs–Duhem to derive tangent intercepts, g'=mu1−mu2, mu1'=(1−x)g'', mu2'=−xg'', and Gamma=x(1−x)g''/RT. Common tangent imposes equality of both chemical potentials. Regular solution g''/RT=1/[x(1−x)]−2A/RT and g'''=0 give Tc=A/(2R), xc=1/2. For van Laar gex/RT=alpha*beta*x(1−x)/[alpha*x+beta*(1−x)], second derivative is −2 alpha² beta²/[alpha*x+beta*(1−x)]³.
- Sections 40–41: convert composition gradients to chemical-potential gradients to derive D12=D*Gamma and regular-solution Gamma=1−2Ax(1−x)/RT. The modified exponent is empirical, not a first-principles derivation.
- Sections 42–43: phase rule gives one intensive freedom for binary VLLE; equality of all fugacities and the immiscible limit give P=sum Psat, yorg=Psatorg/P and steam mass ratio=Psatwater*Mwater/(Psatorg*Morg).

All equations are dimensionally and algebraically consistent after the reported corrections. Limits checked: ideal mixture, pure endpoints, infinite dilution, critical/binodal/spinodal distinction, and immiscible steam distillation. EOS models and empirical transport powers retain their explicit limitations.

## Numerical evidence

`out/work/scratch/final-et-25-43/verify.py` is an independent standard-library Python calculation. `numerical-evidence.json` and `numerical-output.txt` preserve results. All assigned worked examples with calculable numbers were rerun; conceptual phase-rule and graph-reading examples were checked directly.

- ET-25 NIST Antoine: bubble 92.0627 °C, dew 98.7202 °C; at 95 °C x1=0.40223, y1=0.62490, V=0.43909. Small difference from note x1=0.404,V=0.43 is consistent with a different vapor-pressure dataset; the stated K1=1.550,K2=0.628 imply V≈0.436. No material correction needed.
- ET-26 P=0.9525 bar,y1=0.714961; Poynting 0.9986799,1.0015636.
- ET-27 A=385.4778 J/mol; independent NIST Antoine azeotrope 79.3389 °C,xbenzene=0.566933, reproducing note's estimate.
- ET-28 alpha=1.15465794,beta=1.52046076; at x=0.1647 P=1.10747336 bar,y=0.41110637; relative error 4.70888%, range error9.07422%; Margules P=1.10216901 bar.
- ET-30 xideal=0.00603335; gamma=2.91466,2.10956,2.13193; apparent H=489.372,354.196,357.951 bar.
- ET-31 dissolved O2=8.67349 mg/L,N2=13.32 mg/L; H5C=28537.47 atm and solubility ratio1.50679.
- ET-35 all salt table entries independently reproduced, with the one rounding correction above. Debye lengths9.61370,0.961370nm.
- ET-36 binodal0.1447941/0.8552059; splitting gain89.4283 J/mol at300K.
- ET-37 all binodal/spinodal table entries reproduced with the −10C rounding correction above.
- ET-38 common activities agree to floating-point accuracy; binodal0.112806955/0.928432795; spinodal0.270202225/0.805234720; minima0.106775735/0.924261054; phaseI fraction0.52528105.
- ET-39/40 curvature and thermodynamic-factor tables reproduced.
- ET-41 entire illustrative Gamma/Gamma^0.64 table reproduced. Published Redlich–Kister coefficients and raw experimental diffusion data are not included in the notes; did not refit that dataset. Visual plot supports the reported trend and model comparison.
- ET-43 NIST Antoine: toluene T*=84.3361C,y=0.444132,steam ratio0.244715,mass fraction0.803397; decane T*=97.5173C,y=0.0854039,steam ratio1.355950. All delivered values reproduced to their stated precision.

## Figures and limits of audit

All 23 figure files referenced in assigned sections were visually opened via four labelled contact sheets under scratch. Paths resolve and figures agree with nearby explanations. Plots read as estimates retain approximate precision. The ET-33 envelope schematic is too coarse to justify refining its approximate critical/envelope coordinate readouts.

This is an independent audit of final prose, formulas, examples and existing cropped figures. It is not a fresh full page-by-page audit of all source PDFs, nor a new independent reconstruction of experimental datasets. The parent performs final rendering and publication checks.

## Primary external sources actually opened and read

- [NIST Chemistry WebBook: benzene](https://webbook.nist.gov/cgi/cbook.cgi?ID=C71432&Mask=4), [toluene](https://webbook.nist.gov/cgi/cbook.cgi?ID=C108883&Mask=4), [water](https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185&Mask=4), [n-decane](https://webbook.nist.gov/cgi/cbook.cgi?ID=C124185&Mask=4), [cyclohexane](https://webbook.nist.gov/cgi/cbook.cgi?ID=C110827&Mask=4): Antoine data and pure boiling-point checks.
- [DTU electrolyte thermodynamics compendium](https://backend.orbit.dtu.dk/ws/files/131770579/ElectrolyteCompendium.pdf), section4.4,p18: dimensional standard molality and exact activity-coefficient conversion.
- [Kamgar et al., Mutual diffusion in concentrated liquid solutions: a new model based on cluster theory, author manuscript](https://api.repository.cam.ac.uk/server/api/core/bitstreams/011354f3-868f-403c-99d5-346254aee70d/content), pp1–7: thermodynamic-factor transport, critical cluster/fluctuation effects and0.64 empirical power.

IUPAC standard-molality and solubility PDF pages and the QuCosa diffusion proceedings PDF could not be retrieved through browsing; they were not used as evidence.
