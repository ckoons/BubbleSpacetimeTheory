---
title: "The Information Cost of Recombination: an exact per-generation channel for meiotic transmission"
author: "C. S. Koons and Lyra"
date: "2026-09-05"
---

# Abstract

We model meiotic transmission as a communication channel between generations and show that the
information a parent forwards to an offspring is **n - H(d)** bits, where n is the number of
inter-locus junctions and H(d) is the entropy of the crossover pattern. The result holds for **any**
crossover process, including one with arbitrary interference; independence is only the special case
in which the channel factorises into independent binary symmetric channels, one per junction. Two consequences follow in closed form: (i) the linkage information a parent forwards
to an offspring is **1 - H_2(r)** bits per junction, where H_2 is the binary entropy function, so
that forwarding and novelty trade one for one and no recombination rate maximises both; (ii) the information half-life of
a chromosomal segment of genetic length d is ln 2 / d generations, giving 69 generations for a
1 cM block and less than one generation for a chromosome arm. We show that information decays
faster than correlation, so linkage disequilibrium measured as r-squared overstates the surviving
information in half-life. We extend the model to arbitrary ploidy, where
the state space is quotiented by the automorphism group of the pairing structure, and find that
multivalent pairing destroys record roughly twice as fast per crossover as bivalent pairing at the
same ploidy while starting with less. Finally we report a **negative result**: at matched genetic
material, outcrossing carries no information advantage over selfing in this model. We are explicit
throughout about which known phenomena we explain and which we merely price.

# 1. Introduction, and what is not ours

Shannon opened by crediting Nyquist and Hartley. We follow that practice, because most of the
apparatus here is not new and the reader is entitled to know which part is.

Mutual information has been used in population genetics for decades; multilocus linkage
disequilibrium measures built on mutual information are established, and under a linear
approximation such a measure reduces to the familiar r-squared. The geometric decay of linkage
disequilibrium as (1-r)^n is textbook. The **obligate crossover** -- the requirement of at least one
crossover per bivalent for correct disjunction -- is established, as is **crossover interference**,
and it is already understood that crossover frequency and interference strength are jointly
constrained so as to guarantee the obligate crossover at a low total crossover number.
**Diploidization** of polyploids toward bivalent pairing is a long-known cytological fact with
established mechanical explanations. **"Junction" is Fisher's noun**, and the whole of Section 5 --
segment survival e^(-nd) under Haldane's Poisson map, the half-life (ln 2)/d, and the ancestral
block count C + nM -- is Fisher's theory of junctions (Fisher 1949, 1954) as developed by Stam
(1980) and Chapman and Thompson (2003); Section 5 restates it in our currency and claims none of
it. The channel identity itself -- an additive-noise channel on a finite abelian group has capacity
log|G| - H(noise) -- is textbook (Cover and Thomas, the modulo-additive channel).

We do not claim any of those. What we claim is narrower:

1. The **identification**: in the difference coordinate, meiotic transmission of linkage phase IS
   the modulo-additive channel, with the crossover-indicator pattern as the noise, so that the
   textbook identity applies verbatim and for any crossover process. We have not found the
   identification stated. It is not the same object as an inter-locus LD measure: it is a channel
   between *generations*, not an association within a *population*.
2. The consequent retention law **1 - H_2(r)**. (Corollary 2's identity T + N = 1 is a
   restatement of it, since N is *defined* as H_2(r); we do not count it as a separate claim.)
3. An information **currency** for costs that already have mechanical explanations. We do not
   explain the obligate crossover -- segregation does. We price it: every crossover beyond the
   obligate one costs exactly H_2(r) bits of forwarded record. Likewise for diploidization.
4. The observation that information half-life is systematically **shorter** than correlation
   half-life, which is a caution for anyone reading LD as a proxy for surviving information.
5. One negative result (Section 8).

# 2. The model

