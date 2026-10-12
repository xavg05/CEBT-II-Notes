[Previous](<RE-02 - Ideal CSTR and PFR balances.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<RE-04 - Coupled mass and energy balances.md>)

<!-- note-content:start -->
# RE-03: Conversion and changing gas volume

## Overview

Assumed: the ideal-gas equation and the ideal CSTR/PFR balances.

Consider a steady, single gas-phase reaction, with no phase change or side streams. Conversion tracks molar flow of a chosen reactant even if temperature, pressure or total gas moles change. Concentration must then be obtained from stoichiometry and the gas equation of state; it is generally not $C_{A0}(1-X_A)$.

## Intuition

Reactant concentration can fall because A reacts and because the gas expands. Measuring concentration alone cannot distinguish those effects. An inert component reacts neither way, yet its concentration also falls during expansion.

## Derivation

Let $\nu_A<0$ be A's stoichiometric coefficient, $F_{i0}$ the inlet molar flow of species $i$, and $\Delta\nu=\sum_i\nu_i$ the total stoichiometric change in gas moles per reaction as written. Let $F_{T0}$ be total inlet molar flow and $y_{A0}=F_{A0}/F_{T0}$ the inlet mole fraction of A.

**Step 1: determine the extent flow.** Consuming $F_{A0}X_A$ mol s$^{-1}$ of A requires an extent flow $F_{A0}X_A/(-\nu_A)$. Each other species changes by its coefficient times this extent:

$$
F_i=F_{i0}+\nu_i\frac{F_{A0}X_A}{-\nu_A}.
\tag{6}
$$

*Reason:* stoichiometry links species molar flows, independently of density. Inerts have $\nu_i=0$.

**Step 2: sum all gas species.** Summing (6) and factoring the inlet total gives

$$
F_T=F_{T0}(1+\epsilon X_A),\qquad
\epsilon=y_{A0}\frac{\Delta\nu}{-\nu_A}.
\tag{7}
$$

*Reason:* each mole of extent changes total gas flow by $\Delta\nu$. The dimensionless expansion parameter $\epsilon$ includes dilution by inerts. It may be positive, zero or negative.

**Step 3: convert molar flow into volume flow.** For an ideal gas, $Q=F_TRT/P$, where $P$ and $T$ are the local absolute pressure and temperature and $R$ is the gas constant. Dividing by inlet $Q_0=F_{T0}RT_0/P_0$ gives

$$
\frac{Q}{Q_0}=(1+\epsilon X_A)\frac{T}{T_0}\frac{P_0}{P},\qquad
C_A=C_{A0}\frac{1-X_A}{1+\epsilon X_A}\frac{T_0}{T}\frac{P}{P_0}.
\tag{8}
$$

*Reason:* $C_A=F_A/Q$ and $F_A=F_{A0}(1-X_A)$. All factors in the concentration ratio are dimensionless. For a real gas, introduce the additional factor $Z/Z_0$ in $Q/Q_0$, and its inverse in concentration, where $Z$ is compressibility factor.

## Motivation and explanation

Even at fixed temperature and pressure, stoichiometric expansion lowers concentration relative to the constant-flow estimate. Pressure drop and heating lower it further. If $\Delta\nu=0$, total mole flow is constant, but heating or pressure drop can still change volume flow.

The general CSTR expression $V=F_{A0}X_A/(-r_A)$ and PFR differential balance remain valid. Evaluate their rates using (8). A packed bed may also require a pressure-drop equation; prescribing $P=P_0$ is an assumption, not a consequence of the molar balance.

For liquids, an equation of state relating density and composition plays the same role. Constant liquid density is often adequate, but it should be stated.

## Worked example

Take pure A undergoing $A\rightarrow2B$, isothermally at constant pressure, with $-r_A=kC_A$ and $k=0.100$ s$^{-1}$. Here $\epsilon=1$. At $X_A=0.500$, (8) gives $Q/Q_0=1.500$. If $C_{A0}=100$ mol m$^{-3}$, then $C_A=33.3333$ mol m$^{-3}$, compared with the incorrect constant-flow value of $50.0$ mol m$^{-3}$.

Using (8) in the CSTR balance gives

$$
\frac{V}{Q_0}=\frac{X_A(1+\epsilon X_A)}{k(1-X_A)}.
$$

For the PFR, separate the conversion balance:

$$
\frac{V}{Q_0}=\frac{1}{k}\int_0^{X_A}\frac{1+\epsilon x}{1-x}\,dx.
$$

Rewrite the integrand as $(1+\epsilon)/(1-x)-\epsilon$, then integrate each term:

$$
\frac{V}{Q_0}=\frac{-(1+\epsilon)\ln(1-X_A)-\epsilon X_A}{k}.
\tag{9}
$$

At the specified conversion, the inlet-based space times are $15.0$ s for the CSTR and $8.86294$ s for the PFR. Equation (9) reduces to the constant-flow result when $\epsilon=0$. These space times use inlet flow; they are not the gas's actual mean travel times after expansion.

## Link to other topics

In a catalytic gas reactor, partial pressures obtained from these molar flows determine adsorption and surface rates. Coupling conversion to temperature and pressure also couples chemistry to heat transfer and packed-bed fluid mechanics.

## Conclusion

Use conversion to conserve reactant molar flow, then calculate concentration from local volume flow. The next closure is the energy balance that determines local temperature.
<!-- note-content:end -->

[Previous](<RE-02 - Ideal CSTR and PFR balances.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<RE-04 - Coupled mass and energy balances.md>)
