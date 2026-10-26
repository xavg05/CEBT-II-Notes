# PDC: Example Sheet 0

Laplace transforms, transfer functions, frequency response and CSTR balances. Each question gives the answer first, then the understanding behind it, including the follow-up questions that came up in supervision.

Assumed: Year 1–2 Laplace transforms, partial fractions and linear ODEs.

**Contents**

1. Cover-up rule for repeated factors
2. Repeated poles by differentiating with respect to a parameter
3. Inverse transforms
4. First-order lag: transfer function, convolution and deviation variables
5. Second-order step response: transforms of derivatives and initial conditions
6. *(not covered)*
7. Sinusoidal input: the frequency response theorem
8. CSTR balance: residence time, reaction time and reaction order

---

## Q1. Cover-up rule for repeated factors

> Use the cover-up rule to expand $`\dfrac{1}{s(\tau s+1)}`$, then $`\dfrac{1}{s(\tau s+1)^2}`$, then $`\dfrac{1}{s(\tau s+1)^n}`$.

### Answer


```math
\frac{1}{s(\tau s+1)} = \frac{1}{s} - \frac{\tau}{\tau s+1}
```



```math
\frac{1}{s(\tau s+1)^n} = \frac{1}{s} - \sum_{k=1}^{n}\frac{\tau}{(\tau s+1)^k}
```


### Understanding

**How the general case follows from the first.** Divide the $`n=1`$ result by $`(\tau s+1)`$:


```math
\frac{1}{s(\tau s+1)^2} = \frac{1}{s(\tau s+1)} - \frac{\tau}{(\tau s+1)^2} = \frac{1}{s} - \frac{\tau}{\tau s+1} - \frac{\tau}{(\tau s+1)^2}
```


The first term on the right is again the $`n=1`$ expression, which we already know how to expand. Each further division adds one more term, $`-\tau/(\tau s+1)^k`$, which gives the general sum.

**Why it matters.** $`1/[s(\tau s+1)^n]`$ is the step response of $`n`$ identical first-order lags in series. The $`1/s`$ term is the final value, $`1`$, and the sum describes how the cascade approaches it. More lags in series means more terms of the form $`t^{k-1}e^{-t/\tau}`$, so the response is slower and more S-shaped. This is why the 63.2% rule for a single lag does not carry over to a cascade.

---

## Q2. Repeated poles by differentiating with respect to a parameter

> Find $`\mathcal{L}[e^{-\alpha t}]`$, then differentiate both sides with respect to $`\alpha`$ to invert $`\dfrac{1}{(s+\alpha)^2}`$ and $`\dfrac{1}{(s+\alpha)^n}`$.

### Answer


```math
\mathcal{L}[e^{-\alpha t}] = \frac{1}{s+\alpha}, \qquad \mathcal{L}^{-1}\!\left[\frac{1}{(s+\alpha)^2}\right] = te^{-\alpha t}, \qquad \mathcal{L}^{-1}\!\left[\frac{1}{(s+\alpha)^n}\right] = \frac{t^{\,n-1}e^{-\alpha t}}{(n-1)!}
```


### Understanding

The transform is an integral over $`t`$, so differentiating with respect to the parameter $`\alpha`$ can be done inside the integral. On the time side, each differentiation brings down a factor of $`-t`$. On the $`s`$ side, it raises the power of $`(s+\alpha)`$ by one. After $`n-1`$ differentiations, the minus signs cancel on both sides and the factorial collects.

**What a repeated pole looks like in time.** A repeated pole gives $`t^{n-1}e^{-\alpha t}`$. The exponential still decays, so the response is still stable, but the polynomial factor delays the peak. For example, $`te^{-t}`$ rises before it decays, with its maximum at $`t=1/\alpha`$.

---

## Q3. Inverse transforms

| Transform | Inverse | Method |
|---|---|---|
| $`\dfrac{5}{(s+4)(s+1)}`$ | $`\tfrac{5}{3}\left(e^{-t}-e^{-4t}\right)`$ | cover-up |
| $`\dfrac{1}{(s+1)^2(s+2)}`$ | $`te^{-t} - e^{-t} + e^{-2t}`$ | repeated pole, as in Q2 |
| $`\dfrac{1}{s^2+4s+5}`$ | $`e^{-2t}\sin t`$ | complete the square: $`(s+2)^2+1`$ |
| $`\dfrac{2s^2-3s}{(s+1)^2(s+2)}`$ | $`5te^{-t} - 12e^{-t} + 14e^{-2t}`$ | repeated pole plus cover-up |

