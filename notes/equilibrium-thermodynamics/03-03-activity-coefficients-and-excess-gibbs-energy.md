# Activity coefficients and excess Gibbs energy — reading 03.3

[Previous](03-02-activity-coefficients-and-excess-gibbs-energy.md) · [Subject index](README.md) · [Next](04-01-measuring-activity-coefficients-and-freezing-point-depression.md)

<!-- reading-content:start -->
## Section 13: Worked example, liquid oxygen–argon

*Components:* liquid oxygen (52), argon (53).

### Intuition

Oxygen and argon are small, nearly spherical, non-polar molecules of similar size. Their mixture should be close to ideal. A small positive $`A`$ says they attract each other slightly less than they attract their own kind. So we expect $`\Delta\underline{G}_{\mathrm{mix}}`$ to be dominated by the ideal entropy term, with $`\gamma`$'s a little above 1 and partial pressures slightly above Raoult's law. The calculation confirms this and gives the size of the effect.

### Derivation

**(a) Gibbs energy of mixing.** Combine the ideal term and the model:


**Equation (70)**

```math
\Delta\underline{G}_{\mathrm{mix}} = RT\left(x_1\ln x_1 + x_2\ln x_2\right) + Ax_1x_2
```


**(b) Chemical potentials.** From (52) of Section 10 with the Margules $`\gamma`$'s:


**Equation (71)**

```math
\mu_1 = \underline{G}_1 + RT\ln x_1 + Ax_2^2, \qquad \mu_2 = \underline{G}_2 + RT\ln x_2 + Ax_1^2
```


Here $`\underline{G}_i`$ is pure liquid $`i`$ at the same $`T`$ and $`P`$. It can be evaluated from $`d\underline{G}_i = -\underline{S}_i\,dT + \underline{V}_i\,dP`$ and tabulated data, but it cancels in the equilibrium calculation below.

**(c) Vapour–liquid equilibrium for oxygen.** Require $`\mu_1^{L} = \mu_1^{V}`$.

*Liquid side:* (71), $`\mu_1^{L} = \underline{G}_1^{L}(T,P) + RT\ln x_1 + RT\ln\gamma_1`$.

*Vapour side:* assume an ideal-gas mixture, so $`\mu_1^{V} = \underline{G}_1^{\circ}(T) + RT\ln(y_1P/P^{\circ})`$, with $`\underline{G}_1^{\circ}`$ the pure ideal gas at $`T`$, $`P^{\circ}`$.

Choose $`P^{\circ} = P_1^{\mathrm{SAT}}(T)`$. At this pressure pure liquid oxygen coexists with its (ideal) vapour, so $`\underline{G}_1^{L}(T,P_1^{\mathrm{SAT}}) = \underline{G}_1^{\circ}(T)`$ when the reference is taken at $`P^{\circ} = P_1^{\mathrm{SAT}}`$.

*Neglect the liquid's pressure dependence:* $`\underline{G}_1^{L}(T,P)\approx\underline{G}_1^{L}(T,P_1^{\mathrm{SAT}})`$, i.e. ignore the Poynting factor (Section 06).

The pure-component terms then cancel, leaving


**Equation (72)**

```math
RT\ln x_1 + RT\ln\gamma_1 = RT\ln\frac{y_1P}{P_1^{\mathrm{SAT}}} \;\;\Rightarrow\;\; \boxed{x_1\gamma_1P_1^{\mathrm{SAT}} = y_1P}
```


This is modified Raoult's law. In fugacity language it is $`\bar f_1^{L} = \gamma_1x_1f_1^{L}`$ with $`f_1^{L} = P_1^{\mathrm{SAT}}`$, set equal to $`\bar f_1^{V} = y_1P`$. That is why fugacity is the convenient variable: equilibrium becomes a one-line equality.

**Saturation pressure.** Integrating Clausius–Clapeyron with constant $`\Delta\underline{H}^{\mathrm{vap}}`$ from the normal boiling point $`T_b`$, where $`P^{\mathrm{SAT}} = 1`$ atm:


**Equation (73)**

```math
\ln\frac{P^{\mathrm{SAT}}(T)}{P^{\mathrm{SAT}}(T_b)} = -\frac{\Delta\underline{H}^{\mathrm{vap}}}{R}\left(\frac{1}{T} - \frac{1}{T_b}\right)
```


### Worked example

**Data.** $`T = 83.8`$ K, so $`RT = 696.8`$ J mol⁻¹. $`A = 148`$ J mol⁻¹. Oxygen: $`T_b = 90.188`$ K, $`\Delta\underline{H}^{\mathrm{vap}} = 6819`$ J mol⁻¹. Liquid composition $`x_1 = 0.3`$.

**(a) Gibbs energy of mixing at $`x_1 = 0.5`$.** The ideal term is $`RT\ln 0.5 = -483`$ J mol⁻¹, the excess term is $`A/4 = +37`$ J mol⁻¹, and the total is $`\Delta\underline{G}_{\mathrm{mix}} = -446`$ J mol⁻¹. The excess is about 8 % of the ideal term, so the mixture is mildly non-ideal. Since $`A/RT = 0.21`$, the curve stays convex everywhere. The two liquids mix in all proportions, with the minimum at $`x_1 = 0.5`$ by symmetry.

