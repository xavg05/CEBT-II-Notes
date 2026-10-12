[Previous](<AB-16 - Quantitative PCR and the cycle threshold.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-18 - Sequence-specific probes and RT-qPCR.md>)

<!-- note-content:start -->
# Section 17: Absolute and relative quantification, and melt-curve control

## Intuition

The two protocols answer different questions, and the difference is the same one that runs through all measurement: *absolute* against *comparative*.

If you need to know how many viral genomes are in a millilitre, you must compare against something of known quantity. There is no way round running standards, just as there is no way to weigh something without a calibrated balance.

If instead you only need to know whether a gene is expressed twice as strongly in treated cells as in untreated ones, calibration is unnecessary. The unknown constants in the $C_t$ relationship, the threshold, the instrument gain, the proportionality between dye and DNA, are the *same* in both reactions, so taking a difference cancels them. This is why relative quantification is the more common measurement: it is easier and it answers the question biologists usually ask.

The subtlety is that the two reactions are never quite identical. Different amounts of RNA are recovered, pipetting varies, cell numbers differ. A *reference gene* is measured alongside to absorb these differences, which is the second subtraction in $\Delta\Delta C_t$.

## Mechanism and derivation

### Absolute quantification

![A dilution series gives a family of amplification curves, and their Ct values plotted against log concentration give a straight calibration line, from which an unknown Ct is read off](../figs/AB-17-standard-curve.png)

1. Prepare a **serial dilution series** of a standard of known concentration, typically tenfold steps.
2. Run qPCR on all of them, obtaining a $C_t$ for each.
3. Plot $C_t$ against $\log_{10}\rho_0$ and fit a straight line. From Section 16, equation (27), this should be linear with slope $-1/\log_{10}(1+E)$. The fit both calibrates the assay and reports its efficiency.
4. Measure $C_t$ for the unknown, and read $\log\rho_0$ off the line.

The result is an absolute copy number, but only as good as the standard: its concentration must be known independently, and it must amplify with the same efficiency as the unknown.

### Relative quantification: the $\Delta\Delta C_t$ method

The aim is the ratio $\rho_0^{\text{sample}}/\rho_0^{\text{control}}$ for a gene of interest, between two conditions.

**Four reactions** are run: the gene of interest and a reference gene, in each of the sample and the control. The **reference gene** is one expressed at a constant level regardless of condition, a *housekeeping gene*, present at the same copy number in both.

**Step 1: first difference, within each condition.** Define
$$\Delta C_t^{\text{sample}} = C_t^{\text{sample}} - C_t^{\text{ref}}, \qquad \Delta C_t^{\text{control}} = C_t^{\text{control}} - C_t^{\text{ref}} \tag{29}$$
each using its own reaction's reference.

**Step 2: what a $\Delta C_t$ means.** At perfect amplification efficiency, each assay has its own intercept, $b_{\mathrm{target}}$ or $b_{\mathrm{ref}}$, set by its threshold and fluorescence response:
$$C_t^{\mathrm{target}}=b_{\mathrm{target}}-\log_2\rho_0^{\mathrm{target}},\qquad C_t^{\mathrm{ref}}=b_{\mathrm{ref}}-\log_2\rho_0^{\mathrm{ref}}.$$
Subtracting gives $\Delta C_t=b_{\mathrm{target}}-b_{\mathrm{ref}}-\log_2(\rho_0^{\mathrm{target}}/\rho_0^{\mathrm{ref}})$. Therefore
$$\frac{\rho_0^{\text{target}}}{\rho_0^{\text{ref}}}=A\,2^{-\Delta C_t},\qquad A=2^{b_{\mathrm{target}}-b_{\mathrm{ref}}}.\tag{30}$$
The assay factor $A$ need not equal one. A single $\Delta C_t$ therefore does not directly give an absolute target/reference abundance ratio without cross-assay calibration. Crucially, $A$ cancels when the same two assays are compared between conditions.

**Step 3: second difference, between conditions.** Dividing the two instances of (30):
$$\frac{\rho_0^{\text{sample}}/\rho_0^{\text{ref}}}{\rho_0^{\text{control}}/\rho_0^{\text{ref}}} = \frac{2^{-\Delta C_t^{\text{sample}}}}{2^{-\Delta C_t^{\text{control}}}} = 2^{-(\Delta C_t^{\text{sample}}-\Delta C_t^{\text{control}})}$$
Defining $\Delta\Delta C_t = \Delta C_t^{\text{sample}} - \Delta C_t^{\text{control}}$:
$$\boxed{\;\frac{\rho_0^{\text{sample}}}{\rho_0^{\text{control}}} = 2^{-\Delta\Delta C_t}\;}\tag{31}$$

**Step 4: with real efficiency.** Repeating with $(1+E)$ in place of 2:
$$\frac{\rho_0^{\text{sample}}}{\rho_0^{\text{control}}} = (1+E)^{-\Delta\Delta C_t} \tag{32}$$
so (31) assumes $E = 1$ *for both the target and the reference*. This is the method's main hidden assumption.

**Assumptions of (31), stated explicitly:**
1. Both amplicons amplify with efficiency $E = 1$, and with the *same* efficiency as each other.
2. The reference gene is genuinely unchanged between the conditions.
3. Each assay's threshold and response are consistent between sample and control. Target and reference may have different assay intercepts; those differences cancel in the second subtraction.

### Melt-curve control

