# Section 15: Freezing-point depression

## Overview

When a liquid mixture is cooled until a pure solid freezes out (ice from sea water, for example), the freezing temperature depends on the solvent's chemical potential in the liquid. This note derives the general result

$$\ln(\gamma_1x_1) = \frac{\Delta\underline{H}_1^{\mathrm{fus}}}{R}\left(\frac{1}{T_f} - \frac{1}{T}\right),$$

and its familiar dilute limit, the cryoscopic law $\Delta T = K_fm$. Read one way, it is a phase-equilibrium prediction. Read the other way, it measures the solvent activity coefficient $\gamma_1$ even when the vapour pressure is too low to measure. It is also the solid–liquid counterpart of the ice calculation in Section 01.

*Assumed:* $\mu_i = \underline{G}_i + RT\ln(\gamma_ix_i)$ (Section 10); $(\partial\underline{G}/\partial T)_P = -\underline{S}$; equilibrium $\mu_1^S = \mu_1^L$ (Section 01).

*Notation:* component 1 is the solvent that freezes out (e.g. water); component 2 is the solute that stays in the liquid. $T_f$ is the freezing point of pure 1 at the system pressure. $\Delta\underline{H}_1^{\mathrm{fus}}$, $\Delta\underline{S}_1^{\mathrm{fus}}$ and $\Delta\underline{G}_1^{\mathrm{fus}}$ are the molar changes on melting pure 1 (liquid minus solid).

## Intuition

Dissolving a solute lowers the solvent's chemical potential in the liquid, through the $RT\ln x_1$ mixing term (and $\gamma_1$). The pure solid is unaffected, because the solute does not enter it. The liquid is therefore stabilised relative to the solid, and the temperature must fall further before the solid's $\underline{G}$ drops below the liquid's.

*Physically:* the liquid has an entropic advantage (mixing) that the solid cannot share, so the solid can only win once the temperature has fallen enough for its lower enthalpy to dominate.

## Derivation

**Step 1: equilibrium condition.** With pure solid 1 in contact with the liquid mixture at $(T, P)$:

$$\mu_1^{S} = \mu_1^{L} \tag{1}$$

**Step 2: the two sides.** The solid is pure, so $\mu_1^S = \underline{G}_1^S(T,P)$. The liquid side is (Section 10):

$$\mu_1^L = \underline{G}_1^L(T,P) + RT\ln(\gamma_1x_1)$$

where $\underline{G}_1^L$ is *pure liquid* 1 at the same $T$, $P$. Below $T_f$ this is a supercooled liquid: a well-defined hypothetical state.

**Step 3: combine.** Write $\underline{G}_1^S = \underline{G}_1^L - \Delta\underline{G}_1^{\mathrm{fus}}$ and substitute into (1):

$$RT\ln(\gamma_1x_1) = -\Delta\underline{G}_1^{\mathrm{fus}}(T) \tag{2}$$

The pressure dependence of $\Delta\underline{G}^{\mathrm{fus}}$ is dropped, because condensed-phase volumes are small (Section 06).

**Step 4: temperature dependence of $\Delta\underline{G}^{\mathrm{fus}}$.** At $T_f$ the pure solid and liquid coexist, so $\Delta\underline{G}_1^{\mathrm{fus}}(T_f) = 0$ and $\Delta\underline{S}_1^{\mathrm{fus}} = \Delta\underline{H}_1^{\mathrm{fus}}/T_f$. From $(\partial\Delta\underline{G}/\partial T)_P = -\Delta\underline{S}$, with $\Delta\underline{S}^{\mathrm{fus}}$ taken as constant between $T$ and $T_f$:

$$\Delta\underline{G}_1^{\mathrm{fus}}(T) = -\Delta\underline{S}_1^{\mathrm{fus}}(T - T_f) = \frac{\Delta\underline{H}_1^{\mathrm{fus}}}{T_f}(T_f - T) \tag{3}$$

**Step 5: the freezing-point equation.** Substitute (3) into (2) and divide by $RT$:

$$\boxed{\ln(\gamma_1x_1) = \frac{\Delta\underline{H}_1^{\mathrm{fus}}}{R}\left(\frac{1}{T_f} - \frac{1}{T}\right)} \tag{4}$$

Since $\Delta\underline{H}^{\mathrm{fus}} > 0$ and $\gamma_1x_1 < 1$ for an ideal or near-ideal mixture, $T < T_f$: the freezing point is depressed.

**Step 6: small depression.** Let $\Delta T = T_f - T \ll T_f$. Then $1/T_f - 1/T = -\Delta T/(TT_f) \approx -\Delta T/T_f^2$:

