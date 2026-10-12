# Section 02: Equations of state and departure functions

## Overview

The fundamental relation and the "minimum $G$" criterion are the whole theory, but they contain no numbers for any particular substance. An **equation of state** (EOS), $\underline{V}(T,P)$ (plus composition for a mixture), supplies them. This note shows how an EOS gives thermodynamic properties as a **departure from the ideal gas at the same temperature**. The worked example is the enthalpy departure for nitrogen from the van der Waals equation, which is the pattern every later fugacity calculation follows.

*Assumed:* the fundamental relation $dG = -S\,dT + V\,dP$ and its enthalpy form $dH = T\,dS + V\,dP$; Maxwell relations; the van der Waals and Peng–Robinson EOS from earlier years; ideal-gas enthalpy depends on $T$ only.

## Intuition

An ideal gas is the easy reference: its properties are known exactly from $P\underline{V} = RT$ and heat-capacity data. A real fluid differs because its molecules attract one another at moderate separations and repel at short ones. At zero pressure the molecules are infinitely far apart, so every real fluid *is* an ideal gas there.

So the plan is: start at $P = 0$ (ideal), follow the real isotherm up to the pressure of interest, and add up how the real fluid's property changes compared with the ideal gas along the way. The EOS tells us $\underline{V}$ along that path, and the Maxwell relations turn $\underline{V}$ into everything else.

## Derivation

**Step 1: the EOS.** The ideal-gas law $P\underline{V} = RT$ cannot produce a liquid. The van der Waals equation,

$$\left(P + \frac{a}{\underline{V}^2}\right)\left(\underline{V} - b\right) = RT \tag{1}$$

adds two corrections: $b$, the volume excluded by finite molecular size, and $a/\underline{V}^2$, the reduction in wall pressure caused by attractions. It is cubic in $\underline{V}$. Below the critical temperature it has three roots, which is how it predicts a liquid and a vapour. Modern cubic EOS (Peng–Robinson and others) keep this structure with better-tuned $a(T)$ and $b$.

**Step 2: how $\underline{H}$ depends on pressure.** From $d\underline{H} = T\,d\underline{S} + \underline{V}\,dP$, at constant $T$:

$$\left(\frac{\partial \underline{H}}{\partial P}\right)_T = T\left(\frac{\partial \underline{S}}{\partial P}\right)_T + \underline{V}$$

**Step 3: remove the entropy.** From $d\underline{G} = -\underline{S}\,dT + \underline{V}\,dP$, equality of the mixed second derivatives gives the Maxwell relation $(\partial\underline{S}/\partial P)_T = -(\partial\underline{V}/\partial T)_P$. Hence

$$\left(\frac{\partial \underline{H}}{\partial P}\right)_T = \underline{V} - T\left(\frac{\partial \underline{V}}{\partial T}\right)_P \tag{2}$$

*Reason:* the right side contains only $P$–$\underline{V}$–$T$ quantities, which the EOS provides.

**Step 4: integrate from the ideal-gas limit.** At $P \to 0$ the fluid is ideal, so $\underline{H}(T, 0) = \underline{H}^{\mathrm{IG}}(T)$. Integrating (2) along the isotherm:

$$\underline{H}(T,P) - \underline{H}^{\mathrm{IG}}(T) = \int_{0}^{P}\left[\underline{V} - T\left(\frac{\partial \underline{V}}{\partial T}\right)_P\right]dP \tag{3}$$

For an ideal gas the integrand is $RT/P - T(R/P) = 0$, so the departure is zero, as it must be.

**Step 5: low-pressure van der Waals.** At low density, (1) expands to $\underline{V} \approx RT/P + b - a/RT$, i.e. a second virial coefficient $B = b - a/RT$. Then $T(\partial\underline{V}/\partial T)_P = RT/P + a/RT$, and the integrand of (3) is constant:

$$\underline{H} - \underline{H}^{\mathrm{IG}} \approx \left(b - \frac{2a}{RT}\right)P \tag{4}$$

## Motivation and explanation

**Sign and meaning.** In (4), attractions ($a$) lower the enthalpy below the ideal-gas value, because the molecules sit in each other's potential wells. Repulsions ($b$) raise it. At ordinary temperatures attractions win for most gases. Equation (2) is then negative, so a gas throttled at constant $H$ to lower pressure cools (the Joule–Thomson effect). The sign changes at $T = 2a/(Rb)$, the van der Waals estimate of the inversion temperature.

**Why departures, not absolutes.** Equation (3) only gives *differences* from a reference that is known separately. Ideal-gas heat capacities fix $\underline{H}^{\mathrm{IG}}(T)$; the EOS fixes the departure. Process simulators compute every property this way. The same route applied to $\underline{G}$ is what defines fugacity later in the course.

**When it fails.**
- The low-pressure form (4) is only the first term of an expansion in density.
- A cubic EOS is reasonable for non-polar fluids but poor for strongly polar or hydrogen-bonding liquids.
- For mixtures the EOS needs mixing rules for $a$ and $b$, which work for "easy" mixtures (similar molecules) but not for, say, ethanol–water.

## Worked example

**Problem.** Estimate the enthalpy departure of nitrogen at 300 K and 1, 10 and 100 bar from the van der Waals EOS, with $a = 1.370$ L² bar mol⁻² $= 0.1370$ Pa m⁶ mol⁻² and $b = 0.0387$ L mol⁻¹ $= 3.87\times10^{-5}$ m³ mol⁻¹.

**Low-pressure formula (4).** $b - 2a/RT = 3.87\times10^{-5} - 2(0.1370)/(8.314\times300) = -7.11\times10^{-5}$ m³ mol⁻¹. Multiply by $P$:

| $P$ (bar) | (4) low-pressure (J mol⁻¹) | (3) integrated numerically with full vdW (J mol⁻¹) |
|---|---|---|
| 1 | −7.1 | −7.1 |
| 10 | −71.1 | −71.0 |
| 100 | −711 | −661 |

**Interpretation.** At 1–10 bar the linear formula is exact to the precision shown. At 100 bar it overestimates the departure by about 8 % (−711 against −661 J mol⁻¹), because higher-order density terms (repulsions becoming more important) start to matter. For comparison, heating nitrogen by 1 K raises its ideal-gas enthalpy by $\underline{C}_P \approx 7R/2 = 29.1$ J mol⁻¹. So at 100 bar the non-ideal correction equals about 23 K of heating, which is not negligible in a compressor or throttle energy balance. The negative sign means nitrogen at 300 K cools on throttling, since $300\ \text{K} < 2a/(Rb) = 852$ K, the van der Waals inversion temperature.

## Link to other topics

The departure integral (3), with $\underline{V}$ in place of $\underline{V} - T(\partial\underline{V}/\partial T)_P$, gives the Gibbs-energy departure. That is the basis of chemical potentials from an EOS and of fugacity coefficients later in the course. Mixture EOS need partial molar volumes, introduced in the next two sections.

## Conclusion

An EOS turns the general theory into numbers. Any property is computed as an ideal-gas value plus a departure, integrated along the isotherm from $P = 0$, where every fluid is ideal. For mixtures, though, the relevant volume is not the molar volume of the mixture but the contribution each component makes to it: the partial molar volume, which is the subject of the next section.
