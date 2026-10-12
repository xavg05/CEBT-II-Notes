[Previous](<../07 - Poles, zeros, stability and steady-state gain/PDC-19 - Steady-state gain and the final-value theorem.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<PDC-21 - Gravity-draining tank — linear model and exact response.md>)

<!-- note-content:start -->
# PDC-20: Local linearisation and reaction-order comparison

## Overview

Assumed: Taylor expansion, partial derivatives and reactor balances.

Linearisation replaces a nonlinear model by its tangent dynamics at one operating point. The steady state cancels, while the local slopes become gain and decay coefficients. The approximation is valid for sufficiently small deviations.

## Intuition

A curved relationship can look almost straight over a narrow interval. Control near a fixed set point uses that local slope, not a single straight line for every possible operating condition. Moving the operating point can change both sensitivity and response speed.

## Derivation

**Step 1: define linearity.** An operator $`F`$ is linear if $`F(au+bv)=aF(u)+bF(v)`$ for constants $`a,b`$. Powers and products of changing variables generally violate this property. A coefficient that depends on time may preserve linearity but loses time invariance.

**Step 2: expand a dynamic model.** Let output/state $`y`$ obey $`\dot y=f(y,x)`$ for input $`x`$. Choose a constant equilibrium $`(y_s,x_s)`$ with $`f(y_s,x_s)=0`$; define $`y'=y-y_s`$, $`x'=x-x_s`$. Taylor expansion gives


**Equation (61)**

```math
\dot y'\approx f(y_s,x_s)+f_y|_s\,y'+f_x|_s\,x'
=f_y|_s\,y'+f_x|_s\,x'.
```


*Reason:* the constant term vanishes at equilibrium, and terms quadratic or higher in deviations are neglected. Subscripts on $`f`$ denote partial derivatives, evaluated at the operating point. With additional disturbance $`d`$, add $`f_d|_s d'`$; with several states, use the matrix of partial derivatives.

**Step 3: expose the local transfer function.** Write $`a=f_y|_s`$, $`b=f_x|_s`$. For zero initial deviation,


**Equation (62)**

```math
G(s)=\frac{b}{s-a}.
\quad\text{If }a<0:\quad \tau=-1/a,\quad K_p=-b/a.
```


*Reason:* transform $`\dot y'=ay'+bx'`$ and isolate the output. The local restoring slope $`a`$ determines the pole. If $`a=0`$, the first-order model is an integrator and higher-order terms may be decisive for nonlinear stability.

**Step 4: compare reaction orders.** For fixed $`q,V,T`$ and $`\tau=V/q`$, first-order consumption gives $`\tau\dot c_A+(1+k_1\tau)c_A=c_{A0}`$, exactly linear in these concentration variables.

Second-order consumption gives $`\tau\dot c_A+c_A+k_2\tau c_A^2=c_{A0}`$. At its equilibrium, $`c_{A0s}=c_{As}+k_2\tau c_{As}^2`$. Substitute $`c_A=c_{As}+c_A'`$:


```math
\tau\dot c_A'+(1+2k_2\tau c_{As})c_A'+k_2\tau(c_A')^2=c_{A0}'.
```


*Reason:* expand the square and cancel the steady balance. Neglect the final quadratic term to obtain


**Equation (63)**

```math
G(s)\approx\frac1{\tau s+1+2k_2\tau c_{As}},\quad
\tau_{lin}=\frac{\tau}{1+2k_2\tau c_{As}},\quad
K_p=\frac1{1+2k_2\tau c_{As}}.
```


*Reason:* the derivative of the reaction sink is $`2k_2c_{As}`$, not $`k_2c_{As}`$.

## Motivation and explanation

The approximation discards the curvature, not the physical meaning of the original balance. Second-order $`k_2`$ has units concentration$`^{-1}`$ time$`^{-1}`$; $`k_1`$ has inverse-time units. Constant-temperature first-order reaction is linear, but a temperature-dependent Arrhenius rate introduces nonlinear coupling if temperature is a changing state.

The neglected quadratic reaction term is small relative to its first-order reaction perturbation when $`|c_A'|\ll2c_{As}`$. Near $`c_{As}=0`$, that particular comparison fails and one must inspect the full balance instead. A Taylor model says little about distant equilibria or large excursions.

## Worked example

Let $`\tau=100`$ s, $`k_2=0.0100`$ m$`^3`$ mol$`^{-1}`$ s$`^{-1}`$ and $`c_{As}=1.00`$ mol m$`^{-3}`$. The corresponding feed equilibrium is $`c_{A0s}=2.00`$ mol m$`^{-3}`$. Linearisation gives $`\tau_{lin}=33.3333`$ s and $`K_p=0.333333`$.

At unchanged operating conditions, a sufficiently small feed-composition increase has one-third of that increase in its final reactor concentration. Linearising about a different $`c_{As}`$ gives different coefficients; this is a local model rather than a globally linear reaction.

## Link to other topics

The same Taylor procedure converts a gravity-outflow tank into a lag. Products of valve flow and concentration require it in the three-tank mixing process.

## Conclusion

Linearise only after finding a consistent equilibrium. The local derivatives identify the restoring mode and steady sensitivity of small disturbances.
<!-- note-content:end -->

[Previous](<../07 - Poles, zeros, stability and steady-state gain/PDC-19 - Steady-state gain and the final-value theorem.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<PDC-21 - Gravity-draining tank — linear model and exact response.md>)
