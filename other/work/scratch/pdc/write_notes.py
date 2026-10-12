from pathlib import Path
import re,json
D=Path('other/work/drafts/Process Dynamics and Control');D.mkdir(parents=True,exist_ok=True)
notes=[]
def add(n,u,title,overview,intuition,derivation,explanation,example,link,conclusion):
 text=f'# PDC-{n:02d}: {title}\n\n'
 for heading,body in [('Overview',overview),('Intuition',intuition),('Derivation',derivation),('Motivation and explanation',explanation),('Worked example',example),('Link to other topics',link),('Conclusion',conclusion)]:
  if body:text+=f'## {heading}\n\n{body.strip()}\n\n'
 notes.append((n,u,title,text))
add(1,1,'Control objectives, feedback and feedforward',
r'''Assumed: steady material and energy balances.

Control keeps a process near a desired operating condition while its inputs change. A heated, well-mixed tank shows the difference between rejecting a disturbance and following a new target, and between correcting an observed error and anticipating its cause.''',
r'''A steady design tells us how much heat is needed at one condition. It does not make that heat supply adjust when the feed becomes colder. Feedback watches the result; feedforward watches a disturbance and predicts the required correction.

The **controlled variable** is the quantity to regulate, the **manipulated variable** is an input we can adjust, and a **disturbance** is an input change outside this controller's authority. A **set point** is the desired controlled-variable value.''',
r'''**Step 1: identify the physical balance.** Let liquid density be $\rho$, specific heat capacity $c_p$, tank volume $V$, equal inlet/outlet volumetric flow $q$, feed temperature $T_0$, tank/outlet temperature $T$, and heating rate $Q$. Assume perfect mixing, constant properties and volume, no reaction, heat loss or appreciable mixer work. Energy accumulation gives

$$\rho Vc_p\frac{dT}{dt}=\rho qc_p(T_0-T)+Q.\tag{AUTO}$$

*Reason:* inflowing liquid brings sensible heat, the outlet carries heat at the tank temperature, and the heater adds energy. At steady target temperature $T_{sp}$, set the derivative to zero:

$$Q_s=\rho qc_p(T_{sp}-T_{0s}).\tag{AUTO}$$

Here subscript $s$ denotes a steady operating value. This is the heat requirement, not a controller algorithm.

**Step 2: define feedback.** A sensor reports measured temperature $T_m$; the controller forms error $e=T_{sp}-T_m$ and commands the final control element, which changes $Q$. If $T_m$ is too low, more heating should raise $T$; if it is too high, heating should fall.

![Temperature feedback around a heated tank](../figs/PDC-01-heated-tank-feedback.png)

*Reason:* the measurement closes a path from process output back to process input. Sensor and actuator dynamics are part of that path.

**Step 3: define feedforward.** If $T_0$ is measured, an ideal heat command for this simplified tank is

$$Q_{ff}=\rho qc_p(T_{sp}-T_0).\tag{AUTO}$$

*Reason:* replacing the unknown disturbance by its measured value cancels its contribution to the energy balance. With this exact model and instantaneous heating, $\rho Vc_p\dot T=\rho qc_p(T_{sp}-T)$, so a tank initially at the fixed target stays there.''',
r'''**Regulator control** holds the target fixed while rejecting a disturbance. **Servo control** changes the output to follow a changed target. The same loop can perform both; they are different tests of its behaviour.

An on/off thermostat switches heating on below its switching range and off above it. Heat storage and switching can sustain a temperature cycle even with constant outside conditions; feedback alone does not guarantee a smooth response.

Feedback can respond to unmeasured disturbances but requires an error or measurement change before acting. Feedforward can act before an output error, but only for measured disturbances and only as well as the model and actuator permit. Combining them lets feedback correct residual modelling error.

Control objectives include safety constraints, operability and profitability. Inventory, pressure and temperature limits support operation; product quality and energy use support economics. Ordinary regulatory control is only one protective layer. Heater capacity, valve limits and process design constrain what any controller can achieve.''',
r'''Take water with $\rho=1000$ kg m$^{-3}$, $c_p=4200$ J kg$^{-1}$ K$^{-1}$ and $q=0.010$ m$^3$ s$^{-1}$. Holding $T_{sp}=50$ °C with $T_{0s}=20$ °C requires $Q_s=1.260$ MW. If the inlet falls to $15$ °C, the model requires $1.470$ MW, an increase of $0.210$ MW.

A regulator makes that correction while keeping the target at $50$ °C. A servo instead reacts to an operator changing the target. A real feedforward command would also need accurate flow and properties, sufficient heat capacity and allowance for sensor/actuator delay.''',
'The same accumulation balance will give the tank time constant. Feedback design then depends on the combined dynamics of tank, sensor and final control element.',
'Choose the objective and available measurements before choosing a controller. A correct steady heat requirement is the starting point for a dynamic control model.')
add(2,1,'Choosing variables and interpreting distillation loops',
r'''Assumed: distillation equipment and the roles of reflux, reboiling and condensation.

Control-variable labels depend on the chosen process boundary and available actuators. A distillation column makes this concrete: pressure and inventories must be maintained while product compositions are regulated.''',
r'''A vessel level is an inventory signal: it tells us whether material is accumulating. A tray temperature can be a composition signal: at a known pressure and suitable mixture conditions, a changed composition changes the boiling temperature. These measurements solve different problems even though their loops interact.''',
r'''**Step 1: specify boundaries.** Include the column, condenser, reflux drum and reboiler in the process boundary. The feed is an external input; reflux is an internal circulation but remains an actuator-driven input to the column subsystem.

**Step 2: connect inventory to a balance.** If $M_D$ is drum liquid mass and $\dot m_C$, $\dot m_R$, $\dot m_D$ are condensate, reflux and distillate mass flow rates, then

$$\frac{dM_D}{dt}=\dot m_C-\dot m_R-\dot m_D.\tag{AUTO}$$

*Reason:* drum level can remain steady only when inflow matches the two outflows. Adjusting distillate flow changes accumulation directly. An analogous base balance connects bottom level to bottoms withdrawal.

**Step 3: read the five loops.** PC, LC and TC mean pressure, level and temperature controller. Dotted lines carry measurement/control information; solid lines carry material.

![Five-loop distillation control arrangement](../figs/PDC-02-distillation-loops.png)

| Controlled measurement | Manipulated input in this arrangement | Physical reason |
|---|---|---|
| Column overhead pressure | Condenser coolant flow | Heat removal changes condensation and vapour inventory |
| Reflux-drum level | Distillate withdrawal | Removes accumulated condensate |
| Upper-column temperature | Reflux flow | Changes internal liquid flow and upper separation |
| Lower-column temperature | Reboiler steam flow | Changes boil-up and lower separation |
| Column-base level | Bottoms withdrawal | Removes accumulated bottom liquid |

*Reason:* each information path terminates at a valve that can influence its measurement. This is one possible pairing, not a universal rule.''',
r'''The desired variables may be top and bottom composition, while the measured variables are tray temperatures. Temperature is an **inferential measurement** of composition; it must be justified for the mixture and pressure. Pressure changes, multicomponent feeds or weak temperature sensitivity can undermine the inference.

Feed flow, composition and temperature often act as disturbances because an upstream unit determines them. They become manipulated variables only if this controller is allowed to adjust them. Reflux changes both inventories and separation, and steam changes several tray conditions: five loops do not imply five independent processes.''',
r'''Suppose the reflux-drum level rises while its set point is unchanged. Increasing distillate withdrawal makes the right side of the drum balance smaller, opposing accumulation. Reducing reflux could also lower the level, but would disturb upper-column separation; the pairing above reserves reflux for the temperature loop.

If pressure rises, the pressure loop can increase condenser cooling within its available range. A temperature loop should not interpret every simultaneous temperature change as composition error: boiling temperature also depends on pressure.''',
'Phase equilibrium explains why pressure and composition affect tray temperature. Dynamic inventory balances explain why level loops are essential even when product specifications are the main economic objective.',
'A control structure is a set of physically justified measurement–actuator pairings. Its adequacy depends on interactions and dynamics as well as steady separation performance.')
add(3,1,'CSTR variable identification and dynamic model closure',
r'''Assumed: well-mixed reactor mass and energy balances.

For a jacketed CSTR carrying out $A\rightarrow B$, identify inputs, outputs and states before simplifying its balances. Measurements and manipulability are engineering choices, rather than intrinsic properties of a variable.''',
r'''The reactor stores material and energy. Feed and coolant conditions drive its behaviour; concentration, temperature and volume describe its evolving contents. A product-flow valve is physically on an outlet line but may be treated as a model input because its position changes reactor accumulation.''',
r'''**Step 1: label the equipment.** Let $q_0,q_1$ be feed/product volumetric flow rates, $c_{A0},c_{A1}$ their concentrations of A, $T_0,T_1$ their temperatures, $V$ reactor volume, $w_c$ coolant mass flow, and $T_{ci},T_{co}$ coolant inlet/outlet temperatures.

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
\frac{d(Vc_{A1})}{dt}=q_0c_{A0}-q_1c_{A1}-Vr.\tag{AUTO}$$

*Reason:* use the extensive amount $Vc_{A1}$ while volume can change. Expand its derivative and substitute the volume balance:

$$V\dot c_{A1}=q_0(c_{A0}-c_{A1})-Vr.\tag{AUTO}$$

*Reason:* well-mixed withdrawal removes solute and solvent proportionally, so its direct concentration contribution cancels.

For constant liquid properties, negligible pressure work and mixer heating, heat of reaction $\Delta H_r$ per mole reacted, and positive cooling duty $Q_c$,

$$\rho Vc_p\dot T_1=\rho q_0c_p(T_0-T_1)+(-\Delta H_r)Vr-Q_c.\tag{AUTO}$$

*Reason:* the volume derivative cancels the outlet sensible-energy term in the same way. Exothermic reaction has $\Delta H_r<0$ and therefore adds heat. Close the model with a rate law, geometry, valve/flow relations and a heat-transfer model. For example, $Q_c=UA_h(T_1-T_c)$ uses heat-transfer coefficient $U$, area $A_h$ and a representative jacket temperature $T_c$; a dynamic jacket needs its own energy balance.''',
r'''Steady state sets all accumulation terms to zero. It does not remove the need for the rate and heat-transfer relations. A temperature-dependent rate can make concentration and temperature strongly coupled; assuming constant $k$ deliberately excludes that coupling.

The general control-volume energy balance stores internal energy and uses stream enthalpy, heat and work. If full chemical enthalpies include reaction energetics, do not also add a separate reaction-heat term. Here sensible energy and explicit $\Delta H_r$ are a consistent alternative.''',
r'''A colder coolant inlet is a disturbance even when it is measured. It changes heat removal, which changes $T_1$, which may change reaction rate and $c_{A1}$. A coolant-flow adjustment is a manipulated input because the valve can be commanded.

To close a model of $T_{co}$, one cannot merely list that temperature as an independent input. Either apply a quasi-steady coolant balance $Q_c=w_cc_{pc}(T_{co}-T_{ci})$, with coolant heat capacity $c_{pc}$, or include jacket storage and its temperature distribution.''',
'Reactor modelling provides the balances; process control decides which inputs are available and which outputs matter. Transfer functions will describe the response of those outputs near an operating point.',
'A useful model begins with a boundary, a variable assignment and enough constitutive relations to determine the states. The labels alone do not close the dynamics.')
add(4,2,'Mixing tanks and reacting first-order lags',
r'''Assumed: an isothermal CSTR balance and first-order reaction kinetics.

A well-mixed tank converts inlet-composition changes into a first-order lag. Adding reaction changes both the steady gain and the time constant; the hydrodynamic residence time remains $V/q$.''',
r'''Mixing spreads the arrival of new feed through existing contents. A change is felt immediately, but the old contents are only gradually displaced. Reaction removes A as well as flow removing it, so a concentration deviation disappears faster and a feed increase produces a smaller final concentration increase.''',
r'''**Step 1: balance inert solute.** With fixed volume $V$, flow $q$, inlet concentration $c_0$ and uniform tank/outlet concentration $c$, assume constant density, no reaction and perfect mixing:

$$V\dot c=q(c_0-c),\qquad \tau\dot c+c=c_0,\quad \tau=V/q.\tag{AUTO}$$

*Reason:* divide the accumulation balance by $q$ to expose the residence time $\tau$.

**Step 2: solve a feed step.** Initially $c=c_s=c_{0s}$. For $t\geq0$, the inlet changes permanently by $\Delta c_0$. Set $c'=c-c_s$; then $\tau\dot c'+c'=\Delta c_0$ with $c'(0)=0$. Multiply by integrating factor $e^{t/\tau}$:

$$\frac{d}{dt}(e^{t/\tau}c')=\frac{\Delta c_0}{\tau}e^{t/\tau}.
$$

*Reason:* the product derivative collects the derivative and concentration terms. Integration from zero to $t$ gives $e^{t/\tau}c'=\Delta c_0(e^{t/\tau}-1)$, hence

$$c'=\Delta c_0(1-e^{-t/\tau}).\tag{AUTO}$$

**Step 3: include first-order consumption.** For constant rate constant $k>0$, add loss $kVc$:

$$V\dot c=q(c_0-c)-kVc,
\qquad \frac{\tau}{1+k\tau}\dot c+c=\frac{c_0}{1+k\tau}.\tag{AUTO}$$

*Reason:* collect both removal mechanisms and divide by their combined coefficient. Thus the effective time constant is $\tau_r=\tau/(1+k\tau)$ and concentration gain is $K_p=1/(1+k\tau)$.

**Step 4: transform the perturbation balance.** Define $\bar c=\mathcal L[c']$ and $\bar c_0=\mathcal L[c_0']$, where primes mean deviations from the reacting steady state. With zero initial deviation,

$$\frac{\bar c}{\bar c_0}=\frac{1}{\tau s+1+k\tau}
=\frac{K_p}{\tau_rs+1},\qquad p=-\frac{1+k\tau}{\tau}.\tag{AUTO}$$

*Reason:* the Laplace transform replaces $\dot c'$ by $s\bar c$. The pole $p$ gives the exponential decay rate.''',
r'''The inert tank has unit concentration gain and pole $-1/\tau$. Reaction moves the pole farther left and reduces the gain. A faster response therefore does not imply more reactant survives. Taking $k\rightarrow0$ recovers the inert-tank model.

These conclusions require constant $q,V,k$ and negligible thermal coupling. Changing temperature or flow generally changes the coefficients; second-order kinetics requires local linearisation.''',
r'''Let $V=2.00$ m$^3$, $q=0.0200$ m$^3$ s$^{-1}$, so $\tau=100$ s. A feed step of $3.00$ mol m$^{-3}$ gives inert-tank deviation $c'(100)=1.89636$ mol m$^{-3}$ and final deviation $3.00$ mol m$^{-3}$.

With $k=0.0100$ s$^{-1}$, $K_p=0.500$, $\tau_r=50.0$ s and $p=-0.0200$ s$^{-1}$. The same feed step gives final deviation $1.50$ mol m$^{-3}$ and $c'(50)=0.948181$ mol m$^{-3}$.''',
'The inert-tank impulse response also describes a CSTR residence-time distribution. The same first-order structure occurs when heat transfer relaxes a sensor toward the bath temperature.',
'Flow and reaction determine the coefficient of concentration removal. That coefficient controls both the pole and the steady response to feed composition.')
add(5,2,'Variable-volume tanks and finite pulse balances',
r'''Assumed: perfect mixing and the product rule.

When tank volume changes, balance the stored amount $Vc$, not concentration alone. A finite-volume pulse is handled by a jump balance before resuming continuous dynamics.''',
r'''Removing well-mixed liquid lowers the amount of solute but does not instantly change its concentration. Adding feed changes both solute amount and liquid volume. Forgetting the volume derivative makes these two actions look incorrectly equivalent.''',
r'''**Step 1: track volume and solute.** For inlet flow $q_0$, outlet flow $q$, inlet concentration $c_0$, tank concentration $c$ and first-order consumption constant $k$, assume constant density and additive volumes:

$$\dot V=q_0-q,\qquad
\frac{d(Vc)}{dt}=q_0c_0-qc-kVc.\tag{AUTO}$$

*Reason:* storage is an extensive amount. Expanding gives $V\dot c+c\dot V=q_0c_0-qc-kVc$; substitute $\dot V=q_0-q$ and cancel $-qc$:

$$V\dot c=q_0(c_0-c)-kVc.\tag{AUTO}$$

*Reason:* withdrawal leaves the concentration of remaining well-mixed liquid unchanged directly. It still affects later concentration dynamics through $V(t)$.

**Step 2: determine the volume history.** For specified flows,

$$V(t)=V(0)+\int_0^t[q_0(\theta)-q(\theta)]\,d\theta.\tag{AUTO}$$

*Reason:* integrate the volume balance first, then use the resulting $V$ in the concentration ODE. For general time-dependent $V$, this is not a constant-coefficient transfer-function model. If $q_0=0$ and $k=0$, the equation gives $\dot c=0$ even during withdrawal.

**Step 3: cross a short, finite-volume addition.** A pulse adds volume $V_p$ at concentration $c_p$. Let $(V_-,c_-)$ and $(V_+,c_+)$ denote values immediately before and after it. Neglect reaction and ordinary flow during the short addition:

$$V_+=V_-+V_p,\qquad
V_+c_+=V_-c_-+V_pc_p,
\qquad c_+=\frac{V_-c_-+V_pc_p}{V_-+V_p}.\tag{AUTO}$$

*Reason:* total volume and solute are conserved across the jump. Use $(V_+,c_+)$ as initial conditions for the subsequent ODE.''',
r'''A Dirac impulse idealises an input with finite area and negligible duration. A finite-volume addition also changes the model's holdup; it is not automatically the same experiment as an impulse in feed concentration at fixed volume.

The model stops being valid if the tank drains, overflows, mixes poorly or has appreciable volume change on mixing. A pulse too long to neglect reaction or outlet flow must be integrated with those effects.''',
r'''A tank initially contains $V_-=1.00$ m$^3$ at $c_-=2.00$ mol m$^{-3}$. Add $V_p=0.100$ m$^3$ at $c_p=10.0$ mol m$^{-3}$. The jump balances give $V_+=1.100$ m$^3$ and $c_+=2.72727$ mol m$^{-3}$.

Treating the addition as extra solute at unchanged volume would overpredict concentration. If the addition instead displaces liquid to keep volume constant, the overflow must appear in the pulse balance.''',
'Tank-level control also begins with the volume balance. Linearising flow and concentration products later allows a local transfer-function model around a constant-volume operating point.',
'Use amount balances through volume changes and jump balances through short additions. The resulting state then determines the next continuous response.')
add(6,2,'Thermocouple and heated-liquid dynamics',
r'''Assumed: lumped heat capacity and Newton's heat-transfer law.

A temperature sensor and a flowing heated tank both behave as first-order lags, but their time constants have different physical origins. Sensor delay can conceal a process change from feedback.''',
r'''A sensor must gain heat before it reports a hotter bath. Its thermal mass resists a quick change; heat transfer supplies the restoring effect. A flowing tank stores heat too, but replacement by incoming liquid provides its restoring effect in the ideal insulated model.''',
r'''**Step 1: balance the sensor.** Let sensor mass be $m$, specific heat $c_p$, bath temperature $x$, sensor temperature $y$, heat-transfer coefficient $h$ and surface area $A_h$. Assume a uniform sensor temperature, negligible lead conduction, constant properties and a bath unaffected by the sensor:

$$mc_p\dot y=hA_h(x-y),\qquad
\tau_m\dot y+y=x,\quad \tau_m=\frac{mc_p}{hA_h}.\tag{AUTO}$$

*Reason:* heat inflow is proportional to bath–sensor temperature difference. Thermal capacity divided by thermal conductance has units of time. Subtract the initial equilibrium and transform:

$$G_m(s)=\frac{\bar y}{\bar x}=\frac{1}{\tau_ms+1},\qquad p_m=-1/\tau_m.\tag{AUTO}$$

*Reason:* zero initial deviation removes the transform's initial-condition term. The pole represents relaxation of sensor temperature to bath temperature.

**Step 2: balance heated liquid.** For fixed tank volume $V$, equal flow $q$, density $\rho$, liquid heat capacity $c_{pL}$, feed temperature $T_0$ and heating rate $Q$, assume perfect mixing, constant liquid properties, insulation, no reaction and negligible mixer work:

$$\rho Vc_{pL}\dot T=\rho qc_{pL}(T_0-T)+Q,
\qquad \tau\dot T+T=T_0+\frac{Q}{\rho qc_{pL}},\quad \tau=V/q.\tag{AUTO}$$

*Reason:* liquid thermal storage opposes changes driven by feed and heater. For negligible pressure/volume-work effects, liquid internal-energy changes can be approximated by sensible enthalpy changes.

Subtract the steady balance and transform. Holding the other input unchanged gives

$$G_{T_0}(s)=\frac{\bar T}{\bar T_0}=\frac{1}{\tau s+1},\qquad
G_Q(s)=\frac{\bar T}{\bar Q}=\frac{1}{\rho qc_{pL}(\tau s+1)}.\tag{AUTO}$$

*Reason:* both inputs act on the same stored energy and therefore share the same pole. Their gains differ because temperature and heating rate have different units.''',
r'''The sensor model needs sufficiently rapid internal heat conduction, often assessed through a small Biot number. A thermowell, fouling or appreciable lead heat loss may add states or change the gain.

The heated-tank time constant equals residence time only under the stated assumptions. Heat loss to surroundings introduces another restoring term; changes in flow change both time constant and heater gain. A negative heater command is not physically available if the actuator only supplies heat.''',
r'''For a sensor with $m=0.00200$ kg, $c_p=500$ J kg$^{-1}$ K$^{-1}$, $h=200$ W m$^{-2}$ K$^{-1}$ and $A_h=5.00\times10^{-4}$ m$^2$, $\tau_m=10.0$ s. Following a bath step from $20$ to $60$ °C, the sensor reads $45.2848$ °C after $10.0$ s.

For a $1.00$ m$^3$ water tank at $q=0.0100$ m$^3$ s$^{-1}$, $\tau=100$ s. With $\rho=1000$ kg m$^{-3}$ and $c_{pL}=4200$ J kg$^{-1}$ K$^{-1}$, a $0.420$ MW heating increase gives a final $10.0$ K rise and a $6.32121$ K rise after $100$ s. A sensor lag would delay the measured response further.''',
'Combining tank and sensor multiplies their transfer functions. This matters for feedback because the controller responds to the measured temperature rather than the true temperature.',
'Thermal storage divided by a restoring conductance determines each lag. The source of that conductance decides whether its time constant is a heat-transfer time or a flow residence time.')
add(7,2,'Adiabatic discharge of a gas vessel',
r'''Assumed: ideal-gas properties and the open-system first law.

An insulated gas vessel cools as it discharges. The energy carried away is stream enthalpy, while the energy stored is internal energy; their difference is essential to predicting temperature and pressure.''',
r'''Insulation prevents heat exchange through the wall. It does not prevent energy loss through the outlet. The departing gas carries its internal energy plus flow work, so the remaining gas cools.''',
r'''**Step 1: balance mass and energy.** Let vessel volume $V$ be fixed, stored gas mass $m$, outlet mass flow $w>0$, uniform temperature $T$ and pressure $p$. Assume well-mixed ideal gas with constant specific heats $c_v,c_p$, no inflow, wall heat storage, heat transfer or shaft work, and negligible outlet kinetic/potential energy. With $U=mc_vT$ and outlet specific enthalpy $\hat H=c_pT$,

$$\dot m=-w,\qquad
\frac{d(mc_vT)}{dt}=-wc_pT.\tag{AUTO}$$

*Reason:* a fixed control volume stores internal energy but stream enthalpy includes flow work at its boundary.

**Step 2: eliminate time.** Divide the energy balance by $c_v$ and use $\gamma=c_p/c_v$ and $\dot m=-w$:

$$\frac{d(mT)}{dm}=\gamma T
\quad\Rightarrow\quad T+m\frac{dT}{dm}=\gamma T
\quad\Rightarrow\quad \frac{dT}{T}=(\gamma-1)\frac{dm}{m}.\tag{AUTO}$$

*Reason:* the same mass loss drives both equations, so their ratio removes the unknown discharge-flow law. Integrate from initial $(m_0,T_0)$:

$$\frac{T}{T_0}=\left(\frac{m}{m_0}\right)^{\gamma-1}.\tag{AUTO}$$

**Step 3: obtain pressure.** With mass-specific gas constant $R=c_p-c_v$, $pV=mRT$. Divide by its initial value:

$$\frac{p}{p_0}=\left(\frac{m}{m_0}\right)^\gamma,
\qquad \frac{T}{T_0}=\left(\frac{p}{p_0}\right)^{(\gamma-1)/\gamma}.\tag{AUTO}$$

*Reason:* fixed volume makes pressure proportional to $mT$. The result relates states along discharge, not yet to time.

**Step 4: check energy reference invariance.** Let specific internal energy instead be $\hat U=c_vT+C$, where $C$ is a constant offset. Consistency requires $\hat H=\hat U+p/\rho=c_pT+C$. Then

$$c_v\frac{d(mT)}{dt}+C\dot m=-w(c_pT+C).
$$

*Reason:* substitute $\dot m=-w$ and the two $-wC$ terms cancel. A changed reference cannot change the temperature prediction. Choosing unrelated enthalpy and internal-energy offsets breaks $\hat H-\hat U=RT$.''',
r'''All temperatures in the ideal-gas and power-law relations are absolute. The relations do not provide $m(t)$ without an outlet-flow model. Constant prescribed $w$ gives $m=m_0-wt$ only while gas remains and the prescription is physically sustainable.

The lumped vessel model can fail during rapid discharge with spatial gradients or appreciable wall heat transfer. A nozzle's downstream static temperature need not equal vessel temperature; the outlet enthalpy/kinetic-energy accounting must match the chosen boundary.''',
r'''For $T_0=300$ K and $\gamma=1.40$, discharging until $m/m_0=0.500$ gives $T=227.357$ K and $p/p_0=0.378929$. Pressure falls faster than mass because the remaining gas also cools.

Replacing outlet enthalpy by $c_vT$ would predict constant vessel temperature under this model, which omits the outlet flow-work contribution.''',
'The boiler model also distinguishes stored internal energy from stream enthalpy. Thermodynamic reference conventions must remain consistent whenever changing mass multiplies an energy datum.',
'Insulated open-system discharge is not isothermal. A consistent mass–energy balance gives cooling and pressure decline before any particular discharge-valve law is chosen.')
add(8,3,'Deviation variables and transfer-function assumptions',
r'''Assumed: basic Laplace-transform rules.

A transfer function describes the forced response of a linear, time-invariant system with zero initial state deviations. Subtracting a steady operating point allows a physically nonzero concentration or temperature to have zero deviation.''',
r'''The baseline is not the disturbance. A tank at a steady concentration already contains material; control asks how much its concentration changes when an input changes. Deviation variables remove the baseline while retaining exactly the perturbation we care about.''',
r'''**Step 1: subtract the steady state.** For an inert mixed tank, $\tau\dot c+c=c_0$. At equilibrium $c_s=c_{0s}$. Define $c'=c-c_s$ and $c_0'=c_0-c_{0s}$. Substitution gives

$$\tau\dot c'+c_s+c'=c_{0s}+c_0'
\quad\Rightarrow\quad\tau\dot c'+c'=c_0'.\tag{AUTO}$$

*Reason:* the steady values satisfy the original balance and cancel. A prime denotes deviation; a dot denotes time differentiation. They are different operations.

**Step 2: transform with the initial condition retained.** For any deviation output $y'$, write

$$\bar y(s)=\mathcal L[y']=\int_0^\infty y'(t)e^{-st}\,dt,
\qquad \mathcal L[\dot y']=s\bar y-y'(0^-).\tag{AUTO}$$

*Reason:* integration by parts produces the initial-value term. The Laplace variable $s$ has inverse-time units. Transformed variables generally have their original units multiplied by time.

For $\tau\dot y'+y'=K_px'$,

$$\bar y=\frac{K_p}{\tau s+1}\bar x+
\frac{\tau y'(0^-)}{\tau s+1}.\tag{AUTO}$$

*Reason:* collect $\bar y$ and isolate it. The first term is the input-driven response; the second is the free response to stored initial deviation. Set all initial state deviations to zero to define

$$G(s)=\left.\frac{\bar y}{\bar x}\right|_{\text{zero initial state deviations}}
=\frac{K_p}{\tau s+1}.\tag{AUTO}$$

**Step 3: state the scope.** Constant coefficients and superposition define the linear, time-invariant model used here. A SISO transfer function relates one input–output pair. With multiple inputs, hold the other deviations at zero when defining each transfer-matrix element.

*Reason:* a raw ratio of output to one input with other inputs or initial-state effects present does not isolate that pair's dynamics.''',
r'''Subtraction gives zero initial deviations only when the process actually starts at the chosen equilibrium. If it starts elsewhere, include the free-response term. For a second-order ODE, both output and derivative initial conditions matter.

Zero initial state does not require a step input to have zero value or derivative immediately after $t=0$. A step deliberately jumps. Taking $t=0$ at the disturbance is a convenient origin, not a special physical assumption. A nonlinear model only gains a local transfer function after linearisation.''',
r'''An inert tank initially has $c_s=c_{0s}=5.00$ kmol m$^{-3}$. Its feed steps to $8.00$ kmol m$^{-3}$. The transformed input deviation is $\bar c_0=3.00/s$, not $8.00/s$, and the initial output deviation is zero.

For $\tau=100$ s,

$$\bar c=\frac{3.00}{s(100s+1)},\qquad
c(t)=5.00+3.00(1-e^{-t/100}).
$$

The absolute concentration after $100$ s is $6.89636$ kmol m$^{-3}$. The same transfer function would apply around any inert-tank baseline at unchanged flow and volume.''',
'Deviation variables support both first-order response analysis and Taylor linearisation. A pole belongs to the process transfer function; additional factors in an input transform belong to the imposed signal.',
'A transfer function separates process dynamics from baseline, initial conditions and input waveform. Preserve that distinction when interpreting its poles and gain.')
add(9,3,'First-order step and impulse responses',
r'''Assumed: the transfer function of a self-regulating mixed or thermal tank.

For $G(s)=K_p/(\tau s+1)$ with $\tau>0$, gain sets the final response and time constant sets the speed. Step and impulse experiments expose different features of the same stored-state dynamics.''',
r'''A persistent step keeps supplying a new condition until the tank settles. A brief pulse supplies a finite perturbation and then leaves the tank to relax. The response to the pulse therefore decays, while the step response accumulates that decaying response.''',
r'''**Step 1: apply a step.** Let $H(t)$ be the unit Heaviside step and $x'=\Delta x H(t)$. For zero initial state, $\bar x=\Delta x/s$, so

$$\bar y=\frac{K_p\Delta x}{s(\tau s+1)}
=K_p\Delta x\left[\frac1s-\frac{1}{s+1/\tau}\right].\tag{AUTO}$$

*Reason:* multiply the proposed partial fractions by $s(\tau s+1)$ to check that their numerator is one. Invert each term:

$$y'(t)=K_p\Delta x(1-e^{-t/\tau}),\quad
\dot y'(t)=\frac{K_p\Delta x}{\tau}e^{-t/\tau}.\tag{AUTO}$$

*Reason:* the pole $-1/\tau$ generates a decaying exponential; the input's $1/s$ generates the constant final term.

**Step 2: interpret the time constant.** At $t=\tau$, the normalised response is $1-e^{-1}$. The initial tangent is $y'\approx (K_p\Delta x/\tau)t$, which meets the final response at $t=\tau$. To reach fraction $f$ of the final change, solve $f=1-e^{-t/\tau}$:

$$t_f=-\tau\ln(1-f),\qquad 0<f<1.\tag{AUTO}$$

*Reason:* the remaining distance is an exponentially decaying fraction.

**Step 3: apply an impulse.** Let $\delta(t)$ be a unit-area Dirac impulse, with $\mathcal L[\delta]=1$. It is a distribution, not an ordinary finite-height signal. For impulse area $I_x$, $x'=I_x\delta(t)$ and

$$\bar y=I_xG(s),\qquad
 y'(t)=\frac{K_pI_x}{\tau}e^{-t/\tau}\quad(t\geq0).\tag{AUTO}$$

*Reason:* invert the single first-order pole. Since $\delta$ has inverse-time units, $I_x$ has input units times time. Integrating the ODE across the impulse gives $\tau[y'(0^+)-y'(0^-)]=K_pI_x$, confirming the output jump.''',
r'''A lag begins responding immediately; its delayed approach is not dead time. Negative $K_p$ reverses the response direction but does not change stability when $\tau>0$. Comparing the magnitude of gain with one makes sense only after accounting for units or using a consistent scaling.

The unit-step derivative is the unit-impulse response for this zero-state LTI system. Its impulse-response area is $K_p$. Real pulses approximate the impulse only when their duration is short relative to the dynamics and they do not appreciably change the process parameters.''',
r'''With $K_p=2.00$, $\tau=20.0$ s and step $\Delta x=3.00$ in input units, the final output change is $6.00$ and $y'(20)=3.79272$ in output units. For a unit-area input pulse, $y'(20)=0.0367879$ in the corresponding output units.

A first-order response reaches $63.2121\%$ of its final change at one time constant, $95.0213\%$ at three and $99.3262\%$ at five. For $\tau=100$ s, the exact time to $95\%$ is $299.573$ s.''',
'An integrator responds to a step with continuing accumulation instead of settling. Cascading several lags changes the early response and creates higher-order dynamics.',
'The step measures steady sensitivity and relaxation speed; the impulse isolates the decaying response to a finite input area.')
add(10,3,'Integrators and transport dead time',
r'''Assumed: volume balances and the time-shift rule for Laplace transforms.

Two elementary process elements behave very differently from a self-regulating lag. An integrator stores a persistent imbalance; ideal transport dead time shifts a signal without smoothing it.''',
r'''A tank with a fixed pumped outlet cannot increase outflow automatically when its level rises. Extra inflow keeps accumulating. A plug-flow pipe instead carries a temperature front downstream: nothing arrives until its transit time has elapsed, then the same front appears.''',
r'''**Step 1: derive the integrator from level.** For a tank of constant cross-sectional area $A$, level $h$, inlet $q_0$ and prescribed pumped outlet $q$, assume both flows are independent of $h$:

$$A\dot h=q_0-q,\qquad
A\dot h'=q_0'-q',\qquad
\bar h=\frac{1}{As}(\bar q_0-\bar q).\tag{AUTO}$$

*Reason:* volume is $Ah$; subtract the balanced baseline and transform with zero initial level deviation. With net-flow deviation $x'=q_0'-q'$, the transfer function is $1/(As)$, with pole at zero. A constant imbalance $\Delta q$ gives $h'=\Delta q\,t/A$; an impulse of net volume $I_V$ gives a persistent level jump $I_V/A$.

A scaled form is $T_H\dot y'=x'$ and $G=1/(T_Hs)$. Here $T_H$ is a holdup time when $x',y'$ are defined with compatible normalised units; $A$ in the dimensional level equation is an area, not a time.

**Step 2: derive transport delay.** For pipe length $L$, uniform constant velocity $u$, negligible axial mixing and heat exchange, a fluid element takes $t_d=L/u$ to reach the outlet. With inlet temperature deviation $x'$ and outlet $y'$, zero deviation history before the disturbance gives

$$y'(t)=\begin{cases}0,&t<t_d,\\x'(t-t_d),&t\geq t_d.\end{cases}\tag{AUTO}$$

*Reason:* each outlet parcel carries its inlet condition from one transit time earlier. Substitute $\theta=t-t_d$ into the transform:

$$\bar y=\int_{t_d}^{\infty}x'(t-t_d)e^{-st}\,dt
=e^{-st_d}\int_0^{\infty}x'(\theta)e^{-s\theta}\,d\theta,
\qquad G_d(s)=e^{-st_d}.\tag{AUTO}$$

*Reason:* the exponential factor accounts for the time shift and does not change the signal's eventual amplitude.''',
r'''The integrator is not bounded-input bounded-output (BIBO) stable: a bounded nonzero constant input creates an unbounded ramp. Its zero-input level deviation remains constant, so it is neutrally stable in that state sense rather than an exponentially growing mode. It is not asymptotically stable or self-regulating. Real level is bounded by emptying or overflowing, where the ideal model stops applying.

A pure delay is BIBO stable and has unit steady gain. It is not a finite-order rational transfer function. A first-order lag begins changing immediately; a pure delay waits and then reproduces the input. Axial dispersion, wall heat exchange or velocity variation makes a real pipe more than a pure delay.''',
r'''For $A=2.00$ m$^2$ and persistent net inflow $0.00200$ m$^3$ s$^{-1}$, level rises at $0.00100$ m s$^{-1}$ and increases by $0.0600$ m in $60.0$ s.

For a $20.0$ m pipe of diameter $0.0400$ m carrying $0.00100$ m$^3$ s$^{-1}$, cross-sectional velocity is $0.795775$ m s$^{-1}$ and transit time is $25.1327$ s. An ideal inlet temperature step reaches the outlet after that time with its original amplitude.''',
'A gravity-draining tank introduces a level-dependent outflow and can become self-regulating. Transport delay matters in controller design because measurements may describe a condition created well before the current actuator command.',
'A pole at zero represents accumulation without restoring action. The exponential delay factor represents travel time, not a slow approach to equilibrium.')
add(11,4,'Second-order models, poles and damping regimes',
r'''Assumed: two coupled first-order balances and exponential solutions of linear ODEs.

Second-order behaviour requires two dynamic states or one second-order equation. Its pole pair determines whether deviations relax monotonically, decay while oscillating, persist, or grow.''',
r'''Two tanks smooth a disturbance twice. A mass and spring exchange kinetic and elastic energy and can overshoot. Both have two states, but the mechanism of coupling decides whether oscillation is possible.''',
r'''**Step 1: eliminate an intermediate tank state.** Let $x'$ be inlet deviation, $y'$ the first-tank outlet and $z'$ the second, with positive time constants $\tau_1,\tau_2$ and unity gains:

$$\tau_1\dot y'+y'=x',\qquad \tau_2\dot z'+z'=y'.
$$

*Reason:* each mixed-tank balance relaxes its state toward the upstream condition. Substitute $y'=\tau_2\dot z'+z'$ and its derivative into the first balance:

$$\tau_1\tau_2\ddot z'+(\tau_1+\tau_2)\dot z'+z'=x'.\tag{AUTO}$$

**Step 2: define the standard form.** For a general ODE $a_2\ddot y'+a_1\dot y'+a_0y'=bx'$ with constant coefficients and $a_0\ne0$, the conventional form applies when $a_2/a_0>0$:

$$\tau^2\ddot y'+2\zeta\tau\dot y'+y'=K_px',\quad
\tau^2=a_2/a_0,\quad 2\zeta\tau=a_1/a_0,\quad K_p=b/a_0.\tag{AUTO}$$

*Reason:* divide by $a_0$ and define $\tau>0$ as the second-order time scale and $\zeta$ as the dimensionless damping factor. For a forced mass–spring system $m\ddot y'+\mu\dot y'+ky'=F'$, $\tau=\sqrt{m/k}$, $\zeta=\mu/(2\sqrt{mk})$ and force-to-displacement gain is $1/k$. Weight has already cancelled when displacement is measured from equilibrium.

**Step 3: transform and find the poles.** Zero initial state and derivative give

$$G(s)=\frac{K_p}{\tau^2s^2+2\zeta\tau s+1},\qquad
p_{1,2}=\frac{-\zeta\pm\sqrt{\zeta^2-1}}{\tau}.\tag{AUTO}$$

*Reason:* solve the quadratic characteristic equation; each root multiplies time in a free-response exponential.

| Damping | Pole pattern | Response of this constant-numerator model |
|---|---|---|
| $\zeta>1$ | Two negative real poles | Overdamped; monotonic stable step |
| $\zeta=1$ | Repeated pole $-1/\tau$ | Critically damped |
| $0<\zeta<1$ | Complex pair with negative real part | Decaying oscillations |
| $\zeta=0$ | Pair $\pm i/\tau$ | Undamped; persistent free oscillations |
| $\zeta<0$ | Poles with positive real part | Growing deviations |

*Reason:* the real part controls decay/growth and the imaginary part supplies oscillation frequency. At $\zeta=-1$, the repeated positive pole also gives instability.''',
r'''The natural angular frequency is $\omega_n=1/\tau$, in rad per unit time. The undamped period is $2\pi\tau$; $\tau$ itself is not an oscillation period.

For two passive lags, $\tau=\sqrt{\tau_1\tau_2}$ and $\zeta=(\tau_1+\tau_2)/(2\sqrt{\tau_1\tau_2})\geq1$, because $(\sqrt{\tau_1}-\sqrt{\tau_2})^2\geq0$. Thus a simple cascade of two positive lags cannot be underdamped. Equal lags are critically damped. Undamped poles are not BIBO stable, even though their free oscillations are bounded.''',
r'''![Normalised second-order step responses at different damping factors](../figs/PDC-11-damping-regimes.png)

The graph uses $t/\tau$ horizontally and output normalised by its unit-step gain vertically. For two tanks with $\tau_1=20.0$ s and $\tau_2=80.0$ s, the combined time scale is $40.0$ s and $\zeta=1.25$. The poles are $-0.0500$ and $-0.0125$ s$^{-1}$: both modes decay without oscillation.

For $\tau=10.0$ s and $\zeta=0.500$, poles are $-0.0500\pm0.0866025i$ s$^{-1}$. The response oscillates with a decaying envelope rather than behaving like the two passive tanks.''',
'Pole analysis generalises to higher-order models. Overshoot and decay ratio translate this second-order pole pair into directly observable response features.',
'Second order describes the number of dynamic states; damping describes how their modes behave. The physical coupling determines which damping regimes are possible.')
add(12,4,'Second-order step response, overshoot and decay ratio',
r'''Assumed: the standard second-order model with constant numerator, no zeros or dead time, and zero initial output and derivative.

Deriving the step response makes overshoot, oscillation period and decay ratio consequences of the pole pair. These relations apply to the standard model, not every process with two poles.''',
r'''The steady response is a constant particular solution. The transient is the free mode needed to match the starting state. In an underdamped process, that free mode repeatedly crosses the final value while losing amplitude.''',
r'''**Step 1: separate steady and transient parts.** Let the input step be $\Delta x$ and normalise $r(t)=y'(t)/(K_p\Delta x)$, with nonzero $K_p\Delta x$. Then $\tau^2\ddot r+2\zeta\tau\dot r+r=1$. For distinct poles, write $r=1+C_1e^{p_1t}+C_2e^{p_2t}$. Initial conditions require

$$C_1+C_2=-1,\qquad p_1C_1+p_2C_2=0.
$$

*Reason:* neither output nor its first derivative can jump under a finite step for this strictly proper second-order model. Solving these two equations gives

$$r=1+\frac{p_2e^{p_1t}-p_1e^{p_2t}}{p_1-p_2}.\tag{AUTO}$$

**Step 2: handle the repeated root.** At $\zeta=1$, $p=-1/\tau$ and the transient has form $(C_1+C_2t)e^{-t/\tau}$. Enforcing $r(0)=\dot r(0)=0$ gives $C_1=-1$, $C_2=-1/\tau$, so

$$r=1-(1+t/\tau)e^{-t/\tau}.\tag{AUTO}$$

*Reason:* repeated roots need a polynomial factor; simply setting the two exponential coefficients equal would lose one independent solution.

**Step 3: use complex poles.** For $0<\zeta<1$, define $a=\zeta/\tau$ and $\omega_d=\sqrt{1-\zeta^2}/\tau$. Write $r=1+e^{-at}(C\cos\omega_dt+D\sin\omega_dt)$. The same initial conditions give $C=-1$ and $D=-a/\omega_d$, hence

$$r=1-e^{-\zeta t/\tau}\left[\cos(\omega_dt)+
\frac{\zeta}{\sqrt{1-\zeta^2}}\sin(\omega_dt)\right].\tag{AUTO}$$

*Reason:* conjugate modes combine into a real damped sinusoid.

**Step 4: locate the first peak.** Differentiate the preceding result; cosine terms cancel:

$$\dot r=\frac{e^{-\zeta t/\tau}}{\tau\sqrt{1-\zeta^2}}\sin(\omega_dt).
$$

*Reason:* extrema occur at zero sine. The first peak is at $t_p=\pi/\omega_d$, where cosine is $-1$. If $B=|K_p\Delta x|$ is the total steady change and $A$ is the first peak's excess magnitude above the final value,

$$\frac AB=\exp\left[-\frac{\pi\zeta}{\sqrt{1-\zeta^2}}\right],\qquad
t_p=\frac{\pi\tau}{\sqrt{1-\zeta^2}}.\tag{AUTO}$$

**Step 5: compare successive peaks on the same side.** They are separated by $T=2\pi/\omega_d$. If $C$ is the next same-side peak's excess magnitude, its envelope has fallen by $e^{-aT}$:

$$\frac CA=\exp\left[-\frac{2\pi\zeta}{\sqrt{1-\zeta^2}}\right]
=\left(\frac AB\right)^2,\qquad
T=\frac{2\pi\tau}{\sqrt{1-\zeta^2}}.\tag{AUTO}$$

*Reason:* compare peaks measured relative to the final value, not their absolute heights. Consecutive extrema on opposite sides are only half a period apart.''',
r'''![Definitions of overshoot, steady change and successive-peak decay](../figs/PDC-12-overshoot-and-period.png)

The horizontal reference through the oscillations represents the final value; $B$ spans the initial-to-final change. For negative gain, reflect the response and use magnitudes in the overshoot ratio.

Taking $\zeta\rightarrow0$ gives $r=1-\cos(t/\tau)$, with no final settled value. Taking $\zeta\rightarrow1$ requires the repeated-root limit rather than substituting into a singular-looking expression. Zeros or delays alter measured response shape and invalidate a blind fit of these formulas.''',
r'''For $\tau=10.0$ s and $\zeta=0.500$, $\omega_d=0.0866025$ rad s$^{-1}$, $t_p=36.2760$ s and $T=72.5520$ s. Overshoot is $A/B=0.163034$, or $16.3034\%$, and same-side decay ratio is $C/A=0.0265799$. A unit-gain unit-step response therefore first peaks at $1.16303$.

For critical damping, the normalised response at $t=\tau$ is $1-2e^{-1}=0.264241$. Unlike a first-order lag, it has zero initial slope.''',
'Observed oscillation can reveal a complex pole pair. Cascaded tank examples illustrate the critically damped formula without requiring a mechanical analogy.',
'Overshoot comes from the transient mode carrying the output past its steady value. Pole decay and frequency determine the excess peak and the spacing between peaks.')
add(13,5,'Series blocks and the pipe–two-tank response',
r'''Assumed: a plug-flow delay and perfectly mixed tank energy balances.

A pipe followed by two insulated tanks combines transport delay with two first-order lags. Multiplying blocks preserves each element's physical role and produces a delayed second-order response.''',
r'''The pipe postpones the arrival of a hot front. The first tank dilutes it into stored liquid; the second smooths that already changing temperature. The outlet stays unchanged until the front arrives, then initially changes very gently.''',
r'''**Step 1: construct each element.** For pipe length $L$, diameter $D$, constant volumetric flow $q$ and uniform velocity $u=4q/(\pi D^2)$, the delay is $t_d=L/u$. Let temperatures along the sequence be $T_0,T_1,T_2,T_3$, and tank volumes be $V_2,V_3$.

![Pipe followed by two mixed tanks](../figs/PDC-13-pipe-and-tanks.png)

For ideal plug flow, $\bar T_1=e^{-t_ds}\bar T_0$. With constant liquid properties and no heat losses, each tank balance is $\rho V_ic_p\dot T_i=\rho qc_p(T_{i-1}-T_i)$, so its deviation transfer function is $1/(\tau_is+1)$, $\tau_i=V_i/q$.

*Reason:* the pipe preserves the input waveform after transit, whereas tank storage gives a lag.

**Step 2: substitute through the series.** For blocks $G_1,G_2,G_3$, $\bar T_1=G_1\bar T_0$, $\bar T_2=G_2\bar T_1$, $\bar T_3=G_3\bar T_2$. Therefore

$$\frac{\bar T_3}{\bar T_0}=\frac{e^{-t_ds}}{(\tau_2s+1)(\tau_3s+1)}.\tag{AUTO}$$

*Reason:* the output of one element is the next element's input; repeated substitution multiplies their SISO transfer functions.

**Step 3: invert equal lags.** For $\tau_2=\tau_3=\tau$ and inlet step $\Delta T_0$, first remove the delay and decompose

$$\frac{1}{s(\tau s+1)^2}
=\frac1s-\frac{\tau}{\tau s+1}-\frac{\tau}{(\tau s+1)^2}.
$$

*Reason:* multiplying by the common denominator verifies the coefficients. The inverse transforms of the last two terms are $e^{-t/\tau}$ and $(t/\tau)e^{-t/\tau}$. Restore the delay by shifting the complete causal response:

$$T_3'(t)=\begin{cases}
0,&t<t_d,\\
\Delta T_0\left[1-\left(1+\frac{t-t_d}{\tau}\right)e^{-(t-t_d)/\tau}\right],&t\geq t_d.
\end{cases}\tag{AUTO}$$

*Reason:* the pipe postpones the entire two-tank response. The rational part has a repeated pole $-1/\tau$ and is critically damped.''',
r'''Scalar LTI series multiplication commutes, so reordering these ideal blocks leaves the overall input–output transfer function unchanged. Their intermediate signals do change. Reordering real equipment may also change heat losses, mixing, flows or the relevant model; the algebra does not establish physical interchangeability.

Two lags produce a zero initial slope after the delay. They create a smooth rise, not extra exact dead time. The final gain remains one because the insulated system eventually passes the changed temperature through unchanged.''',
r'''Let $q=1.00\times10^{-3}$ m$^3$ s$^{-1}$, $D=0.0400$ m, $L=20.0$ m and $V_2=V_3=0.100$ m$^3$. The calculated velocity is $0.795775$ m s$^{-1}$, $t_d=25.1327$ s and both time constants are $100$ s. Thus

$$G(s)=\frac{e^{-25.1327s}}{(100s+1)^2}.
$$

For a $1.00$ K inlet step, $T_3'(125)=0.263753$ K. Rounding the transit time to $25$ s is reasonable for a coarse estimate, but the calculation here retains the value from the specified geometry.''',
'Series-block algebra extends to sensor and actuator lags. Parallel paths instead require signed addition of contributions to an output.',
'Build the overall response from physically derived elements. The delay sets its onset; the repeated tank pole sets its subsequent smooth approach.')
add(14,5,'Summing contributions and duplicating signals',
r'''Assumed: superposition in linear deviation models.

Series elements multiply; independent contributions to the same output add with their signs. A signal branch copies information and does not divide its value like a material-flow splitter.''',
r'''In a heated tank, warmer feed and extra heater power both affect temperature. Each input passes through its own response path, then the temperature contributions combine. Measuring that temperature does not consume part of it.''',
r'''**Step 1: begin with the balance.** For fixed $V,q,\rho,c_p$, no heat loss or reaction, set $\tau=V/q$ and $C_f=\rho qc_p$, the flowing heat-capacity rate. The tank deviation equation is

$$\tau\dot T'+T'=T_0'+Q'/C_f.\tag{AUTO}$$

*Reason:* subtract the steady energy balance so the two forcing contributions remain. Transform with zero initial deviation:

$$\bar T=G_1\bar T_0+G_2\bar Q,\qquad
G_1=\frac1{\tau s+1},\quad G_2=\frac1{C_f(\tau s+1)}.\tag{AUTO}$$

*Reason:* both sources feed the same state, but the heater input must first be converted from power to temperature-equivalent forcing.

**Step 2: apply a signed summing junction.** A junction labelled $+$ on one path and $-$ on another forms $\bar y=\bar y_1-\bar y_2$. If both paths start with the same input $\bar x$, their equivalent block is $G_1-G_2$; two positive paths give $G_1+G_2$.

*Reason:* superposition is addition of output effects, including their signs. Signals summed at a junction must have compatible units; raw temperature and power cannot be added.

**Step 3: duplicate a signal.** If one ideal branch sends $\bar T$ onward and another to a sensor, both pre-sensor branches equal $\bar T$. The measured signal is $\bar T_m=G_m\bar T$, where $G_m$ is the sensor transfer function.

*Reason:* a branch copies a numerical variable. It is not a material balance and does not halve temperature. Sensor dynamics or loading, if relevant, must be represented separately.''',
r'''Superposition holds for the linear model at fixed coefficients. If flow changes, the heater gain and time constant change too; products such as $q'T'$ require linearisation before this simple summation is justified.

For an ideal measurement scale, $G_m(0)=1$, but a sensor may still lag. Treating the measured output as instantly equal to the true output hides a pole in the feedback path.''',
r'''For water with $C_f=42000$ W K$^{-1}$ and $\tau=100$ s, let the feed temperature fall by $5.00$ K while heating rises by $210000$ W. Their step contributions sum to

$$T'(t)=\left[-5.00+\frac{210000}{42000}\right](1-e^{-t/100})=0.
$$

The exact cancellation follows because both paths share the same tank lag in this model and the commands occur together. An actuator lag in the heat path, a delayed disturbance measurement, or inaccurate $C_f$ produces a transient error even when the steady effects cancel.''',
'Feedforward exploits signed summation to oppose disturbance effects. Transfer-function matrices organise the same idea when several inputs affect several outputs.',
'Write the signal equations before simplifying a block diagram. Their units, signs and branch meanings prevent most combination errors.')
add(15,6,'Transfer-function matrices and coupled CSTR concentrations',
r'''Assumed: constant-volume, isothermal CSTR balances for $A\rightarrow B$.

A MIMO model is a matrix of input–output responses. The reacting CSTR shows how an input can affect its own species directly and another species through a reaction pathway.''',
r'''More A in the feed raises reactor A and therefore makes more B. More B in the feed raises B without creating A because the reaction is irreversible. The matrix should express this directional coupling, not artificially give every input the same effect.''',
r'''**Step 1: define the matrix convention.** With $n$ input deviations and $m$ output deviations,

$$\bar{\boldsymbol y}=\boldsymbol G(s)\bar{\boldsymbol x},\qquad
\bar y_i=\sum_{j=1}^nG_{ij}(s)\bar x_j.\tag{AUTO}$$

*Reason:* output row $i$ sums the contributions from input columns $j$. Define each $G_{ij}$ with all other input deviations and initial state deviations zero. Each entry has units of its row's output divided by its column's input.

**Step 2: balance both components.** Let $V$ be volume, $q$ equal inlet/outlet flow, $\tau=V/q$, $k>0$ first-order rate constant, $c_{A0},c_{B0}$ feed concentrations and $c_A,c_B$ tank concentrations. Assume constant density, one mole B formed per mole A consumed, no volume change and perfect mixing:

$$\tau\dot c_A+(1+k\tau)c_A=c_{A0},\qquad
\tau\dot c_B+c_B=c_{B0}+k\tau c_A.\tag{AUTO}$$

*Reason:* A reaction loss is an equal B reaction source. Subtract the steady balances and transform:

$$\bar c_A=\frac{\bar c_{A0}}{\tau s+1+k\tau},\qquad
\bar c_B=\frac{\bar c_{B0}}{\tau s+1}+
\frac{k\tau\bar c_{A0}}{(\tau s+1)(\tau s+1+k\tau)}.
$$

*Reason:* solve the A equation first, then substitute it into the B equation. This produces

$$\begin{bmatrix}\bar c_A\\\bar c_B\end{bmatrix}
=\begin{bmatrix}
\dfrac1{\tau s+1+k\tau}&0\\
\dfrac{k\tau}{(\tau s+1)(\tau s+1+k\tau)}&\dfrac1{\tau s+1}
\end{bmatrix}
\begin{bmatrix}\bar c_{A0}\\\bar c_{B0}\end{bmatrix}.\tag{AUTO}$$

**Step 3: check the conserved total.** Add the two ODEs:

$$\tau\frac{d(c_A+c_B)}{dt}+(c_A+c_B)=c_{A0}+c_{B0}.\tag{AUTO}$$

*Reason:* reaction cancels in the total concentration balance. Equivalently, the A-feed column sums to $1/(\tau s+1)$, because

$$\frac1{\tau s+1+k\tau}+\frac{k\tau}{(\tau s+1)(\tau s+1+k\tau)}=\frac1{\tau s+1}.
$$''',
r'''The two dynamic modes have poles $-(1+k\tau)/\tau$ and $-1/\tau$. The B response to feed A contains both modes: A first changes, then its changed conversion supplies B. The A response to feed B is zero under the stated irreversible, uncoupled chemistry.

This is a MIMO concentration model. The heated tank with two inputs but only one temperature output is MISO, a single-output special case. If temperature affects $k$, or multiple reactions occur, the zero entry and pole structure can change.''',
r'''Take $\tau=100$ s and $k=0.0100$ s$^{-1}$. A unit step in $c_{A0}$ with no $c_{B0}$ change gives

$$c_A'=\tfrac12(1-e^{-2t/100}),\qquad
c_B'=\tfrac12-e^{-t/100}+\tfrac12e^{-2t/100}.
$$

These follow by taking the A response and subtracting it from total response $1-e^{-t/100}$. At $100$ s, $c_A'=0.432332$ and $c_B'=0.199788$ in the concentration unit used for the input. Final deviations are $0.500$ each. Their sum tracks an inert-tank concentration response at every time.''',
'Material conservation is a strong check on a coupled model. The boiler matrix will combine two different balances and include an integrating inventory output.',
'Rows identify outputs and columns identify inputs. Coupling entries should follow actual pathways, and conserved combinations provide independent verification.')
add(16,6,'Boiler mass–energy balance and integrating inventory',
r'''Assumed: saturated-phase properties, a rigid control volume and simultaneous linear equations.

For a boiler held at fixed pressure, mass and energy balances determine liquid-inventory dynamics and steam production together. This idealised model contains an integrator for inventory and algebraic feed/heat effects on steam flow.''',
r'''Extra heat evaporates stored liquid unless the feed rises to replace it. Extra subcooled feed can temporarily reduce steam output because some heat must warm that feed. Pressure is assumed already maintained; its dynamic control is outside this reduced model.''',
r'''**Step 1: define properties and storage.** Let $F$ be liquid-feed mass flow, $G$ steam mass flow, $Q_H$ heat input, $V_L,V_G$ liquid/vapour volumes, and $V_T=V_L+V_G$ fixed vessel volume. Hold pressure at $8$ bar absolute, so saturation temperature is $170.4$ °C and phase properties remain constant. Densities are $\rho_L,\rho_G$; specific internal energies are $\hat U_L,\hat U_G$; feed and steam specific enthalpies are $\hat H_F,\hat H_G$. Ignore heat loss and other work.

![Boiler feed, heat, steam and liquid holdup](../figs/PDC-16-boiler.png)

Mass is $M=\rho_LV_L+\rho_G(V_T-V_L)$. Internal energy is $U=\rho_L\hat U_LV_L+\rho_G\hat U_G(V_T-V_L)$. Differentiate at fixed properties:

$$(\rho_L-\rho_G)\dot V_L=F-G,\qquad
(\rho_L\hat U_L-\rho_G\hat U_G)\dot V_L
=F\hat H_F-G\hat H_G+Q_H.\tag{AUTO}$$

*Reason:* total vessel volume is constant, so increasing liquid volume displaces vapour volume. Enthalpy accounts for energy carried by streams; internal energy describes storage.

**Step 2: eliminate steam flow.** Define $D_\rho=\rho_L-\rho_G$ and $D_U=\rho_L\hat U_L-\rho_G\hat U_G$. From mass, $G=F-D_\rho\dot V_L$. Substitute into energy:

$$D_U\dot V_L=F(\hat H_F-\hat H_G)+D_\rho\hat H_G\dot V_L+Q_H.
$$

*Reason:* use one balance to close the unknown flow in the other. Define

$$B=D_\rho\hat H_G-D_U
=\rho_L(\hat H_G-\hat U_L)-\rho_G(\hat H_G-\hat U_G).
$$

Then

$$\dot V_L=aF+bQ_H,\quad G=cF+dQ_H,
\quad a=\frac{\hat H_G-\hat H_F}{B},\ b=-\frac1B,
\ c=1-D_\rho a,\ d=\frac{D_\rho}{B}.\tag{AUTO}$$

*Reason:* isolate $\dot V_L$, then recover $G$ from mass. With zero initial deviation, subtract the steady balances and transform:

$$\begin{bmatrix}\bar V_L\\\bar G\end{bmatrix}
=\begin{bmatrix}a/s&b/s\\c&d\end{bmatrix}
\begin{bmatrix}\bar F\\\bar Q_H\end{bmatrix}.\tag{AUTO}$$

*Reason:* liquid volume is the integral of its rate; steam flow is algebraic in this reduced model.''',
r'''The inventory pole is at zero: at fixed $F,Q_H$ the model provides no level-dependent restoring effect. A persistent mismatch drains or fills the boiler until the assumed phase inventory no longer exists. The algebraic steam-flow row represents direct feedthrough, not a lag with an extremely short measured time constant.

At steady state $G_s=F_s$ and $Q_{Hs}=F_s(\hat H_G-\hat H_F)$. The model deliberately omits pressure dynamics, finite evaporation kinetics and heat storage in equipment. It is valid only while saturated liquid and vapour coexist and the fixed-pressure approximation is adequate.''',
r'''Use $\hat H_F=675.5$, $\hat H_G=2768.3$, $\hat U_L=720.0$, $\hat U_G=2576.0$ kJ kg$^{-1}$, and $\rho_L=896.9$, $\rho_G=4.2$ kg m$^{-3}$. Calculate $B=1.83631261\times10^6$ kJ m$^{-3}$. With $F,G$ in kg s$^{-1}$ and $Q_H$ in kJ s$^{-1}$ (kW),

$$\begin{bmatrix}\bar V_L\\\bar G\end{bmatrix}
\approx\begin{bmatrix}
1.13968\times10^{-3}/s&-5.44570\times10^{-7}/s\\
-0.0173881&4.86137\times10^{-4}
\end{bmatrix}
\begin{bmatrix}\bar F\\\bar Q_H\end{bmatrix}.
$$

Here $s$ is in s$^{-1}$. At fixed heat, a $1.00$ kg s$^{-1}$ feed increase gives $\dot V_L'=1.13968\times10^{-3}$ m$^3$ s$^{-1}$ and $G'=-0.0173881$ kg s$^{-1}$. Increasing heat simultaneously by $2092.8$ kW cancels the inventory drift and gives $G'=1.00$ kg s$^{-1}$, as both steady balances require.

If heat is expressed in watts instead, divide the heat-column coefficients by $1000$. The feed enthalpy includes warming the inlet from $160$ °C to saturation; using only saturated-liquid latent heat would miss that load.''',
'Inventory control restores a stable level when a process naturally integrates. The boiler also shows why proper transfer functions can contain direct input-to-output terms.',
'Mass and energy jointly determine steam flow and inventory. The integrating liquid-volume row identifies the need for inventory regulation; the algebraic row reflects the fixed-pressure idealisation.')
add(17,7,'Poles, repeated modes and stability',
r'''Assumed: partial fractions and complex exponentials.

Poles describe the free dynamic modes visible in an input–output model. Repeated poles add polynomial factors; complex conjugate poles combine into real oscillations. Stability must be defined carefully at poles on the imaginary axis.''',
r'''After a pulse is over, each dynamic mode retains a memory of the perturbation. A negative real part makes that memory fade. A positive real part amplifies it. Zero real part does not supply decay, even when a particular free response stays bounded.''',
r'''**Step 1: identify process poles.** For a rational SISO model $G(s)=N(s)/D(s)$ in reduced form, poles are roots of $D(s)$ and zeros are roots of $N(s)$. In $\bar y=G(s)\bar x$, extra roots supplied by $\bar x$ are input-signal poles, not additional process states.

**Step 2: invert elementary pole terms.** For a pole $p$ and integer $j\geq1$,

$$\mathcal L^{-1}\left[\frac{C_j}{(s-p)^j}\right]
=C_j\frac{t^{j-1}}{(j-1)!}e^{pt}.\tag{AUTO}$$

*Reason:* $\mathcal L[e^{pt}]=1/(s-p)$ and successive powers of $t$ arise by differentiating with respect to $s$. Repeated poles therefore require all powers from $1/(s-p)$ through $1/(s-p)^j$ in the partial fraction expansion.

**Step 3: combine a complex pair.** Let $p=a+ib$, residue $C=\alpha+i\beta$, and conjugate terms $p^*,C^*$, where $i^2=-1$. Euler's formula gives

$$Ce^{pt}+C^*e^{p^*t}
=2e^{at}[\alpha\cos(bt)-\beta\sin(bt)].\tag{AUTO}$$

*Reason:* imaginary terms cancel because a real physical model has conjugate poles and residues. The envelope is controlled by $a$, and frequency by $|b|$.

**Step 4: relate modes to stability.** For a finite-dimensional proper rational model with no unstable hidden modes, strictly negative real parts imply asymptotic decay and BIBO stability. A right-half-plane pole gives instability. Simple imaginary-axis poles give nondecaying free modes but fail BIBO stability; bounded resonant forcing can accumulate indefinitely. Repeated imaginary-axis poles can grow even without forcing.

*Reason:* multiplying a decaying exponential by any finite-degree polynomial still tends to zero; without exponential decay that guarantee disappears.''',
r'''Cancellation can hide a mode from one input–output transfer function. An exact unstable pole–zero cancellation is not evidence of internal stability: an initial condition or another input/output path may expose the hidden growing state. Use the full state model when making that claim.

For physical rational models, properness requires numerator degree no larger than denominator degree. Equal degrees allow direct feedthrough. Strictly proper models have lower numerator degree. Pure transport delay is causal but non-rational, so the polynomial-degree test does not describe it.''',
r'''Consider the dimensional time coordinate in seconds and the transfer function

$$G(s)=\frac1{s^6+2s^5+14s^4+60s^3+81s^2+34s}
=\frac1{s(s+1)^2(s+2)[(s-1)^2+16]}.
$$

The poles are $0$, $-1$ twice, $-2$ and $1\pm4i$, in s$^{-1}$. The positive-real-part pair makes the system unstable.

![Pole locations, with the repeated pole plotted at the same point](../figs/PDC-17-pole-map.png)

For a unit-area impulse, partial fractions give the response for $t\geq0$:

$$y'(t)=\frac1{34}-\frac{e^{-2t}}{50}-\frac{e^{-t}}{100}
-\frac{te^{-t}}{20}
+\frac{e^t[\cos(4t)-0.25\sin(4t)]}{1700}.
$$

The constant comes from the process pole at zero because the input is an impulse. The $te^{-t}$ term reveals the repeated pole, and the growing oscillation reveals $1\pm4i$. The residues and factorisation can be checked by recombining the rational terms before inversion.''',
'Pole locations determine whether the final-value theorem can be used. Zeros influence the weighting of these modes and can cause an initial response opposite to the final change.',
'Interpret each pole as a mode with a decay rate and, when complex, an oscillation frequency. Distinguish visible input–output stability from stability of all internal states.')
add(18,7,'Zeros, direct feedthrough and inverse response',
r'''Assumed: poles and partial-fraction responses.

Zeros reshape the forced response without creating a new exponential mode. A right-half-plane zero can make the output initially move opposite to its final direction, even when every process pole is stable.''',
r'''Two physical pathways can compete. A fast pathway may initially push the output down while a slower but stronger pathway eventually raises it. Their sum can therefore dip before rising; the zero encodes that competition.''',
r'''**Step 1: separate modes from their weights.** Write a strictly proper model with distinct poles as $G(s)=\sum_j C_j/(s-p_j)$. For each pole,

$$C_j=\lim_{s\to p_j}(s-p_j)G(s).\tag{AUTO}$$

*Reason:* multiplying removes that term's simple singularity; all other terms vanish in the limit. Changing the numerator changes residues $C_j$, hence the relative amplitudes of modes, while unreduced denominator roots stay fixed unless cancellation occurs.

**Step 2: build an inverse-response example.** Add two stable first-order pathways:

$$G(s)=\frac4{s+1}-\frac6{s+2}
=\frac{2(1-s)}{(s+1)(s+2)}.\tag{AUTO}$$

*Reason:* put the contributions over a common denominator. Poles are $-1,-2$ and the zero is $+1$. Both modes decay, but the zero is in the right half-plane. For a unit step,

$$\bar y=\frac{G(s)}s=\frac1s-\frac4{s+1}+\frac3{s+2},
\qquad y'=1-4e^{-t}+3e^{-2t}.\tag{AUTO}$$

*Reason:* invert each partial fraction. At zero, $y'=0$ but $\dot y'=4-6=-2$; the final value is $1$. The initial direction opposes the final direction.

**Step 3: distinguish feedthrough from storage.** If numerator and denominator degrees are equal, long division gives $G(s)=D_0+G_{sp}(s)$, where $D_0$ is a constant and $G_{sp}$ is strictly proper. In the time domain, $y'=D_0x'$ plus the stored-state response.

*Reason:* a constant block passes an input directly and may create an immediate output jump under a step. It need not be unphysical: the reduced boiler steam-flow model has this form.''',
r'''A right-half-plane zero does not by itself make the open-loop transfer function unstable. It constrains response shaping and makes exact stable causal inversion problematic. A numerator zero can cancel a denominator pole in a mathematical expression, but that can hide internal dynamics.

Not every stable two-pole model has the monotonic step response of the standard constant-numerator second-order model. Its zero structure and feedthrough matter too. The example assumes linearity and no transport delay.''',
r'''For the two-pathway model, solve $\dot y'=4e^{-t}-6e^{-2t}=0$. This gives the minimum at $t=\ln(3/2)=0.405465$ s, where $y'=-1/3=-0.333333$. The response eventually approaches $+1$.

Physically, the negative pathway has the faster pole $-2$ and initially contributes slope $-6$; the positive pathway contributes slope $+4$. Their final step contributions are $-3$ and $+4$, leaving a positive total.''',
'The final-value theorem predicts the endpoint but cannot reveal inverse response. Controller design must account for both poles and zeros when interpreting the transient.',
'Poles set the available modes; zeros set how the input excites them. A stable process can still have an initially misleading response direction.')
add(19,7,'Steady-state gain and the final-value theorem',
r'''Assumed: Laplace transforms of step inputs.

Steady-state gain is the change in settled output per change in settled input. Evaluating $G(0)$ gives this gain only when the relevant response actually settles; an algebraic limit alone cannot prove that it does.''',
r'''A constant input eventually leaves only a constant balance if all transient modes decay. Gain is the sensitivity of that remaining balance. If a mode grows or keeps oscillating, there is no settled output to interpret.''',
r'''**Step 1: read the gain from a balance.** For $\tau\dot y'+y'=K_px'$, a final constant input $\Delta x$ and settled output $\Delta y$ satisfy $\Delta y=K_p\Delta x$.

*Reason:* a steady state has zero derivative. Gain has output/input units; it need not be dimensionless.

**Step 2: use the transform.** The final-value theorem states, under its validity conditions,

$$\lim_{t\to\infty}y'(t)=\lim_{s\to0}s\bar y(s).\tag{AUTO}$$

For a proper rational signal transform, a standard sufficient condition is that all poles of $s\bar y$ lie strictly in the left half-plane after cancellations. Equivalently, $\bar y$ may have a simple pole at the origin for a constant final value, but no other nondecaying modes. A finite causal delay preserves a settling signal's endpoint.

*Reason:* the theorem requires decay of every nonconstant term. Check the complete output transform, including the imposed input and any initial-state contribution, rather than only one process denominator.

**Step 3: specialise to a step.** For zero-state $\bar y=G(s)\Delta x/s$,

$$\Delta y=\Delta x\lim_{s\to0}G(s),\qquad
K_p=G(0),\tag{AUTO}$$

provided the step response settles and the limit is finite.

*Reason:* the step's $1/s$ factor cancels the theorem's factor $s$. For a stable MIMO model, applying a step in one input at a time gives the gain matrix $\boldsymbol G(0)$. Integrating output paths generally lack a finite steady gain.''',
r'''A lag's pole comes from the process; a simple $1/s$ in the output transform may merely come from a step input. Confusing them would label a settling step response unstable.

A pure transport delay satisfies $e^{-t_ds}\rightarrow1$ at $s=0$. It changes timing but not steady gain. In an unstable model, a finite $G(0)$ does not establish an attainable endpoint.''',
r'''Take

$$G(s)=\frac{10e^{-5s}}{(s+1)(s+5)(s+10)},\qquad
x'(t)=1-e^{-t/10},\quad \bar x=\frac1{s(10s+1)}.
$$

The nonconstant modes have negative poles $-1,-5,-10,-0.1$, and the delay is finite. Hence

$$y'(\infty)=\lim_{s\to0}\frac{10e^{-5s}}{(10s+1)(s+1)(s+5)(s+10)}=0.200.
$$

For contrast, $G(s)=1/(s-1)$ with a unit step gives $y'=e^t-1$. The algebraic value $G(0)=-1$ is finite, but the positive pole prevents a final value; using the theorem to claim $y'(\infty)=-1$ would be invalid.''',
'Linearisation produces local gains that are derivatives of nonlinear steady relations. Controller decisions require that endpoint information together with transient poles, zeros and delay.',
'Check settling conditions before evaluating the endpoint. Once they hold, the final-value theorem avoids solving an entire transient just to find its final change.')
add(20,8,'Local linearisation and reaction-order comparison',
r'''Assumed: Taylor expansion, partial derivatives and reactor balances.

Linearisation replaces a nonlinear model by its tangent dynamics at one operating point. The steady state cancels, while the local slopes become gain and decay coefficients. The approximation is valid for sufficiently small deviations.''',
r'''A curved relationship can look almost straight over a narrow interval. Control near a fixed set point uses that local slope, not a single straight line for every possible operating condition. Moving the operating point can change both sensitivity and response speed.''',
r'''**Step 1: define linearity.** An operator $F$ is linear if $F(au+bv)=aF(u)+bF(v)$ for constants $a,b$. Powers and products of changing variables generally violate this property. A coefficient that depends on time may preserve linearity but loses time invariance.

**Step 2: expand a dynamic model.** Let output/state $y$ obey $\dot y=f(y,x)$ for input $x$. Choose a constant equilibrium $(y_s,x_s)$ with $f(y_s,x_s)=0$; define $y'=y-y_s$, $x'=x-x_s$. Taylor expansion gives

$$\dot y'\approx f(y_s,x_s)+f_y|_s\,y'+f_x|_s\,x'
=f_y|_s\,y'+f_x|_s\,x'.\tag{AUTO}$$

*Reason:* the constant term vanishes at equilibrium, and terms quadratic or higher in deviations are neglected. Subscripts on $f$ denote partial derivatives, evaluated at the operating point. With additional disturbance $d$, add $f_d|_s d'$; with several states, use the matrix of partial derivatives.

**Step 3: expose the local transfer function.** Write $a=f_y|_s$, $b=f_x|_s$. For zero initial deviation,

$$G(s)=\frac{b}{s-a}.
\quad\text{If }a<0:\quad \tau=-1/a,\quad K_p=-b/a.\tag{AUTO}$$

*Reason:* transform $\dot y'=ay'+bx'$ and isolate the output. The local restoring slope $a$ determines the pole. If $a=0$, the first-order model is an integrator and higher-order terms may be decisive for nonlinear stability.

**Step 4: compare reaction orders.** For fixed $q,V,T$ and $\tau=V/q$, first-order consumption gives $\tau\dot c_A+(1+k_1\tau)c_A=c_{A0}$, exactly linear in these concentration variables.

Second-order consumption gives $\tau\dot c_A+c_A+k_2\tau c_A^2=c_{A0}$. At its equilibrium, $c_{A0s}=c_{As}+k_2\tau c_{As}^2$. Substitute $c_A=c_{As}+c_A'$:

$$\tau\dot c_A'+(1+2k_2\tau c_{As})c_A'+k_2\tau(c_A')^2=c_{A0}'.
$$

*Reason:* expand the square and cancel the steady balance. Neglect the final quadratic term to obtain

$$G(s)\approx\frac1{\tau s+1+2k_2\tau c_{As}},\quad
\tau_{lin}=\frac{\tau}{1+2k_2\tau c_{As}},\quad
K_p=\frac1{1+2k_2\tau c_{As}}.\tag{AUTO}$$

*Reason:* the derivative of the reaction sink is $2k_2c_{As}$, not $k_2c_{As}$.''',
r'''The approximation discards the curvature, not the physical meaning of the original balance. Second-order $k_2$ has units concentration$^{-1}$ time$^{-1}$; $k_1$ has inverse-time units. Constant-temperature first-order reaction is linear, but a temperature-dependent Arrhenius rate introduces nonlinear coupling if temperature is a changing state.

The neglected quadratic reaction term is small relative to its first-order reaction perturbation when $|c_A'|\ll2c_{As}$. Near $c_{As}=0$, that particular comparison fails and one must inspect the full balance instead. A Taylor model says little about distant equilibria or large excursions.''',
r'''Let $\tau=100$ s, $k_2=0.0100$ m$^3$ mol$^{-1}$ s$^{-1}$ and $c_{As}=1.00$ mol m$^{-3}$. The corresponding feed equilibrium is $c_{A0s}=2.00$ mol m$^{-3}$. Linearisation gives $\tau_{lin}=33.3333$ s and $K_p=0.333333$.

At unchanged operating conditions, a sufficiently small feed-composition increase has one-third of that increase in its final reactor concentration. Linearising about a different $c_{As}$ gives different coefficients; this is a local model rather than a globally linear reaction.''',
'The same Taylor procedure converts a gravity-outflow tank into a lag. Products of valve flow and concentration require it in the three-tank mixing process.',
'Linearise only after finding a consistent equilibrium. The local derivatives identify the restoring mode and steady sensitivity of small disturbances.')
add(21,8,'Gravity-draining tank: linear model and exact response',
r'''Assumed: a volume balance and square-root outflow from Bernoulli's law.

Unlike a tank with prescribed pumped withdrawal, a gravity-draining tank has a restoring outflow. Linearisation makes it a local first-order lag; solving the nonlinear step reveals the approximation's limits.''',
r'''A higher level increases the driving head and therefore increases outflow. That feedback in the physics opposes accumulation without a controller. Because outflow increases as a square root, its slope weakens at larger levels; a single tangent model cannot predict every new equilibrium exactly.''',
r'''**Step 1: write and linearise the balance.** Let area be $A$, level $h>0$, inlet flow $q_0$, and outlet $q=k\sqrt h$ with fixed valve/outlet coefficient $k>0$. Assume constant density and area, quasi-steady outflow, no overflow, and no other inflows. Then

$$A\dot h=q_0-k\sqrt h,\qquad q_{0s}=k\sqrt{h_s}.\tag{AUTO}$$

*Reason:* increasing level stores volume and increases the gravity-driven loss. Define deviations and expand $\sqrt{h_s+h'}\approx\sqrt{h_s}+h'/(2\sqrt{h_s})$. Cancel the steady terms:

$$A\dot h'=q_0'-\frac{k}{2\sqrt{h_s}}h',\qquad
\tau\dot h'+h'=K_pq_0',
\quad\tau=\frac{2A\sqrt{h_s}}k,\quad K_p=\frac{2\sqrt{h_s}}k.\tag{AUTO}$$

*Reason:* the outflow slope supplies a restoring term. The transfer function is $G=K_p/(\tau s+1)$, with pole $-k/(2A\sqrt{h_s})$. Gain has units s m$^{-2}$, equivalent to level per volumetric-flow change.

**Step 2: compare new equilibria.** After a step $\Delta q_0$, the local model gives

$$h'_{lin}=K_p\Delta q_0(1-e^{-t/\tau}),\qquad
h'_{exact,\infty}=K_p\Delta q_0+(\Delta q_0/k)^2.\tag{AUTO}$$

*Reason:* the exact equilibrium is $h_\infty=[(q_{0s}+\Delta q_0)/k]^2$; subtract $h_s=(q_{0s}/k)^2$ and expand the square. The missing quadratic term reveals the finite-step error.

**Step 3: integrate the exact nonlinear step.** Let $z=\sqrt h$, $z_0=\sqrt{h_s}$ and $z_f=(q_{0s}+\Delta q_0)/k$. Since $\dot h=2z\dot z$,

$$2Az\dot z=k(z_f-z),\qquad
 dt=\frac{2A}{k}\frac{z}{z_f-z}\,dz.
$$

*Reason:* substituting the square-root state makes the equation separable. Use $z/(z_f-z)=-1+z_f/(z_f-z)$ and integrate from $z_0$:

$$t=\frac{2A}{k}\left[z_0-z+z_f\ln\left|\frac{z_f-z_0}{z_f-z}\right|\right].\tag{AUTO}$$

*Reason:* the logarithm comes from integrating $1/(z_f-z)$ with its negative derivative. This implicit exact solution applies along a positive-level trajectory before reaching the new equilibrium; a zero step simply gives constant $h$. For a positive inlet step, $z_0<z<z_f$.

**Step 4: linearise in the transformed state too.** Write $z=z_0+z'$ in $2Az\dot z=q_0-kz$. To first order,

$$2Az_0\dot z'+kz'=q_0',\qquad
h'=2z_0z'+O((z')^2).
$$

*Reason:* $z'\dot z'$ is a second-order perturbation, and the output transformation must also be expanded. Together these recover exactly the earlier local $h'$ model. Squaring the approximate $z(t)$ without dropping $(z')^2$ gives a different finite-step approximation, not the first-order linear level model.''',
r'''The tangent approximation needs $|h'|/h_s$ small. It fails near an empty tank, where the square-root derivative is singular. The coefficient $k$ has units m$^{5/2}$ s$^{-1}$, so both the original flow law and the derived time constant are dimensionally consistent.

The exact transient approaches equilibrium asymptotically. A numerical solution of the implicit equation or direct integration can quantify deviations from the local lag without inventing a constant time constant for the nonlinear process.''',
r'''Take $A=3.00$ m$^2$, $k=0.0200$ m$^{5/2}$ s$^{-1}$, $q_{0s}=0.0200$ m$^3$ s$^{-1}$ and $\Delta q_0=0.0100$ m$^3$ s$^{-1}$. Then $h_s=1.00$ m, $\tau=300$ s and $K_p=100$ s m$^{-2}$. The linear final level is $2.00$ m; the exact final level is $2.25$ m.

![Local linear response and nonlinear level response](../figs/PDC-21-linear-and-nonlinear-level.png)

At $1000$ s, the linear model gives $h=1.96433$ m and direct nonlinear integration gives $h=2.13198$ m. The implicit solution returns the same nonlinear value. The figure is qualitative; these values are computed from the balances, not read from the plotted lines. The large inlet change demonstrates why local linearisation must be checked for the intended excursion.''',
'Gravity outflow turns an otherwise integrating level into a self-regulating lag. Its steady gain is the derivative of the nonlinear equilibrium relation at the chosen point.',
'Linearisation preserves the local restoring physics. The exact equilibrium and implicit transient quantify what it loses for a large change.')
add(22,8,'Three-tank mixing: valve linearisation and step response',
r'''Assumed: component balances, deviation variables, series lags and local linearisation.

A three-tank mixer combines variable-flow nonlinearity with a cascade of concentration lags. The valve and disturbance gains must use a consistent steady composition and an explicit percentage convention.''',
r'''Opening the pure-tracer valve adds tracer, but it also increases total flow and changes residence time. The local model captures the first-order composition effect while dropping products of flow and concentration deviations. Downstream tanks smooth that change twice more.''',
r'''**Step 1: define the composition convention and equilibrium.** Three perfectly mixed tanks have equal fixed volume $V=35$ m$^3$; their outlet flows follow the combined inlet flow, maintaining each volume. Stream A is pure inert tracer; stream B contains tracer concentration $x_B$ expressed as a numerical **volume percent**, so pure A has $x_A=100$, not $1$. Assume equal constant densities and additive volumes.

![Three tanks mixing pure tracer and a dilute tracer stream](../figs/PDC-22-three-tank-mixer.png)

Let flows be $q_A,q_B$ in m$^3$ min$^{-1}$, tank volume-percent compositions $x_1,x_2,x_3$, and valve position $v$ as a numerical percent open. A linear valve gives $q_A=k_vv$, $k_v=0.0028$ m$^3$ min$^{-1}$ per percentage point. At $v_s=50$, $q_{As}=0.14$; take $q_{Bs}=6.86$ and $x_{Bs}=2$. Then

$$x_s=\frac{100q_{As}+q_{Bs}x_{Bs}}{q_{As}+q_{Bs}}=3.96,
\qquad \tau=\frac{V}{q_{As}+q_{Bs}}=5.00\ \mathrm{min}.\tag{AUTO}$$

*Reason:* every tank has the same steady composition from the combined feed balance. Retain this equilibrium throughout the perturbation model.

**Step 2: expand tank 1's balance.** Hold $q_B=q_{Bs}$ while $q_A$ and $x_B$ can change:

$$V\dot x_1=100q_A+q_{Bs}x_B-(q_A+q_{Bs})x_1.
$$

Substitute $q_A=q_{As}+q_A'$, $x_B=x_{Bs}+x_B'$ and $x_1=x_s+x_1'$ and cancel the steady balance:

$$V\dot x_1'=-(q_{As}+q_{Bs})x_1'+q_{Bs}x_B'
+(100-x_s)q_A'-q_A'x_1'.
$$

*Reason:* the valve perturbation increases tracer inflow by $100q_A'$ and removes more tank mixture by $x_sq_A'$; their difference sets its local concentration sensitivity. Neglect the product $q_A'x_1'$ and divide by total steady flow:

$$\tau\dot x_1'+x_1'=K_Bx_B'+K_q q_A',\quad
K_B=\frac{q_{Bs}}{q_{As}+q_{Bs}},\quad
K_q=\frac{100-x_s}{q_{As}+q_{Bs}}.\tag{AUTO}$$

**Step 3: linearise the downstream tanks.** Tank 2 obeys $V\dot x_2=(q_A+q_{Bs})(x_1-x_2)$. Because its two baseline compositions are equal, the flow perturbation multiplies only a concentration deviation:

$$\tau\dot x_2'+x_2'=x_1',\qquad
\tau\dot x_3'+x_3'=x_2',\qquad q_A'=k_vv'.
$$

*Reason:* drop the second-order product of flow deviation and concentration difference. Transform and multiply the three lag factors:

$$\bar x_3=\frac{K_B}{(\tau s+1)^3}\bar x_B+
\frac{K_v}{(\tau s+1)^3}\bar v,
\quad K_v=K_qk_v=0.038416,\quad K_B=0.980000.\tag{AUTO}$$

Here $s$ is in min$^{-1}$; $K_v$ is concentration percentage points per valve-opening percentage point. The visible mode has pole $-1/5$ min$^{-1}$ repeated three times.

**Step 4: invert the valve step.** Hold $x_B'=0$ and apply $v'=\Delta vH(t)$. Write

$$\frac1{s(\tau s+1)^3}=
\frac1s-\frac{\tau}{\tau s+1}-\frac{\tau}{(\tau s+1)^2}-\frac{\tau}{(\tau s+1)^3}.
$$

*Reason:* multiplying by the common denominator telescopes to one. Inverting the repeated-pole terms gives

$$x_3'=K_v\Delta v\left[1-\left(1+\frac t\tau+\frac{t^2}{2\tau^2}\right)e^{-t/\tau}\right].\tag{AUTO}$$

*Reason:* the third pole contributes the quadratic-in-time exponential term. With $\tau=5$ min, its quadratic coefficient is $t^2/50$.''',
r'''A volume-percent change from $2$ to $3$ is one **percentage point**; it is not a $1\%$ relative increase. Using volume fractions is equally valid, but requires replacing $100$ by $1$ and rescaling concentration gains consistently.

The cascade has no exact dead time, though its initially flat response can resemble a delay. The local model freezes residence time at its baseline value and is accurate only for small flow/composition changes. A real valve may not be linear in stem position at changing pressure drop.''',
r'''A valve move from $50$ to $60$ percent open has $\Delta v=10$ percentage points. The local model predicts a final tracer increase of $0.384160$ percentage points. At $5.00$ min the increase is $0.0308486$ points; at $15.0$ min it is $0.221587$ points.

The final linear prediction is $4.34416\%$. Recomputing the exact steady feed mixture at $q_A=0.168$ m$^3$ min$^{-1}$ gives $4.34263\%$. Their small difference is due to the neglected flow–composition product. The distinction between the baseline $3.96\%$ and a rounded $4\%$ must not leave an uncancelled constant term in the derivation.''',
'This example brings physical balances, local linearisation, transfer-function summation and repeated poles together. These plant-response models are the starting point for designing feedback controllers once a controller model is introduced.',
'A consistent equilibrium and percentage convention produce a clear local model. Its two input gains and three repeated lag factors separate mixture sensitivity from the dynamics of stored liquid.')
# Publish canonical short notes with continuous subject-wide equation labels.
tag=0;meta=[]
for n,u,title,text in notes:
 def number(m):
  global tag
  tag+=1;return r'\tag{'+str(tag)+'}'
 text=re.sub(r'\\tag\{AUTO\}',number,text)
 filename=f'PDC-{n:02d} - {title.replace(chr(58), chr(32)+chr(8212))}.md';(D/filename).write_text(text.rstrip()+'\n')
 meta.append({'number':n,'unit':u,'title':title,'filename':filename})
Path('other/work/scratch/pdc/note-manifest.json').write_text(json.dumps({'notes':meta,'equations':tag},indent=2))
print(len(notes),'notes;',tag,'equation labels')
