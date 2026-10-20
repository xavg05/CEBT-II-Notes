[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Activity coefficients and excess Gibbs energy

## Overview

Real liquid mixtures are described relative to the ideal mixture, with one correction factor per component, the activity coefficient $`\gamma_i`$, collected into the excess Gibbs energy $`\underline{G}^{ex} = RT\sum x_i\ln\gamma_i`$ (Section 10). Gibbs–Duhem constrains the $`\gamma`$'s, and deriving them all from a single $`\underline{G}^{ex}`$ function satisfies that constraint automatically; the simplest choice is the one-constant Margules model (Section 11). A second constant makes the model asymmetric, parameters are fitted to measured excess Gibbs energies, and binary parameters combine pairwise for multicomponent mixtures (Section 12). A complete calculation for liquid oxygen–argon takes one model constant through to a predicted vapour pressure and derives modified Raoult's law (Section 13).

*Assumed throughout:* ideal-mixture chemical potential (Section 05); fugacity and the Lewis–Randall rule (Section 07); Gibbs–Duhem (Section 04).

## Section 10: The activity coefficient and excess Gibbs energy

*Notation:* superscript "IM" means ideal mixture. Superscript "ex" means excess, i.e. real minus ideal-mixture value at the same $`T`$, $`P`$ and composition. $`\underline{G}_i`$ is pure $`i`$ at the mixture's $`T`$, $`P`$ and phase.

### Intuition

In an ideal mixture each molecule feels the same forces whether its neighbours are its own kind or the other kind. Mixing then only adds entropy: no heat, no volume change. Real liquids are rarely like that.

The figure shows how far from ideal real mixtures are. The volume change on mixing can be positive or negative. Within one family of similar compounds (benzene with C₆F₅Y), the enthalpy of mixing ranges from slightly positive (Y = H) to about −1100 J mol⁻¹ (Y = I). Small chemical changes produce large, hard-to-predict differences.

![Real mixtures: volume change on mixing for methyl formate with methanol (open) and ethanol (filled), and enthalpy change on mixing of benzene with C6F5Y; the ideal-mixture value is zero (red line)](../figs/ET-10-mixing-volume-enthalpy-real-mixtures.png)

The activity coefficient packages all this into one number per component. It says how much more ($`\gamma_i > 1`$) or less ($`\gamma_i < 1`$) a molecule "wants to leave" the mixture than it would in an ideal mixture of the same composition.

*Analogy: a guest at a party.* If the guest likes the other guests less than their own friends ($`\gamma > 1`$), they are keener to leave than an "indifferent" guest would be. If they like them more ($`\gamma < 1`$), they stay. The analogy breaks down because $`\gamma`$ is not about one pair of molecules but the average over all neighbours, and it includes entropic effects (molecular size and orientation), not just "liking".

### Derivation

**Step 1: define $`\gamma_i`$.** Write the real chemical potential as the ideal-mixture value plus a correction:


**Equation (52)**

```math
\mu_i = \underline{G}_i + RT\ln x_i + RT\ln\gamma_i
```


The correction is the **excess chemical potential**:


**Equation (53)**

```math
\mu_i^{ex} \equiv \mu_i - \mu_i^{\mathrm{IM}} = RT\ln\gamma_i
```


**Step 2: excess Gibbs energy.** Use $`\underline{G} = \sum x_i\mu_i`$ for both the real mixture and the ideal mixture, and subtract:


**Equation (54)**

```math
\underline{G}^{ex} \equiv \underline{G} - \underline{G}^{\mathrm{IM}} = \sum_i x_i\mu_i^{ex} = RT\sum_i x_i\ln\gamma_i
```


*Reason:* $`\mu_i^{ex}`$ is the partial molar property of $`G^{ex}`$, just as $`\mu_i`$ is of $`G`$. So, by Euler's theorem (Section 03), the excess Gibbs energy is the mole-fraction-weighted sum. Conversely, $`\gamma_i`$ follows from $`\underline{G}^{ex}`$ by differentiation:


**Equation (55)**

```math
RT\ln\gamma_i = \left(\frac{\partial (n\underline{G}^{ex})}{\partial n_i}\right)_{T,P,n_{j\neq i}}
```


**Step 3: mixing functions.** Subtract the pure-component terms:


**Equation (56)**

```math
\Delta\underline{G}_{\mathrm{mix}} = \underbrace{RT\sum_i x_i\ln x_i}_{\Delta\underline{G}^{\mathrm{IM}}_{\mathrm{mix}}} + \underline{G}^{ex}
```


For the ideal mixture, $`\Delta\underline{H}^{\mathrm{IM}}_{\mathrm{mix}} = \Delta\underline{V}^{\mathrm{IM}}_{\mathrm{mix}} = 0`$ and $`\Delta\underline{S}^{\mathrm{IM}}_{\mathrm{mix}} = -R\sum x_i\ln x_i`$. Every non-zero $`\Delta\underline{H}_{\mathrm{mix}}`$ or $`\Delta\underline{V}_{\mathrm{mix}}`$, like those in the figure, is therefore an excess property.

**Step 4: link to fugacity.** From the definition of fugacity, $`\mu_i - \underline{G}_i = RT\ln(\bar f_i/f_i)`$, where both terms use the same ideal-gas reference. Equating this with (52):

There are two comparisons in (57). The factor $`x_i`$ measures dilution relative to pure liquid $`i`$, whereas $`\gamma_i`$ measures the extra change relative to an *ideal mixture at that dilution*. Consequently, $`\gamma_i>1`$ does not by itself mean the component escapes more readily than from its pure liquid: the full ratio is $`\bar f_i/f_i=x_i\gamma_i`$.

Likewise, a heat or volume of mixing diagnoses a departure from ideality but does not alone give $`\gamma_i`$ at one temperature and pressure. It constrains a derivative of the excess Gibbs energy. Activity coefficients contain both energetic and entropic effects, so a molecular-attraction picture is useful intuition rather than a unique inference from the sign of $`\gamma_i`$.


**Equation (57)**

```math
\gamma_i = \frac{\bar f_i}{x_if_i} \qquad\Longleftrightarrow\qquad \bar f_i = \gamma_i\,x_i\,f_i
```


So $`\gamma_i`$ is the ratio of the actual fugacity to the Lewis–Randall (ideal-mixture) fugacity. The product $`a_i = x_i\gamma_i`$ is called the **activity**.

**Step 5: pressure dependence.** Differentiate (52) with respect to $`P`$ at fixed $`T`$ and composition, using $`(\partial\mu_i/\partial P) = \bar V_i`$ and $`(\partial\underline{G}_i/\partial P) = \underline{V}_i`$:


**Equation (58)**

```math
\left(\frac{\partial\ln\gamma_i}{\partial P}\right)_{T,x} = \frac{\bar V_i - \underline{V}_i}{RT} = \frac{\bar V_i^{ex}}{RT}
```


### Motivation and explanation

**Sign of $`\gamma_i`$.**
- $`\gamma_i > 1`$: $`\mu_i > \mu_i^{\mathrm{IM}}`$, so the escaping tendency is higher than ideal. This is a **positive deviation** from ideality and makes the component more volatile than Raoult's law predicts. Less favourable unlike interactions are a common energetic explanation, but excess entropy can also contribute.
- $`\gamma_i < 1`$: $`\mu_i < \mu_i^{\mathrm{IM}}`$, so the component is held more strongly than in an ideal mixture at the same composition. More favourable unlike interactions, such as hydrogen bonding, can produce this **negative deviation**; size and other entropic effects can also do so.

**Limits.**
- $`x_i\to 1`$: the molecule is surrounded by its own kind, so $`\mu_i\to\underline{G}_i`$ and $`\gamma_i\to 1`$. This is the pure-component reference state of this convention.
- $`x_i\to 0`$: the molecule is surrounded entirely by unlike neighbours, so the deviation is largest. $`\gamma_i`$ tends to its **infinite-dilution** value $`\gamma_i^{\infty}`$.

The Gibbs–Duhem equation requires that $`\gamma_i`$ approach 1 with zero slope near the pure component (next section).

**Why the pressure dependence can be dropped.** Equation (58) says $`\ln\gamma_i`$ changes with pressure only through the excess partial molar volume. For liquids this is tiny, typically a few cm³ mol⁻¹ (see the example). Activity-coefficient models are therefore functions of $`T`$ and composition only, and that is a deliberate approximation.

**Limits of the approach.** $`\gamma_i`$ is defined relative to the pure liquid at the same $`T`$ and $`P`$. If pure $`i`$ cannot exist as a liquid at those conditions (a dissolved gas above its critical temperature, or a dissolved solid), this reference is hypothetical, and other conventions (Henry's law, molality) are used later.

### Link to other topics

Equation (57), $`\bar f_i = \gamma_ix_if_i`$, is the liquid side of the vapour–liquid equilibrium relation used throughout the rest of the course. The fugacity coefficient corrects the vapour; the activity coefficient corrects the liquid. The excess Gibbs energy also controls whether liquids mix at all, which leads to liquid–liquid equilibrium later.

### Summary

The activity coefficient measures, for each component, the departure of its chemical potential from ideal-mixture behaviour, and $`\underline{G}^{ex} = RT\sum x_i\ln\gamma_i`$ collects these into one mixture property. $`\gamma_i > 1`$ means a higher chemical potential than in an ideal mixture at the same composition, and $`\gamma_i\to 1`$ for the pure component. For liquids, $`\gamma_i`$ is effectively independent of pressure.

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

The differentiation must act on the *total* excess Gibbs energy, $`ng(x_1)`$, because adding a mole both increases the system's size and changes its composition. The product rule accounts for the extra amount through $`g`$; the chain rule accounts for the changed environment through the derivative term. Differentiating $`g`$ alone would keep only the second effect and would not give a partial molar property.

For Margules, unlike contacts disappear at either pure endpoint, so $`g`$ vanishes there. Yet inserting one trace molecule into the other pure liquid creates unlike contacts immediately, so the derivative, and hence its infinite-dilution excess chemical potential, can remain finite. Zero mixture excess energy at a pure endpoint does not require zero dilute-solute non-ideality.


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

The denominator $`n`$ in $`\sum_{i\lt j}A_{ij}n_in_j/n`$ changes when $`n_k`$ is increased. Differentiating the numerator gives the interactions involving the added component; differentiating $`1/n`$ gives the common subtraction $`-\underline{G}^{ex}`$ in (69). It represents the dilution of the existing pair contributions as the total amount grows. Treating the mole fractions as independent constants during this derivative would miss it.

The pairwise assumption is a separate choice from thermodynamic consistency. Differentiating one total Gibbs-energy function guarantees consistency, but it cannot prove that binary parameters capture how a third component changes the local environment. The binary limit checks the algebra; multicomponent measurements test that physical assumption.


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

![Measured excess Gibbs energies: (1) trimethylmethane–benzene and (2) trimethylmethane–CCl4 at 0 °C, (3) methane–propane at 100 K, (4) water–hydrogen peroxide at 75 °C](../figs/ET-12-excess-gibbs-energy-data.png)

**Why binary data are enough.** Equation (68) assumes the excess Gibbs energy is a sum of pair contributions. This is the same idea as mixing rules for an EOS. It is usually adequate, and it means a ten-component flowsheet needs only binary data, the 45 pairs, not ten-component experiments. Process simulators store binary parameters as functions of $`T`$ for exactly this reason. The approximation fails when three-body effects matter, e.g. a third component that strongly changes the hydrogen-bonding between the other two.

**Pressure.** As shown in Section 10, the pressure dependence of $`\underline{G}^{ex}`$ for liquids is a few J mol⁻¹ per 100 bar, so the parameters are taken as functions of $`T`$ alone.

### Link to other topics

The infinite-dilution activity coefficients in (67) are what ebulliometry measures directly (Section 14). They also set relative volatility at the ends of a distillation column. The pairwise construction (68)–(69) carries over to all the activity-coefficient models surveyed later (Redlich–Kister, van Laar, Wilson, NRTL, UNIQUAC).

### Summary

Adding $`B(x_1 - x_2)`$ to the Margules model breaks the symmetry while keeping it consistent. $`A`$ and $`B`$ correspond directly to the two infinite-dilution activity coefficients. Model constants come from fitting $`\underline{G}^{ex}`$ inferred from measured fugacities, and binary parameters combine pairwise to describe multicomponent mixtures.

## Section 13: Worked example, liquid oxygen–argon

*Components:* liquid oxygen (1), argon (2).

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

The activity coefficient measures, component by component, how far a liquid mixture departs from ideal mixing; $`\gamma > 1`$ means a higher chemical potential than in an ideal mixture at the same composition. Models are built from $`\underline{G}^{ex}`$ so that they are thermodynamically consistent, and with them modified Raoult's law $`x_i\gamma_iP_i^{\mathrm{SAT}} = y_iP`$ predicts vapour–liquid equilibrium. The next part asks where the model constants come from: measurements of activity coefficients, including from freezing points.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)
