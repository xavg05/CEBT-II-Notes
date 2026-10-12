# Foundations: equilibrium, equations of state and the chemical potential

## Overview

This part sets up everything the rest of the course uses. Equilibrium at fixed temperature and pressure is the minimum of the Gibbs energy, which means equal chemical potential of every component in every phase, with material moving from high to low $\mu_i$ (Section 01). An equation of state supplies the numbers, with each property computed as an ideal-gas value plus a departure integrated from zero pressure (Section 02). In mixtures the relevant quantities are partial molar properties: each component's share of a mixture property, which sum exactly to the total but differ from pure-component values when mixing is non-ideal, as the 3 % volume contraction of whiskey shows (Section 03). The chemical potential is the partial molar Gibbs energy; at fixed $T$ and $P$ the chemical potentials of a mixture are tied together by the Gibbs–Duhem equation (Section 04). Finally, $\mu_i$ is built up for ideal gases, ideal-gas mixtures, ideal mixtures and real fluids, the last needing a correction integral from an equation of state (Section 05).

*Assumed throughout:* first and second laws; $G = H - TS$; Maxwell relations; the van der Waals and Peng–Robinson equations from earlier years.

## Section 01: The criterion for phase equilibrium

*Notation (used throughout):* a plain symbol is a total (extensive) property, e.g. $G$, $V$. An underline is a molar property, e.g. $\underline{G} = G/n$; this course writes $\underline{V}$ where many texts write $V_m$. A subscript $i$ on an underlined symbol means pure $i$, e.g. $\underline{G}_i$. Superscripts $L$, $V$, $S$ label liquid, vapour and solid.

### Intuition

At constant $T$ and $P$ the system exchanges heat and work with surroundings that hold $T$ and $P$ fixed. The Gibbs energy is the quantity that accounts for the entropy change of *both* the system and those surroundings. So "the universe's entropy goes up" becomes "the system's $G$ goes down".

Chemical potential is how much $G$ changes when one more mole of a component is added to a phase. If moving a molecule from phase L to phase V lowers $G$, it will move. It stops moving when the transfer no longer changes $G$, i.e. when the chemical potentials are equal.

*Analogy: water levels in connected tanks.* Water flows from the higher level to the lower until the levels match, and $\mu_i$ plays the role of the level. The analogy breaks down because each component has its own "level", and the levels can differ between components. Also, $\mu_i$ is not a fixed property of a phase: it changes as the phase's composition changes, which a tank's water level does not do in the same way.

### Derivation

**Step 1: $G$ is minimised at constant $T$, $P$.** For a closed system exchanging heat with surroundings at $T$, the surroundings receive $-dH$ as heat at constant $P$, so $dS_{\mathrm{surr}} = -dH/T$. The second law requires $dS + dS_{\mathrm{surr}} \ge 0$. Multiply by $-T$:

$$dG = dH - T\,dS \le 0 \qquad (\text{constant } T, P) \tag{1}$$

*Reason:* at constant $T$, $dG = dH - T\,dS$. So every spontaneous change at fixed $T$ and $P$ lowers $G$, and equilibrium is the minimum.

**Step 2: the fundamental relation.** For a closed, homogeneous phase,

$$dG = -S\,dT + V\,dP \tag{2}$$

This combines the first law, $dU = \delta Q + \delta W$, with $\delta Q_{\mathrm{rev}} = T\,dS$ and the definition of $G$. It holds for any change between equilibrium states. If the phase is *open*, its amounts can also change, and each mole of $i$ added changes $G$ by $\mu_i$:

$$dG = -S\,dT + V\,dP + \sum_i \mu_i\,dn_i, \qquad \mu_i \equiv \left(\frac{\partial G}{\partial n_i}\right)_{T,P,n_{j\neq i}} \tag{3}$$

**Step 3: two phases in contact.** Take a closed system with phases L and V at the same $T$ and $P$. Move $dn$ moles of component $i$ from L to V, so $dn_i^V = +dn$ and $dn_i^L = -dn$. Apply (3) to each phase (each is open, but the whole is closed) at constant $T$, $P$:

$$dG = dG^L + dG^V = \left(\mu_i^V - \mu_i^L\right)dn \tag{4}$$

**Step 4: equilibrium and direction.** At the minimum of $G$, (4) must vanish for any small transfer, so

$$\mu_i^L = \mu_i^V \quad \text{for every component } i \tag{5}$$

