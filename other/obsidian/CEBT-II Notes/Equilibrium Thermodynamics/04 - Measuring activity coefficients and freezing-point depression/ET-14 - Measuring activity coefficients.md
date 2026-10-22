[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-15 - Freezing-point depression.md>)

<!-- note-content:start -->
# Section 14: Measuring activity coefficients

## Intuition

A model with $k$ constants needs, in principle, only $k$ good data points. The most informative points are at the two ends of the composition range: there each component is infinitely dilute, its $\gamma$ is furthest from 1, and the two values $\gamma_1^{\infty}$ and $\gamma_2^{\infty}$ pin down a two-constant model directly.

Ebulliometry exploits a neat feature of the dilute limit. Add a trace of component 1 to boiling pure component 2 at fixed $T$, and the pressure changes in proportion to how "eager to escape" component 1 is, i.e. to $\gamma_1^{\infty}$. Gibbs–Duhem guarantees that the solvent's own $\gamma$ does not change to first order, so the pressure slope reflects the solute alone.

## Derivation

**Step 1: total pressure of a binary.** Sum modified Raoult's law over both components ($y_1 + y_2 = 1$):

$$P = x_1\gamma_1P_1^{\mathrm{SAT}} + x_2\gamma_2P_2^{\mathrm{SAT}} \tag{74}$$

**Step 2: differentiate at constant $T$.** The $P_i^{\mathrm{SAT}}$ are fixed, and only the composition (and hence the $\gamma_i$) varies:

$$dP = \sum_i \gamma_iP_i^{\mathrm{SAT}}\left(dx_i + x_i\,\frac{d\gamma_i}{\gamma_i}\right)$$

**Step 3: binary, with $dx_2 = -dx_1$.**

$$dP = \gamma_1P_1^{\mathrm{SAT}}\left(dx_1 + x_1\,d\ln\gamma_1\right) + \gamma_2P_2^{\mathrm{SAT}}\left(x_2\,d\ln\gamma_2 - dx_1\right)$$

**Step 4: eliminate $d\ln\gamma_1$ with Gibbs–Duhem.** Substitute $x_1\,d\ln\gamma_1 = -x_2\,d\ln\gamma_2$:

$$dP = \left(\gamma_1P_1^{\mathrm{SAT}} - \gamma_2P_2^{\mathrm{SAT}}\right)\left(dx_1 - x_2\,d\ln\gamma_2\right) \tag{75}$$

**Step 5: the limit $x_1\to 0$.**
- Pure 2: $\gamma_2 = 1$ and $\gamma_1 = \gamma_1^{\infty}$.
- Gibbs–Duhem gives $x_2\,d\ln\gamma_2 = -x_1\,d\ln\gamma_1 \to 0$, so the solvent's $\gamma$ is flat there.

Dividing (75) by $dx_1$:

$$\left(\frac{\partial P}{\partial x_1}\right)_T\bigg|_{x_1=0} = \gamma_1^{\infty}P_1^{\mathrm{SAT}} - P_2^{\mathrm{SAT}} \;\;\Rightarrow\;\; \gamma_1^{\infty} = \frac{P_2^{\mathrm{SAT}} + \left(\partial P/\partial x_1\right)_T\big|_{x_1=0}}{P_1^{\mathrm{SAT}}} \tag{76}$$

The same argument at the other end ($x_2\to 0$) gives $\gamma_2^{\infty}$. Experimentally, the slope is estimated as $\Delta P/\Delta x_1$ after adding a weighed small amount of 1. The liquid composition is known from the amounts added, and no vapour analysis is needed.

![Isothermal P–x–y diagram: the bubble-point (liquid) curve's slopes at the two pure ends give the infinite-dilution activity coefficients](../figs/ET-14-ebulliometry-slopes.png)

**Step 6: fixing the model.** With $\gamma_1^{\infty}$ and $\gamma_2^{\infty}$ measured, the two-constant Margules constants follow from Section 12:

$$A = \frac{RT}{2}\left(\ln\gamma_1^{\infty} + \ln\gamma_2^{\infty}\right), \qquad B = \frac{RT}{2}\left(\ln\gamma_2^{\infty} - \ln\gamma_1^{\infty}\right) \tag{77}$$

The van Laar model can be fixed from the same pair.

**Other routes.**
- *Dynamic still:* boil, separate the liquid and vapour at equilibrium, analyse both, and get each $\gamma_i = y_iP/(x_iP_i^{\mathrm{SAT}})$ directly. This gives many points over $T$ and $x$, but analysing both phases is laborious.
- *Static still:* measure only $P$ against $x$ at fixed $T$ in a sealed, degassed cell. The data are fitted to (74) with a model for both $\gamma$'s. The measurements are easier and more accurate, but the fit is non-linear because both $\gamma$'s appear in one equation. Historically this has been the most important method.
- *Freezing point and osmotic pressure* give the solvent's activity when vapour pressures are too low to measure (next section and later).
- *Azeotropes* give both $\gamma$'s at one composition without any composition analysis (later).

## Motivation and explanation

**Why measuring a dilute slope requires precision.** In ebulliometry the initial pressure slope is $\gamma_1^\infty P_1^{\mathrm{SAT}}-P_2^{\mathrm{SAT}}$: adding solute contributes its vapour and simultaneously displaces solvent. The measured slope can be small because these two contributions nearly cancel.
A finite composition addition measures a chord rather than the desired tangent. Making the addition smaller reduces curvature bias, but the measured pressure change also shrinks. With fixed absolute pressure uncertainty $\delta P$, the corresponding uncertainty in the inferred dilute coefficient scales as $\delta\gamma_1^\infty\approx\delta P/(\Delta x_1P_1^{\mathrm{SAT}})$. Thus shrinking the addition amplifies noise. Agreement between two end-limit fits does not remove this sensitivity; both curvature and measurement resolution must be assessed.

**Why Gibbs–Duhem is the key step.** Without it, the slope (75) would depend on how both $\gamma$'s change, and one measurement could not separate them. Near pure 2, the solvent's activity coefficient is stationary, so all the change in $P$ comes from adding a component with escaping tendency $\gamma_1^{\infty}P_1^{\mathrm{SAT}}$ while diluting one with $P_2^{\mathrm{SAT}}$.

**Sign of the slope.** By (76), the slope is positive if $\gamma_1^{\infty}P_1^{\mathrm{SAT}} > P_2^{\mathrm{SAT}}$. So adding a trace of a less volatile solute can still *raise* the pressure, if its activity coefficient is large enough.

**Assumptions and limits.**
- Ideal-gas vapour and negligible Poynting factors (modified Raoult's law).
- Constant $T$.
- A truly limiting slope. Finite additions measure a chord, not a tangent, and the error grows with $\Delta x$.
- Pressure differences are small, so the method needs very good pressure (or, in constant-pressure ebulliometers, temperature) resolution.

## Link to other topics

Infinite-dilution activity coefficients are the most useful single numbers for separation design. They set the relative volatility of trace components at column ends, and they are the input to predictive group-contribution methods. Freezing-point depression, the next route, uses the same equal-chemical-potential logic but with a solid phase in place of the vapour.

## Summary

Activity coefficients come from experiments that measure a fugacity. Ebulliometry is the most elegant: by Gibbs–Duhem, the limiting slope of pressure against composition at fixed $T$ gives $\gamma^{\infty}$ directly via (76), without analysing any phase, and the two limiting values fix a two-constant model. Dynamic and static stills give data over the whole composition range.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-15 - Freezing-point depression.md>)
