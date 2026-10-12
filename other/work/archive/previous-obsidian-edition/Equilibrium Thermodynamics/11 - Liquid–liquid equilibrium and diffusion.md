# Liquid–liquid equilibrium and diffusion

## Overview

Liquids split into two phases when the molar Gibbs energy curve bulges above a chord; the coexisting compositions are found by a common tangent (Section 36). Miscibility gaps open and close with temperature, giving upper and lower consolute points, with an analogy to the vapour–liquid critical point (Section 37). A full numerical example for isobutane–furfural locates the coexisting liquids and the spinodal (Section 38). Between binodal and spinodal a single liquid is metastable; inside the spinodal it decomposes spontaneously (Section 39). The same curvature controls diffusion: the Fickian coefficient contains a thermodynamic factor that vanishes at the spinodal and goes negative inside (Section 40), checked against measurements near the nitrobenzene–hexane consolute point (Section 41).

*Assumed throughout:* $\underline{G} = \sum x_i\underline{G}_i + RT\sum x_i\ln x_i + \underline{G}^{ex}$ (Section 10); Gibbs–Duhem (Section 04); activity-coefficient models (Sections 17–20); Fick's law.

## Section 36: Why liquids separate, the curvature of the Gibbs energy of mixing

### Intuition

Mixing always gains entropy. In an ideal mixture that is the whole story, $\Delta\underline{G}_{\mathrm{mix}} = RT\sum x_i\ln x_i < 0$, and the curve of $\underline{G}$ against $x_1$ bows downward everywhere. Any homogeneous mixture then has a lower $\underline{G}$ than any pair of phases it could split into, so it stays mixed.

If unlike molecules dislike each other strongly ($\underline{G}^{ex}$ large and positive), the energy penalty can locally beat the entropy gain. The curve develops a hump. A mixture under the hump can lower its average $\underline{G}$ by splitting into two liquids whose compositions lie on either side. It moves *down* onto a straight line (the chord) joining the two phases.

*Analogy: a bridge sagging between two hills.* The lever-rule average of two phases lies on the straight line joining them. If the curve sits above that line, splitting is downhill. The analogy breaks down because the "line" is not arbitrary: equilibrium picks the unique line that touches the curve tangentially at both phase compositions.

### Derivation

**Step 1: Gibbs energy of a split system.** If a feed of composition $x_1$ splits into phases I and II, with mole fractions $x_1^{\mathrm{I}}$, $x_1^{\mathrm{II}}$ and amounts in the ratio given by the lever rule, the average molar Gibbs energy is the point at $x_1$ on the straight line joining $(x_1^{\mathrm{I}}, \underline{G}^{\mathrm{I}})$ and $(x_1^{\mathrm{II}}, \underline{G}^{\mathrm{II}})$. Splitting is favoured whenever

$$\underline{G}(x_1) > \lambda^{\mathrm{I}}\underline{G}(x_1^{\mathrm{I}}) + (1 - \lambda^{\mathrm{I}})\underline{G}(x_1^{\mathrm{II}}) \tag{152}$$

where $\lambda^{\mathrm{I}}$ is the fraction of moles in phase I. That is, whenever the curve lies above the chord.

**Step 2: slope of the $\underline{G}$ curve.** Differentiate $\underline{G} = x_1\mu_1 + x_2\mu_2$ with respect to $x_1$. The terms $x_1\,d\mu_1 + x_2\,d\mu_2$ vanish by Gibbs–Duhem, leaving

$$\frac{d\underline{G}}{dx_1} = \mu_1 - \mu_2 \tag{153}$$

The tangent at $x_1$ meets the axis $x_1 = 1$ at $\mu_1$ and the axis $x_1 = 0$ at $\mu_2$.

**Step 3: equilibrium is a common tangent.** Two-phase equilibrium requires $\mu_1^{\mathrm{I}} = \mu_1^{\mathrm{II}}$ and $\mu_2^{\mathrm{I}} = \mu_2^{\mathrm{II}}$. By (153), the tangents at the two phase compositions have the same slope and the same intercepts: they are one line touching the curve at both points. The coexisting compositions are *not* the minima of the curve, but the tangent points.

**Step 4: curvature.** Differentiate (153). Gibbs–Duhem gives $d\mu_2/dx_1 = -(x_1/x_2)\,d\mu_1/dx_1$, so

