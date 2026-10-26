[Previous](<PDC-17 - Poles, repeated modes and stability.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<PDC-19 - Steady-state gain and the final-value theorem.md>)

<!-- note-content:start -->
# PDC-18: Zeros, direct feedthrough and inverse response

## Overview

Assumed: poles and partial-fraction responses.

Zeros reshape the forced response without creating a new exponential mode. A right-half-plane zero can make the output initially move opposite to its final direction, even when every process pole is stable.

## Intuition

Two physical pathways can compete. A fast pathway may initially push the output down while a slower but stronger pathway eventually raises it. Their sum can therefore dip before rising; the zero encodes that competition.

## Derivation

**Step 1: separate modes from their weights.** Write a strictly proper model with distinct poles as $`G(s)=\sum_j C_j/(s-p_j)`$. For each pole,


**Equation (56)**

```math
C_j=\lim_{s\to p_j}(s-p_j)G(s).
```


*Reason:* multiplying removes that term's simple singularity; all other terms vanish in the limit. Changing the numerator changes residues $`C_j`$, hence the relative amplitudes of modes, while unreduced denominator roots stay fixed unless cancellation occurs.

**Step 2: build an inverse-response example.** Add two stable first-order pathways:


**Equation (57)**

```math
G(s)=\frac4{s+1}-\frac6{s+2}
=\frac{2(1-s)}{(s+1)(s+2)}.
```


*Reason:* put the contributions over a common denominator. Poles are $`-1,-2`$ and the zero is $`+1`$. Both modes decay, but the zero is in the right half-plane. For a unit step,


**Equation (58)**

```math
\bar y=\frac{G(s)}s=\frac1s-\frac4{s+1}+\frac3{s+2},
\qquad y'=1-4e^{-t}+3e^{-2t}.
```


*Reason:* invert each partial fraction. At zero, $`y'=0`$ but $`\dot y'=4-6=-2`$; the final value is $`1`$. The initial direction opposes the final direction.

**Step 3: distinguish feedthrough from storage.** If numerator and denominator degrees are equal, long division gives $`G(s)=D_0+G_{sp}(s)`$, where $`D_0`$ is a constant and $`G_{sp}`$ is strictly proper. In the time domain, $`y'=D_0x'`$ plus the stored-state response.

*Reason:* a constant block passes an input directly and may create an immediate output jump under a step. It need not be unphysical: the reduced boiler steam-flow model has this form.

The two pathways settle to different strengths: their gains are $`4`$ and $`-3`$, so the positive contribution wins at long times. Initially, their slopes are $`4`$ and $`-6`$, so the faster negative path wins. That change of dominance explains the dip without requiring an unstable pole. The zero at $`+1`$ appears when the two pathway expressions are combined; it describes their cancellation in the transfer numerator, not an extra growing state.

Feedthrough is another distinct feature. With a finite step and strictly proper lag pathways, the state output remains continuous and only its slope changes. A nonzero direct term $`D_0`$ adds an immediate jump $`D_0\Delta x`$ on top of the stored-state response. Such a jump, a gradual inverse response, and a transport waiting time therefore have different mathematical and physical causes.

## Motivation and explanation

A right-half-plane zero does not by itself make the open-loop transfer function unstable. It constrains response shaping and makes exact stable causal inversion problematic. A numerator zero can cancel a denominator pole in a mathematical expression, but that can hide internal dynamics.

Not every stable two-pole model has the monotonic step response of the standard constant-numerator second-order model. Its zero structure and feedthrough matter too. The two-pathway model assumes linearity and no transport delay.

### Locating the reversal

For the two-pathway step model above, $`\dot y'=4e^{-t}-6e^{-2t}`$. Setting this to zero gives $`e^t=3/2`$ and a minimum at $`t=\ln(3/2)\approx0.405465\ \mathrm{s}`$, with $`y'=-1/3`$. The faster negative path initially wins: its slope is $`-6`$ against $`+4`$. The final contributions are $`-3`$ and $`+4`$, leaving $`+1`$. Initial direction and eventual gain therefore report different balances between pathways.

## Link to other topics

The final-value theorem predicts the endpoint but cannot reveal inverse response. Controller design must account for both poles and zeros when interpreting the transient.

## Conclusion

Poles set the available modes; zeros set how the input excites them. A stable process can still have an initially misleading response direction.
<!-- note-content:end -->

[Previous](<PDC-17 - Poles, repeated modes and stability.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<PDC-19 - Steady-state gain and the final-value theorem.md>)
