# PDC-09: First-order step and impulse responses

## Overview

Assumed: the transfer function of a self-regulating mixed or thermal tank.

For $G(s)=K_p/(\tau s+1)$ with $\tau>0$, gain sets the final response and time constant sets the speed. Step and impulse experiments expose different features of the same stored-state dynamics.

## Intuition

A persistent step keeps supplying a new condition until the tank settles. A brief pulse supplies a finite perturbation and then leaves the tank to relax. The response to the pulse therefore decays, while the step response accumulates that decaying response.

## Derivation

**Step 1: apply a step.** Let $H(t)$ be the unit Heaviside step and $x'=\Delta x H(t)$. For zero initial state, $\bar x=\Delta x/s$, so

$$\bar y=\frac{K_p\Delta x}{s(\tau s+1)}
=K_p\Delta x\left[\frac1s-\frac{1}{s+1/\tau}\right].\tag{28}$$

*Reason:* multiply the proposed partial fractions by $s(\tau s+1)$ to check that their numerator is one. Invert each term:

$$y'(t)=K_p\Delta x(1-e^{-t/\tau}),\quad
\dot y'(t)=\frac{K_p\Delta x}{\tau}e^{-t/\tau}.\tag{29}$$

*Reason:* the pole $-1/\tau$ generates a decaying exponential; the input's $1/s$ generates the constant final term.

**Step 2: interpret the time constant.** At $t=\tau$, the normalised response is $1-e^{-1}$. The initial tangent is $y'\approx (K_p\Delta x/\tau)t$, which meets the final response at $t=\tau$. To reach fraction $f$ of the final change, solve $f=1-e^{-t/\tau}$:

$$t_f=-\tau\ln(1-f),\qquad 0<f<1.\tag{30}$$

*Reason:* the remaining distance is an exponentially decaying fraction.

**Step 3: apply an impulse.** Let $\delta(t)$ be a unit-area Dirac impulse, with $\mathcal L[\delta]=1$. It is a distribution, not an ordinary finite-height signal. For impulse area $I_x$, $x'=I_x\delta(t)$ and

$$\bar y=I_xG(s),\qquad
 y'(t)=\frac{K_pI_x}{\tau}e^{-t/\tau}\quad(t\geq0).\tag{31}$$

*Reason:* invert the single first-order pole. Since $\delta$ has inverse-time units, $I_x$ has input units times time. Integrating the ODE across the impulse gives $\tau[y'(0^+)-y'(0^-)]=K_pI_x$, confirming the output jump.

## Motivation and explanation

A lag begins responding immediately; its delayed approach is not dead time. Negative $K_p$ reverses the response direction but does not change stability when $\tau>0$. Comparing the magnitude of gain with one makes sense only after accounting for units or using a consistent scaling.

The unit-step derivative is the unit-impulse response for this zero-state LTI system. Its impulse-response area is $K_p$. Real pulses approximate the impulse only when their duration is short relative to the dynamics and they do not appreciably change the process parameters.

## Worked example

With $K_p=2.00$, $\tau=20.0$ s and step $\Delta x=3.00$ in input units, the final output change is $6.00$ and $y'(20)=3.79272$ in output units. For a unit-area input pulse, $y'(20)=0.0367879$ in the corresponding output units.

A first-order response reaches $63.2121\%$ of its final change at one time constant, $95.0213\%$ at three and $99.3262\%$ at five. For $\tau=100$ s, the exact time to $95\%$ is $299.573$ s.

## Link to other topics

An integrator responds to a step with continuing accumulation instead of settling. Cascading several lags changes the early response and creates higher-order dynamics.

## Conclusion

The step measures steady sensitivity and relaxation speed; the impulse isolates the decaying response to a finite input area.
