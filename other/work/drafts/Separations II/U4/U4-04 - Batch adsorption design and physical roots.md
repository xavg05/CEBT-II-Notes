# Batch adsorption design and physical roots

## Overview

Assumed: material balances and the Langmuir isotherm.

A batch adsorber is one equilibrium contact between a finite liquid volume and a finite solid mass. Combining its inventory balance with an isotherm determines either required adsorbent mass or final liquid concentration.

## Intuition

Removing solute lowers its liquid concentration, which also lowers the loading that the solid can sustain. The final state is an intersection of the material-balance line and the isotherm, not the original feed concentration evaluated in the isotherm.

## Derivation

**Step 1: conserve solute.** Let $V$ be liquid volume, $C_0$ initial liquid concentration, $C_e$ final concentration, $M$ dry adsorbent mass and $q_0,q_e$ initial and final solid loadings. Assume constant volume, temperature and no chemical destruction:

$$V(C_0-C_e)=M(q_e-q_0).\tag{1}$$

*Reason:* the loss from liquid equals the increase in solid inventory. For fresh solid, $q_0=0$.

**Step 2: size for a specified target.** With fresh solid and $q_e=Q_mC_e/(K_d+C_e)$,

$$M=\frac{V(C_0-C_e)(K_d+C_e)}{Q_m C_e}.\tag{2}$$

*Reason:* substitute equilibrium loading into the balance and isolate solid mass. The denominator tends to zero as a positive feed is polished toward zero concentration; finite Langmuir affinity cannot achieve complete removal with finite mass.

**Step 3: solve concentration for a given mass.** Multiply Equation (1) by $K_d+C_e$ and expand:

$$V C_e^2+[V(K_d-C_0)+M Q_m]C_e-V C_0K_d=0.\tag{3}$$

*Reason:* clearing the rational isotherm produces a quadratic, whose root still requires a physical check. With positive parameters, its constant term is negative, so one root is positive and the other negative. The admissible root must also satisfy $0<C_e<C_0$.

## Motivation and explanation

The final liquid concentration appears inside the isotherm because adsorption and depletion proceed together. Evaluating solid capacity at the original feed concentration assumes the liquid remains rich even after removing its solute. Solving for the intersection instead enforces that the final solid loading is sustainable at the liquid concentration actually left behind.

The negative algebraic root fails before any kinetic question arises: it implies negative fluid inventory. Checking the positive root against the original, uncleared balance also confirms that clearing the isotherm denominator has not introduced an inadmissible state. Time to reach that root remains a separate transport calculation.

Contact time and agitation determine approach to that endpoint. A reused adsorbent also requires its initial loading $q_0$ in the balance; it does not have the full capacity of fresh solid.

A graphical construction plots $q_e$ against $C_e$: the balance line has slope $-V/M$ and intercept $VC_0/M+q_0$. Its intersection with the increasing isotherm is the equilibrium state. A steeper balance line reflects less adsorbent per liquid volume.

## Link to other topics

Batch adsorption uses the same equilibrium/inventory separation as extraction. Fixed beds retain that balance but introduce spatially varying loading and breakthrough.

## Conclusion

Solve the balance and isotherm together, retain the physical root and check inventory. A flowing bed requires tracking capacity as a front advances.
