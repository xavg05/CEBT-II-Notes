# Protein structure - determination and prediction — reading 08.3

[Previous](<../../../../../notes/Advanced Biotechnology/08 - Protein structure - determination and prediction/Complete section.md>) · [Subject index](<../../../../../notes/Advanced Biotechnology/README.md>) · [Next](<../../../../../notes/Advanced Biotechnology/09 - Protein engineering/Complete section.md>)

<!-- reading-content:start -->
## Section 25: Cryo-electron microscopy and NMR

### Intuition

Both methods start from the same observation: the crystal in Section 24 served only to amplify a weak signal by adding together millions of identical, identically oriented copies. If the signal can be built up some other way, the crystal is unnecessary.

**Cryo-EM** keeps the averaging but drops the lattice. Molecules are frozen in random orientations in a thin film of ice and imaged individually. Each image is desperately noisy, but if thousands sharing an orientation are aligned and averaged, the noise falls while the signal survives. The crystal's job — adding copies together — is done in software, so the copies need not be ordered.

**NMR** abandons averaging over copies entirely and measures a different observable: distances between nearby nuclei in a molecule tumbling in solution. Enough distance constraints determine the fold.

*Analogy for cryo-EM:* recognising a statue from thousands of blurred photographs taken from unknown angles, by sorting them into groups that look alike and averaging each group. The analogy breaks down because the sorting is done on the images themselves with no prior knowledge of the statue, which is why the method needed both better detectors and better algorithms before it worked.

### Mechanism

#### Cryo-electron microscopy

**Why electrons.** Resolution requires a wavelength comparable to the features imaged. Visible light is hundreds of nanometres, far too long. Electrons accelerated through 300 kV have a de Broglie wavelength of about **0.02 Å**, roughly 80 times shorter than Cu Kα X-rays and far shorter than any atomic spacing. **Wavelength is therefore not the limiting factor.**

**What actually limits it** is the sample. Electrons deposit energy as they pass, and the resulting *beam-induced damage* destroys the molecule. A conventional transmission electron microscope avoids this by staining with heavy metals — but then one images the stain, not the protein, so resolution is limited to the stain's granularity. Molecular motion blurs images further.

Cryo-EM solves both by **vitrification**: the sample is plunge-frozen so fast (into liquid ethane at −180 °C) that water forms amorphous ice rather than crystalline ice. Crystalline ice would diffract and destroy the image. Vitrification immobilises the molecules in random orientations and limits radiation damage, so low electron doses can be used.

![The cryo-EM pipeline: sample, grid, freezing, imaging, particle picking, 2D classification, 3D classification, 3D map and model](figs/AB-25-cryoem-pipeline.png)

**The pipeline:**
1. **Vitrify** the sample on a grid in a thin film.
2. **Image** at low dose. Each molecule appears as a faint **2D projection** at an unknown orientation.
3. **Pick particles** — identify individual molecules in the micrographs, typically $`10^5`$ or more.
4. **Classify and average.** Particles are sorted into groups sharing an orientation and averaged, raising the signal-to-noise ratio. This is the step that replaces the crystal.
5. **Reconstruct.** Projections from many known relative orientations are combined by Fourier transform to give a 3D **density map**, in the same way a CT scan builds a volume from projections.
6. **Build** an atomic model into the map.

#### NMR

![The NMR pipeline: isotope-labelled sample, resonance assignment, secondary structure, distance restraints, structure calculation, ensemble of models](figs/AB-25-nmr-pipeline.png)

1. **Prepare** the protein with isotope labels (¹⁵N, ¹³C, ²H), since the common isotopes ¹²C and ¹⁶O have no nuclear spin and are invisible.
2. **Assign resonances** — work out which peak belongs to which backbone and side-chain nucleus. This is the laborious step and it scales badly with size.
3. **Extract restraints.** The **nuclear Overhauser effect (NOE)** couples nuclei through space and falls off as $`r^{-6}`$, so it reports that two nuclei are within about 5 Å. Coupling constants give backbone dihedral angles $`\phi`$ and $`\psi`$.
4. **Calculate structures** by restrained molecular dynamics with simulated annealing: find conformations consistent with all restraints.
5. The result is an **ensemble** of structures, not one. Spread within the ensemble shows where the restraints are weak — often also where the protein is genuinely flexible.

