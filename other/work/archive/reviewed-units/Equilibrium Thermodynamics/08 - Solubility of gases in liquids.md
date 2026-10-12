# Solubility of gases in liquids

## Overview

A gas above its critical temperature has no pure liquid to serve as the activity-coefficient reference. One fix extrapolates the vapour-pressure curve to a hypothetical liquid fugacity, best read from a corresponding-states chart, giving a solvent-independent ideal solubility (Section 29). For methane in three solvents this gives activity coefficients of 2–3 from measured solubilities (Section 30). The other fix uses Henry's constant as the reference: the dilute-limit slope of fugacity against mole fraction, with its own activity coefficient $\gamma^{*}$ (Section 31).

*Assumed throughout:* the γ–φ formulation (Section 26); infinite-dilution activity coefficients (Section 14); corresponding states.

## Section 29: Gas solubility, the hypothetical liquid and ideal solubility

### Intuition

Above $T_c$ there is no vapour-pressure curve to read $P^{\mathrm{SAT}}$ from. But the curve does not stop abruptly in any physical sense; it just ends at the critical point. Continue it smoothly past $T_c$ and read off a "vapour pressure" at the temperature of interest. That value describes a liquid that cannot exist on its own, but it is a perfectly good *reference number*, as long as every calculation uses it consistently.

Ideal solubility then asks: if the dissolved gas mixed ideally with the solvent ($\gamma = 1$), how much would dissolve? The answer depends only on the gas, not on the solvent, which makes it a useful yardstick.

### Derivation

**Step 1: the equilibrium condition.**

$$\gamma_ix_if_i^{\,l}(T,P) = \bar f_i^{\,v} \approx y_iP \tag{139}$$

The vapour approximation holds at modest pressure; for a gas well above $T_c$ at a fraction of $P_c$, $\phi\approx 1$.

**Step 2: the reference fugacity.** For $T < T_c$, $f_i^{\,l}\approx P_i^{\mathrm{SAT}}$ (neglecting $\phi^{\mathrm{SAT}}$ and the Poynting factor). For $T > T_c$ this is undefined, so extrapolate the saturation line beyond the critical point to define a hypothetical "$P_i^{\mathrm{SAT}}(T)$" and hence $f_i^{\,l}$.

![Extending the vapour-pressure curve past the critical point gives a hypothetical liquid fugacity at T2 > Tc](figs/ET-29-hypothetical-liquid-extrapolation.png)

**Step 3: a corresponding-states chart.** Simple extrapolation (e.g. Clausius–Clapeyron) becomes unreliable far above $T_c$. Prausnitz and Shair instead back-calculated $f_i^{\,l}$ from solubility data for many gases. They found that $f_i^{\,l}/P_c$ falls on a single curve when plotted against the reduced temperature $T_r = T/T_c$ (corresponding states). One chart then serves for all simple gases.

**Step 4: ideal solubility.** Set $\gamma_i = 1$ in (139):

$$x_i^{\mathrm{ideal}} = \frac{\bar f_i^{\,v}}{f_i^{\,l}} \approx \frac{y_iP}{f_i^{\,l}} \tag{140}$$

**Step 5: activity coefficient from measured solubility.** Comparing (139) and (140):

$$\gamma_i = \frac{\bar f_i^{\,v}}{x_if_i^{\,l}} = \frac{x_i^{\mathrm{ideal}}}{x_i} \tag{141}$$

So the ratio of ideal to measured solubility *is* the activity coefficient of the dissolved gas.

### Motivation and explanation

**Why solvent-independent.** Equation (140) contains only properties of the gas ($f_i^{\,l}$) and of the vapour ($y_iP$). Every solvent would dissolve the same amount if mixing were ideal. Real solvents differ through $\gamma_i$, which by (141) is read straight from measurements.

**Trends.**
- Gases with low $T_c$ (He, H₂, N₂) are far above $T_c$, so $f^{\,l}$ is large and solubility is low.
- Gases closer to $T_c$ (CO₂, ethane) have a smaller hypothetical vapour pressure and are more soluble.
- Solubility is proportional to the gas partial pressure (at fixed $f^{\,l}$), the root of Henry's law (Section 31).

