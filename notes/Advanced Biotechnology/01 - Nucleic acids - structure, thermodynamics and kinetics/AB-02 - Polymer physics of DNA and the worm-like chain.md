[Previous](<AB-01 - Chemistry and structure of DNA and RNA.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-03 - Two-state hybridisation and DNA melting.md>)

<!-- note-content:start -->
# Section 02: Polymer physics of DNA and the worm-like chain

## Intuition

Follow the chain along its contour. Thermal kicks bend it a little at every point. Over a short distance the bends are small and the chain still "remembers" which way it was pointing. Over a long distance the small bends add up and the direction is forgotten. The persistence length is the distance over which the memory fades. A stiff chain (dsDNA) remembers over about 50 nm; a floppy one (ssDNA) over about 1–2 nm.

*Analogy:* a cooked spaghetti strand (ssDNA) against a garden hose (dsDNA). Both are straight over short lengths and curve over long ones; the hose just needs a longer length before it turns round. The analogy breaks down because the bending here is driven by thermal motion, not gravity or handling, and the stiffness measured as $`l_P`$ scales with $`1/T`$.

## Derivation

Notation: $`s`$ is the arc length along the chain, $`\hat t(s)`$ is the unit tangent at $`s`$, $`L`$ is the contour length, and $`\vec R = \int_0^L \hat t\,ds`$ is the end-to-end vector.

**Step 1: bending energy.** A rod with bending stiffness $`\kappa`$ (units J·m) stores energy proportional to the square of its curvature, just as a spring stores energy proportional to the square of its extension:

**Equation (1)**

```math
E_{\text{bend}} = \frac{\kappa}{2}\int_0^L\left|\frac{d\hat t}{ds}\right|^2 ds
```


**Step 2: one short segment.** Over a short length $`\Delta s`$, the tangent turns by a small angle $`\theta`$ and the curvature is $`\theta/\Delta s`$. From (1), the segment's energy is $`E = \kappa\theta^2/(2\Delta s)`$. The deflection has two independent transverse components ($`\theta_x`$, $`\theta_y`$), each a quadratic term, so equipartition gives each $`\tfrac12 k_BT`$:

**Equation (2)**

```math
\frac{\kappa}{2\Delta s}\langle\theta^2\rangle = 2\cdot\tfrac12 k_BT \;\Rightarrow\; \langle\theta^2\rangle = \frac{2\,k_BT\,\Delta s}{\kappa}
```


**Step 3: correlation across one segment.** For a small angle, $`\cos\theta \approx 1-\theta^2/2`$. Using (2):

**Equation (3)**

```math
\langle \hat t(s+\Delta s)\cdot\hat t(s)\rangle = \langle\cos\theta\rangle \approx 1 - \frac{k_BT}{\kappa}\Delta s = 1-\frac{\Delta s}{l_P}, \qquad l_P \equiv \frac{\kappa}{k_BT}
```


**Step 4: many segments.** Each segment's bend is independent of the others, and its azimuth is random. Only the component of $`\hat t`$ along the previous direction survives on average, so the correlations multiply. Splitting $`s`$ into $`N = s/\Delta s`$ segments and letting $`\Delta s\to 0`$:

**Equation (4)**

```math
\langle \hat t(s)\cdot\hat t(0)\rangle = \left(1-\frac{\Delta s}{l_P}\right)^{s/\Delta s} \to e^{-s/l_P}
```

This is the defining property of the WLC: orientation decays exponentially, and $`l_P`$ is the decay length.

This exponential describes an ensemble average, not a sharp bend at a distance $`l_P`$. Individual molecules fluctuate between many shapes, and different segments of one molecule point in different directions. The tangent correlation measures how much directional information remains; it does not say that the chain breaks into rigid pieces of length $`l_P`$. The Kuhn links introduced below are an equivalent description of large-scale size, rather than literal joints in the backbone.

**Step 5: end-to-end distance.** Square $`\vec R`$ and average. The correlation depends only on the separation $`|s-s'|`$:

```math
\langle R^2\rangle = \int_0^L\!\!\int_0^L \langle\hat t(s)\cdot\hat t(s')\rangle\,ds\,ds' = \int_0^L\!\!\int_0^L e^{-|s-s'|/l_P}\,ds\,ds'
```

