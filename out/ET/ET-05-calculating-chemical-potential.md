# Section 05: Calculating the chemical potential

## Overview

Phase equilibrium needs $\mu_i$ in every phase. This note builds $\mu_i$ up in order of difficulty: pure ideal gas, ideal-gas mixture, ideal mixture (the definition behind Raoult's law), and finally real fluids, using an equation of state. The last case gives a **real-fluid correction integral**: the departure of $\mu_i$ from the ideal-gas mixture value. It also shows why the EOS route only works for "easy" mixtures, and why real liquid mixtures need the activity-coefficient approach developed later.

*Assumed:* $\mu_i = (\partial G/\partial n_i)_{T,P,n_j}$; $G = \sum n_i\mu_i$ (Section 04); $(\partial\underline{G}/\partial P)_T = \underline{V}$; departure integrals from $P = 0$ (Section 02).

*Notation:* $P^{\circ}$ is a reference pressure. $\underline{G}_i^{\circ}(T)$ is the molar Gibbs energy of pure $i$ **as an ideal gas** at $T$ and $P^{\circ}$. $\underline{G}_i(T,P)$ is that of real pure $i$ at $T$, $P$ in the phase of interest. $x_i$ is the mole fraction in whichever phase is being described.

## Intuition

For an ideal gas the only thing that changes $\mu$ is how crowded the molecules are, i.e. the pressure, entering through $RT\ln P$. In a mixture of ideal gases the molecules ignore each other, so each component behaves as if it were alone at its own partial pressure. Mixing then only adds entropy, through the $RT\ln x_i$ term.

An **ideal mixture** of liquids takes that entropy term and nothing else: the molecules are assumed to interact with each other exactly as they do with their own kind. So mixing changes neither volume nor enthalpy. Any real deviation, such as the 3 % contraction of whiskey, means unlike molecules interact differently, and $\mu_i$ needs a correction.

## Derivation

**Step 1: pure ideal gas.** At constant $T$, $d\underline{G} = \underline{V}\,dP = (RT/P)\,dP$. Integrating from $P^{\circ}$:

$$\mu_i = \underline{G}_i = \underline{G}_i^{\circ}(T) + RT\ln\frac{P}{P^{\circ}} \tag{1}$$

**Step 2: ideal-gas mixture.** Ideal-gas molecules do not interact, so component $i$ has the same $\mu_i$ as if it occupied the volume alone at its partial pressure $P_i = x_iP$:

$$\mu_i = \underline{G}_i^{\circ}(T) + RT\ln\frac{x_iP}{P^{\circ}} = \underline{G}_i^{\mathrm{IG}}(T,P) + RT\ln x_i \tag{2}$$

where $\underline{G}_i^{\mathrm{IG}}(T,P)$ is pure ideal-gas $i$ at the mixture's $T$ and $P$, from (1). Summing with $\underline{G} = \sum x_i\mu_i$:

$$\underline{G} = \sum_i x_i\,\underline{G}_i^{\mathrm{IG}}(T,P) + RT\sum_i x_i\ln x_i \tag{3}$$

The second term is the Gibbs energy of mixing. It is always negative because every $x_i < 1$, and it does not depend on $P$.

**Step 3: ideal mixture (definition).** Define an ideal mixture (IM) as any mixture, liquid or gas, whose *mixing* behaviour copies (2) and (3), but with **real pure-component** Gibbs energies:

$$\mu_i^{\mathrm{IM}} = \underline{G}_i(T,P) + RT\ln x_i, \qquad \underline{G}^{\mathrm{IM}} = \sum_i x_i\underline{G}_i + RT\sum_i x_i\ln x_i \tag{4}$$

**Step 4: consequences for volume (cross-derivative).** The partial molar volume follows from $\mu_i$ through mixed second derivatives of $G$:

$$\left(\frac{\partial\mu_i}{\partial P}\right)_{T,n} = \frac{\partial}{\partial P}\left(\frac{\partial G}{\partial n_i}\right) = \frac{\partial}{\partial n_i}\left(\frac{\partial G}{\partial P}\right) = \left(\frac{\partial V}{\partial n_i}\right)_{T,P,n_{j\neq i}} = \bar V_i \tag{5}$$

*Reason:* the order of differentiation does not matter for a smooth function, and $(\partial G/\partial P)_{T,n} = V$.

Apply (5) to (4). At fixed composition, $RT\ln x_i$ does not depend on $P$, so $\bar V_i^{\mathrm{IM}} = (\partial\underline{G}_i/\partial P)_T = \underline{V}_i$. An ideal mixture therefore has **no volume change on mixing**. In the same way, the Gibbs–Helmholtz relation gives $\bar H_i^{\mathrm{IM}} = \underline{H}_i$, so there is no heat of mixing either.

**Step 5: real pure substance from an EOS.** Integrate $d\underline{G}_i = \underline{V}_i\,dP$ along the real isotherm:

$$\mu_i = \underline{G}_i(T,P) = \underline{G}_i(T,P^{\circ}) + \int_{P^{\circ}}^{P}\underline{V}_i\,dP \tag{6}$$

This still needs $\underline{G}_i(T,P^{\circ})$ for the *real* fluid. To tie it to the tabulated ideal-gas value, extend the integral down to $P\to 0$, where the fluid becomes ideal (Step 7).

**Step 6: real mixture from an EOS.** Integrate (5) along the isotherm at fixed composition:

$$\mu_i(T,P) = \mu_i(T,P^{\ast}) + \int_{P^{\ast}}^{P}\bar V_i\,dP \tag{7}$$

Here $\bar V_i$ comes from a mixture EOS as a function of $T$, $P$ and composition.

**Step 7: anchor at zero pressure (the real-fluid correction).** Write (7) for the real mixture, and the same equation for the ideal-gas mixture of the same composition, for which $\bar V_i = RT/P$. Subtract the two. As $P^{\ast}\to 0$ the real mixture becomes an ideal-gas mixture, so $\mu_i - \mu_i^{\mathrm{IG}}\to 0$ at the lower limit. Then add (2):

$$\mu_i(T,P) = \underline{G}_i^{\circ}(T) + RT\ln\frac{x_iP}{P^{\circ}} + \int_{0}^{P}\left(\bar V_i - \frac{RT}{P}\right)dP \tag{8}$$

The first two terms are the ideal-gas-mixture value. The integral is the real-fluid correction. It is finite because $\bar V_i - RT/P$ stays bounded as $P\to 0$.

## Motivation and explanation

**Why $RT\ln x_i$ survives at zero pressure.** Taking the real mixture down to $P = 0$ removes the *interactions*, but it does not unmix the components. The $RT\ln x_i$ term in (8) is the ideal entropy of mixing, which is present even for ideal gases. Section 02's pure-fluid departures had no such term. Forgetting it is a common error.

**Limiting cases.**
- (8) with $\bar V_i = RT/P$: the integral vanishes and (2) is recovered.
- (4) with $x_i = 1$: $\mu_i = \underline{G}_i$, the pure-component value.
- (2) and (4) as $x_i\to 0$: $\mu_i\to-\infty$. This is the logarithmic behaviour that later motivates working with fugacity instead of $\mu$.

**When each approach fails.**
- Equation (8) is exact, but only as good as the mixture EOS that supplies $\bar V_i$. Cubic EOS with simple mixing rules work for "easy" mixtures: gases, homologous series (e.g. alkanes) and isomers.
- They fail for liquid mixtures of chemically different molecules (polar, hydrogen-bonding or associating), where the EOS cannot capture the specific interactions.
- The ideal mixture (4) fails whenever unlike interactions differ from like ones. Real liquid mixtures are therefore handled by writing $\mu_i = \mu_i^{\mathrm{IM}} + $ (a correction), the activity-coefficient approach developed later.

## Worked example

**Problem.** (a) Find the ideal Gibbs energy of mixing for the whiskey of Sections 03–04 ($x_{\mathrm{EtOH}} = 0.17$, 29.08 mol in total) at 20 °C. (b) Use Step 4 to test whether ethanol–water is an ideal mixture.

**(a) Ideal Gibbs energy of mixing.** From (4), per mole of mixture:

$$\Delta\underline{G}_{\mathrm{mix}}^{\mathrm{IM}} = RT\left[x_1\ln x_1 + x_2\ln x_2\right] = 8.314\times293.15\times\left[0.17\ln0.17 + 0.83\ln0.83\right] = -1111\ \text{J mol}^{-1}$$

For the 29.08 mol in the bottle, that is −32.3 kJ. Mixing is strongly spontaneous even with no energetic preference at all, purely from entropy.

**(b) Ideality test.** If the mixture were ideal, Step 4 says $\bar V_i = \underline{V}_i$, so the bottle's contents would occupy $\sum n_i\underline{V}_i = 721$ cm³. They actually occupy 700 cm³, so the volume of mixing is −21 cm³ in total, or −0.73 cm³ per mole of mixture. Since $\Delta\underline{V}_{\mathrm{mix}} \neq 0$, the partial molar volumes differ from the pure ones. By (5), $\mu_i$ must then have a pressure-dependent part beyond (4). **Ethanol–water is not an ideal mixture.** Its real Gibbs energy of mixing differs from −1111 J mol⁻¹, and finding by how much is the job of activity-coefficient models.

## Link to other topics

The correction integral in (8) reappears as the fugacity coefficient: dividing by $RT$, the integral is $\ln\bar\phi_i$, which turns the chemical potential into a "corrected partial pressure". The ideal mixture (4), combined with an ideal-gas vapour, gives Raoult's law, and deviations from it are measured by activity coefficients.

## Conclusion

The chemical potential follows from (1) for a pure ideal gas, (2) for an ideal-gas mixture and (4) for an ideal mixture. Real fluids add the correction integral of (8), which needs partial molar volumes from a mixture EOS. That works only for simple mixtures, so the course next recasts $\mu$ in a more convenient variable, fugacity, starting with the simplest real case: a pure liquid under an inert gas.
