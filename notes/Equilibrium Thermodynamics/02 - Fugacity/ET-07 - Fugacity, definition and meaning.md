[Previous](<ET-06 - The Poynting correction (vapour pressure under an inert gas).md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-08 - Fugacity from volumetric data and the fugacity coefficient.md>)

<!-- note-content:start -->
# Section 07: Fugacity, definition and meaning

*Notation:* $`\underline{G}_i`$ is the molar Gibbs energy of pure $`i`$. $`\mu_i`$ is the chemical potential of $`i`$ in a mixture. $`P^{\circ}`$ is a reference pressure (e.g. 1 bar). $`\underline{G}_i^{\circ}(T,P^{\circ})`$ is the molar Gibbs energy of pure $`i`$ **as an ideal gas** at $`T`$ and $`P^{\circ}`$. $`f_i`$ is the fugacity of pure $`i`$, and $`\bar{f}_i`$ is the fugacity of $`i`$ in a mixture. Many textbooks write $`\hat{f}_i`$ for the mixture fugacity. The overbar here does **not** mean a partial molar property: fugacity is not one (see below).

## Intuition

The word comes from the Latin *fugere*, to flee: fugacity is a substance's **escaping tendency**. Think of the partial pressure that a component "would like" to exert. The previous note found that a compressed liquid behaves, as far as its vapour is concerned, as if it had a pressure $`P^{\mathrm{SAT}}\exp[\underline{V}^{l}(P-P^{\mathrm{SAT}})/RT]`$. That is not a pressure anyone can measure on a gauge, but it is the partial pressure an ideal gas would need in order to sit in equilibrium with the liquid. That quantity is the liquid's fugacity.

*Analogy: fugacity is to mass transfer what temperature is to heat transfer.* Heat flows from high $`T`$ to low $`T`$ and stops when the temperatures are equal. A component moves from the phase where its fugacity is high to where it is low, and stops when the fugacities are equal. The analogy breaks down in two places. Each component has its own fugacity, and two components can move in opposite directions at the same time. And fugacities can only be compared at the same temperature.

There is no new thermodynamics here. Fugacity is a change of variable, $`\mu \leftrightarrow RT\ln f`$, chosen because it behaves better than $`\mu`$: $`\mu_i \to -\infty`$ as $`P\to 0`$ or $`x_i\to 0`$, whereas $`\bar f_i \to 0`$.

## Derivation

**Step 1: definition for a pure substance.** At fixed $`T`$, define $`f_i`$ by


**Equation (33)**

```math
\underline{G}_i(T,P) = \underline{G}_i^{\circ}(T,P^{\circ}) + RT\ln\frac{f_i}{P^{\circ}}
```


*Reason:* this has exactly the ideal-gas form, but with the real molar Gibbs energy on the left. All the non-ideality is pushed into $`f_i`$. The reference state is always the hypothetical pure ideal gas at $`(T,P^{\circ})`$, whatever the actual phase of $`i`$.

**Step 2: ideal-gas check.** For an ideal gas, $`\underline{G}_i = \underline{G}_i^{\circ} + RT\ln(P/P^{\circ})`$. Comparing with (33):


**Equation (34)**

```math
f_i^{\mathrm{IG}} = P
```


Every real gas becomes ideal as $`P\to 0`$, so $`f_i/P \to 1`$ in that limit. Many textbooks take this limit, together with (35), as the definition. The two definitions are equivalent.

**Step 3: pressure dependence.** At constant $`T`$, $`d\underline{G}_i = \underline{V}_i\,dP`$. Differentiate (33), noting that the reference term is fixed:


**Equation (35)**

```math
RT\,d\ln f_i = \underline{V}_i\,dP \qquad (\text{constant } T)
```


*Reason:* this is the working equation for computing $`f_i`$ from volumetric data or an equation of state. Integrating it is the subject of Section 08. For an ideal gas, $`\underline{V}_i = RT/P`$ and (35) gives $`d\ln f_i = d\ln P`$, which is consistent with (34).

**Step 4: equilibrium criterion, pure substance.** Two phases $`\alpha`$, $`\beta`$ of pure $`i`$ at the same $`T`$ are in equilibrium when $`\underline{G}_i^{\alpha} = \underline{G}_i^{\beta}`$. Write both using (33). They share the same reference term (same $`T`$, same ideal-gas state), so


