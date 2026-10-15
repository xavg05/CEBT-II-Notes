[Previous](<PDC-13 - Series blocks and the pipe–two-tank response.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<../06 - Multiple-input multiple-output models/PDC-15 - Transfer-function matrices and coupled CSTR concentrations.md>)

<!-- note-content:start -->
# PDC-14: Summing contributions and duplicating signals

## Overview

Assumed: superposition in linear deviation models.

Series elements multiply; independent contributions to the same output add with their signs. A signal branch copies information and does not divide its value like a material-flow splitter.

## Intuition

In a heated tank, warmer feed and extra heater power both affect temperature. Each input passes through its own response path, then the temperature contributions combine. Measuring that temperature does not consume part of it.

## Derivation

**Step 1: begin with the balance.** For fixed $`V,q,\rho,c_p`$, no heat loss or reaction, set $`\tau=V/q`$ and $`C_f=\rho qc_p`$, the flowing heat-capacity rate. The tank deviation equation is


**Equation (45)**

```math
\tau\dot T'+T'=T_0'+Q'/C_f.
```


*Reason:* subtract the steady energy balance so the two forcing contributions remain. Transform with zero initial deviation:


**Equation (46)**

```math
\bar T=G_1\bar T_0+G_2\bar Q,\qquad
G_1=\frac1{\tau s+1},\quad G_2=\frac1{C_f(\tau s+1)}.
```


*Reason:* both sources feed the same state, but the heater input must first be converted from power to temperature-equivalent forcing.

**Step 2: apply a signed summing junction.** A junction labelled $`+`$ on one path and $`-`$ on another forms $`\bar y=\bar y_1-\bar y_2`$. If both paths start with the same input $`\bar x`$, their equivalent block is $`G_1-G_2`$; two positive paths give $`G_1+G_2`$.

*Reason:* superposition is addition of output effects, including their signs. Signals summed at a junction must have compatible units; raw temperature and power cannot be added.

**Step 3: duplicate a signal.** If one ideal branch sends $`\bar T`$ onward and another to a sensor, both pre-sensor branches equal $`\bar T`$. The measured signal is $`\bar T_m=G_m\bar T`$, where $`G_m`$ is the sensor transfer function.

*Reason:* a branch copies a numerical variable. It is not a material balance and does not halve temperature. Sensor dynamics or loading, if relevant, must be represented separately.

It is legitimate to sum the two temperature contributions because each is already expressed in output-temperature units. The factor $`1/C_f`$ converts heating power into the feed-temperature change with the same thermal effect. Then the common lag applies to their sum. A block diagram is bookkeeping for these equations: a line is a signal, a summing point adds signed effects, and a branch sends the same value to more than one destination.

Exact dynamic compensation requires the paths to cancel as functions of $`s`$, not merely at $`s=0`$. If the heater has an extra actuator lag, its final temperature contribution can still cancel the cold feed while its early contribution is too slow. That produces a temporary temperature drop even when the eventual temperature error is zero.

## Motivation and explanation

Superposition holds for the linear model at fixed coefficients. If flow changes, the heater gain and time constant change too; products such as $`q'T'`$ require linearisation before this simple summation is justified.

For an ideal measurement scale, $`G_m(0)=1`$, but a sensor may still lag. Treating the measured output as instantly equal to the true output hides a pole in the feedback path.

## Worked example

For water with $`C_f=42000`$ W K$`^{-1}`$ and $`\tau=100`$ s, let the feed temperature fall by $`5.00`$ K while heating rises by $`210000`$ W. Their step contributions sum to


```math
T'(t)=\left[-5.00+\frac{210000}{42000}\right](1-e^{-t/100})=0.
```


The exact cancellation follows because both paths share the same tank lag in this model and the commands occur together. An actuator lag in the heat path, a delayed disturbance measurement, or inaccurate $`C_f`$ produces a transient error even when the steady effects cancel.

## Link to other topics

Feedforward exploits signed summation to oppose disturbance effects. Transfer-function matrices organise the same idea when several inputs affect several outputs.

## Conclusion

Write the signal equations before simplifying a block diagram. Their units, signs and branch meanings prevent most combination errors.
<!-- note-content:end -->

[Previous](<PDC-13 - Series blocks and the pipe–two-tank response.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<../06 - Multiple-input multiple-output models/PDC-15 - Transfer-function matrices and coupled CSTR concentrations.md>)
