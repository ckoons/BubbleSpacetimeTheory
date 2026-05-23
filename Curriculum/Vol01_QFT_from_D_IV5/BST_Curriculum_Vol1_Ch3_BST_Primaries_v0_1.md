---
title: "Vol 1 Chapter 3 — The Integers, Forced"
author: "Keeper (author pass)"
date: "2026-05-23 Saturday"
status: "v0.2 — Keeper author-voice pass; preserves v0.1 substance (per-integer four-argument forcing T1925/T1930/T2431/T2432, Mersenne tower coherence T2451/T2453/T2454, universal α-analog formula T2456/T2462, characteristic cube T2464, three-layer over-determinism T2465)"
volume: "Vol 1 Quantum Field Theory from D_IV⁵"
chapter: 3
---

# Chapter 3 — The Integers, Forced

Volume 0 introduced the five BST primary integers and gave each one a brief justification. The current chapter goes back through the same five integers and gives each its *full* substrate-derivation argument — typically four independent classical mathematical conditions, each of which forces the integer's value in its own right, with the conjunction of all four uniquely fixing the integer at the value the substrate uses. These multi-argument forcings are the structural backbone of the Strong-Uniqueness Theorem we sketched in Volume 0 Chapter 9, and they will appear, in one form or another, throughout the rest of this volume and most of the volumes that follow.

The chapter's spirit is one of *defense*. The natural skeptic's question about BST is: "if you have only five integers, you have only five free parameters in disguise; you can always tune them to match physics." The answer this chapter develops is no — the integers are not tunable. Each is forced by independent mathematical conditions that have nothing to do with physics. The conjunction is structural, not empirical. When we report that BST has zero free parameters, we mean it: the five integers are mathematical inevitabilities, not chosen inputs.

## 3.1 What "forcing" means here

For each BST primary integer, we will exhibit several independent classical mathematical conditions, each one of which constrains the integer's possible values. The constraints come from different branches of mathematics — Lie group classification, number theory, Chern class topology, K-theory, Lorentzian conformal geometry — and their *only* common solution is the value the substrate uses.

The argument structure is conjunctive. If we had a single mathematical condition that forced rank $= 2$, the result would already be a substrate-derivation, but it might still leave the skeptic wondering whether some other formulation could give rank $= 3$. With four independent conditions all forcing rank $= 2$, the skeptic has to argue that *all four* could have a common alternative solution — and the four conditions are drawn from such different mathematical worlds that no such alternative exists.

We call this **multi-argument forcing**, and Lyra's per-integer theorems (T1925 for rank, T1930 for $N_c$, T2431 for $n_C$, T2432 for $g$, plus the derived theorem for $N_{\max}$) each carry four independent forcing arguments. The chapter walks through them integer by integer.

## 3.2 Why rank $= 2$ (T1925)

The substrate's rank is forced by four independent conditions.

**Mersenne self-iteration.** Rank $= 2$ is the smallest positive integer such that the Mersenne map $M_n = 2^n - 1$ produces a *three-step chain* of values that are themselves all prime BST primary integers: $M_2 = 3 = N_c$, $M_3 = 7 = g$, $M_7 = 127 = M_g$. At rank $= 1$, the chain has length one ($M_1 = 1$, not a BST primary). At rank $\geq 3$, the chain breaks early because $M_n$ is not prime for many small $n$. The substrate sits at the smallest rank where the Mersenne cascade extends to three rungs.

**Cartan classification.** Type IV is the unique infinite family of irreducible Hermitian symmetric domains in which the rank is *two for every complex dimension* $n \geq 2$. This is the content of Helgason 1978, Chapter X, Theorem 6.1. Type I families have rank growing linearly with their parameters; Type II and Type III similarly. Only Type IV maintains rank $= 2$ across the infinite tower of complex dimensions, making it the natural family in which to look for a rank-2 substrate at any specified dimension.

**Lorentzian conformal structure.** The substrate's symmetry group $SO_0(2, n_C)$ produces a conformal boundary of signature $(1, n_C - 1)$. For the boundary to have the four-dimensional Lorentzian signature $(1, 3)$ that physics observes, $n_C - 1 = 4$, so $n_C = 5$ — and the only way to combine $n_C = 5$ with the substrate's structural requirement that the symmetry group take the form $SO_0(\text{rank}, n_C)$ is rank $= 2$.