Away from equilibrium, (1) requires $dG < 0$. If $\mu_i^L > \mu_i^V$, then $dn > 0$: component $i$ moves from the phase where its chemical potential is higher to where it is lower.

**Step 5: pure substance.** For pure $i$, $G = n\underline{G}_i(T,P)$, so $\mu_i = \partial G/\partial n = \underline{G}_i$. Equation (5) becomes

$$\underline{G}^L = \underline{G}^V \tag{6}$$

### Motivation and explanation

**Why $\mu_i$ and not concentration.** Material does not, in general, move down a concentration gradient. Water and oil sit side by side with very different water concentrations and nothing flows. What equalises is $\mu_i$, which includes the energetic preference of each molecule for its surroundings.

**What is held constant.** Equation (1) needs fixed $T$ and $P$. Equation (5) also assumes:
- thermal equilibrium (same $T$ in both phases);
- mechanical equilibrium (same $P$, which is true across a flat interface);
- that component $i$ can actually cross between the phases.

Later sections relax these one at a time. Across a curved interface (droplets and bubbles) the pressures differ. Across a semipermeable membrane only some components can cross (osmosis). Each case changes which equalities hold, and that is exactly how those problems are solved.

**Sanity check.** At the normal melting point, ice and water coexist, so (6) holds at 0 °C and 1 atm. Below that temperature (6) fails and the phase with the lower $\underline{G}$ wins. The example below quantifies this.

### Worked example

**Problem.** Water is supercooled to −10 °C at 1 atm. Which phase is stable, and what is the driving force for freezing? The enthalpy of fusion is 333.55 J g⁻¹ (so $\Delta\underline{H}_{\mathrm{fus}} = 6009$ J mol⁻¹), and the melting point is $T_f = 273.15$ K.

**Temperature dependence of $\underline{G}$.** From (2) at constant $P$, $(\partial\underline{G}/\partial T)_P = -\underline{S}$. Applying this to each phase and subtracting:

$$\frac{d}{dT}\left(\underline{G}^L - \underline{G}^S\right) = -\left(\underline{S}^L - \underline{S}^S\right) = -\Delta\underline{S}_{\mathrm{fus}}$$

**Anchor at $T_f$.** At the melting point $\underline{G}^L = \underline{G}^S$, which also gives $\Delta\underline{S}_{\mathrm{fus}} = \Delta\underline{H}_{\mathrm{fus}}/T_f = 22.0$ J mol⁻¹ K⁻¹. Assuming $\Delta\underline{S}_{\mathrm{fus}}$ is constant over 10 K and integrating from $T_f$ to $T$:

$$\underline{G}^L - \underline{G}^S \approx \Delta\underline{S}_{\mathrm{fus}}\,(T_f - T) = 22.0 \times 10 = 220\ \text{J mol}^{-1}$$

**Answer.** The liquid's molar Gibbs energy is about 220 J mol⁻¹ higher than the solid's, so ice is stable and the water will freeze given a nucleation site. At −5 °C the driving force is half as large, about 110 J mol⁻¹. *Physically:* the liquid's higher entropy lets it win above $T_f$; below $T_f$ the $-T\underline{S}$ term no longer compensates for its higher enthalpy.

### Link to other topics

The same calculation, with the liquid's chemical potential lowered by a dissolved solute, gives freezing-point depression later in the course. The chemical potential defined in (3) is the partial molar Gibbs energy, the subject of the partial-molar-property sections that follow.

### Summary

At constant $T$ and $P$, equilibrium is the minimum of $G$. Between phases this means equal molar Gibbs energy for a pure substance and equal chemical potential of every component for a mixture, with material flowing from high to low $\mu_i$. Everything else is about computing $\mu_i$.

## Section 02: Equations of state and departure functions

### Intuition

An ideal gas is the easy reference: its properties are known exactly from $P\underline{V} = RT$ and heat-capacity data. A real fluid differs because its molecules attract one another at moderate separations and repel at short ones. At zero pressure the molecules are infinitely far apart, so every real fluid *is* an ideal gas there.

So the plan is: start at $P = 0$ (ideal), follow the real isotherm up to the pressure of interest, and add up how the real fluid's property changes compared with the ideal gas along the way. The EOS tells us $\underline{V}$ along that path, and the Maxwell relations turn $\underline{V}$ into everything else.

### Derivation

**Step 1: the EOS.** The ideal-gas law $P\underline{V} = RT$ cannot produce a liquid. The van der Waals equation,

$$\left(P + \frac{a}{\underline{V}^2}\right)\left(\underline{V} - b\right) = RT \tag{7}$$

