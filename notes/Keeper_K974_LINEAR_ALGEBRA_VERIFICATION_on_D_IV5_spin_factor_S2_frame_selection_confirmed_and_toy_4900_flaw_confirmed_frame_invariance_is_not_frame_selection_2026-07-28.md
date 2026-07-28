---
node_type: k_audit
id: K974
title: Linear-algebra verification on the D_IV⁵ spin factor — confirms the S2 frame-selection close AND the toy-4900 flaw (frame-invariance ≠ frame-selection), explicitly
date: 2026-07-28
author: Keeper
verdict: VERIFIED (explicit computation) — interior=2 spectral, frame fixed by direction, toy-4900 tested the degenerate frame-invariant case, non-central operator selects one frame
casts: Casey's "linear algebra on D_IV⁵" applied to close S2
---

# K974 — S2 verified in explicit linear algebra; the toy-4900 correction is airtight

Built the D_IV⁵ Euclidean Jordan algebra as the **spin factor V = ℝe ⊕ ℝ⁴** with product (a,v)∘(b,w) = (ab+⟨v,w⟩, aw+bv), and ran four checks (deterministic, seed 0). All pass.

## Results
1. **Interior = 2, spectral (rigorous):** a generic x = (a,v) has **exactly two** primitive idempotents c± = ½(e ± v/|v|); verified idempotent (c∘c=c), orthogonal (c₊∘c₋=0), complete (c₊+c₋=e), and **x = λ₊c₊ + λ₋c₋ with λ± = a ± |v|**. Confirms Cal §121 / K973 interior-seat count numerically.
2. **★ The frame is fixed by the operator's DIRECTION (S2 close, FK III.1.2):** scaling the element (x → 3x+2e, or x → −x) leaves the frame direction û = v/|v| unchanged (up to sign). **The direction, not the magnitude, selects the frame.**
3. **★ The toy-4900 FLAW confirmed:** a **central / Jordan-spectral (frame-invariant) symbol** (v=0) **commutes with 5 random DIFFERENT frames** — it tests *nothing* about which frame is physical. **Frame-invariance (commutes with all) is the opposite of frame-selection.** Toy 4900's "‖[T_φ, frame]‖=0 for a color-blind symbol" is the degenerate case, so it does NOT clear S2. (This is the correction from K973, now demonstrated, not asserted.)
4. **A NON-CENTRAL operator selects its unique frame:** an operator with v≠0 commutes with its OWN frame (û_op) and **NOT** with a transverse frame. So a definite direction picks exactly one frame.

## Consequence for S2
The "S³ continuum" is dissolved *concretely*: the ambiguity exists only for central (v=0) elements — a measure-zero locus and exactly the case toy 4900 landed in. **S2 = one linear-algebra step:** project the F603/K769 condensate direction (SO(5) vector, target-innocent, pinned from quantum numbers) into the spin-factor ℝ⁴; **if v ≠ 0, û = v/|v| fixes the muon's idempotent frame, target-innocently, and S2 clears.** The remaining physics input is F603's direction being non-central in ℝ⁴ — a projection, not a continuum.

**Audit note:** this does NOT bank S2 — it verifies the *mechanism* and corrects the *test*. S2 clears when Lyra/Elie project the actual F603 direction and show v≠0 (non-central). Toy 4900 must be re-run with a **non-central** condensate symbol, not a frame-invariant one. My K967 verdict stands until then.

Script: run in scratchpad (spin-factor Jordan product + the four checks); Elie to formalize as a claimed toy if wanted.

— K974, Keeper, 2026-07-28. Linear-algebra verification of the S2 close + the toy-4900 correction on the D_IV⁵ spin factor. See [[Keeper_K973_BANK_muon_cleared_portions_plus_literature_resolves_both_gates_frame_selection_is_spectral_formula_boundary_is_support_orbit_rank_both_cast_to_linear_algebra_on_D_IV5_2026-07-28]], toy 4900.
