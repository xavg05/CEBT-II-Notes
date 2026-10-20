# Apparent kinetics and oxide redox cycles

## Overview

Assume logarithmic differentiation, Arrhenius kinetics and Langmuir–Hinshelwood coverages. Observed order and activation energy are local slopes of a multistep rate, not necessarily the elementary reaction's stoichiometry or barrier.

## Intuition

Increasing pressure supplies reagent but also changes who occupies the surface. Increasing temperature accelerates elementary reaction but commonly removes adsorbed reagents. Either change can therefore reduce the overall rate in an appropriate regime.

## Derivation of reaction order

For $r=k_sK_AK_BP_AP_B/D^2$, with $D=1+K_AP_A+K_BP_B+K_{AB}P_{AB}$, define the local A order at fixed temperature and all other partial pressures as

$$n_A=\left(\frac{\partial\ln r}{\partial\ln P_A}\right)_{T,P_B,P_{AB}}.$$

Taking logarithms gives $\ln r=\ln k_s+\ln K_A+\ln K_B+\ln P_A+\ln P_B-2\ln D$. Only $\ln P_A$ and $D$ change with $P_A$, so differentiation gives

$$n_A=1-2\frac{K_AP_A}D=1-2\theta_A.$$

As A coverage varies from dilute to saturated, order varies from approximately +1 to −1. It is generally fractional. At fixed $P_B,P_{AB}$ write $a=1+K_BP_B+K_{AB}P_{AB}$. Then $r$ is proportional to $P_A/(a+K_AP_A)^2$. Differentiating gives a numerator proportional to $a-K_AP_A$, so the maximum occurs when

$$K_AP_A=a,\qquad\theta_A=\tfrac12,\qquad n_A=0.$$

The zero derivative is a maximum because the derivative changes from positive to negative. For the stated Eley–Rideal model with no A adsorption, $n_A=1$. Its B order is $1-\theta_B$ when other partial pressures are fixed.

## Derivation of apparent activation energy

Define

$$E_{\mathrm{app}}=-\mathcal R\left(\frac{\partial\ln r}{\partial(1/T)}\right)_{P_i}
=\mathcal RT^2\left(\frac{\partial\ln r}{\partial T}\right)_{P_i}.$$

For $k_s=A_s\exp[-E_s/(\mathcal RT)]$ with constant prefactor, $\mathcal RT^2d\ln k_s/dT=E_s$. Van't Hoff similarly gives $\mathcal RT^2d\ln K_i/dT=\Delta H_i$, where $\Delta H_i$ is the adsorption enthalpy of species $i$. Differentiating $D$ at fixed pressures gives

$$\mathcal RT^2\frac{d\ln D}{dT}
=\frac{K_AP_A\Delta H_A+K_BP_B\Delta H_B+K_{AB}P_{AB}\Delta H_{AB}}D
=\theta_A\Delta H_A+\theta_B\Delta H_B+\theta_{AB}\Delta H_{AB}.$$

Substituting each logarithmic derivative into the rate expression yields

$$E_{\mathrm{app}}=E_s+(1-2\theta_A)\Delta H_A
+(1-2\theta_B)\Delta H_B-2\theta_{AB}\Delta H_{AB}.$$

At dilute coverage this approaches $E_s+\Delta H_A+\Delta H_B$. Exothermic adsorption can make it negative: raising temperature removes the two reagents faster than elementary chemistry accelerates. At near-complete A coverage it approaches $E_s-\Delta H_A+\Delta H_B$, assuming other coverages vanish. Temperature-dependent prefactors or enthalpies contribute additional terms or make the slope vary. A fitted Arrhenius slope is therefore meaningful only over its stated operating range and pressure path.

![Temperature, coverage and apparent Arrhenius slopes](../figs/RE-S5-02-temperature-effects.png)

## Oxide reaction mechanism

Oxides provide metal sites, lattice oxygen, vacancies and hydroxyls rather than one uniform metal-site population. In a Mars–van Krevelen cycle an oxidised site supplies oxygen to reagent A; oxidant B restores the reduced or vacant site. Let $f$ denote the oxidised-site fraction and $1-f$ the reduced fraction. An illustrative two-step model has reduction rate $r_1=k_1P_Af$ and reoxidation rate $r_2=k_2P_B(1-f)$, with equivalent cycle stoichiometry absorbed into the coefficients.

At steady site inventory $r_1=r_2$, so $f(k_1P_A+k_2P_B)=k_2P_B$. The cycle rate is then

$$r=\frac{k_1k_2P_AP_B}{k_1P_A+k_2P_B}.$$

If reoxidation is much faster, $k_2P_B\gg k_1P_A$ and $r\approx k_1P_A$: first order in A and approximately zero order in B. If reduction is much faster, oxidant restoration controls. These limiting orders follow from the model; other adsorption steps or oxidant stoichiometry can alter pressure powers.

For CO oxidation over copper oxide, $2\mathrm{CuO}+\mathrm{CO}\to\mathrm{Cu_2O}+\mathrm{CO_2}$ followed by $\mathrm{Cu_2O}+\tfrac12\mathrm{O_2}\to2\mathrm{CuO}$ illustrates the cycle. CO may first bind, form a carbonate-like intermediate with lattice oxygen, and leave as CO₂; the vacancy is then replenished. Isotope-labelled lattice oxygen appearing in product supports this mechanism. Surface roughening is consistent with restructuring but is less specific evidence by itself.

An illustrative copper-oxide case at 573 K exhibits first-order CO and approximately zero-order oxygen dependence, consistent with rapid reoxidation relative to reduction in that regime. That observation constrains the active regime rather than assigning the same order to every oxide, temperature or feed composition.

## Motivation and explanation

A logarithmic derivative compares fractional rate change with fractional pressure change, so it reveals the local competition between additional supply and displacement. It is local because coverage changes as the pressure moves. A negative order therefore means that more A reduces the available partner coverage strongly enough to outweigh its own supply benefit; it does not imply negative chemical consumption.

In the oxide cycle, steady equality of reduction and reoxidation rates prevents the solid's oxidation state from drifting. A slow restoring step leaves most sites reduced and unable to supply oxygen; a slow consuming step leaves most sites oxidised. Adjusting the site fraction makes the two throughputs equal. This explains why increasing the already fast reagent supply has little effect on the overall rate and why a missing restoring step would make the solid a finite reagent.

Order is measured while holding the other independent variables fixed. A pressure experiment that changes temperature, total-pressure-dependent transport or other partial pressures measures a different slope. A negative activation energy, fractional order or product inhibition need not violate elementary kinetics: the observed rate combines several steps and inventories.

## Link to other topics

Internal diffusion can further disguise intrinsic order and activation energy. Oxide regeneration is a catalytic cycle, whereas irreversible depletion of lattice reagent requires a solid-reagent model.

## Conclusion

Local slopes reveal how reaction and coverage combine. A mechanism must conserve both sites and any lattice atoms that participate.