NMR works **in solution at room temperature**, so it reports conformational dynamics that crystallography cannot. But resonance overlap and faster relaxation limit it to small proteins, under roughly 30 kDa, which is why it accounts for only about 6 % of deposited structures.

### Motivation and explanation

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

### Link to other topics

Cryo-EM reconstruction is computed tomography: combining projections taken at many angles into a volume. The difference is that in a CT scanner the angles are known because the source is moved, whereas here they must be inferred from the images themselves.

### Summary

Both methods remove the crystal. Cryo-EM replaces the lattice's averaging with computational classification of vitrified single particles, trading resolution for freedom from crystallisation and working best on exactly the large assemblies crystallography finds hardest.

## Section 26: AlphaFold and computational structure prediction

### Intuition

Anfinsen's dogma says the 3D structure of most natural proteins is determined only by their amino acid sequence. That makes prediction well posed, and it is why the field persisted for fifty years without success.

The breakthrough did not come from simulating physics. It came from a different source of information: **evolution has already run the experiment**. For almost any protein there are thousands of homologues across species, all with the same fold and different sequences. Those differences are not random.

If two residues touch in the folded structure, a mutation at one that disrupts the contact is tolerated only if a compensating mutation occurs at the other. Over evolutionary time, **residues in contact mutate together** — they *co-evolve*. The converse holds too: independently varying positions are probably far apart.

A multiple sequence alignment therefore carries a noisy picture of the *contact map*, and a contact map plus chain connectivity largely determines the fold. The sequence database is a record of a search already completed.

*Analogy:* inferring which parts of a machine touch by examining thousands of variants and noting which pairs of parts always change together. The analogy breaks down because co-evolution also arises indirectly — A couples to B and B to C, making A and C appear correlated — and disentangling direct from indirect coupling is much of the difficulty.

### Mechanism

**CASP.** The Critical Assessment of Structure Prediction is a biennial blind test: predictors are given sequences whose structures have been solved but not released. DeepMind's earlier AlphaFold won CASP13 (2018) but by a small margin, and the predictions were not accurate enough for the problem to be considered solved. **AlphaFold 2 at CASP14 (2020)** reached accuracy comparable to experiment, and the problem was declared largely solved.

![Co-evolution: residues in contact mutate in a correlated way across species, while independent positions do not](figs/AB-26-coevolution.png)

![The AlphaFold 2 pipeline: input sequence, database searches producing an MSA and templates, MSA and pair representations, Evoformer, structure module, and recycling](figs/AB-26-alphafold-architecture.png)

**The AlphaFold 2 pipeline:**

**1. Inputs.** The target sequence is used to search:
- a **genetic database**, producing a **multiple sequence alignment (MSA)** of homologues — the primary input, carrying the co-evolution signal;
- a **structure database**, producing **templates** of any known similar structures.

These become two representations:
- the **MSA representation** $`(s, r, c)`$, indexed by sequence and residue;
- the **pair representation** $`(r, r, c)`$, indexed by *pairs* of residues — effectively a running hypothesis about which residues are in contact.

**2. Evoformer (48 blocks).** The core of the network. It updates both representations repeatedly, and the essential feature is the **continuous flow of information between them**: evidence of co-evolution in the MSA updates the pair representation, and geometric constraints in the pair representation inform how the MSA is read. Because the pair representation is geometric, the network can enforce consistency — if A is near B and B near C, then A and C are constrained — which is how indirect correlations are separated from direct contacts.

**3. Structure module (8 blocks).** Converts the refined representations into explicit **3D atomic coordinates**, rather than a contact map to be folded afterwards. It also outputs a **per-residue confidence score**, which is as important as the structure itself.

**4. Recycling (three times).** The outputs are fed back as inputs and the whole network is run again, each pass refining the previous hypothesis.

