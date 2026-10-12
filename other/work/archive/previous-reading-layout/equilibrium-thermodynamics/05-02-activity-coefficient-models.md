# Activity-coefficient models — reading 05.2

[Previous](<../../../../../notes/Equilibrium Thermodynamics/05 - Activity-coefficient models/Complete section.md>) · [Subject index](<../../../../../notes/Equilibrium Thermodynamics/README.md>) · [Next](<../../../../../notes/Equilibrium Thermodynamics/05 - Activity-coefficient models/Complete section.md>)

<!-- reading-content:start -->
## Section 18: Flory–Huggins theory for size-asymmetric mixtures

*Notation:* solvent 1, polymer 2. $`m = \underline{V}_2/\underline{V}_1`$ is the number of lattice sites (solvent-sized segments) per chain. Volume fractions: $`\phi_1 = x_1/(x_1 + mx_2)`$, $`\phi_2 = mx_2/(x_1 + mx_2)`$.

### Intuition

Picture a lattice in which each site holds one solvent molecule or one chain segment. A dissolved polymer of $`m`$ segments occupies $`m`$ connected sites. There are far fewer ways to place one connected chain than $`m`$ separate small molecules, so the entropy gained on mixing is much smaller per segment than for small molecules. It is, however, much larger *per mole of polymer* than the ideal $`-R\ln x`$ suggests, because each polymer molecule spreads over many sites.

The volume fraction is the natural "how much space does it fill" variable, and entropy comes out as $`\ln\phi`$ instead of $`\ln x`$. *The lattice picture breaks down* for real chains, which are flexible and can cluster in dilute solution. The mean-field assumption that segments are spread uniformly then fails.

### Derivation

**Step 1: entropy of mixing (lattice counting result).**


**Equation (95)**

```math
\Delta\underline{S}^{\mathrm{mix}} = -R\left(x_1\ln\phi_1 + x_2\ln\phi_2\right)
```


This reduces to the ideal $`-R\sum x_i\ln x_i`$ when $`m = 1`$, since then $`\phi_i = x_i`$.

**Step 2: enthalpy of mixing.** Random contacts between solvent and segments, as in Margules, but counted per lattice site. There are $`(x_1 + mx_2)`$ sites per mole of molecules:


**Equation (96)**

```math
\Delta\underline{H}^{\mathrm{mix}} = \underline{H}^{ex} = \chi RT\,(x_1 + mx_2)\,\phi_1\phi_2
```


Here $`\chi`$ is the dimensionless interaction energy per contact, in units of $`RT`$. It can be estimated as $`\chi \approx \underline{V}_1(\delta_1 - \delta_2)^2/RT`$, as in RST.

**Step 3: excess Gibbs energy.** Subtract the ideal mixing terms from $`\Delta\underline{G}^{\mathrm{mix}} = \Delta\underline{H}^{\mathrm{mix}} - T\Delta\underline{S}^{\mathrm{mix}}`$:


**Equation (97)**

```math
\frac{\underline{G}^{ex}}{RT} = \underbrace{x_1\ln\frac{\phi_1}{x_1} + x_2\ln\frac{\phi_2}{x_2}}_{-\underline{S}^{ex}/R} + \underbrace{\chi(x_1 + mx_2)\phi_1\phi_2}_{\underline{H}^{ex}/RT}
```


Unlike RST, $`\underline{S}^{ex}\neq 0`$ whenever $`m\neq 1`$. The energetic term has the one-constant Margules structure, written in volume fractions.

**Step 4: solvent activity.** Differentiate $`n\Delta\underline{G}^{\mathrm{mix}}/RT = n_1\ln\phi_1 + n_2\ln\phi_2 + \chi n_1\phi_2`$ with respect to $`n_1`$:


**Equation (98)**

```math
\ln a_1 = \ln(\gamma_1x_1) = \ln\phi_1 + \left(1 - \frac{1}{m}\right)\phi_2 + \chi\phi_2^2
```


This is the quantity measured by vapour-pressure lowering, freezing point or osmotic pressure of polymer solutions.

**Step 5: when does the solution split?** Per lattice site, $`\Delta G^{\mathrm{mix}}/RT = (1-\phi)\ln(1-\phi) + (\phi/m)\ln\phi + \chi\phi(1-\phi)`$, with $`\phi = \phi_2`$. A homogeneous solution is unstable where the curvature is negative:


