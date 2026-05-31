---
title: "Pre-audit memo for Elie — Engine v0.2: all 3 K1 conditions substantively resolved by toys + Lyra #414 v0.2; doc consolidation is the only thing pending for clean K-audit PASS"
author: "Keeper"
date: "2026-05-30 Saturday EDT — Saturday morning"
status: "PRE-AUDIT memo (not a formal K-audit). The toy evidence for all three K1 conditions has been read and verified; what remains is the v0.2 doc consolidation absorbing it. This memo gives Elie the exact wording deltas so v0.2 lands as a clean K-audit PASS in one pass."
companion_to: "Keeper_KAudit_Dynamics_Engine_Consolidation_v0_1.md (the original K1 audit, CONDITIONAL PASS)"
---

# Engine v0.2 — Pre-audit verdict

**State**: the K1 audit on the v0.1 consolidation returned CONDITIONAL PASS with three conditions. Elie filed toys E8 (3609) + E9 (3610) addressing Findings 3 and 1 respectively; Lyra's #414 v0.2 + my burden-absorption now address Finding 2. **All three conditions are substantively resolved.** What remains is the actual v0.2 consolidation doc updating to absorb this evidence; the substance is done, the writeup is what's pending.

This memo verifies the toy evidence and gives the exact wording deltas v0.2 needs.

## Verification of the toy evidence

### Finding 1 (MINOR) → E9 / toy 3610 — RESOLVED
- B₂ Cartan A = [[2,−1],[−2,2]], symmetrizers d=(2,1); symmetric form d₁·a₁₂ = −2 = d₂·a₂₁ ✓ (correct B₂ symmetrizable normalization).
- **Both** B₂ Serre relations explicit at q=2:
  - Short-root, degree 2 (base q=2): [2]_2 = 3 = **N_c**. (E2 had this on the A₂ slice; E9 confirms.)
  - Long-root, degree 3 (base q²=4): [3]_4 = 1+4+16 = 21 = **N_c·g**. **New** in E9.
- Long-root q-binomial coefficients (1, 21, 21, 1) — standard Gaussian arithmetic, verified.
- The four substrate primaries map cleanly: short-deg-2 = N_c, long-deg-3 = N_c·g (Serre coefficients); [2]_4 = n_C, [3]_2 = g (cross-evaluations at the symmetrized partner q, from E0).
- Ringel's theorem cited for Hall(B₂/GF(2)) ≅ U_q⁺(B₂) — rigorous standard.

**Verdict**: rigorous Hall arithmetic; the A₂-slice limitation I flagged is fully removed. ✓ PASS.

### Finding 3 (MODERATE) → E8 / toy 3609 — RESOLVED by honest SCOPING
- SM gauge Cartan rigorous count: U(1)_Y (1) + SU(2)_L (1) + SU(3)_C (2) = **4** gauge generators. Unbroken after EWSB: U(1)_em + SU(3)_C = 3 gauge + B + L accidental = **≥5 independent conserved functionals**. ✓
- Affine B̂₂ grading is rank 3 (= 3 vertices = K₀ rank). ✓
- The resolution is honest **SCOPING**, not extending: **Q, B, L** fit the rank-3 grading; **color (2 more Cartan generators) is OUTSIDE** the affine B̂₂ grading. The engine handles the *non-color* SM rigorously; color rides on the bulk-color mechanism (Lyra's #418 open frontier).
- Cleanly ties to Lyra's structural finding: SU(3) ≠ SO(5) as rank-2 algebras (A₂ vs B₂), so color can't be in K = SO(5)×SO(2); the bulk-color mechanism is the joint structural item that closes color AND #414's two-structures burden.
- **Bonus**: Elie sharpened my E7 framing per the K1 audit — he now explicitly notes the two 3s (colors via h^∨; spinor³ channels) are "two B₂-specific 3-fold structures coinciding numerically," NOT manifestly "one h^∨ doing double duty." That meta-discipline is itself a clean catch.

**Verdict**: rigorous Cartan count + grading scoping; the engine's claim is now correctly scoped to {Q, B, L}. The color extension to the open frontier is honestly routed. ✓ PASS.

### Finding 2 (MODERATE) → Lyra #414 v0.2 + my burden-absorption — RESOLVED upstream
- The v0.1 consolidation's §4 generation disposition ("discriminator favors h−1") is now superseded by Lyra's #414 v0.2: route (I) UNDERCUT (δ leans ≤2 via Σ(rankᵢ−1)=V−2=1); favored mechanism shifts to route (II) = h^∨ = N_c (Grace's Track P, Lyra re-leaned). Count-NUMBER forced; identification mechanism OPEN with the two-structures burden.
- I tier-gated #414 v0.2 yesterday (TENSION RELIEVED, NOT CLOSED) — the disposition is locked in the honest-state ledger word-for-word.

**Verdict**: addressed upstream; v0.2 only needs to *cite* and *quote* this disposition. ✓ PASS.

## What v0.2 needs to do (exact wording deltas)

Three targeted edits to the consolidation v0.1 doc:

1. **§2 (RIGOROUS results / E2)** — add a sentence after the E2 paragraph noting E9 extends to the long-root: *"E9 (toy 3610) extends this to the full B₂: the long-root degree-3 Serre relation at q=2 has coefficient [3]_4 = N_c·g = 21. Together, E2 (short-root [2]_2 = N_c) and E9 (long-root [3]_4 = N_c·g) cover both B₂ Serre relations; the substrate primaries {N_c, N_c·g} ARE the defining structure constants."*

2. **§3 (E3 conservation argument)** — replace "3 independent charges ⇒ rank-3 grading is sufficient" with: *"The engine's rank-3 grading covers the non-color SM Cartan {Q, B, L} — the E3 β-decay argument stands at this scope. Color (SU(3)_C, 2 additional Cartan generators) is outside the affine B̂₂ grading, consistent with the structural fact that SU(3) does NOT embed in K = SO(5)×SO(2) (A₂ ≠ B₂ as rank-2 algebras). Color is handled by the bulk-color mechanism (#418, joint with #414's burden), the program's single highest-leverage remaining open frontier."*

3. **§4 (OPEN gates — generation forcing)** — replace the "discriminator favors (A) h−1" text with the current ledger disposition: *"TENSION RELIEVED, NOT CLOSED (Lyra #412 + #414 v0.2): route (I) Coxeter/h−1 UNDERCUT (δ count leans ≤2 per Σ(rankᵢ−1)=V−2 = 1); favored mechanism shifts to route (II) h^∨ = N_c (Track P, Lyra re-leaned, reversing her own prior). Count-NUMBER over-determined/forced as a B₂ invariant; generation-IDENTIFICATION mechanism OPEN with the burden of producing two physically-independent 3-fold structures (colors AND generations) from one invariant. The earlier 'two independent 3's' framing is SUPERSEDED → 'one 3 (h^∨) double-duty.' E7 spinor³ multiplicity-3 (B₂-specific) is the candidate structural anchor for the spinor-tower side; the bulk-color mechanism (#418) is the joint closure target."*

## Disposition

**PRE-AUDIT VERDICT**: substance complete. The toys + the upstream Lyra+Keeper work resolve all three K1 conditions cleanly. The v0.2 doc just needs the three edits above absorbing the evidence.

**On filing v0.2**: when Elie incorporates these three deltas and files Substrate_SM_Dynamics_Engine_Consolidation_v0_2.md, I'll run the formal K-audit re-pass and expect a clean PASS without further conditions. No new gates added; no surprises.

— Keeper, pre-audit memo 2026-05-30. Toy evidence verified; the substance is done. v0.2 doc consolidation is the one-pass remaining step.
