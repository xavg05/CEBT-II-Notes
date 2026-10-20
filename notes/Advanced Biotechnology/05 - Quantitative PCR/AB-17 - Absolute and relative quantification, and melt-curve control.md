[Previous](<AB-16 - Quantitative PCR and the cycle threshold.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-18 - Sequence-specific probes and RT-qPCR.md>)

<!-- note-content:start -->
# Section 17: Absolute and relative quantification, and melt-curve control

## Intuition

The two protocols answer different questions, and the difference is the same one that runs through all measurement: *absolute* against *comparative*.

If you need to know how many viral genomes are in a millilitre, you must compare against something of known quantity. There is no way round running standards, just as there is no way to weigh something without a calibrated balance.

If instead you only need to know whether a gene is expressed twice as strongly in treated cells as in untreated ones, calibration is unnecessary. The unknown constants in the $`C_t`$ relationship, the threshold, the instrument gain, the proportionality between dye and DNA, are the *same* in both reactions, so taking a difference cancels them. This is why relative quantification is the more common measurement: it is easier and it answers the question biologists usually ask.

The subtlety is that the two reactions are never quite identical. Different amounts of RNA are recovered, pipetting varies, cell numbers differ. A *reference gene* is measured alongside to absorb these differences, which is the second subtraction in $`\Delta\Delta C_t`$.

## Mechanism and derivation

### Absolute quantification

![A dilution series gives a family of amplification curves, and their Ct values plotted against log concentration give a straight calibration line, from which an unknown Ct is read off](../figs/AB-17-standard-curve.png)

1. Prepare a **serial dilution series** of a standard of known concentration, typically tenfold steps.
2. Run qPCR on all of them, obtaining a $`C_t`$ for each.
3. Plot $`C_t`$ against $`\log_{10}\rho_0`$ and fit a straight line. From Section 16, equation (27), this should be linear with slope $`-1/\log_{10}(1+E)`$. The fit both calibrates the assay and reports its efficiency.
4. Measure $`C_t`$ for the unknown, and read $`\log\rho_0`$ off the line.

The result is an absolute copy number, but only as good as the standard: its concentration must be known independently, and it must amplify with the same efficiency as the unknown.

### Relative quantification: the $`\Delta\Delta C_t`$ method

The aim is the ratio $`\rho_0^{\text{sample}}/\rho_0^{\text{control}}`$ for a gene of interest, between two conditions.

**Four reactions** are run: the gene of interest and a reference gene, in each of the sample and the control. The **reference gene** is one expressed at a constant level regardless of condition, a *housekeeping gene*, present at the same copy number in both.

**Step 1: first difference, within each condition.** Define

**Equation (29)**

```math
\Delta C_t^{\text{sample}} = C_t^{\text{sample}} - C_t^{\text{ref}}, \qquad \Delta C_t^{\text{control}} = C_t^{\text{control}} - C_t^{\text{ref}}
```

each using its own reaction's reference.

**Step 2: what a $`\Delta C_t`$ means.** At perfect amplification efficiency, each assay has its own intercept, $`b_{\mathrm{target}}`$ or $`b_{\mathrm{ref}}`$, set by its threshold and fluorescence response:

```math
C_t^{\mathrm{target}}=b_{\mathrm{target}}-\log_2\rho_0^{\mathrm{target}},\qquad C_t^{\mathrm{ref}}=b_{\mathrm{ref}}-\log_2\rho_0^{\mathrm{ref}}.
```

Subtracting gives $`\Delta C_t=b_{\mathrm{target}}-b_{\mathrm{ref}}-\log_2(\rho_0^{\mathrm{target}}/\rho_0^{\mathrm{ref}})`$. Therefore

**Equation (30)**

```math
\frac{\rho_0^{\text{target}}}{\rho_0^{\text{ref}}}=A\,2^{-\Delta C_t},\qquad A=2^{b_{\mathrm{target}}-b_{\mathrm{ref}}}.
```

The assay factor $`A`$ need not equal one. A single $`\Delta C_t`$ therefore does not directly give an absolute target/reference abundance ratio without cross-assay calibration. Crucially, $`A`$ cancels when the same two assays are compared between conditions.

A useful test is to imagine loading more of exactly the same RNA preparation into one reaction set. Target and reference should both appear earlier by the same cycle shift, leaving their difference unchanged. By contrast, a genuine target-specific expression change moves the target crossing without the matching reference shift. This is the causal distinction the first subtraction is designed to make; it works only for effects shared proportionally by both assays.

**Step 3: second difference, between conditions.** Dividing the two instances of (30):