```math
\frac{\partial^2}{\partial\phi^2} = \frac{1}{1-\phi} + \frac{1}{m\phi} - 2\chi < 0
```


The smallest $`\chi`$ for which this can happen is the minimum over $`\phi`$ of $`\tfrac12[1/(1-\phi) + 1/(m\phi)]`$. Setting its derivative to zero gives $`\phi_c = 1/(1+\sqrt m)`$ and


**Equation (99)**

```math
\chi_c = \frac{1}{2}\left(1 + \frac{1}{\sqrt m}\right)^2 \;\xrightarrow{m\to\infty}\; \frac12
```


### Motivation and explanation

**Why volume fractions.** Each segment, not each molecule, takes up a site. Mole fraction badly understates how much of the space the polymer fills: 1 mol % of a 1000-segment chain occupies about 91 % of the volume.

**Meaning of $`\chi`$.**
- $`\chi < \chi_c`$: miscible at all compositions (a "good" solvent when $`\chi`$ is small).
- $`\chi > \chi_c`$: phase separation.

For long chains $`\chi_c\to 0.5`$, so a very small energetic penalty is enough to make a polymer insoluble. The entropic gain is tiny per segment, so it cannot pay for much unfavourable energy. This is why most pairs of polymers do not mix.

**Limits.**
- Mean-field lattice theory is poor in dilute solution.
- In practice $`\chi`$ depends on composition and temperature.
- A constant-$`\chi`$ model does not describe temperature-driven miscibility changes. A suitable $`\chi(T,x)`$ can represent a lower critical solution temperature, but specific interactions must then enter through that parameter or a richer model.

### Worked example

**Problem.** A polymer with $`m = 1000`$ dissolves in a solvent with an assumed $`\chi = 0.4`$ (illustrative value). Find the solvent activity at polymer volume fractions $`\phi_2 = 0.1`$ and $`0.5`$, compare with Raoult's law ($`a_1 = x_1`$), and check whether the solution is stable.

**Mole fractions.** From $`\phi_2/\phi_1 = mx_2/x_1`$:
- at $`\phi_2 = 0.1`$, $`x_1 = 0.99989`$;
- at $`\phi_2 = 0.5`$, $`x_1 = 0.99900`$.

The solution is nearly pure solvent by mole fraction.

**Activities from (98).**

| $`\phi_2`$ | $`a_1`$ (FH, $`\chi = 0.4`$) | $`a_1`$ (athermal, $`\chi = 0`$) | Raoult $`x_1`$ | $`\gamma_1 = a_1/x_1`$ |
|---|---|---|---|---|
| 0.1 | 0.9985 | 0.9946 | 0.9999 | 0.9987 |
| 0.5 | 0.911 | 0.824 | 0.999 | 0.912 |

**Interpretation.** At half volume fraction the solvent's activity is 9 % below Raoult's prediction ($`\gamma_1 = 0.91`$), even though the mixture is 99.9 mol % solvent. With $`\chi = 0`$ (no energetic effect at all) the activity drops further, to 0.82. So the deviation is mainly *entropic*, from the size difference. The positive $`\chi`$ partly offsets it.

**Stability.** From (99), $`\chi_c = \tfrac12(1 + 1/\sqrt{1000})^2 = 0.532`$ at $`\phi_c = 0.031`$. Since $`0.4 < 0.532`$, the solution is stable at all compositions. Raising $`\chi`$ above 0.53, e.g. by cooling, would make it split into a dilute and a concentrated polymer phase. The critical point lies at only 3 % polymer.

### Link to other topics

The curvature condition used in Step 5 is the general test for liquid–liquid phase separation, developed fully later for small-molecule mixtures (binodal and spinodal). The combinatorial (size-and-shape) entropy of Flory–Huggins reappears as the combinatorial term of UNIQUAC.

### Summary

Flory–Huggins theory writes the entropy of mixing in volume fractions and adds one Margules-like energy parameter $`\chi`$. For a large solute it predicts strong, mainly entropic, negative deviations of the solvent activity from Raoult's law. It also predicts phase separation when $`\chi`$ exceeds $`\tfrac12(1 + m^{-1/2})^2`$, close to ½ for long chains.

## Section 19: Local-composition models (Wilson and NRTL)

### Intuition

