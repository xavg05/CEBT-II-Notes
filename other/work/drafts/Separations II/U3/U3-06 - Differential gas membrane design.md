# Differential gas membrane design

## Overview

Assumed knowledge: binary local membrane transport and differential material balances.

This note derives a numerical design procedure for a gas membrane as feed flow and composition change. The calculation distinguishes newly permeated gas from all permeate collected upstream and replaces guessed averages with an area integral.

## Intuition

Each small patch removes gas of composition $y_i$, leaving a slightly smaller, less oxygen-rich retentate. Adding those small changes gives the final retentate and the mixture of gas collected as permeate. The distinction matters because downstream gas mixes with an inventory of richer gas generated earlier.

## Derivation

Assume steady, isothermal binary gas separation, constant permeances and pressures, negligible film resistance and no sweep. Feed moves in plug flow. In the asymmetric-membrane model used here, each local emerging flux remains compositionally isolated in the porous support until collection; the support has negligible hydraulic resistance. Its interface composition is therefore $y_i(x)$, given by the local binary quadratic. Let $Q_1$ be inlet reference-volume flow, $Q_p$ cumulative permeate flow and $Q$ remaining feed-side flow.

Define $S=Q_p/Q_1$. The overall flow balance gives

$$
Q=Q_1(1-S),\qquad dQ_p=Q_1\,dS. \tag{1}
$$

Let $x_1$ be inlet composition, $x$ local retentate composition and $\bar y$ composition of the collected permeate up to that position. An overall component balance gives

$$
Q_1x_1=Q_1(1-S)x+Q_1S\bar y,
$$

so cancellation and rearrangement yield

$$
\bar y=\frac{x_1-(1-S)x}{S}. \tag{2}
$$

This is defined for $S>0$; as $S\to0$, the collected composition tends to the first local flux composition.

For a differential patch, the component amount lost from retentate is the amount newly permeated:

$$
d(Qx)=-y_i\,dQ_p.
$$

Expand the derivative, substitute $Q=Q_1(1-S)$ and $dQ=-Q_1dS$, then divide by $Q_1$:

$$
(1-S)\,dx-x\,dS=-y_i\,dS.
$$

Hence

$$
\frac{dS}{1-S}=\frac{dx}{x-y_i(x)}. \tag{3}
$$

For the preferentially permeating component, $y_i>x$ and $dx<0$, so $dS>0$, as required. Integrating from inlet $(S=0,x=x_1)$ gives

$$
-\ln(1-S)=\int_{x_1}^{x}\frac{d\xi}{\xi-y_i(\xi)}. \tag{4}
$$

Here $\xi$ is only an integration variable. Evaluate the positive integral numerically, then obtain $S=1-e^{-I}$, where $I$ denotes that integral.

The component flux $J_A$ over area $dA$ transfers the same amount as $y_i\,dQ_p$. Thus

$$
J_A\,dA=Q_1y_i\,dS,
\qquad
A=Q_1\int_0^{S_2}\frac{y_i}{J_A}\,dS. \tag{5}
$$

Use a common reference-volume basis for $Q_1$ and $J_A$, or consistently use molar flow and molar flux.

The product derivative $d(Qx)=Q\,dx+x\,dQ$ retains both ways the feed-side oxygen inventory decreases: its concentration falls and the total flow carrying it shrinks. Omitting the second term would treat the membrane like a dilute absorber with constant total gas flow, although a substantial fraction of the whole gas stream is being removed.

The collected-composition balance is an inventory sum over all preceding patches, whereas the local composition controls the next transported increment under the stated support-mixing model. Keeping those roles distinct explains why the collected curve lies above the downstream local curve and why neither curve can simply replace the other in a partial-pressure law.

## Motivation and explanation

The integration procedure is:

1. Select a decreasing mesh of $x$ values from the inlet to the target retentate. This makes the known local-composition relation convenient to evaluate.
2. Solve the physical quadratic root for $y_i$ at each mesh point and verify positive component driving forces.
3. Integrate Equation (4) to each position and calculate $S$. A trapezium rule averages reciprocal denominators; evaluating the reciprocal of averaged endpoint denominators is a different, also convergent approximation.
4. Calculate $\bar y$ from Equation (2), so collected composition satisfies the overall balance.
5. Integrate Equation (5) with local fluxes, then refine the mesh until the area and recovery stop changing materially.

For a membrane directly contacting a common co-current permeate channel, use that channel's actual composition $\bar y$ in the partial-pressure driving forces. The newly transported gas then has composition $Y=N_A/(N_A+N_B)$, which generally differs from $\bar y$. Equation (3) uses $Y$ in that model and must be solved together with the collected-permeate balance. The closed local quadratic $y_i(x)$ alone no longer supplies the whole solution.

## Link to other topics

Changing flow and composition must be tracked together in both membrane and packed-column design. Liquid reverse-osmosis balances use the same differential structure but require solvent flux, concentration polarisation and osmotic pressure in place of gas enrichment alone.

## Conclusion

A consistent differential design calculates recovery, collected composition and area together. Its validity depends as much on the permeate mixing model as on the numerical integration.
