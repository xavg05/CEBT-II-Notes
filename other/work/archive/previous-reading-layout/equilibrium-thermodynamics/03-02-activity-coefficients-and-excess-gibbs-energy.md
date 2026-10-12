# Activity coefficients and excess Gibbs energy — reading 03.2

[Previous](<../../../../../notes/Equilibrium Thermodynamics/03 - Activity coefficients and excess Gibbs energy/Complete section.md>) · [Subject index](<../../../../../notes/Equilibrium Thermodynamics/README.md>) · [Next](<../../../../../notes/Equilibrium Thermodynamics/03 - Activity coefficients and excess Gibbs energy/Complete section.md>)

<!-- reading-content:start -->
## Section 11: Thermodynamic consistency and the one-constant Margules model

### Intuition

Gibbs–Duhem says that, at fixed $`T`$ and $`P`$, the chemical potentials of a binary cannot all rise together as the composition changes. If adding component 1 makes component 1's environment less ideal, it must make component 2's environment more ideal, weighted by the amounts present.

So you cannot pick $`\gamma_1(x)`$ and $`\gamma_2(x)`$ independently. The way round this is to model the one mixture-level quantity, $`\underline{G}^{ex}(x)`$, and obtain both $`\gamma`$'s from it by differentiation, as partial molar quantities. Then they automatically fit together.

The simplest physically sensible $`\underline{G}^{ex}`$ is proportional to $`x_1x_2`$. In a randomly mixed liquid, the fraction of neighbour contacts that are between unlike molecules is proportional to $`x_1x_2`$. If each unlike contact costs (or gains) a fixed amount of energy, the excess Gibbs energy follows that product. This picture ignores non-random arrangement and size differences; later models (Wilson, NRTL, UNIQUAC) add them.

### Derivation

**Step 1: Gibbs–Duhem in terms of $`\gamma`$.** At constant $`T`$, $`P`$ in a binary, $`n_1\,d\mu_1 + n_2\,d\mu_2 = 0`$. Substitute $`d\mu_i = RT\,d\ln x_i + RT\,d\ln\gamma_i`$ ($`\underline{G}_i`$ is constant at fixed $`T`$, $`P`$), and divide by $`nRT`$:


```math
x_1\,d\ln x_1 + x_2\,d\ln x_2 + x_1\,d\ln\gamma_1 + x_2\,d\ln\gamma_2 = 0
```


**Step 2: the ideal terms cancel.** $`x_i\,d\ln x_i = dx_i`$, and $`dx_1 + dx_2 = 0`$ because the mole fractions sum to 1. Hence


**Equation (59)**

```math
x_1\,d\ln\gamma_1 + x_2\,d\ln\gamma_2 = 0 \qquad (\text{constant } T, P)
```


A model must also give $`\underline{G}^{ex} = 0`$ for each pure component:


**Equation (60)**

```math
\underline{G}^{ex}(x_1 = 0) = \underline{G}^{ex}(x_1 = 1) = 0
```


**Step 3: activity coefficients from any $`\underline{G}^{ex}(x_1)`$.** Write $`n\underline{G}^{ex} = n\,g(x_1)`$ with $`x_1 = n_1/n`$. At fixed $`n_2`$, $`\partial n/\partial n_1 = 1`$ and $`\partial x_1/\partial n_1 = x_2/n`$. Differentiate:


**Equation (61)**

```math
RT\ln\gamma_1 = g + x_2\,\frac{dg}{dx_1}, \qquad RT\ln\gamma_2 = g - x_1\,\frac{dg}{dx_1}
```


(the second by symmetry, since $`\partial x_1/\partial n_2 = -x_1/n`$). Geometrically, these are the intercepts at $`x_1 = 1`$ and $`x_1 = 0`$ of the tangent to the $`\underline{G}^{ex}`$ curve: the tangent construction for partial molar quantities.

**Step 4: any such model satisfies (59).** Differentiate (61): $`d(RT\ln\gamma_1)/dx_1 = g' - g' + x_2g'' = x_2g''`$ and $`d(RT\ln\gamma_2)/dx_1 = -x_1g''`$. Then


```math
x_1(x_2g'') + x_2(-x_1g'') = 0
```


for every function $`g`$. This is why models are always built from $`\underline{G}^{ex}`$: consistency comes for free.

**Step 5: one-constant Margules.** Choose


**Equation (62)**

```math
\underline{G}^{ex} = A\,x_1x_2
```