Take an equimolar mixture. Around a molecule of type 1 you might find four other 1's and three 2's among seven neighbours. Around a molecule of 2, three 1's and four 2's. The bulk is 50:50, but each species locally "sees" more of its own kind if like interactions are stronger. The local mole fractions $`x_{ji}`$ (the fraction of $`j`$ around a central $`i`$) differ from the bulk $`x_j`$.

The model weights each possible neighbour by $`\exp(-\text{interaction energy}/RT)`$, so the local composition shifts towards energetically favoured neighbours. It shifts less as temperature rises, since thermal motion randomises the arrangement.

*Analogy: people at a party clustering with friends.* The overall guest list is 50:50, but each group looks more homogeneous from the inside. The analogy breaks down because molecules have no fixed "friends": the preference is a Boltzmann-weighted average over fluctuating neighbours. And the model's two-body energy parameters are still effective, fitted quantities, not true pair potentials.

### Derivation

**Step 1: local compositions (Wilson).** Around a central molecule 1, the ratio of 2-neighbours to 1-neighbours is the bulk ratio, weighted by Boltzmann factors of the interaction energies $`\lambda_{21}`$ (2–1) and $`\lambda_{11}`$ (1–1):


**Equation (100)**

```math
\frac{x_{21}}{x_{11}} = \frac{x_2}{x_1}\exp\!\left(-\frac{\lambda_{21} - \lambda_{11}}{RT}\right), \qquad \frac{x_{12}}{x_{22}} = \frac{x_1}{x_2}\exp\!\left(-\frac{\lambda_{12} - \lambda_{22}}{RT}\right)
```


**Step 2: Wilson's excess Gibbs energy.** Wilson used local volume fractions in a Flory–Huggins-type entropy expression. The result is


**Equation (101)**

```math
\frac{\underline{G}^{ex}}{RT} = -x_1\ln(x_1 + \Lambda_{12}x_2) - x_2\ln(x_2 + \Lambda_{21}x_1)
```


with


```math
\Lambda_{12} = \frac{\underline{V}_2}{\underline{V}_1}\exp\!\left(-\frac{\lambda_{12} - \lambda_{11}}{RT}\right), \qquad \Lambda_{21} = \frac{\underline{V}_1}{\underline{V}_2}\exp\!\left(-\frac{\lambda_{21} - \lambda_{22}}{RT}\right).
```


Here the Wilson pair energy is symmetric, $`\lambda_{12}=\lambda_{21}`$, so the unlike-energy labels in the local-composition ratios and in the $`\Lambda`$ definitions are equivalent. The fitted parameters are the two unlike-minus-like energy differences. Their Boltzmann factors supply a physical temperature dependence, although extrapolation still depends on the parameter fit.

**Step 3: Wilson activity coefficients.** Differentiating (101):


**Equation (102)**

```math
\ln\gamma_1 = -\ln(x_1 + \Lambda_{12}x_2) + x_2\left(\frac{\Lambda_{12}}{x_1 + \Lambda_{12}x_2} - \frac{\Lambda_{21}}{x_2 + \Lambda_{21}x_1}\right)
```


with $`\ln\gamma_2`$ obtained by swapping 1 ↔ 2. At infinite dilution:


**Equation (103)**

```math
\ln\gamma_1^{\infty} = 1 - \ln\Lambda_{12} - \Lambda_{21}, \qquad \ln\gamma_2^{\infty} = 1 - \ln\Lambda_{21} - \Lambda_{12}
```


**Step 4: NRTL.** Renon and Prausnitz introduced a non-randomness factor $`\alpha`$ into the Boltzmann weighting. Define


```math
\tau_{21} = \frac{g_{21} - g_{11}}{RT}, \qquad \tau_{12} = \frac{g_{12} - g_{22}}{RT}, \qquad G_{ij} = \exp(-\alpha\tau_{ij}),
```


so that $`x_{21}/x_{11} = (x_2/x_1)G_{21}`$. Then


**Equation (104)**

```math
\frac{\underline{G}^{ex}}{RT} = x_1x_2\left(\frac{\tau_{21}G_{21}}{x_1 + x_2G_{21}} + \frac{\tau_{12}G_{12}}{x_2 + x_1G_{12}}\right)
```



**Equation (105)**

