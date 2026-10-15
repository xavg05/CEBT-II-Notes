# HETP and theoretical-stage relationships

## Overview

Assumed background: equilibrium-stage stepping and overall gas transfer units. The height equivalent to a theoretical plate, HETP, expresses a packed bed's performance using an equivalent stage count. It is generally different from the height of a transfer unit because stage stepping and continuous rate integration are different constructions.

## Intuition

An equivalent theoretical stage is a performance comparison: the packed bed achieves the same separation as that stage model. It does not mean that the bulk gas and liquid become mutually equilibrated at periodic physical planes inside the bed.

## Derivation

Let $Z$ be packed height and $n$ the equivalent number of theoretical stages for the same equilibrium relationship, flow ratio and inlet/outlet specifications. Define

$$
Z=n\,\mathrm{HETP},\qquad \mathrm{HETP}=\frac Zn. \tag{1}
$$

Assume dilute constant-flow operation with straight equilibrium $y^*=H_mx$ and operating slope $r=L_m/G_m$, where $L_m,G_m$ are liquid/gas molar flows. Define absorption factor $\mathcal A=r/H_m=L_m/(G_mH_m)$; this symbol differs from tower area $A$. Let $\Delta y=y-H_mx$ be the vertical gap between the lines at a passing-stream point.

To derive the stage relation, number ideal stages upwards from the bottom. Gas enters stage $j$ at $y_{j-1}$ and leaves at $y_j$; liquid leaves downwards at $x_j$ and enters from above at $x_{j+1}$. Stage equilibrium gives $y_j=H_mx_j$. The passing points $(x_j,y_{j-1})$ and $(x_{j+1},y_j)$ both lie on the operating line. Consequently,

$$
y_{j-1}-y_j=r(x_j-x_{j+1}),
\qquad \Delta y_j=y_{j-1}-H_mx_j=y_{j-1}-y_j. \tag{2}
$$

For the next stage, $\Delta y_{j+1}=y_j-H_mx_{j+1}=H_m(x_j-x_{j+1})$. Eliminate the liquid difference using equation (2):

$$
\Delta y_j=\mathcal A\Delta y_{j+1},
\qquad \frac{\Delta y_B}{\Delta y_T}=\mathcal A^n. \tag{3}
$$

Each equilibrium step therefore changes the gap by the same factor. The top and bottom points here are the passing-stream endpoints of the whole cascade; extending the recurrence to the terminal liquid inlet gives the indicated ratio. Taking logarithms gives, for $\mathcal A\ne1$,

$$
n=\frac{\ln(\Delta y_B/\Delta y_T)}{\ln\mathcal A}. \tag{4}
$$

This can be a fractional theoretical-stage equivalent. The continuous-contacting integral gives $\mathrm{NTU}_{og}=\ln(\Delta y_B/\Delta y_T)/(1-1/\mathcal A)$. Divide $Z=\mathrm{HTU}_{og}\mathrm{NTU}_{og}$ by equation (4):

$$
\mathrm{HETP}=\mathrm{HTU}_{og}
\frac{\ln\mathcal A}{1-1/\mathcal A}. \tag{5}
$$

As $\mathcal A\to1$, both numerator and denominator vanish. Their first-order expansions both equal $\mathcal A-1$, so the ratio tends to one. Parallel lines have constant force, giving

$$
n=\frac{y_B-y_T}{\Delta y}=\mathrm{NTU}_{og},
\qquad \mathrm{HETP}=\mathrm{HTU}_{og}. \tag{6}
$$

This equality is special to the parallel straight-line case.

One ideal stage imposes equilibrium on leaving streams, which converts the gap from one stage to the next by a multiplicative factor. Continuous contacting instead integrates a local rate over a continuously varying gap. The logarithm of the stage factor and the continuous driving-force integral therefore produce different dimensionless counts even for the same specified separation.

In the worked example, both routes predict the same packed height after each count is multiplied by its own appropriate height measure. The disagreement between the counts is consequently not a conservation error. Using NTU as a tray count would combine the count from one model with the length scale from another.

## Motivation and explanation

HETP depends on transfer effectiveness, hydrodynamics and the operating/equilibrium slopes. It is not purely a geometrical length set by the packing. Empirical values must be applicable to the fluid system and operating range: indicative absorption values can be around $1.5$–$1.8\ \mathrm m$ for some random packings and $0.1$–$0.3\ \mathrm m$ for efficient structured packings, but those ranges are not universal design guarantees. Tray spacing, often of order $0.5\ \mathrm m$, is a hardware distance and should not be identified with a theoretical-stage height without tray efficiency.

If equilibrium is curved or coefficients vary, a single equation (5) cannot generally represent the complete bed. Use actual equilibrium stepping and a suitable rate calculation or validated empirical HETP.

## Worked example

For an illustrative linear absorber with $L_m/G_m=3$, $H_m=2$, $y_B=0.020$, $y_T=0.002$ and fresh solvent, the equilibrium endpoint gap ratio is $4$. Thus $\mathcal A=1.5$, $n=3.41902$ theoretical-stage equivalents and $\mathrm{NTU}_{og}=4.15888$. If $\mathrm{HTU}_{og}=0.600\ \mathrm m$, then $Z=2.49533\ \mathrm m$ and $\mathrm{HETP}=0.729837\ \mathrm m$. The two different dimensionless counts describe the same separation through different models.

## Link to other topics

HETP connects packed-column performance to the equilibrium-stage picture used in distillation and absorption. HTU retains the explicit transport resistance, making it particularly useful when the effect of solvent flow or packing performance must be explained.

## Conclusion

HETP converts a stage-equivalent separation into height. Keep stage count and transfer-unit count distinct, and use their equality only when the straight operating and equilibrium lines are parallel.
