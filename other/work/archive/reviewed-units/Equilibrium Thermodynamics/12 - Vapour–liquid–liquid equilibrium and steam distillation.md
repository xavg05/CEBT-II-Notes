# Vapour–liquid–liquid equilibrium and steam distillation

## Overview

Partially miscible liquids have large activity coefficients, so their vapour–liquid curves have a minimum-boiling azeotrope. Lowering the pressure drives those curves into the miscibility gap, creating a three-phase line where one vapour coexists with two liquids at a single temperature (Section 42). In the fully immiscible limit each liquid exerts its own vapour pressure, so the mixture boils where the two pure vapour pressures sum to the applied pressure: steam distillation (Section 43).

*Assumed throughout:* minimum-boiling azeotropes (Section 27); liquid–liquid equilibrium and consolute points (Sections 36–37); the phase rule (Section 21).

## Section 42: Vapour–liquid–liquid equilibrium

### Intuition

Two independent things happen as the pressure changes.
- *Boiling temperatures* respond strongly to pressure. Clausius–Clapeyron makes $T^{\mathrm{SAT}}$ fall steeply as $P$ falls.
- *The liquid–liquid gap* barely moves, because $d\mu_i = \bar V_i\,dP$ and liquid volumes are small.

So at high pressure the bubble curve lies above the top of the miscibility gap, and the two regions are separate. At lower pressure the bubble curve drops until its minimum hits the gap. Then a liquid in the gap boils at a single temperature, producing one vapour in equilibrium with both liquids.

### Derivation

**Step 1: phase rule for three phases.** Binary, $C = 2$, three phases (V, $\mathrm{L}_{\mathrm{I}}$, $\mathrm{L}_{\mathrm{II}}$):

$$F = C - P + 2 = 2 - 3 + 2 = 1 \tag{164}$$

At fixed pressure, the three-phase temperature $T^{*}$ and the three compositions ($x_1^{\mathrm{I}}$, $y_1$, $x_1^{\mathrm{II}}$) are all fixed.

**Step 2: equilibrium conditions.** Each component has one fugacity common to all three phases:

$$\gamma_i^{\mathrm{I}}x_i^{\mathrm{I}}P_i^{\mathrm{SAT}} = \gamma_i^{\mathrm{II}}x_i^{\mathrm{II}}P_i^{\mathrm{SAT}} = y_iP, \qquad i = 1, 2 \tag{165}$$

