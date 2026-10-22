# PDC-01: Control objectives, feedback and feedforward

## Overview

Assumed: steady material and energy balances.

Control keeps a process near a desired operating condition while its inputs change. A heated, well-mixed tank shows the difference between rejecting a disturbance and following a new target, and between correcting an observed error and anticipating its cause.

## Intuition

A steady design tells us how much heat is needed at one condition. It does not make that heat supply adjust when the feed becomes colder. Feedback watches the result; feedforward watches a disturbance and predicts the required correction.

The **controlled variable** is the quantity to regulate, the **manipulated variable** is an input we can adjust, and a **disturbance** is an input change outside this controller's authority. A **set point** is the desired controlled-variable value.

Follow a cold-feed disturbance through the tank. Colder liquid first reduces the energy arriving each second; stored energy then falls, so the tank cools. Feedback detects that temperature fall and raises heating. Feedforward measures the colder feed and raises heating before the tank needs to cool. This causal sequence explains why feedback needs a changed measurement and why feedforward needs a model of the disturbance's effect.

## Derivation

**Step 1: identify the physical balance.** Let liquid density be $\rho$, specific heat capacity $c_p$, tank volume $V$, equal inlet/outlet volumetric flow $q$, feed temperature $T_0$, tank/outlet temperature $T$, and heating rate $Q$. Assume perfect mixing, constant properties and volume, no reaction, heat loss or appreciable mixer work. Energy accumulation gives

$$\rho Vc_p\frac{dT}{dt}=\rho qc_p(T_0-T)+Q.\tag{1}$$

*Reason:* inflowing liquid brings sensible heat, the outlet carries heat at the tank temperature, and the heater adds energy. At steady target temperature $T_{sp}$, set the derivative to zero:

$$Q_s=\rho qc_p(T_{sp}-T_{0s}).\tag{2}$$

Here subscript $s$ denotes a steady operating value. This is the heat requirement, not a controller algorithm.

**Step 2: define feedback.** A sensor reports measured temperature $T_m$; the controller forms error $e=T_{sp}-T_m$ and commands the final control element, which changes $Q$. If $T_m$ is too low, more heating should raise $T$; if it is too high, heating should fall.

![Temperature feedback around a heated tank](../figs/PDC-01-heated-tank-feedback.png)

*Reason:* the measurement closes a path from process output back to process input. Sensor and actuator dynamics are part of that path.

**Step 3: define feedforward.** If $T_0$ is measured, an ideal heat command for this simplified tank is

$$Q_{ff}=\rho qc_p(T_{sp}-T_0).\tag{3}$$

*Reason:* replacing the unknown disturbance by its measured value cancels its contribution to the energy balance. With this exact model and instantaneous heating, $\rho Vc_p\dot T=\rho qc_p(T_{sp}-T)$, so a tank initially at the fixed target stays there.

## Motivation and explanation

**Regulator control** holds the target fixed while rejecting a disturbance. **Servo control** changes the output to follow a changed target. The same loop can perform both; they are different tests of its behaviour.

An on/off thermostat switches heating on below its switching range and off above it. Heat storage and switching can sustain a temperature cycle even with constant outside conditions; feedback alone does not guarantee a smooth response.

Feedback can respond to unmeasured disturbances but requires an error or measurement change before acting. Feedforward can act before an output error, but only for measured disturbances and only as well as the model and actuator permit. Combining them lets feedback correct residual modelling error.

Control objectives include safety constraints, operability and profitability. Inventory, pressure and temperature limits support operation; product quality and energy use support economics. Ordinary regulatory control is only one protective layer. Heater capacity, valve limits and process design constrain what any controller can achieve.

### Feedforward power and stored heat

For the heated-water balance, define heat-capacity flow $C_f=\rho qc_p$. Holding a fixed target requires $Q_s=C_f(T_{sp}-T_{0s})$, so an inlet-temperature change $\Delta T_0$ requires $\Delta Q=-C_f\Delta T_0$. The tank's stored heat determines how quickly an uncompensated error develops, but it does not change this final power requirement. A feedforward command can preserve an existing target if the measurement, model and heater are adequate; it cannot make stored liquid jump instantly to a new target.

## Link to other topics

The same accumulation balance will give the tank time constant. Feedback design then depends on the combined dynamics of tank, sensor and final control element.

## Conclusion

Choose the objective and available measurements before choosing a controller. A correct steady heat requirement is the starting point for a dynamic control model.
