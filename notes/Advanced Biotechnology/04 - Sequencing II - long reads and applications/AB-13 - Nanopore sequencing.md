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

![An array of membrane-supported pores on a sensor chip in a flow cell, with the current trace from one pore and the hand-held device](../figs/AB-13-minion-array.png)

**5. The device.** A flow cell holds an array of wells, each with its own membrane, pore and amplifier, so thousands of strands are read in parallel. The instrument is a hand-held device drawing power over USB, with no optics.

## Motivation and explanation

**Why reads are so long.** Nothing in the method limits read length. There is no resolution limit as in Sanger (Section 10) and no loss of synchrony as in Illumina (Section 12), because there is only ever one molecule. The read continues until the strand finishes or breaks. Reads of 100 kb are routine, and the practical limit is how gently the DNA can be extracted without shearing it. This is the decisive advantage: reads longer than a repeat can span it, resolving the assembly problem of Section 12.

**Why homopolymers are the characteristic failure.** A run such as CCCCC gives the *same* k-mer, and so the same current level, for several successive steps. The level does not change, so the only evidence of how many C's passed is how *long* the level persisted. Translocation is stochastic, so dwell time is a noisy measure of step count, and the base caller must infer "five C's" from a duration. This produces insertions and deletions in homopolymer runs, and it is a **systematic** error: it recurs at the same place in every read of that sequence.

**Why that systematic character matters more than the raw error rate.** Raw single-read accuracy is around 95–99 %, against about 99.9 % for Illumina. Random errors average away with coverage, so a high random error rate is tolerable. Systematic errors do not: every read of a homopolymer makes the same mistake, so the consensus is confidently wrong. The worked example quantifies this.

**Other consequences of reading the native strand.**
- *Modified bases are visible.* A methylated cytosine obstructs the pore slightly differently from an unmodified one, so epigenetic marks are read directly in the same run, with no separate chemistry.
- *RNA can be sequenced directly,* without reverse transcription to cDNA, so modifications and true transcript lengths survive.
- *No amplification bias* (Section 11), because there is no amplification.
- *Minimal preparation:* minutes rather than days, since there is no library PCR or cluster generation.

**Where this leaves it.** Portability plus fast preparation makes nanopore the method of choice when the answer is needed quickly or far from a laboratory: outbreak sequencing in the field, rapid clinical identification. The accuracy deficit matters for calling single-base variants and does not matter for determining genome structure.

## Worked example

*Timing, information content and the consensus limit.* Computed in Python.

**1. Signal levels.** With five bases in the constriction, the number of distinguishable states is $`4^5 = 1024`$. If the full current range spanned by these states is about 60 pA, the mean spacing between adjacent levels is $`60/1024 \approx 0.06`$ pA, far below the noise on a single measurement. This is why no amount of care in reading one level identifies a base, and why the decoding must use the whole trace.

**2. Translocation.** At about 450 bases per second, each base occupies $`1000/450 = 2.2`$ ms. A 100 kb read therefore takes $`10^{5}/450 = 222`$ s, under four minutes. A 10-base homopolymer passes in 22 ms, and the base caller must convert that duration into a count of ten.

**3. Why coverage does not rescue a systematic error.** Suppose the single-read error probability is $`p=0.05`$ and observations are independent. If $`K`$ is the number of erroneous observations among $`n`$ reads, then $`K`$ is binomial. More than half the observations being correct guarantees a correct majority call, so a conservative error bound is

```math
P_{\mathrm{error}}\leq\sum_{k=\lceil n/2\rceil}^{n}\binom{n}{k}p^k(1-p)^{n-k}.
```

For even $`n`$, ties are conservatively included as failures. This bound groups all wrong bases together; it is not an exact four-base consensus error model.

| Coverage | Error upper bound (independent model) | Corresponding $`Q`$ lower bound |
|---|---|---|
| 5 | $`0.0012`$ | 29 |
| 10 | $`6.4e-05`$ | 42 |
| 30 | $`2.3e-12`$ | 116 |

Even these conservative model estimates become unrealistically small. Real nanopore errors include correlated sequence-context effects, particularly at homopolymers; their probability does not shrink according to an independent binomial model. More coverage helps random error, but correlated errors require improved chemistry and base calling. These figures illustrate the statistical assumption rather than predicting real instrument accuracy.

**4. Compare with Illumina.** A 95 % raw read is $`Q13`$; Illumina's 99.9 % is $`Q30`$. In a 100 kb nanopore read, $`10^{5}\times0.05 = 5000`$ bases are wrong. Such a read is nevertheless useful, because its value lies in spanning a long distance and establishing structure, not in the identity of any single base.

## Wider pathway

Long reads and short reads are complementary rather than competing: a common strategy is to establish genome structure with long reads and then correct the base-level sequence with high-accuracy short reads. The same pore technology is also being developed to read protein sequence, which would do for proteomics what this did for genomics.

## Link to other topics

Measuring an analyte by its obstruction of a current through an aperture is the Coulter principle, long used for counting and sizing cells and particles. Nanopore sequencing is the same measurement taken to single-molecule resolution, where the "particle" is a few nucleotides.

## Summary

Threading a single native strand through a protein pore and recording the ionic current gives sequence without amplification, optics or copying, in a hand-held device, with reads limited only by how intact the DNA is. The costs are a lower raw accuracy and, more importantly, a systematic weakness at homopolymers that coverage cannot remove, because the signal reports a five-base window rather than one base.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-14 - PacBio SMRT sequencing and comparison of platforms.md>)
