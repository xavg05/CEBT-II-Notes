[Previous](<ET-42 - Vapour–liquid–liquid equilibrium.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Section 43: Steam distillation

## Intuition

Each nearly pure liquid layer exerts its own full vapour pressure, regardless of the other layer. Unlike a single mixed liquid, neither dilutes the other. The vapour pressures simply add, so the total reaches 1 atm at a lower temperature than either liquid alone needs. The organic leaves at that low temperature, carried along by the steam. After condensation the two liquids separate again by decanting.

## Derivation

**Step 1: equilibrium in both liquids.** From (165) of Section 42:


```math
y_1P = \gamma_1x_1P_1^{\mathrm{SAT}}, \qquad y_2P = \gamma_2x_2P_2^{\mathrm{SAT}}
```


holding for *both* liquid phases, since there is only one vapour.

**Step 2: the immiscible limit.** Let phase I be nearly pure 2, so $`x_2^{\mathrm{I}}\approx 1`$ and $`\gamma_2^{\mathrm{I}}\approx 1`$. Let phase II be nearly pure 1, so $`x_1^{\mathrm{II}}\approx 1`$ and $`\gamma_1^{\mathrm{II}}\approx 1`$. Then


**Equation (166)**

```math
y_2P\approx P_2^{\mathrm{SAT}}, \qquad y_1P\approx P_1^{\mathrm{SAT}}
```


The same partial pressures must hold in the *other* phase, where each component is dilute. This gives $`\gamma_1^{\mathrm{I}}\approx 1/x_1^{\mathrm{I}}`$ and $`\gamma_2^{\mathrm{II}}\approx 1/x_2^{\mathrm{II}}`$: the tiny mutual solubilities are the reciprocals of the large dilute-phase activity coefficients.

**Step 3: total pressure and boiling temperature.** Adding the two parts of (166):

Each partial pressure is set by the liquid layer in which that component is nearly pure. The two near-unity mole fractions belong to *different* liquids, so adding the two partial pressures does not violate mole-fraction normalisation within either phase. A single homogeneous ideal mixture would dilute both components; two immiscible layers each retain almost the pure component's escaping tendency.

Changing the relative amounts of the layers therefore does not change the boiling temperature or equilibrium vapour ratio while both remain present. The mass ratio in (168) converts that vapour composition into the accompanying steam per mass of organic recovered. It does not include steam condensed to heat equipment, losses, or incomplete equilibration with plant material, so actual operating steam consumption can exceed the equilibrium co-distillation ratio.


**Equation (167)**

```math
P = P_1^{\mathrm{SAT}}(T^{*}) + P_2^{\mathrm{SAT}}(T^{*})
```


$`T^{*}`$ is the temperature where the pure vapour pressures sum to the applied pressure. It is below *both* pure boiling points, since each $`P_i^{\mathrm{SAT}}(T^{*}) < P`$.

**Step 4: vapour composition and steam requirement.**


**Equation (168)**

```math
y_{\mathrm{org}} = \frac{P_{\mathrm{org}}^{\mathrm{SAT}}(T^{*})}{P}, \qquad \frac{m_{\mathrm{water}}}{m_{\mathrm{org}}} = \frac{P_{\mathrm{w}}^{\mathrm{SAT}}M_{\mathrm{w}}}{P_{\mathrm{org}}^{\mathrm{SAT}}M_{\mathrm{org}}}
```


The second form follows from the ratio of moles in the vapour times the molar masses.

## Motivation and explanation

**Why it is valuable.** Natural fragrance and flavour compounds (terpenes such as limonene, boiling at 176 °C) decompose or oxidise near their boiling points. Steam distillation takes them overhead below 100 °C at atmospheric pressure, without vacuum equipment, and the condensate separates into oil and water layers.

**The cost.** By (168), the steam needed per kilogram of product is large when the organic's vapour pressure at $`T^{*}`$ is small (high-boiling organics). Heavy oils need a lot of steam, which is why vacuum or superheated steam is sometimes combined with the method.

**Limits.**
- Requires real immiscibility. If the organic dissolves appreciably in water, $`\gamma`$'s depart from the limits in Step 2 and the full equations of Section 42 must be solved.
- Assumes an ideal-gas vapour at low pressure.
- In practice the organic is often trapped in plant material, so mass transfer, not equilibrium, can limit the rate.

## Worked example

**Problem.** At 1 atm, estimate the steam-distillation temperature, vapour composition and steam requirement for (a) toluene and (b) n-decane, as a model high-boiling oil. Compare (a) with the tabulated water–toluene heterogeneous azeotrope (84.1 °C, 79.8 wt % toluene). Vapour pressures are evaluated with Antoine correlations tabulated by NIST, with temperature in kelvin and pressure in bar: water $`(A,B,C)=(5.08354,1663.125,-45.622)`$, toluene $`(4.07827,1343.943,-53.773)`$ and n-decane $`(4.07857,1501.268,-78.67)`$, using $`\log_{10}P^{\mathrm{SAT}}=A-B/(T+C)`$.

**Solving (167) and (168):**

| Organic | Pure boiling point | $`T^{*}`$ | $`y_{\mathrm{org}}`$ (mol) | kg water per kg organic |
|---|---|---|---|---|
| Toluene | 110.6 °C | 84.3 °C | 0.444 | 0.24 |
| n-Decane | 174.1 °C | 97.5 °C | 0.085 | 1.36 |

**Check against data.** For toluene, the predicted 84.3 °C and 80.3 wt % toluene in the vapour (from 0.24 kg water per kg toluene) match the measured 84.1 °C and 79.8 wt % to within 0.2 K and 0.5 %. The immiscible-limit model is excellent here, because the mutual solubilities are small enough for each liquid layer to have activities close to those of its pure major component.

**Interpretation.** Decane, which boils at 174 °C on its own, distils with steam at 97.5 °C, 77 K lower, but needs about 1.4 kg of steam per kg of product because its vapour pressure is still small at that temperature. Even though decane makes up only 8.5 mol % of the vapour, it is over 40 % by mass, because its molar mass (142) is almost eight times water's. The heavy molecule rides out on the steam.

## Link to other topics

Steam stripping in refineries, deodorisation of edible oils and recovery of solvents from wastewater all use the same principle. It is also the simplest example of the heterogeneous-azeotrope designs used in Separations.

## Summary

For two immiscible liquids, each layer exerts its own pure vapour pressure, so the mixture boils where $`P_1^{\mathrm{SAT}} + P_2^{\mathrm{SAT}} = P`$, below both pure boiling points. This lets heat-sensitive, high-boiling organics be distilled with steam below 100 °C, at a steam cost set by the organic's vapour pressure at that temperature. For water–toluene the simple model reproduces the measured heterogeneous azeotrope to within 0.2 K. This completes equilibrium thermodynamics: from the criterion of equal chemical potentials, through fugacity and activity, to vapour–liquid, liquid–liquid and three-phase equilibria.

## Conclusion

When a vapour coexists with two liquids, the binary has one degree of freedom, so at fixed pressure it boils at one temperature whatever the proportions of the liquid layers. In the immiscible limit that temperature is set by $`P_1^{\mathrm{SAT}} + P_2^{\mathrm{SAT}} = P`$, which lets heat-sensitive organics be distilled with steam below 100 °C. This completes equilibrium thermodynamics: from the criterion of equal chemical potentials, through fugacity and activity, to vapour–liquid, liquid–liquid and three-phase equilibria.
<!-- note-content:end -->

[Previous](<ET-42 - Vapour–liquid–liquid equilibrium.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)
