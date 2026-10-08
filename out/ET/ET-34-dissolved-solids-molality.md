# Section 34: Dissolved solids and the molality standard state

## Overview

A dissolved solid (sugar, a drug, a protein) has no pure-liquid state at the solution's temperature. Like a supercritical gas, it therefore needs a different reference. The convention for solutes is to measure activity relative to an **ideal dilute solution at unit molality**, with activity coefficient $\gamma_i^{\#}\to 1$ at infinite dilution. This note:
- builds that convention;
- relates it to the pure-liquid ($\gamma_i$) and Henry ($\gamma_i^{*}$) conventions;
- stresses the one rule that keeps them straight: always know which standard state you are using.

*Assumed:* $\mu_i = \underline{G}_i + RT\ln(\gamma_ix_i)$ (Section 10); Henry's law and $\gamma_i^{*}$ (Section 31).

*Notation:* $m_i$ is the molality of solute $i$ (mol per kg of solvent). $\gamma_i^{\#}$ is the molality-scale activity coefficient and $a_i^{\#} = \gamma_i^{\#}m_i$ the molality-scale activity. $\mu_i^{\circ}$ is the standard chemical potential on this scale.

## Intuition

For a solute, the natural "ideal" behaviour is the dilute one: each molecule is surrounded only by solvent, so its escaping tendency is proportional to its concentration (Henry-like). Molality is used rather than mole fraction because it is easy to make up by weighing, and it does not change with temperature (unlike molarity, which changes as the solution expands).

The standard state is then: *the solute at 1 mol kg⁻¹, but behaving as if it were still infinitely dilute.* It is reached by extending the dilute straight line to $m = 1$, so it is hypothetical. A real 1 mol kg⁻¹ solution is generally not ideal.

## Derivation

**Step 1: the definition.**

$$\mu_i = \mu_i^{\circ} + RT\ln\left(\gamma_i^{\#}\,\frac{m_i}{m^{\circ}}\right), \qquad \gamma_i^{\#}\to 1 \text{ as } m_i\to 0 \tag{1}$$

with $m^{\circ} = 1$ mol kg⁻¹, so the logarithm's argument is dimensionless. $\mu_i^{\circ}$ is the chemical potential the solute would have at unit molality if it stayed ideally dilute.

**Step 2: link to mole fraction.** For solvent of molar mass $M_s$, $x_i = m_iM_s/(1 + \sum_jm_jM_s)$, so in the dilute limit $x_i\approx M_sm_i$. Dilute ideality in molality is therefore the same physics as Henry's law: $\bar f_i\propto x_i\propto m_i$.

**Step 3: relation between conventions.** The same chemical potential written in two conventions must agree. Equating (1) with the Henry form $\mu_i = \mu_i^{*} + RT\ln(\gamma_i^{*}x_i)$ shows that $\gamma_i^{\#}$ and $\gamma_i^{*}$ differ only by the factor $x_i/(M_sm_i) = 1/(1 + \sum_jm_jM_s)$, which tends to 1 in dilute solution. Both are normalised at infinite dilution. The pure-liquid $\gamma_i$ is normalised at the opposite end:

| Symbol | Standard state | $\to 1$ when |
|---|---|---|
| $\gamma_i$ | pure liquid $i$ at $T$, $P$ | $x_i\to 1$ |
| $\gamma_i^{*}$ | Henry's constant (extrapolated from $x_i\to 0$ to $x_i = 1$) | $x_i\to 0$ |
| $\gamma_i^{\#}$ | ideal dilute solute at 1 mol kg⁻¹ | $m_i\to 0$ |

![Molality standard state: the real activity curve follows the ideal dilute line at low m; the standard state is the point at m = 1 on the extrapolated ideal line](figs/ET-34-molality-standard-state.png)

## Motivation and explanation

**Why change standard state again?** Only convenience, but it is decisive. A pure-liquid reference for sucrose or NaCl at 25 °C would need properties of a supercooled melt, far from anything measurable. The dilute reference uses only measurements on solutions. Equilibrium constants for reactions in solution (acid dissociation, solubility products) are tabulated on this scale.

**Getting answers right.** Chemical potentials and fugacities are physical, so they do not depend on the convention. The *numbers* $\gamma$, $a$ and $\mu^{\circ}$ do depend on it, and must not be mixed: an equilibrium constant defined with molality activities must be used with $\gamma^{\#}$, not $\gamma$.

**Limits.** At high concentrations the dilute reference is far from the real state, and $\gamma^{\#}$ can depart greatly from 1. For electrolytes the dilute region itself is very narrow, because charged ions interact over long distances. That is the subject of the next section.

## Worked example

**Problem.** For a 0.5 mol kg⁻¹ aqueous solution of an ideal non-electrolyte at 25 °C, find the solute mole fraction and compare the molality-scale and mole-fraction ideal activities. Then express the solvent's activity, which is used with the pure-liquid convention.

**Mole fraction.** $x_i = 0.5\times0.018015/(1 + 0.5\times0.018015) = 8.93\times10^{-3}$, against the dilute approximation $M_sm_i = 9.01\times10^{-3}$. The two differ by 0.9 %, the factor $1/(1 + m_iM_s)$.

**Solute.** "Ideal" on the molality scale means $\gamma^{\#} = 1$, so $a^{\#} = 0.5$. On the Henry mole-fraction scale, the same ideal solution has $a^{*} = x_i = 8.93\times10^{-3}$, again with $\gamma^{*} = 1$. The activities differ by a constant factor $1/M_s = 55.5$ mol kg⁻¹ (plus the 0.9 % dilution correction). That factor is absorbed into the different standard chemical potentials, so $\mu_i$ itself is the same.

**Solvent.** Water stays on the pure-liquid scale: $a_{\mathrm{w}} = x_{\mathrm{w}} = 0.9911$ (ideal). This is the quantity that sets freezing-point depression and osmotic pressure (Sections 15 and 22).

**Interpretation.** In a solution, solvent and solute naturally use *different* conventions (pure liquid for the solvent, dilute solute for the solute), and both are consistent through Gibbs–Duhem. The size of "activity" depends entirely on the scale chosen. That is why the standard state must always be stated.

## Link to other topics

The molality scale is used for all aqueous chemistry: pH, buffer design, solubility products in crystallisation, and the protein-solubility (salting-out) behaviour met in bioprocessing. Next, ionic solutes introduce mean activity coefficients and Debye–Hückel theory.

## Conclusion

Dissolved solids are referred to a hypothetical ideal-dilute solution at 1 mol kg⁻¹, giving $\mu_i = \mu_i^{\circ} + RT\ln(\gamma_i^{\#}m_i)$ with $\gamma_i^{\#}\to 1$ at infinite dilution. This is essentially Henry's convention on a molality scale. Three conventions ($\gamma$, $\gamma^{*}$, $\gamma^{\#}$) are now in use, and correct calculations depend only on applying each one consistently with its own standard state. The next section applies this to salts, which dissociate into ions whose individual activities cannot be measured.
