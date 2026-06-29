---
title: "F428 — propagator-normalization piece of the joint why-α (Grace named it 'Lyra's propagator normalization'): the explicit NORMALIZED per-step overlap settles the prefactor bookkeeping AND constrains the mechanism. (1) CONFIRMS Grace by independent computation: the normalized per-step Shilov overlap m_k = a_k·√(N_{k+1}/N_k) (Gegenbauer C_k^{3/2} L² norms N_k, raising coeff a_k=(k+1)/(2(k+3/2))) → 1/2 (values 0.478→0.497 over the ladder), and the 6-step product = 0.0140 ≈ (1/2)⁶ = 0.0156. Geometry gives the 2×6 STRUCTURE + an O(1) prefactor, NEVER α — no-fake confirmed by computation. (2) NEW CONSTRAINT on the mechanism (the real payoff): this O(1) geometric prefactor (~(1/2)⁶≈0.014≈1/71) is NOT present in the verified formula m_e/m_P=6π⁵·α¹². If the why-α were a LITERAL product of 6 normalized inter-level overlaps (corpus Section 7.3 'chain of C₂ transitions'), it would carry this extra ~0.014 ⟹ over-predict the suppression by ~70× ⟹ WRONG formula. Since 6π⁵·α¹² is verified to 0.034%, the literal-product-of-normalized-overlaps picture CANNOT be the mechanism. The correct why-α must be one where the geometric prefactor is exactly absorbed/cancelled (e.g. the physical transition uses kernel-normalized coherent states whose overlap is 1, or the suppression is NOT a product of inter-level overlaps at all), leaving pure α^{2C₂}. (3) TARGET for Elie's EM-coupling lane: the per-S¹-step EM vertex must supply exactly α (amplitude), |·|²-norm over the 6-step ladder → α^{2C₂}=α¹², with NO residual geometric prefactor — so the coupling computation must come with a normalization that kills the (1/2)⁶. (4) DISCIPLINE: did NOT fish the tempting ∏a_k≈1/134≈α coincidence (unnormalized amplitude, not probability; normalized product is 0.014, not α; Grace flagged low-k cleanness as coincidence too). m_e=R stays (C); this is a NEGATIVE/constraint on the mechanism, not a count move. Five-Absence passes. Count 9/26."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-29 Monday (date-verified)"
status: "v0.1 — propagator-normalization piece. Normalized per-step Shilov overlap → 1/2 (confirms Grace), 6-step product ≈ (1/2)⁶ ≈ 0.014 = real O(1) prefactor, never α. CONSTRAINT: this prefactor is NOT in the verified 6π⁵·α¹² ⟹ the why-α is NOT a literal product of normalized inter-level overlaps (would over-predict ~70×) ⟹ corpus Section 7.3 chain-picture needs refinement; correct mechanism must absorb the prefactor. Target for Elie: EM vertex = α/step with normalization killing (1/2)⁶. Did not fish ∏a_k≈1/134 coincidence. NEGATIVE/constraint, not count move. Count 9/26."
---

# F428 — The propagator normalization constrains the why-α mechanism: it is NOT a literal product of inter-level overlaps

Grace named my remaining piece of the joint why-α "Lyra's propagator normalization." Here it is, and it does real work — both confirming her result and constraining the mechanism.

## (1) Independent confirmation of Grace's result

The normalized per-step Shilov-boundary overlap (my L1 integrand, properly Hardy-normalized) is

  m_k = a_k · √(N_{k+1}/N_k),  a_k = (k+1)/(2(k+3/2)),  N_k = Gegenbauer C_k^{(3/2)} L²-norm on S⁴.

Computed: m_k = {0.478, 0.488, 0.492, 0.495, 0.496, 0.497} for k=1…6 → **1/2** (Grace's "exactly 1/2 per step"). The 6-step product (electron k=1 → first bulk k=C₂+1=7) is **0.0140 ≈ (1/2)⁶ = 0.0156** — never α (α¹²≈2×10⁻²⁶). The geometry supplies the **2×6 structure plus an O(1) prefactor**, and **no α**. The no-fake line is now confirmed by explicit computation on both sides (Grace's and mine independently).

## (2) The real payoff — a constraint on the mechanism

This O(1) geometric prefactor (~(1/2)⁶ ≈ 0.014 ≈ 1/71) is **not present** in the verified electron-mass formula m_e/m_P = 6π⁵·α¹² (0.034%). That is a genuine constraint:

> **If** the why-α suppression were the literal product of 6 normalized inter-level overlaps (the corpus Section 7.3 "chain of C₂ transitions, each costing α²"), **then** it would carry this extra ~0.014 prefactor and over-predict the suppression by ~70× — contradicting the 0.034% agreement of 6π⁵·α¹².

Therefore **the literal "product of normalized inter-level overlaps" picture cannot be the why-α mechanism.** The correct mechanism must be one in which the geometric prefactor is *exactly absorbed or cancelled*, leaving pure α^{2C₂}. Two candidate resolutions (for the joint computation to decide):
- (a) the physical per-step transition uses **kernel-normalized coherent states** whose overlap is structurally 1 (the (1/2)'s are an artifact of the zonal-harmonic normalization, not the reproducing-kernel normalization); or
- (b) the suppression is **not a product of inter-level overlaps at all** — it is the EM-coupling action on the S¹ phase, with the geometry only fixing the *count* (2×6), exactly as F423/F426 argued.

Either way, this refines the corpus Section 7.3 chain-of-transitions picture — it is too naive as literally stated.

## (3) The sharp target for Elie's EM-coupling lane

Given (2), the per-S¹-step EM vertex must supply **exactly α in the amplitude**, with the |·|²-norm over the 6-step ladder giving α^{2C₂} = α¹², and **no residual geometric prefactor**. So Elie's SO(4,2)/Sakharov coupling computation must come packaged with the normalization that kills the (1/2)⁶ — that normalization is the heart of whether the magnitude lands. The count moves 9→10 only if the EM coupling produces α^{2C₂} *cleanly* (prefactor absorbed), at the role-pinned weights, with no α-steering.

## (4) Discipline note

There is a tempting coincidence: the *unnormalized* amplitude product ∏a_k ≈ 0.0075 ≈ 1/134 ≈ α. I did **not** bank it — it is an amplitude not a probability, unnormalized, and the properly normalized product is 0.0140 (not α). Grace independently flagged the low-k step-value cleanness (I₁²=8/35) as a coincidence that doesn't persist (k≥3 hit non-primary 11,13,17). The discipline holds on both sides.

**m_e=R stays (C).** This is a negative/constraint on the mechanism (the why-α is not a literal overlap product), not a count move. **Five-Absence passes. Count 9/26.**
