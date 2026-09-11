---
title: "Lecture 3 — Quantum Mechanics"
spine: "D_IV⁵: QM, GR and the SM — the derivations, tiered"
author: "Keeper, for Casey Koons and the team"
date: "2026-09-11 — v0.1"
sources: "The Axioms paper (notes/BST_paper_Axioms_of_QM_from_D_IV5_DRAFT_2026-08-04.md; Cal-vetted Section 447, Keeper PASS); the W1 resolution of 2026-08-22 (the physical Hilbert space is H²); T754 (Born from the invariant measure, Gleason), T753 (uncertainty from curvature; the word 'constant' repaired 09-09), T2543 (Code-Forces-Fermion; colour clause struck 09-09), T2545, T2401 (Born = Bergman projection, v0.1), T2630 (the Born-resolution row, with Cal Section 935's caveat verbatim), K1815 (the Internal-A floor), K1880–K1886 (the substrate lane), Cal Section 945 (the 10/10 count needs a registry row)"
tier_line: "DERIVED: the state space, observables, unitary evolution, Born rule, arrow, composites, and the measurement process with its odds, on H²(D_IV⁵); matter fermionic (T2543's theorem stands). STRUCTURE-DERIVED: the (3,1) signature. IDENTIFIED: the push as the Szegő projection; the commitment effect as an observable. OPEN: the Bergman-to-Hardy probability link; the registry row for the ten-item count. NOT CLAIMED: the single outcome; that measurement is 'solved'."
---

# Lecture 3 — Quantum Mechanics

## The question

Where do the rules of quantum mechanics come from?

Textbooks give them as postulates: states are vectors in a complex Hilbert space, observables are self-adjoint operators, evolution is unitary, probabilities are squared amplitudes, measurement makes things definite. They work perfectly and explain nothing about themselves. The question this program asks is whether those rules are *features of one shape* — whether, having chosen the object of Lecture 1, we are then obliged to find quantum mechanics inside it. We think the answer is yes, and this lecture says exactly how far that yes goes.

## For the reader in a hurry

Our object has an inside and an edge. Functions that live smoothly on the inside and have well-behaved values on the edge form a space with exactly the structure quantum mechanics needs: you can add them, take their lengths, and rotate them without changing lengths. The edge is where anything definite happens — where a wave becomes a record — and the geometry of the edge tells you the odds. Ten standard rules of quantum mechanics come out as descriptions of this one space. What does *not* come out is which particular thing happens when you look: that is a fact about the world, not about the shape, and we do not pretend otherwise.

## The space, and a confusion we made ourselves

Two natural Hilbert spaces of holomorphic functions live on $D_{IV}^5$ (Lecture 1): the Bergman space $A^2$, square-integrable over the interior, and the Hardy space $H^2$, with square-integrable boundary values on the Šilov boundary $\check S$. For some months our papers wrote "the Bergman/Hardy space $H^2$" as if these were one thing. They are not, and the difference is physical: the Bergman space carries the interior's measure, the Hardy space carries the boundary's, and the boundary is where records are made.

**The physical Hilbert space is $H^2(D_{IV}^5)$** — the Hardy space, on which the group $G = \mathrm{SO}_0(5,2)$ acts by the holomorphic discrete series (the W1 resolution, 2026-08-22). Everything below is stated there. The Bergman space is still used — the Born rule was first proved on its measure — and where the two meet is the one door in this lecture that is still open.

## Ten rules, one shape

The scorecard, as the Axioms paper states it and as the registry carries it this week. "Derived" means the mechanism is proved and the inputs are named.

| # | rule | on $D_{IV}^5$ | tier |
|---|---|---|---|
| 1 | states form a complex Hilbert space | $H^2(D_{IV}^5)$ | derived |
| 2 | observables are self-adjoint operators | operators on $H^2$; the physical ones are functions of the one generator and the boundary generators | derived |
| 3 | evolution is unitary | the unitary face $e^{i\tau H}$ of the one generator (Lecture 4 names it) | derived |
| 4 | probability is a squared amplitude | Gleason's theorem on the unique automorphism-invariant measure; Lebesgue excluded (T754) | derived |
| 5 | uncertainty, $\Delta x\,\Delta p \geq \hbar/2$ | the holomorphic sectional curvature of the domain — the blur of imaging a discrete interior onto a continuum (T753) | proved, with a caveat: the curvature of a rank-two domain is not constant, and the row's old word "constant" was repaired on 2026-09-09; the normalisation is pinned to the source, not asserted |
| 6 | an arrow of time | the positivity of the contractive face $e^{-\tau H}$ | derived (the *geometric* arrow; the thermodynamic cost of unwriting a record is a separate theorem in the companion paper) |
| 7 | composite systems are tensor products | the two-particle kernel on $D \times D$ | derived, for distinguishable subsystems; identical particles are rule 10 |
| 8 | measurement makes things definite, with odds | a contractive commit — a forced drop to the boundary composed with the measure-keeping projection; the odds are Born | derived, as process and odds; the *single outcome* is a boundary datum |
| 9 | spacetime has signature $(3,1)$; CPT | the descent $\mathrm{SO}(5,2)\to\mathrm{SO}(4,2)\to\mathrm{SO}(3,1)$; the $(3,1)$ count from the long root (T2545); CPT universal | structure-derived; the descent is *induced*, Lecture 9 |
| 10 | matter is fermionic | a committed record is an idempotent, $e\circ e = e$; an idempotent occupation has spectrum $\{0,1\}$ — Pauli's bit (T2543) | derived; this was held as a posit through three rounds of refusal before a computation forced it, and it is stronger for that |

