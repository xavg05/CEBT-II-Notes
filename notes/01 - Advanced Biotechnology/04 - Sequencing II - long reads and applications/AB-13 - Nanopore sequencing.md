[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-14 - PacBio SMRT sequencing and comparison of platforms.md>)

<!-- note-content:start -->
# Section 13: Nanopore sequencing

## Intuition

Put a hole in an insulating membrane separating two salt solutions, apply a voltage, and ions flow through the hole: a measurable current. Now push something through the hole. While it is in there it occupies space that ions would otherwise use, so the current drops. How *much* it drops depends on the shape and chemistry of whatever is blocking.

DNA is a charged polymer, so the same electric field that drives the ions also drags DNA through the pore. If the hole is narrow enough that only a single strand fits, and if the four bases obstruct the opening by measurably different amounts, then the current over time is a direct transcript of the sequence passing through.

This is a fundamentally different measurement from everything before it. Sanger and Illumina both *synthesise* a copy and infer the template from what was added. Nanopore reads the original molecule itself, and never copies it. That is why there is no amplification step, and why chemical modifications on the original strand remain visible.

*Analogy:* identifying a chain of differently-shaped beads by pulling it through a hole and recording how much water still gets past. The analogy breaks down in the way that matters most: the hole is not thin enough to see one bead at a time. Several beads sit in the constriction together, so the flow reports a *combination*, which is the central difficulty of the method.

## Mechanism

![A protein pore in a lipid bilayer, with a helicase on top feeding single-stranded DNA through; a voltage is applied across the membrane and the current measured](../figs/AB-13-nanopore-principle.png)

**1. The pore.** A protein pore is inserted into a synthetic membrane. Its narrowest constriction is of order 1 nm, comparable to the width of single-stranded DNA, so ssDNA passes but double-stranded DNA cannot. Pores are protein-engineered variants, chosen and modified to sharpen the difference in current between sequences.

**2. The driving force.** A voltage across the membrane drives a steady ionic current through the pore, of order 100 pA, which can be measured precisely. The DNA backbone is negatively charged (Section 01), so the same field pulls DNA from the negative (*cis*) side to the positive (*trans*) side.

**3. The motor protein.** A helicase sits on top of the pore and does two jobs:
- *Unwinds* the duplex, so that only one strand enters. Without it, double-stranded DNA would simply block the pore.
- *Ratchets* the strand through one base at a time. This is the critical function. Unaided electrophoretic translocation is far too fast, of order a microsecond per base, to measure anything. The helicase slows it to roughly 2 ms per base, giving the amplifier time to average out noise.

**4. Base calling.** As the strand moves, the current traces out a series of levels.

![A sequence of bases passing the pore produces a characteristic sequence of current levels, which are converted into base calls](../figs/AB-13-nanopore-current-trace.png)

The essential complication: the constriction is longer than one nucleotide, so roughly five bases occupy it simultaneously. The current level therefore reports a **k-mer**, not a base. With $`k = 5`$ there are $`4^5 = 1024`$ possible current levels, spread over a range of tens of picoamps, so the levels overlap heavily and cannot be read off individually.

The sequence is instead recovered computationally. As the strand advances by one base the k-mer shifts by one, so successive levels are strongly constrained by each other, and the whole current trace is decoded as a sequence using a neural network trained on known sequences. The base caller, not the hardware, is what converts signal into sequence, and improvements to it have historically raised accuracy without any change to the chemistry.

Successive windows overlap in all but one base: when one nucleotide leaves the constriction, one new nucleotide enters. A plausible interpretation of the next current level must therefore agree with most of the previous window, rather than being chosen independently from every possible k-mer. This shared context supplies information that a single noisy level lacks. A homopolymer weakens that constraint because advancing the strand leaves the window's sequence unchanged.

![An array of membrane-supported pores on a sensor chip in a flow cell, with the current trace from one pore and the hand-held device](../figs/AB-13-minion-array.png)