![Gibbs energy of mixing for liquid oxygen–argon at 83.8 K: ideal term (red, minimum −483 J/mol), small positive excess (green, +37 J/mol) and the total (purple, −446 J/mol)](figs/ET-13-oxygen-argon-gibbs-mixing.png)

**(b) Chemical potentials at $`x_1 = 0.3`$.** From (71):


```math
\mu_1 - \underline{G}_1 = 696.8\ln0.3 + 148(0.7)^2 = -766\ \text{J mol}^{-1}
```


```math
\mu_2 - \underline{G}_2 = 696.8\ln0.7 + 148(0.3)^2 = -235\ \text{J mol}^{-1}
```


Both are negative, so each component is more stable in the mixture than pure: mixing is spontaneous. The dilute component (oxygen) gains more, because $`RT\ln x`$ is steepest at small $`x`$.

**(c) Oxygen partial pressure.**
- Activity coefficient: $`\gamma_1 = \exp(148\times0.49/696.8) = 1.110`$.
- Saturation pressure from (73): $`P_1^{\mathrm{SAT}}(83.8\ \mathrm{K}) = 1.01325\exp\!\left[-\frac{6819}{8.314}\left(\frac{1}{83.8} - \frac{1}{90.188}\right)\right] = 0.507`$ bar.
- From (72): $`y_1P = 0.3\times1.110\times0.507 = 0.169`$ bar.

Raoult's law ($`\gamma_1 = 1`$) would give 0.152 bar. The positive deviation raises oxygen's partial pressure by 11 %.

*Accuracy check.* An accurate equation of state for oxygen gives $`P_1^{\mathrm{SAT}}(83.8\ \mathrm{K}) = 0.492`$ bar. Clausius–Clapeyron with a constant $`\Delta\underline{H}^{\mathrm{vap}}`$ overestimates it by 3 %, so a better estimate is $`y_1P = 0.164`$ bar. The vapour-pressure data, not the activity coefficient, limit the precision here.

**(d) Extension: bubble pressure and vapour composition.** 83.8 K is argon's triple-point temperature (83.81 K), where its vapour pressure is 0.689 bar. Then $`\gamma_2 = \exp(148\times0.09/696.8) = 1.019`$, and applying (72) to argon:

```math
y_2P = 0.7\times1.019\times0.689 = 0.491\ \text{bar}
```

Adding the two partial pressures:

| | $`P`$ (bar) | $`y_1`$ |
|---|---|---|
| Margules, with Clausius–Clapeyron $`P_1^{\mathrm{SAT}}`$ | 0.660 | 0.255 |
| Raoult's law, same data | 0.634 | 0.240 |

The liquid boils at a 4 % higher pressure than an ideal mixture would. Its vapour is slightly richer in oxygen than Raoult's law predicts, because oxygen, the more dilute component, has the larger $`\gamma`$.

### Motivation and explanation

**What each assumption costs.**
- Ideal-gas vapour: good below 1 bar.
- Neglecting the Poynting factor: under 0.1 % at these pressures (Section 06).
- Constant $`\Delta\underline{H}^{\mathrm{vap}}`$: 3 % error in $`P^{\mathrm{SAT}}`$ over 6 K.
- One-constant Margules: adequate for two similar small molecules.

The non-ideal correction (11 % on oxygen's partial pressure) is larger than all the other approximations. So the activity coefficient is worth including even for this nearly ideal mixture. For an air-separation column, which separates O₂, Ar and N₂ with small relative volatilities, it is essential.

**Limiting cases.** As $`x_1\to 1`$, $`\gamma_1\to 1`$ and (72) gives $`y_1P\to P_1^{\mathrm{SAT}}`$, the pure vapour pressure. As $`x_1\to 0`$, $`\gamma_1\to\exp(A/RT) = 1.24`$, so oxygen's partial pressure approaches $`1.24\,x_1P_1^{\mathrm{SAT}}`$. That is linear in $`x_1`$ with a modified slope: Henry's law behaviour, discussed later.

### Link to other topics

Equation (72), $`x_i\gamma_iP_i^{\mathrm{SAT}} = y_iP`$, is the workhorse of low-pressure vapour–liquid equilibrium. Bubble- and dew-point calculations, azeotropes and the design of distillation columns in Separations all start from it. Turned around, measured $`x`$, $`y`$, $`P`$ data give $`\gamma_i`$ directly, which is how activity-coefficient parameters are obtained.

### Summary

Starting from a single model constant, $`A = 148`$ J mol⁻¹, we obtained the Gibbs energy of mixing, the chemical potentials, and, through modified Raoult's law, the oxygen partial pressure (≈0.17 bar) and the bubble pressure (≈0.66 bar) of a 30 % oxygen liquid at 83.8 K. Positive deviation raises them by 11 % and 4 % above Raoult's law.

## Conclusion

The activity coefficient measures, component by component, how far a liquid mixture departs from ideal mixing; $`\gamma > 1`$ means unlike molecules attract less than like ones. Models are built from $`\underline{G}^{ex}`$ so that they are thermodynamically consistent, and with them modified Raoult's law $`x_i\gamma_iP_i^{\mathrm{SAT}} = y_iP`$ predicts vapour–liquid equilibrium. The next part asks where the model constants come from: measurements of activity coefficients, including from freezing points.
<!-- reading-content:end -->

[Previous](03-02-activity-coefficients-and-excess-gibbs-energy.md) · [Subject index](README.md) · [Next](04-01-measuring-activity-coefficients-and-freezing-point-depression.md)
