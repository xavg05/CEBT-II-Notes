# PDC-06: Thermocouple and heated-liquid dynamics

## Overview

Assumed: lumped heat capacity and Newton's heat-transfer law.

A temperature sensor and a flowing heated tank both behave as first-order lags, but their time constants have different physical origins. Sensor delay can conceal a process change from feedback.

## Intuition

A sensor must gain heat before it reports a hotter bath. Its thermal mass resists a quick change; heat transfer supplies the restoring effect. A flowing tank stores heat too, but replacement by incoming liquid provides its restoring effect in the ideal insulated model.

## Derivation

**Step 1: balance the sensor.** Let sensor mass be $m$, specific heat $c_p$, bath temperature $x$, sensor temperature $y$, heat-transfer coefficient $h$ and surface area $A_h$. Assume a uniform sensor temperature, negligible lead conduction, constant properties and a bath unaffected by the sensor:

$$mc_p\dot y=hA_h(x-y),\qquad
\tau_m\dot y+y=x,\quad \tau_m=\frac{mc_p}{hA_h}.\tag{16}$$

*Reason:* heat inflow is proportional to bath–sensor temperature difference. Thermal capacity divided by thermal conductance has units of time. Subtract the initial equilibrium and transform:

$$G_m(s)=\frac{\bar y}{\bar x}=\frac{1}{\tau_ms+1},\qquad p_m=-1/\tau_m.\tag{17}$$

*Reason:* zero initial deviation removes the transform's initial-condition term. The pole represents relaxation of sensor temperature to bath temperature.

**Step 2: balance heated liquid.** For fixed tank volume $V$, equal flow $q$, density $\rho$, liquid heat capacity $c_{pL}$, feed temperature $T_0$ and heating rate $Q$, assume perfect mixing, constant liquid properties, insulation, no reaction and negligible mixer work:

$$\rho Vc_{pL}\dot T=\rho qc_{pL}(T_0-T)+Q,
\qquad \tau\dot T+T=T_0+\frac{Q}{\rho qc_{pL}},\quad \tau=V/q.\tag{18}$$

*Reason:* liquid thermal storage opposes changes driven by feed and heater. For negligible pressure/volume-work effects, liquid internal-energy changes can be approximated by sensible enthalpy changes.

Subtract the steady balance and transform. Holding the other input unchanged gives

$$G_{T_0}(s)=\frac{\bar T}{\bar T_0}=\frac{1}{\tau s+1},\qquad
G_Q(s)=\frac{\bar T}{\bar Q}=\frac{1}{\rho qc_{pL}(\tau s+1)}.\tag{19}$$

*Reason:* both inputs act on the same stored energy and therefore share the same pole. Their gains differ because temperature and heating rate have different units.

In both models, normalising means dividing by the coefficient of the stored temperature, not by its derivative coefficient. For the sensor this is $hA_h$: at equilibrium $y=x$, so gain is one, and capacity $mc_p$ divided by conductance $hA_h$ gives the time constant. Increasing sensor mass slows it; increasing exposed area or heat transfer speeds it. The analogy with a mixing tank concerns this balance structure; heat transfer does not imply that sensor material is being replaced by flowing liquid.

For the heated tank, setting the derivative to zero gives $T=T_0+Q/(\rho qc_{pL})$. A one-kelvin feed change therefore produces a one-kelvin settled tank change, whereas a watt of heating produces $1/(\rho qc_{pL})$ kelvin. Both inputs share the same relaxation rate because there is only one stored tank temperature. They do not create two separate tank states.

## Motivation and explanation

The sensor model needs sufficiently rapid internal heat conduction, often assessed through a small Biot number. A thermowell, fouling or appreciable lead heat loss may add states or change the gain.

The heated-tank time constant equals residence time only under the stated assumptions. Heat loss to surroundings introduces another restoring term; changes in flow change both time constant and heater gain. A negative heater command is not physically available if the actuator only supplies heat.

### Driving a sensor with a changing temperature

In a tank–sensor chain, the tank temperature begins changing first and becomes the sensor's time-dependent input. The sensor's bath-step formula assumes its own input jumps to a constant value, so it cannot be applied directly to the gradually changing tank temperature. Solve the two balances together or multiply their zero-state transfer functions. A small sensor time constant can justify approximate tracking; otherwise measured temperature retains an additional memory of past tank temperatures.

## Link to other topics

Combining tank and sensor multiplies their transfer functions. This matters for feedback because the controller responds to the measured temperature rather than the true temperature.

## Conclusion

Thermal storage divided by a restoring conductance determines each lag. The source of that conductance decides whether its time constant is a heat-transfer time or a flow residence time.