```math
\ln\gamma_1 = x_2^2\left[\tau_{21}\left(\frac{G_{21}}{x_1 + x_2G_{21}}\right)^2 + \frac{\tau_{12}G_{12}}{(x_2 + x_1G_{12})^2}\right], \qquad \ln\gamma_1^{\infty} = \tau_{21} + \tau_{12}G_{12}
```


The third parameter $`\alpha`$ is usually fixed rather than fitted: about 0.2–0.3 for general liquids, 0.2 for liquid–liquid equilibria, and higher for aqueous systems.

### Motivation and explanation

**Why local composition helps.** Using energy differences divided by $`RT`$ captures, with two parameters, how non-ideality changes with temperature. The parameters describe pairs, so binary data alone build multicomponent models with good accuracy (pairwise additivity is built in).

**Wilson cannot split.** For any positive $`\Lambda`$'s, Wilson's $`\Delta\underline{G}_{\mathrm{mix}}`$ stays convex in composition. So it can never predict two liquid phases, however large the activity coefficients. NRTL's extra parameter removes this restriction. That is the main practical reason for choosing it.

**Limits.** Both models remain empirical, and the "energies" are fitted quantities. Wilson also cannot show extrema in $`\ln\gamma`$, as with van Laar.

### Worked example

**Problem.**
(a) Fit Wilson to the water (1)–hydrogen peroxide (2) infinite-dilution values from Section 12 ($`\gamma_1^{\infty} = 0.509`$, $`\gamma_2^{\infty} = 0.288`$ at 75 °C), and compare $`\underline{G}^{ex}`$ with the two-constant Margules fit.
(b) For a strongly positive system with $`\gamma_1^{\infty} = \gamma_2^{\infty} = e^3 = 20.1`$, test whether Margules, Wilson and NRTL ($`\alpha = 0.3`$) predict a phase split.

**(a)** Solving (103) for the stated rounded dilute-limit values gives $`\Lambda_{12} = 2.544`$ and $`\Lambda_{21} = 0.742`$.

| $`x_1`$ | Wilson $`\underline{G}^{ex}`$ (J mol⁻¹) | Margules $`\underline{G}^{ex}`$ (J mol⁻¹) |
|---|---|---|
| 0.2 | −343 | −366 |
| 0.5 | −628 | −695 |
| 0.8 | −489 | −524 |

The two models share the same end points but differ by up to 10 % in the middle. The measured minimum (≈ −710 J mol⁻¹) favours Margules here, because that fit used the minimum itself. Two-point fits pin the ends; they do not guarantee the middle. Fit to data across the range when you have it.

**(b)** Each model is matched to $`\ln\gamma^{\infty} = 3`$ at both ends:
- Margules: $`A/RT = 3`$.
- Wilson: $`\Lambda_{12} = \Lambda_{21} = 0.120`$.
- NRTL ($`\alpha = 0.3`$): $`\tau_{12} = \tau_{21} = 1.92`$.

Evaluate the minimum curvature of $`\Delta\underline{G}_{\mathrm{mix}}/RT`$ over $`0 < x_1 < 1`$:

| Model | Min $`\partial^2(\Delta\underline{G}_{\mathrm{mix}}/RT)/\partial x_1^2`$ | Phase split? |
|---|---|---|
| Margules | −2.0 | yes |
| Wilson | +0.18 | no |
| NRTL | −1.09 | yes |

With identical dilute-limit behaviour, Wilson insists the liquids mix, while Margules and NRTL correctly allow splitting. If immiscibility is possible, Wilson is the wrong model.

### Link to other topics

NRTL is the standard model for liquid–liquid extraction and for heterogeneous azeotropic distillation. The curvature test used in (b) is developed into binodal and spinodal curves in the liquid–liquid equilibrium sections later.

### Summary

Local-composition models weight neighbours by Boltzmann factors of unlike-minus-like interaction energies. Wilson gives accurate, well-extrapolating fits for miscible mixtures but can never predict a phase split. NRTL adds a non-randomness parameter $`\alpha`$ and handles partial miscibility.
<!-- reading-content:end -->

[Previous](<../../../../../notes/Equilibrium Thermodynamics/05 - Activity-coefficient models/Complete section.md>) · [Subject index](<../../../../../notes/Equilibrium Thermodynamics/README.md>) · [Next](<../../../../../notes/Equilibrium Thermodynamics/05 - Activity-coefficient models/Complete section.md>)
