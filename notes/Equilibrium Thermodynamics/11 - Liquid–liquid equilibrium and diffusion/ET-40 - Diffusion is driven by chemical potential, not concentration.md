[Previous](<ET-39 - Binodal, spinodal and the stability of a single liquid.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-41 - Example, diffusion near the nitrobenzene–hexane consolute point.md>)

<!-- note-content:start -->
# Section 40: Diffusion is driven by chemical potential, not concentration

*Notation:* $`N_1`$ is the molar flux of 1 (mol m⁻² s⁻¹), $`c`$ the total molar concentration, $`z`$ position, and $`D`$ a diffusion coefficient.

## Intuition

Molecules do not "know" concentration; they respond to differences in free energy. In an ideal mixture the two coincide, since $`\mu_1`$ rises smoothly with $`x_1`$, so Fick's law works. In a strongly non-ideal mixture, $`\mu_1`$ may barely change, or even fall, as $`x_1`$ rises. Then a large concentration difference may give little or negative driving force.

At an equilibrium interface between two liquids, $`\mu_1`$ is equal on both sides, so there is no net flux despite the jump in composition.

## Derivation

**Step 1: ideal mixture.** $`\mu_1 = \underline{G}_1 + RT\ln x_1`$, so $`\partial\mu_1/\partial x_1 = RT/x_1`$. Change the variable in Fick's law:


**Equation (159)**

```math
N_1 = -Dc\frac{dx_1}{dz} = -Dc\left(\frac{\partial x_1}{\partial\mu_1}\right)\frac{d\mu_1}{dz} = -\frac{Dcx_1}{RT}\frac{d\mu_1}{dz}
```


The two forms are identical for an ideal mixture.

**Step 2: real mixture, taking (159) as fundamental.** Postulate that the chemical-potential form holds with a well-behaved coefficient $`D`$, and convert back using $`\partial\mu_1/\partial x_1 = RT(1/x_1 + \partial\ln\gamma_1/\partial x_1)`$:


**Equation (160)**

```math
N_1 = -\frac{Dcx_1}{RT}\frac{\partial\mu_1}{\partial x_1}\frac{dx_1}{dz} = -Dc\left(1 + \frac{\partial\ln\gamma_1}{\partial\ln x_1}\right)\frac{dx_1}{dz}
```


The measured (Fickian) coefficient is therefore

The conversion separates two questions. The mobility coefficient describes how readily molecules respond to a given chemical-potential gradient. The thermodynamic factor describes how much chemical-potential gradient a given composition gradient creates. Diffusion can therefore slow because the restoring force weakens even when molecules remain mobile.

Inside the spinodal the factor changes sign, but the mobility need not become negative: material still moves towards lower chemical potential. It runs uphill in concentration because, there, increasing concentration lowers chemical potential. Using a negative Fickian coefficient alone at arbitrarily short length scales would not describe the developing interface; the omitted gradient free energy supplies the additional physics needed for a spatial phase-separation model.


**Equation (161)**

```math
D_{12} = D\,\Gamma, \qquad \Gamma = 1 + \frac{\partial\ln\gamma_1}{\partial\ln x_1} = \frac{x_1x_2}{RT}\frac{\partial^2\underline{G}}{\partial x_1^2}
```


(the last form from (154) of Section 36).

**Step 3: consequences.**
- *Ideal mixture:* $`\Gamma = 1`$.
- *At the spinodal:* $`\Gamma = 0`$, so $`D_{12} = 0`$, whatever the molecular mobility.
- *Inside the spinodal:* $`\Gamma < 0`$, so the flux runs *up* the concentration gradient.
- *At an equilibrium interface:* the bulk chemical potentials are equal in the two phases, so there is no net transfer despite the composition jump. Across a diffuse interface, gradient contributions to the free energy must be included in the chemical potential; the homogeneous-liquid formula alone does not describe the interface.

**Step 4: regular solution.** For one-constant Margules, $`\ln\gamma_1 = (A/RT)x_2^2`$, so $`\partial\ln\gamma_1/\partial\ln x_1 = x_1\cdot(A/RT)\cdot2x_2\cdot(-1)`$, and


**Equation (162)**

```math
\Gamma = 1 - 2\frac{A}{RT}x_1x_2
```


## Motivation and explanation

**Why this matters.** Diffusion coefficients in strongly non-ideal liquids (near phase separation, or in associating mixtures) vary greatly with composition. Much of that variation is thermodynamic ($`\Gamma`$), not molecular ($`D`$). Correlations that separate the two, $`D_{12} = D\Gamma`$, extrapolate far better. This is the binary case of the Maxwell–Stefan approach to multicomponent diffusion.

**Limits.** Equation (160) assumes $`D`$ itself is a constant or smooth property. Very close to a consolute point, concentration fluctuations make that inadequate (next section).

## Link to other topics

The thermodynamic factor appears in mass-transfer correlations for extraction and in membrane transport. Section 41 tests (160) against measurements on nitrobenzene–hexane near its consolute point.

## Summary

Material moves down chemical-potential gradients. Rewriting Fick's law that way shows that the measured diffusion coefficient is a mobility times the thermodynamic factor $`\Gamma = 1 + \partial\ln\gamma_1/\partial\ln x_1`$. $`\Gamma`$ is 1 for an ideal mixture, zero at the spinodal and negative inside it. This explains zero flux across an equilibrium interface, and uphill diffusion during phase separation.
<!-- note-content:end -->

[Previous](<ET-39 - Binodal, spinodal and the stability of a single liquid.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-41 - Example, diffusion near the nitrobenzene–hexane consolute point.md>)
