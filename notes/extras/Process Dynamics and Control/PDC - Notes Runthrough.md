# PDC: Notes Runthrough

Covers: PDC-09–22 (topics 03–08, chapters 1–2). Later chapters will be added as they are released.

A companion to the PDC notes, not a replacement. Each section collects the questions that came up while working through one topic, with the explanation that resolved each one: the physical picture first, then the algebra, with the reason for each non-obvious step. Equation numbers refer to the notes.

Assumed: the PDC notes themselves, plus Year 1–2 Laplace transforms, partial fractions and linear ODEs. Primes denote deviation variables, $`y' = y - y_s`$, never derivatives. Dots denote time derivatives, and $`\bar y = \mathcal{L}[y']`$.

**Contents**

1. 03 - Transfer functions and elementary responses (PDC-09, PDC-10)
2. 04 - Second-order dynamics and damping (PDC-11, PDC-12)
3. 05 - Combining process elements (PDC-13, PDC-14)
4. 06 - Multiple-input multiple-output models (PDC-15, PDC-16)
5. 07 - Poles, zeros, stability and steady-state gain (PDC-17 to PDC-19)
6. 08 - Linearisation around an operating point (PDC-20 to PDC-22)

---

## 03 - Transfer functions and elementary responses

### PDC-09: Where does the step-response partial fraction (Eq. 28) come from?

**Physical picture.** A step holds the input at a new value, so the tank heads for a new steady state. The response is "the new steady state, minus a deficit that decays".

**Algebra.** The step $`x' = \Delta x\,H(t)`$ has transform $`\bar x = \Delta x/s`$. Zero initial state means no initial-condition terms, so


```math
\bar y = G(s)\bar x = \frac{K_p\Delta x}{s(\tau s+1)}
```


The two denominator roots have different origins: $`s=0`$ comes from the **input** (a held step), and $`s=-1/\tau`$ comes from the **process** (its storage).

Partial fractions are needed because the product has no direct table entry, while $`1/s`$ and $`1/(s+a)`$ do. Write $`1 = A(\tau s+1) + Bs`$:

- $`s=0`$ gives $`A=1`$.
- $`s=-1/\tau`$ gives $`1 = -B/\tau`$, so $`B=-\tau`$.


```math
\frac{1}{s(\tau s+1)} = \frac{1}{s} - \frac{\tau}{\tau s+1} = \frac{1}{s} - \frac{1}{s+1/\tau}
```


The last step divides top and bottom by $`\tau`$, which puts the pole in the standard $`1/(s+a)`$ form so it can be read from a table.

| Term | From | Inverse | Meaning |
|---|---|---|---|
| $`K_p\Delta x/s`$ | input pole $`s=0`$ | $`K_p\Delta x`$ | the new steady state |
| $`-K_p\Delta x/(s+1/\tau)`$ | process pole $`-1/\tau`$ | $`-K_p\Delta x\,e^{-t/\tau}`$ | the remaining gap, which shrinks |

At $`t=0`$ the two terms cancel, so $`y'(0)=0`$: storage stops the output from jumping. As $`t\to\infty`$ only $`K_p\Delta x`$ remains. $`\tau`$ appears only in the decaying term, so it controls speed, not endpoint.

### PDC-09: Why is the initial tangent $`(K_p\Delta x/\tau)\,t`$ if it is taken at $`t=0`$?

The **slope** is evaluated at $`t=0`$. The **line** keeps that slope for all later $`t`$.

A straight line needs a point and a slope, both taken from the curve at $`t=0`$:

- point: $`y'(0) = 0`$
- slope: $`\dot y'(0) = \dfrac{K_p\Delta x}{\tau}e^{0} = \dfrac{K_p\Delta x}{\tau}`$


```math
y'_{\mathrm{tan}}(t) = y'(0) + \dot y'(0)\,t = \frac{K_p\Delta x}{\tau}\,t
```


This is the same as $`y = mx + c`$: $`m`$ is found at one point, but $`x`$ still varies. The "≈" in the note means the curve and the tangent agree for small $`t`$, because $`1-e^{-t/\tau} = t/\tau - t^2/(2\tau^2) + \dots`$.

Setting the tangent equal to the final value gives $`t=\tau`$. If the output kept its starting rate, it would arrive in one time constant. The real slope falls straight away, so at $`t=\tau`$ only $`1-e^{-1}\approx 63.2\%`$ of the change is complete. Writing the line as $`y'_{\mathrm{tan}}`$ rather than $`y'`$ avoids the confusion of one symbol for both the curve and the line.

### PDC-09: Why isn't the impulse jump zero, if the formula gives the same value at $`0^-`$ and $`0^+`$?

Eq. (31) holds only **after** the impulse. Before it, the process is at rest. The full solution is


```math
y'(t) = \frac{K_pI_x}{\tau}e^{-t/\tau}H(t)
```


so $`y'(0^-) = 0`$ (the $`t<0`$ branch) and $`y'(0^+) = K_pI_x/\tau`$. Putting both $`0^-`$ and $`0^+`$ into the exponential wrongly assumes the output was already decaying before anything happened.

**The independent check.** Integrate $`\tau\dot y' + y' = K_pI_x\delta(t)`$ from $`0^-`$ to $`0^+`$:


```math
\tau\int_{0^-}^{0^+}\dot y'\,dt + \int_{0^-}^{0^+}y'\,dt = K_pI_x\int_{0^-}^{0^+}\delta(t)\,dt
```


1. Storage term: the integral of a derivative is the change, $`\tau\left[y'(0^+)-y'(0^-)\right]`$.
2. Outflow term: $`y'`$ is finite and the interval has zero width, so it is $`0`$.
3. Input term: $`\delta`$ has unit area however thin it is, so it is $`K_pI_x`$.

Hence $`y'(0^+) = K_pI_x/\tau`$, matching the Laplace result. The asymmetry between terms 2 and 3 is the point: an infinitely tall input survives integration over zero width, an ordinary finite term does not.

**Physical picture.** Dump a mass $`M`$ of tracer into a tank of volume $`V`$ at once. Outflow has no time to remove any of it, so the concentration jumps to $`M/V`$, then washes out. A finite step cannot make a lag jump; only an impulse (infinite height, finite area) can.

### PDC-10: How does the pumped tank become an integrator?

**Balance.** Volume is $`Ah`$ with constant area, so $`A\dot h = q_0 - q`$. The essential assumption is that **neither flow depends on $`h`$**: the inlet is set upstream and the outlet is pumped.

**Deviation form and transform.** The steady state has $`q_{0s} = q_s`$, so subtracting it gives $`A\dot h' = q_0' - q'`$. With $`h'(0)=0`$ and net imbalance $`x' = q_0' - q'`$:


```math
\bar h = \frac{1}{As}\bar x \quad\Leftrightarrow\quad h'(t) = \frac{1}{A}\int_0^t x'\,dt
```


The level is the accumulated net volume divided by area.

**Comparison with a lag.** With a gravity outlet linearised as $`q' = h'/R`$:


```math
A\dot h' = q_0' - \frac{h'}{R} \quad\Rightarrow\quad G = \frac{R}{ARs+1}, \qquad \tau = AR, \quad K_p = R
```


The $`-h'/R`$ term is a **restoring term**: a higher level drains faster until outflow matches the new inflow. A pump removes the same flow at every level, which is the limit $`R\to\infty`$. Then $`R/(ARs+1)\to 1/(As)`$, and both gain and time constant become unbounded: the level never settles.

**Scaled form.** $`A`$ is an area, not a time. With $`y' = h'/h_{\mathrm{ref}}`$ and $`x' = (q_0'-q')/q_{\mathrm{ref}}`$, the balance becomes $`T_H\dot y' = x'`$ with $`T_H = Ah_{\mathrm{ref}}/q_{\mathrm{ref}}`$, the time a reference imbalance takes to change the level by $`h_{\mathrm{ref}}`$. It sets the ramp speed. It is not a time constant: there is no final value to reach 63% of.

### PDC-10: Derive the step and impulse responses of the integrator

The procedure is always: transform the input, multiply by $`G`$, invert.

**Step**, $`x' = \Delta q\,H(t)`$. The input transform is $`\Delta q/s`$, so


```math
\bar h = \frac{\Delta q}{A}\cdot\frac{1}{s^2}
```


The pair $`t\leftrightarrow 1/s^2`$ comes from integration by parts with $`u=t`$, $`dv = e^{-st}dt`$:


```math
\mathcal{L}[t] = \Big[-\frac{t\,e^{-st}}{s}\Big]_0^\infty + \frac{1}{s}\int_0^\infty e^{-st}\,dt = 0 + \frac{1}{s^2}
```


The bracket vanishes at both limits (the factor $`t`$ at $`0`$, the exponential at $`\infty`$). So $`h'(t) = \Delta q\,t/A`$, a ramp. One $`1/s`$ comes from the step and one from the integrator: a double pole at zero gives a ramp.

**Impulse**, $`x' = I_V\delta(t)`$. Treat the impulse as the limit of a pulse of height $`I_V/\varepsilon`$ and duration $`\varepsilon`$:


```math
\bar x = \frac{I_V}{\varepsilon}\cdot\frac{1-e^{-s\varepsilon}}{s} \approx \frac{I_V}{\varepsilon}\cdot\frac{s\varepsilon}{s} = I_V
```


So $`\mathcal{L}[\delta]=1`$: an infinitely short pulse has a transform equal to its area. Then $`\bar h = I_V/(As)`$ and $`h' = I_V/A`$ for $`t>0`$. The level jumps and **stays**, because nothing removes the extra volume.

For a pure integrator the time domain is just as quick, since $`h' = \frac{1}{A}\int x'\,dt`$. The transform route is worth practising because it works the same way once lags, delays and integrators are combined. Each pole at zero, from the input or the process, adds one power of $`t`$.

### PDC-10: What is the "physical memory" represented by $`1/s`$?

Compare the two tanks after a temporary extra inflow of duration $`T`$:

- **Gravity-drained (lag).** While the extra inflow lasts, the level rises, which raises outflow until it matches. When the inflow returns to normal, the level is still raised, so outflow exceeds inflow and the tank drains back. It **forgets** the disturbance.
- **Pumped (integrator).** The level rises at $`\Delta q/A`$ during the pulse. Afterwards $`\dot h' = 0`$, so the level stays at $`\Delta q\,T/A`$ for good.

The steady balance of the pumped tank, $`0 = q_0' - q'`$, **does not contain $`h'`$**. It fixes the flows but not the level, so every level is an equilibrium and the tank stays wherever it was left. The lag's pole at $`-1/(AR)`$ gives the mode $`e^{-t/(AR)}`$, so $`1/(AR)`$ is its forgetting rate. The pump moves the pole to $`0`$, giving the mode $`e^{0t}=1`$: a forgetting rate of zero.

An analogy is a bank account with a fixed standing order: extra income accumulates because nothing spends more as the balance rises. It breaks down at the extremes, since a tank overflows or runs dry, and a real pump's flow drifts slightly with head, which acts like a very large but finite $`R`$. Because a pumped tank never returns by itself, a level controller must supply the restoring action.

### PDC-10: Explain the transport-delay transform (Eq. 34) step by step

1. **Drop the empty interval.** For $`t<t_d`$ the outlet still carries fluid that entered before the disturbance, so $`y'=0`$ and that stretch contributes nothing. The integral starts at $`t_d`$.
2. **Substitute $`\theta = t - t_d`$.** The goal is to make the integrand look like the definition of $`\bar x`$. Then $`dt = d\theta`$, the limits become $`0`$ to $`\infty`$, and $`e^{-st} = e^{-s\theta}e^{-st_d}`$.
3. **Pull out the constant.** $`e^{-st_d}`$ does not depend on $`\theta`$, and what remains is exactly $`\bar x`$:

