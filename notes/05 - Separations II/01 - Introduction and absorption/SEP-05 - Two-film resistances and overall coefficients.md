[Previous](<SEP-04 - Operating lines and pinch limits.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-06 - Film models and coefficient measurement.md>)

<!-- note-content:start -->
# SEP-05: Two-film resistances and overall coefficients

## Overview

Assumed background: linear gas–liquid partitioning and film transfer coefficients. Solute must pass through both phases. Adding their resistances on one consistent concentration basis eliminates unknown interfacial concentrations and gives an overall coefficient measurable from bulk streams.

## Intuition

The gas and liquid resistances act in series: the same steady solute flux passes through each. A concentration jump at the interface is compatible with equilibrium because gas and liquid have different molecular environments. Equal chemical potential, not equal concentration, is the interfacial condition.

## Derivation

Let $`C_g,C_l`$ denote bulk solute concentrations and $`C_{gi},C_{li}`$ the corresponding interfacial concentrations, in $`\mathrm{kmol\,m^{-3}}`$. Assume dilute physical absorption, constant properties, no interfacial accumulation and negligible intrinsic resistance to crossing the interface. Interfacial equilibrium gives


**Equation (12)**

```math
C_{gi}=H_cC_{li}.
```


Define gas- and liquid-film coefficients $`k_g,k_l`$ in $`\mathrm{m\,s^{-1}}`$. Conservation of solute at the interface requires the same flux $`N`$ in $`\mathrm{kmol\,m^{-2}\,s^{-1}}`$ through both films:


**Equation (13)**

```math
N=k_g(C_g-C_{gi})=k_l(C_{li}-C_l).
```


Rearrange the gas equation to $`N/k_g=C_g-C_{gi}`$. Multiply the rearranged liquid equation by $`H_c`$ so that both drops use gas concentration: $`NH_c/k_l=C_{gi}-H_cC_l`$. Add the two drops to cancel the unknown interface concentration:


**Equation (14)**

```math
N\left(\frac1{k_g}+\frac{H_c}{k_l}\right)=C_g-H_cC_l.
```


Define $`C_g^*=H_cC_l`$, the gas concentration in equilibrium with the **bulk** liquid, and define the overall coefficient $`K_g`$ through $`N=K_g(C_g-C_g^*)`$. Comparison gives


**Equation (15)**

```math
\frac1{K_g}=\frac1{k_g}+\frac{H_c}{k_l}.
```


For a liquid basis, divide the gas drop by $`H_c`$ and add the unchanged liquid drop. Define $`C_l^*=C_g/H_c`$ to obtain


**Equation (16)**

```math
N=K_l(C_l^*-C_l),\qquad
\frac1{K_l}=\frac1{k_l}+\frac1{H_ck_g},\qquad K_l=H_cK_g.
```


The last identity follows because $`C_g-C_g^*=H_c(C_l^*-C_l)`$ and both expressions must describe the same flux. All four coefficients have velocity units; their inverses have units $`\mathrm{s\,m^{-1}}`$.

To use mole fractions, introduce total molar densities $`\rho_{mg},\rho_{ml}`$ and $`H_c=H_m\rho_{mg}/\rho_{ml}`$. Substitution into equation (13) and the overall laws gives


**Equation (17)**

```math
N=k_g\rho_{mg}(y-y_i)=k_l\rho_{ml}(x_i-x)
=K_g\rho_{mg}(y-y^*)=K_l\rho_{ml}(x^*-x),
```


where $`y_i=H_mx_i`$, $`y^*=H_mx`$, and $`x^*=y/H_m`$. In particular, a mole-fraction-based coefficient such as $`K_g\rho_{mg}`$ has flux units, not velocity units. Its numerical value cannot replace $`K_g`$ without conversion.

The electrical-resistance analogy concerns a common flux and additive driving-force drops. The two physical concentration drops cannot be added directly because they belong to different phases. Multiplying the liquid drop by the partition coefficient expresses its consequence on the gas basis; only then do the interfacial terms cancel. The analogy does not require gas and liquid concentrations to be continuous at the interface.

If one converted resistance is already much larger than the other, reducing the smaller one barely changes their sum. That explains the different improvement priorities in the carbon-dioxide and ammonia examples: the same change in gas agitation can matter greatly in one service and very little in another. Compare converted resistances, not the bare numerical film coefficients.

## Motivation and explanation

Gas-side resistance is $`1/k_g`$ and the liquid resistance converted to the gas basis is $`H_c/k_l`$. Large $`H_c`$ represents weak solubility and tends to make the liquid-side contribution large. Small $`H_c`$ tends to make gas-side resistance dominant. Dominance must be checked from both $`H_c`$ and the coefficients; solubility alone is not enough.

Representative concentration-based values in water around $`20\ ^\circ\mathrm C`$ span a wide range: nitrogen $`H_c\approx60`$, oxygen $`H_c\approx30`$, carbon dioxide $`H_c\approx1.05`$, sulfur dioxide $`H_c\approx9.0\times10^{-3}`$ and ammonia $`H_c\approx4.5\times10^{-4}`$. The progressively smaller ratio means a progressively greater liquid concentration in equilibrium with a given gas concentration, under the chemical conditions implicit in those measurements.

If liquid resistance dominates, $`C_{gi}\approx C_g`$: most of the gas concentration drop is negligible. If gas resistance dominates, $`C_{li}\approx C_l`$: the liquid concentration drop is negligible. Chemical reaction in the liquid, temperature variation, nonlinear equilibrium or appreciable interface resistance require extensions to these constant-coefficient equations.

Use illustrative $`k_g=0.040\ \mathrm{m\,s^{-1}}`$ and $`k_l=2.00\times10^{-4}\ \mathrm{m\,s^{-1}}`$. At approximately $`20\ ^\circ\mathrm C`$ in water, the following partition values illustrate how changing solubility changes control:

| Gas | $`H_c`$ | $`K_g`$ ($`\mathrm{m\,s^{-1}}`$) | $`K_l`$ ($`\mathrm{m\,s^{-1}}`$) | Gas share of total resistance |
|---|---|---|---|---|
| Carbon dioxide | $`1.05`$ | $`1.89573\times10^{-4}`$ | $`1.99052\times10^{-4}`$ | $`0.474\%`$ |
| Ammonia | $`4.5\times10^{-4}`$ | $`0.0366972`$ | $`1.65138\times10^{-5}`$ | $`91.7\%`$ |
| Sulfur dioxide | $`9.0\times10^{-3}`$ | $`0.0142857`$ | $`1.28571\times10^{-4}`$ | $`35.7\%`$ |

Carbon dioxide is liquid-controlled in this illustrative model: improving gas turbulence has little effect on the total resistance. Ammonia is mainly gas-controlled, while sulfur dioxide has meaningful resistance in both phases. Aqueous reactive-species values should be used only with the chemical conditions implicit in their measured equilibrium data.

## Link to other topics

Overall coefficients play the same role as overall heat-transfer coefficients: series resistances are converted to a common driving-force basis. In an absorption column, the operating line provides the bulk compositions and the two-film model converts their disequilibrium into flux.

## Conclusion

Add resistances only after converting them to a consistent basis. Overall coefficients remove inaccessible interfacial compositions while preserving the physical contribution of each film.
<!-- note-content:end -->

[Previous](<SEP-04 - Operating lines and pinch limits.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Next](<SEP-06 - Film models and coefficient measurement.md>)