**Reading the poles.** Each pole of the transform appears directly in the time response:

- a real pole at $`-a`$ gives $`e^{-at}`$
- a repeated pole adds a factor of $`t`$
- a complex pair $`-2\pm i`$ gives a decaying oscillation $`e^{-2t}\sin t`$, where the real part sets the decay rate and the imaginary part sets the frequency

---

## Q4. First-order lag: transfer function, convolution and deviation variables

> Find the transfer function for $`\tau\dot y + y = x`$ and write the solution as a convolution. Compare with the integrating-factor solution, with $`y(0)=0`$, and evaluate for $`x=1`$.

### Answer

**Transfer function.** With $`y(0)=0`$, transforming gives $`(\tau s+1)Y = X`$:


```math
G(s) = \frac{1}{\tau s+1}, \qquad g(t) = \mathcal{L}^{-1}[G] = \frac{1}{\tau}e^{-t/\tau}
```


**Convolution.** Since $`Y = GX`$, the convolution theorem gives


```math
y(t) = \int_0^t \frac{1}{\tau}e^{-(t-t')/\tau}\,x(t')\,dt'
```


**Integrating factor.**

1. Divide by $`\tau`$ to put the ODE in standard form: $`\dot y + \dfrac{1}{\tau}y = \dfrac{x}{\tau}`$.
2. Multiply by $`e^{t/\tau}`$. The left side becomes an exact derivative: $`\dfrac{d}{dt}\left(y\,e^{t/\tau}\right) = \dfrac{1}{\tau}x(t)\,e^{t/\tau}`$.
3. Integrate from $`0`$ to $`t`$ with dummy variable $`t'`$: $`y(t)\,e^{t/\tau} - y(0) = \displaystyle\int_0^t \frac{1}{\tau}x(t')\,e^{t'/\tau}\,dt'`$.
4. Use $`y(0)=0`$ and multiply by $`e^{-t/\tau}`$. This gives exactly the convolution above.

**Unit step.**


```math
y(t) = \frac{1}{\tau}e^{-t/\tau}\int_0^t e^{t'/\tau}\,dt' = \frac{1}{\tau}e^{-t/\tau}\cdot\tau\left(e^{t/\tau}-1\right) = 1 - e^{-t/\tau}
```


### Understanding: convolution as memory

The convolution says the present output is a weighted sum of all past inputs. The weight $`g(t-t')`$ decays with the age $`t-t'`$ of each input. Recent inputs count most, and inputs older than a few $`\tau`$ are effectively forgotten. The integrating factor builds the same weighting, so the two methods have to agree. The Laplace route gets there through $`Y = GX`$ without any integration.

### Understanding: do we need deviation variables here?

**No.** A transfer function needs every initial condition to be zero, because


```math
\mathcal{L}[\dot y] = sY - y(0)
```


and a $`y(0)`$ term would add a part of the output that doesn't depend on the input. Here $`y(0)=0`$ is given, and the ODE has no constant term, so the absolute variables already behave like deviation variables.

**When they are needed.** Deviation variables are needed when the process starts at a nonzero steady state. Take $`\tau\dot y + y = Kx`$ starting from $`y(0) = y_s = Kx_s \neq 0`$. Transforming the absolute variables gives


```math
Y = \frac{K}{\tau s+1}X + \frac{\tau y_s}{\tau s+1}
```


The second term doesn't depend on $`X`$, so $`Y/X`$ is not a fixed function of $`s`$. Every starting point would give a different "transfer function".

Subtracting the steady-state equation $`y_s = Kx_s`$, with $`y' = y-y_s`$ and $`x' = x-x_s`$, gives


```math
\tau\dot y' + y' = Kx', \qquad y'(0) = 0 \quad\Rightarrow\quad \frac{Y'}{X'} = \frac{K}{\tau s+1}
```


This is the same equation with zero initial conditions, and it holds at any operating point.

**Where the steady state goes.** Split the input as $`x = x_s + x'`$, so $`X = x_s/s + X'`$. Then


```math
Y = \underbrace{\frac{Kx_s}{s(\tau s+1)}}_{\text{steady input}} + \underbrace{\frac{\tau y_s}{\tau s+1}}_{\text{initial condition}} + \underbrace{\frac{KX'}{\tau s+1}}_{\text{the change}}
```


Use $`Kx_s = y_s`$ and put the first two terms over the same denominator:


```math
\frac{y_s}{s(\tau s+1)} + \frac{\tau s\,y_s}{s(\tau s+1)} = \frac{y_s(1+\tau s)}{s(\tau s+1)} = \frac{y_s}{s}
```


