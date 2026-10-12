[Previous](<../01 - Control objectives, variables and dynamic modelling/PDC-03 - CSTR variable identification and dynamic model closure.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<PDC-05 - Variable-volume tanks and finite pulse balances.md>)

<!-- note-content:start -->
# PDC-04: Mixing tanks and reacting first-order lags

## Overview

Assumed: an isothermal CSTR balance and first-order reaction kinetics.

A well-mixed tank converts inlet-composition changes into a first-order lag. Adding reaction changes both the steady gain and the time constant; the hydrodynamic residence time remains $V/q$.

## Intuition

Mixing spreads the arrival of new feed through existing contents. A change is felt immediately, but the old contents are only gradually displaced. Reaction removes A as well as flow removing it, so a concentration deviation disappears faster and a feed increase produces a smaller final concentration increase.

## Derivation

**Step 1: balance inert solute.** With fixed volume $V$, flow $q$, inlet concentration $c_0$ and uniform tank/outlet concentration $c$, assume constant density, no reaction and perfect mixing:

$$V\dot c=q(c_0-c),\qquad \tau\dot c+c=c_0,\quad \tau=V/q.\tag{8}$$

*Reason:* divide the accumulation balance by $q$ to expose the residence time $\tau$.

**Step 2: solve a feed step.** Initially $c=c_s=c_{0s}$. For $t\geq0$, the inlet changes permanently by $\Delta c_0$. Set $c'=c-c_s$; then $\tau\dot c'+c'=\Delta c_0$ with $c'(0)=0$. Multiply by integrating factor $e^{t/\tau}$:

$$\frac{d}{dt}(e^{t/\tau}c')=\frac{\Delta c_0}{\tau}e^{t/\tau}.
$$

*Reason:* the product derivative collects the derivative and concentration terms. Integration from zero to $t$ gives $e^{t/\tau}c'=\Delta c_0(e^{t/\tau}-1)$, hence

$$c'=\Delta c_0(1-e^{-t/\tau}).\tag{9}$$

**Step 3: include first-order consumption.** For constant rate constant $k>0$, add loss $kVc$:

$$V\dot c=q(c_0-c)-kVc,
\qquad \frac{\tau}{1+k\tau}\dot c+c=\frac{c_0}{1+k\tau}.\tag{10}$$

*Reason:* collect both removal mechanisms and divide by their combined coefficient. Thus the effective time constant is $\tau_r=\tau/(1+k\tau)$ and concentration gain is $K_p=1/(1+k\tau)$.

**Step 4: transform the perturbation balance.** Define $\bar c=\mathcal L[c']$ and $\bar c_0=\mathcal L[c_0']$, where primes mean deviations from the reacting steady state. With zero initial deviation,

$$\frac{\bar c}{\bar c_0}=\frac{1}{\tau s+1+k\tau}
=\frac{K_p}{\tau_rs+1},\qquad p=-\frac{1+k\tau}{\tau}.\tag{11}$$

*Reason:* the Laplace transform replaces $\dot c'$ by $s\bar c$. The pole $p$ gives the exponential decay rate.

## Motivation and explanation

The inert tank has unit concentration gain and pole $-1/\tau$. Reaction moves the pole farther left and reduces the gain. A faster response therefore does not imply more reactant survives. Taking $k\rightarrow0$ recovers the inert-tank model.

These conclusions require constant $q,V,k$ and negligible thermal coupling. Changing temperature or flow generally changes the coefficients; second-order kinetics requires local linearisation.

## Worked example

Let $V=2.00$ m$^3$, $q=0.0200$ m$^3$ s$^{-1}$, so $\tau=100$ s. A feed step of $3.00$ mol m$^{-3}$ gives inert-tank deviation $c'(100)=1.89636$ mol m$^{-3}$ and final deviation $3.00$ mol m$^{-3}$.

With $k=0.0100$ s$^{-1}$, $K_p=0.500$, $\tau_r=50.0$ s and $p=-0.0200$ s$^{-1}$. The same feed step gives final deviation $1.50$ mol m$^{-3}$ and $c'(50)=0.948181$ mol m$^{-3}$.

## Link to other topics

The inert-tank impulse response also describes a CSTR residence-time distribution. The same first-order structure occurs when heat transfer relaxes a sensor toward the bath temperature.

## Conclusion

Flow and reaction determine the coefficient of concentration removal. That coefficient controls both the pole and the steady response to feed composition.
<!-- note-content:end -->

[Previous](<../01 - Control objectives, variables and dynamic modelling/PDC-03 - CSTR variable identification and dynamic model closure.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<PDC-05 - Variable-volume tanks and finite pulse balances.md>)
