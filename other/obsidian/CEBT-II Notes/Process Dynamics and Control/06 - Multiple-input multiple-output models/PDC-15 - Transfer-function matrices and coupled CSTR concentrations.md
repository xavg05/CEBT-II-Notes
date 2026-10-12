[Previous](<../05 - Combining process elements/PDC-14 - Summing contributions and duplicating signals.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<PDC-16 - Boiler mass–energy balance and integrating inventory.md>)

<!-- note-content:start -->
# PDC-15: Transfer-function matrices and coupled CSTR concentrations

## Overview

Assumed: constant-volume, isothermal CSTR balances for $A\rightarrow B$.

A MIMO model is a matrix of input–output responses. The reacting CSTR shows how an input can affect its own species directly and another species through a reaction pathway.

## Intuition

More A in the feed raises reactor A and therefore makes more B. More B in the feed raises B without creating A because the reaction is irreversible. The matrix should express this directional coupling, not artificially give every input the same effect.

## Derivation

**Step 1: define the matrix convention.** With $n$ input deviations and $m$ output deviations,

$$\bar{\boldsymbol y}=\boldsymbol G(s)\bar{\boldsymbol x},\qquad
\bar y_i=\sum_{j=1}^nG_{ij}(s)\bar x_j.\tag{47}$$

*Reason:* output row $i$ sums the contributions from input columns $j$. Define each $G_{ij}$ with all other input deviations and initial state deviations zero. Each entry has units of its row's output divided by its column's input.

**Step 2: balance both components.** Let $V$ be volume, $q$ equal inlet/outlet flow, $\tau=V/q$, $k>0$ first-order rate constant, $c_{A0},c_{B0}$ feed concentrations and $c_A,c_B$ tank concentrations. Assume constant density, one mole B formed per mole A consumed, no volume change and perfect mixing:

$$\tau\dot c_A+(1+k\tau)c_A=c_{A0},\qquad
\tau\dot c_B+c_B=c_{B0}+k\tau c_A.\tag{48}$$

*Reason:* A reaction loss is an equal B reaction source. Subtract the steady balances and transform:

$$\bar c_A=\frac{\bar c_{A0}}{\tau s+1+k\tau},\qquad
\bar c_B=\frac{\bar c_{B0}}{\tau s+1}+
\frac{k\tau\bar c_{A0}}{(\tau s+1)(\tau s+1+k\tau)}.
$$

*Reason:* solve the A equation first, then substitute it into the B equation. This produces

$$\begin{bmatrix}\bar c_A\\\bar c_B\end{bmatrix}
=\begin{bmatrix}
\dfrac1{\tau s+1+k\tau}&0\\
\dfrac{k\tau}{(\tau s+1)(\tau s+1+k\tau)}&\dfrac1{\tau s+1}
\end{bmatrix}
\begin{bmatrix}\bar c_{A0}\\\bar c_{B0}\end{bmatrix}.\tag{49}$$

**Step 3: check the conserved total.** Add the two ODEs:

$$\tau\frac{d(c_A+c_B)}{dt}+(c_A+c_B)=c_{A0}+c_{B0}.\tag{50}$$

*Reason:* reaction cancels in the total concentration balance. Equivalently, the A-feed column sums to $1/(\tau s+1)$, because

$$\frac1{\tau s+1+k\tau}+\frac{k\tau}{(\tau s+1)(\tau s+1+k\tau)}=\frac1{\tau s+1}.
$$

## Motivation and explanation

The two dynamic modes have poles $-(1+k\tau)/\tau$ and $-1/\tau$. The B response to feed A contains both modes: A first changes, then its changed conversion supplies B. The A response to feed B is zero under the stated irreversible, uncoupled chemistry.

This is a MIMO concentration model. The heated tank with two inputs but only one temperature output is MISO, a single-output special case. If temperature affects $k$, or multiple reactions occur, the zero entry and pole structure can change.

## Worked example

Take $\tau=100$ s and $k=0.0100$ s$^{-1}$. A unit step in $c_{A0}$ with no $c_{B0}$ change gives

$$c_A'=\tfrac12(1-e^{-2t/100}),\qquad
c_B'=\tfrac12-e^{-t/100}+\tfrac12e^{-2t/100}.
$$

These follow by taking the A response and subtracting it from total response $1-e^{-t/100}$. At $100$ s, $c_A'=0.432332$ and $c_B'=0.199788$ in the concentration unit used for the input. Final deviations are $0.500$ each. Their sum tracks an inert-tank concentration response at every time.

## Link to other topics

Material conservation is a strong check on a coupled model. The boiler matrix will combine two different balances and include an integrating inventory output.

## Conclusion

Rows identify outputs and columns identify inputs. Coupling entries should follow actual pathways, and conserved combinations provide independent verification.
<!-- note-content:end -->

[Previous](<../05 - Combining process elements/PDC-14 - Summing contributions and duplicating signals.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<PDC-16 - Boiler mass–energy balance and integrating inventory.md>)
