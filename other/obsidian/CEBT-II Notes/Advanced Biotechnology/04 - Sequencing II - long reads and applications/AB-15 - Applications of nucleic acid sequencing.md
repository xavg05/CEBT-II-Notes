[Previous](<AB-14 - PacBio SMRT sequencing and comparison of platforms.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Section 15: Applications of nucleic acid sequencing

## Intuition

Sequencing answers three different kinds of question, and the distinction determines which platform and which depth to use.

1. **What is the sequence?** Comparing a sample against a reference to find differences. Diagnosis, variant discovery, verifying a construct. Needs accuracy at individual bases.
2. **How much of it is there?** Counting how many reads come from each source. Gene expression, chromosome dosage, species abundance. Here the read is a *counting token*: individual base accuracy barely matters, but the number of reads does.
3. **How is it arranged?** Determining structure, order and repeats. Genome assembly, structural variants. Needs read length, not base accuracy.

Most misapplications come from confusing these. Deep Illumina coverage will not resolve a repeat (question 3), and a few long nanopore reads will not establish a transcript's abundance (question 2).

## Mechanism

### Scope: how much to sequence

| Approach | Target | Share of human genome | Trade-off |
|---|---|---|---|
| Whole genome | everything | 100 % | Most informative: finds non-coding and structural variants. Most expensive. |
| Whole exome | protein-coding regions | 1–2 % (about 47 Mb) | Roughly 50–70× less sequence for a given depth. Most known disease variants are in coding regions, so it captures most of the diagnostic yield. Blind to regulatory and structural variation. |
| Targeted panel | chosen genes | ≪1 % | Cheapest and deepest. Requires knowing in advance what to look for. |

The choice is a classic sampling decision: narrowing the target buys depth and cost at the price of only finding what was anticipated.

### Transcriptomics (RNA-seq)

RNA cannot be read by most platforms directly, so it is reverse-transcribed into complementary DNA (cDNA) and sequenced as DNA. Nanopore is the exception (Section 13).

Counting reads per transcript measures **gene expression levels**: which genes are on, and how strongly, in this cell under these conditions. Because reads span exon junctions, it also reveals **alternative splicing**, which exons were included in a given transcript. Applications include cellular responses to drugs, cancer profiling to find biomarkers, and development and immunology.

This is question 2 above, so what matters is the number of reads per transcript, not base-level accuracy.

### Clinical and diagnostic uses

- **Verifying engineered constructs.** Every recombinant organism or plasmid is sequenced to confirm correct insertion, absence of mutations, and no off-target changes. This closes the loop from Sections 06–09.
- **Personalised medicine.** Same disease, same symptoms, different treatment, chosen by genotype. In non-small-cell lung cancer, a tumour is tested for mutations: an *EGFR* mutation indicates an EGFR inhibitor, an *ALK* rearrangement indicates an ALK inhibitor. The sequence selects the drug.
- **Rare disease diagnosis.** Many genetic diseases are hard to diagnose by symptoms alone. Whole genome or exome sequencing of undiagnosed cases identifies the causal variant, enabling targeted therapy, carrier screening, and informed family planning. Examples include Huntington's disease (a CAG repeat expansion, and note that counting repeat length needs long reads) and Duchenne muscular dystrophy.
- **Risk prediction.** Common diseases such as type 2 diabetes and coronary artery disease are influenced by thousands of variants of individually small effect. Aggregating them gives a risk score, identifying high-risk individuals before symptoms appear, which enables earlier screening, lifestyle change and preventive therapy.
- **Non-invasive prenatal screening,** below.

### Population and environmental uses

- **Genomic surveillance of viruses.** Sequencing viral genomes over time tracks mutations, identifies variants of concern, reconstructs transmission chains, and guides vaccine updates. SARS-CoV-2 variants were defined and tracked this way, and influenza vaccine strain selection depends on it. Nanopore's portability matters here.
- **Environmental DNA (eDNA).** All organisms shed DNA into their surroundings, so sequencing everything in a water or soil sample reveals what lives there without observing or capturing anything. It characterises microbial communities, detects whether a given species is present, and discovers new species. A survey of Loch Ness found no reptile DNA but a large amount of eel DNA.
- **Forensics.** Matching DNA from hair, blood, saliva or remains against crime-scene samples, identifying remains, and establishing kinship or paternity. Sequencing also *exonerates*, which has been its most consequential forensic use.

## Motivation and explanation

**Why cost collapsing changed what is possible.** Section 10 showed cost per base falling by about six orders of magnitude. The consequence is not that the same experiments became cheaper, but that entirely different ones became feasible. Sequencing a genome to answer one clinical question, or sequencing thousands of viral genomes a week, or sequencing a bucket of lake water, are only sensible when a genome costs a few hundred pounds. This is why the sequencing market continues to grow at roughly 15 % per year.

**Why the counting applications are the subtle ones.** Questions of type 2 have a statistical structure that the others do not. The signal is a small difference in proportion, and whether it can be detected depends on how many reads are counted, through $\sqrt{N}$. The prenatal-counting model below shows why depth controls random uncertainty.

**Limits worth stating.**
- *Risk scores are probabilistic,* and derived largely from European-ancestry cohorts, so they transfer poorly to other populations.
- *Finding a variant is not the same as interpreting it.* Most variants discovered are of unknown significance, and interpretation, not sequencing, is now the bottleneck in clinical genomics.
- *Screening is not diagnosis.* A positive non-invasive prenatal screen is confirmed by an invasive diagnostic test, because a chromosome excess in placental DNA is not itself a direct fetal karyotype.

### Non-invasive prenatal chromosome screening

During pregnancy, cell-free DNA in maternal plasma includes a placental contribution, commonly called the fetal fraction, mixed with maternal DNA. The placental contribution can reveal fetal chromosome dosage, although placenta and fetus need not have identical chromosome complements. Chromosome counting can use the mixture directly: sequence fragments, map reads to chromosomes, and compare the chromosome-21 proportion with a calibrated euploid baseline. Each read need not be assigned to mother or fetus.

![Maternal plasma DNA is sequenced and chromosome-specific read counts are compared; a chromosome-21 excess is a screening signal](../figs/AB-15-prenatal-screening.png)

Let $p$ be the normal chromosome-21 read fraction and let $f$ denote the placental contribution expressed as a fraction of diploid genome equivalents before adding an extra chromosome. A trisomic contribution carries three copies instead of two, raising its chromosome-21 dosage by a factor $3/2$. Before normalising the total DNA amount, the expected chromosome-21 count is proportional to $p(1+f/2)$. The extra chromosome also increases the total by $fp/2$, giving

$$p'=\frac{p(1+f/2)}{1+fp/2}\approx p(1+f/2).$$

The approximation neglects the small change in the denominator. For illustrative $p=46.7/3100$ and $f=0.10$, the exact model gives $p'=0.015806$ versus $p=0.015065$: an increase of about $4.92\%$ relative to baseline. The absolute excess is small because the maternal contribution dilutes the dosage change. A clinical fetal-fraction estimate may use a different convention, so its definition must match the model.

If $N$ usable reads independently fall on chromosome 21 with probability $p$, the count is binomial and the measured fraction has standard error $\sigma=\sqrt{p(1-p)/N}$. To resolve an excess $\Delta p=p'-p$ at a chosen idealised ratio $z=\Delta p/\sigma$, rearrange to obtain $N=p(1-p)(z/\Delta p)^2$. The illustrative model needs approximately $6.75\times10^5$ reads for $z=5$. This is a counting-only comparison against a known baseline, rather than a validated clinical cutoff or a calculation of predictive value.

For small $f$, $\Delta p$ is proportional to $f$, so maintaining the same counting precision requires $N\propto f^{-2}$. Lowering $f$ from $0.10$ to $0.04$ requires roughly 6.25 times the depth in this approximation. Short uniquely mapping reads can suffice because the observation is chromosome identity, although accurate mapping and correction of capture/GC bias still matter. More reads reduce random uncertainty; they cannot remove biased sampling or establish the biological source of an excess. This remains a screen: a statistical placental-DNA signal does not by itself establish the fetal karyotype.

## Wider pathway

This closes the sequencing unit. Sections 16–19 return to nucleic acids as *reagents* rather than as information: amplifying and quantifying specific sequences by PCR, and selecting functional sequences from libraries.

## Link to other topics

The prenatal calculation is a signal-detection problem of a familiar kind: a small shift in a mean against a background whose noise falls as $1/\sqrt{N}$. The same $\sqrt{N}$ reasoning governs how long any measurement must be averaged to resolve a given difference.

## Summary

Sequencing answers three distinct questions — what the sequence is, how much of it there is, and how it is arranged — and each favours a different platform and depth. The counting applications are the ones where falling cost has changed practice most, because detection depends on read number through $\sqrt{N}$ rather than on any property of the chemistry.

## Conclusion

Long reads preserve molecular context, and the appropriate platform depends on the biological question and error tolerance. The next unit develops quantitative pcr.
<!-- note-content:end -->

[Previous](<AB-14 - PacBio SMRT sequencing and comparison of platforms.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)
