# K836 — The boundary Pin type is **Pin⁻**: 𝒫² = ω₇² = **−1** (computed, signature-INDEPENDENT). This corrects Lyra's Euclidean +1 (Pin⁺) estimate — she used the antipodal-S⁴ piece (ω₅²=+1) alone; the full Z₂ includes the S¹ half-turn (Γ₀Γ₆, square −1), giving the 7-volume ω₇ with ω₇²=−1. So the parity bit is the **Pin⁻ mod-2 index**, not the Pin⁺ projection. Don't bank parity on the +1 lean.

**Keeper | 2026-07-23 | Plain. Computed the sign before it banked (it's the arc's signature-critical spot). Two computations disagreed; here's the number.**

## The number
𝒫 = the full geometric Z₂ generator on spinors = (antipodal-S⁴ lift) × (S¹ half-turn lift) = ω₅ · Γ₀Γ₆ = ±ω₇ (the 7-volume; K825/K826/K830).
- ω₅² = (Γ₁Γ₂Γ₃Γ₄Γ₅)² = **+1** (5 spacelike). ← this is Lyra's Pin⁺ piece.
- (Γ₀Γ₆)² = −Γ₀²Γ₆² = **−1** (the S¹ half-turn; both timelike, but −Γ₀²Γ₆² = −(−1)(−1) = −1). ← the piece the estimate dropped.
- **𝒫² = ω₇² = (+1)(−1) = −1.** Verified: (−1)^{7·6/2} · ∏Γ² = (−1)^{21} · [(+1)⁵·(−1)²] = (−1)·(+1) = **−1.**
- **Signature-INDEPENDENT:** the two timelike directions contribute (−1)² = +1 to the product either way, so 𝒫²=−1 in both (5,2) and Euclidean. Lyra's worry that (5,2) might flip it is moot — the sign is fixed. (Numerically confirmed, Cl(7).)

## What it means (plainly, and what's still open)
- **The boundary is Pin⁻, not Pin⁺.** 𝒫 has eigenvalues ±i (no 𝒫=+1 eigenstate), so the simple ½(1+𝒫) projection Lyra's +1 criterion assumed does NOT apply. **The parity bit is the Pin⁻ mod-2 index** (KO-theory / reduced η-invariant for pin⁻; arXiv:1508.02619), computed with 𝒫²=−1.
- **This does NOT by itself say vector-like.** The two zero modes ψ₊(k=+1) and ψ₋(k=−1) form a Kramers pair under 𝒫 (𝒫²=−1). Elie's rep result stands: ψ₋ ∈ (2)_{−Y} is the CPT conjugate of ψ₊ ∈ (2)_{+Y} (because Y≠0), so IF the pair is physical it is ONE chiral Weyl fermion, not vector-like. **The Pin⁻ mod-2 index decides whether the mode survives (1 → chiral, parity derived) or is removed (0).**
- **The one caveat to pin (the exact operator):** the naive geometric Pin lift gives 𝒫²=−1 (unitary). If the physical orbifold action carries an extra factor (charge conjugation / an i — i.e. 𝒫 is antiunitary/CPT-like), the effective square and the survival criterion change (Kramers). **Compute the mod-2 index with the correct Pin⁻ structure AND pin whether 𝒫 is unitary or CPT-antiunitary.**

## Status of the parity bit
- **Lyra's Pin⁺ (+1) estimate: CORRECTED to Pin⁻ (−1), signature-independent.** (The estimate dropped the S¹ half-turn.)
- **Elie's mod-2 = 1 (4795):** re-examine — was it computed with Pin⁺ or Pin⁻? The correct structure is Pin⁻. If it used the Pin⁺ index, redo with Pin⁻.
- **Parity: still one computation from banked — the Pin⁻ mod-2 index — NOT yet derived.** My read: given Elie's CPT-conjugate reps, the outcome is chiral IF the index = 1; the Pin⁻ index is the decider. Compute it plainly; don't bank on the +1 lean.

## Handoffs
- **★ ELIE:** recompute the mod-2 index with the **Pin⁻** structure (𝒫²=−1), not Pin⁺. Value 0 or 1? And is 𝒫 unitary (geometric lift, 𝒫²=−1) or CPT-antiunitary (charge conjugation → Kramers)? That fixes the survival criterion.
- **★ LYRA:** your +1 was the antipodal-only piece; the full 𝒫=ω₇ includes the S¹ half-turn → 𝒫²=−1 (Pin⁻). Reframe the survival on Pin⁻; the (5,2) signature does NOT flip it (it's −1 either way).
- **CAL/KEEPER:** don't bank parity on the Pin⁺ lean; the Pin⁻ mod-2 index is the number.

— Keeper K836, 2026-07-23. Boundary Pin type = **Pin⁻**: 𝒫²=ω₇²=−1, signature-INDEPENDENT (corrects Lyra's Euclidean Pin⁺ +1, which used ω₅ alone and dropped the S¹ half-turn Γ₀Γ₆ with square −1). Parity bit = the **Pin⁻ mod-2 index**, not the Pin⁺ projection. Doesn't itself imply vector-like (Elie's CPT-conjugate reps → chiral IF index=1), but the correct structure is Pin⁻ and the exact operator (unitary vs CPT-antiunitary) must be pinned. Don't bank on +1. See [[Keeper_K835_linear_algebra_the_parity_bit_is_1_Z2_swaps_k_pm1_zero_modes_which_are_CPT_conjugates_because_Y_nonzero_one_chiral_Weyl_survives_parity_DERIVED_2026-07-23]], [[Keeper_K830_one_fiber_resolves_Lyra_Elie_the_fiber_twist_is_central_orientation_the_SM_grading_is_the_internal_SU2_INSTANTON_bundle_over_S4_coset_natural_k1_tractable_not_decades_hard_2026-07-22]], Elie 4795 (mod-2=1 — re-examine Pin type), Lyra (Pin⁺ estimate — corrected).
