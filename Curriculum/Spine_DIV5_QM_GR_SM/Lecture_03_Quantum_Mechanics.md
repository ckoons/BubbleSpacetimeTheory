---
title: "Lecture 3 — Quantum Mechanics"
spine: "D_IV⁵: QM, GR and the SM — the derivations, tiered"
author: "Keeper, for Casey Koons and the team"
date: "2026-09-11 — v0.1"
sources: "The Axioms paper (notes/BST_paper_Axioms_of_QM_from_D_IV5_DRAFT_2026-08-04.md; Cal-vetted Section 447, Keeper PASS); the W1 resolution of 2026-08-22 (the physical Hilbert space is H²); T754 (Born from the invariant measure, Gleason), T753 (uncertainty from curvature; the defect at the word 'constant' recorded 09-09, repair owed to Lyra), T2543 (Code-Forces-Fermion; colour clause RULED struck 09-09, registry edit owed), T2545, T2401 (Born = Bergman projection, v0.1), T2630 (the Born-resolution row, with Cal Section 935's caveat verbatim), K1815 (the Internal-A floor), K1880–K1888 (the substrate lane; K1888 is the ruling on T2401 and the rate), Cal Sections 935 and 945 (the 10/10 count needs a registry row)"
tier_line: "DERIVED: the state space, observables, unitary evolution, Born rule, arrow, composites, and the measurement process with its odds, on H²(D_IV⁵); matter fermionic (T2543's theorem stands). STRUCTURE-DERIVED: the (3,1) signature. SUPERSEDED FOR THIS STEP, NOT REFUTED: T2401's Bergman-projection reading (K1888). OPEN: the α-hole — nothing in the dictionary now carries α (Lecture 8); the registry row for the ten-item count. NOT CLAIMED: the single outcome; that measurement is 'solved'."
---

# Lecture 3 — Quantum Mechanics

## The question

Where do the rules of quantum mechanics come from?

Textbooks give them as postulates: states are vectors in a complex Hilbert space, observables are self-adjoint operators, evolution is unitary, probabilities are squared amplitudes, measurement makes things definite. They work perfectly and explain nothing about themselves. The question this program asks is whether those rules are *features of one shape* — whether, having chosen the object of Lecture 1, we are then obliged to find quantum mechanics inside it. We think the answer is yes, and this lecture says exactly how far that yes goes.

## For the reader in a hurry

Our object has an inside and an edge. Functions that live smoothly on the inside and have well-behaved values on the edge form a space with exactly the structure quantum mechanics needs: you can add them, take their lengths, and rotate them without changing lengths. The edge is where anything definite happens — where a wave becomes a record — and the geometry of the edge tells you the odds. Ten standard rules of quantum mechanics come out as descriptions of this one space. What does *not* come out is which particular thing happens when you look: that is a fact about the world, not about the shape, and we do not pretend otherwise.

## The space, and a confusion we made ourselves

Two natural Hilbert spaces of holomorphic functions live on $D_{IV}^5$ (Lecture 1): the Bergman space $A^2$, square-integrable over the interior, and the Hardy space $H^2$, with square-integrable boundary values on the Šilov boundary $\check S$. For some months our papers wrote "the Bergman/Hardy space $H^2$" as if these were one thing. They are not, and the difference is physical: the Bergman space carries the interior's measure, the Hardy space carries the boundary's, and the boundary is where records are made.

**The physical Hilbert space is $H^2(D_{IV}^5)$** — the Hardy space (the W1 resolution, 2026-08-22). One label, pinned by Lyra in Round 142: $G = \mathrm{SO}_0(5,2)$ acts on it by the scalar-type unitary highest-weight representation with parameter $\nu = 5/2$, which lies in the analytic continuation *below* the discrete-series threshold $\nu > 4$ — it is the *Bergman* space, at $\nu = 5$, that is holomorphic discrete series. The W1 cell's phrase "holomorphic discrete series" attaches the Bergman label to the Hardy space and is flagged for correction; no theorem below needs more than "irreducible unitary." Everything below is stated there. The Bergman space is still used — the Born rule was first proved on its measure — and where the two meet is the one door in this lecture that is still open.

