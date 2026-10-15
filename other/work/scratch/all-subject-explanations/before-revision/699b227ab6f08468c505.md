# Binary gas membrane selectivity

## Overview

Assumed knowledge: ideal-gas partial pressures and membrane permeance.

A selective gas membrane enriches the more permeable component in the permeate. This note derives the local binary composition relation and shows why finite permeate pressure imposes a purity limit even when the membrane has very high selectivity.

## Intuition

A component crosses because its partial pressure is higher on the feed side. Enrichment raises its permeate-side partial pressure and therefore opposes further passage. Improving material selectivity cannot overcome a vanishing driving force.

## Derivation

Take a binary ideal gas containing components $A$ and $B$. Let $x$ be the feed-side mole fraction of $A$, $y_i$ the mole fraction of $A$ in the locally emerging permeate, and $P_f$, $P_p$ the absolute pressures. Assume constant permeances $K_{m,A}$, $K_{m,B}$, isothermal conditions and negligible external film resistance.

The following local relation applies when the permeate at the selective layer has composition $y_i$. It describes a small isolated membrane patch, and can also describe an asymmetric membrane whose porous support prevents mixing of emerging gas with permeate already collected downstream. It does not automatically apply when the selective layer directly contacts an accumulated mixed permeate channel.

Partial-pressure driving forces give

$$
N_A=K_{m,A}(P_fx-P_py_i),\qquad
N_B=K_{m,B}[P_f(1-x)-P_p(1-y_i)]. \tag{1}
$$

Define $\gamma=P_p/P_f$ and $\alpha=K_{m,A}/K_{m,B}$. Both fluxes have the same molar basis, so the composition of gas newly crossing is its component flux divided by total flux:

$$
y_i=\frac{N_A}{N_A+N_B}
=\frac{\alpha(x-\gamma y_i)}{\alpha(x-\gamma y_i)+1-x-\gamma+\gamma y_i}. \tag{2}
$$

Multiply by the denominator to remove the fraction:

$$
y_i[\alpha x-\alpha\gamma y_i+1-x-\gamma+\gamma y_i]
=\alpha x-\alpha\gamma y_i.
$$

Move the right-hand side to the left and collect powers of $y_i$:

$$
\gamma(1-\alpha)y_i^2+
[1-\gamma+(\alpha-1)x+\alpha\gamma]y_i-\alpha x=0.
$$

Multiplying by $-1/\gamma$, for $\gamma>0$, gives the standard quadratic

$$
(\alpha-1)y_i^2+
\left[1-\alpha-\frac1\gamma-\frac{(\alpha-1)x}{\gamma}\right]y_i
+\frac{\alpha x}{\gamma}=0. \tag{3}
$$

Choose the root in $0\le y_i\le1$ that gives physically permitted component flux directions. A second algebraic root outside this range is not a possible composition.

When $P_p/P_f\to0$, use Equation (2) directly because Equation (3) divides by $\gamma$. Neglecting permeate partial pressures gives

$$
y_i=\frac{\alpha x}{1+(\alpha-1)x}. \tag{4}
$$

## Motivation and explanation

At $\alpha=1$, the membrane has no intrinsic preference and $y_i=x$. For $\alpha>1$ and positive forward flux, $A$ becomes enriched. Equation (4) resembles the relative-volatility expression for vapour–liquid equilibrium, but its origin is a ratio of transport rates rather than phase equilibrium.

For finite permeate pressure, $N_A>0$ requires $x-\gamma y_i>0$. Thus

$$
y_i<\frac{x}{\gamma}. \tag{5}
$$

Together with $y_i\le1$, this limits attainable purity. In the high-selectivity limit, $y_i$ tends towards the smaller of $1$ and $x/\gamma$. At the pressure-limited boundary the driving force for $A$ approaches zero; the limiting composition is approached rather than obtained at useful finite flux.

![Permeate composition versus selectivity at different pressure ratios](../figs/u3-04-gas-selectivity.png)

To use the graph, first select feed composition $x$, then choose the pressure-ratio curve, then read $y_i$ at the membrane selectivity. The reason for this order is that neither selectivity nor pressure ratio alone determines enrichment. Values read from the graph are estimates; Equation (3) gives the calculation.

## Worked example

Take oxygen as $A$ and approximate air as a binary mixture with $x=0.209$. For $\alpha=5$, $P_f=10\,\mathrm{bar(a)}$ and $P_p=1\,\mathrm{bar(a)}$, $\gamma=0.1$. Equation (3) becomes

$$
4y_i^2-22.36y_i+10.45=0.
$$

Its physical root is $y_i=0.514753$, so the newly permeating gas is about $51.5\%$ oxygen. At a retentate composition $x=0.05$, the quadratic is $4y_i^2-16y_i+2.5=0$, giving $y_i=0.162883$. The downstream local gas is still enriched relative to its local feed, even though its oxygen fraction is below that of the original air.

## Link to other topics

The purity limit is a chemical-potential driving-force limit, similar to an absorption pinch. A complete module design must combine this local transport relation with the changing feed flow and composition.

## Conclusion

Binary enrichment depends jointly on membrane selectivity and pressure ratio. The local flux composition is useful for design only when the permeate-side interfacial mixing assumption is stated explicitly.
