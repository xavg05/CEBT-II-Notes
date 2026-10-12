# PDC-18: Zeros, direct feedthrough and inverse response

## Overview

Assumed: poles and partial-fraction responses.

Zeros reshape the forced response without creating a new exponential mode. A right-half-plane zero can make the output initially move opposite to its final direction, even when every process pole is stable.

## Intuition

Two physical pathways can compete. A fast pathway may initially push the output down while a slower but stronger pathway eventually raises it. Their sum can therefore dip before rising; the zero encodes that competition.

## Derivation

**Step 1: separate modes from their weights.** Write a strictly proper model with distinct poles as $G(s)=\sum_j C_j/(s-p_j)$. For each pole,

$$C_j=\lim_{s\to p_j}(s-p_j)G(s).\tag{56}$$

*Reason:* multiplying removes that term's simple singularity; all other terms vanish in the limit. Changing the numerator changes residues $C_j$, hence the relative amplitudes of modes, while unreduced denominator roots stay fixed unless cancellation occurs.

**Step 2: build an inverse-response example.** Add two stable first-order pathways:

$$G(s)=\frac4{s+1}-\frac6{s+2}
=\frac{2(1-s)}{(s+1)(s+2)}.\tag{57}$$

*Reason:* put the contributions over a common denominator. Poles are $-1,-2$ and the zero is $+1$. Both modes decay, but the zero is in the right half-plane. For a unit step,

$$\bar y=\frac{G(s)}s=\frac1s-\frac4{s+1}+\frac3{s+2},
\qquad y'=1-4e^{-t}+3e^{-2t}.\tag{58}$$

*Reason:* invert each partial fraction. At zero, $y'=0$ but $\dot y'=4-6=-2$; the final value is $1$. The initial direction opposes the final direction.

**Step 3: distinguish feedthrough from storage.** If numerator and denominator degrees are equal, long division gives $G(s)=D_0+G_{sp}(s)$, where $D_0$ is a constant and $G_{sp}$ is strictly proper. In the time domain, $y'=D_0x'$ plus the stored-state response.

*Reason:* a constant block passes an input directly and may create an immediate output jump under a step. It need not be unphysical: the reduced boiler steam-flow model has this form.

## Motivation and explanation

A right-half-plane zero does not by itself make the open-loop transfer function unstable. It constrains response shaping and makes exact stable causal inversion problematic. A numerator zero can cancel a denominator pole in a mathematical expression, but that can hide internal dynamics.

Not every stable two-pole model has the monotonic step response of the standard constant-numerator second-order model. Its zero structure and feedthrough matter too. The example assumes linearity and no transport delay.

## Worked example

For the two-pathway model, solve $\dot y'=4e^{-t}-6e^{-2t}=0$. This gives the minimum at $t=\ln(3/2)=0.405465$ s, where $y'=-1/3=-0.333333$. The response eventually approaches $+1$.

Physically, the negative pathway has the faster pole $-2$ and initially contributes slope $-6$; the positive pathway contributes slope $+4$. Their final step contributions are $-3$ and $+4$, leaving a positive total.

## Link to other topics

The final-value theorem predicts the endpoint but cannot reveal inverse response. Controller design must account for both poles and zeros when interpreting the transient.

## Conclusion

Poles set the available modes; zeros set how the input excites them. A stable process can still have an initially misleading response direction.