In the time domain, the initial condition decays as $`y_se^{-t/\tau}`$, while the steady input builds up as $`y_s(1-e^{-t/\tau})`$. The decay of one exactly balances the rise of the other, so the sum stays at $`y_s`$. A system at steady state with an unchanged input does nothing. Only the change $`x'`$ produces any dynamics. Deviation variables remove the constant part before the problem is solved.

**Why $`y_s`$ means the initial steady state, not the final one.** There are two steady states. Before the change, $`y(0) = y_s`$. After a step $`\Delta x`$, the process settles at $`y(\infty) = y_s + K\Delta x`$. The reference must be the initial one, for three reasons:

- It is the only choice that makes $`y'(0)=0`$. Using the final state would give $`y'(0) = -K\Delta x \neq 0`$, and the initial-condition term would come back.
- It is known before solving, since it is where the plant is running now.
- The deviation then measures the size of the change: $`y'(\infty) = K\Delta x`$.

**Why control uses them routinely.**

- They cancel constant terms, as in $`\tau\dot y + y = Kx + c`$.
- Linearising a nonlinear model about an operating point produces deviation variables automatically.
- Controllers act on changes from the normal operating point: setpoint changes, disturbances and valve moves.

### Key points

- $`G(s)`$ is defined only for zero initial conditions. Deviation variables from the **initial** steady state provide them.
- The steady part of the input and the initial-condition term cancel into the constant $`y_s`$. Only changes produce dynamics.
- Convolution, the integrating factor and $`Y = GX`$ are three routes to the same weighted memory of the input.

---

## Q5. Second-order step response: transforms of derivatives and initial conditions

> Find the transfer function for $`6\ddot y + 5\dot y + y = x`$, evaluate for $`x=1`$, and compare with the complementary function plus particular integral, with $`y(0)=\dot y(0)=0`$.

### Answer

**Transfer function.**


```math
G(s) = \frac{1}{6s^2+5s+1} = \frac{1}{(3s+1)(2s+1)}
```


**Laplace step response.** Cover-up gives $`-9`$ at $`s=-\tfrac13`$ and $`4`$ at $`s=-\tfrac12`$:


```math
Y = \frac{1}{s(3s+1)(2s+1)} = \frac{1}{s} - \frac{9}{3s+1} + \frac{4}{2s+1} \quad\Rightarrow\quad y(t) = 1 - 3e^{-t/3} + 2e^{-t/2}
```


**Complementary function plus particular integral.**

1. **Complementary function.** $`6m^2+5m+1 = (3m+1)(2m+1) = 0`$ gives $`m = -\tfrac13, -\tfrac12`$, so $`y_{CF} = Ae^{-t/3} + Be^{-t/2}`$.
2. **Particular integral.** For constant forcing, try $`y = C`$. Both derivatives vanish, so $`C=1`$.
3. **Initial conditions.** $`y(0)=0`$ gives $`1+A+B=0`$. $`\dot y(0)=0`$ gives $`-\tfrac{A}{3} - \tfrac{B}{2} = 0`$, so $`B = -\tfrac23A`$.
4. **Solve.** $`1 + A - \tfrac23A = 0`$, so $`A = -3`$ and $`B = 2`$. This gives the same $`y(t)`$.

**Checks.** $`y(0) = 1-3+2 = 0`$, $`\dot y(0) = 1-1 = 0`$, and $`y\to1 = G(0)`$, the steady-state gain.

**Comparing the methods.** The cover-up rule finds $`-3`$ and $`+2`$ in one step, because the initial conditions are already in the transform. The ODE method has to fit them separately as simultaneous equations.

### Understanding: could we use deviation variables anyway?

Yes, they are always allowed. The system starts at rest with $`x=0`$, so $`y_s = x_s = 0`$, and the deviation variables equal the absolute variables. Nothing changes.

The question also shows what deviation variables do not do. They set the **value** to zero, but not the derivatives. Since $`y_s`$ is constant, $`\dot y' = \dot y`$. The derivative initial conditions are zero only because a system at steady state is not changing. A second-order system released with a nonzero velocity would keep its $`\dot y(0)`$ term even in deviation variables.

### Understanding: where the initial conditions come from

**First derivative.** Integrate by parts with $`u = e^{-st}`$ and $`dv = \dot y\,dt`$. This moves the derivative onto the exponential, which differentiates to $`-s`$ times itself:


```math
\mathcal{L}[\dot y] = \int_0^\infty \dot y\,e^{-st}\,dt = \Big[y\,e^{-st}\Big]_0^\infty + s\int_0^\infty y\,e^{-st}\,dt = sY - y(0)
```