$$\frac{d^2\underline{G}}{dx_1^2} = \frac{1}{x_2}\frac{d\mu_1}{dx_1} = \frac{RT}{x_1x_2}\left(1 + x_1\frac{d\ln\gamma_1}{dx_1}\right) \tag{154}$$

using $\mu_1 = \underline{G}_1 + RT\ln x_1 + RT\ln\gamma_1$. For an ideal mixture the bracket is 1 and the curvature is always positive. A "wiggle" (a hump between two dips) needs the bracket to change sign, with two points where $d^2\underline{G}/dx_1^2 = 0$.

**Step 5: link to azeotropes.** The bracket in (154) is the same factor that appeared in $dP/dx_1$ in Section 27. Where it vanishes, the pressure–composition curve also has a turning point. That was the "other" root, and it signals the onset of liquid–liquid splitting.

### Motivation and explanation

**Entropy against energy.** $\Delta\underline{G}_{\mathrm{mix}} = \Delta\underline{H}_{\mathrm{mix}} - T\Delta\underline{S}_{\mathrm{mix}}$. The ideal entropy term is steepest near the pure components, since $d(x\ln x)/dx\to -\infty$. So even very immiscible liquids dissolve each other slightly: the convex dips near $x = 0$ and $x = 1$ always exist. Splitting happens in the middle, where a positive excess enthalpy can win.

**Why it matters.** Immiscibility is a nuisance in some equipment (two liquid phases on distillation trays) but useful in others:
- liquid–liquid extraction (e.g. furfural to refine lubricating oils);
- steam distillation of essential oils;
- dispersions and emulsions for polymerisation and microencapsulation.

![Real mixture G–x curve at constant T and P with a wiggle: the common tangent (line of minimum G) touches at the coexisting compositions xI and xII; a feed between them lies above the chord and splits](figs/ET-36-G-x-common-tangent.png)

### Worked example

**Problem.** A binary obeys one-constant Margules with $A/RT = 2.5$. Find the coexisting compositions and the Gibbs energy gained by an equimolar mixture when it splits.

**Model.** $\Delta\underline{G}_{\mathrm{mix}}/RT = x\ln x + (1-x)\ln(1-x) + 2.5\,x(1-x)$. The curve is symmetric about $x = 0.5$, so the common tangent is horizontal and touches the curve at its two minima. (For an asymmetric model the tangent is tilted and the tangent points are not the minima; see Section 38.)

**Binodal.** Setting the slope to zero gives $\ln[x/(1-x)] = 2.5(2x - 1)$, so $x^{\mathrm{I}} = 0.145$ and $x^{\mathrm{II}} = 0.855$.

**Gibbs energy gain.** $\Delta\underline{G}_{\mathrm{mix}}/RT$ is −0.068 for the homogeneous equimolar liquid, and −0.104 at the tangent points. Splitting lowers the Gibbs energy by $0.036RT$ per mole, about 90 J mol⁻¹ at 300 K. The mixture separates into two equal amounts (by symmetry) of 14.5 % and 85.5 % liquid.

### Link to other topics

The common tangent is the liquid–liquid counterpart of the equal-area construction for vapour–liquid coexistence of a pure fluid. Solvent extraction design starts from these coexisting compositions, extended to ternaries as tie lines on triangular diagrams.

### Summary

Liquids split when the curve of $\underline{G}$ against $x_1$ bulges above a chord. Equilibrium compositions lie at the points of a common tangent, because equal slopes and intercepts mean equal chemical potentials. A wiggle needs $1 + x_1\,d\ln\gamma_1/dx_1$ to change sign: strong enough positive deviations from ideality.

## Section 37: Temperature dependence, consolute points and the vapour–liquid analogy

### Intuition

$\Delta\underline{G}_{\mathrm{mix}} = \underline{H}^{ex} - T\left(\Delta\underline{S}^{\mathrm{IM}}_{\mathrm{mix}} + \underline{S}^{ex}\right)$, with $\Delta\underline{S}^{\mathrm{IM}}_{\mathrm{mix}} = -R\sum x_i\ln x_i > 0$.
- *UCST (normal):* unlike contacts cost energy ($\underline{H}^{ex} > 0$). The entropic reward for mixing grows with $T$, so it eventually wins and the liquids mix.
- *LCST:* unlike molecules hydrogen-bond specifically ($\underline{H}^{ex} < 0$), but that forces them into ordered arrangements ($\underline{S}^{ex} < 0$). At low $T$ the favourable energy wins and they mix. At high $T$ the $-T\underline{S}^{ex}$ penalty grows and they separate. Triethylamine–water is the classic example.
- *Closed loops* (both an LCST and a UCST) occur when these effects overlap.

