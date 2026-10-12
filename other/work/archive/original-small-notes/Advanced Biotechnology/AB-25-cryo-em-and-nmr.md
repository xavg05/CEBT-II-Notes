# Section 25: Cryo-electron microscopy and NMR

## Overview

Crystallography's bottleneck is the crystal (Section 24). The two other experimental methods avoid it. **Cryo-EM** images individual frozen molecules and averages thousands of them computationally; **NMR** measures distances between nuclei in solution and builds structures that satisfy them. This note covers the mechanism of each and sets out when to use which.

*Assumed:* the crystallography workflow and its bottlenecks (Section 24); the de Broglie relation; nuclear spin in a magnetic field.

## Intuition

Both methods start from the same observation: the crystal in Section 24 served only to amplify a weak signal by adding together millions of identical, identically oriented copies. If the signal can be built up some other way, the crystal is unnecessary.

**Cryo-EM** keeps the averaging but drops the lattice. Molecules are frozen in random orientations in a thin film of ice and imaged individually. Each image is desperately noisy, but if thousands sharing an orientation are aligned and averaged, the noise falls while the signal survives. The crystal's job — adding copies together — is done in software, so the copies need not be ordered.

**NMR** abandons averaging over copies entirely and measures a different observable: distances between nearby nuclei in a molecule tumbling in solution. Enough distance constraints determine the fold.

*Analogy for cryo-EM:* recognising a statue from thousands of blurred photographs taken from unknown angles, by sorting them into groups that look alike and averaging each group. The analogy breaks down because the sorting is done on the images themselves with no prior knowledge of the statue, which is why the method needed both better detectors and better algorithms before it worked.

## Mechanism

### Cryo-electron microscopy

**Why electrons.** Resolution requires a wavelength comparable to the features imaged. Visible light is hundreds of nanometres, far too long. Electrons accelerated through 300 kV have a de Broglie wavelength of about **0.02 Å**, roughly 80 times shorter than Cu Kα X-rays and far shorter than any atomic spacing. **Wavelength is therefore not the limiting factor.**

**What actually limits it** is the sample. Electrons deposit energy as they pass, and the resulting *beam-induced damage* destroys the molecule. A conventional transmission electron microscope avoids this by staining with heavy metals — but then one images the stain, not the protein, so resolution is limited to the stain's granularity. Molecular motion blurs images further.

Cryo-EM solves both by **vitrification**: the sample is plunge-frozen so fast (into liquid ethane at −180 °C) that water forms amorphous ice rather than crystalline ice. Crystalline ice would diffract and destroy the image. Vitrification immobilises the molecules in random orientations and limits radiation damage, so low electron doses can be used.

![The cryo-EM pipeline: sample, grid, freezing, imaging, particle picking, 2D classification, 3D classification, 3D map and model](figs/AB-25-cryoem-pipeline.png)

**The pipeline:**
1. **Vitrify** the sample on a grid in a thin film.
2. **Image** at low dose. Each molecule appears as a faint **2D projection** at an unknown orientation.
3. **Pick particles** — identify individual molecules in the micrographs, typically $10^5$ or more.
4. **Classify and average.** Particles are sorted into groups sharing an orientation and averaged, raising the signal-to-noise ratio. This is the step that replaces the crystal.
5. **Reconstruct.** Projections from many known relative orientations are combined by Fourier transform to give a 3D **density map**, in the same way a CT scan builds a volume from projections.
6. **Build** an atomic model into the map.

### NMR

![The NMR pipeline: isotope-labelled sample, resonance assignment, secondary structure, distance restraints, structure calculation, ensemble of models](figs/AB-25-nmr-pipeline.png)

1. **Prepare** the protein with isotope labels (¹⁵N, ¹³C, ²H), since the common isotopes ¹²C and ¹⁶O have no nuclear spin and are invisible.
2. **Assign resonances** — work out which peak belongs to which backbone and side-chain nucleus. This is the laborious step and it scales badly with size.
3. **Extract restraints.** The **nuclear Overhauser effect (NOE)** couples nuclei through space and falls off as $r^{-6}$, so it reports that two nuclei are within about 5 Å. Coupling constants give backbone dihedral angles $\phi$ and $\psi$.
4. **Calculate structures** by restrained molecular dynamics with simulated annealing: find conformations consistent with all restraints.
5. The result is an **ensemble** of structures, not one. Spread within the ensemble shows where the restraints are weak — often also where the protein is genuinely flexible.

NMR works **in solution at room temperature**, so it reports conformational dynamics that crystallography cannot. But resonance overlap and faster relaxation limit it to small proteins, under roughly 30 kDa, which is why it accounts for only about 6 % of deposited structures.

## Motivation and explanation

**Choosing a method.**

| | X-ray crystallography | Cryo-EM |
|---|---|---|
| Resolution | **0.5–2 Å**, atomic | 3–4 Å, improving |
| Size | no limit in principle, but crystallisation gets harder with size | **better with large** assemblies, >100 kDa |
| Crystal | **required** | not required |
| Purity | milligrams, homogeneous | **less critical** |
| Sample state | lattice, cryogenic | vitrified, near-native |
| *In situ* | no | **yes**, by cryo-tomography |

The two are complementary in exactly the regime where each struggles: crystallography is easiest for small, well-behaved proteins and hardest for large flexible complexes, while cryo-EM is the reverse.

**Why cryo-EM does better with large particles.** Alignment in step 4 requires recognising a particle's orientation from a noisy projection. A larger particle has more distinguishing features and scatters more electrons, so its orientation is determined more reliably. Below about 100 kDa the particle is too faint to align, which sets the lower size limit. This is the opposite of the crystallographic constraint, where size hinders crystallisation.

**Why cryo-EM grew so quickly.** Of about 235 000 deposited structures, roughly 81 % are X-ray, 13 % cryo-EM and 6 % NMR, but almost all the cryo-EM entries are recent. The change came from direct electron detectors, which record individual electrons and so allow motion correction, and from improved classification algorithms — not from new physics.

**Shared limitation.** Both give a *static* structure, or in cryo-EM's case a set of discrete states from classification. Neither reports the continuous motion that biological function usually depends on, which is where NMR retains its advantage.

## Link to other topics

Cryo-EM reconstruction is computed tomography: combining projections taken at many angles into a volume. The difference is that in a CT scanner the angles are known because the source is moved, whereas here they must be inferred from the images themselves.

## Conclusion

Both methods remove the crystal. Cryo-EM replaces the lattice's averaging with computational classification of vitrified single particles, trading resolution for freedom from crystallisation and working best on exactly the large assemblies crystallography finds hardest. NMR measures distance restraints in solution and uniquely reports dynamics, at the cost of a strict size limit. Section 26 turns to predicting structures without any experiment at all.