Consider a diploid individual at L ordered loci, heterozygous at every locus. Write the **phase**
as p in {0,1}^L, where p_i records which of the two homologs carries the allele labelled 1 at
locus i. Phase is defined modulo global complement, since the homologs are unlabelled; the phase
space therefore has 2^(L-1) elements.

Meiosis is modelled as follows. A gamete is assembled by walking the L loci and copying from one
homolog, switching homologs independently at each of the L-1 junctions with probability r, the
recombination fraction. Write the switch pattern as g in {0,1}^L, so that the gamete's allele
vector is a = NOT(g XOR p).

To keep the offspring heterozygous at every locus and the state space closed, we take the partner
gamete to be the complement of a. This is the standard backcross-to-a-heterozygous-tester design.
Section 8 relaxes it.

**Definition.** The *difference coordinate* of a phase p is D(p) in {0,1}^(L-1) with
D(p)_i = p_i XOR p_{i+1}. D is a bijection from phase space (modulo complement) to {0,1}^(L-1).

# 3. Theorem 1 (exact reduction)

> **Theorem 1.** In the difference coordinate, meiotic transmission acts as
> D(offspring) = D(parent) XOR d, where d is the crossover-indicator pattern.
> **For any distribution of d whatever, the transmitted information is**
>
>   **I = n - H(d) bits,   n = L - 1.**
>
> If the d_i are independent Bernoulli(r) this factorises into n independent binary symmetric
> channels and H(d) = n H_2(r); but independence is not needed for the identity.

*Proof.* The offspring phase is q = a = NOT(g XOR p), which modulo global complement equals
g XOR p. Then

  D(q)_i = q_i XOR q_{i+1} = (p_i XOR g_i) XOR (p_{i+1} XOR g_{i+1}) = D(p)_i XOR D(g)_i.

The switch pattern g contributes only through D(g)_i = g_i XOR g_{i+1}, which is by construction
the indicator of a crossover at junction i. Set d = D(g). The starting homolog, the only other
freedom in g, is annihilated by the quotient by global complement, so d is independent of D(p).
With D(p) uniform, D(q) = D(p) XOR d is uniform, and

  I(D(p); D(q)) = H(D(q)) - H(D(q) | D(p)) = n - H(d),

since conditioning on the parent leaves exactly the entropy of d. QED

**Remark.** Nothing in this proof uses independence of the d_i. Crossover interference changes the
distribution of d and therefore H(d); it does not touch the identity. Section 6a computes what
interference is worth. Two things the proof does use. First, that d is independent of D(p):
crossover placement does not read phase, which is the model's assumption and the biological one.
Second, uniform input: the theorem states the mutual information at a uniform phase distribution,
and because the noise is additive on the group F_2^n the uniform input is capacity-achieving, so
n - H(d) is the channel's capacity and not merely its rate at one input. At a population's actual
(LD-bearing) phase distribution the transmitted information is at most this.

**Corollary 1 (retention).** The mutual information between parent and offspring phase is

  **I = (L-1) (1 - H_2(r))   bits**,

i.e. **1 - H_2(r) bits per junction per generation**, with H_2(x) = -x log2 x - (1-x) log2(1-x).

**Corollary 2 (zero-sum, definitional).** Writing T = 1 - H_2(r) for the forwarded information
per junction and N = H_2(r) for the information created per junction, T + N = 1 for every r. This
cannot fail, because N is defined as H_2(r); it is recorded as the accounting used in Section 5,
not as a result.

**Verification.** Theorem 1 was checked against brute-force enumeration of the full joint
distribution for n = 3, 5, 7 against five crossover processes each: independent at r = 0.10 and
r = 0.25, exactly-one-crossover (maximal interference), a hotspot-restricted process, and a
**deliberately correlated random distribution on all of F_2^n**. All fifteen agree with n - H(d)
to within 1e-9. Corollary 1 was separately checked for L = 3, 5, 7 and r in
{0, 0.01, 0.05, 0.10, 0.25, 0.50}, agreeing to 8.1e-13. Corollary 2 needs no check.

