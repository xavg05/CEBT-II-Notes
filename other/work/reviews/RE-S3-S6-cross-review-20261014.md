# Independent Reaction Engineering cross-review, 14 October 2026

Reviewer: separate Codex reviewer, not the author. Ownership is restricted to this report and `scratch/coverage-audit-20261014/review/`; no study notes, source PDFs, indexes, PLAN or BOARD edited.

## Scope and evidence

Read the 15 `other/work/drafts/Reaction Engineering II/RE-S*.md` drafts and visually compared the original source pages through the existing rendered images: section 3 pp1–29, section 4 pp1–15, section 5 pp1–7, section 6 pp1–19. Also reviewed RE-01–06 against section 1 pp1–8, using the existing L1 page montages. Equation readings below come from those original page images, not the author's transcription or verification record.

Opened all seven new cropped figures in `notes/Reaction Engineering II/figs/RE-S*.png`; they are legible and match their described subject. Their intended `../figs/` paths resolve from a published topic directory. They do not resolve literally from the draft directory; this is a publisher placement matter, not a demand to change draft links. Final published links and subject-wide equation numbers require publisher verification after approved numbering.

Independently reconstructed the balances, site inventories, probability integrals and gradients, then executed `other/work/tools/python/python.exe other/work/scratch/coverage-audit-20261014/review/independent_re.py`. The output is `independent-re-results.json`: 57 scalar numerical checks passed, plus exothermic/endothermic sign assertions. Direct numerical integrations independently reproduce the spherical/slab effectiveness and diesel RTD survival; finite differences reproduce the apparent order and activation energy. The author's numerical script was not used.

## Findings for owner

1. **Coverage: section 3 p4 process/catalyst table only partly represented.** Include a compact mapping for the supplied industrial processes. Present drafts omit or do not clearly map naphtha reforming/Pt alloys; alkylation/H2SO4, HF or solid acids; ethene/propene polymerisation/Cr and TiCl4/MgCl2; vinyl chloride/Cu chloride; acrylonitrile/Bi–Mo and Fe–Sb oxides; vegetable-oil hydrogenation/Ni; exhaust CO/hydrocarbon oxidation/Pt–Pd; NOx reduction/Rh and vanadium oxides. The p11–12 family table also includes sulfide-based selective reduction/desulfurisation and solid-acid alkylation/polymerisation. Explain sulfide active phases rather than treating oxide precursor labels as the active HDS species. This is the main substantive supplied-source omission.

2. **Small but useful source-detail additions:** section 3 pp9–10 specifies zeolite Y cage diameter approximately 2.5 nm and aperture approximately 0.75 nm, and ZSM-5 channels approximately 0.56 nm; the existing distinction between cage and aperture is correct but lacks these dimensions. Section 3 pp27–28 gives ammonia oxidation around 750–850 °C, NO selectivity 94–98% before improved gauzes, and Rh addition 6–15% with selectivity up to99%. These approximate illustrative ranges can accompany the correct qualitative discussion.

3. **Section 4 small explicit source details:** p2's indicative adsorption enthalpy magnitudes are 10–250 kJ/mol for chemisorption and 5–30 kJ/mol for physisorption; qualify overlap instead of presenting them as a definition. Section 4 p10 gives nitrogen at77K, perfect wetting, `ln(Pcond/Psat)=−0.959 nm/r_curv`. Adding this supplied shortcut, with curvature units explicit and no extra contact-angle factor, makes the original pore-sizing relation directly usable. Current general Kelvin derivation is correct.

4. **Section 5 p7's Cu oxide example is at573K.** Current mechanism, balanced redox cycle, limiting observed orders and isotope evidence are correctly covered. Including the stated temperature preserves this source detail.

5. **Section 1 p2's recalled rate-law examples:** RE-01 correctly treats first-/second-order species conventions but does not explicitly include `r=k C_A C_B` or the recalled Michaelis–Menten form `r=k C_A/(K_M+C_A)`. Include their reagent dependence, `K_M` concentration units, and dilute/saturated limits. This is revision material rather than a new mechanistic derivation.