**Limits.** The hypothetical liquid is a convention, so $\gamma$'s computed with it depend on that convention. The chart is for non-polar gases at modest pressure. Polar or reacting gases (NH₃, SO₂, CO₂ in water) need other treatments.

### Link to other topics

Gas solubility governs absorption columns (CO₂ capture, acid-gas removal), bioreactor aeration, and gas–liquid reactors. Section 30 works through ideal and real solubilities for methane in three solvents.

### Summary

For a supercritical solute the pure-liquid reference is hypothetical, and its fugacity is obtained by extrapolating the saturation curve, best done with a corresponding-states chart of $f^{\,l}/P_c$ against $T/T_c$. The ideal solubility $x^{\mathrm{ideal}} = y_iP/f_i^{\,l}$ is solvent-independent, and the ratio $x^{\mathrm{ideal}}/x$ is the gas's activity coefficient in a given solvent.

## Section 30: Worked example, solubility of methane

### Intuition

Methane at 25 °C is far above its critical temperature (−82.6 °C), so its hypothetical liquid is extremely "volatile". Even ideally, it dissolves only at the parts-per-thousand level at 10 bar. The solvents are all non-polar, so methane should be modestly unhappy in each ($\gamma > 1$), most so in the solvent least like itself.

### Derivation

**Problem.** At $T = 25$ °C and $P = 10.13$ bar, a gas of $y_{\mathrm{CH_4}} = 0.1$ (rest nitrogen) is in equilibrium with each solvent. Measured methane mole fractions: benzene $2.07\times10^{-3}$, CCl₄ $2.86\times10^{-3}$, cyclohexane $2.83\times10^{-3}$. Critical constants: CH₄ $T_c = 190.6$ K, $P_c = 46.0$ bar; N₂ $T_c = 126.2$ K, $P_c = 33.9$ bar.

**Step 1: vapour fugacity.** Both gases have $T\gg T_c$ and $P\ll P_c$, so treat the vapour as an ideal-gas mixture:
$$\bar f^{\,v}_{\mathrm{CH_4}} = y_{\mathrm{CH_4}}P = 1.013\ \text{bar}.$$
Nitrogen is assumed not to affect methane's solubility (each gas dissolves independently at these dilutions).

**Step 2: hypothetical liquid fugacity.** $T_r = 298.2/190.6 = 1.56$. The chart gives $f^{\,l}/P_c\approx 3.65$, so $f^{\,l}_{\mathrm{CH_4}}\approx 3.65\times46.0 = 168$ bar. This is a value read from a graph.

![Corresponding-states chart for the hypothetical liquid fugacity of dissolved gases: at Tr = 1.56, f^L/Pc ≈ 3.65 for methane](figs/ET-30-prausnitz-shair-chart.png)

**Step 3: ideal solubility.**
$$x^{\mathrm{ideal}}_{\mathrm{CH_4}} = \frac{1.013}{167.9} = 6.03\times10^{-3}$$

**Step 4: activity coefficients and Henry's constants.** $\gamma = x^{\mathrm{ideal}}/x$, and $\bar f^{\,v}/x$ is the apparent Henry's constant (Section 31):

| Solvent | $x_{\mathrm{CH_4}}$ | $\gamma_{\mathrm{CH_4}}$ | $\bar f^{\,v}/x$ (bar) |
|---|---|---|---|
| benzene | $2.07\times10^{-3}$ | 2.91 | 489 |
| CCl₄ | $2.86\times10^{-3}$ | 2.11 | 354 |
| cyclohexane | $2.83\times10^{-3}$ | 2.13 | 358 |

### Motivation and explanation

**All $\gamma > 1$.** Methane is less soluble in every solvent than an ideal mixture would allow. As small, weakly attracting molecules, methane pays to break the stronger solvent–solvent attractions in order to fit in.

**Why benzene is the worst solvent.** In regular-solution terms, $\ln\gamma\propto(\delta_{\mathrm{CH_4}} - \delta_{\mathrm{solvent}})^2$. Methane's (hypothetical-liquid) solubility parameter is low. Benzene has the highest $\delta$ of the three (18.7 MPa^½ against 16.8 for cyclohexane, Section 17), so it is the most unlike methane and dissolves it least. Cyclohexane and CCl₄ have similar, lower $\delta$'s and almost equal $\gamma$'s.