# 4. The range

| r | retained T | created N | biological setting |
|---|---|---|---|
| 0.000 | **1.0000** | 0.0000 | inversion, supergene, Y chromosome, mtDNA |
| 0.001 | 0.9886 | 0.0114 | ~0.1 cM |
| 0.010 | 0.9192 | 0.0808 | ~1 cM (~1 Mb in human) |
| 0.050 | 0.7136 | 0.2864 | ~5 cM |
| 0.100 | 0.5310 | 0.4690 | ~11 cM |
| 0.200 | 0.2781 | 0.7219 | ~26 cM |
| 0.500 | **0.0000** | 1.0000 | unlinked |

The endpoints are the two degenerate regimes. At r = 0 the channel is noiseless and forwards
everything, creating nothing; at r = 1/2 it forwards nothing.

# 5. Decay over generations (known; restated in our currency)

Everything in this section is Fisher's theory of junctions (Fisher 1949, 1954; Stam 1980; Chapman
and Thompson 2003), with Haldane's (1919) Poisson map; we restate it because Section 6 needs it in
bits. Composing n generations of the channel gives a binary symmetric channel with crossover probability
p_n = (1 - (1-2r)^n)/2, so retention after n generations is 1 - H_2(p_n) bits per junction.
Equivalently, for a *segment* of genetic length d Morgans, the probability that no crossover falls
inside it in n generations is exp(-nd) under a Poisson map, giving

> **Half-life of a segment of genetic length d = (ln 2)/d generations.**

| segment | d (Morgans) | survives one generation | half-life |
|---|---|---|---|
| 0.1 cM (~100 kb) | 0.001 | 0.9990 | **693 generations** |
| 1 cM (~1 Mb) | 0.010 | 0.9900 | **69 generations** |
| 10 cM (~10 Mb) | 0.100 | 0.9048 | **7 generations** |
| 50 cM | 0.500 | 0.6065 | **1.4 generations** |
| chromosome arm (~75 cM) | 0.750 | 0.4724 | **0.9 generations** |
| human genome (~34 Morgans) | 34.0 | 1.7e-15 | **0.02 generations** |

A gene-sized block is an heirloom lasting of order a hundred generations. A chromosome arm does not
survive one. The ancestral block count after n generations is approximately C + nM for C
chromosomes and total map length M Morgans. Taking the published human maps -- **4460 cM female,
2590 cM male**, sex-averaged 35.3 Morgans, over 23 chromosomes -- this gives **58 blocks after one
generation, 376 after ten, 3,553 after a hundred**. (Physical scale: one centimorgan is about one
megabase in human on average.)

# 6. Information decays faster than correlation

The correlation between generation 0 and generation n decays as (1-2r)^n, giving a correlation
half-life of ln(1/2)/ln(1-2r). The information does not follow it, because H_2 has infinite slope
at the origin and therefore falls steeply for small crossover probabilities.

| r | correlation half-life | information half-life | ratio |
|---|---|---|---|
| 0.001 | 346.2 generations | **124.1** | 0.36 |
| 0.010 | 34.3 | **12.3** | 0.36 |
| 0.050 | 6.6 | **2.4** | 0.36 |
| 0.100 | 3.1 | **1.1** | 0.36 |
| 0.200 | 1.4 | **0.5** | 0.36 |

Here the information half-life is the (continuous) n at which the retained information first falls
to half a bit, printed to one decimal; the r = 0.2 row is below one generation, i.e. a single
meiosis at that linkage already leaves less than half a bit. **The constancy of the ratio is
definitional, not a finding**: a fixed threshold in H_2 is a fixed crossover probability
p* = 0.1100, so the information half-life is ln(1 - 2p*)/ln(1/2) = 0.359 times the correlation
half-life by construction, for any threshold one chooses. (An earlier draft printed the integer
ceiling of n, which made the ratio appear to drift from 0.36 to 0.74; the drift was the rounding,
and the constancy that replaced it is the definition.)

