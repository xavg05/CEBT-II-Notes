# Section 14: Measuring activity coefficients

## Overview

Activity-coefficient models are consistent interpolating functions, and their constants have to come from measurements of $\gamma_i$ for binary mixtures. This note covers the main routes:
1. infinite-dilution ebulliometry, which gives $\gamma^{\infty}$ from boiling pressures alone;
2. dynamic stills ($P$–$T$–$x$–$y$ data);
3. static stills ($P$–$T$–$x$ data);
4. freezing-point depression, azeotropes and osmotic pressure, for systems where vapour pressures are awkward.

The key derivation shows how Gibbs–Duhem lets a pressure slope give $\gamma^{\infty}$ with no composition analysis at all.

*Assumed:* modified Raoult's law $x_i\gamma_iP_i^{\mathrm{SAT}} = y_iP$ for an ideal-gas vapour (Section 13); the binary Gibbs–Duhem equation $x_1\,d\ln\gamma_1 + x_2\,d\ln\gamma_2 = 0$ (Section 11); two-constant Margules with $RT\ln\gamma_1^{\infty} = A - B$, $RT\ln\gamma_2^{\infty} = A + B$ (Section 12).

## Intuition

A model with $k$ constants needs, in principle, only $k$ good data points. The most informative points are at the two ends of the composition range: there each component is infinitely dilute, its $\gamma$ is furthest from 1, and the two values $\gamma_1^{\infty}$ and $\gamma_2^{\infty}$ pin down a two-constant model directly.

Ebulliometry exploits a neat feature of the dilute limit. Add a trace of component 1 to boiling pure component 2 at fixed $T$, and the pressure changes in proportion to how "eager to escape" component 1 is, i.e. to $\gamma_1^{\infty}$. Gibbs–Duhem guarantees that the solvent's own $\gamma$ does not change to first order, so the pressure slope reflects the solute alone.

## Derivation

**Step 1: total pressure of a binary.** Sum modified Raoult's law over both components ($y_1 + y_2 = 1$):

$$P = x_1\gamma_1P_1^{\mathrm{SAT}} + x_2\gamma_2P_2^{\mathrm{SAT}} \tag{1}$$

**Step 2: differentiate at constant $T$.** The $P_i^{\mathrm{SAT}}$ are fixed, and only the composition (and hence the $\gamma_i$) varies:

$$dP = \sum_i \gamma_iP_i^{\mathrm{SAT}}\left(dx_i + x_i\,\frac{d\gamma_i}{\gamma_i}\right)$$

**Step 3: binary, with $dx_2 = -dx_1$.**

$$dP = \gamma_1P_1^{\mathrm{SAT}}\left(dx_1 + x_1\,d\ln\gamma_1\right) + \gamma_2P_2^{\mathrm{SAT}}\left(x_2\,d\ln\gamma_2 - dx_1\right)$$

**Step 4: eliminate $d\ln\gamma_1$ with Gibbs–Duhem.** Substitute $x_1\,d\ln\gamma_1 = -x_2\,d\ln\gamma_2$:

$$dP = \left(\gamma_1P_1^{\mathrm{SAT}} - \gamma_2P_2^{\mathrm{SAT}}\right)\left(dx_1 - x_2\,d\ln\gamma_2\right) \tag{2}$$

**Step 5: the limit $x_1\to 0$.**
- Pure 2: $\gamma_2 = 1$ and $\gamma_1 = \gamma_1^{\infty}$.
- Gibbs–Duhem gives $x_2\,d\ln\gamma_2 = -x_1\,d\ln\gamma_1 \to 0$, so the solvent's $\gamma$ is flat there.

Dividing (2) by $dx_1$:

$$\left(\frac{\partial P}{\partial x_1}\right)_T\bigg|_{x_1=0} = \gamma_1^{\infty}P_1^{\mathrm{SAT}} - P_2^{\mathrm{SAT}} \;\;\Rightarrow\;\; \gamma_1^{\infty} = \frac{P_2^{\mathrm{SAT}} + \left(\partial P/\partial x_1\right)_T\big|_{x_1=0}}{P_1^{\mathrm{SAT}}} \tag{3}$$

The same argument at the other end ($x_2\to 0$) gives $\gamma_2^{\infty}$. Experimentally, the slope is estimated as $\Delta P/\Delta x_1$ after adding a weighed small amount of 1. The liquid composition is known from the amounts added, and no vapour analysis is needed.