The intercalating dye of Section 16 reports *any* double-stranded DNA. The melt curve checks whether the signal is consistent with one dominant product at the expected melting temperature; it does not establish its sequence.

![Melting curves for three genotypes, and the corresponding −dF/dT derivative curves showing one peak per distinct product](../figs/AB-17-melt-curve.png)

1. After the last cycle, ramp the temperature up slowly while continuously reading fluorescence.
2. As each product melts, its strands separate, the dye is released, and fluorescence falls. This is the melting transition of Section 03, read out by dye rather than by absorbance.
3. Plot $-dF/dT$. Each distinct product gives a **peak** at its own $T_m$.

**Reading the result:**
- *One sharp peak*: consistent with one dominant product. Different products can have similar melting temperatures, so this is a specificity check rather than proof of identity.
- *Multiple peaks, a shoulder, or a broad peak*: more than one product. Different amplicons have different lengths and GC contents, hence different $T_m$ (Section 04).
- A peak at *low* temperature is characteristically a **primer dimer**: two primers amplifying each other, giving a short product that melts early.

The melt curve can expose some specificity problems without running a gel. Validated high-resolution melting assays can also distinguish genotypes through melting-profile differences, including heteroduplex formation. A heterozygote does not necessarily give two resolved peaks, and routine melt analysis does not automatically identify a genotype.

## Motivation and explanation

**Why the reference gene is the weak point.** Equation (31) is only as good as assumption 2. Genes described as "housekeeping" (GAPDH, actin, 18S rRNA) are *not* constant under all conditions; their expression changes with cell cycle, confluence, hypoxia and many treatments. If the reference shifts between conditions, that shift appears directly in $\Delta\Delta C_t$ and is misread as a change in the gene of interest. Good practice is to validate the reference for the specific conditions, or to use the geometric mean of several.

**Why the differences cancel what they cancel.** It is worth being precise about which error each subtraction removes:
- The *first* difference (target minus reference, within one sample) cancels anything affecting both reactions of that sample equally: the amount of input material, RNA recovery, reverse-transcription efficiency, pipetting of the template.
- The *second* difference (sample minus control) cancels anything that is a constant property of the *assay*: the threshold, the two amplicons' intrinsic efficiencies, the dye response.

What neither cancels is a difference in the reference gene's true expression, or a difference in amplification efficiency between the two amplicons.

**Absolute or relative?** Absolute is needed when the number itself matters: viral load, copies per genome, quantifying a standard. Relative is needed when a comparison matters: gene expression under treatment, knockdown efficiency. Relative is less work and usually more precise, because the subtractions remove systematic error that absolute quantification has to control explicitly.

## Worked example

*A gene-expression measurement, with uncertainty.* Computed in Python.

Four reactions, all on one plate:

| | Gene of interest | Reference gene |
|---|---|---|
| Treated sample | $C_t = 22.4$ | $C_t = 18.1$ |
| Untreated control | $C_t = 25.9$ | $C_t = 18.3$ |

**Step 1.** $\Delta C_t^{\text{sample}} = 22.4 - 18.1 = 4.3$; $\Delta C_t^{\text{control}} = 25.9 - 18.3 = 7.6$.

**Step 2.** $\Delta\Delta C_t = 4.3 - 7.6 = -3.3$.

**Step 3.** Fold change $= 2^{-(-3.3)} = 2^{3.3} = 9.85$.

The treatment increases expression of the gene of interest about **tenfold**.

**Sense check.** The reference gene barely moved (18.1 against 18.3), so the two reactions were comparably loaded. The gene of interest appeared 3.5 cycles earlier in the treated sample, and $2^{3.5} = 11$, close to the answer. The reference correction of 0.2 cycles trimmed it to 9.85.

**Effect of assuming $E = 1$.** If both amplicons actually run at $E = 0.9$, equation (32) gives $1.9^{3.3} = 8.3$ rather than 9.85, an 16 % overestimate. For a tenfold change this hardly alters the conclusion; for a claimed 1.3-fold change it would.

**Propagating uncertainty.** Suppose each $C_t$ has a standard deviation of 0.15 cycles from pipetting and curve fitting. $\Delta\Delta C_t$ is a combination of four independent measurements, so
$$\sigma_{\Delta\Delta C_t} = \sqrt{4}\times0.15 = 0.30\ \text{cycles}.$$
The fold change therefore carries a multiplicative uncertainty of $2^{0.30} = 1.23$, so the result is about 9.8 with a range of roughly 8.0 to 12.1.

**The practical consequence.** A fold change is uncertain by a factor of about 1.23 even with good technique. To claim a twofold change ($\Delta\Delta C_t = -1$) reliably, the uncertainty of 0.30 cycles must be small against 1 cycle, which it is but not overwhelmingly. **Changes below about 1.5-fold are not resolvable by this method** without many replicates, which is why small fold changes in the literature should be treated with suspicion.

## Link to other topics

Both subtractions are differential measurement: removing a common-mode error by taking a difference against a reference that experiences the same disturbance. It is the same principle as a differential pressure transducer, a Wheatstone bridge, or any tare weighing.

## Summary

A calibration curve converts $C_t$ into an absolute copy number and simultaneously reports efficiency. Two successive subtractions give a fold change, equation (31), with no calibration at all, because the unknown constants are shared and cancel.
<!-- note-content:end -->

[Previous](<AB-16 - Quantitative PCR and the cycle threshold.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-18 - Sequence-specific probes and RT-qPCR.md>)
