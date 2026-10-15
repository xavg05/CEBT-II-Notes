# Graphical calculation of drying time

## Overview

Experimental drying curves provide the local rate when a simple equation does not. Combine the operating line with a family of rate curves, then integrate reciprocal rate against solid moisture. Every construction step represents either conservation or the measured material response.

Assumptions: experimental curves represent the same material geometry, gas velocity and applicable gas-property range as the proposed dryer.

## Intuition

*A small moisture interval takes a long time wherever its drying rate is small.* The reciprocal-rate plot turns those slow regions into large areas. An inlet pinch and a near-equilibrium outlet can both dominate total time.

## Derivation

Let $w$ be kg liquid/kg dry solid and $r=-dw/dt>0$. Rearrangement gives $dt=-dw/r$. Integrating from inlet $w_1$ to smaller outlet $w_2$,

$$
t=\int_{w_2}^{w_1}\frac{1}{r(w)}\,dw.
\tag{1}
$$

For countercurrent air/water with constant $H^W$, dry-gas/dry-solid ratio $m$ and inlet-gas driving force $\Delta H_2$,

$$
\Delta H(w)=\Delta H_2-\frac{w-w_2}{m}.
\tag{2}
$$

Equation (2) is a balance, not a drying-rate relation. A measured family $r=f(w,\Delta H)$ supplies the second ingredient. Together they determine

$$
r(w)=f\!\left(w,\Delta H_2-\frac{w-w_2}{m}\right).
\tag{3}
$$

For tabulated points ordered $w_2=w^{(0)}<w^{(1)}<\cdots<w^{(n)}=w_1$, trapezoidal integration gives

$$
t\approx\sum_{i=0}^{n-1}
\frac{w^{(i+1)}-w^{(i)}}{2}
\left(\frac{1}{r_i}+\frac{1}{r_{i+1}}\right).
\tag{4}
$$

The superscript labels table points, while $r_i$ is the rate at point $i$. Each positive area contributes time. Use rate in s⁻¹ or h⁻¹ consistently with the time unit and recorded material basis.

## Motivation and explanation

![Experimental drying-rate family and critical-moisture locus](../figs/u2-drying-rate-family.png)

Construct the result as follows:

1. Choose moisture points between both endpoints, with extra points near a regime transition or low-rate region. These resolve the part of the integral that can contribute most time.
2. Calculate $\Delta H$ from the operating line at each point. This establishes the local gas state paired with the solid.
3. On the experimental family, read the rate at that $(w,\Delta H)$ pair. Interpolate between adjacent humidity curves only inside their measured range.
4. Tabulate $w,\Delta H,r,1/r$. Plot $1/r$ against increasing $w$ and integrate its positive area.
5. Refine the table and check sensitivity to graph-reading uncertainty. A low rate makes both residence time and relative error large.

The shown chart ends at $w=0.5$ kg/kg. It cannot alone calculate a complete path beginning at $w=0.9$ without additional measured data or a justified model. Some listed humidity-family values also lie outside a particular operating path; retain only points actually reached within the target interval.

## Worked example

To check the integration method independently of graph-reading uncertainty, use the specified analytical model

$$
r(w)=\min\{10(0.01325-0.0125w),\,0.5w\}
$$

on $0.1\le w\le0.9$, with time in hours. This table is generated from that model, not digitised from the figure:

| $w$ (kg/kg) | $\Delta H$ (kg/kg) | $r$ (kg/kg per h) | $1/r$ (h per unit $w$) |
|---|---|---|---|
| 0.100 | 0.01200 | 0.050 | 20.00 |
| 0.212 | 0.01060 | 0.106 | 9.434 |
| 0.500 | 0.00700 | 0.070 | 14.29 |
| 0.900 | 0.00200 | 0.020 | 50.00 |

Trapezoidal integration with 8, 80 and 800 equal intervals gives 15.232, 14.849 and 14.845 h respectively. The analytical result is 14.8445 h. Refinement tests numerical quadrature; it does not improve experimental accuracy or establish a material law.

## Link to other topics

Reciprocal-rate integration is the same residence-time construction used when reaction rates vary along a reactor. Here the rate is read from a two-variable drying response combined with a conservation line.

## Conclusion

The graphical method separates the operating balance from experimental kinetics and makes slow regions visible. Other solvents require one more local calculation because their wet-bulb reference can vary along the gas path.
