[Previous](<ET-08 - Fugacity from volumetric data and the fugacity coefficient.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Section 09: fugacity of steam at 400 °C

## Intuition

At 400 °C water is above its critical temperature (373.9 °C). So the isotherm from $`P = 0`$ upward never crosses a phase boundary, and a single integral covers the whole path. This is pure water, not water under an inert gas, so the Poynting correction plays no part.

At 20 bar the molecules are far apart, and the attractions between them make only a small dent in the Gibbs energy. At 500 bar the fluid is compressed to liquid-like density, where hydrogen-bonding attractions are strong. Each molecule is held much more tightly than in an ideal gas, so its escaping tendency is far below what the pressure alone suggests.

## Derivation

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

**Water constants.** $`T_c = 647.096`$ K, $`P_c = 220.64`$ bar. The acentric factor follows from its definition, $`\omega = -\log_{10}(P^{\mathrm{SAT}}/P_c) - 1`$ at $`T/T_c = 0.7`$. Water's saturation pressure there (452.97 K) is 9.986 bar, giving $`\omega = 0.344`$. Then $`\kappa = 0.873`$ and $`\alpha(673.15\ \mathrm{K}) = 0.965`$.

## Motivation and explanation

**Resolving an integral through a dense region.** At low density $`\underline V-RT/P\to B`$, not zero. A trapezoidal integration that sets the zero-pressure endpoint to zero therefore introduces a small avoidable bias. On the 400 °C isotherm up to 20 bar, the volume departure is nearly constant, so the low-pressure endpoint correction is small and steam's fugacity remains close to its pressure.
At much higher pressure the integrand varies rapidly as the density crosses from gas-like to liquid-like. Since 400 °C is above water's critical temperature, this is a continuous supercritical crossover: no saturation plateau or latent-heat discontinuity belongs in the integral. A fine pressure grid should resolve the region of rapid density change, with convergence checked by refining the grid.
The compressibility factor $`Z`$ measures the volume error at the final state, while $`\ln\phi`$ measures an accumulated area over all lower pressures. An EOS can therefore predict fugacity well while predicting the final density less well: errors may occupy only a small part of the integral or offset one another. Agreement in equilibrium calculations does not establish equal accuracy for density-dependent equipment sizing.

**Numerical resolution on the supercritical isotherm.** The following reference-EOS molar volumes at 673.15 K provide the coarse grid discussed below. The volume entries are in $`10^{-3}\ \mathrm{m^3\,mol^{-1}}`$.

| $`P`$ (bar) | 50 | 100 | 150 | 200 | 250 | 300 | 350 | 400 | 450 | 500 |
|---|---|---|---|---|---|---|---|---|---|---|
| $`\underline V`$ | 1.042 | 0.476 | 0.282 | 0.179 | 0.108 | 0.0504 | 0.0379 | 0.0344 | 0.0325 | 0.0312 |

Using $`B\approx-0.078\times10^{-3}\ \mathrm{m^3\,mol^{-1}}`$ at zero pressure, trapezoidal integration of the departure gives about $`-5.02\ \mathrm{kJ\,mol^{-1}}`$ and $`\phi\approx0.408`$. A fine reference-EOS integration gives approximately $`\phi=0.409`$ and $`f=204.5`$ bar. The corresponding Peng-Robinson result is about $`\phi=0.421`$; its final-state $`Z=0.375`$ differs appreciably from the reference value 0.279. This comparison makes the different accuracy of local volume and accumulated Gibbs energy explicit.

**Physical reading.** At 500 bar, $`RT\ln\phi \approx -5.0`$ kJ mol⁻¹. Strong attractions in the dense fluid lower the molar Gibbs energy by about 5 kJ mol⁻¹ below the ideal-gas value. As a result, the fluid's tendency to escape (into a vapour, a solvent, or a reaction) corresponds to an ideal gas at only about 205 bar, not 500. Any phase- or reaction-equilibrium calculation that used $`P`$ in place of $`f`$ would be off by a factor of about 2.4.

**Why PR gets $`\phi`$ right but $`Z`$ wrong.** At 500 bar PR overestimates the molar volume by about a third ($`Z = 0.375`$ against 0.279). Yet it is within 3 % on $`\phi`$. Two reasons:
- $`\phi`$ is an *integral* over the whole path from $`P = 0`$, much of which lies in the gas-like region where PR is accurate.
- PR's $`\alpha(T)`$ is fitted to vapour pressures through $`\omega`$, and vapour pressures are equal-fugacity conditions. So the EOS is effectively tuned to give fugacities (Gibbs energies) right, not liquid densities.

That is why process simulators use cubic EOS for phase equilibria but often switch to other correlations for liquid densities.

**Numerical lessons.**
1. The integrand tends to the virial coefficient $`B`$, not zero, at $`P = 0`$.
2. Differencing four-figure volumes at low pressure gives a noisy integrand.
3. Where the integrand has a sharp feature, step size matters. Here, the 50 bar trapezoid from the printed table gives $`\phi \approx 0.408`$, about 0.3 % below the fine reference value. Its close agreement does not remove the need to check convergence on a finer grid.

## Link to other topics

Fugacities of compressed fluids like this enter supercritical extraction and high-pressure reactor equilibria, such as the equilibrium constant for steam reforming written in fugacities. The same PR expression, with mixing rules, gives the vapour-phase fugacity coefficients used in vapour–liquid equilibrium at high pressure.

## Summary

At 400 °C and 20 bar, steam's fugacity is 19.5 bar, close to ideal. At 500 bar it is about 205 bar, so $`\phi \approx 0.41`$, because the fluid is compressed to liquid-like density, where attractions are strong. A cubic EOS reproduces this to within a few percent. Evaluating the integral from tables needs care at both ends: the low-pressure limit, and any steep region. This completes fugacity for pure fluids.

## Conclusion

Fugacity turns "equal chemical potentials" into "equal corrected pressures". For a pure fluid it follows from volumetric data through $`RT\ln\phi = \int_0^P(\underline{V} - RT/P)\,dP`$; for a compressed liquid it is the saturation fugacity times the Poynting factor. Gas-phase non-ideality is now in hand. The next part treats the non-ideality of liquid mixtures, through the activity coefficient.
<!-- note-content:end -->

[Previous](<ET-08 - Fugacity from volumetric data and the fugacity coefficient.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)
