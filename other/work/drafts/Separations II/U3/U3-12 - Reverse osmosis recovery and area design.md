# Reverse-osmosis recovery and area design

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
\frac{C_f}{C_1}=(1-S)^{-R}. \tag{1}
$$

At overall recovery $S_2$, set $C_f=C_3$ to obtain retentate concentration. The collected permeate concentration $C_2$ follows from the overall salt balance:

$$
C_1=S_2C_2+(1-S_2)C_3.
$$

Divide by $C_1$, substitute Equation (1) and solve for $C_2$:

$$
\frac{C_2}{C_1}=\frac{1-(1-S_2)^{1-R}}{S_2}. \tag{2}
$$

The numerator accounts for total salt lost into all local permeate increments. Consequently $C_2$ is generally different from the final local $C_p=(1-R)C_3$.

For local water flux $J_V(S)$, the volume crossing an area element is $dQ_p=J_VdA=Q_1dS$, so

$$
A=Q_1\int_0^{S_2}\frac{dS}{J_V(S)}. \tag{3}
$$

If the osmotic-pressure relation is linear, $\Pi=\varphi C$, and polarisation is negligible, the local osmotic difference is $\varphi(C_f-C_p)=\varphi RC_f$. Using Equation (1),

$$
J_V(S)=K_V[\Delta P-\varphi R C_1(1-S)^{-R}]. \tag{4}
$$

The bracket must remain positive throughout the required recovery range. Approaching zero downstream creates an area penalty and ultimately an unattainable finite-area target.

Constant rejection specifies the fraction of the local feed concentration appearing in each new permeate increment. It does not specify one constant permeate concentration along the whole module: the feed becomes more concentrated as water leaves. The collected permeate is therefore a flow-weighted mixture, while the final local permeate is associated only with the most concentrated end.

The area integral divides each additional permeate increment by its own local flux. Downstream osmotic opposition makes those increments more costly in area. The example's integer-module difference is a consequence of an equipment threshold lying between two close area estimates; it is not evidence that numerical refinement creates a physical operating margin.

## Motivation and explanation

For $R=1$, Equation (1) becomes $C_3/C_1=1/(1-S_2)$ and Equation (2) gives salt-free permeate. For $R=0$, neither stream concentrates or depletes salt. As $S_2\to0$, the collected permeate ratio tends to $1-R$, matching the first local increment.

With constant rejection, concentration profiles can be calculated without a flux law. Area cannot: Equation (3) still needs permeance, pressures and osmotic properties. If polarisation is significant, solve wall concentration and local flux together; constant $R$ may also cease to be adequate.

## Worked example

Produce $Q_2=100\,\mathrm{m^3\,day^{-1}}$ permeate from feed containing $C_1=35\,\mathrm{g\,L^{-1}}$ salt. Take overall recovery $S_2=0.30$, apparent rejection $R=0.995$, water permeance $K_V=0.004\,\mathrm{m^3\,m^{-2}\,h^{-1}\,bar^{-1}}$, and transmembrane pressure $\Delta P=55\,\mathrm{bar}$. Use the specified empirical osmotic relation $\Pi\,[\mathrm{bar}]=0.82c$, with $c$ the concentration value in $\mathrm{g\,L^{-1}}$. Each module offers $3\,\mathrm{m^2}$.

1. Find the feed rate from recovery: $Q_1=Q_2/S_2=333.333\,\mathrm{m^3\,day^{-1}}$, and use this rate in the differential area integral.
2. Calculate retentate concentration from Equation (1): $C_3=49.9109\,\mathrm{g\,L^{-1}}$.
3. Calculate collected permeate concentration from Equation (2): $C_2=0.207875\,\mathrm{g\,L^{-1}}$. This meets an assumed design salt target of $0.25\,\mathrm{g\,L^{-1}}$; that single salt target is not a complete drinking-water quality specification.
4. Calculate local permeate salt: $C_{p,1}=0.175000$ and $C_{p,3}=0.249555\,\mathrm{g\,L^{-1}}$.
5. Use Equation (4). The inlet and outlet net driving pressures are $26.4435$ and $14.2777\,\mathrm{bar}$, respectively.
6. For a first estimate, average these endpoint driving pressures, giving $J_{V,\mathrm{ar}}=0.0814424\,\mathrm{m\,h^{-1}}$. Divide production flow by this flux on a consistent time basis: $A_{\mathrm{ar}}=51.1609\,\mathrm{m^2}$.

The endpoint estimate needs $\lceil51.1609/3\rceil=18$ whole modules. Rounding the fractional module count to the nearest integer would fail to provide the estimated area.

Refining the same ideal model with Equation (3), using $C_f(S)$ throughout the module rather than averaging endpoint fluxes, gives $A=50.9024\,\mathrm{m^2}$. This refined ideal calculation needs $17$ modules, offering $51\,\mathrm{m^2}$. The difference is small in area but crosses an integer equipment threshold. The two counts belong to different calculation accuracies; neither includes a fouling or operational design margin.

Check the overall salt balance with the calculated $C_2$ and $C_3$ before accepting the result. Also verify positive flux downstream. A polarisation-free calculation at this concentration is an assumption that must be supported by hydrodynamic data; a dilute fibre test cannot establish it for this seawater design.

## Link to other topics

The differential balance has the same structure as gas-membrane depletion, while the driving force comes from solvent chemical potential. The increasing downstream area penalty resembles a packed-column pinch where a diminishing driving force demands more contact area.

## Conclusion

Recovery and rejection determine concentration profiles under the stated approximation, while the local net pressure determines area. Integrate the rate law before making a close integer module decision, and keep actual operating margins separate from the ideal-model result.