$$\ln(\gamma_1x_1) \approx -\frac{\Delta\underline{H}_1^{\mathrm{fus}}}{RT_f^2}\,\Delta T \tag{5}$$

**Step 7: dilute ideal limit.** For dilute solute, $\gamma_1\to 1$ (Gibbs–Duhem, Section 11) and $-\ln x_1 = -\ln(1-x_2)\approx x_2$. With molality $m$ (mol solute per kg solvent) and solvent molar mass $M_1$, $x_2\approx M_1m$. Hence

$$\Delta T \approx \frac{RT_f^2M_1}{\Delta\underline{H}_1^{\mathrm{fus}}}\,m = K_f\,m \tag{6}$$

## Motivation and explanation

**A colligative property.** Equation (6) contains nothing about the solute's identity, only how many solute particles there are. If the solute dissociates (NaCl gives Na⁺ and Cl⁻), $x_2$ counts the particles, roughly doubling the effect. In concentrated solutions the solute affects the result only through $\gamma_1$, which is exactly why (4) can be used to *measure* $\gamma_1$.

**Measuring activity coefficients.** Measure $T$ at known $x_1$. Then (4) gives $\gamma_1x_1$, hence $\gamma_1$, with no vapour-pressure measurement. This is essential for involatile mixtures (salts, polymers, sugars). Gibbs–Duhem then gives the solute's $\gamma_2$.

**What is assumed, and when it fails.**
1. *Only pure solid 1 freezes out.* This fails for solid solutions, and for hydrates or water of crystallisation.
2. *Constant $\Delta\underline{S}^{\mathrm{fus}}$ (equivalently $\Delta\underline{H}^{\mathrm{fus}}$).* Over tens of kelvin, the heat-capacity difference between liquid and solid changes $\Delta\underline{H}^{\mathrm{fus}}$ noticeably (see the next section).
3. *Small $\Delta T$* for (5)–(6). Large depressions, e.g. alloys such as solders, need (4).
4. *Pressure effects neglected.* This is fine at ordinary pressures.

## Worked example

**Problem.** (a) Compute water's cryoscopic constant from $\Delta\underline{H}^{\mathrm{fus}} = 333.55$ J g⁻¹, i.e. 6009 J mol⁻¹. (b) Find the freezing point of an ideal 1 mol kg⁻¹ aqueous solution of a non-electrolyte using (4) and (6). (c) Estimate the freezing point of sea water, with 35 g kg⁻¹ of salt, about 0.6 mol kg⁻¹ NaCl.

**(a)** $K_f = RT_f^2M_1/\Delta\underline{H}^{\mathrm{fus}} = 8.314\times273.15^2\times0.018015/6009 = 1.860$ K kg mol⁻¹. This matches the textbook value of 1.86, derived here entirely from the thermodynamics of the pure solvent.

**(b)** $x_2 = 0.018015/(1 + 0.018015) = 0.01770$, so $-\ln x_1 = 0.01785$.
- Equation (4) with $\gamma_1 = 1$: $\Delta T = 1.83$ K.
- Equation (6): $\Delta T = 1.86$ K.

The linear law overestimates by 1.6 % even at 1 mol kg⁻¹, because it linearises both $\ln(1-x_2)$ and $1/T$.

**(c)** NaCl dissociates fully into two particles, so treat sea water as about 1.2 mol kg⁻¹ of ideal solute particles. Equation (4) gives $\Delta T \approx 2.2$ K, against observed sea water at about −2 °C. Agreement is fair. The remaining difference reflects the approximate composition and the non-ideality of a concentrated electrolyte ($\gamma_1\neq 1$), which ionic-solution theory addresses later in the course.

## Link to other topics

The same derivation, with the vapour in place of the solid, gives boiling-point elevation. With a semipermeable membrane in place of the phase boundary, it gives osmotic pressure. All three are colligative properties and all three measure solvent activity. Equation (4) applied to each component in turn gives the full solid–liquid phase diagram, with its eutectic, in the next section.

## Conclusion

Freezing equilibrium between a pure solid and a liquid mixture gives $\ln(\gamma_1x_1) = (\Delta\underline{H}_1^{\mathrm{fus}}/R)(1/T_f - 1/T)$. In the dilute limit this becomes the cryoscopic law $\Delta T = K_fm$, with $K_f = RT_f^2M_1/\Delta\underline{H}^{\mathrm{fus}}$ (1.86 K kg mol⁻¹ for water). In concentrated mixtures it is a way to measure the solvent's activity coefficient. The next section applies it to both components of ethylene glycol–water, building the freezing curves, locating the eutectic, and using real data to reveal non-ideality.
