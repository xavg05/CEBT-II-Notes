# Countercurrent drying and minimum gas flow

## Overview

A continuous countercurrent dryer pairs wet incoming solid with humid outgoing gas, and dry outgoing solid with fresh incoming gas. A water balance constructs the operating line and gives a limiting gas requirement before residence time is calculated.

Assumptions: steady flow, conserved dry solid and dry carrier gas, negligible entrainment, an adiabatic air/water path with approximately constant wet bulb, and negligible net sensible heating of the solid in the simplified gas-path model.

## Intuition

The gas picks up moisture as it travels toward the wet-solid inlet. More dry gas can carry the same evaporated water with a smaller humidity increase. The minimum gas flow corresponds to a saturation pinch, where the driving force becomes zero.

## Derivation

Label the solid inlet end 1 and solid outlet end 2. The solid enters with $w_1$ and leaves with $w_2$ kg water/kg dry solid; gas enters end 2 at humidity $H_2$ and leaves end 1 at $H_1$ kg water/kg dry gas. Define

$$
m=\frac{\dot m_g}{\dot m_s},
\tag{1}
$$

where $\dot m_g,\dot m_s$ are dry-gas and dry-solid mass flow rates. $m$ is kg dry gas/kg dry solid, not a standalone gas mass flow rate.

On a basis of 1 kg dry solid, inlet water equals outlet water:

$$
w_1+mH_2=w_2+mH_1,
\qquad
m(H_1-H_2)=w_1-w_2.
\tag{2}
$$

Take a control region from an intermediate cross-section to end 2. Gas picks up exactly the liquid lost by the solid over that region, giving

$$
m(H-H_2)=w-w_2.
\tag{3}
$$

This **operating line** fixes which gas humidity meets each solid moisture. If $H^W$ stays constant along the approximate air/water gas path, set $\Delta H=H^W-H$ and $\Delta H_2=H^W-H_2$. Subtract (3) from the saturation reference:

$$
\Delta H=\Delta H_2-\frac{w-w_2}{m}.
\tag{4}
$$

The negative slope means the wetter solid meets gas with a smaller evaporation driving force.

If incoming material has a fully wet surface, limiting outlet gas approaches saturation at the common wet-bulb temperature, $H_1\to H^W$. Insert that endpoint in (2):

$$
m_{\min}
=\frac{w_1-w_2}{H^W-H_2}.
\tag{5}
$$

This is a thermodynamic lower bound within the model. At equality, the inlet-solid end has $\Delta H=0$ and finite throughput requires unbounded contacting time or length for a linear flux law.

The minimum gas ratio follows from water-carrying capacity, while the actual ratio sets the local humidity rise per unit water picked up. With more dry gas, each increment of evaporated water causes a smaller humidity increase, leaving the gas farther from saturation. The selected margin therefore creates a finite driving force but does not by itself determine residence time.

In countercurrent operation, plot position along the solid path and position along the gas path run in opposite directions. Anchoring the operating line at the dry-solid/fresh-gas end fixes that pairing before any signs are chosen. The negative driving-force slope is a consequence of this physical pairing, not a convention that can be copied unchanged to cocurrent operation.

## Motivation and explanation

![Countercurrent gas and solid endpoints](../figs/u2-countercurrent.png)

Construct the design in order. Specify inlet gas and its wet-bulb/saturation humidity from the correct-pressure chart. Calculate water removed on a dry-solid basis. Find the limiting gas ratio from the pinch, then select a larger operating ratio. Draw (3), or (4) when its assumptions apply, through the outlet-solid/inlet-gas endpoint. Check both endpoints against the overall balance.

Gas saturation at wet bulb is not saturation at inlet dry-bulb temperature. Using the latter would overestimate gas water-carrying capacity. A hygroscopic feed that does not present a fully wet surface can impose a different equilibrium limit.

## Link to other topics

The drying operating line is constructed by the same conserved-component logic as a countercurrent absorption operating line. Its minimum gas ratio is a pinch bound rather than a rate-based equipment size.

## Conclusion

The gas ratio and operating line establish the local humidity driving force. Residence time comes next, from integrating the actual rate as the solid follows that line.
