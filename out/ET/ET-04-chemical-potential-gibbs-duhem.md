# Section 04: Chemical potential and the Gibbs–Duhem equation

## Overview

The chemical potential that decides phase equilibrium is the partial molar Gibbs energy. Treating it as a partial molar property gives two results.
1. $G = \sum n_i\mu_i$: if each $\mu_i$ is known in each phase, the equilibrium position follows.
2. The **Gibbs–Duhem equation**: the chemical potentials in a mixture cannot change independently. In a binary, knowing one fixes the other.

This constraint is what every activity-coefficient model must obey later in the course. Here it is checked on the ethanol–water partial molar volumes.

*Assumed:* $dG = -S\,dT + V\,dP + \sum\mu_i\,dn_i$ and the criterion $\mu_i^L = \mu_i^V$ (Section 01); partial molar properties and Euler's theorem (Section 03).

## Intuition

Section 03 showed that partial molar volumes are shares of a total and that the shares depend on the environment. If one component's share grows as the composition changes, the other's must shrink to keep the books balanced. The Gibbs–Duhem equation states this exactly.

For the Gibbs energy it has a sharp physical meaning. In a binary at fixed $T$ and $P$, you cannot raise the escaping tendency of both components at once by changing the composition. Whatever makes component 1 "happier" in the mixture must make component 2 less so, in proportion to how much of each is present.

*Analogy: a seesaw with the fulcrum at the composition.* The mole fractions are the lever arms. A small change in $\mu_1$ on the long arm must be balanced by a larger change in $\mu_2$ on the short arm. The analogy breaks down because a seesaw balances forces at one instant, while Gibbs–Duhem is a relation between *changes*, $d\mu_i$, along a path of compositions. It says nothing about the absolute values of $\mu_i$.

## Derivation

**Step 1: chemical potential as a partial molar property.** By definition

$$\mu_i = \left(\frac{\partial G}{\partial n_i}\right)_{T,P,n_{j\neq i}} \equiv \bar G_i \tag{1}$$

so Euler's theorem (Section 03, applied to $G$ at fixed $T$, $P$) gives

$$G = \sum_i n_i\,\mu_i, \qquad \underline{G} = \sum_i x_i\,\mu_i \tag{2}$$

**Step 2: differentiate (2).** By the product rule, for any change:

$$dG = \sum_i n_i\,d\mu_i + \sum_i \mu_i\,dn_i$$

**Step 3: compare with the fundamental relation.** For an open phase, $dG = -S\,dT + V\,dP + \sum_i\mu_i\,dn_i$. Subtracting from Step 2, the $\mu_i\,dn_i$ terms cancel:

$$\sum_i n_i\,d\mu_i = -S\,dT + V\,dP \tag{3}$$

**Step 4: constant $T$ and $P$.**

$$\sum_i n_i\,d\mu_i = 0 \qquad\Longleftrightarrow\qquad \sum_i x_i\,d\mu_i = 0 \qquad (\text{constant } T, P) \tag{4}$$

This is the Gibbs–Duhem equation. Dividing by $n$ gives the mole-fraction form.

**Step 5: the same holds for any partial molar property.** Repeat Steps 2–4 with $V$. Since $(\partial V/\partial n_i)$ already defines $\bar V_i$, and at constant $T$, $P$ we have $dV = \sum\bar V_i\,dn_i$:

$$\sum_i x_i\,d\bar V_i = 0 \qquad (\text{constant } T, P) \tag{5}$$

**Step 6: binary form.** With $x_2 = 1 - x_1$, divide (5) by $dx_1$:

$$x_1\,\frac{d\bar V_1}{dx_1} + x_2\,\frac{d\bar V_2}{dx_1} = 0 \tag{6}$$

The two slopes have opposite signs, and their magnitudes are in the inverse ratio of the mole fractions.

## Motivation and explanation

**Why it matters.** Equation (2) says the mixture Gibbs energy is fully determined by the chemical potentials. So the whole problem of phase equilibrium reduces to finding the $\mu_i$. Equation (4) says those $\mu_i$ are not independent.
- In a binary, measuring or modelling one component's $\mu$ against composition gives the other's by integration.
- Experimental data for both components can be checked for consistency with (4); data that violate it contain errors.
- Any model for $\mu_i$ must satisfy it. Later sections build models from a single function, the excess Gibbs energy, precisely so that this is automatic.