**Accuracy.** $f^{\,l}$ comes from a correlation read off a log-scale chart, so the absolute $\gamma$'s carry several percent uncertainty. The *ratios* between solvents do not depend on $f^{\,l}$ at all, since they come straight from the measured $x$'s. The ranking is therefore robust.

**Assumptions to check.**
- Ideal-gas vapour: at 10 bar and $T_r = 1.56$, a representative pure-methane fugacity coefficient is about 0.98, suggesting a correction of a few percent. The methane fugacity coefficient in the nitrogen-rich mixture requires a mixture EOS.
- No nitrogen effect: reasonable at mole fractions of $10^{-3}$.
- Solvent vapour in the gas phase: neglected. Benzene's vapour pressure at 25 °C is about 0.13 bar, small compared with 10 bar.

### Link to other topics

The same calculation sizes absorbers for natural-gas processing. The apparent Henry's constants in the table are what designers usually tabulate, which is the motivation for the Henry's-law standard state in the next section.

### Summary

At 25 °C and 1.01 bar partial pressure, methane's hypothetical liquid fugacity of about 168 bar gives an ideal solubility of $6.0\times10^{-3}$. Measured solubilities are 2–3 times lower, giving $\gamma_{\mathrm{CH_4}}$ = 2.1–2.9, with benzene the least favourable solvent because its cohesive energy differs most from methane's.

## Section 31: Henry's law and the Henry standard state

### Intuition

A dilute solute molecule is surrounded entirely by solvent. Adding a few more solute molecules does not change that environment, so each behaves the same, and the escaping tendency is simply proportional to how many there are. The proportionality constant reflects how comfortable one solute molecule is among solvent molecules. That is exactly the infinite-dilution activity coefficient times the pure-liquid fugacity.

Raoult's law is the opposite limit: the *solvent*, nearly pure, behaves as if it were alone. Every dilute binary obeys Raoult for the solvent and Henry for the solute at the same time, and Gibbs–Duhem guarantees the two are consistent.

### Derivation

**Step 1: dilute limit.** As $x_i\to 0$, $\gamma_i\to\gamma_i^{\infty}$, a constant at fixed $T$ (and pressure, to a good approximation). Then

$$\bar f_i = \gamma_ix_if_i^{\,l}\;\to\;x_i\,\gamma_i^{\infty}f_i^{\,l}\equiv x_iH_i(T) \tag{142}$$

$$H_i = \gamma_i^{\infty}f_i^{\,l} \tag{143}$$

$H_i$ has units of pressure and depends on $T$ and on both the solute and the solvent. It can be measured directly as $\lim_{x_i\to0}\bar f_i/x_i$, without ever constructing $f_i^{\,l}$.

**Step 2: a new standard state.** The conventional activity uses the pure liquid as reference, $a_i = x_i\gamma_i = \bar f_i/f_i^{\,l}$, so $a_i = 1$ for pure $i$. Instead, use $H_i$ as the reference fugacity:

$$a_i^{*} = x_i\gamma_i^{*} = \frac{\bar f_i}{H_i} \qquad\Rightarrow\qquad \bar f_i = \gamma_i^{*}x_iH_i \tag{144}$$

**Step 3: how the two activity coefficients relate.** Dividing (144) by $\bar f_i = \gamma_ix_if_i^{\,l}$ and using (143):

$$\gamma_i^{*} = \frac{\gamma_i}{\gamma_i^{\infty}} \tag{145}$$

So $\gamma_i^{*}\to 1$ as $x_i\to 0$, while $\gamma_i\to 1$ as $x_i\to 1$. The two conventions are normalised at opposite ends.

**Step 4: graphical meaning.** On a plot of $\bar f_i$ against $x_i$:
- Henry's law is the tangent at $x_i = 0$, reaching $H_i$ at $x_i = 1$;
- Raoult's law (ideal mixture) is the straight line to $f_i^{\,l}$.

