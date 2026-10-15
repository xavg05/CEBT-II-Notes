[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)

<!-- note-content:start -->
# Section 19: Aptamers and SELEX

## Intuition

An antibody binds its target because the protein folds into a complementary surface. Nothing in that argument requires a protein. A single strand also folds — through internal pairing, stacking and structures like G-quadruplexes — into loops, bulges and pockets, and given enough sequences some of those shapes will fit any target.

The difficulty is the search: no theory maps sequence to affinity, so a binder cannot be designed. But nucleic acids have a property no protein has — **they can be copied** — which makes an evolutionary search possible in a tube. Make every sequence you can, keep those that bind, copy them, repeat. Each round the binders take a larger share, and after enough rounds you sequence the pool to find out what you made.

*Analogy:* finding the few people in a stadium who can pick a particular lock, without knowing what makes a good lock-picker. Give everyone a go, keep whoever succeeds, let each recruit a thousand copies of themselves, and repeat. It breaks down at the crucial point: SELEX generates no new variation, only selection on what the library already contained, unless mutagenic PCR is used deliberately.

## Mechanism

**Definition.** An aptamer is a short DNA or RNA oligonucleotide selected to bind a specific target — a small molecule, a protein, or a whole cell. Affinity is quoted as the dissociation constant $K_d$, typically nanomolar and sometimes tens of picomolar, comparable with antibodies. The name is from the Latin *aptus*, "to fit".

### The SELEX cycle

![The SELEX cycle: a random library is incubated with the target, unbound sequences are washed away, bound sequences are eluted and amplified, and the enriched pool enters the next round; after the final round the pool is cloned and sequenced](../figs/AB-19-SELEX-cycle.png)

**1. The naïve library.** $10^{13}$ to $10^{15}$ distinct oligonucleotides. Each has the same three-part architecture:
$$\underbrace{\text{constant, 15–25 nt}}_{\text{primer site}} \;-\; \underbrace{\text{random, 20–80 nt}}_{\text{variable region}} \;-\; \underbrace{\text{constant, 15–25 nt}}_{\text{primer site}}$$
The **random region** supplies the diversity, since every member folds differently. The **constant flanks** are identical in every member, so one primer pair amplifies the whole library whatever lies between them — which is what makes the pool copyable, and the reason the architecture exists.

*The library is made in one synthesis:* in the random region, all four phosphoramidites are supplied together at each coupling step (Section 06), so every bead receives a random base at every position.

**2. Incubate** with the target, usually immobilised on beads or a column. Each sequence binds according to its fold.

**3. Wash** away unbound and weakly bound sequences. This is the selection: physical removal of the failures.

**4. Elute** by changing ionic strength, pH or temperature, releasing the strong binders. The recovered pool is **enriched**.

**5. Amplify** by PCR, restoring a workable quantity. For RNA aptamers the pool is reverse-transcribed (Section 18), amplified as DNA, then transcribed back.

This step is easy to overlook and is the crux of the method. After a wash only a trace of material remains, far too little to use. Amplification restores the numbers while preserving the composition, so selection can be applied again. **It is the only reason this works on nucleic acids and not on proteins** — a selected protein cannot copy itself.

**6. Repeat 10–15 times**, raising stringency in later rounds (shorter incubation, harsher washes, less target).

**7. Sequence** the final pool (Sections 10–12) and measure $K_d$ for the aptamers that emerged.

### Cell-SELEX

Whole cells as the target, used to find aptamers for drug delivery that recognise a cell *type* rather than a purified molecule. Its distinguishing feature is **negative (counter) selection**: the library is first exposed to the wrong cells (say, healthy ones) and the sequences that **do not** bind are kept, before the remainder is exposed to the target cells. The result binds target cells and not controls — selectivity, not merely affinity. The trade-off is that the molecular target is **unknown**: the aptamer binds something on the surface, but the selection does not reveal what.

## Motivation and explanation

**Why enrichment is exponential.** Each round multiplies the ratio of binders to non-binders by an enrichment factor $f$, the ratio of their survival probabilities through wash and elution. After $r$ rounds that ratio has grown by $f^{\,r}$ — the "exponential enrichment" of the name, and the reason a vanishingly rare binder can come to dominate.

The wash is also a kinetic experiment. Once free target or free aptamer is removed, a bound sequence that dissociates may be swept away before it can rebind. Longer washing can therefore favour slow dissociation, while a short incubation can favour fast association. These are different routes to enrichment from simply having a low equilibrium $K_d$. The recovered candidates must be characterised under the conditions relevant to their eventual use.

**Aptamers against antibodies.**

| | Aptamers | Antibodies |
|---|---|---|
| Production | chemical synthesis, *in vitro* | animals or cell culture |
| Batch variation | negligible, defined sequence | significant |
| Target range | includes toxins and small molecules | needs an immune response |
| Stability | thermally stable, refolds reversibly | denatures irreversibly |
| Modification | straightforward (Section 06) | harder |
| Size | small, better tissue penetration | large |
| *In vivo* lifetime | **short**: nuclease degradation, renal clearance | long |
| Track record | approved therapeutic examples include pegaptanib and avacincaptad pegol | many approved therapeutics |

