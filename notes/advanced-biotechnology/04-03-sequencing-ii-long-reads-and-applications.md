# Sequencing II - long reads and applications — reading 04.3

[Previous](04-02-sequencing-ii-long-reads-and-applications.md) · [Subject index](README.md) · [Next](05-01-quantitative-pcr.md)

<!-- reading-content:start -->
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

**Why the counting applications are the subtle ones.** Questions of type 2 have a statistical structure that the others do not. The signal is a small difference in proportion, and whether it can be detected depends on how many reads are counted, through $`\sqrt{N}`$. The worked example shows this.

**Limits worth stating.**
- *Risk scores are probabilistic,* and derived largely from European-ancestry cohorts, so they transfer poorly to other populations.
- *Finding a variant is not the same as interpreting it.* Most variants discovered are of unknown significance, and interpretation, not sequencing, is now the bottleneck in clinical genomics.
- *Screening is not diagnosis.* A positive non-invasive prenatal screen is confirmed by an invasive diagnostic test, for the reason the worked example makes clear.

### Worked example

*Non-invasive prenatal screening for trisomy 21.* Computed in Python.

During pregnancy, placental DNA circulates in the mother's blood, so a blood sample contains a mixture of maternal and fetal cell-free DNA. The fetal portion is typically about 10 % and it cannot be physically separated. How can an extra fetal chromosome be detected?

![Cell-free fetal DNA in maternal blood is sequenced, and reads are counted per chromosome; an excess of chromosome 21 indicates trisomy](figs/AB-15-prenatal-screening.png)

**The insight: do not identify, just count.** Sequence everything, map each read to a chromosome, and ask whether the *proportion* of reads from chromosome 21 is higher than expected. No read needs to be assigned to mother or fetus.

**1. Expected proportions.** Chromosome 21 is about 46.7 Mb of a 3.1 Gb genome, so a normal sample gives a chromosome 21 read fraction of

```math
p_{21} = 46.7/3100 = 0.01506.
```

With a fetal fraction $`f = 0.10`$, and a trisomic fetus contributing 1.5 times the normal chromosome 21 dose:

```math
p_{21}' = (1-f)p_{21} + f\times1.5\,p_{21} = p_{21}(1+0.5f) = 0.01582.
```

The difference is $`\Delta p = 7.5\times10^{-4}`$, a **5 % relative increase**, and only because the fetal fraction is 10 %. The entire measurement rests on resolving 1.582 % against 1.506 %.

**2. How many reads are needed?** Each read is a Bernoulli trial, so the standard error on the measured fraction is $`\sqrt{p(1-p)/N}`$:

| Reads $`N`$ | Standard error | $`z = \Delta p/\sigma`$ |
|---|---|---|
| $`10^{5}`$ | $`3.9\times10^{-4}`$ | 2.0 |
| $`10^{6}`$ | $`1.2\times10^{-4}`$ | 6.2 |
| $`5\times10^{6}`$ | $`5.4\times10^{-5}`$ | 13.8 |

For $`z = 5`$, $`N = p(1-p)(5/\Delta p)^2 = 6.5\times10^{5}`$ reads. A few million reads gives a comfortable margin, which is a small fraction of one Illumina run, and explains why the test is inexpensive enough to offer routinely.

**3. What this implies about the method.**
- *Short reads are ideal.* Each read only needs to be assignable to a chromosome, so 50 bases suffices, and cell-free DNA is already fragmented to about that length. Read length would be wasted here.
- *Base accuracy barely matters.* A miscalled base rarely changes which chromosome a read maps to. This is a counting problem, not a sequence problem.
- *Fetal fraction is the critical variable.* $`\Delta p \propto f`$, so $`N \propto 1/f^2`$. At $`f = 0.04`$ instead of 0.10, the required read count rises by a factor of $`(10/4)^2 = 6.3`$. Low fetal fraction, which occurs in early gestation and with high maternal BMI, is the main cause of test failure and of false negatives.
- *It is a screen, not a diagnosis.* It measures a statistical excess in a mixture, not the fetal karyotype, so a positive result is confirmed invasively.

### Wider pathway

This closes the sequencing unit. Sections 16–19 return to nucleic acids as *reagents* rather than as information: amplifying and quantifying specific sequences by PCR, and selecting functional sequences from libraries.

### Link to other topics

The prenatal calculation is a signal-detection problem of a familiar kind: a small shift in a mean against a background whose noise falls as $`1/\sqrt{N}`$. The same $`\sqrt{N}`$ reasoning governs how long any measurement must be averaged to resolve a given difference.

### Summary

Sequencing answers three distinct questions — what the sequence is, how much of it there is, and how it is arranged — and each favours a different platform and depth. The counting applications are the ones where falling cost has changed practice most, because detection depends on read number through $`\sqrt{N}`$ rather than on any property of the chemistry.

## Conclusion

Long reads preserve molecular context, and the appropriate platform depends on the biological question and error tolerance. The next unit develops quantitative pcr.
<!-- reading-content:end -->

[Previous](04-02-sequencing-ii-long-reads-and-applications.md) · [Subject index](README.md) · [Next](05-01-quantitative-pcr.md)
