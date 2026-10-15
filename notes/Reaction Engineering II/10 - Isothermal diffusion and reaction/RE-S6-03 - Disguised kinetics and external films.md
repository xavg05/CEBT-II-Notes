[Previous](<RE-S6-02 - Isothermal pellet profiles and effectiveness.md>) · [Subject index](../README.md) · [Topic overview](README.md)

<!-- note-content:start -->
# Disguised kinetics and external films

## Overview

Assume the definition of pellet effectiveness and steady diffusion. Nonlinear intrinsic kinetics and external mass-transfer resistance change the rate seen by the reactor. The apparent order and activation energy can therefore differ from the chemical rate law.

## Intuition

Increasing reaction speed shortens the penetration depth. Under strong internal diffusion limitation, more active catalyst does not translate proportionally into more total consumption. An external film can reduce the surface concentration further before reagent enters the pellet.

## Derivation of the strong-diffusion limit

Let intrinsic disappearance rate be $`k_VC^n`$ per pellet volume, with $`n\ge0`$, constant $`D_e`$ and uniform temperature. When penetration is thin compared with pellet dimensions, approximate a locally flat semi-infinite layer. Let coordinate $`x`$ point inward from the surface. The balance is $`D_eC''=k_VC^n`$. Multiply by $`C'`$ and integrate from a depleted interior where $`C=C'=0`$ to any position:


**Equation (76)**

```math
\frac{D_e}{2}(C')^2=\frac{k_V}{n+1}C^{n+1}.
```


The inward gradient is negative. Taking its magnitude at $`C=C_s`$ gives inward flux


**Equation (77)**

```math
J_s=\sqrt{\frac{2D_ek_V}{n+1}}C_s^{(n+1)/2},\qquad
\dot n_A\approx A_{\mathrm{ext}}J_s.
```


Dividing by the fully supplied intrinsic rate $`k_VC_s^nV`$ gives the reciprocal of a generalised modulus,


**Equation (78)**

```math
\phi_{n,\mathrm{gen}}=\frac V{A_{\mathrm{ext}}}
\sqrt{\frac{(n+1)k_VC_s^{n-1}}{2D_e}},\qquad
\eta\approx\frac1{\phi_{n,\mathrm{gen}}}.
```


For $`n=1`$ this agrees with the common first-order definition. At small modulus, the concentration is nearly uniform and $`\eta\to1`$. At strong limitation, measured order with respect to $`C_s`$ is $`(n+1)/2`$, because that is the exponent in the flux. Second-order intrinsic reaction therefore appears order 1.5. Changing $`C_s`$ also changes modulus for $`n\ne1`$; a constant effectiveness cannot be imposed while varying concentration.

Because strong-limitation rate is proportional to $`\sqrt{D_ek_V}`$, an Arrhenius intrinsic constant with barrier $`E`$ gives approximately $`E/2`$ apparent barrier if $`D_e`$ has weak temperature dependence. If $`D_e`$ itself has an activated temperature dependence with energy $`E_D`$, the apparent barrier becomes approximately $`(E+E_D)/2`$. Temperature-dependent adsorption or external concentration adds further effects. Measured order with respect to **bulk** concentration equals this surface-based result only when $`C_s`$ tracks the bulk proportionally.

Zero-order kinetics require care. A fully supplied slab has $`C=C_s-k_V(L^2-x^2)/(2D_e)`$. If this predicts negative centre concentration, reaction cannot remain zero order through the entire pellet; a depleted dead region and moving penetration boundary must replace the unphysical continuation. Other power laws generally require numerical pellet solutions away from limiting regimes.

## External mass-transfer derivation

Let $`C_b`$ be bulk concentration and $`k_g`$ film mass-transfer coefficient in $`\mathrm{m\,s^{-1}}`$. For an isothermal first-order pellet, steady external supply equals internal consumption:


**Equation (79)**

```math
k_gA_{\mathrm{ext}}(C_b-C_s)=\eta k_VVC_s.
```


Rearranging gives


**Equation (80)**

```math
C_s=\frac{C_b}{1+\eta k_VV/(k_gA_{\mathrm{ext}})},\qquad
\dot n_A=\frac{\eta k_VVC_b}{1+\eta k_VV/(k_gA_{\mathrm{ext}})}.
```


Define overall effectiveness $`\Omega=\dot n_A/(k_VVC_b)`$, using bulk conditions rather than surface conditions. Then


**Equation (81)**

```math
\Omega=\frac\eta{1+\eta k_VV/(k_gA_{\mathrm{ext}})}.
```


The dimensionless ratio $`\eta k_VV/(k_gA_{\mathrm{ext}})`$ compares internal consumption capacity with film supply capacity. When small, $`C_s\approx C_b`$ and $`\Omega\approx\eta`$. When large, $`\dot n_A\approx k_gA_{\mathrm{ext}}C_b`$, independent of intrinsic first-order constant. If $`\eta\to1`$ but the film remains important, $`\Omega`$ remains below one: a uniformly supplied interior relative to its own surface does not imply that the surface equals the bulk.

## Motivation and explanation

Multiplying the diffusion–reaction equation by $`C'`$ turns curvature times gradient into the derivative of a squared gradient. Integration then links the surface gradient directly to concentration and reaction strength, without first finding the complete profile. In the thin reacting layer, faster chemistry steepens the gradient but also shortens penetration; the resulting flux grows less strongly than the fully supplied intrinsic rate. That loss of accessible depth is what disguises order and activation energy.

The film balance places two demands on the same unknown $`C_s`$: the exterior supplies through $`C_b-C_s`$, while the interior consumes in proportion to $`C_s`$ for this first-order isothermal model. Stronger internal demand lowers $`C_s`$ until the rates agree. Thus a high internal effectiveness can coexist with a poor overall effectiveness: the whole pellet may be nearly uniform at a surface concentration already well below the bulk. Nonlinear kinetics require solving this balance with the concentration-dependent internal solution.

Reducing particle size improves internal supply and raises exterior area per volume, but increases packed-bed pressure drop and may complicate separation. Changing fluid velocity affects $`k_g`$ and possibly wetting. Such experiments help diagnose transport limitations, while intrinsic kinetics need measurements in a regime where transport is demonstrably adequate.

## Worked example

For an illustrative sphere with $`R_p=1\ \mathrm{mm}`$, $`k_V=1\ \mathrm{s^{-1}}`$, $`D_e=2.5\times10^{-7}\ \mathrm{m^2\,s^{-1}}`$ and $`k_g=10^{-3}\ \mathrm{m\,s^{-1}}`$, raw spherical modulus is 2 and $`\eta=0.805972`$. Since $`V/A_{\mathrm{ext}}=R_p/3`$, Python gives $`C_s/C_b=0.788235`$ and $`\Omega=0.635295`$. Replacing $`C_s`$ by $`C_b`$ would overstate the actual rate.


## Link to other topics

The same surface film must carry reaction heat, potentially moving the pellet away from bulk temperature. Transport can conceal both coverage effects and intrinsic activation energy.

## Conclusion

Apparent kinetics combine chemical consumption with supply. Use surface conditions for internal effectiveness and bulk conditions for overall effectiveness.
<!-- note-content:end -->

[Previous](<RE-S6-02 - Isothermal pellet profiles and effectiveness.md>) · [Subject index](../README.md) · [Topic overview](README.md)
