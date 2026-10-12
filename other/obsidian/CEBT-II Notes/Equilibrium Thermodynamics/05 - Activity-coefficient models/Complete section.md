[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Activity-coefficient models

## Overview

This part surveys the models in common use. Random-mixing models put all non-ideality into energy: the flexible Redlich–Kister polynomial, van Laar (derived from the van der Waals equation) and regular solution theory, which predicts $\gamma$'s from pure-component solubility parameters (Section 17). Flory–Huggins theory handles molecules of very different size, writing the entropy in volume fractions (Section 18). Local-composition models (Wilson, NRTL) let each molecule's neighbourhood differ from the bulk; only NRTL can predict two liquid phases (Section 19). UNIQUAC splits size-and-shape from energy, UNIFAC estimates both from functional groups, and the part ends with how to choose a model (Section 20). Margules, regular solution theory and van Laar are the models to be able to use by hand.

*Assumed throughout:* $RT\ln\gamma_i = \partial(n\underline{G}^{ex})/\partial n_i$ and the consistency results of Sections 11–12.

## Section 17: Random-mixing models (Redlich–Kister, van Laar, regular solution theory)

### Intuition

If molecules mix at random, the entropy of mixing is the ideal value, and all non-ideality is energetic: the cost (or gain) of replacing like–like contacts with like–unlike ones. For non-polar molecules held together by dispersion forces, a good rule of thumb is that the unlike attraction is the geometric mean of the two like attractions. That makes the energy of mixing proportional to the *square of the difference* in "stickiness" of the two liquids. The result is always a positive deviation, larger the more different the liquids are: "like dissolves like".

The solubility parameter $\delta$ is a measure of that stickiness per unit volume. It comes from the energy needed to vaporise the liquid.

*Analogy: magnets of different strengths.* Mixing strong and weak magnets loses some of the strong–strong attraction, and the weak–strong pairs never fully make it up. The analogy breaks down for hydrogen bonding and charge transfer, where unlike pairs can attract *more* strongly than either like pair. RST cannot describe those negative deviations.

### Derivation

**Step 1: Redlich–Kister.** Expand $\underline{G}^{ex}$ as a polynomial in $(x_1 - x_2)$ multiplied by $x_1x_2$, which guarantees $\underline{G}^{ex} = 0$ for each pure component:

$$\underline{G}^{ex} = x_1x_2\left[A + B(x_1 - x_2) + C(x_1 - x_2)^2 + \dots\right] \tag{89}$$

One term gives one-constant Margules; two terms give two-constant Margules (Section 12). Activity coefficients follow from Section 11's formulas, and consistency is automatic. The constants are fitting parameters with no physical meaning, so extrapolating beyond the fitted $T$ and composition range is unsafe.

**Step 2: van Laar, from the van der Waals equation.** Assume random mixing ($\underline{S}^{ex} = 0$) and no volume change ($\underline{V}^{ex} = 0$, so $\underline{H}^{ex} = \underline{U}^{ex}$). For a vdW liquid with $\underline{V}\approx b$, the energy relative to the ideal gas is $\underline{U} - \underline{U}^{\mathrm{IG}} = -a/b$. Apply this to each pure liquid and to the mixture, using the vdW mixing rules $a = (x_1\sqrt{a_1} + x_2\sqrt{a_2})^2$ and $b = x_1b_1 + x_2b_2$. The ideal-gas energies cancel (no excess for ideal gases), leaving

$$\underline{G}^{ex} = \underline{U}^{ex} = -\frac{a}{b} + x_1\frac{a_1}{b_1} + x_2\frac{a_2}{b_2} = \frac{x_1x_2b_1b_2}{x_1b_1 + x_2b_2}\left(\frac{\sqrt{a_1}}{b_1} - \frac{\sqrt{a_2}}{b_2}\right)^2 \tag{90}$$

(the last step is algebra, checked symbolically).

**Step 3: van Laar activity coefficients.** Define

$$\alpha = \frac{b_1}{RT}\left(\frac{\sqrt{a_1}}{b_1} - \frac{\sqrt{a_2}}{b_2}\right)^2, \qquad \beta = \frac{b_2}{b_1}\,\alpha .$$

Then (90) becomes $\underline{G}^{ex}/RT = \alpha\beta x_1x_2/(\alpha x_1 + \beta x_2)$, and differentiating gives

$$\ln\gamma_1 = \frac{\alpha}{\left(1 + \dfrac{\alpha x_1}{\beta x_2}\right)^2}, \qquad \ln\gamma_2 = \frac{\beta}{\left(1 + \dfrac{\beta x_2}{\alpha x_1}\right)^2} \tag{91}$$

At infinite dilution, $\ln\gamma_1^{\infty} = \alpha$ and $\ln\gamma_2^{\infty} = \beta$. In practice $\alpha$ and $\beta$ are fitted to data, e.g. two $\gamma^{\infty}$ values from ebulliometry, rather than computed from vdW constants, which predict poorly.

**Step 4: regular solution theory.** Keep van Laar's structure, but replace the vdW quantities with measured ones:
- $b_i \to \underline{V}_i$, the liquid molar volume;
- $\sqrt{a_i}/b_i \to \delta_i$, since $a_i/b_i^2$ is the energy per unit volume needed to pull the liquid apart.

That energy is the **cohesive energy density**, measured by vaporisation:

$$\delta_i = \sqrt{\frac{\Delta\underline{H}_i^{\mathrm{vap}} - RT}{\underline{V}_i}} \tag{92}$$

($\Delta\underline{U}^{\mathrm{vap}} = \Delta\underline{H}^{\mathrm{vap}} - RT$ for an ideal-gas vapour.) With volume fractions $\Phi_i = x_i\underline{V}_i/\sum_jx_j\underline{V}_j$, (90) becomes

$$\underline{G}^{ex} = \underline{H}^{ex} = (x_1\underline{V}_1 + x_2\underline{V}_2)\,\Phi_1\Phi_2\,(\delta_1 - \delta_2)^2 \tag{93}$$

and differentiating with respect to $n_1$ gives

$$\ln\gamma_1 = \frac{\underline{V}_1}{RT}\,\Phi_2^2\,(\delta_1 - \delta_2)^2, \qquad \ln\gamma_2 = \frac{\underline{V}_2}{RT}\,\Phi_1^2\,(\delta_1 - \delta_2)^2 \tag{94}$$

A refinement replaces $(\delta_1 - \delta_2)^2$ with $(\delta_1 - \delta_2)^2 + 2l_{12}\delta_1\delta_2$, where the binary correction $l_{12}$ allows for departures from the geometric-mean rule. It is usually set to zero, which keeps RST fully predictive.

### Motivation and explanation

**Why the square.** The geometric-mean rule $a_{12} = \sqrt{a_1a_2}$ gives an unlike interaction that is never stronger than the average of the like ones. The energy lost on mixing is then a perfect square, so RST and vdW-based van Laar always give $\gamma > 1$.

**Ranking the three.**
- *Redlich–Kister:* the most flexible fit, but with no physics and no extrapolation. It is the best choice for your own calculations when you have good data.
- *Van Laar:* two physically motivated parameters equal to $\ln\gamma^{\infty}$, but $\ln\gamma$ is monotonic and the model cannot show extrema.
- *RST:* no mixture data needed, good for non-polar mixtures, and ideal for back-of-envelope estimates. It fails for polar and hydrogen-bonding systems and cannot give negative deviations.

**Excess entropy.** The regular-solution derivation and the vdW-based van Laar derivation here take $\underline{S}^{ex}\approx0$. Redlich–Kister is a general fit to $\underline{G}^{ex}(T,x)$ and imposes no such restriction: $\underline{S}^{ex}=-(\partial\underline{G}^{ex}/\partial T)_{P,x}$ follows from its fitted temperature dependence. Size differences and oriented interactions can give significant excess entropy, motivating Flory–Huggins and local-composition models.

### Worked example

**Problem.** Use RST to predict the activity coefficients of (a) n-hexane (1)–benzene (2) and (b) cyclohexane (1)–benzene (2) at 25 °C.

**Pure-component data** (from vaporisation enthalpies and liquid densities at 298.15 K, via (92)):

| Liquid | $\underline{V}$ (cm³ mol⁻¹) | $\delta$ (MPa^½) |
|---|---|---|
| n-hexane | 131.6 | 14.86 |
| cyclohexane | 108.7 | 16.76 |
| benzene | 89.4 | 18.73 |

The n-hexane value matches the tabulated 14.9 MPa^½. Note that 1 MPa = 1 J cm⁻³, so $\underline{V}(\delta_1 - \delta_2)^2$ comes out directly in J mol⁻¹.

**Predictions from (93)–(94)** with $RT = 2479$ J mol⁻¹:

| Mixture | $\gamma_1^{\infty}$ | $\gamma_2^{\infty}$ | $\gamma_1$, $\gamma_2$ at $x_1 = 0.5$ | $\underline{G}^{ex}(0.5)$ (J mol⁻¹) |
|---|---|---|---|---|
| hexane–benzene | 2.21 | 1.72 | 1.14, 1.21 | 399 |
| cyclohexane–benzene | 1.19 | 1.15 | 1.04, 1.04 | 95 |

**Interpretation.**
- Hexane and benzene differ by 3.9 MPa^½ in $\delta$, so RST predicts strong positive deviation, with dilute hexane more than twice as volatile as Raoult's law suggests.
- Cyclohexane, closer in $\delta$, gives a mixture only slightly non-ideal.
- The asymmetry ($\gamma_1^{\infty}\neq\gamma_2^{\infty}$) comes purely from the different molar volumes.

These are predictions with no mixture data. They are good enough to tell whether a separation will be easy or hard, but should be checked against measured $\gamma$'s before design. Benzene's $\pi$-electrons interact specifically with other molecules, which pure dispersion theory ignores.

### Link to other topics

Solubility parameters are used directly to choose solvents for extraction and polymer processing, and they feed the Flory–Huggins $\chi$ parameter in Section 18. Van Laar constants are what an azeotrope measurement gives directly later in the course, through the two $\gamma$'s at the azeotropic composition.

### Summary

Redlich–Kister is a flexible fitting polynomial that can describe either sign of deviation and nonzero excess entropy through its temperature-dependent coefficients. Van Laar derives the $x_1x_2/(\alpha x_1+\beta x_2)$ form from the van der Waals equation, while RST replaces the vdW constants with solubility parameters to predict $\gamma$ from pure-component data, as $\ln\gamma_1=\underline{V}_1\Phi_2^2(\delta_1-\delta_2)^2/RT$. The particular geometric-mean derivations of van Laar and RST used here assume zero excess entropy and give positive deviations; empirical van Laar parameters can also fit negative deviations.

## Section 18: Flory–Huggins theory for size-asymmetric mixtures

*Notation:* solvent 1, polymer 2. $m = \underline{V}_2/\underline{V}_1$ is the number of lattice sites (solvent-sized segments) per chain. Volume fractions: $\phi_1 = x_1/(x_1 + mx_2)$, $\phi_2 = mx_2/(x_1 + mx_2)$.

### Intuition

Picture a lattice in which each site holds one solvent molecule or one chain segment. A dissolved polymer of $m$ segments occupies $m$ connected sites. There are far fewer ways to place one connected chain than $m$ separate small molecules, so the entropy gained on mixing is much smaller per segment than for small molecules. It is, however, much larger *per mole of polymer* than the ideal $-R\ln x$ suggests, because each polymer molecule spreads over many sites.

The volume fraction is the natural "how much space does it fill" variable, and entropy comes out as $\ln\phi$ instead of $\ln x$. *The lattice picture breaks down* for real chains, which are flexible and can cluster in dilute solution. The mean-field assumption that segments are spread uniformly then fails.

### Derivation

**Step 1: entropy of mixing (lattice counting result).**

$$\Delta\underline{S}^{\mathrm{mix}} = -R\left(x_1\ln\phi_1 + x_2\ln\phi_2\right) \tag{95}$$

This reduces to the ideal $-R\sum x_i\ln x_i$ when $m = 1$, since then $\phi_i = x_i$.

**Step 2: enthalpy of mixing.** Random contacts between solvent and segments, as in Margules, but counted per lattice site. There are $(x_1 + mx_2)$ sites per mole of molecules:

$$\Delta\underline{H}^{\mathrm{mix}} = \underline{H}^{ex} = \chi RT\,(x_1 + mx_2)\,\phi_1\phi_2 \tag{96}$$

Here $\chi$ is the dimensionless interaction energy per contact, in units of $RT$. It can be estimated as $\chi \approx \underline{V}_1(\delta_1 - \delta_2)^2/RT$, as in RST.

**Step 3: excess Gibbs energy.** Subtract the ideal mixing terms from $\Delta\underline{G}^{\mathrm{mix}} = \Delta\underline{H}^{\mathrm{mix}} - T\Delta\underline{S}^{\mathrm{mix}}$:

$$\frac{\underline{G}^{ex}}{RT} = \underbrace{x_1\ln\frac{\phi_1}{x_1} + x_2\ln\frac{\phi_2}{x_2}}_{-\underline{S}^{ex}/R} + \underbrace{\chi(x_1 + mx_2)\phi_1\phi_2}_{\underline{H}^{ex}/RT} \tag{97}$$

Unlike RST, $\underline{S}^{ex}\neq 0$ whenever $m\neq 1$. The energetic term has the one-constant Margules structure, written in volume fractions.

**Step 4: solvent activity.** Differentiate $n\Delta\underline{G}^{\mathrm{mix}}/RT = n_1\ln\phi_1 + n_2\ln\phi_2 + \chi n_1\phi_2$ with respect to $n_1$:

$$\ln a_1 = \ln(\gamma_1x_1) = \ln\phi_1 + \left(1 - \frac{1}{m}\right)\phi_2 + \chi\phi_2^2 \tag{98}$$

This is the quantity measured by vapour-pressure lowering, freezing point or osmotic pressure of polymer solutions.

**Step 5: when does the solution split?** Per lattice site, $\Delta G^{\mathrm{mix}}/RT = (1-\phi)\ln(1-\phi) + (\phi/m)\ln\phi + \chi\phi(1-\phi)$, with $\phi = \phi_2$. A homogeneous solution is unstable where the curvature is negative:

$$\frac{\partial^2}{\partial\phi^2} = \frac{1}{1-\phi} + \frac{1}{m\phi} - 2\chi < 0$$

The smallest $\chi$ for which this can happen is the minimum over $\phi$ of $\tfrac12[1/(1-\phi) + 1/(m\phi)]$. Setting its derivative to zero gives $\phi_c = 1/(1+\sqrt m)$ and

$$\chi_c = \frac{1}{2}\left(1 + \frac{1}{\sqrt m}\right)^2 \;\xrightarrow{m\to\infty}\; \frac12 \tag{99}$$

### Motivation and explanation

**Why volume fractions.** Each segment, not each molecule, takes up a site. Mole fraction badly understates how much of the space the polymer fills: 1 mol % of a 1000-segment chain occupies about 91 % of the volume.

**Meaning of $\chi$.**
- $\chi < \chi_c$: miscible at all compositions (a "good" solvent when $\chi$ is small).
- $\chi > \chi_c$: phase separation.

For long chains $\chi_c\to 0.5$, so a very small energetic penalty is enough to make a polymer insoluble. The entropic gain is tiny per segment, so it cannot pay for much unfavourable energy. This is why most pairs of polymers do not mix.

**Limits.**
- Mean-field lattice theory is poor in dilute solution.
- In practice $\chi$ depends on composition and temperature.
- A constant-$\chi$ model does not describe temperature-driven miscibility changes. A suitable $\chi(T,x)$ can represent a lower critical solution temperature, but specific interactions must then enter through that parameter or a richer model.

### Worked example

**Problem.** A polymer with $m = 1000$ dissolves in a solvent with an assumed $\chi = 0.4$ (illustrative value). Find the solvent activity at polymer volume fractions $\phi_2 = 0.1$ and $0.5$, compare with Raoult's law ($a_1 = x_1$), and check whether the solution is stable.

**Mole fractions.** From $\phi_2/\phi_1 = mx_2/x_1$:
- at $\phi_2 = 0.1$, $x_1 = 0.99989$;
- at $\phi_2 = 0.5$, $x_1 = 0.99900$.

The solution is nearly pure solvent by mole fraction.

**Activities from (98).**

| $\phi_2$ | $a_1$ (FH, $\chi = 0.4$) | $a_1$ (athermal, $\chi = 0$) | Raoult $x_1$ | $\gamma_1 = a_1/x_1$ |
|---|---|---|---|---|
| 0.1 | 0.9985 | 0.9946 | 0.9999 | 0.9987 |
| 0.5 | 0.911 | 0.824 | 0.999 | 0.912 |

**Interpretation.** At half volume fraction the solvent's activity is 9 % below Raoult's prediction ($\gamma_1 = 0.91$), even though the mixture is 99.9 mol % solvent. With $\chi = 0$ (no energetic effect at all) the activity drops further, to 0.82. So the deviation is mainly *entropic*, from the size difference. The positive $\chi$ partly offsets it.

**Stability.** From (99), $\chi_c = \tfrac12(1 + 1/\sqrt{1000})^2 = 0.532$ at $\phi_c = 0.031$. Since $0.4 < 0.532$, the solution is stable at all compositions. Raising $\chi$ above 0.53, e.g. by cooling, would make it split into a dilute and a concentrated polymer phase. The critical point lies at only 3 % polymer.

### Link to other topics

The curvature condition used in Step 5 is the general test for liquid–liquid phase separation, developed fully later for small-molecule mixtures (binodal and spinodal). The combinatorial (size-and-shape) entropy of Flory–Huggins reappears as the combinatorial term of UNIQUAC.

### Summary

Flory–Huggins theory writes the entropy of mixing in volume fractions and adds one Margules-like energy parameter $\chi$. For a large solute it predicts strong, mainly entropic, negative deviations of the solvent activity from Raoult's law. It also predicts phase separation when $\chi$ exceeds $\tfrac12(1 + m^{-1/2})^2$, close to ½ for long chains.

## Section 19: Local-composition models (Wilson and NRTL)

### Intuition

Take an equimolar mixture. Around a molecule of type 1 you might find four other 1's and three 2's among seven neighbours. Around a molecule of 2, three 1's and four 2's. The bulk is 50:50, but each species locally "sees" more of its own kind if like interactions are stronger. The local mole fractions $x_{ji}$ (the fraction of $j$ around a central $i$) differ from the bulk $x_j$.

The model weights each possible neighbour by $\exp(-\text{interaction energy}/RT)$, so the local composition shifts towards energetically favoured neighbours. It shifts less as temperature rises, since thermal motion randomises the arrangement.

*Analogy: people at a party clustering with friends.* The overall guest list is 50:50, but each group looks more homogeneous from the inside. The analogy breaks down because molecules have no fixed "friends": the preference is a Boltzmann-weighted average over fluctuating neighbours. And the model's two-body energy parameters are still effective, fitted quantities, not true pair potentials.

### Derivation

**Step 1: local compositions (Wilson).** Around a central molecule 1, the ratio of 2-neighbours to 1-neighbours is the bulk ratio, weighted by Boltzmann factors of the interaction energies $\lambda_{21}$ (2–1) and $\lambda_{11}$ (1–1):

$$\frac{x_{21}}{x_{11}} = \frac{x_2}{x_1}\exp\!\left(-\frac{\lambda_{21} - \lambda_{11}}{RT}\right), \qquad \frac{x_{12}}{x_{22}} = \frac{x_1}{x_2}\exp\!\left(-\frac{\lambda_{12} - \lambda_{22}}{RT}\right) \tag{100}$$

**Step 2: Wilson's excess Gibbs energy.** Wilson used local volume fractions in a Flory–Huggins-type entropy expression. The result is

$$\frac{\underline{G}^{ex}}{RT} = -x_1\ln(x_1 + \Lambda_{12}x_2) - x_2\ln(x_2 + \Lambda_{21}x_1) \tag{101}$$

with

$$\Lambda_{12} = \frac{\underline{V}_2}{\underline{V}_1}\exp\!\left(-\frac{\lambda_{12} - \lambda_{11}}{RT}\right), \qquad \Lambda_{21} = \frac{\underline{V}_1}{\underline{V}_2}\exp\!\left(-\frac{\lambda_{21} - \lambda_{22}}{RT}\right).$$

Here the Wilson pair energy is symmetric, $\lambda_{12}=\lambda_{21}$, so the unlike-energy labels in the local-composition ratios and in the $\Lambda$ definitions are equivalent. The fitted parameters are the two unlike-minus-like energy differences. Their Boltzmann factors supply a physical temperature dependence, although extrapolation still depends on the parameter fit.

**Step 3: Wilson activity coefficients.** Differentiating (101):

$$\ln\gamma_1 = -\ln(x_1 + \Lambda_{12}x_2) + x_2\left(\frac{\Lambda_{12}}{x_1 + \Lambda_{12}x_2} - \frac{\Lambda_{21}}{x_2 + \Lambda_{21}x_1}\right) \tag{102}$$

with $\ln\gamma_2$ obtained by swapping 1 ↔ 2. At infinite dilution:

$$\ln\gamma_1^{\infty} = 1 - \ln\Lambda_{12} - \Lambda_{21}, \qquad \ln\gamma_2^{\infty} = 1 - \ln\Lambda_{21} - \Lambda_{12} \tag{103}$$

**Step 4: NRTL.** Renon and Prausnitz introduced a non-randomness factor $\alpha$ into the Boltzmann weighting. Define

$$\tau_{21} = \frac{g_{21} - g_{11}}{RT}, \qquad \tau_{12} = \frac{g_{12} - g_{22}}{RT}, \qquad G_{ij} = \exp(-\alpha\tau_{ij}),$$

so that $x_{21}/x_{11} = (x_2/x_1)G_{21}$. Then

$$\frac{\underline{G}^{ex}}{RT} = x_1x_2\left(\frac{\tau_{21}G_{21}}{x_1 + x_2G_{21}} + \frac{\tau_{12}G_{12}}{x_2 + x_1G_{12}}\right) \tag{104}$$

$$\ln\gamma_1 = x_2^2\left[\tau_{21}\left(\frac{G_{21}}{x_1 + x_2G_{21}}\right)^2 + \frac{\tau_{12}G_{12}}{(x_2 + x_1G_{12})^2}\right], \qquad \ln\gamma_1^{\infty} = \tau_{21} + \tau_{12}G_{12} \tag{105}$$

The third parameter $\alpha$ is usually fixed rather than fitted: about 0.2–0.3 for general liquids, 0.2 for liquid–liquid equilibria, and higher for aqueous systems.

### Motivation and explanation

**Why local composition helps.** Using energy differences divided by $RT$ captures, with two parameters, how non-ideality changes with temperature. The parameters describe pairs, so binary data alone build multicomponent models with good accuracy (pairwise additivity is built in).

**Wilson cannot split.** For any positive $\Lambda$'s, Wilson's $\Delta\underline{G}_{\mathrm{mix}}$ stays convex in composition. So it can never predict two liquid phases, however large the activity coefficients. NRTL's extra parameter removes this restriction. That is the main practical reason for choosing it.

**Limits.** Both models remain empirical, and the "energies" are fitted quantities. Wilson also cannot show extrema in $\ln\gamma$, as with van Laar.

### Worked example

**Problem.**
(a) Fit Wilson to the water (1)–hydrogen peroxide (2) infinite-dilution values from Section 12 ($\gamma_1^{\infty} = 0.509$, $\gamma_2^{\infty} = 0.288$ at 75 °C), and compare $\underline{G}^{ex}$ with the two-constant Margules fit.
(b) For a strongly positive system with $\gamma_1^{\infty} = \gamma_2^{\infty} = e^3 = 20.1$, test whether Margules, Wilson and NRTL ($\alpha = 0.3$) predict a phase split.

**(a)** Solving (103) for the stated rounded dilute-limit values gives $\Lambda_{12} = 2.544$ and $\Lambda_{21} = 0.742$.

| $x_1$ | Wilson $\underline{G}^{ex}$ (J mol⁻¹) | Margules $\underline{G}^{ex}$ (J mol⁻¹) |
|---|---|---|
| 0.2 | −343 | −366 |
| 0.5 | −628 | −695 |
| 0.8 | −489 | −524 |

The two models share the same end points but differ by up to 10 % in the middle. The measured minimum (≈ −710 J mol⁻¹) favours Margules here, because that fit used the minimum itself. Two-point fits pin the ends; they do not guarantee the middle. Fit to data across the range when you have it.

**(b)** Each model is matched to $\ln\gamma^{\infty} = 3$ at both ends:
- Margules: $A/RT = 3$.
- Wilson: $\Lambda_{12} = \Lambda_{21} = 0.120$.
- NRTL ($\alpha = 0.3$): $\tau_{12} = \tau_{21} = 1.92$.

Evaluate the minimum curvature of $\Delta\underline{G}_{\mathrm{mix}}/RT$ over $0 < x_1 < 1$:

| Model | Min $\partial^2(\Delta\underline{G}_{\mathrm{mix}}/RT)/\partial x_1^2$ | Phase split? |
|---|---|---|
| Margules | −2.0 | yes |
| Wilson | +0.18 | no |
| NRTL | −1.09 | yes |

With identical dilute-limit behaviour, Wilson insists the liquids mix, while Margules and NRTL correctly allow splitting. If immiscibility is possible, Wilson is the wrong model.

### Link to other topics

NRTL is the standard model for liquid–liquid extraction and for heterogeneous azeotropic distillation. The curvature test used in (b) is developed into binodal and spinodal curves in the liquid–liquid equilibrium sections later.

### Summary

Local-composition models weight neighbours by Boltzmann factors of unlike-minus-like interaction energies. Wilson gives accurate, well-extrapolating fits for miscible mixtures but can never predict a phase split. NRTL adds a non-randomness parameter $\alpha$ and handles partial miscibility.

## Section 20: UNIQUAC, UNIFAC and choosing a model

*Notation:* $r_i$ is a volume parameter and $q_i$ a surface-area parameter for molecule $i$, relative to a standard segment. $\phi_i = x_ir_i/\sum_jx_jr_j$ is the segment (volume) fraction and $\theta_i = x_iq_i/\sum_jx_jq_j$ the area fraction. $z = 10$ is the lattice coordination number.

### Intuition

Molecules interact through their *surfaces*: a long chain exposes more contact area per unit volume than a compact sphere. UNIQUAC therefore counts arrangements with volumes (as Flory–Huggins does), corrects them for surface area (shape), and counts interactions through surface-area fractions.

UNIFAC adds a powerful idea. A CH₂ group behaves much the same whether it sits in hexane or in a fatty acid. So the mixture can be modelled as a soup of groups whose interactions were fitted once, across many systems. *The analogy breaks down* when neighbouring groups influence each other strongly, for example an OH next to a C=O. That is the main source of UNIFAC errors, and why its predictions must be checked.

### Derivation

**Step 1: UNIQUAC structure.**

$$\frac{\underline{G}^{ex}}{RT} = \frac{\underline{G}^{ex}_{\mathrm{comb}}}{RT} + \frac{\underline{G}^{ex}_{\mathrm{res}}}{RT} \tag{106}$$

**Step 2: combinatorial (size and shape) part.**

$$\frac{\underline{G}^{ex}_{\mathrm{comb}}}{RT} = \sum_i x_i\ln\frac{\phi_i}{x_i} + \frac{z}{2}\sum_i q_ix_i\ln\frac{\theta_i}{\phi_i} \tag{107}$$

The first sum is the Flory–Huggins entropy; the second corrects for shape (area relative to volume). Differentiating gives, at infinite dilution of $i$ in $j$ (with $V = r_i/r_j$, $F = q_i/q_j$):

$$\ln\gamma_i^{C,\infty} = 1 - V + \ln V - \frac{z}{2}q_i\left(1 - \frac{V}{F} + \ln\frac{V}{F}\right) \tag{108}$$

**Step 3: residual (energy) part.**

$$\frac{\underline{G}^{ex}_{\mathrm{res}}}{RT} = -\sum_i q_ix_i\ln\left(\sum_j\theta_j\tau_{ji}\right), \qquad \tau_{ji} = \exp\!\left(-\frac{u_{ji} - u_{ii}}{RT}\right) \tag{109}$$

Two parameters per binary, $u_{12} - u_{22}$ and $u_{21} - u_{11}$, are fitted to data as in Wilson. With $\tau_{ij} = 1$ (no energetic difference), the residual term vanishes.

**Step 4: getting $r_i$ and $q_i$ by group contribution.** Sum tabulated group values: $r_i = \sum_k\nu_k^{(i)}R_k$ and $q_i = \sum_k\nu_k^{(i)}Q_k$, where $\nu_k^{(i)}$ is the number of groups of type $k$ in molecule $i$. UNIFAC does the same for the residual term, using tabulated group–group interaction parameters in place of fitted molecular ones.

### Motivation and explanation

**Why split size from energy.** The combinatorial part is fixed by molecular structure and needs no data. Only the energetic part needs fitting, so the fitted parameters are fewer and depend less on temperature. This makes UNIQUAC the default in process simulators when no better-tested model exists for a system.

**Why UNIFAC is both useful and dangerous.** It gives activity coefficients for systems never measured, which is useful at the screening stage. But the residual (energy) part from groups is much less accurate than the combinatorial part. Treat UNIFAC numbers as first estimates, and verify them before designing equipment.

**Choosing a model.**
1. *Moderately non-ideal mixtures:* all models perform well. Use what the data and software support.
2. *Quick hand estimates:* RST, or one-constant Margules.
3. *Very different species* (polar/non-polar, hydrogen bonding): Wilson, NRTL or UNIQUAC are more reliable. Multi-term Redlich–Kister also fits well but extrapolates poorly in temperature.
4. *If liquid–liquid splitting is possible:* not Wilson. Use NRTL, UNIQUAC or Redlich–Kister.
5. *In a process simulator, by default:* UNIQUAC. For your own calculations: Redlich–Kister fitted to data.
6. *No data:* measure binary VLE (or have it measured); otherwise estimate with UNIFAC and treat the result with suspicion.

Every model is a fit. Its reliability depends as much on the data behind the parameters (range of $T$ and composition, quality) as on the model. A sophisticated model fitted to sparse data is no better than a simple one.

### Worked example

**Problem.** Using UNIFAC group parameters, find the UNIQUAC combinatorial (size–shape) contribution to $\gamma^{\infty}$ for (a) n-hexadecane dilute in n-hexane and the reverse, and (b) ethanol dilute in water and the reverse.

**Group values.**

| Group | $R_k$ | $Q_k$ |
|---|---|---|
| CH₃ | 0.9011 | 0.848 |
| CH₂ | 0.6744 | 0.540 |
| OH | 1.0000 | 1.200 |
| H₂O | 0.9200 | 1.400 |

**Molecules.**

| Molecule | Groups | $r$ | $q$ |
|---|---|---|---|
| n-hexane | 2 CH₃ + 4 CH₂ | 4.500 | 3.856 |
| n-hexadecane | 2 CH₃ + 14 CH₂ | 11.244 | 9.256 |
| ethanol | CH₃ + CH₂ + OH | 2.576 | 2.588 |
| water | H₂O | 0.920 | 1.400 |

**From (108).**

| Solute (dilute) in solvent | $\gamma^{C,\infty}$ |
|---|---|
| hexadecane in hexane | 0.58 |
| hexane in hexadecane | 0.74 |
| ethanol in water | 1.68 |
| water in ethanol | 1.15 |

**Interpretation.**
- *Alkanes:* the two have nearly identical chemistry, so the residual term is close to zero and these combinatorial values are essentially the whole prediction. Both $\gamma$'s are below 1: size differences alone produce *negative* deviations from Raoult's law, as Flory–Huggins showed. A long chain dissolved in short ones gains entropy.
- *Ethanol–water:* the combinatorial part is modest. The large and temperature-dependent non-ideality of this system comes from the residual (hydrogen-bonding) term, which needs fitted or group-interaction parameters.

So the combinatorial term matters most for size asymmetry, and the residual term matters most for chemical difference.

### Link to other topics

These models supply the $\gamma_i$ in $y_iP = x_i\gamma_iP_i^{\mathrm{SAT}}$ for the vapour–liquid equilibrium, azeotrope and liquid–liquid equilibrium sections that follow, and in distillation and extraction design.

### Summary

UNIQUAC splits $\underline{G}^{ex}$ into a combinatorial size–shape term, computed from volume and area parameters, and a residual energy term with two fitted parameters. UNIFAC estimates both from functional groups when no data exist. All activity-coefficient models are consistent fits whose reliability depends on the data behind them. Choose the simplest model the system allows, avoid Wilson when liquids may split, and verify group-contribution estimates.

## Conclusion

Every activity-coefficient model is a thermodynamically consistent fit whose reliability depends on the data behind it. Random-mixing models are simple and good for non-polar mixtures; Flory–Huggins handles size asymmetry; local-composition models extrapolate better and (except Wilson) can describe liquid splitting; UNIFAC gives first estimates without data. The next part returns to equilibrium itself, starting with the phase rule and equilibria where pressure is not uniform.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)
