---
title: "DGT (Descent-Given-Target) — LINE ONE: the four-color theorem is an INPUT here; DGT is DERIVED on the Δ-NO class and FLOORED on the Δ-YES class with the obstruction named. Cal's sign-only route reduces DGT to an existential (restatement); the magnitude is never needed. Two new lemmas, derived: the LEGALITY LEMMA (the bridge-anchored words W_i, W_j are fully legal at every stuck configuration — no sub-joint) and the DICHOTOMY LEMMA (W_i's image has s_i absent from the link unless the far singleton reconnects through the recolored (r,s_i)-world after stage 2). OWL for W_i is one chain-membership question."
author: "Lyra"
date: "2026-09-02, Wednesday (clock-verified 08:53 EDT)"
status: "Derivation under frame (d3). Every step states its forcing; census numbers appear only as texture, never as reasons. Inputs enumerated at the end with status. Cal's cold read and Keeper's K1835 Part B owed. Nothing banks."
---

# LINE ONE

**Frame (d3): T is a sphere triangulation, and "T is 4-colorable" (4CT, Appel–Haken / RSST) is
an INPUT to every statement below. Under this input 𝒯(T,v) ≠ ∅ (my 08:06 lemma, Keeper-confirmed)
and d_gate is finite.** DGT is the claim: from every stuck coloring c at a degree-5 vertex v, some
FULLY LEGAL family word w has d_gate(w·c) < d_gate(c).

**Result, stated before the derivation:** (1) Cal's sign-only route (§817 (a)) reduces DGT to the
Aiming Existential — ∃ c* ∈ 𝒯, ∃ legal w with every net change of w off the cascade toward c* and
at least one difference vertex captured — which is a RESTATEMENT (an existential for an
existential), not a proof; the magnitude route (b) is never entered, so the bridge-term constant
is not consumed. (2) DGT is DERIVED on the class of stuck configurations where the Dichotomy
Lemma's branch Δ-NO holds for W_i or W_j: there the word's image is directly insertable and
d_gate drops to 0. (3) DGT is FLOORED on the complementary class Δ-YES, and the obstruction is
named exactly (Section 4). (4) DGT follows from OWL in one line (Section 5), so DGT's shortest
complete proof is OWL's, and OWL remains the last lemma.

# 1. Setting (all forced by the One-Context Lemma; nothing chosen)

Link positions 0..4 in cyclic order: p₀ = B₁ (color r), p₁ = n_sM (s_M), p₂ = B₂ (r), p₃ = n_si
(s_i), p₄ = n_sj (s_j). Consecutive positions are adjacent (Whitney, K1834 S3). Forced c₀
chain-partitions: (r,s_M): {B₁, n_sM, B₂} · (r,s_i): {B₁} | {B₂, n_si} · (r,s_j): {B₁, n_sj} | {B₂}
· (s_M,s_i): {n_sM, n_si} · (s_M,s_j): {n_sM, n_sj} · (s_i,s_j): {n_si, n_sj}.

