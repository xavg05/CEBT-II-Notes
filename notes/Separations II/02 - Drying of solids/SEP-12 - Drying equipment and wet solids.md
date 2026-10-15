[Previous](<../01 - Introduction and absorption/SEP-11 - Designing an ammonia absorber.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-13 - Humidity and saturation charts.md>)

<!-- note-content:start -->
# SEP-12: Drying equipment and wet solids

## Overview

Drying removes water or another volatile liquid by vaporisation. Its design couples heat supply, movement of moisture through the solid and removal of vapour from the surface. The first choice is how to handle the material and supply heat; a high evaporation capacity is useful only if the final product keeps its required structure.

Assumed background: heat-transfer coefficients, latent heat and elementary mass balances.

## Intuition

*Removing liquid mechanically avoids paying the energy cost of converting it into vapour.* Drainage, filtration or centrifugation therefore precedes thermal drying wherever practical. Once the readily removable liquid has gone, heat must reach the evaporation region and vapour must escape.

Water held in open spaces between particles can leave with little change to the solid. Water dissolved in a polymer, held in fibres or confined in fine pores may leave only slowly; the solid can shrink as it dries and swell on rewetting. The same gas conditions can consequently give very different drying times.

## Derivation

Let $`m_s`$ be the conserved mass of bone-dry solid and $`m_l`$ its liquid mass. Define dry-basis moisture content $`w=m_l/m_s`$, in kg liquid per kg dry solid. Conservation gives the liquid removed between two states:


**Equation (51)**

```math
\Delta m_l=m_s(w_1-w_2).
```


The denominator stays fixed, which makes this basis convenient even while the product loses mass.

If a fraction $`z=m_l/(m_l+m_s)`$ is instead reported on a wet basis, divide both numerator and denominator by $`m_s`$:


**Equation (52)**

```math
z=\frac{w}{1+w},
\qquad
w=\frac{z}{1-z}.
```


This conversion is essential before comparing product specifications with dry-basis rate data. An ideal lower estimate of the latent-heat duty is


**Equation (53)**

```math
Q_{\mathrm{vap}}=\Delta m_l\lambda,
```


where $`\lambda`$ is the latent heat in J/kg liquid. Actual duty also includes sensible heating and losses; the estimate does not size equipment.

Dry-basis accounting removes a moving denominator. Evaporating liquid changes the wet product mass, so a decrease in wet-basis moisture combines a change of liquid inventory with a change in the reference mass. Dividing by the conserved dry solid isolates the inventory that is actually being removed. This is why the dry-basis moisture difference can be multiplied directly by dry-solid mass.

The latent-heat estimate accounts for an amount of evaporation, not its speed. The same liquid removal can require a short intense heat input or a longer gentle input, subject to internal transport and product limits. Equipment choice needs those rates and constraints as well as the integrated energy duty.

## Motivation and explanation

In a **direct dryer**, hot gas touches the wet solid, supplies heat and carries away vapour. Gas can pass across a surface or through a permeable bed. Moving particles can shower through rising gas, remain in a fluidised bed or become entrained in a rapid gas stream. Continuous sheets favour a conveyor or supported surface; readily fluidised particles allow much more intimate gas contact.

In an **indirect dryer**, heat comes through a heated wall or from radiation or microwave absorption. An agitator, screw, paddle or rotating vessel can expose fresh material to the heating surface. A sweep gas may still remove vapour: indirect heating does not require the complete absence of carrier gas.

Batch versus continuous operation, agitation and reduced pressure are separate choices. Vacuum lowers the boiling temperature, although evaporation into unsaturated gas can occur without bulk boiling. “Adiabatic direct drying” means no substantial heat crosses the dryer boundary after the hot gas enters; heating the inlet gas still requires energy.

Choose in sequence: establish product form and temperature limits; locate the moisture and likely transport resistance; identify a workable handling/contacting method; then obtain drying-rate data under representative conditions. Increasing surface heat transfer alone may overheat a material whose internal moisture migration already controls.

## Worked example

A cloth with $`w=0.9`$ kg water/kg dry cloth contains a wet-basis water fraction $`z=0.4737`$, approximately 47%. Conversely, a product containing 20% water on a wet basis has $`w=0.25`$ kg/kg dry solid. These are different moisture specifications, despite both being mass ratios.

A fragile hygroscopic sheet calls for controlled temperature and supported handling. A mechanically robust granular solid can instead tolerate agitation and through-flow gas. The distinction follows from product integrity and transport paths, before any calculation of dryer length.

## Link to other topics

Mechanical dewatering connects drying to filtration and centrifugation. The gas-side state is described using humidity and enthalpy, while the changing solid moisture determines which drying regime applies.

## Conclusion

A dryer must handle the material, supply vaporisation energy and remove vapour at compatible rates. Humidity gives the next piece of the design: how much moisture the gas already contains and how close it is to saturation.
<!-- note-content:end -->

[Previous](<../01 - Introduction and absorption/SEP-11 - Designing an ammonia absorber.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-13 - Humidity and saturation charts.md>)