**Practical consequence.** Linkage disequilibrium reported as an r-squared correlation overstates
the surviving *information*: at the half-bit threshold the information half-life is about a third
of the correlation half-life, at every recombination fraction, by the definition above.

# 6a. What interference and hotspots are worth

By Theorem 1 the only thing that matters is H(d). Interference reduces it, so **interference buys
information back**, and the amount has a closed form.

Compare a chromosome of n junctions carrying on average one crossover, under two regimes: crossovers
independent at rate r = 1/n, and exactly one crossover at a uniformly random junction (maximal
interference). Then

  H_indep(d) = n H_2(1/n) = log2 n + log2 e + O(1/n),   H_one(d) = log2 n,

so the information recovered is

> **Interference gain = n H_2(1/n) - log2 n --> log2 e = 1.4427 bits**,

**per chromosome per meiosis, asymptotically independent of chromosome size.** Measured: 1.3680 at
n = 10, 1.4282 at n = 50, 1.4355 at n = 100, 1.4413 at n = 500, 1.4420 at n = 1000.

If in addition crossovers are confined to a fraction f of junctions -- recombination hotspots --
then H(d) = log2(fn) and

> **Hotspot gain = log2(1/f) bits per crossover**, also independent of n.

**The human figure is contested and we give the range rather than a point.** The classic estimate
has roughly 80 per cent of recombination in under 15 per cent of the genome (f ~ 0.15, gain 2.74
bits); larger recent samples find much weaker concentration -- of order 39 per cent of crossovers in
10 per cent of sequence -- and roughly 40 per cent of events fall outside hotspots defined from
linkage disequilibrium at all. Across that range:

| f | 0.05 | 0.10 | 0.15 | 0.30 | 0.50 |
|---|---|---|---|---|---|
| gain log2(1/f), bits per crossover | 4.32 | 3.32 | **2.74** | 1.74 | 1.00 |

So the recovered information is **of order one to four bits per crossover**, and the prediction
below is stated in a form that does not depend on which estimate is right.

We flag this as a **prediction, not a repricing**: unlike the obligate crossover, we are not aware
of an existing argument that hotspot *concentration* is itself an information optimisation. But it
is not free, and Section 6b says what it costs.

# 6b. The spanning constraint, and why hotspots must move

Section 6a leaves an obvious hole. Subject only to "at least one crossover per bivalent", the
information-optimal meiosis would place that crossover at a **fixed** position: H(d) = 0, full
retention, segregation satisfied. Real meiosis does not do this, so a second constraint must exist.

It does, and it is the same algebra. The set of haplotypes a lineage can ever reach is the orbit of
the group generated by the **support** of the crossover distribution. Hence:

> **The spanning constraint.** A crossover process can reach 2^k haplotypes, where k is the rank of
> the subgroup generated by its support. To reach the whole space it must span.

Verified by explicit orbit enumeration (n = 6, 8, 10):

| crossover support | H(d) | haplotypes reachable (n=10, space 1024) | spans? |
|---|---|---|---|
| fixed cut at one junction | 0.000 | **2** (0.20%) | no |
| two fixed cuts | 1.000 | 4 (0.39%) | no |
| confined to 30% of junctions | 1.585 | 8 (0.78%) | **no** |
| confined to 50% of junctions | 2.322 | 32 (3.12%) | **no** |
| uniform over all n junctions | 3.322 | **1024** (100%) | **yes** |

So the fixed-cut optimum is excluded: it reaches two haplotypes and no more, forever. The real
optimisation is **minimise H(d) per generation subject to spanning within an acceptable time**, and
the cheapest spanning process is one crossover at a uniformly random junction -- which is exactly
what maximal interference already delivers. Interference and spanning agree.

