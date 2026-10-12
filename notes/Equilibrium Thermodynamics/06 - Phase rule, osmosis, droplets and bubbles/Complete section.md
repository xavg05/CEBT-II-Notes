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

**What $`F`$ means physically.**
- $`F = 2`$: an area on a phase diagram. A single-phase pure fluid can have any $`T`$ and $`P`$.
- $`F = 1`$: a line. Liquid and vapour of a pure substance coexist only along the vapour-pressure curve; choose $`T`$ and $`P`$ is fixed.
- $`F = 0`$: a point. The triple point is fixed by nature, which is why it is used to define temperature scales.

**For mixtures.** A binary in vapour–liquid equilibrium has $`F = 2 - 2 + 2 = 2`$. Fix $`T`$ and the liquid composition, and the pressure and vapour composition follow. That is exactly what was done for oxygen–argon (Section 13): $`T = 83.8`$ K and $`x_1 = 0.3`$ gave $`P`$ and $`y_1`$.

**A common slip.** Air dissolved in or above water adds components, so "water boiling at 100 °C under 1 atm of air" is not a one-component system. With an insoluble inert gas present, the liquid–vapour equilibrium of water is no longer tied to its pure vapour-pressure curve (Section 06).

### Worked example

**Problem.** Find $`F`$ and say what must be specified for:
(a) pure liquid water + steam, no air;
(b) water + steam + ice;
(c) a binary liquid in equilibrium with its vapour;
(d) a binary with two liquid phases and a vapour;
(e) a ternary liquid–vapour mixture.

| System | $`C`$ | $`P`$ | $`F = C - P + 2`$ | Specify |
|---|---|---|---|---|
| (a) water + steam | 1 | 2 | 1 | $`T`$ (or $`P`$): e.g. 100 °C fixes 1.013 bar |
| (b) water + steam + ice | 1 | 3 | 0 | nothing: 273.16 K, 611.65 Pa |
| (c) binary L + V | 2 | 2 | 2 | e.g. $`T`$ and $`x_1`$ |
| (d) binary L + L + V | 2 | 3 | 1 | e.g. $`P`$; then $`T`$ and all three compositions are fixed |
| (e) ternary L + V | 3 | 2 | 3 | e.g. $`T`$, $`x_1`$, $`x_2`$ |

![Schematic phase diagram of pure water: single-phase areas (F = 2), coexistence lines (F = 1) meeting at the triple point (F = 0), and the vapour-pressure line ending at the critical point](../figs/ET-21-water-phase-diagram.png)

**Interpretation.**
- Case (b) explains why the triple point of water (273.16 K, 611.65 Pa) is a reproducible reference.
- Case (d) explains why a heterogeneous (two-liquid) azeotrope boils at a single temperature at fixed pressure, whatever the overall feed composition. The feed composition only changes the amounts of the phases. This is the basis of steam distillation later in the course.
- The critical point is not a third phase. It is where the liquid and vapour become identical, adding the extra conditions that end the coexistence line.

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

**Colligative.** Equation (115) depends only on the number of solute particles. An ionising solute (NaCl gives Na⁺ + Cl⁻) roughly doubles it. The solute's identity enters only through $`\gamma_1`$. So measuring $`\Delta P`$ against $`x_1`$ gives $`\gamma_1(x_1)`$ directly, which is very useful for polymers and proteins, whose vapour-pressure effects are tiny. It is also how polymer molar masses are measured.

**Size of the effect.** $`RT/\underline{V}_1`$ for water at 25 °C is about 1370 bar, so even $`x_2 = 0.01`$ gives about 14 bar. Osmotic pressures are large compared with other colligative effects, which is why they matter for cells, membranes and desalination.

**Assumptions.** A perfect membrane (no solute leakage); an incompressible liquid; equal temperature on both sides. Real membranes leak slightly. The effective pressure difference is then reduced by a "reflection coefficient", a transport rather than an equilibrium concept.

### Worked example

**Problem.** Estimate the osmotic pressure of sea water at 25 °C, the minimum pressure a reverse-osmosis plant must apply to produce fresh water. Approximate sea water as about 0.6 mol NaCl per kg water, fully dissociated. Check the answer against sea water's freezing point of about −2 °C, and against the commonly quoted ≈27 bar.

**Dissolved particles.** 1.2 mol per kg of water, so $`x_2 = 1.2\times0.018015/(1 + 1.2\times0.018015) = 0.0212`$. Water's molar volume at 25 °C is $`\underline{V}_1 = 1.807\times10^{-5}`$ m³ mol⁻¹.