**Equation (36)**

```math
f_i^{\alpha} = f_i^{\beta}
```


**Step 5: liquid fugacity.** A saturated liquid is in equilibrium with its saturated vapour. If that vapour is an ideal gas, (36) and (34) give


**Equation (37)**

```math
f_i^{l,\mathrm{sat}} = P_i^{\mathrm{SAT}}
```


Integrating (35) for an incompressible liquid from $`P_i^{\mathrm{SAT}}`$ to $`P`$ then gives the compressed-liquid fugacity. This is the Poynting result in fugacity language:


**Equation (38)**

```math
f_i^{l}(T,P) = P_i^{\mathrm{SAT}}\exp\!\left[\frac{\underline{V}_i^{l}\,(P-P_i^{\mathrm{SAT}})}{RT}\right]
```


**Step 6: component in a mixture.** Define $`\bar f_i`$ in the same way, using the chemical potential:


**Equation (39)**

```math
\mu_i = \mu_i^{\circ} + RT\ln\frac{\bar f_i}{P^{\circ}}, \qquad \mu_i^{\circ} = \underline{G}_i^{\circ}(T,P^{\circ})
```


*Reason:* the reference is still the *pure* ideal gas, so $`\mu_i^{\circ}`$ is the same quantity as in (33). As in Step 4, equal chemical potentials in two phases then mean


**Equation (40)**

```math
\bar f_i^{\alpha} = \bar f_i^{\beta} \quad \text{for every component } i
```


**Step 7: limiting cases in a mixture.**

*Ideal-gas mixture.* Here $`\mu_i = \underline{G}_i^{\circ} + RT\ln(y_iP/P^{\circ})`$, where $`y_i`$ is the vapour mole fraction. Comparing with (39):


**Equation (41)**

```math
\bar f_i^{\mathrm{IG}} = y_i P
```


So the fugacity is the partial pressure, as the definition intends.

*Ideal mixture.* Here $`\mu_i = \underline{G}_i + RT\ln x_i`$, where $`\underline{G}_i`$ is pure $`i`$ at the same $`T`$, $`P`$ and phase. Subtract (33) from (39); the reference terms cancel:


**Equation (42)**

```math
RT\ln\frac{\bar f_i}{f_i} = RT\ln x_i \;\;\Rightarrow\;\; \bar f_i = x_i f_i
```


This is the **Lewis–Randall rule**: in an ideal mixture, each component's fugacity is its mole fraction times its pure-component fugacity at the same $`T`$ and $`P`$. With (37), it becomes Raoult's law for an ideal liquid in contact with an ideal-gas vapour.

**Step 8: fugacity is not a partial molar quantity.** The molar Gibbs energy of a mixture is $`\underline{G} = \sum_i x_i\mu_i`$. Using (39):


**Equation (43)**

```math
\underline{G} = \sum_i x_i\,\mu_i^{\circ} + RT\sum_i x_i\ln\frac{\bar f_i}{P^{\circ}}
```


The mole-fraction-weighted sum acts on $`\ln\bar f_i`$, not on $`\bar f_i`$. So $`\sum_i x_i\bar f_i`$ is not "the fugacity of the mixture", and has no thermodynamic meaning in this course.

## Motivation and explanation

**Why this form.** Equation (33) inverts to $`f_i = P^{\circ}\exp[(\underline{G}_i - \underline{G}_i^{\circ})/RT]`$. Fugacity is therefore the exponential of the Gibbs energy measured from the ideal-gas state. A difference of $`RT\ln 2`$ in Gibbs energy is a factor of 2 in fugacity. This is why fugacity always has units of pressure and is always positive, while $`\mu`$ has no absolute zero.

**Why it is useful.**
1. *Equilibrium becomes simple.* Equations (36) and (40) replace "equal chemical potentials" with "equal corrected pressures". For a gas mixture in contact with a liquid, the left side is close to $`y_iP`$ and the right side close to $`x_iP_i^{\mathrm{SAT}}`$. The non-idealities then appear as correction factors: a fugacity coefficient for the gas (Section 08) and an activity coefficient for the liquid (a later note).
2. *Good behaviour at the limits.* As $`x_i\to 0`$, $`\mu_i\to-\infty`$, but $`\bar f_i\to 0`$ smoothly. This matters for dilute solutes and trace components.

