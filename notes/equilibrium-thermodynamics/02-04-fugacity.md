# Fugacity — reading 02.4

[Previous](02-03-fugacity.md) · [Subject index](README.md) · [Next](03-01-activity-coefficients-and-excess-gibbs-energy.md)

<!-- reading-content:start -->
## Section 09: Worked example, fugacity of steam at 400 °C

### Intuition

At 400 °C water is above its critical temperature (373.9 °C). So the isotherm from $`P = 0`$ upward never crosses a phase boundary, and a single integral covers the whole path. This is pure water, not water under an inert gas, so the Poynting correction plays no part.

At 20 bar the molecules are far apart, and the attractions between them make only a small dent in the Gibbs energy. At 500 bar the fluid is compressed to liquid-like density, where hydrogen-bonding attractions are strong. Each molecule is held much more tightly than in an ideal gas, so its escaping tendency is far below what the pressure alone suggests.

### Derivation

**Method.**
1. Tabulate $`\underline{V}`$ at 673.15 K over $`0 \le P \le P_{\mathrm{final}}`$.
2. Form the integrand $`\underline{V} - RT/P`$.
3. Extrapolate it to $`P = 0`$. It tends to the second virial coefficient $`B`$, not to zero, because $`\underline{V} = RT/P + B + O(P)`$.
4. Integrate numerically (trapezoidal rule), then $`\phi = \exp(I/RT)`$ and $`f = \phi P`$, where $`I`$ is the integral.

**Why the integrand is delicate.** At low $`P`$, $`\underline{V}`$ and $`RT/P`$ are both large and nearly equal, and the integrand is their small difference. Volumes given to four significant figures leave the difference uncertain by several percent. For example, at 2 bar, $`\underline{V} = 27.89\times10^{-3}`$ m³ mol⁻¹ known to $`\pm0.005\times10^{-3}`$, while the difference itself is only about $`0.08\times10^{-3}`$. Errors from step size and from rounding dominate the result. They are not physics.

**Peng–Robinson route.** Substituting the PR equation into the $`Z`$-form integral, changing variable from $`P`$ to $`\underline{V}`$ and integrating analytically gives a standard closed form. The algebra is long and is not reproduced here:


**Equation (51)**

```math
\ln\phi = Z - 1 - \ln(Z - B^{*}) - \frac{A^{*}}{2\sqrt{2}\,B^{*}}\ln\frac{Z + (1+\sqrt2)B^{*}}{Z + (1-\sqrt2)B^{*}}
```


with

```math
A^{*} = \frac{a\alpha P}{(RT)^2}, \qquad B^{*} = \frac{bP}{RT}, \qquad a = 0.45724\frac{R^2T_c^2}{P_c}, \qquad b = 0.07780\frac{RT_c}{P_c},
```


```math
\alpha = \left[1+\kappa\left(1-\sqrt{T/T_c}\right)\right]^2, \qquad \kappa = 0.37464 + 1.54226\,\omega - 0.26992\,\omega^2.
```


Here $`Z`$ is the largest real root of the PR cubic, $`A^{*}`$ and $`B^{*}`$ are the dimensionless PR parameters (not the virial $`B`$), and $`\omega`$ is the acentric factor. The idea is the same as Section 08: the attraction term ($`a`$) lowers $`\phi`$ through the last term, and the repulsion term ($`b`$) raises it through $`-\ln(Z - B^{*})`$. Evaluating the integral numerically with PR volumes gives the same $`\phi`$ as (51) to four figures, which confirms the formula.

**Water constants.** $`T_c = 647.096`$ K, $`P_c = 220.64`$ bar. The acentric factor follows from its definition, $`\omega = -\log_{10}(P^{\mathrm{SAT}}/P_c) - 1`$ at $`T/T_c = 0.7`$. Water's saturation pressure there (452.97 K) is 9.986 bar, giving $`\omega = 0.344`$. Then $`\kappa = 0.874`$ and $`\alpha(673.15\ \mathrm{K}) = 0.965`$.

### Worked example

**(a) 400 °C, 20 bar, from steam-table volumes.** Units: $`10^{-3}`$ m³ mol⁻¹.

| $`P`$ (bar) | 0 | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $`\underline{V}`$ | ∞ | 27.89 | 13.91 | 9.247 | 6.917 | 5.519 | 4.586 | 3.920 | 3.421 | 3.032 | 2.722 |
| $`\underline{V} - RT/P`$ | → $`B`$ | −0.09 | −0.08 | −0.081 | −0.079 | −0.078 | −0.078 | −0.078 | −0.077 | −0.077 | −0.076 |

The integrand is almost constant, as the virial picture predicts ($`\underline{V} - RT/P \approx B`$ at low density). Applying the trapezoidal rule with 2 bar steps:
- taking the integrand as 0 at $`P = 0`$ gives $`I = -151`$ J mol⁻¹;
- taking its physical limit, $`B \approx -0.078\times10^{-3}`$ m³ mol⁻¹, gives $`I = -159`$ J mol⁻¹.

With $`RT = 5597`$ J mol⁻¹, these give $`\phi = 0.973`$ and $`0.972`$. So **$`f \approx 19.4`$–$`19.5`$ bar**.