(modified Raoult's law, low pressure). The liquid–liquid part is the equal-activity condition of Section 38; the vapour sets the common value of the activities.

**Step 3: reading the diagram (constant $P$).**
- Above the three-phase line, two vapour–liquid lenses run from each pure boiling point down to the three-phase temperature $T^{*}$.
- At $T^{*}$, a horizontal line joins $x_1^{\mathrm{I}}$, $y_1$ and $x_1^{\mathrm{II}}$.
- Below $T^{*}$, the two-liquid region (the binodal) is cut off at the top by the line.
- The vapour composition $y_1$ lies *between* the two liquid compositions.

![High pressure: the minimum-boiling VLE lens lies wholly above the LLE gap with its upper consolute point](figs/ET-42-VLE-above-LLE.png)

### Motivation and explanation

**Heating a two-liquid mixture at constant $P$** (the green path in the figure below; the decorative drawing on the diagram is not part of the physics):
1. Below $T^{*}$, two liquids at the binodal compositions.
2. At $T^{*}$, vapour of composition $y_1$ appears. The temperature stays at $T^{*}$, because $F = 0$ at fixed $P$, until one liquid phase is used up.
3. For an overall composition different from $y_1$, one liquid remains after the other is exhausted; above $T^{*}$ it coexists with vapour along the bubble and dew curves until the last drop evaporates. If the overall composition equals $y_1$, both liquids can be exhausted together at $T^{*}$, leaving only vapour.

Any feed between $x_1^{\mathrm{I}}$ and $x_1^{\mathrm{II}}$ starts boiling at the same $T^{*}$, the lowest boiling temperature of the system.

The three-phase line fixes the compositions of the phases, not their amounts. Heat can convert some liquid into vapour while the amounts of the two liquid layers adjust to conserve both components. As long as both layers remain, they supply the same common activities and the same equilibrium vapour, so temperature need not rise.

Once a layer is exhausted, its equilibrium condition no longer constrains the system. There are only two phases, so an intensive freedom reappears at fixed pressure and the boiling temperature can change. The special overall composition equal to the three-phase vapour composition permits both layers to disappear together; otherwise the remaining layer carries the excess of one component into the subsequent two-phase stage.

![Lower pressure: the boiling curves drop into the miscibility gap, creating a three-phase line at T* where vapour y1 coexists with liquids xI and xII (heterogeneous azeotrope)](figs/ET-42-VLLE-heteroazeotrope.png)

**Why it is useful.** The vapour from a heterogeneous azeotrope condenses into two liquid layers, which separate by simply decanting. This lets a distillation cross the azeotrope:
- dehydrating ethanol with an entrainer (benzene, cyclohexane);
- the decanter on top of a water-stripping column;
- steam distillation (next section).

**Limits.** If the components are extremely immiscible ($x^{\mathrm{I}}\approx 0$, $x^{\mathrm{II}}\approx 1$), the diagram simplifies: each liquid behaves as nearly pure, which is the basis of the steam-distillation formula. If they are only moderately immiscible, an activity-coefficient model that can predict LLE (NRTL, UNIQUAC, not Wilson) is needed to solve (165).

### Link to other topics

Heterogeneous azeotropic distillation and decanter design in Separations use exactly this diagram, extended to ternary residue-curve maps. Section 43 takes the immiscible limit and derives steam distillation.

### Summary

Lowering the pressure drives the vapour–liquid curves of a partially miscible system down into its miscibility gap. This produces a three-phase line where a vapour coexists with two liquids at a single temperature $T^{*}$ (one degree of freedom, fixed by pressure). Any two-liquid feed boils there, and its condensed vapour splits into two layers. The final section exploits this to distil heat-sensitive organics with steam.

## Section 43: Steam distillation

### Intuition

Each nearly pure liquid layer exerts its own full vapour pressure, regardless of the other layer. Unlike a single mixed liquid, neither dilutes the other. The vapour pressures simply add, so the total reaches 1 atm at a lower temperature than either liquid alone needs. The organic leaves at that low temperature, carried along by the steam. After condensation the two liquids separate again by decanting.

### Derivation

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

### Motivation and explanation

**Why it is valuable.** Natural fragrance and flavour compounds (terpenes such as limonene, boiling at 176 °C) decompose or oxidise near their boiling points. Steam distillation takes them overhead below 100 °C at atmospheric pressure, without vacuum equipment, and the condensate separates into oil and water layers.

**The cost.** By (168), the steam needed per kilogram of product is large when the organic's vapour pressure at $T^{*}$ is small (high-boiling organics). Heavy oils need a lot of steam, which is why vacuum or superheated steam is sometimes combined with the method.

**Limits.**
- Requires real immiscibility. If the organic dissolves appreciably in water, $\gamma$'s depart from the limits in Step 2 and the full equations of Section 42 must be solved.
- Assumes an ideal-gas vapour at low pressure.
- In practice the organic is often trapped in plant material, so mass transfer, not equilibrium, can limit the rate.

### Link to other topics

Steam stripping in refineries, deodorisation of edible oils and recovery of solvents from wastewater all use the same principle. It is also the simplest example of the heterogeneous-azeotrope designs used in Separations.

### Summary

For two immiscible liquids, each layer exerts its own pure vapour pressure, so the mixture boils where $P_1^{\mathrm{SAT}} + P_2^{\mathrm{SAT}} = P$, below both pure boiling points. This lets heat-sensitive, high-boiling organics be distilled with steam below 100 °C, at a steam cost set by the organic's vapour pressure at that temperature. For water–toluene the simple model reproduces the measured heterogeneous azeotrope to within 0.2 K. This completes equilibrium thermodynamics: from the criterion of equal chemical potentials, through fugacity and activity, to vapour–liquid, liquid–liquid and three-phase equilibria.

## Conclusion

When a vapour coexists with two liquids, the binary has one degree of freedom, so at fixed pressure it boils at one temperature whatever the proportions of the liquid layers. In the immiscible limit that temperature is set by $P_1^{\mathrm{SAT}} + P_2^{\mathrm{SAT}} = P$, which lets heat-sensitive organics be distilled with steam below 100 °C. This completes equilibrium thermodynamics: from the criterion of equal chemical potentials, through fugacity and activity, to vapour–liquid, liquid–liquid and three-phase equilibria.
