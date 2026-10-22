[Previous](<ET-04 - Chemical potential and the Gibbs–Duhem equation.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Section 05: Calculating the chemical potential

*Notation:* $`P^{\circ}`$ is a reference pressure. $`\underline{G}_i^{\circ}(T)`$ is the molar Gibbs energy of pure $`i`$ **as an ideal gas** at $`T`$ and $`P^{\circ}`$. $`\underline{G}_i(T,P)`$ is that of real pure $`i`$ at $`T`$, $`P`$ in the phase of interest. $`x_i`$ is the mole fraction in whichever phase is being described.

## Intuition

For an ideal gas the only thing that changes $`\mu`$ is how crowded the molecules are, i.e. the pressure, entering through $`RT\ln P`$. In a mixture of ideal gases the molecules ignore each other, so each component behaves as if it were alone at its own partial pressure. Mixing then only adds entropy, through the $`RT\ln x_i`$ term.

An **ideal mixture** of liquids takes that entropy term and nothing else: the molecules are assumed to interact with each other exactly as they do with their own kind. So mixing changes neither volume nor enthalpy. Any real deviation, such as the 3 % contraction of whiskey, means unlike molecules interact differently, and $`\mu_i`$ needs a correction.

## Derivation

**Step 1: pure ideal gas.** At constant $`T`$, $`d\underline{G} = \underline{V}\,dP = (RT/P)\,dP`$. Integrating from $`P^{\circ}`$:


**Equation (20)**

```math
\mu_i = \underline{G}_i = \underline{G}_i^{\circ}(T) + RT\ln\frac{P}{P^{\circ}}
```


**Step 2: ideal-gas mixture.** Ideal-gas molecules do not interact, so component $`i`$ has the same $`\mu_i`$ as if it occupied the volume alone at its partial pressure $`P_i = x_iP`$:


**Equation (21)**

```math
\mu_i = \underline{G}_i^{\circ}(T) + RT\ln\frac{x_iP}{P^{\circ}} = \underline{G}_i^{\mathrm{IG}}(T,P) + RT\ln x_i
```


where $`\underline{G}_i^{\mathrm{IG}}(T,P)`$ is pure ideal-gas $`i`$ at the mixture's $`T`$ and $`P`$, from (20). Summing with $`\underline{G} = \sum x_i\mu_i`$:


**Equation (22)**

```math
\underline{G} = \sum_i x_i\,\underline{G}_i^{\mathrm{IG}}(T,P) + RT\sum_i x_i\ln x_i
```


The second term is the Gibbs energy of mixing. It is always negative because every $`x_i < 1`$, and it does not depend on $`P`$.

**Step 3: ideal mixture (definition).** Define an ideal mixture (IM) as any mixture, liquid or gas, whose *mixing* behaviour copies (21) and (22), but with **real pure-component** Gibbs energies:


**Equation (23)**

```math
\mu_i^{\mathrm{IM}} = \underline{G}_i(T,P) + RT\ln x_i, \qquad \underline{G}^{\mathrm{IM}} = \sum_i x_i\underline{G}_i + RT\sum_i x_i\ln x_i
```


**Step 4: consequences for volume (cross-derivative).** The partial molar volume follows from $`\mu_i`$ through mixed second derivatives of $`G`$:


**Equation (24)**

```math
\left(\frac{\partial\mu_i}{\partial P}\right)_{T,n} = \frac{\partial}{\partial P}\left(\frac{\partial G}{\partial n_i}\right) = \frac{\partial}{\partial n_i}\left(\frac{\partial G}{\partial P}\right) = \left(\frac{\partial V}{\partial n_i}\right)_{T,P,n_{j\neq i}} = \bar V_i
```


*Reason:* the order of differentiation does not matter for a smooth function, and $`(\partial G/\partial P)_{T,n} = V`$.

Apply (24) to (23). At fixed composition, $`RT\ln x_i`$ does not depend on $`P`$, so $`\bar V_i^{\mathrm{IM}} = (\partial\underline{G}_i/\partial P)_T = \underline{V}_i`$. An ideal mixture therefore has **no volume change on mixing**. In the same way, the Gibbs–Helmholtz relation gives $`\bar H_i^{\mathrm{IM}} = \underline{H}_i`$, so there is no heat of mixing either.

**Step 5: real pure substance from an EOS.** Integrate $`d\underline{G}_i = \underline{V}_i\,dP`$ along the real isotherm:


**Equation (25)**

```math
\mu_i = \underline{G}_i(T,P) = \underline{G}_i(T,P^{\circ}) + \int_{P^{\circ}}^{P}\underline{V}_i\,dP
```


This still needs $`\underline{G}_i(T,P^{\circ})`$ for the *real* fluid. To tie it to the tabulated ideal-gas value, extend the integral down to $`P\to 0`$, where the fluid becomes ideal (Step 7).

**Step 6: real mixture from an EOS.** Integrate (24) along the isotherm at fixed composition:


**Equation (26)**

```math
\mu_i(T,P) = \mu_i(T,P^{\ast}) + \int_{P^{\ast}}^{P}\bar V_i\,dP
```


Here $`\bar V_i`$ comes from a mixture EOS as a function of $`T`$, $`P`$ and composition.

**Step 7: anchor at zero pressure (the real-fluid correction).** Write (26) for the real mixture, and the same equation for the ideal-gas mixture of the same composition, for which $`\bar V_i = RT/P`$. Subtract the two. As $`P^{\ast}\to 0`$ the real mixture becomes an ideal-gas mixture, so $`\mu_i - \mu_i^{\mathrm{IG}}\to 0`$ at the lower limit. Then add (21):


**Equation (27)**

```math
\mu_i(T,P) = \underline{G}_i^{\circ}(T) + RT\ln\frac{x_iP}{P^{\circ}} + \int_{0}^{P}\left(\bar V_i - \frac{RT}{P}\right)dP
```


The first two terms are the ideal-gas-mixture value. The integral is the real-fluid correction. It is finite because $`\bar V_i - RT/P`$ stays bounded as $`P\to 0`$.

The subtraction is made between two fluids at the same temperature, pressure and composition. It removes only the effect of intermolecular interactions, leaving the entropy of mixing in the ideal reference. Holding composition fixed along the integration path matters: otherwise $`\mu_i`$ would change because both pressure and the molecular environment were changing, and the pressure integral alone would miss part of that change.

In the bottle example, volume contraction tests the *pressure derivative* of the chemical-potential model. It establishes non-ideality, but it does not determine the whole Gibbs-energy correction at one pressure. A function's slope cannot fix its value without a reference; activity measurements supply the additional information.

## Motivation and explanation

**Separating entropy of mixing from non-ideality.** For the ethanol–water composition $`x_1=0.17`$ at 293.15 K, the ideal expression gives

```math
\Delta\underline G_{\mathrm{mix}}^{\mathrm{IM}}=RT[0.17\ln0.17+0.83\ln0.83]\approx-1111\ \mathrm{J\,mol^{-1}}.
```

For 29.08 mol this is approximately $`-32.3\ \mathrm{kJ}`$. The ideal reference already favours mixing through entropy; favourable unlike-molecule interactions are not required for this sign. The observed volume contraction independently shows that a pressure-independent ideal-mixture correction is inadequate: $`(\partial\mu_i^{ex}/\partial P)_{T,x}=\bar V_i-\underline V_i`$. It establishes a pressure-dependent excess contribution, rather than fixing its value at the measurement pressure.

**Why $`RT\ln x_i`$ survives at zero pressure.** Taking the real mixture down to $`P = 0`$ removes the *interactions*, but it does not unmix the components. The $`RT\ln x_i`$ term in (27) is the ideal entropy of mixing, which is present even for ideal gases. Section 02's pure-fluid departures had no such term. Forgetting it is a common error.

**Limiting cases.**
- (27) with $`\bar V_i = RT/P`$: the integral vanishes and (21) is recovered.
- (23) with $`x_i = 1`$: $`\mu_i = \underline{G}_i`$, the pure-component value.
- (21) and (23) as $`x_i\to 0`$: $`\mu_i\to-\infty`$. This is the logarithmic behaviour that later motivates working with fugacity instead of $`\mu`$.

**When each approach fails.**
- Equation (27) is exact, but only as good as the mixture EOS that supplies $`\bar V_i`$. Cubic EOS with simple mixing rules work for "easy" mixtures: gases, homologous series (e.g. alkanes) and isomers.
- They fail for liquid mixtures of chemically different molecules (polar, hydrogen-bonding or associating), where the EOS cannot capture the specific interactions.
- The ideal mixture (23) fails whenever unlike interactions differ from like ones. Real liquid mixtures are therefore handled by writing $`\mu_i = \mu_i^{\mathrm{IM}} + `$ (a correction), the activity-coefficient approach developed later.

## Link to other topics

The correction integral in (27) reappears as the fugacity coefficient: dividing by $`RT`$, the integral is $`\ln\bar\phi_i`$, which turns the chemical potential into a "corrected partial pressure". The ideal mixture (23), combined with an ideal-gas vapour, gives Raoult's law, and deviations from it are measured by activity coefficients.

## Summary

The chemical potential follows from (20) for a pure ideal gas, (21) for an ideal-gas mixture and (23) for an ideal mixture. Real fluids add the correction integral of (27), which needs partial molar volumes from a mixture EOS. That works only for simple mixtures, so the course next recasts $`\mu`$ in a more convenient variable, fugacity, starting with the simplest real case: a pure liquid under an inert gas.

## Conclusion

Phase equilibrium reduces to computing chemical potentials. They are partial molar Gibbs energies, they sum to the mixture Gibbs energy, and Gibbs–Duhem ties their changes together. For ideal gases and ideal mixtures they have simple logarithmic forms; for real fluids an equation of state adds a correction integral that only works for simple mixtures. The next part recasts $`\mu`$ as a corrected pressure, the fugacity, which is the convenient variable for every equilibrium calculation that follows.
<!-- note-content:end -->

[Previous](<ET-04 - Chemical potential and the Gibbs–Duhem equation.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)
