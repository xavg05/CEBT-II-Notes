[Previous](<SEP-13 - Humidity and saturation charts.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-15 - Dew point and cooling moist gas.md>)

<!-- note-content:start -->
# SEP-14: Humid enthalpy and adiabatic saturation

## Overview

Evaporation into an insulated gas stream trades sensible heat for latent heat. A humid-gas enthalpy balance explains the falling temperature, rising humidity and approach to adiabatic saturation.

Assumptions: ideal gas enthalpies, constant heat capacities, constant pressure, no shaft work and negligible kinetic/potential energy changes.

## Intuition

*The energy carried by hot air can be spent making vapour instead of keeping the mixture hot.* Added liquid evaporates while the gas cools. Eventually the gas is saturated at a lower temperature and cannot vaporise further liquid under the same conditions.

## Derivation

Take 1 kg dry gas. It accompanies $H$ kg vapour. Set dry-gas and liquid enthalpies to zero at reference temperature $T_0$. Let $C_{p,g},C_{p,v},C_{p,l}$ be specific heat capacities, and $\lambda_0$ the liquid-to-vapour enthalpy difference at $T_0$. Adding the component enthalpies gives

$$
h=C_{p,g}(T-T_0)
+H[\lambda_0+C_{p,v}(T-T_0)].
\tag{58}
$$

$h$ is J/kg dry gas. The **humid heat**, $s$, is the fixed-$H$ temperature derivative:

$$
s=C_{p,g}+HC_{p,v},
\qquad
h=s(T-T_0)+H\lambda_0.
\tag{59}
$$

It is per kg dry gas, not per kg mixture, and changes as $H$ changes.

Now let inlet state $(T_1,H_1)$ contact liquid supplied at $T_l$. If all added liquid evaporates, its mass per kg dry gas is $H_3-H_1$. Conservation of energy therefore gives

$$
h(T_3,H_3)
=h(T_1,H_1)+(H_3-H_1)C_{p,l}(T_l-T_0).
\tag{60}
$$

This equation retains the incoming liquid's energy. If its contribution is negligible, $h_3\approx h_1$. Differentiate (1) along that approximate path:

$$
0=s\,dT+[\lambda_0+C_{p,v}(T-T_0)]\,dH,
\qquad
\frac{dH}{dT}
=-\frac{s}{\lambda_0+C_{p,v}(T-T_0)}.
\tag{61}
$$

The negative slope represents evaporative cooling. Dropping vapour sensible enthalpy in the denominator gives the common slope $-s/\lambda_0$; treating $s$ as constant makes the line approximately straight.

At adiabatic saturation let the gas leave at $T^S$ with $H^S=H^*(T^S,P)$. For an equilibrated saturator supplied with liquid at $T^S$, insert these conditions into (3):

$$
h(T^S,H^S)
=h(T_1,H_1)+(H^S-H_1)C_{p,l}(T^S-T_0).
\tag{62}
$$

Solve this energy equation together with the saturation relation, rather than assuming an arbitrary outlet temperature.

## Motivation and explanation

On the humidity chart, start at the inlet state and follow the adiabatic-saturation line toward its intersection with the saturation curve. The curve imposes equilibrium; the path imposes energy conservation. Approximate constant-enthalpy lines nearly reproduce that construction for ordinary air/water conditions, but the liquid sensible term and changing humid heat explain why the descriptions are not exactly interchangeable.

The latent term is large, so a relatively small humidity increase can absorb substantial sensible energy. Additional wall heating or significant heating of the solid changes the path and must enter the balance.

## Worked example

Using $T_0=0$°C, $C_{p,g}=1.006$, $C_{p,v}=1.86$ kJ/(kg K), and $\lambda_0=2501$ kJ/kg, air at 40°C with $H=0.020$ has $s=1.0432$ kJ/(kg dry gas K) and $h=91.748$ kJ/kg dry gas, approximately 92.

For 40°C, $H=0.010$ and $P=100$ kPa, solve (5) using $C_{p,l}=4.186$ kJ/(kg K) and the water saturation relation. The result is $T^S\approx22.43$°C and $H^S\approx0.01735$ kg/kg. Chart estimates are approximately 22.5°C and 0.0174 kg/kg. If the incoming liquid enthalpy is neglected, the constant-$h$ intersection is approximately 22.24°C: close, but a different approximation.

## Link to other topics

The humid enthalpy balance combines phase-change thermodynamics with conserved carrier-gas accounting. It establishes the gas path needed for drying calculations and provides a comparison with the wet-bulb heat-transfer balance.

## Conclusion

Adiabatic saturation is an equilibrium endpoint selected by an energy balance. Dew point describes a different route to saturation: cooling at unchanged humidity before condensation begins.
<!-- note-content:end -->

[Previous](<SEP-13 - Humidity and saturation charts.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-15 - Dew point and cooling moist gas.md>)
