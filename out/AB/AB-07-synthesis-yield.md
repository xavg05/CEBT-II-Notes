# Section 07: Yield against length in oligonucleotide synthesis

## Overview

A coupling efficiency of 99 % sounds almost perfect. Compounded over every coupling in a long oligo, it is not. This note:
- derives the full-length yield $Y(n)=P^{n-1}$;
- derives the length at which yield halves;
- derives the distribution of failure products, with and without capping.

The conclusion is the reason oligos stop at about 200 nt and why genes are assembled from pieces.

*Assumed:* the synthesis cycle of Section 06; independent probabilities multiply.

## Intuition

Each coupling is a coin toss that lands "success" with probability $P$. The full-length product needs *every* toss to succeed, so the probabilities multiply and the yield decays geometrically: a fixed *fraction* is lost per nucleotide, not a fixed amount. Halving the failure rate per step roughly doubles the length that can be made at a given yield.

## Derivation

Notation: $n$ is the oligo length (nt); $P$ is the coupling efficiency (probability that a chain adds the next monomer in one cycle); $Y(n)$ is the fraction of chains that are full length.

**Assumptions.** Every coupling succeeds independently with the same $P$, whatever the base or position. Capped failures never react again. Losses from depurination and deprotection are ignored. The first nucleoside is pre-attached to the bead, so an $n$-mer needs $n-1$ couplings.

**Step 1: full-length yield.** All $n-1$ couplings must succeed, and they are independent:
$$Y(n) = P^{\,n-1} \tag{1}$$

**Step 2: half-yield length.** Set $Y = \tfrac12$ and take logarithms. For $P$ close to 1, $\ln P\approx -(1-P)$:
$$n_{1/2} = 1+\frac{\ln 2}{-\ln P} \approx 1 + \frac{0.693}{1-P} \tag{2}$$
The usable length scales as $1/(1-P)$, the inverse of the failure rate.

**Step 3: truncation spectrum (with capping).** A chain that is length $k$ when it fails is capped and stays length $k$. That requires $k-1$ successes and then one failure:
$$\Pr(\text{length } k) = P^{\,k-1}(1-P), \qquad k = 1,\dots,n-1 \tag{3}$$
This is a geometric distribution. Summing (3) over $k$ gives $1-P^{n-1}$, so together with (1) the probabilities add up to 1.

**Step 4: deletions (without capping).** If failed chains are not capped, each continues in the next cycle. A chain then ends at full nominal length minus the number of failures. The number of failures in $n-1$ attempts is binomial, so the fraction with exactly one internal deletion is:
$$\Pr(\text{one deletion}) = (n-1)(1-P)P^{\,n-2} \tag{4}$$

## Motivation and explanation

![Theoretical full-length product against oligo length for 99.4 % and 99.1 % coupling efficiency](figs/AB-07-yield-vs-length.png)

- **Small differences in $P$ compound.** 99.4 % against 99.1 % looks like a trivial gap, but by (2) the half-yield length is 116 nt against 78 nt.
- **Capping does not raise the yield.** Equation (1) holds either way. What capping changes is *what the impurities are*. With capping, the impurities from (3) are spread over all lengths (mean about 28 nt for a 60-mer) and lack the final DMT. Without capping, (4) gives a large population of $(n-1)$-mers with an internal error that are nearly impossible to separate from the product.
- **When (1) is optimistic.** Purine-rich sequences depurinate more. Some monomers (modified bases, RNA) couple less well. Secondary structure on the bead can hinder coupling. Purification also loses product. Real yields of long oligos are therefore lower than (1).

## Worked example

*For coupling efficiencies of 99.4 % and 99.1 %, find the full-length yield for 20, 60, 120 and 200 nt, the half-yield length, and the impurity profile of a 60-mer.* Computed in Python.

| $n$ (nt) | $Y$ at $P=0.994$ | $Y$ at $P=0.991$ |
|---|---|---|
| 20 | 0.892 | 0.842 |
| 60 | 0.701 | 0.587 |
| 120 | 0.489 | 0.341 |
| 200 | 0.302 | 0.165 |
| $n_{1/2}$ from (2) | 116 | 78 |

The 120-nt values match the plotted curve (≈49 % and ≈34 %).

**Coupling efficiency needed for longer oligos.** For 50 % full-length yield at 200 nt, (1) needs $P = 0.5^{1/199} = 0.99652$. At 1000 nt it needs $P = 0.99931$. Each tenfold increase in length needs a tenfold smaller failure rate.

**A 60-mer at $P = 0.994$:**
- 70.1 % full length and 29.9 % truncated. The truncations have a mean length of 28.3 nt, and only 0.42 % are the $(n-1)$-mer.
- Without capping, 25.0 % of chains would be single-deletion 59-mers carrying DMT, and 4.4 % would have two deletions.

Capping therefore turns a 25 % impurity that cannot be separated into a spread of short truncations that can.

## Link to other topics

Equation (1) is the same compounding that sets step-growth polymer chain lengths (Carothers) and the overall yield of any multi-step synthesis or separation train: overall yield is the product of the step yields.

## Conclusion

Full-length yield falls as $P^{n-1}$, so the usable length scales as $1/(1-P)$: about 100–200 nt at today's 99–99.5 % coupling. Capping does not raise the yield, but it makes the failures easy to remove. Longer DNA has to be assembled from oligos, which is the subject of Section 08.
