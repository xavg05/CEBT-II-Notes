[Previous](<SEP-30 - Concentration polarisation and limiting flux.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-32 - Coupled ultrafiltration pressure and flux.md>)

<!-- note-content:start -->
# SEP-31: Osmotic pressure and reverse solvent flow

## Overview

Assumed knowledge: chemical potential, solvent activity and incompressible liquid pressure dependence.

Solute lowers solvent chemical potential. Osmosis follows from that difference, while reverse osmosis applies enough pressure to reverse the solvent's direction. This note derives the pressure correction needed in a liquid membrane flux law and identifies when a dilute osmotic-pressure formula is adequate.

## Intuition

At equal pressure, water prefers to enter a solution rather than leave it: mixing lowers its chemical potential. Pressurising the solution raises the water chemical potential and can balance that preference. Increasing pressure beyond the balance drives water from the concentrated solution towards the dilute permeate.

The membrane's adjacent wall concentration matters because solvent crosses at the wall. A bulk solution can be fairly dilute while a polarised wall layer imposes a much larger osmotic penalty.

## Derivation

At fixed temperature $`T`$, write the chemical potential of solvent $`V`$ as


```math
\mu_V=\mu_V^\circ+RT\ln a_V+\bar V_V(P-P^\circ),
```


where $`a_V`$ is solvent activity on the pure-liquid standard state, $`R`$ the gas constant and $`\bar V_V`$ approximately constant solvent partial molar volume. The last term integrates $`d\mu_V=\bar V_V\,dP`$ for an incompressible liquid.

Let pure solvent be at pressure $`P_1`$ and solution at $`P_1+\Pi`$. Osmotic equilibrium requires equal solvent chemical potentials; pure solvent has $`a_V=1`$. Thus


```math
\mu_V^\circ+\bar V_V(P_1-P^\circ)
=\mu_V^\circ+RT\ln a_V+\bar V_V(P_1+\Pi-P^\circ).
```


Cancel the common standard-state and pressure terms, giving


**Equation (132)**

```math
\Pi=-\frac{RT}{\bar V_V}\ln a_V.
```


Since ordinary dilute solutions have $`a_V<1`$, their osmotic pressure is positive. Using activity rather than concentration permits nonideal behaviour to be represented.

For a dilute ideal nonelectrolyte, $`a_V\approx x_V=1-x_B`$. Expand $`\ln(1-x_B)=-x_B+\cdots`$ and retain its first term. Because $`n_B\ll n_V`$ and total solution volume $`V\approx n_V\bar V_V`$,


```math
\Pi\approx\frac{RT}{\bar V_V}x_B
\approx\frac{RT}{\bar V_V}\frac{n_B}{n_V}
\approx RT\frac{n_B}{V}.
```


Writing $`C_B=n_B/V`$ and allowing a dissociation factor $`f_B`$, the dilute van't Hoff result is


**Equation (133)**

```math
\Pi\approx f_BRTC_B.
```


Ideal complete dissociation gives $`f_B=2`$ for NaCl and $`3`$ for calcium chloride; a nonelectrolyte has $`f_B=1`$. At significant electrolyte concentration, ion interactions require activities or an osmotic coefficient rather than assuming that ideal counting is exact.

For feed-wall and permeate solutions at pressures $`P_f`$ and $`P_p`$, apply the chemical-potential difference between the two sides. Their osmotic pressures are $`\Pi_w`$ and $`\Pi_p`$. The effective pressure driving solvent out of feed is therefore


```math
\Delta P_{\mathrm{net}}=(P_f-P_p)-(\Pi_w-\Pi_p).
```


For hydraulic permeance $`K_V`$, the linear solvent flux law becomes


**Equation (134)**

```math
J_V=K_V[\Delta P-(\Pi_w-\Pi_p)].
```


The pressure correction and activity term describe opposing contributions to the same solvent chemical potential. At osmotic equilibrium they cancel, although the solutions on the two sides still have different concentrations and pressures. Zero net water flow therefore does not require identical states on each side.

For reverse osmosis, the imposed pressure must first cancel that activity-related difference before any excess is available to drive water through hydraulic resistance. High permeance reduces the pressure needed for a specified additional flow; it cannot remove the equilibrium threshold. The relevant threshold uses both transporting interfaces, including wall enrichment and any permeate solute.

## Motivation and explanation

At $`\Delta P=\Pi_w-\Pi_p`$, net solvent flux vanishes. Above this pressure, solvent leaves the concentrated feed; below it, solvent flows towards the more concentrated side. Equation (134) assumes a membrane strongly selective for solvent and a suitable linear hydraulic coefficient; a leaky membrane may require a more general coupled transport model.

If solute is completely rejected and permeate contains pure solvent, $`\Pi_p=0`$. Otherwise both sides contribute: dropping $`\Pi_p`$ can overstate the osmotic opposition, even though it may be a small correction.

Proteins have high molecular mass and therefore low molar concentration for a given mass concentration. Their dilute ideal osmotic pressure can be relatively small, but strong concentration polarisation and nonideal interactions at the wall invalidate that simple estimate. Measured correlations can take the form


**Equation (135)**

```math
\Pi=A_1C_B+A_2C_B^2+A_3C_B^3
\quad\text{or}\quad \Pi=\varphi C_B^\beta.
```


The coefficients are dimensional and depend on the concentration units, temperature and solution. A fitted formula must be used within its stated range, with its original units.

## Worked example

Estimate the osmotic pressure of $`0.1\,\mathrm M`$ NaCl at $`20^\circ\mathrm C`$ under dilute ideal complete-dissociation assumptions. Convert to $`C_B=100\,\mathrm{mol\,m^{-3}}`$ and $`T=293.15\,\mathrm K`$, and use $`f_B=2`$ in Equation (133). The result is $`\Pi\approx4.87477\,\mathrm{bar}`$.

This is an ideal-model estimate, not a high-accuracy salt-solution property. If the membrane wall is more concentrated than the bulk, even this approximation must use the wall concentration when calculating feed-side osmotic opposition. Water can leave that wall solution only when the imposed pressure exceeds the relevant osmotic-pressure difference.

## Link to other topics

This is the same solvent chemical-potential balance used in equilibrium thermodynamics, now coupled to a finite transport rate. The coupling to the polarisation film determines whether more pressure produces useful extra flux or mostly increases wall concentration.

## Conclusion

Osmotic pressure is the pressure needed to offset the solution's reduction in solvent chemical potential. Membrane design uses the resulting net pressure at the transporting interfaces, with nonideal osmotic data where dilute ideal assumptions fail.
<!-- note-content:end -->

[Previous](<SEP-30 - Concentration polarisation and limiting flux.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-32 - Coupled ultrafiltration pressure and flux.md>)
