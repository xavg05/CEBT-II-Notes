# Solutes and electrolytes

## Overview

Dissolved solids have no pure-liquid state at the solution temperature, so their activity is referred to a hypothetical ideal-dilute solution at 1 mol kg⁻¹, with $\gamma^{\#}\to 1$ at infinite dilution; the key rule is to know which of the three conventions ($\gamma$, $\gamma^{*}$, $\gamma^{\#}$) is in use (Section 34). Salts dissociate into ions whose individual activities cannot be measured, so they are described by a mean ionic activity coefficient, lowered by the ionic atmosphere according to the Debye–Hückel law (Section 35).

*Assumed throughout:* activity coefficients and Henry's convention (Sections 10 and 31); Coulomb's law.

## Section 34: Dissolved solids and the molality standard state

*Notation:* $m_i$ is the molality of solute $i$ (mol per kg of solvent), $m^{\circ}=1$ mol kg⁻¹ is the standard molality, and $M_s$ is the solvent molar mass in kg mol⁻¹. $\gamma_i^{\#}$ is the molality-scale activity coefficient and $a_i^{\#}=\gamma_i^{\#}m_i/m^{\circ}$ the dimensionless molality-scale activity. $\mu_i^{\circ}$ is the standard chemical potential on this scale.

### Intuition

For a solute, the natural "ideal" behaviour is the dilute one: each molecule is surrounded only by solvent, so its escaping tendency is proportional to its concentration (Henry-like). Molality is used rather than mole fraction because it is easy to make up by weighing, and it does not change with temperature (unlike molarity, which changes as the solution expands).

The standard state is then: *the solute at 1 mol kg⁻¹, but behaving as if it were still infinitely dilute.* It is reached by extending the dilute straight line to $m = 1$, so it is hypothetical. A real 1 mol kg⁻¹ solution is generally not ideal.

### Derivation

**Step 1: the definition.**

$$\mu_i = \mu_i^{\circ} + RT\ln\left(\gamma_i^{\#}\,\frac{m_i}{m^{\circ}}\right), \qquad \gamma_i^{\#}\to 1 \text{ as } m_i\to 0 \tag{147}$$

with $m^{\circ} = 1$ mol kg⁻¹, so the logarithm's argument is dimensionless. $\mu_i^{\circ}$ is the chemical potential the solute would have at unit molality if it stayed ideally dilute.

**Step 2: link to mole fraction.** For solvent of molar mass $M_s$, $x_i = m_iM_s/(1 + \sum_jm_jM_s)$, so in the dilute limit $x_i\approx M_sm_i$. Dilute ideality in molality is therefore the same physics as Henry's law: $\bar f_i\propto x_i\propto m_i$.

**Step 3: relation between conventions.** Equal chemical potentials require $\mu_i^{\circ}=\mu_i^{*}+RT\ln(M_sm^{\circ})$ and $\gamma_i^{\#}=\gamma_i^{*}x_i/(M_sm_i)=\gamma_i^{*}/(1+M_s\sum_jm_j)$. The activity coefficients approach 1 together at infinite dilution, but at a finite molality the same solution cannot have both coefficients exactly 1. The pure-liquid $\gamma_i$ is normalised at the opposite end:

| Symbol | Standard state | $\to 1$ when |
|---|---|---|
| $\gamma_i$ | pure liquid $i$ at $T$, $P$ | $x_i\to 1$ |
| $\gamma_i^{*}$ | Henry's constant (extrapolated from $x_i\to 0$ to $x_i = 1$) | $x_i\to 0$ |
| $\gamma_i^{\#}$ | ideal dilute solute at 1 mol kg⁻¹ | $m_i\to 0$ |

![Molality standard state: the real activity curve follows the ideal dilute line at low m; the standard state is the point at m = 1 on the extrapolated ideal line](figs/ET-34-molality-standard-state.png)

### Motivation and explanation

**Why change standard state again?** Only convenience, but it is decisive. A pure-liquid reference for sucrose or NaCl at 25 °C would need properties of a supercooled melt, far from anything measurable. The dilute reference uses only measurements on solutions. Equilibrium constants for reactions in solution (acid dissociation, solubility products) are tabulated on this scale.

**Getting answers right.** Chemical potentials and fugacities are physical, so they do not depend on the convention. The *numbers* $\gamma$, $a$ and $\mu^{\circ}$ do depend on it, and must not be mixed: an equilibrium constant defined with molality activities must be used with $\gamma^{\#}$, not $\gamma$.

**Limits.** At high concentrations the dilute reference is far from the real state, and $\gamma^{\#}$ can depart greatly from 1. For electrolytes the dilute region itself is very narrow, because charged ions interact over long distances. That is the subject of the next section.

### Worked example

**Problem.** For a 0.5 mol kg⁻¹ aqueous solution of a non-electrolyte that is ideal on the mole-fraction scale at 25 °C ($\gamma^{*}=1$), find the solute mole fraction and compare its Henry and molality activities. Then express the solvent activity on the pure-liquid scale.

**Mole fraction.** $x_i = 0.5\times0.018015/(1 + 0.5\times0.018015) = 8.93\times10^{-3}$, against the dilute approximation $M_sm_i = 9.01\times10^{-3}$. The two differ by 0.9 %, the factor $1/(1 + m_iM_s)$.

**Solute.** On the Henry mole-fraction scale, $a^{*}=x_i=8.93\times10^{-3}$ and $\gamma^{*}=1$. The exact conversion gives $\gamma^{\#}=1/(1+M_sm_i)=0.9911$ and $a^{\#}=\gamma^{\#}m_i/m^{\circ}=0.4955$. Thus $a^{\#}/a^{*}=1/(M_sm^{\circ})=55.51$, a dimensionless constant absorbed into the different standard chemical potentials. The chemical potential itself is unchanged. Setting $\gamma^{\#}=1$ instead would define a different ideal model at this finite concentration.

**Solvent.** Water stays on the pure-liquid scale: $a_{\mathrm{w}} = x_{\mathrm{w}} = 0.9911$ (ideal). This is the quantity that sets freezing-point depression and osmotic pressure (Sections 15 and 22).

**Interpretation.** In a solution, solvent and solute naturally use *different* conventions (pure liquid for the solvent, dilute solute for the solute), and both are consistent through Gibbs–Duhem. The size of "activity" depends entirely on the scale chosen. That is why the standard state must always be stated.

### Link to other topics

The molality scale is used for all aqueous chemistry: pH, buffer design, solubility products in crystallisation, and the protein-solubility (salting-out) behaviour met in bioprocessing. Next, ionic solutes introduce mean activity coefficients and Debye–Hückel theory.

### Summary

Dissolved solids are referred to a hypothetical ideal-dilute solution at 1 mol kg⁻¹, giving $\mu_i = \mu_i^{\circ} + RT\ln(\gamma_i^{\#}m_i/m^{\circ})$ with $\gamma_i^{\#}\to 1$ at infinite dilution. This is essentially Henry's convention on a molality scale. Three conventions ($\gamma$, $\gamma^{*}$, $\gamma^{\#}$) are now in use, and correct calculations depend only on applying each one consistently with its own standard state.

## Section 35: Ionic solutions, mean activity coefficients and Debye–Hückel theory

*Notation:* for a salt $\mathrm{M}_p\mathrm{A}_q\to p\mathrm{M}^{z_+} + q\mathrm{A}^{z_-}$, $m$ is the salt molality, $z_\pm$ are the ion charge numbers, and $I = \tfrac12\sum_i z_i^2m_i$ is the ionic strength. All $\gamma$'s here are on the molality scale; the superscript # is dropped.

### Intuition

Around each positive ion, negative ions are slightly more likely to be found than positive ones, and vice versa. Every ion therefore sits in a diffuse cloud of net opposite charge, its **ionic atmosphere**. The attraction between an ion and its atmosphere lowers the ion's energy, and so its chemical potential, below the ideal value: $\gamma_{\pm} < 1$.

The atmosphere's thickness, the Debye length, shrinks as more ions are added. Denser screening means a closer, stronger stabilising cloud. The effect scales with the square root of concentration, which is why even millimolar salt solutions are measurably non-ideal.

*Analogy: a celebrity in a crowd.* A celebrity draws admirers close, and the crowd's attention lowers their "escaping tendency". The analogy breaks down because the atmosphere is a time-averaged statistical excess of charge, not a fixed group. Every ion is simultaneously the centre of its own cloud and a member of others.

### Derivation

**Step 1: chemical potential of the dissolved salt.** For NaCl,

$$\mu_{\mathrm{NaCl}} = \mu_{\mathrm{Na^+}} + \mu_{\mathrm{Cl^-}} = \mu^{\circ}_{\mathrm{Na^+}} + \mu^{\circ}_{\mathrm{Cl^-}} + RT\ln\left(\gamma_{\mathrm{Na^+}}m_{\mathrm{Na^+}}/m^{\circ}\right) + RT\ln\left(\gamma_{\mathrm{Cl^-}}m_{\mathrm{Cl^-}}/m^{\circ}\right)$$

Adding a single ion type would violate neutrality, so only this *sum* is physically defined.

**Step 2: mean ionic activity coefficient.** With $m_{\mathrm{Na^+}} = m_{\mathrm{Cl^-}} = m$, define the geometric mean $\gamma_{\pm} = (\gamma_{\mathrm{Na^+}}\gamma_{\mathrm{Cl^-}})^{1/2}$. Then

$$\mu_{\mathrm{NaCl}} = \mu^{\circ}_{\mathrm{NaCl}} + RT\ln a_{\mathrm{NaCl}}, \qquad a_{\mathrm{NaCl}} = (\gamma_{\pm}m/m^{\circ})^2 \tag{148}$$

The square reflects two particles per formula unit. Plotted against $m^2$, the ideal-dilute line has unit slope.

**Step 3: general salt.** For $\mathrm{M}_p\mathrm{A}_q$, with $m_+ = pm$ and $m_- = qm$:

$$a_{\mathrm{M}_p\mathrm{A}_q} = a_+^{\,p}a_-^{\,q}, \qquad \gamma_{\pm}^{\,p+q} = \gamma_+^{\,p}\gamma_-^{\,q} \tag{149}$$

**Step 4: Debye–Hückel limiting law.** Treat the ions as point charges in a continuous dielectric. Then:
- solve Poisson's equation for the potential around a central ion, with the surrounding ion densities following Boltzmann distributions;
- linearise for weak potentials;
- compute the electrical work of charging the ion in its atmosphere.

The full derivation is beyond this course. The result is

$$\ln\gamma_{\pm} = -\alpha\,|z_+z_-|\sqrt{I} \tag{150}$$

where $\alpha$ depends only on the solvent's permittivity and the temperature. For water at 25 °C, $\alpha = 1.171$ kg^½ mol^-½. This is often written as $\log_{10}\gamma_{\pm} = -0.509|z_+z_-|\sqrt{I}$.

**Step 5: extended Debye–Hückel.** Giving the ions a finite size $a$, the distance of closest approach, caps how close the atmosphere can get:

$$\ln\gamma_{\pm} = -\frac{\alpha|z_+z_-|\sqrt{I}}{1 + \beta a\sqrt{I}} + \delta I \tag{151}$$

With $\beta = 0.3281$ Å⁻¹ kg^½ mol^-½ in water at 25 °C, and a typical $a$ of a few ångströms. An empirical linear term $\delta I$ is added at higher strengths.

### Motivation and explanation

**Why $\sqrt{I}$ and not $I$.** The atmosphere's size, the Debye length $\kappa^{-1}$, scales as $I^{-1/2}$. The ion–atmosphere energy goes as $1/\kappa^{-1}\propto\sqrt{I}$. This square-root law is a hallmark of long-range forces. Short-range (neutral-molecule) non-idealities start linearly in concentration.

**Why ionic strength.** Screening depends on all ions present, weighted by charge squared. In the dilute Debye–Hückel regime, adding another salt therefore lowers $\gamma_{\pm}$. Screening helps explain salting-in of proteins at low ionic strength. Salting-out at higher salt concentrations also involves hydration and other specific interactions and is beyond the Debye–Hückel limiting law.

**Limits.**
- The limiting law is exact as $I\to 0$ but accurate only below about $I\approx 0.01$ mol kg⁻¹.
- The extended form works to roughly $I\approx 0.1$.
- At higher strengths, real $\gamma_{\pm}$ curves pass through a minimum and rise again (ion hydration, ion pairing), which needs empirical models such as Pitzer's.

### Worked example

**Problem.** At 25 °C, compute $\gamma_{\pm}$ from the limiting law (150) and the extended law (151) (without the $\delta$ term, $a = 3$ Å) for NaCl (1:1) and CaCl₂ (2:1) at $m = 0.001$, 0.01, 0.1 and 0.5 mol kg⁻¹. For CaCl₂, $I = \tfrac12(4m + 2m) = 3m$ and $|z_+z_-| = 2$. Also find the Debye length at $I = 0.001$ and 0.1.

| $m$ (mol kg⁻¹) | NaCl $I$ | NaCl limiting | NaCl extended | CaCl₂ $I$ | CaCl₂ limiting | CaCl₂ extended |
|---|---|---|---|---|---|---|
| 0.001 | 0.001 | 0.964 | 0.965 | 0.003 | 0.880 | 0.885 |
| 0.01 | 0.01 | 0.889 | 0.899 | 0.03 | 0.667 | 0.707 |
| 0.1 | 0.1 | 0.691 | 0.754 | 0.3 | 0.277 | 0.435 |
| 0.5 | 0.5 | 0.437 | 0.614 | 1.5 | 0.057 | 0.272 |

Debye length (water, 25 °C, relative permittivity 78.4): 9.6 nm at $I = 0.001$, 0.96 nm at $I = 0.1$.

**Interpretation.**
- At 0.001 mol kg⁻¹ the two laws agree. Even then, NaCl's activity is 3.6 % below ideal, a non-ideality that a neutral solute would only show at much higher concentration.
- The two laws diverge from about 0.01 mol kg⁻¹ for 1:1 salts. Above 0.1 the limiting law is far too low, and finite ion size, captured by the extended law, matters.
- The doubly charged calcium ion makes CaCl₂ much more non-ideal at the same molality (factor $|z_+z_-| = 2$ and three times the ionic strength).
- At 0.1 mol kg⁻¹ the screening length (≈1 nm) is only a few ion diameters. This is why point-charge theory fails there.

### Link to other topics

Mean activity coefficients are needed for any equilibrium involving ions: solubility of salts in crystallisers, pH and buffer calculations, electrochemical cells, and protein precipitation by salting out in downstream bioprocessing, where ionic strength controls protein solubility.

### Summary

Individual ion activities are not measurable, so salts are described by a mean activity coefficient $\gamma_{\pm}$ with $a_{\mathrm{M}_p\mathrm{A}_q} = (\gamma_{\pm}m_{\pm}/m^{\circ})^{p+q}$, where $m_{\pm}=(m_+^p m_-^q)^{1/(p+q)}$. The ionic atmosphere lowers $\gamma_{\pm}$ in proportion to $|z_+z_-|\sqrt{I}$ (Debye–Hückel). This is exact as $I\to 0$, needs a size correction above about 0.01 mol kg⁻¹, and becomes empirical beyond about 0.1.

## Conclusion

Solutes use a molality-scale, infinitely-dilute standard state, and electrolytes add a mean ionic activity coefficient that falls as $\sqrt{I}$ in dilute solution. Debye–Hückel is exact as the ionic strength tends to zero, needs a size correction above about 0.01 mol kg⁻¹ and becomes empirical beyond about 0.1. The next part returns to non-electrolytes whose deviations are so strong that the liquids refuse to mix.
