[Previous](<AB-33 - Cell removal by filtration — equipment and operation.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Section 34: Dead-end filtration theory and filter sizing

## Intuition

Flow through the filter is driven by the pressure drop and opposed by two resistances in series: the **filter medium** (the cloth, constant) and the **cake** (growing). Flow rate is driving force over resistance, as in any transport problem.

The crucial feature is that the cake resistance is proportional to how much cake there is, and the amount of cake is proportional to how much filtrate has already passed. So the resistance grows in proportion to the volume collected, and the flow rate falls as that volume rises. Integrating a rate that decays with the amount already produced gives a time that scales as **volume squared** — the key result.

*Analogy:* paying off a debt where each payment increases the interest rate. The analogy breaks down because the cake also compresses under pressure, so pushing harder makes the obstacle worse — an effect with no financial equivalent, and the one that produces the surprising result at the end.

## Derivation

Notation: $A$ filter area (m²), $V_f$ filtrate volume (m³), $t$ filtration time (s), $\Delta p$ pressure drop (Pa), $\mu_f$ filtrate viscosity (Pa s), $M_c$ total mass of solids in the cake (kg), $\phi$ average specific cake resistance, $R_M$ filter medium resistance, $c$ mass of solids deposited per unit volume of filtrate (kg m⁻³).

**Step 1: the governing equation.** The filtrate flux (volumetric flow per unit area) equals the driving force divided by the total resistance:
$$\frac{1}{A}\frac{dV_f}{dt} = \frac{\Delta p}{\mu_f\left[\phi\left(\dfrac{M_c}{A}\right) + R_M\right]} \tag{43}$$
The two resistances add because they are **in series**: the liquid passes through the cake and then the medium. The cake term carries $M_c/A$, the mass of solids per unit area, because resistance scales with cake thickness.

**Step 2: relate cake mass to filtrate volume.** Every unit volume of filtrate deposits a fixed mass of solids, so
$$M_c = cV_f \tag{44}$$
This assumes the feed concentration is constant through the run. Substituting into (43):
$$\frac{1}{A}\frac{dV_f}{dt} = \frac{\Delta p}{\mu_f\left[\phi\left(\dfrac{cV_f}{A}\right) + R_M\right]} \tag{45}$$

Here $c$ is defined per volume of filtrate collected, rather than automatically being the solids concentration per volume of incoming broth. Some liquid remains in the wet cake, so these bases can differ appreciably for a concentrated suspension. The laboratory property group and the plant duty must use compatible volume and solids-loading definitions; otherwise an apparently correct area scaling transfers the wrong mass of cake per unit filtrate.

**Step 3: separate variables.** Rearranging (45) to put $V_f$ on one side and $t$ on the other:
$$dt = \frac{\mu_f}{A\Delta p}\left(\frac{\phi c}{A}V_f + R_M\right)dV_f \tag{46}$$

**Step 4: integrate** from $t=0$, $V_f=0$ to $t$, $V_f$. The right-hand side is linear in $V_f$, so the integral gives a quadratic:
$$t = \frac{\mu_f}{A\Delta p}\left(\frac{\phi c}{2A}V_f + R_M\right)V_f \tag{47}$$
The factor of 2 arises from integrating the linear term: the *average* cake resistance over the run is half its final value.

**Step 5: neglect the medium.** Once an appreciable cake has formed, the cloth contributes very little, so $R_M \ll \dfrac{\phi c}{2A}V_f$ and
$$t = \frac{\phi\,c\,\mu_f\,V_f^{\,2}}{2A^2\Delta p} \tag{48}$$

**Checks on (48).** Time rises as $V_f^2$, not $V_f$ — doubling the volume quadruples the time, because the later filtrate passes through a thicker cake. Time falls as $A^2$: doubling the area halves the required filtrate volume per unit area *and* halves the final cake thickness, so the gain is quadratic. More viscous or more concentrated broth takes proportionally longer.

**Step 6: cake compressibility.** Biological cakes are soft, so the cake compacts under pressure and its specific resistance rises:
$$\phi = \phi'\Delta p^{\,s} \tag{49}$$
with $\phi'$ a constant set by particle size and morphology, and $s$ the **cake compressibility** ($s = 0$ incompressible, $s = 1$ fully compressible). Substituting (49) into (48):
$$\boxed{\;t = \frac{\phi'\,c\,\mu_f\,V_f^{\,2}}{2A^2\,\Delta p^{\,1-s}}\;}\tag{50}$$

Rearranged for the design variable, the area:
$$A = \sqrt{\frac{\phi'c\,\mu_f\,V_f^{\,2}}{2t}}\;\Delta p^{\,(s-1)/2} \tag{51}$$

## Motivation and explanation

**What compressibility does to the pressure dependence.** In (50) the pressure appears as $\Delta p^{1-s}$, not $\Delta p$. The exponent on area in (51) is $(s-1)/2$:

| $s$ | Area exponent | Area increase on halving $\Delta p$ |
|---|---|---|
| 0 (incompressible) | −0.5 | ×1.41 |
| 0.5 | −0.25 | ×1.19 |
| 0.8 | −0.10 | ×1.07 |
| 1 (fully compressible) | 0 | ×1.00 |

At $s = 1$ the pressure drops out of the equation entirely: **raising the pressure gains nothing at all**, because the cake compresses in exact proportion to the extra driving force. Real biological cakes sit between these limits, and the weak dependence means pressure is a poor design variable — area is the one that matters, which is why (43) labels $A$ the key parameter.

**The physical picture.** A higher pressure drop squeezes the cake, closing the pores between particles and raising its resistance. The extra driving force is partly cancelled by the extra obstruction. For a soft mycelial or cellular cake this cancellation is substantial.

![Sketch comparing low and high pressure drop: at low Δp the cake is open with good liquid flux; at high Δp the particles are compressed together and flow is impeded](../figs/AB-34-cake-compression.png)

**When (50) fails.** It assumes constant $\Delta p$, constant feed concentration, a cake of uniform properties, and negligible medium resistance. The last fails at the start of a run, when there is no cake, and that is exactly when (48) predicts infinite flux. It also assumes no particles penetrate the medium; if they do, the cloth blinds and $R_M$ rises rather than staying constant.

## Link to other topics

Equation (47) is the standard series-resistance result: a driving force divided by the sum of resistances, integrated when one resistance grows with the extent of the process. Compressibility makes the resistance depend on the driving force itself, which is the same self-limiting feedback seen in fouling and in flow through deformable porous media.

## Summary

Filtration time rises as $V_f^2/A^2$ because cake resistance grows in proportion to the filtrate already collected, so area is the dominant design variable. Cake compressibility weakens the pressure dependence to $\Delta p^{1-s}$, and for the penicillin example at $s = 0.5$ halving the pressure costs only 19 % more area ; the economic choice still depends on area, pumping and equipment costs.

## Conclusion

Cell removal links broth properties to equipment duty, and cake compressibility makes added filtration area more reliable than added pressure. The next unit develops centrifugation.
<!-- note-content:end -->

[Previous](<AB-33 - Cell removal by filtration — equipment and operation.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)
