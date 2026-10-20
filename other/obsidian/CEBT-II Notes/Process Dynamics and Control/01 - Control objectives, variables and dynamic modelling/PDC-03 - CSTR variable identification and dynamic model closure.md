[Previous](<PDC-02 - Choosing variables and interpreting distillation loops.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<../02 - Physical balances and first-order dynamics/PDC-04 - Mixing tanks and reacting first-order lags.md>)

<!-- note-content:start -->
# PDC-03: CSTR variable identification and dynamic model closure

## Overview

Assumed: well-mixed reactor mass and energy balances.

For a jacketed CSTR carrying out $A\rightarrow B$, identify inputs, outputs and states before simplifying its balances. Measurements and manipulability are engineering choices, rather than intrinsic properties of a variable.

## Intuition

The reactor stores material and energy. Feed and coolant conditions drive its behaviour; concentration, temperature and volume describe its evolving contents. A product-flow valve is physically on an outlet line but may be treated as a model input because its position changes reactor accumulation.

## Derivation

**Step 1: label the equipment.** Let $q_0,q_1$ be feed/product volumetric flow rates, $c_{A0},c_{A1}$ their concentrations of A, $T_0,T_1$ their temperatures, $V$ reactor volume, $w_c$ coolant mass flow, and $T_{ci},T_{co}$ coolant inlet/outlet temperatures.

![Jacketed CSTR and its labelled streams](../figs/PDC-03-cooled-cstr.png)

**Step 2: state one plausible control assignment.** Let the upstream process determine $q_0,c_{A0},T_0$. Use product withdrawal to control volume and coolant flow to control reactor temperature.

| Variable | Model role under this assignment | Typical measurement and use |
|---|---|---|
| $q_0$ | Disturbance input | Flowmeter; monitor or use for compensation |
| $c_{A0}$ | Disturbance input | Online analyser or sampled analysis; may be unmeasured online |
| $T_0$ | Disturbance input | Temperature sensor |
| $q_1$ | Manipulated input | Flowmeter and product valve/pump |
| $c_{A1}$ | Output/state | Analyser or sampled analysis; possible quality target |
| $T_1$ | Controlled output/state | Temperature sensor; coolant-flow loop |
| $V$ | Controlled output/state | Level measurement with geometry conversion |
| $w_c$ | Manipulated input | Coolant flowmeter and valve |
| $T_{ci}$ | Disturbance input | Temperature sensor; utility condition |
| $T_{co}$ | Output of coolant subsystem | Temperature sensor; heat-duty monitoring |

*Reason:* disturbances enter from outside the selected authority, whereas actuators can be commanded. An input can be measured; an output can be unmeasured. If $q_1$ instead follows a gravity-outflow law, it becomes a dependent output and a different actuator must regulate volume.

**Step 3: write the balances.** For constant equal liquid densities, no volume change on mixing, and positive reaction-consumption rate $r(c_{A1},T_1)$ per reactor volume,

$$\dot V=q_0-q_1,\qquad
\frac{d(Vc_{A1})}{dt}=q_0c_{A0}-q_1c_{A1}-Vr.\tag{5}$$

*Reason:* use the extensive amount $Vc_{A1}$ while volume can change. Expand its derivative and substitute the volume balance:

$$V\dot c_{A1}=q_0(c_{A0}-c_{A1})-Vr.\tag{6}$$

*Reason:* well-mixed withdrawal removes solute and solvent proportionally, so its direct concentration contribution cancels.

For constant liquid properties, negligible pressure work and mixer heating, heat of reaction $\Delta H_r$ per mole reacted, and positive cooling duty $Q_c$,

$$\rho Vc_p\dot T_1=\rho q_0c_p(T_0-T_1)+(-\Delta H_r)Vr-Q_c.\tag{7}$$

*Reason:* the volume derivative cancels the outlet sensible-energy term in the same way. Exothermic reaction has $\Delta H_r<0$ and therefore adds heat. Close the model with a rate law, geometry, valve/flow relations and a heat-transfer model. For example, $Q_c=UA_h(T_1-T_c)$ uses heat-transfer coefficient $U$, area $A_h$ and a representative jacket temperature $T_c$; a dynamic jacket needs its own energy balance.

The outlet-flow cancellation is physical, not just convenient algebra. Removing a small portion of perfectly mixed liquid removes the same fraction of A as of total volume, leaving the remaining concentration unchanged at that instant. It still changes $V$, so subsequent feed dilution and reaction per stored amount can evolve differently. A concentration is a ratio; the amount balance and volume balance must agree before an equation for that ratio is trustworthy.

Model closure means being able to calculate every right-hand side from the current states and specified inputs. Knowing $V,c_{A1},T_1$ is insufficient if $r$ or $Q_c$ is still unknown. A rate law supplies $r$; a heat-transfer relation and, if needed, a jacket energy balance supply $Q_c$. Each additional stored quantity needs its own initial condition and balance.

## Motivation and explanation

Steady state sets all accumulation terms to zero. It does not remove the need for the rate and heat-transfer relations. A temperature-dependent rate can make concentration and temperature strongly coupled; assuming constant $k$ deliberately excludes that coupling.

The general control-volume energy balance stores internal energy and uses stream enthalpy, heat and work. If full chemical enthalpies include reaction energetics, do not also add a separate reaction-heat term. Here sensible energy and explicit $\Delta H_r$ are a consistent alternative.

## Link to other topics

Reactor modelling provides the balances; process control decides which inputs are available and which outputs matter. Transfer functions will describe the response of those outputs near an operating point.

## Conclusion

A useful model begins with a boundary, a variable assignment and enough constitutive relations to determine the states. The labels alone do not close the dynamics.
<!-- note-content:end -->

[Previous](<PDC-02 - Choosing variables and interpreting distillation loops.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<../02 - Physical balances and first-order dynamics/PDC-04 - Mixing tanks and reacting first-order lags.md>)
