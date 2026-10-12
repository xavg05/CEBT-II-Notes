# Protein structure - determination and prediction — reading 08.1

[Previous](<../../../../../notes/Advanced Biotechnology/07 - DNA nanotechnology/Complete section.md>) · [Subject index](<../../../../../notes/Advanced Biotechnology/README.md>) · [Next](<../../../../../notes/Advanced Biotechnology/08 - Protein structure - determination and prediction/Complete section.md>)

<!-- reading-content:start -->
## Overview

Protein folding connects amino-acid sequence to molecular function. X-ray crystallography, cryo-electron microscopy and NMR infer structure from experimental signals; computational methods predict it from learned constraints, with different limitations and validation needs.

*Assumed throughout:* amino-acid chemistry, thermodynamics and molecular recognition.

## Section 23: Levels of protein structure and the folding problem

### Intuition

A protein is a chain of amino acids joined by peptide bonds, with a backbone that repeats identically and side chains that differ. All the information is in the side chains' order.

Folding is driven by a conflict. The backbone is polar and would happily hydrogen-bond to water, but burying it inside the protein means its donors and acceptors must find partners *within* the chain. The two secondary structures, the α-helix and the β-sheet, are the two ways of satisfying every backbone hydrogen bond using only the chain itself. They exist because the backbone must be neutralised before it can be buried.

What drives burial is the hydrophobic effect: non-polar side chains disrupt water's hydrogen-bond network, so water pushes them together. The protein collapses, and the backbone that comes with them must be satisfied by helices and sheets.

*Analogy:* folding a long strip of magnetic tape so that every magnet on the backing finds a partner while the oily patches end up inside. The analogy breaks down because the "magnets" here are satisfied by *two* specific geometric patterns rather than arbitrary pairings, and because the whole thing happens in water that is actively squeezing the oily patches together.

### Mechanism

![Primary sequence, secondary α-helix and β-sheet, tertiary fold with heme, and quaternary assembly of haemoglobin](figs/AB-23-structure-levels.png)

**Four levels of organisation:**

1. **Primary** — the amino acid sequence.
2. **Secondary** — local structures, principally the α-helix and β-sheet, formed by backbone hydrogen bonding.
3. **Tertiary** — the folded polypeptide including any cofactors, held by *intra*molecular bonds. This is the biologically active form.
4. **Quaternary** — assembly of several discrete polypeptides (subunits) through *inter*molecular bonds, as in haemoglobin's four chains.

![An α-helix: ribbon, hydrogen bonding between i and i+4, and the view down the axis showing no central cavity](figs/AB-23-alpha-helix.png)

**The α-helix**, proposed by Astbury (from keratin fibre diffraction) and Pauling (from paper models):
- typically 10–40 residues;
- **right-handed**, with no space inside — the backbone packs against itself;
- hydrogen bonds between the carbonyl CO of residue $`i`$ and the amide NH of residue $`i+4`$;
- 100° of rotation per residue, so **3.6 residues per turn**;
- side chains extend outwards and tilt towards the N-terminus, giving the "Christmas tree" appearance.

![A β-sheet with parallel and antiparallel strands hydrogen-bonded on both sides](figs/AB-23-beta-sheet.png)

**The β-sheet**, also proposed by Astbury:
- stretches of extended chain (**β-strands**) lying side by side;
- CO and NH hydrogen-bond to **neighbouring strands on both sides**, rather than within one strand;
- strands may be **parallel or antiparallel** depending on their relative direction;
- can close into barrels, as in green fluorescent protein;
- side chains alternate above and below the sheet along a strand, but point the same way across strands — so **every second residue sits on one face**, which lets a sheet present one hydrophobic face and one polar face.

### Derivation

**The Levinthal paradox.** Tertiary structure is determined by the sequence alone: no external template is required. But consider finding it by search.

Take a 100-residue protein. Each residue has two freely rotating backbone dihedrals ($`\phi`$, $`\psi`$), so a chain of 100 residues has about 198 of them. Allowing each only **three** stable values from the Ramachandran plot:

**Equation (39)**

```math
N_{\text{conf}} = 3^{198} = 3.0\times10^{94}
```


Sampling one conformation every 0.1 ps, an exhaustive search takes

**Equation (40)**

```math
t = 3.0\times10^{94}\times10^{-13}\ \text{s} = 3\times10^{81}\ \text{s} \approx 9\times10^{73}\ \text{years}
```

about $`7\times10^{63}`$ times the age of the universe. **Proteins nevertheless fold in milliseconds.** Folding cannot be a search.

**The resolution: the funnel.** The energy landscape is not flat with one narrow minimum; it is a **funnel**. Partially correct structures are already downhill, so the chain is guided towards the native state rather than sampling blindly. Folding follows a limited number of pathways, often through a collapsed intermediate (a **molten globule**) that has secondary structure but not yet fixed side-chain packing.

![A funnel-shaped energy landscape: unfolded states at the rim, a molten globule partway down, the native state at the bottom](figs/AB-23-folding-funnel.png)

In 1 ms at 0.1 ps per step, a chain samples about $`10^{10}`$ conformations — a factor of $`10^{84}`$ short of (39), so the funnel must eliminate essentially the whole search space.

### Motivation and explanation

**Proteins are barely stable.** The native state is the most stable conformation, but only by **20–40 kJ/mol** over the denatured state. At 310 K that is 8–16 $`k_BT`$ for the whole molecule, and for a 100-residue protein about **0.1 $`k_BT`$ per residue** — the difference of a few hydrogen bonds. Two consequences:
- Folding is a near-cancellation of two large numbers, the enthalpy of burial and the entropy lost on ordering the chain, so modest changes in temperature, pH or a single mutation can unfold a protein.
- Marginal stability is probably functional: proteins must be degradable and must flex to work.

**Why this matters for prediction.** Equation (39) says the structure cannot be found by enumeration, and marginal stability says it cannot be found by crude energy minimisation either, since the correct fold is only slightly below many wrong ones. For fifty years this is why prediction failed, and it is the background to Section 26.

**Where the simple picture fails.** Not all proteins fold alone; many require chaperones. Some pass through no molten globule. A large fraction of eukaryotic proteins are *intrinsically disordered*, with no single native structure, and the whole framework does not apply to them.

### Link to other topics

The funnel is the same argument as nucleation in crystallisation: a process that would be impossibly slow as a random search becomes fast once partially correct states are downhill in free energy, so that the system is guided rather than searching.

### Summary

Protein structure is organised in four levels, with the α-helix and β-sheet existing to satisfy backbone hydrogen bonds so that the chain can be buried. The sequence determines the fold, but $`3^{198}`$ conformations rule out any search, and a funnelled landscape with marginal final stability — 20–40 kJ/mol — is what makes millisecond folding possible.
<!-- reading-content:end -->

[Previous](<../../../../../notes/Advanced Biotechnology/07 - DNA nanotechnology/Complete section.md>) · [Subject index](<../../../../../notes/Advanced Biotechnology/README.md>) · [Next](<../../../../../notes/Advanced Biotechnology/08 - Protein structure - determination and prediction/Complete section.md>)
