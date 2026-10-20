[Previous](<ET-34 - Dissolved solids and the molality standard state.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Section 35: Ionic solutions, mean activity coefficients and Debye–Hückel theory

*Notation:* for a salt $`\mathrm{M}_p\mathrm{A}_q\to p\mathrm{M}^{z_+} + q\mathrm{A}^{z_-}`$, $`m`$ is the salt molality, $`z_\pm`$ are the ion charge numbers, and $`I = \tfrac12\sum_i z_i^2m_i`$ is the ionic strength. All $`\gamma`$'s here are on the molality scale; the superscript # is dropped.

## Intuition

Around each positive ion, negative ions are slightly more likely to be found than positive ones, and vice versa. Every ion therefore sits in a diffuse cloud of net opposite charge, its **ionic atmosphere**. The attraction between an ion and its atmosphere lowers the ion's energy, and so its chemical potential, below the ideal value: $`\gamma_{\pm} < 1`$.

The atmosphere's thickness, the Debye length, shrinks as more ions are added. Denser screening means a closer, stronger stabilising cloud. The effect scales with the square root of concentration, which is why even millimolar salt solutions are measurably non-ideal.

*Analogy: a celebrity in a crowd.* A celebrity draws admirers close, and the crowd's attention lowers their "escaping tendency". The analogy breaks down because the atmosphere is a time-averaged statistical excess of charge, not a fixed group. Every ion is simultaneously the centre of its own cloud and a member of others.

## Derivation

**Step 1: chemical potential of the dissolved salt.** For NaCl,


```math
\mu_{\mathrm{NaCl}} = \mu_{\mathrm{Na^+}} + \mu_{\mathrm{Cl^-}} = \mu^{\circ}_{\mathrm{Na^+}} + \mu^{\circ}_{\mathrm{Cl^-}} + RT\ln\left(\gamma_{\mathrm{Na^+}}m_{\mathrm{Na^+}}/m^{\circ}\right) + RT\ln\left(\gamma_{\mathrm{Cl^-}}m_{\mathrm{Cl^-}}/m^{\circ}\right)
```


Adding a single ion type would violate neutrality, so only this *sum* is physically defined.

**Step 2: mean ionic activity coefficient.** With $`m_{\mathrm{Na^+}} = m_{\mathrm{Cl^-}} = m`$, define the geometric mean $`\gamma_{\pm} = (\gamma_{\mathrm{Na^+}}\gamma_{\mathrm{Cl^-}})^{1/2}`$. Then


**Equation (148)**

```math
\mu_{\mathrm{NaCl}} = \mu^{\circ}_{\mathrm{NaCl}} + RT\ln a_{\mathrm{NaCl}}, \qquad a_{\mathrm{NaCl}} = (\gamma_{\pm}m/m^{\circ})^2
```


The square reflects two particles per formula unit. Plotted against $`m^2`$, the ideal-dilute line has unit slope.

**Step 3: general salt.** For $`\mathrm{M}_p\mathrm{A}_q`$, with $`m_+ = pm`$ and $`m_- = qm`$:

Adding a neutral formula unit adds the cations and anions together in their stoichiometric proportions. Their chemical potentials therefore add with those same weights. Because each chemical potential contains a logarithm, adding them multiplies the ionic activities and raises them to stoichiometric powers. Taking the corresponding root defines the geometric mean $`\gamma_{\pm}`$; an arithmetic mean would not reproduce the salt chemical potential.

The mean coefficient is not itself the complete salt activity. The latter also contains the ion molalities and their powers, as (148) shows for NaCl. In comparing the two salts in the table, equal salt molality gives neither equal ionic strength nor equal charge factor, so both changes must be included before attributing their different non-idealities to charge alone.


**Equation (149)**

```math
a_{\mathrm{M}_p\mathrm{A}_q} = a_+^{\,p}a_-^{\,q}, \qquad \gamma_{\pm}^{\,p+q} = \gamma_+^{\,p}\gamma_-^{\,q}
```


**Step 4: Debye–Hückel limiting law.** Treat the ions as point charges in a continuous dielectric. Then:
- solve Poisson's equation for the potential around a central ion, with the surrounding ion densities following Boltzmann distributions;
- linearise for weak potentials;
- compute the electrical work of charging the ion in its atmosphere.

The full derivation is beyond this course. The result is


**Equation (150)**

```math
\ln\gamma_{\pm} = -\alpha\,|z_+z_-|\sqrt{I}
```


where $`\alpha`$ depends only on the solvent's permittivity and the temperature. For water at 25 °C, $`\alpha = 1.171`$ kg^½ mol^-½. This is often written as $`\log_{10}\gamma_{\pm} = -0.509|z_+z_-|\sqrt{I}`$.

**Step 5: extended Debye–Hückel.** Giving the ions a finite size $`a`$, the distance of closest approach, caps how close the atmosphere can get:


**Equation (151)**

```math
\ln\gamma_{\pm} = -\frac{\alpha|z_+z_-|\sqrt{I}}{1 + \beta a\sqrt{I}} + \delta I
```


With $`\beta = 0.3281`$ Å⁻¹ kg^½ mol^-½ in water at 25 °C, and a typical $`a`$ of a few ångströms. An empirical linear term $`\delta I`$ is added at higher strengths.

## Motivation and explanation

**Why $`\sqrt{I}`$ and not $`I`$.** The atmosphere's size, the Debye length $`\kappa^{-1}`$, scales as $`I^{-1/2}`$. The ion–atmosphere energy goes as $`1/\kappa^{-1}\propto\sqrt{I}`$. This square-root law is a hallmark of long-range forces. Short-range (neutral-molecule) non-idealities start linearly in concentration.

**Why ionic strength.** Screening depends on all ions present, weighted by charge squared. In the dilute Debye–Hückel regime, adding another salt therefore lowers $`\gamma_{\pm}`$. Screening helps explain salting-in of proteins at low ionic strength. Salting-out at higher salt concentrations also involves hydration and other specific interactions and is beyond the Debye–Hückel limiting law.

**Limits.**
- The limiting law is exact as $`I\to 0`$ but accurate only below about $`I\approx 0.01`$ mol kg⁻¹.
- The extended form works to roughly $`I\approx 0.1`$.
- At higher strengths, real $`\gamma_{\pm}`$ curves pass through a minimum and rise again (ion hydration, ion pairing), which needs empirical models such as Pitzer's.

## Link to other topics

Mean activity coefficients are needed for any equilibrium involving ions: solubility of salts in crystallisers, pH and buffer calculations, electrochemical cells, and protein precipitation by salting out in downstream bioprocessing, where ionic strength controls protein solubility.

## Summary

Individual ion activities are not measurable, so salts are described by a mean activity coefficient $`\gamma_{\pm}`$ with $`a_{\mathrm{M}_p\mathrm{A}_q} = (\gamma_{\pm}m_{\pm}/m^{\circ})^{p+q}`$, where $`m_{\pm}=(m_+^p m_-^q)^{1/(p+q)}`$. The ionic atmosphere lowers $`\gamma_{\pm}`$ in proportion to $`|z_+z_-|\sqrt{I}`$ (Debye–Hückel). This is exact as $`I\to 0`$, needs a size correction above about 0.01 mol kg⁻¹, and becomes empirical beyond about 0.1.

## Conclusion

Solutes use a molality-scale, infinitely-dilute standard state, and electrolytes add a mean ionic activity coefficient that falls as $`\sqrt{I}`$ in dilute solution. Debye–Hückel is exact as the ionic strength tends to zero, needs a size correction above about 0.01 mol kg⁻¹ and becomes empirical beyond about 0.1. The next part returns to non-electrolytes whose deviations are so strong that the liquids refuse to mix.
<!-- note-content:end -->

[Previous](<ET-34 - Dissolved solids and the molality standard state.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)
