[Previous](<PDC-18 - Zeros, direct feedthrough and inverse response.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<../08 - Linearisation around an operating point/PDC-20 - Local linearisation and reaction-order comparison.md>)

<!-- note-content:start -->
# PDC-19: Steady-state gain and the final-value theorem

## Overview

Assumed: Laplace transforms of step inputs.

Steady-state gain is the change in settled output per change in settled input. Evaluating $G(0)$ gives this gain only when the relevant response actually settles; an algebraic limit alone cannot prove that it does.

## Intuition

A constant input eventually leaves only a constant balance if all transient modes decay. Gain is the sensitivity of that remaining balance. If a mode grows or keeps oscillating, there is no settled output to interpret.

## Derivation

**Step 1: read the gain from a balance.** For $\tau\dot y'+y'=K_px'$, a final constant input $\Delta x$ and settled output $\Delta y$ satisfy $\Delta y=K_p\Delta x$.

*Reason:* a steady state has zero derivative. Gain has output/input units; it need not be dimensionless.

**Step 2: use the transform.** The final-value theorem states, under its validity conditions,

$$\lim_{t\to\infty}y'(t)=\lim_{s\to0}s\bar y(s).\tag{59}$$

For a proper rational signal transform, a standard sufficient condition is that all poles of $s\bar y$ lie strictly in the left half-plane after cancellations. Equivalently, $\bar y$ may have a simple pole at the origin for a constant final value, but no other nondecaying modes. A finite causal delay preserves a settling signal's endpoint.

*Reason:* the theorem requires decay of every nonconstant term. Check the complete output transform, including the imposed input and any initial-state contribution, rather than only one process denominator.

**Step 3: specialise to a step.** For zero-state $\bar y=G(s)\Delta x/s$,

$$\Delta y=\Delta x\lim_{s\to0}G(s),\qquad
K_p=G(0),\tag{60}$$

provided the step response settles and the limit is finite.

*Reason:* the step's $1/s$ factor cancels the theorem's factor $s$. For a stable MIMO model, applying a step in one input at a time gives the gain matrix $\boldsymbol G(0)$. Integrating output paths generally lack a finite steady gain.

Evaluating at $s=0$ removes derivative factors, which is why it reproduces the static balance when a static balance is actually reached. The final-value theorem makes that connection precise; it does not supply decay that the process lacks. A unit step has transform $1/s$, so $s\bar y=G(s)$ for that experiment, and the stability condition must be checked before taking its limit.

Gain and speed can change independently. Multiplying a stable transfer function by a constant scales its endpoint without moving its poles. Adding pure delay shifts its timing without changing $G(0)$. Moving a pole while adjusting the numerator can change speed at fixed gain. A final-value calculation deliberately discards transient detail and must be paired with a dynamics check when timing matters.

## Motivation and explanation

A lag's pole comes from the process; a simple $1/s$ in the output transform may merely come from a step input. Confusing them would label a settling step response unstable.

A pure transport delay satisfies $e^{-t_ds}\rightarrow1$ at $s=0$. It changes timing but not steady gain. In an unstable model, a finite $G(0)$ does not establish an attainable endpoint.

## Worked example

Take

$$G(s)=\frac{10e^{-5s}}{(s+1)(s+5)(s+10)},\qquad
x'(t)=1-e^{-t/10},\quad \bar x=\frac1{s(10s+1)}.
$$

The nonconstant modes have negative poles $-1,-5,-10,-0.1$, and the delay is finite. Hence

$$y'(\infty)=\lim_{s\to0}\frac{10e^{-5s}}{(10s+1)(s+1)(s+5)(s+10)}=0.200.
$$

For contrast, $G(s)=1/(s-1)$ with a unit step gives $y'=e^t-1$. The algebraic value $G(0)=-1$ is finite, but the positive pole prevents a final value; using the theorem to claim $y'(\infty)=-1$ would be invalid.

## Link to other topics

Linearisation produces local gains that are derivatives of nonlinear steady relations. Controller decisions require that endpoint information together with transient poles, zeros and delay.

## Conclusion

Check settling conditions before evaluating the endpoint. Once they hold, the final-value theorem avoids solving an entire transient just to find its final change.
<!-- note-content:end -->

[Previous](<PDC-18 - Zeros, direct feedthrough and inverse response.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<../08 - Linearisation around an operating point/PDC-20 - Local linearisation and reaction-order comparison.md>)
