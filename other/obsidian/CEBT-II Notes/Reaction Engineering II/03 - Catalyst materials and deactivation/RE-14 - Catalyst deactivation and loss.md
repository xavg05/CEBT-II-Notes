[Previous](<RE-13 - Catalyst materials and preparation.md>) · [Subject index](../README.md) · [Topic overview](README.md)

<!-- note-content:start -->
# RE-14: Catalyst deactivation and loss

## Overview

Assume the distinction between active metal, support and pore space. Catalyst performance declines through loss of accessible sites, chemical blocking and mechanical loss. Choosing a regeneration strategy requires identifying which mechanism occurred.

## Intuition

A catalyst can remain chemically present while becoming ineffective. Merging many small metal particles into fewer large ones hides atoms in their interiors. Covering an active site prevents its use. Blocking a pore makes downstream sites inaccessible even if those sites remain chemically active.

## Mechanisms

**Sintering** is the growth or coalescence of particles driven by reduction of surface free energy. Undercoordinated surface atoms have higher chemical potential than bulk atoms; high temperature increases their mobility. Migration and coalescence, or transfer of atoms from small to larger particles, reduce accessible surface area. Nanoparticles can become mobile well below the bulk melting temperature. A support stabilises dispersion but does not guarantee it.

**Poisoning** is strong occupation or chemical alteration of sites by impurities. Sulfur binds strongly to many metals, and metal-containing contaminants can accumulate in zeolites. Some poisoning is reversible when the impurity is removed; strong binding or structural damage can make it effectively irreversible on the operating timescale. Preventing contamination with feed purification or guard beds is often preferable to attempting recovery.

**Coking and fouling** deposit material on the surface or in pore entrances. Carbonaceous deposits from hydrocarbon reactions can be oxidised away. Burning coke is strongly exothermic, so an uncontrolled regeneration may remove the deposit while permanently sintering metal or damaging the support. Heat removal and oxygen supply therefore matter during regeneration as well as reaction.

**Attrition and fragmentation** physically remove catalyst. Fluidised particles collide, and internal thermal or mechanical stresses can fracture pellets. Fines may contaminate products, escape with gas or accumulate in fixed beds and increase pressure drop. Capillary forces during pore filling or drying can also stress a porous structure.

## Derivation

For an illustrative collection of spherical metal particles of diameter $d$, total metal volume $V_m$ and surface area $A_m$, each particle contributes $\pi d^3/6$ volume and $\pi d^2$ area. Eliminating the number of particles gives

$$A_m=\frac{6V_m}{d}.
\tag{40}$$

This holds for equal-sized spheres with fixed total metal volume. It isolates the geometrical reason that coarsening reduces area; it does not calculate sintering kinetics or account for buried metal–support contact.

## Motivation and explanation

The area calculation holds the amount of metal fixed. Coarsening changes where its atoms sit: a larger fraction becomes buried inside particles and a smaller fraction remains exposed. Recovering clean feed cannot reverse that geometrical loss, whereas removing a reversibly bound competitor can restore vacant sites without rebuilding the metal. A falling reactor rate alone cannot identify which change occurred.

A regeneration restores performance only if it reverses the limiting loss mechanism without creating another one. Coke oxidation can reopen pores, but the released heat raises the local sintering rate; increasing oxygen supply can therefore accelerate cleaning and worsen permanent damage at the same time. This explains why regeneration conditions need their own heat and transport model instead of being inferred from the original reaction temperature.

Slow deactivation may permit long fixed-bed campaigns with periodic replacement. Fast, regenerable coking favours continuous catalyst circulation between reactor and regenerator. The decision involves loss mechanism and timescale, rather than activity alone. Higher operating temperature can improve instantaneous rate while shortening useful catalyst life.

## Link to other topics

Deactivation determines whether a fixed, moving or fluidised bed is practical. Surface coverage by a reversible reactant must be distinguished from lasting occupation by a poison.

## Conclusion

Regeneration can remove reversible deposits, but it cannot reliably undo sintering or mechanical loss. Reactor selection must include the catalyst lifecycle.
<!-- note-content:end -->

[Previous](<RE-13 - Catalyst materials and preparation.md>) · [Subject index](../README.md) · [Topic overview](README.md)