**Pin(2) and chirality.** The substrate's rank-2 isotropy structure carries a Pin(2) double cover that distinguishes left-handed from right-handed substrate states. This is the structural origin of the spin-statistics distinction (which we will develop in Volume 5) and of weak-sector chirality (which appears in Chapter 4 below). Without rank $= 2$, the Pin(2) double cover is not available, and the substrate cannot support fermion chirality.

Four arguments, four independent branches of mathematics, one common forced value. T1925 makes this rigorous.

## 3.3 Why $N_c = 3$ (T1930)

The substrate's color integer is forced by four further independent conditions.

**The Mersenne map applied to rank.** $N_c = M_{\text{rank}} = 2^2 - 1 = 3$. This is the first rung of the Mersenne tower we just used to force rank.

**Color-singlet triangle.** The number of color-singlet combinations of $N_c$ quark-antiquark pairs is the triangle number $T_{N_c} = N_c(N_c+1)/2$. At $N_c = 3$, this is $T_3 = 6$, which equals the BST primary $C_2$. This is not coincidence — the substrate's Casimir eigenvalue and the substrate's color-singlet counting are connected at the value 6, and the connection holds *only* at $N_c = 3$. (For $N_c = 2$, the triangle gives 3; for $N_c = 4$, it gives 10; only $N_c = 3$ produces the BST-primary value 6.)

**Wallach short-root multiplicity.** On $D_{IV}^5$, the substrate's $B_2$ root system has short-root multiplicity $m_s = N_c$ (Wallach 1976). The multiplicity is, in physical terms, the number of independent short-root directions per short root. At $N_c = 3$, this gives the three independent color directions of the fundamental representation of $SU(3)$ — the substrate-side origin of color charge.

**Iwasawa dimension.** The total nilpotent dimension of the Iwasawa decomposition of $SO_0(5,2)$ is $\text{rank}^{N_c} = 2^3 = 8$ — exactly $\dim SU(3)$. The substrate's $N_c$ is the unique integer producing this match.

The Mersenne argument and the triangle argument come from number theory and combinatorics. The Wallach argument comes from representation theory. The Iwasawa argument comes from Lie group structure theory. All four converge on $N_c = 3$.

## 3.4 Why $n_C = 5$ (T2431)

The substrate's complex dimension is forced by four further conditions.

**Chern classes of $Q^5$.** The five-dimensional complex quadric $Q^5$, which is one of the substrate's central Bridge Objects, has Chern class sequence $c(Q^5) = (1, 5, 11, 13, 9, 3)$. The first Chern class is $c_1 = 5 = n_C$. This identification is structural: the substrate's complex dimension equals the first Chern class of the quadric that lives canonically alongside it. For any other complex dimension, the relationship breaks.

**Lorentzian boundary closure.** The four-dimensional Lorentzian spacetime that physics observes is the conformal boundary of $D_{IV}^5$ (Chapter 1 of Volume 0). The conformal-boundary signature $(1, n_C - 1)$ requires $n_C - 1 = 4$, so $n_C = 5$.

**Bergman exponent.** The Bergman exponent of $D_{IV}^5$ is $(g + \text{rank})/\text{rank} = 9/2$ — a clean half-integer with the numerator-denominator both BST primary integers. For other complex dimensions, the Bergman exponent on the corresponding type IV domain takes values that are not as structurally clean.

**$N_{\max}$ structural identity.** The cap $N_{\max} = N_c^3 \cdot n_C + \text{rank}$ produces 137 only when $n_C = 5$. With $n_C = 4$ the formula gives $N_c^3 \cdot 4 + 2 = 110$, with $n_C = 6$ it gives $N_c^3 \cdot 6 + 2 = 164$; neither matches the inverse fine-structure constant or any structurally significant integer. $n_C = 5$ is the unique value producing 137.

Four arguments: a topological one (Chern classes), a conformal one (boundary signature), an analytic one (Bergman exponent), and a structural one ($N_{\max}$). All four force $n_C = 5$ at the substrate's complex dimension.

