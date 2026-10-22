[Previous](<ET-42 - Vapour–liquid–liquid equilibrium.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Section 43: Steam distillation

## Intuition

Each nearly pure liquid layer exerts its own full vapour pressure, regardless of the other layer. Unlike a single mixed liquid, neither dilutes the other. The vapour pressures simply add, so the total reaches 1 atm at a lower temperature than either liquid alone needs. The organic leaves at that low temperature, carried along by the steam. After condensation the two liquids separate again by decanting.

## Derivation

**Step 1: equilibrium in both liquids.** From (165) of Section 42:

$$y_1P = \gamma_1x_1P_1^{\mathrm{SAT}}, \qquad y_2P = \gamma_2x_2P_2^{\mathrm{SAT}}$$

holding for *both* liquid phases, since there is only one vapour.

**Step 2: the immiscible limit.** Let phase I be nearly pure 2, so $x_2^{\mathrm{I}}\approx 1$ and $\gamma_2^{\mathrm{I}}\approx 1$. Let phase II be nearly pure 1, so $x_1^{\mathrm{II}}\approx 1$ and $\gamma_1^{\mathrm{II}}\approx 1$. Then

$$y_2P\approx P_2^{\mathrm{SAT}}, \qquad y_1P\approx P_1^{\mathrm{SAT}} \tag{166}$$

The same partial pressures must hold in the *other* phase, where each component is dilute. This gives $\gamma_1^{\mathrm{I}}\approx 1/x_1^{\mathrm{I}}$ and $\gamma_2^{\mathrm{II}}\approx 1/x_2^{\mathrm{II}}$: the tiny mutual solubilities are the reciprocals of the large dilute-phase activity coefficients.

**Step 3: total pressure and boiling temperature.** Adding the two parts of (166):

Each partial pressure is set by the liquid layer in which that component is nearly pure. The two near-unity mole fractions belong to *different* liquids, so adding the two partial pressures does not violate mole-fraction normalisation within either phase. A single homogeneous ideal mixture would dilute both components; two immiscible layers each retain almost the pure component's escaping tendency.

Changing the relative amounts of the layers therefore does not change the boiling temperature or equilibrium vapour ratio while both remain present. The mass ratio in (168) converts that vapour composition into the accompanying steam per mass of organic recovered. It does not include steam condensed to heat equipment, losses, or incomplete equilibration with plant material, so actual operating steam consumption can exceed the equilibrium co-distillation ratio.

$$P = P_1^{\mathrm{SAT}}(T^{*}) + P_2^{\mathrm{SAT}}(T^{*}) \tag{167}$$

$T^{*}$ is the temperature where the pure vapour pressures sum to the applied pressure. It is below *both* pure boiling points, since each $P_i^{\mathrm{SAT}}(T^{*}) < P$.

**Step 4: vapour composition and steam requirement.**

$$y_{\mathrm{org}} = \frac{P_{\mathrm{org}}^{\mathrm{SAT}}(T^{*})}{P}, \qquad \frac{m_{\mathrm{water}}}{m_{\mathrm{org}}} = \frac{P_{\mathrm{w}}^{\mathrm{SAT}}M_{\mathrm{w}}}{P_{\mathrm{org}}^{\mathrm{SAT}}M_{\mathrm{org}}} \tag{168}$$

The second form follows from the ratio of moles in the vapour times the molar masses.

## Motivation and explanation

**Steam cost depends on vapour composition by mass.** A high-boiling organic can distil below water's normal boiling point because its vapour pressure adds to water's. But a low organic vapour mole fraction means more steam is needed per mole of recovered organic. Conversion to mass must include both molar masses: a heavy organic may be a substantial mass fraction even when a small mole fraction.
Using $\log_{10}(P^{\mathrm{SAT}}/\mathrm{bar})=A-B/(T+C)$ with $T$ in kelvin, Antoine triples $(A,B,C)$ are $(5.08354,1663.125,-45.622)$ for water, $(4.07827,1343.943,-53.773)$ for toluene and $(4.07857,1501.268,-78.67)$ for n-decane. Solving the immiscible-limit boiling condition at 1 atm gives:

| Organic | Boiling mixture temperature | Organic vapour mole fraction | kg water per kg organic |
|---|---|---|---|
| Toluene | 84.3 °C | 0.444 | 0.24 |
| n-Decane | 97.5 °C | 0.085 | 1.36 |

The toluene prediction is close to the measured heterogeneous azeotrope at 84.1 °C and 79.8 wt % toluene, consistent with small mutual solubilities. Decane's vapour is only about 8.5 mol % organic but about 42 % organic by mass, using molar masses 142.29 and $18.015\ \mathrm{g\,mol^{-1}}$. Steam distillation reduces thermal exposure at a real steam cost. These are equilibrium requirements; release from a plant matrix or a liquid film can additionally limit the actual recovery rate.

**Why it is valuable.** Natural fragrance and flavour compounds (terpenes such as limonene, boiling at 176 °C) decompose or oxidise near their boiling points. Steam distillation takes them overhead below 100 °C at atmospheric pressure, without vacuum equipment, and the condensate separates into oil and water layers.

**The cost.** By (168), the steam needed per kilogram of product is large when the organic's vapour pressure at $T^{*}$ is small (high-boiling organics). Heavy oils need a lot of steam, which is why vacuum or superheated steam is sometimes combined with the method.

**Limits.**
- Requires real immiscibility. If the organic dissolves appreciably in water, $\gamma$'s depart from the limits in Step 2 and the full equations of Section 42 must be solved.
- Assumes an ideal-gas vapour at low pressure.
- In practice the organic is often trapped in plant material, so mass transfer, not equilibrium, can limit the rate.

## Link to other topics

Steam stripping in refineries, deodorisation of edible oils and recovery of solvents from wastewater all use the same principle. It is also the simplest example of the heterogeneous-azeotrope designs used in Separations.

## Summary

For two immiscible liquids, each layer exerts its own pure vapour pressure, so the mixture boils where $P_1^{\mathrm{SAT}} + P_2^{\mathrm{SAT}} = P$, below both pure boiling points. This lets heat-sensitive, high-boiling organics be distilled with steam below 100 °C, at a steam cost set by the organic's vapour pressure at that temperature. For water–toluene the simple model reproduces the measured heterogeneous azeotrope to within 0.2 K. This completes equilibrium thermodynamics: from the criterion of equal chemical potentials, through fugacity and activity, to vapour–liquid, liquid–liquid and three-phase equilibria.

## Conclusion

When a vapour coexists with two liquids, the binary has one degree of freedom, so at fixed pressure it boils at one temperature whatever the proportions of the liquid layers. In the immiscible limit that temperature is set by $P_1^{\mathrm{SAT}} + P_2^{\mathrm{SAT}} = P$, which lets heat-sensitive organics be distilled with steam below 100 °C. This completes equilibrium thermodynamics: from the criterion of equal chemical potentials, through fugacity and activity, to vapour–liquid, liquid–liquid and three-phase equilibria.
<!-- note-content:end -->

[Previous](<ET-42 - Vapour–liquid–liquid equilibrium.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)