The deciding weakness *in vivo* is degradation, addressed by chemical modification: 2′-fluoro or 2′-O-methyl substitutions resist nucleases, and PEGylation slows renal clearance by increasing effective size.

**Limitations of the method.**
- *PCR bias.* Some sequences amplify better than others regardless of binding, so they enrich for the wrong reason. Sequences that amplify well but bind poorly can take over the pool.
- *Affinity is not specificity.* Selecting for the tightest binding does not select against binding other things, unless counter-selection is used explicitly.
- *The constant regions participate.* The flanks can take part in folding, so an aptamer may lose activity when truncated to its random region alone.

## Worked example

*Sequence-space coverage, and the arithmetic of enrichment.* Computed in Python.

**1. How much of sequence space does a library cover?** A library of $10^{15}$ molecules is $10^{15}/6.022\times10^{23} = 1.7$ nanomoles — a vanishingly small amount of material, and about the largest number of distinct molecules that can be handled.

| Random region $n$ | $4^n$ sequences | Fraction covered by $10^{15}$ |
|---|---|---|
| 20 | $1.1\times10^{12}$ | all of it (each present ~1000×) |
| 30 | $1.2\times10^{18}$ | $8.7\times10^{-4}$ |
| 40 | $1.2\times10^{24}$ | $8.3\times10^{-10}$ |
| 80 | $1.5\times10^{48}$ | $7\times10^{-34}$ |

At $n = 20$ the library is **complete**, with every possible sequence present a thousand times over. By $n = 40$ it samples under one in a billion. A typical 40–80 nt random region therefore means SELEX is a random sample of a space it could never enumerate — which is why the method is an evolutionary search and not a screen.

**2. How enrichment compounds.** Take an initial binder fraction of $10^{-10}$ (one good binder in ten billion) and a tenfold enrichment per round:

| Round | Fraction of pool that binds |
|---|---|
| 0 | $10^{-10}$ |
| 3 | $10^{-7}$ |
| 6 | $10^{-4}$ |
| 9 | 0.09 |
| 12 | 0.99 |
| 15 | 0.99999 |

The pool is almost pure binder by round 12. The curve is flat for many rounds and then turns over sharply, which is the signature of exponential growth from a small base: nothing appears to be happening for eight rounds, then the composition changes completely within three.

**This explains the protocol.** Fewer than about 10 rounds and the pool is still mostly junk. Beyond about 15 the gain is negligible, while PCR bias accumulates and diversity is lost. **Ten to fifteen rounds is where the enrichment has saturated but the pool has not yet degenerated.**

**3. Why stringency must rise.** Once the pool is mostly binders, a wash that removes non-binders no longer discriminates: everything survives, $f \to 1$, and enrichment stops. Harsher later conditions re-create a survival difference between good and excellent binders, keeping $f > 1$ so that *affinity* keeps improving rather than merely purity.

## Applications

**Therapeutics.** *Pegaptanib* (Macugen) is a modified RNA aptamer that antagonises VEGF in macular degeneration. PEGylation and injection directly into the eye address its short systemic lifetime. It was the first approved aptamer medicine, rather than the only one: *avacincaptad pegol* (Izervay), approved by the FDA in 2023, is a PEGylated RNA aptamer that inhibits complement protein C5 for geographic atrophy secondary to age-related macular degeneration. These examples show that nucleic-acid recognition can target different disease mechanisms.

**Biosensing.** The anti-thrombin aptamer is the best-studied example and folds around a **G-quadruplex** (Section 01), as many aptamers do. Others detect viral spike proteins, and small molecules such as cocaine and theophylline — targets that are hard to raise antibodies against, because small molecules are poorly immunogenic.

## Wider pathway

SELEX is one instance of a general strategy: make a huge library, apply a physical selection, amplify the survivors, repeat. The same logic drives phage display for antibodies (Section 30) and directed evolution of enzymes. What differs is how the selected molecule is linked to a copyable sequence — here trivially, because the molecule *is* the sequence.

## Link to other topics

The cycle is a staged separation with recycle: each round is a separation whose cut is imperfect, and feeding the product back repeatedly turns a weak single-stage separation factor into a sharp overall one. The same reasoning gives a cascade of stages its resolving power.

## Summary

A folded single strand can bind a target as an antibody does, but no theory predicts which sequence folds the right way. SELEX replaces prediction with iterated selection and amplification, exploiting the one property that makes nucleic acids uniquely suited to directed evolution: a selected molecule can copy itself.

## Conclusion

Selection conditions determine which binding properties are enriched, so amplification alone is never evidence of useful specificity. The next unit develops dna nanotechnology.
<!-- note-content:end -->

[Subject index](../README.md) · [Topic overview](README.md) · [Complete section](<Complete section.md>)
