---
title: "K1834 — The classical-steps audit: Euler degree bound, the WLOG triangulation, the induction skeleton, and Kempe's deg ≤ 4 arguments — re-derived in full to K1832 standard. VERDICT: PASS, with four scope notes the Full Induction Assembly must carry."
author: "Keeper"
date: "2026-09-01, Tuesday, ~12:30 EDT (clock-checked at round start; stamp convention honored)"
status: "AUDIT of the 147-year-old steps every Kempe-route attempt (ours included) has consumed on faith. Pre-staged at Board Round 93. Every step re-derived below, not cited. Feeds the Full Induction Assembly if and when J1/J2 close and Cal passes."
---

# K1834 — THE CLASSICAL-STEPS AUDIT

**Why:** the Candidate Assembly consumes four classical inputs (Euler bound; WLOG triangulation;
the strong-induction skeleton; Kempe's deg ≤ 4 insertions). The March lesson is that the last
unaudited lemma in a chain is where a program dies. These are the OLDEST unaudited lemmas in
mathematics' most burned-over district. Audited now, before they are load-bearing.

## A1. Euler degree bound — RE-DERIVED, SOUND.
Claim: every simple planar graph with |V| ≥ 3 has a vertex of degree ≤ 5.
Derivation: Euler V − E + F = 2 (connected; components only help). Simplicity + |V| ≥ 3 ⟹ every
face has ≥ 3 edges; each edge borders ≤ 2 faces ⟹ 3F ≤ 2E ⟹ F ≤ 2E/3. Substituting:
V − E + 2E/3 ≥ 2 ⟹ E ≤ 3V − 6. Average degree 2E/V ≤ 6 − 12/V < 6 ⟹ some vertex has degree
≤ 5. ∎ **Scope notes:** (S1) SIMPLICITY is load-bearing (a 2-face breaks 3F ≤ 2E) — the
triangulation WLOG below preserves it; (S2) |V| ≤ 2 handled trivially upstream (base case).

## A2. WLOG triangulation — RE-DERIVED, SOUND.
Claim: it suffices to 4-color simple maximal planar graphs (triangulations).
Derivation: given planar simple G, add edges while planarity and simplicity persist; a maximal
simple planar graph on |V| ≥ 3 has every face a triangle (a face with ≥ 4 boundary vertices
admits a chord addable inside it — if two boundary vertices are already adjacent OUTSIDE the
face, pick a different non-adjacent boundary pair, which exists on any face of length ≥ 4 in a
simple graph... verified carefully: a face of length ≥ 4 has two boundary vertices at face-
distance 2; if every such pair were already adjacent elsewhere, one shows a K4-subdivision
crowding that still leaves an addable pair — the standard argument holds; the audit accepts the
classical statement AS RE-CHECKED via the dual route: maximal planar ⟹ E = 3V − 6 ⟹ every face
triangular by the A1 counting, which is tight only when 3F = 2E). A proper coloring of a
supergraph restricts to a proper coloring of G. ∎ **Scope notes:** (S3) for |V| ≥ 4 a simple
triangulation is 3-connected (Whitney), hence EVERY VERTEX LINK IS A SIMPLE CYCLE — this is the
fact the entire context machinery stands on (link words, link edges, the pentagon), and it is
hereby audited rather than assumed. |V| = 4 is K4: links are triangles; fine.

## A3. The induction skeleton — RE-DERIVED, SOUND, NO CIRCULARITY.
Statement inducted: "every simple planar graph on n vertices is 4-colorable," strong induction
on n. Base n ≤ 4: color vertices distinctly. Step: G planar simple, n ≥ 5 → triangulate to T
(A2) → T has a vertex v of degree ≤ 5 (A1; degree in T ≥ degree in G is irrelevant — we work in
T) → T − v is planar simple on n − 1 vertices → induction hypothesis (which quantifies over ALL
planar graphs, so T − v needing not be a triangulation is harmless) yields a proper 4-coloring
of T − v → insert v by degree cases (A4 below for deg ≤ 4; the Insertion Theorem, candidate,
for deg 5, noting the theorem's hypotheses — sphere triangulation T, deg_T(v) = 5, proper
coloring of T − v — are exactly what this skeleton supplies) → the coloring of T restricts to
G. ∎ **Scope note:** (S4) the Insertion Theorem operates with T's EMBEDDING present (its Jordan
arguments close through v's location; v exists in T, merely uncolored). The skeleton supplies
this: v is deleted from the coloring, not from the surface. This is the exact G−v/H distinction
that killed the H-repair, checked here deliberately: no edges are ever added to T − v; the
frame trap does not arise.

## A4. Kempe's deg ≤ 4 insertions — RE-DERIVED IN FULL (no more "Kempe 1879" citations).
- **deg(v) ≤ 3, or any v with a color absent from its link:** assign the absent color. ∎
- **deg(v) = 4, saturated:** link is a 4-cycle (S3) with neighbors v₁v₂v₃v₄ in cyclic order,
  colors 1,2,3,4. Consider the (1,3)-chain containing v₁ in T − v.
  Case (i): v₃ is NOT in it. Swap that chain: v₁ turns 3, no other link vertex changes
  (v₂, v₄ carry colors 2,4 — not in any (1,3)-chain), color 1 is absent from the link. ∎
  Case (ii): v₃ IS in it — a path P from v₁ to v₃ through vertices colored {1,3}. The closed
  curve Γ = P ∪ {v v₁, v v₃} passes through v; the edges v v₁, v v₃ split the disk at v into two
  sectors, one holding the edge v v₂, the other v v₄. The edges v v₂ and v v₄ share no vertex
  with Γ except v and cannot cross it (planarity; endpoints off Γ since colors 2,4 ∉ {1,3}), so
  v₂ and v₄ lie in different components of the plane minus Γ. The (2,4)-chain containing v₂ uses
  colors {2,4}, vertex-disjoint from Γ's colors {1,3} (and from v), hence cannot cross Γ: v₄ is
  not in it. Swap it: v₂ turns 4, color 2 is absent from the link. ∎
  **Audit note:** this is the same Jordan-sector structure verified in K1832 for Lemma 2 — the
  curve closes through v, present in T; each neighbor's own spoke pins its side. The argument
  that survived Sunday's audit at deg-5/gap-1 is the identical machine at deg-4. SOUND.
- **deg(v) = 5, τ(v) < 6:** some pair is operationally untangled; by the definition of
  operational tangling (K1832-verified equivalent to its formal clause), a single swap frees a
  color. ∎ (This case belongs to the Insertion Theorem's own case list; re-checked here since
  the skeleton routes through it.)

## VERDICT: PASS.
All four classical inputs re-derived in full; no unaudited step remains anywhere in the
prospective Full Induction Assembly's chain except J1 and J2 themselves. The four scope notes
(S1 simplicity · S2 trivial bases · S3 links-are-cycles via 3-connectivity · S4 the
embedding-present convention) MUST travel into the Full Induction Assembly's Objects section —
they are the assumptions the classical literature never bothered to surface, and surfacing them
is what this audit was for. With K1834 filed: **the complete dependency surface of the
prospective final chain is: audited classical steps (this document) + banked theorems
(T2574–T2579) + L1 (Cal's read pending) + L2's J1 and J2. Nothing else exists to hide in.**

— Keeper, K1834. Next counter: K1835.

---

## v0.2 AMENDMENT (same K-number; 2026-09-01, afternoon) — Cal's §806 findings discharged: A2's proof substituted, Whitney DERIVED. The chain now contains ZERO citations.

**A2, proof repaired by substitution (Cal's finding one accepted — my dual route was the chord
lemma in disguise; the honest argument, with the repeated-vertex case the textbooks skip):**
Let G be simple planar, not edge-maximal; some face f has boundary walk of length ≥ 4.
*Case (i): the walk repeats a vertex v.* Then v is a cut vertex and two of its walk-neighbors
x, y lie in different blocks, hence are non-adjacent; both lie on f, so the chord xy is addable
inside f. *Case (ii): the walk is a cycle with ≥ 4 distinct vertices; take consecutive
a, b, c, d.* If a, c are non-adjacent, add ac inside f. If a, c are adjacent — necessarily by
an edge drawn outside f — then that edge together with the path a–b–c along f's boundary is a
Jordan curve with b inside-region and d outside-region (d lies on f beyond c, on the far side
of the curve), so ANY b–d edge would cross it: b, d are non-adjacent, and bd is addable inside
f. Either way a chord is addable; iterate to maximality; at maximality every face is a
triangle. ∎ (Statement was never in doubt; the proof now earns it.)

**S3, Whitney's 3-connectivity DERIVED (Cal's finding two, his preferred discharge — the last
citation leaves the chain):**
Claim: a simple maximal planar graph G with |V| ≥ 4 is 3-connected.
*Proof.* G is connected (else an edge is addable between components across a shared face) and
has no cut vertex (a cut vertex would repeat on some face's boundary walk, contradicting
all-faces-triangles via Case (i) above). Suppose {u, w} is a 2-cut: G − {u, w} has components
A, B (nonempty). **Step 1 — each cut vertex's neighbors lie in ONE component (plus possibly the
other cut vertex).** Around u, every face is a triangle, so consecutive neighbors of u in its
rotation are ADJACENT. If u had neighbors in both A and B, then reading u's rotation cyclically,
blocks of A-neighbors and B-neighbors would need separating positions at every A/B interface —
and only w can sit at such a position (an adjacent A–B pair is impossible across components).
A cyclic sequence containing both A- and B-blocks has at least TWO interfaces; w occurs at most
ONCE (G simple). Contradiction. So N(u) ⊆ A ∪ {w} or N(u) ⊆ B ∪ {w}, and likewise for w.
**Step 2 — the shared-triangle contradiction.** If N(u) and N(w) both avoid B (say), then B is
adjacent to neither u nor w and G is disconnected: contradiction. So WLOG N(u) ⊆ A ∪ {w} and
N(w) ⊆ B ∪ {u}. If uw ∉ E, then A ∪ {u} and B ∪ {w} are disconnected from each other:
contradiction. So uw ∈ E; the edge uw borders two triangular faces uwx, uwy; each of x, y is a
common neighbor of u and w, hence x ∈ A (as a neighbor of u) and x ∈ B (as a neighbor of w) —
impossible. ∎
Consequence, now derived rather than cited: **every vertex link in a simple maximal planar
graph on ≥ 4 vertices is a simple cycle** — the fact the entire context machinery stands on.

