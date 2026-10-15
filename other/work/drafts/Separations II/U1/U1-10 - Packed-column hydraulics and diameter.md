# Packed-column hydraulics and diameter

## Overview

Assumed background: superficial velocity, pressure drop and countercurrent contacting. Packed height supplies transfer area; diameter supplies enough open flow area to avoid excessive pressure drop and flooding. Both dimensions must be checked together because changing diameter changes the transfer coefficients and wetting.

## Intuition

Gas pushes upwards through the same void space in which liquid drains downwards. At low gas velocity, drainage remains easy. As gas velocity increases, it holds more liquid in the bed, shrinking the available gas passages and increasing resistance. Flooding is the limit at which stable countercurrent drainage breaks down.

## Derivation

Let $G$ and $L$ be **mass** flow rates of gas and liquid in $\mathrm{kg\,s^{-1}}$, unlike the molar flows $G_m,L_m$ used in the composition balances. For gas mass density $\rho_g$ and tower area $A$, the superficial gas velocity is

$$
U_g=\frac{G}{\rho_gA}. \tag{1}
$$

“Superficial” means based on the whole tower cross-section; velocity within the open voids is larger. Increasing liquid loading $L/A$ reduces gas space and raises pressure drop at a given $U_g$.

![Loading and flooding on a pressure-drop diagram](../figs/u1-pressure-drop.png)

The graph's $X$ points mark loading, where liquid holdup begins to rise strongly with gas flow; $Y$ points mark flooding. Wet drained packing has greater pressure drop than dry packing. A log–log slope near $1.8$ indicates an approximate power law $\Delta P\propto U_g^{1.8}$ in the depicted low-loading region. The steeper loaded region and nearly vertical flood region show why extending that simple power law to flooding fails.

One empirical chart convention uses a flow parameter $F_{LV}$ and an ordinate $K_4$:

$$
F_{LV}=\frac LG\sqrt{\frac{\rho_g}{\rho_l}},
\qquad
K_4=\frac{13.1(G/A)^2F_p(\mu_l/\rho_l)^{0.1}}
{\rho_g(\rho_l-\rho_g)}. \tag{2}
$$

Here $\rho_l$ is liquid mass density in $\mathrm{kg\,m^{-3}}$, $\mu_l$ liquid dynamic viscosity in $\mathrm{Pa\,s}$ and $F_p$ the packing factor in $\mathrm{m^{-1}}$. The numerical coefficient belongs to this chart's empirical unit convention; it is not a universally dimensionless constant. Use the specified units and the matching chart, and never substitute a packing surface area for $F_p$.

![Empirical packed-column pressure-drop and flooding chart](../figs/u1-hydraulic-chart.png)

The curve labels specify pressure drop in mm of water per metre of packed height. To use the construction:

1. Calculate actual mass flows and fluid properties, then $F_{LV}$. This fixes the horizontal location because the chart groups columns by relative liquid/gas loading.
2. Read the flooding ordinate $K_{4,f}$ at that location. This establishes the limiting gas capacity for the chosen packing.
3. Choose an operating velocity fraction $f=U_g/U_{g,f}$ below flooding and check the corresponding pressure-drop curve. The allowable fraction depends on packing and service; a conservative preliminary value might be $0.5$–$0.6$.
4. Convert the velocity fraction to an ordinate fraction. At fixed properties and packing, equation (2) is quadratic in $G/A$, hence in $U_g$:

$$
\frac{K_4}{K_{4,f}}=f^2. \tag{3}
$$

5. Rearrange the chart ordinate to obtain the permissible gas mass flux $J_g=G/A$:

$$
J_g=\left[\frac{K_4\rho_g(\rho_l-\rho_g)}
{13.1F_p(\mu_l/\rho_l)^{0.1}}\right]^{1/2},
\qquad A=\frac G{J_g},\qquad D_c=\sqrt{\frac{4A}{\pi}}. \tag{4}
$$

Here $D_c$ is tower diameter. The square root follows from the quadratic ordinate; the diameter follows from circular cross-sectional area.

Check a tower-to-random-packing size ratio of at least roughly ten as an initial wall-effect criterion. Then calculate transfer coefficients and effective wetted area at the resulting flow per area, and recalculate height. Repeat if the selected geometry changes those correlations materially.

At fixed total gas flow, reducing cross-section increases superficial velocity and hence the gas's opposition to liquid drainage. Greater liquid holdup then narrows the remaining gas passages, which raises resistance further. This feedback explains the sharp upward turn near flooding: a low-loading pressure-drop power law cannot represent a geometry that is progressively filling with liquid.

The velocity fraction must be squared because the chart ordinate depends on gas mass flux squared. This is an algebraic consequence of the chosen ordinate, not a different flooding margin. After selecting diameter, the new gas and liquid flows per unit area must also be used in the mass-transfer calculation; diameter and height are coupled through hydrodynamics.

## Motivation and explanation

Flooding margin and pressure drop are different checks. A column can be below flooding yet exceed the allowable pressure budget. Too large an area can also cause inadequate liquid distribution or wetting. Empirical chart readings are estimates; alternative correlations can differ substantially, so precise final dimensions require suitable packing-specific data.

At incipient flooding, pressure support is comparable to the weight of retained liquid over the bed. A hydrostatic scale $\rho_l gZ$ helps interpret the growth in pressure drop, but treating it as an exact flooding criterion ignores void fraction, holdup, entrainment and detailed geometry. Correlations capture those effects empirically.

## Worked example

Suppose a preliminary hydraulic estimate gives gas volume flow $1.00\ \mathrm{m^3\,s^{-1}}$ and flooding velocity $2.00\ \mathrm{m\,s^{-1}}$. Choose explicitly $f=0.55$. Then $U_g=1.10\ \mathrm{m\,s^{-1}}$, $A=0.909091\ \mathrm{m^2}$ and $D_c=1.07587\ \mathrm m$. The corresponding chart ordinate fraction is $f^2=0.3025$, not $0.55$. Pressure drop, wetting and distributor design still need separate checks before accepting this illustrative diameter.

## Link to other topics

Hydraulics supplies the cross-section needed to convert required packed volume into height. The selected area also changes HTU through superficial flows, making rate and hydraulic design an iterative calculation.

## Conclusion

Use flow loading and a matching empirical chart to select a feasible diameter, with explicit flooding and pressure-drop margins. Convert velocity fractions consistently and then revisit mass-transfer performance at the selected area.
