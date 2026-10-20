[Subject index](../README.md) · [Topic overview](README.md) · [Next](<RE-S5-02 - Apparent kinetics and oxide redox cycles.md>)

<!-- note-content:start -->
# Surface reaction mechanisms

## Overview

Assume competitive Langmuir adsorption. A surface reaction rate follows from the elementary rate-controlling step and the coverages supplied by faster steps. Distinguish gas–adsorbate collision from reaction between two adsorbates.

## Intuition

Two adsorbed reagents must coexist on a crowded surface for a Langmuir–Hinshelwood reaction. In an Eley–Rideal model one reagent stays in the gas and strikes an adsorbed partner, so the rate has a different dependence on the site inventory.

## Derivation

For overall irreversible $`\mathrm{A(g)+B(g)\to AB(g)}`$, assume transport is rapid, adsorption and desorption are fast relative to surface reaction, sites are equivalent, and the reacting pairs mix randomly. The Langmuir–Hinshelwood sequence is


**Equation (53)**

```math
\mathrm{A(g)}+*\rightleftharpoons\mathrm{A*},\quad
\mathrm{B(g)}+*\rightleftharpoons\mathrm{B*},\quad
\mathrm{A*+B*}\longrightarrow\mathrm{AB*}+*,\quad
\mathrm{AB*}\rightleftharpoons\mathrm{AB(g)}+*.
```


Fast reversible steps are approximately at adsorption equilibrium. With $`D=1+K_AP_A+K_BP_B+K_{AB}P_{AB}`$, their site balance gives $`\theta_A=K_AP_A/D`$ and $`\theta_B=K_BP_B/D`$. Define $`k_s`$ as the surface-reaction rate coefficient on the chosen catalyst basis, including site density and pair-count factors. The slow step gives $`r=k_s\theta_A\theta_B`$, hence


**Equation (54)**

```math
r=\frac{k_sK_AK_BP_AP_B}{(1+K_AP_A+K_BP_B+K_{AB}P_{AB})^2}.
```


The denominator is squared because the reaction needs two occupied fractions. A finite adsorption constant for product is compatible with a slow forward irreversible reaction; near overall equilibrium, however, the reverse surface reaction must be included and the net rate must vanish at the thermodynamic equilibrium condition.

For the Eley–Rideal sequence, take B adsorbed and A unadsorbed:


**Equation (55)**

```math
\mathrm{B(g)}+*\rightleftharpoons\mathrm{B*},\qquad
\mathrm{A(g)+B*}\longrightarrow\mathrm{AB*},\qquad
\mathrm{AB*}\rightleftharpoons\mathrm{AB(g)}+*.
```


There is no A coverage in the inventory under this assumption. Thus $`\theta_B=K_BP_B/(1+K_BP_B+K_{AB}P_{AB})`$. A gas collision rate is proportional to $`P_A`$, giving


**Equation (56)**

```math
r=k_sP_A\theta_B
=\frac{k_sK_BP_AP_B}{1+K_BP_B+K_{AB}P_{AB}}.
```


If A also adsorbs inertly on these sites, add its inventory term and distinguish that inhibitory adsorption from its reactive gas collision. Different mechanisms have different $`k_s`$ units because one uses two dimensionless coverages and the other also includes pressure.

## Motivation and explanation

A fast reversible adsorption step can carry the slow catalytic throughput while remaining close to equilibrium: its large forward and backward rates differ by only the small net flux needed by surface reaction. Setting their difference approximately to zero determines leading-order coverages; it does not assert that every net step in the catalytic cycle has stopped. This approximation fails when adsorption cannot replenish the consumed intermediate fast enough.

For Langmuir–Hinshelwood reaction, raising A pressure helps populate A sites but also reduces B's share of the same surface. Multiplying the two occupied fractions preserves both effects and produces the squared denominator. In the specified Eley–Rideal model, gaseous A needs no surface inventory of its own, so increasing its pressure changes collision frequency without displacing B. The different pressure responses follow from those physical inventories, not from an arbitrary choice of denominator power.

At dilute coverage both forms can appear first order in both reagents. Saturation and competition reveal differences. Strong adsorption is not automatically helpful: it can remove the neighbouring vacancies or partner coverage required for reaction. Product adsorption causes inhibition even when reverse reaction is negligible.

Rate-controlling adsorption or desorption cannot simultaneously be assumed at equilibrium. In those cases, retain its forward and backward rates and use steady balances for surface intermediates. Similarly, if internal or external diffusion is slow, the gas pressure at the active site differs from the bulk value.

## Link to other topics

Local reaction orders and apparent activation energies quantify these changing coverage effects. Oxide redox cycles need a different inventory because the solid supplies an atom to the product.

## Conclusion

Write the elementary steps, identify their timescales and conserve sites before simplifying the rate. The denominator then has a physical meaning.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Next](<RE-S5-02 - Apparent kinetics and oxide redox cycles.md>)
