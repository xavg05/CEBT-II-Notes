# Phase rule, osmosis, droplets and bubbles — reading 06.1

[Previous](05-03-activity-coefficient-models.md) · [Subject index](README.md) · [Next](06-02-phase-rule-osmosis-droplets-and-bubbles.md)

<!-- reading-content:start -->
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

![Schematic phase diagram of pure water: single-phase areas (F = 2), coexistence lines (F = 1) meeting at the triple point (F = 0), and the vapour-pressure line ending at the critical point](figs/ET-21-water-phase-diagram.png)

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

**Step 1: why the phase rule changes.** Two phases, two components: the naive count gives $`F = 2 - 2 + 2 = 2`$. But the solute cannot cross, so $`\mu_2^{\mathrm{I}} = \mu_2^{\mathrm{II}}`$ is *not* required (one fewer constraint). The membrane is rigid, so $`P^{\mathrm{I}} = P^{\mathrm{II}}`$ is not required either (another one fewer). So $`F = 4`$: for example $`T`$, $`P^{\mathrm{I}}`$, and the compositions on each side. The osmotic pressure then follows.

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


A freezing-point measurement therefore predicts the osmotic pressure, at temperature $`T`$, without knowing what the solute is.

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

![Osmometer: solution (phase II, components 1 + 2) and pure solvent (phase I) separated by a membrane permeable only to 1; at equilibrium the solution rises by h, so ΔP = ρgh](figs/ET-22-osmotic-cell.png)

### Link to other topics

Reverse osmosis and other membrane separations are designed around (114), with the osmotic pressure of the concentrated retentate setting the minimum work of separation. In biotechnology, osmotic balance governs cell lysis by osmotic shock and the design of buffers.

### Summary

When a membrane blocks the solute, only the solvent's chemical potential equalises. That frees the pressure and gives $`-RT\ln(\gamma_1x_1) = \underline{V}_1\Delta P`$, which reduces to van 't Hoff's $`\Delta P = c_2RT`$ for dilute solutions. For sea water it is about 27 bar, consistent with its freezing point.
<!-- reading-content:end -->

[Previous](05-03-activity-coefficient-models.md) · [Subject index](README.md) · [Next](06-02-phase-rule-osmosis-droplets-and-bubbles.md)
