[Previous](<SEP-33 - Continuous membrane plants and fouling.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<../04 - Adsorption and chromatography/SEP-35 - Adsorbents, affinity and cyclic operation.md>)

<!-- note-content:start -->
# SEP-34: Reverse-osmosis recovery and area design

## Overview

Assumed knowledge: differential liquid balances and osmotic-pressure-corrected solvent flux.

A reverse-osmosis module concentrates salt along its feed side, reducing its water flux downstream. This note derives retentate and collected permeate concentrations under constant apparent rejection, then sizes a seawater example and separates an endpoint estimate from a refined area calculation.

## Intuition

Removing water leaves progressively more salt per unit liquid volume. High rejection makes the permeate dilute but also makes the remaining feed more concentrated, increasing osmotic opposition. Overall recovery therefore affects both product quality and area requirement.

## Derivation

Assume steady dilute incompressible liquid flow, approximately additive volumes, no sweep and constant apparent local rejection $R=1-C_p/C_f$. For area sizing also assume negligible concentration polarisation, constant temperature, hydraulic permeance and transmembrane pressure. These are design approximations to check, not consequences of high rejection.

Let $Q_1,C_1$ denote inlet flow and salt concentration, $S=Q_p/Q_1$ cumulative permeate recovery, and $Q=Q_1(1-S)$ remaining feed flow. A differential salt balance is

$$
d(QC_f)=-C_p\,dQ_p.
$$

Expand and substitute $dQ=-Q_1dS$, $dQ_p=Q_1dS$, then divide by $Q_1$:

$$
(1-S)dC_f-C_f\,dS=-C_p\,dS.
$$

Rearranging and using $C_f-C_p=RC_f$ gives

$$
\frac{dC_f}{C_f}=R\frac{dS}{1-S}.
$$

Integrate from $C_f=C_1,S=0$ to the local position:

$$
\ln(C_f/C_1)=-R\ln(1-S),
\qquad
\frac{C_f}{C_1}=(1-S)^{-R}. \tag{147}
$$

At overall recovery $S_2$, set $C_f=C_3$ to obtain retentate concentration. The collected permeate concentration $C_2$ follows from the overall salt balance:

$$
C_1=S_2C_2+(1-S_2)C_3.
$$

Divide by $C_1$, substitute Equation (147) and solve for $C_2$:

$$
\frac{C_2}{C_1}=\frac{1-(1-S_2)^{1-R}}{S_2}. \tag{148}
$$

The numerator accounts for total salt lost into all local permeate increments. Consequently $C_2$ is generally different from the final local $C_p=(1-R)C_3$.

For local water flux $J_V(S)$, the volume crossing an area element is $dQ_p=J_VdA=Q_1dS$, so

$$
A=Q_1\int_0^{S_2}\frac{dS}{J_V(S)}. \tag{149}
$$

If the osmotic-pressure relation is linear, $\Pi=\varphi C$, and polarisation is negligible, the local osmotic difference is $\varphi(C_f-C_p)=\varphi RC_f$. Using Equation (147),

$$
J_V(S)=K_V[\Delta P-\varphi R C_1(1-S)^{-R}]. \tag{150}
$$

The bracket must remain positive throughout the required recovery range. Approaching zero downstream creates an area penalty and ultimately an unattainable finite-area target.

Constant rejection specifies the fraction of the local feed concentration appearing in each new permeate increment. It does not specify one constant permeate concentration along the whole module: the feed becomes more concentrated as water leaves. The collected permeate is therefore a flow-weighted mixture, while the final local permeate is associated only with the most concentrated end.

The area integral divides each additional permeate increment by its own local flux. Downstream osmotic opposition makes those increments more costly in area. The example's integer-module difference is a consequence of an equipment threshold lying between two close area estimates; it is not evidence that numerical refinement creates a physical operating margin.

## Motivation and explanation

For $R=1$, Equation (147) becomes $C_3/C_1=1/(1-S_2)$ and Equation (148) gives salt-free permeate. For $R=0$, neither stream concentrates or depletes salt. As $S_2\to0$, the collected permeate ratio tends to $1-R$, matching the first local increment.

With constant rejection, concentration profiles can be calculated without a flux law. Area cannot: Equation (149) still needs permeance, pressures and osmotic properties. If polarisation is significant, solve wall concentration and local flux together; constant $R$ may also cease to be adequate.

## Link to other topics

The differential balance has the same structure as gas-membrane depletion, while the driving force comes from solvent chemical potential. The increasing downstream area penalty resembles a packed-column pinch where a diminishing driving force demands more contact area.

## Conclusion

Recovery and rejection determine concentration profiles under the stated approximation, while the local net pressure determines area. Integrate the rate law before making a close integer module decision, and keep actual operating margins separate from the ideal-model result.
<!-- note-content:end -->

[Previous](<SEP-33 - Continuous membrane plants and fouling.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<../04 - Adsorption and chromatography/SEP-35 - Adsorbents, affinity and cyclic operation.md>)
