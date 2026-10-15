# PDC-11: Second-order models, poles and damping regimes

## Overview

Assumed: two coupled first-order balances and exponential solutions of linear ODEs.

Second-order behaviour requires two dynamic states or one second-order equation. Its pole pair determines whether deviations relax monotonically, decay while oscillating, persist, or grow.

## Intuition

Two tanks smooth a disturbance twice. A mass and spring exchange kinetic and elastic energy and can overshoot. Both have two states, but the mechanism of coupling decides whether oscillation is possible.

## Derivation

**Step 1: eliminate an intermediate tank state.** Let $x'$ be inlet deviation, $y'$ the first-tank outlet and $z'$ the second, with positive time constants $\tau_1,\tau_2$ and unity gains:

$$\tau_1\dot y'+y'=x',\qquad \tau_2\dot z'+z'=y'.
$$

*Reason:* each mixed-tank balance relaxes its state toward the upstream condition. Substitute $y'=\tau_2\dot z'+z'$ and its derivative into the first balance:

$$\tau_1\tau_2\ddot z'+(\tau_1+\tau_2)\dot z'+z'=x'.\tag{35}$$

**Step 2: define the standard form.** For a general ODE $a_2\ddot y'+a_1\dot y'+a_0y'=bx'$ with constant coefficients and $a_0\ne0$, the conventional form applies when $a_2/a_0>0$:

$$\tau^2\ddot y'+2\zeta\tau\dot y'+y'=K_px',\quad
\tau^2=a_2/a_0,\quad 2\zeta\tau=a_1/a_0,\quad K_p=b/a_0.\tag{36}$$

*Reason:* divide by $a_0$ and define $\tau>0$ as the second-order time scale and $\zeta$ as the dimensionless damping factor. For a forced mass–spring system $m\ddot y'+\mu\dot y'+ky'=F'$, $\tau=\sqrt{m/k}$, $\zeta=\mu/(2\sqrt{mk})$ and force-to-displacement gain is $1/k$. Weight has already cancelled when displacement is measured from equilibrium.

**Step 3: transform and find the poles.** Zero initial state and derivative give

$$G(s)=\frac{K_p}{\tau^2s^2+2\zeta\tau s+1},\qquad
p_{1,2}=\frac{-\zeta\pm\sqrt{\zeta^2-1}}{\tau}.\tag{37}$$

*Reason:* solve the quadratic characteristic equation; each root multiplies time in a free-response exponential.

| Damping | Pole pattern | Response of this constant-numerator model |
|---|---|---|
| $\zeta>1$ | Two negative real poles | Overdamped; monotonic stable step |
| $\zeta=1$ | Repeated pole $-1/\tau$ | Critically damped |
| $0<\zeta<1$ | Complex pair with negative real part | Decaying oscillations |
| $\zeta=0$ | Pair $\pm i/\tau$ | Undamped; persistent free oscillations |
| $\zeta<0$ | Poles with positive real part | Growing deviations |

*Reason:* the real part controls decay/growth and the imaginary part supplies oscillation frequency. At $\zeta=-1$, the repeated positive pole also gives instability.

Normalising by $a_0$ makes the final output/input ratio visible as $K_p=b/a_0$; matching the derivative coefficients then defines $\tau$ and $\zeta$. Do not read $a_1$ alone as a first-order time constant: both derivative terms jointly determine two poles. For a complex pair, $e^{(-\zeta/\tau+i\omega_d)t}$ separates into decay envelope $e^{-\zeta t/\tau}$ and oscillation. The envelope time is $\tau/\zeta$, while the oscillation period depends on $\omega_d$.

For the mass–spring analogy, displacement can keep increasing after crossing equilibrium because velocity is still positive: kinetic energy carries it past the target. Dissipation reduces that stored energy on each swing. Two sequential mixing tanks lack this inertial exchange mechanism; the downstream tank merely follows a progressively changing upstream input. The shared second-order equation does not make their physical couplings identical.

## Motivation and explanation

The natural angular frequency is $\omega_n=1/\tau$, in rad per unit time. The undamped period is $2\pi\tau$; $\tau$ itself is not an oscillation period.

For two passive lags, $\tau=\sqrt{\tau_1\tau_2}$ and $\zeta=(\tau_1+\tau_2)/(2\sqrt{\tau_1\tau_2})\geq1$, because $(\sqrt{\tau_1}-\sqrt{\tau_2})^2\geq0$. Thus a simple cascade of two positive lags cannot be underdamped. Equal lags are critically damped. Undamped poles are not BIBO stable, even though their free oscillations are bounded.

## Worked example

![Normalised second-order step responses at different damping factors](../figs/PDC-11-damping-regimes.png)

The graph uses $t/\tau$ horizontally and output normalised by its unit-step gain vertically. For two tanks with $\tau_1=20.0$ s and $\tau_2=80.0$ s, the combined time scale is $40.0$ s and $\zeta=1.25$. The poles are $-0.0500$ and $-0.0125$ s$^{-1}$: both modes decay without oscillation.

For $\tau=10.0$ s and $\zeta=0.500$, poles are $-0.0500\pm0.0866025i$ s$^{-1}$. The response oscillates with a decaying envelope rather than behaving like the two passive tanks.

Read the response graph in two parts: the common final normalised value expresses gain, while the curvature and crossings express damping. For the unequal tanks, the pole nearer zero, $-0.0125$ s$^{-1}$, corresponds to the slower $80.0$ s mode and governs the late tail when its coefficient is nonzero. For the complex example, the real part sets how quickly peaks shrink and the imaginary part sets how closely they are spaced.

## Link to other topics

Pole analysis generalises to higher-order models. Overshoot and decay ratio translate this second-order pole pair into directly observable response features.

## Conclusion

Second order describes the number of dynamic states; damping describes how their modes behave. The physical coupling determines which damping regimes are possible.