**5. The device.** A flow cell holds an array of wells, each with its own membrane, pore and amplifier, so thousands of strands are read in parallel. The instrument is a hand-held device drawing power over USB, with no optics.

## Motivation and explanation

**Why reads are so long.** Nothing in the method limits read length. There is no resolution limit as in Sanger (Section 10) and no loss of synchrony as in Illumina (Section 12), because there is only ever one molecule. The read continues until the strand finishes or breaks. Reads of 100 kb are routine, and the practical limit is how gently the DNA can be extracted without shearing it. This is the decisive advantage: reads longer than a repeat can span it, resolving the assembly problem of Section 12.

**Why homopolymers are the characteristic failure.** A run such as CCCCC gives the *same* k-mer, and so the same current level, for several successive steps. The level does not change, so the only evidence of how many C's passed is how *long* the level persisted. Translocation is stochastic, so dwell time is a noisy measure of step count, and the base caller must infer "five C's" from a duration. This can produce insertions and deletions in homopolymer runs. Errors can be biased by sequence context and correlated between reads, without every read necessarily making the same mistake.

**Why error correlations matter as well as the raw error rate.** For the illustrative raw accuracies used here, nanopore reads are around 95–99 % accurate, against about 99.9 % for Illumina. Independent random errors can be reduced by combining reads. Sequence-context-dependent errors can remain correlated, so the improvement need not follow an independent binomial model. The independent-error bound below makes that model and its practical limitations explicit.

**Other consequences of reading the native strand.**
- *Modified bases are visible.* A methylated cytosine obstructs the pore slightly differently from an unmodified one, so epigenetic marks are read directly in the same run, with no separate chemistry.
- *RNA can be sequenced directly,* without reverse transcription to cDNA, so modifications and true transcript lengths survive.
- *No amplification bias* (Section 11), because there is no amplification.
- *Minimal preparation:* minutes rather than days, since there is no library PCR or cluster generation.

**Where this leaves it.** Portability plus fast preparation makes nanopore the method of choice when the answer is needed quickly or far from a laboratory: outbreak sequencing in the field, rapid clinical identification. The accuracy deficit matters for calling single-base variants and does not matter for determining genome structure.

### What the independent-error limit teaches

The conservative binomial consensus bound derived for base calls applies only when observations are independent and correctly aligned. With illustrative per-read error probability $`p=0.05`$, it gives upper bounds of $`1.16\times10^{-3}`$, $`6.37\times10^{-5}`$ and $`2.31\times10^{-12}`$ at 5, 10 and 30 observations. Even-pass ties are included as failure. These are statistical model outputs, rather than platform specifications.

The unrealistic improvement at high depth exposes the missing mechanism: sequence-context bias can be shared across reads. Extra independent molecules help random error, while a repeated misinterpretation of the same homopolymer signal requires better measurement or decoding. Long reads can still resolve which unique regions flank a repeat even when some individual bases remain uncertain.

## Wider pathway

Long reads and short reads are complementary rather than competing: a common strategy is to establish genome structure with long reads and then correct the base-level sequence with high-accuracy short reads. The same pore technology is also being developed to read protein sequence, which would do for proteomics what this did for genomics.

## Link to other topics

Measuring an analyte by its obstruction of a current through an aperture is the Coulter principle, long used for counting and sizing cells and particles. Nanopore sequencing is the same measurement taken to single-molecule resolution, where the "particle" is a few nucleotides.

## Summary

Threading a single native strand through a protein pore and recording the ionic current gives sequence without amplification, optics or copying, in a hand-held device, with reads limited by DNA integrity and sustained measurement. Sequence-context effects, particularly at homopolymers, can limit consensus improvement because the signal reflects several bases at once. Coverage reduces independent errors; correlated errors do not follow the same statistical gain.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-14 - PacBio SMRT sequencing and comparison of platforms.md>)