adds two corrections: $b$, the volume excluded by finite molecular size, and $a/\underline{V}^2$, the reduction in wall pressure caused by attractions. It is cubic in $\underline{V}$. Below the critical temperature it has three roots, which is how it predicts a liquid and a vapour. Modern cubic EOS (Peng–Robinson and others) keep this structure with better-tuned $a(T)$ and $b$.

**Step 2: how $\underline{H}$ depends on pressure.** From $d\underline{H} = T\,d\underline{S} + \underline{V}\,dP$, at constant $T$:

$$\left(\frac{\partial \underline{H}}{\partial P}\right)_T = T\left(\frac{\partial \underline{S}}{\partial P}\right)_T + \underline{V}$$

**Step 3: remove the entropy.** From $d\underline{G} = -\underline{S}\,dT + \underline{V}\,dP$, equality of the mixed second derivatives gives the Maxwell relation $(\partial\underline{S}/\partial P)_T = -(\partial\underline{V}/\partial T)_P$. Hence

$$\left(\frac{\partial \underline{H}}{\partial P}\right)_T = \underline{V} - T\left(\frac{\partial \underline{V}}{\partial T}\right)_P \tag{8}$$

*Reason:* the right side contains only $P$–$\underline{V}$–$T$ quantities, which the EOS provides.

**Step 4: integrate from the ideal-gas limit.** At $P \to 0$ the fluid is ideal, so $\underline{H}(T, 0) = \underline{H}^{\mathrm{IG}}(T)$. Integrating (8) along the isotherm:

$$\underline{H}(T,P) - \underline{H}^{\mathrm{IG}}(T) = \int_{0}^{P}\left[\underline{V} - T\left(\frac{\partial \underline{V}}{\partial T}\right)_P\right]dP \tag{9}$$

For an ideal gas the integrand is $RT/P - T(R/P) = 0$, so the departure is zero, as it must be.

**Step 5: low-pressure van der Waals.** At low density, (7) expands to $\underline{V} \approx RT/P + b - a/RT$, i.e. a second virial coefficient $B = b - a/RT$. Then $T(\partial\underline{V}/\partial T)_P = RT/P + a/RT$, and the integrand of (9) is constant:

$$\underline{H} - \underline{H}^{\mathrm{IG}} \approx \left(b - \frac{2a}{RT}\right)P \tag{10}$$

### Motivation and explanation

**Sign and meaning.** In (10), attractions ($a$) lower the enthalpy below the ideal-gas value, because the molecules sit in each other's potential wells. Repulsions ($b$) raise it. At ordinary temperatures attractions win for most gases. Equation (8) is then negative, so a gas throttled at constant $H$ to lower pressure cools (the Joule–Thomson effect). The sign changes at $T = 2a/(Rb)$, the van der Waals estimate of the inversion temperature.

**Why departures, not absolutes.** Equation (9) only gives *differences* from a reference that is known separately. Ideal-gas heat capacities fix $\underline{H}^{\mathrm{IG}}(T)$; the EOS fixes the departure. Process simulators compute every property this way. The same route applied to $\underline{G}$ is what defines fugacity later in the course.

**When it fails.**
- The low-pressure form (10) is only the first term of an expansion in density.
- A cubic EOS is reasonable for non-polar fluids but poor for strongly polar or hydrogen-bonding liquids.
- For mixtures the EOS needs mixing rules for $a$ and $b$, which work for "easy" mixtures (similar molecules) but not for, say, ethanol–water.

### Worked example

**Problem.** Estimate the enthalpy departure of nitrogen at 300 K and 1, 10 and 100 bar from the van der Waals EOS, with $a = 1.370$ L² bar mol⁻² $= 0.1370$ Pa m⁶ mol⁻² and $b = 0.0387$ L mol⁻¹ $= 3.87\times10^{-5}$ m³ mol⁻¹.

**Low-pressure formula (10).** $b - 2a/RT = 3.87\times10^{-5} - 2(0.1370)/(8.314\times300) = -7.11\times10^{-5}$ m³ mol⁻¹. Multiply by $P$:

| $P$ (bar) | (10) low-pressure (J mol⁻¹) | (9) integrated numerically with full vdW (J mol⁻¹) |
|---|---|---|
| 1 | −7.1 | −7.1 |
| 10 | −71.1 | −71.0 |
| 100 | −711 | −661 |