### Derivation

**Step 1: regular solution.** Take one-constant Margules with $A$ independent of $T$ (pure energy, no excess entropy):

$$\frac{\Delta\underline{G}_{\mathrm{mix}}}{RT} = x\ln x + (1-x)\ln(1-x) + \frac{A}{RT}x(1-x)$$

**Step 2: curvature.**

$$\frac{1}{RT}\frac{d^2\Delta\underline{G}_{\mathrm{mix}}}{dx^2} = \frac{1}{x(1-x)} - \frac{2A}{RT}$$

The first term is smallest at $x = \tfrac12$, where it equals 4.

**Step 3: consolute point.** The curve first loses convexity (at $x = \tfrac12$) when $2A/RT = 4$:

$$T_c = \frac{A}{2R}, \qquad x_c = \tfrac12 \tag{155}$$

At a consolute point both $d^2\underline{G}/dx^2 = 0$ and $d^3\underline{G}/dx^3 = 0$: the two spinodal points merge.

**Step 4: below $T_c$.**
- *Binodal* (coexistence) compositions from the common tangent. By symmetry, $\ln[x/(1-x)] = (A/RT)(2x - 1)$.
- *Spinodal* compositions where the curvature vanishes: $x(1-x) = RT/(2A)$.

**Step 5: analogy with pure-fluid VLE.**

| Pure fluid, $P$–$\underline{V}$ isotherms | Binary liquid, $\underline{G}$–$x_1$ isotherms |
|---|---|
| Van der Waals loop below $T_c$ | Wiggle below $T_c$ |
| Equal areas → coexisting $\underline{V}^l$, $\underline{V}^v$ | Common tangent → coexisting $x_1^{\mathrm{I}}$, $x_1^{\mathrm{II}}$ |
| $dP/d\underline{V} = 0$: limit of metastability | $d^2\underline{G}/dx_1^2 = 0$: spinodal |
| Critical point: $dP/d\underline{V} = d^2P/d\underline{V}^2 = 0$ | Consolute point: $d^2\underline{G}/dx^2 = d^3\underline{G}/dx^3 = 0$ |

*Where the analogy breaks down:* at a consolute point the two coexisting *liquids* become identical in composition, but the system is still liquid and is not a gas–liquid critical point. Its pressure dependence is weak, and the "order parameter" is composition, not density.

![T–x diagram with an upper consolute point: binodal (solid) and spinodal (dashed) meet at Tc; G–x isotherms above, at and below Tc](figs/ET-37-binodal-spinodal-analogy.png)

![Four types of liquid–liquid phase diagram: LCST (triethylamine–water), UCST (phenol–water), closed loop (D2O–2-methylpyridine), and separate UCST and LCST regions (sulphur–triphenylamine)](figs/ET-37-UCST-LCST-shapes.png)

### Motivation and explanation

**Phase rule.** In the two-liquid region, $F = 2 - 2 + 2 = 2$. Fix $T$ and $P$ and both compositions are fixed; the feed composition only sets the amounts (lever rule). At the consolute point the extra condition $x^{\mathrm{I}} = x^{\mathrm{II}}$ leaves $F = 1$: at fixed pressure it is a single point.

**Real systems are asymmetric.** Consolute compositions are rarely 0.5 (hexane–nitrobenzene: $x_c\approx 0.42$ nitrobenzene). Asymmetric models (van Laar, NRTL) are needed to place them correctly. $A$ also usually varies with $T$, so a real $\underline{S}^{ex}\neq 0$.

### Worked example

**Problem.** Hexane–nitrobenzene has a UCST at about 19.4 °C (292.55 K). Treat it as a symmetric regular solution and estimate (a) the interaction parameter $A$, and (b) the coexisting and spinodal compositions at 15, 10, 0 and −10 °C.

**(a)** From (155), $A = 2RT_c = 2\times8.314\times292.55 = 4865$ J mol⁻¹.

**(b)** $A/RT = 2T_c/T$:

| $T$ (°C) | $A/RT$ | Binodal $x$ | Spinodal $x$ |
|---|---|---|---|
| 15 | 2.031 | 0.394 / 0.606 | 0.439 / 0.561 |
| 10 | 2.066 | 0.347 / 0.653 | 0.410 / 0.590 |
| 0 | 2.142 | 0.283 / 0.717 | 0.371 / 0.629 |
| −10 | 2.223 | 0.237 / 0.763 | 0.341 / 0.659 |

