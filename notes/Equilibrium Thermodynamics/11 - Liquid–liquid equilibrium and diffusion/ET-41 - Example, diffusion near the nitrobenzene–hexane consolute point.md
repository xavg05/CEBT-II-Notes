[Previous](<ET-40 - Diffusion is driven by chemical potential, not concentration.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Section 41: Example, diffusion near the nitrobenzene–hexane consolute point

*Components:* nitrobenzene (1), hexane (2).

## Intuition

At the consolute point the curvature of $`\underline{G}`$ vanishes, so $`\Gamma=0`$ and long-wavelength mutual diffusion becomes arbitrarily slow; molecular self-diffusion remains finite. Near that point, long-lived composition fluctuations couple to fluid motion and change the effective molecular mobility. A smooth-mobility approximation $`D_{12}=D\Gamma`$ therefore predicts a steeper slowdown than observed. Replacing $`\Gamma`$ by $`\Gamma^n`$, with $`n<1`$, captures the gentler measured decrease empirically; it is not derived merely by averaging $`\Gamma`$ over local compositions.

## Derivation

**Step 1: thermodynamic factor from data.** $`\Gamma`$ was computed from a four-constant Redlich–Kister model fitted to measured total-pressure ($`P`$–$`x_1`$) data at 21, 25 and 35 °C. The fit used the full γ–φ equation, including Poynting and second-virial vapour corrections:


```math
P = \sum_i x_i\gamma_iP_i^{\mathrm{SAT}}\exp\!\left[\frac{(\underline{V}_i^{L} - B_{ii})(P - P_i^{\mathrm{SAT}})}{RT}\right]
```


The fitted model reproduces the flat, nearly constant pressure across the middle of the composition range. A flat $`P`$–$`x`$ curve is the signature of a system close to liquid–liquid splitting, by (132) of Section 27.

**Step 2: diffusion law.**


**Equation (163)**

```math
N_1 = -Dc\,\Gamma^{\,n}\,\frac{dx_1}{dz}
```


with $`D`$ taken as a smooth function of temperature and $`n`$ fitted.

## Motivation and explanation

**Why $`n\neq 1`$.** Near a critical point, composition fluctuations have a growing correlation length and couple to hydrodynamic motion. The transport mobility is therefore not a smooth background coefficient. Critical-phenomena and mode-coupling theories describe these coupled fluctuations; their full derivation is beyond this course. The power $`\Gamma^n`$ represents the resulting transport enhancement relative to the simple $`D\Gamma`$ model. Thinking of diffusion as sampling fluctuating compositions is useful intuition, but simple averaging of $`\Gamma`$ is not a derivation of the fitted exponent. Values near 0.6 work for several systems.

**What is robust.** The qualitative prediction (diffusion slows to zero at the consolute point, through thermodynamics rather than viscosity) is confirmed. The quantitative form needs the empirical exponent.

**Limits.** The fitted $`n`$ depends on the activity-coefficient model used for $`\Gamma`$; a poor $`\gamma`$ model would be absorbed into $`n`$. Far from the consolute point, fluctuations are small and $`n\to 1`$ is expected to suffice.

## Link to other topics

Critical slowing-down of diffusion matters in extraction and crystallisation operated near miscibility limits, and in supercritical-fluid processes. The same thermodynamic-factor correction applies to multicomponent diffusion in non-ideal mixtures.

## Summary

Near the nitrobenzene–hexane consolute point (≈19.4 °C), the measured diffusion coefficient collapses towards zero, as the thermodynamic factor predicts. Within this empirical model, raising $`\Gamma`$ to a power of about 0.64 fits the data, representing the effect of critical composition fluctuations on transport. The final unit adds a vapour to two liquid phases: vapour–liquid–liquid equilibrium and steam distillation.

## Conclusion

Liquid–liquid equilibrium is governed by the curvature of the Gibbs energy of mixing: the common tangent gives the equilibrium phases, the spinodal the limit of stability, and the consolute point where they meet. Because the true driving force for diffusion is the chemical-potential gradient, the same curvature makes diffusion slow to zero at the spinodal and run uphill inside it. The final part combines liquid–liquid and vapour–liquid equilibrium.
<!-- note-content:end -->

[Previous](<ET-40 - Diffusion is driven by chemical potential, not concentration.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)
