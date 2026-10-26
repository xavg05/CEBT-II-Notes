# PDC: Example Sheet 0

Supervision questions on Laplace transforms, transfer functions, frequency response and CSTR balances. Worked answers come first, then the ideas that came up while doing them.

Assumed: Year 1–2 Laplace transforms, partial fractions and linear ODEs.

## Worked answers

### Q1. Partial fractions by the cover-up rule

Expand $\dfrac{1}{s(\tau s+1)}$, then $\dfrac{1}{s(\tau s+1)^2}$, then $\dfrac{1}{s(\tau s+1)^n}$.

$$\frac{1}{s(\tau s+1)^n} = \frac{1}{s} - \sum_{k=1}^{n}\frac{\tau}{(\tau s+1)^k}$$

The cases $n=1$ and $n=2$ are the first one and two terms of the sum. For example, $\dfrac{1}{s(\tau s+1)} = \dfrac{1}{s} - \dfrac{\tau}{\tau s+1}$.

### Q2. Inverse transform of a repeated pole

Find $\mathcal{L}[e^{-\alpha t}]$, then differentiate with respect to $\alpha$ to invert $1/(s+\alpha)^2$ and $1/(s+\alpha)^n$.

$\mathcal{L}[e^{-\alpha t}] = 1/(s+\alpha)$. Each differentiation with respect to $\alpha$ brings down a factor of $-t$ on the left and $-k/(s+\alpha)^{k+1}$ on the right. Repeating this $n-1$ times gives

$$\mathcal{L}^{-1}\!\left[\frac{1}{(s+\alpha)^n}\right] = \frac{t^{\,n-1}e^{-\alpha t}}{(n-1)!}$$

### Q3. Inverse transforms

| Transform | Inverse |
|---|---|
| $\dfrac{5}{(s+4)(s+1)}$ | $\tfrac{5}{3}\left(e^{-t}-e^{-4t}\right)$ |
| $\dfrac{1}{(s+1)^2(s+2)}$ | $te^{-t} - e^{-t} + e^{-2t}$ |
| $\dfrac{1}{s^2+4s+5}$ | $e^{-2t}\sin t$ |
| $\dfrac{2s^2-3s}{(s+1)^2(s+2)}$ | $5te^{-t} - 12e^{-t} + 14e^{-2t}$ |

For the third row, complete the square: $s^2+4s+5 = (s+2)^2+1$, then use the frequency-shift rule.

### Q4. First-order lag as a convolution

Find the transfer function for $\tau\dot y + y = x$, write the solution as a convolution, compare with the integrating-factor solution (with $y(0)=0$), and evaluate for $x=1$.

**Transfer function.** Deviation variables are not needed: the ODE has no constant term and $y(0)=0$, so the absolute variables already have zero initial conditions. Transforming gives $(\tau s+1)Y = X$:

$$G(s) = \frac{1}{\tau s+1}$$

**Convolution.** The inverse of $G$ is the impulse response, $g(t) = \frac{1}{\tau}e^{-t/\tau}$. Since $Y=GX$, the convolution theorem gives

