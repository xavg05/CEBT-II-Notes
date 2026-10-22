# RE-27: Thermal effects in catalyst pellets

## Overview

Assume steady pellet mass balances, Fourier heat conduction and Arrhenius kinetics. Internal and external temperature gradients change rate and can produce ignition, extinction and multiple steady states. A small fractional temperature rise must also be checked against Arrhenius sensitivity.

## Intuition

An exothermic pellet can become hotter than its surface, and its surface hotter than the surrounding fluid. Heating accelerates reaction, which generates more heat. Supply and heat removal eventually limit this feedback. An endothermic pellet instead cools and usually reacts more slowly than a calculation at bulk temperature predicts.

## Coupled balance derivation

For a spherical pellet of radius $R_p$, local radius $r$, pore-fluid concentration $C$ and temperature $T$, take constant effective diffusivity $D_e$, constant effective conductivity $\lambda_e$ and disappearance rate $k_V(T)C^n$ per total pellet volume. Let $\Delta H_A$ be reaction enthalpy per mole of reagent consumed, negative for exothermic reaction. Conservation gives

$$D_e\frac1{r^2}\frac d{dr}\left(r^2\frac{dC}{dr}\right)=k_V(T)C^n,
\tag{99}$$

$$\lambda_e\frac1{r^2}\frac d{dr}\left(r^2\frac{dT}{dr}\right)=\Delta H_Ak_V(T)C^n.
\tag{100}$$

The heat equation follows from conduction plus generation $(-\Delta H_A)k_VC^n$: writing steady $\lambda_e\nabla^2T+(-\Delta H_A)k_VC^n=0$ fixes the sign. Centre symmetry requires $C'(0)=T'(0)=0$; surface conditions are $C(R_p)=C_s$ and $T(R_p)=T_s$ when those values are specified. With constant Arrhenius prefactor,

$$\frac{k_V(T)}{k_V(T_s)}=\exp\left[-\frac E{\mathcal R}\left(\frac1T-\frac1{T_s}\right)\right].
\tag{101}$$

Internal effectiveness relative to surface conditions is

$$\eta=\frac{\int_0^{R_p}4\pi r^2 k_V(T(r))C(r)^n\,dr}
{k_V(T_s)C_s^n(4\pi R_p^3/3)}
=3\int_0^1 \rho^2\left(\frac{C}{C_s}\right)^n
\frac{k_V(T)}{k_V(T_s)}\,d\rho,\quad\rho=\frac r{R_p}.
\tag{102}$$

The factor 3 ensures a uniform pellet at $C_s,T_s$ gives $\eta=1$, since $3\int_0^1\rho^2d\rho=1$. Heat-enhanced reaction can outweigh depletion and make $\eta>1$. Nonconstant material properties require conservative equations $\nabla\cdot(D_e\nabla C)$ and $\nabla\cdot(\lambda_e\nabla T)$ rather than pulling coefficients outside derivatives.

## Prater relation and bound

Multiply the concentration equation by $\Delta H_A$ and subtract it from the heat equation. The reaction term cancels, leaving

$$\nabla^2\left[T-\frac{\Delta H_AD_e}{\lambda_e}C\right]=0.
\tag{103}$$

In radial geometry integrate $d[r^2(T'-\alpha C')]/dr=0$, where $\alpha=\Delta H_AD_e/\lambda_e$. The integration constant vanishes by regularity at the centre, so $T'-\alpha C'=0$. Integrating again and imposing surface values gives

$$T-T_s=\frac{\Delta H_AD_e}{\lambda_e}(C-C_s)
=\frac{-\Delta H_AD_e}{\lambda_e}(C_s-C).
\tag{104}$$

Exothermic reaction has $\Delta H_A<0$ and $C<C_s$, hence $T>T_s$. With $C\ge0$, the largest possible internal rise is bounded by

$$T-T_s\le\frac{(-\Delta H_A)D_eC_s}{\lambda_e},\qquad
\beta=\frac{(-\Delta H_A)D_eC_s}{\lambda_e T_s}.
\tag{105}$$

Equality needs complete local depletion; $\beta$ is a maximum possible fractional rise rather than the actual rise everywhere. For exothermic steady operation with $C_s\le C_b$ and $T_s\ge T_b$, a conservative bulk estimate is $\beta\le(-\Delta H_A)D_eC_b/(\lambda_e T_b)$. The relation also applies to other shapes when coefficients are constant and the surface concentration and temperature are uniform. Heterogeneous boundary values need their own boundary-value problem.

An approximate conductivity correlation is $\lambda_e\approx\lambda_s\exp[-1.5\varepsilon_p/(1-\varepsilon_p)]$, with solid conductivity $\lambda_s$ and porosity $\varepsilon_p$. This is an empirical estimate, not universal for all porous composites.

## External heat transfer

Let heat-transfer coefficient $h$ be in $\mathrm{W\,m^{-2}\,K^{-1}}$ and exterior area $A_{\mathrm{ext}}$. For an exothermic pellet at steady state, outward heat removal equals generation:

