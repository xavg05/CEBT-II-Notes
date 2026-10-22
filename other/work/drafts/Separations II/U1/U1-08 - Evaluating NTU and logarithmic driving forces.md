# Evaluating NTU and logarithmic driving forces

## Overview

Assumed background: the packed-column height balance. Both the actual gas composition $y$ and its equilibrium counterpart $y^*$ change along the tower. Evaluate that relationship explicitly before integrating; straight operating and equilibrium lines give a logarithmic expression, while curved data require numerical integration.

## Intuition

The equilibrium counterpart depends on the liquid **at the same height**. It cannot be held at one inlet or outlet value throughout the column. The integral weights difficult locations by the reciprocal driving force, so a narrow region near a pinch can contribute much of the required height.

## Derivation

For a dilute absorber with constant gas/liquid molar flows $G_m,L_m$, the operating line is $y-y_T=(L_m/G_m)(x-x_T)$. For linear equilibrium $y^*=H_mx$, define $y_T^*=H_mx_T$. Replace $x$ and $x_T$ because we want $y^*$ as a function of integration variable $y$:

$$
y^*=y_T^*+q(y-y_T),\qquad q=\frac{G_mH_m}{L_m}. \tag{1}
$$

Subtract this counterpart from the actual gas composition:

$$
\Delta y\equiv y-y^*=(1-q)y+q y_T-y_T^*
=\alpha y+\beta, \tag{2}
$$

where $\alpha=1-q$ and $\beta=q y_T-y_T^*$. For $\alpha\ne0$, integrate using $d(\alpha y+\beta)=\alpha\,dy$:

$$
\mathrm{NTU}_{og}=\int_{y_T}^{y_B}\frac{dy}{\alpha y+\beta}
=\frac1{1-q}\ln\left(\frac{\Delta y_B}{\Delta y_T}\right). \tag{3}
$$

Here $\Delta y_B=y_B-y_B^*$ and $\Delta y_T=y_T-y_T^*$ are the positive endpoint driving forces. If $q=1$, the two lines are parallel and the driving force is constant, giving

$$
\mathrm{NTU}_{og}=\frac{y_B-y_T}{\Delta y}. \tag{4}
$$

This is the limit of equation (3), not a failure of the physical model.

Since equation (2) is linear, $\Delta y_B-\Delta y_T=(1-q)(y_B-y_T)$. Substitute this identity into equation (3) to define the logarithmic mean:

$$
(\Delta y)_{\mathrm{lm}}=
\frac{\Delta y_B-\Delta y_T}{\ln(\Delta y_B/\Delta y_T)},
\qquad \mathrm{NTU}_{og}=\frac{y_B-y_T}{(\Delta y)_{\mathrm{lm}}}. \tag{5}
$$

With equal endpoint forces, use their common value. Multiply the height balance $Z=G_m\mathrm{NTU}_{og}/(\rho_{mg}K_gaA)$ by $\rho_{mg}K_gaA$ and use the whole-column transfer rate $Q_m=G_m(y_B-y_T)$:

$$
Q_m=\rho_{mg}K_gaAZ(\Delta y)_{\mathrm{lm}}. \tag{6}
$$

Here $\rho_{mg}$ is gas total molar density, $K_g$ the concentration-based overall coefficient, $a$ wetted area per packed volume and $A$ tower area. Equation (6) requires constant prefactor and straight operating/equilibrium lines.

For curved equilibrium, construct the integral rather than imposing equation (5): choose trial $y$ values, solve the operating line for $x$, read or interpolate $y^*=f(x)$, then evaluate $1/(y-y^*)$. Plotting this reciprocal against $y$ gives an area equal to NTU. Refine the grid particularly near the clean-gas end or a pinch because the integrand can change quickly there. Repeat the calculation at finer spacing until the answer stabilises. A fixed minimum number of points is only a starting grid, not an accuracy guarantee.

The logarithm comes from integrating the reciprocal of a linearly changing driving force. A small-force end is expensive because the reciprocal weights it strongly, so an arithmetic average of the endpoint forces gives too much credit to the favourable end. The log mean packages that exact integral into one effective force for the linear case; it is not a preferred average chosen independently of the balance.

When the two endpoint forces coincide, the physical problem is regular: every slice has the same force. The apparent zero divided by zero is a feature of the logarithmic expression, so taking its limit must recover the ordinary composition change divided by that common force. Curved equilibrium requires the actual intervening profile, not just this endpoint check.

## Motivation and explanation

The logarithmic mean is lower than an arithmetic mean for unequal positive forces, reflecting the disproportionate cost of weak driving-force regions. Using only endpoint forces for a curved equilibrium relationship overlooks interior curvature and can misestimate height even when endpoints are correct.

Individual-film transfer units can also be defined. Let $\mathrm{HTU}_g=G_m/(\rho_{mg}k_gaA)$ and $\mathrm{HTU}_l=L_m/(\rho_{ml}k_laA)$, where $\rho_{ml}$ is liquid total molar density and $k_g,k_l$ are individual concentration-based coefficients. Insert $1/K_g=1/k_g+H_m\rho_{mg}/(\rho_{ml}k_l)$ into the overall HTU definition:

$$
\mathrm{HTU}_{og}=\mathrm{HTU}_g+q\,\mathrm{HTU}_l,
\qquad \mathrm{HTU}_{ol}=\mathrm{HTU}_l+\frac1q\mathrm{HTU}_g. \tag{7}
$$

The liquid expression follows by the same resistance conversion. Individual-film NTUs involve $y-y_i$ or $x_i-x$ and require interfacial compositions; overall coefficients usually make design simpler.

A small endpoint driving force carries disproportionate weight because height integrates its reciprocal. Arithmetic averaging can therefore underestimate the required height. For the linear absorber model, the log mean follows from that integral; curved equilibrium requires the actual intervening profile rather than an endpoint average.

## Link to other topics

Logarithmic driving-force integration has the same mathematical origin as the log-mean temperature difference in a heat exchanger. Equilibrium-stage counts use a different geometric progression, which explains why NTU generally differs from the number of theoretical stages.

## Conclusion

Use the logarithmic expression for linear profiles and the constant-force limit for parallel lines. With curved data, integrate the actual operating–equilibrium gap and demonstrate numerical convergence.
