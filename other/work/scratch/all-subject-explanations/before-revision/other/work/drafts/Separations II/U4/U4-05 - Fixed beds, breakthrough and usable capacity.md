# Fixed beds, breakthrough and usable capacity

## Overview

Assumed: adsorption equilibrium and transient material balances.

A fixed bed can treat a continuously flowing feed while its solid loading changes. Breakthrough measures when the outlet no longer meets specification; integrating the breakthrough curve measures captured inventory.

## Intuition

The inlet region loads first. A **mass-transfer zone** separates loaded upstream material from relatively fresh downstream material and travels toward the outlet. When its leading edge arrives there, solute begins to escape even though the whole bed is not saturated.

![Concentration profiles moving through an adsorption bed](../figs/u4-fronts.png)

## Derivation

**Step 1: define outlet and flow.** Let $C_1$ be constant inlet solute concentration, $C_2(t)$ outlet concentration and $Q=uA$ volumetric flow, with superficial velocity $u$ and bed cross-sectional area $A$. Define $f(t)=C_2(t)/C_1$.

For adsorbent mass $M$, average loading $\bar q$, initial loading $q_0$ and changing fluid-phase inventory $m_f$,

$$M[\bar q(t)-q_0]+[m_f(t)-m_f(0)]=Q C_1\int_0^t[1-f(\tau)]\,d\tau.\tag{1}$$

*Reason:* integrated inlet minus outlet equals all accumulated solute, including that within the bed fluid. Neglecting fluid storage is an approximation justified when solid inventory dominates.

**Step 2: define breakthrough and total capture time.** Choose an outlet limit $f_b$ and find the first $t_b$ at which $f(t_b)=f_b$. If the curve approaches one sufficiently fast, define

$$t^*=\int_0^\infty[1-f(t)]\,dt,\qquad M(q_{\mathrm{sat}}-q_0)\approx Q C_1t^*.\tag{2}$$

*Reason:* area above the outlet curve counts feed retained rather than discharged. The integral has units **time**; dividing it by elapsed time gives a captured fraction over that interval.

**Step 3: interpret the midpoint cautiously.** For a centred symmetric transition with negligible early leakage, deficits before the half-height point match tails after it, giving $t^*\approx t_{0.5}$. The capacity-equivalent unused length at breakthrough is approximately

$$\frac{L_{\mathrm{UB}}}{L}\approx1-\frac{t_b}{t^*}.\tag{3}$$

*Reason:* before breakthrough, captured feed is approximately proportional to elapsed time. A travelling front of unchanged shape then leaves a nearly constant unused-equivalent length as total bed length increases. This length is not automatically identical to the geometric mass-transfer-zone width.

## Motivation and explanation

Finite transfer resistance and axial dispersion broaden the zone. An ideal instantaneous-equilibrium, nondispersive front is sharper, but real isotherm shape also influences front spreading. A sharper curve gives more useful service before a low outlet limit is exceeded **when total capacity and operating conditions are comparable**.

![Breakthrough and the area representing captured feed](../figs/u4-breakthrough.png)

For design, specify the allowable outlet concentration, measure or model the curve at the intended conditions, integrate captured inventory, then allow for the heel left after regeneration. Larger particles, higher flow and different loading conditions can change the zone; extrapolating an unchanged $L_{\mathrm{UB}}$ requires evidence.

## Worked example

Illustrative measurements at times $0,100,200,300,400,500,600\ \mathrm{s}$ give outlet fractions $0,0,0,0.2,0.5,0.8,1$. Piecewise-linear integration gives $t^*=400\ \mathrm{s}$. For $Q=0.0100\ \mathrm{m^3\,s^{-1}}$, $C_1=0.200\ \mathrm{kg\,m^{-3}}$ and $M=10.0\ \mathrm{kg}$, neglecting fluid inventory gives a capacity increase of **$0.0800\ \mathrm{kg\,kg^{-1}}$**.

A $5\%$ outlet limit gives $t_b=225\ \mathrm{s}$ by interpolation. Equation (3) estimates $L_{\mathrm{UB}}/L\approx0.4375$. This approximation neglects the small amount already discharged before breakthrough; Equation (1) remains the inventory authority.

## Link to other topics

Breakthrough connects transient transport to equilibrium capacity. The same band spreading reappears in chromatography, where the objective is to separate eluting species rather than stop before contaminant escape.

## Conclusion

Service capacity depends on the outlet limit and front shape. Regeneration must restore enough working capacity before the next bed switches into service.
