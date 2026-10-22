[Previous](<ET-37 - Temperature dependence, consolute points and the vapour–liquid analogy.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-39 - Binodal, spinodal and the stability of a single liquid.md>)

<!-- note-content:start -->
# Section 38: isobutane–furfural liquid–liquid equilibrium

*Components:* isobutane (1), furfural (2).

## Intuition

Furfural is polar (an aldehyde on a furan ring); isobutane is a small, non-polar alkane. Large van Laar constants ($\gamma^{\infty} = e^{2.62}\approx 14$ and $e^{3.02}\approx 20$) say each strongly dislikes the other. We expect two nearly pure phases, each holding only a little of the other component. That is the situation exploited when furfural extracts aromatics from hydrocarbon oils.

## Derivation

**Step 1: equilibrium equations.** With the same pure-liquid reference in both phases, $\mu_i^{\mathrm{I}} = \mu_i^{\mathrm{II}}$ becomes equal activities:

$$x_1^{\mathrm{I}}\gamma_1^{\mathrm{I}} = x_1^{\mathrm{II}}\gamma_1^{\mathrm{II}}, \qquad x_2^{\mathrm{I}}\gamma_2^{\mathrm{I}} = x_2^{\mathrm{II}}\gamma_2^{\mathrm{II}} \tag{156}$$

with van Laar $\ln\gamma_1 = \alpha/[1 + \alpha x_1/(\beta x_2)]^2$ and $\ln\gamma_2 = \beta/[1 + \beta x_2/(\alpha x_1)]^2$.

**Step 2: solve.** At 37.8 °C use $\alpha=2.62$ and $\beta=3.02$ (dimensionless). Solve the two non-linear equations for two distinct compositions, $x_1^{\mathrm{I}}<x_1^{\mathrm{II}}$; the trivial equal-composition root is not a phase split. Equivalently, find the common tangent to
$$\frac{\Delta\underline{G}_{\mathrm{mix}}}{RT} = \sum_i x_i\ln x_i + \sum_i x_i\ln\gamma_i.$$

**Step 3: spinodals.** Where $d^2(\Delta\underline{G}_{\mathrm{mix}}/RT)/dx_1^2 = 0$, located numerically.

## Motivation and explanation

**Equal activities through compensation.** Solving the stated van Laar model gives a furfural-rich liquid at $x_1\approx0.1128$ and an isobutane-rich liquid at $x_1\approx0.9284$. Isobutane's activity coefficients are about 8.375 and 1.018, respectively. Their products $x_1\gamma_1$ are equal to about 0.945: the large dilute-phase coefficient compensates for its small mole fraction. Furfural satisfies the same compensation. Equal chemical potentials therefore coexist with very unequal concentrations.
The equimolar feed splits into approximately 52.5 % furfural-rich and 47.5 % isobutane-rich liquid by the lever rule. At fixed temperature and pressure, moving the overall composition within the gap changes these fractions, not the two equilibrium endpoints. The spinodals near 0.270 and 0.805 and the minima near 0.107 and 0.924 are distinct from those endpoints; this asymmetric curve needs a tilted common tangent.
![Isobutane–furfural mixing Gibbs energy: the common tangent touches at the coexistence compositions, while crosses mark the separate spinodal boundaries](../figs/ET-38-isobutane-furfural-Gmix.png)

**Why the tangent points are not the minima.** The model is asymmetric ($\beta > \alpha$), so the common tangent is tilted. A tilted line touches each dip slightly off its lowest point. Only for a symmetric curve is the tangent horizontal, with tangent points at the minima.

**Reading the activity coefficients.**
- The dilute component in each phase has a large $\gamma$ (8.4 for isobutane in furfural, 12.8 for furfural in isobutane), while the major component has $\gamma\approx 1$. This is the Gibbs–Duhem behaviour of Section 11 seen in practice.
- *A quick estimate.* From (156), $\gamma_1^{\mathrm{I}}\approx x_1^{\mathrm{II}}/x_1^{\mathrm{I}}$ when $\gamma_1^{\mathrm{II}}\approx 1$: $0.9284/0.1128 = 8.23$, against the exact 8.375. The solubility of a component in the "wrong" phase is roughly $1/\gamma$ in that phase.

**Assumptions.** The van Laar constants are taken as valid at 37.8 °C (they depend on $T$). Pressure (5 bar, to keep isobutane liquid) has negligible effect on liquid-phase activities (Section 10).

## Link to other topics

Equation (156) with a solute added is the basis of distribution coefficients in liquid–liquid extraction. A solute's partition between two solvents equals the ratio of its activity coefficients in them.

## Summary

Solving equal-activity conditions with van Laar gives coexisting liquids at $x_1 = 0.1128$ and 0.9284, with spinodals at 0.270 and 0.805. The minor component in each phase has a large activity coefficient, approximately the ratio of its mole fractions in the two phases.
<!-- note-content:end -->

[Previous](<ET-37 - Temperature dependence, consolute points and the vapour–liquid analogy.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-39 - Binodal, spinodal and the stability of a single liquid.md>)
