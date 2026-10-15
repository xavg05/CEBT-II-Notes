[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-18 - Flory–Huggins theory for size-asymmetric mixtures.md>)

<!-- note-content:start -->
# Section 17: Random-mixing models (Redlich–Kister, van Laar, regular solution theory)

## Intuition

If molecules mix at random, the entropy of mixing is the ideal value, and all non-ideality is energetic: the cost (or gain) of replacing like–like contacts with like–unlike ones. For non-polar molecules held together by dispersion forces, a good rule of thumb is that the unlike attraction is the geometric mean of the two like attractions. That makes the energy of mixing proportional to the *square of the difference* in "stickiness" of the two liquids. The result is always a positive deviation, larger the more different the liquids are: "like dissolves like".

The solubility parameter $\delta$ is a measure of that stickiness per unit volume. It comes from the energy needed to vaporise the liquid.

*Analogy: magnets of different strengths.* Mixing strong and weak magnets loses some of the strong–strong attraction, and the weak–strong pairs never fully make it up. The analogy breaks down for hydrogen bonding and charge transfer, where unlike pairs can attract *more* strongly than either like pair. RST cannot describe those negative deviations.

## Derivation

**Step 1: Redlich–Kister.** Expand $\underline{G}^{ex}$ as a polynomial in $(x_1 - x_2)$ multiplied by $x_1x_2$, which guarantees $\underline{G}^{ex} = 0$ for each pure component:

$$\underline{G}^{ex} = x_1x_2\left[A + B(x_1 - x_2) + C(x_1 - x_2)^2 + \dots\right] \tag{89}$$

One term gives one-constant Margules; two terms give two-constant Margules (Section 12). Activity coefficients follow from Section 11's formulas, and consistency is automatic. The constants are fitting parameters with no physical meaning, so extrapolating beyond the fitted $T$ and composition range is unsafe.

**Step 2: van Laar, from the van der Waals equation.** Assume random mixing ($\underline{S}^{ex} = 0$) and no volume change ($\underline{V}^{ex} = 0$, so $\underline{H}^{ex} = \underline{U}^{ex}$). For a vdW liquid with $\underline{V}\approx b$, the energy relative to the ideal gas is $\underline{U} - \underline{U}^{\mathrm{IG}} = -a/b$. Apply this to each pure liquid and to the mixture, using the vdW mixing rules $a = (x_1\sqrt{a_1} + x_2\sqrt{a_2})^2$ and $b = x_1b_1 + x_2b_2$. The ideal-gas energies cancel (no excess for ideal gases), leaving

$$\underline{G}^{ex} = \underline{U}^{ex} = -\frac{a}{b} + x_1\frac{a_1}{b_1} + x_2\frac{a_2}{b_2} = \frac{x_1x_2b_1b_2}{x_1b_1 + x_2b_2}\left(\frac{\sqrt{a_1}}{b_1} - \frac{\sqrt{a_2}}{b_2}\right)^2 \tag{90}$$

(the last step is algebra, checked symbolically).

Putting the three energy terms in (90) over the common denominator $x_1b_1+x_2b_2$ cancels the pure-component contributions. What remains is proportional to $x_1x_2$: only replacing like contacts by unlike contacts can create an excess. Factoring the remaining quadratic as a square exposes a strong prediction of the geometric-mean rule: that replacement cannot lower the energy of mixing.

When the two cohesive energy densities match, the square vanishes even if the molecules have different volumes. RST then predicts no energetic departure; it has not shown that every real size-dependent or orientational effect vanishes. The separate entropy correction in the next model addresses precisely what this regular-solution assumption leaves out.

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

## Motivation and explanation

**Why the square.** The geometric-mean rule $a_{12} = \sqrt{a_1a_2}$ gives an unlike interaction that is never stronger than the average of the like ones. The energy lost on mixing is then a perfect square, so RST and vdW-based van Laar always give $\gamma > 1$.

**Ranking the three.**
- *Redlich–Kister:* the most flexible fit, but with no physics and no extrapolation. It is the best choice for your own calculations when you have good data.
- *Van Laar:* two physically motivated parameters equal to $\ln\gamma^{\infty}$, but $\ln\gamma$ is monotonic and the model cannot show extrema.
- *RST:* no mixture data needed, good for non-polar mixtures, and ideal for back-of-envelope estimates. It fails for polar and hydrogen-bonding systems and cannot give negative deviations.

**Excess entropy.** The regular-solution derivation and the vdW-based van Laar derivation here take $\underline{S}^{ex}\approx0$. Redlich–Kister is a general fit to $\underline{G}^{ex}(T,x)$ and imposes no such restriction: $\underline{S}^{ex}=-(\partial\underline{G}^{ex}/\partial T)_{P,x}$ follows from its fitted temperature dependence. Size differences and oriented interactions can give significant excess entropy, motivating Flory–Huggins and local-composition models.

## Worked example

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

## Link to other topics

Solubility parameters are used directly to choose solvents for extraction and polymer processing, and they feed the Flory–Huggins $\chi$ parameter in Section 18. Van Laar constants are what an azeotrope measurement gives directly later in the course, through the two $\gamma$'s at the azeotropic composition.

## Summary

Redlich–Kister is a flexible fitting polynomial that can describe either sign of deviation and nonzero excess entropy through its temperature-dependent coefficients. Van Laar derives the $x_1x_2/(\alpha x_1+\beta x_2)$ form from the van der Waals equation, while RST replaces the vdW constants with solubility parameters to predict $\gamma$ from pure-component data, as $\ln\gamma_1=\underline{V}_1\Phi_2^2(\delta_1-\delta_2)^2/RT$. The particular geometric-mean derivations of van Laar and RST used here assume zero excess entropy and give positive deviations; empirical van Laar parameters can also fit negative deviations.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-18 - Flory–Huggins theory for size-asymmetric mixtures.md>)
