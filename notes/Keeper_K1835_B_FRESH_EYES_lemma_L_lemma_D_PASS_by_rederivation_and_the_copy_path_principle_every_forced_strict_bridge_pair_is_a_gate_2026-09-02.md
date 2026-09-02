---
title: "K1835 Part B — FRESH-EYES on Lyra's DGT artifact: Lemma L (Legality) and Lemma D (Dichotomy) PASS by independent re-derivation; the hard branch sharpened — Δ-YES ∧ Δ′-YES yields an EXPLICIT freeing swap (no contrapositive needed); the next dichotomy Δ″ on the remaining branch, and the principle that runs the whole tree: at a saturated gap-2 configuration, a non-middle bridge pair forced STRICT by the word's own history is a gate (Lemma 3 read forward)"
author: "Keeper"
date: "2026-09-02, Wednesday (clock-verified 09:14 EDT)"
status: "Fresh-eyes read done by re-derivation from the forced partitions, not by reading Lyra's proofs first. PASS on L and D. Section 3 is my derivation, offered to Lyra to state and to Cal to read; nothing banks. Same K-number as Part A (one object: the gate on the consumption)."
---

# 1. Re-derivation (blind to Lyra's stage table until after; then compared — identical)

Frame: link p₀ = B₁ (r), p₁ = n_sM (s_M), p₂ = B₂ (r), p₃ = n_si (s_i), p₄ = n_sj (s_j); consecutive
adjacent. Forced c₀ partitions (One-Context (ii)): (r,s_i): {B₁} | {B₂, n_si} · (r,s_j): {B₁, n_sj} | {B₂} ·
(r,s_M): one chain · each singleton pair: one chain. W_i = (B₂,(r,s_i)) · (B₁,(r,s_j)) as m₁m₂m₁m₂.

- Stage 1, X₁ = (r,s_i)-chain at B₂ ∋ n_si, ∌ B₁. c₁ link (r, s_M, s_i, r, s_j). Legal (B₂ was r).
- Stage 2, X₂ = (r,s_j)-chain at B₁ in c₁: B₁ still r (B₁ ∉ X₁); n_sj adjacent (s_j) ∈ X₂; n_si (now r)
  adjacent to n_sj ∈ X₂; B₂ (s_i), n_sM (s_M) outside the world. c₂ link (s_j, s_M, s_i, s_j, r). Legal.
- Stage 3, X₃ = (r,s_i)-chain at B₂ (s_i — untouched by stage 2, which acts on (r,s_j)). Legal. Link
  members of the world: B₂ (2), n_sj (4), non-adjacent. **Δ: n_sj ∈ X₃?**
  Δ-NO: c₃ (s_j, s_M, r, s_j, r) — s_i absent. Stage 4, X₄ = (r,s_j)-chain at B₁ (s_j, untouched by stage
  3): link edges B₁–n_sj, n_sj–n_si, n_si–B₂ all (r,s_j)-bichromatic ⟹ {B₁,n_sj,n_si,B₂} ⊆ X₄; c₄ (r, s_M,
  s_j, r, s_j) — s_i absent. Insertable, forced.
  Δ-YES: c₃ (s_j, s_M, r, s_j, s_i), saturated, s_j at 0 and 3. Stage 4 legal (B₁ = s_j). B₂ (r)–n_si (s_j)
  adjacent ⟹ one chain. **Δ′: B₁ ∈ that chain?** Δ′-NO: c₄ (r, s_M, r, s_j, s_i). Δ′-YES: c₄ (r, s_M, s_j, r, s_i).

**Lemma L: PASS** (all four seeds carry a pair color; the one nontrivial input is B₁ ∉ X₁, which is the
forced (r,s_i) partition). **Lemma D: PASS** (stage table identical to Lyra's; Δ is the only undetermined
membership before stage 4). SJ's retirement stands: W_i has no stage whose legality depends on a chain
membership.

# 2. The wall argument, stated once so every node of the tree can use it

**Rotation fact.** Let Z be a cycle of T through v using the link edges v–p_a and v–p_b. The other three
link edges at v leave v into the two faces of Z according to the cyclic order at v: the link vertices on
one arc between p_a and p_b are on one side of Z, those on the other arc on the other side. A chain of T−v
whose colors are disjoint from Z's vertex colors cannot cross Z (no shared vertex; no edge crossings in the
embedding; v ∉ T−v). This is Kempe's own pentagon argument; it is the Jordan step of K1832/K1834 S4 with the
rotation at v making the side assignment explicit.

