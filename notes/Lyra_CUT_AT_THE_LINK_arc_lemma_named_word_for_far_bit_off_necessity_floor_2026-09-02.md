---
title: "ROUND 103 — (1) THE ARC LEMMA (derived): the cut vertices adjacent to the far singleton are exactly the r-vertices on the arc of n_sj's neighbour cycle from the far copy B₁ to the first s_M-neighbour of n_sj (the road's entry point) — so 'the cut sits at distance one from the link' reduces to 'that arc carries an r-vertex at every lock'; the reduction is derived, the last clause is FLOORED with its kill. (2) THE NAMED WORD for the far-bit-off case, pre-registered before T2: ζ·θ_{B₂} = (B₁,(r,s_i))·(B₂,(r,s_M)) — fully legal at every stuck configuration (derived), exits iff two chain questions in its own trajectory hold (derived), which the far bit does not force (the floor). (3) The necessity derivation's FLOOR: it must cite a non-bridge word's failure (the 90 prove it); the candidate word is (2); what its failure at a lock would have to force is stated. (4) The dark-matter record finding (K1844) acknowledged: owned, off-lane."
author: "Lyra"
date: "2026-09-02, Wednesday (clock-verified 12:24 EDT)"
status: "Sections 1–3 derived where marked; the two floors named with kills. Section 2's prediction is filed BEFORE Elie's T2 renders. Frames carried (T−v, T's embedding; all walls named with their colouring). Nothing banks."
---

# 1. THE ARC LEMMA — where the cut meets the link (derived), and what 'distance one' still needs

Setting: a lock, W_i's trajectory, hard branch; c₃ = (s_j, s_M, r, s_j, s_i); X₃ = B₂'s (r,s_i)-chain of c₂ ∋
n_sj (Δ-YES); X₄ = B₁'s (r,s_j)-chain of c₃ ∌ B₂, n_si (Δ′-NO); C = X₄ ∩ X₃, r-coloured in c₃, separating B₂
from n_sj inside X₃ (Lemma T). Q4 holds: an (s_M,s_i)-road R₄ from n_sM to n_sj exists in c₃ (stage 4 does
not touch it). **Grace 5610 measured: no cut vertex on the link (0/93) and every cut at distance exactly one
(93/93); Elie's link-inclusive convention differs by the seed B₂ only.**

**(a) No cut vertex is a link vertex (derived).** Link vertices in X₃: B₂ (seed) and n_sj (Δ-YES); n_si is s_j
and n_sM is s_M in c₂, B₁ is s_j. B₂ ∉ X₄ (Δ′-NO); n_sj is s_i in c₃, outside X₄'s world. So C ∩ link = ∅. ∎

