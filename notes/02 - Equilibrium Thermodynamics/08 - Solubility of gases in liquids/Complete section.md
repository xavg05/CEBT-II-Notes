[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Solubility of gases in liquids

## Overview

A gas above its critical temperature has no pure liquid to serve as the activity-coefficient reference. One fix extrapolates the vapour-pressure curve to a hypothetical liquid fugacity, best read from a corresponding-states chart, giving a solvent-independent ideal solubility (Section 29). For methane in three solvents this gives activity coefficients of 2–3 from measured solubilities (Section 30). The other fix uses Henry's constant as the reference: the dilute-limit slope of fugacity against mole fraction, with its own activity coefficient $`\gamma^{*}`$ (Section 31).

*Assumed throughout:* the γ–φ formulation (Section 26); infinite-dilution activity coefficients (Section 14); corresponding states.

## Section 29: Gas solubility, the hypothetical liquid and ideal solubility

### Intuition

Above $`T_c`$ there is no vapour-pressure curve to read $`P^{\mathrm{SAT}}`$ from. But the curve does not stop abruptly in any physical sense; it just ends at the critical point. Continue it smoothly past $`T_c`$ and read off a "vapour pressure" at the temperature of interest. That value describes a liquid that cannot exist on its own, but it is a perfectly good *reference number*, as long as every calculation uses it consistently.

Ideal solubility then asks: if the dissolved gas mixed ideally with the solvent ($`\gamma = 1`$), how much would dissolve? The answer depends only on the gas, not on the solvent, which makes it a useful yardstick.

### Derivation

**Step 1: the equilibrium condition.**


**Equation (139)**

```math
\gamma_ix_if_i^{\,l}(T,P) = \bar f_i^{\,v} \approx y_iP
```


The vapour approximation holds at modest pressure; for a gas well above $`T_c`$ at a fraction of $`P_c`$, $`\phi\approx 1`$.

**Step 2: the reference fugacity.** For $`T < T_c`$, $`f_i^{\,l}\approx P_i^{\mathrm{SAT}}`$ (neglecting $`\phi^{\mathrm{SAT}}`$ and the Poynting factor). For $`T > T_c`$ this is undefined, so extrapolate the saturation line beyond the critical point to define a hypothetical "$`P_i^{\mathrm{SAT}}(T)`$" and hence $`f_i^{\,l}`$.

![Extending the vapour-pressure curve past the critical point gives a hypothetical liquid fugacity at T2 > Tc](../figs/ET-29-hypothetical-liquid-extrapolation.png)

**Step 3: a corresponding-states chart.** Simple extrapolation (e.g. Clausius–Clapeyron) becomes unreliable far above $`T_c`$. Prausnitz and Shair instead back-calculated $`f_i^{\,l}`$ from solubility data for many gases. They found that $`f_i^{\,l}/P_c`$ falls on a single curve when plotted against the reduced temperature $`T_r = T/T_c`$ (corresponding states). One chart then serves for all simple gases.

**Step 4: ideal solubility.** Set $`\gamma_i = 1`$ in (139):


**Equation (140)**

```math
x_i^{\mathrm{ideal}} = \frac{\bar f_i^{\,v}}{f_i^{\,l}} \approx \frac{y_iP}{f_i^{\,l}}
```


**Step 5: activity coefficient from measured solubility.** Comparing (139) and (140):

The hypothetical liquid is a reference for the chemical potential, not a proposed second phase above the pure solute's critical temperature. Changing its assigned fugacity changes the corresponding $`\gamma_i`$ inversely, leaving the measurable product $`x_i\gamma_if_i^{\,l}`$ unchanged. The convention is useful only when the reference and activity coefficient are used together consistently.

Accordingly, solvent-independent ideal solubility is a benchmark for that convention, not a claim that all real solvents behave alike. Measured departures from it put the solvent preference into $`\gamma_i`$. Henry's constant later combines the reference fugacity and dilute preference into one measurable coefficient, avoiding this hypothetical reference in routine design.


**Equation (141)**

```math
\gamma_i = \frac{\bar f_i^{\,v}}{x_if_i^{\,l}} = \frac{x_i^{\mathrm{ideal}}}{x_i}
```


So the ratio of ideal to measured solubility *is* the activity coefficient of the dissolved gas.

### Motivation and explanation

**Why solvent-independent.** Equation (140) contains only properties of the gas ($`f_i^{\,l}`$) and of the vapour ($`y_iP`$). Every solvent would dissolve the same amount if mixing were ideal. Real solvents differ through $`\gamma_i`$, which by (141) is read straight from measurements.

**Trends.**
- Gases with low $`T_c`$ (He, H₂, N₂) are far above $`T_c`$, so $`f^{\,l}`$ is large and solubility is low.
- Gases closer to $`T_c`$ (CO₂, ethane) have a smaller hypothetical vapour pressure and are more soluble.
- Solubility is proportional to the gas partial pressure (at fixed $`f^{\,l}`$), the root of Henry's law (Section 31).

**Limits.** The hypothetical liquid is a convention, so $`\gamma`$'s computed with it depend on that convention. The chart is for non-polar gases at modest pressure. Polar or reacting gases (NH₃, SO₂, CO₂ in water) need other treatments.

### Link to other topics

Gas solubility governs absorption columns (CO₂ capture, acid-gas removal), bioreactor aeration, and gas–liquid reactors. Section 30 works through ideal and real solubilities for methane in three solvents.

### Summary

For a supercritical solute the pure-liquid reference is hypothetical, and its fugacity is obtained by extrapolating the saturation curve, best done with a corresponding-states chart of $`f^{\,l}/P_c`$ against $`T/T_c`$. The ideal solubility $`x^{\mathrm{ideal}} = y_iP/f_i^{\,l}`$ is solvent-independent, and the ratio $`x^{\mathrm{ideal}}/x`$ is the gas's activity coefficient in a given solvent.

## Section 30: solubility of methane

### Intuition

Methane at 25 °C is far above its critical temperature (−82.6 °C), so its hypothetical liquid is extremely "volatile". Even ideally, it dissolves only at the parts-per-thousand level at 10 bar. The solvents are all non-polar, so methane should be modestly unhappy in each ($`\gamma > 1`$), most so in the solvent least like itself.

### Derivation

**Problem.** At $`T = 25`$ °C and $`P = 10.13`$ bar, a gas of $`y_{\mathrm{CH_4}} = 0.1`$ (rest nitrogen) is in equilibrium with each solvent. Measured methane mole fractions: benzene $`2.07\times10^{-3}`$, CCl₄ $`2.86\times10^{-3}`$, cyclohexane $`2.83\times10^{-3}`$. Critical constants: CH₄ $`T_c = 190.6`$ K, $`P_c = 46.0`$ bar; N₂ $`T_c = 126.2`$ K, $`P_c = 33.9`$ bar.

**Step 1: vapour fugacity.** Both gases have $`T\gg T_c`$ and $`P\ll P_c`$, so treat the vapour as an ideal-gas mixture:

```math
\bar f^{\,v}_{\mathrm{CH_4}} = y_{\mathrm{CH_4}}P = 1.013\ \text{bar}.
```

Nitrogen is assumed not to affect methane's solubility (each gas dissolves independently at these dilutions).

The gas supplies methane according to its partial fugacity, not according to the pressure gauge alone. In the ideal-gas approximation, increasing nitrogen at fixed methane partial pressure raises total pressure without increasing methane's dissolution driving force. Increasing total pressure at fixed gas composition does increase that force. Stating what is fixed is essential when using the example to predict the effect of pressurisation.

All three solvent measurements use the same gas-side methane fugacity and the same hypothetical-liquid reference. Their different dissolved mole fractions therefore isolate the solvent effect in $`\gamma`$. A common uncertainty in the chart shifts all the inferred coefficients together; it cannot account for the measured ordering of the solvents.

**Step 2: hypothetical liquid fugacity.** $`T_r = 298.2/190.6 = 1.56`$. The chart gives $`f^{\,l}/P_c\approx 3.65`$, so $`f^{\,l}_{\mathrm{CH_4}}\approx 3.65\times46.0 = 168`$ bar. This is a value read from a graph.

![Corresponding-states chart for the hypothetical liquid fugacity of dissolved gases: at Tr = 1.56, f^L/Pc ≈ 3.65 for methane](../figs/ET-30-prausnitz-shair-chart.png)

**Step 3: ideal solubility.**

```math
x^{\mathrm{ideal}}_{\mathrm{CH_4}} = \frac{1.013}{167.9} = 6.03\times10^{-3}
```


**Step 4: activity coefficients and Henry's constants.** $`\gamma = x^{\mathrm{ideal}}/x`$, and $`\bar f^{\,v}/x`$ is the apparent Henry's constant (Section 31):

| Solvent | $`x_{\mathrm{CH_4}}`$ | $`\gamma_{\mathrm{CH_4}}`$ | $`\bar f^{\,v}/x`$ (bar) |
|---|---|---|---|
| benzene | $`2.07\times10^{-3}`$ | 2.91 | 489 |
| CCl₄ | $`2.86\times10^{-3}`$ | 2.11 | 354 |
| cyclohexane | $`2.83\times10^{-3}`$ | 2.13 | 358 |

### Motivation and explanation

**All $`\gamma > 1`$.** Methane is less soluble in every solvent than an ideal mixture would allow. As small, weakly attracting molecules, methane pays to break the stronger solvent–solvent attractions in order to fit in.

**Why benzene is the worst solvent.** In regular-solution terms, $`\ln\gamma\propto(\delta_{\mathrm{CH_4}} - \delta_{\mathrm{solvent}})^2`$. Methane's (hypothetical-liquid) solubility parameter is low. Benzene has the highest $`\delta`$ of the three (18.7 MPa^½ against 16.8 for cyclohexane, Section 17), so it is the most unlike methane and dissolves it least. Cyclohexane and CCl₄ have similar, lower $`\delta`$'s and almost equal $`\gamma`$'s.

**Accuracy.** $`f^{\,l}`$ comes from a correlation read off a log-scale chart, so the absolute $`\gamma`$'s carry several percent uncertainty. The *ratios* between solvents do not depend on $`f^{\,l}`$ at all, since they come straight from the measured $`x`$'s. The ranking is therefore robust.

**Assumptions to check.**
- Ideal-gas vapour: at 10 bar and $`T_r = 1.56`$, a representative pure-methane fugacity coefficient is about 0.98, suggesting a correction of a few percent. The methane fugacity coefficient in the nitrogen-rich mixture requires a mixture EOS.
- No nitrogen effect: reasonable at mole fractions of $`10^{-3}`$.
- Solvent vapour in the gas phase: neglected. Benzene's vapour pressure at 25 °C is about 0.13 bar, small compared with 10 bar.

### Link to other topics

The same calculation sizes absorbers for natural-gas processing. The apparent Henry's constants in the table are what designers usually tabulate, which is the motivation for the Henry's-law standard state in the next section.

### Summary

At 25 °C and 1.01 bar partial pressure, methane's hypothetical liquid fugacity of about 168 bar gives an ideal solubility of $`6.0\times10^{-3}`$. Measured solubilities are 2–3 times lower, giving $`\gamma_{\mathrm{CH_4}}`$ = 2.1–2.9, with benzene the least favourable solvent because its cohesive energy differs most from methane's.

## Section 31: Henry's law and the Henry standard state

### Intuition

A dilute solute molecule is surrounded entirely by solvent. Adding a few more solute molecules does not change that environment, so each behaves the same, and the escaping tendency is simply proportional to how many there are. The proportionality constant reflects how comfortable one solute molecule is among solvent molecules. That is exactly the infinite-dilution activity coefficient times the pure-liquid fugacity.

Raoult's law is the opposite limit: the *solvent*, nearly pure, behaves as if it were alone. Every dilute binary obeys Raoult for the solvent and Henry for the solute at the same time, and Gibbs–Duhem guarantees the two are consistent.

### Derivation

**Step 1: dilute limit.** As $`x_i\to 0`$, $`\gamma_i\to\gamma_i^{\infty}`$, a constant at fixed $`T`$ (and pressure, to a good approximation). Then


**Equation (142)**

```math
\bar f_i = \gamma_ix_if_i^{\,l}\;\to\;x_i\,\gamma_i^{\infty}f_i^{\,l}\equiv x_iH_i(T)
```



**Equation (143)**

```math
H_i = \gamma_i^{\infty}f_i^{\,l}
```


$`H_i`$ has units of pressure and depends on $`T`$ and on both the solute and the solvent. It can be measured directly as $`\lim_{x_i\to0}\bar f_i/x_i`$, without ever constructing $`f_i^{\,l}`$.

**Step 2: a new standard state.** The conventional activity uses the pure liquid as reference, $`a_i = x_i\gamma_i = \bar f_i/f_i^{\,l}`$, so $`a_i = 1`$ for pure $`i`$. Instead, use $`H_i`$ as the reference fugacity:


**Equation (144)**

```math
a_i^{*} = x_i\gamma_i^{*} = \frac{\bar f_i}{H_i} \qquad\Rightarrow\qquad \bar f_i = \gamma_i^{*}x_iH_i
```


**Step 3: how the two activity coefficients relate.** Dividing (144) by $`\bar f_i = \gamma_ix_if_i^{\,l}`$ and using (143):


**Equation (145)**

```math
\gamma_i^{*} = \frac{\gamma_i}{\gamma_i^{\infty}}
```


So $`\gamma_i^{*}\to 1`$ as $`x_i\to 0`$, while $`\gamma_i\to 1`$ as $`x_i\to 1`$. The two conventions are normalised at opposite ends.

Normalising the dilute coefficient to unity does not remove the solute–solvent interactions. It puts their dilute-limit effect into $`H_i`$ and the corresponding standard chemical potential. A poorly soluble gas can therefore obey Henry's law very accurately while having a large Henry constant: every solute molecule experiences the same unfavourable environment, so the response is linear even though dissolution is difficult.

For the pressure-over-mole-fraction convention used here, $`x_i=\bar f_i/H_i`$ at fixed temperature. A larger $`H_i`$ means less dissolved gas at a given fugacity. Other tabulations use the reciprocal convention, so the stated units and defining relation matter as much as the name of the constant.

**Step 4: graphical meaning.** On a plot of $`\bar f_i`$ against $`x_i`$:
- Henry's law is the tangent at $`x_i = 0`$, reaching $`H_i`$ at $`x_i = 1`$;
- Raoult's law (ideal mixture) is the straight line to $`f_i^{\,l}`$.

At any composition A, with the real curve at D, the Henry line at C and the Raoult line at B: $`\gamma_i^{*} = AD/AC`$ and $`\gamma_i = AD/AB`$.

![Henry and Raoult reference lines for a dissolved gas: γ* = AD/AC measures deviation from the Henry line, γ = AD/AB from the (hypothetical) Raoult line](../figs/ET-31-henry-vs-raoult.png)

### Motivation and explanation

**A small dissolved inventory needs continual replenishment.** For oxygen in water at 298.15 K, $`H=4.3\times10^4`$ atm and oxygen partial pressure 0.21 atm give $`x_{\mathrm{O_2}}\approx4.9\times10^{-6}`$. Taking 55.5 mol water per litre gives about $`8.7\ \mathrm{mg\,L^{-1}}`$. This small equilibrium inventory helps explain why an aerobic bioreactor can be oxygen-transfer limited even while its gas phase contains abundant oxygen.
With $`H(T)=H(298.15)\exp[-1700(1/T-1/298.15)]`$, the same gas fugacity gives about 1.51 times as much dissolved oxygen at 278.15 K. Holding fugacity fixed is essential in interpreting that temperature comparison. Henry-scale ideality means a linear dilute response with $`\gamma^*\to1`$; it does not mean dissolution is favourable or the inventory large.

**Why switch reference.** For a supercritical gas, $`f_i^{\,l}`$ is hypothetical and must come from an extrapolation or correlation (Section 29). $`H_i`$ is measured directly in the dilute region where the gas actually lives, and then $`\gamma_i^{*}\approx 1`$. Any standard state is allowed, as long as it is used consistently.

**Temperature dependence.** $`\ln H_i`$ usually varies with $`1/T`$ through the enthalpy of solution (a van 't Hoff form). For permanent gases in water near room temperature, dissolution is exothermic, so $`H`$ falls and solubility rises as temperature falls. That is why cold water holds more oxygen.

**Limits.** Henry's law is a limiting law. It fails as $`x_i`$ grows (then $`\gamma_i^{*}\neq 1`$) and for gases that react or ionise in the solvent: CO₂, NH₃ and SO₂ in water dissolve far beyond the Henry value because of the chemistry. At high pressure, the gas-phase fugacity and the pressure dependence of $`H`$ (through the partial molar volume of the solute) must be included.

### Link to other topics

Henry's constants are the standard input for absorber and stripper design and for gas–liquid mass transfer in bioreactors, where the oxygen saturation concentration sets the transfer driving force. The infinite-dilution activity coefficient in (143) links back to ebulliometry (Section 14), which measures it for condensable solutes.

### Summary

In the dilute limit the solute fugacity is linear in mole fraction, $`\bar f_i = x_iH_i`$, with $`H_i = \gamma_i^{\infty}f_i^{\,l}`$. Using $`H_i`$ as the standard state removes the need for a hypothetical liquid and gives an activity coefficient $`\gamma_i^{*}`$ that is 1 at infinite dilution. Applied to air and water, it predicts the familiar ~9 mg L⁻¹ of dissolved oxygen and its rise on cooling.

## Conclusion

Gas solubility is ordinary phase equilibrium with an awkward reference state. The hypothetical liquid gives an ideal solubility and activity coefficients; Henry's constant avoids the hypothetical state and is the standard design input, predicting for example about 9 mg L⁻¹ of dissolved oxygen in water at 25 °C. The next part moves to high pressure, where vapour and liquid approach each other near critical points.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)