The upper limit vanishes when $`y`$ grows no faster than some $`e^{\alpha t}`$ and $`\mathrm{Re}\,s > \alpha`$. That is the same condition needed for $`Y`$ to exist. The lower limit gives $`-y(0)`$.

**Higher derivatives.** Apply the same rule to $`\dot y`$, then to $`\ddot y`$:


```math
\mathcal{L}[\ddot y] = s\,\mathcal{L}[\dot y] - \dot y(0) = s^2Y - s\,y(0) - \dot y(0)
```



```math
\mathcal{L}\left[y^{(3)}\right] = s^3Y - s^2y(0) - s\,\dot y(0) - \ddot y(0)
```


By induction (the base case is $`n=1`$, and each step applies the first-derivative rule to $`y^{(n)}`$):


```math
\mathcal{L}\!\left[y^{(n)}\right] = s^nY - \sum_{k=0}^{n-1}s^{\,n-1-k}\,y^{(k)}(0)
```


**What this means.**

- Differentiation becomes multiplication by $`s`$. This is what turns a linear ODE into algebra.
- Each differentiation brings in one initial condition, from the boundary term of the integration by parts. An $`n`$th-order system needs $`n`$ initial conditions, the same as the number of constants in its complementary function.
- For a system that starts at rest at steady state, all the initial conditions are zero, so $`\mathcal{L}[y^{(n)}] = s^nY`$. $`G(s)`$ is then simply a ratio of polynomials in $`s`$.

### Key points

- The poles $`-\tfrac13`$ and $`-\tfrac12`$ are the roots of the auxiliary equation. Laplace and CF+PI find the same modes.
- Initial conditions enter the transform through the boundary terms of integration by parts, one per derivative.
- Deviation variables zero the value. Zero derivatives come from starting at steady state.

---

## Q7. Sinusoidal input: the frequency response theorem

> The process $`\ddot y + 3\dot y + 2y = x`$ has input $`x = \cos\omega t`$. Find the output for large $`t`$ (i) from the ODE directly, explaining why only the particular integral is needed, and (ii) from the transfer function and the frequency response theorem.

### Answer (i): ODE directly

**Why only the particular integral.** The auxiliary equation $`(m+1)(m+2)=0`$ gives $`y_{CF} = Ae^{-t} + Be^{-2t}`$. Both roots are negative, so the complementary function decays whatever the initial conditions. That is also why no initial conditions are given. The slowest term is $`e^{-t}`$, so "large $`t`$" means $`t\gg1`$.

**Particular integral.** Try $`y = a\cos\omega t + b\sin\omega t`$:


```math
\dot y = -a\omega\sin\omega t + b\omega\cos\omega t, \qquad \ddot y = -a\omega^2\cos\omega t - b\omega^2\sin\omega t
```


Matching coefficients:


```math
\cos\omega t:\ a(2-\omega^2) + 3\omega b = 1, \qquad \sin\omega t:\ b(2-\omega^2) - 3\omega a = 0 \;\Rightarrow\; b = \frac{3\omega a}{2-\omega^2}
```


Substitute into the cos equation. The denominator factorises: $`(2-\omega^2)^2 + 9\omega^2 = (\omega^2+1)(\omega^2+4)`$.


```math
a = \frac{2-\omega^2}{(\omega^2+1)(\omega^2+4)}, \qquad b = \frac{3\omega}{(\omega^2+1)(\omega^2+4)}
```



```math
y(t) = \frac{(2-\omega^2)\cos\omega t + 3\omega\sin\omega t}{(\omega^2+1)(\omega^2+4)}
```


**Amplitude–phase form.** Writing $`y = R\cos(\omega t - \theta)`$ gives $`R = 1/\sqrt{(1+\omega^2)(4+\omega^2)}`$ and $`\tan\theta = 3\omega/(2-\omega^2)`$. Watch the quadrant: for $`\omega > \sqrt2`$, $`a<0`$, so add $`\pi`$ to the calculator's $`\arctan`$.

### Answer (ii): frequency response theorem

The transfer function $`G(s) = \dfrac{1}{(s+1)(s+2)}`$ has poles at $`-1`$ and $`-2`$, so it is stable and the theorem applies.


```math
G(i\omega) = \frac{1}{(1+i\omega)(2+i\omega)}, \qquad |G(i\omega)| = \frac{1}{\sqrt{(1+\omega^2)(4+\omega^2)}}, \qquad \arg G(i\omega) = -\arctan\omega - \arctan\frac{\omega}{2}
```