$$y(t) = \int_0^t \frac{1}{\tau}e^{-(t-t')/\tau}\,x(t')\,dt'$$

**Integrating factor.** Divide by $\tau$ to get standard form, $\dot y + y/\tau = x/\tau$. The integrating factor $e^{t/\tau}$ turns the left side into an exact derivative:

$$\frac{d}{dt}\left(y\,e^{t/\tau}\right) = \frac{1}{\tau}\,x(t)\,e^{t/\tau}$$

Integrate from $0$ to $t$ with dummy variable $t'$, use $y(0)=0$, and multiply by $e^{-t/\tau}$. This gives the same integral as the convolution. The integrating factor is doing the convolution.

**Unit step.** With $x=1$:

$$y(t) = \frac{1}{\tau}e^{-t/\tau}\cdot\tau\left(e^{t/\tau}-1\right) = 1 - e^{-t/\tau}$$

### Q5. Second-order step response two ways

Find the transfer function for $6\ddot y + 5\dot y + y = x$, evaluate for $x=1$, and compare with the complementary function plus particular integral, with $y(0)=\dot y(0)=0$.

**Transfer function.** Both initial conditions are zero and there is no constant term, so again deviation variables change nothing:

$$G(s) = \frac{1}{6s^2+5s+1} = \frac{1}{(3s+1)(2s+1)}$$

**Laplace step response.** Cover-up gives coefficients $-9$ (at $s=-\tfrac13$) and $4$ (at $s=-\tfrac12$):

$$Y = \frac{1}{s(3s+1)(2s+1)} = \frac{1}{s} - \frac{9}{3s+1} + \frac{4}{2s+1} \quad\Rightarrow\quad y(t) = 1 - 3e^{-t/3} + 2e^{-t/2}$$

**Complementary function plus particular integral.**

- Auxiliary equation: $6m^2+5m+1 = (3m+1)(2m+1) = 0$, so $m=-\tfrac13, -\tfrac12$ and $y_{CF} = Ae^{-t/3} + Be^{-t/2}$.
- Particular integral: try $y=C$. Both derivatives vanish, so $C=1$.
- Initial conditions: $y(0)=0$ gives $1+A+B=0$. $\dot y(0)=0$ gives $-A/3 - B/2 = 0$, so $B = -\tfrac23A$. Substituting, $A/3 = -1$, so $A=-3$ and $B=2$.

This gives the same $y(t)$.

**Checks.** $y(0) = 1-3+2 = 0$, $\dot y(0) = 1-1 = 0$, and $y\to1 = G(0)$, the steady-state gain. The Laplace method finds the coefficients in one step because the initial conditions are already in the transform. The ODE method has to fit them separately as simultaneous equations.

### Q7. Response to a sinusoid

The process $\ddot y + 3\dot y + 2y = x$ has input $x=\cos\omega t$. Find the output for large $t$ (i) from the ODE directly and (ii) from the frequency response theorem.

**(i) ODE directly.** The auxiliary equation $(m+1)(m+2)=0$ gives $y_{CF} = Ae^{-t} + Be^{-2t}$. Both roots are negative, so this decays whatever the initial conditions. That is why only the particular integral is needed, and why no initial conditions are given. The slowest term is $e^{-t}$, so "large $t$" means $t\gg1$.

Try $y = a\cos\omega t + b\sin\omega t$ and match coefficients:

$$\cos\omega t:\ a(2-\omega^2) + 3\omega b = 1, \qquad \sin\omega t:\ b(2-\omega^2) - 3\omega a = 0$$

The denominator factorises, $(2-\omega^2)^2+9\omega^2 = (\omega^2+1)(\omega^2+4)$, giving

$$y(t) = \frac{(2-\omega^2)\cos\omega t + 3\omega\sin\omega t}{(\omega^2+1)(\omega^2+4)}$$

**(ii) Frequency response theorem.** The transfer function $G(s) = \dfrac{1}{(s+1)(s+2)}$ has poles at $-1$ and $-2$, so the system is stable and the theorem applies.

$$|G(i\omega)| = \frac{1}{\sqrt{(1+\omega^2)(4+\omega^2)}}, \qquad \arg G(i\omega) = -\arctan\omega - \arctan\frac{\omega}{2}$$

$$y(t) = \frac{1}{\sqrt{(1+\omega^2)(4+\omega^2)}}\cos\!\left(\omega t - \arctan\omega - \arctan\frac{\omega}{2}\right)$$

**Agreement.** Expanding, $(1+i\omega)(2+i\omega) = (2-\omega^2) + 3i\omega$. Rationalising $G(i\omega)$ and taking $\mathrm{Re}\!\left[G(i\omega)e^{i\omega t}\right]$ gives exactly the result of (i). The factored form avoids a quadrant error. In the expanded form, $\arctan\!\big(3\omega/(2-\omega^2)\big)$ needs $+\pi$ once $\omega>\sqrt2$, where $2-\omega^2<0$.

**Interpretation.**

- $\omega\to0$: $y\to\tfrac12 = G(0)$. A slow input acts like a constant.
- $\omega=\sqrt2$: the lag is exactly $90^\circ$ and the amplitude is $1/(3\sqrt2)$.
- $\omega\to\infty$: the amplitude falls as $1/\omega^2$ and the lag approaches $180^\circ$, up to $90^\circ$ from each of the two lags.

### Q8. CSTR with varying volume

A CSTR has feed $q_0$ and discharge $q$, and $V$, $q_0$ and $q$ may all vary. Show that $V\dot c = q_0(c_0 - c)$ for an inert tracer, then add a first-order reaction.

Assume the tank is well mixed (the outlet is at $c$) and the density is constant (a volume balance replaces the mass balance).

1. Volume balance: $\dfrac{dV}{dt} = q_0 - q$.
2. Tracer balance: $\dfrac{d(Vc)}{dt} = q_0c_0 - qc$.
3. Product rule, because $V$ and $c$ both vary: $V\dfrac{dc}{dt} + c\dfrac{dV}{dt} = q_0c_0 - qc$.
4. Substitute the volume balance. The $qc$ terms cancel:

$$V\frac{dc}{dt} = q_0(c_0-c)$$

**Why $q$ drops out.** The outlet removes liquid at the tank's own concentration. It lowers the amount of tracer and the volume in the same proportion, so $c$ is unchanged. Only feed of a different concentration changes $c$.

**With reaction.** First-order consumption removes $kcV$ per unit time throughout the volume. The same steps give

$$V\frac{dc}{dt} = q_0(c_0-c) - kVc$$

With constant $V$ and $q_0$ this is a first-order lag, $\tau\dot c + c = Kc_0$, with

$$\tau = \frac{V}{q_0+kV}, \qquad K = \frac{q_0}{q_0+kV} = \frac{1}{1+k\tau_R}$$

where $\tau_R = V/q_0$ is the residence time. If $V$ or $q_0$ varies, the products $q_0c$ and $Vc$ make the ODE nonlinear, so linearise about a steady state before taking a transfer function.

## Ideas behind the answers

### Deviation variables

A transfer function needs zero initial conditions, because $\mathcal{L}[\dot y] = sY - y(0)$. A process usually starts at a nonzero operating point. Take $\tau\dot y + y = Kx$ starting from steady state $y_s = Kx_s\neq0$. In absolute variables,

$$Y = \frac{K}{\tau s+1}X + \frac{\tau y_s}{\tau s+1}$$

The second term doesn't depend on $X$, so $Y/X$ is not a fixed function of $s$.

**Where the constant goes.** Split the input as $x = x_s + x'$, so $X = x_s/s + X'$. Using $Kx_s = y_s$, the steady part of the input and the initial-condition term combine:

$$\frac{y_s}{s(\tau s+1)} + \frac{\tau s\,y_s}{s(\tau s+1)} = \frac{y_s(1+\tau s)}{s(\tau s+1)} = \frac{y_s}{s}$$

In the time domain, the initial condition decays as $y_se^{-t/\tau}$ while the steady input builds $y_s(1-e^{-t/\tau})$. The two sum to a flat $y_s$: a system at steady state with unchanged input does nothing. By linearity, $y = y_s + y'(t)$, where $y'$ is the response to $x'$ alone. Defining $y' = y-y_s$ and $x' = x-x_s$ applies this split before transforming, giving $Y' = \frac{K}{\tau s+1}X'$ directly.

**The reference is the initial steady state.** $y_s$ is the steady state before the disturbance, so $y(0) = y_s$. The final steady state is different: for a step $\Delta x$, $y(\infty) = y_s + K\Delta x$. Taking the final state as the reference would make $y'(0) = -K\Delta x \neq 0$, so the initial-condition term would come back. The initial state is also known before solving, and with it as reference $y'(\infty)$ measures the size of the change directly.

**Deviation variables set the value to zero, not the derivatives.** Since $y_s$ is constant, $\dot y' = \dot y$. Derivative initial conditions are zero only because the system starts at steady state.

**Why they are standard.** They cancel constant terms (for example $\tau\dot y + y = Kx + c$). Linearisation about an operating point produces them automatically. And controllers act on changes from the normal operating point. In Q4 and Q5 the operating point is zero, so deviation and absolute variables coincide.

### Transforms of derivatives

Integrate by parts with $u = e^{-st}$ and $dv = \dot y\,dt$. This moves the derivative onto the exponential:

$$\mathcal{L}[\dot y] = \Big[y\,e^{-st}\Big]_0^\infty + s\int_0^\infty y\,e^{-st}\,dt = sY - y(0)$$

The upper limit vanishes if $y$ grows no faster than $e^{\alpha t}$ and $\mathrm{Re}\,s>\alpha$, which is the same condition for $Y$ to exist. Applying the rule to $\dot y$, then to $\ddot y$, gives

$$\mathcal{L}[\ddot y] = s^2Y - s\,y(0) - \dot y(0), \qquad \mathcal{L}\left[y^{(3)}\right] = s^3Y - s^2y(0) - s\,\dot y(0) - \ddot y(0)$$

and by induction

$$\mathcal{L}\!\left[y^{(n)}\right] = s^nY - \sum_{k=0}^{n-1}s^{\,n-1-k}y^{(k)}(0)$$

Each differentiation becomes a factor of $s$ and brings in one initial condition, from the boundary term. An $n$th-order system therefore needs $n$ initial conditions, the same as the number of constants in its complementary function.

**Example: Q7 with general initial conditions.**

$$(s^2+3s+2)Y = X + (s+3)\,y(0) + \dot y(0)$$

$$Y = \underbrace{\frac{1}{(s+1)(s+2)}}_{G(s)}X + \frac{(s+3)\,y(0) + \dot y(0)}{(s+1)(s+2)}$$

The initial-condition term has only the process poles. Cover-up turns it into $\big[2y(0)+\dot y(0)\big]e^{-t} - \big[y(0)+\dot y(0)\big]e^{-2t}$, which is the complementary function with its constants fixed by the initial conditions. It decays for a stable process, so it has no effect at large $t$.

### Frequency response theorem

For a stable linear system with input $A\cos\omega t$, once the transients have decayed,

$$y(t) = A\,|G(i\omega)|\cos(\omega t + \phi), \qquad \phi = \arg G(i\omega)$$

**Derivation.**

1. Transform the input: $X = \dfrac{As}{(s-i\omega)(s+i\omega)}$.
2. Partial fractions separate the input's poles from the process poles $p_k$:
$$Y = \frac{c}{s-i\omega} + \frac{\bar c}{s+i\omega} + \sum_k\frac{d_k}{s-p_k}$$
3. Cover-up gives $c = G(i\omega)\dfrac{Ai\omega}{2i\omega} = \dfrac{A}{2}G(i\omega)$. The second coefficient is $\bar c$ because $G$ has real coefficients, so $G(-i\omega) = \overline{G(i\omega)}$.
4. Stability means $\mathrm{Re}\,p_k<0$, so every $d_ke^{p_kt}$ decays. Repeated poles give $t^me^{p_kt}$, which also decays.
5. What remains is $c\,e^{i\omega t} + \bar c\,e^{-i\omega t} = A\,\mathrm{Re}\!\left[G(i\omega)e^{i\omega t}\right] = A|G|\cos(\omega t+\phi)$.

**Why the frequency cannot change.** In convolution form, $y = \int_0^\infty g(\tau')x(t-\tau')\,d\tau'$. With $x = e^{i\omega t}$ this becomes $e^{i\omega t}\int_0^\infty g(\tau')e^{-i\omega\tau'}d\tau' = G(i\omega)e^{i\omega t}$. A linear time-invariant system can only form weighted sums of delayed copies of the input. A sum of delayed sinusoids at one frequency is a sinusoid at that frequency. So a linear system cannot create new frequencies. A nonlinear one produces harmonics, which is one way to detect nonlinearity in a test.

**Physical picture.** For a first-order lag $K/(\tau s+1)$,

$$|G(i\omega)| = \frac{K}{\sqrt{1+\omega^2\tau^2}}, \qquad \phi = -\arctan\omega\tau$$

- $\omega\tau\ll1$: the input changes slowly compared with the storage time. The output stays close to steady state, with $|G|\to K$ and $\phi\to0$.
- $\omega\tau\gg1$: the input reverses before the inventory can respond. Storage averages out the swings, so the amplitude falls about as $K/(\omega\tau)$ and the lag approaches $90^\circ$. The lag behaves like an integrator, turning $\cos$ into $\sin$.
- $\omega\tau=1$: the amplitude is $K/\sqrt2$ and the lag is $45^\circ$.

An order-$n$ process with no zeros approaches $-90n^\circ$ and an $\omega^{-n}$ fall at high frequency. Phase lag matters in feedback: at $180^\circ$ a corrective action arrives in phase with the error and reinforces it.

**Validity.** The theorem needs stability, since an unstable or integrating mode never decays to a steady oscillation. It describes the output only after several of the slowest time constants. For a linearised process, the amplitude must also be small enough to stay near the operating point.

**Sign conventions for phase.** Two conventions are in use, and mixing them gives a double negative.

- $\phi = \arg G$, which is negative for lags, used in $\cos(\omega t+\phi)$.
- $\phi = -\arg G$, the positive lag, used in $\cos(\omega t-\phi)$.

Both give $\cos(\omega t - \arctan\omega - \arctan\frac{\omega}{2})$ for Q7. The physical check: storage delays the output, so a process made of lags must have $\omega t$ minus a positive angle.

### Arguments of a product and pole vectors

In polar form, multiplying complex numbers multiplies their magnitudes and adds their arguments: $\arg(z_1z_2) = \arg z_1 + \arg z_2$. A reciprocal reverses the angle: $\arg(1/z) = -\arg z$. So

$$\arg\frac{1}{(1+i\omega)(2+i\omega)} = -\arg(1+i\omega) - \arg(2+i\omega) = -\arctan\omega - \arctan\frac{\omega}{2}$$

Each factor has a positive real part, so each $\arctan$ lies between $0$ and $90^\circ$ without a quadrant correction.

Geometrically, $1+i\omega = i\omega - (-1)$ is the vector from the pole at $s=-1$ to the point $i\omega$. Then $|G|$ is $1$ over the product of the pole-vector lengths, and $\arg G$ is minus the sum of their angles. As $\omega$ rises, each vector turns from horizontal towards vertical. A pole nearer the imaginary axis (the slower time constant) turns sooner, so its lag builds up at lower frequency.

### Residence time, reaction time and reaction order

A reacting CSTR removes material in two ways, and each has its own timescale.

- **Residence time** $\tau_R = V/q_0$: the time to deliver one tank volume of feed. It is set by the equipment and flow, not the chemistry.
- **Reaction time** $\tau_{rxn} = c/r(c)$: the time to consume the current contents at the current rate. It is set by the chemistry.

| Order | Rate $r$ | $\tau_{rxn} = c/r$ | Per-molecule reaction probability per unit time, $r/c$ |
|---|---|---|---|
| 0 | $k_0$ | $c/k_0$ | $k_0/c$: saturated sites shared among more molecules |
| 1 | $kc$ | $1/k$ | $k$: each molecule reacts independently |
| 2 | $kc^2$ | $1/(kc)$ | $kc$: a partner must be met, and partners scale with $c$ |

**Why first order is independent of $c$.** The rate is proportional to the amount present, so a fixed fraction reacts per unit time, as in radioactive decay. Batch decay $c_0e^{-kt}$ therefore has a half-life $\ln2/k$ whatever the value of $c_0$. First order is also the only order where $r/c = \partial r/\partial c$, so the balance is linear and its time constant and gain are the same at every operating point. Strictly this holds for a unimolecular step. A bimolecular reaction with its partner in large excess is pseudo-first-order, with $k = k_2c_B$, until $c_B$ starts to fall.

**How the two combine (first order).** Dividing the balance by $V$ gives

$$\frac{dc}{dt} = \frac{c_0-c}{\tau_R} - \frac{c}{\tau_{rxn}}, \qquad \frac{1}{\tau} = \frac{1}{\tau_R} + \frac{1}{\tau_{rxn}}$$

The removal rates add, like conductances in parallel. The faster route dominates, and $\tau$ is shorter than either alone. So with reaction, the time constant is not the residence time. Their ratio is the Damköhler number:

$$\mathrm{Da} = \frac{\tau_R}{\tau_{rxn}} = k\tau_Rc^{\,n-1}$$

- $\mathrm{Da}\ll1$: material washes out before it reacts, so $c\approx c_0$ and $\tau\approx\tau_R$.
- $\mathrm{Da}\gg1$: material reacts before it washes out, so $c\ll c_0$ and $\tau\approx\tau_{rxn}$.
- For first order, the steady-state gain is $K = 1/(1+\mathrm{Da})$.

**The dynamic time constant uses the slope of the rate.** For $n\neq1$, linearise about $c_s$ using $kc^n\approx kc_s^n + nkc_s^{n-1}c'$:

$$\frac{dc'}{dt} = \frac{c_0'-c'}{\tau_R} - nkc_s^{n-1}c', \qquad \frac{1}{\tau} = \frac{1}{\tau_R} + \frac{\partial r}{\partial c}\bigg|_{c_s}$$

The dynamic reaction time constant is $1/(\partial r/\partial c) = \tau_{rxn}/n$, not $c/r$. What restores a disturbance is how much faster the reaction runs when $c$ rises, not the size of the rate. For second order, a 1% rise in $c$ raises the rate by 2%, so the response is faster than $c/r$ suggests.

### Zero-order reaction in a CSTR

With $r = k_0$ and constant $V$ and $q_0$,

$$\frac{dc}{dt} = \frac{c_0-c}{\tau_R} - k_0$$

This is already linear, because the reaction term is a constant.

- **Steady state:** $c_s = c_{0,s} - k_0\tau_R$. Each feed element spends about $\tau_R$ in the tank and loses $k_0$ per unit time. This requires $c_{0,s} > k_0\tau_R$.
- **Dynamics:** subtracting the steady state cancels $k_0$, just as a constant term cancels in deviation variables. This leaves $\tau_R\dot c' + c' = c_0'$, so $G = 1/(\tau_Rs+1)$: the inert-tracer result, shifted down by $k_0\tau_R$.

**Physical reason.** Extra tracer doesn't speed up a zero-order reaction, so only flow removes the excess. The reaction lowers the level but provides no restoring feedback, because $\partial r/\partial c = 0$. As an analogy, a fixed-rate pump lowers a sink's level but doesn't respond to it, while a plug hole drains faster when the level rises. The analogy fails at $c=0$, where a reaction stops but a pump would keep running.

**Where the reaction does appear: as a disturbance input.** If $k_0$ changes (for example temperature, catalyst activity or enzyme loading), then $\tau_R\dot c' + c' = c_0' - \tau_Rk_0'$, so

$$\frac{C'}{K_0'} = \frac{-\tau_R}{\tau_Rs+1}$$

**Validity.** Zero order is the saturated limit of real kinetics, for example Michaelis–Menten, $r = V_{max}c/(K_m+c)$, with slope

$$\frac{\partial r}{\partial c} = \frac{V_{max}K_m}{(K_m+c)^2}$$

For $c\gg K_m$ the slope is small and the zero-order result holds. As $c$ approaches $K_m$, the slope rises towards $V_{max}/K_m$, the reaction starts to restore disturbances, and $\tau$ drops below $\tau_R$. The zero-order model fails once a disturbance takes the tank out of the saturated region.
