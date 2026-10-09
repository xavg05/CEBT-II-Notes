# Foundations: equilibrium, equations of state and the chemical potential — reading 01.3

[Previous](01-02-foundations.md) · [Subject index](README.md) · [Next](02-01-fugacity.md)

<!-- reading-content:start -->
## Section 04: Chemical potential and the Gibbs–Duhem equation

### Intuition

Section 03 showed that partial molar volumes are shares of a total and that the shares depend on the environment. If one component's share grows as the composition changes, the other's must shrink to keep the books balanced. The Gibbs–Duhem equation states this exactly.

For the Gibbs energy it has a sharp physical meaning. In a binary at fixed $`T`$ and $`P`$, you cannot raise the escaping tendency of both components at once by changing the composition. Whatever makes component 1 "happier" in the mixture must make component 2 less so, in proportion to how much of each is present.

*Analogy: a seesaw with the fulcrum at the composition.* The mole fractions are the lever arms. A small change in $`\mu_1`$ on the long arm must be balanced by a larger change in $`\mu_2`$ on the short arm. The analogy breaks down because a seesaw balances forces at one instant, while Gibbs–Duhem is a relation between *changes*, $`d\mu_i`$, along a path of compositions. It says nothing about the absolute values of $`\mu_i`$.

### Derivation

**Step 1: chemical potential as a partial molar property.** By definition


```math
\mu_i = \left(\frac{\partial G}{\partial n_i}\right)_{T,P,n_{j\neq i}} \equiv \bar G_i \tag{14}
```


so Euler's theorem (Section 03, applied to $`G`$ at fixed $`T`$, $`P`$) gives


```math
G = \sum_i n_i\,\mu_i, \qquad \underline{G} = \sum_i x_i\,\mu_i \tag{15}
```


**Step 2: differentiate (15).** By the product rule, for any change:


```math
dG = \sum_i n_i\,d\mu_i + \sum_i \mu_i\,dn_i
```


**Step 3: compare with the fundamental relation.** For an open phase, $`dG = -S\,dT + V\,dP + \sum_i\mu_i\,dn_i`$. Subtracting from Step 2, the $`\mu_i\,dn_i`$ terms cancel:


```math
\sum_i n_i\,d\mu_i = -S\,dT + V\,dP \tag{16}
```


**Step 4: constant $`T`$ and $`P`$.**


```math
\sum_i n_i\,d\mu_i = 0 \qquad\Longleftrightarrow\qquad \sum_i x_i\,d\mu_i = 0 \qquad (\text{constant } T, P) \tag{17}
```


This is the Gibbs–Duhem equation. Dividing by $`n`$ gives the mole-fraction form.

**Step 5: the same holds for any partial molar property.** Repeat Steps 2–4 with $`V`$. Since $`(\partial V/\partial n_i)`$ already defines $`\bar V_i`$, and at constant $`T`$, $`P`$ we have $`dV = \sum\bar V_i\,dn_i`$:


```math
\sum_i x_i\,d\bar V_i = 0 \qquad (\text{constant } T, P) \tag{18}
```


**Step 6: binary form.** With $`x_2 = 1 - x_1`$, divide (18) by $`dx_1`$:


```math
x_1\,\frac{d\bar V_1}{dx_1} + x_2\,\frac{d\bar V_2}{dx_1} = 0 \tag{19}
```


The two slopes have opposite signs, and their magnitudes are in the inverse ratio of the mole fractions.

### Motivation and explanation

**Why it matters.** Equation (15) says the mixture Gibbs energy is fully determined by the chemical potentials. So the whole problem of phase equilibrium reduces to finding the $`\mu_i`$. Equation (17) says those $`\mu_i`$ are not independent.
- In a binary, measuring or modelling one component's $`\mu`$ against composition gives the other's by integration.
- Experimental data for both components can be checked for consistency with (17); data that violate it contain errors.
- Any model for $`\mu_i`$ must satisfy it. Later sections build models from a single function, the excess Gibbs energy, precisely so that this is automatic.

**Reading the graph in Section 03.** In dilute ethanol ($`x_{\mathrm{EtOH}}`$ small), (19) says water's partial molar volume barely changes, because its slope is multiplied by the small $`x_{\mathrm{EtOH}}/x_{\mathrm{H_2O}}`$. Meanwhile ethanol's changes steeply. Both features are visible on the curves near $`x_{\mathrm{EtOH}} = 0`$: water's curve is flat and ethanol's is steep.

**What is held constant.** Equations (17)–(19) require constant $`T`$ and $`P`$. If $`T`$ or $`P`$ vary, the full form (16) applies.