At any composition A, with the real curve at D, the Henry line at C and the Raoult line at B: $\gamma_i^{*} = AD/AC$ and $\gamma_i = AD/AB$.

![Henry and Raoult reference lines for a dissolved gas: γ* = AD/AC measures deviation from the Henry line, γ = AD/AB from the (hypothetical) Raoult line](figs/ET-31-henry-vs-raoult.png)

### Motivation and explanation

**Why switch reference.** For a supercritical gas, $f_i^{\,l}$ is hypothetical and must come from an extrapolation or correlation (Section 29). $H_i$ is measured directly in the dilute region where the gas actually lives, and then $\gamma_i^{*}\approx 1$. Any standard state is allowed, as long as it is used consistently.

**Temperature dependence.** $\ln H_i$ usually varies with $1/T$ through the enthalpy of solution (a van 't Hoff form). For permanent gases in water near room temperature, dissolution is exothermic, so $H$ falls and solubility rises as temperature falls. That is why cold water holds more oxygen.

**Limits.** Henry's law is a limiting law. It fails as $x_i$ grows (then $\gamma_i^{*}\neq 1$) and for gases that react or ionise in the solvent: CO₂, NH₃ and SO₂ in water dissolve far beyond the Henry value because of the chemistry. At high pressure, the gas-phase fugacity and the pressure dependence of $H$ (through the partial molar volume of the solute) must be included.

### Worked example

**Problem.** Henry's constants in water at 25 °C are $4.3\times10^4$ atm for O₂ and $9.1\times10^4$ atm for N₂. (a) How much oxygen and nitrogen dissolves in water in equilibrium with air at 1 atm? (b) How much more oxygen dissolves at 5 °C, given $-\Delta_{\mathrm{sol}}H/R = 1700$ K for O₂?

**(a)** With an ideal-gas vapour, $\bar f_i = y_iP$:
- $x_{\mathrm{O_2}} = 0.21/4.3\times10^4 = 4.9\times10^{-6}$, about 8.7 mg L⁻¹ (taking 55.5 mol of water per litre);
- $x_{\mathrm{N_2}} = 0.78/9.1\times10^4 = 8.6\times10^{-6}$, about 13 mg L⁻¹.

**(b)** $H(T) = H(298.15)\exp[-1700(1/T - 1/298.15)]$, which at 278.15 K gives $H = 2.9\times10^4$ atm. Solubility is inversely proportional to $H$, so 1.5 times more oxygen dissolves at 5 °C than at 25 °C.

**Interpretation.** The oxygen value (~8.7 mg L⁻¹) matches the familiar saturation level of fresh water at 25 °C. Such low solubility is why aerobic bioreactors are often limited by oxygen transfer: the liquid can never hold more than a few milligrams per litre, so oxygen must be supplied continuously. The 50 % gain on cooling is part of why cold waters support more aquatic life. In Henry's terms, N₂ and O₂ are "ideal" here: $\gamma^{*} = 1$ by construction at these tiny mole fractions.

### Link to other topics

Henry's constants are the standard input for absorber and stripper design and for gas–liquid mass transfer in bioreactors, where the oxygen saturation concentration sets the transfer driving force. The infinite-dilution activity coefficient in (143) links back to ebulliometry (Section 14), which measures it for condensable solutes.

### Summary

In the dilute limit the solute fugacity is linear in mole fraction, $\bar f_i = x_iH_i$, with $H_i = \gamma_i^{\infty}f_i^{\,l}$. Using $H_i$ as the standard state removes the need for a hypothetical liquid and gives an activity coefficient $\gamma_i^{*}$ that is 1 at infinite dilution. Applied to air and water, it predicts the familiar ~9 mg L⁻¹ of dissolved oxygen and its rise on cooling.

## Conclusion

Gas solubility is ordinary phase equilibrium with an awkward reference state. The hypothetical liquid gives an ideal solubility and activity coefficients; Henry's constant avoids the hypothetical state and is the standard design input, predicting for example about 9 mg L⁻¹ of dissolved oxygen in water at 25 °C. The next part moves to high pressure, where vapour and liquid approach each other near critical points.
