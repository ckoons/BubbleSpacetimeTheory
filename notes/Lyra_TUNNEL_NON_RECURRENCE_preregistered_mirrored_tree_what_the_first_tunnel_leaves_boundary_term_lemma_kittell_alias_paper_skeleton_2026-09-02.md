---
title: "TUNNEL NON-RECURRENCE — LINE ONE: NOT DERIVED. What is derived: the mirrored tree at a stuck leaf with frames carried (the second image's link word is the ORIGINAL word), the exact residue of the first tunnel (the cut K survives two stages unchanged; the fence is demolished at K and at B₂'s side), the necessary conditions for a second tunnel, and one commutation fact (stages 4 and 1′ are disjoint chains and commute). The KILL and the THIRD DOOR pre-registered before Elie's depth curve at n = 23–24. Plus: the Boundary-Term Lemma for Grace's grade test (T2594), the Kittell Alias Theorem as a theorem (T2593), and a one-page paper skeleton for Casey's desk."
author: "Lyra"
date: "2026-09-02, Wednesday (clock-verified 09:43 EDT)"
status: "Round 98 deliverable. Sections 1–3 derived (frames carried at every node); Section 4 is a pre-registration filed BEFORE contact with the 49's second-word data or the n = 23–24 depth curve; Section 5 derived (two-line orientation bookkeeping, positive control owed); Section 6 the alias theorem; Section 7 the skeleton. Registered this hour: T2590 (Lemma T), T2591 (L), T2592 (D), T2593 (Kittell alias), T2594 (Boundary term). Nothing banks."
---

# 0. Line one

**Tunnel Non-Recurrence (TNR) is not derived in this artifact.** The statement is stated exactly, its
four exits are named, what the first tunnel leaves behind is derived exactly, and the second tunnel's
necessary conditions are derived — but no contradiction between them closes. The measured fact (depth 3
= 0 on 374,658 in-frame stuck colorings) is evidence for TNR and for nothing stronger; it does not tell us
the second word that exits is the mirror word (Lane B decides that, and TNR is a statement about the
mirror word specifically). Per the rule of the day the kill and the third door are pre-registered in
Section 4 before any count reaches me.

# 1. The mirrored tree at a stuck leaf (derived; every node in T−v with T's embedding)

Let c₄ = (r, s_M, r, s_j, s_i) be a stuck leaf of W_i (Δ-YES ∧ Δ′-NO ∧ Q3 ∧ Q4). Frame of c₄: copies B₁ (0),
B₂ (2); middle n_sM; singleton adjacent to B₂ is n_si (position 3, color s_j); singleton adjacent to B₁ is
n_sj (position 4, color s_i). The bridge-anchored word in this frame is **W′ := (B₂,(r,s_j))·(B₁,(r,s_i))**
(each copy with the pair of the singleton it touches). Lemma L and Lemma D apply with i↔j (their proofs use
only the forced partitions, which c₄ has by stuckness, and color-world disjointness). Writing Y_k for the
chain swapped at stage k′ and c₄₊ₖ for the image:

- **Stage 1′.** Y₁ = B₂'s (r,s_j)-chain in c₄ ∋ n_si (edge 2–3), ∌ B₁ (Q1). c₅ = (r, s_M, s_j, r, s_i).
- **Stage 2′.** Y₂ = B₁'s (r,s_i)-chain in c₅ ∋ n_sj (edge 0–4: r,s_i), ∋ n_si (edge 3–4: r,s_i). Swap B₁ → s_i,
  n_sj → r, n_si → s_i. c₆ = (s_i, s_M, s_j, s_i, r). Saturated; the two-stage prefix never inserts.