**Interpretation.** The two-phase region widens rapidly just below $T_c$ (the binodal opens roughly as $\sqrt{T_c - T}$), then more slowly. A 5 K drop below the UCST already gives phases differing by 0.2 in mole fraction. The symmetric model puts the consolute point at $x = 0.5$, whereas the real system's is at 0.42. Use these numbers for trends, not design.

### Link to other topics

Temperature-swing extraction exploits the opening and closing of the miscibility gap. Polymer solutions with an LCST (e.g. thermoresponsive hydrogels) are used in drug delivery and bioseparations. The vapour–liquid analogy returns when vapour and two liquids coexist (VLLE) in the final sections.

### Summary

Miscibility gaps open and close with temperature through the balance of $\underline{H}^{ex}$ and $T\underline{S}$. A regular solution has a UCST at $T_c = A/2R$, while LCSTs need favourable but ordering interactions. At a consolute point the spinodal and binodal meet, analogous to (but not the same as) a vapour–liquid critical point.

## Section 38: Worked example, isobutane–furfural liquid–liquid equilibrium

*Components:* isobutane (1), furfural (2).

### Intuition

Furfural is polar (an aldehyde on a furan ring); isobutane is a small, non-polar alkane. Large van Laar constants ($\gamma^{\infty} = e^{2.62}\approx 14$ and $e^{3.02}\approx 20$) say each strongly dislikes the other. We expect two nearly pure phases, each holding only a little of the other component. That is the situation exploited when furfural extracts aromatics from hydrocarbon oils.

### Derivation

**Step 1: equilibrium equations.** With the same pure-liquid reference in both phases, $\mu_i^{\mathrm{I}} = \mu_i^{\mathrm{II}}$ becomes equal activities:

$$x_1^{\mathrm{I}}\gamma_1^{\mathrm{I}} = x_1^{\mathrm{II}}\gamma_1^{\mathrm{II}}, \qquad x_2^{\mathrm{I}}\gamma_2^{\mathrm{I}} = x_2^{\mathrm{II}}\gamma_2^{\mathrm{II}} \tag{156}$$

with van Laar $\ln\gamma_1 = \alpha/[1 + \alpha x_1/(\beta x_2)]^2$ and $\ln\gamma_2 = \beta/[1 + \beta x_2/(\alpha x_1)]^2$.

**Step 2: solve.** At 37.8 °C use $\alpha=2.62$ and $\beta=3.02$ (dimensionless). Solve the two non-linear equations for two distinct compositions, $x_1^{\mathrm{I}}<x_1^{\mathrm{II}}$; the trivial equal-composition root is not a phase split. Equivalently, find the common tangent to
$$\frac{\Delta\underline{G}_{\mathrm{mix}}}{RT} = \sum_i x_i\ln x_i + \sum_i x_i\ln\gamma_i.$$

**Step 3: spinodals.** Where $d^2(\Delta\underline{G}_{\mathrm{mix}}/RT)/dx_1^2 = 0$, located numerically.

### Worked example

**Results.**

| | Phase I (furfural-rich) | Phase II (isobutane-rich) |
|---|---|---|
| $x_1$ | 0.1128 | 0.9284 |
| $x_2$ | 0.8872 | 0.0716 |
| $\gamma_1$ | 8.375 | 1.018 |
| $\gamma_2$ | 1.030 | 12.77 |
| $a_1 = x_1\gamma_1$ | 0.9448 | 0.9448 |
| $a_2 = x_2\gamma_2$ | 0.9140 | 0.9140 |

The equal activities confirm (156). Further:
- spinodals at $x_1 = 0.270$ and 0.805;
- the minima of $\Delta\underline{G}_{\mathrm{mix}}/RT$ lie at $x_1 = 0.107$ and 0.924, close to but not the same as the phase compositions;
- an equimolar feed splits into 52.5 % phase I and 47.5 % phase II (lever rule).

![ΔG_mix/RT for isobutane–furfural at 37.8 °C from van Laar: two dips, a hump between, spinodal points (crosses) and the common tangent touching at x1 = 0.1128 and 0.9284](figs/ET-38-isobutane-furfural-Gmix.png)

### Motivation and explanation