```math
y(t) = \frac{1}{\sqrt{(1+\omega^2)(4+\omega^2)}}\cos\!\left(\omega t - \arctan\omega - \arctan\frac{\omega}{2}\right)
```


**Agreement.** $`(1+i\omega)(2+i\omega) = (2-\omega^2) + 3i\omega`$, so $`\arg G = -\theta`$. Rationalising gives $`G(i\omega) = \dfrac{(2-\omega^2) - 3i\omega}{(\omega^2+1)(\omega^2+4)}`$, and $`\mathrm{Re}\!\left[G(i\omega)e^{i\omega t}\right]`$ reproduces (i) exactly.

**What the result means.**

| Frequency | Amplitude | Phase lag | Meaning |
|---|---|---|---|
| $`\omega\to0`$ | $`\tfrac12 = G(0)`$ | $`0`$ | slow input acts like a constant, and the output follows it |
| $`\omega = \sqrt2`$ | $`1/(3\sqrt2)`$ | $`90^\circ`$ | output is a pure $`\sin`$ term |
| $`\omega\to\infty`$ | $`\sim 1/\omega^2`$ | $`\to 180^\circ`$ | each lag contributes up to $`90^\circ`$ |

### Understanding: why only the particular integral survives

Transform the ODE while keeping general initial conditions:


```math
\big[s^2Y - s\,y(0) - \dot y(0)\big] + 3\big[sY - y(0)\big] + 2Y = X
```



```math
(s^2+3s+2)\,Y = X + (s+3)\,y(0) + \dot y(0)
```



```math
Y = \underbrace{\frac{1}{(s+1)(s+2)}}_{G(s)}X + \underbrace{\frac{(s+3)\,y(0) + \dot y(0)}{(s+1)(s+2)}}_{\text{initial conditions}}
```


The initial-condition term contains **only the process poles**. Cover-up turns it into


```math
\big[2y(0)+\dot y(0)\big]e^{-t} - \big[y(0)+\dot y(0)\big]e^{-2t}
```


This is the complementary function, with $`A`$ and $`B`$ fixed by the initial conditions. At $`t=0`$ it gives $`y(0)`$, as it should. It decays for a stable process. At large $`t`$, only the poles of the input, $`\pm i\omega`$, are left.

### Understanding: deriving the frequency response theorem

**Statement.** For a stable linear system with input $`A\cos\omega t`$, after the transients have decayed:


```math
y(t) = A\,|G(i\omega)|\cos(\omega t + \phi), \qquad \phi = \arg G(i\omega)
```


**Proof.**

1. Transform the input: $`X = \dfrac{As}{(s-i\omega)(s+i\omega)}`$.
2. Partial fractions separate the input's poles from the process poles $`p_k`$:

```math
Y = G(s)\frac{As}{(s-i\omega)(s+i\omega)} = \frac{c}{s-i\omega} + \frac{\bar c}{s+i\omega} + \sum_k\frac{d_k}{s-p_k}
```

3. Cover-up at $`s = i\omega`$: $`c = G(i\omega)\dfrac{Ai\omega}{2i\omega} = \dfrac{A}{2}G(i\omega)`$. The second coefficient is $`\bar c`$, because $`G`$ has real coefficients, so $`G(-i\omega) = \overline{G(i\omega)}`$.
4. Stability means $`\mathrm{Re}\,p_k < 0`$, so every $`d_ke^{p_kt}`$ decays. A repeated pole gives $`t^me^{p_kt}`$, which also decays.
5. What remains is $`c\,e^{i\omega t} + \bar c\,e^{-i\omega t} = 2\,\mathrm{Re}\!\left[c\,e^{i\omega t}\right] = A\,\mathrm{Re}\!\left[G(i\omega)e^{i\omega t}\right]`$. Writing $`G = |G|e^{i\phi}`$ gives $`A|G|\cos(\omega t + \phi)`$.

The long-time output comes only from the input's poles. The process poles contribute a transient that dies away.

**A linear system cannot create new frequencies.** Using the convolution from Q4, with an input that has been running for a long time:


```math
y(t) = \int_0^\infty g(\tau')\,x(t-\tau')\,d\tau' \quad\xrightarrow{\;x = e^{i\omega t}\;}\quad e^{i\omega t}\int_0^\infty g(\tau')\,e^{-i\omega\tau'}\,d\tau' = G(i\omega)\,e^{i\omega t}
```


A linear time-invariant system can only form weighted sums of delayed copies of its input. A delayed sinusoid is still a sinusoid at the same frequency, and a sum of them is a single sinusoid with a new amplitude and phase. $`G(i\omega)`$ is that sum. A nonlinear system creates harmonics, which is one way to detect nonlinearity in a test.