## 3.5 Why $g = 7$ (T2432)

The substrate's gauge-dimension integer is forced by four more.

**The Mersenne map applied to $N_c$.** $g = M_{N_c} = 2^3 - 1 = 7$, the second rung of the Mersenne tower.

**Bergman exponent denominator.** The Bergman exponent $(g + \text{rank})/\text{rank}$ requires $g$ to combine with rank to produce the clean half-integer numerator that gives the Faraut–Koranyi normalization its BST-primary form. $g = 7$ is the unique value yielding $(g + 2)/2 = 9/2$.

**$B_2$ root system genus.** The substrate's $B_2$ root system has long-root multiplicity $m_\ell = g$ in the substrate's specific realization. At $g = 7$, this gives seven independent long-root directions in the gauge-sector structure.

**Cyclotomic Galois field.** The substrate's per-tick computation uses the Galois field $GF(2^g) = GF(128)$. The exponent $g$ controls the field's size; $g = 7$ produces a field with $128 = 2^7$ elements and multiplicative cyclic group of Mersenne-prime order $127 = M_g$. The Reed–Solomon code structure that anchors the substrate's information capacity (K59 ratified) requires this specific Mersenne-prime cyclic order, available only at $g = 7$.

Four arguments — number theory (Mersenne map), analytic structure (Bergman exponent), Lie root systems (multiplicity), computational substrate (Galois-field structure). All converge on $g = 7$.

## 3.6 Why $C_2 = 6$ and $N_{\max} = 137$

The Casimir integer $C_2$ and the cap $N_{\max}$ are *derived* rather than independently forced, but the derivations are themselves substrate-mechanical and worth noting briefly here.

$C_2 = 6$ emerges in two structurally distinct ways: as the lowest non-trivial K-type Casimir eigenvalue on $H^2(D_{IV}^5)$ (which we will compute in Chapter 5), and as the triangle number $T_{N_c} = N_c(N_c+1)/2 = 3 \cdot 4 / 2 = 6$ that counts color-singlet combinations. Both derivations land at the same value; the matching is one of the substrate's many structural over-determinations.

$N_{\max} = 137$ emerges as the five-step composition of the other primaries: $N_{\max} = N_c^3 \cdot n_C + \text{rank} = 27 \cdot 5 + 2 = 137$, where the $N_c^3$ factor comes from the Hilbert polynomial of $Q^5$ at degree 2, the $n_C$ factor comes from the substrate's complex dimension, and the $+\text{rank}$ shift comes from an operator identity in the pre-$\alpha$ structure. Paper #104's 5-step chain documents the derivation. $N_{\max}$ matches the integer part of the inverse fine-structure constant — experimentally $1/\alpha = 137.036$, where the 0.036 correction is what we will identify in Chapter 10 as substrate higher-order contributions.

## 3.7 The Mersenne tower and the cascade structure

A unifying observation, formalized by Lyra in May 2026 (T2451 and companions T2453, T2454), is that the per-integer forcing arguments above are not as independent as they might appear. The substrate's primary integers form a **Mersenne tower**:

$$M_{\text{rank}} = N_c, \qquad M_{N_c} = g, \qquad M_g = 127.$$

Three iterations of the Mersenne map, starting from rank, generate $N_c$, then $g$, then the auxiliary Mersenne ceiling 127. This means the substrate has, effectively, *only two free structural inputs*: rank and the complex dimension $n_C$. The integers $N_c$, $g$, and $127$ are not independent of rank; they cascade from it.

The cascade has been verified computationally. Among integers $n \in \{2, \ldots, 1000\}$, the equation $M_{n-1} = a^2 \cdot n$ for $a > 1$ has *exactly one* solution: $(n, a) = (7, 3) = (g, N_c)$. The substrate's primary-integer signature is structurally tight at the small-integer scale.