```math
\bar y = e^{-st_d}\int_0^\infty x'(\theta)e^{-s\theta}\,d\theta = e^{-st_d}\bar x
```

4. **Zero history is required.** If the inlet had already been disturbed before $`t=0`$, the outlet would carry that disturbance on $`0<t<t_d`$. Step 1 would no longer give zero, and $`\bar y`$ would gain a term that is not a multiple of $`\bar x`$.

**What the factor means.**

- A pure shift: every part of the signal arrives $`t_d`$ later, with the same shape.
- Steady gain $`G_d(0) = 1`$, and $`|e^{-i\omega t_d}| = 1`$ at every frequency: a delay adds phase lag but never attenuates, unlike a lag.
- Not a ratio of polynomials, so it has no finite poles and cannot be written as a finite-order ODE.

### PDC-10: What distinguishes a delay from a lag and an integrator?

All three store something, but they remember the past differently. A pipe holds a whole **profile**: each position records a different past moment, and the records stay separate, so nothing is smoothed. A stirred tank holds **one number**, a weighted average of past inputs, and that blending turns a sharp step into a curve.

| Element | Memory of past input | Step response |
|---|---|---|
| Lag | a fading average, weighted by $`e^{-t/\tau}`$ | rises **immediately**, curves to a final value |
| Integrator | the running total, kept forever | **ramps** while the imbalance lasts |
| Delay | an exact copy, held for $`t_d`$ | **nothing**, then the full step at $`t_d`$ |

A lag has a nonzero initial slope, $`K_p\Delta x/\tau`$; it is slow to finish but starts at once. A delay does not respond at all for $`t_d`$. During that time the outlet measurement carries no information about the disturbance or the last control action, which is why delays are hard to control. In a real pipe, dispersion and wall heat transfer round the front, so it looks like a delay followed by a lag.

### PDC-10: Derive $`\bar T_1 = e^{-t_ds}\bar T_0`$ for plug flow from a balance

**Balance on a slice** of a pipe with area $`A`$, constant velocity $`u`$, constant $`\rho`$ and $`c_p`$, no dispersion and no wall heat exchange:


```math
\rho c_pA\Delta z\,\frac{\partial T}{\partial t} = \rho c_puA\,T(z) - \rho c_puA\,T(z+\Delta z) \quad\Rightarrow\quad \frac{\partial T}{\partial t} + u\frac{\partial T}{\partial z} = 0
```


Temperature is carried along at speed $`u`$, with nothing added or smoothed. The steady state is uniform, so the same PDE holds for $`T'`$.

**Transform in time only**, with $`T'(z,0)=0`$ for every $`z`$ (the whole pipe starts at steady state). $`z`$ is not the transform variable, so $`\partial/\partial z`$ passes through the integral:


```math
s\bar T + u\frac{d\bar T}{dz} = 0 \quad\Rightarrow\quad \bar T(z,s) = \bar T_0(s)\,e^{-sz/u}
```


At $`z=L`$, with $`t_d = L/u`$, this gives $`\bar T_1 = e^{-st_d}\bar T_0`$.

Each length $`dz`$ multiplies the transform by $`e^{-s\,dz/u}`$, a delay of $`dz/u`$, and delays in series multiply. The assumptions do real work: dispersion would add $`D\,\partial^2T/\partial z^2`$ (rounding the front), and wall heat loss would add a decay below 1.

**Link to tanks in series.** Discretise into $`n`$ cells of length $`\Delta z = L/n`$ with the upstream difference:


```math
\frac{dT_k}{dt} = \frac{u}{\Delta z}\left(T_{k-1}-T_k\right)
```


This is exactly a stirred tank with $`\tau = t_d/n`$ fed by the cell before it. Refining the grid is the limit $`1/(1+st_d/n)^n\to e^{-st_d}`$. (The PDC notes reach Eq. 34 from the physical time shift instead; this balance route is not in them.)

### PDC-10: Is the pipe's transfer function the same as $`1/(\tau s+1)`$?

No. Applying the same definition, $`G = \mathcal{L}[y']/\mathcal{L}[x']`$ with zero initial deviations, gives different forms because the storage is different:

| | Mixed tank | Plug-flow pipe |
|---|---|---|
| Balance | lumped: $`V\dot T_2 = q(T_1-T_2)`$ | distributed: $`\partial T/\partial t + u\,\partial T/\partial z = 0`$ |
| Zero initial state | one number, $`T_2'(0)=0`$ | a whole profile, $`T'(z,0)=0`$ |
| After transforming | algebraic | still an ODE, in $`z`$ |
| Result | $`1/(\tau s+1)`$, rational, one pole | $`e^{-t_ds}`$, no finite poles |
| $`G(0)`$ | $`1`$ | $`1`$ |

A single tank with $`\tau = t_d`$ matches the pipe only to first order in $`s`$:


```math
e^{-t_ds} = \frac{1}{1 + t_ds + \tfrac12(t_ds)^2 + \dots} \approx \frac{1}{t_ds+1}
```


Both have gain 1 and mean residence time $`-\left.\dfrac{dG}{ds}\right|_{s=0} = t_d`$, but the tank smears the front (variance $`t_d^2`$) while the pipe keeps it sharp. Exact equivalence needs infinitely many tanks.

### Key points