**Ideal estimate.**
- From (114) with $`\gamma_1 = 1`$: $`\Delta P = -RT\ln(1 - x_2)/\underline{V}_1 = 29.3`$ bar.
- From (115): 29.0 bar.

**Freezing-point route.** From (116) with $`\Delta T_f\approx 2`$ K: $`\ln a_1 = -0.0194`$, $`a_1 = 0.981`$, and $`\Delta P \approx 26.6`$ bar at 25 °C. Equivalently, each kelvin of freezing-point depression corresponds to about 13.3 bar of osmotic pressure at 25 °C.

**Interpretation.** The freezing-point route (≈27 bar) agrees with the quoted value. The ideal particle count overestimates slightly (29 bar), because concentrated NaCl solution is non-ideal: the effective number of particles is less than 2 per formula unit. A reverse-osmosis plant must exceed about 27 bar just to stop osmosis, and higher still to drive a useful flux. As brine concentrates along the membrane, its osmotic pressure rises too, which is why seawater RO plants operate at several tens of bar. 27 bar is the pressure at the foot of a water column about 276 m high.

![Osmometer: solution (phase II, components 1 + 2) and pure solvent (phase I) separated by a membrane permeable only to 1; at equilibrium the solution rises by h, so ΔP = ρgh](../figs/ET-22-osmotic-cell.png)

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

**Same physics as Poynting.** In Section 06 the extra pressure on the liquid came from an inert gas. Here it comes from curvature. Either way, compressing the liquid by $`\Delta P`$ multiplies its fugacity by $`\exp(\underline{V}^{L}\Delta P/RT)`$.

**Unstable equilibrium and nucleation.** In vapour at a given supersaturation $`S = P^{V}/P^{\mathrm{SAT}}`$, (119) defines a critical radius $`r^{*} = 2\sigma\underline{V}^{L}/(RT\ln S)`$. Smaller droplets evaporate; larger ones grow. Forming a droplet from scratch means passing through tiny, highly unstable sizes. So pure vapour can stay supersaturated (metastable) for a long time. Real clouds form on dust, salt or ions, which provide surfaces large enough to skip that stage. The same effect makes small crystals more soluble than large ones, which drives Ostwald ripening in crystallisers.

**Limits.**
- At radii of a few nanometres, a droplet contains only hundreds of molecules, and a bulk surface tension is no longer meaningful.
- The ideal-gas vapour assumption fails near the critical point.
- Solutes on the droplet (e.g. dissolved salt in cloud droplets) lower its vapour pressure (Raoult) and compete with the Kelvin effect.

### Worked example

**Problem.** For pure water droplets at 20 °C, find the vapour pressure enhancement $`P^{V}/P^{\mathrm{SAT}}`$ for radii 1 µm, 100 nm, 10 nm and 1 nm, and the critical radius at supersaturations of 0.1 %, 1 % and 10 %. Data: $`\sigma = 72.7`$ mN m⁻¹, $`\underline{V}^{L} = 1.805\times10^{-5}`$ m³ mol⁻¹, $`P^{\mathrm{SAT}} = 2339`$ Pa.

**Enhancement from (119)**, with $`2\sigma\underline{V}^{L}/RT = 1.077`$ nm:

| $`r`$ | $`2\sigma/r`$ (bar) | $`P^{V}/P^{\mathrm{SAT}}`$ (119) | Full (118) |
|---|---|---|---|
| 1 µm | 1.45 | 1.0011 | 1.0011 |
| 100 nm | 14.5 | 1.011 | 1.011 |
| 10 nm | 145 | 1.114 | 1.114 |
| 1 nm | 1455 | 2.94 | 2.94 |

The neglected term in (118) changes nothing to four figures, because $`P^{V} - P^{\mathrm{SAT}}`$ is at most kilopascals, while $`2\sigma/r`$ is bars to kilobars.

**Critical radii.**

| Supersaturation $`S`$ | 1.001 | 1.01 | 1.1 |
|---|---|---|---|
| $`r^{*}`$ | 1.08 µm | 108 nm | 11 nm |

**Interpretation.** Air in a real cloud is typically only slightly supersaturated (well under a few percent). There, a droplet must already be about 0.1 µm across to grow. Random clustering of water molecules cannot reach that size, so clouds form on aerosol particles of about that size or larger. Without them, vapour would need several-fold supersaturation (the 1 nm row) to condense spontaneously.

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

**Graphical view.** Plot $`\mu_1`$ (molar $`\underline{G}`$) against $`T`$ at constant $`P`$. Each phase gives a line of slope $`-\underline{S}`$: steepest for vapour, shallowest for solid. Melting and boiling points are where the lines cross. A solute lowers *only the liquid line*, by $`RT\ln(\gamma_1x_1)`$, because the solid and vapour are pure. The liquid's crossing with the solid moves to lower $`T`$ (freezing-point depression), and its crossing with the vapour moves to higher $`T`$ (boiling-point elevation). The vapour line is steeper than the solid line, so the same downward shift moves the boiling point less than the freezing point: $`K_b < K_f`$.

