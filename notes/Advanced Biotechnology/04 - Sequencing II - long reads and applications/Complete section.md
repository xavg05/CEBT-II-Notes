[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Sequencing II - long reads and applications

## Overview

Nanopore and PacBio sequencing read individual molecules through different physical signals. Their long reads complement short-read methods by spanning repeats, resolving variants and supporting applications that depend on molecular context.

*Assumed throughout:* nucleotide polymerisation and the short-read sequencing principles.

## Section 13: Nanopore sequencing

### Intuition

Put a hole in an insulating membrane separating two salt solutions, apply a voltage, and ions flow through the hole: a measurable current. Now push something through the hole. While it is in there it occupies space that ions would otherwise use, so the current drops. How *much* it drops depends on the shape and chemistry of whatever is blocking.

DNA is a charged polymer, so the same electric field that drives the ions also drags DNA through the pore. If the hole is narrow enough that only a single strand fits, and if the four bases obstruct the opening by measurably different amounts, then the current over time is a direct transcript of the sequence passing through.

This is a fundamentally different measurement from everything before it. Sanger and Illumina both *synthesise* a copy and infer the template from what was added. Nanopore reads the original molecule itself, and never copies it. That is why there is no amplification step, and why chemical modifications on the original strand remain visible.

*Analogy:* identifying a chain of differently-shaped beads by pulling it through a hole and recording how much water still gets past. The analogy breaks down in the way that matters most: the hole is not thin enough to see one bead at a time. Several beads sit in the constriction together, so the flow reports a *combination*, which is the central difficulty of the method.

### Mechanism

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

### Motivation and explanation

**Why reads are so long.** Nothing in the method limits read length. There is no resolution limit as in Sanger (Section 10) and no loss of synchrony as in Illumina (Section 12), because there is only ever one molecule. The read continues until the strand finishes or breaks. Reads of 100 kb are routine, and the practical limit is how gently the DNA can be extracted without shearing it. This is the decisive advantage: reads longer than a repeat can span it, resolving the assembly problem of Section 12.

**Why homopolymers are the characteristic failure.** A run such as CCCCC gives the *same* k-mer, and so the same current level, for several successive steps. The level does not change, so the only evidence of how many C's passed is how *long* the level persisted. Translocation is stochastic, so dwell time is a noisy measure of step count, and the base caller must infer "five C's" from a duration. This can produce insertions and deletions in homopolymer runs. Errors can be biased by sequence context and correlated between reads, without every read necessarily making the same mistake.

**Why error correlations matter as well as the raw error rate.** For the illustrative raw accuracies used here, nanopore reads are around 95–99 % accurate, against about 99.9 % for Illumina. Independent random errors can be reduced by combining reads. Sequence-context-dependent errors can remain correlated, so the improvement need not follow an independent binomial model. The independent-error bound below makes that model and its practical limitations explicit.

**Other consequences of reading the native strand.**
- *Modified bases are visible.* A methylated cytosine obstructs the pore slightly differently from an unmodified one, so epigenetic marks are read directly in the same run, with no separate chemistry.
- *RNA can be sequenced directly,* without reverse transcription to cDNA, so modifications and true transcript lengths survive.
- *No amplification bias* (Section 11), because there is no amplification.
- *Minimal preparation:* minutes rather than days, since there is no library PCR or cluster generation.

**Where this leaves it.** Portability plus fast preparation makes nanopore the method of choice when the answer is needed quickly or far from a laboratory: outbreak sequencing in the field, rapid clinical identification. The accuracy deficit matters for calling single-base variants and does not matter for determining genome structure.

#### What the independent-error limit teaches

The conservative binomial consensus bound derived for base calls applies only when observations are independent and correctly aligned. With illustrative per-read error probability $`p=0.05`$, it gives upper bounds of $`1.16\times10^{-3}`$, $`6.37\times10^{-5}`$ and $`2.31\times10^{-12}`$ at 5, 10 and 30 observations. Even-pass ties are included as failure. These are statistical model outputs, rather than platform specifications.

The unrealistic improvement at high depth exposes the missing mechanism: sequence-context bias can be shared across reads. Extra independent molecules help random error, while a repeated misinterpretation of the same homopolymer signal requires better measurement or decoding. Long reads can still resolve which unique regions flank a repeat even when some individual bases remain uncertain.

### Wider pathway

Long reads and short reads are complementary rather than competing: a common strategy is to establish genome structure with long reads and then correct the base-level sequence with high-accuracy short reads. The same pore technology is also being developed to read protein sequence, which would do for proteomics what this did for genomics.

### Link to other topics

Measuring an analyte by its obstruction of a current through an aperture is the Coulter principle, long used for counting and sizing cells and particles. Nanopore sequencing is the same measurement taken to single-molecule resolution, where the "particle" is a few nucleotides.

### Summary

Threading a single native strand through a protein pore and recording the ionic current gives sequence without amplification, optics or copying, in a hand-held device, with reads limited by DNA integrity and sustained measurement. Sequence-context effects, particularly at homopolymers, can limit consensus improvement because the signal reflects several bases at once. Coverage reduces independent errors; correlated errors do not follow the same statistical gain.

## Section 14: PacBio SMRT sequencing and comparison of platforms

### Intuition

To watch one polymerase add bases in real time, two things must be solved.

**The background problem.** The reaction needs labelled nucleotides at micromolar concentrations so that the polymerase finds them quickly. But in any ordinary illuminated volume there are thousands of free labelled nucleotides diffusing about, all fluorescing. The one sitting in the polymerase is invisible against them. The fix is to make the observed volume so small that, on average, it contains almost no free nucleotides: then anything bright is almost certainly the one being incorporated.

**The persistence problem.** In Illumina, the label stays attached and must be chemically cleaved off between cycles, which stops the reaction, costs time, and leaves scars (Section 12). Here the aim is continuous operation, so the label must remove *itself* as part of the chemistry. The fix is to attach it to the part of the nucleotide that the reaction discards anyway.

*Analogy:* watching one worker on a crowded factory floor by shining a spotlight on a patch the size of a single workstation, and giving each component a tag on the packaging rather than the part, so the tag leaves with the rubbish. The analogy breaks down because the "spotlight" is not a beam that can be aimed: the confinement is a property of the aperture itself, as described below.

### Mechanism

![A hairpin-adapter circular template in a nanowell with a single polymerase; labelled nucleotides produce a pulse of fluorescence as each is incorporated](../figs/AB-14-SMRT-nanowell.png)

**1. Library: circularisation.** Hairpin adapters are ligated to both ends of a double-stranded fragment. Because a hairpin joins the two strands of the duplex, the result is a closed single-stranded loop: the SMRTbell. The polymerase can therefore go round and round the same molecule indefinitely, which is the basis of the accuracy in point 6.

**2. The zero-mode waveguide (ZMW).** The chip is a metal film on glass, perforated with millions of holes about 70 nm across. This is much smaller than the wavelength of the exciting light (several hundred nm). An aperture below the cut-off size does not transmit a propagating wave: the field entering it decays exponentially within a few tens of nanometres. Illumination from below therefore penetrates only a short distance into the well, lighting an observation volume of order $`10^{-20}`$ litres, a few tens of zeptolitres, at the very bottom.

A single polymerase is anchored at the bottom of each well, inside this illuminated region. Free nucleotides diffusing in the bulk of the well are not excited.

**3. Phospholinked nucleotides.** The fluorophore is attached to the *terminal phosphate*, not to the base.

![A nucleotide carrying its fluorophore on the terminal phosphate rather than on the base or sugar](../figs/AB-14-phospholinked-dNTP.png)

Recall that a polymerase forms the phosphodiester bond by attacking the α-phosphate and releasing the β and γ phosphates as pyrophosphate. A label on the terminal phosphate is therefore **cleaved off by the normal chemistry of incorporation** and diffuses away. Two consequences:
- The growing strand is left completely natural: no scar, no accumulating modification, so the polymerase runs continuously for tens of thousands of bases. This is precisely what limits Illumina to a few hundred.
- The fluorescent signal is a *pulse*, not a persistent state. It begins when the nucleotide is held in the active site and ends when it is cleaved and released.

**4. Read-out.** Each well is monitored continuously. The sequence is read as the time-ordered series of coloured pulses, with the four bases distinguished by emission wavelength. Millions of wells run in parallel.

**5. Kinetic information.** The *interval between* pulses depends on how fast the polymerase is working, and that in turn depends on the template. A methylated base slows the polymerase measurably, so modified bases are detected from the timing of the pulses, with no separate assay, in the same way nanopore detects them from current.

**6. Circular consensus (HiFi).** A single pass over the template has a raw error rate of roughly 10–15 %, which is high. But because the template is circular, the polymerase passes over the same sequence many times in one read. Each pass observes the same molecule again. Many random pulse-detection errors can be reduced by combining passes, although independence is approximate and sequence-context errors can remain. Averaging the passes therefore does reduce the error, and the result is a *HiFi read*: tens of kilobases long at better than 99.9 % accuracy.

### Motivation and explanation

**Why repeated observations improve accuracy.** SMRT pulse detection has stochastic errors that can often be reduced by combining passes over the same molecule. Nanopore measurements also contain random error as well as sequence-context-dependent bias, and repeated reads can improve their consensus too. The important statistical distinction is between independent error, which repeated observations reduce, and correlated error, which can persist. Neither platform has perfectly independent errors or a universal quality ceiling determined by its mechanism alone. Actual consensus accuracy must be measured for the chemistry, specimen and analysis used.

**The trade-off in read length.** The polymerase processivity is fixed, so a read of total length $`L`$ over an insert of length $`\ell`$ gives $`L/\ell`$ passes. Longer inserts give longer reads but fewer passes, hence lower accuracy. Shorter inserts give higher accuracy but less reach. This is a design choice made per experiment, and it has no analogue on the other platforms.

The repeated passes belong to one original insert. They improve confidence in that molecule's sequence, but they do not supply independent molecules for estimating the frequency of a rare variant in a sample. Conversely, sequencing many different molecules once increases sample coverage without giving each one the repeated observations used for circular consensus. An experiment must budget separately for accurate molecular reads and representative sampling.

**Limitations.**
- *Cost per base* is high, above both Illumina and nanopore.
- *The instrument* is large, expensive and not portable, in contrast to the hand-held nanopore device.
- *Run time* is long, 15–30 hours.
- *Library preparation* requires circularisation, so it is more involved than nanopore's.

### Comparison of platforms

| | Sanger (S10) | Illumina (S11–12) | Nanopore (S13) | PacBio SMRT (S14) |
|---|---|---|---|---|
| Read length | 500–1000 nt | 50–300 nt | up to ~100 kb | 10–25 kb |
| Raw accuracy | 99.99 % | ~99.9 % | ~95–99 % | ~85–90 % per pass |
| Consensus accuracy | — | very high | improved by repeated observations; correlated errors can remain | >99.9 % (HiFi), measured performance |
| Error character | stochastic and context-dependent | mainly substitutions; correlated biases can remain | stochastic and context-dependent; indels at homopolymers | stochastic pulse errors; context-dependent errors can remain |
| Amplification | sufficient template required; cloning in shotgun workflows | PCR + bridge PCR | **none** | **none** |
| Throughput | ~96 reads | $`10^{9}`$–$`10^{10}`$ reads | moderate | moderate |
| Cost per base | very high | **lowest** | low | high |
| Preparation | purified template; separate clone preparation for shotgun libraries | 1–2 days | minutes | circularisation |
| Run time | hours | days | real-time output | 15–30 h |
| Instrument | benchtop | large, expensive | **hand-held** | large, expensive |
| Modified bases | no | no (needs separate chemistry) | **yes, directly** | **yes, from kinetics** |
| Direct RNA | no | no | **yes** | no |

**How to choose.** Verifying one plasmid: Sanger. Counting and variant-calling at scale: Illumina. Genome structure, repeats, or an answer needed in the field: nanopore. Long reads where every base must be right: PacBio HiFi.

#### Quantifying optical background and repeated passes

For free fluorescent nucleotides at molar concentration $`c`$ in observation volume $`V`$, the mean number present is $`\bar N=cN_AV`$, where $`N_A`$ is Avogadro's constant. Setting $`\bar N=1`$ gives $`c=1/(N_AV)`$. With $`V=20`$ zeptolitres, this concentration is approximately $`83\,\mu\mathrm M`$; at $`5\,\mu\mathrm M`$, the mean free occupancy is only $`0.0602`$. A one-femtolitre observation volume at the same concentration would contain approximately 3011 free labelled molecules. Optical confinement therefore removes background without forcing the entire reaction to use a negligibly low substrate concentration.

Repeated passes trade molecular reach for confidence. A fixed total polymerase read budget of 100 kb supplies approximately 20 passes over a 5 kb insert or 5 over a 20 kb insert, ignoring adapters. An independent-error majority model illustrates the gain, but pulse information, alignment and correlated errors determine measured HiFi performance; a pass count alone is not an accuracy specification.

### Wider pathway

Sections 10–14 complete the reading side of the field. What they enable is covered in Section 15, and the methods recur throughout: sequencing verifies every construct built in Sections 06–09, quantifies transcripts alongside the amplification methods of Sections 16–18, and reads out the selections in Section 19.

### Link to other topics

The ZMW is an evanescent-field device: below the cut-off size an aperture carries no propagating mode, and the field decays exponentially. The same physics appears in waveguides below cut-off and in total internal reflection, and it is used here as a way of defining a reaction volume optically rather than physically.

### Summary

Confining the observation volume and placing the label on the leaving group allow one polymerase to be monitored continuously. Circularising the template supplies repeated observations for consensus; stochastic errors can be reduced, while correlated errors and insufficient passes limit the gain. HiFi accuracy is an observed platform result, rather than a guarantee from a chosen raw error rate alone.

## Section 15: Applications of nucleic acid sequencing

### Intuition

Sequencing answers three different kinds of question, and the distinction determines which platform and which depth to use.

1. **What is the sequence?** Comparing a sample against a reference to find differences. Diagnosis, variant discovery, verifying a construct. Needs accuracy at individual bases.
2. **How much of it is there?** Counting how many reads come from each source. Gene expression, chromosome dosage, species abundance. Here the read is a *counting token*: individual base accuracy barely matters, but the number of reads does.
3. **How is it arranged?** Determining structure, order and repeats. Genome assembly, structural variants. Needs read length, not base accuracy.

Most misapplications come from confusing these. Deep Illumina coverage will not resolve a repeat (question 3), and a few long nanopore reads will not establish a transcript's abundance (question 2).

### Mechanism

#### Scope: how much to sequence

| Approach | Target | Share of human genome | Trade-off |
|---|---|---|---|
| Whole genome | everything | 100 % | Most informative: finds non-coding and structural variants. Most expensive. |
| Whole exome | protein-coding regions | 1–2 % (about 47 Mb) | Roughly 50–70× less sequence for a given depth. Most known disease variants are in coding regions, so it captures most of the diagnostic yield. Blind to regulatory and structural variation. |
| Targeted panel | chosen genes | ≪1 % | Cheapest and deepest. Requires knowing in advance what to look for. |

The choice is a classic sampling decision: narrowing the target buys depth and cost at the price of only finding what was anticipated.

#### Transcriptomics (RNA-seq)

RNA cannot be read by most platforms directly, so it is reverse-transcribed into complementary DNA (cDNA) and sequenced as DNA. Nanopore is the exception (Section 13).

Counting reads per transcript measures **gene expression levels**: which genes are on, and how strongly, in this cell under these conditions. Because reads span exon junctions, it also reveals **alternative splicing**, which exons were included in a given transcript. Applications include cellular responses to drugs, cancer profiling to find biomarkers, and development and immunology.

This is question 2 above, so what matters is the number of reads per transcript, not base-level accuracy.

#### Clinical and diagnostic uses

- **Verifying engineered constructs.** Every recombinant organism or plasmid is sequenced to confirm correct insertion, absence of mutations, and no off-target changes. This closes the loop from Sections 06–09.
- **Personalised medicine.** Same disease, same symptoms, different treatment, chosen by genotype. In non-small-cell lung cancer, a tumour is tested for mutations: an *EGFR* mutation indicates an EGFR inhibitor, an *ALK* rearrangement indicates an ALK inhibitor. The sequence selects the drug.
- **Rare disease diagnosis.** Many genetic diseases are hard to diagnose by symptoms alone. Whole genome or exome sequencing of undiagnosed cases identifies the causal variant, enabling targeted therapy, carrier screening, and informed family planning. Examples include Huntington's disease (a CAG repeat expansion, and note that counting repeat length needs long reads) and Duchenne muscular dystrophy.
- **Risk prediction.** Common diseases such as type 2 diabetes and coronary artery disease are influenced by thousands of variants of individually small effect. Aggregating them gives a risk score, identifying high-risk individuals before symptoms appear, which enables earlier screening, lifestyle change and preventive therapy.
- **Non-invasive prenatal screening,** below.

#### Population and environmental uses

- **Genomic surveillance of viruses.** Sequencing viral genomes over time tracks mutations, identifies variants of concern, reconstructs transmission chains, and guides vaccine updates. SARS-CoV-2 variants were defined and tracked this way, and influenza vaccine strain selection depends on it. Nanopore's portability matters here.
- **Environmental DNA (eDNA).** All organisms shed DNA into their surroundings, so sequencing everything in a water or soil sample reveals what lives there without observing or capturing anything. It characterises microbial communities, detects whether a given species is present, and discovers new species. A survey of Loch Ness found no reptile DNA but a large amount of eel DNA.
- **Forensics.** Matching DNA from hair, blood, saliva or remains against crime-scene samples, identifying remains, and establishing kinship or paternity. Sequencing also *exonerates*, which has been its most consequential forensic use.

### Motivation and explanation

**Why cost collapsing changed what is possible.** Section 10 showed cost per base falling by about six orders of magnitude. The consequence is not that the same experiments became cheaper, but that entirely different ones became feasible. Sequencing a genome to answer one clinical question, or sequencing thousands of viral genomes a week, or sequencing a bucket of lake water, are only sensible when a genome costs a few hundred pounds. This is why the sequencing market continues to grow at roughly 15 % per year.

**Why the counting applications are the subtle ones.** Questions of type 2 have a statistical structure that the others do not. The signal is a small difference in proportion, and whether it can be detected depends on how many reads are counted, through $`\sqrt{N}`$. The prenatal-counting model below shows why depth controls random uncertainty.

**Limits worth stating.**
- *Risk scores are probabilistic,* and derived largely from European-ancestry cohorts, so they transfer poorly to other populations.
- *Finding a variant is not the same as interpreting it.* Most variants discovered are of unknown significance, and interpretation, not sequencing, is now the bottleneck in clinical genomics.
- *Screening is not diagnosis.* A positive non-invasive prenatal screen is confirmed by an invasive diagnostic test, because a chromosome excess in placental DNA is not itself a direct fetal karyotype.

#### Non-invasive prenatal chromosome screening

During pregnancy, cell-free DNA in maternal plasma includes a placental contribution, commonly called the fetal fraction, mixed with maternal DNA. The placental contribution can reveal fetal chromosome dosage, although placenta and fetus need not have identical chromosome complements. Chromosome counting can use the mixture directly: sequence fragments, map reads to chromosomes, and compare the chromosome-21 proportion with a calibrated euploid baseline. Each read need not be assigned to mother or fetus.

![Maternal plasma DNA is sequenced and chromosome-specific read counts are compared; a chromosome-21 excess is a screening signal](../figs/AB-15-prenatal-screening.png)

Let $`p`$ be the normal chromosome-21 read fraction and let $`f`$ denote the placental contribution expressed as a fraction of diploid genome equivalents before adding an extra chromosome. A trisomic contribution carries three copies instead of two, raising its chromosome-21 dosage by a factor $`3/2`$. Before normalising the total DNA amount, the expected chromosome-21 count is proportional to $`p(1+f/2)`$. The extra chromosome also increases the total by $`fp/2`$, giving


```math
p'=\frac{p(1+f/2)}{1+fp/2}\approx p(1+f/2).
```


The approximation neglects the small change in the denominator. For illustrative $`p=46.7/3100`$ and $`f=0.10`$, the exact model gives $`p'=0.015806`$ versus $`p=0.015065`$: an increase of about $`4.92\%`$ relative to baseline. The absolute excess is small because the maternal contribution dilutes the dosage change. A clinical fetal-fraction estimate may use a different convention, so its definition must match the model.

If $`N`$ usable reads independently fall on chromosome 21 with probability $`p`$, the count is binomial and the measured fraction has standard error $`\sigma=\sqrt{p(1-p)/N}`$. To resolve an excess $`\Delta p=p'-p`$ at a chosen idealised ratio $`z=\Delta p/\sigma`$, rearrange to obtain $`N=p(1-p)(z/\Delta p)^2`$. The illustrative model needs approximately $`6.75\times10^5`$ reads for $`z=5`$. This is a counting-only comparison against a known baseline, rather than a validated clinical cutoff or a calculation of predictive value.

For small $`f`$, $`\Delta p`$ is proportional to $`f`$, so maintaining the same counting precision requires $`N\propto f^{-2}`$. Lowering $`f`$ from $`0.10`$ to $`0.04`$ requires roughly 6.25 times the depth in this approximation. Short uniquely mapping reads can suffice because the observation is chromosome identity, although accurate mapping and correction of capture/GC bias still matter. More reads reduce random uncertainty; they cannot remove biased sampling or establish the biological source of an excess. This remains a screen: a statistical placental-DNA signal does not by itself establish the fetal karyotype.

### Wider pathway

This closes the sequencing unit. Sections 16–19 return to nucleic acids as *reagents* rather than as information: amplifying and quantifying specific sequences by PCR, and selecting functional sequences from libraries.

### Link to other topics

The prenatal calculation is a signal-detection problem of a familiar kind: a small shift in a mean against a background whose noise falls as $`1/\sqrt{N}`$. The same $`\sqrt{N}`$ reasoning governs how long any measurement must be averaged to resolve a given difference.

### Summary

Sequencing answers three distinct questions — what the sequence is, how much of it there is, and how it is arranged — and each favours a different platform and depth. The counting applications are the ones where falling cost has changed practice most, because detection depends on read number through $`\sqrt{N}`$ rather than on any property of the chemistry.

## Conclusion

Long reads preserve molecular context, and the appropriate platform depends on the biological question and error tolerance. The next unit develops quantitative pcr.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)
