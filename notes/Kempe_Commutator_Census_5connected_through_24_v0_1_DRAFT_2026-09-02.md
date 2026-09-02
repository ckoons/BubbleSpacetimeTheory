---
title: "Kempe commutators at a stuck pentagon: an exhaustive census on 5-connected triangulations through 24 vertices — DRAFT v0.1"
author: "Casey Koons, with Lyra, Elie, Grace, Keeper (CI co-authors); visiting referee Cal A. Brate"
date: "2026-09-02, Wednesday (draft assembled 12:43 EDT; v0.1 — internal, not for dispatch; Cal's referee read and Keeper's K-gate owed tomorrow)"
status: "DRAFT v0.1. Every number below is a census number produced on two independent instruments with blind-hashed witness lists (Appendix B); every lemma marked DERIVED has an artifact and an independent re-derivation on record; every open clause is marked. Nothing in this document claims a proof of the Four Colour Theorem, and nothing in it concerns triangulations with more than 24 vertices."
---

# Abstract

At a degree-five vertex v of a 4-coloured sphere triangulation T minus v, a colouring is *stuck* when every colour
appears on the link and no single Kempe swap frees one. We prove that stuckness forces a single local context up
to symmetry: one link word and six forced chain partitions, hence exactly eight Kempe chains meeting the link,
and these are Kittell's eight switches of 1935 under an explicit seed rule (Section 2). We study one operation
on that context — the four-swap commutator of two link-seeded Kempe swaps with the seeds held fixed — and derive
its stage table: the bridge-anchored commutator is legal at every stuck configuration (Lemma L); its image is
insertable unless one named chain reconnects (Lemma D); and on the remaining branch the image is stuck exactly when
two chain-coincidence questions both hold, which forces the fourth chain to cut the third at r-vertices one step
from the link (Lemma T, the Arc Lemma). We prove that where the far copy's chain misses the middle road, Kempe's
own two swaps of 1879 insert v while the commutator built from the same two chains is the identity (Theorem KP).
We then report an exhaustive census of every stuck colouring, modulo colour permutation, at every degree-five vertex
of every 5-connected sphere triangulation with 12 to 24 vertices: 7,379,253 stuck colourings. All but 349 reach the
gate phase (τ ≤ 5, one swap from insertable) within one fully legal word of the frozen 186-word commutator menu; all
349 reach it within two; none needs three. The 349 are *commutator-locked at depth one*, a menu-relative notion: in
the unrestricted alphabet of plain Kempe swaps, 27 of them exit in one swap and Kempe's own pairing inserts on two.
We give the census in both alphabets, a measured necessary condition for the commutator lock that holds on all 349
and on 35 percent of the census, the growth of the one-word hitting set with n, and the family's image-count
collapse at the lock, each beside the null that predicts it. We state what is asserted for all n (the lemmas) and
what is not (every count). The open question is Gethner, Kallichanda, Mentis et al.'s of 2009, sharpened: whether a
bounded number of fixed-seed commutators always suffices, and if so, why.

# 0. Definitions and the naming ruling

**Setting.** T a sphere triangulation (simple, every face a triangle; by Whitney every vertex link is a simple
cycle for |V| ≥ 4), v a vertex of degree five, c a proper 4-colouring of T − v with T's embedding retained (v is
uncoloured, not deleted; every Jordan argument below closes through v's location). Colours {r, s_M, s_i, s_j} are
named by role once the context is fixed (Section 2.1). A *Kempe chain* is a component of the subgraph induced by
two colour classes; a *swap* exchanges the two colours on one chain and preserves properness.

**Frame.** All census statements are on *5-connected* sphere triangulations (no separating 3- or 4-cycles; δ = 5
follows). This is the class every minimal counterexample to the Four Colour Theorem belongs to (Birkhoff 1913;
re-derived in the corpus as A5.1–A5.3 without citation), stated as a class of real graphs and never as "minimal
counterexamples," on which any statement would be vacuous or false. Nothing below uses 5-connectivity in a
derivation; every lemma is an all-T lemma; the frame governs the census only.