No numerical or equation defect requiring correction was found in the reviewed drafts. Findings 1 and5 are coverage requests;2–4 are source-detail completions appropriate to the user's exhaustive audit. The initial review requested these additions; the closure record below supersedes that pending status. It does not declare a complete course, because RE sections2,7,8 remain absent.

## Source-to-note coverage and scientific checks

| Original source pages | Draft destination | Independent assessment |
|---|---|---|
| S1 pp1–2 | RE-01 | Rate bases, turnover, signed extent and stoichiometric renormalisation correct. Add recalled rate-law examples above. Course-outline/admin and bibliographic material need not become exam notes. |
| S1 pp3–5 | RE-02/03/04 | General CSTR and PFR balances correctly distinguished from constant-flow closures. Gas expansion is sound added closure. PFR enthalpy product rule avoids double counting heat; all signs and units pass. |
| S1 pp6–8 | RE-04/05/06 | Pressure-drop need, RTD, equal tanks, segregation and first-order mixing independence covered. Added nonlinear reactor-order example correct and shows same tracer RTD, differing conversion. |
| S3 pp1–6 | S3-01/05 | Definition, phases, selectivity, supported metals and syngas routes covered. Industrial table incomplete as finding1. Economic market figures, historical biographies and Nobel list are context, deliberately outside scientific study scope. |
| S3 pp7–11 | S3-01 | Support preparation, activation, oxides/sulfides, framework charge, acid sites and three shape-selectivity types sound; pore numbers absent as finding2. CuO cycle is element balanced. |
| S3 pp12–13 | S3-02 | Sintering, poisons, coke and mechanical loss covered. Independent area derivation A=6V/d correct. Reversible poisoning qualification is scientifically appropriate. |
| S3 pp13–18 | S3-03 | All main bed arrangements, heat exchange, interstage cooling, PFR inverse-rate area and empirical tanks estimates covered. Heat-capacity basis correction sound. Cropped figure uses catalyst-mass rate while derivation uses volume; note explicitly and correctly distinguishes these. |
| S3 pp19–25 | S3-04 | Full diesel calculation, microscopic/segregated equivalence and source's unfinished bed-length exercise completed correctly. At fixed flow with N and tau scaling together, required length factor3.33347; at fixed N required time factor4.32237 relative to original PFR-design baseline. Qualification avoids claiming baseline calibration. |
| S3 pp26–29 | S3-05 | EO, methanol, ammonia oxidation and seven-step transport pathway covered. NO net product and balanced stoichiometry correct. Gauze wire correction from printed70nm to tens of micrometres is physically sensible; author's primary-source evidence still controls precise commercial0.076mm figure. |
| S4 pp1–5 | S4-01 | Adsorption/absorption, uptake basis, isotherm/isobar/isostere, Langmuir balance, thermodynamic T dependence and named isotherms covered. General qualifications improve inaccurate universal exothermicity claims. |
| S4 pp6–7 | S4-02 | Atomic dissociation site count, random-neighbour assumption, shared competition denominator, products and independent site populations correct. |
| S4 pp7–9 | S4-03 | BET column sum and straight-line slope/intercept derivation independently verified. Surface area conversion and273.15K/1bar reference consistent. Finite pore capacity and fitting range limitations covered. |
| S4 pp9–13 | S4-04 | Kelvin pressure sign, curvature averaging, film thickness, cylindrical vs hemispherical emptying, tensile liquid and hysteresis covered. Width-based pore classification is scientifically preferable to ambiguous radius threshold in original. Add nitrogen coefficient as finding3. |
| S4 pp14–15 | S4-04 | Affinity and pressure slope signs distinguished correctly; isosteric released heat is positive while adsorption enthalpy negative. Dissociative Henry-law qualification appropriate. |
| S5 pp1–3 | S5-01/02 | Elementary steps conserve sites; L–H numerator and squared denominator correct. Eley–Rideal swaps A/B roles relative to original, but states definitions consistently and obtains the same mechanism with relabelled species. |
| S5 pp3–6 | S5-02 | Local order1−2thetaA, maximum at half A coverage, apparent barrier with all product terms, and low/high coverage limits correct. Temperature figure illustrates one barrier regime; text covers the negative-slope regime too. |
| S5 pp6–7 | S5-02 | Oxide sites, MvK inventory, harmonic two-step rate, restore cycle, isotope evidence covered; add573K as finding4. |
| S6 pp1–4 | S6-01 | Effective area/pore concentration convention correct; tortuosity qualification suitable. Molecular and Knudsen wall collisions are series resistance, not original's blanket direct sum. Surface flux can add only after loading/area conversion; units pass. |
| S6 pp4–10 | S6-02 | Slab ODE, symmetry, cosh profile, sphere transformation u=rC, central limit, flux-derived effectiveness and generalised length correct. Small/large modulus expansions and normalised geometric comparison pass. |
| S6 pp11–13 | S6-03 | Power-law strong-limit integral, order(n+1)/2, barrier half-limit, zero-order dead-core qualification and external-film balance correct. Internal vs overall effectiveness clearly distinguished. |
| S6 pp14–17 | S6-04 | Coupled heat/concentration signs, volume-average factor3, Arrhenius ratio and Prater bound re-derived correctly. Source's missing normalisation factor and sign ambiguities corrected. Kinetic-sensitivity caveat improves rough beta≤0.02 heuristic. |
| S6 pp17–19 | S6-04 | Surface heat balance, Wakao range, multiplicity/stability, finite supply temperature bound and external-film vs internal-diffusion rates correct. Keeping kg/h prevents original's dimensional error. Source's suggested sustained oscillation is properly distinguished from steady multiplicity. |

