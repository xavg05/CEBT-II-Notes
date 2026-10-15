[Previous](<../01 - Control objectives, variables and dynamic modelling/PDC-03 - CSTR variable identification and dynamic model closure.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<PDC-05 - Variable-volume tanks and finite pulse balances.md>)

<!-- note-content:start -->
# PDC-04: Mixing tanks and reacting first-order lags

## Overview

Assumed: an isothermal CSTR balance and first-order reaction kinetics.

A well-mixed tank converts inlet-composition changes into a first-order lag. Adding reaction changes both the steady gain and the time constant; the hydrodynamic residence time remains $`V/q`$.

## Intuition

Mixing spreads the arrival of new feed through existing contents. A change is felt immediately, but the old contents are only gradually displaced. Reaction removes A as well as flow removing it, so a concentration deviation disappears faster and a feed increase produces a smaller final concentration increase.

## Derivation

**Step 1: balance inert solute.** With fixed volume $`V`$, flow $`q`$, inlet concentration $`c_0`$ and uniform tank/outlet concentration $`c`$, assume constant density, no reaction and perfect mixing:


**Equation (8)**

```math
V\dot c=q(c_0-c),\qquad \tau\dot c+c=c_0,\quad \tau=V/q.
```


*Reason:* fixed volume gives $`d(Vc)/dt=V\dot c`$. Dividing by $`q`$ makes the coefficient of $`c`$ equal to one. In the standard first-order form $`\tau\dot c+c=K_pc_0`$, the derivative coefficient is the time constant and the right-side coefficient is the gain. Setting $`\dot c=0`$ gives $`c=c_0`$, so an inert tank has unit gain.

The ratio $`V/q`$ is also the mean residence time: stored liquid volume divided by volume replaced each second. Perfect mixing allows some new feed to leave quickly and some to remain longer, so it is an average, not an identical transit time for every fluid element.

**Step 2: solve a feed step.** Initially $`c=c_s=c_{0s}`$. For $`t\geq0`$, the inlet changes permanently by $`\Delta c_0`$. Set $`c'=c-c_s`$; then $`\tau\dot c'+c'=\Delta c_0`$ with $`c'(0)=0`$. Subtracting the old steady balance removes constant terms; because the tank starts there, its initial deviation is zero. First divide the ODE by $`\tau`$, then multiply by $`e^{t/\tau}`$:


```math
\frac{d}{dt}(e^{t/\tau}c')=\frac{\Delta c_0}{\tau}e^{t/\tau}.
```


*Reason:* the product rule gives $`d(e^{t/\tau}c')/dt=e^{t/\tau}\dot c'+e^{t/\tau}c'/\tau`$, exactly the left side after multiplication. The integrating factor is chosen to create that exact derivative. Integration from zero to $`t`$ gives $`e^{t/\tau}c'=\Delta c_0(e^{t/\tau}-1)`$, hence


**Equation (9)**

```math
c'=\Delta c_0(1-e^{-t/\tau}).
```


**Step 3: include first-order consumption.** For constant rate constant $`k>0`$, add loss $`kVc`$:


**Equation (10)**

```math
V\dot c=q(c_0-c)-kVc,
\qquad \frac{\tau}{1+k\tau}\dot c+c=\frac{c_0}{1+k\tau}.
```


*Reason:* reaction consumes $`kc`$ per unit volume, hence $`kVc`$ in the whole tank. Collecting terms gives $`V\dot c+(q+kV)c=qc_0`$. Divide by the coefficient of $`c`$, namely $`q+kV`$, to put this in standard form:


```math
\tau_r=\frac{V}{q+kV}=\frac{\tau}{1+k\tau},\qquad
K_p=\frac{q}{q+kV}=\frac{1}{1+k\tau}.
```


The same total removal coefficient appears below both ratios. Storage divided by removal sets the response time; input coefficient divided by removal sets the settled sensitivity. These are different properties even though reaction reduces both here.

