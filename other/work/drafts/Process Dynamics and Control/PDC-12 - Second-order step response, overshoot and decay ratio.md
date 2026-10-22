# PDC-12: Second-order step response, overshoot and decay ratio

## Overview

Assumed: the standard second-order model with constant numerator, no zeros or dead time, and zero initial output and derivative.

Deriving the step response makes overshoot, oscillation period and decay ratio consequences of the pole pair. These relations apply to the standard model, not every process with two poles.

## Intuition

The steady response is a constant particular solution. The transient is the free mode needed to match the starting state. In an underdamped process, that free mode repeatedly crosses the final value while losing amplitude.

## Derivation

**Step 1: separate steady and transient parts.** Let the input step be $\Delta x$ and normalise $r(t)=y'(t)/(K_p\Delta x)$, with nonzero $K_p\Delta x$. Then $\tau^2\ddot r+2\zeta\tau\dot r+r=1$. For distinct poles, write $r=1+C_1e^{p_1t}+C_2e^{p_2t}$. Initial conditions require

$$C_1+C_2=-1,\qquad p_1C_1+p_2C_2=0.
$$

*Reason:* neither output nor its first derivative can jump under a finite step for this strictly proper second-order model. Solving these two equations gives

$$r=1+\frac{p_2e^{p_1t}-p_1e^{p_2t}}{p_1-p_2}.\tag{38}$$

**Step 2: handle the repeated root.** At $\zeta=1$, $p=-1/\tau$ and the transient has form $(C_1+C_2t)e^{-t/\tau}$. Enforcing $r(0)=\dot r(0)=0$ gives $C_1=-1$, $C_2=-1/\tau$, so

$$r=1-(1+t/\tau)e^{-t/\tau}.\tag{39}$$

*Reason:* repeated roots need a polynomial factor; simply setting the two exponential coefficients equal would lose one independent solution.

**Step 3: use complex poles.** For $0<\zeta<1$, define $a=\zeta/\tau$ and $\omega_d=\sqrt{1-\zeta^2}/\tau$. Write $r=1+e^{-at}(C\cos\omega_dt+D\sin\omega_dt)$. The same initial conditions give $C=-1$ and $D=-a/\omega_d$, hence

$$r=1-e^{-\zeta t/\tau}\left[\cos(\omega_dt)+
\frac{\zeta}{\sqrt{1-\zeta^2}}\sin(\omega_dt)\right].\tag{40}$$

*Reason:* conjugate modes combine into a real damped sinusoid.

**Step 4: locate the first peak.** Differentiate the preceding result; cosine terms cancel:

$$\dot r=\frac{e^{-\zeta t/\tau}}{\tau\sqrt{1-\zeta^2}}\sin(\omega_dt).
$$

*Reason:* extrema occur at zero sine. The first peak is at $t_p=\pi/\omega_d$, where cosine is $-1$. If $B=|K_p\Delta x|$ is the total steady change and $A$ is the first peak's excess magnitude above the final value,

$$\frac AB=\exp\left[-\frac{\pi\zeta}{\sqrt{1-\zeta^2}}\right],\qquad
t_p=\frac{\pi\tau}{\sqrt{1-\zeta^2}}.\tag{41}$$

**Step 5: compare successive peaks on the same side.** They are separated by $T=2\pi/\omega_d$. If $C$ is the next same-side peak's excess magnitude, its envelope has fallen by $e^{-aT}$:

$$\frac CA=\exp\left[-\frac{2\pi\zeta}{\sqrt{1-\zeta^2}}\right]
=\left(\frac AB\right)^2,\qquad
T=\frac{2\pi\tau}{\sqrt{1-\zeta^2}}.\tag{42}$$

*Reason:* compare peaks measured relative to the final value, not their absolute heights. Consecutive extrema on opposite sides are only half a period apart.

The constant $1$ in the normalised solution is the forced equilibrium. The transient starts at $-1$ to cancel it at $t=0$ and must also match the zero initial slope. This is why the oscillatory part is not an arbitrary sine curve placed around the endpoint: its sine and cosine weights are fixed by the starting state. As $t$ grows, the transient decays and leaves the forced equilibrium.

At the first peak the response has travelled half an oscillation period. There the sine term is zero and the cosine is $-1$, so the excess above the final value equals the exponential decay factor at that instant. Successive peaks on the same side are a full period apart, so their excesses shrink by the full-period decay factor. In the figure, measure excesses from the final-value line; measuring peak heights from zero would mix the steady part into the transient ratio.

## Motivation and explanation

![Definitions of overshoot, steady change and successive-peak decay](../figs/PDC-12-overshoot-and-period.png)

The horizontal reference through the oscillations represents the final value; $B$ spans the initial-to-final change. For negative gain, reflect the response and use magnitudes in the overshoot ratio.

Taking $\zeta\rightarrow0$ gives $r=1-\cos(t/\tau)$, with no final settled value. Taking $\zeta\rightarrow1$ requires the repeated-root limit rather than substituting into a singular-looking expression. Zeros or delays alter measured response shape and invalidate a blind fit of these formulas.

### Comparing a repeated lag with a single lag

For critical damping the normalised response at $t=\tau$ is $1-2e^{-1}\approx0.264241$. Its zero initial slope reflects sequential storage: the second state first needs a change in the first state to drive it. There is no exact waiting interval. In an oscillatory response, overshoot is the peak's excess above the final value divided by the initial-to-final change; a same-side decay ratio compares successive excesses above that reference, rather than successive absolute peak heights.

## Link to other topics

Observed oscillation can reveal a complex pole pair. Cascaded tank examples illustrate the critically damped formula without requiring a mechanical analogy.

## Conclusion

Overshoot comes from the transient mode carrying the output past its steady value. Pole decay and frequency determine the excess peak and the spacing between peaks.
