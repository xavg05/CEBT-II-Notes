[Previous](<../02 - Physical balances and first-order dynamics/PDC-07 - Adiabatic discharge of a gas vessel.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<PDC-09 - First-order step and impulse responses.md>)

<!-- note-content:start -->
# PDC-08: Deviation variables and transfer-function assumptions

## Overview

Assumed: basic Laplace-transform rules.

A transfer function describes the forced response of a linear, time-invariant system with zero initial state deviations. Subtracting a steady operating point allows a physically nonzero concentration or temperature to have zero deviation.

## Intuition

The baseline is not the disturbance. A tank at a steady concentration already contains material; control asks how much its concentration changes when an input changes. Deviation variables remove the baseline while retaining exactly the perturbation we care about.

## Derivation

**Step 1: subtract the steady state.** For an inert mixed tank, $`\tau\dot c+c=c_0`$. At equilibrium $`c_s=c_{0s}`$. Define $`c'=c-c_s`$ and $`c_0'=c_0-c_{0s}`$. Substitution gives


**Equation (24)**

```math
\tau\dot c'+c_s+c'=c_{0s}+c_0'
\quad\Rightarrow\quad\tau\dot c'+c'=c_0'.
```


*Reason:* the steady values satisfy the original balance and cancel. A prime denotes deviation; a dot denotes time differentiation. They are different operations.

**Step 2: transform with the initial condition retained.** For any deviation output $`y'`$, write


**Equation (25)**

```math
\bar y(s)=\mathcal L[y']=\int_0^\infty y'(t)e^{-st}\,dt,
\qquad \mathcal L[\dot y']=s\bar y-y'(0^-).
```


*Reason:* integration by parts produces the initial-value term. The Laplace variable $`s`$ has inverse-time units. Transformed variables generally have their original units multiplied by time.

For $`\tau\dot y'+y'=K_px'`$,


**Equation (26)**

```math
\bar y=\frac{K_p}{\tau s+1}\bar x+
\frac{\tau y'(0^-)}{\tau s+1}.
```


*Reason:* collect $`\bar y`$ and isolate it. The first term is the input-driven response; the second is the free response to stored initial deviation. Set all initial state deviations to zero to define


**Equation (27)**

```math
G(s)=\left.\frac{\bar y}{\bar x}\right|_{\text{zero initial state deviations}}
=\frac{K_p}{\tau s+1}.
```


**Step 3: state the scope.** Constant coefficients and superposition define the linear, time-invariant model used here. A SISO transfer function relates one input–output pair. With multiple inputs, hold the other deviations at zero when defining each transfer-matrix element.

*Reason:* a raw ratio of output to one input with other inputs or initial-state effects present does not isolate that pair's dynamics.

Subtracting a baseline and neglecting an initial condition are separate decisions. Baseline subtraction is an exact change of coordinates. Zero initial deviation is justified only by actually starting at that baseline. If a tank begins above its chosen equilibrium, that stored excess relaxes even when the input deviation stays zero; the second term in equation (26) accounts for it. A transfer function isolates how the imposed input acts, so that free response is handled separately.

For a stable lag, the denominator $`\tau s+1`$ is the transformed competition between storage and removal. The transform has made a differential equation algebraic; it has not added a new physical mechanism. Returning to the time domain gives the same exponential relaxation derived by an integrating factor.

## Motivation and explanation

Subtraction gives zero initial deviations only when the process actually starts at the chosen equilibrium. If it starts elsewhere, include the free-response term. For a second-order ODE, both output and derivative initial conditions matter.

Zero initial state does not require a step input to have zero value or derivative immediately after $`t=0`$. A step deliberately jumps. Taking $`t=0`$ at the disturbance is a convenient origin, not a special physical assumption. A nonlinear model only gains a local transfer function after linearisation.

## Link to other topics

Deviation variables support both first-order response analysis and Taylor linearisation. A pole belongs to the process transfer function; additional factors in an input transform belong to the imposed signal.

## Conclusion

A transfer function separates process dynamics from baseline, initial conditions and input waveform. Preserve that distinction when interpreting its poles and gain.
<!-- note-content:end -->

[Previous](<../02 - Physical balances and first-order dynamics/PDC-07 - Adiabatic discharge of a gas vessel.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<PDC-09 - First-order step and impulse responses.md>)
