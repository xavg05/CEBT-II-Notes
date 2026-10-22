[Previous](<ET-17 - Random-mixing models (Redlich–Kister, van Laar, regular solution theory).md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-19 - Local-composition models (Wilson and NRTL).md>)

<!-- note-content:start -->
# Section 18: Flory–Huggins theory for size-asymmetric mixtures

*Notation:* solvent 1, polymer 2. $m = \underline{V}_2/\underline{V}_1$ is the number of lattice sites (solvent-sized segments) per chain. Volume fractions: $\phi_1 = x_1/(x_1 + mx_2)$, $\phi_2 = mx_2/(x_1 + mx_2)$.

## Intuition

Picture a lattice in which each site holds one solvent molecule or one chain segment. A dissolved polymer of $m$ segments occupies $m$ connected sites. There are far fewer ways to place one connected chain than $m$ separate small molecules, so the entropy gained on mixing is much smaller per segment than for small molecules. It is, however, much larger *per mole of polymer* than the ideal $-R\ln x$ suggests, because each polymer molecule spreads over many sites.

The volume fraction is the natural "how much space does it fill" variable, and entropy comes out as $\ln\phi$ instead of $\ln x$. *The lattice picture breaks down* for real chains, which are flexible and can cluster in dilute solution. The mean-field assumption that segments are spread uniformly then fails.

## Derivation

**Step 1: entropy of mixing (lattice counting result).**

$$\Delta\underline{S}^{\mathrm{mix}} = -R\left(x_1\ln\phi_1 + x_2\ln\phi_2\right) \tag{95}$$

This reduces to the ideal $-R\sum x_i\ln x_i$ when $m = 1$, since then $\phi_i = x_i$.

**Step 2: enthalpy of mixing.** Random contacts between solvent and segments, as in Margules, but counted per lattice site. There are $(x_1 + mx_2)$ sites per mole of molecules:

$$\Delta\underline{H}^{\mathrm{mix}} = \underline{H}^{ex} = \chi RT\,(x_1 + mx_2)\,\phi_1\phi_2 \tag{96}$$

Here $\chi$ is the dimensionless interaction energy per contact, in units of $RT$. It can be estimated as $\chi \approx \underline{V}_1(\delta_1 - \delta_2)^2/RT$, as in RST.

**Step 3: excess Gibbs energy.** Subtract the ideal mixing terms from $\Delta\underline{G}^{\mathrm{mix}} = \Delta\underline{H}^{\mathrm{mix}} - T\Delta\underline{S}^{\mathrm{mix}}$:

$$\frac{\underline{G}^{ex}}{RT} = \underbrace{x_1\ln\frac{\phi_1}{x_1} + x_2\ln\frac{\phi_2}{x_2}}_{-\underline{S}^{ex}/R} + \underbrace{\chi(x_1 + mx_2)\phi_1\phi_2}_{\underline{H}^{ex}/RT} \tag{97}$$

Unlike RST, $\underline{S}^{ex}\neq 0$ whenever $m\neq 1$. The energetic term has the one-constant Margules structure, written in volume fractions.

**Step 4: solvent activity.** Differentiate $n\Delta\underline{G}^{\mathrm{mix}}/RT = n_1\ln\phi_1 + n_2\ln\phi_2 + \chi n_1\phi_2$ with respect to $n_1$:

One polymer chain adds many occupied sites but only one independently translating molecule. The lattice count keeps both facts: volume fractions describe where the sites are, while $n_2$ counts how many chains can be placed. This is why replacing every chain by the same number of free small molecules would overestimate the mixing entropy.

For the solvent derivative, adding solvent increases the total number of sites and therefore changes *both* volume fractions. These derivative contributions produce the term linear in $\phi_2$ in (98), in addition to $\ln\phi_1$ and the interaction term. Simply replacing $x_1$ by $\phi_1$ in Raoult's law would miss that rearrangement. In the equal-size limit, volume and mole fractions coincide and the extra linear term disappears.

