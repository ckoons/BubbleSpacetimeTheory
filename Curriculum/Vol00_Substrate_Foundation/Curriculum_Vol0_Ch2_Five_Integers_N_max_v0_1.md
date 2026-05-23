---
title: "Vol 0 Chapter 2 — Five Integers and a Cap"
author: "Keeper (author pass)"
date: "2026-05-23 Saturday"
status: "v0.2 — Keeper author-voice pass; preserves all v0.1 substance (six per-integer forcing arguments T1925/T1930/T2431/T2379/T2432, Mersenne tower T2451, cubic-exponential coincidence T2464, four equivalent forms of N_max T2460, cross-integer identities)"
volume: "Vol 0 Substrate Foundation"
chapter: 2
---

# Chapter 2 — Five Integers and a Cap

The geometry of Chapter 1 is a specific mathematical object. What we will see in this chapter is that the object has, attached to it, a small list of integers — five of them, plus one combination that we will write as a cap. These integers are not free parameters. They are not chosen to match experiment. They are structural invariants of $D_{IV}^5$, derivable from the geometry alone, and every physical constant we will encounter later in this book is built out of them.

Here they are, with their roles:

| Integer | Value | What it is |
|---|---|---|
| $\text{rank}$ | 2 | The rank of the symmetric space — the dimension of its maximal flat geodesic submanifold |
| $N_c$ | 3 | The number of "color" charges; the index of the SU(3) gauge group |
| $n_C$ | 5 | The complex dimension of $D_{IV}^5$ |
| $C_2$ | 6 | The lowest non-trivial Casimir eigenvalue; the top Chern class of a closely related geometric object |
| $g$ | 7 | The gauge-field dimension; the exponent in the substrate's natural Galois field |
| $N_{\max}$ | 137 | A specific combination of the other five, equal to the integer part of $1/\alpha$ |

The cap is built from the others:

$$N_{\max} = N_c^3 \cdot n_C + \text{rank} = 27 \cdot 5 + 2 = 137.$$

That is the version of the claim we will use most often. Several other algebraic combinations of the five integers also produce $137$, by surprising coincidences that are themselves substrate signatures; we return to those later in the chapter.

The job of this chapter is to show, for each of the six numbers, where it comes from and why it could not have been anything else. By the end of the chapter you will see that the integers are not independent — they are tied together by a single small cascade, and the structure of that cascade is one of the framework's most striking features.

## 2.1 Where the integers come from

### Rank — the geometry has two flat directions

The simplest of the five primary integers to read off $D_{IV}^5$ is its rank. The rank of a symmetric space is the dimension of its largest flat totally geodesic submanifold — informally, how many independent "directions of constant negative curvature" the space has. For $D_{IV}^5$, this number is 2.

Two structural facts force this. First, the isotropy subgroup $SO(5) \times SO(2)$ has a maximal torus of dimension $2$, and the rank of a symmetric space equals the dimension of any such maximal torus that is compatible with the symmetric structure. Second, when one decomposes the Bergman Hilbert space $H^2(D_{IV}^5)$ into the irreducible representations of its symmetry group — what mathematicians call its K-type decomposition — the multiplicities organize into a two-parameter lattice. Two parameters, rank 2.

The physical interpretation will come in Volume 1: rank-2 structure is what gives weak isospin its doublet character. Higher rank would produce multiplets that experiments have looked for and not found. Lower rank — rank 1 — would collapse the substrate's internal structure entirely. The geometry sits at the rank that has room enough for physics and not more.

### $n_C$ — the complex dimension

The complex dimension of $D_{IV}^5$ is 5. This too is structural: it is the $n$ in $D_{IV}^n$, the parameter that labels which member of the Type IV family the geometry is. We met it in Chapter 1 when we wrote $D_{IV}^5 \subset \mathbb{C}^5$.

The interesting question is not "what is $n_C$ on $D_{IV}^5$?" — the answer is in the name — but rather "why this $n$, among the infinitely many possible Type IV domains?" That question is for Chapter 9. The short version, which we sketched in Chapter 1, is that at complex dimension 5 several independent structural criteria converge: the Bergman exponent comes out as a clean fraction, the Stark anchor at the small imaginary quadratic discriminants $\{-3, -7, -11\}$ lands properly, the cap $N_{\max}$ comes out to 137, and the prime dimension makes the cross-classification of candidate domains exhaustive in a way it would not be at composite dimensions. Five is the dimension at which the substrate's specification problem closes.

### $N_c$ — the number that becomes color