### Understanding: the physical picture

For a first-order lag $`K/(\tau s+1)`$, for example a well-mixed tank:


```math
|G(i\omega)| = \frac{K}{\sqrt{1+\omega^2\tau^2}}, \qquad \phi = -\arctan\omega\tau
```


- **Slow input, $`\omega\tau\ll1`$.** One cycle lasts much longer than the time constant. The tank stays close to steady state with the current input, so $`|G|\to K`$ and $`\phi\to0`$.
- **Fast input, $`\omega\tau\gg1`$.** The input reverses before the inventory can respond. Storage averages out the swings, so the amplitude falls about as $`K/(\omega\tau)`$ and the lag approaches $`90^\circ`$. The tank behaves like an integrator, turning a $`\cos`$ into a $`\sin`$.
- **Corner, $`\omega\tau = 1`$.** The amplitude is $`K/\sqrt2`$ and the lag is $`45^\circ`$. Here the period is comparable to how long the storage takes to fill or empty.

In general, $`g(t)`$ is the process's memory. When the input changes little over that memory, the output follows it. When the memory spans several cycles, they largely cancel. An $`n`$th-order process with no zeros approaches a lag of $`90n^\circ`$ and a fall of $`\omega^{-n}`$ at high frequency. Phase lag matters in feedback: at $`180^\circ`$, a corrective action arrives in phase with the error and reinforces it.

**Validity.**

- **Stable only.** An unstable or integrating mode never settles to a steady oscillation.
- **Large $`t`$ only.** It applies after several of the slowest time constants, judged against the tolerance you need.
- **Linear only.** For a linearised process, the input amplitude must be small enough to stay near the operating point.

### Understanding: why $`\arg G`$ is a sum of arctangents

Two rules for complex numbers in polar form:

- Multiplying multiplies magnitudes and adds angles: $`r_1e^{i\theta_1}\cdot r_2e^{i\theta_2} = r_1r_2e^{i(\theta_1+\theta_2)}`$.
- A reciprocal reverses the angle: $`\arg(1/z) = -\arg z`$.

So $`\arg G = 0 - \arg(1+i\omega) - \arg(2+i\omega)`$. Each factor has a positive real part, so it lies in the right half-plane and its argument is a plain $`\arctan`$ between $`0`$ and $`90^\circ`$:


```math
\arg(1+i\omega) = \arctan\omega, \qquad \arg(2+i\omega) = \arctan\frac{\omega}{2}
```


The factored form avoids the quadrant problem in (i), where the real part $`2-\omega^2`$ changes sign at $`\omega=\sqrt2`$.

**Pole vectors.** $`1+i\omega = i\omega - (-1)`$ is the arrow from the pole at $`s=-1`$ to the point $`i\omega`$ on the imaginary axis. $`|G|`$ is $`1`$ over the product of the arrow lengths, and $`\arg G`$ is minus the sum of their angles. As $`\omega`$ rises, each arrow turns from horizontal towards vertical, adding up to $`90^\circ`$ of lag. The pole nearer the axis, $`s=-1`$, which has the slower time constant, turns sooner, so its lag builds up at lower frequency.

### Understanding: the sign of the phase

Two conventions are in use:

| Convention | Form | $`\phi`$ for Q7 |
|---|---|---|
| $`\phi`$ is the phase angle of $`G`$ | $`\cos(\omega t + \phi)`$ | $`-\arctan\omega - \arctan\frac{\omega}{2}`$ (negative) |
| $`\phi`$ is the phase lag | $`\cos(\omega t - \phi)`$ | $`+\arctan\omega + \arctan\frac{\omega}{2}`$ (positive) |

Both give $`\cos(\omega t - \arctan\omega - \arctan\frac{\omega}{2})`$. Mixing them, by writing $`\cos(\omega t - \phi)`$ with $`\phi = \arg G`$, gives a double negative and an output that leads the input, which is wrong. The physical check: storage delays the output, so a process made of lags must have $`\omega t`$ minus a positive angle.

### Key points

- At large $`t`$, only the input's poles $`\pm i\omega`$ remain. The initial-condition terms carry only the process poles and decay.
- Same frequency out. The amplitude is scaled by $`|G(i\omega)|`$ and the phase is shifted by $`\arg G(i\omega)`$.
- Factor $`G`$ first. Magnitudes multiply, angles add, and there is no quadrant trap.

---

## Q8. CSTR balance: residence time, reaction time and reaction order

