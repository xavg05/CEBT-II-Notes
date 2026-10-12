# SEP-U2 independent cross-review

Reviewer: codex absorption agent, independently of the drying author. Date: 12 October 2026.

Status: independent scientific/numerical/figure review PASSED; owner repairs completed and inspected. No edits made to U2 author files. Root still owns final publication/rendering validation.

## Scope and evidence

Read every original scan p001–p034 individually in bounded batches 1–12,13–24,25–34. Read all 11 drafts and compared source data/graphs/handwritten derivations. Independent Python script: `other/work/scratch/separations/review-U2/independent_check.py`; results: `results.json`. Script does not import or run author code; solves inverse wet-bulb humidity by bisection rather than the author's explicit inverse equation. ASHRAE Psychrometrics chapter actually opened to verify ideal moist-air assumptions and psychrometric definitions: https://handbook.ashrae.org/Handbooks/F25/SI/F25_Ch01/F25_Ch01_si.aspx.

## Scientific rederivation

- U2-01 dry/wet moisture conversion follows conserved dry solid; latent duty is explicitly a lower estimate.
- U2-02 Dalton mole ratio gives H=(Mv/Mg)p/(P−p); inverse p=PH/(epsilon+H). Derived percentage-saturation/RH distinction independently. Approximate graphical numbers distinguished from computed properties.
- U2-03 summed enthalpies per kg dry gas give humid heat s=Cpg+HCpv. Full liquid-makeup balance retained. Differential constant-h slope has vapor sensible term; simple −s/lambda is identified as approximate.
- U2-04 constant humidity cooling gives partial-pressure dewpoint; humidity falls only after condensation.
- U2-05 gas flux to humidity conversion, dry-carrier density, saturated interface at wet bulb and latent-flux energy product all correct. Chilton–Colburn relation yields U/(rho kg)=s(Sc/Pr)^(2/3); wet bulb versus thermodynamic saturation explicitly approximate, not asserted identical.
- U2-06 free/bound/unbound distinctions consistent. Dry-solid balance r=a_wNw and constant-area wet heat model correct. Falling laws vanish at w*; zero-equilibrium fits not extrapolated blindly.
- U2-07 countercurrent balance m(H−H2)=w−w2 and negative driving-force slope correct. Minimum ratio assumes fully wet inlet and gas-path idealisations explicitly stated.
- U2-08 reciprocal time positive limits, transition beta(a−bw)=alpha w and both log integrals independently derived. Rate varies along dryer despite regime name. Pinch/equilibrium divergence correctly explained.
- U2-09 cocurrent operating line positive driving-force/moisture slope; transition below target correctly means one wet branch. Co-/counter-current fully wet equivalence conditional on same endpoint states/coefficient, not on constant local force.
- U2-10 positive reciprocal-area quadrature correct. Experimental chart range stops at w0.5, so source graph is not extrapolated to0.9; complete calculation labelled a specified analytical model example. Refinement shown.
- U2-11 mass balance survives changing solvent; Hwet recalculated locally. Coupled external-heat surface balance and lumped sensible equation consistent with enthalpy removed in evaporated liquid. Negligible interior conduction/temperature gradients identified as model assumptions.

Checked dimensions of flux, dry-gas/solid ratios, heat coefficients, area/mass, latent energy and both time integrals. Checked saturation, zero-force and w→w* limits. Every calculation recomputed independently; hand-read chart values visually checked rather than claimed numerically exact.

## Numerical checks

| Example | Independent result | Draft result |
|---|---|---|
| Wet/dry moisture | z0.4736842,w0.25 | agrees |
| Hsat30°C/100kPa | 0.027578985 | agrees |
| H/Hsat and RH at H0.015 | 54.3892%,55.4634% | agrees |
| Humid heat/enthalpy at40°C,H0.02 | 1.0432,91.748kJ/kgdry | agrees |
| Saturator40°C,H0.01 | Ts22.4265388°C,Hs0.0173527869 | agrees |
| Constant-h saturation | 22.2439869°C | agrees |
| Dewpoint H0.01 | 13.8426717°C | agrees |
| Wet25°C,H0.01 approximate thermodynamic | 17.8460190°C,Hwet0.01298028 | agrees |
| Humidity40°C/wet20°C approximate thermodynamic | 0.00659718,RH14.21556% | agrees |
| Constant wet model | 240s | agrees |
| Cloth gas/transition | mmin66.66667,m80,Hout0.0136,wc0.212 | agrees |
| Countercurrent cloth times | wet13.3416546h,fall1.5028322h,total14.8444867h | agrees |
| Constant-h exhaust temperature | 24.8471826°C | agrees |
| Cocurrent cloth | wc0.02,total14.3340758h | agrees |
| 8/80/800 trapezoids | 15.2316000/14.8487332/14.8445248h | agrees |
| Fixed-flux external heating | 5K | agrees |

Chloroform 192kJ/kg at80°C and1.4kJ/kgdry/K atH0.8 visually confirmed on original auxiliary axes, remain approximate. Independent table values for reciprocal-rate example also agree. No consequential numerical inconsistency found.

## Figures and style

All ten linked u2 PNGs opened individually. Publication figure targets exist. Eleven drafts each have the seven prescribed sections, local consecutive equation tags, defined symbols and prose-only links; no lecturer/PDF/slide references or wikilinks. Independent script stores structural/link evidence. Root must complete final rendered KaTeX/export checks after publication.

Requested owner repairs:

1. `u2-chloroform-chart.png`: top boundary clips humid-heat auxiliary-axis title; move top465→around425 in displayed coordinates. Its label is needed for the worked auxiliary-axis reading.
2. `u2-moisture-isotherm.png`: left boundary clips the moisture-content label; move left25→0.
3. `u2-countercurrent.png`: left boundary clips w1; expand left110→around70. Remove administrative “Solution:” at top if a tighter crop preserves labels.
4. `u2-dewpoint.png`: remove bottom administrative Q1 annotation with tighter bottom around1600 if the dewpoint handwriting remains intact.
5. Optional prose cleanup: remove 'evaluated in Python' and 'Python trapezoidal integration' from study notes U2-08/10; retain computation provenance in work record.

No scientific blocking findings. Owner repaired all consequential clipping and removed implementation mentions. Reviewer reopened the four revised crops and reran independent checks: pass. Humid-heat auxiliary label, moisture-axis label, countercurrent w1 and dewpoint annotation now readable. A residual “Solution:” label on the original diagram is harmless and retained to preserve the physical annotations; a small uninformative corner below the dewpoint graph does not impair interpretation. Review closed.