Do the inner integral for fixed $`s`$, splitting it at $`s'=s`$; this gives $`l_P\left(2 - e^{-s/l_P} - e^{-(L-s)/l_P}\right)`$. Then integrate over $`s`$:

**Equation (5)**

```math
\langle R^2\rangle = 2l_PL\left[1 - \frac{l_P}{L}\left(1-e^{-L/l_P}\right)\right]
```


**Limits (sanity checks).**
- *Rod*, $`L\ll l_P`$: expand $`e^{-x}\approx 1-x+x^2/2`$ with $`x=L/l_P`$. The bracket becomes $`L/(2l_P)`$, so $`\langle R^2\rangle \to L^2`$. The ends are a full contour length apart.
- *Coil*, $`L\gg l_P`$: the bracket tends to 1, so $`\langle R^2\rangle\to 2l_PL`$. This is a freely jointed chain with $`N=L/b`$ links of length $`b = 2l_P`$ (the *Kuhn length*), since $`Nb^2 = 2l_PL`$. Size grows as $`\sqrt L`$, the random-walk scaling.

## Motivation and explanation

**Why ds and ss differ so much.**

![Single-stranded DNA as a compact coil (left) and double-stranded DNA as a gently curving helix (right)](../figs/AB-02-ss-vs-ds.png)

- **dsDNA:** $`l_P \approx 40`$–$`60`$ nm, which at 0.34 nm/bp is about 120–180 bp (about 150 bp for 50 nm). Bending a duplex compresses the base stack on the inside of the bend and stretches it on the outside. It also squeezes the charged backbones together. Both cost energy, so $`\kappa`$ is large. The duplex also resists twisting (it "sustains torsion"), which matters for supercoiling.
- **ssDNA:** $`l_P\approx 1`$–$`2`$ nm, a few nucleotides. Without a partner strand, the backbone bonds rotate almost freely (a "free swivel"), so there is little to resist bending.
- **Salt dependence.** Part of $`\kappa`$ is electrostatic repulsion along the backbone. Lowering the salt concentration screens the charges less and *raises* $`l_P`$. This is most visible for ssDNA, where reported values range from about 1 nm to several nm depending on ionic strength.

**When the model fails.**
- It ignores the volume the chain occupies (*excluded volume*), so it underestimates the size of very long coils.
- It ignores sequence-dependent intrinsic curvature (A-tracts bend DNA).
- It does not capture sharp kinks under strong bending.
- It describes single-stranded DNA only roughly, because ssDNA also forms transient internal base pairs.

## Worked example

$`\sqrt{\langle R^2\rangle}`$ for dsDNA with $`l_P = 50`$ nm, from (5), computed in Python:

| Length (bp) | $`L`$ (nm) | $`R_{\text{rms}}`$ (nm) | $`R_{\text{rms}}/L`$ |
|---|---|---|---|
| 20 | 6.8 | 6.65 | 0.98 |
| 150 | 51 | 43.6 | 0.86 |
| 1000 | 340 | 170 | 0.50 |
| 48 502 (λ phage) | 16 490 | 1282 | 0.078 |

- A 20 bp duplex is effectively a rigid rod. DNA nanotechnology (Section 21) depends on this: short duplexes act as straight struts.
- Once $`L`$ reaches about $`l_P`$ (around 150 bp), the duplex is noticeably bent.
- A whole λ genome (16.5 µm of contour) forms a coil only about 1.3 µm across.
- A 20 nt single strand ($`l_P\approx 1`$–$`2`$ nm) is already a coil. This is the source of the entropy lost on hybridisation in Section 03.

## Link to other topics

The exponential-correlation argument is the same one used for any Markov process. Turning a stiffness into a length scale by dividing by $`k_BT`$ is the same move as a Debye length or a capillary length.

## Summary

Thermal bending makes the orientation of DNA decay as $`e^{-s/l_P}`$, with $`l_P=\kappa/k_BT`$. This gives rod-like behaviour below $`l_P`$ and a random coil of Kuhn length $`2l_P`$ above it. dsDNA ($`l_P\approx 50`$ nm) is about 30 times stiffer than ssDNA ($`\approx`$1–2 nm).
<!-- note-content:end -->

[Previous](<AB-01 - Chemistry and structure of DNA and RNA.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-03 - Two-state hybridisation and DNA melting.md>)
