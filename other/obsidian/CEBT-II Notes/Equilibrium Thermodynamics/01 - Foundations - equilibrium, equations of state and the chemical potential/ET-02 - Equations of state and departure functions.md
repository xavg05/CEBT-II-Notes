[Previous](<ET-01 - The criterion for phase equilibrium.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-03 - Partial molar properties.md>)

<!-- note-content:start -->
# Section 02: Equations of state and departure functions

## Intuition

An ideal gas is the easy reference: its properties are known exactly from $P\underline{V} = RT$ and heat-capacity data. A real fluid differs because its molecules attract one another at moderate separations and repel at short ones. At zero pressure the molecules are infinitely far apart, so every real fluid *is* an ideal gas there.

So the plan is: start at $P = 0$ (ideal), follow the real isotherm up to the pressure of interest, and add up how the real fluid's property changes compared with the ideal gas along the way. The EOS tells us $\underline{V}$ along that path, and the Maxwell relations turn $\underline{V}$ into everything else.

## Derivation

**Step 1: the EOS.** The ideal-gas law $P\underline{V} = RT$ cannot produce a liquid. The van der Waals equation,

$$\left(P + \frac{a}{\underline{V}^2}\right)\left(\underline{V} - b\right) = RT \tag{7}$$

adds two corrections: $b$, the volume excluded by finite molecular size, and $a/\underline{V}^2$, the reduction in wall pressure caused by attractions. It is cubic in $\underline{V}$. Below the critical temperature it has three roots, which is how it predicts a liquid and a vapour. Modern cubic EOS (Peng–Robinson and others) keep this structure with better-tuned $a(T)$ and $b$.

**Step 2: how $\underline{H}$ depends on pressure.** From $d\underline{H} = T\,d\underline{S} + \underline{V}\,dP$, at constant $T$:

$$\left(\frac{\partial \underline{H}}{\partial P}\right)_T = T\left(\frac{\partial \underline{S}}{\partial P}\right)_T + \underline{V}$$

**Step 3: remove the entropy.** From $d\underline{G} = -\underline{S}\,dT + \underline{V}\,dP$, equality of the mixed second derivatives gives the Maxwell relation $(\partial\underline{S}/\partial P)_T = -(\partial\underline{V}/\partial T)_P$. Hence

$$\left(\frac{\partial \underline{H}}{\partial P}\right)_T = \underline{V} - T\left(\frac{\partial \underline{V}}{\partial T}\right)_P \tag{8}$$

*Reason:* the right side contains only $P$–$\underline{V}$–$T$ quantities, which the EOS provides.

The substitution does more than remove an inconvenient symbol. An EOS measures how the fluid expands when heated at fixed pressure; the Maxwell relation turns that measurable response into the entropy change on compression. Equation (8) combines that entropy contribution with the direct $\underline{V}\,dP$ contribution to enthalpy. Their exact cancellation for an ideal gas explains why its enthalpy depends only on temperature.

For throttling, pressure and temperature change together while enthalpy stays fixed: $0=\underline{C}_P\,dT+(\partial\underline{H}/\partial P)_T\,dP$. With positive $\underline{C}_P$, a negative pressure derivative therefore makes a pressure decrease accompany a temperature decrease. This connects the sign in the departure calculation to cooling without treating the throttle itself as isothermal.

**Step 4: integrate from the ideal-gas limit.** At $P \to 0$ the fluid is ideal, so $\underline{H}(T, 0) = \underline{H}^{\mathrm{IG}}(T)$. Integrating (8) along the isotherm:

$$\underline{H}(T,P) - \underline{H}^{\mathrm{IG}}(T) = \int_{0}^{P}\left[\underline{V} - T\left(\frac{\partial \underline{V}}{\partial T}\right)_P\right]dP \tag{9}$$

For an ideal gas the integrand is $RT/P - T(R/P) = 0$, so the departure is zero, as it must be.

**Step 5: low-pressure van der Waals.** At low density, (7) expands to $\underline{V} \approx RT/P + b - a/RT$, i.e. a second virial coefficient $B = b - a/RT$. Then $T(\partial\underline{V}/\partial T)_P = RT/P + a/RT$, and the integrand of (9) is constant:

$$\underline{H} - \underline{H}^{\mathrm{IG}} \approx \left(b - \frac{2a}{RT}\right)P \tag{10}$$

## Motivation and explanation

**Reading the departure as an energy scale.** In the low-pressure van der Waals approximation, the sign and magnitude are set by $(b-2a/RT)P$. The correction vanishes with pressure; attraction lowers enthalpy while excluded volume provides the opposing term. For nitrogen at 300 K, using $a=0.1370\ \mathrm{Pa\,m^6\,mol^{-2}}$ and $b=3.87\times10^{-5}\ \mathrm{m^3\,mol^{-1}}$, this coefficient is $-7.12\times10^{-5}\ \mathrm{m^3\,mol^{-1}}$. The linear estimate therefore changes from about $-7.1\ \mathrm{J\,mol^{-1}}$ at 1 bar to $-712\ \mathrm{J\,mol^{-1}}$ at 100 bar. The latter is comparable in magnitude to roughly 24 K of ideal-gas heating with $\underline C_P=7R/2$. It is an energy-scale comparison, not a throttling temperature change. Higher-density EOS terms must be retained before trusting the 100 bar estimate. The local throttling direction is determined by $(\partial H/\partial P)_T$, rather than the sign of the accumulated departure alone.

**Sign and meaning.** In (10), attractions ($a$) lower the enthalpy below the ideal-gas value, because the molecules sit in each other's potential wells. Repulsions ($b$) raise it. At ordinary temperatures attractions win for most gases. Equation (8) is then negative, so a gas throttled at constant $H$ to lower pressure cools (the Joule–Thomson effect). The sign changes at $T = 2a/(Rb)$, the van der Waals estimate of the inversion temperature.

**Why departures, not absolutes.** Equation (9) only gives *differences* from a reference that is known separately. Ideal-gas heat capacities fix $\underline{H}^{\mathrm{IG}}(T)$; the EOS fixes the departure. Process simulators compute every property this way. The same route applied to $\underline{G}$ is what defines fugacity later in the course.

**When it fails.**
- The low-pressure form (10) is only the first term of an expansion in density.
- A cubic EOS is reasonable for non-polar fluids but poor for strongly polar or hydrogen-bonding liquids.
- For mixtures the EOS needs mixing rules for $a$ and $b$, which work for "easy" mixtures (similar molecules) but not for, say, ethanol–water.

## Link to other topics

The Gibbs-energy departure uses the ideal-gas subtraction, $\underline{G}-\underline{G}^{\mathrm{IG}}=\int_0^P[\underline{V}-RT/P]\,dP$, rather than the enthalpy integrand in (9). That is the basis of chemical potentials from an EOS and of fugacity coefficients later in the course. Mixture EOS need partial molar volumes, introduced in the next two sections.

## Summary

An EOS turns the general theory into numbers. Any property is computed as an ideal-gas value plus a departure, integrated along the isotherm from $P = 0$, where every fluid is ideal.
<!-- note-content:end -->

[Previous](<ET-01 - The criterion for phase equilibrium.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-03 - Partial molar properties.md>)
