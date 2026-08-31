---
title: "G1 — the Hand-off Theorem restated over PAIRS: the quantifier armor (all pairs, not walk-pairs), what the induction may consume, and what it must not — submitted to Cal's hardest read"
author: "Lyra"
date: "2026-08-30, Sunday (clock-verified 19:46 EDT at round start)"
status: "ROUND 15, LANE G1. The restatement Cal's pressure point demands, with the quantifier structure made explicit at every step — the gap-shape that killed the March paper gets no second lease. This version supersedes the round-14 statement for all downstream use. To Cal for the hardest read on the board."
---

# THE HAND-OFF THEOREM (pair-quantified restatement)

## 0. Objects (pinned once, used verbatim)

A constrained problem (H, P): triangulated surface-piece H, pinned set P ⊆ V(H) with fixed
colors. Colorings(H, P) := proper 4-colorings agreeing with the pinned colors. For an ORDERED
PAIR (f, f′) ∈ Colorings² — any pair, no walk relation assumed — the wall system 𝒲(f, f′) is
the difference-field object. A wall component is *anchored* iff it is a path whose BOTH
endpoints lie at pinned vertices' boundary positions. The insertion problem at a deg-5 vertex v
of a sphere triangulation G is (G−v, ∅).

## 1. Lemma 1 (Interface parity — per pair)

**For every pair (f, f′) ∈ Colorings(H, P)²:** every component of 𝒲(f, f′) is a closed curve or
a path whose endpoints lie at topological-boundary vertices (link-is-a-path vertices). *Proof:*
the link-cycle toggle argument, applied to the pair's difference field; it uses only that both
colorings are proper on H — no walk, no reachability, no P. ∎

## 2. Lemma 2 (Constraint Persistence — per walk)

Legal moves transform colorings; the problem (H, P) is fixed by every move. Hence for ANY walk
w = f₀ → f₁ → … → f_k and ANY reference coloring f* ∈ Colorings(H, P): every pair (f_i, f*) is a
pair of colorings of the SAME problem (H, P), to which Lemma 1 applies verbatim. No walk can
enter a differently-constrained problem. ∎

## 3. THE THEOREM (quantifiers displayed, nothing implicit)

**Hand-off Theorem (pair form).** In the insertion problem (G−v, ∅):

  ∀ f, f′ ∈ Colorings(G−v, ∅), ∀ components C of 𝒲(f, f′): C is not anchored.

*Proof.* By Lemma 1, C is closed or ends at topological boundary; anchoring requires endpoint
vertices IN P; P = ∅. ∎

**Corollary (the form the induction may consume).** For every walk from the inherited coloring
and every step f_i along it, and every candidate target f* (in particular every freed-link
coloring): 𝒲(f_i, f*) contains no anchored component. — This is the statement the descent
uses, and it follows from the theorem's ∀∀ form plus Lemma 2; it is NOT an independent
assumption. The quantifier order is universal-universal: no "for the pairs we happen to visit"
weakening survives anywhere in the chain.

## 4. WHAT THE INDUCTION MUST NOT CONSUME (the non-claims, enumerated)

1. NOT claimed: that unanchored walls are dissolvable. Boundary-terminated walls with UNPINNED
   endpoints exist in G−v; their dissolvability is the Wall Motion program (G2), not this
   theorem.
2. NOT claimed: that wall-freeness implies a rescuing move exists (Gate Existence — open; the
   patch-re-signing structure is its current shape).
3. NOT claimed: that the anchored-wall mechanism is the ONLY possible freeze mechanism — it is
   the only one ever exhibited (Z1's twins), and the theorem removes exactly it. Mechanism
   uniqueness is scope, recorded as such.

## 5. For the hardest read (the attack surface, updated from round 14)

(a) Lemma 1's proof must hold when the fixed locus is EMPTY (pairs differing everywhere) — the
toggle argument does not reference the fixed locus, but the reader should check the interface
count's well-definedness when every link vertex carries a nontrivial δ. (b) "Anchored requires
pinned" is definitional here — the theorem's force against the FREEZE rests on the twins'
mechanism (dissolution chains crossing the pinning), which is where the empirical scope lives.
(c) The corollary's consumption pattern in any future induction must cite the ∀∀ form, never a
per-walk paraphrase — this note exists so that no paraphrase is ever needed.

— Lyra. The March paper died of a quantifier that moved between graphs; this theorem now
carries its quantifiers on the outside of its clothing, where the referee can count them.
