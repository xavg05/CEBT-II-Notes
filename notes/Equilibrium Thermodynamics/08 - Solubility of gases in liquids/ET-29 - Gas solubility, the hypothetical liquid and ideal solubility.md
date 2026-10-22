[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-30 - solubility of methane.md>)

<!-- note-content:start -->
# Section 29: Gas solubility, the hypothetical liquid and ideal solubility

## Intuition

Above $`T_c`$ there is no vapour-pressure curve to read $`P^{\mathrm{SAT}}`$ from. But the curve does not stop abruptly in any physical sense; it just ends at the critical point. Continue it smoothly past $`T_c`$ and read off a "vapour pressure" at the temperature of interest. That value describes a liquid that cannot exist on its own, but it is a perfectly good *reference number*, as long as every calculation uses it consistently.

Ideal solubility then asks: if the dissolved gas mixed ideally with the solvent ($`\gamma = 1`$), how much would dissolve? The answer depends only on the gas, not on the solvent, which makes it a useful yardstick.

## Derivation

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

## Motivation and explanation

**Why solvent-independent.** Equation (140) contains only properties of the gas ($`f_i^{\,l}`$) and of the vapour ($`y_iP`$). Every solvent would dissolve the same amount if mixing were ideal. Real solvents differ through $`\gamma_i`$, which by (141) is read straight from measurements.

**Trends.**
- Gases with low $`T_c`$ (He, H₂, N₂) are far above $`T_c`$, so $`f^{\,l}`$ is large and solubility is low.
- Gases closer to $`T_c`$ (CO₂, ethane) have a smaller hypothetical vapour pressure and are more soluble.
- Solubility is proportional to the gas partial pressure (at fixed $`f^{\,l}`$), the root of Henry's law (Section 31).

**Limits.** The hypothetical liquid is a convention, so $`\gamma`$'s computed with it depend on that convention. The chart is for non-polar gases at modest pressure. Polar or reacting gases (NH₃, SO₂, CO₂ in water) need other treatments.

## Link to other topics

Gas solubility governs absorption columns (CO₂ capture, acid-gas removal), bioreactor aeration, and gas–liquid reactors. Section 30 works through ideal and real solubilities for methane in three solvents.

## Summary

For a supercritical solute the pure-liquid reference is hypothetical, and its fugacity is obtained by extrapolating the saturation curve, best done with a corresponding-states chart of $`f^{\,l}/P_c`$ against $`T/T_c`$. The ideal solubility $`x^{\mathrm{ideal}} = y_iP/f_i^{\,l}`$ is solvent-independent, and the ratio $`x^{\mathrm{ideal}}/x`$ is the gas's activity coefficient in a given solvent.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-30 - solubility of methane.md>)