**Interpretation.** At 1–10 bar the linear formula is exact to the precision shown. At 100 bar it overestimates the departure by about 8 % (−711 against −661 J mol⁻¹), because higher-order density terms (repulsions becoming more important) start to matter. For comparison, heating nitrogen by 1 K raises its ideal-gas enthalpy by $\underline{C}_P \approx 7R/2 = 29.1$ J mol⁻¹. So at 100 bar the non-ideal correction equals about 23 K of heating, which is not negligible in a compressor or throttle energy balance. The negative sign means nitrogen at 300 K cools on throttling, since $300\ \text{K} < 2a/(Rb) = 852$ K, the van der Waals inversion temperature.

### Link to other topics

The Gibbs-energy departure uses the ideal-gas subtraction, $\underline{G}-\underline{G}^{\mathrm{IG}}=\int_0^P[\underline{V}-RT/P]\,dP$, rather than the enthalpy integrand in (9). That is the basis of chemical potentials from an EOS and of fugacity coefficients later in the course. Mixture EOS need partial molar volumes, introduced in the next two sections.

### Summary

An EOS turns the general theory into numbers. Any property is computed as an ideal-gas value plus a departure, integrated along the isotherm from $P = 0$, where every fluid is ideal.

## Section 03: Partial molar properties

*Notation:* $V$ is the total volume. $\underline{V}$ is the molar volume of the system (pure or mixture). $\underline{V}_i$ is the molar volume of pure $i$. $\bar V_i$ is the partial molar volume of $i$ in a mixture. $x_i = n_i/n$ is the mole fraction, where $n$ is the total amount.

### Intuition

Add one mole of water to a swimming pool of pure water and the volume rises by 18 cm³, the molar volume of water. Add the same mole of water to a swimming pool of pure ethanol and the volume rises by only about 14 cm³. The water molecules are the same; what differs is their surroundings. Hydrogen bonding with ethanol and different packing let them occupy less space.

The partial molar volume is that increase: the volume a component *effectively* occupies in a particular mixture. It is a property of the component **in that environment**, so it changes with composition. The swimming pool is large so that adding one mole does not change the composition.

*Analogy:* pouring sand into a jar of marbles. The sand fills the gaps, so the total rises by less than the sand's own volume. This breaks down for molecules. Water–ethanol contraction comes from intermolecular forces (hydrogen bonding) as well as shape, so the "gaps" depend on energetics and temperature, not just geometry.

### Derivation

**Step 1: definition.** For any extensive property, using volume as the example,

$$\bar V_i \equiv \left(\frac{\partial V}{\partial n_i}\right)_{T,P,n_{j\neq i}} \tag{11}$$

*Reason:* this is the change in total volume per mole of $i$ added, with $T$, $P$ and all other amounts fixed. That is the swimming-pool experiment taken to the limit of an infinitesimal addition.

**Step 2: scaling property.** At fixed $T$ and $P$, doubling every amount doubles the volume. In general, for any factor $\lambda$:

$$V(T,P,\lambda n_1,\dots,\lambda n_N) = \lambda\,V(T,P,n_1,\dots,n_N) \tag{12}$$

*Reason:* $V$ is extensive. Mathematically, it is homogeneous of degree one in the amounts.

**Step 3: differentiate (12) with respect to $\lambda$.** Using the chain rule on the left side:

$$\sum_i \frac{\partial V}{\partial(\lambda n_i)}\,n_i = V$$

**Step 4: set $\lambda = 1$.** The derivatives become the partial molar volumes (11):

$$V = \sum_i n_i\,\bar V_i \qquad\Longleftrightarrow\qquad \underline{V} = \sum_i x_i\,\bar V_i \tag{13}$$

*Reason:* dividing by $n$ gives the molar form. This is Euler's theorem for homogeneous functions. It says the partial molar volumes are the right "shares" of the total: they add up exactly to the mixture volume.

**Step 5: pure-component limit.** For pure $i$, $V = n_i\underline{V}_i$, so $\bar V_i = \underline{V}_i$.

The same steps apply to $U$, $H$, $S$, $A$ and $G$. Each has partial molar properties that sum like (13).

### Motivation and explanation

**Why not just use pure volumes?** If mixing changed nothing, $\bar V_i$ would equal $\underline{V}_i$ and the mixture volume would be $\sum n_i\underline{V}_i$. Any difference between the two is a measure of non-ideal mixing, the subject of most of this course. Volume is the easiest place to see it because it can be measured with a measuring cylinder.