## Ten rules, one shape

The scorecard, as the Axioms paper states it and as the registry carries it this week. "Derived" means the mechanism is proved and the inputs are named.

| # | rule | on $D_{IV}^5$ | tier |
|---|---|---|---|
| 1 | states form a complex Hilbert space | $H^2(D_{IV}^5)$ | derived |
| 2 | observables are self-adjoint operators | operators on $H^2$; the physical ones are functions of the one generator and the boundary generators | derived |
| 3 | evolution is unitary | the unitary face $e^{i\theta J}$ of the one generator — $J$, the linear conformal Hamiltonian on the centre of $K$ (Lecture 4). The Axioms paper wrote the $K$-Casimir $H_B$ here; "Time, Derived" corrected it to $J$, and the two vetted papers disagree on the row. Keeper's ruling (2026-09-11, on Cal's second pass): the carrier is $J$ — a Casimir is scalar on each irreducible representation and cannot generate a flow within one — and T2631's generator clause records the collision | derived (the generator's *forcing* is the paper's own Structure-Derived, Lecture 4) |
| 4 | probability is a squared amplitude | Gleason's theorem on the unique automorphism-invariant measure; Lebesgue excluded (T754) | derived |
| 5 | uncertainty, $\Delta x\,\Delta p \geq \hbar/2$ | the holomorphic sectional curvature of the domain sets a resolution limit (T753) | proved, with a caveat: a rank-two domain has no constant holomorphic sectional curvature, and the row's word "constant" is a recorded defect whose repair is owed (Grace R140 G2 → Lyra); the normalisation is pinned to the source, not asserted |
| 6 | an arrow of time | the positivity of the contractive face $e^{-\tau H}$ | derived (the *geometric* arrow; the thermodynamic cost of unwriting a record is a separate theorem in the companion paper) |
| 7 | composite systems are tensor products | the two-particle kernel on $D \times D$ | derived, for distinguishable subsystems; identical particles are rule 10 |
| 8 | measurement makes things definite, with odds | a write — multiplication by a boundary coordinate on $H^2(\check S)$ — whose outcome weights are Hua's branching; there is no separate "push" step (T2630 retired the two-step composition an earlier draft of this row still carried); the odds are Born | derived, as process and odds; the *single outcome* is a boundary datum |
| 9 | spacetime has signature $(3,1)$; CPT | the descent $\mathrm{SO}(5,2)\to\mathrm{SO}(4,2)\to\mathrm{SO}(3,1)$; the $(3,1)$ count from the irreducibility of the three-dimensional slot $V_{12}$ (T2545, re-grounded 2026-09-11); CPT universal | structure-derived; the descent is *induced*, Lecture 9 |
| 10 | matter is fermionic | a committed record is an idempotent, $e\circ e = e$; an idempotent occupation has spectrum $\{0,1\}$ — Pauli's bit (T2543) | derived; this was held as a posit through three rounds of refusal before a computation forced it, and it is stronger for that |