**Why the tangent points are not the minima.** The model is asymmetric ($\beta > \alpha$), so the common tangent is tilted. A tilted line touches each dip slightly off its lowest point. Only for a symmetric curve is the tangent horizontal, with tangent points at the minima.

**Reading the activity coefficients.**
- The dilute component in each phase has a large $\gamma$ (8.4 for isobutane in furfural, 12.8 for furfural in isobutane), while the major component has $\gamma\approx 1$. This is the Gibbs–Duhem behaviour of Section 11 seen in practice.
- *A quick estimate.* From (156), $\gamma_1^{\mathrm{I}}\approx x_1^{\mathrm{II}}/x_1^{\mathrm{I}}$ when $\gamma_1^{\mathrm{II}}\approx 1$: $0.9284/0.1128 = 8.23$, against the exact 8.375. The solubility of a component in the "wrong" phase is roughly $1/\gamma$ in that phase.

**Assumptions.** The van Laar constants are taken as valid at 37.8 °C (they depend on $T$). Pressure (5 bar, to keep isobutane liquid) has negligible effect on liquid-phase activities (Section 10).

### Link to other topics

Equation (156) with a solute added is the basis of distribution coefficients in liquid–liquid extraction. A solute's partition between two solvents equals the ratio of its activity coefficients in them.

### Summary

Solving equal-activity conditions with van Laar gives coexisting liquids at $x_1 = 0.1128$ and 0.9284, with spinodals at 0.270 and 0.805. The minor component in each phase has a large activity coefficient, approximately the ratio of its mole fractions in the two phases.

## Section 39: Binodal, spinodal and the stability of a single liquid

### Intuition

Normally, adding more of component 1 to a region raises $\mu_1$ there. So any local excess of component 1 pushes it away, and concentration fluctuations die out: the mixture is stable.

Inside the spinodal the opposite holds: adding component 1 *lowers* $\mu_1$. A region that happens to gain a little component 1 now attracts more, the fluctuation grows, and the liquid tears itself into two phases everywhere at once. No nucleation is needed.

Between binodal and spinodal, small fluctuations still die out, but a large enough fluctuation (a nucleus of the other phase) can grow. That is the same situation as a supersaturated vapour (Section 23).

### Derivation

**Step 1: chemical potentials from the $\underline{G}$ curve.** From $\underline{G} = x_1\mu_1 + x_2\mu_2$ and $d\underline{G}/dx_1 = \mu_1 - \mu_2$:

$$\mu_1 = \underline{G} + x_2\frac{d\underline{G}}{dx_1}, \qquad \mu_2 = \underline{G} - x_1\frac{d\underline{G}}{dx_1} \tag{157}$$

These are the tangent intercepts.

**Step 2: derivatives.** Differentiate (157); the $d\underline{G}/dx_1$ terms cancel:

$$\frac{\partial\mu_1}{\partial x_1} = x_2\frac{\partial^2\underline{G}}{\partial x_1^2}, \qquad \frac{\partial\mu_2}{\partial x_1} = -x_1\frac{\partial^2\underline{G}}{\partial x_1^2} \tag{158}$$

**Step 3: stability criterion.** Both $\partial\mu_1/\partial x_1$ and $\partial\mu_2/\partial x_2$ have the sign of $\partial^2\underline{G}/\partial x_1^2$:
- positive curvature: each component's chemical potential rises with its own concentration, so small fluctuations decay (**locally stable**). Inside the binodal such a state can still be metastable;
- zero curvature: the **spinodal**, where $\partial\mu_1/\partial x_1 = \partial\mu_2/\partial x_1 = 0$;
- negative curvature: each component moves *up* its own concentration gradient (**unstable**).

**Step 4: limiting values.** As $x_2\to 0$, $\mu_1\to\underline{G}_1$ and $\mu_2\to -\infty$, and vice versa. At a stationary point of $\underline{G}$, $\mu_1 = \mu_2 = \underline{G}$. Plotting $\mu_1$ and $\mu_2$ against $x_1$ therefore shows two S-shaped curves. At the binodal compositions each $\mu_i$ takes the same value (the horizontal lines), and between the spinodals each runs backwards.

![G–x curve with spinodal (green) and binodal (orange) compositions, and below it μ1 and μ2 against x1: between the spinodals each chemical potential decreases with its own mole fraction](figs/ET-39-G-and-mu-vs-x.png)

### Motivation and explanation

