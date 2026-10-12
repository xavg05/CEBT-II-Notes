# Vapour–liquid equilibrium of real mixtures — reading 07.3

[Previous](<../../../../../notes/Equilibrium Thermodynamics/07 - Vapour–liquid equilibrium of real mixtures/Complete section.md>) · [Subject index](<../../../../../notes/Equilibrium Thermodynamics/README.md>) · [Next](<../../../../../notes/Equilibrium Thermodynamics/08 - Solubility of gases in liquids/Complete section.md>)

<!-- reading-content:start -->
## Section 28: Worked example, van Laar parameters from an azeotrope

*Components:* n-pentane (1), propanal (2).

### Intuition

At an azeotrope, modified Raoult's law collapses. The $`y_i`$ and $`x_i`$ cancel, leaving $`\gamma_i = P/P_i^{\mathrm{SAT}}`$: one measured pressure gives both activity coefficients. Two numbers fix two model constants. Everything else on the curve is then a *prediction*, and its accuracy depends on how well the model's shape matches the real mixture away from the single point used.

### Derivation

**Step 1: $`\gamma`$'s at the azeotrope.** From $`\gamma_ix_iP_i^{\mathrm{SAT}} = y_iP`$ with $`x_i = y_i`$:


**Equation (135)**

```math
\gamma_1^{\mathrm{az}} = \frac{P^{\mathrm{az}}}{P_1^{\mathrm{SAT}}}, \qquad \gamma_2^{\mathrm{az}} = \frac{P^{\mathrm{az}}}{P_2^{\mathrm{SAT}}}
```


**Step 2: van Laar.**


**Equation (136)**

```math
\ln\gamma_1 = \frac{\alpha}{\left(1 + \dfrac{\alpha x_1}{\beta x_2}\right)^2}, \qquad \ln\gamma_2 = \frac{\beta}{\left(1 + \dfrac{\beta x_2}{\alpha x_1}\right)^2}
```


**Step 3: invert for the constants.** Let $`u = \alpha x_1/(\beta x_2)`$. Then (136) reads $`\ln\gamma_1 = \alpha/(1+u)^2`$ and $`\ln\gamma_2 = \beta u^2/(1+u)^2`$. Dividing the second by the first gives $`\ln\gamma_2/\ln\gamma_1 = (\beta/\alpha)u^2 = u\,x_1/x_2`$, so $`u = x_2\ln\gamma_2/(x_1\ln\gamma_1)`$. Substituting back into the two expressions:


**Equation (137)**

```math
\alpha = \ln\gamma_1\left(1 + \frac{x_2\ln\gamma_2}{x_1\ln\gamma_1}\right)^2, \qquad \beta = \ln\gamma_2\left(1 + \frac{x_1\ln\gamma_1}{x_2\ln\gamma_2}\right)^2
```


*Check:* substituting (137) back into (136) reproduces the input $`\gamma`$'s. The fitted model's $`P`$–$`x`$ curve also has zero slope at $`x_1^{\mathrm{az}}`$, as it must; both were verified numerically.

**Step 4: predict.** At any other $`x_1`$, compute $`\gamma_1`$ and $`\gamma_2`$ from (136), then the bubble pressure


**Equation (138)**

```math
P = x_1\gamma_1P_1^{\mathrm{SAT}} + x_2\gamma_2P_2^{\mathrm{SAT}}, \qquad y_1 = \frac{x_1\gamma_1P_1^{\mathrm{SAT}}}{P}
```


### Worked example

**Data (40 °C).** $`P_1^{\mathrm{SAT}} = 1.1541`$ bar (n-pentane), $`P_2^{\mathrm{SAT}} = 0.7609`$ bar (propanal). Azeotrope at $`x_1 = 0.682`$, $`P = 1.364`$ bar. Measured bubble pressure at $`x_1 = 0.1647`$: 1.1622 bar.