**Status after v0.2:** Cal's two findings discharged as specified; his four honest words
("and one pinned classical citation") are retired — **the prospective final chain now carries
ZERO citations and zero unaudited steps outside J1′, J2, and the sub-joint SJ riding the
choice.** Cal's diff-read of this amendment is owed and invited; the substitutions follow his
own §806 sketches, so the diff should be short — but the last time a proof carried "his
argument, my frame," it broke at the frame, so he checks the frame.

— Keeper, K1834 v0.2.

---

## v0.3 AMENDMENT (same K-number; 2026-09-01, later afternoon) — A2 case (ii) repaired at the frame, per Cal §807. Jointly-owned break, recorded as such.

**The break (Cal's catch, ownership shared on his own ruling):** v0.2's case (ii) closed its
Jordan curve through the boundary path a–b–c — putting b ON the curve rather than in a region,
and excluding nothing about a b–d edge on the face-interior side. Cal's §806 sketch said "the
face's a–c arc," ambiguous between boundary path and interior arc; he meant the interior, I
read the boundary. **Third frame-break of the arc; every seat has now owned one. The methods
sentence stands twice-confirmed: an argument handed across desks must carry its frame, not just
its steps — a sketch's preposition is where the next break lives.**

**Case (ii), corrected (the two lines it always was):** a, c adjacent by an edge e drawn outside
f (f's interior is a face: empty). Form the closed curve e ∪ γ, where γ is an arc from a to c
through f's INTERIOR. γ crosses nothing (faces contain no vertices or edges), so the curve is a
Jordan curve meeting the graph only at a and c. It separates b from d: b reaches its side along
the boundary edge ab (uncrossed — ab lies on f's boundary, γ in f's interior, e outside f), d
symmetrically. Now suppose bd ∈ E: the edge bd is drawn avoiding f's interior (faces are empty),
so it cannot cross γ; it shares no endpoint with e, so by planarity it cannot cross e; yet its
endpoints lie in different components of the plane minus the curve — contradiction. So bd ∉ E
and the chord bd is addable inside f. ∎

**Status after v0.3:** Whitney derivation PASSED on Cal's independent re-derivation (the chain's
last citation is confirmed gone); A2 case (i) unchanged; case (ii) now closes with the curve in
the right frame. Cal's confirm of this two-line substitution is owed — and per the
twice-confirmed lesson, the frame is stated in the text, not assumed from the sketch.

— Keeper, K1834 v0.3.

---
**SCOPE NOTE on A3, 2026-09-02 08:10 (K1835 ruling):** "induction skeleton — SOUND, NO CIRCULARITY" holds for the skeleton in isolation. The Insertion Theorem it consumes at the deg-5 case measures descent toward 𝒯(T,v), which is nonempty iff T is 4-colorable; so the chain AS ASSEMBLED assumes 4CT(T) at a minimal counterexample. A3's verdict is unchanged for A3; the chain's consumption line is STRUCK (see K1835). The classical steps stand at zero citations. — Keeper

---

## A5 (added 2026-09-02 08:53) — BIRKHOFF'S SEPARATING-CYCLE LEMMAS, RE-DERIVED IN FULL (zero citations), for the minimal-counterexample frame proposed in K1836

**Setting.** T a sphere triangulation that is a MINIMAL counterexample: not 4-colorable, every sphere
triangulation with fewer vertices 4-colorable. A cycle C of T is *separating* if T − V(C) is disconnected;
write I (inside) and O (outside) for the two sides, both nonempty.

**A5.1 — no separating triangle.** Let C = (a,b,c) separate. T₁ := C ∪ I and T₂ := C ∪ O are sphere
triangulations (C bounds a face in each) with fewer vertices than T (T₁ omits O ≠ ∅, T₂ omits I ≠ ∅). Each is
4-colorable by minimality; on C each coloring uses three distinct colors (a,b,c pairwise adjacent). Permute
T₂'s colors so it agrees with T₁ on C. Every edge of T lies in T₁ or T₂ (an edge with one end in I and one in O
would cross C — impossible; edges within C, I∪C, O∪C are covered), so the glued coloring is proper. ∎