$$hA_{\mathrm{ext}}(T_s-T_b)=(-\Delta H_A)\dot n_A,
\tag{106}$$

$$T_s-T_b=\frac V{A_{\mathrm{ext}}}
\frac{\eta k_V(T_s)C_s^n(-\Delta H_A)}h.
\tag{107}$$

The same signed equation works for endothermic reaction, when both sides are negative. It predicts a surface temperature below the bulk. For an internally isothermal pellet with negligible external concentration drop,

$$\Omega=\eta\frac{k_V(T_s)}{k_V(T_b)}
=\eta\exp\left[\frac E{\mathcal R}\left(\frac1{T_b}-\frac1{T_s}\right)\right].
\tag{108}$$

If external mass transfer also matters, include $(C_s/C_b)^n$ in this overall effectiveness and solve the mass and heat balances together. For estimating $h$ in an appropriate packed-bed regime, a Wakao-type correlation is $\mathrm{Nu}=2+1.1\mathrm{Re}^{0.6}\mathrm{Pr}^{1/3}$, typically over particle Reynolds numbers around $10$–$10^4$. Here $\mathrm{Nu}=hd_p/\lambda_f$, $\mathrm{Re}=ud_p/\nu$ and $\mathrm{Pr}=\nu/a_f$, with fluid conductivity $\lambda_f$, kinematic viscosity $\nu$, thermal diffusivity $a_f$ and a consistently defined velocity $u$. Check the correlation's velocity and bed conventions before use.

### A small temperature rise can matter kinetically

A fractional temperature bound must be translated into its kinetic effect. With Arrhenius barrier $E=80\ \mathrm{kJ\,mol^{-1}}$, raising temperature from $500$ to $505\ \mathrm K$ gives $k_V(505)/k_V(500)\approx1.20989$. A 1% temperature rise can therefore change intrinsic rate by about 21%. This comparison illustrates sensitivity; the Prater bound alone does not establish that the pellet actually reaches the higher temperature.

## Motivation and explanation

Eliminating the common reaction term in the mass and heat equations works because the same local consumption both removes reagent and releases a fixed enthalpy per mole. The Prater relation consequently links the concentration deficit and temperature rise without needing an explicit rate law. Kinetics are still required to determine how large that deficit becomes; the bound alone is not a predicted centre temperature or proof of isothermal behaviour.

At a thermal steady state, consider a small upward temperature disturbance while other variables follow the reduced model's assumptions. If heat generation increases more than heat removal, the excess heat raises temperature further and the intersection is unstable. If removal increases more, the disturbance is opposed. Reactant depletion and finite supply can bend the generation curve back toward a bounded rate, which helps explain how a hot steady branch can coexist with a cool one without implying indefinite temperature growth.

Internal and external thermal gradients are distinct. A pellet can be internally nearly uniform yet substantially hotter than the gas because gas-film heat transfer is weak. Screening limits such as a fractional rise near 0.02 are rough guides. The local Arrhenius change is better screened by $E\Delta T/(\mathcal RT^2)$; if it is not small, a small relative temperature rise can still change rate appreciably.

Heat-removal rate grows approximately linearly with $T_s-T_b$, while heat generation can grow steeply through Arrhenius kinetics. Their intersections may give a cool branch, an intermediate unstable branch and a hot branch. For a positive thermal capacity, a steady intersection is locally thermally stable in the reduced model when $d\dot Q_{\mathrm{gen}}/dT_s<hA_{\mathrm{ext}}$. Crossing a fold can cause ignition or extinction and hysteresis. Multiple steady states alone do not prove sustained oscillation; oscillations require dynamic analysis and suitable feedback or supply dynamics.

At high temperature, external reactant supply bounds the rate. With $\dot n_A=k_gA_{\mathrm{ext}}(C_b-C_s)$, eliminate rate between mass and heat balances:

$$T_s-T_b=\frac{(-\Delta H_A)k_g}{h}(C_b-C_s)
\le\frac{(-\Delta H_A)k_gC_b}{h}.
\tag{109}$$

The ratio $k_g/h$ cannot be dropped: its units convert molar heat release and concentration into temperature. A heat–mass-transfer analogy can relate $h$ to $\rho c_pk_g$, with appropriate Lewis-number corrections, but $k_g$ and $h$ are not dimensionally equal. For a first-order sphere in the external mass-transfer limit,

$$\Omega\approx\frac{k_gA_{\mathrm{ext}}C_b}{k_V(T_b)VC_b}
=\frac{3k_g}{R_pk_V(T_b)}.
\tag{110}$$

In strong isothermal internal diffusion, by contrast, $\Omega\approx\eta\approx3\sqrt{D_e/k_V}/R_p$. These forms contain different transport coefficients and different powers of intrinsic rate.

## Link to other topics

The pellet's thermal feedback resembles the mass-and-energy coupling of a nonisothermal CSTR. Adsorption and transport temperature dependences must also be included when fitting apparent kinetics.

## Conclusion

Use coupled balances, consistent reference conditions and dimensional heat–mass-transfer relations. Thermal uniformity and kinetic insensitivity are separate checks.
