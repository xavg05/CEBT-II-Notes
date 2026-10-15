[Previous](<SEP-35 - Adsorbents, affinity and cyclic operation.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-37 - Adsorption transport and uptake kinetics.md>)

<!-- note-content:start -->
# SEP-36: Langmuir and Freundlich equilibrium models

## Overview

Assumed: reversible adsorption and equilibrium constants.

An adsorption isotherm relates solid loading to fluid composition at fixed temperature. The Langmuir model predicts finite monolayer capacity; the Freundlich model describes a limited experimental range without a saturation limit.

## Intuition

Initially many sites are empty, so adding solute increases uptake strongly. As sites fill, the same increase in concentration produces less extra loading. A favourable isotherm loads substantially even at low concentration, but that same affinity can make desorption difficult.

## Derivation

**Step 1: write site rates.** Let $\theta$ be occupied-site fraction, $p_A$ solute partial pressure, and $k_a,k_d$ adsorption and desorption rate constants. Assume identical independent sites, one molecule per site and no lateral interactions:

$$r_a=k_a p_A(1-\theta),\qquad r_d=k_d\theta.\tag{152}$$

*Reason:* adsorption requires a molecule and an empty site; desorption requires an occupied site.

**Step 2: impose equilibrium and solve.** Equal forward and reverse rates give $k_a p_A=k_d\theta+k_a p_A\theta$. Define affinity $b=k_a/k_d$, with inverse-pressure units. Then

$$\theta=\frac{bp_A}{1+bp_A}.\tag{153}$$

*Reason:* collecting the occupied fraction isolates the finite-site constraint. For $bp_A\ll1$, $\theta\approx bp_A$; for $bp_A\gg1$, $\theta\to1$. Gas volumes measured at the same reference temperature and pressure give $\theta=V_{\mathrm{ads}}/V_{\mathrm{monolayer}}$.

**Step 3: convert to liquid loading.** Replace partial pressure by equilibrium liquid concentration $C^*$ and define dissociation concentration $K_d=k_d/k_a$. If $Q_m$ is monolayer loading per unit dry adsorbent mass,

$$q^*=Q_m\theta=\frac{Q_m C^*}{K_d+C^*}.\tag{154}$$

*Reason:* multiplying site fraction by capacity gives solid loading. Here larger $K_d$ means weaker affinity; it is the reciprocal convention to a concentration-based association constant.

**Step 4: obtain a parameter plot.** Taking reciprocals and separating terms yields

$$\frac1{q^*}=\frac{K_d}{Q_m}\frac1{C^*}+\frac1{Q_m}.\tag{155}$$

The Langmuir denominator records competition for a finite set of empty sites. At low concentration most sites remain available, so arrival rate can rise nearly proportionally with concentration. As occupancy grows, increasing arrival pressure cannot create new sites, and the incremental loading becomes small. This is why a high-pressure loading close to capacity need not double when pressure doubles.

The reciprocal plot exposes parameters by separating the original rational expression into a slope term and intercept. That algebra does not preserve the measurement-error structure: a small uncertainty in a low loading becomes a large uncertainty in its reciprocal. The plot is useful for interpretation, while a quantitative fit must respect the actual data uncertainties.

**Step 5: state the empirical alternative.** A Freundlich fit is

$$q^*=b_F(C^*)^m,\qquad 0<m<1.\tag{156}$$

Here $b_F$ is a dimensional fitting constant, distinct from gas affinity $b$. A log–log plot has slope $m$, provided fixed reference units are used. This is an empirical correlation, not a finite-site derivation.

## Motivation and explanation

Langmuir curvature is downward on a $q^*$ versus $C^*$ graph. Increasing concentration continues to increase loading, but its marginal benefit decreases. A Freundlich power with $0<m<1$ also curves downward; it cannot reproduce an S-shaped multilayer curve. Neither model should be extrapolated beyond its physical or fitted range.

Temperature-labelled isotherms are different from **isosteres**, which compare conditions at fixed loading. Exothermic adsorption commonly loads less at higher temperature. A nearly rectangular isotherm sometimes called “irreversible” describes very strong affinity; its shape alone does not establish molecular irreversibility.

## Worked example

For illustrative gas affinity $b=0.02\ \mathrm{kPa^{-1}}$, Equation (153) gives $\theta=0.009901$ at $p_A=0.5\ \mathrm{kPa}$ and $\theta=0.9091$ at $500\ \mathrm{kPa}$. The asymptotic conditions concern $bp_A$ relative to **one**.

For $Q_m=0.20\ \mathrm{kg\,kg^{-1}}$, $K_d=0.05\ \mathrm{kg\,m^{-3}}$ and $C^*=0.10\ \mathrm{kg\,m^{-3}}$, Equation (154) gives $q^*=0.1333\ \mathrm{kg\,kg^{-1}}$.

## Link to other topics

The same site balance appears in catalytic adsorption, but here its purpose is separation capacity. A batch balance uses the isotherm to connect remaining liquid concentration to captured solid inventory.

## Conclusion

Choose an isotherm for its supported range and mechanism. Equilibrium loading sets the endpoint; transport determines how quickly it is approached.
<!-- note-content:end -->

[Previous](<SEP-35 - Adsorbents, affinity and cyclic operation.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-37 - Adsorption transport and uptake kinetics.md>)