**This qualifies Section 6a's hotspot result, against our own interest.** A crossover process
permanently confined to a fraction f of junctions, with **zero** crossovers elsewhere, does not
span: it reaches 2^(fn) of 2^n haplotypes and leaves the remaining junctions permanently
unrecombined. The log2(1/f) bits are therefore available only if either the hotspots move or the
background rate off the hotspots is positive. Section 6a's own figure -- of order 40 per cent of
human crossovers fall outside hotspots -- says the background is positive, so real meiosis spans by
both routes, and what the constraint prices is the **time** to span, not reachability.

| f | H(d) | bits saved | hotspot sets needed to cover | ~turnover periods to span (m ln m) |
|---|---|---|---|---|
| 1.00 | 9.966 | 0.000 | 1.0 | 1 |
| 0.50 | 8.966 | 1.000 | 2.0 | 1.4 |
| 0.15 | 7.229 | **2.737** | 6.7 | **12.6** |
| 0.05 | 5.644 | 4.322 | 20.0 | 59.9 |
| 0.01 | 3.322 | 6.644 | 100.0 | 460.5 |

Smaller f is cheaper per generation and slower to span; the product is the real cost. The last
column is the coupon-collector leading term m ln m for m = 1/f hotspot sets; the exact expectation
m H_m is about 30 per cent larger at m = 6.7.

> **Consequence: at zero background, hotspot turnover is required; with a positive background it
> is what makes spanning fast.** A species with static hotspots and no background recombination
> would leave most of its haplotype space unreachable; with a background it spans, slowly, and
> turnover buys the time back.

Mammalian recombination hotspots are known to turn over rapidly, driven by PRDM9, and the standard
framing of this is the "hotspot paradox" -- biased gene conversion destroys the very motifs that
define a hotspot, so hotspots appear self-defeating. On the present account the turnover is what
buys back the log2(1/f) bits without paying in spanning time. The prediction we can defend is
therefore conditional: **turnover or background, and the ledger prices the rate** -- a species with
weak background recombination should show faster hotspot turnover than one with strong background,
at matched genome size.

**Honesty note on provenance.** The spanning constraint and the exclusion of the fixed-cut optimum
were stated before the computation. The finding that confined hotspots do not span -- the result
that qualifies our own claim -- was **measured, not predicted**: the pre-registration file for that
run failed to execute, and we do not claim foresight we cannot document.

# 7. Ploidy and the cost of the pairing structure

For general ploidy p, homologs are unlabelled only up to the automorphism group Aut of the pairing
structure: for a bivalent, the swap within the pair; for two disjoint bivalents at 4n, a group of
order 8; for a fully multivalent configuration, the whole symmetric group. Quotienting by Aut and
recomputing gives:

| ploidy | pairing | states | record lost per crossover position | \|Aut\| |
|---|---|---|---|---|
| 2n | bivalent | 64 | **1.000, exactly flat** | 2 |
| 3n | bivalent + univalent | 122 | 0.656, 0.639, 0.590, 0.443 | 2 |
| 3n | trivalent | 41 | 1.556, 1.510, 1.365 | 6 |
| 4n | two bivalents | 172 | 1.227, 1.113, 0.789 | 8 |
| 4n | quadrivalent | 60 | **2.385, 2.151, 1.371** | 24 |

Two effects, both in the same direction. **Multivalent pairing melts the record roughly twice as
fast per crossover at fixed ploidy** (4n: 2.385 against 1.227; 3n: 1.556 against 0.656), **and it
starts with less**, because a larger pairing automorphism group leaves fewer distinguishable states
(60 against 172 at 4n). This supplies an information price for diploidization. It does not explain
it; meiotic stability does.

The diploid bivalent is the unique flat-rate configuration in the table, losing exactly one bit per
crossover position and never more. This is Theorem 1 showing through: crossovers commute, so the
move set is abelian and the record is a codimension count.