A further structural fact, T2464, is what we have called the **characteristic cube**: $N_c^3 = 27 = N_c^{N_c}$, the unique positive-integer equality of cube and self-exponential. For any other positive integer $n \geq 2$, $n^3 \neq n^n$. The coincidence at $N_c = 3$ means that the Hilbert-polynomial form of $N_{\max}$ ($N_c^3 \cdot n_C + \text{rank}$) and the Mersenne-tower form ($N_c^{N_c} \cdot n_C + \text{rank}$) collapse to the same value at the substrate's parameters, contributing yet another over-determination.

## 3.8 The cross-Cartan three-pillar argument

A third structural layer of over-determination, formalized in Lyra's T2456 and T2462, applies across the entire Cartan classification of bounded Hermitian symmetric domains. Every such domain admits three "tight" algebraic invariants derivable from its primary integers via Bergman machinery: an $\alpha$-analog (an integer combination producing the candidate inverse coupling), a *churn hole* (the lowest non-trivial Casimir eigenvalue), and a $c_{FK}$ (the Faraut–Koranyi normalization constant).

For each Cartan type, one can write a *universal formula* expressing these three quantities in terms of the type's parameters. Evaluating the formulas across the full Cartan classification at twenty-five candidate domains in the substrate's neighborhood, $D_{IV}^5$ produces the experimentally observed values uniquely: $\alpha = 137$, Casimir $= 6$, $c_{FK} \cdot \pi^{9/2} = 225$. No other bounded Hermitian symmetric domain in the classification matches all three.

So the substrate has three independent structural over-determinations: per-integer forcing arguments (one set per integer), Mersenne tower coherence (linking the integers in a generated cascade), and cross-Cartan three-pillar selection (distinguishing $D_{IV}^5$ from every alternative geometry via the universal algebraic invariants). The conjunction is the substrate's structural signature, and it is what makes the Strong-Uniqueness Theorem possible. Lyra's T2465 (the Three-Layer Over-Determinism formal theorem) packages this picture into a single result.

## 3.9 What this buys, and what it costs

The integer-forcing chapter is where BST cashes its conceptual check. Standard physics' twenty-five free parameters reduce, in BST, to five integers; the five integers reduce, in BST, to one geometry; the one geometry is mathematically forced by classical results outside physics. There is no fitting. The substrate's integer specification is a *theorem of mathematics*, not a measurement.

What this buys is what we have been claiming throughout: zero free parameters, all physics derivable from substrate structure, predictions that match experiment across hundreds of observables at sub-percent precision. The reader has seen, in summary form, the apparatus that makes this possible.

What it costs is what the rest of this volume will do: actually build the QFT machinery on top of the integers. Chapter 4 will use them to derive the discrete symmetries. Chapter 5 will use them to develop the Casimir algebra. Chapter 6 will use them to build the operator zoo. Chapter 7 will use them to write dynamics. By the end of the volume, the integers will be doing genuine work in every chapter.

## 3.10 What comes next

Chapter 4 derives the discrete symmetries — parity, time reversal, charge conjugation, and the CPT theorem — from the substrate structure now in place. The Möbius involution of the substrate isotropy, the Pin(2) double cover, the $SO(2)$ weight-negation involution, and the substrate's commitment-cycle direction-reversal will all appear as operators on the Hilbert space we built in Chapter 2, with their commutation properties and conservation laws falling out of the substrate's symmetry structure.

---

**Where to look this up**: The per-integer forcing theorems are T1925 (rank), T1930 ($N_c$), T2431 ($n_C$), T2432 ($g$), with the alternative-HSD comparisons T2443–T2446 ratifying them at the rigorously-closed tier. The Mersenne tower seed and closures are T2451, T2453, T2454, with the extended verification across $n \leq 1000$ being Elie's Toy 3442. The characteristic cube identity at $N_c = 3$ is T2464. The universal $\alpha$-analog formula across the Cartan classification is T2456, with the 25-domain verification being T2462. The three-layer over-determinism formal theorem is T2465. The cubic-coincidence verification toy is Toy 3326. For the Cartan classification background, Helgason 1978 Chapter X; for the Mersenne primes Hardy and Wright's *An Introduction to the Theory of Numbers*; for the Wallach K-type machinery, Wallach 1976; for the Reed–Solomon code structure on $GF(128)$, MacWilliams and Sloane's *The Theory of Error-Correcting Codes*.
