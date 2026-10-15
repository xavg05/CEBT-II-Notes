[Previous](<RE-S3-03 - Catalytic reactor types and staged beds.md>) · [Subject index](../README.md) · [Topic overview](README.md)

<!-- note-content:start -->
# Diesel desulfurisation and nonideal flow

## Overview

Assume isothermal, constant-density first-order reactor balances and the tanks-in-series RTD. This example shows why matching moderate conversion does not justify extrapolating a plug-flow model to very high removal.

## Intuition

At moderate removal, a small early-exiting fraction is tolerable. At very high removal it can contain most of the residual reagent. The desired product specification therefore depends on the short-residence-time tail, not just on the average time.

## Derivation

Hydrogen dissolves in diesel and reacts with a sulfur-containing compound, represented by $`\mathrm{RSH}`$:


**Equation (27)**

```math
\mathrm{H_2+RSH\longrightarrow H_2S+RH}.
```


With hydrogen effectively abundant, let $`C_A`$ denote RSH concentration and $`-r_A=k'C_A`$ the disappearance rate per bed volume. The effective constant $`k'`$ includes the particular catalyst, wetting and transport conditions. It should not be assumed invariant when flow, particle size, porosity or catalyst age changes.

For an ideal PFR at constant volumetric flow $`Q`$, the balance $`Q\,dC_A=-k'C_A\,dV`$ gives $`dC_A/C_A=-k'\,dV/Q`$. Integrating from inlet $`C_{A0}`$ to outlet and defining total space time $`\tau=V/Q`$ gives


**Equation (28)**

```math
\frac{C_A}{C_{A0}}=1-X=e^{-k'\tau}.
```


For a single element of a chain of $`N`$ equal CSTRs, inflow minus outflow equals consumption:


**Equation (29)**

```math
Q(C_{j-1}-C_j)=k'C_j\frac VN.
```


Dividing by $`QC_j`$ gives $`C_{j-1}/C_j=1+k'\tau/N`$. Multiplying the concentration ratios through the chain gives


**Equation (30)**

```math
1-X=\left(1+\frac{k'\tau}{N}\right)^{-N}.
```


There is no inlet concentration in this ratio because the kinetics are linear. As $`N`$ tends to infinity, $`N\ln(1+k'\tau/N)`$ tends to $`k'\tau`$, recovering plug flow.

The segregated-fluid calculation gives the same result for first-order reaction. With element residence time $`t`$, batch concentration is $`C_{A0}e^{-k't}`$. If each equivalent tank has mean time $`\tau_i=\tau/N`$, its chain RTD is


**Equation (31)**

```math
E(t)=\frac{t^{N-1}e^{-t/\tau_i}}{(N-1)!\tau_i^N}.
```


Averaging the remaining concentration gives


**Equation (32)**

```math
1-X=\frac1{(N-1)!\tau_i^N}\int_0^\infty t^{N-1}e^{-at}\,dt,
\qquad a=k'+\frac1{\tau_i}.
```


To evaluate this integral without hiding the algebra, define $`I_m(a)=\int_0^\infty t^m e^{-at}dt`$. Integration by parts makes the boundary term vanish and gives $`I_m=(m/a)I_{m-1}`$. Since $`I_0=1/a`$, repeated substitution gives $`I_{N-1}=(N-1)!/a^N`$. Substitution yields $`(1+k'\tau_i)^{-N}`$, exactly the CSTR-chain result. Molecular mixing does matter for nonlinear kinetics; this agreement is specific to the first-order model.

## Motivation and explanation

The outlet residual is an average of surviving fractions, not survival evaluated at the average residence time. Old elements have already lost nearly all their A and cannot compensate for A carried by young elements. As the required residual becomes small, that early-exiting population therefore matters increasingly, explaining why a mean-time plug-flow estimate can miss a stringent outlet specification.

Holding $`N`$ fixed while increasing $`\tau`$ stretches the same relative spread of waiting times. Extending the bed while increasing both $`N`$ and $`\tau`$ adds successive reaction stages and narrows the relative spread as well. These are different interventions, so their required factors need not agree. The worked results compare those model choices; choosing between them for a real bed requires knowing how the new flow conditions change wetting, dispersion and the effective kinetic constant.

Reducing liquid flow raises mean time but may worsen wetting or dispersion; increasing bed length can raise time while making the flow distribution relatively narrower. Sterically hindered sulfur compounds can have different intrinsic rates, but a discrepancy must also be tested against flow and transport before assigning it to chemistry.

## Worked example

Use $`k'=0.0552\ \mathrm{s^{-1}}`$, bed length $`L=1\ \mathrm m`$, particle diameter $`d_p=0.005\ \mathrm m`$ and diesel kinematic viscosity $`\nu=10^{-5}\ \mathrm{m^2\,s^{-1}}`$. Operating conditions are 50 bar and 350 °C. These are illustrative design data.

The plug-flow time for 90% removal is $`\ln(10)/k'=41.7135\ \mathrm s`$. With the superficial-velocity convention $`u=L/\tau`$, the particle Reynolds number $`ud_p/\nu=11.9865`$, approximately 12. In a partially wetted bed, actual liquid velocity and holdup require separate definitions; this estimate does not establish ideal flow.

For 99.9% removal the plug-flow model predicts $`\tau=125.1405\ \mathrm s`$, three times the initial model time. Set $`N=L/(20d_p)=10`$ for the illustrative trickle-bed correlation. At that time the remaining fraction is $`0.00523770`$, approximately five times the target $`0.001`$. Using the rounded $`k'\tau=6.9`$ instead gives $`0.00526178`$.

Solving the chain equation for the required total time gives


**Equation (33)**

```math
k'\tau=N\left[(1-X)^{-1/N}-1\right].
```


At $`X=0.999`$ and $`N=10`$, $`k'\tau=9.95262`$ and $`\tau=180.3011\ \mathrm s`$. This is 4.32237 times the initial **plug-flow design time**, while keeping $`N`$ and $`k'`$ fixed. It is not an independently calibrated factor relative to an observed baseline: at the initial plug-flow time the chain itself predicts a different conversion. A measured baseline should be used to fit the nonideal model before predicting a plant change.

If length is increased at constant cross-section and flow, and if $`N`$ and $`\tau`$ both scale with length by a factor $`f`$, then $`k'\tau/N`$ stays constant. Thus


**Equation (34)**

```math
1-X=\left(1+\frac{k'\tau_0}{N_0}\right)^{-fN_0},\qquad
f=\frac{-\ln(1-X)}{N_0\ln(1+k'\tau_0/N_0)}.
```


Using $`N_0=10`$ and $`\tau_0=41.7135\ \mathrm s`$ gives $`f=3.33347`$. This is a model estimate: extra length also raises pressure drop and may change wetting, so hydraulic and transport checks remain necessary.


## Link to other topics

Adsorption and diffusion explain why the apparent $`k'`$ can change with operation. The same RTD reasoning applies to other high-conversion first-order processes.

## Conclusion

High removal requires a validated flow model and a rate appropriate to the new operating conditions. Mean residence time alone is insufficient.
<!-- note-content:end -->

[Previous](<RE-S3-03 - Catalytic reactor types and staged beds.md>) · [Subject index](../README.md) · [Topic overview](README.md)