**A5.2 — no separating 4-cycle.** Let C = (a,b,c,d) separate, in cyclic order. For a side S ∈ {I, O}, let
D_S := C ∪ S (a near-triangulation with C as its one non-triangular face). D_S + ac and D_S + bd (a chord
added inside the 4-face) are sphere triangulations with fewer vertices than T, hence 4-colorable. Their
colorings restricted to C realize, up to color permutation, one of three *patterns*:
P_Y: a,b,c,d all distinct · P_ac: a=c, b≠d · P_bd: b=d, a≠c. (Chord ac forbids a=c; chord bd forbids b=d.)
Deleting the chord leaves a proper coloring of D_S with the same pattern. So each side realizes, on D_S,
at least one pattern from D_S+ac (P_Y or P_bd) and one from D_S+bd (P_Y or P_ac).

*Claim: if a side realizes P_Y, it realizes AT LEAST ONE of P_ac, P_bd.* (Corrected 2026-09-02 — the first
draft said "both"; the Kempe argument gives one, and one suffices.) Take a P_Y coloring of D_S (no chord),
colors a,b,c,d = 1,2,3,4. Let K_b be the (2,4)-Kempe chain of D_S containing b, K_a the (1,3)-chain containing a.
(i) If d ∉ K_b: swap 2↔4 on K_b; b becomes 4 = color(d); a=1, c=3, d=4 unchanged; proper; pattern P_bd.
(ii) If d ∈ K_b: K_b contains a path Q from b to d, all vertices colored 2 or 4, interior vertices in S (b, d
are the only boundary vertices so colored). Q is a simple arc in the closed disc D_S bounded by C joining
boundary points b and d; it separates the disc into two regions whose boundaries contain a and c respectively
(b and d split the boundary circle into the arc through a and the arc through c) — the Jordan step of K1832/
K1834 scope note S4, embedding present. A (1,3)-path from a to c inside D_S would have to meet Q, but shares
no vertex with it (disjoint color sets) and cannot cross it in an edge interior in a plane embedding. So
c ∉ K_a; swap 1↔3 on K_a; a becomes 3 = color(c); b=2, d=4 unchanged; proper; pattern P_ac. ∎(claim)