**What is held constant.** Equation (11) holds $T$, $P$ and all other $n_j$ fixed. It is not a derivative with respect to mole fraction, because adding $i$ changes all the mole fractions at once.

**Graphical meaning.** Partial molar volumes in a binary are found from plots of $\underline{V}$ against $x$ (the tangent construction), or plotted directly as below. They are intensive: they depend on composition, $T$ and $P$, not on how much mixture there is.

![Partial molar volumes of water (left axis) and ethanol (right axis) against ethanol mole fraction; the lines mark x = 0.17](figs/ET-03-partial-molar-volumes-ethanol-water.png)

The curves move in opposite directions. Where ethanol's partial molar volume rises, water's falls. This is not a coincidence: it is the Gibbs–Duhem equation, derived in the next section.

### Worked example

**Problem.** A 700 cm³ bottle contains a whiskey-like ethanol–water mixture prepared from pure-liquid volumes in the ratio 40:60. Here 40 % means ethanol volume divided by the sum of the two pure-liquid volumes before mixing; it is not the usual alcohol-by-volume (ABV) label, which uses the final drink volume. How much ethanol and water does it contain, and what volume would the two pure liquids have occupied before mixing? Pure molar volumes: $\underline{V}_{\mathrm{EtOH}} = 58$ cm³ mol⁻¹, $\underline{V}_{\mathrm{H_2O}} = 18$ cm³ mol⁻¹.

**Mole fraction.** For this explicitly defined pre-mixing recipe, take 100 cm³ of separate pure liquids: $40/58 = 0.690$ mol ethanol and $60/18 = 3.333$ mol water, so $x_{\mathrm{EtOH}} = 0.171$, about 17 mol %. Use $x_{\mathrm{EtOH}} \approx 0.17$ for the graph estimates below.

**Partial molar volumes at $x_{\mathrm{EtOH}} = 0.17$** (read from the graph, so ≈): $\bar V_{\mathrm{EtOH}} \approx 54.7$ cm³ mol⁻¹, $\bar V_{\mathrm{H_2O}} \approx 17.8$ cm³ mol⁻¹. Both are below their pure values.

**Total amount from (13).** With $V = n\,(x_{\mathrm{EtOH}}\bar V_{\mathrm{EtOH}} + x_{\mathrm{H_2O}}\bar V_{\mathrm{H_2O}})$:

$$700 = n\,(0.17\times54.7 + 0.83\times17.8) \;\Rightarrow\; n = 29.08\ \text{mol}$$

so $n_{\mathrm{EtOH}} = 4.94$ mol and $n_{\mathrm{H_2O}} = 24.13$ mol.

**Volumes before mixing.** Ethanol: $4.94\times58 = 287$ cm³. Water: $24.13\times18 = 434$ cm³. Together that is **721 cm³ of pure liquids, which make 700 cm³ of whiskey**: a contraction of 21 cm³, or 2.9 %.

**Interpretation.** Adding pure-component volumes would overfill the bottle by 3 %. Ethanol–water is a non-ideal mixture, and a model that assumes ideal mixing gets even the volume wrong. Because the volume differs from the ideal value, the Gibbs energy and chemical potentials must differ too.

### Link to other topics

The chemical potential is the partial molar property of $G$, so (13) becomes $G = \sum n_i\mu_i$: the identity that underlies the Gibbs–Duhem equation and every later model of mixture non-ideality. Excess volumes such as the 21 cm³ here are the volumetric counterpart of the excess Gibbs energy used to build activity-coefficient models.

### Summary

A partial molar property is a component's contribution to a mixture property in its actual environment. The contributions sum exactly to the total, but they differ from pure-component values whenever mixing is non-ideal, as the 3 % contraction of whiskey shows.

## Section 04: Chemical potential and the Gibbs–Duhem equation

### Intuition

Section 03 showed that partial molar volumes are shares of a total and that the shares depend on the environment. If one component's share grows as the composition changes, the other's must shrink to keep the books balanced. The Gibbs–Duhem equation states this exactly.

For the Gibbs energy it has a sharp physical meaning. In a binary at fixed $T$ and $P$, you cannot raise the escaping tendency of both components at once by changing the composition. Whatever makes component 1 "happier" in the mixture must make component 2 less so, in proportion to how much of each is present.

*Analogy: a seesaw with the fulcrum at the composition.* The mole fractions are the lever arms. A small change in $\mu_1$ on the long arm must be balanced by a larger change in $\mu_2$ on the short arm. The analogy breaks down because a seesaw balances forces at one instant, while Gibbs–Duhem is a relation between *changes*, $d\mu_i$, along a path of compositions. It says nothing about the absolute values of $\mu_i$.

