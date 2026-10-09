# DNA synthesis and gene assembly — reading 02.2

[Previous](02-01-dna-synthesis-and-gene-assembly.md) · [Subject index](README.md) · [Next](02-03-dna-synthesis-and-gene-assembly.md)

<!-- reading-content:start -->
## Section 07: Yield against length in oligonucleotide synthesis

### Intuition

Each coupling is a coin toss that lands "success" with probability $`P`$. The full-length product needs *every* toss to succeed, so the probabilities multiply and the yield decays geometrically: a fixed *fraction* is lost per nucleotide, not a fixed amount. Halving the failure rate per step roughly doubles the length that can be made at a given yield.

### Derivation

Notation: $`n`$ is the oligo length (nt); $`P`$ is the coupling efficiency (probability that a chain adds the next monomer in one cycle); $`Y(n)`$ is the fraction of chains that are full length.

**Assumptions.** Every coupling succeeds independently with the same $`P`$, whatever the base or position. Capped failures never react again. Losses from depurination and deprotection are ignored. The first nucleoside is pre-attached to the bead, so an $`n`$-mer needs $`n-1`$ couplings.

**Step 1: full-length yield.** All $`n-1`$ couplings must succeed, and they are independent:

```math
Y(n) = P^{\,n-1} \tag{19}
```


**Step 2: half-yield length.** Set $`Y = \tfrac12`$ and take logarithms. For $`P`$ close to 1, $`\ln P\approx -(1-P)`$:

```math
n_{1/2} = 1+\frac{\ln 2}{-\ln P} \approx 1 + \frac{0.693}{1-P} \tag{20}
```

The usable length scales as $`1/(1-P)`$, the inverse of the failure rate.

**Step 3: truncation spectrum (with capping).** A chain that is length $`k`$ when it fails is capped and stays length $`k`$. That requires $`k-1`$ successes and then one failure:

```math
\Pr(\text{length } k) = P^{\,k-1}(1-P), \qquad k = 1,\dots,n-1 \tag{21}
```

This is a geometric distribution. Summing (21) over $`k`$ gives $`1-P^{n-1}`$, so together with (19) the probabilities add up to 1.

**Step 4: deletions (without capping).** If failed chains are not capped, each continues in the next cycle. A chain then ends at full nominal length minus the number of failures. The number of failures in $`n-1`$ attempts is binomial, so the fraction with exactly one internal deletion is:

```math
\Pr(\text{one deletion}) = (n-1)(1-P)P^{\,n-2} \tag{22}
```


### Motivation and explanation

![Theoretical full-length product against oligo length for 99.4 % and 99.1 % coupling efficiency](figs/AB-07-yield-vs-length.png)

- **Small differences in $`P`$ compound.** 99.4 % against 99.1 % looks like a trivial gap, but by (20) the half-yield length is 116 nt against 78 nt.
- **Capping does not raise the yield.** Equation (19) holds either way. What capping changes is *what the impurities are*. With capping, the impurities from (21) are spread over all lengths (mean about 28 nt for a 60-mer) and lack the final DMT. Without capping, (22) gives a large population of $`(n-1)`$-mers with an internal error that are nearly impossible to separate from the product.
- **When (19) is optimistic.** Purine-rich sequences depurinate more. Some monomers (modified bases, RNA) couple less well. Secondary structure on the bead can hinder coupling. Purification also loses product. Real yields of long oligos are therefore lower than (19).

### Worked example

*For coupling efficiencies of 99.4 % and 99.1 %, find the full-length yield for 20, 60, 120 and 200 nt, the half-yield length, and the impurity profile of a 60-mer.* Computed in Python.

| $`n`$ (nt) | $`Y`$ at $`P=0.994`$ | $`Y`$ at $`P=0.991`$ |
|---|---|---|
| 20 | 0.892 | 0.842 |
| 60 | 0.701 | 0.587 |
| 120 | 0.489 | 0.341 |
| 200 | 0.302 | 0.165 |
| $`n_{1/2}`$ from (20) | 116 | 78 |

The 120-nt values match the plotted curve (≈49 % and ≈34 %).

**Coupling efficiency needed for longer oligos.** For 50 % full-length yield at 200 nt, (19) needs $`P = 0.5^{1/199} = 0.99652`$. At 1000 nt it needs $`P = 0.99931`$. Each tenfold increase in length needs a tenfold smaller failure rate.

**A 60-mer at $`P = 0.994`$:**
- 70.1 % full length and 29.9 % truncated. The truncations have a mean length of 28.3 nt, and only 0.42 % are the $`(n-1)`$-mer.
- Without capping, 25.0 % of chains would be single-deletion 59-mers carrying DMT, and 4.4 % would have two deletions.

Capping therefore turns a 25 % impurity that cannot be separated into a spread of short truncations that can.

### Link to other topics

Equation (19) is the same compounding that sets step-growth polymer chain lengths (Carothers) and the overall yield of any multi-step synthesis or separation train: overall yield is the product of the step yields.

### Summary

Full-length yield falls as $`P^{n-1}`$, so the usable length scales as $`1/(1-P)`$: about 100–200 nt at today's 99–99.5 % coupling. Capping does not raise the yield, but it makes the failures easy to remove.

## Section 08: Assembling genes from synthetic oligonucleotides

### Intuition

The problem is not making the bonds, since enzymes do that readily. The problem is making the pieces join *in the right order* when they are all mixed in one tube.

The answer is to let the sequence carry the ordering information. Each piece is designed so that its end is complementary to the start of the piece that should follow it. Two pieces can therefore only hybridise where they are meant to be adjacent, and enzymes then make the joint permanent. Nothing has to be added in a particular order, and nothing has to be positioned.

