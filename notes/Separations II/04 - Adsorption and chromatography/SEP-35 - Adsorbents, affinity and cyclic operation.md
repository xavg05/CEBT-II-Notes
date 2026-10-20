[Previous](<../03 - Membrane separations/SEP-34 - Reverse-osmosis recovery and area design.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-36 - Langmuir and Freundlich equilibrium models.md>)

<!-- note-content:start -->
# SEP-35: Adsorbents, affinity and cyclic operation

## Overview

Assumed: phase equilibrium and material balances.

Adsorption separates a solute by concentrating it on a solid surface. A useful adsorbent must combine selective affinity, accessible capacity and a practical way to release the captured solute. This makes regeneration part of the separation design from the outset.

## Intuition

The **adsorbate** is the captured solute; the **adsorbent** is the solid that captures it. Adsorption occurs at a surface, whereas absorption distributes a species into the bulk of another phase. A porous bead exposes internal surfaces, but molecules must reach those surfaces before their capacity can be used.

Physical adsorption arises principally from intermolecular forces; chemical adsorption involves chemical bonding at surface sites. Physical adsorption can form multiple layers. Chemical adsorption is often more specific and difficult to reverse. These are mechanistic distinctions: a single binding-energy cutoff does not reliably classify every system.

## Derivation

**Step 1: distinguish equilibrium loading from working capacity.** Let $`q_L`$ be the loading reached after adsorption and $`q_H`$ the residual loading after regeneration, both in kg solute per kg dry adsorbent. For adsorbent mass $`M`$, solute released over a cycle is


**Equation (151)**

```math
m_{\mathrm{cycle}}=M(q_L-q_H).
```


*Reason:* loading is inventory per unit solid mass; subtracting the residual inventory gives the amount available for the next cycle. Equilibrium saturation capacity alone therefore overstates usable cyclic capacity.

**Step 2: identify the direction of regeneration.** At equilibrium the chemical potential of a species in the fluid equals that in the adsorbed phase. Changing temperature, partial pressure or liquid composition changes that equilibrium. For ordinary exothermic gas adsorption, heating or lowering partial pressure reduces equilibrium loading and promotes desorption.

*Reason:* regeneration requires reversing the chemical-potential difference that previously drove uptake. Surface area cannot replace that thermodynamic requirement.

A cycle uses a difference between inventories, not the maximum inventory alone. A material can load strongly under feed conditions yet retain nearly as much under the available regeneration conditions, leaving little capacity for the next cycle. Selective capture and useful release must therefore be assessed as a pair of operating states.

The equilibrium difference is still an upper opportunity, not a guarantee of throughput. Finite loading and regeneration times determine how much of that difference is reached before switching. Transport can leave capacity inaccessible even when the isotherm predicts room for more solute.

## Motivation and explanation

The cycle is load, optionally wash, desorb and restore the adsorbent to its loading conditions. Washing removes unbound material in liquid separations; it can also lose weakly bound product. Ion-exchange purification changes solute charge through pH or uses salt competition to release a bound biomolecule. Gas beds commonly omit washing and combine desorption with regeneration.

Activated carbon is useful for many organic impurities; alumina can remove water, and zeolites combine pore-size selectivity with chemical affinity. Water softening exchanges dissolved cations for counterions; deionisation uses complementary cation and anion exchangers. These operations require appropriate charge balances as well as capacity balances.

Large internal area is useful only when pores admit the solute and transport is fast enough. Particle size, pressure drop, attrition, thermal stability and regeneration time can determine the practical choice.

## Link to other topics

Adsorption equilibrium connects to chemical potential, while accessible capacity depends on the diffusion mechanisms used in porous catalyst models. Biomolecule purification adds selectivity and recovery requirements to the same inventory balance.

## Conclusion

An adsorbent must capture selectively and release usefully. The next step is to relate equilibrium loading to fluid concentration or partial pressure.
<!-- note-content:end -->

[Previous](<../03 - Membrane separations/SEP-34 - Reverse-osmosis recovery and area design.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-36 - Langmuir and Freundlich equilibrium models.md>)