**Sanity checks.**
- Ideal gas: $`f = P`$.
- Ideal-gas mixture: $`\bar f_i = y_iP`$.
- Pure component in an ideal mixture ($`x_i = 1`$): $`\bar f_i = f_i`$.
- Saturated liquid with an ideal-gas vapour: $`f = P^{\mathrm{SAT}}`$.

**Where the simple forms fail.** Equations (37), (38), (41) and (42) each rest on an ideality assumption. Real gases at high pressure have $`f\neq P`$, so (37) becomes $`f^{l,\mathrm{sat}} = \phi^{\mathrm{sat}}P^{\mathrm{SAT}}`$, where $`\phi`$ is a fugacity coefficient. Real liquid mixtures break (42), which is where activity coefficients come in. The definitions (33) and (39), and the criteria (36) and (40), are exact and never fail.

## Worked example

**Problem.** A glass of water stands in room air at 20 °C and 1 atm, at 60 % relative humidity. Use fugacities to decide whether water evaporates or condenses, find the driving force, and find the humidity at which the water and air would be in equilibrium. Data: $`P^{\mathrm{SAT}} = 0.02339`$ bar, $`\underline{V}^{l} = 1.805\times10^{-5}`$ m³ mol⁻¹. Treat the air–water vapour as an ideal-gas mixture and air as insoluble.

**Liquid fugacity.** From (38) at $`P = 1.01325`$ bar: $`f^{l} = 0.023407`$ bar, the Poynting factor of 1.0007 from the previous note.

**Vapour fugacity.** Relative humidity is $`p_w/P^{\mathrm{SAT}}`$, and by (41) $`\bar f_w^{v} = p_w`$. So $`\bar f_w^{v} = 0.6\times0.02339 = 0.014034`$ bar.

**Direction.** $`f^{l} > \bar f_w^{v}`$, so water leaves the liquid: it evaporates.

To see why a pressure-like ratio gives the driving force, write (39) for water in each phase and subtract. The identical ideal-gas reference cancels, leaving $`\mu^{l}-\mu^{v}=RT\ln(f^{l}/\bar f_w^{v})`$. A ratio above unity gives evaporation, a ratio below unity gives condensation, and unity gives no net transfer. The absolute size of either fugacity is less informative than this comparison.

The humidity example therefore establishes the direction and thermodynamic incentive for transfer. It does not give an evaporation rate: that also needs transport through the gas next to the surface and the heat needed to sustain evaporation. Equal fugacities describe the endpoint, not how quickly it is reached.

**Driving force.** The chemical-potential difference is $`\mu^{l}-\mu^{v} = RT\ln(f^{l}/\bar f_w^{v}) \approx 1247`$ J mol⁻¹. This is positive, so water moves from liquid to vapour.

**Equilibrium.** Equation (40) requires $`\bar f_w^{v} = f^{l}`$, i.e. $`p_w = 0.023407`$ bar. That is a relative humidity of 100.07 %, or a water mole fraction in the air of $`y_w = 0.0231`$. Even air at exactly 100 % RH (measured against $`P^{\mathrm{SAT}}`$) is very slightly unsaturated with respect to liquid under 1 atm of air: the driving force is only 1.8 J mol⁻¹, and it comes entirely from the Poynting factor.

## Link to other topics

Equation (40) is the starting point for vapour–liquid equilibrium. In later sections it becomes $`y_i\bar\phi_iP = x_i\gamma_if_i`$, with a fugacity coefficient correcting the vapour and an activity coefficient correcting the liquid. Reaction equilibrium uses the same idea: the equilibrium constant is written in terms of fugacity ratios (activities) rather than partial pressures.

## Summary

Fugacity is the molar Gibbs energy (or chemical potential) expressed as a corrected pressure, measured from the ideal-gas state. It equals pressure for an ideal gas, partial pressure for an ideal-gas mixture, and $`x_if_i`$ in an ideal mixture. In every case, phase equilibrium means equal fugacities of each component.
<!-- note-content:end -->

[Previous](<ET-06 - The Poynting correction (vapour pressure under an inert gas).md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-08 - Fugacity from volumetric data and the fugacity coefficient.md>)