Ten of ten *recovered*, at the tiers in the table; the derivations pass through four named posits (the ten-item row, T2631 — Cal's Round 142 C2 ruling that the count gets a row rather than retirement, Keeper-assigned, Grace to register verbatim), and "zero posits" is retired. The row licenses exactly this sentence: seven derived (two of them through an identification and a posit), one proved with a named caveat, one structure-derived on an induced descent, one identified — a count of recoveries, not a tier. It does not license "10/10 derived," "zero posits," or "zero free parameters," and the Axioms paper's subtitle that said so is retired with it.

On row 10, one open edit: T2543 also said that the middle Peirce space "is colour." That clause was ruled struck (Lecture 2); the registry row still carries it pending the edit. The theorem about records and idempotents does not use it and stands.

## The Born rule, and a naming

The Born rule is derived once, from the inside. The second passage below does not derive it a second time; it *names* the objects the rule applies to on the boundary, and that naming is this year's result.

**From the inside.** The automorphisms of the domain fix a unique invariant measure — the Bergman, or Faraut–Korányi, measure. Gleason's theorem says that on a Hilbert space of dimension at least three, any probability assignment to closed subspaces that is additive on orthogonal families is a squared amplitude against some density operator. Our Hilbert space is infinite-dimensional; the invariant measure gives the density; the Born rule follows (T754). One small honesty: the row's proof once said "dimension $\geq 3$ because $N_c = 3$." Gleason's hypothesis is met by any Hardy space; the $N_c$ was decoration, and it has been removed.

**From the edge.** On the Šilov boundary every point has $|z|^2 = 1$. Write $W_u = M_{z_u}$ for multiplication by the $u$-th coordinate in an orthonormal frame — the operation of *writing* one more symbol of a record. Then $\sum_u W_u^* W_u = \sum_u M_{|z_u|^2} = I$ on $H^2(\check S)$: **the write tuple is a resolution of the identity** — in operator-theory terms a *spherical* isometry (the column $(W_1;\ldots;W_5)$ is isometric; not a *row* isometry, which would need orthogonal ranges — T2630's registered text has the wrong word and is flagged to Grace) — and therefore its components define probabilities. Split each of the five writes by Hua's branching of the boundary harmonics and the weights come out, for $k = 0, 1, 2, \ldots$, as $(k+3)/(2k+3)$ and $k/(2k+3)$, summing to one at every $k$ (T2630; Elie's toy 5747 in exact rationals, Lyra to degree five, no table consulted). Chaining only those weights, the probability that a three-symbol word reads $(1,1)$ is $1/5 + (4/5)(2/7) = 3/7$ exactly. (The same rational names three other, unrelated objects in the corpus — a dipole weight, a push-cost cell, a zonal outcome; noted, not counted as corroboration.)

The same sum, evaluated with the *interior's* weight instead of the boundary's, fails to be one — by exactly $1/2$, $10/21$, $25/63$, $\ldots$ — and that failure is what an earlier round had been calling "the cost of a push." So four rounds of work collapsed into one fact: the push cost is the isometry defect of the write tuple, zero at the boundary, and the branching weights are Born probabilities.

Here is the caveat, carried in Cal's words because it was the condition of registration (Section 935). Sense one: the identity $\sum_u |z_u|^2 = 1$ holds on *any* subset of the unit sphere in $\mathbb{C}^5$, for the coordinate tuple of *any* orthonormal frame. Sense two: the branching weights were *defined* as normalised squared norms, so "these are Born probabilities" restates their computation. One thing that sharpens the caveat rather than diluting it: the *identity* is tautological on any subset of the sphere, but the *weights* are not — they carry $n - 2 = 3$, and the descending ("matter") branch exists only because $\check S$ is the Lie sphere; on the unit sphere $S^9$ the coordinate tuple has no descending branch at all. So "the write tuple is a resolution of the identity" is a tautology of the boundary condition in two independent senses, and what T2630 establishes is a **naming** — that the objects the program calls writes and records *are* a POVM whose probabilities are Hua's weights — not a derivation of new physics. We think the naming is worth having. We do not think it is more than that.

## Measurement as commitment

The ontology underneath rows 8 and 10 has a name in the program: measurement is *commitment*. A superposition is uncommitted capacity in the interior; a measurement is a write to the boundary; a record is what persists there, and persistence — $e \circ e = e$, a record that reads the same twice — is what makes the occupation a bit and the matter fermionic. The process and the odds are derived. The *particular outcome* is not: it is a boundary datum, the way an initial condition is a datum, and the over-claim we refuse is that quantum randomness has been explained away.

## What T2630 dissolved, and the hole it left

For a round the program looked for a separate "commitment effect" — a non-isometric push distinct from the writes, whose cost would be a probability and whose rate against the write rate might be $\alpha$. T2630 dissolved that search rather than solving it (K1888): the writes *are* the resolution of the identity, push and write are one event, so their ratio is one and no rate in the dictionary is of order $1/137$. T2401's reading of the Born rule as the Bergman projection is *superseded for this step, not refuted* — T754 remains load-bearing, licensing the expectation as a probability while the tuple supplies the effect. The hole this leaves is real and stated as one: **nothing in the dictionary now carries $\alpha$** (Lecture 8). (An earlier draft of this section named a "Bergman-to-Hardy probability link" as the open door and promised the clock would be "read as reliability"; that was one round stale — Cal, Round 142 — and is withdrawn.)

## A loss, with the same ceremony as a win

Quantum mechanics has one laboratory that belongs to it alone — Bell's — and the program once made a prediction there. In May 2026 it registered a *sub-Tsirelson ceiling*: the maximal CHSH value would be $S = \sqrt{126/16} = 2.80624$, below the quantum bound $2\sqrt 2 = 2.82843$ by exactly $1/2^{N_c} = 1/8$ in $S^2$, and it called this "the sharpest falsifier in the program," with a six-to-twelve-month window for a Bell test. The test had been done ten years earlier. Poh, Joshi, Ceré, Cabello and Kurtsiefer (*Phys. Rev. Lett.* **115**, 180408, 2015) measured $S = 2.82759 \pm 0.00051$, a distance $0.00084 \pm 0.00051$ from Tsirelson's bound — and $41.9\sigma$ above the program's ceiling. The falsifier **fired**, and it fired before it was written (Grace, Round 142 G3; certified K1893; register row E4).

What died: the ceiling as a prediction; the Bell-apparatus proposal and its letter; the two legacy chapters that *are* the prediction (Vol 5 Ch 8, Vol 14 Ch 6); the substrate-coding principle's place among the program's standing principles. What survives: the integer identity, which never said anything until it was attached to $S$; the trace identity $\mathrm{Tr}(B^2) = 126/16$ as a fact about an operator on $H^2$, with no laboratory claim; and — the point that matters for this lecture — **the Tsirelson bound itself is untouched**, because the quantum mechanics recovered on the Hardy space *is* standard quantum mechanics, whose bound is $2\sqrt 2$. The fired number was a coding reading laid over QM, not a consequence of the geometry. The lesson, in one line: a falsifier that names an experiment is checked against the literature the day it is registered.

## Tier line

- **Derived, on $H^2(D_{IV}^5)$:** rules 1–4, 6, 7 (distinguishable scope), 8 (process and odds), 10.
- **Proved with a named caveat:** rule 5 (curvature normalisation pinned, not asserted).
- **Structure-derived:** rule 9.
- **Superseded for this step, not refuted:** T2401's Bergman-projection reading (K1888).
- **Fired and lost (register E4):** the sub-Tsirelson ceiling.
- **Open:** the α-hole (Lecture 8); the registry row for the ten-item count.
- **Not claimed:** the single outcome; that measurement is "solved"; that CPT is distinctive (it is universal).

## What would make this lecture wrong

Rules 1–4 and 6–8 are theorems on a fixed space; they fail only if the space is the wrong one, and Lecture 2 tells you exactly which input picks it. Rule 10 has no laboratory falsifier, and we say why: by the floor's first step, repeatability *is* idempotence — a "record" that read differently the second time would not be a record — so the rule fires only against its own definition; its empirical content, no stable parafermionic matter in $3+1$ dimensions, is Leinaas–Myrheim's theorem, not an experiment. This lecture's laboratory exposure was the sub-Tsirelson ceiling, and it fired (above). What remains exposed is the hole, and the count awaiting its row.

## Where to look

The Axioms paper and its narrative pilot (2026-08-13) for the scorecard and the floor; T754, T753, T2543, T2545, T2401 and T2630 in the registry, with their September annotations; K1815 for the Internal-A floor (repeatability implies idempotence; nontriviality implies rank $\geq 2$; rank $= 2$ the posit; a simple rank-2 Euclidean Jordan algebra is a spin factor, whose domain is a Lie ball — Faraut–Korányi, cited and not banked; note that rank-2 *domains* also include $I_{2,q}$, $II_5$, $III_2$ and the $E_6$ type, so the step is about the Jordan algebra, not the domain list); K1880–K1886 for the substrate lane that produced T2630; Cal Sections 935 and 945.