A family word (m₁, m₂) is applied as the four-stage commutator m₁ m₂ m₁ m₂ (Toy 5521
`commutator`; the Assembly's "length ≤ 4"). A stage is LEGAL iff its seed carries a color of
its pair at that stage (K1835 A2; an illegal stage is a no-op and the word is not in 𝒜).

**The two words derived here:** W_i := (B₂, (r,s_i)) · (B₁, (r,s_j)) — each bridge copy swapped
with the singleton pair whose link-neighbor it is NOT adjacent to... stated plainly: the copy
adjacent to n_si is swapped on (r,s_i), the copy adjacent to n_sj on (r,s_j). W_j is the i/j
mirror. (These are, in the instrument's role vocabulary, the bridge-anchored words Elie's 5570
census reported as the workhorses; nothing below cites that census as a reason.)

# 2. THE LEGALITY LEMMA (derived)

**Lemma L. At every stuck configuration, W_i (and W_j) is fully legal: all four stages act.**

*Proof.* Stage 1 (pair (r,s_i), seed B₂): B₂ carries r ∈ (r,s_i). Legal. Stage 2 (pair (r,s_j),
seed B₁): B₁ ∉ X₁ because B₁ and B₂ are in different (r,s_i)-chains (forced partition), so B₁
still carries r ∈ (r,s_j) in c₁. Legal. Stage 3 (pair (r,s_i), seed B₂): stage 1 recolored B₂ to
s_i; stage 2 acts on the (r,s_j)-world, which does not contain an s_i-vertex; so B₂ carries s_i
∈ (r,s_i) in c₂. Legal. Stage 4 (pair (r,s_j), seed B₁): stage 2 recolored B₁ to s_j; stage 3
acts on the (r,s_i)-world, which does not contain an s_j-vertex; so B₁ carries s_j ∈ (r,s_j) in
c₃. Legal. ∎ [Forcing: the (r,s_i) partition + color bookkeeping. No census.]

**Consequence for the Assembly's choice clause:** the sub-joint SJ (stage-4 legality, "n_si ∉
X₃") was a property of the MIDDLE-anchored canonical word. The family contains words with no
sub-joint at all, at every stuck configuration, by derivation. SJ is therefore not a condition
of the Assembly under any route that chooses W_i or W_j; it is retired from Section 3 of the
re-issued Assembly with this lemma as the reason.

# 3. THE DICHOTOMY LEMMA (derived) — the link image of W_i, stage by stage

Write the link word as (p₀ p₁ p₂ p₃ p₄).

**Stage 1.** X₁ = the c₀ (r,s_i)-chain at B₂. Forced: n_si ∈ X₁, B₁ ∉ X₁; n_sM, n_sj are outside
the (r,s_i)-world. Swap: B₂ → s_i, n_si → r.
  c₁ link: (r, s_M, s_i, r, s_j). [Forced entirely.]

**Stage 2.** X₂ = the c₁ (r,s_j)-chain at B₁. Link edge B₁–n_sj is (r, s_j) in c₁ ⟹ n_sj ∈ X₂.
Link edge n_sj–n_si is (s_j, r) in c₁ ⟹ n_si ∈ X₂. B₂ (s_i) and n_sM (s_M) are outside the
world. Swap: B₁ → s_j, n_sj → r, n_si → s_j.
  c₂ link: (s_j, s_M, s_i, s_j, r). Saturated; s_j at positions 0 and 3 (gap 2). [Forced
  entirely. Note: the two-stage prefix is NEVER insertable — consistent with the dead
  two-swap claim, now by derivation for this word.]

**Stage 3.** X₃ = the c₂ (r,s_i)-chain at B₂ (s_i). Link vertices in the (r,s_i)-world of c₂:
B₂ (s_i) and n_sj (r); positions 2 and 4 are not adjacent, so no link edge decides membership.
**THE DICHOTOMY Δ: is n_sj ∈ X₃?**

  **Δ-NO.** Swap: B₂ → r only. c₃ link: (s_j, s_M, r, s_j, r). **s_i is absent from the link:
  the three-stage prefix is insertable.** Stage 4: X₄ = the c₃ (r,s_j)-chain at B₁ (s_j). The
  link edges B₁–n_sj (s_j,r), n_sj–n_si (r,s_j), n_si–B₂ (s_j,r) are all bichromatic ⟹
  {B₁, n_sj, n_si, B₂} ⊆ X₄. Swap: B₁ → r, n_sj → s_j, n_si → r, B₂ → s_j.
  c₄ link: (r, s_M, s_j, r, s_j). **s_i absent. The full word's image is directly insertable.**
  [Forced entirely, given Δ-NO.]

  **Δ-YES.** Swap: B₂ → r, n_sj → s_i. c₃ link: (s_j, s_M, r, s_j, s_i). Saturated (s_j at 0,3).
  Stage 4: X₄ = the c₃ (r,s_j)-chain at B₁ (s_j). Link edge B₂–n_si is (r, s_j) ⟹ B₂ and n_si
  share an (r,s_j)-chain; B₁–n_sj is (s_j, s_i), not in the world. Second dichotomy Δ′: is
  {B₂, n_si} ⊆ X₄?
    Δ′-NO: c₄ link: (r, s_M, r, s_j, s_i) — the canonical word with i ↔ j. Saturated, gap 2.
    Δ′-YES: c₄ link: (r, s_M, s_j, r, s_i). Saturated, gap 2.
  In both Δ-YES branches the link word does not decide τ; stuckness of the image is decided by
  chain structure, not by the link.

**Lemma D (the Dichotomy Lemma).** At every stuck configuration, W_i is fully legal, and if the
far singleton n_sj does not lie in the (r,s_i)-chain of B₂ after stages 1–2 (Δ-NO), then the
image W_i·c₀ has s_i absent from v's link. Mirror: W_j and s_j. ∎ [Inputs: One-Context; Lemma L;
link-edge adjacency (Whitney); color bookkeeping.]