Ten of ten. We have said "ten of ten, zero posits" in many places, and it is true on the floor the companion paper ratified — but Cal ruled in September (Section 945) that a completeness count with no registry row of its own is a claim no audit was ever obliged to check. The row is owed. Until it exists we quote the count at the tier of the rows it rests on, which are listed above, and not as a headline.

On row 10, one repair: T2543 also said that the middle Peirce space "is colour." That clause is struck (Lecture 2). The theorem about records and idempotents does not use it and stands.

## The Born rule, twice

The Born rule is the rule we can show you from two directions, and the second direction is this year's result.

**From the inside.** The automorphisms of the domain fix a unique invariant measure — the Bergman, or Faraut–Korányi, measure. Gleason's theorem says that on a Hilbert space of dimension at least three, any probability assignment to closed subspaces that is additive on orthogonal families is a squared amplitude against some density operator. Our Hilbert space is infinite-dimensional; the invariant measure gives the density; the Born rule follows (T754). One small honesty: the row's proof once said "dimension $\geq 3$ because $N_c = 3$." Gleason's hypothesis is met by any Hardy space; the $N_c$ was decoration, and it has been removed.

**From the edge.** On the Šilov boundary every point has $|z|^2 = 1$. Write $W_u = M_{z_u}$ for multiplication by the $u$-th coordinate in an orthonormal frame — the operation of *writing* one more symbol of a record. Then $\sum_u W_u^* W_u = \sum_u M_{|z_u|^2} = I$ on $H^2(\check S)$: **the write tuple is a resolution of the identity** — a row isometry — and therefore its components define probabilities. Split each of the five writes by Hua's branching of the boundary harmonics and the weights come out, for $k = 0, 1, 2, \ldots$, as $(k+3)/(2k+3)$ and $k/(2k+3)$, summing to one at every $k$ (T2630; Elie's toy 5747 in exact rationals, Lyra to degree five, no table consulted). Chaining only those weights, the probability that a three-symbol word reads $(1,1)$ is $1/5 + (4/5)(2/7) = 3/7$ exactly — a fraction that had appeared in the program months earlier by another route.

The same sum, evaluated with the *interior's* weight instead of the boundary's, fails to be one — by exactly $1/2$, $10/21$, $25/63$, $\ldots$ — and that failure is what an earlier round had been calling "the cost of a push." So four rounds of work collapsed into one fact: the push cost is the isometry defect of the write tuple, zero at the boundary, and the branching weights are Born probabilities.

Here is the caveat, carried in Cal's words because it was the condition of registration (Section 935). The identity $\sum_u |z_u|^2 = 1$ holds on *any* subset of the unit sphere in $\mathbb{C}^5$, for the coordinate tuple of *any* orthonormal frame. So "the write tuple is a resolution of the identity" is a tautology of the boundary condition, in two independent senses, and what T2630 establishes is a **naming** — that the objects the program calls writes and records *are* a POVM whose probabilities are Hua's weights — not a derivation of new physics. We think the naming is worth having. We do not think it is more than that.

## Measurement as commitment

The ontology underneath rows 8 and 10 has a name in the program: measurement is *commitment*. A superposition is uncommitted capacity in the interior; a measurement is a write to the boundary; a record is what persists there, and persistence — $e \circ e = e$, a record that reads the same twice — is what makes the occupation a bit and the matter fermionic. The process and the odds are derived. The *particular outcome* is not: it is a boundary datum, the way an initial condition is a datum, and the over-claim we refuse is that quantum randomness has been explained away.

## The one open door

The Born rule from the inside is proved on the Bergman measure. The push — the map that takes an interior state to its boundary record — is identified with the Szegő projection, which is the Hardy space's own projection. No registry row yet reads a Bergman-normalised state's *Hardy mass* as a probability. That missing link is small, technical, and load-bearing: it caps the commitment chain at version 0.1 of T2401 however much else is proved. Lyra's candidate form is "two kernels, two roles" — the probability is read on the interior, the projection is the map applied on commit. If that row is written, the push cost becomes a probability and the clock of Lecture 4 is read as reliability. If it cannot be written, this lecture ends where it stands, and we will say so.

## Tier line

- **Derived, on $H^2(D_{IV}^5)$:** rules 1–4, 6, 7 (distinguishable scope), 8 (process and odds), 10.
- **Proved with a named caveat:** rule 5 (curvature normalisation pinned, not asserted).
- **Structure-derived:** rule 9.
- **Identified:** the push as the Szegő projection; the commitment effect $M_{|z|^2}$ as a two-outcome observable.
- **Open:** the Bergman-to-Hardy probability link; the registry row for the ten-item count.
- **Not claimed:** the single outcome; that measurement is "solved"; that CPT is distinctive (it is universal).

## What would make this lecture wrong

Rules 1–4 and 6–8 are theorems on a fixed space; they fail only if the space is the wrong one, and Lecture 2 tells you exactly which measured input picks it. Rule 10 fails if a persistent record can be exhibited whose occupation is not idempotent — a stable "record" that reads differently the second time — which would be a discovery about the world. The honest exposure of this lecture is not a laboratory number; it is the open door above, and the count awaiting its row.

## Where to look

The Axioms paper and its narrative pilot (2026-08-13) for the scorecard and the floor; T754, T753, T2543, T2545, T2401 and T2630 in the registry, with their September annotations; K1815 for the Internal-A floor (repeatability implies idempotence; nontriviality implies rank $\geq 2$; rank $= 2$ the posit; rank $2$ implies type IV by Faraut–Korányi, cited and not banked); K1880–K1886 for the substrate lane that produced T2630; Cal Sections 935 and 945.