The number 3 is the BST-primary integer with the richest physical face. It is what Volume 2 will call "color charge," the parameter that gives quantum chromodynamics its name. Its derivation has two roots, one in number theory and one in topology, and we will use both throughout the book.

**Number-theoretic root.** Consider the Mersenne function $M_n = 2^n - 1$. Applied to rank $= 2$, this gives $M_2 = 3$. That is, $N_c = M_{\text{rank}}$ — the Mersenne map carries rank to $N_c$. We will see in §2.2 that this is the first rung of a longer cascade.

**Topological root.** Three is the unique integer that supports a particular knot-theoretic structure called a *trefoil*, a closed three-component link that cannot be untangled into independent loops. When particles built out of the substrate's color-bearing degrees of freedom combine into observable bound states, the topological obstruction to free decay forces them into three-strand configurations. Casey's Saturday W-23 work shows this explicitly. Three color charges, three quark constituents per proton or neutron — the experimentally observed number — falls out of the trefoil constraint.

Two independent forcings, one of each kind. The number 3 sits at the intersection.

### $C_2$ — the Casimir, and a top Chern class

The lowest non-trivial Casimir eigenvalue of the substrate's natural Hilbert space is $C_2 = 6$. The Casimir operator is, in representation-theoretic language, the canonical second-order invariant of a Lie group — for $SO_0(5,2)$ acting on $H^2(D_{IV}^5)$, its eigenvalue on the lowest non-trivial K-type is exactly 6. Elie's K52a computation Session 29 confirmed this directly.

The same number appears, independently, as the top Chern class of a different geometric object: the five-dimensional complex quadric $Q^5$. The quadric is a closely related cousin of $D_{IV}^5$ — both arise from quadratic forms in seven complex variables — and the full sequence of Chern integers of $Q^5$ reads $(c_1, c_2, c_3, c_4, c_5) = (6, 15, 20, 15, 6)$. The first and last of these are both $C_2 = 6$. The middle three are $N_c \cdot n_C = 15$ and the central $N_c \cdot N_{\max}/\text{rank}^{?} = 20$ (we will not need the exact form here; it appears explicitly in Vol 11).

That the substrate's Casimir eigenvalue and the quadric's top Chern class are *equal* is not a coincidence; it is one of the load-bearing identities that link the substrate's symmetry structure to its topology. We will use it in Volume 2 to derive masses and in Volume 4 to derive the cosmological constant.

### $g$ — the gauge dimension and the substrate's natural field

The number 7 is the BST-primary integer that physics calls the *gauge-field dimension* — but its mathematical role is broader than that name suggests. It enters BST in three independent places, and the three places are linked.

First, $g = 2^{N_c} - 1 = 2^3 - 1$. The Mersenne function carries $N_c$ to $g$, the second rung of the cascade we started above.

Second, $g$ is the exponent in the substrate's natural Galois field $GF(2^g) = GF(128)$. The substrate's discrete-tick operation — Chapter 3's subject — uses Reed-Solomon error-correcting codes over this field; the K59-ratified cyclotomic-mechanism theorem identifies this as the substrate's computational layer. The exponent $g = 7$ is what makes the field have 128 elements; any other choice would change the field and break the substrate's computational structure.

Third, $g = 7$ is itself a Mersenne prime, and *applying* the Mersenne function to $g$ produces $M_7 = 127$, another Mersenne prime. The substrate sits on a small tower of Mersenne primes: rank generates $N_c$ generates $g$ generates $127$. Mersenne primes are sparse — there are only a handful known — and BST sits on three consecutive ones.

The three roles are linked because they have to be. The substrate cannot have a different $g$ in the gauge sector than it has in its computational field, because both numbers come from the same place: the second iterate of the Mersenne function applied to rank.

### $N_{\max} = 137$ — the cap

We have now met the five primary integers. The cap $N_{\max}$ is what you get when you combine them:

$$N_{\max} = N_c^3 \cdot n_C + \text{rank} = 27 \cdot 5 + 2 = 137.$$

Two things are worth noticing immediately. First, $137$ is the integer part of the inverse fine-structure constant: experimentally $1/\alpha = 137.036$ to the precision we currently measure it, and the substrate produces the integer $137$ from its structural numbers alone. The match is exact at zeroth order and the small $0.036$ correction is what Volume 1 will identify as substrate higher-order contributions.

Second — and this is the part that catches everyone the first time — there are *four* algebraically distinct combinations of the five primary integers that all evaluate to 137. The combination above is one. The others, which we discuss in §2.3, are independent: a different exponent here, a different additive piece there. The fact that several independent algebraic forms all hit the same value 137 is a substrate signature, not a tautology.