- **Stage 3′.** Y₃ = B₂'s (r,s_j)-chain in c₆ (B₂ = s_j). **Δ₂: n_sj ∈ Y₃?**
  - Δ₂-NO → c₇ = (s_i, s_M, r, s_i, r): **s_j absent** (leaf I at the prefix); stage 4′'s chain is forced through
    the three bichromatic link edges to contain {B₁, n_sj, n_si, B₂}; c₈ = (r, s_M, s_i, r, s_i): **s_j absent.
    Leaf I at the word image.**
  - Δ₂-YES → c₇ = (s_i, s_M, r, s_i, s_j), saturated; second wall W₂ := P₂ ∪ v, P₂ ⊆ Y₃ an (r,s_j)-path B₂ → n_sj
    in c₆; it separates n_si (3) from {B₁, n_sM} for (s_M,s_i)-paths.
    - **Stage 4′.** Y₄ = B₁'s (r,s_i)-chain in c₇ (B₁ = s_i). **Δ₂′: {B₂, n_si} ⊆ Y₄?** YES → τ(c₇) ≤ 5 (Cal §819's
      planarity line, mirrored: the B₁–n_si (r,s_i)-path closed through v separates n_sM from n_sj, so the
      (s_M,s_j)-chain at n_sM misses n_sj; swap it: s_M absent). Leaf G at the prefix.
    - Δ₂′-NO → **c₈ = (r, s_M, r, s_i, s_j) — the ORIGINAL link word c₀.** By Lemma T mirrored: stuck iff
      **Q3₂ (n_sM ~ n_si in (s_M,s_i)) ∧ Q4₂ (n_sM ~ n_sj in (s_M,s_j))**, with Q4₂ decided in c₇ and Q3₂
      requiring the tunneling cut K₂ := Y₄ ∩ r(Y₃) to separate B₂ from n_sj inside Y₃.

**TNR, stated exactly:** if c₄ is a stuck leaf of W_i via a tunnel, then c₈ = W′·c₄ is not a stuck leaf via a
tunnel — i.e. at least one of {Δ₂-NO, Δ₂′-YES, ¬Q3₂, ¬Q4₂} holds. **Note what a double tunnel would be:** an
8-swap word returning the link to its ORIGINAL word with all six template partitions restored — a stuck
configuration in the original frame, two commutators later. That is the object Elie's depth-3 search hunts.

# 2. What the first tunnel leaves behind (derived)

Let K := X₄ ∩ X₃ (the first cut; r-colored in c₃; separates B₂ from n_sj inside X₃; K ∩ {B₂, n_si} = ∅).
- **(R1) K is s_j in c₄ and lies in X₄'s (r,s_j)-chain, not in Y₁'s.** Stage 4 recolored K. In c₄, B₁'s
  (r,s_j)-chain is X₄ as a set; B₂'s is Y₁; they are distinct (Q1). So K ∩ Y₁ = ∅.
- **(R2) K survives stages 1′ and 2′ unchanged.** Stage 1′ swaps Y₁ (K ∉ Y₁); stage 2′ is an (r,s_i)-swap
  (K is s_j). So in c₆, K is still s_j and still adjacent, on its B₂-side, to the r-vertices of X₃ that
  stage 1′ did not recolor, and on its n_sj-side to X₃'s r-vertices there (untouched by 1′ unless in Y₁,
  untouched by 2′ unless in Y₂ — and X₃'s r-vertices in Y₂ turned s_i).
- **(R3) The fence is demolished twice.** P (the first wall, (r,s_i) in c₃) loses K at stage 4 (→ s_j), and
  loses its r-vertices in Y₁ — B₂ among them — at stage 1′ (→ s_j). What remains (r,s_i)-colored of P in
  c₆ is P ∖ (K ∪ Y₁), and stage 2′ then flips P's remaining r-vertices in Y₂ to s_i and its s_i-vertices in
  Y₂ to r (n_sj among the latter).
- **(R4) Stages 4 and 1′ commute.** X₄ and Y₁ are distinct (r,s_j)-chains of c₃/c₄ (Δ′-NO ⟺ Q1), so swapping
  them in either order is the simultaneous swap of two disjoint chains. Hence W′·W_i·c₀ = Y₄ Y₃ Y₂ (X₄Y₁) X₃ X₂
  X₁ · c₀ with (X₄Y₁) one double swap: the 8-swap composite has a 7-block normal form. Whether the block
  structure yields anything is open; it is the first algebraic fact about the composite.
- **(R5) The (r,s_j)-world of c₆ relative to c₄.** It differs from c₄'s exactly by: Y₁ recolored in place
  (same vertex set); B₁, n_si and every other old-r vertex of Y₂ REMOVED (→ s_i); every old-s_i vertex of Y₂
  ADDED (→ r), n_sj among them. Nothing else moves.