**A note on ploidy and fitness.** The triploid bivalent-plus-univalent configuration is the *best
retainer in the table*, losing 0.44 to 0.66 bits per crossover, and triploids are sterile. Retention
is therefore not fitness. In this framework retention and construction are separate capacities, and
sterility is a failure of the second, not the first.

# 8. A negative result: outcrossing carries no information advantage

We relaxed the tester design of Section 2 and compared, at **matched genetic material** — four
parental homologs either way — selfing (two isolated lineages) against outcrossing (one junction).

| \|J\| | self | outcross | ratio |
|---|---|---|---|
| 0 | 2.5850 | 2.0000 | **0.77** |
| 1 | 4.1219 | 4.0000 | 0.97 |
| 2 | 5.6144 | 6.0000 | 1.07 |
| 3 | 7.0875 | 7.0000 | 0.99 |
| 5 | 9.0378 | 9.0378 | 1.00 |

We had predicted outcrossing to exceed selfing by more than a factor of two, on the reasoning that a
junction between two records carries more than the records do separately. **It does not, and at zero
recombination selfing is ahead.** The reason is instructive and we state it as the correction:
a junction pays only when it **blocks moves**. Fertilisation blocks nothing — both homologs of a
zygote recombine exactly as freely whether they came from one parent or two. Any advantage of
outcrossing in real populations must therefore come from something outside this model (masking of
deleterious recessives, or selection on the created variance), not from the information geometry of
the junction itself. This reproduces, in our currency, the known fact that without selection
recombination is pure noise: every argument for an advantage of recombination is selection-driven
(Fisher 1930; Muller 1932; Hill and Robertson 1966; Felsenstein 1974).

# 8a. The living boundary: exactly one generator

A record system is at its *living boundary* when it is as close to frozen as possible while still
moving -- maximal R subject to H_thermo > 0. Because crossovers commute, the meiotic instance has a
sharp answer.

| n | 6 | 8 | 10 | 12 | 16 |
|---|---|---|---|---|---|
| **H_thermo at the boundary** | **1.0000** | **1.0000** | **1.0000** | **1.0000** | **1.0000** |
| R/H at the boundary | 0.833 | 0.875 | 0.900 | 0.917 | 0.938 |

**H_thermo is exactly one bit at every system size** -- one accessible crossover position, no more --
while the *ratio* R/H drifts toward 1 as the genome grows. The exactness is a theorem of the
construction, not a measurement: the smallest nonzero move set of commuting involutions is one
generator, and one generator is one bit; the table is a check that the code implements that. The invariant is therefore the **absolute
floor, not the ratio**: as n increases R/H rises automatically, so no fixed ratio can characterise
the boundary while the floor does.

This is exact here because the moves commute. Where a system's generators are coupled rather than
independent, the smallest available step is a block rather than a single generator, and the floor
sits correspondingly higher -- a system with coupled machinery must carry more freedom than it would
choose. Meiosis, whose crossovers are independent by construction, achieves the minimum.

# 9. What this does and does not do

**Priced, not explained.** The obligate crossover and crossover interference are explained by
segregation mechanics. This paper supplies their currency: each crossover beyond the obligate one
costs exactly H_2(r) bits of forwarded record, which is why an organism that must have one has a
quantitative reason to have no more. Taking the published maps, **human male meiosis runs 2590 cM = 25.9
crossovers across 23 chromosomes, or 1.13 per chromosome -- within thirteen per cent of the
segregation floor of one** (the observation that crossover number tracks the number of chromosome
arms is Pardo-Manuel de Villena and Sapienza 2001, and the per-arm floor is the sharper one). Female meiosis runs 4460 cM = 44.6 crossovers, 1.94 per chromosome, and
the model prices the difference at H_2(r) per additional junction crossed. **That the sex with the
higher crossover number is the one with the longer-arrested prophase is a coincidence this model
does not explain and we do not claim it does.** Diploidization is likewise
priced, not explained.

