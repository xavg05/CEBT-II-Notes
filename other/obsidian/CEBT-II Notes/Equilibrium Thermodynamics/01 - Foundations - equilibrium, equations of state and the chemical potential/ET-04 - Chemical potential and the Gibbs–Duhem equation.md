[Previous](<ET-03 - Partial molar properties.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-05 - Calculating the chemical potential.md>)

<!-- note-content:start -->
# Section 04: Chemical potential and the Gibbs–Duhem equation

## Intuition

Section 03 showed that partial molar volumes are shares of a total and that the shares depend on the environment. If one component's share grows as the composition changes, the other's must shrink to keep the books balanced. The Gibbs–Duhem equation states this exactly.

For the Gibbs energy it has a sharp physical meaning. In a binary at fixed $T$ and $P$, you cannot raise the escaping tendency of both components at once by changing the composition. Whatever makes component 1 "happier" in the mixture must make component 2 less so, in proportion to how much of each is present.

*Analogy: a seesaw with the fulcrum at the composition.* The mole fractions are the lever arms. A small change in $\mu_1$ on the long arm must be balanced by a larger change in $\mu_2$ on the short arm. The analogy breaks down because a seesaw balances forces at one instant, while Gibbs–Duhem is a relation between *changes*, $d\mu_i$, along a path of compositions. It says nothing about the absolute values of $\mu_i$.

## Derivation

**Step 1: chemical potential as a partial molar property.** By definition

$$\mu_i = \left(\frac{\partial G}{\partial n_i}\right)_{T,P,n_{j\neq i}} \equiv \bar G_i \tag{14}$$

so Euler's theorem (Section 03, applied to $G$ at fixed $T$, $P$) gives

$$G = \sum_i n_i\,\mu_i, \qquad \underline{G} = \sum_i x_i\,\mu_i \tag{15}$$

**Step 2: differentiate (15).** By the product rule, for any change:

$$dG = \sum_i n_i\,d\mu_i + \sum_i \mu_i\,dn_i$$

**Step 3: compare with the fundamental relation.** For an open phase, $dG = -S\,dT + V\,dP + \sum_i\mu_i\,dn_i$. Subtracting from Step 2, the $\mu_i\,dn_i$ terms cancel:

$$\sum_i n_i\,d\mu_i = -S\,dT + V\,dP \tag{16}$$

**Step 4: constant $T$ and $P$.**

$$\sum_i n_i\,d\mu_i = 0 \qquad\Longleftrightarrow\qquad \sum_i x_i\,d\mu_i = 0 \qquad (\text{constant } T, P) \tag{17}$$

This is the Gibbs–Duhem equation. Dividing by $n$ gives the mole-fraction form.

The cancellation has a useful meaning. Changing amounts already contributes $\sum_i\mu_i\,dn_i$ to $dG$ through the fundamental relation. Differentiating $G=\sum_i n_i\mu_i$ appears to add a second contribution because the chemical potentials also change. At fixed $T$ and $P$, that extra weighted contribution must cancel. Gibbs–Duhem prevents the same change in mixture Gibbs energy from being counted twice.

It constrains slopes along a composition change, not the signs of departures from the pure liquids. Both partial molar volumes can therefore be below their pure values in the bottle example, even though their composition derivatives have opposite signs. Recovering one component's curve from the other also needs a reference value, normally the known pure-component endpoint, to fix the integration constant.

**Step 5: the same holds for any partial molar property.** Repeat Steps 2–4 with $V$. Since $(\partial V/\partial n_i)$ already defines $\bar V_i$, and at constant $T$, $P$ we have $dV = \sum\bar V_i\,dn_i$:

$$\sum_i x_i\,d\bar V_i = 0 \qquad (\text{constant } T, P) \tag{18}$$

**Step 6: binary form.** With $x_2 = 1 - x_1$, divide (18) by $dx_1$:

$$x_1\,\frac{d\bar V_1}{dx_1} + x_2\,\frac{d\bar V_2}{dx_1} = 0 \tag{19}$$

The two slopes have opposite signs, and their magnitudes are in the inverse ratio of the mole fractions.

## Motivation and explanation

**Building a consistent property model.** The pair
$$\bar V_1=\underline V_1+Ax_2^2,\qquad\bar V_2=\underline V_2+Ax_1^2$$
comes from the single excess-volume function $\underline V^E=Ax_1x_2$. Differentiating with $x_2=1-x_1$ gives $d\bar V_1/dx_1=-2Ax_2$ and $d\bar V_2/dx_1=2Ax_1$, so the Gibbs–Duhem combination cancels exactly. This demonstrates why fitting both component properties through one extensive-property model enforces consistency automatically.
For the ethanol–water graph estimates, fitting $\bar V_1\approx54.7$ at $x_1=0.17$ with $\underline V_1=58$ gives $A\approx-4.79\ \mathrm{cm^3\,mol^{-1}}$. With $\underline V_2=18$, the other component is then predicted to have $\bar V_2\approx17.86\ \mathrm{cm^3\,mol^{-1}}$, close to the graph estimate 17.8. The corresponding infinite-dilution predictions are 53.2 and $13.2\ \mathrm{cm^3\,mol^{-1}}$, against graph estimates of about 52.6 and 14.3. Consistency does not ensure accuracy: a symmetric parameter cannot reproduce both asymmetric endpoints, motivating a more flexible model.

**Why it matters.** Equation (15) says the mixture Gibbs energy is fully determined by the chemical potentials. So the whole problem of phase equilibrium reduces to finding the $\mu_i$. Equation (17) says those $\mu_i$ are not independent.
- In a binary, measuring or modelling one component's $\mu$ against composition gives the other's by integration.
- Experimental data for both components can be checked for consistency with (17); data that violate it contain errors.
- Any model for $\mu_i$ must satisfy it. Later sections build models from a single function, the excess Gibbs energy, precisely so that this is automatic.

**Reading the graph in Section 03.** In dilute ethanol ($x_{\mathrm{EtOH}}$ small), (19) says water's partial molar volume barely changes, because its slope is multiplied by the small $x_{\mathrm{EtOH}}/x_{\mathrm{H_2O}}$. Meanwhile ethanol's changes steeply. Both features are visible on the curves near $x_{\mathrm{EtOH}} = 0$: water's curve is flat and ethanol's is steep.

**What is held constant.** Equations (17)–(19) require constant $T$ and $P$. If $T$ or $P$ vary, the full form (16) applies.

## Link to other topics

The binary Gibbs–Duhem equation applied to $\mu_i = \mu_i^{\mathrm{ideal}} + RT\ln\gamma_i$ becomes $x_1\,d\ln\gamma_1 + x_2\,d\ln\gamma_2 = 0$. That is the constraint behind the Margules and van Laar models and behind consistency tests of vapour–liquid equilibrium data. Equation (16) with the composition terms removed is also the basis of the Gibbs phase rule, which counts how many intensive variables are free.

## Summary

The chemical potential is the partial molar Gibbs energy. The mixture's Gibbs energy is the mole-fraction-weighted sum of the chemical potentials, and at fixed $T$ and $P$ their changes are tied together by Gibbs–Duhem. In a binary, knowing one gives the other, as the ethanol–water volumes show.
<!-- note-content:end -->

[Previous](<ET-03 - Partial molar properties.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-05 - Calculating the chemical potential.md>)