![Isothermal P–x–y diagram: the bubble-point (liquid) curve's slopes at the two pure ends give the infinite-dilution activity coefficients](figs/ET-14-ebulliometry-slopes.png)

**Step 6: fixing the model.** With $\gamma_1^{\infty}$ and $\gamma_2^{\infty}$ measured, the two-constant Margules constants follow from Section 12:

$$A = \frac{RT}{2}\left(\ln\gamma_1^{\infty} + \ln\gamma_2^{\infty}\right), \qquad B = \frac{RT}{2}\left(\ln\gamma_2^{\infty} - \ln\gamma_1^{\infty}\right) \tag{4}$$

The van Laar model can be fixed from the same pair.

**Other routes.**
- *Dynamic still:* boil, separate the liquid and vapour at equilibrium, analyse both, and get each $\gamma_i = y_iP/(x_iP_i^{\mathrm{SAT}})$ directly. This gives many points over $T$ and $x$, but analysing both phases is laborious.
- *Static still:* measure only $P$ against $x$ at fixed $T$ in a sealed, degassed cell. The data are fitted to (1) with a model for both $\gamma$'s. The measurements are easier and more accurate, but the fit is non-linear because both $\gamma$'s appear in one equation. Historically this has been the most important method.
- *Freezing point and osmotic pressure* give the solvent's activity when vapour pressures are too low to measure (next section and later).
- *Azeotropes* give both $\gamma$'s at one composition without any composition analysis (later).

## Motivation and explanation

**Why Gibbs–Duhem is the key step.** Without it, the slope (2) would depend on how both $\gamma$'s change, and one measurement could not separate them. Near pure 2, the solvent's activity coefficient is stationary, so all the change in $P$ comes from adding a component with escaping tendency $\gamma_1^{\infty}P_1^{\mathrm{SAT}}$ while diluting one with $P_2^{\mathrm{SAT}}$.

**Sign of the slope.** By (3), the slope is positive if $\gamma_1^{\infty}P_1^{\mathrm{SAT}} > P_2^{\mathrm{SAT}}$. So adding a trace of a less volatile solute can still *raise* the pressure, if its activity coefficient is large enough.

**Assumptions and limits.**
- Ideal-gas vapour and negligible Poynting factors (modified Raoult's law).
- Constant $T$.
- A truly limiting slope. Finite additions measure a chord, not a tangent, and the error grows with $\Delta x$.
- Pressure differences are small, so the method needs very good pressure (or, in constant-pressure ebulliometers, temperature) resolution.

## Worked example

**Problem.** Use the oxygen (1)–argon (2) model of Section 13 ($A = 148$ J mol⁻¹ at 83.8 K, so $\gamma^{\infty} = e^{A/RT} = 1.237$) to simulate an ebulliometry experiment, with $P_1^{\mathrm{SAT}} = 0.4917$ bar and $P_2^{\mathrm{SAT}} = 0.6892$ bar. (a) What pressure change follows adding 1 mol % oxygen to boiling argon? (b) What $\gamma_1^{\infty}$ would be inferred from (3), and how sensitive is it to pressure error?

**(a) Expected slope** from (3): $\gamma_1^{\infty}P_1^{\mathrm{SAT}} - P_2^{\mathrm{SAT}} = 1.237\times0.4917 - 0.6892 = -0.0812$ bar per unit $x_1$. Evaluating (1) exactly at $x_1 = 0.01$ gives $\Delta P = -82$ Pa; at $x_1 = 0.001$, $\Delta P = -8.1$ Pa. Oxygen is less volatile than argon here, so even with $\gamma > 1$ the pressure falls.

**(b) Back-calculation.**

| Addition $\Delta x_1$ | Chord slope (bar) | Inferred $\gamma_1^{\infty}$ | True value |
|---|---|---|---|
| 0.01 | −0.0823 | 1.234 | 1.237 |
| 0.001 | −0.0813 | 1.236 | 1.237 |

The same analysis at the argon-dilute end gives $\gamma_2^{\infty} = 1.233$ (for $\Delta x = 0.01$). Feeding both into (4) recovers $A = 146$ J mol⁻¹ and $B = -0.4$ J mol⁻¹ (essentially zero), i.e. the original symmetric model.

**Sensitivity.** With $\Delta x_1 = 0.01$, a 1 Pa error in $\Delta P$ shifts the slope by $10^{-3}$ bar and $\gamma_1^{\infty}$ by $10^{-3}/0.4917 = 0.002$. So pascal-level pressure resolution is needed for three-figure $\gamma^{\infty}$, which is why dedicated ebulliometers are precision instruments.

## Link to other topics

Infinite-dilution activity coefficients are the most useful single numbers for separation design. They set the relative volatility of trace components at column ends, and they are the input to predictive group-contribution methods. Freezing-point depression, the next route, uses the same equal-chemical-potential logic but with a solid phase in place of the vapour.

## Conclusion

Activity coefficients come from experiments that measure a fugacity. Ebulliometry is the most elegant: by Gibbs–Duhem, the limiting slope of pressure against composition at fixed $T$ gives $\gamma^{\infty}$ directly via (3), without analysing any phase, and the two limiting values fix a two-constant model. Dynamic and static stills give data over the whole composition range. Freezing-point depression extends the measurements to involatile systems, which is the subject of the next section.
