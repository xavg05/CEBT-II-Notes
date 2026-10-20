[Previous](<AB-13 - Nanopore sequencing.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-15 - Applications of nucleic acid sequencing.md>)

<!-- note-content:start -->
# Section 14: PacBio SMRT sequencing and comparison of platforms

## Intuition

To watch one polymerase add bases in real time, two things must be solved.

**The background problem.** The reaction needs labelled nucleotides at micromolar concentrations so that the polymerase finds them quickly. But in any ordinary illuminated volume there are thousands of free labelled nucleotides diffusing about, all fluorescing. The one sitting in the polymerase is invisible against them. The fix is to make the observed volume so small that, on average, it contains almost no free nucleotides: then anything bright is almost certainly the one being incorporated.

**The persistence problem.** In Illumina, the label stays attached and must be chemically cleaved off between cycles, which stops the reaction, costs time, and leaves scars (Section 12). Here the aim is continuous operation, so the label must remove *itself* as part of the chemistry. The fix is to attach it to the part of the nucleotide that the reaction discards anyway.

*Analogy:* watching one worker on a crowded factory floor by shining a spotlight on a patch the size of a single workstation, and giving each component a tag on the packaging rather than the part, so the tag leaves with the rubbish. The analogy breaks down because the "spotlight" is not a beam that can be aimed: the confinement is a property of the aperture itself, as described below.

## Mechanism

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

## Motivation and explanation

**Why repeated observations improve accuracy.** SMRT pulse detection has stochastic errors that can often be reduced by combining passes over the same molecule. Nanopore measurements also contain random error as well as sequence-context-dependent bias, and repeated reads can improve their consensus too. The important statistical distinction is between independent error, which repeated observations reduce, and correlated error, which can persist. Neither platform has perfectly independent errors or a universal quality ceiling determined by its mechanism alone. Actual consensus accuracy must be measured for the chemistry, specimen and analysis used.

**The trade-off in read length.** The polymerase processivity is fixed, so a read of total length $`L`$ over an insert of length $`\ell`$ gives $`L/\ell`$ passes. Longer inserts give longer reads but fewer passes, hence lower accuracy. Shorter inserts give higher accuracy but less reach. This is a design choice made per experiment, and it has no analogue on the other platforms.

The repeated passes belong to one original insert. They improve confidence in that molecule's sequence, but they do not supply independent molecules for estimating the frequency of a rare variant in a sample. Conversely, sequencing many different molecules once increases sample coverage without giving each one the repeated observations used for circular consensus. An experiment must budget separately for accurate molecular reads and representative sampling.

**Limitations.**
- *Cost per base* is high, above both Illumina and nanopore.
- *The instrument* is large, expensive and not portable, in contrast to the hand-held nanopore device.
- *Run time* is long, 15–30 hours.
- *Library preparation* requires circularisation, so it is more involved than nanopore's.

## Comparison of platforms

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

## Wider pathway

Sections 10–14 complete the reading side of the field. What they enable is covered in Section 15, and the methods recur throughout: sequencing verifies every construct built in Sections 06–09, quantifies transcripts alongside the amplification methods of Sections 16–18, and reads out the selections in Section 19.

## Link to other topics

The ZMW is an evanescent-field device: below the cut-off size an aperture carries no propagating mode, and the field decays exponentially. The same physics appears in waveguides below cut-off and in total internal reflection, and it is used here as a way of defining a reaction volume optically rather than physically.

## Summary

Confining the observation volume and placing the label on the leaving group allow one polymerase to be monitored continuously. Circularising the template supplies repeated observations for consensus; stochastic errors can be reduced, while correlated errors and insufficient passes limit the gain. HiFi accuracy is an observed platform result, rather than a guarantee from a chosen raw error rate alone.
<!-- note-content:end -->

[Previous](<AB-13 - Nanopore sequencing.md>) · [Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>) · [Next](<AB-15 - Applications of nucleic acid sequencing.md>)