$$\ln a_1 = \ln(\gamma_1x_1) = \ln\phi_1 + \left(1 - \frac{1}{m}\right)\phi_2 + \chi\phi_2^2 \tag{98}$$

This is the quantity measured by vapour-pressure lowering, freezing point or osmotic pressure of polymer solutions.

**Step 5: when does the solution split?** Per lattice site, $\Delta G^{\mathrm{mix}}/RT = (1-\phi)\ln(1-\phi) + (\phi/m)\ln\phi + \chi\phi(1-\phi)$, with $\phi = \phi_2$. A homogeneous solution is unstable where the curvature is negative:

$$\frac{\partial^2}{\partial\phi^2} = \frac{1}{1-\phi} + \frac{1}{m\phi} - 2\chi < 0$$

The smallest $\chi$ for which this can happen is the minimum over $\phi$ of $\tfrac12[1/(1-\phi) + 1/(m\phi)]$. Setting its derivative to zero gives $\phi_c = 1/(1+\sqrt m)$ and

$$\chi_c = \frac{1}{2}\left(1 + \frac{1}{\sqrt m}\right)^2 \;\xrightarrow{m\to\infty}\; \frac12 \tag{99}$$

## Motivation and explanation

**Why mole fraction can conceal a concentrated polymer.** For a polymer occupying $m$ solvent-sized sites, $x_1=(1-\phi_2)/(1-\phi_2+\phi_2/m)$. With $m=1000$ and polymer volume fraction $\phi_2=0.5$, the solvent still has $x_1\approx0.999$. Raoult's law would therefore suggest almost pure-solvent activity.
Flory–Huggins instead gives $\ln a_1=\ln(1-\phi_2)+(1-1/m)\phi_2+\chi\phi_2^2$. At this composition $a_1\approx0.824$ for $\chi=0$, and 0.911 for $\chi=0.4$. Size asymmetry alone lowers the activity; the positive energetic parameter partly offsets that entropic effect. The model's critical value is $\chi_c=\tfrac12(1+1/\sqrt m)^2\approx0.532$, at polymer volume fraction $1/(1+\sqrt m)\approx0.031$. Thus the assumed $\chi=0.4$ is below the demixing threshold throughout the composition range, despite the substantial activity departure.

**Why volume fractions.** Each segment, not each molecule, takes up a site. Mole fraction badly understates how much of the space the polymer fills: 1 mol % of a 1000-segment chain occupies about 91 % of the volume.

**Meaning of $\chi$.**
- $\chi < \chi_c$: miscible at all compositions (a "good" solvent when $\chi$ is small).
- $\chi > \chi_c$: phase separation.

For long chains $\chi_c\to 0.5$, so a very small energetic penalty is enough to make a polymer insoluble. The entropic gain is tiny per segment, so it cannot pay for much unfavourable energy. This is why most pairs of polymers do not mix.

**Limits.**
- Mean-field lattice theory is poor in dilute solution.
- In practice $\chi$ depends on composition and temperature.
- A constant-$\chi$ model does not describe temperature-driven miscibility changes. A suitable $\chi(T,x)$ can represent a lower critical solution temperature, but specific interactions must then enter through that parameter or a richer model.

## Link to other topics

The curvature condition used in Step 5 is the general test for liquid–liquid phase separation, developed fully later for small-molecule mixtures (binodal and spinodal). The combinatorial (size-and-shape) entropy of Flory–Huggins reappears as the combinatorial term of UNIQUAC.

## Summary

Flory–Huggins theory writes the entropy of mixing in volume fractions and adds one Margules-like energy parameter $\chi$. For a large solute it predicts strong, mainly entropic, negative deviations of the solvent activity from Raoult's law. It also predicts phase separation when $\chi$ exceeds $\tfrac12(1 + m^{-1/2})^2$, close to ½ for long chains.
<!-- note-content:end -->

[Previous](<ET-17 - Random-mixing models (Redlich–Kister, van Laar, regular solution theory).md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<ET-19 - Local-composition models (Wilson and NRTL).md>)
