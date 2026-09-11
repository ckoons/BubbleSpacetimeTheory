# K1882-PRE-A — the fork decided by the math, not by a ruling

**Keeper, 2026-09-08 (Tuesday) 10:04 EDT, clock-verified.** Casey, 10:04: "To be fair and honest, the math needs to decide and not for me to make a ruling." This note is the decision as the algebra gives it; Cal scores it blind before it registers.

## 1. What a reset has to be, if it is a law
The record space carries one structure: the action of G, and at a bulk point the isotropy K = SO(5) × SO(2). A reset that is a LAW of the substrate can use only that structure — it cannot take an input the substrate does not supply. So a lawful reset is **SO(5)-covariant**: R(g·ρ) = g·R(ρ) for every rotation, and its output, the survivor, must be a well-defined object of the record space with no external label.

## 2. Schur decides between the two rows
- **On vectors.** A linear SO(5)-equivariant map from the angular block H_k (irreducible, k > 0) to the SO(5)-invariants (the trivial representation) is ZERO — Schur's lemma. This is Elie's 5726 P1 as a theorem, not a computation: **no linear covariant reset carries a k > 0 word onto a vector survivor.** The (D) map is not equivariant at all: its target ℂ[z·z, z·ξ] is not an SO(5)-invariant subspace, so "equivariance" is not even defined for it. (D) breaks the symmetry BY ITS TARGET, and the ξ it needs is an input the substrate does not supply.
- **On states.** The SO(5)-covariant channels whose output is SO(5)-invariant are exactly the maps that factor through the twirl ρ ↦ ∫ g ρ g† dg (any covariant map with invariant output is unchanged by pre-composing with the twirl, and the twirl is idempotent). Followed by any classical map on the labels (j, k). The one that keeps the clock is "forget k," K1860 §G's rule. **So the twirl-then-forget-k channel, (C), is the unique lawful reset up to the classical relabeling of (j, k), and every member of that class carries the same information: H(j) = 4.02 / 10.16 / 12.15 bits (Round 132: k is a function of j at the stop).**

## 3. What (D) is, in these terms
(D) becomes lawful only if ξ is a FUNCTION OF THE STATE — e.g. the direction of maximal zonal overlap, ξ*(Y) = argmax_ξ |⟨Y_k, Z_k^ξ⟩|. That map is covariant (ξ*(gY) = g ξ*(Y)) but NONLINEAR: it is a measurement of the direction, and its output weight is the best zonal fit of the saturated state, which needs a Born reading to mean anything (Cal §910 C1). **So (D) = (C) followed by a measurement of the axis.** The corpus posits no measurement at the reset; K1860-P's writes are isometries, and no row says the reset collapses. Without that posit, (D) is not on the table. With it, (D) is a Born row of its own, and it should be written as one, not as a reset.

## 4. Where the direction went
Round 133's dilation is what makes this decision painless: under (C) the angular content is not destroyed, it is traced out into the environment (K1860 line 14, "put beyond a horizon"), where a direction lives at full weight. Casey's "one dimension closes down" and his "information selected and passed on" are then statements about the ENVIRONMENT and about RE-ENTRY (Round 133 E2/E3), not about the survivor. The survivor is a clock; the direction waits outside the horizon. That is a stronger version of his sentence than (D) offered, because it needs no measurement and no external ξ.

## 5. Decision as the algebra gives it (for Cal's blind score, then Grace)
- **The reset is (C).** Forced: covariance (a law uses only the substrate's structure) + Schur (on vectors) + the twirl's universality (on states). Tier: DERIVED given the definition "a lawful reset is covariant"; that definition is the one posit, and it is the weakest possible one — it says the reset takes no outside input.
- **(D) is not a competing reset;** it is (C) plus a Born measurement of the axis, POSITED nowhere. Lyra's (D) row stays in the file as "what a measurement at the reset would keep," with its norm theorem (|a−b|³) intact as mathematics.
- **Registration:** Lyra's row (C) — "a probability distribution on the winding number; measured 4–12 bits" — meets Cal's §909(5) one-map condition; the bulk-point survivor paragraph of L2 registers in the (C) category (distribution on j, not a subspace).
- **For Elie (E4, hashed):** the canonical-(D) weight, max_ξ |⟨Y_k, Z_k^ξ⟩|²/(‖Y_k‖²‖Z_k‖²), for the chain's product states at k = 2, 5, 10, 20 — the size of what a measurement would have to keep; if it is O(1) the Born row would have content, if it is O(1/dim) it would not.

— Keeper
