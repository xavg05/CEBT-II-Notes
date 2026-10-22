[Previous](<RE-05 - Residence-time distributions and tanks in series.md>) · [Subject index](../README.md) · [Topic overview](README.md)

<!-- note-content:start -->
# RE-06: Mixing and conversion

## Overview

Assumed: ideal reactor balances and residence-time distributions.

Assume steady, constant-density, isothermal operation with a uniform feed. An RTD specifies how long fluid stays, but not when elements of different composition mix. For first-order kinetics that distinction does not change conversion under these assumptions; for nonlinear kinetics it can.

## Intuition

In complete segregation, fluid behaves as separate globules. Each globule is internally uniform but exchanges no material with other globules until the outlet, so it reacts as a small batch reactor. Molecular mixing instead lets fresh and partly reacted material share reactants during reaction.

For first-order consumption, averaging concentrations and then calculating rate gives the same result as averaging rates: $k\langle C\rangle=\langle kC\rangle$. For second-order consumption, $\langle C^2\rangle=\langle C\rangle^2+\operatorname{Var}(C)$. Concentration variation can therefore change the average rate even at the same average concentration.

## Derivation

**Step 1: follow a segregated globule.** Let $C_{A,\mathrm{batch}}(t)$ be its concentration after time $t$, starting from feed concentration $C_{A0}$. Constant globule volume gives $dC_{A,\mathrm{batch}}/dt=r_A$, where $r_A$ is evaluated at its own state. Its conversion is $X_{\mathrm{batch}}(t)=1-C_{A,\mathrm{batch}}(t)/C_{A0}$.

*Reason:* without interchange, only reaction changes its concentration.

**Step 2: average at the exit.** With exit-age probability density $E(t)$, the fraction arriving with ages in $[t,t+dt]$ is $E(t)dt$. The outlet concentration and overall conversion are therefore

$$
\bar C_A=\int_0^\infty C_{A,\mathrm{batch}}(t)E(t)\,dt,\qquad
\bar X_A=\int_0^\infty X_{\mathrm{batch}}(t)E(t)\,dt.
\tag{18}
$$

*Reason:* sum the contributions of all residence-time groups, weighted by their exiting fractions. The conversion expression uses common feed concentration and constant density. Variable-density systems need the appropriate molar-flow weighting.

**Step 3: first-order kinetics.** For $r_A=-kC_A$ with constant $k$, separate the batch balance: $dC_A/C_A=-k\,dt$. Integration gives $C_{A,\mathrm{batch}}/C_{A0}=e^{-kt}$. Substitution into (18) gives

$$
1-\bar X_A=\int_0^\infty e^{-kt}E(t)\,dt.
\tag{19}
$$

*Reason:* the surviving fraction is exponential in time. Linearity means molecular interchange does not change the averaged result. This also applies to pseudo-first-order kinetics only while the excess reagent and $k$ remain effectively constant. An RTD alone is insufficient if temperature histories differ between paths.

**Step 4: compare with a mixed cascade.** For one of $N$ equal ideal tanks, inlet concentration $C_{j-1}$ and outlet $C_j$ obey $Q(C_{j-1}-C_j)=kC_jV/N$, where $V$ is total cascade volume. Dividing by $Q$, setting total $\tau=V/Q$, and rearranging gives $C_j/C_{j-1}=1/(1+k\tau/N)$. Multiplying all $N$ ratios gives

$$
1-X_A=\left(1+\frac{k\tau}{N}\right)^{-N}.
\tag{20}
$$

*Reason:* the equal first-order concentration ratio repeats at every stage. Equation (19) yields the same answer using the cascade RTD: put $b=k+1/\tau_i$ and use $\int_0^\infty t^{N-1}e^{-bt}dt=(N-1)!/b^N$. That identity follows by integration by parts repeatedly, beginning with $\int_0^\infty e^{-bt}dt=1/b$.

### A network with the same RTD and different conversion

Take an isothermal, constant-density second-order reaction $-r_A=k_2C_A^2$. Place one ideal PFR and one ideal CSTR in series, each with residence time $\tau_s$, and set the dimensionless group $k_2C_{A0}\tau_s=1$. With $c=C_A/C_{A0}$, integration of the PFR balance gives $1/c_{\mathrm{out}}-1/c_{\mathrm{in}}=1$, whereas the CSTR balance gives $c_{\mathrm{in}}-c_{\mathrm{out}}=c_{\mathrm{out}}^2$. Their positive maps are

$$c_{\mathrm{PFR,out}}=\frac{c_{\mathrm{in}}}{1+c_{\mathrm{in}}},\qquad
c_{\mathrm{CSTR,out}}=\frac{-1+\sqrt{1+4c_{\mathrm{in}}}}2.$$

Starting at $c=1$, PFR then CSTR gives outlet $c\approx0.366025$ and conversion $0.633975$. Reversing their order gives outlet $c\approx0.381966$ and conversion $0.618034$. Both passive-tracer RTDs are

$$E(t)=\begin{cases}0,&0\le t<\tau_s,\\
\tau_s^{-1}e^{-(t-\tau_s)/\tau_s},&t\ge\tau_s.
\end{cases}$$

The deterministic PFR transit simply shifts the tank's exponential waiting-time distribution, regardless of order. The nonlinear concentration maps do not commute, so the same tracer RTD permits different reactive conversion. This demonstrates why an RTD alone cannot close nonlinear reaction performance.

## Motivation and explanation

For first-order consumption, each surviving molecule has the same probability per unit time of reacting at the specified temperature, independent of the concentrations around it. Mixing two groups therefore changes neither their total instantaneous consumption nor the surviving fraction associated with their residence times. A quadratic law differs because bringing concentrated and depleted material together changes the average of the squared concentration.

In the nonlinear network derived above, reversing the equipment changes the concentration presented to each reaction environment while leaving the tracer's total waiting-time distribution unchanged. The PFR retains a concentration history; the CSTR immediately shares its incoming material with its dilute contents. Their two nonlinear inlet-to-outlet maps do not commute, even though the two passive-tracer convolutions do. The different conversions therefore isolate a mixing-sequence effect under the stated constant-density, isothermal assumptions.

For $N=1$, (20) is the first-order CSTR result. As $N\rightarrow\infty$, taking logarithms gives $-N\ln(1+k\tau/N)\rightarrow-k\tau$, so the surviving fraction tends to $e^{-k\tau}$, the PFR result.

Keep the vocabulary distinct: macromixing describes bulk flow and residence-time behaviour; micromixing describes concentration mixing at molecular scales. Complete segregation is a limiting micromixing model. Maximum mixedness is another limiting model, in which mixing occurs as early as permitted by the specified RTD. A generic well-mixed network is not automatically the maximum-mixedness realisation of its RTD. Ideal CSTR and PFR balances can model a specified network, but an arbitrary RTD needs an explicit mixing closure.

## Link to other topics

Tanks-in-series models will help describe packed and trickle beds whose flow departs from plug flow. Distinguishing flow effects, molecular mixing and transport to catalytic sites prevents attributing every shortfall in conversion to a poor intrinsic rate constant.

## Conclusion

Specify both residence-time behaviour and the mixing model before predicting nonlinear conversion. These foundations prepare the analysis of reactions involving a solid reagent and, subsequently, heterogeneous catalysts.
<!-- note-content:end -->

[Previous](<RE-05 - Residence-time distributions and tanks in series.md>) · [Subject index](../README.md) · [Topic overview](README.md)