## Independent numerical results

Diesel: initial PFR41.713498s, Re11.986528; target PFR125.140494s; ten-tank survival at that time0.00523769816; chain target180.301144s; proportional-length factor3.33346750. The explicit length-extension equation reproduces remaining fraction0.001.

BET: Vm10cm3, C10, monolayer0.000440316145mol, total area42.956662m2, specific area429.566620m2/g. Isosteric example gives−27.663102kJ/mol.

Pellets at raw modulus2: direct slab integral0.482013790; direct sphere volume integral0.805972081; centre fraction0.551441130. Film surface/bulk0.788234894 and overall effectiveness0.635295318. Prater rise5K, beta0.01;500→505K intrinsic rate factor1.20989123.

Finite differences reproduce L–H order and Eapp including product inhibition. BET column sums normalise to1; direct RTD integration normalises to0.999999996 and exactly reproduces the ten-tank survival to numerical precision.

## External access limitations

To independently check niche source corrections, searched for primary Johnson Matthey gauze and IUPAC physisorption references. Opened the Johnson Matthey [Knitted Gauze for Ammonia Oxidation](https://technology.matthey.com/content/journals/10.1595/003214091X3525864) landing page; it did **not** expose readable article full text in this browser. The full-text endpoint was inaccessible. IUPAC1985 PDF and2001 terminology requests returned403; the hosted2015 report timed out. Those unsuccessful requests are **not** evidence for the precise wire dimension or modern pore taxonomy and are not claimed as read supporting sources. Review of independently derived mass/energy equations and existing source images did not depend on those endpoints. Before final delivery, retain the author's successfully read primary evidence for those external corrections.

## Closure after owner corrections

Reread the author's changed S3-01, S3-05, S4-01, S4-04 and RE-01 in full. Full process table, correctly labelled oxide/sulfide active systems and oxychlorination rather than ambiguous final vinyl-chloride step now cover finding1. Rate laws, units and saturating limits close finding5. Adsorption ranges, nitrogen curvature shortcut and hot-gauze operating ranges correctly close findings2–3; owner reports573K also added to S5-02, checked by targeted reread below. Specific Y cage2.5nm should not be repeated without authoritative confirmation; the aperture/cage conceptual distinction is fully covered. Approximate window numbers are optional illustrative context, not a missing scientific topic or unresolved review blocker.

**Scientific cross-review passes for supplied RE sections1,3,4,5,6**, with57 independent numerical checks and all seven new source crops opened. Final publication checks belong to the coordinator: provisional section identifiers, continuous equation numbers, portable maths/export and actual GitHub links must be validated after publishing. No remaining consequential scientific finding identified in this review. Missing sections2,7,8 still limit full-course exam readiness.