### Worked example

**Problem.** Use a one-parameter model for the ethanol (1)–water (2) partial molar volumes,

```math
\bar V_1 = \underline{V}_1 + A\,x_2^2, \qquad \bar V_2 = \underline{V}_2 + A\,x_1^2,
```

with $`\underline{V}_1 = 58`$ and $`\underline{V}_2 = 18`$ cm³ mol⁻¹. (a) Show that it obeys Gibbs–Duhem. (b) Fit $`A`$ to $`\bar V_1 \approx 54.7`$ cm³ mol⁻¹ at $`x_1 = 0.17`$, predict $`\bar V_2`$ there, and compare with the graph value of ≈17.8 cm³ mol⁻¹. (c) Test the model at the two ends of the composition range.

**(a) Consistency.** $`d\bar V_1/dx_1 = -2Ax_2`$ and $`d\bar V_2/dx_1 = 2Ax_1`$. Substitute into (19):

```math
x_1(-2Ax_2) + x_2(2Ax_1) = 0
```

so it is satisfied at every composition. This model corresponds to an excess volume $`\underline{V}^E = Ax_1x_2`$, i.e. $`\underline{V} = x_1\underline{V}_1 + x_2\underline{V}_2 + Ax_1x_2`$. Differentiating that, as in Section 03, returns the expressions above.

**(b) Fit and predict.** $`A = (54.7 - 58)/0.83^2 = -4.79`$ cm³ mol⁻¹. Then

```math
\bar V_2 = 18 + (-4.79)(0.17)^2 = 17.86\ \text{cm}^3\,\text{mol}^{-1},
```

against ≈17.8 read from the graph. Gibbs–Duhem has predicted water's partial molar volume from ethanol's alone. As a cross-check, the model's excess volume at $`x_1 = 0.17`$ is $`Ax_1x_2 = -0.68`$ cm³ mol⁻¹. For the 29.08 mol in the whiskey bottle that is a contraction of 19.7 cm³, close to the 21 cm³ found in Section 03.

**(c) Limits.**

| Quantity | Model | Graph |
|---|---|---|
| Ethanol at infinite dilution in water, $`\underline{V}_1 + A`$ | 53.2 | ≈52.6 |
| Water at infinite dilution in ethanol, $`\underline{V}_2 + A`$ | 13.2 | ≈14.3 |

A single symmetric parameter cannot reproduce both ends, because the real curves are asymmetric. A two-parameter (asymmetric) model would fix this. The same issue, and the same remedy, comes up with activity-coefficient models.

### Link to other topics

The binary Gibbs–Duhem equation applied to $`\mu_i = \mu_i^{\mathrm{ideal}} + RT\ln\gamma_i`$ becomes $`x_1\,d\ln\gamma_1 + x_2\,d\ln\gamma_2 = 0`$. That is the constraint behind the Margules and van Laar models and behind consistency tests of vapour–liquid equilibrium data. Equation (16) with the composition terms removed is also the basis of the Gibbs phase rule, which counts how many intensive variables are free.

### Summary

The chemical potential is the partial molar Gibbs energy. The mixture's Gibbs energy is the mole-fraction-weighted sum of the chemical potentials, and at fixed $`T`$ and $`P`$ their changes are tied together by Gibbs–Duhem. In a binary, knowing one gives the other, as the ethanol–water volumes show.

## Section 05: Calculating the chemical potential

*Notation:* $`P^{\circ}`$ is a reference pressure. $`\underline{G}_i^{\circ}(T)`$ is the molar Gibbs energy of pure $`i`$ **as an ideal gas** at $`T`$ and $`P^{\circ}`$. $`\underline{G}_i(T,P)`$ is that of real pure $`i`$ at $`T`$, $`P`$ in the phase of interest. $`x_i`$ is the mole fraction in whichever phase is being described.

### Intuition

For an ideal gas the only thing that changes $`\mu`$ is how crowded the molecules are, i.e. the pressure, entering through $`RT\ln P`$. In a mixture of ideal gases the molecules ignore each other, so each component behaves as if it were alone at its own partial pressure. Mixing then only adds entropy, through the $`RT\ln x_i`$ term.

An **ideal mixture** of liquids takes that entropy term and nothing else: the molecules are assumed to interact with each other exactly as they do with their own kind. So mixing changes neither volume nor enthalpy. Any real deviation, such as the 3 % contraction of whiskey, means unlike molecules interact differently, and $`\mu_i`$ needs a correction.

### Derivation