![Molar Gibbs energy against T at constant P for solid, liquid and vapour; dissolving a solute lowers only the liquid line by RT ln(γ1x1), depressing the freezing point and raising the boiling point](../figs/ET-24-G-vs-T-solute.png)

**Pressure dependence.** $`(\partial\underline{G}/\partial P)_T = \underline{V}`$ and $`\underline{V}^{V}\gg\underline{V}^{L},\underline{V}^{S}`$. So changing the pressure mainly moves the vapour line. That is why boiling points depend strongly on pressure (altitude, pressure cookers) while melting points barely do.

**Limits.**
- Equation (121) treats the bubble as pure vapour. Dissolved gases add to the pressure inside it and reduce the superheat needed, which is one reason degassed water superheats more easily.
- At very small $`r`$ (nanometres), bulk $`\sigma`$ fails.
- Constant $`\Delta\underline{H}^{\mathrm{vap}}`$ in (122) is approximate for large superheats.

### Worked example

**Problem.** (a) For water at 1 atm, find the temperature at which a vapour bubble of radius 10 µm, 1 µm or 0.1 µm is in equilibrium. Data: $`\sigma(100\,°\mathrm{C}) = 58.9`$ mN m⁻¹, $`\Delta\underline{H}^{\mathrm{vap}} = 40.65`$ kJ mol⁻¹, $`T_b = 373.12`$ K. (b) Find water's ebullioscopic constant, and the boiling-point rise from 10 g of NaCl per kg of water (pasta water).

**(a)** From (121), then (122), holding $`\sigma`$ at its 100 °C value for this illustrative estimate; IAPWS steam tables convert the same required pressures to temperatures for comparison. Actual surface tension falls as temperature rises, so a self-consistent prediction at large superheat must also update $`\sigma(T)`$:

| $`r`$ | $`P^{\mathrm{SAT}}`$ required (bar) | $`T`$ from (122) | $`T`$ from steam tables |
|---|---|---|---|
| 10 µm | 1.131 | 103.1 °C | 103.1 °C |
| 1 µm | 2.19 | 123.3 °C | 123.1 °C |
| 0.1 µm | 12.8 | 189.5 °C | 190.9 °C |

**(b)** $`K_b = RT_b^2M_1/\Delta\underline{H}^{\mathrm{vap}} = 8.314\times373.12^2\times0.018015/40650 = 0.513`$ K kg mol⁻¹ (tabulated: 0.512). 10 g of NaCl is 0.171 mol, about 0.342 mol of ions per kg, so $`\Delta T_b\approx 0.18`$ K.

**Interpretation.**
- *Superheat:* a liquid with only micrometre-scale nuclei must be superheated by about 20 K before bubbles can grow. That is why smooth glassware bumps, and why boiling surfaces in evaporators and reboilers are engineered with nucleation sites.
- *Salt:* the boiling-point rise is under 0.2 K, irrelevant for cooking. The sudden fizz when salt is thrown into nearly boiling water is not thermodynamic. The crystals provide nucleation sites that release the superheat already stored in the liquid.

### Link to other topics

Nucleate boiling and its superheat govern heat-transfer coefficients in reboilers and evaporators. Boiling-point elevation sets the extra driving force needed in multiple-effect evaporators concentrating salt or sugar solutions. Cavitation in pumps is the same bubble equilibrium, reached by lowering the pressure rather than raising the temperature.

### Summary

A bubble needs its vapour pressure to exceed the surrounding pressure by $`2\sigma/r`$. Small nuclei therefore need substantial superheat, about 20 K for a 1 µm bubble in water, and clean liquids can be superheated until nucleation intervenes. Separately, an involatile solute lowers the liquid's chemical potential and raises the boiling point by $`K_bm`$, with $`K_b = 0.513`$ K kg mol⁻¹ for water. With equilibria at curved interfaces and membranes done, the course turns to the main event: vapour–liquid equilibrium of real binary mixtures.

## Conclusion

Each effect in this part follows from equal chemical potentials once the right mechanical condition is used: a membrane or a curved interface lets the pressures differ, and the compressed phase gains $`\underline{V}\,\Delta P`$ of chemical potential. Osmotic pressure, freezing-point depression and boiling-point elevation are all colligative measures of solvent activity. The next part turns to the central topic: vapour–liquid equilibrium of real binary mixtures.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)
