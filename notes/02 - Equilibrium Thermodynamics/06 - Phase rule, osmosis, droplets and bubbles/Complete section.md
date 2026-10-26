[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Phase rule, osmosis, droplets and bubbles

## Overview

The Gibbs phase rule $`F = C - P + 2`$ counts the independent intensive variables of a system at equilibrium, assuming equal pressures and that every component can reach every phase (Section 21). Relaxing those assumptions gives three familiar effects. A semipermeable membrane frees the pressure on the solution side, giving osmotic pressure, about 27 bar for sea water (Section 22). Surface tension raises the pressure inside a droplet, so small droplets have a higher vapour pressure: the Kelvin equation, which explains supersaturated vapour and cloud nucleation (Section 23). Inside a bubble the curvature is reversed, so liquids must be superheated to boil, and a dissolved solute raises the boiling point (Section 24).

*Assumed throughout:* equal $`T`$, $`P`$ and $`\mu_i`$ at equilibrium (Section 01); $`\mu_1 = \underline{G}_1 + RT\ln(\gamma_1x_1)`$ (Section 10); the Poynting correction (Section 06); freezing-point depression (Section 15).

## Section 21: The Gibbs phase rule

*Notation:* $`C`$ is the number of components, $`P`$ the number of phases, $`F`$ the number of degrees of freedom (independent intensive variables). Here $`P`$ is a count, not a pressure.

### Intuition

Intensive variables (temperature, pressure, compositions) describe the *state* of each phase, not how much of it there is. They come in pairs with the extensive quantity that flows when they differ:
- temperature with entropy (heat flows);
- pressure with volume (boundaries move);
- chemical potential with amount (matter moves).

Equilibrium means nothing flows. Each pair of phases must therefore agree on each driving force, and every such agreement removes one freedom.

### Derivation

**Step 1: variables.** A single phase with $`C`$ components needs $`T`$, $`P`$ and $`C - 1`$ independent mole fractions (they sum to 1): $`C + 1`$ intensive variables. For $`P`$ separate phases with no connection between them:


**Equation (110)**

```math
\text{variables} = P\,(C - 1 + 2)
```


**Step 2: constraints from equilibrium.** Between $`P`$ phases there are $`P - 1`$ independent equalities for each equilibrium condition:
- thermal: $`T^{\mathrm{I}} = T^{\mathrm{II}} = \dots`$, giving $`P - 1`$ equations;
- mechanical: $`P^{\mathrm{I}} = P^{\mathrm{II}} = \dots`$, giving $`P - 1`$ equations (true for flat interfaces);
- chemical: $`\mu_i^{\mathrm{I}} = \mu_i^{\mathrm{II}} = \dots`$ for each of the $`C`$ components, giving $`C(P - 1)`$ equations.

Choose one phase as a reference and equate each of the others to it. That gives $`P-1`$ independent equalities for a given intensive quantity. Equating every possible pair would count some conditions twice: once two phases both match the reference, they already match each other. This is the reason for the factor $`P-1`$, rather than the number of phase pairs.

Changing a phase amount does not necessarily change any intensive state variable. Water can evaporate into steam at a fixed coexistence temperature and pressure while their amounts change. The phase rule counts which coexistence states are possible; conservation balances and any specified total volume or enthalpy determine how much of each phase occupies that state.


**Equation (111)**

```math
\text{constraints} = (P - 1)(2 + C)
```


**Step 3: degrees of freedom.** Subtract (111) from (110):


**Equation (112)**

```math
F = P(C + 1) - (P - 1)(C + 2) = C - P + 2
```


This counts intensive variables only. How much of each phase is present is extra, extensive information (fixed later by mass balances, e.g. the lever rule).

**Step 4: when the count changes.** Each constraint in Step 2 assumes something physical:
- equal pressures need a flat, free interface;
- equal $`\mu_i`$ needs component $`i`$ to be able to cross every interface and be present in every phase;
- a chemical reaction adds a constraint (an equilibrium constant) and reduces $`F`$.

Whenever one of these fails, the count must be redone from Steps 1–2 rather than by applying (112) blindly.

### Motivation and explanation

**Reading a phase diagram through degrees of freedom.** Pure liquid and vapour have $`F=1`$: choosing their coexistence temperature fixes the pressure. Adding a third pure phase gives $`F=0`$, which is why the triple point is reproducible. For a binary, liquid–vapour equilibrium has $`F=2`$, whereas two liquids plus vapour have $`F=1`$. Specifying pressure in the latter case fixes the boiling temperature and all three phase compositions. Changing the overall feed composition then changes phase amounts rather than those intensive equilibrium values, provided every phase remains present.
The critical point is not an extra phase. It is where two phases become identical and the coexistence line ends.
![Pure-water phase diagram: single-phase regions have two degrees of freedom, coexistence lines one, and the triple point zero](../figs/ET-21-water-phase-diagram.png)

**What $`F`$ means physically.**
- $`F = 2`$: an area on a phase diagram. A single-phase pure fluid can have any $`T`$ and $`P`$.
- $`F = 1`$: a line. Liquid and vapour of a pure substance coexist only along the vapour-pressure curve; choose $`T`$ and $`P`$ is fixed.
- $`F = 0`$: a point. The triple point is fixed by nature, which is why it is used to define temperature scales.

**For mixtures.** A binary in vapour–liquid equilibrium has $`F = 2 - 2 + 2 = 2`$. Fix $`T`$ and the liquid composition, and the pressure and vapour composition follow. That is exactly what was done for oxygen–argon (Section 13): $`T = 83.8`$ K and $`x_1 = 0.3`$ gave $`P`$ and $`y_1`$.

**A common slip.** Air dissolved in or above water adds components, so "water boiling at 100 °C under 1 atm of air" is not a one-component system. With an insoluble inert gas present, the liquid–vapour equilibrium of water is no longer tied to its pure vapour-pressure curve (Section 06).

### Link to other topics

The phase rule fixes the number of specifications in every flash, bubble-point and dew-point calculation in process simulators. Sections 22–24 apply the same counting to cases where one equilibrium condition does not hold: a membrane that blocks one component, or a curved interface with unequal pressures.

### Summary

Counting intensive variables, $`P(C + 1)`$, minus equilibrium constraints, $`(P - 1)(C + 2)`$, gives $`F = C - P + 2`$: areas, lines and points on phase diagrams. The rule is only as good as its assumptions: equal pressures, and every component able to reach every phase.

## Section 22: Osmotic equilibrium

*Notation:* component 1 is the solvent (passes the membrane); component 2 is the solute (blocked). Phase I is pure solvent at pressure $`P^{\mathrm{I}}`$; phase II is the solution at $`P^{\mathrm{II}}`$. The osmotic pressure is $`\Delta P = P^{\mathrm{II}} - P^{\mathrm{I}}`$.

### Intuition

Dissolving solute lowers the solvent's chemical potential (the $`RT\ln x_1`$ term). Solvent therefore flows from the pure side into the solution, down its chemical-potential gradient. Raising the pressure on the solution side pushes the solvent's chemical potential back up, by $`\underline{V}_1\,\Delta P`$. Flow stops when the two effects cancel.

In the classic set-up, the extra pressure is provided by a column of liquid that rises in a tube above the solution (the osmometer in the figure). In plants, the same pressure keeps cells turgid.

*Analogy:* the solute side "pulls" solvent like a sponge, and the pressure is the force needed to wring it back out. The analogy breaks down because nothing pulls mechanically. The solvent moves because random molecular motion carries more solvent across from the side where its chemical potential is higher. The membrane matters only because it stops the solute from equalising too.

### Derivation

**Step 1: why the phase-rule count changes.** If both sides can contain independently specified amounts of the two components, there are six phase variables: two temperatures, two pressures and two compositions. Thermal equilibrium and equality of solvent chemical potential impose two constraints, giving $`F=4`$. In the setup here, phase I is stipulated to be pure solvent, so its composition is already fixed and $`F=3`$: specify $`T`$, $`P^{\mathrm{I}}`$ and the solution composition. The osmotic pressure then follows. The membrane supports unequal pressures and blocks transfer of solute.

**Step 2: the remaining condition.** Only the solvent equilibrates:


**Equation (113)**

```math
\mu_1^{\mathrm{I}} = \mu_1^{\mathrm{II}}
```


**Step 3: each side.** The pure side is pure 1 at $`P^{\mathrm{I}}`$; the solution side is pure 1 at $`P^{\mathrm{II}}`$ plus the mixing terms:


```math
\mu_1^{\mathrm{I}} = \underline{G}_1(T,P^{\mathrm{I}}), \qquad \mu_1^{\mathrm{II}} = \underline{G}_1(T,P^{\mathrm{II}}) + RT\ln(\gamma_1x_1)
```


**Step 4: relate the two pure-solvent terms.** Integrate $`d\underline{G}_1 = \underline{V}_1\,dP`$ with the liquid incompressible:


```math
\underline{G}_1(T,P^{\mathrm{II}}) = \underline{G}_1(T,P^{\mathrm{I}}) + \underline{V}_1(P^{\mathrm{II}} - P^{\mathrm{I}})
```


**Step 5: combine with (113).**

The pure-solvent reference is written at each side's actual pressure so that the pressure difference appears explicitly before the common reference is cancelled. The two remaining terms oppose one another: mixing lowers the solvent's chemical potential in the solution, and additional pressure raises it. Dividing their balance by the solvent molar volume converts an energy deficit per mole into the pressure required to cancel it.

At this pressure difference the net solvent flux is zero. Raising solution-side pressure further reverses the chemical-potential difference and drives solvent towards the pure side. During real reverse osmosis, removal of solvent concentrates the retained solute, so the opposing osmotic pressure rises. The quoted seawater threshold is therefore an initial equilibrium requirement rather than a single pressure that guarantees the same driving force throughout concentration.


**Equation (114)**

```math
\boxed{-RT\ln(\gamma_1x_1) = \underline{V}_1\,\Delta P}
```


Since $`\gamma_1x_1 < 1`$ for a normal solution, $`\Delta P > 0`$: the solution side is at the higher pressure.

**Step 6: dilute ideal limit.** With $`\gamma_1\to 1`$ and $`-\ln x_1 = -\ln(1 - x_2)\approx x_2`$:


**Equation (115)**

```math
\Delta P \approx \frac{RT\,x_2}{\underline{V}_1} \approx c_2RT
```


since $`x_2/\underline{V}_1`$ is approximately the solute concentration $`c_2`$ (mol m⁻³). This is van 't Hoff's law. It is *formally* the ideal-gas law: the dilute solute behaves like a gas of particles in the solvent's volume.

**Step 7: link to freezing point.** Section 15 gives $`\ln(\gamma_1x_1)\approx -\Delta\underline{H}^{\mathrm{fus}}\Delta T_f/(RT_f^2)`$. Substituting into (114):


**Equation (116)**

```math
\Delta P \approx \frac{\Delta\underline{H}^{\mathrm{fus}}\,\Delta T_f}{T_f^2}\cdot\frac{T}{\underline{V}_1}
```


In the dilute colligative limit, or when the temperature dependence of solvent activity is negligible, a freezing-point measurement therefore estimates osmotic pressure at temperature $`T`$. More generally, the solvent activity must be evaluated at the osmotic experiment’s temperature and pressure.

### Motivation and explanation

**Connecting solvent activity to reverse osmosis.** An idealised seawater particle count of 0.6 mol NaCl per kilogram of water, fully dissociated, gives 1.2 mol of solute particles and an ideal osmotic pressure near 29 bar at 298.15 K. A more informative route is measured freezing-point depression: it determines the solvent activity without assuming an ideal particle count. Using a depression of approximately 2 K in the constant-fusion-enthalpy relation gives an osmotic pressure near 27 bar at 298.15 K.
This is the pressure difference needed to balance the chemical-potential effect of dissolved solute. Reverse osmosis needs a larger applied difference to drive a finite solvent flux, and the required pressure rises as the retained brine concentrates. The difference between the ideal particle estimate and an activity-based estimate represents solution non-ideality; it need not mean incomplete dissociation.
![Osmometer with solution and pure solvent separated by a solvent-permeable membrane; the hydrostatic head balances the osmotic pressure](../figs/ET-22-osmotic-cell.png)

**Colligative.** Equation (115) depends only on the number of solute particles. An ionising solute (NaCl gives Na⁺ + Cl⁻) roughly doubles it. The solute's identity enters only through $`\gamma_1`$. So measuring $`\Delta P`$ against $`x_1`$ gives $`\gamma_1(x_1)`$ directly, which is very useful for polymers and proteins, whose vapour-pressure effects are tiny. It is also how polymer molar masses are measured.

**Size of the effect.** $`RT/\underline{V}_1`$ for water at 25 °C is about 1370 bar, so even $`x_2 = 0.01`$ gives about 14 bar. Osmotic pressures are large compared with other colligative effects, which is why they matter for cells, membranes and desalination.

**Assumptions.** A perfect membrane (no solute leakage); an incompressible liquid; equal temperature on both sides. Real membranes leak slightly. The effective pressure difference is then reduced by a "reflection coefficient", a transport rather than an equilibrium concept.

### Link to other topics

Reverse osmosis and other membrane separations are designed around (114), with the osmotic pressure of the concentrated retentate setting the minimum work of separation. In biotechnology, osmotic balance governs cell lysis by osmotic shock and the design of buffers.

### Summary

When a membrane blocks the solute, only the solvent's chemical potential equalises. That frees the pressure and gives $`-RT\ln(\gamma_1x_1) = \underline{V}_1\Delta P`$, which reduces to van 't Hoff's $`\Delta P = c_2RT`$ for dilute solutions. For sea water it is about 27 bar, consistent with its freezing point.

## Section 23: Droplets and the Kelvin equation

*Notation:* $`\sigma`$ is the surface tension (N m⁻¹), $`r`$ the droplet radius, $`P^{L}`$ the pressure inside the droplet, $`P^{V}`$ the surrounding vapour pressure, and $`P^{\mathrm{SAT}}(T)`$ the vapour pressure over a flat surface. Pure substance throughout.

### Intuition

Surface tension acts like a stretched skin around the droplet, pressing inwards. The smaller the droplet, the more sharply curved the skin and the harder it presses. Liquid inside is therefore compressed, and compressed liquid has a higher escaping tendency (Section 06). So a small droplet evaporates into vapour that would be exactly saturated over a flat surface.

Equilibrium with a droplet of radius $`r`$ needs a *supersaturated* vapour, and the equilibrium is unstable:
- a droplet slightly smaller than that $`r`$ has an even higher vapour pressure, so it evaporates further;
- a droplet slightly larger grows.

### Derivation

**Step 1: the phase-rule count.** One component, two phases: naively $`F = 1`$, one boiling point per pressure. But $`P^{L}\neq P^{V}`$ across a curved interface, which removes one constraint. So $`F = 2`$: for example the pressure *and* the droplet radius.

**Step 2: mechanical equilibrium (Young–Laplace).** Cut the droplet through its centre. The pressure excess acting on the cross-section, $`(P^{L} - P^{V})\pi r^2`$, is balanced by surface tension acting round the rim, $`2\pi r\sigma`$:


**Equation (117)**

```math
P^{L} - P^{V} = \frac{2\sigma}{r}
```


**Step 3: chemical potentials.** Reference both phases to the flat-interface saturation state, where $`\underline{G}^{L} = \underline{G}^{V} = \underline{G}^{\mathrm{SAT}}(T)`$ at $`P^{\mathrm{SAT}}`$.
- Incompressible liquid: $`\mu^{L} = \underline{G}^{\mathrm{SAT}} + \underline{V}^{L}(P^{L} - P^{\mathrm{SAT}})`$.
- Ideal-gas vapour: $`\mu^{V} = \underline{G}^{\mathrm{SAT}} + RT\ln(P^{V}/P^{\mathrm{SAT}})`$.

**Step 4: equate.** $`\mu^{L} = \mu^{V}`$ gives the same equation as the Poynting correction,


```math
\underline{V}^{L}(P^{L} - P^{\mathrm{SAT}}) = RT\ln\frac{P^{V}}{P^{\mathrm{SAT}}}
```


but now $`P^{L}`$ is set by (117): $`P^{L} = P^{V} + 2\sigma/r`$.

**Step 5: the Kelvin equation.** Substitute:


**Equation (118)**

```math
\underline{V}^{L}\left(\frac{2\sigma}{r} + P^{V} - P^{\mathrm{SAT}}\right) = RT\ln\frac{P^{V}}{P^{\mathrm{SAT}}}
```


For droplets larger than a few nanometres, $`P^{V} - P^{\mathrm{SAT}}`$ is negligible compared with $`2\sigma/r`$, so


**Equation (119)**

```math
\ln\frac{P^{V}}{P^{\mathrm{SAT}}} \approx \frac{2\sigma\underline{V}^{L}}{rRT}
```


**Graphical form.** On the isotherm, the flat-interface case is Maxwell's equal-area construction at $`P^{\mathrm{SAT}}`$. For a droplet, the liquid branch is pushed up to $`P^{L}`$. The extra liquid-side area must be balanced by raising the vapour line slightly, to $`P^{V} > P^{\mathrm{SAT}}`$.

![Isotherm: flat interface (purple, Maxwell equal areas at P^SAT) versus droplet (green): compressing the liquid to P^L raises the equilibrium vapour pressure to P^V](../figs/ET-23-droplet-isotherm.png)

### Motivation and explanation

**The size scale of curvature.** For water at 293.15 K with $`\sigma=0.0727\ \mathrm{N\,m^{-1}}`$ and $`\underline V^L=1.805\times10^{-5}\ \mathrm{m^3\,mol^{-1}}`$, the Kelvin length $`2\sigma\underline V^L/(RT)`$ is about 1.077 nm. A 100 nm radius therefore needs a vapour-pressure ratio of about 1.011; a 10 nm radius needs about 1.114. At a supersaturation ratio of 1.01 the critical radius is approximately 108 nm. Small supersaturation cannot support arbitrarily tiny droplets: smaller clusters have the greater escaping tendency and evaporate. Aerosols provide a route to droplet growth, although real nuclei also involve wetting and solute effects. Extrapolation to molecular radii would require checking the continuum interface and bulk surface-tension assumptions.

**Same physics as Poynting.** In Section 06 the extra pressure on the liquid came from an inert gas. Here it comes from curvature. Either way, compressing the liquid by $`\Delta P`$ multiplies its fugacity by $`\exp(\underline{V}^{L}\Delta P/RT)`$.

The large pressure in the droplet is not the vapour pressure surrounding it. It acts on a dense liquid, whose chemical potential responds through its small molar volume. The gas matches that energy change through a logarithmic change of its much smaller pressure. This explains how the table can contain a large Laplace pressure alongside only a modest relative vapour-pressure enhancement.

The critical-radius argument holds the surrounding temperature and supersaturation fixed, as if the droplet exchanges molecules with a large vapour reservoir. A slightly smaller droplet then needs a higher vapour pressure than that reservoir provides and shrinks further. In a closed vessel with appreciable condensation, the vapour inventory and supersaturation also change, so that feedback must be included before inferring the fate of the whole droplet population.

**Unstable equilibrium and nucleation.** In vapour at a given supersaturation $`S = P^{V}/P^{\mathrm{SAT}}`$, (119) defines a critical radius $`r^{*} = 2\sigma\underline{V}^{L}/(RT\ln S)`$. Smaller droplets evaporate; larger ones grow. Forming a droplet from scratch means passing through tiny, highly unstable sizes. So pure vapour can stay supersaturated (metastable) for a long time. Real clouds form on dust, salt or ions, which provide surfaces large enough to skip that stage. The same effect makes small crystals more soluble than large ones, which drives Ostwald ripening in crystallisers.

**Limits.**
- At radii of a few nanometres, a droplet contains only hundreds of molecules, and a bulk surface tension is no longer meaningful.
- The ideal-gas vapour assumption fails near the critical point.
- Solutes on the droplet (e.g. dissolved salt in cloud droplets) lower its vapour pressure (Raoult) and compete with the Kelvin effect.

### Link to other topics

The same equation controls capillary condensation in porous adsorbents (concave menisci *lower* the vapour pressure), cavitation, and crystal size distributions in crystallisers. Section 24 applies the same mechanical-plus-chemical equilibrium to bubbles, where the curvature is reversed.

### Summary

Surface tension raises the pressure inside a droplet by $`2\sigma/r`$. By the Poynting argument, this raises its equilibrium vapour pressure, giving the Kelvin equation $`\ln(P^{V}/P^{\mathrm{SAT}}) = 2\sigma\underline{V}^{L}/(rRT)`$. The effect is negligible above a micrometre but dominant at nanometres. This makes droplet nucleation hard and supersaturated vapours metastable.

## Section 24: Bubbles, superheating and boiling

### Intuition

Boiling means forming vapour *inside* the liquid. A newborn bubble is tiny, so surface tension squeezes it hard. It needs internal vapour pressure equal to the atmosphere plus $`2\sigma/r`$, and at the normal boiling point the liquid only supplies 1 atm. So a small bubble collapses unless the liquid is hotter.

In a clean, smooth pot, the liquid can sit above 100 °C with nothing happening until a bubble finally nucleates, then it boils violently ("bumping"). Scratches, dissolved gas, boiling chips or a handful of salt provide ready-made nuclei, and boiling starts close to the true boiling point.

*Physically:* the boiling point is where the vapour pressure equals the external pressure. That is a thermodynamic condition. Whether bubbles actually appear is a kinetic question about nucleation.

### Derivation

**Step 1: degrees of freedom.** As for droplets, the curved interface frees the pressure: $`F = 2`$, e.g. external pressure and bubble radius.

**Step 2: mechanical equilibrium.** The liquid is at atmospheric pressure (shallow pool), and the vapour inside is higher by the Laplace pressure:


**Equation (120)**

```math
P^{V} = P^{L} + \frac{2\sigma}{r} = P^{\mathrm{ATM}} + \frac{2\sigma}{r}
```


**Step 3: chemical equilibrium.** Ideal-gas vapour: $`\mu^{V} = \underline{G}^{\mathrm{SAT}}(T) + RT\ln(P^{V}/P^{\mathrm{SAT}})`$. The liquid is only at about 1 atm, so its Poynting term is negligible: $`\mu^{L}\approx\underline{G}^{\mathrm{SAT}}(T)`$. (This is the difference from droplets, where the liquid was the compressed phase.) Equating gives $`P^{V} = P^{\mathrm{SAT}}(T)`$, so


**Equation (121)**

```math
P^{\mathrm{SAT}}(T) = P^{\mathrm{ATM}} + \frac{2\sigma}{r}
```


The liquid must be hot enough that its *flat-surface* vapour pressure equals the pressure inside the bubble.

For a droplet, the compressed phase is liquid and the surrounding vapour changes only slightly. For a bubble, the compressed phase is vapour itself: the gas must supply the entire Laplace pressure. Raising temperature increases its saturation pressure until this mechanical requirement and chemical equilibrium can both hold. As the bubble grows, the required pressure excess falls, making further growth easier.

The salt calculation addresses a separate cause of a higher boiling temperature. Solute changes the bulk liquid's chemical potential even for a flat interface; small-radius superheat arises because forming the curved interface requires extra pressure. A nucleation site can reduce the latter while leaving the solvent-activity effect intact, which explains why the appearance of bubbles on adding salt is not a measure of the equilibrium boiling-point elevation.

**Step 4: the required temperature.** At the normal boiling point $`T_b`$, $`P^{\mathrm{SAT}}(T_b) = P^{\mathrm{ATM}}`$. Integrating Clausius–Clapeyron with constant $`\Delta\underline{H}^{\mathrm{vap}}`$:


**Equation (122)**

```math
\ln\frac{P^{\mathrm{SAT}}(T)}{P^{\mathrm{ATM}}} = \frac{\Delta\underline{H}^{\mathrm{vap}}}{R}\left(\frac{1}{T_b} - \frac{1}{T}\right)
```


Combining (121) and (122) gives the temperature at which a bubble of radius $`r`$ is just in equilibrium. Smaller bubbles need more superheat.

**Step 5: boiling-point elevation by an involatile solute.** Now take a flat surface and a liquid containing an involatile solute (salt or sugar), with the vapour pure solvent. Equilibrium for the solvent at pressure $`P`$:


```math
\underline{G}_1^{L}(T,P) + RT\ln(\gamma_1x_1) = \underline{G}_1^{V}(T,P)
```


so $`RT\ln(\gamma_1x_1) = \Delta\underline{G}^{\mathrm{vap}}(T)`$. As in Section 15, $`\Delta\underline{G}^{\mathrm{vap}}(T)\approx\Delta\underline{H}^{\mathrm{vap}}(T_b - T)/T_b`$, giving


**Equation (123)**

```math
\ln(\gamma_1x_1) = \frac{\Delta\underline{H}^{\mathrm{vap}}}{R}\left(\frac{1}{T} - \frac{1}{T_b}\right) \;\;\Rightarrow\;\; \Delta T_b \approx \frac{RT_b^2M_1}{\Delta\underline{H}^{\mathrm{vap}}}\,m = K_b\,m
```


in the dilute ideal limit ($`-\ln x_1\approx x_2\approx M_1m`$, with $`m`$ the solute molality). Since $`\gamma_1x_1 < 1`$, $`T > T_b`$: the boiling point rises.

### Motivation and explanation

**Nucleation and colligative boiling shifts are different effects.** Smaller vapour nuclei require higher internal pressure through $`2\sigma/r`$, and therefore higher saturation temperature before they can grow. Holding surface tension at its normal-boiling value is only an illustrative approximation: substantial superheat also changes $`\sigma`$, so both relations must be solved consistently. Nucleation sites in heated surfaces reduce the barrier and the stored superheat needed for bubble growth.
Water's pure-component data give $`K_b\approx0.513\ \mathrm{K\,kg\,mol^{-1}}`$. Fully dissociating 10 g NaCl in one kilogram of water gives an ideal boiling-point elevation of only about 0.18 K. A burst of bubbles on adding salt to nearly boiling water therefore reflects nucleation of an already superheated liquid, rather than a large equilibrium boiling-point change.

**Graphical view.** Plot $`\mu_1`$ (molar $`\underline{G}`$) against $`T`$ at constant $`P`$. Each phase gives a line of slope $`-\underline{S}`$: steepest for vapour, shallowest for solid. Melting and boiling points are where the lines cross. A solute lowers *only the liquid line*, by $`RT\ln(\gamma_1x_1)`$, because the solid and vapour are pure. The liquid's crossing with the solid moves to lower $`T`$ (freezing-point depression), and its crossing with the vapour moves to higher $`T`$ (boiling-point elevation). The vapour line is steeper than the solid line, so the same downward shift moves the boiling point less than the freezing point: $`K_b < K_f`$.

![Molar Gibbs energy against T at constant P for solid, liquid and vapour; dissolving a solute lowers only the liquid line by RT ln(γ1x1), depressing the freezing point and raising the boiling point](../figs/ET-24-G-vs-T-solute.png)

**Pressure dependence.** $`(\partial\underline{G}/\partial P)_T = \underline{V}`$ and $`\underline{V}^{V}\gg\underline{V}^{L},\underline{V}^{S}`$. So changing the pressure mainly moves the vapour line. That is why boiling points depend strongly on pressure (altitude, pressure cookers) while melting points barely do.

**Limits.**
- Equation (121) treats the bubble as pure vapour. Dissolved gases add to the pressure inside it and reduce the superheat needed, which is one reason degassed water superheats more easily.
- At very small $`r`$ (nanometres), bulk $`\sigma`$ fails.
- Constant $`\Delta\underline{H}^{\mathrm{vap}}`$ in (122) is approximate for large superheats.

### Link to other topics

Nucleate boiling and its superheat govern heat-transfer coefficients in reboilers and evaporators. Boiling-point elevation sets the extra driving force needed in multiple-effect evaporators concentrating salt or sugar solutions. Cavitation in pumps is the same bubble equilibrium, reached by lowering the pressure rather than raising the temperature.

### Summary

A bubble needs its vapour pressure to exceed the surrounding pressure by $`2\sigma/r`$. Small nuclei therefore need substantial superheat, about 20 K for a 1 µm bubble in water, and clean liquids can be superheated until nucleation intervenes. Separately, an involatile solute lowers the liquid's chemical potential and raises the boiling point by $`K_bm`$, with $`K_b = 0.513`$ K kg mol⁻¹ for water. With equilibria at curved interfaces and membranes done, the course turns to the main event: vapour–liquid equilibrium of real binary mixtures.

## Conclusion

Each effect in this part follows from equal chemical potentials once the right mechanical condition is used: a membrane or a curved interface lets the pressures differ, and the compressed phase gains $`\underline{V}\,\Delta P`$ of chemical potential. Osmotic pressure, freezing-point depression and boiling-point elevation are all colligative measures of solvent activity. The next part turns to the central topic: vapour–liquid equilibrium of real binary mixtures.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)
