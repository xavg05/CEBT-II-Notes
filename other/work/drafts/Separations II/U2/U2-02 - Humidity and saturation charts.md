# Humidity and saturation charts

## Overview

Humidity is measured per unit mass of dry carrier gas. That conserved basis links a gas composition to a drying mass balance. A humidity chart then locates the actual gas state relative to saturation at the same pressure.

Assumptions: an ideal binary gas mixture, an inert non-condensable carrier and equilibrium with a pure liquid at a flat interface.

## Intuition

*Heating a closed amount of moist air does not create water.* Its humidity stays fixed while its saturation humidity rises. It therefore becomes less saturated and can accept more evaporated water.

Saturation depends on vapour pressure, not on the total mass of gas. The dry carrier supplies the convenient accounting basis.

## Derivation

Let $n_v,n_g$ be vapour and dry-carrier mole amounts and $M_v,M_g$ their molar masses. Define $H$ in kg vapour/kg dry gas. Dalton's law at total pressure $P$ gives $n_v/n_g=p_v/(P-p_v)$, where $p_v$ is the vapour partial pressure. Therefore

$$
H=\frac{M_vn_v}{M_gn_g}
=\frac{M_v}{M_g}\frac{p_v}{P-p_v}.
\tag{1}
$$

The dry-gas partial pressure appears in the denominator because the basis excludes vapour. With $\epsilon=M_v/M_g$, multiply through and collect terms in $p_v$:

$$
H(P-p_v)=\epsilon p_v,
\qquad
p_v=\frac{PH}{\epsilon+H}.
\tag{2}
$$

At saturation $p_v=p^{\mathrm{sat}}(T)$, giving

$$
H^*(T,P)=\epsilon\frac{p^{\mathrm{sat}}(T)}{P-p^{\mathrm{sat}}(T)}.
\tag{3}
$$

Use a vapour-pressure correlation with its specified temperature units, pressure units and logarithm base. For example $\ln[p^{\mathrm{sat}}/p_{\mathrm{ref}}]=A-B/(T+C)$ is an Antoine form; coefficients for $\log_{10}$ cannot be inserted unchanged.

Two percentage measures require care. Define $H_R=100H/H^*$ as **percentage saturation**, and conventional relative humidity $\phi=p_v/p^{\mathrm{sat}}$ as a fraction. Substituting (1) and (3),

$$
\frac{H_R}{100}
=\phi\frac{P-p^{\mathrm{sat}}}{P-\phi p^{\mathrm{sat}}}.
\tag{4}
$$

They agree at zero humidity and saturation, and approximately when both vapour pressures are small compared with $P$. Away from that limit they differ.

At fixed pressure and humidity, the vapour-to-carrier mole ratio and thus vapour partial pressure stay fixed during sensible heating. Saturation pressure rises with temperature, so relative humidity falls even though no water has left the gas. The gas becomes more capable of accepting water because its equilibrium endpoint has moved, not because heating has reduced its existing vapour inventory.

Percentage saturation uses a mass ratio with dry gas as denominator; relative humidity uses a partial-pressure ratio. The nonlinear conversion between mass ratio and partial pressure explains their unequal numerical values away from the dilute-vapour limit. Both locate the same physical state when their definitions are used consistently.

## Motivation and explanation

![Humidity chart with saturation, wet-bulb, enthalpy and volume lines](../figs/u2-humidity-chart.png)

Use the chart for its stated pressure. Locate dry-bulb temperature on the bottom scale and the humidity on its labelled lines; their intersection fixes the gas state. For $H^*$, follow the dry-bulb line to the saturation boundary, then read humidity there. A saturated gas is at equilibrium with liquid; gas lying below the boundary can accept more vapour.

The chart also contains curved relative-humidity lines, dashed enthalpy lines, solid wet-bulb lines and specific-volume lines. Follow the labels rather than judging a line by its angle. All mass-specific quantities here use kg dry gas as denominator.

Equation (3) requires $p^{\mathrm{sat}}<P$: as that pressure is approached the finite dry-carrier basis becomes inappropriate for describing a vapour-dominated mixture.

## Link to other topics

The saturation condition is the same phase-equilibrium condition used in vapour–liquid equilibrium. Dry-gas humidity ratios play the same conserved-basis role as solute-free concentration ratios in absorption.

## Conclusion

Use dry-gas humidity for material balances and specify the percentage-humidity convention. An energy balance requires the enthalpy associated with that same dry-gas basis.