**Step 4: transform the perturbation balance.** The reacting equilibrium is $`c_s=c_{0s}/(1+k\tau)`$, so it differs from the inert equilibrium. Subtracting it gives $`\tau\dot c'+(1+k\tau)c'=c_0'`$. Define $`\bar c=\mathcal L[c']`$ and $`\bar c_0=\mathcal L[c_0']`$, where primes mean deviations from the reacting steady state. With zero initial deviation,


**Equation (11)**

```math
\frac{\bar c}{\bar c_0}=\frac{1}{\tau s+1+k\tau}
=\frac{K_p}{\tau_rs+1},\qquad p=-\frac{1+k\tau}{\tau}.
```


*Reason:* with zero initial deviation, the transform gives $`[\tau s+1+k\tau]\bar c=\bar c_0`$. Dividing isolates the output/input ratio. The pole is the value making the denominator zero. Its free-response term is $`e^{pt}`$, so a negative pole gives decay, and a more negative pole gives faster decay. Setting $`s=0`$ gives $`G(0)=K_p`$, the settled gain for this stable lag.

## Motivation and explanation

An excess of A can disappear by washout and by reaction. Both sinks strengthen the restoring effect, shortening the concentration response. At steady state, however, feed A must supply both sinks: $`qc_0=(q+kV)c`$. Only the fraction $`q/(q+kV)`$ leaves unreacted, which explains the smaller concentration gain.

The dimensionless group $`k\tau`$, the Damköhler number for this model, compares the reaction timescale with the flow-through timescale. When $`k\tau\ll1`$, washout dominates and $`K_p\to1`$, $`\tau_r\to\tau`$. When $`k\tau\gg1`$, little A survives, $`K_p\approx1/(k\tau)`$, and $`\tau_r\to1/k`$. The fluid's mean residence time is still $`V/q`$; reaction shortens the concentration memory without speeding up the liquid flow.

These conclusions require constant $`q,V,k`$ and negligible thermal coupling. If flow becomes another changing input, $`qc`$ contains a product of changing variables; a local model drops the product of their deviations. A prescribed new constant flow still permits a lag model, but with new coefficients. Temperature-dependent kinetics couples concentration to the energy balance. Second-order consumption $`kc^2`$ has local slope $`2kc_s`$, so its linearised response depends on the chosen operating concentration.

## Worked example

Let $`V=2.00`$ m$`^3`$, $`q=0.0200`$ m$`^3`$ s$`^{-1}`$, so $`\tau=100`$ s. A feed step of $`3.00`$ mol m$`^{-3}`$ gives inert-tank deviation $`c'(100)=1.89636`$ mol m$`^{-3}`$ and final deviation $`3.00`$ mol m$`^{-3}`$.

With $`k=0.0100`$ s$`^{-1}`$, $`K_p=0.500`$, $`\tau_r=50.0`$ s and $`p=-0.0200`$ s$`^{-1}`$. The same feed step gives final deviation $`1.50`$ mol m$`^{-3}`$ and $`c'(50)=0.948181`$ mol m$`^{-3}`$.

Both responses reach $`63.2121\%`$ of their own final change at their own time constant. The reacting tank reaches that fraction sooner, but its final increase is only half as large. For a common $`95\%`$ settling criterion, the inert and reacting times are $`299.573`$ s and $`149.787`$ s respectively. Neither response finishes exactly at a finite time. The initial slopes are equal here: $`\Delta c_0/\tau=K_p\Delta c_0/\tau_r=0.0300`$ mol m$`^{-3}`$ s$`^{-1}`$. Reaction changes the subsequent curvature and endpoint, while the unchanged feed step sets the same initial accumulation rate.

## Link to other topics

The inert-tank impulse response also describes a CSTR residence-time distribution. The same first-order structure occurs when heat transfer relaxes a sensor toward the bath temperature.

## Conclusion

Flow and reaction determine the coefficient of concentration removal. That coefficient controls both the pole and the steady response to feed composition.
<!-- note-content:end -->

[Previous](<../01 - Control objectives, variables and dynamic modelling/PDC-03 - CSTR variable identification and dynamic model closure.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<PDC-05 - Variable-volume tanks and finite pulse balances.md>)