*Analogy:* a jigsaw in which every edge is cut to fit exactly one neighbour. You can shake the box and correct pairs will find each other. The analogy breaks down in two places. First, jigsaw edges either fit or they do not, whereas DNA overlaps bind with a *strength* that varies with sequence and temperature, so near-matches can mis-join. Second, a jigsaw piece cannot be built wrong, whereas every enzymatic copying step can introduce a sequence error.

### Mechanism

The methods differ in what the starting pieces are and in which enzymes finish the joint, but they share one logic:

**1. Design the overlaps.** Neighbouring pieces are given a shared region of sequence, typically 20–50 bases. This is the "address" that determines adjacency.

**2. Let the overlaps hybridise.** The mixture is held at a temperature at which an intended overlap is stably paired but shorter, accidental complementarity is not. This is a direct application of Section 03: the correct overlap must have a melting temperature comfortably above the working temperature, and spurious matches must have one below it.

**3. Convert the hybrid into continuous double-stranded DNA.** A polymerase extends base-paired 3′ ends to fill in single-stranded regions, and where two strands abut, a ligase closes the remaining break in the backbone.

**4. Select the full-length product.** Partial assemblies always form. They are removed either by amplifying only molecules that carry both end sequences, or by separating on size.

![Overlapping oligonucleotides on alternating strands are extended into longer products, then amplified from the two ends](figs/AB-08-PCA.png)

![Fragments sharing end sequences are processed to expose complementary single strands, which anneal and are repaired into a continuous duplex](figs/AB-08-Gibson.png)

**Two regimes.** Starting from short synthetic oligos, the overlaps tile the whole target and the polymerase does most of the building; this reaches a few kilobases. Starting from existing double-stranded fragments, the overlaps exist only at the joints, which are exposed as single strands before annealing; this joins much larger pieces, is seamless (it leaves no scar sequence at the joint) and runs at a single temperature in one tube. The second is what makes assembly above a few kilobases practical.

### Motivation and explanation

**Why overlaps must have matched melting temperatures.** All joints are processed at the same temperature. If one overlap had a much lower $`T_m`$ than the others, it would be largely unpaired at the working temperature and that joint would fail; if one were much higher, it would tolerate mismatches and allow incorrect joints. Designing overlaps to a common $`T_m`$, rather than a common length, is therefore the central design rule, and it is why GC content matters (Section 04).

**Why secondary structure is excluded.** A piece that folds back on itself competes with the intended pairing. A hairpin is unimolecular, so unlike hybridisation its stability does not fall when the solution is diluted (Section 03). It can therefore dominate at exactly the concentrations used.

**Why errors set the real limit.** Assembly is not limited by how long a molecule can be built, but by the chance that the molecule is *correct*. Chemical synthesis introduces errors, and so does every enzymatic copying step. Errors are roughly independent per base, so the probability that a construct is error-free falls exponentially with length. This is the same compounding as Section 07, and it is why long constructs are built from verified pieces rather than in one step.

**Where the approach fails.** Repetitive sequences defeat it entirely, because an overlap is no longer unique and pieces join in the wrong order or loop out. Very GC-rich or structured regions resist both synthesis and annealing.

### Worked example

*Overlap design and error accounting.* All numbers computed in Python.

**1. How many pieces?** Tiling a 1 kb target with 60-nt oligos overlapping by 20 nt advances $`60-20 = 40`$ nt per oligo, so it needs $`(1000-20)/40 \approx 25`$ oligos.

**2. Is a 20-base overlap stable at the working temperature?** For the 20-mer of Section 05, at 0.25 µM, the nearest-neighbour model (Section 04) with the salt correction gives:

| Na⁺ | $`T_m`$ |
|---|---|
| 1 M | 66.2 °C |
| 0.05 M | 51.4 °C |

At a typical buffer ionic strength, a 20-base overlap melts at around 50–55 °C. That sits just above a 50 °C working temperature, which is why overlaps of this length are the shortest used, and why longer overlaps (40–50 bases) are preferred when the joint must be robust.

**3. Error-free fraction of a 1 kb construct.** With a per-base error probability $`\varepsilon`$, the chance that all 1000 bases are correct is $`(1-\varepsilon)^{1000}`$:

| $`\varepsilon`$ | Error-free fraction | Clones to screen for 95 % chance of one correct |
|---|---|---|
| 1 in 300 | 3.5 % | 83 |
| 1 in 600 | 18.9 % | 15 |
| 1 in 1500 | 51.3 % | 5 |

The last column is $`\ln(0.05)/\ln(1-Y)`$, the number of independent clones needed before the probability of finding no correct one falls below 5 %.

This is why a synthetic gene is always *sequence-verified* (Sections 10–12) rather than simply used, and why halving the error rate matters more than any improvement in assembly yield.

### Wider pathway

Assembled, verified genes are the input to everything downstream in this course: expressing an engineered protein (Section 29), building a genetic circuit (Sections 48–52), and the hierarchical construction of whole genomes (Section 09). The sequence-verification step at the end of assembly is what links this section to sequencing, which is the subject of the next three sections.

### Link to other topics

The design rule "match the $`T_m`$ of every joint" is the same reasoning as specifying a common operating temperature for a set of parallel units in a process: the slowest or least stable element sets the condition that all the others must tolerate.

### Summary

Enzymatic assembly solves ordering by writing adjacency into the sequence as overlaps, then converting hybridised overlaps into continuous duplex. The design constraints follow directly from hybridisation thermodynamics: overlaps matched in melting temperature and free of competing structure.
<!-- reading-content:end -->

[Previous](02-01-dna-synthesis-and-gene-assembly.md) · [Subject index](README.md) · [Next](02-03-dna-synthesis-and-gene-assembly.md)