**Cooling a single liquid into the gap (UCST system).**
1. Above the binodal: a single liquid is the equilibrium state.
2. Between binodal and spinodal: two liquids are the equilibrium, but the single liquid persists until a nucleus forms (on impurities, walls or stirring). The result is typically droplets of one phase growing in the other.
3. On crossing the spinodal: spontaneous separation everywhere, giving a very fine, interconnected dispersion of the two phases.

![Cooling path: single liquid; then two equilibrium liquids but nucleation needed (between binodal and spinodal); at the spinodal spontaneous separation](figs/ET-39-cooling-path.png)

**Practical consequences.** Spinodal decomposition produces fine, co-continuous structures, the basis of porous glasses, phase-separation membranes and some alloy and polymer-blend microstructures. Metastability explains why a quickly cooled mixture can stay cloudy-free (single-phase) for a while before suddenly separating.

### Worked example

**Problem.** For the regular solution with $A/RT = 2.5$ (Section 36), classify the states at $x_1 = 0.10$, 0.20 and 0.40, and give the sign of $\partial\mu_1/\partial x_1$ at each.

**Boundaries.** Binodal $x = 0.145/0.855$; spinodal $x = 0.276/0.724$.

**Curvature.** $\frac{1}{RT}\frac{\partial^2\underline{G}}{\partial x^2} = \frac{1}{x(1-x)} - 5$:

| $x_1$ | $1/[x(1-x)] - 5$ | Region | Behaviour |
|---|---|---|---|
| 0.10 | +6.11 | outside binodal | stable single liquid |
| 0.20 | +1.25 | between binodal and spinodal | metastable; splits only after nucleation |
| 0.40 | −0.83 | inside spinodal | unstable; spinodal decomposition |

By (158), $\partial\mu_1/\partial x_1 = x_2\,\partial^2\underline{G}/\partial x_1^2$ has the same sign as the curvature: positive at 0.10 and 0.20, negative at 0.40.

**Interpretation.** A 20 % liquid quenched quickly to this temperature can stay homogeneous until nucleated. A 40 % liquid cannot: it separates immediately into a fine dispersion. Both end up as the same two equilibrium phases (14.5 % and 85.5 %). The routes, and the resulting structures, differ.

### Link to other topics

The sign of $\partial\mu_1/\partial x_1$ is exactly what controls diffusion. Section 40 shows that the ordinary Fickian diffusion coefficient is proportional to it, so it vanishes at the spinodal and turns negative inside.

### Summary

Single-phase stability requires each chemical potential to increase with that component's own concentration, i.e. $\partial^2\underline{G}/\partial x_1^2 > 0$. The spinodal ($\partial^2\underline{G}/\partial x_1^2 = 0$) separates metastable states, which need nucleation, from unstable ones, which decompose spontaneously. The binodal marks where two liquids become the equilibrium.

## Section 40: Diffusion is driven by chemical potential, not concentration

*Notation:* $N_1$ is the molar flux of 1 (mol m⁻² s⁻¹), $c$ the total molar concentration, $z$ position, and $D$ a diffusion coefficient.

### Intuition

Molecules do not "know" concentration; they respond to differences in free energy. In an ideal mixture the two coincide, since $\mu_1$ rises smoothly with $x_1$, so Fick's law works. In a strongly non-ideal mixture, $\mu_1$ may barely change, or even fall, as $x_1$ rises. Then a large concentration difference may give little or negative driving force.

At an equilibrium interface between two liquids, $\mu_1$ is equal on both sides, so there is no net flux despite the jump in composition.

### Derivation

**Step 1: ideal mixture.** $\mu_1 = \underline{G}_1 + RT\ln x_1$, so $\partial\mu_1/\partial x_1 = RT/x_1$. Change the variable in Fick's law:

$$N_1 = -Dc\frac{dx_1}{dz} = -Dc\left(\frac{\partial x_1}{\partial\mu_1}\right)\frac{d\mu_1}{dz} = -\frac{Dcx_1}{RT}\frac{d\mu_1}{dz} \tag{159}$$

The two forms are identical for an ideal mixture.

**Step 2: real mixture, taking (159) as fundamental.** Postulate that the chemical-potential form holds with a well-behaved coefficient $D$, and convert back using $\partial\mu_1/\partial x_1 = RT(1/x_1 + \partial\ln\gamma_1/\partial x_1)$:

$$N_1 = -\frac{Dcx_1}{RT}\frac{\partial\mu_1}{\partial x_1}\frac{dx_1}{dz} = -Dc\left(1 + \frac{\partial\ln\gamma_1}{\partial\ln x_1}\right)\frac{dx_1}{dz} \tag{160}$$

The measured (Fickian) coefficient is therefore

$$D_{12} = D\,\Gamma, \qquad \Gamma = 1 + \frac{\partial\ln\gamma_1}{\partial\ln x_1} = \frac{x_1x_2}{RT}\frac{\partial^2\underline{G}}{\partial x_1^2} \tag{161}$$

(the last form from (154) of Section 36).

**Step 3: consequences.**
- *Ideal mixture:* $\Gamma = 1$.
- *At the spinodal:* $\Gamma = 0$, so $D_{12} = 0$, whatever the molecular mobility.
- *Inside the spinodal:* $\Gamma < 0$, so the flux runs *up* the concentration gradient.
- *At an equilibrium interface:* the bulk chemical potentials are equal in the two phases, so there is no net transfer despite the composition jump. Across a diffuse interface, gradient contributions to the free energy must be included in the chemical potential; the homogeneous-liquid formula alone does not describe the interface.

**Step 4: regular solution.** For one-constant Margules, $\ln\gamma_1 = (A/RT)x_2^2$, so $\partial\ln\gamma_1/\partial\ln x_1 = x_1\cdot(A/RT)\cdot2x_2\cdot(-1)$, and

$$\Gamma = 1 - 2\frac{A}{RT}x_1x_2 \tag{162}$$

### Motivation and explanation

**Why this matters.** Diffusion coefficients in strongly non-ideal liquids (near phase separation, or in associating mixtures) vary greatly with composition. Much of that variation is thermodynamic ($\Gamma$), not molecular ($D$). Correlations that separate the two, $D_{12} = D\Gamma$, extrapolate far better. This is the binary case of the Maxwell–Stefan approach to multicomponent diffusion.

**Limits.** Equation (160) assumes $D$ itself is a constant or smooth property. Very close to a consolute point, concentration fluctuations make that inadequate (next section).

### Worked example

**Problem.** For the regular solution with $A/RT = 2.5$, compute $\Gamma$ and the ratio $D_{12}/D$ at $x_1 = 0.145$ (binodal), 0.40 and 0.50.

**Equation (162)**, $\Gamma = 1 - 5x_1x_2$:

| $x_1$ | $\Gamma = D_{12}/D$ | Meaning |
|---|---|---|
| 0.145 (binodal) | +0.38 | diffusion slowed to 38 % of the "ideal" value |
| 0.276 (spinodal) | 0 | no diffusive smoothing |
| 0.40 | −0.20 | uphill diffusion |
| 0.50 | −0.25 | uphill diffusion |

**Interpretation.** Even on the equilibrium phase boundary, thermodynamics alone slows diffusion by a factor of almost 3 compared with an ideal mixture of the same mobility. Inside the spinodal the effective coefficient is negative, which is the mechanism of spinodal decomposition: diffusion *creates* composition differences rather than destroying them.

### Link to other topics

The thermodynamic factor appears in mass-transfer correlations for extraction and in membrane transport. Section 41 tests (160) against measurements on nitrobenzene–hexane near its consolute point.

### Summary

Material moves down chemical-potential gradients. Rewriting Fick's law that way shows that the measured diffusion coefficient is a mobility times the thermodynamic factor $\Gamma = 1 + \partial\ln\gamma_1/\partial\ln x_1$. $\Gamma$ is 1 for an ideal mixture, zero at the spinodal and negative inside it. This explains zero flux across an equilibrium interface, and uphill diffusion during phase separation.

## Section 41: Example, diffusion near the nitrobenzene–hexane consolute point

*Components:* nitrobenzene (1), hexane (2).

### Intuition

At the consolute point the curvature of $\underline{G}$ vanishes, so $\Gamma=0$ and long-wavelength mutual diffusion becomes arbitrarily slow; molecular self-diffusion remains finite. Near that point, long-lived composition fluctuations couple to fluid motion and change the effective molecular mobility. A smooth-mobility approximation $D_{12}=D\Gamma$ therefore predicts a steeper slowdown than observed. Replacing $\Gamma$ by $\Gamma^n$, with $n<1$, captures the gentler measured decrease empirically; it is not derived merely by averaging $\Gamma$ over local compositions.

### Derivation