**Operational tangling (Definition 5 of the corpus's standalone paper).** A colour pair (a,b) is *operationally
untangled* at v if a single (a,b)-swap in T − v frees a or b at v. τ(v) is the number of tangled pairs, 0 ≤ τ ≤ 6.
v is *insertable* if some colour is absent from its link; *the gate phase* is τ ≤ 5 or insertable (one swap from
insertable); *stuck* is τ = 6.

**The menu.** Fifteen *moves* (seed, pair): the five link vertices, each with the three pairs containing its colour.
A *word* is an ordered pair of moves with distinct pairs, applied as the four-stage commutator m₁ m₂ m₁ m₂; 225 − 39
same-pair pairs = 186 words, 93 orbits under the context's mirror. A stage is *legal* if its seed carries a colour
of its pair at that stage; a word is *fully legal* if all four stages act. The menu is a position: every factor
(five roles, three pairs per role, the commutator shape) is forced by the context or by the definition of a word;
it is frozen, and a stuck configuration no word frees is recorded as a kill of the one-word claim, never as an
amendment of the menu.

**The corrected noun.** A stuck colouring is *commutator-locked at depth one* if no fully legal word of the
186-menu takes it to the gate phase. The notion is *menu-relative*: it depends on the fixed-seed four-stage shape
and on link-seeding. It is not Kempe-locking (Tilley 2018, an edge-relative and unbounded notion) and it is not a
property of the colouring's Kempe landscape: Section 3.3 exhibits commutator-locked colourings that a single plain
swap, seeded off the link, takes to the gate phase, and two on which Kempe's own two swaps insert v. We never write
"locked" bare. *[Cal: the definition paragraph with the naming ruling, in your wording, replaces this paragraph in
v0.2.]*

**The frame-independent number.** The *unrestricted Kempe depth* of a stuck colouring is the least number of plain
Kempe swaps (any seed in T − v, any pair) taking it to the gate phase. It is the number a referee will ask for
first, and Section 3.3 reports it beside the commutator depth. *[Slot: the unrestricted depth table — Elie, this
afternoon.]*

# 1. Where Kempe was right, and why the commutator hides it

**Theorem KP (DERIVED; independent re-derivation on record).** Let c be stuck with the canonical context of Section
2.1; let ζ be the far copy B₁'s (r,s_i)-chain and η the far copy B₂'s (r,s_j)-chain (Kempe's pairing: each copy
with the pair of the singleton it does *not* touch). If ζ contains no vertex of the middle road F_i (the
(s_M,s_i)-chain joining the middle vertex to the near singleton), then: (i) the single swap of ζ already puts c in
the gate phase; (ii) the two swaps ζ then η make a colour absent at v — Kempe's argument of 1879 is correct
exactly here; (iii) the fully legal four-stage word ζ·η is the identity on c.

*Proof.* F_i closed through v is a cycle separating the near copy B₂ from {B₁, n_sj}. ζ is colour-disjoint from
{s_M} and cannot pass through v, so under the hypothesis it lies entirely on B₁'s side. After the ζ-swap, F_i is
untouched and B₂'s side is unchanged; the (r,s_j)-chain of B₂ is colour-disjoint from the wall, hence equals η, the
c-chain, which by the forced partition contains neither B₁ nor n_sj. So (r,s_j) is untangled after one swap — (i) —
and after the η-swap the link reads (s_i, s_M, s_j, s_i, s_j), r absent — (ii). Stages 3 and 4 swap the same two
vertex sets back (toggling colours inside a chain does not change its membership in the two-colour world, and the
wall keeps the two sides independent): c₄ = c — (iii). ∎

**What KP says.** Heawood's counterexample is the hypothesis failing: the far chain touching the road lets the new
r-material reconnect B₂ to n_sj. And the fixed-seed commutator, built from Kempe's two chains, undoes in stages 3 and
4 the exit its own prefix performs. The menu's virtue is derivability — the stage tables of Section 2 — not depth; a
shape can hide its own prefixes, and the census of Section 3.3 shows it does. KP is one-directional: a far chain
that *does* meet the road forbids nothing (two of the 349 commutator-locked colourings have Kempe's pairing insert v).

# 2. The derived structure

## 2.1 The One-Context Lemma (DERIVED, zero census inputs)

At a stuck degree-five vertex of any sphere triangulation, up to rotation, reflection and colour permutation: the
link word is (r, s_M, r, s_i, s_j) — bridge colour r at positions 0 and 2, middle colour s_M at position 1,
singletons s_i, s_j at positions 3, 4 — and the six pair-partitions of the link vertices into chains are forced:
(r,s_M): {B₁, n_sM, B₂} one chain · (r,s_i): {B₁} | {B₂, n_si} · (r,s_j): {B₁, n_sj} | {B₂} · (s_M,s_i): {n_sM, n_si}
· (s_M,s_j): {n_sM, n_sj} · (s_i,s_j): {n_si, n_sj}. (Inputs: the gap-1 bound and the strict-tangle bound of the
standalone paper, both re-derived; Middle-Strict; Orientation; the singleton remark. Escorted at 4,858/4,858 and
374,658/374,658 with a positive control.) B₂ is the copy adjacent to n_si; B₁ the copy adjacent to n_sj.

## 2.2 The eight chains and Kittell's alphabet (DERIVED)

The fifteen moves name exactly eight distinct chains at a stuck configuration, because the six forced partitions
merge the seeds: M = (r,s_M) ∋ {B₁, n_sM, B₂}; F_i = (s_M,s_i) ∋ {n_sM, n_si}; F_j = (s_M,s_j) ∋ {n_sM, n_sj}; E =
(s_i,s_j) ∋ {n_si, n_sj}; δ = B₂'s (r,s_i) ∋ n_si; γ = B₁'s (r,s_j) ∋ n_sj; ζ = B₁'s (r,s_i); η = B₂'s (r,s_j). These
are Kittell's eight (Kittell 1935; relettered by Gethner et al. 2009) *under the far-copy seed rule*: read at the
other seeds, two of Kittell's names collapse onto the adjacent-pairing chains and the list names six. The
identification is of chains at a stuck configuration, not of operations: Kittell's group is frame-relative (the
ring vertex moves after each operation) and his identity for the adjacent-pairing switches is a statement in that
convention; our commutators hold their seeds fixed. Theorem KP is the fixed-seed analogue of his identity for the
Kempe-pairing switches. **Three-column key** (left/right up to the mirror):

| Kittell 1935 | Kittell's name | Gethner et al. 2009 | this paper |
|---|---|---|---|
| α, β | left/right-hand chain (copy with non-adjacent singleton's pair) | γ, η at the far seeds | ζ = B₁'s (r,s_i), η = B₂'s (r,s_j) |
| γ, δ | left/right-hand circuit (middle–singleton) | α, β | F_i, F_j |
| ε | end tangent chain | ε | E |
| ζ, η | left/right-hand tangent (copy with adjacent singleton's pair) | δ, γ at the near seeds | δ = B₂'s (r,s_i), γ = B₁'s (r,s_j) |
| θ | osculating chain | θ | M |

## 2.3 The bridge-anchored commutator: Lemmas L, D, T (DERIVED; independent re-derivations on record)

W_i := (B₂,(r,s_i))·(B₁,(r,s_j)) — each copy swapped with the pair of the singleton it touches; W_j its mirror.

**Lemma L (Legality).** W_i is fully legal at every stuck configuration: stage 1's seed carries r; stage 2's seed
B₁ is not in B₂'s (r,s_i)-chain and still carries r; stage 3's seed carries s_i because an (r,s_j)-swap touches no
s_i-vertex; stage 4's seed carries s_j because an (r,s_i)-swap touches no s_j-vertex. (Consequence: the choice of
word never needs a legality sub-condition.)

**Lemma D (Dichotomy).** Stages 1–2 are forced on the link: c₁ = (r, s_M, s_i, r, s_j); c₂ = (s_j, s_M, s_i, s_j, r),
saturated — the two-swap prefix never inserts (Heawood's interference as a theorem for this word). Stage 3 asks one
question, Δ: is the far singleton n_sj in the near copy's (r,s_i)-chain of c₂? If not, c₃ = (s_j, s_M, r, s_j, r)
has s_i absent, stage 4's chain is forced through three bichromatic link edges to contain all four of {B₁, n_sj,
n_si, B₂}, and c₄ = (r, s_M, s_j, r, s_j) has s_i absent: directly insertable. If so, stage 4 asks Δ′: are the near
copy and near singleton in the far copy's (r,s_j)-chain of c₃? If so, the three-stage prefix is in the gate phase
(a direct planarity line exhibits the freeing swap). If not, c₄ = (r, s_M, r, s_j, s_i) is the canonical word with
the singleton colours exchanged.

**Lemma T (the two-question lemma).** On that last branch, c₄ is stuck if and only if Q3 (the middle vertex and the
near singleton share an (s_M,s_j)-chain of c₄) and Q4 (the middle vertex and the far singleton share an
(s_M,s_i)-chain of c₄). Two of the six template partitions are automatic, one is forced by Δ′-NO, and Q3 ⟹ the
remaining one by Jordan through v. Q4 is decided in c₃. Q3 forces, by Menger, the fourth chain's r-vertices to
separate the near copy from the far singleton inside the third chain: *the cut*, C = X₄ ∩ X₃. (Escorted 548/548 on
the out-of-frame census and on every hard-branch instance in frame; the six gate leaves are exactly (Q3, ¬Q4).)

**Linear form (necessity only).** A stuck image of W_i is the conjunction of three connectivity facts in three
bichromatic worlds: C separates inside the (r,s_i)-world, Q3 holds in the (s_M,s_j)-world, Q4 in the (s_M,s_i)-world
— three rank conditions on three subgraph Laplacians, none sufficient alone. *[Wording pending Cal.]*

## 2.4 The Arc Lemma (DERIVED to one adjacency; the adjacency is open)

At a commutator lock, on W_i's hard branch: the far singleton n_sj is s_i in c₃ and every r-coloured neighbour of
it lies in X₃; the road R₄ of Q4 enters n_sj through an s_M-neighbour, and R₄ closed through v is a wall the
(r,s_j)-chain X₄ cannot cross, so X₄ — and the cut — lie on the far copy's side. On n_sj's neighbour cycle that side
is the arc from the far copy B₁ to the road's entry point x_b; every vertex on the arc is in X₄ by adjacency from
B₁, and every r-coloured one is in X₃ by adjacency to n_sj. Hence **C ∩ N(n_sj) is exactly the set of r-vertices on
that arc, and no cut vertex is a link vertex.** Measured: the cut sits at distance exactly one from the link on all
349 locks for both bridge words (and on 28,549 of 28,558 bridge-stuck images, the nine exceptions not being locks).
**Open:** that the arc carries an r-vertex at every lock — one adjacency, with its kill recorded.

## 2.5 The cut by original colour, the letter table, and the Necessity Lemma (DERIVED)

A cut vertex is either an r-vertex of the near copy's own chain in c (type A) or an s_i-vertex the second swap
annexed (type B); measured on the 93: 36 type A, 421 type B. A word whose net support misses the closed
neighbourhood of the bridge chains and the two roads re-locks with the same cut (Lemma N). Which letters can move
which type at which stage is a bookkeeping table (the corpus's letter table); it predicts that a word with no
middle-colour letter cannot move a type-B vertex, and the census agrees.

## 2.6 The type table: 22 forced bits and five measured necessary conditions

The incidence matrix of the eight chains has 28 off-diagonal entries; 22 are forced by the context (two chains
sharing a link vertex meet; colour-disjoint pairs miss; same-pair chains are distinct components) and six are free,
so the type is a 6-bit word. In frame, 40 of 64 words occur, and the count stops growing at n = 21. **Necessary
conditions for the commutator lock (T2595; measured, not derived; converse false):** the far copy's chain meets both
the middle road and the singleton road on its side — all four bits — on 349/349 locks (256 of them out of sample at
n = 24); the same four hold on 1,121 of the 1,211 configurations where both bridge words fail (the 90 violators are
on disk and are not locks) and on 35 percent of a generic stratified sample; a fifth bit (at least one of the two
copy-pairings' chains meet) holds on 349/349 and on 26 percent generically. No incidence pattern at any refinement
tried is sufficient (Section 4: purity by fragmentation is not classification).

# 3. The census

Generator: plantri 5.8, `-c5`, n = 12…24 (graph counts 1 · 0 · 1 · 1 · 3 · 4 · 12 · 23 · 71 · 187 · 627 · 1,970 ·
6,833). At every degree-five vertex, every proper 4-colouring of T − v modulo colour permutation, every stuck one
tested. Two instruments per number (union-find/BFS; Laplacian rank), witness lists hashed before comparison.

## 3.1 Commutator depth (the menu's own units)

| n | stuck colourings | no direct one-word exit | one legal word to the gate phase | exactly two | three or more |
|---|---|---|---|---|---|
| ≤ 21 | 87,361 | 334 | 308 | 26 | 0 |
| 22 | 287,297 | 827 | 804 | 23 | 0 |
| 23 | 1,216,851 | 1,579 | 1,535 | 44 | 0 |
| 24 | 5,787,744 | 10,488 | 10,232 | 256 | 0 |
| total | 7,379,253 | 13,228 | 12,879 | **349** | **0** |

The 349 are commutator-locked at depth one (n = 17: 8 · 21: 18 · 22: 23 · 23: 44 · 24: 256). Every classical Kempe
killer is out of frame (degree ≤ 4 vertices present) and is depth one there: Fritsch 72/72, Poussin 38/38, Kittell
670/670, Errera 200/200 direct one-word exits.

**The null beside the zero.** A depth-three configuration requires every fully legal image of a locked configuration
to be locked. At the measured lock rate (4.4 × 10⁻⁵ of stuck colourings at n = 24), with lock probability clustering
near 80 percent along the bridge words and near zero along the other sixteen orbits, the expected number of
depth-three configurations in this census is below one. The observed zero therefore supports no mechanism, and we
claim none.

**The falling fraction, as numbers only.** Of the stuck colourings without a direct one-word exit, those needing two
words: 26/334, 23/827, 44/1,579, 256/10,488 (7.8, 2.8, 2.8, 2.4 percent). Not extrapolated.

## 3.2 The second word and the exit mechanism

On every one of the 349, the two-word exits run through a first word that moves the middle colour and a second word
that is a bridge word in the image's own frame; the bridge words as *first* word lead to a two-word exit on 10 of
the first 49 only. Exits act by **re-routing**, not by removing the cut: after an exiting first word the third
chain reconnects around the cut in 6,207 of 6,503 exits; the cut vanishes in 138. Pair-specific containment of the
cut by a middle-pair stage is a sufficient certificate of exit with a perfect control (720/720 exits; 0/3,632
non-exits) and is not necessary (1,216 exits without it). The image's bridge leaf after an exiting word is Δ-NO on
69 percent against a census base near 99.7 percent at the same n: the first word leaves the image harder than a
generic stuck colouring, and no orbit is the flipper (rates 0.65–0.77, flat).

## 3.3 The unrestricted alphabet (the field's units)

On the 349, plain Kempe swaps with any seed: **one swap reaches the gate phase on 27**; Kempe's own pairing (ζ then η
or the reverse) inserts v on 2; two link-seeded switches, the second re-derived in the image, reach the gate on 113;
one swap anywhere then one switch on 116; every lock resolves in at most three Kittell switches. Two commutators are
eight plain swaps. **The commutator's contribution is derivability, not depth.** *[Slot: the unrestricted Kempe
depth table on the 349, the 10,488, and the stratified sample — distribution and maximum per population.]*

## 3.4 Hitting sets and the family's collapse

The minimum one-word hitting set (gate-phase exits, exact) grows with n: 1 · 2 · 8 · 4 · 6 · 9 · 14 · 21 for
n = 14…22 (orbit level 12 at n = 22); out of frame it was three words and flat. On the 90 far-bit-off bridge-fail
configurations the exact hitting set is four words (three orbits) and no single word exits all 90. *The menu is
doing work no one has derived.* The one feature that separates locks from matched depth-one configurations on the
same (T, v) is the number of distinct images the 186 words make: mode 8 at a lock, mode 13 otherwise (best split
155/186) — a feature, not a grade.

# 4. What died, reported as results

Each item was pre-registered with its kill and died by it. The one-word form of the claim (refuted in frame by 49
exhaustive witnesses at n ≤ 22, 349 at n ≤ 24; never refuted out of frame in 3,581 configurations). "A lock is
where the single-swap null is zero" (false on 27 of 349). Tunnel non-recurrence along the bridge path (double
tunnels in 194 of 196 trials). Cut containment as the exit mechanism (a perfect one-directional control and no
necessity; the verb is re-route). Nine candidate potentials, including the metric of an earlier draft that measured
distance to the set of gate-phase colourings — whose nonemptiness is equivalent to the Four Colour Theorem for T,
so that every descent statement against it presupposed the theorem (Appendix C). Six-bit and 68-bit incidence
types as a classification of the lock: **purity by fragmentation is not classification** — refining a partition
raises purity because cells shrink toward singletons; on our census the 68-bit trajectory type reaches 1,259 cells
with 12 pure-locked cells carrying 29 of 401 lock instances, while the one cell every lock shares is mixed. We report
locks-in-pure-cells and the median cell size together, and we report the incidence types only as the chain of
necessary conditions they establish.

# 5. What is asserted for all n, and what is not

**Asserted for all sphere triangulations:** the One-Context Lemma; the eight chains and their identification with
Kittell's alphabet under the seed rule; Lemmas L, D, T; Theorem KP; the Arc Lemma to its one adjacency; the 22
forced bits; Lemma N; the Boundary-Term formula for the Mohar–Salas face degree under a Kempe swap on T − v
(ΔD′ = −2·S_X, every triangle meeting the chain flips; parity S_X ≡ Σ_{u∈X} deg_{T−v}(u) + |E(X) ∩ E(link)| mod 2);
Birkhoff's reductions.

**Not asserted:** any count beyond n = 24; any depth bound for all n; any mechanism for the depth-two observation;
any classification of the lock; the Four Colour Theorem. The census is not an unavoidable set (no discharging, no
claim any configuration appears in every large triangulation) and its exits are not reducibility (the chains are
global; no bounded ring confines them). The open question is Gethner et al.'s ("it is unknown if there is always a
series of Kempe–Kittell chain switches that will result in successful resolution of the impasse"), sharpened to a
bounded, fixed-seed form and given 349 witnesses of where one commutator is not enough.

# Provenance

Kempe 1879; Heawood 1890; Poussin 1896; Errera 1921; Kittell 1935, Bull. AMS 41 (the alphabet, the impasse group
of order ≥ 120, the frame-relative identities); Gethner, Kallichanda, Mentis et al. 2009, Involve 2:3 (the modern
restatement, the relettering, the open question); Mohar–Salas 2009 (the degree invariant); Tilley 2018; Feghali
2023; Florek 2025; Belavadi–Cameron 2025 (the Kempe-equivalence frontier); Bonamy et al. 2020 and Ito et al. 2022
(reconfiguration between given colourings — a different problem); Birkhoff 1913; Appel–Haken 1977;
Robertson–Sanders–Seymour–Thomas 1997 (the theorem we do not reprove and the frame we borrow); plantri 5.8
(Brinkmann–McKay). Every witness is on disk as (n, plantri index, vertex, colouring) and can be checked by hand from
the definitions.

# Appendices (slots)

**A.** The witness gallery: types, bits, cut anatomy, hashes (Grace). **B.** Instruments, hashes, plantri version,
witness formats (Elie). **C.** The metric finding: why distance-to-the-gate-phase presupposes the theorem (one page,
from the corpus artifact of 2026-09-02 08:06). **D.** The stage tables in full (L, D, T, the mirrored tree, the
letter table).
