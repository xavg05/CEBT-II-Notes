[Previous](<ET-18 - Flory–Huggins theory for size-asymmetric mixtures.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-20 - UNIQUAC, UNIFAC and choosing a model.md>)

<!-- note-content:start -->
# Section 19: Local-composition models (Wilson and NRTL)

## Intuition

Take an equimolar mixture. Around a molecule of type 1 you might find four other 1's and three 2's among seven neighbours. Around a molecule of 2, three 1's and four 2's. The bulk is 50:50, but each species locally "sees" more of its own kind if like interactions are stronger. The local mole fractions $x_{ji}$ (the fraction of $j$ around a central $i$) differ from the bulk $x_j$.

The model weights each possible neighbour by $\exp(-\text{interaction energy}/RT)$, so the local composition shifts towards energetically favoured neighbours. It shifts less as temperature rises, since thermal motion randomises the arrangement.

*Analogy: people at a party clustering with friends.* The overall guest list is 50:50, but each group looks more homogeneous from the inside. The analogy breaks down because molecules have no fixed "friends": the preference is a Boltzmann-weighted average over fluctuating neighbours. And the model's two-body energy parameters are still effective, fitted quantities, not true pair potentials.

## Derivation

**Step 1: local compositions (Wilson).** Around a central molecule 1, the ratio of 2-neighbours to 1-neighbours is the bulk ratio, weighted by Boltzmann factors of the interaction energies $\lambda_{21}$ (2–1) and $\lambda_{11}$ (1–1):

$$\frac{x_{21}}{x_{11}} = \frac{x_2}{x_1}\exp\!\left(-\frac{\lambda_{21} - \lambda_{11}}{RT}\right), \qquad \frac{x_{12}}{x_{22}} = \frac{x_1}{x_2}\exp\!\left(-\frac{\lambda_{12} - \lambda_{22}}{RT}\right) \tag{100}$$

**Step 2: Wilson's excess Gibbs energy.** Wilson used local volume fractions in a Flory–Huggins-type entropy expression. The result is

A Boltzmann factor changes a *relative* probability; it does not by itself specify a local composition. The local fractions must still sum to unity. Normalising the two possible neighbour weights is what produces denominators such as $x_1+x_2G_{21}$ in NRTL. They compare the available populations after energetic preferences have been applied, rather than adding extra neighbours to a fixed coordination shell.

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

## Motivation and explanation

**Why local composition helps.** Using energy differences divided by $RT$ captures, with two parameters, how non-ideality changes with temperature. The parameters describe pairs, so binary data alone build multicomponent models with good accuracy (pairwise additivity is built in).

**Wilson cannot split.** For any positive $\Lambda$'s, Wilson's $\Delta\underline{G}_{\mathrm{mix}}$ stays convex in composition. So it can never predict two liquid phases, however large the activity coefficients. NRTL's extra parameter removes this restriction. That is the main practical reason for choosing it.

**Limits.** Both models remain empirical, and the "energies" are fitted quantities. Wilson also cannot show extrema in $\ln\gamma$, as with van Laar.

## Worked example

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

## Link to other topics

NRTL is the standard model for liquid–liquid extraction and for heterogeneous azeotropic distillation. The curvature test used in (b) is developed into binodal and spinodal curves in the liquid–liquid equilibrium sections later.

## Summary

Local-composition models weight neighbours by Boltzmann factors of unlike-minus-like interaction energies. Wilson gives accurate, well-extrapolating fits for miscible mixtures but can never predict a phase split. NRTL adds a non-randomness parameter $\alpha$ and handles partial miscibility.
<!-- note-content:end -->

[Previous](<ET-18 - Flory–Huggins theory for size-asymmetric mixtures.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-20 - UNIQUAC, UNIFAC and choosing a model.md>)
