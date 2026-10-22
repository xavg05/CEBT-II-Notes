# RE-16: Diesel desulfurisation and nonideal flow

## Overview

Assume isothermal, constant-density first-order reactor balances and the tanks-in-series RTD. This example shows why matching moderate conversion does not justify extrapolating a plug-flow model to very high removal.

## Intuition

At moderate removal, a small early-exiting fraction is tolerable. At very high removal it can contain most of the residual reagent. The desired product specification therefore depends on the short-residence-time tail, not just on the average time.

## Derivation

Hydrogen dissolves in diesel and reacts with a sulfur-containing compound, represented by $\mathrm{RSH}$:

$$\mathrm{H_2+RSH\longrightarrow H_2S+RH}.
\tag{44}$$

With hydrogen effectively abundant, let $C_A$ denote RSH concentration and $-r_A=k'C_A$ the disappearance rate per bed volume. The effective constant $k'$ includes the particular catalyst, wetting and transport conditions. It should not be assumed invariant when flow, particle size, porosity or catalyst age changes.

For an ideal PFR at constant volumetric flow $Q$, the balance $Q\,dC_A=-k'C_A\,dV$ gives $dC_A/C_A=-k'\,dV/Q$. Integrating from inlet $C_{A0}$ to outlet and defining total space time $\tau=V/Q$ gives

$$\frac{C_A}{C_{A0}}=1-X=e^{-k'\tau}.
\tag{45}$$

For a single element of a chain of $N$ equal CSTRs, inflow minus outflow equals consumption:

$$Q(C_{j-1}-C_j)=k'C_j\frac VN.
\tag{46}$$

Dividing by $QC_j$ gives $C_{j-1}/C_j=1+k'\tau/N$. Multiplying the concentration ratios through the chain gives

$$1-X=\left(1+\frac{k'\tau}{N}\right)^{-N}.
\tag{47}$$

There is no inlet concentration in this ratio because the kinetics are linear. As $N$ tends to infinity, $N\ln(1+k'\tau/N)$ tends to $k'\tau$, recovering plug flow.

The segregated-fluid calculation gives the same result for first-order reaction. With element residence time $t$, batch concentration is $C_{A0}e^{-k't}$. If each equivalent tank has mean time $\tau_i=\tau/N$, its chain RTD is

$$E(t)=\frac{t^{N-1}e^{-t/\tau_i}}{(N-1)!\tau_i^N}.
\tag{48}$$

Averaging the remaining concentration gives

$$1-X=\frac1{(N-1)!\tau_i^N}\int_0^\infty t^{N-1}e^{-at}\,dt,
\qquad a=k'+\frac1{\tau_i}.
\tag{49}$$

To evaluate this integral without hiding the algebra, define $I_m(a)=\int_0^\infty t^m e^{-at}dt$. Integration by parts makes the boundary term vanish and gives $I_m=(m/a)I_{m-1}$. Since $I_0=1/a$, repeated substitution gives $I_{N-1}=(N-1)!/a^N$. Substitution yields $(1+k'\tau_i)^{-N}$, exactly the CSTR-chain result. Molecular mixing does matter for nonlinear kinetics; this agreement is specific to the first-order model.

### Distinguishing more residence time from a longer bed

For $N$ equal tanks, rearrange the first-order surviving fraction by taking its $-1/N$ power:

$$k'\tau=N[(1-X)^{-1/N}-1].
\tag{50}$$

Increasing time at fixed $N$ and increasing bed length are different comparisons. If both $N$ and $\tau$ scale with length by a factor $f$, then $k'\tau/N$ stays fixed, and

$$1-X=\left(1+\frac{k'\tau_0}{N_0}\right)^{-fN_0},\qquad
f=\frac{-\ln(1-X)}{N_0\ln(1+k'\tau_0/N_0)}.
\tag{51}$$

Here subscript zero denotes the baseline bed. Calibrate that baseline against measured performance before predicting a plant change: a plug-flow baseline time and an uncalibrated nonideal model do not describe the same starting conversion. Extra length also increases pressure drop and may alter wetting, so the length estimate needs hydraulic and transport checks.

## Motivation and explanation

The outlet residual is an average of surviving fractions, not survival evaluated at the average residence time. Old elements have already lost nearly all their A and cannot compensate for A carried by young elements. As the required residual becomes small, that early-exiting population therefore matters increasingly, explaining why a mean-time plug-flow estimate can miss a stringent outlet specification.

Holding $N$ fixed while increasing $\tau$ stretches the same relative spread of waiting times. Extending the bed while increasing both $N$ and $\tau$ adds successive reaction stages and narrows the relative spread as well. These are different interventions, so their required factors need not agree. These expressions compare those model choices; choosing between them for a real bed requires knowing how the new flow conditions change wetting, dispersion and the effective kinetic constant.

Reducing liquid flow raises mean time but may worsen wetting or dispersion; increasing bed length can raise time while making the flow distribution relatively narrower. Sterically hindered sulfur compounds can have different intrinsic rates, but a discrepancy must also be tested against flow and transport before assigning it to chemistry.

## Link to other topics

Adsorption and diffusion explain why the apparent $k'$ can change with operation. The same RTD reasoning applies to other high-conversion first-order processes.

## Conclusion

High removal requires a validated flow model and a rate appropriate to the new operating conditions. Mean residence time alone is insufficient.