**AlphaFold 3** extends this beyond single proteins to **proteins, DNA, RNA, small molecules, ions, modified residues and glycosylation** in one model. Architecturally it replaces the structure module with a **diffusion module**, trained to take *noised* atomic coordinates and recover the correct ones, then applied iteratively from noise. This makes AF3 a generative model predicting raw atom coordinates directly.

![AlphaFold 3 predictions overlaid on experimental structures: a transcriptional regulator bound to DNA, and a glycosylated viral spike protein](figs/AB-26-af3-examples.png)

### Motivation and explanation

**Why confidence scores matter.** A prediction without an error estimate cannot be used in practice. AlphaFold reports per-residue confidence, which is empirically well calibrated: high-confidence regions are usually right and low-confidence regions usually are not. Low confidence is also informative — it often marks genuinely disordered regions (Section 23), so the model reports a real property rather than simply failing.

**The effect on crystallography.** AlphaFold models are good enough to serve as search models for **molecular replacement** (Section 24), which needs a model within about 1–1.5 Å RMSD over at least 30 % of atoms. Prediction has therefore not replaced experiment; it has removed the phase problem's dependence on finding a pre-existing homologue. The two methods now feed each other.

**What AlphaFold 2 does and does not do.**

| Predicts well | Struggles | Does not predict |
|---|---|---|
| Single protein chains | Multiple conformations of one sequence | Protein–DNA and protein–RNA complexes |
| Protein multimers | Effects of point mutations | Ligand and ion binding |
| Multisubunit complexes | Nucleic acid structures | Post-translational modifications |
| | Antigen–antibody interactions | Membrane plane for transmembrane domains |

**The pattern in that table is worth seeing.** AlphaFold 2 predicts the single most likely structure of a *polypeptide in isolation*. It struggles or fails wherever the answer depends on something not in the sequence or its evolutionary record:
- *Multiple conformations* — the output is one structure, but many proteins function by switching between several.
- *Point mutations* — a single substitution barely changes the MSA, so the prediction barely changes, even when the real protein unfolds. Given the 20–40 kJ/mol marginal stability of Section 23, this is unsurprising: the model has learned which fold the sequence family adopts, not the energetics that make it marginal.
- *Ligands, ions, modifications and membranes* — context the sequence does not contain.

**The deeper limitation.** AlphaFold predicts structure, not function or mechanism, and its reliance on the MSA means it is weakest on sequences with few homologues — designed proteins, rapidly evolving ones, antibody loops. It has not solved the folding *process*: it does not say how a chain reaches its native state, only where it ends up. The Levinthal paradox of Section 23 is bypassed, not explained.

### Link to other topics

Reading structure from correlated variation across a database, rather than from a physical model, is the same inference used in any empirical correlation: a sufficiently large body of observations substitutes for a theory of the mechanism. The usual caveat applies — such models extrapolate badly outside the data they were fitted to, which here means sequences with few relatives.

### Wider pathway

Reliable structures for essentially every known protein change what is routine: enzyme engineering, binder design and drug discovery can start from a model rather than a multi-year structural project. Section 27 begins protein engineering, where knowing the structure is the precondition for deciding what to change.

### Summary

AlphaFold 2 solved prediction not by simulating folding but by extracting contacts from the co-evolutionary record in multiple sequence alignments, cycling that information against a geometric pair representation and emitting coordinates with calibrated confidence. It predicts an isolated chain's single most likely fold, and fails where the answer depends on conformational change, energetics or molecular context — gaps that AlphaFold 3 begins to close by modelling nucleic acids, ligands and modifications together.

## Conclusion

Experimental determination and computational prediction answer related structural questions, and each requires validation against its own limitations. The next unit develops protein engineering.
<!-- reading-content:end -->

[Previous](<../../../../../notes/Advanced Biotechnology/08 - Protein structure - determination and prediction/Complete section.md>) · [Subject index](<../../../../../notes/Advanced Biotechnology/README.md>) · [Next](<../../../../../notes/Advanced Biotechnology/09 - Protein engineering/Complete section.md>)
