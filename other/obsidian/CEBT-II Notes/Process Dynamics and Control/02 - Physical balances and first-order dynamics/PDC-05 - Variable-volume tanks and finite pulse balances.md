[Previous](<PDC-04 - Mixing tanks and reacting first-order lags.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<PDC-06 - Thermocouple and heated-liquid dynamics.md>)

<!-- note-content:start -->
# PDC-05: Variable-volume tanks and finite pulse balances

## Overview

Assumed: perfect mixing and the product rule.

When tank volume changes, balance the stored amount $Vc$, not concentration alone. A finite-volume pulse is handled by a jump balance before resuming continuous dynamics.

## Intuition

Removing well-mixed liquid lowers the amount of solute but does not instantly change its concentration. Adding feed changes both solute amount and liquid volume. Forgetting the volume derivative makes these two actions look incorrectly equivalent.

## Derivation

**Step 1: track volume and solute.** For inlet flow $q_0$, outlet flow $q$, inlet concentration $c_0$, tank concentration $c$ and first-order consumption constant $k$, assume constant density and additive volumes:

$$\dot V=q_0-q,\qquad
\frac{d(Vc)}{dt}=q_0c_0-qc-kVc.\tag{12}$$

*Reason:* storage is an extensive amount. Expanding gives $V\dot c+c\dot V=q_0c_0-qc-kVc$; substitute $\dot V=q_0-q$ and cancel $-qc$:

$$V\dot c=q_0(c_0-c)-kVc.\tag{13}$$

*Reason:* withdrawal leaves the concentration of remaining well-mixed liquid unchanged directly. It still affects later concentration dynamics through $V(t)$.

**Step 2: determine the volume history.** For specified flows,

$$V(t)=V(0)+\int_0^t[q_0(\theta)-q(\theta)]\,d\theta.\tag{14}$$

*Reason:* integrate the volume balance first, then use the resulting $V$ in the concentration ODE. For general time-dependent $V$, this is not a constant-coefficient transfer-function model. If $q_0=0$ and $k=0$, the equation gives $\dot c=0$ even during withdrawal.

**Step 3: cross a short, finite-volume addition.** A pulse adds volume $V_p$ at concentration $c_p$. Let $(V_-,c_-)$ and $(V_+,c_+)$ denote values immediately before and after it. Neglect reaction and ordinary flow during the short addition:

$$V_+=V_-+V_p,\qquad
V_+c_+=V_-c_-+V_pc_p,
\qquad c_+=\frac{V_-c_-+V_pc_p}{V_-+V_p}.\tag{15}$$

*Reason:* total volume and solute are conserved across the jump. Use $(V_+,c_+)$ as initial conditions for the subsequent ODE.

Why does outlet flow disappear from the concentration equation while inlet flow remains? The outlet has exactly the tank composition, so it removes solute and total volume in matching proportions. Feed at $c_0\ne c$ changes those proportions. As a check, feed at $c_0=c$ cannot change an inert tank's concentration even if it changes the volume. Withdrawal can still shorten the time over which a later feed change acts by reducing the stored volume.

## Motivation and explanation

A Dirac impulse idealises an input with finite area and negligible duration. A finite-volume addition also changes the model's holdup; it is not automatically the same experiment as an impulse in feed concentration at fixed volume.

The model stops being valid if the tank drains, overflows, mixes poorly or has appreciable volume change on mixing. A pulse too long to neglect reaction or outlet flow must be integrated with those effects.

### Interpreting the state after a pulse

The jump concentration is a volume-weighted average, so with positive additive volumes it lies between the original and pulse concentrations. Rich added liquid raises concentration, but its own volume dilutes the added solute. Treating a finite liquid addition as solute at unchanged volume overpredicts the concentration; maintaining constant volume instead requires including the displaced outflow. The jump supplies a new initial state for subsequent dynamics, not a new steady state unless later flows and reaction balance there.

## Link to other topics

Tank-level control also begins with the volume balance. Linearising flow and concentration products later allows a local transfer-function model around a constant-volume operating point.

## Conclusion

Use amount balances through volume changes and jump balances through short additions. The resulting state then determines the next continuous response.
<!-- note-content:end -->

[Previous](<PDC-04 - Mixing tanks and reacting first-order lags.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<PDC-06 - Thermocouple and heated-liquid dynamics.md>)