**Structural, and we believe new.** The identification of Theorem 1 (the identity is textbook; the
identification of meiosis with it is what we claim). The pairing-automorphism accounting of
Section 7. Section 5 is Fisher's; the information/correlation half-life ratio of Section 6 is a
definition, not a result.

**Limits.** The model is a single lineage with a fixed map, no selection, no drift, no gene
conversion and no mutation. Interference is *not* a limit: by Theorem 1 it enters only through
H(d), and Section 6a computes its value. Selection, drift and mutation are genuine omissions.
The remaining structural gap is the one Section 6b opens and does not close: the optimisation
"minimise H(d) per generation subject to spanning within an acceptable time" is stated, not
solved, and the turnover-or-background it requires is priced by the last table of Section 6b but
the rate is not derived.

# 10. Methods

All results are exact enumerations, not simulations. Theorem 1's corollaries were verified against
brute-force computation of the joint parent-offspring distribution over all 2^(L-1) phases and all
2^(L-1) switch patterns. Ploidy results enumerate the full quotient state space and compute
connected components of the crossover move graph directly. Predictions for every experiment were
written and hashed before the corresponding run; the prediction files and their SHA-256 digests are
retained. One modelling error was found and corrected during this work by a positive control: an
earlier version canonicalised states by sorting homologs, which silently made "the pair (0,1)" mean
"the two lexicographically smallest" rather than a fixed pairing, and moved zero of 41 states under
the first crossover. All p >= 3 numbers in Section 7 are from the corrected model.

# References

*Internal draft. Every entry below is from the authors' memory and must be pinned to the primary
source before any external copy; the standing rule is that a citation not checked against the
primary is not a citation.*

- Baudat F, et al. (2010). PRDM9 is a major determinant of meiotic recombination hotspots in humans and mice. Science 327, 836-840.
- Boulton A, Myers RS, Redfield RJ (1997). The hotspot conversion paradox and the evolution of meiotic recombination. PNAS 94, 8058-8063.
- Chapman NH, Thompson EA (2003). A model for the length of tracts of identity by descent in finite random mating populations. Theor. Popul. Biol. 64, 141-150.
- Cover TM, Thomas JA (2006). Elements of Information Theory, 2nd ed. Wiley. (Modulo-additive noise channel.)
- Felsenstein J (1974). The evolutionary advantage of recombination. Genetics 78, 737-756.
- Fisher RA (1930). The Genetical Theory of Natural Selection. Clarendon.
- Fisher RA (1949). The Theory of Inbreeding. Oliver and Boyd.
- Fisher RA (1954). A fuller theory of "junctions" in inbreeding. Heredity 8, 187-197.
- Gravel S (2012). Population genetics models of local ancestry. Genetics 191, 607-619.
- Haldane JBS (1919). The combination of linkage values, and the calculation of distances between the loci of linked factors. J. Genet. 8, 299-309.
- Halldorsson BV, et al. (2019). Characterizing mutagenic effects of recombination through a sequence-level genetic map. Science 363, eaau1043.
- Hill WG, Robertson A (1966). The effect of linkage on limits to artificial selection. Genet. Res. 8, 269-294.
- Kong A, et al. (2002). A high-resolution recombination map of the human genome. Nat. Genet. 31, 241-247.
- Muller HJ (1932). Some genetic aspects of sex. Am. Nat. 66, 118-138.
- Myers S, et al. (2005). A fine-scale map of recombination rates and hotspots across the human genome. Science 310, 321-324.
- Pardo-Manuel de Villena F, Sapienza C (2001). Recombination is proportional to the number of chromosome arms in mammals. Mamm. Genome 12, 318-322.
- Shannon CE (1948). A mathematical theory of communication. Bell Syst. Tech. J. 27, 379-423, 623-656.
- Stam P (1980). The distribution of the fraction of the genome identical by descent in finite random mating populations. Genet. Res. 35, 131-155.