where $`A`$ is a function of $`T`$ only, fitted to data. It satisfies (60). With $`g = Ax_1(1-x_1)`$, $`g' = A(1-2x_1)`$, and (61) gives


**Equation (63)**

```math
RT\ln\gamma_1 = A\,x_2^2, \qquad RT\ln\gamma_2 = A\,x_1^2
```


*Check:* $`Ax_1x_2 + x_2A(1-2x_1) = Ax_2(x_1 + 1 - 2x_1) = Ax_2^2`$. ✓

**Step 6: infinite dilution.** Setting $`x_1\to 0`$ in (63):


**Equation (64)**

```math
\gamma_1^{\infty} = \gamma_2^{\infty} = \exp\!\left(\frac{A}{RT}\right)
```


### Motivation and explanation

**Symmetry.** Swapping $`x_1`$ and $`x_2`$ leaves (62) unchanged, so the two $`\gamma`$ curves are mirror images that cross at $`x_1 = 0.5`$. That is fine for molecules of similar size and shape (e.g. oxygen and argon). It is wrong whenever the two infinite-dilution behaviours differ, which is the usual case.

**Gibbs–Duhem near a pure component.** From (59), $`d\ln\gamma_1 = -(x_2/x_1)\,d\ln\gamma_2`$. As $`x_1\to 1`$ the factor $`x_2/x_1\to 0`$, so $`\gamma_1`$ approaches 1 with zero slope. A nearly pure component obeys Raoult's law almost exactly, while the dilute one deviates most. Model (63) shows this: $`\ln\gamma_1 \propto x_2^2`$ is flat at $`x_2 = 0`$.

**Meaning of $`A`$.**
- $`A > 0`$: positive deviation, $`\gamma > 1`$ (unlike contacts unfavourable).
- $`A < 0`$: negative deviation.
- The size of $`A/RT`$ sets how non-ideal the mixture is.

Later sections show that a large positive $`A/RT`$ makes $`\Delta\underline{G}_{\mathrm{mix}}`$ non-convex, so the liquid splits into two phases. Because $`A`$ depends on $`T`$, the same mixture can be miscible at one temperature and split at another.

**Limits of validity.** Consistent does not mean accurate. The one-constant model has one parameter, is symmetric, and is reliable only for simple, similar molecules.

### Worked example

**Problem.** For a binary with $`A/RT = 1`$, find $`\gamma_1`$ and $`\gamma_2`$ across the composition range, and check Gibbs–Duhem at $`x_1 = 0.5`$.

**Values from (63).**

| $`x_1`$ | 0 | 0.2 | 0.5 | 0.8 | 1 |
|---|---|---|---|---|---|
| $`\gamma_1 = e^{x_2^2}`$ | 2.718 | 1.896 | 1.284 | 1.041 | 1 |
| $`\gamma_2 = e^{x_1^2}`$ | 1 | 1.041 | 1.284 | 1.896 | 2.718 |

![Activity coefficients from the one-constant Margules model with A/RT = 1: mirror-image curves crossing at x1 = 0.5, each reaching e ≈ 2.72 at infinite dilution](figs/ET-11-margules-one-constant-gamma.png)

**Gibbs–Duhem check at $`x_1 = 0.5`$.** $`d\ln\gamma_1/dx_1 = -2(A/RT)x_2 = -1`$ and $`d\ln\gamma_2/dx_1 = 2(A/RT)x_1 = +1`$. Then $`0.5(-1) + 0.5(+1) = 0`$. ✓

**Interpretation.** Each component is 2.7 times "more eager to escape" when infinitely dilute than in an ideal mixture, but only 4 % more at $`x = 0.8`$. In a distillation, this means the dilute component is much more volatile than Raoult's law predicts, which matters most at the ends of a column, where products are nearly pure.

### Link to other topics

Equation (61) and the requirement to start from $`\underline{G}^{ex}`$ underpin every activity-coefficient model in the course, from van Laar to UNIQUAC. The same Gibbs–Duhem relation (59) is used later as a consistency test on measured vapour–liquid equilibrium data.

### Summary

Gibbs–Duhem forces $`x_1\,d\ln\gamma_1 + x_2\,d\ln\gamma_2 = 0`$, and any model that obtains both $`\gamma`$'s by differentiating a single $`\underline{G}^{ex}(x)`$ satisfies it automatically. The simplest choice, $`\underline{G}^{ex} = Ax_1x_2`$, gives $`RT\ln\gamma_i = Ax_j^2`$: consistent and easy to use, but symmetric.