**Step 1: pure ideal gas.** At constant $`T`$, $`d\underline{G} = \underline{V}\,dP = (RT/P)\,dP`$. Integrating from $`P^{\circ}`$:


```math
\mu_i = \underline{G}_i = \underline{G}_i^{\circ}(T) + RT\ln\frac{P}{P^{\circ}} \tag{20}
```


**Step 2: ideal-gas mixture.** Ideal-gas molecules do not interact, so component $`i`$ has the same $`\mu_i`$ as if it occupied the volume alone at its partial pressure $`P_i = x_iP`$:


```math
\mu_i = \underline{G}_i^{\circ}(T) + RT\ln\frac{x_iP}{P^{\circ}} = \underline{G}_i^{\mathrm{IG}}(T,P) + RT\ln x_i \tag{21}
```


where $`\underline{G}_i^{\mathrm{IG}}(T,P)`$ is pure ideal-gas $`i`$ at the mixture's $`T`$ and $`P`$, from (20). Summing with $`\underline{G} = \sum x_i\mu_i`$:


```math
\underline{G} = \sum_i x_i\,\underline{G}_i^{\mathrm{IG}}(T,P) + RT\sum_i x_i\ln x_i \tag{22}
```


The second term is the Gibbs energy of mixing. It is always negative because every $`x_i < 1`$, and it does not depend on $`P`$.

**Step 3: ideal mixture (definition).** Define an ideal mixture (IM) as any mixture, liquid or gas, whose *mixing* behaviour copies (21) and (22), but with **real pure-component** Gibbs energies:


```math
\mu_i^{\mathrm{IM}} = \underline{G}_i(T,P) + RT\ln x_i, \qquad \underline{G}^{\mathrm{IM}} = \sum_i x_i\underline{G}_i + RT\sum_i x_i\ln x_i \tag{23}
```


**Step 4: consequences for volume (cross-derivative).** The partial molar volume follows from $`\mu_i`$ through mixed second derivatives of $`G`$:


```math
\left(\frac{\partial\mu_i}{\partial P}\right)_{T,n} = \frac{\partial}{\partial P}\left(\frac{\partial G}{\partial n_i}\right) = \frac{\partial}{\partial n_i}\left(\frac{\partial G}{\partial P}\right) = \left(\frac{\partial V}{\partial n_i}\right)_{T,P,n_{j\neq i}} = \bar V_i \tag{24}
```


*Reason:* the order of differentiation does not matter for a smooth function, and $`(\partial G/\partial P)_{T,n} = V`$.

Apply (24) to (23). At fixed composition, $`RT\ln x_i`$ does not depend on $`P`$, so $`\bar V_i^{\mathrm{IM}} = (\partial\underline{G}_i/\partial P)_T = \underline{V}_i`$. An ideal mixture therefore has **no volume change on mixing**. In the same way, the Gibbs–Helmholtz relation gives $`\bar H_i^{\mathrm{IM}} = \underline{H}_i`$, so there is no heat of mixing either.

**Step 5: real pure substance from an EOS.** Integrate $`d\underline{G}_i = \underline{V}_i\,dP`$ along the real isotherm:


```math
\mu_i = \underline{G}_i(T,P) = \underline{G}_i(T,P^{\circ}) + \int_{P^{\circ}}^{P}\underline{V}_i\,dP \tag{25}
```


This still needs $`\underline{G}_i(T,P^{\circ})`$ for the *real* fluid. To tie it to the tabulated ideal-gas value, extend the integral down to $`P\to 0`$, where the fluid becomes ideal (Step 7).

**Step 6: real mixture from an EOS.** Integrate (24) along the isotherm at fixed composition:


```math
\mu_i(T,P) = \mu_i(T,P^{\ast}) + \int_{P^{\ast}}^{P}\bar V_i\,dP \tag{26}
```


Here $`\bar V_i`$ comes from a mixture EOS as a function of $`T`$, $`P`$ and composition.

**Step 7: anchor at zero pressure (the real-fluid correction).** Write (26) for the real mixture, and the same equation for the ideal-gas mixture of the same composition, for which $`\bar V_i = RT/P`$. Subtract the two. As $`P^{\ast}\to 0`$ the real mixture becomes an ideal-gas mixture, so $`\mu_i - \mu_i^{\mathrm{IG}}\to 0`$ at the lower limit. Then add (21):


```math
\mu_i(T,P) = \underline{G}_i^{\circ}(T) + RT\ln\frac{x_iP}{P^{\circ}} + \int_{0}^{P}\left(\bar V_i - \frac{RT}{P}\right)dP \tag{27}
```


