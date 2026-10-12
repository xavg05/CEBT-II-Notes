# Section 22: Osmotic equilibrium

## Overview

A semipermeable membrane lets solvent through but blocks the solute. At equilibrium the solution side sits at a higher pressure than the pure-solvent side: the **osmotic pressure**. This note derives

$$-RT\ln(\gamma_1x_1) = \underline{V}_1\,\Delta P \;\;\xrightarrow{\text{dilute}}\;\; \Delta P \approx \frac{RTx_2}{\underline{V}_1}\approx c_2RT,$$

shows how it breaks the naive phase rule, and applies it to sea water and reverse osmosis. Like freezing-point depression, osmotic pressure is colligative, and it can be used to measure the solvent's activity coefficient.

*Assumed:* $\mu_1 = \underline{G}_1 + RT\ln(\gamma_1x_1)$ (Section 10); $(\partial\underline{G}/\partial P)_T = \underline{V}$; the phase rule (Section 21); freezing-point depression (Section 15).

*Notation:* component 1 is the solvent (passes the membrane); component 2 is the solute (blocked). Phase I is pure solvent at pressure $P^{\mathrm{I}}$; phase II is the solution at $P^{\mathrm{II}}$. The osmotic pressure is $\Delta P = P^{\mathrm{II}} - P^{\mathrm{I}}$.

## Intuition

Dissolving solute lowers the solvent's chemical potential (the $RT\ln x_1$ term). Solvent therefore flows from the pure side into the solution, down its chemical-potential gradient. Raising the pressure on the solution side pushes the solvent's chemical potential back up, by $\underline{V}_1\,\Delta P$. Flow stops when the two effects cancel.

In the classic set-up, the extra pressure is provided by a column of liquid that rises in a tube above the solution (the osmometer in the figure). In plants, the same pressure keeps cells turgid.

*Analogy:* the solute side "pulls" solvent like a sponge, and the pressure is the force needed to wring it back out. The analogy breaks down because nothing pulls mechanically. The solvent moves because random molecular motion carries more solvent across from the side where its chemical potential is higher. The membrane matters only because it stops the solute from equalising too.

## Derivation

**Step 1: why the phase rule changes.** Two phases, two components: the naive count gives $F = 2 - 2 + 2 = 2$. But the solute cannot cross, so $\mu_2^{\mathrm{I}} = \mu_2^{\mathrm{II}}$ is *not* required (one fewer constraint). The membrane is rigid, so $P^{\mathrm{I}} = P^{\mathrm{II}}$ is not required either (another one fewer). So $F = 4$: for example $T$, $P^{\mathrm{I}}$, and the compositions on each side. The osmotic pressure then follows.

**Step 2: the remaining condition.** Only the solvent equilibrates:

$$\mu_1^{\mathrm{I}} = \mu_1^{\mathrm{II}} \tag{1}$$

**Step 3: each side.** The pure side is pure 1 at $P^{\mathrm{I}}$; the solution side is pure 1 at $P^{\mathrm{II}}$ plus the mixing terms:

$$\mu_1^{\mathrm{I}} = \underline{G}_1(T,P^{\mathrm{I}}), \qquad \mu_1^{\mathrm{II}} = \underline{G}_1(T,P^{\mathrm{II}}) + RT\ln(\gamma_1x_1)$$

**Step 4: relate the two pure-solvent terms.** Integrate $d\underline{G}_1 = \underline{V}_1\,dP$ with the liquid incompressible:

$$\underline{G}_1(T,P^{\mathrm{II}}) = \underline{G}_1(T,P^{\mathrm{I}}) + \underline{V}_1(P^{\mathrm{II}} - P^{\mathrm{I}})$$

**Step 5: combine with (1).**

$$\boxed{-RT\ln(\gamma_1x_1) = \underline{V}_1\,\Delta P} \tag{2}$$

Since $\gamma_1x_1 < 1$ for a normal solution, $\Delta P > 0$: the solution side is at the higher pressure.

**Step 6: dilute ideal limit.** With $\gamma_1\to 1$ and $-\ln x_1 = -\ln(1 - x_2)\approx x_2$:

$$\Delta P \approx \frac{RT\,x_2}{\underline{V}_1} \approx c_2RT \tag{3}$$