- In $`\bar y = G\bar x`$, separate **input poles** (a step's $`1/s`$ gives the final value) from **process poles** (which give the transient).
- An initial tangent uses the slope at $`t=0`$; the line itself varies with $`t`$.
- Only an impulse can make a lag's output jump; across the impulse the storage term balances the input's area.
- No level-dependent removal term means no restoring action: a pole at zero, a ramp under a step, and a permanent offset after a pulse.
- A delay is a pure time shift with unit gain at every frequency. It is not a lag, and equals a lag only in the limit of infinitely many stages.

---

## 04 - Second-order dynamics and damping

### PDC-11: Physically, how can a system overshoot when $`\zeta<1`$?

**Why a first-order system cannot.** For a lag, $`\tau\dot y' = K_px' - y'`$: the rate is set entirely by the distance from the target and is exactly zero at the target. Speed is not a separate quantity with its own history, so nothing can carry the output past the target.

**What second order adds.** For a mass on a spring, $`m\ddot y' = -ky' - \mu\dot y' + F'`$, the force sets the **acceleration**. Velocity becomes a state with its own memory. After a step in $`F'`$:

1. The mass is far from equilibrium, the net force is large, and kinetic energy builds up.
2. At the target the net force is zero, but the velocity is near its largest.
3. Momentum carries it past; the spring then stops it beyond equilibrium, turning kinetic into elastic energy.
4. The spring pushes it back, and it overshoots the other way, by less each time because of dissipation.

Overshoot happens because the restoring action works through a store (momentum) that keeps acting after the error has gone. The repeated energy swap is the oscillation in time and the imaginary part of the poles in $`s`$.

**What $`\zeta`$ measures.** $`\zeta = \mu/(2\sqrt{mk})`$ compares how fast friction drains velocity ($`\mu/m`$) with how fast the spring swings the mass across ($`\sqrt{k/m}`$); their ratio is $`2\zeta`$. For $`\zeta\geq1`$, the velocity is drained before it can build, and the mass creeps in. For $`\zeta<1`$, momentum survives to the target.

### PDC-11: So a cascade of tanks never overshoots?

Not on its own, for any number of passive, non-interacting stable lags. Three steps show it:

1. A single tank's impulse response, $`\tfrac{1}{\tau}e^{-t/\tau}`$, is never negative.
2. In a cascade the overall impulse response is these non-negative curves convolved together, so it stays non-negative.
3. The step response's slope equals the impulse response, so the step response only ever rises.

Material moves only downstream and each tank only chases the one before it. In PDC-11, $`\zeta = (\tau_1+\tau_2)/(2\sqrt{\tau_1\tau_2})\geq1`$ for any two lags, and interacting tanks are even more overdamped.

Overshoot can still appear when something extra is present:

| Situation | Why it can overshoot |
|---|---|
| feedback control around the tanks | a controller's integral action keeps pushing after the error reaches zero, like momentum |
| a zero from parallel paths | a fast path delivers more than its share early on |
| recycle around three or more units | circulation can give complex poles, usually weakly damped modes dominated by a real one |

Real poles alone do not rule out overshoot. For $`\dfrac{\tau_as+1}{(s+1)(2s+1)}`$, the computed step response peaks at $`1`$ (no overshoot) for $`\tau_a = 0.5`$ and $`2`$, but at $`1.5625`$ for $`\tau_a = 5`$, even though both poles are real and negative. A zero lets the impulse response change sign, which breaks step 1.

### PDC-11: Does oscillation never happen in real processes, then?

It is common, just not from a passive cascade. The structural rule: **one-way coupling** (each state follows the one upstream) gives a monotonic response; **two-way coupling with a sign flip** can oscillate if damping is low enough. Examples:

- **Feedback loops**, the most common source: a badly tuned PI loop makes flow, level or temperature hunt about the setpoint, and delays make it worse.
- **Fluid or mechanical inertia**: a U-tube manometer sloshing, water hammer when a valve closes quickly in a long line, compressor surge.
- **Coupled chemistry and heat**: in an exothermic CSTR, higher $`T`$ speeds reaction, which consumes reactant, which cuts heat release, which lowers $`T`$, while fresh feed restores the reactant.
- **Biology**: glycolytic oscillations, circadian clocks and predator–prey dynamics come from feedback with delay or inhibition.

### PDC-11: Which curves of the damping figure can a given system actually reach?

The figure plots solutions of the general standard form for many $`\zeta`$; mathematically every curve is valid. The physical system decides which $`\zeta`$ it can supply:

| System | $`\zeta`$ | Reachable curves |
|---|---|---|
| two tanks in series | $`\dfrac{\tau_1+\tau_2}{2\sqrt{\tau_1\tau_2}}\geq1`$ | only $`\zeta\geq1`$; equal tanks sit on $`\zeta=1`$ |
| mass–spring–damper | $`\dfrac{\mu}{2\sqrt{mk}}\geq0`$ | all of them |
| process inside a PI loop | set partly by tuning | all of them |

Two tanks and a mass–spring share the same ODE form, but their physical couplings limit the coefficients differently. The $`\zeta=0`$ curve needs zero dissipation, so it is an idealisation; real sustained oscillations are usually nonlinear limit cycles. Controller tuning often aims near $`\zeta\approx0.5`$, trading modest overshoot for speed; pushing above $`\zeta=1`$ removes overshoot but slows the response markedly.

### PDC-12: Derive the second-order step response clearly

**Normalise.** Divide by $`K_p\Delta x`$ and set $`r = y'/(K_p\Delta x)`$, so every response goes from $`0`$ to $`1`$:


```math
\tau^2\ddot r + 2\zeta\tau\dot r + r = 1
```


**Final value plus transient.** A constant particular solution gives $`r_{ss}=1`$. Trying $`e^{pt}`$ in the homogeneous equation gives $`\tau^2p^2 + 2\zeta\tau p + 1 = 0`$, so $`p_{1,2} = \left(-\zeta\pm\sqrt{\zeta^2-1}\right)/\tau`$.

**Initial conditions $`r(0) = \dot r(0) = 0`$.** The slope cannot jump because $`\tau^2\ddot r = 1 - r - 2\zeta\tau\dot r`$ stays finite during a finite step, and a finite acceleration cannot change velocity in zero time.

**Distinct poles.** With $`r = 1 + C_1e^{p_1t} + C_2e^{p_2t}`$, the conditions give $`C_1+C_2 = -1`$ and $`p_1C_1 + p_2C_2 = 0`$. Multiply the first by $`p_2`$ and subtract it from the second:


```math
C_1 = \frac{p_2}{p_1-p_2}, \qquad C_2 = \frac{-p_1}{p_1-p_2} \quad\Rightarrow\quad r = 1 + \frac{p_2e^{p_1t} - p_1e^{p_2t}}{p_1-p_2}
```


This is Eq. (38); at $`t=0`$ the fraction is $`-1`$. It fails at $`\zeta=1`$, where $`p_1=p_2`$.

**Repeated root, $`\zeta=1`$.** $`(\tau p+1)^2 = 0`$ supplies only one exponential, which cannot meet two conditions, so the second independent solution is $`te^{pt}`$. With $`r = 1 + (C_1 + C_2t)e^{-t/\tau}`$: $`r(0)=0`$ gives $`C_1=-1`$; $`\dot r(0) = C_2 - C_1/\tau = 0`$ gives $`C_2 = -1/\tau`$. That is Eq. (39), $`r = 1 - (1+t/\tau)e^{-t/\tau}`$.

**Complex poles, $`0<\zeta<1`$.** Write $`p = -a\pm i\omega_d`$ with $`a = \zeta/\tau`$ and $`\omega_d = \sqrt{1-\zeta^2}/\tau`$. A real output needs the conjugate modes combined as $`r = 1 + e^{-at}(C\cos\omega_dt + D\sin\omega_dt)`$. Then:

- $`r(0)=0`$ gives $`C=-1`$.
- By the product rule, $`\dot r = e^{-at}\left[(-aC + \omega_dD)\cos\omega_dt + (-aD - \omega_dC)\sin\omega_dt\right]`$, and $`\dot r(0) = 0`$ gives $`D = aC/\omega_d = -\zeta/\sqrt{1-\zeta^2}`$.

This is Eq. (40).

**Why the cosine terms cancel in $`\dot r`$.** The cosine coefficient $`-aC + \omega_dD`$ is the very combination set to zero by the slope condition, so it vanishes for all $`t`$. The sine coefficient is $`(a^2 + \omega_d^2)/\omega_d`$, and $`a^2 + \omega_d^2 = 1/\tau^2`$, so


```math
\dot r = \frac{e^{-\zeta t/\tau}}{\tau\sqrt{1-\zeta^2}}\sin\omega_dt
```


**Peaks and decay ratio.** The prefactor is positive, so extrema fall at $`\sin\omega_dt = 0`$. At the first peak, $`t_p = \pi/\omega_d`$, the cosine is $`-1`$, so $`r(t_p) = 1 + e^{-at_p}`$. The excess equals the envelope at that instant, which gives Eq. (41). The next peak above 1 is a full period later, so


```math
\frac{C}{A} = e^{-2a\pi/\omega_d} = \left(\frac{A}{B}\right)^2
```


The decay ratio is the overshoot squared because the first peak is half a period from the start and the next same-side peak is a full period later. For $`\zeta=0.5`$ the computed overshoot is $`0.163`$ and the decay ratio $`0.0266`$.

**Geometry.** Since $`a^2 + \omega_d^2 = 1/\tau^2`$, the poles lie on a circle of radius $`1/\tau`$, and $`\zeta`$ is the cosine of their angle from the negative real axis. $`\zeta`$ sets the angle, hence the overshoot; $`\tau`$ sets the distance from the origin, hence the speed. $`\tau`$ cancels in $`A/B`$.

### PDC-12: What happens to $`n`$ tanks in series as $`n\to\infty`$?

It depends on what is held fixed.

- **Each tank fixed at $`\tau`$.** $`G = 1/(\tau s+1)^n`$. Each tank adds smoothing and another $`\tau`$ of mean lag, so the response gets slower and centres near $`n\tau`$. As $`n\to\infty`$ it never arrives.
- **Total residence time $`\theta`$ fixed, $`\tau = \theta/n`$.** This is one vessel divided into more compartments:

```math
G = \frac{1}{(\theta s/n + 1)^n} \;\xrightarrow{\;n\to\infty\;}\; e^{-\theta s}
```

The cascade becomes a pure delay: plug flow.

Computed unit-step responses for $`\theta = 1`$ (the Erlang cumulative distribution):

| $`n`$ | $`y`$ at $`t=\theta`$ | 10% reached at | 90% reached at | 10–90% width |
|---|---|---|---|---|
| 1 | 0.632 | 0.105 | 2.303 | 2.20 |
| 2 | 0.594 | 0.266 | 1.945 | 1.68 |
| 5 | 0.560 | 0.487 | 1.599 | 1.11 |
| 20 | 0.530 | 0.726 | 1.295 | 0.57 |
| 100 | 0.513 | 0.874 | 1.130 | 0.26 |

What changes as $`n`$ grows:

1. **The start flattens.** Only $`n=1`$ has a nonzero initial slope; near $`t=0`$ the response goes like $`(t/\tau)^n/n!`$, so a high-order lag looks like a delay although no element waits.
2. **It becomes S-shaped and centres on $`\theta`$**, with $`y(\theta)`$ moving from 63% towards 50%.
3. **The spread shrinks as $`1/\sqrt{n}`$.** The impulse response has mean $`\theta`$ and standard deviation $`\theta/\sqrt{n}`$; quadrupling $`n`$ halves the width.
4. **It never oscillates.** All $`n`$ poles sit at $`-n/\theta`$, real and negative, and move to $`-\infty`$ as $`n\to\infty`$.

With $`\tau`$ fixed instead, the absolute spread grows as $`\sqrt{n}\,\tau`$ but the delay grows as $`n\tau`$, so relative to its own delay the front still sharpens as $`1/\sqrt{n}`$. This is the tanks-in-series reactor model, with $`\sigma^2/\theta^2 = 1/n`$, and the reason first-order-plus-dead-time models fit high-order processes so often.

### Key points

- Overshoot needs a momentum-like store: a state that keeps acting after the error reaches zero.
- A passive cascade of lags is monotonic for any $`n`$. Overshoot needs feedback, opposing parallel paths (zeros) or circulation.
- The same ODE form does not give the same reachable $`\zeta`$: physical coupling limits the coefficients.
- In the second-order step response, initial conditions fix the transient weights, the cosine cancels in $`\dot r`$, peaks fall at multiples of $`\pi/\omega_d`$, and the decay ratio is the overshoot squared.
- Many small mixed stages at fixed total volume approach a pure delay, with front width $`\propto1/\sqrt{n}`$.

---

## 05 - Combining process elements

### PDC-13: How does the tank lag come from the general energy balance?

1. **General balance** on tank $`i`$, with enthalpy relative to $`T_{\mathrm{ref}}`$:

```math
\frac{d}{dt}\left[\rho V_ic_p(T_i - T_{\mathrm{ref}})\right] = \rho qc_p(T_{i-1}-T_{\mathrm{ref}}) - \rho qc_p(T_i - T_{\mathrm{ref}}) + Q - W_s
```

The outlet is at $`T_i`$ because the tank is perfectly mixed.
2. **Assumptions.** Insulated and no work, so $`Q = W_s = 0`$; inflow equals outflow, so $`V_i`$ is constant; constant $`\rho`$ and $`c_p`$. The $`T_{\mathrm{ref}}`$ terms cancel, and dividing by $`\rho c_p`$ gives $`V_i\dot T_i = q(T_{i-1} - T_i)`$.
3. **Deviation form.** The steady state gives $`T_{i,s} = T_{i-1,s}`$. Subtracting it gives $`V_i\dot T_i' = q(T_{i-1}' - T_i')`$, exact only because $`q`$ is constant; a varying flow would make $`qT`$ a product needing linearisation.
4. **Normalise by the restoring coefficient $`q`$.** $`\tau_i\dot T_i' + T_i' = T_{i-1}'`$ with $`\tau_i = V_i/q`$: storage over removal gives the residence time, and input over removal gives gain 1, because an insulated tank ends at its feed temperature.
5. **Transform.** $`\bar T_i/\bar T_{i-1} = 1/(\tau_is+1)`$.

### PDC-13: In Eq. (43), why isn't the pipe written as another $`1/(\tau s+1)`$ block?

$`G`$ is a generic label for "output transform over input transform"; it does not mean a lag. Each block's form comes from its own balance:

| Block | Element | Transfer function |
|---|---|---|
| $`G_1`$ | plug-flow pipe, $`T_0\to T_1`$ | $`e^{-t_ds}`$ |
| $`G_2`$ | mixed tank, $`T_1\to T_2`$ | $`1/(\tau_2s+1)`$ |
| $`G_3`$ | mixed tank, $`T_2\to T_3`$ | $`1/(\tau_3s+1)`$ |

Substituting through the chain gives $`\bar T_3 = G_3G_2G_1\bar T_0`$. The pipe cannot use the lag form because it moves the front without blending it. What the blocks share is the definition (a ratio of deviation transforms with zero initial state), and that shared definition is what allows multiplying them.

### PDC-13: In Step 3, how does $`e^{-t_ds}`$ become $`1/s`$?

It doesn't. The $`1/s`$ comes from the **step input**, $`\bar T_0 = \Delta T_0/s`$:


```math
\bar T_3 = \underbrace{e^{-t_ds}}_{\text{pipe}}\cdot\underbrace{\frac{1}{(\tau s+1)^2}}_{\text{two equal tanks}}\cdot\underbrace{\frac{\Delta T_0}{s}}_{\text{step}}
```


"Remove the delay" means set it aside: write $`\bar T_3 = e^{-t_ds}F(s)`$, invert $`F`$, then shift.

**Invert $`F`$.** With $`1 = A(\tau s+1)^2 + Bs(\tau s+1) + Cs`$: $`s=0`$ gives $`A=1`$; $`s=-1/\tau`$ gives $`C=-\tau`$; the $`s^2`$ coefficients give $`A\tau^2 + B\tau = 0`$, so $`B=-\tau`$. Using $`\mathcal{L}[te^{-at}] = 1/(s+a)^2`$ (the pair $`t\leftrightarrow1/s^2`$ with $`s`$ shifted by $`a`$):


```math
f(t) = \Delta T_0\left[1 - \left(1 + \frac{t}{\tau}\right)e^{-t/\tau}\right]
```


**Shift by $`t_d`$**, replacing **every** $`t`$ with $`t - t_d`$ and setting the response to zero before $`t_d`$. This gives Eq. (44).

If only the exponential were shifted, at $`t = t_d`$ the bracket would give $`1 - (1 + t_d/\tau) = -t_d/\tau`$: a jump to a negative value when the front arrives, impossible behind two tanks, and a violation of the zero starting conditions the partial fractions were built on. Shifting the whole curve keeps it causal: zero until its cause arrives.

To see the shapes, a plotting tool can draw the pipe alone (a jump at $`t_d`$), pipe plus one tank (a rise starting at $`t_d`$ with nonzero slope) and pipe plus two tanks (zero slope at $`t_d`$, S-shaped). Moving $`t_d`$ slides the curve sideways; increasing $`\tau`$ stretches the rise without changing the final value.

### PDC-13: Gain, the repeated pole and the shift

- **Zero-frequency gain** $`G(0)`$ is the final output change per unit step, from the final value theorem. Each block has $`G(0)=1`$ (the pipe passes the temperature unchanged; insulated tanks end at their feed temperature), so the product is 1 and $`T_3'(\infty) = \Delta T_0`$. Heat loss would make a tank's gain less than 1.
- **The repeated pole** supplies $`te^{-t/\tau}`$. It decays, so it cannot change the endpoint, but it changes the shape. Differentiating $`f`$,

```math
\dot f = \Delta T_0\,\frac{t}{\tau^2}e^{-t/\tau}
```

which is zero at $`t=0`$: tank 2 cannot warm until tank 1 has warmed. Poles decide how the output gets there; the gain decides where it ends.
- **The repeated pole belongs to the ODE.** Eliminating the intermediate tank gives $`\tau^2\ddot T_3' + 2\tau\dot T_3' + T_3' = T_1'`$, whose characteristic equation is $`(\tau p+1)^2 = 0`$. Transforming with zero initial conditions turns $`d^n/dt^n`$ into $`s^n`$, so the poles of $`G`$ are the characteristic roots. Substitution confirms $`te^{-t/\tau}`$ solves the homogeneous equation. The repeated root gives the form; the zero starting slope fixes its coefficient at $`-\Delta T_0/\tau`$.

### PDC-13: How is the intermediate tank's temperature found?

Only the upstream elements matter. Tank 2's balance,


```math
\rho V_2c_p\dot T_2 = \underbrace{\rho qc_pT_1}_{\text{gain from the pipe}} - \underbrace{\rho qc_pT_2}_{\text{loss to tank 3}}
```


already contains its loss to the next tank, which depends only on $`q`$ and $`T_2`$. $`T_3`$ does not appear: tank 3 receives the flow but sends nothing back. So multiply the blocks up to the point of interest:


```math
\bar T_2 = G_2G_1\bar T_0 = \frac{e^{-t_ds}}{\tau_2s+1}\cdot\frac{\Delta T_0}{s} \quad\Rightarrow\quad T_2'(t) = \Delta T_0\left[1 - e^{-(t-t_d)/\tau_2}\right],\ t\geq t_d
```


This is a delayed first-order response with no S-shape; the S-shape appears only at tank 3. Downstream effects matter only for **two-way coupling**: interacting tanks (the downstream level sets the upstream outflow), recycle or backmixing, or heat conduction through a shared wall. Then the balances must be solved together, which is the MIMO approach.

### PDC-14: Why is a heat input $`Q`$ now allowed?

$`Q=0`$ in PDC-13 only because those tanks had no heater. PDC-14 adds one to show two inputs adding at one output: feed temperature as the disturbance and heater power as the manipulated input.

With $`C_f = \rho qc_p`$, the balance $`\rho Vc_p\dot T = C_f(T_0 - T) + Q`$ has steady state $`T_s = T_{0,s} + Q_s/C_f`$. Subtracting cancels the baseline duty, leaving only $`Q'`$; dividing by $`C_f`$ gives Eq. (45):


```math
\tau\dot T' + T' = T_0' + \frac{Q'}{C_f}
```


$`Q'/C_f`$ is the feed-temperature change that would deliver the same extra heat, which is why it can be added to $`T_0'`$.

A heater is not a heat loss:

| Term | Depends on $`T`$? | Effect |
|---|---|---|
| heater $`Q`$ | no, set externally | an extra **input** path, $`1/(C_f(\tau s+1))`$ |
| heat loss $`UA(T - T_a)`$ | yes | an extra **removal** term |

With heat loss, $`\rho Vc_p\dot T' = C_fT_0' - (C_f + UA)T' + Q'`$. Dividing by $`C_f + UA`$ gives a faster time constant, $`\rho Vc_p/(C_f+UA)`$, and a gain below 1, $`C_f/(C_f + UA)`$.

### PDC-14: What does duplicating a signal mean?

A block-diagram line carries the **value** of a variable, not material. A branch point copies the value to each destination; it never divides it. Even a physical flow splitter divides the flow but not the temperature, which is intensive. Halving a signal at a branch is a common factor-of-two error.

The measured value is $`\bar T_m = G_m\bar T`$. A thermocouple bead obeys $`m_bc_b\dot T_m = h_bA_b(T - T_m)`$, so


```math
G_m = \frac{1}{\tau_ms+1}, \qquad \tau_m = \frac{m_bc_b}{h_bA_b}
```


the same storage-over-restoring structure as a tank. It reads correctly eventually, $`G_m(0)=1`$, but lags. The controller acts on $`T_m`$, so this pole sits inside the feedback loop. "Loading" is the exception to the branch idea: a sensor that removes noticeable heat from the process, such as a heavy thermowell in a small vessel, must go into the energy balance as a real heat term.

| Diagram feature | Rule |
|---|---|
| blocks in series | multiply |
| summing junction | add with signs, in the same units |
| branch point | copy: every branch carries the full value |

### PDC-14: Why must dynamic compensation cancel "as functions of $`s`$, not merely at $`s=0`$"?

$`G(0)`$ says how much the output finally changes; the dependence on $`s`$ says when and how. Cancelling at $`s=0`$ means equal and opposite final effects; cancelling at all $`s`$ means the effects cancel at every instant.

**No actuator lag.** A $`5\ \mathrm{K}`$ feed drop and a simultaneous heater step worth $`5\ \mathrm{K}`$ both pass through the same tank lag, so they are identical curves of opposite sign and cancel at every $`t`$.

**Heater with actuator lag** $`1/(\tau_as+1)`$. Both paths still have gain 1, so $`T'(\infty) = 0`$, but the heater contribution builds up more slowly. Combining,


```math
\bar T = -\frac{5\tau_a}{(\tau s+1)(\tau_as+1)} \quad\Rightarrow\quad T'(t) = -\frac{5\tau_a}{\tau - \tau_a}\left(e^{-t/\tau} - e^{-t/\tau_a}\right)
```


For $`\tau = 100\ \mathrm{s}`$ and $`\tau_a = 20\ \mathrm{s}`$, the computed dip reaches $`-0.669\ \mathrm{K}`$ at $`t\approx40\ \mathrm{s}`$, is $`-0.062\ \mathrm{K}`$ at $`300\ \mathrm{s}`$, and is negligible by $`600\ \mathrm{s}`$.

**Physically.** The cold feed acts at once while the heater is still ramping up, so less heat arrives than needed and the tank cools. Once the heater reaches full power the deficit stops growing. The tank is then below target, so its outflow carries away less enthalpy than at steady state, and that small surplus refills the lost heat through self-regulation. The size of the correction was right; its timing was wrong.

Exact cancellation would need the heater command to include $`(\tau_as + 1)`$, an initial extra kick. A pure $`(\tau_as+1)`$ needs an instantaneous spike, so real feedforward uses a lead–lag approximation. The steady part of feedforward is easy; the timing is the hard part.

### Series and parallel combinations

- **Series, non-interacting:** $`\bar y = G_n\cdots G_1\bar x`$. Poles accumulate, the response becomes slower and S-shaped, and no zeros are created.
- **Signals at a junction:** add with signs, $`\bar y = (G_1\pm G_2)\bar x`$. This can create zeros, including inverse response.
- **Merging material streams with constant flows:** the merged composition is a flow-weighted average, so $`G = w_1G_1 + w_2G_2`$ with $`w_i = q_i/\sum q_j`$ and $`w_1 + w_2 = 1`$.

For example, with a fraction $`f`$ bypassing a tank,


```math
G = f + \frac{1-f}{\tau s+1} = \frac{f\tau s+1}{\tau s+1}
```


The weights sum to 1, so $`G(0) = 1`$ and no material is lost. If the flows themselves vary, the products $`q_ic_i`$ must be linearised first.

### Key points

- Every $`G`$ uses the same definition, but its form comes from its own balance: a pipe is $`e^{-t_ds}`$, a mixed tank is a lag.
- A step's $`1/s`$ gives the final value; the delay is never inverted on its own but shifts the finished curve, with every $`t`$ replaced.
- Gains multiply along a series chain; repeated poles change the shape, not the endpoint.
- Non-interacting stages depend only on what is upstream.
- An input term (heater) adds a path; a state-dependent term (heat loss) changes the time constant and gain.
- A branch copies a value; a sensor adds its own lag.
- Feedforward must match timing, not just steady size.

---

## 06 - Multiple-input multiple-output models

### PDC-15: What does an entry of the matrix mean? Must feed B take a particular value?

An entry is a **response rule**, not a value. $`G_{ij}`$ answers: if input $`j`$ changes in some way, with the other inputs fixed, how does output $`i`$ respond? The input change is yours to choose:


```math
\bar c_B = G_{22}(s)\,\bar c_{B0} = \frac{1}{\tau s+1}\bar c_{B0} \qquad (\bar c_{A0} = 0)
```


A step $`\Delta_B`$ gives $`c_B' = \Delta_B(1 - e^{-t/\tau})`$; doubling the step doubles the response.

$`G_{22}`$ is the transfer function of a non-reacting tank: extra B only mixes and washes through, because nothing consumes it. $`G_{12} = 0`$ says feed B has no effect on A, since the reaction is irreversible. The pattern of zero and nonzero entries maps which inputs reach which outputs.

### PDC-15: Why is a column sum the response of the total concentration to one feed?

Write the matrix out:


```math
\bar c_A = G_{11}\bar c_{A0} + G_{12}\bar c_{B0}, \qquad \bar c_B = G_{21}\bar c_{A0} + G_{22}\bar c_{B0}
```


"Holding the other feed fixed" means its deviation is zero, so with $`\bar c_{B0} = 0`$ only column 1 survives. Transforms are linear, so the transform of a sum is the sum of the transforms:


```math
\overline{c_A + c_B} = \bar c_A + \bar c_B = (G_{11} + G_{21})\,\bar c_{A0}
```


Going down a column adds the species; that is why the result is the total. This holds for any matrix. Conservation is the extra fact that decides what the sum turns out to be.

### PDC-15: Why does conservation make every column sum equal to $`1/(\tau s+1)`$?

**Algebra.** Over the common denominator,


```math
\frac{1}{\tau s+1+k\tau} + \frac{k\tau}{(\tau s+1)(\tau s+1+k\tau)} = \frac{(\tau s+1) + k\tau}{(\tau s+1)(\tau s+1+k\tau)} = \frac{1}{\tau s+1}
```


The numerator turns out to be the reaction factor, so the reaction pole cancels.

**Why it must.** Adding the two balances cancels the reaction terms ($`-k\tau c_A`$ and $`+k\tau c_A`$), giving Eq. (50), a non-reacting tank. Transform it and compare it with the sum of the matrix rows:


```math
\bar c_T = \frac{1}{\tau s+1}\bar c_{A0} + \frac{1}{\tau s+1}\bar c_{B0} = (G_{11} + G_{21})\,\bar c_{A0} + (G_{12} + G_{22})\,\bar c_{B0}
```


Both expressions hold for any inputs, so each column sum equals the coefficient of its own feed in Eq. (50). Both feeds enter Eq. (50) with coefficient 1, because the total does not care which species a molecule entered as. So both column sums are $`1/(\tau s+1)`$.

**Physical picture.** Label every molecule. The reaction only relabels A as B; the total changes only through inflow and outflow. So the total responds like an inert tracer whatever $`k`$ is, and an extra unit of either feed counts the same.

### PDC-15: Do row sums give the same result?

No. Only the two **column** sums are equal to each other:

| Sum | Result |
|---|---|
| column 1 | $`\dfrac{1}{\tau s+1}`$ |
| column 2 | $`\dfrac{1}{\tau s+1}`$ |
| row 1 | $`\dfrac{1}{\tau s+1+k\tau}`$ |
| row 2 | $`\dfrac{\tau s+1+2k\tau}{(\tau s+1)(\tau s+1+k\tau)}`$ |

A row sum is one output's response when both feeds change by the same amount at once. No conservation law lies behind that experiment, so nothing simplifies. Summing outputs matches a conserved quantity; summing inputs does not.

### PDC-15: Why does the check test "more than the final numbers"?

At $`s=0`$ (steady state, where every derivative vanishes, and where $`\lim_{t\to\infty}y' = G(0)\Delta`$ for a stable system) the column gives $`\frac{1}{1+k\tau} + \frac{k\tau}{1+k\tau} = 1`$: unconverted plus converted is everything fed. That tests only the endpoint. Steady state here is not chemical equilibrium: the reactor is still reacting, but inflow, outflow and reaction balance.

The identity holds for every $`s`$, so it tests the whole time course. For example, the wrong entry $`G_{21} = k\tau/[(1+k\tau)(\tau s+1)]`$ has the correct steady gain, so a final-value check passes, but its column sum does not reduce to $`1/(\tau s+1)`$.

**Fast A, slow total.** A has two ways out (outflow and reaction), so its pole is $`-(1+k\tau)/\tau`$. The total has one (outflow), so its pole is $`-1/\tau`$. For a step $`\Delta`$ in feed A,


```math
c_B' = c_T' - c_A' = \Delta\left(1 - e^{-t/\tau}\right) - \frac{\Delta}{1+k\tau}\left(1 - e^{-(1+k\tau)t/\tau}\right)
```


B carries both modes, with its fast mode opposite in sign to A's, so the fast modes cancel exactly in the total.

### PDC-15: What changes for $`A\to\nu B`$?

With constant volume and flow, each A consumed makes $`\nu`$ B, so only the B source term changes: $`\tau\dot c_B + c_B = c_{B0} + \nu k\tau c_A`$. Only $`G_{21}`$ changes, scaled by $`\nu`$:


```math
G_{21} = \frac{\nu k\tau}{(\tau s+1)(\tau s+1+k\tau)}
```


The plain column sum is now $`\dfrac{(\tau s+1) + \nu k\tau}{(\tau s+1)(\tau s+1+k\tau)}`$, which cancels only for $`\nu=1`$. Steady gains with $`k\tau = 1`$:

| $`\nu`$ | A out | B out | total out per unit extra feed A |
|---|---|---|---|
| 0 | 0.5 | 0 | 0.5 (moles lost) |
| 1 | 0.5 | 0.5 | 1 (conserved) |
| 2 | 0.5 | 1.0 | 1.5 (moles created) |
| 3 | 0.5 | 1.5 | 2.0 |

**The fix:** weight by stoichiometry to count a conserved quantity. $`\nu\times`$ the A balance plus the B balance cancels the reaction:


```math
\tau\frac{d(\nu c_A + c_B)}{dt} + (\nu c_A + c_B) = \nu c_{A0} + c_{B0}, \qquad \nu G_{11} + G_{21} = \frac{\nu}{\tau s+1}
```


In practice this is an atom balance. In the gas phase, a change in moles changes the volumetric flow and breaks the constant-$`\tau`$ balances; a rate such as $`kc_A^2`$ for $`2A\to B`$ must be linearised first.

### PDC-16: Why is the vapour mass loss $`\rho_G\,dV_L`$?

The vessel is rigid, so $`V_G = V_T - V_L`$ and the vapour gives up exactly the volume the liquid gains. At fixed pressure the saturated vapour density is fixed, so it cannot become denser to fit the smaller space. Hence $`dm_G = \rho_G\,dV_G = -\rho_G\,dV_L`$, and


```math
\dot M = \rho_L\dot V_L - \rho_G\dot V_L = (\rho_L - \rho_G)\dot V_L = F - G
```


The balance does not need to know whether that vapour left through the steam line or condensed. If pressure could rise, the vapour could be compressed instead, a $`\dot\rho_G`$ term would appear, and pressure dynamics would enter. With the illustrative 8 bar values used below, the computed $`\rho_L/\rho_G\approx214`$, so the correction is small but needed for an exact balance.

### PDC-16: Derive the boiler energy balance (Eq. 51)

Stored energy is $`U = \rho_L\hat U_LV_L + \rho_G\hat U_G(V_T - V_L)`$. Differentiating at fixed properties gives $`\dot U = (\rho_L\hat U_L - \rho_G\hat U_G)\dot V_L`$. The open-system first law, ignoring kinetic and potential energy, with no shaft work and no heat loss, is $`\dot U = F\hat H_F - G\hat H_G + Q_H`$.

**Why $`\hat U`$ for storage and $`\hat H`$ for streams.** Pushing a kilogram into or out of a pressurised vessel involves flow work $`P\hat v`$, so each stream carries $`\hat U + P\hat v = \hat H`$. The vessel is rigid, so storage is just $`U`$. Here $`P`$ and $`V_T`$ are both fixed, so $`H = U + PV_T`$ has $`\dot H = \dot U`$, and using $`\hat H`$ for storage would give the same left side, since $`P\left(\rho_L\cdot\tfrac{1}{\rho_L} - \rho_G\cdot\tfrac{1}{\rho_G}\right)\dot V_L = 0`$. $`\hat U`$ is the general rule.

### PDC-16: Derive $`a`$, $`b`$, $`c`$, $`d`$ and explain their meaning

With $`D_\rho = \rho_L - \rho_G`$ and $`D_U = \rho_L\hat U_L - \rho_G\hat U_G`$:

1. **Mass gives** $`G = F - D_\rho\dot V_L`$.
2. **Substitute into energy:** $`D_U\dot V_L = F(\hat H_F - \hat H_G) + D_\rho\hat H_G\dot V_L + Q_H`$.
3. **Collect $`\dot V_L`$**, multiplying by $`-1`$ so the coefficient is positive:

```math
B\dot V_L = F(\hat H_G - \hat H_F) - Q_H, \qquad B = D_\rho\hat H_G - D_U = \rho_L(\hat H_G - \hat U_L) - \rho_G(\hat H_G - \hat U_G)
```

4. **Divide by $`B`$:** $`a = (\hat H_G - \hat H_F)/B`$ and $`b = -1/B`$.
5. **Back to mass:** $`G = F - D_\rho(aF + bQ_H)`$, so $`c = 1 - D_\rho a`$ and $`d = -D_\rho b = D_\rho/B`$.

$`B`$ is the heat needed to boil off one cubic metre of liquid: about latent heat, corrected for vapour already in the vacated space.

Illustrative values at 8 bar with feed at 160 °C: $`\hat H_F = 675.5`$, $`\hat H_G = 2768.3`$, $`\hat U_L = 720.0`$, $`\hat U_G = 2576.0\ \mathrm{kJ\,kg^{-1}}`$; $`\rho_L = 896.9`$, $`\rho_G = 4.2\ \mathrm{kg\,m^{-3}}`$. The computed values are:

| Coefficient | Meaning (other input fixed) | Value |
|---|---|---|
| $`a`$ | extra feed → level rise rate | $`1.14\times10^{-3}\ \mathrm{m^3\,kg^{-1}}`$ |
| $`b`$ | extra heat → level fall rate | $`-5.45\times10^{-7}\ \mathrm{m^3\,kJ^{-1}}`$ |
| $`c`$ | extra feed → steam change | $`-0.0174`$ |
| $`d`$ | extra heat → extra steam | $`4.86\times10^{-4}\ \mathrm{kg\,kJ^{-1}}`$ |

with $`B = 1.84\times10^{6}\ \mathrm{kJ\,m^{-3}}`$.

- $`a`$: an extra kilogram of feed would need $`\hat H_G - \hat H_F`$ to become steam. That energy is not supplied, so dividing it by the energy per cubic metre boiled gives the liquid volume left behind. It is slightly more than $`1/\rho_L = 1.115\times10^{-3}\ \mathrm{m^3\,kg^{-1}}`$, because the inventory also keeps liquid that no longer boils.
- $`b`$: each kJ boils off $`1/B`$ of liquid volume.
- $`d`$: the computed $`1/d\approx2057\ \mathrm{kJ\,kg^{-1}}`$, close to the latent heat at 8 bar.
- Holding the level steady needs $`aF' + bQ_H' = 0`$, so $`Q_H'/F' = -a/b = \hat H_G - \hat H_F`$, computed as $`2092.8\ \mathrm{kJ\,kg^{-1}}`$: the full heat to turn the extra feed into steam.

### PDC-16: Why can extra feed reduce steam, and how is that compatible with mass conservation?

Over the common denominator,


```math
c = \frac{D_\rho\hat H_F - D_U}{B} = \frac{\rho_L(\hat H_F - \hat U_L) - \rho_G(\hat H_F - \hat U_G)}{B}
```


The computed terms are $`-39\,912`$ and $`+7\,982\ \mathrm{kJ\,m^{-3}}`$. The first dominates because the feed is subcooled, so part of the fixed heat warms the feed instead of boiling. For saturated feed the first term almost vanishes and $`c\approx0`$.

**Signs follow the energy pathways.** Extra heat boils liquid, so $`b<0`$ and $`d>0`$; the liquid lost equals the steam gained. Extra subcooled feed accumulates ($`a>0`$) and diverts heat into warming, so steam falls slightly ($`c<0`$).

**Mass check.** Accumulation is $`F' - G'`$, and $`D_\rho a`$ is computed as $`1.0174\ \mathrm{kg\,s^{-1}}`$ per $`\mathrm{kg\,s^{-1}}`$ of extra feed. The vessel keeps the full extra feed plus liquid that would have boiled. The surprise is only in how mass splits between staying and leaving. Raising feed to restore level therefore briefly cuts steam, a counter-intuitive effect for an operator. Real drums also show "shrink and swell" from bubble volume, which this fixed-pressure model omits.

### PDC-16: Why are $`a`$–$`d`$ exact partial derivatives?

At fixed pressure and feed temperature every property in them is constant, and no term multiplies two variables. Solving linear equations gives linear results, so $`\dot V_L = aF + bQ_H`$ with constant $`a`$ and $`b`$, and $`\partial(aF + bQ_H)/\partial F = a`$ everywhere, with no Taylor remainder. If feed temperature varied, $`F\hat H_F`$ would be a product of variables, and the coefficients would become derivatives evaluated at one operating point, valid only for small deviations. "Exact" means exact within the fixed-pressure model.

### PDC-16: Why is the level an integrator but the steam flow instantaneous?

- **Level.** $`\dot V_L' = aF' + bQ_H'`$ has **no $`V_L'`$ term**: feed and heat are set externally, and boiling depends on heat, not on how much liquid is present. A constant imbalance gives $`V_L' = (aF' + bQ_H')\,t`$; no level is a new equilibrium. Only rebalancing feed and heat, or a level controller, stops the drift. The model fails if the level uncovers the heating tubes, because boiling then depends on level.
- **Steam.** $`G' = cF' + dQ_H'`$ has no $`s`$. At fixed pressure the vapour density is fixed, so the vapour space cannot store extra steam; whatever is produced leaves at once.

**What a real boiler adds:**

| Missing effect | What it stores | What it adds |
|---|---|---|
| pressure dynamics | vapour mass as density rises with pressure | a lag in $`G`$ |
| heat transfer through the tubes | heat in the metal | a lag in the effective $`Q_H`$ |
| bubbles in the liquid | vapour volume | shrink and swell: the level can briefly move the wrong way |

### Key points

- A matrix entry is a response function: choose the input change, the entry gives the output.
- A column sum is the response of the summed outputs to one feed. Conservation makes it independent of the reaction; weight by stoichiometry when moles change.
- Steady-state checks test endpoints; identities in $`s`$ test the whole time course.
- Store with $`\hat U`$, transport with $`\hat H`$.
- In the boiler, level is an integrator and steam flow is algebraic at fixed pressure. Subcooled feed slightly reduces steam because it diverts heat.

---

## 07 - Poles, zeros, stability and steady-state gain

### PDC-17: What does "poles describe the free dynamic modes visible in an input–output model" mean?

- **Free:** how the system behaves once the input stops pushing it, starting from a disturbed state. That behaviour belongs to the process.
- **Modes:** each pole $`p`$ contributes the pattern $`e^{pt}`$. Every response is built from these plus terms from the input itself.
- **Visible in an input–output model:** a mode appears as a pole of $`G`$ only if the input can excite it and the output can see it. Otherwise it cancels from that $`G`$ while still existing inside the process.

For example, the reaction mode in PDC-15 appears in $`c_A`$ and $`c_B`$ separately but cancels from the total $`c_A + c_B`$.

| Pole | Mode | Behaviour |
|---|---|---|
| real, $`-1/\tau`$ | $`e^{-t/\tau}`$ | decays |
| at zero | $`1`$ | holds constant (integrator memory) |
| repeated | $`e^{pt}`$, $`te^{pt}`$, … | polynomial factor |
| complex pair $`-a\pm i\omega`$ | $`e^{-at}\cos\omega t`$, $`e^{-at}\sin\omega t`$ | decaying oscillation |
| positive real part | growing | unstable |

### PDC-17: Why do the imaginary terms cancel for a complex pair (Eq. 55)?

**Pairs exist** because $`D(s)`$ has real coefficients (built from real physical quantities), so $`D(p^*) = [D(p)]^* = 0`$ whenever $`D(p) = 0`$. The same holds for the residues: the residue at $`p^*`$ is $`C^*`$.

**Algebra.** With $`p = a + ib`$, $`C = \alpha + i\beta`$ and Euler's formula:


```math
Ce^{pt} = e^{at}\Big[(\alpha\cos bt - \beta\sin bt) + i(\alpha\sin bt + \beta\cos bt)\Big]
```


The conjugate term has the same real part and the opposite imaginary part, so


```math
Ce^{pt} + C^*e^{p^*t} = 2e^{at}\left[\alpha\cos bt - \beta\sin bt\right] = 2|C|e^{at}\cos(bt + \phi), \qquad \phi = \arg C
```


This is $`z + z^* = 2\,\mathrm{Re}\,z`$. The output is physical, so it must be real; imaginary parts that fail to cancel signal an unconjugated residue. The pole fixes decay ($`a`$) and frequency ($`b`$); the residue, set by input and output, fixes size and phase. PDC-12's direct sine–cosine form is justified by this.

### PDC-17: How does pole position set the shape of a mode?

1. **Simple real pole $`-r`$:** mode $`e^{-rt}`$ with time constant $`1/r`$. Further left means faster decay; poles nearest the imaginary axis govern the slow tail.
2. **Complex pair $`a\pm ib`$:** the cosine changes sign every $`\pi/|b|`$, inside an envelope $`\pm2|C|e^{at}`$ fixed by $`a`$. Moving left speeds the decay; moving up or down changes only the frequency.
3. **Repeated negative pole:** $`te^{-rt}`$ is $`t`$ (growing) times $`e^{-rt}`$ (shrinking). Since $`\frac{d}{dt}\left(te^{-rt}\right) = e^{-rt}(1 - rt)`$, it peaks at $`t = 1/r`$, then decays: an exponential beats any polynomial. Two equal tanks have impulse response $`\frac{t}{\tau^2}e^{-t/\tau}`$: tracer reaches tank 2, peaks at $`t=\tau`$, then washes out. Rising before decaying is not instability.
4. **Repeated pole at zero:** no exponential to win. $`1/s`$ gives a constant, $`1/s^2`$ gives $`t`$, $`1/s^3`$ gives $`t^2/2`$. A frictionless mass with no spring is a double integrator: one kick gives constant velocity and position $`\propto t`$ without limit, so repeated imaginary-axis poles are unstable even without forcing.

### PDC-17: How can cancellation hide a mode from one transfer function?

A pole's residue is roughly (how strongly the input drives the mode) × (how strongly the output reads it). If either is zero, the numerator has a zero at $`s = p`$ and the factor cancels.

| Situation | Example | Safe? |
|---|---|---|
| output blind to the mode | total $`c_A + c_B`$ in PDC-15 | yes, if the hidden mode is stable |
| input not connected to the mode | feed B column in PDC-15 | yes, if stable |
| an unstable pole cancelled by a zero | open-loop compensation below | **no** |

### PDC-17: Why does open-loop pole cancellation fail?

**Setup.** An unstable process, such as an exothermic CSTR at an unstable operating point, modelled in scaled deviation variables as


```math
\dot y' = y' + u' \quad\Rightarrow\quad G_p = \frac{1}{s-1}
```


Its free mode $`e^{+t}`$ grows.

**The block in front.** The operator gives a command $`r`$, and a controller computes $`u`$ from it, open loop (it never measures $`y`$). The controller is an algorithm or circuit, so its transfer function is a design choice. Choosing $`C(s)`$ means programming the ODE it represents; for example


```math
C(s) = \frac{s-1}{s+1} = 1 - \frac{2}{s+1} \quad\Rightarrow\quad u = r - 2w, \quad \dot w = -w + r
```


which needs one stored variable and no differentiation. The limits on this freedom: $`C`$ must be proper (a pure $`s-1`$ needs a differentiator, which amplifies noise without bound), causal, achievable by real actuators, and it assumes the process pole is known exactly.

**Why try it.** Giving the block a numerator $`(s-1)`$ cancels the denominator: $`\bar y/\bar r = 1/(s+1)`$, which looks like a stable lag. Starting from rest, the block shapes $`u`$ so the growing mode is never fed.

**Why it fails.** $`G`$ is defined with zero initial state and $`r`$ as the only input. Transform the process with a general $`y'(0)`$:


```math
s\bar y - y'(0) = \bar y + \bar u \quad\Rightarrow\quad \bar y = \underbrace{\frac{1}{s+1}\bar r}_{\text{path through }C} + \underbrace{\frac{y'(0)}{s-1}}_{\text{stored state, no block}}
```


The initial condition acts like an impulse injected **between** the block and the process. It never passes through $`C`$, so nothing cancels its $`(s-1)`$, and it inverts to $`y'(0)\,e^{+t}`$. The transfer function is correct, but its definition deletes exactly the term where the unstable mode survives. A real $`y'(0)`$ is never exactly zero: the computed growth of $`y'(0) = 0.001`$ is to $`0.148`$ by $`t = 5`$ and $`22.0`$ by $`t = 10`$. A disturbance entering at the process input bypasses $`C`$ in the same way, and a slight model mismatch (a true pole at $`1.01`$) leaves a small but growing term.

**What works.** Feedback, $`u' = K(r' - y')`$, gives $`\dot y' = (1-K)y' + Kr'`$: the pole moves to $`1 - K`$, stable for $`K>1`$. The restoring term acts on $`y`$ itself, so it corrects any initial condition or disturbance. Feedback moves an unstable pole; open-loop cancellation only hides it.

### PDC-18: What does the zero at $`+1`$ mean?

**Setup.** One input is copied to two parallel paths and subtracted at a junction:

- path 1: $`\dot y_1 + y_1 = 4x'`$, gain 4, time constant 1: slow and strong
- path 2: $`\dot y_2 + 2y_2 = 6x'`$, gain 3, time constant $`0.5`$: fast and weaker in the end
- output $`y' = y_1 - y_2`$


```math
G(s) = \frac{4}{s+1} - \frac{6}{s+2} = \frac{4(s+2) - 6(s+1)}{(s+1)(s+2)} = \frac{2(1-s)}{(s+1)(s+2)}
```


**Meaning.** Neither path has a zero alone. $`G(s) = 0`$ where $`4/(s+1) = 6/(s+2)`$, at $`s = 1`$: the one value where the opposing paths have equal strength and cancel. An input shaped like $`e^{t}`$ would produce equal and opposite path outputs, so a zero blocks one input shape. It adds no state: the modes are only $`e^{-t}`$ and $`e^{-2t}`$, and the zero changes their weights. A **pole** at $`+1`$, by contrast, is a growing mode $`e^{t}`$.

**Why a right-half-plane zero means inverse response.** Low $`s`$ describes late behaviour and high $`s`$ early behaviour. $`G(0) = 1>0`$, so the strong path wins in the end. As $`s\to\infty`$, $`G\approx(4-6)/s = -2/s`$, so the initial slope is $`-2`$. $`G`$ changes sign along the positive real axis, so it must cross zero there.

**Series cannot do this.** Series blocks multiply: $`\frac{4}{s+1}\cdot\frac{6}{s+2} = \frac{24}{(s+1)(s+2)}`$, with a constant numerator and no zero. Zeros come from adding pathways; a right-half-plane zero needs opposing paths where the faster one loses in the long run. Boiler drum level shows this physically: cold feed first collapses bubbles (fast, negative), then adds inventory (slow, positive).

### PDC-18: What is feedthrough, and how does it differ from inverse response and delay?

**Strictly proper paths cannot jump.** Every such path passes through storage, so a finite step changes only the rate. The initial value theorem gives $`y'(0^+) = G(\infty)\Delta x = 0`$; only the slope jumps.

**Feedthrough.** If numerator and denominator degrees are equal, long division gives $`G = D_0 + G_{sp}`$, and $`y'(0^+) = D_0\Delta x`$. Some input reaches the output without storage. A tank with bypass fraction $`f`$ is an example:


```math
T_{\mathrm{out}} = fT_{\mathrm{in}} + (1-f)T_{\mathrm{tank}} \quad\Rightarrow\quad G = f + \frac{1-f}{\tau s+1}
```


The outlet jumps by $`f\Delta T`$ at once, then the rest follows the lag. The fixed-pressure boiler steam flow is pure feedthrough.

| Feature | In $`G(s)`$ | Step response | Physical cause |
|---|---|---|---|
| feedthrough jump | $`G(\infty) = D_0\neq0`$ | instant jump, then gradual | a path with no storage |
| inverse response | right-half-plane zero | continuous, starts the wrong way | opposing parallel paths |
| dead time | $`e^{-t_ds}`$ | flat for $`t_d`$, then responds | transport |

The way a response starts identifies the cause, and each needs a different control approach.

### PDC-19: Why does a settled output satisfy $`\Delta y = K_p\Delta x`$?

Settled means $`\dot y' = 0`$. Substituting into $`\tau\dot y' + y' = K_px'`$ removes the storage term and leaves the restoring term balancing the input. $`\tau`$ sets how fast; $`K_p`$ sets where. This equals $`G(0)`$. It requires a stable lag that actually settles, a restoring term (an integrator, $`\tau\dot y' = x'`$, gives only $`0 = x'`$ and ramps instead), and an input held long enough for the transient to die. $`y'`$ here is the deviation from the initial steady state, not a derivative.

### PDC-19: Derive the final value theorem (Eq. 59) and Eq. 60

**Derivation.** Start from $`\int_0^\infty\dot y'\,e^{-st}\,dt = s\bar y - y'(0)`$. Let $`s\to0`$: the left side becomes $`\int_0^\infty\dot y'\,dt = y'(\infty) - y'(0)`$. Cancelling $`y'(0)`$ gives


```math
\lim_{t\to\infty}y'(t) = \lim_{s\to0}s\bar y(s)
```


Taking $`s\to0`$ inside the integral is valid only if $`y'`$ settles, so that the integral converges.

**Eq. 60.** Zero state means no initial-condition terms, so $`\bar y = G\bar x`$; a step has $`\bar x = \Delta x/s`$. Then $`s\bar y = G(s)\Delta x`$, the $`s`$ cancelling the step's $`1/s`$, and


```math
\Delta y = \Delta x\lim_{s\to0}G(s), \qquad K_p = G(0)
```


For an integrator $`G(0)`$ is infinite, correctly signalling no finite gain.

### PDC-19: Why does the theorem need every nonconstant term to decay?

In partial fractions, $`\bar y = A/s + \sum_jC_j/(s - p_j)`$ and $`y = A + \sum_jC_je^{p_jt}`$. Multiplying by $`s`$ and letting $`s\to0`$ keeps $`A`$ and sends every $`sC_j/(s-p_j)`$ with $`p_j\neq0`$ to zero, whatever that mode does. The theorem returns the constant term, which is the final value only if every other term decays.

| $`\bar y`$ | Theorem gives | True $`y(t)`$ | Problem |
|---|---|---|---|
| $`\dfrac{1}{s(s+1)}`$ | $`1`$ | $`1 - e^{-t}\to1`$ | none |
| $`\dfrac{1}{s(s-1)}`$ | $`-1`$ | $`-1 + e^{t}\to\infty`$ | the growing mode is ignored |
| $`\dfrac{1}{s(s^2+1)}`$ | $`1`$ | $`1 - \cos t`$ | never settles; $`1`$ is the average |
| $`\dfrac{1}{s^2}`$ | $`\infty`$ | $`t`$ | the ramp does not decay |

Check first that every pole of $`s\bar y`$ is strictly in the left half-plane.

### Key points

- Poles give the modes; residues give their weights in a particular response.
- Conjugate pairs combine into real damped sinusoids: real part for decay, imaginary part for frequency.
- Repeated poles multiply modes by powers of $`t`$: harmless with exponential decay, unstable on the imaginary axis.
- Transfer functions show only modes connecting that input to that output. An unstable pole cancelled open loop still grows from initial conditions and disturbances; feedback is needed to move it.
- A zero marks cancellation between pathways; a right-half-plane zero means early and late responses have opposite signs.
- A jump means feedthrough, a wrong-way start means opposing paths, a flat start means transport delay.
- $`K_p = G(0)`$ and the final value theorem hold only when the response settles.

---

## 08 - Linearisation around an operating point

### PDC-20: What does the notation in Eq. 61 mean?

| Symbol | Meaning |
|---|---|
| $`f(y,x)`$ | the right-hand side of $`\dot y = f(y,x)`$: the net rate of change, possibly nonlinear |
| $`(y_s,x_s)`$ | the steady operating point; subscript $`s`$ means steady |
| $`f(y_s,x_s) = 0`$ | nothing changes at steady state, so the constant term drops out |
| $`y'`$, $`x'`$ | deviations from the operating point |
| $`\dot y'`$ | equals $`\dot y`$, because $`y_s`$ is constant |
| $`f_y\vert_s`$, $`f_x\vert_s`$ | $`\partial f/\partial y`$ and $`\partial f/\partial x`$ evaluated at $`(y_s,x_s)`$: sensitivities of the rate to state and input |
| $`\approx`$ | quadratic and product terms in deviations are dropped |

For a CSTR with second-order reaction, $`f(c,c_0) = \frac{q}{V}(c_0 - c) - kc^2`$ gives


```math
f_c\big|_s = -\frac{q}{V} - 2kc_s, \qquad f_{c_0}\big|_s = \frac{q}{V}
```


$`f_c`$ contains $`c`$, so its value depends on the chosen steady state: that is what "local" means. $`f_y|_s`$ plays the restoring coefficient.

### PDC-20: Derive Eq. 62, and what are $`X`$ and $`Y`$ in Eq. 63?

With $`a = f_y|_s`$ and $`b = f_x|_s`$ constant, transform $`\dot y' = ay' + bx'`$ with zero initial deviation:


```math
s\bar y = a\bar y + b\bar x \quad\Rightarrow\quad G(s) = \frac{b}{s-a}
```


The local slope is the pole. For $`a<0`$, divide top and bottom by $`-a`$:


```math
G = \frac{-b/a}{(-1/a)s + 1} \quad\Rightarrow\quad \tau = -\frac{1}{a}, \qquad K_p = -\frac{b}{a}
```


which is "divide by the restoring coefficient": storage 1, restoring $`-a`$, input $`b`$. If $`a = 0`$, the linear model is an integrator and higher-order terms decide whether the real system drifts. If $`a>0`$, the operating point is locally unstable.

In Eq. (63), $`G = \bar c_A/\bar c_{A0}`$: tank concentration deviation over feed concentration deviation, with $`q`$, $`V`$ and $`T`$ fixed. Naming the input and output explicitly avoids the ambiguity.

### PDC-20: Give a simple case that needs linearisation

An isothermal CSTR with first-order reaction where the **input is the flow** $`q`$, with $`c_0`$ fixed:


```math
V\dot c = q(c_0 - c) - kVc
```


$`qc`$ is a product of two changing variables, so the balance is nonlinear even for first order. With $`c_0`$ as the input it would be linear: the choice of input decides whether linearisation is needed.

Expand with deviations, cancel the steady balance and drop $`q'c'`$:


```math
V\dot c' = (c_0 - c_s)\,q' - (q_s + kV)\,c'
```


Keep both linear terms: flow changes the feed term and the washout. Dividing by the restoring coefficient,


```math
G = \frac{\bar c}{\bar q} = \frac{K}{\tau s+1}, \qquad \tau = \frac{V}{q_s + kV}, \qquad K = \frac{c_0 - c_s}{q_s + kV}
```


The gain is proportional to $`c_0 - c_s`$: extra flow helps only because it brings feed richer than the tank. Reaction and washout both remove A, so $`\tau`$ is shorter than $`V/q_s`$.

With $`V = 2\ \mathrm{m^3}`$, $`k = 0.005\ \mathrm{s^{-1}}`$, $`c_0 = 1\ \mathrm{kmol\,m^{-3}}`$ and $`q_s = 0.01\ \mathrm{m^3\,s^{-1}}`$, the computed values are $`c_s = 0.5\ \mathrm{kmol\,m^{-3}}`$, $`\tau = 100\ \mathrm{s}`$ (against $`V/q_s = 200\ \mathrm{s}`$) and $`K = 25\ \mathrm{kmol\,m^{-3}}`$ per $`\mathrm{m^3\,s^{-1}}`$. Final changes:

| Flow step as % of $`q_s`$ | Linear $`\Delta c`$ | Exact $`\Delta c`$ | Linear overestimates by |
|---|---|---|---|
| 5% | 0.0125 | 0.0122 | 2.5% |
| 20% | 0.0500 | 0.0455 | 10% |
| 50% | 0.125 | 0.100 | 25% |

The exact $`c_s(q)`$ flattens as the tank approaches feed concentration, so the tangent overshoots more as the step grows.

### PDC-20: Where do the partial derivatives come in?

They give the same result. Writing $`f(c,q) = \frac{q}{V}(c_0 - c) - kc`$:


```math
a = \frac{\partial f}{\partial c}\bigg|_s = -\frac{q_s + kV}{V}, \qquad b = \frac{\partial f}{\partial q}\bigg|_s = \frac{c_0 - c_s}{V}
```


Multiplying $`\dot c' = ac' + bq'`$ by $`V`$ reproduces the hand expansion, and $`\tau = -1/a`$, $`K = -b/a`$ agree. Expanding brackets and keeping linear terms is a first-order Taylor expansion; the dropped $`q'c'`$ is the second-order part. Brackets work only for products and powers; otherwise differentiate:

| Nonlinearity | Example | Linear coefficient |
|---|---|---|
| square root | gravity outflow $`q = k_v\sqrt{h}`$ | $`\dfrac{k_v}{2\sqrt{h_s}}`$ |
| Arrhenius | $`k(T) = k_0e^{-E/RT}`$ | $`k_s\dfrac{E}{RT_s^2}`$ |
| valve characteristic | flow vs opening and pressure drop | partials of the valve equation |

The habit: write $`\dot y = f(y,x)`$, find the steady state, take both partials there, and read off $`\tau`$ and $`K`$.

### PDC-21: What is quasi-steady outflow?

The outlet is assumed to obey its steady relation $`q = k\sqrt{h}`$ at every instant, as if the outflow adjusts instantly to each new level. A momentum balance on the outlet liquid, length $`L`$, is roughly


```math
\rho L\frac{dv}{dt} = \rho gh - \tfrac12\rho v^2(1 + K_f)
```


and quasi-steady sets the left side to zero, giving $`v\propto\sqrt{h}`$. This works because the fluid accelerates in about $`L/v`$ (seconds) while the level changes over $`Ah/q`$ (minutes or more). Treating the fast process as algebraic removes its state and keeps the model first order, as for the boiler's steam flow. It fails for long outlet lines (momentum becomes a second state, and the momentum–level coupling can oscillate like a U-tube), fast valve closure (water hammer) and sloshing.

### PDC-21: Compare the linear and exact final levels (Eq. 66)

**Linear.** $`h'_{\mathrm{lin}}(t) = K_p\Delta q_0(1 - e^{-t/\tau})`$, so $`h'_{\mathrm{lin},\infty} = K_p\Delta q_0`$ once the exponential has died. Eq. (66) compares final values, so the exponential plays no part.

**Exact.** At the new steady state, $`q_{0s} + \Delta q_0 = k\sqrt{h_\infty}`$. Subtract $`h_s = (q_{0s}/k)^2`$ and expand:


```math
h'_{\mathrm{exact},\infty} = \frac{2q_{0s}}{k^2}\Delta q_0 + \left(\frac{\Delta q_0}{k}\right)^2 = \underbrace{K_p\Delta q_0}_{h'_{\mathrm{lin},\infty}} + \underbrace{\left(\frac{\Delta q_0}{k}\right)^2}_{\text{dropped by linearisation}}
```


using $`2q_{0s}/k^2 = 2\sqrt{h_s}/k = K_p`$.

The extra term is a square, so the true level is always higher than predicted: a step up rises more, a step down falls less. Outflow $`\propto\sqrt{h}`$ bends over, so it increases less than the tangent suggests, and the tank must rise further to pass the new flow. The relative error is


```math
\frac{(\Delta q_0/k)^2}{K_p\Delta q_0} = \frac{\Delta q_0}{2q_{0s}}
```


half the fractional flow step.

### PDC-21: What does the exact integral (Eq. 67) do?

It gives the whole exact curve for a step, written as $`t(h)`$.

1. **Substitute $`z = \sqrt{h}`$.** By the chain rule $`\dot h = 2z\dot z`$, and with $`z_f = q_0/k`$ (the final $`\sqrt{h}`$), the balance becomes $`2Az\dot z = k(z_f - z)`$, linear on the right.
2. **Separate:** $`dt = \dfrac{2A}{k}\cdot\dfrac{z}{z_f - z}\,dz`$.
3. **Divide the fraction** so it integrates: $`\dfrac{z}{z_f - z} = -1 + \dfrac{z_f}{z_f - z}`$.
4. **Integrate** from $`z_0 = \sqrt{h_s}`$, using $`\frac{d}{dz}\ln|z_f - z| = -1/(z_f - z)`$, to obtain Eq. (67).

It is implicit: pick levels, compute times, plot. At $`t = 0`$ both models have slope $`\Delta q_0/A`$, because the same imbalance fills the same area. Near the end the logarithm dominates, and the approach looks like a lag with $`\tau_{\mathrm{end}} = 2A\sqrt{h_\infty}/k`$, the linear formula at the **new** level, which is slower for a step up.

Computed for $`A = 1\ \mathrm{m^2}`$, $`k = 0.01\ \mathrm{m^{2.5}\,s^{-1}}`$ and $`h_s = 1\ \mathrm{m}`$ (so $`\tau = 200\ \mathrm{s}`$ and $`K_p = 200\ \mathrm{s\,m^{-2}}`$), level rise above $`h_s`$:

| Inflow step | Quantity | Linear | Exact |
|---|---|---|---|
| +10% | at $`t = \tau`$ | $`0.126\ \mathrm{m}`$ | $`0.128\ \mathrm{m}`$ |
| | final | $`0.200\ \mathrm{m}`$ | $`0.210\ \mathrm{m}`$ |
| | time to 95% of own change | $`599\ \mathrm{s}`$ | $`650\ \mathrm{s}`$ |
| +50% | at $`t = \tau`$ | $`0.632\ \mathrm{m}`$ | $`0.659\ \mathrm{m}`$ |
| | final | $`1.00\ \mathrm{m}`$ | $`1.25\ \mathrm{m}`$ |
| | time to 95% of own change | $`599\ \mathrm{s}`$ | $`856\ \mathrm{s}`$ |

The integral is more accurate but less useful: it works only for a step, gives no transfer function to combine or analyse, and is implicit. Its role is as a benchmark for how large a step the linear model can take.

### PDC-21: What does each technique need, and how is it used?

| Technique | Needs | How it is used | Gives |
|---|---|---|---|
| 1. Linearise | a steady operating point, $`f`$ differentiable there, small deviations | steady state → partials at it → deviation ODE → transform → $`\tau`$, $`K_p`$ | $`G(s)`$ for any input, block diagrams, stability |
| 2. Exact steady state | input held constant, stable equilibrium | set $`\dot h = 0`$ in the full balance, solve, subtract $`h_s`$ | the true endpoint only |
| 3. Exact integration | constant input, one separable state, an integral doable by hand | substitute, separate, partial fractions, integrate to $`t(h)`$ | the exact curve for a step |
| 4. Numerical integration | the full ODE, initial state, input history, a solver | integrate forward; halve the step or tolerance to check | any input, size or number of states, as numbers only |

The usual workflow: design with the linear model, then check its predictions for the expected sizes of change against the exact steady state and a numerical simulation.

### PDC-22: What is $`x_s`$, and why does its formula add terms from two streams?

Only **one species** is tracked: the tracer. Every $`x`$ is a tracer content in volume percent: $`x_A = 100`$ (stream A is pure tracer), $`x_B = 2`$, and $`x_s`$ is the tank's steady tracer content. The sum is over **streams**, not species.

**Steady tracer balance** (in = out):


```math
x_s\sum_iq_i = \sum_ix_iq_i \quad\Rightarrow\quad x_s = \frac{100\,q_{As} + q_{Bs}x_{Bs}}{q_{As} + q_{Bs}}
```


- Tracer in: each stream carries composition × flow.
- Tracer out: one outlet, whose flow equals the total inflow (constant volume) and whose composition is $`x_s`$ (perfect mixing).
- Assumptions: steady state, constant volume and density with additive volumes, perfect mixing, inert tracer.

**Percent, not fractions.** With fractions $`\phi = x/100`$, pure A has $`\phi_A = 1`$ and the balance is $`1\cdot q_A + \phi_Bq_B = (q_A + q_B)\phi`$. Multiplying by 100 gives the note's form; the factor cancels. The conventions cannot be mixed: $`1\cdot q_A + x_Bq_B`$ with $`x_B = 2`$ is wrong. The gains inherit the convention, so $`K_v`$ is in percentage points per percentage point.

**Meaning.** $`x_s`$ is the flow-weighted average of the feeds. The computed flow fractions are $`0.02`$ for A and $`0.98`$ for B, and the tracer contributions are $`14`$ and $`13.72`$, so $`x_s = 3.96`$. A sample from any tank at steady state is $`3.96\%`$ tracer. With no reaction, tank 2's steady balance $`0 = q(x_s - x_2)`$ gives $`x_2 = x_s`$, and likewise tank 3, so one equilibrium holds throughout. The non-tracer balance, $`(100 - x_s)(q_A + q_B) = 0\cdot q_A + (100 - 2)q_B`$, follows automatically. $`x_s`$ is both the deviation baseline and the linearisation point.

**Time constant.** $`\tau = V/(q_{As} + q_{Bs})`$, computed as $`5.00\ \mathrm{min}`$: storage $`V`$ over removal by washout. With no reaction it equals the residence time. It uses the steady total flow, because the valve's effect on residence time enters only through the dropped product $`q_A'x_1'`$. All three tanks share it, giving the triple pole at $`-0.2\ \mathrm{min^{-1}}`$.

### PDC-22: Why hold $`q_B`$ fixed?

It is a choice of which inputs to study: $`q_A`$ (through the valve) is the manipulated variable, $`x_B`$ the disturbance, and $`q_B`$ is assumed steady from upstream. Holding it fixed leaves only $`q_A'x_1'`$ as a product to drop. If $`q_B`$ varied, linearisation would add a third input by superposition:


```math
K_{qB} = \frac{x_{Bs} - x_s}{q_{As} + q_{Bs}}
```


which is negative, because extra stream B brings in 2% and pushes out 3.96%.

### PDC-22: Why is the valve gain $`(100 - x_s)`$, and why does the flow not affect tanks 2 and 3?

**Tank 1.** Extra flow $`q_A'`$ does two things: it brings in $`100\,q_A'`$ of tracer, and, since the volume is fixed, it pushes out the same extra volume of mixture at about $`x_s`$, removing $`x_sq_A'`$. In the algebra, the outflow term expands as


```math
(q_{As} + q_{Bs} + q_A')(x_s + x_1') = (q_{As} + q_{Bs})x_s + (q_{As} + q_{Bs})x_1' + x_sq_A' + q_A'x_1'
```


The net is $`(100 - x_s)q_A'`$, so $`K_q = (100 - x_s)/(q_{As} + q_{Bs})`$. Ignoring the displacement overstates the effect; at $`x_s = 100`$ the valve would do nothing. Analogy: topping up an overflowing pot of soup with brine, where the salt gained is the salt added minus the salt spilt; it fails if the pot is not well mixed. The $`x_s`$ is the operating-point value of the outflow composition, accurate while $`x_1`$ stays close to it.

**Tank 2.** $`V\dot x_2 = q(x_1 - x_2)`$. Both baselines are $`x_s`$, so $`x_1 - x_2 = x_1' - x_2'`$ and


```math
V\dot x_2' = q_s(x_1' - x_2') + \underbrace{q_A'(x_1' - x_2')}_{\text{deviation}\times\text{deviation, dropped}}
```


At the operating point, extra flow into tank 2 brings fluid identical to its contents, like replacing water with the same water. So the valve affects tanks 2 and 3 only through tank 1, giving one gain and the cascade $`x_1'\to x_2'\to x_3'`$.

### PDC-22: Derive Eqs. 70 and 71

**Eq. 70.** Substitute $`q_A' = k_vv'`$ into tank 1, so its input term becomes $`K_vv'`$ with $`K_v = K_qk_v`$. Transform each tank with zero initial deviation and chain them:


```math
\bar x_3 = \frac{1}{\tau s+1}\cdot\frac{1}{\tau s+1}\cdot\frac{K_B\bar x_B + K_v\bar v}{\tau s+1} = \frac{K_B}{(\tau s+1)^3}\bar x_B + \frac{K_v}{(\tau s+1)^3}\bar v
```


Computed gains: $`K_B = 0.98`$ (B is 98% of the flow), $`K_q = 13.72`$ and $`K_v = 0.038416`$ percentage points per percentage point of valve opening. Both inputs enter only at tank 1, so they share the triple lag and differ only in gain.

**Eq. 71.** For a valve step, $`\bar x_3 = K_v\Delta v/[s(\tau s+1)^3]`$. A triple pole needs every power up to three:


```math
1 = A(\tau s+1)^3 + Bs(\tau s+1)^2 + Cs(\tau s+1) + Ds
```


$`s = 0`$ gives $`A = 1`$; $`s = -1/\tau`$ gives $`D = -\tau`$; the $`s^3`$ coefficients give $`B = -\tau`$; the $`s^2`$ coefficients, $`3A\tau^2 + 2B\tau + C\tau = 0`$, give $`C = -\tau`$.

**The telescoping check.** Combining terms one at a time, each step uses $`(\tau s+1) - \tau s = 1`$ and absorbs one more factor:


```math
\frac{1}{s} - \frac{\tau}{\tau s+1} = \frac{1}{s(\tau s+1)}, \qquad \frac{1}{s(\tau s+1)} - \frac{\tau}{(\tau s+1)^2} = \frac{1}{s(\tau s+1)^2}, \qquad \frac{1}{s(\tau s+1)^2} - \frac{\tau}{(\tau s+1)^3} = \frac{1}{s(\tau s+1)^3}
```


which is also why every coefficient is $`-\tau`$.

**Inversion.** Writing each term as $`1/(s+1/\tau)^j`$ and using Eq. (54):

| Term | Inverse |
|---|---|
| $`\dfrac{\tau}{\tau s+1}`$ | $`e^{-t/\tau}`$ |
| $`\dfrac{\tau}{(\tau s+1)^2}`$ | $`\dfrac{t}{\tau}e^{-t/\tau}`$ |
| $`\dfrac{\tau}{(\tau s+1)^3}`$ | $`\dfrac{t^2}{2\tau^2}e^{-t/\tau}`$ |

Each extra repeat adds the next power of $`t`$; with $`\tau = 5\ \mathrm{min}`$ the quadratic term is $`t^2/50`$. Near $`t = 0`$ the bracket of Eq. (71) behaves like $`\tfrac16(t/\tau)^3`$, so value, slope and curvature all start at zero. The computed fractions of the final change are 8.0% at $`t = \tau`$, 57.7% at $`3\tau`$ and 87.5% at $`5\tau`$: the single-lag 63.2% rule does not apply to the cascade.

### Key points

- Linearise with partial derivatives at a consistent steady state; for products, expanding brackets is the same first-order Taylor expansion.
- $`\tau = -1/a`$ and $`K_p = -b/a`$: divide by the restoring coefficient. The coefficients depend on the operating point.
- Whether linearisation is needed depends on which variable is the input.
- Linear errors grow with step size; for the square-root tank the endpoint error is $`\Delta q_0/(2q_{0s})`$ and always in the same direction.
- Exact solutions are benchmarks; linear models are the design tool; numerical integration handles large or complicated changes.
- In mixing, the gain of an extra pure stream is (incoming composition − tank composition)/total flow; downstream tanks feel a flow change only at second order.