## Section 12: Asymmetric models, parameters from data, and multicomponent mixtures

### Intuition

Asymmetry is the normal case. A small polar molecule dissolved in a large non-polar one is surrounded by neighbours it barely interacts with. The reverse situation is quite different. A single symmetric constant forces the two infinite-dilution activity coefficients to be equal; a second constant lets them differ.

The parameters are not predicted from first principles here. They are fitted to $`\underline{G}^{ex}`$ obtained from experiments. Vapour-pressure (VLE), freezing-point and osmotic-pressure measurements all give fugacities or chemical potentials, and hence $`\gamma_i`$ and $`\underline{G}^{ex}`$. The model is then a smooth, thermodynamically consistent interpolation of those data. It is not a theory of the mixture.

### Derivation

**Step 1: two-constant Margules.** Add an antisymmetric term:


**Equation (65)**

```math
\underline{G}^{ex} = x_1x_2\left[A + B(x_1 - x_2)\right]
```


$`A`$ and $`B`$ depend on $`T`$ only. Swapping the labels 1 ↔ 2 changes the sign of $`B`$, so $`B \neq 0`$ makes the model asymmetric. It still vanishes for both pure components.

**Step 2: activity coefficients.** Apply Section 11's formulas with $`g = x_1(1-x_1)\left[A + B(2x_1 - 1)\right]`$. After collecting powers of the other component's mole fraction:


**Equation (66)**

```math
RT\ln\gamma_1 = (A + 3B)\,x_2^2 - 4B\,x_2^3, \qquad RT\ln\gamma_2 = (A - 3B)\,x_1^2 + 4B\,x_1^3
```


**Step 3: consistency check.** Differentiate (66) with respect to $`x_1`$:
- $`d(RT\ln\gamma_1)/dx_1 = -2(A+3B)x_2 + 12Bx_2^2`$
- $`d(RT\ln\gamma_2)/dx_1 = 2(A-3B)x_1 + 12Bx_1^2`$

Then


```math
x_1\left[-2(A+3B)x_2 + 12Bx_2^2\right] + x_2\left[2(A-3B)x_1 + 12Bx_1^2\right] = x_1x_2\left[-12B + 12B(x_1 + x_2)\right] = 0
```


using $`x_1 + x_2 = 1`$. This is guaranteed by the general proof in Section 11, since (66) came from a single $`\underline{G}^{ex}`$.

**Step 4: infinite dilution.** Set $`x_2 = 1`$ in the first of (66) and $`x_1 = 1`$ in the second:


**Equation (67)**

```math
RT\ln\gamma_1^{\infty} = A - B, \qquad RT\ln\gamma_2^{\infty} = A + B
```


So the two constants map directly onto the two infinite-dilution activity coefficients, and $`B`$ measures the asymmetry. With $`B = 0`$, (66) reduces to the one-constant model.

**Step 5: multicomponent mixtures.** Sum over each *pair* of components once:


**Equation (68)**

```math
\underline{G}^{ex} = \sum_{i\lt j} A_{ij}\,x_ix_j
```


where $`A_{ij}`$ is the one-constant parameter fitted to the $`i`$–$`j`$ binary. To differentiate, write $`n\underline{G}^{ex} = \sum_{i\lt j}A_{ij}n_in_j/n`$. Differentiating with respect to $`n_k`$ gives


**Equation (69)**

```math
RT\ln\gamma_k = \sum_{j\neq k} A_{kj}\,x_j - \underline{G}^{ex}
```


*Check:* for a binary, $`Ax_2 - Ax_1x_2 = Ax_2(1 - x_1) = Ax_2^2`$, matching Section 11. ✓

### Motivation and explanation

**Where $`\underline{G}^{ex}`$ comes from.** In practice one measures something that gives a fugacity. For example, in vapour–liquid equilibrium with an ideal-gas vapour, $`\gamma_i = y_iP/(x_iP_i^{\mathrm{SAT}})`$, a result derived in Section 13. That gives $`\underline{G}^{ex} = RT\sum x_i\ln\gamma_i`$ point by point, and the model constants are fitted to the resulting curve. Freezing-point depression and osmotic pressure give the solvent's chemical potential in the same way; both appear later in the course.