since $x_2/\underline{V}_1$ is approximately the solute concentration $c_2$ (mol m⁻³). This is van 't Hoff's law. It is *formally* the ideal-gas law: the dilute solute behaves like a gas of particles in the solvent's volume.

**Step 7: link to freezing point.** Section 15 gives $\ln(\gamma_1x_1)\approx -\Delta\underline{H}^{\mathrm{fus}}\Delta T_f/(RT_f^2)$. Substituting into (2):

$$\Delta P \approx \frac{\Delta\underline{H}^{\mathrm{fus}}\,\Delta T_f}{T_f^2}\cdot\frac{T}{\underline{V}_1} \tag{4}$$

A freezing-point measurement therefore predicts the osmotic pressure, at temperature $T$, without knowing what the solute is.

## Motivation and explanation

**Colligative.** Equation (3) depends only on the number of solute particles. An ionising solute (NaCl gives Na⁺ + Cl⁻) roughly doubles it. The solute's identity enters only through $\gamma_1$. So measuring $\Delta P$ against $x_1$ gives $\gamma_1(x_1)$ directly, which is very useful for polymers and proteins, whose vapour-pressure effects are tiny. It is also how polymer molar masses are measured.

**Size of the effect.** $RT/\underline{V}_1$ for water at 25 °C is about 1370 bar, so even $x_2 = 0.01$ gives about 14 bar. Osmotic pressures are large compared with other colligative effects, which is why they matter for cells, membranes and desalination.

**Assumptions.** A perfect membrane (no solute leakage); an incompressible liquid; equal temperature on both sides. Real membranes leak slightly. The effective pressure difference is then reduced by a "reflection coefficient", a transport rather than an equilibrium concept.

## Worked example

**Problem.** Estimate the osmotic pressure of sea water at 25 °C, the minimum pressure a reverse-osmosis plant must apply to produce fresh water. Approximate sea water as about 0.6 mol NaCl per kg water, fully dissociated. Check the answer against sea water's freezing point of about −2 °C, and against the commonly quoted ≈27 bar.

**Dissolved particles.** 1.2 mol per kg of water, so $x_2 = 1.2\times0.018015/(1 + 1.2\times0.018015) = 0.0212$. Water's molar volume at 25 °C is $\underline{V}_1 = 1.807\times10^{-5}$ m³ mol⁻¹.

**Ideal estimate.**
- From (2) with $\gamma_1 = 1$: $\Delta P = -RT\ln(1 - x_2)/\underline{V}_1 = 29.3$ bar.
- From (3): 29.0 bar.

**Freezing-point route.** From (4) with $\Delta T_f\approx 2$ K: $\ln a_1 = -0.0194$, $a_1 = 0.981$, and $\Delta P \approx 26.6$ bar at 25 °C. Equivalently, each kelvin of freezing-point depression corresponds to about 13.3 bar of osmotic pressure at 25 °C.

**Interpretation.** The freezing-point route (≈27 bar) agrees with the quoted value. The ideal particle count overestimates slightly (29 bar), because concentrated NaCl solution is non-ideal: the effective number of particles is less than 2 per formula unit. A reverse-osmosis plant must exceed about 27 bar just to stop osmosis, and higher still to drive a useful flux. As brine concentrates along the membrane, its osmotic pressure rises too, which is why seawater RO plants operate at several tens of bar. 27 bar is the pressure at the foot of a water column about 276 m high.

![Osmometer: solution (phase II, components 1 + 2) and pure solvent (phase I) separated by a membrane permeable only to 1; at equilibrium the solution rises by h, so ΔP = ρgh](figs/ET-22-osmotic-cell.png)

## Link to other topics

Reverse osmosis and other membrane separations are designed around (2), with the osmotic pressure of the concentrated retentate setting the minimum work of separation. In biotechnology, osmotic balance governs cell lysis by osmotic shock and the design of buffers.

## Conclusion

When a membrane blocks the solute, only the solvent's chemical potential equalises. That frees the pressure and gives $-RT\ln(\gamma_1x_1) = \underline{V}_1\Delta P$, which reduces to van 't Hoff's $\Delta P = c_2RT$ for dilute solutions. For sea water it is about 27 bar, consistent with its freezing point. The next section relaxes the equal-pressure condition by a different route: a curved interface, where surface tension sets the pressure difference and droplets acquire a size-dependent vapour pressure.