> A CSTR has feed $`q_0`$ and discharge $`q`$, and $`V`$, $`q_0`$ and $`q`$ may all vary with time. Show that $`V\dfrac{dc}{dt} = q_0(c_0-c)`$ for an inert tracer. Find the corresponding expression for a first-order reaction.

### Answer

Assume the tank is well mixed, so the outlet is at $`c`$, and that the density is constant, so a volume balance replaces the mass balance.

1. **Volume balance:** $`\dfrac{dV}{dt} = q_0 - q`$
2. **Tracer balance:** $`\dfrac{d(Vc)}{dt} = q_0c_0 - qc`$
3. **Product rule**, because $`V`$ and $`c`$ both vary: $`V\dfrac{dc}{dt} + c\dfrac{dV}{dt} = q_0c_0 - qc`$
4. **Substitute the volume balance:** $`V\dfrac{dc}{dt} + q_0c - qc = q_0c_0 - qc`$. The $`qc`$ terms cancel.


```math
V\frac{dc}{dt} = q_0(c_0-c)
```


**With a first-order reaction**, the tracer is consumed at $`kc`$ per unit volume, so $`kcV`$ disappears per unit time. The same steps give


```math
V\frac{dc}{dt} = q_0(c_0-c) - kVc
```


The reaction term is multiplied by $`V`$ because reaction happens throughout the volume, while feed only enters through the inlet.

### Understanding: why $`q`$ drops out

The outlet removes liquid at the tank's own concentration. It lowers the amount of tracer and the volume in the same proportion, so $`c`$ is unchanged. Draining part of a well-mixed tank only leaves less of the same mixture. Concentration changes only when feed of a different concentration mixes in, at a rate set by $`q_0`$ and by how different the feed is, $`c_0 - c`$. The outlet flow affects only $`V`$.

### Understanding: two time constants

With constant $`V`$ and $`q_0`$, the reacting balance is a first-order lag:


```math
\underbrace{\frac{V}{q_0+kV}}_{\tau}\frac{dc}{dt} + c = \underbrace{\frac{q_0}{q_0+kV}}_{K}c_0
```


The tank removes tracer in two ways, and each has a timescale.

- **Residence time, $`\tau_R = V/q_0`$.** The time to deliver one tank volume of feed. It is set by the equipment and the flow, not the chemistry.
- **Reaction time, $`\tau_{rxn} = c/r(c)`$.** The time to consume the current contents at the current rate. It is set by the chemistry. For first order it is $`1/k`$.

Dividing the balance by $`V`$ shows how they combine:


```math
\frac{dc}{dt} = \frac{c_0-c}{\tau_R} - \frac{c}{\tau_{rxn}}, \qquad \frac{1}{\tau} = \frac{1}{\tau_R} + \frac{1}{\tau_{rxn}}
```


The removal rates add, like conductances in parallel. The faster route dominates, and $`\tau`$ is always shorter than either alone. **With reaction, the time constant is not the residence time.**

Their ratio is the Damköhler number:


```math
\mathrm{Da} = \frac{\tau_R}{\tau_{rxn}} = k\tau_R\,c^{\,n-1}
```


| Regime | Behaviour | Time constant |
|---|---|---|
| $`\mathrm{Da}\ll1`$ | washes out before reacting, so $`c\approx c_0`$ and the tank is basically a mixer | $`\tau\approx\tau_R`$ |
| $`\mathrm{Da}\gg1`$ | reacts before washing out, so $`c\ll c_0`$ | $`\tau\approx\tau_{rxn}`$, set by the chemistry |

For first order, the steady-state gain is $`K = c/c_0 = 1/(1+\mathrm{Da})`$. $`\mathrm{Da}`$ alone fixes the conversion.

### Understanding: why the reaction time depends on order

Look at the reaction per molecule. The probability that a given molecule reacts per unit time is $`r/c`$.

| Order | Rate $`r`$ | $`\tau_{rxn} = c/r`$ | Per-molecule picture |
|---|---|---|---|
| 0 | $`k_0`$ | $`c/k_0`$ | fixed throughput through saturated sites, so more molecules each wait longer |
| 1 | $`kc`$ | $`1/k`$ | each molecule reacts **independently**, with fixed probability $`k`$ per unit time |
| 2 | $`kc^2`$ | $`1/(kc)`$ | a partner must be met, so a dilute mixture means a longer wait |