**Reading the data.** The figure shows measured $`\underline{G}^{ex}`$ for four binaries.
- Curves 1–3 are positive: hydrocarbons with benzene or CCl₄, and methane–propane. Unlike contacts are unfavourable.
- Curve 4, water–hydrogen peroxide, is strongly negative and clearly skewed, with its minimum near $`x_1 \approx 0.57`$, not 0.5. Water and H₂O₂ hydrogen-bond to each other more strongly than to themselves, and the skew is exactly what $`B`$ is for.

![Measured excess Gibbs energies: (1) trimethylmethane–benzene and (2) trimethylmethane–CCl4 at 0 °C, (3) methane–propane at 100 K, (4) water–hydrogen peroxide at 75 °C](figs/ET-12-excess-gibbs-energy-data.png)

**Why binary data are enough.** Equation (68) assumes the excess Gibbs energy is a sum of pair contributions. This is the same idea as mixing rules for an EOS. It is usually adequate, and it means a ten-component flowsheet needs only binary data, the 45 pairs, not ten-component experiments. Process simulators store binary parameters as functions of $`T`$ for exactly this reason. The approximation fails when three-body effects matter, e.g. a third component that strongly changes the hydrogen-bonding between the other two.

**Pressure.** As shown in Section 10, the pressure dependence of $`\underline{G}^{ex}`$ for liquids is a few J mol⁻¹ per 100 bar, so the parameters are taken as functions of $`T`$ alone.

### Worked example

**Problem.** For water (1) and hydrogen peroxide (2) at 75 °C, the measured $`\underline{G}^{ex}`$ curve has a minimum of ≈ −710 J mol⁻¹ at $`x_1 \approx 0.57`$ (read from the figure). (a) Fit the two-constant Margules model to these two features. (b) Compare with a one-constant fit. (c) Predict the infinite-dilution activity coefficients.

**(a) Two-constant fit.** Require $`\underline{G}^{ex}(0.57) = -710`$ J mol⁻¹ and $`d\underline{G}^{ex}/dx_1 = 0`$ at $`x_1 = 0.57`$. Solving the two equations in $`A`$ and $`B`$ numerically gives $`A = -2781`$ J mol⁻¹ and $`B = -827`$ J mol⁻¹. The fitted curve gives $`\underline{G}^{ex}(0.5) = -695`$ J mol⁻¹, slightly above the minimum, as the skewed data require.

**(b) One-constant fit.** A symmetric model has its minimum at $`x_1 = 0.5`$ with value $`A/4`$. Matching the depth gives $`A = -2840`$ J mol⁻¹, but it cannot put the minimum in the right place.

**(c) Infinite dilution**, from (67) with $`RT = 8.314\times348.15 = 2895`$ J mol⁻¹:

| Model | $`\gamma_1^{\infty}`$ (water dilute in H₂O₂) | $`\gamma_2^{\infty}`$ (H₂O₂ dilute in water) |
|---|---|---|
| Two-constant Margules | 0.51 | 0.29 |
| One-constant Margules | 0.37 | 0.37 |

**Interpretation.** Both activity coefficients are well below 1, so each component is held strongly by the other: a negative deviation, so the mixture is less volatile than Raoult's law predicts. The two-constant fit says the effect is much stronger for H₂O₂ dilute in water than the reverse. The symmetric model averages this away, misjudging $`\gamma^{\infty}`$ by about 30 % at each end. Since the curve minimum is read by eye, all values are estimates. The asymmetry, though, is clearly real.

### Link to other topics

The infinite-dilution activity coefficients in (67) are what ebulliometry measures directly (Section 14). They also set relative volatility at the ends of a distillation column. The pairwise construction (68)–(69) carries over to all the activity-coefficient models surveyed later (Redlich–Kister, van Laar, Wilson, NRTL, UNIQUAC).

### Summary

Adding $`B(x_1 - x_2)`$ to the Margules model breaks the symmetry while keeping it consistent. $`A`$ and $`B`$ correspond directly to the two infinite-dilution activity coefficients. Model constants come from fitting $`\underline{G}^{ex}`$ inferred from measured fugacities, and binary parameters combine pairwise to describe multicomponent mixtures.
<!-- reading-content:end -->

[Previous](<../../../../../notes/Equilibrium Thermodynamics/03 - Activity coefficients and excess Gibbs energy/Complete section.md>) · [Subject index](<../../../../../notes/Equilibrium Thermodynamics/README.md>) · [Next](<../../../../../notes/Equilibrium Thermodynamics/03 - Activity coefficients and excess Gibbs energy/Complete section.md>)
