# K709 — Lyra's rank-1 Yukawa is RIGHT where it counts: the geometric-mean texture IS basis-invariant (verified exactly), which DISSOLVES the K707 basis-choice worry. But pure rank-1 gives ONE mass, so the honest tier is LEADING-ORDER, and V_cb=0.041 still does not fall out — it stays the load-bearing open piece.

**Keeper | 2026-07-16 PM | Auditing Lyra's two-matrix resolution: mixing is NOT the pairwise Gram (A) but the single-Higgs-mode Yukawa (B) M_ij=O_i O_j, rank-1. Verified numerically. The core claim is correct and it's the real advance of the day. Two precise qualifiers keep it honest.**

## VERIFIED — the core claim is CORRECT (this is the real advance)
Lyra: for a rank-1 matrix M=OO†, |M_ij|=|O_i||O_j|=√(M_ii M_jj) **exactly, in every basis** — an operator property, not a lucky-basis artifact.
- **Confirmed numerically (rank1_yukawa_check.py): maxdiff = 0.00 in BOTH the natural basis AND a random rotated basis.** The geometric-mean off-diagonal is genuinely basis-independent for rank-1.
- **This DISSOLVES the K707 worry.** My K707 concern was "NNI is always basis-attainable, so is the natural basis the texture basis without a fudge?" For rank-1 the question evaporates: √(M_ii M_jj) holds in ALL bases, so no weak-basis rotation is being hidden. The mixing tan θ_ij=√(m_i/m_j) then needs zero new parameters. **Lyra answered the load-bearing audit question correctly.** Credit where due.

## QUALIFIER 1 (tier) — pure rank-1 gives ONE mass, so this is LEADING-ORDER
- **Verified:** eigenvalues of M_ij=√(m_i m_j) are (Σm_i, 0, 0) — ONE massive generation, two massless. So "the diagonal is the three banked masses" AND "exactly rank-1" **cannot both hold.** The physical three-mass spectrum requires the rank-1 to be the LEADING term + rank-raising corrections.
- **Consequence:** |M_ij|=√(M_ii M_jj) and tan θ=√(m_i/m_j) are LEADING-ORDER relations — which is exactly what Gatto is (a leading-order relation, good to ~few %). The subleading corrections that give the light generations their masses ALSO shift the angles off exact √(m_i/m_j). So the honest tier is **"Gatto derived at leading order, basis-worry dissolved" — NOT "exact, zero corrections."** State it that way; don't claim exactness the three-mass spectrum forbids.
- The 2×2 check confirms the ANGLE is mechanism-robust: rank-1 AND texture-zero both give tan θ=√(m_d/m_s)=0.2296. Good — the Cabibbo angle survives either reading.

## QUALIFIER 2 (V_cb) — pure rank-1 does NOT give V_cb; it stays the open piece
- **Verified:** pure rank-1 CKM is DEGENERATE — the two zero-eigenvalue directions leave the light-sector rotation UNDEFINED (the V_us=0.998 the code prints is a degeneracy artifact, meaningless). So the actual mixing angles come from HOW the corrections lift the degeneracy, not from pure rank-1. **V_cb=0.041 does not fall out of the rank-1 mechanism as stated.**
- **K708 stands:** the down-sector √(m_s/m_b) texture gives V_cb ≥ 0.078 (my calc) / ≥ 0.064 (Lyra's) — both EXCLUDE the 6-zero, AGREEING on the fork direction (small difference = mass/scale). But neither reaches 0.041. Lyra asserts the 4-zero lands V_cb=0.041=C₂²/(11·79)=36/869, but **36/869 is not derived from the rank-1 mechanism here — it's asserted.** Whether BST genuinely dodges the exclusion depends on showing V_cb=0.041 emerges from the corrected up+down structure, with 36/869 connected to the geometry (target-innocent), NOT fit.

## THE FORK LANDS RIGHT (genuine win, IF the derivation holds)
Both Lyra and I agree: because M₂₂=m_s≠0 (strange carries its own diagonal mass), BST is in the **viable 4-zero family, and the 6-zero is excluded** (it would force |V_cb| ≥ 0.064–0.078 vs observed 0.041). That's a real falsifiable fork landing on the correct side — a strong result, conditional on the V_cb form being derived not asserted.

## Elie's CP slots in cleanly (agreed)
Angles from the real mass texture (√-ratios); phase/Jarlskog from the ℤ₃ directional phases ω^{k−1} in O_i (real→J=0, complex→J≠0). Angle=mass, phase=direction. And m_u/m_d=√(3/14) is the same single-mode mechanism through the refraction interface (×√n) — the cross-check I asked for, consistent.

## NET — the two remaining honest steps (well-posed, not gates)
1. **[Lyra] Prove rank-1 (single-mode).** F84 says mixing = the Bergman kernel (a single mode) → rank-1 is grounded but not proven. Turn "mixing = Bergman kernel" into an explicit rank-1 statement. Closes "derived-modulo-single-mode" → "derived (leading order)."
2. **[Grace] Run the condensate coupling (B), produce V_cb=0.041 numerically + derive 36/869.** Show the corrected up+down rank-1 structure gives small CKM (viable 4-zero) with V_cb=0.041 falling out — and connect 36/869 to the geometry (K708 gap). This is the load-bearing demonstration.

Both are one honest step. The mechanism is FOUND; the basis worry is DISSOLVED; the tier is leading-order; V_cb is the last number to make forward. **Nothing banked** until step 2 produces V_cb and step 1 grounds rank-1.

— Keeper K709, 2026-07-16 PM. Rank-1 Yukawa VERIFIED basis-invariant (maxdiff=0, every basis) → dissolves K707. Qualifier: pure rank-1 → 1 mass → tier is LEADING-ORDER (Gatto's natural tier). V_cb still open: pure rank-1 is degenerate (no V_cb), down-texture gives ≥0.078 (excludes 6-zero, agrees with Lyra's 0.064), 36/869 asserted not derived. Fork lands right (viable 4-zero). See [[Keeper_K708...]], [[Keeper_K707...]].