**Necessary conditions for a second tunnel (derived from R1–R5):**
- **(N1) Δ₂-YES needs a bridge built from Y₂'s old-s_i vertices.** In c₄, B₂'s (r,s_j)-chain Y₁ and the
  chain X₄ ∋ K are distinct, and n_sj is outside the world. In c₆ an (r,s_j)-path from B₂ (∈ Y₁) to n_sj must
  therefore leave Y₁ and enter material that was not (r,s_j)-connected to Y₁ in c₄ — and by R5 the only new
  connective tissue is Y₂'s old-s_i vertices turned r. So P₂ contains an old-s_i vertex u of Y₂ adjacent to
  Y₁-material (or u = n_sj itself adjacent to a Y₁ vertex). In words: **the second tunnel's reconnection is
  built from the far copy's (r,s_i)-chain of c₅, exactly as the first was built from X₂'s old-s_j vertices.**
- **(N2) K₂ must cut Y₃ at r-vertices avoiding B₂ and n_si** (Δ₂′-NO), while Y₄ = B₁'s (r,s_i)-chain in c₇ —
  B₁ now s_i, its link neighbours n_sM (s_M) and n_sj (s_j in c₇) both outside the (r,s_i)-world — so Y₄ leaves
  the link only through B₁'s interior (r,s_i)-neighbours.
- **(N3) Q4₂ needs an (s_M,s_j)-road n_sM → n_sj in c₇.** The (s_M,s_j)-world of c₇ relative to c₄: Y₁'s old-s_j
  (n_si among them) removed and its old-r (B₂ among them) added at 1′; Y₃'s old-s_j removed and old-r added
  (n_sj among them, under Δ₂-YES) at 3′. The first road R₃ (n_sM → n_si through K, Q3) loses n_si at 1′; so
  Q4₂'s road must reach n_sj by a route that did not exist in c₄ at n_sj (n_sj was s_i there).
