# RE-01: Rate bases and stoichiometry

## Overview

Assumed: species balances and elementary rate laws from earlier reaction engineering.

A heterogeneous reactor contains more than one phase. Its measured performance can depend on transport between phases as well as chemical reaction. Before writing a balance, specify which species the rate describes, its sign, and whether it is quoted per reactor volume, solid surface area or catalyst mass. These choices change the numerical rate constant without changing the physical reaction.

## Intuition

A solid can be consumed as a reagent, or provide catalytic sites and be regenerated during a reaction cycle. In the catalytic case, reactants must reach the solid, adsorb, react and leave. More catalyst mass does not necessarily mean proportionally more usable sites: some may be inaccessible because of diffusion or deactivation.

Think of a rate basis as a denominator attached to a measurement. “Moles per second per kilogram” cannot enter a volume balance until the kilograms associated with that volume are supplied.

## Derivation

**Step 1: distinguish species rate from reaction rate.** For one reaction, let $\xi$ be the extent in mol and $\nu_i$ the signed stoichiometric coefficient of species $i$ (negative for reactants). Reaction changes its amount $n_i$ according to $dn_i=\nu_i\,d\xi$. Dividing by time and a fixed common basis $B$ gives

$$
r_i=\frac{1}{B}\left(\frac{dn_i}{dt}\right)_{\mathrm{reaction}}=\nu_i r,
\qquad r=\frac{1}{B}\frac{d\xi}{dt}.
\tag{1}
$$

*Reason:* each increment of extent makes or consumes the stoichiometric number of moles. The subscript “reaction” excludes inlet and outlet flows. Thus $r_A$ is negative for a consumed species, even when forward $r$ is positive. With several reactions, sum their contributions: $r_i=\sum_j\nu_{ij}r_j$, where $j$ labels reactions.

**Step 2: convert the basis.** Let $\dot n_{i,\mathrm{reaction}}$ be the total species production in mol s$^{-1}$. For uniform rates on the chosen basis,

$$
\dot n_{i,\mathrm{reaction}}
=r_{i,V}V=r_{i,SA}A_s=r_{i,M}M_{\mathrm{cat}}.
\tag{2}
$$

Here $V$ is the reactor volume used to define $r_{i,V}$, $A_s$ the relevant solid surface area, and $M_{\mathrm{cat}}$ the catalyst mass. Their units are respectively m$^3$, m$^2$ and kg; the corresponding rates have units mol m$^{-3}$ s$^{-1}$, mol m$^{-2}$ s$^{-1}$ and mol kg$^{-1}$ s$^{-1}$.

*Reason:* multiplying by the denominator recovers the same total production. For nonuniform conditions, integrate the local rate over its basis instead. In particular, $r_{i,V}=r_{i,M}(M_{\mathrm{cat}}/V)$ only when the mass-specific rate is uniform. State whether volume means whole bed, void fluid or catalyst solid: these are different denominators.

**Step 3: count active sites.** Turnover frequency $N$ is the number of specified molecular reaction events per active site per second. If $n_{\mathrm{sites}}$ is the amount of active sites in mol, then the corresponding molar event rate is $Nn_{\mathrm{sites}}$.

*Reason:* the molecular-to-molar conversion cancels between events and sites. $N$ has units s$^{-1}$; its interpretation requires a definition and measurement of the active-site population. Apply stoichiometry separately if the event rate is converted into a species rate.

## Motivation and explanation

For $2A\rightarrow3B$, a rate law written as $r=kC_A^2$ gives $r_A=-2kC_A^2$ and $r_B=3kC_A^2$, where $C_A$ is concentration. Rewriting the reaction as $A\rightarrow1.5B$ halves each stoichiometric coefficient. To preserve $r_A$ and $r_B$, the extent-based $r$ and its $k$ must double. A fitted $k$ is therefore incomplete without its rate convention.

For a volume-based $r=kC_A^2$, $k$ has units m$^3$ mol$^{-1}$ s$^{-1}$. For a catalyst-mass-based law with the same concentration dependence, its units become m$^6$ mol$^{-1}$ kg$^{-1}$ s$^{-1}$. Reaction order describes concentration dependence; it does not determine the rate basis.

Gas-phase surface kinetics are often written using partial pressure $P_A$. For an ideal gas, $C_A=P_A/(RT)$, with $R$ the gas constant and $T$ absolute temperature. Replacing concentrations by pressures changes the units and temperature dependence assigned to the fitted coefficient. Adsorption can also produce saturation or inhibition, so a simple power law may hold only over a limited pressure range.

## Worked example

Take $2A\rightarrow3B$ with a volume-based extent rate $r=kC_A^2$, $k=0.0100$ m$^3$ mol$^{-1}$ s$^{-1}$ and $C_A=100$ mol m$^{-3}$. Substitution gives

$$
r=100\ \mathrm{mol\,m^{-3}\,s^{-1}},\qquad
r_A=-200\ \mathrm{mol\,m^{-3}\,s^{-1}},\qquad
r_B=300\ \mathrm{mol\,m^{-3}\,s^{-1}}.
$$

The same species rates follow from $A\rightarrow1.5B$ with $k=0.0200$ m$^3$ mol$^{-1}$ s$^{-1}$. The change is bookkeeping, not faster chemistry.

## Link to other topics

Reactor balances use species production, while reaction heat uses extent rate multiplied by enthalpy per mole of reaction as written. Later, catalyst effectiveness factors connect an intrinsic rate at specified surface conditions to the rate actually achieved inside a porous solid.

## Conclusion

Attach a species, sign and basis to every rate before using it. The next step is to combine that rate with a model of how fluid moves through the reactor.