### Derivation

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

**Step 5: the same holds for any partial molar property.** Repeat Steps 2–4 with $V$. Since $(\partial V/\partial n_i)$ already defines $\bar V_i$, and at constant $T$, $P$ we have $dV = \sum\bar V_i\,dn_i$:

$$\sum_i x_i\,d\bar V_i = 0 \qquad (\text{constant } T, P) \tag{18}$$

**Step 6: binary form.** With $x_2 = 1 - x_1$, divide (18) by $dx_1$:

$$x_1\,\frac{d\bar V_1}{dx_1} + x_2\,\frac{d\bar V_2}{dx_1} = 0 \tag{19}$$

The two slopes have opposite signs, and their magnitudes are in the inverse ratio of the mole fractions.

### Motivation and explanation

**Why it matters.** Equation (15) says the mixture Gibbs energy is fully determined by the chemical potentials. So the whole problem of phase equilibrium reduces to finding the $\mu_i$. Equation (17) says those $\mu_i$ are not independent.
- In a binary, measuring or modelling one component's $\mu$ against composition gives the other's by integration.
- Experimental data for both components can be checked for consistency with (17); data that violate it contain errors.
- Any model for $\mu_i$ must satisfy it. Later sections build models from a single function, the excess Gibbs energy, precisely so that this is automatic.

**Reading the graph in Section 03.** In dilute ethanol ($x_{\mathrm{EtOH}}$ small), (19) says water's partial molar volume barely changes, because its slope is multiplied by the small $x_{\mathrm{EtOH}}/x_{\mathrm{H_2O}}$. Meanwhile ethanol's changes steeply. Both features are visible on the curves near $x_{\mathrm{EtOH}} = 0$: water's curve is flat and ethanol's is steep.

**What is held constant.** Equations (17)–(19) require constant $T$ and $P$. If $T$ or $P$ vary, the full form (16) applies.

### Worked example

**Problem.** Use a one-parameter model for the ethanol (1)–water (2) partial molar volumes,
$$\bar V_1 = \underline{V}_1 + A\,x_2^2, \qquad \bar V_2 = \underline{V}_2 + A\,x_1^2,$$
with $\underline{V}_1 = 58$ and $\underline{V}_2 = 18$ cm³ mol⁻¹. (a) Show that it obeys Gibbs–Duhem. (b) Fit $A$ to $\bar V_1 \approx 54.7$ cm³ mol⁻¹ at $x_1 = 0.17$, predict $\bar V_2$ there, and compare with the graph value of ≈17.8 cm³ mol⁻¹. (c) Test the model at the two ends of the composition range.

**(a) Consistency.** $d\bar V_1/dx_1 = -2Ax_2$ and $d\bar V_2/dx_1 = 2Ax_1$. Substitute into (19):
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

### Link to other topics

The binary Gibbs–Duhem equation applied to $\mu_i = \mu_i^{\mathrm{ideal}} + RT\ln\gamma_i$ becomes $x_1\,d\ln\gamma_1 + x_2\,d\ln\gamma_2 = 0$. That is the constraint behind the Margules and van Laar models and behind consistency tests of vapour–liquid equilibrium data. Equation (16) with the composition terms removed is also the basis of the Gibbs phase rule, which counts how many intensive variables are free.

### Summary

The chemical potential is the partial molar Gibbs energy. The mixture's Gibbs energy is the mole-fraction-weighted sum of the chemical potentials, and at fixed $T$ and $P$ their changes are tied together by Gibbs–Duhem. In a binary, knowing one gives the other, as the ethanol–water volumes show.

## Section 05: Calculating the chemical potential

*Notation:* $P^{\circ}$ is a reference pressure. $\underline{G}_i^{\circ}(T)$ is the molar Gibbs energy of pure $i$ **as an ideal gas** at $T$ and $P^{\circ}$. $\underline{G}_i(T,P)$ is that of real pure $i$ at $T$, $P$ in the phase of interest. $x_i$ is the mole fraction in whichever phase is being described.

### Intuition

For an ideal gas the only thing that changes $\mu$ is how crowded the molecules are, i.e. the pressure, entering through $RT\ln P$. In a mixture of ideal gases the molecules ignore each other, so each component behaves as if it were alone at its own partial pressure. Mixing then only adds entropy, through the $RT\ln x_i$ term.