The first two terms are the ideal-gas-mixture value. The integral is the real-fluid correction. It is finite because $`\bar V_i - RT/P`$ stays bounded as $`P\to 0`$.

### Motivation and explanation

**Why $`RT\ln x_i`$ survives at zero pressure.** Taking the real mixture down to $`P = 0`$ removes the *interactions*, but it does not unmix the components. The $`RT\ln x_i`$ term in (27) is the ideal entropy of mixing, which is present even for ideal gases. Section 02's pure-fluid departures had no such term. Forgetting it is a common error.

**Limiting cases.**
- (27) with $`\bar V_i = RT/P`$: the integral vanishes and (21) is recovered.
- (23) with $`x_i = 1`$: $`\mu_i = \underline{G}_i`$, the pure-component value.
- (21) and (23) as $`x_i\to 0`$: $`\mu_i\to-\infty`$. This is the logarithmic behaviour that later motivates working with fugacity instead of $`\mu`$.

**When each approach fails.**
- Equation (27) is exact, but only as good as the mixture EOS that supplies $`\bar V_i`$. Cubic EOS with simple mixing rules work for "easy" mixtures: gases, homologous series (e.g. alkanes) and isomers.
- They fail for liquid mixtures of chemically different molecules (polar, hydrogen-bonding or associating), where the EOS cannot capture the specific interactions.
- The ideal mixture (23) fails whenever unlike interactions differ from like ones. Real liquid mixtures are therefore handled by writing $`\mu_i = \mu_i^{\mathrm{IM}} + `$ (a correction), the activity-coefficient approach developed later.

### Worked example

**Problem.** (a) Find the ideal Gibbs energy of mixing for the whiskey of Sections 03–04 ($`x_{\mathrm{EtOH}} = 0.17`$, 29.08 mol in total) at 20 °C. (b) Use Step 4 to test whether ethanol–water is an ideal mixture.

**(a) Ideal Gibbs energy of mixing.** From (23), per mole of mixture:


```math
\Delta\underline{G}_{\mathrm{mix}}^{\mathrm{IM}} = RT\left[x_1\ln x_1 + x_2\ln x_2\right] = 8.314\times293.15\times\left[0.17\ln0.17 + 0.83\ln0.83\right] = -1111\ \text{J mol}^{-1}
```


For the 29.08 mol in the bottle, that is −32.3 kJ. Mixing is strongly spontaneous even with no energetic preference at all, purely from entropy.

**(b) Ideality test.** If the mixture were ideal, Step 4 says $`\bar V_i = \underline{V}_i`$, so the bottle's contents would occupy $`\sum n_i\underline{V}_i = 721`$ cm³. They actually occupy 700 cm³, so the volume of mixing is −21 cm³ in total, or −0.73 cm³ per mole of mixture. Since $`\Delta\underline{V}_{\mathrm{mix}} \neq 0`$, the partial molar volumes differ from the pure ones. By (24), $`\mu_i`$ must then have a pressure-dependent part beyond (23). **Ethanol–water is not an ideal mixture.** Its real Gibbs energy of mixing differs from −1111 J mol⁻¹, and finding by how much is the job of activity-coefficient models.

### Link to other topics

The correction integral in (27) reappears as the fugacity coefficient: dividing by $`RT`$, the integral is $`\ln\bar\phi_i`$, which turns the chemical potential into a "corrected partial pressure". The ideal mixture (23), combined with an ideal-gas vapour, gives Raoult's law, and deviations from it are measured by activity coefficients.

### Summary

The chemical potential follows from (20) for a pure ideal gas, (21) for an ideal-gas mixture and (23) for an ideal mixture. Real fluids add the correction integral of (27), which needs partial molar volumes from a mixture EOS. That works only for simple mixtures, so the course next recasts $`\mu`$ in a more convenient variable, fugacity, starting with the simplest real case: a pure liquid under an inert gas.

## Conclusion

Phase equilibrium reduces to computing chemical potentials. They are partial molar Gibbs energies, they sum to the mixture Gibbs energy, and Gibbs–Duhem ties their changes together. For ideal gases and ideal mixtures they have simple logarithmic forms; for real fluids an equation of state adds a correction integral that only works for simple mixtures. The next part recasts $`\mu`$ as a corrected pressure, the fugacity, which is the convenient variable for every equilibrium calculation that follows.
<!-- reading-content:end -->

[Previous](01-02-foundations.md) · [Subject index](README.md) · [Next](02-01-fugacity.md)
