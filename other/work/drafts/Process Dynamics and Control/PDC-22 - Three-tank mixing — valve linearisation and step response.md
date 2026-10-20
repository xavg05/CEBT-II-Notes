# PDC-22: Three-tank mixing: valve linearisation and step response

## Overview

Assumed: component balances, deviation variables, series lags and local linearisation.

A three-tank mixer combines variable-flow nonlinearity with a cascade of concentration lags. The valve and disturbance gains must use a consistent steady composition and an explicit percentage convention.

## Intuition

Opening the pure-tracer valve adds tracer, but it also increases total flow and changes residence time. The local model captures the first-order composition effect while dropping products of flow and concentration deviations. Downstream tanks smooth that change twice more.

## Derivation

**Step 1: define the composition convention and equilibrium.** Three perfectly mixed tanks have equal fixed volume $V=35\ \mathrm{m^3}$; their outlet flows follow the combined inlet flow, maintaining each volume. Stream A is pure inert tracer; stream B contains tracer concentration $x_B$ expressed as a numerical **volume percent**, so pure A has $x_A=100$, not $1$. Assume equal constant densities and additive volumes.

![Three tanks mixing pure tracer and a dilute tracer stream](../figs/PDC-22-three-tank-mixer.png)

Let flows be $q_A,q_B$ in $\mathrm{m^3\,min^{-1}}$, tank volume-percent compositions $x_1,x_2,x_3$, and valve position $v$ as a numerical percent open. A linear valve gives $q_A=k_vv$, $k_v=0.0028\ \mathrm{m^3\,min^{-1}}$ per percentage point. At $v_s=50$, $q_{As}=0.14$; take $q_{Bs}=6.86$ and $x_{Bs}=2$. Then

$$x_s=\frac{100q_{As}+q_{Bs}x_{Bs}}{q_{As}+q_{Bs}}=3.96,
\qquad \tau=\frac{V}{q_{As}+q_{Bs}}=5.00\ \mathrm{min}.\tag{68}$$

*Reason:* every tank has the same steady composition from the combined feed balance. Retain this equilibrium throughout the perturbation model.

**Step 2: expand tank 1's balance.** Hold $q_B=q_{Bs}$ while $q_A$ and $x_B$ can change:

$$V\dot x_1=100q_A+q_{Bs}x_B-(q_A+q_{Bs})x_1.
$$

Substitute $q_A=q_{As}+q_A'$, $x_B=x_{Bs}+x_B'$ and $x_1=x_s+x_1'$ and cancel the steady balance:

$$V\dot x_1'=-(q_{As}+q_{Bs})x_1'+q_{Bs}x_B'
+(100-x_s)q_A'-q_A'x_1'.
$$

*Reason:* the valve perturbation increases tracer inflow by $100q_A'$ and removes more tank mixture by $x_sq_A'$; their difference sets its local concentration sensitivity. Neglect the product $q_A'x_1'$ and divide by total steady flow:

$$\tau\dot x_1'+x_1'=K_Bx_B'+K_q q_A',\quad
K_B=\frac{q_{Bs}}{q_{As}+q_{Bs}},\quad
K_q=\frac{100-x_s}{q_{As}+q_{Bs}}.\tag{69}$$

**Step 3: linearise the downstream tanks.** Tank 2 obeys $V\dot x_2=(q_A+q_{Bs})(x_1-x_2)$. Because its two baseline compositions are equal, the flow perturbation multiplies only a concentration deviation:

$$\tau\dot x_2'+x_2'=x_1',\qquad
\tau\dot x_3'+x_3'=x_2',\qquad q_A'=k_vv'.
$$

*Reason:* drop the second-order product of flow deviation and concentration difference. Transform and multiply the three lag factors:

$$\bar x_3=\frac{K_B}{(\tau s+1)^3}\bar x_B+
\frac{K_v}{(\tau s+1)^3}\bar v,
\quad K_v=K_qk_v=0.038416,\quad K_B=0.980000.\tag{70}$$

Here $s$ is in $\mathrm{min^{-1}}$; $K_v$ is concentration percentage points per valve-opening percentage point. The visible mode has pole $-1/5\ \mathrm{min^{-1}}$ repeated three times.

**Step 4: invert the valve step.** Hold $x_B'=0$ and apply $v'=\Delta vH(t)$. Write

$$\frac1{s(\tau s+1)^3}=
\frac1s-\frac{\tau}{\tau s+1}-\frac{\tau}{(\tau s+1)^2}-\frac{\tau}{(\tau s+1)^3}.
$$

*Reason:* multiplying by the common denominator telescopes to one. Inverting the repeated-pole terms gives

$$x_3'=K_v\Delta v\left[1-\left(1+\frac t\tau+\frac{t^2}{2\tau^2}\right)e^{-t/\tau}\right].\tag{71}$$

*Reason:* the third pole contributes the quadratic-in-time exponential term. With $\tau=5\ \mathrm{min}$, its quadratic coefficient is $t^2/50$.

The first-tank valve gain contains $100-x_s$ because each extra unit of pure-tracer inflow also drives out an extra unit of the existing mixture. Counting only the incoming tracer would overstate its effect. In a downstream tank, the baseline inlet and outlet compositions are identical, so changing flow alone creates no first-order composition forcing. It multiplies only the developing composition difference, which is why that contribution is a product of deviations.

Each tank adds one stored concentration and one lag factor. After a valve step, tank 1 begins changing first; its emerging change drives tank 2, which then drives tank 3. The polynomial multiplying the exponential in equation (71) enforces the initially gentle downstream response. A repeated pole describes several sequential memories with the same decay rate, not a single lag with its time constant multiplied by three.

## Motivation and explanation

A volume-percent change from $2$ to $3$ is one **percentage point**; it is not a $1\%$ relative increase. Using volume fractions is equally valid, but requires replacing $100$ by $1$ and rescaling concentration gains consistently.

The cascade has no exact dead time, though its initially flat response can resemble a delay. The local model freezes residence time at its baseline value and is accurate only for small flow/composition changes. A real valve may not be linear in stem position at changing pressure drop.

## Link to other topics

This example brings physical balances, local linearisation, transfer-function summation and repeated poles together. These plant-response models are the starting point for designing feedback controllers once a controller model is introduced.

## Conclusion

A consistent equilibrium and percentage convention produce a clear local model. Its two input gains and three repeated lag factors separate mixture sensitivity from the dynamics of stored liquid.