An **ideal mixture** of liquids takes that entropy term and nothing else: the molecules are assumed to interact with each other exactly as they do with their own kind. So mixing changes neither volume nor enthalpy. Any real deviation, such as the 3 % contraction of whiskey, means unlike molecules interact differently, and $\mu_i$ needs a correction.

### Derivation

**Step 1: pure ideal gas.** At constant $T$, $d\underline{G} = \underline{V}\,dP = (RT/P)\,dP$. Integrating from $P^{\circ}$:

$$\mu_i = \underline{G}_i = \underline{G}_i^{\circ}(T) + RT\ln\frac{P}{P^{\circ}} \tag{20}$$

**Step 2: ideal-gas mixture.** Ideal-gas molecules do not interact, so component $i$ has the same $\mu_i$ as if it occupied the volume alone at its partial pressure $P_i = x_iP$:

$$\mu_i = \underline{G}_i^{\circ}(T) + RT\ln\frac{x_iP}{P^{\circ}} = \underline{G}_i^{\mathrm{IG}}(T,P) + RT\ln x_i \tag{21}$$

where $\underline{G}_i^{\mathrm{IG}}(T,P)$ is pure ideal-gas $i$ at the mixture's $T$ and $P$, from (20). Summing with $\underline{G} = \sum x_i\mu_i$:

$$\underline{G} = \sum_i x_i\,\underline{G}_i^{\mathrm{IG}}(T,P) + RT\sum_i x_i\ln x_i \tag{22}$$

The second term is the Gibbs energy of mixing. It is always negative because every $x_i < 1$, and it does not depend on $P$.

**Step 3: ideal mixture (definition).** Define an ideal mixture (IM) as any mixture, liquid or gas, whose *mixing* behaviour copies (21) and (22), but with **real pure-component** Gibbs energies:

$$\mu_i^{\mathrm{IM}} = \underline{G}_i(T,P) + RT\ln x_i, \qquad \underline{G}^{\mathrm{IM}} = \sum_i x_i\underline{G}_i + RT\sum_i x_i\ln x_i \tag{23}$$

**Step 4: consequences for volume (cross-derivative).** The partial molar volume follows from $\mu_i$ through mixed second derivatives of $G$:

$$\left(\frac{\partial\mu_i}{\partial P}\right)_{T,n} = \frac{\partial}{\partial P}\left(\frac{\partial G}{\partial n_i}\right) = \frac{\partial}{\partial n_i}\left(\frac{\partial G}{\partial P}\right) = \left(\frac{\partial V}{\partial n_i}\right)_{T,P,n_{j\neq i}} = \bar V_i \tag{24}$$

*Reason:* the order of differentiation does not matter for a smooth function, and $(\partial G/\partial P)_{T,n} = V$.

Apply (24) to (23). At fixed composition, $RT\ln x_i$ does not depend on $P$, so $\bar V_i^{\mathrm{IM}} = (\partial\underline{G}_i/\partial P)_T = \underline{V}_i$. An ideal mixture therefore has **no volume change on mixing**. In the same way, the Gibbs–Helmholtz relation gives $\bar H_i^{\mathrm{IM}} = \underline{H}_i$, so there is no heat of mixing either.

**Step 5: real pure substance from an EOS.** Integrate $d\underline{G}_i = \underline{V}_i\,dP$ along the real isotherm:

$$\mu_i = \underline{G}_i(T,P) = \underline{G}_i(T,P^{\circ}) + \int_{P^{\circ}}^{P}\underline{V}_i\,dP \tag{25}$$

This still needs $\underline{G}_i(T,P^{\circ})$ for the *real* fluid. To tie it to the tabulated ideal-gas value, extend the integral down to $P\to 0$, where the fluid becomes ideal (Step 7).

**Step 6: real mixture from an EOS.** Integrate (24) along the isotherm at fixed composition:

$$\mu_i(T,P) = \mu_i(T,P^{\ast}) + \int_{P^{\ast}}^{P}\bar V_i\,dP \tag{26}$$

Here $\bar V_i$ comes from a mixture EOS as a function of $T$, $P$ and composition.

**Step 7: anchor at zero pressure (the real-fluid correction).** Write (26) for the real mixture, and the same equation for the ideal-gas mixture of the same composition, for which $\bar V_i = RT/P$. Subtract the two. As $P^{\ast}\to 0$ the real mixture becomes an ideal-gas mixture, so $\mu_i - \mu_i^{\mathrm{IG}}\to 0$ at the lower limit. Then add (21):

