[Previous](<SEP-26 - Binary gas membrane selectivity.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-28 - Differential gas membrane design.md>)

<!-- note-content:start -->
# SEP-27: Estimating gas membrane area

## Overview

Assumed knowledge: binary gas membrane fluxes and overall material balances.

An initial gas-membrane area estimate uses inlet and outlet fluxes and a representative permeate composition. This note works through an air-separation example and explains why the chosen average matters when the driving force changes substantially.

## Intuition

As oxygen preferentially leaves air, its feed-side concentration decreases. The last part of the membrane transfers oxygen more slowly than the first. Dividing the required oxygen flow by the inlet flux would assign the entire area the performance of its best section and therefore undersize the device.

The gas newly crossing a downstream patch is also less oxygen-rich than gas crossing upstream. The final collected permeate is a flow-weighted mixture of all those local contributions, not simply the outlet local composition.

## Derivation

Let $Q_1$, $Q_2$, $Q_3$ denote inlet feed, collected permeate and retentate flows, all reported at the **same reference pressure and temperature**. Let $x_1$, $x_3$ be feed and retentate oxygen fractions and $\bar y_2$ the collected permeate oxygen fraction. Assume steady binary ideal-gas operation and no sweep.

The total balance gives $Q_3=Q_1-Q_2$. Substituting into the oxygen balance gives

$$
Q_1x_1=Q_2\bar y_2+(Q_1-Q_2)x_3.
$$

Divide by $Q_1$ and define $S=Q_2/Q_1$:

$$
x_1=x_3+S(\bar y_2-x_3),\qquad
S=\frac{x_1-x_3}{\bar y_2-x_3}. \tag{114}
$$

For membrane oxygen permeance $K_{m,A}$ on a reference-volume basis, the local oxygen flux is

$$
J_A=K_{m,A}P_f(x-\gamma y_i),\qquad \gamma=P_p/P_f. \tag{115}
$$

$J_A$ has units $\mathrm{Nm^3\,m^{-2}\,s^{-1}}$ when $K_{m,A}$ has units $\mathrm{Nm^3\,m^{-2}\,s^{-1}\,bar^{-1}}$ and pressures are in bar. Here $\mathrm{Nm^3}$ denotes the explicitly stated reference conditions, not an unqualified universal convention.

The integrated oxygen flow is $Q_2\bar y_2=\int_AJ_A\,dA$. Replacing the variable flux with an assumed average $\langle J_A\rangle$ gives

$$
A\approx\frac{Q_2\bar y_2}{\langle J_A\rangle}. \tag{116}
$$

Two possible endpoint averages are

$$
J_{\mathrm{ar}}=\frac{J_{A,1}+J_{A,3}}2,\qquad
J_{\mathrm{lm}}=\frac{J_{A,1}-J_{A,3}}{\ln(J_{A,1}/J_{A,3})}. \tag{117}
$$

Both tend to the common flux when their two endpoints approach equality. Neither is automatically the correct average for a membrane whose flow and composition both vary.

There are two averages to establish, with different weights. Collected permeate composition is weighted by how much gas each patch produces. The area calculation is weighted by how much area is needed to transfer each increment at its local flux. Replacing both by endpoint arithmetic means imposes two separate approximations, so correcting the flux average alone cannot make the whole calculation exact.

The reference-volume convention allows the total-flow and oxygen-flow balances to share the same amount basis. Compression changes the operating volume of that gas, but not its number of moles. Using actual volumes from opposite pressure sides without conversion would violate the very component balance used to estimate stage cut.

## Motivation and explanation

The arithmetic mean of endpoint local permeate fractions approximates the final collected composition. It is exact only under restrictive weighting conditions: for example, if equal increments of permeate have a composition that varies linearly from the first to the last. Constant flux alone does not establish that linearity.

A logarithmic mean is exact in some simple exchanger and mass-transfer problems because the relevant driving force follows a particular differential balance. Membrane selectivity introduces a nonlinear local composition relation, so importing that mean by analogy gives an estimate rather than a derivation.

A modest endpoint flux ratio can justify a rough arithmetic estimate, but a ratio below two is a practical screening rule rather than an error bound. Refine the differential calculation when the area estimate controls equipment selection.

## Worked example

Separate a binary approximation to air with $x_1=0.209$ to a retentate with $x_3=0.05$. Take $Q_1=1\,\mathrm{Nm^3\,s^{-1}}$, referenced here to $1\,\mathrm{bar(a)}$ and $25^\circ\mathrm C$; $\alpha=5$; $P_f=10\,\mathrm{bar(a)}$; $P_p=1\,\mathrm{bar(a)}$; and $K_{m,A}=1.7\times10^{-5}\,\mathrm{Nm^3\,m^{-2}\,s^{-1}\,bar^{-1}}$. Assume constant permeances and pressures, no film resistance, and compositionally isolated emerging permeate at the selective layer before collection.

1. Solve the local composition quadratic at both ends. This gives $y_{i,1}=0.514753$ and $y_{i,3}=0.162883$.
2. Approximate the collected composition by their arithmetic mean, $\bar y_2\approx0.338818$.
3. Apply Equation (114), obtaining $S\approx0.550520$ and $Q_2\approx0.550520\,\mathrm{Nm^3\,s^{-1}}$.
4. Evaluate Equation (115): $J_{A,1}=2.67792\times10^{-5}$ and $J_{A,3}=5.73099\times10^{-6}\,\mathrm{Nm^3\,m^{-2}\,s^{-1}}$.
5. Compute the endpoint means and divide the required oxygen flow by each, using Equations (3)–(4).

The results are

| Average | Oxygen flux, $\mathrm{Nm^3\,m^{-2}\,s^{-1}}$ | Estimated area, $\mathrm{m^2}$ |
|---|---:|---:|
| Arithmetic | $1.62551\times10^{-5}$ | $11\,475$ |
| Logarithmic | $1.36523\times10^{-5}$ | $13\,663$ |

The inlet flux is $4.673$ times the outlet flux. This substantial variation makes the difference between the estimates meaningful and motivates integrating the membrane balances. Both estimates also inherit the approximation for $\bar y_2$.

## Link to other topics

The area integral is analogous to the transfer-unit approach in absorption: a local rate law must be integrated as the driving force changes. Gas-membrane design adds changing total flow and a permeate composition determined by selective transport.

## Conclusion

An endpoint calculation provides a useful first area estimate. The large variation in oxygen flux here requires a differential calculation to obtain consistent recovery, collected composition and area.
<!-- note-content:end -->

[Previous](<SEP-26 - Binary gas membrane selectivity.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-28 - Differential gas membrane design.md>)
