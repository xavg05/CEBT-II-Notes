# RE-20: BET adsorption and surface area

## Overview

Assume monolayer adsorption and geometric series. The Brunauer–Emmett–Teller model extends adsorption to multiple layers and estimates a monolayer capacity from physisorption measurements. That capacity can be converted to accessible area.

## Intuition

The first layer touches the solid; higher layers touch adsorbate. Their binding energies differ. Near saturation pressure, adding layers becomes increasingly similar to condensation, so a monolayer saturation model is inadequate.

## Derivation

Define relative pressure $z=P/P^{\mathrm{sat}}$, where $P^{\mathrm{sat}}$ is vapour saturation pressure at measurement temperature. Let $f_i$ be the fraction of surface columns containing exactly $i$ molecules and $f_0$ the empty fraction. Assume equivalent columns, first-layer equilibrium constant $K_1$, a common higher-layer constant $K_2$, no lateral interactions and unlimited layers. In this model $K_2P=z$, with $K_2P^{\mathrm{sat}}=1$ so unlimited growth occurs at saturation. Define $C=K_1/K_2$.

Successive layer equilibria give $f_1=Czf_0$, $f_2=z f_1$ and generally $f_i=Cz^i f_0$ for $i\ge1$. Normalising the column fractions,

$$1=f_0\left[1+C\sum_{i=1}^{\infty}z^i\right]
=f_0\left[1+\frac{Cz}{1-z}\right].
\tag{61}$$

Hence $f_0=(1-z)/[1+(C-1)z]$. The average number of molecules per column is the total loading divided by monolayer loading, $V/V_m$. Multiplying column fractions by their occupation gives

$$\frac V{V_m}=\sum_{i=1}^{\infty}i f_i
=Cf_0\sum_{i=1}^{\infty}iz^i.
\tag{62}$$

Differentiate $\sum_{i=0}^{\infty}z^i=(1-z)^{-1}$ and multiply by $z$ to obtain $\sum_{i=1}^{\infty}iz^i=z/(1-z)^2$. Substitution gives

$$\frac V{V_m}=\frac{Cz}{(1-z)[1+(C-1)z]}.
\tag{63}$$

Invert and multiply by $z/(1-z)$ to obtain the straight-line form

$$\frac{z}{V(1-z)}=\frac1{V_mC}+\frac{C-1}{V_mC}z.
\tag{64}$$

If fitted intercept is $b$ and slope is $m$, adding them gives $m+b=1/V_m$, so

$$V_m=\frac1{m+b},\qquad C=1+\frac mb.
\tag{65}$$

Both $m$ and $b$ have reciprocal-volume units. If $V$ is gas-equivalent volume at reference pressure $P_{\mathrm{ref}}$ and temperature $T_{\mathrm{ref}}$, monolayer amount is $n_m=P_{\mathrm{ref}}V_m/(\mathcal RT_{\mathrm{ref}})$ for ideal reference gas. With molecular cross-sectional area $a$ and Avogadro constant $N_A$,

$$A_s=n_mN_Aa.
\tag{66}$$

Divide by sample mass to obtain specific surface area. A capacity quoted per mass already produces specific area when converted consistently.

## Motivation and explanation

A BET monolayer capacity counts enough molecules to cover the substrate once; the model does not require every column to contain exactly one molecule at a particular measured pressure. Empty columns and multilayer columns can coexist. Weighting each fraction $f_i$ by $i$ is therefore essential: counting only occupied columns would miss the additional uptake in higher layers.

The transformed straight line separates the two unknowns because adding its slope and intercept removes $C$ and isolates $V_m$. The area calculation then converts gas-equivalent uptake to a molecule count before assigning an area per molecule. Its result describes surface accessible to that probe under measurement conditions. It does not directly count metal active sites or guarantee that the reacting fluid can use the same area in operation.

If first-layer binding is much stronger than condensation-like binding, $C\gg1$ and a pronounced monolayer knee appears. Similar binding strengths give $C$ nearer unity and a less distinct knee. Assuming equal kinetic prefactor ratios, $C\approx\exp[-(\Delta H_1-\Delta H_2)/(\mathcal RT)]$, but fitting $C$ is usually more reliable than predicting it from approximate enthalpies.

![BET loading for different first-layer binding strengths](../figs/RE-20-bet-isotherms.png)

The often useful relative-pressure interval around 0.05–0.35 is a starting guide, not a universal rule. Select a physically sensible linear region before pore filling or capillary condensation dominates. A positive $C$, a sensible inferred monolayer pressure and a consistent fitting interval are necessary checks. Microporous materials and heterogeneous surfaces can yield an apparent BET area whose physical meaning needs qualification. The model's divergence at saturation is not infinite capacity in a finite real specimen; finite pore volume eventually controls uptake.

## Link to other topics

Capillary condensation explains why high-pressure uptake can depart sharply from a multilayer prediction. Surface area alone does not establish the number or accessibility of chemically active catalytic sites.

## Conclusion

BET gives monolayer capacity from a fitted loading curve. Its conversion to area is useful only when reference units, fitting range and pore-filling limitations are explicit.