```math
\frac{\rho_0^{\text{sample}}/\rho_0^{\text{ref}}}{\rho_0^{\text{control}}/\rho_0^{\text{ref}}} = \frac{2^{-\Delta C_t^{\text{sample}}}}{2^{-\Delta C_t^{\text{control}}}} = 2^{-(\Delta C_t^{\text{sample}}-\Delta C_t^{\text{control}})}
```

Defining $`\Delta\Delta C_t = \Delta C_t^{\text{sample}} - \Delta C_t^{\text{control}}`$:

**Equation (31)**

```math
\boxed{\;\frac{\rho_0^{\text{sample}}}{\rho_0^{\text{control}}} = 2^{-\Delta\Delta C_t}\;}
```


**Step 4: with real efficiency.** Repeating with $`(1+E)`$ in place of 2:

**Equation (32)**

```math
\frac{\rho_0^{\text{sample}}}{\rho_0^{\text{control}}} = (1+E)^{-\Delta\Delta C_t}
```

so (31) assumes $`E = 1`$ *for both the target and the reference*. This is the method's main hidden assumption.

**Assumptions of (31), stated explicitly:**
1. Both amplicons amplify with efficiency $`E = 1`$, and with the *same* efficiency as each other.
2. The reference gene is genuinely unchanged between the conditions.
3. Each assay's threshold and response are consistent between sample and control. Target and reference may have different assay intercepts; those differences cancel in the second subtraction.

### Melt-curve control

The intercalating dye of Section 16 reports *any* double-stranded DNA. The melt curve checks whether the signal is consistent with one dominant product at the expected melting temperature; it does not establish its sequence.

![Melting curves for three genotypes, and the corresponding −dF/dT derivative curves showing one peak per distinct product](../figs/AB-17-melt-curve.png)

1. After the last cycle, ramp the temperature up slowly while continuously reading fluorescence.
2. As each product melts, its strands separate, the dye is released, and fluorescence falls. This is the melting transition of Section 03, read out by dye rather than by absorbance.
3. Plot $`-dF/dT`$. Each distinct product gives a **peak** at its own $`T_m`$.

**Reading the result:**
- *One sharp peak*: consistent with one dominant product. Different products can have similar melting temperatures, so this is a specificity check rather than proof of identity.
- *Multiple peaks, a shoulder, or a broad peak*: more than one product. Different amplicons have different lengths and GC contents, hence different $`T_m`$ (Section 04).
- A peak at *low* temperature is characteristically a **primer dimer**: two primers amplifying each other, giving a short product that melts early.

The melt curve can expose some specificity problems without running a gel. Validated high-resolution melting assays can also distinguish genotypes through melting-profile differences, including heteroduplex formation. A heterozygote does not necessarily give two resolved peaks, and routine melt analysis does not automatically identify a genotype.

## Motivation and explanation

**Why the reference gene is the weak point.** Equation (31) is only as good as assumption 2. Genes described as "housekeeping" (GAPDH, actin, 18S rRNA) are *not* constant under all conditions; their expression changes with cell cycle, confluence, hypoxia and many treatments. If the reference shifts between conditions, that shift appears directly in $`\Delta\Delta C_t`$ and is misread as a change in the gene of interest. Good practice is to validate the reference for the specific conditions, or to use the geometric mean of several.

**Why the differences cancel what they cancel.** It is worth being precise about which error each subtraction removes:
- The *first* difference (target minus reference, within one sample) cancels anything affecting both reactions of that sample equally: the amount of input material, RNA recovery, reverse-transcription efficiency, pipetting of the template.
- The *second* difference (sample minus control) cancels the fixed **intercepts** of the same target and reference assays, including consistent fluorescence thresholds and response factors. Amplification efficiency still sets the concentration-to-cycle slope and must be equal between assays, or explicitly accounted for; taking a second difference does not remove that requirement.

What neither cancels is a difference in the reference gene's true expression, or a difference in amplification efficiency between the two amplicons.

**Absolute or relative?** Absolute is needed when the number itself matters: viral load, copies per genome, quantifying a standard. Relative is needed when a comparison matters: gene expression under treatment, knockdown efficiency. Relative is less work and usually more precise, because the subtractions remove systematic error that absolute quantification has to control explicitly.

## Link to other topics

Both subtractions are differential measurement: removing a common-mode error by taking a difference against a reference that experiences the same disturbance. It is the same principle as a differential pressure transducer, a Wheatstone bridge, or any tare weighing.

## Summary

A calibration curve converts $`C_t`$ into an absolute copy number and simultaneously reports efficiency. Two successive subtractions give a fold change, equation (31), with no calibration at all, because the unknown constants are shared and cancel.
<!-- note-content:end -->

[Previous](<AB-16 - Quantitative PCR and the cycle threshold.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-18 - Sequence-specific probes and RT-qPCR.md>)