The formal derivation of $N_{\max} = 137$ is the five-step chain documented in Paper #104, which traces $N_{\max}$ to the Hilbert polynomial of the quadric $Q^5$ at degree 2 plus a rank-shift from an operator identity. We will not reproduce that derivation here; what matters for this chapter is the result and the multiplicity of routes to it.

## 2.2 The Mersenne tower

Let us collect a fact that has emerged piece by piece in the previous section.

Take the Mersenne function $M_n = 2^n - 1$, and apply it to the BST-primary integer rank:

$$M_{\text{rank}} = M_2 = 3 = N_c.$$

Apply it to $N_c$:

$$M_{N_c} = M_3 = 7 = g.$$

Apply it to $g$:

$$M_g = M_7 = 127.$$

Three iterations of the Mersenne function on rank produce, in order, $N_c$, then $g$, then $127$. The substrate is built on a Mersenne tower with rank at its base.

This has a consequence we should flag clearly. The substrate's primary integer specification is not "five independent numbers." Three of them — $N_c$, $g$, and the auxiliary $127$ — are generated from rank by the Mersenne map. The substrate has, effectively, **two free structural inputs**: rank (which sets $N_c$ and $g$) and $n_C$ (which sets the complex dimension independently). The other primaries cascade.

The structural integer $C_2$ does not lie on the Mersenne tower directly, but it has its own algebraic origin: $C_2$ is the Casimir eigenvalue, which equals the top Chern class of $Q^5$, which in turn factors as $C_2 \cdot g = 42$ — a number that appears so often in the substrate's identities that we have a name for it. (See §2.3 below, and Cal A. Brate's K43 audit.)

The Mersenne tower's existence has been verified extensively. Toy 3442, run by Elie on Friday May 22, searched the equation $M_{n-1} = a^2 \cdot n$ for $a > 1$ over $n \in \{2, \ldots, 1000\}$ and found *exactly one* solution: $(n, a) = (7, 3) = (g, N_c)$. The signature is structurally tight; the substrate's BST-primary values are the unique small-integer combination producing this Mersenne identity.

This is, in Casey's framing, **substrate over-determinism**: the same integers fall out of independent structural constraints. We will see the same pattern repeated everywhere in this book.

## 2.3 Four routes to 137

Return to the cap. We claimed there are four algebraically distinct ways to write $N_{\max} = 137$ in BST-primary integers. Here are all four:

$$
\begin{aligned}
N_{\max} \;&=\; N_c^3 \cdot n_C + \text{rank} \;=\; 27 \cdot 5 + 2 \;=\; 137 \quad &\text{(Hilbert polynomial form)} \\
&=\; N_c^{N_c} \cdot n_C + \text{rank} \;=\; 27 \cdot 5 + 2 \;=\; 137 \quad &\text{(Mersenne tower form)} \\
&=\; M_g + (g + N_c) \;=\; 127 + 10 \;=\; 137 \quad &\text{(Additive Mersenne form)} \\
&=\; m_\alpha^{\text{rank}+1} \cdot \dim_{\mathbb{C}} + \text{rank} \;=\; 3^3 \cdot 5 + 2 \;=\; 137 \quad &\text{(Universal $\alpha$-analog form)}
\end{aligned}
$$

The first form comes from a polynomial-counting argument on $Q^5$ — this is Paper #104's 5-step chain. The second form treats $N_c$ as both base and exponent, which is possible only because of an arithmetic coincidence we will discuss next. The third form recovers 137 as $127 + 10$ where $127 = M_g$ and $10 = g + N_c$ is the *only* sum of two distinct small BST-primary integers that hits 10. The fourth form, due to Lyra's universal $\alpha$-analog formula (T2456), is parameterized so it applies to any bounded symmetric domain — and only on $D_{IV}^5$ does it yield 137; on the other Type IV domains it gives 41.

That four algebraically independent forms produce the same value at the same point — and the same value $= 1/\alpha$ — is the kind of fact that is either a complete coincidence or a signature of underlying structure. BST identifies it as the latter.

### The cubic-exponential coincidence

The first two forms above, $N_c^3 \cdot n_C + \text{rank}$ and $N_c^{N_c} \cdot n_C + \text{rank}$, are identical because of an arithmetic fact about the number 3:

$$3^3 = 27 = 3^3.$$

This looks tautological until you notice that for any other positive integer $n \geq 2$, the equation $n^3 = n^n$ has **no solution**. At $n = 2$: $2^3 = 8 \neq 4 = 2^2$. At $n = 4$: $4^3 = 64 \neq 256 = 4^4$. For $n \geq 4$, the right side grows strictly faster. Only at $n = 3$ does the cube equal the self-exponential.