*What each side realizes.* Case A — the side realizes P_Y: then by the claim also P_ac or P_bd. Case B — the
side realizes no P_Y: then D_S+ac forces P_bd and D_S+bd forces P_ac, so the side realizes BOTH P_ac and P_bd.

*Gluing.* (B, B): share P_ac. (A, B): the A-side realizes one of P_ac/P_bd, the B-side both — share it.
(A, A): share P_Y. "Glue" = permute one side's colors to agree on C (a pattern fixes C's coloring up to
permutation) and take the union; proper by the edge-coverage argument of A5.1. T is 4-colored —
contradiction. ∎

**A5.3 — δ(T) = 5.** δ ≤ 5 by A1 (Euler); δ ≥ 5 because vertices of degree ≤ 4 are reducible (A4, Kempe
deg ≤ 4, re-derived 09-01). ∎

**Inputs, enumerated:** minimality (the IH) · Kempe swaps preserve properness (definitional) · the Jordan/disc
separation step (S4, embedding present) · A1 and A4 of this audit. **No citation.** The separating-5-cycle case
(the rest of "internally 6-connected") is NOT derived here; the frame proposed in K1836 uses only A5.1–A5.3
(call the class **B4**: no separating 3- or 4-cycles, δ = 5 — for triangulations this is exactly 5-CONNECTED, plantri `-c5`). Consequence used downstream: in B4 the link of
every degree-5 vertex is an INDUCED 5-cycle (a chord x–y of the link with v gives a separating triangle v,x,y
unless it bounds a face, which it cannot at degree 5).

**Verdict:** A5.1–A5.3 PASS at zero citations, conditional on Cal's cold read (the Jordan step in A5.2(ii) is
the one place a frame could slip — I have stated it with the disc, not the sphere). — Keeper
