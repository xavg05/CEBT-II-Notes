# Cocurrent drying and flow arrangement

## Overview

In cocurrent drying, fresh gas meets the wettest solid, and gas becomes more humid as the material dries. Reversing the operating-line slope changes the rate history and may move the regime transition outside the required moisture range.

Assumptions: the same steady dry-gas/dry-solid accounting and approximate constant-wet-bulb air/water path used for countercurrent drying.

## Intuition

The wettest solid receives the strongest gas-side driving force. At the product end both gas and solid have cooled, but the gas is now humid. Countercurrent flow instead exposes the driest material to the freshest, hottest gas; product temperature and internal drying resistance both matter when choosing between them.

## Derivation

Let end 1 now contain both inlets and end 2 both outlets. Define $w_1,w_2$ as inlet/outlet solid moisture and $H_1,H_2$ as inlet/outlet gas humidity. Let $m$ be kg dry gas/kg dry solid. The overall water balance still gives

$$
m(H_2-H_1)=w_1-w_2.
\tag{1}
$$

For a control region from the inlets to a local section, the gas has gained the water the solid has lost:

$$
m(H-H_1)=w_1-w.
\tag{2}
$$

With fixed surface saturation humidity $H^W$, define inlet driving force $\Delta H_1=H^W-H_1$. Subtract (2) from $H^W$:

$$
\Delta H=\Delta H_1-\frac{w_1-w}{m}.
\tag{3}
$$

Alternatively anchor the line at the outlet pair, using $\Delta H_2=H^W-H_2$:

$$
\Delta H=\Delta H_2+\frac{w-w_2}{m}.
\tag{4}
$$

The slope in a plot of $\Delta H$ against $w$ is positive. As the moving material dries, it follows this line toward a smaller driving force.

To calculate time, insert (3) into the local rate law and integrate $t=\int_{w_2}^{w_1}dw/r(w)$. Check whether a transition $r_{\mathrm{wet}}=r_{\mathrm{fall}}$ lies inside the interval; an algebraic crossing outside it does not create an extra regime.

In the specified cocurrent case the external rate stays below the fitted internal-supply rate throughout the target interval, so a wet surface can be maintained down to the chosen endpoint. Countercurrent operation assigns different gas conditions to the same solid moisture and therefore crosses the two rates at a different point. The change in calculated regimes follows from matching local demand to local supply, not from a change in the material coefficients.

Equal ideal wet-regime times for some terminal states do not imply identical temperature histories. The hottest gas meets wet material in one arrangement and drier material in the other. Product overheating and damage therefore require the material-energy calculation even when the simplified moisture-time integrals happen to coincide.

## Motivation and explanation

![Cocurrent gas–solid operation and the outlet-anchored operating line](../figs/u2-cocurrent.png)

Use endpoint numbers consistently: $H_1$ is inlet humidity in this arrangement, whereas it labelled outlet humidity in the countercurrent arrangement. Naming the physical streams before writing a balance avoids a sign error.

If the solid remains fully wet throughout, $r=\beta\Delta H$ with constant $\beta$, and both arrangements share the same terminal gas states, changing the integration variable from $w$ to $\Delta H$ gives

$$
t=\frac{m}{\beta}
\ln\!\left(\frac{\Delta H_{\mathrm{in}}}{\Delta H_{\mathrm{out}}}\right).
\tag{5}
$$

Thus their ideal fully wet times can coincide. Their local driving forces still vary and are paired with opposite solid endpoints. Falling-rate transport, coefficient changes, solid sensible heating or different gas distribution remove this simple equivalence. Cross-flow requires its actual gas distribution and cannot inherit (3) automatically.

## Link to other topics

The operating-line sign change resembles the distinction between cocurrent and countercurrent mass-transfer contactors. Heat-sensitive product design also requires the solid temperature history, beyond the water balance.

## Conclusion

Changing flow direction changes the gas–solid pairing, the operating line and sometimes the number of regimes traversed. Measured rate curves can replace analytical branches when the material response is more complicated.
