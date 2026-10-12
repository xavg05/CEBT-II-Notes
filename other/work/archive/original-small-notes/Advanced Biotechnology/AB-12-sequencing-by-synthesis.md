# Section 12: Sequencing by synthesis and read assembly

## Overview

Section 11 left a flow cell carrying millions of clusters, each a thousand identical copies of one fragment. This note covers how they are read: a cycle of controlled single-base extension and imaging, repeated once per position. It explains:
- the reversible terminator, which is what makes "one base per cycle" possible with all four nucleotides present at once;
- why read length is limited to a few hundred bases, and the mechanism (phasing) that sets the limit;
- how short reads are turned back into a long sequence, and when that fails.

*Assumed:* cluster generation (Section 11); chain termination (Section 10); coverage statistics (Section 10).

## Intuition

Sanger reads a sequence by making fragments of every length and sorting them (Section 10). Sequencing by synthesis does the opposite: it keeps the molecules still and advances them all together, one base at a time, watching what is added at each step. The sequence is read in time rather than in space.

For that to work, extension must be *stoppable and restartable*. If nucleotides were added freely, a cluster would run to the end of the template in one step and a single image would show only the last base. So each nucleotide is supplied with a removable block on its 3′ position: the polymerase adds one, then cannot add another until the block is taken off. Each cycle is a controlled single step, and the fluorophore attached to that nucleotide says which base it was.

The contrast with Section 10 is worth holding onto: Sanger uses an *irreversible* terminator in a small proportion, so that chains stop at random positions. Here the terminator is *reversible* and used exclusively, so that every chain stops at the same position every cycle.

*Analogy:* a ratchet that advances one tooth per turn of a handle, with the tooth colour read off at each click. The analogy breaks down because a real ratchet cannot slip; in a cluster, a small fraction of strands fail to extend or extend twice, and those errors accumulate.

## Mechanism

![A primer is extended one labelled nucleotide at a time; the flow cell is imaged after each addition, giving a sequence of colours per cluster](figs/AB-12-SBS.png)

**One cycle:**

1. **Prime.** A sequencing primer anneals to the adapter sequence common to every cluster (Section 11). All clusters therefore start from the same point, which is why the fragments needed standardised ends.
2. **Extend by one.** All four nucleotides are supplied simultaneously, each carrying a spectrally distinct fluorophore and a 3′ blocking group. The polymerase incorporates whichever one is complementary at that position, and the block prevents any further addition. Supplying all four at once is what makes this different from stepwise chemistry: the *template* chooses, not the operator.
3. **Image.** The whole flow cell is scanned. Every cluster fluoresces in the colour of the single base it just added. All copies in a cluster added the same base, so their signals sum, which is what makes the spot visible.
4. **Deblock.** The fluorophore and the 3′ block are cleaved chemically and washed away, restoring a normal 3′-OH and leaving no label behind. The strand is now ready for the next cycle.

Repeating this gives, for each cluster, a sequence of colours over time: its read.

**Paired-end reading.** After the first read, one more round of bridge amplification regenerates the complementary strands on the surface, the already-read strands are cleaved away, and the process is repeated from the other end. Each fragment then yields two reads, one from each end, with a known approximate separation. This matters for assembly, below.

## Motivation and explanation

**Why the fluorophore and the block are on the same nucleotide.** The fluorophore identifies the base; the block enforces one addition per cycle. Removing both in the same chemical step means a single reagent restores the strand to a natural state. A residue left behind by imperfect cleavage ("scar") impedes the polymerase and is one of the reasons signal degrades along a read.

**Phasing: what limits the read length.** The cluster is read as a sum over about a thousand strands, and the method assumes they are all at the same position. In each cycle a small fraction fail to extend (*phasing*, falling behind) or lose their block and extend twice (*pre-phasing*, running ahead).

These errors are cumulative and irreversible. After $n$ cycles the population has spread over a range of positions, so the image at cycle $n$ is a blend of several positions, dominated by the intended one but increasingly contaminated. The signal-to-noise ratio falls monotonically with cycle number, which is why:
- reads are limited to roughly 50–300 bases;
- quality declines along the read, with the 3′ end worst;
- base-call errors are predominantly substitutions, not insertions or deletions.

