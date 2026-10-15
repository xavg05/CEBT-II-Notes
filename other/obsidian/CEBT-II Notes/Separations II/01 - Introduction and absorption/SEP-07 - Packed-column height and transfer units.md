[Previous](<SEP-06 - Film models and coefficient measurement.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-08 - Evaluating NTU and logarithmic driving forces.md>)

<!-- note-content:start -->
# SEP-07: Packed-column height and transfer units

## Overview

Assumed background: operating lines and overall transfer coefficients. A differential solute balance converts local flux into packed height. With approximately constant transport properties, the result separates into a height of a transfer unit and a number of transfer units.

## Intuition

Each thin slice removes a small amount of solute. A large interfacial area or coefficient lets the slice do more work. A small local driving force makes it do less. Height accumulates most rapidly wherever the gas and liquid are close to equilibrium.

## Derivation

Assume steady, dilute, isothermal countercurrent plug flow with constant gas molar flow $G_m$, gas total molar density $\rho_{mg}$, overall concentration-based coefficient $K_g$, and effective wetted area per packed volume $a$. Let $A$ be tower cross-sectional area, $Z$ total packed height, and $z$ a coordinate measured upwards from the bottom. The slice volume is $A\,dz$, so its gas–liquid contact area is $aA\,dz$. Units of $a$ are $\mathrm{m^2\,m^{-3}}$.

At local gas and liquid mole fractions $y,x$, let $y^*=f(x)$ be the gas composition in equilibrium with the bulk liquid. The absorption flux is $N=K_g\rho_{mg}(y-y^*)$. The gas loses solute as it passes upwards, so its balance is

$$
G_m y-N aA\,dz=G_m(y+dy),
\qquad -G_m\,dy=\rho_{mg}K_gaA(y-y^*)\,dz. \tag{23}
$$

Rearrange because the design variable is height, then integrate from bottom $y_B$ to top $y_T$:

$$
Z=\frac{G_m}{\rho_{mg}K_gaA}\int_{y_T}^{y_B}\frac{dy}{y-y^*}
\equiv \mathrm{HTU}_{og}\,\mathrm{NTU}_{og}. \tag{24}
$$

The swapped composition limits remove the negative sign. Define

$$
\mathrm{HTU}_{og}=\frac{G_m}{\rho_{mg}K_gaA},
\qquad \mathrm{NTU}_{og}=\int_{y_T}^{y_B}\frac{dy}{y-y^*}. \tag{25}
$$

The subscript $og$ means overall gas basis. HTU has length units because $G_m/(\rho_{mg}K_gaA)$ combines $\mathrm{kmol\,s^{-1}}$ with $\mathrm{kmol\,m^{-1}\,s^{-1}}$. NTU is dimensionless.

For the liquid balance, liquid entering the slice from above has $x+dx$ and leaves below with $x$. With constant liquid molar flow $L_m$, total molar density $\rho_{ml}$ and overall coefficient $K_l$, conservation gives $L_m dx=-\rho_{ml}K_laA(x^*-x)dz$. Integrating yields

$$
Z=\frac{L_m}{\rho_{ml}K_laA}\int_{x_T}^{x_B}\frac{dx}{x^*-x}
\equiv \mathrm{HTU}_{ol}\,\mathrm{NTU}_{ol}. \tag{26}
$$

Here $x^*=f^{-1}(y)$ and $ol$ denotes overall liquid basis. For linear equilibrium $y^*=H_mx$, the balance gives $dy=(L_m/G_m)dx$ and the driving forces obey $y-y^*=H_m(x^*-x)$. Therefore

$$
\mathrm{NTU}_{og}=\frac{L_m}{G_mH_m}\mathrm{NTU}_{ol},
\qquad \mathrm{HTU}_{og}=\frac{G_mH_m}{L_m}\mathrm{HTU}_{ol}. \tag{27}
$$

Their products give the same height; the individual factors generally differ. At constant pressure and temperature, the gas integral may equivalently use partial pressure $p$ or concentration $C_g$:

$$
\mathrm{NTU}_{og}=\int_T^B\frac{dp}{p-p^*}
=\int_T^B\frac{dC_g}{C_g-C_g^*}. \tag{28}
$$

Constant scaling cancels between each numerator and denominator.

Rearranging the slice balance for $dz$ asks how much additional height is needed to remove a specified small composition increment. The required height is inversely proportional to the local driving force: a narrow gap costs more height for the same decrement in gas composition. Integrating adds those unequal costs rather than assuming that every part of the bed works at its inlet rate.

The HTU–NTU split separates the transport prefactor from the dimensionless integral only after the stated quantities are treated as constant. It does not make either factor universal. Changing packing at fixed flow and composition path primarily changes the prefactor; changing solvent flow also changes the path through the operating line and can change both factors.

## Motivation and explanation

HTU packages transport, wetting and flow per tower area; representative values can be tenths of a metre to around a metre or more. NTU describes separation difficulty **for the chosen operating line**. Changing $L_m/G_m$ changes $x(y)$ and hence the integral, so NTU is not generally independent of flow rates. Packing changes HTU directly; it need not change NTU if the composition specifications, equilibrium and operating line remain fixed.

The effective $a$ is wetted interfacial area, not automatically the packing's geometric surface area. If $K_g$, $a$, density or flow varies significantly, retain them inside the height integral instead of factoring out one constant HTU. A pinch makes the denominator approach zero and produces unbounded height in the limiting ideal model.

## Worked example

For an illustrative design, $\mathrm{HTU}_{og}=0.600\ \mathrm m$ and $\mathrm{NTU}_{og}=4.15888$, giving $Z=2.49533\ \mathrm m$. The NTU describes this separation's driving-force demand; the HTU describes how effectively the chosen equipment supplies it. Neither factor alone is a count of trays.

## Link to other topics

The operating line and equilibrium curve determine the integral; transport correlations determine the prefactor. This separation parallels heat-exchanger sizing, where available conductance and required thermal driving forces enter different parts of the calculation.

## Conclusion

Derive height from the local balance and evaluate the driving force throughout the tower. The HTU–NTU product is convenient when the transport prefactor is approximately constant.
<!-- note-content:end -->

[Previous](<SEP-06 - Film models and coefficient measurement.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-08 - Evaluating NTU and logarithmic driving forces.md>)