**Why first order does not depend on $`c`$.** Algebraically, $`c/(kc) = 1/k`$. Physically, each molecule has a fixed chance of reacting in each instant, like a radioactive nucleus, and the other molecules make no difference to it. A fixed fraction reacts per unit time, whatever the amount present. This is why the batch half-life $`\ln2/k`$ does not depend on $`c_0`$, while the second-order half-life $`1/(kc_0)`$ does.

First order is also the only order for which $`r/c = \partial r/\partial c`$. The balance is then linear, and its gain and time constant are the same at every operating point. Strictly, first order applies to a unimolecular step. A bimolecular reaction $`k_2c\,c_B`$ with B in large excess is **pseudo-first-order**, with $`k = k_2c_B`$, until $`c_B`$ starts to fall.

### Understanding: the dynamic time constant uses the slope of the rate

For $`n\neq1`$ the balance is nonlinear. Linearise about $`c_s`$ using $`kc^n \approx kc_s^n + nkc_s^{n-1}c'`$:


```math
\frac{dc'}{dt} = \frac{c_0'-c'}{\tau_R} - \underbrace{nkc_s^{n-1}}_{\partial r/\partial c}\,c', \qquad \frac{1}{\tau} = \frac{1}{\tau_R} + \frac{\partial r}{\partial c}\bigg|_{c_s}
```


The dynamic reaction time constant is $`1/(\partial r/\partial c) = \tau_{rxn}/n`$, not $`c/r`$. What restores a disturbance is how much faster the reaction runs when $`c`$ rises, not how fast it runs on average. For second order, a 1% rise in $`c`$ raises the rate by 2%, so the restoring effect is twice what $`c/r`$ suggests.

### Understanding: the zero-order case

With $`r = k_0`$, constant, in units of concentration per time:


```math
\frac{dc}{dt} = \frac{c_0-c}{\tau_R} - k_0
```


This is already linear, because the reaction term is a constant.

- **Steady state: the level drops.** $`c_s = c_{0,s} - k_0\tau_R`$. Each feed element spends about $`\tau_R`$ in the tank and loses $`k_0`$ per unit time. This requires $`c_{0,s} > k_0\tau_R`$.
- **Dynamics: no restoring effect.** Subtracting the steady state cancels $`k_0`$, just as a constant term cancels with deviation variables (Q4). This leaves

```math
\tau_R\dot c' + c' = c_0' \quad\Rightarrow\quad G = \frac{1}{\tau_Rs+1}
```

which is exactly the inert-tracer result, shifted down by $`k_0\tau_R`$.

**Why.** Extra tracer doesn't speed up a zero-order reaction, so only flow removes the excess: $`\partial r/\partial c = 0`$. As an analogy, a fixed-rate pump lowers a sink's level but doesn't respond to it, while a plug hole drains faster when the level rises, which is negative feedback. The analogy breaks down at $`c = 0`$: a reaction stops when there is nothing left, but a pump would keep running.

**The reaction acts as a disturbance input.** If $`k_0`$ changes (for example temperature, catalyst activity or enzyme loading):


```math
\tau_R\dot c' + c' = c_0' - \tau_Rk_0' \quad\Rightarrow\quad \frac{C'}{K_0'} = \frac{-\tau_R}{\tau_Rs+1}
```


**Where zero order breaks down.** A rate cannot stay zero-order down to $`c = 0`$. Zero order is the saturated limit of kinetics such as Michaelis–Menten, $`r = V_{max}c/(K_m+c)`$:


```math
\frac{\partial r}{\partial c} = \frac{V_{max}K_m}{(K_m+c)^2}
```


- **$`c\gg K_m`$:** the slope is approximately $`V_{max}K_m/c^2`$, which is small, so the zero-order picture holds.
- **$`c`$ near $`K_m`$ or below:** the slope rises towards $`V_{max}/K_m`$. The reaction starts to restore disturbances, as in first order, and $`\tau`$ drops below $`\tau_R`$.

**Varying $`V`$ or $`q_0`$.** If these vary with time, $`q_0c`$ and $`Vc`$ are products of variables, so the ODE is nonlinear even for first order. Linearise about a steady state before taking a transfer function.

### Key points

- The outlet doesn't change a well-mixed concentration. Only the feed and the reaction do.
- Removal rates add: $`1/\tau = 1/\tau_R + \partial r/\partial c`$. With reaction, $`\tau`$ is not the residence time.
- $`\mathrm{Da} = \tau_R/\tau_{rxn}`$ decides whether flow or chemistry controls the conversion and the speed.
- First order: $`\tau_{rxn} = 1/k`$, independent of $`c`$, because molecules react independently.
- Zero order lowers the level but doesn't restore disturbances. It enters as an input, not as a time constant.
