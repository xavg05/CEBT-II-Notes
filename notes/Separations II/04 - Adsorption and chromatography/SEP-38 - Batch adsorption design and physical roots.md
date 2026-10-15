[Previous](<SEP-37 - Adsorption transport and uptake kinetics.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-39 - Fixed beds, breakthrough and usable capacity.md>)

<!-- note-content:start -->
# SEP-38: Batch adsorption design and physical roots

## Overview

Assumed: material balances and the Langmuir isotherm.

A batch adsorber is one equilibrium contact between a finite liquid volume and a finite solid mass. Combining its inventory balance with an isotherm determines either required adsorbent mass or final liquid concentration.

## Intuition

Removing solute lowers its liquid concentration, which also lowers the loading that the solid can sustain. The final state is an intersection of the material-balance line and the isotherm, not the original feed concentration evaluated in the isotherm.

## Derivation

**Step 1: conserve solute.** Let $`V`$ be liquid volume, $`C_0`$ initial liquid concentration, $`C_e`$ final concentration, $`M`$ dry adsorbent mass and $`q_0,q_e`$ initial and final solid loadings. Assume constant volume, temperature and no chemical destruction:


**Equation (160)**

```math
V(C_0-C_e)=M(q_e-q_0).
```


*Reason:* the loss from liquid equals the increase in solid inventory. For fresh solid, $`q_0=0`$.

**Step 2: size for a specified target.** With fresh solid and $`q_e=Q_mC_e/(K_d+C_e)`$,


**Equation (161)**

```math
M=\frac{V(C_0-C_e)(K_d+C_e)}{Q_m C_e}.
```


*Reason:* substitute equilibrium loading into the balance and isolate solid mass. The denominator tends to zero as a positive feed is polished toward zero concentration; finite Langmuir affinity cannot achieve complete removal with finite mass.

**Step 3: solve concentration for a given mass.** Multiply Equation (160) by $`K_d+C_e`$ and expand:


**Equation (162)**

```math
V C_e^2+[V(K_d-C_0)+M Q_m]C_e-V C_0K_d=0.
```


*Reason:* clearing the rational isotherm produces a quadratic, whose root still requires a physical check. With positive parameters, its constant term is negative, so one root is positive and the other negative. The admissible root must also satisfy $`0<C_e<C_0`$.

## Motivation and explanation

The final liquid concentration appears inside the isotherm because adsorption and depletion proceed together. Evaluating solid capacity at the original feed concentration assumes the liquid remains rich even after removing its solute. Solving for the intersection instead enforces that the final solid loading is sustainable at the liquid concentration actually left behind.

The negative algebraic root fails before any kinetic question arises: it implies negative fluid inventory. Checking the positive root against the original, uncleared balance also confirms that clearing the isotherm denominator has not introduced an inadmissible state. Time to reach that root remains a separate transport calculation.

Contact time and agitation determine approach to that endpoint. A reused adsorbent also requires its initial loading $`q_0`$ in the balance; it does not have the full capacity of fresh solid.

A graphical construction plots $`q_e`$ against $`C_e`$: the balance line has slope $`-V/M`$ and intercept $`VC_0/M+q_0`$. Its intersection with the increasing isotherm is the equilibrium state. A steeper balance line reflects less adsorbent per liquid volume.

## Worked example

An illustrative batch has $`V=1.00\ \mathrm{m^3}`$, $`C_0=0.100\ \mathrm{kg\,m^{-3}}`$, $`M=1.00\ \mathrm{kg}`$, $`Q_m=0.200\ \mathrm{kg\,kg^{-1}}`$ and $`K_d=0.0500\ \mathrm{kg\,m^{-3}}`$. The physical quadratic root is


```math
C_e=0.0280776\ \mathrm{kg\,m^{-3}},\qquad q_e=0.0719224\ \mathrm{kg\,kg^{-1}}.
```


Substitution conserves the initial solute inventory. If instead the target is $`C_e=0.0100\ \mathrm{kg\,m^{-3}}`$, Equation (161) requires **$`M=2.70\ \mathrm{kg}`$** of fresh adsorbent. This calculation specifies an equilibrium mass, not a residence time.

## Link to other topics

Batch adsorption uses the same equilibrium/inventory separation as extraction. Fixed beds retain that balance but introduce spatially varying loading and breakthrough.

## Conclusion

Solve the balance and isotherm together, retain the physical root and check inventory. A flowing bed requires tracking capacity as a front advances.
<!-- note-content:end -->

[Previous](<SEP-37 - Adsorption transport and uptake kinetics.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-39 - Fixed beds, breakthrough and usable capacity.md>)