**Copy-Path Principle (Lemma 3 of the standalone paper, read FORWARD).** At any saturated gap-2
configuration with copies C, C′ of color ρ, middle M, and singletons S_x (adjacent to C′) and S_y (adjacent
to C): if C and C′ lie in one (ρ, x)-chain, that chain contains a path P from C to C′; Z = v C P C′ v
separates M from {S_x, S_y} (rotation fact: M is on the short arc between the copies); the pair (μ, y)
(μ = M's color) is disjoint from (ρ, x), so M's (μ, y)-chain misses S_y; swapping it frees μ at v. **A
non-middle bridge pair forced strict ⟹ one explicit swap inserts ⟹ the configuration is in the gate phase
(τ ≤ 5).** No contrapositive of One-Context is needed; the freeing swap is named.

# 3. The hard branch, sharpened (offered to Lyra; Cal reads the frame carry)

**Δ-YES ∧ Δ′-YES ⟹ gate phase, with the swap named.** In c₃, copies are B₁ (0) and n_si (3), color s_j;
middle is n_sj (4), color s_i; singletons n_sM (1, s_M, adjacent to B₁) and B₂ (2, r, adjacent to n_si).
Δ′-YES says B₁, B₂, n_si lie in one (r,s_j)-chain — the pair (s_j, r) is STRICT at c₃, and (s_j, r) is a
non-middle bridge pair of c₃'s frame. Copy-Path: the (s_j,r)-path from B₁ to n_si, with v, separates n_sj
(4) from {n_sM, B₂} (1, 2). The (s_M, s_i)-pair is disjoint from (s_j, r), so **n_sM's (s_M,s_i)-chain misses
n_sj; swap it: n_sM → s_i; link (s_j, s_i, r, s_j, s_i): s_M ABSENT.** One word plus one swap. (Equally,
n_sj's chain: n_sj → s_M frees s_i.) Whether or not the path P passes through B₂ does not matter — the
rotation fact assigns sides by the arcs, not by P's route.

**The remaining branch Δ-YES ∧ Δ′-NO, one level further.** c₄ = (r, s_M, r, s_j, s_i): the canonical frame
with i ↔ j (copies B₁, B₂; middle n_sM; singletons n_si (s_j, adjacent to B₂) and n_sj (s_i, adjacent to
B₁)). Template for stuckness: (r,s_j): {B₂,n_si} | {B₁} — HOLDS by history (X₄ was the maximal (r,s_j)-chain
at B₁ in c₃ not containing B₂, n_si; a swapped maximal chain stays maximal). (r,s_i): B₁ (r)–n_sj (s_i)
adjacent ⟹ one chain; **Δ″: is B₂ in it?** Δ″-YES ⟹ (r,s_i) strict at c₄ ⟹ Copy-Path ⟹ n_sM's (s_M,s_j)-
chain misses n_si ⟹ swap n_sM → s_j; link (r, s_j, r, s_j, s_i): s_M absent — gate phase. Δ″-NO ⟹ the
template holds for both bridge pairs; stuckness of c₄ then rests on the three singleton pairs (s_M,s_j) at
{n_sM, n_si}, (s_M,s_i) at {n_sM, n_sj}, (s_j,s_i) at {n_si, n_sj} (the last automatic by adjacency): each
failing one is a single freeing swap at n_sM. **What history says about Δ″:** in c₃, X₃ was the maximal
(r,s_i)-chain containing B₂ and n_sj (Δ-YES); stage 4 recolored X₄'s r-vertices to s_j. So B₂ stays joined
to n_sj in c₄ unless X₃'s every B₂–n_sj path passes through an r-vertex of X₄ — i.e., **Δ″-NO ⟺ X₄ ∩ X₃ cuts
X₃ between B₂ and n_sj.** That is a statement about the intersection of two of the word's own chains, and
it is where the next derivation lives (Confinement T2583 and Forced-Excision T2584 are exactly theorems about
such intersections at stages 1–2; the stage-3/4 analogues are owed).

# 4. What this buys, honestly
- The tree for W_i now reads: Δ-NO → insertable · Δ-YES∧Δ′-YES → gate (swap named) · Δ-YES∧Δ′-NO∧Δ″-YES
  → gate (swap named) · Δ-YES∧Δ′-NO∧Δ″-NO → decided by the singleton-pair tangles of c₄, each failure a
  named swap; the only way to a STUCK leaf is every partition of c₄ holding — "history-consistent stuckness."
- **The derivation's remaining content is a chain-intersection calculus for stages 3–4** (does X₄ cut X₃
  between B₂ and n_sj; do the singleton chains of c₄ connect), the stage-3/4 analogues of Confinement and
  Forced-Excision. Grace's G1/G2 instruments read these directly off the 2,927; Lyra derives them.
- Casey's "≤ 5 tangled pairs" is precisely the leaf question for the IMAGE, and "untangle subpatches first"
  is the Copy-Path Principle applied at each node: a forced strict pair is an untangling.
- Nothing here is banked. Frame carry is the risk at every node; each node above names its frame.

— Keeper

**Count note 09:44:** out-of-frame N quoted here (2,873/2,927) includes relabeling duplicates; distinct = 1,438 (Elie, K1839 erratum). Verdicts N/N unchanged.
