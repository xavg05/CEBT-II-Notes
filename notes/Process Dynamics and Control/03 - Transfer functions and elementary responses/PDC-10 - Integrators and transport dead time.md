[Previous](<PDC-09 - First-order step and impulse responses.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<../04 - Second-order dynamics and damping/PDC-11 - Second-order models, poles and damping regimes.md>)

<!-- note-content:start -->
# PDC-10: Integrators and transport dead time

## Overview

Assumed: volume balances and the time-shift rule for Laplace transforms.

Two elementary process elements behave very differently from a self-regulating lag. An integrator stores a persistent imbalance; ideal transport dead time shifts a signal without smoothing it.

## Intuition

A tank with a fixed pumped outlet cannot increase outflow automatically when its level rises. Extra inflow keeps accumulating. A plug-flow pipe instead carries a temperature front downstream: nothing arrives until its transit time has elapsed, then the same front appears.

## Derivation

**Step 1: derive the integrator from level.** For a tank of constant cross-sectional area $`A`$, level $`h`$, inlet $`q_0`$ and prescribed pumped outlet $`q`$, assume both flows are independent of $`h`$:


**Equation (32)**

```math
A\dot h=q_0-q,\qquad
A\dot h'=q_0'-q',\qquad
\bar h=\frac{1}{As}(\bar q_0-\bar q).
```


*Reason:* volume is $`Ah`$; subtract the balanced baseline and transform with zero initial level deviation. With net-flow deviation $`x'=q_0'-q'`$, the transfer function is $`1/(As)`$, with pole at zero. A constant imbalance $`\Delta q`$ gives $`h'=\Delta q\,t/A`$; an impulse of net volume $`I_V`$ gives a persistent level jump $`I_V/A`$.

A scaled form is $`T_H\dot y'=x'`$ and $`G=1/(T_Hs)`$. Here $`T_H`$ is a holdup time when $`x',y'`$ are defined with compatible normalised units; $`A`$ in the dimensional level equation is an area, not a time.

**Step 2: derive transport delay.** For pipe length $`L`$, uniform constant velocity $`u`$, negligible axial mixing and heat exchange, a fluid element takes $`t_d=L/u`$ to reach the outlet. With inlet temperature deviation $`x'`$ and outlet $`y'`$, zero deviation history before the disturbance gives


**Equation (33)**

```math
y'(t)=\begin{cases}0,&t<t_d,\\x'(t-t_d),&t\geq t_d.\end{cases}
```


*Reason:* each outlet parcel carries its inlet condition from one transit time earlier. Substitute $`\theta=t-t_d`$ into the transform:


**Equation (34)**

```math
\bar y=\int_{t_d}^{\infty}x'(t-t_d)e^{-st}\,dt
=e^{-st_d}\int_0^{\infty}x'(\theta)e^{-s\theta}\,d\theta,
\qquad G_d(s)=e^{-st_d}.
```


*Reason:* the exponential factor accounts for the time shift and does not change the signal's eventual amplitude.

## Motivation and explanation

The integrator is not bounded-input bounded-output (BIBO) stable: a bounded nonzero constant input creates an unbounded ramp. Its zero-input level deviation remains constant, so it is neutrally stable in that state sense rather than an exponentially growing mode. It is not asymptotically stable or self-regulating. Real level is bounded by emptying or overflowing, where the ideal model stops applying.

A pure delay is BIBO stable and has unit steady gain. It is not a finite-order rational transfer function. A first-order lag begins changing immediately; a pure delay waits and then reproduces the input. Axial dispersion, wall heat exchange or velocity variation makes a real pipe more than a pure delay.

## Worked example

For $`A=2.00`$ m$`^2`$ and persistent net inflow $`0.00200`$ m$`^3`$ s$`^{-1}`$, level rises at $`0.00100`$ m s$`^{-1}`$ and increases by $`0.0600`$ m in $`60.0`$ s.

For a $`20.0`$ m pipe of diameter $`0.0400`$ m carrying $`0.00100`$ m$`^3`$ s$`^{-1}`$, cross-sectional velocity is $`0.795775`$ m s$`^{-1}`$ and transit time is $`25.1327`$ s. An ideal inlet temperature step reaches the outlet after that time with its original amplitude.

## Link to other topics

A gravity-draining tank introduces a level-dependent outflow and can become self-regulating. Transport delay matters in controller design because measurements may describe a condition created well before the current actuator command.

## Conclusion

A pole at zero represents accumulation without restoring action. The exponential delay factor represents travel time, not a slow approach to equilibrium.
<!-- note-content:end -->

[Previous](<PDC-09 - First-order step and impulse responses.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<../04 - Second-order dynamics and damping/PDC-11 - Second-order models, poles and damping regimes.md>)