**Reading the graph in Section 03.** In dilute ethanol ($x_{\mathrm{EtOH}}$ small), (6) says water's partial molar volume barely changes, because its slope is multiplied by the small $x_{\mathrm{EtOH}}/x_{\mathrm{H_2O}}$. Meanwhile ethanol's changes steeply. Both features are visible on the curves near $x_{\mathrm{EtOH}} = 0$: water's curve is flat and ethanol's is steep.

**What is held constant.** Equations (4)–(6) require constant $T$ and $P$. If $T$ or $P$ vary, the full form (3) applies.

## Worked example

**Problem.** Use a one-parameter model for the ethanol (1)–water (2) partial molar volumes,
$$\bar V_1 = \underline{V}_1 + A\,x_2^2, \qquad \bar V_2 = \underline{V}_2 + A\,x_1^2,$$
with $\underline{V}_1 = 58$ and $\underline{V}_2 = 18$ cm³ mol⁻¹. (a) Show that it obeys Gibbs–Duhem. (b) Fit $A$ to $\bar V_1 \approx 54.7$ cm³ mol⁻¹ at $x_1 = 0.17$, predict $\bar V_2$ there, and compare with the graph value of ≈17.8 cm³ mol⁻¹. (c) Test the model at the two ends of the composition range.

**(a) Consistency.** $d\bar V_1/dx_1 = -2Ax_2$ and $d\bar V_2/dx_1 = 2Ax_1$. Substitute into (6):
$$x_1(-2Ax_2) + x_2(2Ax_1) = 0$$
so it is satisfied at every composition. This model corresponds to an excess volume $\underline{V}^E = Ax_1x_2$, i.e. $\underline{V} = x_1\underline{V}_1 + x_2\underline{V}_2 + Ax_1x_2$. Differentiating that, as in Section 03, returns the expressions above.

**(b) Fit and predict.** $A = (54.7 - 58)/0.83^2 = -4.79$ cm³ mol⁻¹. Then
$$\bar V_2 = 18 + (-4.79)(0.17)^2 = 17.86\ \text{cm}^3\,\text{mol}^{-1},$$
against ≈17.8 read from the graph. Gibbs–Duhem has predicted water's partial molar volume from ethanol's alone. As a cross-check, the model's excess volume at $x_1 = 0.17$ is $Ax_1x_2 = -0.68$ cm³ mol⁻¹. For the 29.08 mol in the whiskey bottle that is a contraction of 19.7 cm³, close to the 21 cm³ found in Section 03.

**(c) Limits.**

| Quantity | Model | Graph |
|---|---|---|
| Ethanol at infinite dilution in water, $\underline{V}_1 + A$ | 53.2 | ≈52.6 |
| Water at infinite dilution in ethanol, $\underline{V}_2 + A$ | 13.2 | ≈14.3 |

A single symmetric parameter cannot reproduce both ends, because the real curves are asymmetric. A two-parameter (asymmetric) model would fix this. The same issue, and the same remedy, comes up with activity-coefficient models.

## Link to other topics

The binary Gibbs–Duhem equation applied to $\mu_i = \mu_i^{\mathrm{ideal}} + RT\ln\gamma_i$ becomes $x_1\,d\ln\gamma_1 + x_2\,d\ln\gamma_2 = 0$. That is the constraint behind the Margules and van Laar models and behind consistency tests of vapour–liquid equilibrium data. Equation (3) with the composition terms removed is also the basis of the Gibbs phase rule, which counts how many intensive variables are free.

## Conclusion

The chemical potential is the partial molar Gibbs energy. The mixture's Gibbs energy is the mole-fraction-weighted sum of the chemical potentials, and at fixed $T$ and $P$ their changes are tied together by Gibbs–Duhem. In a binary, knowing one gives the other, as the ethanol–water volumes show. What remains is to calculate $\mu_i$ itself, first for ideal gases and ideal mixtures, then for real fluids from an equation of state: the subject of the next section.