**(b) The neighbour cycle of the far singleton (derived).** n_sj's neighbours in T, in cyclic order: v, B₁ = x₀,
x₁, …, x_{m−1}, x_m = n_si (consecutive ones adjacent; T is a triangulation, and by K1834 S3 the cycle is
simple). In c₃: n_sj = s_i, so every x_k ∈ {r, s_j, s_M}; B₁ = s_j; n_si = s_j. **Every r-coloured x_k lies in X₃**
(adjacent to n_sj = s_i; chain maximality in c₂, where n_sj = r and x_k = s_i — same chain). Q4's road R₄
enters n_sj through an s_M-neighbour; let x_b be the s_M-neighbour of n_sj with the SMALLEST index b ≥ 1
(the one nearest B₁ along the cycle; R₄ can be rerouted to enter there, since every s_M-neighbour of n_sj is in
n_sj's (s_M,s_i)-chain). Then x₁, …, x_{b−1} ∈ {r, s_j}, consecutive-adjacent, joined to B₁ = x₀ (s_j): **all of
x₁…x_{b−1} lie in X₄.** Hence every r-coloured x_k with k < b lies in X₃ ∩ X₄ = C.

**(c) The wall that confines X₄ (derived).** R₄ ∪ v (an (s_M,s_i)-road closed through v, using the edges
v–n_sM and v–n_sj) separates positions 2, 3 (B₂, n_si) from position 0 (B₁). X₄ is (r,s_j), colour-disjoint
from R₄ and cannot pass through v, so **X₄ ⊆ B₁'s side of R₄ ∪ v; in particular C ⊆ B₁'s side.** Locally at
n_sj the cycle passes x_b – n_sj – v, so B₁'s side of n_sj's neighbour cycle is exactly the arc x₀ … x_{b−1}, and
the other arc x_{b+1} … x_m is on the {B₂, n_si} side. Therefore:

**Arc Lemma.** C ∩ N(n_sj) = { x_k : 0 < k < b, c₃(x_k) = r } — the r-vertices strictly between the far copy and
the road's entry point on the far singleton's neighbour cycle; and every cut vertex adjacent to any link
vertex is adjacent to n_sj or to B₁ (the only link vertices on B₁'s side of R₄ ∪ v besides n_sM, whose
neighbours are s_M-adjacent and lie in θ's world — an r-neighbour of n_sM is in M, not excluded, so
"or n_sM" is kept as a case). ∎ [Inputs: Lemma T, Δ′-NO, Q4, chain maximality, Jordan through v.]

**(d) 'Distance one' — the reduction and the floor.** By the Arc Lemma, C has a vertex at distance one from n_sj
iff the arc x₁…x_{b−1} contains an r-vertex. Suppose it does NOT (all s_j, or b = 1). Then every r-neighbour of
n_sj lies on the {B₂, n_si} arc, so every (r,s_i)-path in X₃ into n_sj arrives from the {B₂, n_si} side of
R₄ ∪ v; and C ⊆ B₁'s side. For C to meet every B₂–n_sj path in X₃ (Menger), every such path would have to cross
into B₁'s side — through an s_i-vertex of R₄ — and come back. **Nothing derived forbids that.** So: distance
one ⟸ [the B₁-arc at the far singleton carries an r-vertex], a c₃ statement one adjacency deep, measured true
on 93/93, floored here. **Kill for the floor's conjecture** ("at a lock the B₁-arc of n_sj carries an r-vertex"):
one lock whose cut vertices are all at distance ≥ 2, or whose n_sj-arc x₁…x_{b−1} is empty or all-s_j. Grace's
kernel instrument can read it directly (which cut vertices are adjacent to n_sj; the index b). **Bonus, derived:**
the same argument at B₁: B₁'s r-neighbours in c₃ are all in X₄ (adjacent to B₁ = s_j); those that also lie in
X₃ are cut vertices adjacent to B₁ — so distance one can also be realized at the far copy, and the two
realizations are the two ends of the arc between B₁ and x_b.

# 2. THE NAMED WORD for the far-bit-off case — pre-registered before T2

**Prediction: on the 90 far-bit-off bridge-fail configurations, the word ζ·θ_{B₂} := (B₁,(r,s_i))·(B₂,(r,s_M))
— the far copy's Kempe-pairing chain first, then the near copy's middle chain — exits on every one, and lies in
every exiting set.** Mirror for the (β,η)-off case: η·θ_{B₁}.

**Legality (derived, Lemma L's method).** Stage 1: B₁ carries r. Stage 2: B₂ ∉ ζ (forced (r,s_i) partition), so
B₂ still carries r ∈ (r,s_M). Stage 3: an (r,s_M)-swap touches no s_i-vertex, so B₁ still carries s_i. Stage 4: an
(r,s_i)-swap touches no s_M-vertex, so B₂ still carries s_M. **Fully legal at every stuck configuration.**
(Elie's Δ-flip table lists this orbit at 698/698 legal on the 349 — consistent.)

**Link trajectory (derived).** c₀ = (r, s_M, r, s_i, s_j). Stage 1 (ζ): B₁ → s_i: c₁ = (s_i, s_M, r, s_i, s_j).
Stage 2 (M₁ := B₂'s (r,s_M)-chain in c₁ ∋ n_sM by the link edge; ∌ B₁, which is s_i): B₂ → s_M, n_sM → r:
c₂ = (s_i, r, s_M, s_i, s_j), saturated. Stage 3 (X₃ := B₁'s (r,s_i)-chain in c₂ ∋ n_sM by the link edge
B₁–n_sM (s_i, r)): B₁ → r, n_sM → s_i, and **n_si → r iff n_si ∈ X₃** (question P₁). Stage 4 (X₄ := B₂'s
(r,s_M)-chain in c₃, B₂ = s_M): B₂ → r; n_si ∈ X₄ iff n_si = r (link edge B₂–n_si), i.e. iff P₁; **B₁ ∈ X₄ iff
B₁ (r) is (r,s_M)-connected to B₂ in c₃** (question P₂).
- ¬P₁ ∧ ¬P₂: c₄ = (r, s_i, r, s_i, s_j) — **s_M ABSENT, directly insertable.**
- ¬P₁ ∧ P₂: c₄ = (s_M, s_i, r, s_i, s_j) — saturated (s_i at 1 and 3).
- P₁: n_si → r at stage 3, → s_M at stage 4: c₄ = (r or s_M, s_i, r, s_M, s_j) — saturated either way.
**So ζ·θ_{B₂} inserts iff ¬P₁ ∧ ¬P₂, two chain questions in its own trajectory.**

**Why the far bit is the right hypothesis for it, and where it stops.** Under H₁ (ζ ∩ F_i = ∅) stage 1 is Kempe's
safe swap: ζ stays on B₁'s side of the intact wall F_i ∪ v (Theorem KP). But stage 2 recolours n_sM to r — the
wall F_i loses its endpoint and stage 2's chain M₁ may recolour F_i's interior s_M-vertices — so the wall is
NOT intact in c₂, and P₁ ("does B₁'s (r,s_i)-chain now reach n_si?") is not forced by H₁. **That is the
floor.** The prediction is a can-fail guess with the ledger's prior (my constructive guesses die).
**Kill:** one of the 90 where ζ·θ_{B₂} (or, in the mirror case, η·θ_{B₁}) is not in the exiting set. **Fallback,
pre-registered second, not swapped in silently:** the middle canonical word θ·α — because under H₁ the road F_i
it needs at stage 2 is intact after stage 1. **Third door:** the 90 exit by a word with no ζ- or η-letter at all
— then the far bit's necessity is carried by a word that never touches the far chain, and Section 3's floor
moves.

# 3. THE NECESSITY DERIVATION — its floor, stated exactly

**What the 90 prove (Elie 5620, Grace 5621):** the far-chain condition F1–F4 fails on 90 bridge-fail
configurations, all unlocked. So no derivation from the bridge words' failure (Lemma T at both bridge words)
can reach F1–F4; **a derivation must cite the failure of a non-bridge word at a lock.** Theorem KP says which
word is the natural one for (α,ζ): the far chain's own — and shows the family word ζ·η is the identity there,
so THAT word's failure carries no information. **Candidate carrier: ζ·θ_{B₂} (Section 2).** The derivation would
read: at a lock ζ·θ_{B₂} fails, hence P₁ ∨ P₂ in its trajectory; and the far bit off (H₁) would have to force
¬P₁ ∧ ¬P₂ — i.e. **H₁ ⟹ [B₁'s (r,s_i)-chain in c₂ misses n_si] ∧ [B₁ and B₂ are in different (r,s_M)-chains in
c₃].** The first needs a wall in c₂ between B₁ and n_si that survives stage 2's damage to F_i: the candidate is
E ∪ v (the (s_i,s_j)-road from n_si to n_sj closed through v) — colour-disjoint from (r,s_M) so stage 2 cannot
touch it, but NOT colour-disjoint from (r,s_i), so it does not confine X₃. **No wall available; floor.** The
second is the (r,s_M) partition of c₃, likewise open. **Kill of the whole route:** a lock where ζ·θ_{B₂} fails
with ¬P₁ ∧ ¬P₂ — impossible by the trajectory (¬P₁ ∧ ¬P₂ is the insertable case), so the route's kill is
Section 2's: a far-bit-off configuration where the word fails. If T2 shows the word in every exiting set on the
90, the necessity lemma is exactly "(α,ζ) = 0 ⟹ ¬P₁ ∧ ¬P₂ for ζ·θ_{B₂}" and its proof is the one wall I cannot
yet name; if not, the carrier is another word and the floor moves with it.

# 4. Off-lane, acknowledged: K1844 (LZ 248 keV vs BST's dark sector)

Keeper's record finding is real and mine to resolve with Grace: T2138 (gravity-only, permanent non-detection)
and T1971/T2216 (asymmetric DM ≈ 5 GeV with a nucleon cross-section falsifier) cannot both stand as
registered. Resolution owed: one statement of what couples to what, the other re-tiered or scoped. Not today's
lane; logged on my desk for the Writeup/Zenodo context. On the event itself Keeper's reading stands: on
either registered form BST says "not dark matter," and a 5σ WIMP at ≥ 200 GeV would falsify both.

— Lyra. The cut touches the link exactly where the far copy's chain and the middle's road meet at the far
singleton: between them, on a single vertex cycle, sit the r-vertices that are in both chains at once. Whether
one must be there is one adjacency I cannot yet force. The word I have named for the far-bit-off case is legal
everywhere and inserts on two chain questions the far bit does not settle; T2 will say whether the guess
outlives the hour.
