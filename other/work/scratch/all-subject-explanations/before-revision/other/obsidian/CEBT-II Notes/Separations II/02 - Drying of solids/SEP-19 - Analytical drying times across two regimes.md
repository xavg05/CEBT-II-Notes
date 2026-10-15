[Previous](<SEP-18 - Countercurrent drying and minimum gas flow.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-20 - Cocurrent drying and flow arrangement.md>)

<!-- note-content:start -->
# SEP-19: Analytical drying times across two regimes

## Overview

The residence time in a continuous dryer follows from the local rate at every moisture content. A fully wet regime and an internally limited regime require separate integrals, joined where their rate expressions agree.

Assumptions: steady countercurrent air/water drying, constant dry-gas/dry-solid ratio $m$, approximately constant $H^W$, negligible initial warm-up time, and applicable empirical laws over the specified moisture range.

## Intuition

*Water removal can accelerate while the cloth becomes drier.* In countercurrent flow it meets increasingly fresh gas. Once internal supply becomes restrictive, however, further drying slows despite that favourable gas environment.

## Derivation

Let $w$ be kg water/kg dry solid, $t$ time followed by a moving solid element, and $r=-dw/dt>0$ its specific drying rate. Rearrange this definition:

$$
dt=-\frac{dw}{r(w)}.
\tag{81}
$$

The minus sign is essential because $w$ decreases while time increases. For endpoints $w_1>w_2$,

$$
t=\int_{w_1}^{w_2}-\frac{dw}{r(w)}
=\int_{w_2}^{w_1}\frac{dw}{r(w)}.
\tag{82}
$$

The positive reciprocal-rate area is therefore the residence time.

Suppose the operating line is $\Delta H=a-bw$, where $b=1/m$ and $a=\Delta H_2+w_2/m$. The wet-surface branch is $r=\beta(a-bw)$; the fitted falling-rate branch is $r=\alpha w$, assuming equilibrium moisture negligible in the tested range. At their intersection,

$$
\beta(a-bw_c)=\alpha w_c,
\qquad
w_c=\frac{\beta a}{\alpha+\beta b}.
\tag{83}
$$

Use this computed transition only if $w_2<w_c<w_1$. Otherwise integrate the applicable branch over the whole interval.

In the wet-surface regime, insert its rate into (2). Since $d(a-bw)=-b\,dw$,

$$
t_{\mathrm{const}}
=\int_{w_c}^{w_1}\frac{dw}{\beta(a-bw)}
=\frac{1}{\beta b}
\ln\!\left(\frac{a-bw_c}{a-bw_1}\right).
\tag{84}
$$

The logarithm reflects a changing driving force, even though the regime is called “constant rate”. In the internally limited branch,

$$
t_{\mathrm{fall}}
=\int_{w_2}^{w_c}\frac{dw}{\alpha w}
=\frac{1}{\alpha}\ln\!\left(\frac{w_c}{w_2}\right).
\tag{85}
$$

Add the two positive times. As $w_2$ approaches the equilibrium endpoint of this zero-equilibrium fit, the logarithm diverges.

## Motivation and explanation

The transition is not a fixed material number in this model: it moves when gas ratio or gas humidity changes. At the saturated-gas pinch, $a-bw_1\to0$, the time in (4) diverges. This supplies the rate-based reason for operating above the minimum gas requirement.

The distinction between a branch independent of moisture **at fixed gas conditions** and a constant rate **along a dryer** prevents using one average-rate division in place of (4).

If the final moisture is unknown but residence time is known, trial a final $w_2$, reconstruct its operating line, find the transition and compute total time. Update $w_2$ until the required time is met. Changing the endpoint changes the operating line as well as the integral limits.

## Worked example

Use countercurrent cloth drying from $w_1=0.9$ to $w_2=0.1$ kg/kg, with $m=80$ kg dry air/kg dry cloth and

$$
\Delta H=0.01325-0.0125w,
\qquad
r_{\mathrm{wet}}=10\Delta H,
\qquad
r_{\mathrm{fall}}=0.5w.
$$

Time is in hours; the coefficient 10 includes the dry-gas/dry-solid humidity-basis conversion. Equation (83) gives $w_c=0.212$ kg/kg. Equations (4)–(5) give

$$
t_{\mathrm{const}}\approx13.34\ \mathrm{h},
\qquad
t_{\mathrm{fall}}\approx1.50\ \mathrm{h},
\qquad
t_{\mathrm{total}}\approx14.84\ \mathrm{h}.
$$

Given approximate chart inputs, report the total as approximately 14.8 h. Exit humidity from the mass balance is approximately 0.0136 kg/kg. Following the inlet adiabatic chart line gives an exit dry bulb roughly 25°C; a constant-enthalpy calculation gives approximately 24.85°C. The gas-path approximation and chart precision limit a more exact temperature claim.

## Link to other topics

Following a solid element converts a continuous dryer into a local time-integration problem, like a plug-flow residence-time calculation. The rate law and operating line remain separate ingredients.

## Conclusion

Join rate branches at a consistent transition and integrate reciprocal rate with positive limits. Flow arrangement changes which gas conditions meet the material and therefore changes that integral.
<!-- note-content:end -->

[Previous](<SEP-18 - Countercurrent drying and minimum gas flow.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-20 - Cocurrent drying and flow arrangement.md>)