- **(N4) Q3₂ needs an (s_M,s_i)-road n_sM → n_si in c₈** crossing W₂ at a vertex of K₂; and Q4 (the first
  leaf's (s_M,s_i)-road n_sM → n_sj) is reshaped only by stage 2′ and 4′, which remove Y₂'s and Y₄'s old-s_i
  (n_sj at 2′) and add their old-r.

No pair of N1–N4 contradicts; the derivation floors here. **The likeliest closing route, named for the next
session:** N1 + R1 — the second bridge must be built from Y₂, and Y₂ is B₁'s (r,s_i)-chain in c₅, which by Q2
(c₄) does not contain B₂ and by the first cut's geometry sits on n_sj's side of K. A Jordan argument that
Y₂'s old-s_i material cannot reach Y₁ without crossing the demolished fence's remnant would close Δ₂-NO; the
remnant is (r,s_i)-colored in c₅ only on P ∖ (K ∪ Y₁), so the argument needs that remnant, plus v, to still
separate. It does not obviously do so. That is the honest floor.

# 3. Frames (the check the order demanded at every node)

Every chain above is a chain of a proper coloring of T−v with T's embedding present. One-Context is
invoked in c₄'s frame only through Lemma T (already frame-checked, Cal §819 on the c₃ analogue). No
H-frame, no contraction, no edge added; the link is v's link cycle in T throughout; 5-connectivity unused
(Cal's induced-link corollary is available: no chord between non-consecutive link vertices).

# 4. PRE-REGISTRATION — the kill, the third door, and what each outcome means (filed before contact)

**Claim under test:** TNR — at every stuck leaf c₄ of W_i (or W_j), the mirror word W′ in c₄'s frame does
not produce a stuck leaf via a tunnel.

**Kill condition (K-TNR):** one configuration c₀ (any frame; in-frame preferred) with W_i·c₀ = c₄ stuck via
the tunnel signature (K ≠ ∅ separating, Grace's 5603 test) AND W′·c₄ = c₈ stuck via the tunnel signature
(K₂ ≠ ∅ separating). Two instruments (Elie BFS/union-find; Grace rank). One instance kills TNR outright.
Existence check already run in one direction: depth 3 = 0 on 374,658 means no in-frame c₀ needs three
words — which implies K-TNR cannot fire on any in-frame c₀ at n ≤ 22 ONLY IF the depth-2 exit is W′ itself
(Lane B). If Lane B shows exits by other words, K-TNR remains untested at n ≤ 22.

**Third door (D-TNR):** W′·c₄ is stuck but NOT via a tunnel — i.e. c₈ stuck with Q3₂ ∧ Q4₂ but the cut K₂
empty or non-separating. Lemma T mirrored says Q3₂ forces a separating cut, so D-TNR would be a theorem
error in Lemma T or a labeling bug; it re-opens T2590 at once (positive control on the derivation, Cal's
three-label rule).

**Fourth exit, named so it is not a surprise (A-TNR, alphabet dependence):** TNR holds (W′ never recurs)
but the depth-2 exits on the 49 are NOT by W′ — the second word ranges over other orbits. Then the two-word
statement is alphabet-dependent in the way the one-word one was (the in-frame hitting-set growth 1·2·8·4·6·
9·14 already points here), TNR is true-but-not-the-mechanism, and the derivation target moves to "which
second word, and why."

**Pre-score:** K-TNR fires → TNR dead, depth-3 witness in hand, Lane A closed, the successor object is at
least a three-word reach (a kill, never a menu amendment). K-TNR silent at 23–24 AND Lane B says exit = W′
→ TNR is the derivation target with a clean existence check behind it. A-TNR → the object is the second
word's identity, not recurrence.

# 5. THE BOUNDARY-TERM LEMMA (T2594) — for Grace's grade candidate (i)

Fix an orientation of the sphere and the boundary orientation of the tetrahedron on the four colors:
∂[1,2,3,4] = [2,3,4] − [1,3,4] + [1,2,4] − [1,2,3], so the face opposite color x carries the induced
orientation, and **two faces sharing an edge traverse it in opposite directions.** For a triangle t of T−v
(the pentagon excluded) with colors (a,b,c) read in the positive sense, z_t := +1 if (a,b,c) is the
orientation of the tetrahedron face {a,b,c}, else −1. D′(c) := Σ_t z_t. (On a closed triangulation
Σ_t z_t = 4·deg — each color face covered deg times — and deg mod 12 is Mohar–Salas's invariant on the
Eulerian class.)

**Lemma.** Under an (a,b)-swap on a chain X in T−v, every triangle meeting X flips its sign and no other
triangle changes:
  **ΔD′ = −2·S_X, S_X := Σ_{t ⊂ T−v, t ∩ X ≠ ∅} z_t.**
*Proof.* A triangle not meeting X is unchanged. A triangle with an a-vertex and a b-vertex: both are in X
(adjacent a,b vertices share the (a,b)-chain), the swap exchanges their colors, so the cyclic color order
around t reverses: z_t → −z_t. A triangle with exactly one X-vertex, colored a, and two others colored c, d
∉ {a,b}: before, t maps to the face {a,c,d} (opposite b); after, to {b,c,d} (opposite a); these two faces
share the edge cd and traverse it in opposite directions, while t's own orientation traverses cd the same
way both times; so z_t → −z_t. ∎ (Agrees with the corpus's Straddle-Flip, 08-30: Δdeg = −½·Σ_straddle z_t
with "straddle" = every face meeting X.)

**Vertex-charge form (for the instrument):** c_u := Σ_{t ∋ u} z_t. Around u colored a the neighbours cycle
through the other three colors; each consecutive pair (x,y) contributes ±1 by whether x→y is a forward step
in the cyclic order of the face opposite a; so **c_u = 3·w_u**, w_u the winding number of u's neighbour
colors around the color triangle. Deg 4: w = 0. Deg 5: 3w odd with |3w| ≤ 5 ⟹ w = ±1, c = ±3. Deg 6:
c ∈ {0, ±6}. Then S_X = Σ_{u∈X} c_u − E_X, E_X := Σ_{t ⊇ an X-edge} z_t (faces containing an a–b edge of X
are counted twice in the vertex sum; each such face contains exactly one X-edge).

**The boundary term.** For a link vertex n_k ∈ X the two triangles {v, n_{k±1}, n_k} of T are absent from
T−v, so c_{n_k} is a three-face sum (degree 5 in T, three faces in T−v) and is NOT quantized to ±3. Writing
D(T; e) for the closed degree sum with v assigned color e, **D′(T−v) = D(T; e) − Σ_{k} z_{v n_k n_{k+1}}(e)**,
which makes any closed-surface comparison well-defined once e is chosen; the intrinsic T−v formula
ΔD′ = −2·S_X needs no choice. **Parity [CORRECTED 11:32, Cal §821]:** #faces meeting X = Σ_{u∈X} deg_{T−v}(u) − 2|E(X)| + |E(X) ∩ E(link)| (a link edge lies in one triangle of T−v), so S_X ≡ Σ_{u∈X} deg_{T−v}(u) + |E(X) ∩ E(link)| (mod 2).

**Positive control for Grace (before any grade is read):** ΔD′ = −2·S_X must hold EXACTLY on every legal
swap of every configuration in the census; one miss is a bug in the orientation convention (the face-
opposite-x rule and the sphere's orientation must be fixed once) or in this lemma. Then the grade test:
D′-distance between the 49 and the matched depth-1 sample, reported as separation counts.

# 6. THE KITTELL ALIAS THEOREM (T2593) — statement

At every stuck configuration of a sphere triangulation, the fifteen link-seeded moves name exactly eight
distinct Kempe chains, and they are Kittell's eight (Kittell 1935; Gethner et al. 2009, Definition 5):
θ = M (r,s_M) · α = F_i · β = F_j · ε = E · γ = B₁'s (r,s_j) ∋ n_sj · δ = B₂'s (r,s_i) ∋ n_si · ζ@v₁ = B₁'s
(r,s_i) · η@v₃ = B₂'s (r,s_j), under G,R,G,B,Y = r,s_M,r,s_i,s_j with v₁ = B₁, v₃ = B₂, v₄ = n_si, v₅ = n_sj.
*Proof.* The six forced partitions (One-Context) decide when two seeds name one chain: the two split
bridge pairs contribute two chains each, the other four pairs one each; 2+2+1+1+1+1 = 8. Matching Gethner's
list letter by letter is Section 6 of the Dichotomy Tree artifact. ∎ Measured 2,927/2,927 (Grace 5599).
Corollaries: 186 words = 52 chain-commutators (26 mod mirror); impasse = τ_v = 6; the field's open **[SWEEP 2026-09-02 11:32, Cal §821: the "52 chain-commutators = compression by identity" clause is STRUCK — 186 seed-words PROJECT onto 52 stage-1 chain pairs; seed-words over one pair can differ from stage 3 on. The seed rule (ζ@v₁, η@v₃) is part of the alias statement; with the other seeds Kittell's list names six chains.]**
question is the unbounded form of ours; the novelty is the shape, never the alphabet.

# 7. ONE-PAGE PAPER SKELETON (for Casey's desk; K1839 §5's shape; decide after n = 23–24)

**Title (working):** *Kempe's commutators at a degree-five vertex: forced chains, a dichotomy tree, and an
exhaustive census on 5-connected triangulations through 22 vertices.*
**Abstract (five sentences, no 4CT claim):** At a stuck degree-5 vertex of a 4-colored sphere triangulation
minus that vertex, the eight Kempe chains meeting the link are forced up to symmetry (One-Context) and
coincide with Kittell's 1935 switches. Composing two of the non-freeing chains as a four-swap commutator
is always legal (Lemma L) and its outcome is decided by one chain-coincidence question (Lemma D); on the
hard branch the image is stuck iff two singleton–middle chain questions hold (Lemma T), and the stuck case
carries a tunneling signature. An exhaustive census of every stuck coloring at every degree-5 vertex of
every 5-connected triangulation with at most 22 vertices (374,658 colorings mod S₄) finds that one
commutator reaches the gate phase in all but 49 cases and two commutators in all cases; no case needs
three. The one-commutator statement is therefore false and the two-commutator statement is open; we state
it as the bounded form of Kittell's question and give the 49 witnesses. Nothing here bears on the
four-color theorem beyond restating what a bounded Kempe method would need.
**Sections:** 1 Setting and Kittell's alphabet (T2593) · 2 The forced context (One-Context; Lemmas 2–3
re-derived) · 3 The commutator (L, D, T; the wall; the tunnel) · 4 The census (frame = 5-connected;
plantri; two instruments; the 49; hitting-set curve) · 5 What is open (two-word reach; non-recurrence;
grade) · 6 Non-claims. **Appendix:** the metric finding (why descent-to-the-gate-phase presupposes 4CT),
one page, because a referee will ask.
**Referee's first question (Cal's outside-voice prompt, my guess):** "Why should depth two persist past
22?" — answered only by n = 23–24 and by a mechanism; until then the paper says "through 22."

— Lyra. The first tunnel leaves a cut that survives two stages and a fence broken in two places; a second
tunnel must be built from the far copy's chain on the far side of that cut. I can see the shape of the
Jordan argument that says it cannot; I cannot yet write it. The pre-registration says what would prove me
wrong before anyone looks.