**Step 1: thermodynamic factor from data.** $\Gamma$ was computed from a four-constant Redlich–Kister model fitted to measured total-pressure ($P$–$x_1$) data at 21, 25 and 35 °C. The fit used the full γ–φ equation, including Poynting and second-virial vapour corrections:

$$P = \sum_i x_i\gamma_iP_i^{\mathrm{SAT}}\exp\!\left[\frac{(\underline{V}_i^{L} - B_{ii})(P - P_i^{\mathrm{SAT}})}{RT}\right]$$

The fitted model reproduces the flat, nearly constant pressure across the middle of the composition range. A flat $P$–$x$ curve is the signature of a system close to liquid–liquid splitting, by (132) of Section 27.

**Step 2: diffusion law.**

$$N_1 = -Dc\,\Gamma^{\,n}\,\frac{dx_1}{dz} \tag{163}$$

with $D$ taken as a smooth function of temperature and $n$ fitted.

### Worked example

**(a) Illustration with a regular-solution model.** Treating the system as a symmetric regular solution with $T_c = 292.55$ K (so $A = 2RT_c$), at the consolute composition (162) of Section 40 gives $\Gamma = 1 - T_c/T$:

| $T$ (K) | $\Gamma$ | $\Gamma^{0.64}$ |
|---|---|---|
| 293.15 | 0.0020 | 0.019 |
| 295.15 | 0.0088 | 0.048 |
| 298.15 | 0.0188 | 0.079 |
| 303.15 | 0.0350 | 0.117 |
| 308.15 | 0.0506 | 0.148 |

Within 15 K of the consolute point, $\Gamma$ itself is only 0.2–5 %. The exponent raises the effective factor by a factor of 3–10 near $T_c$, and changes how steeply diffusion collapses. These numbers come from a deliberately crude model; the published comparison used the Redlich–Kister fit.

**(b) Comparison with measurements.** Measured diffusion coefficients at the consolute composition, from three independent data sets, fall from about $3\times10^{-10}$ m² s⁻¹ at 308 K towards zero at about 292.5 K. With the Redlich–Kister $\Gamma$:
- $n = 1$ predicts values several times too low over the whole range;
- $n = 0.64$ fits all three data sets closely.

![Diffusion coefficient of nitrobenzene–hexane at the consolute composition against temperature: experimental data from three studies, the Γ^n model with n = 0.64 (blue) and with n = 1 (grey)](figs/ET-41-nitrobenzene-hexane-diffusion.png)

### Motivation and explanation

**Why $n\neq 1$.** Near a critical point, composition fluctuations have a growing correlation length and couple to hydrodynamic motion. The transport mobility is therefore not a smooth background coefficient. Critical-phenomena and mode-coupling theories describe these coupled fluctuations; their full derivation is beyond this course. The power $\Gamma^n$ represents the resulting transport enhancement relative to the simple $D\Gamma$ model. Thinking of diffusion as sampling fluctuating compositions is useful intuition, but simple averaging of $\Gamma$ is not a derivation of the fitted exponent. Values near 0.6 work for several systems.

**What is robust.** The qualitative prediction (diffusion slows to zero at the consolute point, through thermodynamics rather than viscosity) is confirmed. The quantitative form needs the empirical exponent.

**Limits.** The fitted $n$ depends on the activity-coefficient model used for $\Gamma$; a poor $\gamma$ model would be absorbed into $n$. Far from the consolute point, fluctuations are small and $n\to 1$ is expected to suffice.

### Link to other topics

Critical slowing-down of diffusion matters in extraction and crystallisation operated near miscibility limits, and in supercritical-fluid processes. The same thermodynamic-factor correction applies to multicomponent diffusion in non-ideal mixtures.

### Summary

Near the nitrobenzene–hexane consolute point (≈19.4 °C), the measured diffusion coefficient collapses towards zero, as the thermodynamic factor predicts. Within this empirical model, raising $\Gamma$ to a power of about 0.64 fits the data, representing the effect of critical composition fluctuations on transport. The final unit adds a vapour to two liquid phases: vapour–liquid–liquid equilibrium and steam distillation.

## Conclusion

Liquid–liquid equilibrium is governed by the curvature of the Gibbs energy of mixing: the common tangent gives the equilibrium phases, the spinodal the limit of stability, and the consolute point where they meet. Because the true driving force for diffusion is the chemical-potential gradient, the same curvature makes diffusion slow to zero at the spinodal and run uphill inside it. The final part combines liquid–liquid and vapour–liquid equilibrium.
