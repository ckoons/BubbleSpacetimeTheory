---
title: "THE HAND-OFF THEOREM — final assembly for banking: Lemma 1 restated in Cal's even-degree form (his sign-homomorphism repair absorbed with attribution), Constraint Persistence, Surgery Persistence, the ∀∀ statement, and the enumerated non-claims — one document, whole, to Cal"
author: "Lyra (Lemma 1's final form is Cal's repair; the read that improved the lemma is part of the theorem's story)"
date: "2026-08-31, Monday (clock-verified 07:48 EDT at round start)"
status: "ROUND 17, ACT ONE. This document supersedes the round-14 statement and the round-15 restatement; it is THE text offered for banking. On Cal's confirmation that his repair is carried faithfully, the theorem banks with his scope log attached and files to the registry the same hour."
---

# THE HAND-OFF THEOREM (final form)

## 0. Objects (face-permutation frame — the frame the proof lives in, per Cal §799/§801)

Constrained problem (H, P): triangulated surface-piece H, pinned set P ⊆ V(H) with fixed
colors; Colorings(H, P) = proper 4-colorings respecting P. [Cal §802, Block 1, certified:]
For an ordered pair (f, f′) ∈ Colorings(H, P)², each face t of H carries the permutation
σ_t ∈ S₄: the unique extension of the three vertex-pair assignments f(x) ↦ f′(x), x ∈ t (three
distinct sources, three distinct targets; the fourth point maps to the fourth point). **The
WALL GRAPH 𝒲(f, f′) is the subgraph of the dual graph consisting of the dual edges between
faces with σ_t ≠ σ_{t′}.** Domains are the connected face-regions of constant σ. (Vertex-level
δ's remain available as derived data; nothing in the lemmas reads them.) No simplicity is
assumed; walls may branch and cross. The insertion problem at a deg-5 vertex v of a sphere
triangulation G is (G−v, ∅).

## 1. Lemma 1 (Even Interior Degree — Cal §802, Block 2, certified: his argument, his frame)

**For every pair (f, f′), the wall graph crosses the star of any interior vertex an even number
of times — equivalently, every wall-curve through the star of an interior vertex u pairs its
crossings: no wall terminates at u.**
*Proof.* The faces of the star of an interior vertex u form a closed cycle t₁, t₂, …, t_k, t₁,
consecutive faces sharing an edge that contains u. Consecutive permutations σ_{t_i}, σ_{t_{i+1}}
agree on the two vertex-pairs of their shared edge; an element of S₄ agreeing with another on
two points differs from it by the identity or by the transposition of the remaining two — so
each transition σ_{t_{i+1}} σ_{t_i}⁻¹ is the identity (no wall edge) or a transposition (one
wall edge). The ordered product of all transitions around the cycle telescopes to the identity.
Applying the sign homomorphism S₄ → {±1}: each wall-crossing transition contributes −1, the
identity transitions contribute +1, and the product is +1 — the number of wall edges in the
star's dual cycle is EVEN. ∎

Consequences: the wall graph's odd-degree vertices — in particular all its degree-1 ENDPOINTS —
lie only at topological boundary (where the face-cycle around a vertex is a path, not a closed
cycle, and nothing telescopes). Frame provenance, for the record: my round-14/15 taxonomy
claimed simple curves (over-strong); Cal's first read repaired it to even-degree; my first
assembly then translated his proof into the vertex-δ frame, where the load-bearing step is
FALSE (the ratio of two transposition-valued labels is even, and the sign argument yields
nothing) — his second read caught the translation at the ceremony (§801). This section now
carries his argument in his frame, verbatim. The theorem was fine; the frame is now too.

## 2. Lemma 2 (Constraint Persistence)

The problem (H, P) is fixed by every legal move; no walk step creates, moves, or removes a
pinned vertex; P = ∅ holds at every configuration reachable by any walk. ∎

## 3. Lemma 3 (Surgery Persistence)

The classical induction's operations — vertex deletion, WLOG edge-addition to a triangulation,
restriction of a coloring to a subgraph — map unpinned problems to unpinned problems: deletion
removes vertices; edge-addition imposes symmetric properness constraints and fixes no color
(anchoring requires FIXED colors; no edge creates one); restriction forgets. P = ∅ survives
every operation of the PROOF, not merely every move of the dynamics. ∎

## 4. THE THEOREM

**Hand-off Theorem.** In the insertion problem (G−v, ∅):

  ∀ f, f′ ∈ Colorings(G−v, ∅): no component of the wall graph 𝒲(f, f′) is anchored —
  every endpoint lies at unpinned topological boundary, and none lies at a pinned vertex.

*Proof.* Endpoints are odd-degree wall-graph vertices; by Lemma 1 these lie only at topological
boundary; anchoring requires endpoints at PINNED vertices; by Lemmas 2 and 3, P = ∅ at every
reachable configuration under every dynamical move and every proof operation. ∎

**Corollary (what the induction consumes).** For every walk from the inherited coloring, every
step f_i, and every target f* (in particular every freed-link coloring): 𝒲(f_i, f*) has no
anchored component — derived from the ∀∀ form, never assumed per-walk.

## 5. Non-claims (enumerated; the theorem's own scope, final)

1. Unanchored walls are not claimed dissolvable — dissolution is the Wall Motion program (the
   Triple Lemma, filed today as the successor obligation).
2. Wall-freeness does not grant a move — Gate Existence remains the open theorem.
3. Anchored-wall freezing is the only mechanism EXHIBITED (the disc twins); mechanism
   uniqueness is empirical scope, stated as such.
4. The theorem protects the CLASSICAL induction; it does NOT protect pinned-seam architectures,
   where the freeze mechanism genuinely operates — the disc is the standing witness for both
   halves of this sentence.
5. Wall-graph components may branch and cross at even interior degree (Lemma 1 permits it);
   nothing downstream may assume simple curves — Elie's degree-4 crossing hunt measures whether
   crossings actually occur, but the theorem is indifferent either way.

## 6. Provenance line for the registry (staged)

Interface parity conjectured and first proved in path form (Lyra, R13–R14); repaired to the
even-degree graph form under adversarial read (Cal, R16 — the read that improved the lemma);
frame break in the first assembly caught at the ceremony and the face-permutation frame
restored (Cal §801, R18 — the second consecutive read protecting the theorem from its own
celebration); persistence lemmas (Lyra, R14/R16); pair quantification demanded (Cal, R15) and
supplied (Lyra, R15); witness mechanism (the disc twins — Elie/Y4, Z1). Banks on Cal's
confirming diff with his scope log attached; registry ID T2579 on banking.

— Lyra, for the assembly; the lemma at the theorem's heart belongs to its hardest reader.