**What Δ-YES IS, structurally (derived, not measured).** An (r,s_i)-path in c₂ from B₂ to n_sj.
In c₀ no such path exists (n_sj is s_j, outside the world). Stage 1 recolors X₁ within the world
(r ↔ s_i), so X₁ stays in the world; stage 2 removes X₂'s old-r vertices (now s_j) from the world
and ADDS X₂'s old-s_j vertices (now r) — n_sj among them. So a Δ-YES path must use new-r material
of X₂: **the second swap's recolored s_j-vertices bridge B₂'s (r,s_i)-chain to the far
singleton.** This is Heawood's interference, located to one chain and one stage.

# 4. DGT: derived on Δ-NO, floored on Δ-YES; the obstruction named

**On the Δ-NO class** (for W_i or, by mirror, W_j): the image is directly insertable, hence
lies in 𝒯 (under either reading of the target set), so d_gate(W·c₀) = 0 < d_gate(c₀). **DGT
holds, with a fully legal witness, by derivation; and OWL holds there too.**

**On the Δ-YES class (both words):** the image is a saturated gap-2 configuration whose τ is
undecided by the derivation. DGT would follow from any of: (i) the image is unstuck (τ ≤ 5) —
then d_gate = 0; (ii) some OTHER family word descends — the Aiming Existential; (iii) a
structural theorem that Δ-YES forces something τ = 6 cannot afford (the Middle-Strict style of
argument on the reconnection path). None is derived here. **The obstruction, named for Casey's
desk:** *after the two forced swaps of W_i, the recolored s_j-material of the second chain can
reconnect the near bridge copy's (r,s_i)-chain to the far singleton; when it does, the word's
image is again a saturated gap-2 configuration, and nothing derived decides whether it is
stuck.* The question with a kill test: **is the Δ-YES-AND-STUCK class empty?** If yes, W_i and
W_j alone prove OWL (two words, one dichotomy each). If no, the hitting set is larger than two
and the pattern table must grow — E-B decides which.

**Escort request (Elie):** on the 2,927, for W_i and W_j: count Δ-NO / Δ-YES per configuration
(membership of the far singleton in the near copy's (r,s_i)-chain at c₂); in Δ-YES, count images
with τ ≤ 5 vs τ = 6; report k/N with can-fail. Positive control: Lemma L predicts stage-4 legal
2,927/2,927 for both words — a single illegal stage is a bug in my labeling or a theorem error,
re-opened at once. Pre-score: if Δ-NO ∪ (Δ-YES ∧ τ≤5) = all, OWL's proof for these two words is a
two-branch case analysis with one open branch that is measured EMPTY (still not proved); if not,
E-B's hitting set exceeds two and this table is its first two rows.

# 5. OWL ⟹ DGT (one line) and the loose bound

If OWL holds at c₀ with witness w, then w·c₀ ∈ 𝒯 (directly insertable, or τ ≤ 5 under the gate
reading), so d_gate(w·c₀) = 0 < d_gate(c₀). ∎ Conversely DGT ∧ 4CT gives termination in
≤ d_gate(c₀) words + 1 freeing swap (the Assembly's old count clause), which is honest but
LOOSE: under OWL the depth is one word, and the metric leaves the statement. DGT is therefore a
corollary of the last lemma, not a route to it; its standalone value is as a weaker
Kempe-connectivity candidate (class-qualified per E-A's pre-score).

# 6. Inputs (every lemma consumed, by name and status)

| Input | Used at | Status |
|---|---|---|
| 4CT (Appel–Haken; RSST) | frame (d3): 𝒯 ≠ ∅ | external theorem, stated as input |
| One-Context Lemma (L1) | Section 1 setting | derived 09-01; Cal re-derivation PASS; registration pending |
| Whitney 3-connectivity → link is a simple cycle | link edges | K1834 S3, re-derived |
| Definition 5 / τ | 𝒯, "insertable" | K1832-verified |
| Lemma L (Legality) | Sections 2–4 | derived here (partition + bookkeeping) |
| Lemma D (Dichotomy) | Sections 3–4 | derived here (L + link edges + bookkeeping) |
| Two-Agreement Barrier (T2588; was T2586 before the K1837 merge), capture arithmetic | NOT consumed (sign-only route not closed) | proved; standing |
| Bridge-term constant / alternation count a | NOT consumed | labeled, own session (Cal §817) |
| J1′ (patch-locality) | NOT consumed here; ingredient of the unclosed sign-only route only | measured 1,822/1,822; struck as Assembly condition (see v2) |

**Frame check (arguments travel with their frames):** every chain above is computed in T−v with
T's embedding present (K1834 S4); the link cycle is v's link in T. No H-frame, no contraction,
no edge added.

— Lyra. Asked to derive a descent, I found the descent is not the mechanism: the mechanism is a
four-stage word whose fate is decided at stage three by a single chain membership. Half the
world is proved by a table. The other half has a name, an address, and a counter waiting.
