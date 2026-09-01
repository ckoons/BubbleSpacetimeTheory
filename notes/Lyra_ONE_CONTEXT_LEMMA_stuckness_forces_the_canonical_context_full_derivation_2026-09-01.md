---
title: "L1 — THE ONE-CONTEXT LEMMA: stuckness at a degree-5 hole forces the canonical context up to symmetry — full derivation from banked machinery, zero census joints, every input's status named"
author: "Lyra"
date: "2026-09-01, Tuesday (clock-verified 09:20 EDT at round start)"
status: "Derivation complete; every input cited with its epistemic status. The census (Toy 5562, 1,822/1,822, zero splits, positive control) CONFIRMS this lemma and additionally shows the context suffices to determine the outcome — that sufficiency is consumed downstream (L2/L3), never here. Cal's read owed before any banking."
---

# THE ONE-CONTEXT LEMMA

## Statement

Let G be ANY sphere triangulation, v a degree-5 vertex, c a proper 4-coloring of G−v that is
STUCK at v: no color is free at v and no single Kempe swap frees one. Then, up to rotation and
reflection of the link and permutation of colors:

**(i) the link word is (0,1,0,2,3)** — bridge color 0 at positions {0,2}, middle color 1 at
position 1, singletons 2, 3 at positions {3,4};

**(ii) the six pair-partitions of the link vertices into chains are exactly:**
(0,1): {0,1,2} one chain · (0,2): {0} | {2,3} · (0,3): {0,4} | {2} ·
(1,2): {1,3} · (1,3): {1,4} · (2,3): {3,4}.
*(Convention, pinned per Cal §805 pressure point 5: each entry lists the chain-partition of
the link POSITIONS carrying that pair's two colors — positions absent from an entry carry
neither color of the pair and are not partitioned by it.)*

In particular the bounded context (word, partitions) realized by ANY stuck configuration in ANY
sphere triangulation is the single canonical one — Middle-Strict at context level.

## Proof

**(a) Stuck ⟹ saturated with a unique bridge.** If some color is absent from the link, it is
free at v — not stuck. So all four colors appear among five neighbors: exactly one color
repeats (the bridge r, copies B₁, B₂), three singletons. [Counting; no inputs.]

**(b) The gap is 2.** gap(v) ∈ {1,2} (five positions, one repeat). If gap = 1, then τ(v) ≤ 5
(Lemma 2 of the standalone paper — STATUS: audit-verified sound by independent re-derivation,
K1832 Section 1; the Jordan sector argument at v is legitimate in G−v since v is present in G),
so some pair is operationally untangled and a single swap frees a color — not stuck. Hence
gap = 2, and the link reads (r, s_M, r, s_i, s_j) in cyclic order: the word (0,1,0,2,3) after
relabeling. Stuckness is exactly saturation with τ(v) = 6 from here on. [One input: Lemma 2.]

**(c) The six partitions are forced.**
- **(r, s_M) = (0,1): {0,1,2}.** The link edges (B₁, n_sM) and (n_sM, B₂) exist (consecutive
  link vertices are adjacent in a triangulation) and are (r,s_M)-bichromatic: all three vertices
  lie in one chain. [Middle-Strict — STATUS: proved, link-edge algebra only, no Jordan curves
  (K1832 Section 4.1; independently blind-converged R2; verified 862/862 in G−v and 4,242/4,242
  in H); UNREGISTERED — flagged for /theorem claim with Keeper's priority.]
- **(r, s_i) = (0,2): {0} | {2,3}.** The link edge (B₂, n_si) (positions 2,3 consecutive) is an
  (r,s_i)-edge: n_si and B₂ share a chain, always [Orientation, forced form — STATUS: proved,
  R7, link edges only]. If B₁ shared that chain, (r,s_i) would be STRICTLY tangled — but at
  τ = 6 only the middle pair can be strict (Lemma 3 of the standalone paper — STATUS:
  audit-verified sound, K1832 Section 1; its Jordan separation is legitimate in G−v). So B₁ is
  in a different (r,s_i)-chain. [Two inputs: Orientation; Lemma 3.]
- **(r, s_j) = (0,3): {0,4} | {2}.** Symmetric: the link edge (n_sj, B₁) (positions 4,0
  consecutive) ties them; Lemma 3 excludes B₂ from that chain. [Same inputs, mirrored.]
- **(1,2), (1,3), (2,3): {1,3}, {1,4}, {3,4}.** At τ = 6 every pair is operationally tangled;
  for singleton pairs operational and strict tangling coincide (both reduce to "the two
  singleton link vertices share a chain" — the standalone paper's Definition 9 Remark, STATUS:
  audit-verified, K1832 Section 1, checked in both directions). So each singleton pair's two
  link vertices share a chain; for (2,3) the link edge (positions 3,4) makes it automatic.
  [One input: the Remark.]

**(d) Uniqueness up to symmetry.** The choices consumed — where the cyclic word starts, its
orientation, and which colors are named 0,1,2,3 — are exactly the dihedral and color symmetries
quotiented in the statement. Nothing else was chosen. ∎

## Input ledger (the lemma's entire dependency surface)

| Input | Status |
|---|---|
| Lemma 2 (gap-1 ⟹ τ ≤ 5) | audit-verified sound (K1832 Sec 1 re-derivation) |
| Lemma 3 (τ=6 ⟹ only middle strict) | audit-verified sound (K1832 Sec 1 re-derivation) |
| Middle-Strict | proved (link edges only); unregistered — registration flagged |
| Orientation (forced form) | proved (link edges only) |
| Def 9 Remark (singleton: strict = operational) | audit-verified (K1832 Sec 1, both directions) |

Zero census joints: no step above leans on a measured number. The census's confirming role
(1,822/1,822, zero splits, positive control discriminating on loose populations) and its
ADDITIONAL content — that this bounded context determines the gate outcome — are consumed
downstream, with labels, where they belong.

— Lyra. The context was always going to be unique: the word is Corollary 1 wearing coordinates,
and the partitions are the weekend's lemmas reading their own signatures back to us.