This is a different limit from Sanger's. Sanger is limited by *electrophoretic resolution* between fragments; this is limited by *loss of synchrony* within a cluster. Neither is improved by running longer.

**Why accuracy is nevertheless high.** Each base call averages a thousand molecules, and each genomic position is covered by many independent reads. Both average away random error, which is why per-base accuracy reaches about 99.9 % and consensus accuracy is far higher still.

**The trade-off against Sanger.** Illumina wins overwhelmingly on throughput and cost per base, and loses on read length and on turnaround. For verifying a single plasmid, Sanger is faster and simpler; for anything requiring millions of reads, there is no comparison.

### Assembly

![Reads overlapping into contigs, which are merged into the assembled sequence](figs/AB-12-assembly-contigs.png)

Reads carry no positional information, so position must be recovered from sequence:
- **Mapping** to a known reference: each read is aligned to the position it matches. Fast and reliable, and used whenever a reference exists.
- **De novo assembly:** reads are overlapped with each other and merged into *contigs*, contiguous stretches built from overlapping reads. Contigs are then ordered and oriented into *scaffolds* using paired-end information, since the two reads of a pair are known to lie a certain distance apart and in opposite orientations.

**Why repeats are the fundamental problem.** A read shorter than a repeated element cannot be placed: it matches every copy of the repeat equally well. The assembly then breaks at that point, or collapses the copies together and loses the true structure. This is not a defect of the chemistry but a consequence of read length, and no amount of coverage fixes it. It is the main reason long-read platforms exist alongside short-read ones.

## Worked example

*Quality scores, coverage and consensus accuracy.* Computed in Python.

**1. Quality scores.** Base calls carry a Phred score $Q = -10\log_{10}p$, where $p$ is the probability that the call is wrong:

| $Q$ | Error probability | Meaning |
|---|---|---|
| 20 | $10^{-2}$ | 1 wrong base in 100 |
| 30 | $10^{-3}$ | 1 in 1000 |
| 40 | $10^{-4}$ | 1 in 10 000 |

At $Q30$, a 150-base read contains on average $150\times10^{-3} = 0.15$ errors, so about one read in seven has a miscalled base. Across $6.2\times10^{8}$ reads that is roughly $10^{8}$ wrong bases in a run, which only becomes acceptable because of redundancy.

**2. Why coverage rescues it.** With 30× coverage and independent errors at $p = 10^{-3}$, a consensus call at a position is wrong only if most of the 30 reads are wrong in the same way. The probability of 16 or more errors among 30 reads is $1.4\times10^{-40}$. The consensus is therefore limited by *systematic* bias (GC bias, repeats, mapping error), not by random base-call error.

**3. Coverage still has to reach every base.** From Section 10, uncovered fraction $e^{-c}$: at 30×, essentially none of the genome is missed by chance. Combined with the result above, this is why 30× is a standard specification for human genome sequencing: it is the point at which both random gaps and random miscalls stop being the limiting factor.

## Wider pathway

Together, Sections 10–12 give the two complementary reading technologies: one accurate and long but serial, the other short but massively parallel. Their shared weakness is read length, which is what the single-molecule platforms of Sections 13–14 address by reading one long molecule directly rather than many short amplified ones.

## Link to other topics

The cluster is a population of identical reactors intended to run in lockstep, and phasing is the gradual spread of their state distribution: the same loss of synchrony that broadens residence-time distributions, and the same reason that a signal averaged over a drifting population degrades with time.

## Conclusion

Reversible terminators turn polymerisation into a stepwise, readable process, with one imaged base per cycle across the whole flow cell at once. Loss of synchrony within each cluster, not chemistry, caps the read at a few hundred bases, and that short read length is what makes repeats the hard part of assembly. Section 13 turns to a platform that abandons amplification entirely and reads a single molecule as it passes through a pore.
