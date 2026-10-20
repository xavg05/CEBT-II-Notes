[Previous](<AB-36 - Stokes settling and the throughput of a tubular bowl centrifuge.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Section 37: Sigma theory and centrifuge scale-up

## Intuition

To compare two centrifuges fairly, they must be compared on the same feed. If a figure of merit could be found that depends only on the machine, then the ratio of throughputs of any two centrifuges on *any* common sample would equal the ratio of those figures — and scale-up would reduce to matching one number.

The trick is to notice that the sample's properties enter $`Q_{\text{cut}}`$ only through the combination that forms the **gravitational settling velocity** $`u_g`$. Multiplying and dividing by $`u_g`$ therefore isolates everything else, and what remains is the machine.

The machine factor has units of area. With the convention used here, $`Q_{\text{cut}}=2\Sigma u_g`$, the corresponding ideal gravity-settler area is $`A_{\mathrm{eq}}=Q_{\text{cut}}/u_g=2\Sigma`$. Thus $`\Sigma=32.4`$ m² corresponds to about 64.8 m² of gravity-settling area for the same stated capture criterion.

*Analogy:* expressing a device's performance as the equivalent area of a simpler separator. The comparison is conditional on matching feed, capture criterion and ideal flow assumptions; it does not make real centrifuge scale-up exact.

## Derivation

**Step 1: start from the cut-off flow rate.** From Section 36, equation (61):

**Equation (62)**

```math
Q_{\text{cut}} = \frac{D_p^2(\rho_p-\rho_l)\omega^2}{18\mu\,\ln\!\left(\dfrac{2r_2}{r_1+r_2}\right)}\,\pi(r_2^2-r_1^2)h
```


**Step 2: multiply and divide by $`u_g`$.** The gravitational settling velocity of the same particle is

**Equation (63)**

```math
u_g = \frac{D_p^2(\rho_p-\rho_l)g}{18\mu}
```

Writing (62) as itself multiplied by $`u_g/u_g`$ and substituting (63) in the denominator, the whole group $`D_p^2(\rho_p-\rho_l)/18\mu`$ cancels, leaving $`g`$ behind:

**Equation (64)**

```math
Q_{\text{cut}} = \frac{\pi(r_2^2-r_1^2)h\,\omega^2}{g\,\ln\!\left(\dfrac{2r_2}{r_1+r_2}\right)}\;u_g
```


**Step 3: define $`\Sigma`$.** Writing (64) as $`Q_{\text{cut}} = 2\Sigma u_g`$:

**Equation (65)**

```math
\boxed{\;\Sigma(r_1,r_2,h,\omega) = \frac{\pi(r_2^2-r_1^2)h\,\omega^2}{2g\,\ln\!\left(\dfrac{2r_2}{r_1+r_2}\right)}\;}
```


Two properties follow immediately:
- **$`\Sigma`$ depends only on the centrifuge**, not on the sample. Every sample-dependent quantity has been collected into $`u_g`$.
- **$`\Sigma`$ has dimensions of area.** Dimensionally $`Q = 2\Sigma u_g`$ is (volume/time) = (area)(velocity), so the equivalent ideal gravity-settler area at this throughput is **$`2\Sigma`$**, under the stated $`Q_{\text{cut}}=2\Sigma u_g`$ convention.

**Step 4: the scale-up rule.** For two centrifuges processing the **same sample**, $`u_g`$ is common:

```math
Q_1 = 2\Sigma_1 u_g, \qquad Q_2 = 2\Sigma_2 u_g
```

Dividing, $`u_g`$ cancels:

**Equation (66)**

```math
\frac{Q_1}{Q_2} = \frac{\Sigma_1}{\Sigma_2}
```


Matching $`Q/\Sigma`$ matches the ideal settling challenge imposed on the feed under the same area convention. It is useful because the unknown particle settling velocity cancels from the comparison. That cancellation fails if upstream handling changes the cells: flocculation increases effective particle size, while disruption or a viscosity change alters settling. Such changes belong to the feed factor and cannot be absorbed into the geometric machine factor.

**To increase the throughput of a centrifuge by a factor $`X`$, $`\Sigma`$ must increase by the same factor $`X`$.** This ideal ratio requires the same feed settling properties, capture criterion and flow assumptions; real machines can need empirical efficiency corrections.

## Motivation and explanation

**The area factor depends on the design and convention.** Equation (65) uses $`Q=2\Sigma u_g`$. For a disc stack, state the full equivalent area $`A_{\mathrm{eq,disc}}`$, defined by $`Q=A_{\mathrm{eq,disc}}u_g`$:

**Equation (67)**

```math
A_{\mathrm{eq,disc}} = \frac{2\pi\omega^2(N-1)}{3g\tan\theta}\left(r_2^3-r_1^3\right)
```

with $`N`$ the number of discs, $`r_2`$ and $`r_1`$ the outer and inner disc radii and $`\theta`$ the disc angle to the rotation axis. Under the half-area convention of (65), use $`\Sigma_{\mathrm{disc}}=A_{\mathrm{eq,disc}}/2`$.

![A disc-stack centrifuge showing the feed, overflow, disc radius r, half-cone angle θ, and solids collecting at the bowl wall](../figs/AB-37-disc-stack-geometry.png)

Equation (67) explains the throughput figures in Section 35. $`\Sigma`$ scales with $`(N-1)`$, so a stack of a hundred discs has roughly a hundred times the equivalent area of a single surface, and it scales with $`r^3`$ rather than $`r^2`$. That is how a disc stack delivers 800 L/min at only 5500 g while a tubular bowl at 15 000 g manages 80 L/min — **equivalent settling area, which includes the rotation speed, sets the ideal throughput for a given feed and capture criterion.**

**$`\Sigma`$ is convention-dependent.** The derivation of $`t_{\text{cut}}`$ took a particle starting at the mid-point of the liquid layer, which is somewhat arbitrary. Different conventions give different expressions; another in common use is

**Equation (68)**

```math
\Sigma = \frac{\pi\omega^2 h}{2g}\left(3r_2^2+r_1^2\right)
```

For the example below, (68) gives 35.4 m² against 32.4 m² from (65), about 9 % higher. Quote the value with its definition and capture criterion. Their difference is not merely a universal prefactor: it depends on the radius ratio, so scale-up ratios calculated from different geometric expressions need not agree for dissimilar bowls.

**When ratios are robust.** A common constant prefactor cancels from a ratio. Both tubular-bowl expressions also scale as $`L^3\omega^2`$ for geometrically similar bowls, so they give the same speed ratio in the doubled-size example. Dissimilar geometries require matched capture criteria, and real scale-up requires checking flow and separation-efficiency corrections.

## Link to other topics

Expressing a device's performance as an equivalent area of a simpler device is the same move as the HETP of a distillation column or the NTU of a heat exchanger: a dimensional figure of merit that separates equipment performance from the properties of what passes through it, so that scale-up becomes a matter of matching one number.

## Summary

Factorising $`Q_{\text{cut}}=2\Sigma u_g`$ separates the ideal machine factor from the feed settling velocity. In this convention the equivalent gravity-settler area is $`2\Sigma`$.

## Conclusion

Sigma theory supports scale-up when feed properties, separation criteria and geometric conventions remain consistent. The next unit develops cell disruption.
<!-- note-content:end -->

[Previous](<AB-36 - Stokes settling and the throughput of a tubular bowl centrifuge.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)