| Method, 20 bar | $`\phi`$ | $`f`$ (bar) |
|---|---|---|
| Steam-table trapezoid | 0.973 | 19.5 |
| IAPWS-95 reference equation (integrated finely) | 0.974 | 19.5 |
| Peng–Robinson, eq. (51) | 0.970 | 19.4 |

All three agree within 0.4 %. At 20 bar, steam at 400 °C is close to ideal: its Gibbs energy is only about 150 J mol⁻¹ below the ideal-gas value.

**(b) 400 °C, 500 bar.** The same method needs volumes up to 500 bar. Values below are from the IAPWS-95 formulation, in $`10^{-3}`$ m³ mol⁻¹:

| $`P`$ (bar) | 50 | 100 | 150 | 200 | 250 | 300 | 350 | 400 | 450 | 500 |
|---|---|---|---|---|---|---|---|---|---|---|
| $`\underline{V}`$ | 1.042 | 0.476 | 0.282 | 0.179 | 0.108 | 0.0504 | 0.0379 | 0.0344 | 0.0325 | 0.0312 |
| $`\underline{V} - RT/P`$ | −0.077 | −0.083 | −0.091 | −0.101 | −0.116 | −0.136 | −0.122 | −0.106 | −0.092 | −0.081 |

The integrand is no longer constant. It dips sharply between 250 and 350 bar, where the volume collapses from gas-like to liquid-like values (the dense, near-critical region). The integral is dominated by this region.
- Trapezoidal rule with 50 bar steps: $`I = -5153`$ J mol⁻¹, so $`\phi = 0.398`$.
- Integrating finely (0.125 bar steps): $`I = -5004`$ J mol⁻¹, so $`\phi = 0.409`$, $`f = 204.5`$ bar. This matches the Gibbs-energy difference computed directly from IAPWS-95, $`\phi = 0.4091`$.

| Method, 500 bar | $`\phi`$ | $`f`$ (bar) | $`Z`$ |
|---|---|---|---|
| Coarse trapezoid (50 bar steps) | 0.398 | 199 | — |
| IAPWS-95 (fine integration) | 0.409 | 204.5 | 0.279 |
| Peng–Robinson, eq. (51) | 0.421 | 210.5 | 0.375 |

### Motivation and explanation

**Physical reading.** At 500 bar, $`RT\ln\phi \approx -5.0`$ kJ mol⁻¹. Strong attractions in the dense fluid lower the molar Gibbs energy by about 5 kJ mol⁻¹ below the ideal-gas value. As a result, the fluid's tendency to escape (into a vapour, a solvent, or a reaction) corresponds to an ideal gas at only about 205 bar, not 500. Any phase- or reaction-equilibrium calculation that used $`P`$ in place of $`f`$ would be off by a factor of about 2.4.

**Why PR gets $`\phi`$ right but $`Z`$ wrong.** At 500 bar PR overestimates the molar volume by about a third ($`Z = 0.375`$ against 0.279). Yet it is within 3 % on $`\phi`$. Two reasons:
- $`\phi`$ is an *integral* over the whole path from $`P = 0`$, much of which lies in the gas-like region where PR is accurate.
- PR's $`\alpha(T)`$ is fitted to vapour pressures through $`\omega`$, and vapour pressures are equal-fugacity conditions. So the EOS is effectively tuned to give fugacities (Gibbs energies) right, not liquid densities.

That is why process simulators use cubic EOS for phase equilibria but often switch to other correlations for liquid densities.

**Numerical lessons.**
1. The integrand tends to the virial coefficient $`B`$, not zero, at $`P = 0`$.
2. Differencing four-figure volumes at low pressure gives a noisy integrand.
3. Where the integrand has a sharp feature, step size matters. Here, coarse 50 bar steps under-predict $`\phi`$ by about 3 %.

### Link to other topics

Fugacities of compressed fluids like this enter supercritical extraction and high-pressure reactor equilibria, such as the equilibrium constant for steam reforming written in fugacities. The same PR expression, with mixing rules, gives the vapour-phase fugacity coefficients used in vapour–liquid equilibrium at high pressure.

### Summary

At 400 °C and 20 bar, steam's fugacity is 19.5 bar, close to ideal. At 500 bar it is about 205 bar, so $`\phi \approx 0.41`$, because the fluid is compressed to liquid-like density, where attractions are strong. A cubic EOS reproduces this to within a few percent. Evaluating the integral from tables needs care at both ends: the low-pressure limit, and any steep region. This completes fugacity for pure fluids.

## Conclusion

Fugacity turns "equal chemical potentials" into "equal corrected pressures". For a pure fluid it follows from volumetric data through $`RT\ln\phi = \int_0^P(\underline{V} - RT/P)\,dP`$; for a compressed liquid it is the saturation fugacity times the Poynting factor. Gas-phase non-ideality is now in hand. The next part treats the non-ideality of liquid mixtures, through the activity coefficient.
<!-- reading-content:end -->

[Previous](02-03-fugacity.md) · [Subject index](README.md) · [Next](03-01-activity-coefficients-and-excess-gibbs-energy.md)