![P–x–y sketch at 40 °C: maximum-pressure azeotrope at x1 = 0.682, 1.364 bar; the bubble pressure is to be predicted at x1 = 0.1647](figs/ET-28-pentane-propanal-sketch.png)

**(135) Azeotropic $`\gamma`$'s.** $`\gamma_1 = 1.364/1.1541 = 1.182`$ and $`\gamma_2 = 1.364/0.7609 = 1.793`$.

**(137) Constants.** $`\alpha = 1.155`$, $`\beta = 1.520`$, so $`\gamma_1^{\infty} = 3.17`$ and $`\gamma_2^{\infty} = 4.57`$. This is a strongly positive deviation: polar propanal and non-polar pentane dislike each other.

**(138) Prediction at $`x_1 = 0.1647`$.** $`\gamma_1 = 2.395`$, $`\gamma_2 = 1.026`$, so


```math
P = 0.1647(2.395)(1.1541) + 0.8353(1.026)(0.7609) = 1.107\ \text{bar}, \qquad y_1 = 0.41
```


**Comparison.** Measured 1.1622 bar, so the prediction is 4.7 % low. As a fraction of the pressure range of the diagram ($`P^{\mathrm{az}} - P_2^{\mathrm{SAT}} = 0.603`$ bar), the error is 9 %.

**Cross-check with a different model.** A two-constant Margules model fitted to the same azeotrope gives 1.102 bar (5.2 % low). Both models, fitted to the same single point, err in the same direction.

### Motivation and explanation

**Why the error?**
1. *One data point.* Both constants come from the azeotrope at $`x_1 = 0.68`$; the prediction is far away at $`x_1 = 0.16`$. Any model fitted at one point is only an interpolation scheme with an assumed shape. Two different shapes (van Laar, Margules) both under-predict, so the real $`\gamma_1`$ in the propanal-rich region must be larger than either shape allows.
2. *Polar component.* Propanal's dipole gives specific interactions with orientational (non-random) structure. Van Laar's random-mixing, van der Waals origin is poorly suited to that. A local-composition model (Wilson, NRTL) fitted to several points would do better.
3. *Small effects.* At about 1 bar, the vapour-phase and Poynting corrections are around 1 %. They are not the main cause.

**How to do better.** Fit to data spread across the composition range, or add infinite-dilution values (ebulliometry, Section 14) at both ends.

**Strength of the method.** Despite its limits, one azeotrope measurement gave a model correct to about 5 % in pressure, with no composition analysis of the vapour at all. That is useful for screening.

### Link to other topics

The same calculation (activity coefficients from measured $`P`$–$`x`$ data, then a fitted model) is how binary interaction parameters in process simulators are generated. Predicting $`y_1`$ (0.41 here, against a liquid of 0.16) gives the relative volatility needed for distillation design.

### Summary

At an azeotrope, $`\gamma_i = P/P_i^{\mathrm{SAT}}`$, which fixes both van Laar constants from a single measurement ($`\alpha = 1.155`$, $`\beta = 1.520`$ for pentane–propanal at 40 °C). The resulting model predicts the bubble pressure elsewhere to about 5 %. The residual error reflects fitting a two-parameter shape at one point to a polar mixture, not the low-pressure approximations.

## Conclusion

At low pressure, vapour–liquid equilibrium is $`y_iP = x_i\gamma_iP_i^{\mathrm{SAT}}`$, and the activity coefficient carries the important non-ideality. Large enough deviations produce azeotropes, which limit distillation but also provide a cheap measurement of $`\gamma`$. The next part deals with components that cannot exist as pure liquids at the conditions of interest: supercritical gases dissolved in liquids.
<!-- reading-content:end -->

[Previous](<../../../../../notes/Equilibrium Thermodynamics/07 - Vapour–liquid equilibrium of real mixtures/Complete section.md>) · [Subject index](<../../../../../notes/Equilibrium Thermodynamics/README.md>) · [Next](<../../../../../notes/Equilibrium Thermodynamics/08 - Solubility of gases in liquids/Complete section.md>)