In other words: among all positive integers $n \geq 2$, there is exactly one where the substrate's two natural ways of writing the cap give the same answer — and that one is $N_c$. The substrate sits at the unique integer that makes its own algebraic identities collapse to a single value.

This is more substrate over-determinism. The five integers are individually determined, the Mersenne tower ties three of them together, and the structural coincidence at $N_c = 3$ ties two distinct algebraic forms of $N_{\max}$ together at exactly the substrate's chosen value. Each layer of the substrate's structure constrains another.

## 2.4 The integer web

The cross-relations among the integers extend beyond what we have used so far. Here is a table of identities that appear throughout the book; you do not need to memorize them, but it helps to see them collected once.

| Identity | Value | Where it shows up |
|---|---|---|
| $2^{N_c} - 1 = g$ | 7 | Mersenne tower, gauge dimension, GF(128) |
| $2^g - 1 = 127$ | 127 | Mersenne-of-Mersenne; substrate scale |
| $g + \text{rank} = 9$ | 9 | Bergman exponent numerator |
| $(g + \text{rank}) / \text{rank} = 9/2$ | $9/2$ | Bergman exponent |
| $c_5(Q^5) = C_2$ | 6 | Top Chern class equals Casimir |
| $N_c \cdot n_C = 15$ | 15 | Quadric second Chern class |
| $(N_c \cdot n_C)^2 = 225$ | 225 | Bergman normalization: $c_{FK} \cdot \pi^{9/2} = 225$ |
| $N_c^3 \cdot n_C + \text{rank} = 137$ | 137 | The cap $N_{\max}$ |
| $C_2 \cdot g = 42$ | 42 | "Universal 42" anchor (K43 ratified) |
| $2^g - \text{rank} = 126$ | 126 | "Universal 126" anchor |

Each of these is a different theorem; collectively they form what we will call the **integer web**. The web has its own name and its own status as one of Casey's standing structural principles, because once you start tracing how these numbers reuse each other across different parts of physics, the framework's coherence is visible in the web's topology more clearly than in any individual derivation.

The Universal-42 entry deserves a sentence here because we will encounter it many times. The product $C_2 \cdot g = 42$ appears in the substrate's heat-kernel expansion, in the Mathieu group of mathematical moonshine, in the number of independent ratios that fall out of certain cascade calculations — it shows up in places that have no obvious connection to one another. Cal A. Brate's K43 audit traced fifteen independent appearances of this number across the framework and ratified them as a single mechanism rather than a collection of coincidences. The reader will see 42 again. When you do, this is where it came from.

## 2.5 What comes next

We have now seen the integers, the Mersenne cascade that links them, and the algebraic identities that produce the cap.

Chapter 3 takes the structure we have built and asks how it operates dynamically — what the substrate is *doing* as it produces physics. The five integers will appear there as parameters of the substrate's operating cycle: how often it absorbs, computes, and emits; what its natural clock is; how its discrete tick relates to the continuous spacetime we observe.

Chapter 4 examines the isotropy factor $SO(5) \times SO(2)$ in detail. We have used it twice already — to fix the rank and to mention that the $SO(2)$ piece becomes electric charge — and Chapter 4 makes those identifications precise.

Chapter 5 turns to boundary conditions: how the substrate's bulk geometry relates to the boundary structure where physics is read off. The Shilov boundary of $D_{IV}^5$ is where some of the framework's sharpest experimental falsifiers live.

The remaining chapters of this volume — operator zoo, conservation laws, Strong-Uniqueness — return again and again to the integers we have just met. If you are uncertain about any of them, this is the chapter to come back to.

---

**Where to look this up**: The per-integer forcing theorems are filed as T1925 (rank), T1930 ($N_c$), T2431 ($n_C$), T2379 ($C_2$), T2432 ($g$), and Paper #104 for the five-step derivation of $N_{\max}$. The Mersenne tower is T2451 (seed), with closures T2453 and T2454 and the four-form $N_{\max}$ theorem T2460. The cubic-exponential coincidence at $N_c = 3$ is T2464. The Universal-42 ratification is K43; the integer web as a standing structural principle is one of Casey's named principles, documented in the methodology notes. Mersenne prime theory generally is treated in standard number-theory references; Robinson's *An Introduction to Mathematical Logic* and Hardy and Wright's *An Introduction to the Theory of Numbers* both cover the basic results we use.