$$\mu_i(T,P) = \underline{G}_i^{\circ}(T) + RT\ln\frac{x_iP}{P^{\circ}} + \int_{0}^{P}\left(\bar V_i - \frac{RT}{P}\right)dP \tag{27}$$

The first two terms are the ideal-gas-mixture value. The integral is the real-fluid correction. It is finite because $\bar V_i - RT/P$ stays bounded as $P\to 0$.

### Motivation and explanation

**Why $RT\ln x_i$ survives at zero pressure.** Taking the real mixture down to $P = 0$ removes the *interactions*, but it does not unmix the components. The $RT\ln x_i$ term in (27) is the ideal entropy of mixing, which is present even for ideal gases. Section 02's pure-fluid departures had no such term. Forgetting it is a common error.

**Limiting cases.**
- (27) with $\bar V_i = RT/P$: the integral vanishes and (21) is recovered.
- (23) with $x_i = 1$: $\mu_i = \underline{G}_i$, the pure-component value.
- (21) and (23) as $x_i\to 0$: $\mu_i\to-\infty$. This is the logarithmic behaviour that later motivates working with fugacity instead of $\mu$.

**When each approach fails.**
- Equation (27) is exact, but only as good as the mixture EOS that supplies $\bar V_i$. Cubic EOS with simple mixing rules work for "easy" mixtures: gases, homologous series (e.g. alkanes) and isomers.
- They fail for liquid mixtures of chemically different molecules (polar, hydrogen-bonding or associating), where the EOS cannot capture the specific interactions.
- The ideal mixture (23) fails whenever unlike interactions differ from like ones. Real liquid mixtures are therefore handled by writing $\mu_i = \mu_i^{\mathrm{IM}} + $ (a correction), the activity-coefficient approach developed later.

### Worked example

**Problem.** (a) Find the ideal Gibbs energy of mixing for the whiskey of Sections 03–04 ($x_{\mathrm{EtOH}} = 0.17$, 29.08 mol in total) at 20 °C. (b) Use Step 4 to test whether ethanol–water is an ideal mixture.

**(a) Ideal Gibbs energy of mixing.** From (23), per mole of mixture:

$$\Delta\underline{G}_{\mathrm{mix}}^{\mathrm{IM}} = RT\left[x_1\ln x_1 + x_2\ln x_2\right] = 8.314\times293.15\times\left[0.17\ln0.17 + 0.83\ln0.83\right] = -1111\ \text{J mol}^{-1}$$

For the 29.08 mol in the bottle, that is −32.3 kJ. Mixing is strongly spontaneous even with no energetic preference at all, purely from entropy.

**(b) Ideality test.** If the mixture were ideal, Step 4 says $\bar V_i = \underline{V}_i$, so the bottle's contents would occupy $\sum n_i\underline{V}_i = 721$ cm³. They actually occupy 700 cm³, so the volume of mixing is −21 cm³ in total, or −0.73 cm³ per mole of mixture. Since $\Delta\underline{V}_{\mathrm{mix}} \neq 0$, the partial molar volumes differ from the pure ones. By (24), $\mu_i$ must then have a pressure-dependent part beyond (23). **Ethanol–water is not an ideal mixture.** Its real Gibbs energy of mixing differs from −1111 J mol⁻¹, and finding by how much is the job of activity-coefficient models.

### Link to other topics

The correction integral in (27) reappears as the fugacity coefficient: dividing by $RT$, the integral is $\ln\bar\phi_i$, which turns the chemical potential into a "corrected partial pressure". The ideal mixture (23), combined with an ideal-gas vapour, gives Raoult's law, and deviations from it are measured by activity coefficients.

### Summary

The chemical potential follows from (20) for a pure ideal gas, (21) for an ideal-gas mixture and (23) for an ideal mixture. Real fluids add the correction integral of (27), which needs partial molar volumes from a mixture EOS. That works only for simple mixtures, so the course next recasts $\mu$ in a more convenient variable, fugacity, starting with the simplest real case: a pure liquid under an inert gas.

## Conclusion

Phase equilibrium reduces to computing chemical potentials. They are partial molar Gibbs energies, they sum to the mixture Gibbs energy, and Gibbs–Duhem ties their changes together. For ideal gases and ideal mixtures they have simple logarithmic forms; for real fluids an equation of state adds a correction integral that only works for simple mixtures. The next part recasts $\mu$ as a corrected pressure, the fugacity, which is the convenient variable for every equilibrium calculation that follows.
