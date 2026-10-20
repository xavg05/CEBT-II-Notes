[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-11 - Thermodynamic consistency and the one-constant Margules model.md>)

<!-- note-content:start -->
# Section 10: The activity coefficient and excess Gibbs energy

*Notation:* superscript "IM" means ideal mixture. Superscript "ex" means excess, i.e. real minus ideal-mixture value at the same $`T`$, $`P`$ and composition. $`\underline{G}_i`$ is pure $`i`$ at the mixture's $`T`$, $`P`$ and phase.

## Intuition

In an ideal mixture each molecule feels the same forces whether its neighbours are its own kind or the other kind. Mixing then only adds entropy: no heat, no volume change. Real liquids are rarely like that.

The figure shows how far from ideal real mixtures are. The volume change on mixing can be positive or negative. Within one family of similar compounds (benzene with C₆F₅Y), the enthalpy of mixing ranges from slightly positive (Y = H) to about −1100 J mol⁻¹ (Y = I). Small chemical changes produce large, hard-to-predict differences.

![Real mixtures: volume change on mixing for methyl formate with methanol (open) and ethanol (filled), and enthalpy change on mixing of benzene with C6F5Y; the ideal-mixture value is zero (red line)](../figs/ET-10-mixing-volume-enthalpy-real-mixtures.png)

The activity coefficient packages all this into one number per component. It says how much more ($`\gamma_i > 1`$) or less ($`\gamma_i < 1`$) a molecule "wants to leave" the mixture than it would in an ideal mixture of the same composition.

*Analogy: a guest at a party.* If the guest likes the other guests less than their own friends ($`\gamma > 1`$), they are keener to leave than an "indifferent" guest would be. If they like them more ($`\gamma < 1`$), they stay. The analogy breaks down because $`\gamma`$ is not about one pair of molecules but the average over all neighbours, and it includes entropic effects (molecular size and orientation), not just "liking".

## Derivation

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


## Motivation and explanation

**Sign of $`\gamma_i`$.**
- $`\gamma_i > 1`$: $`\mu_i > \mu_i^{\mathrm{IM}}`$, so the escaping tendency is higher than ideal. This is a **positive deviation** from ideality and makes the component more volatile than Raoult's law predicts. Less favourable unlike interactions are a common energetic explanation, but excess entropy can also contribute.
- $`\gamma_i < 1`$: $`\mu_i < \mu_i^{\mathrm{IM}}`$, so the component is held more strongly than in an ideal mixture at the same composition. More favourable unlike interactions, such as hydrogen bonding, can produce this **negative deviation**; size and other entropic effects can also do so.

**Limits.**
- $`x_i\to 1`$: the molecule is surrounded by its own kind, so $`\mu_i\to\underline{G}_i`$ and $`\gamma_i\to 1`$. This is the pure-component reference state of this convention.
- $`x_i\to 0`$: the molecule is surrounded entirely by unlike neighbours, so the deviation is largest. $`\gamma_i`$ tends to its **infinite-dilution** value $`\gamma_i^{\infty}`$.

The Gibbs–Duhem equation requires that $`\gamma_i`$ approach 1 with zero slope near the pure component (next section).

**Why the pressure dependence can be dropped.** Equation (58) says $`\ln\gamma_i`$ changes with pressure only through the excess partial molar volume. For liquids this is tiny, typically a few cm³ mol⁻¹ (see the example). Activity-coefficient models are therefore functions of $`T`$ and composition only, and that is a deliberate approximation.

**Limits of the approach.** $`\gamma_i`$ is defined relative to the pure liquid at the same $`T`$ and $`P`$. If pure $`i`$ cannot exist as a liquid at those conditions (a dissolved gas above its critical temperature, or a dissolved solid), this reference is hypothetical, and other conventions (Henry's law, molality) are used later.

## Link to other topics

Equation (57), $`\bar f_i = \gamma_ix_if_i`$, is the liquid side of the vapour–liquid equilibrium relation used throughout the rest of the course. The fugacity coefficient corrects the vapour; the activity coefficient corrects the liquid. The excess Gibbs energy also controls whether liquids mix at all, which leads to liquid–liquid equilibrium later.

## Summary

The activity coefficient measures, for each component, the departure of its chemical potential from ideal-mixture behaviour, and $`\underline{G}^{ex} = RT\sum x_i\ln\gamma_i`$ collects these into one mixture property. $`\gamma_i > 1`$ means a higher chemical potential than in an ideal mixture at the same composition, and $`\gamma_i\to 1`$ for the pure component. For liquids, $`\gamma_i`$ is effectively independent of pressure.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-11 - Thermodynamic consistency and the one-constant Margules model.md>)
