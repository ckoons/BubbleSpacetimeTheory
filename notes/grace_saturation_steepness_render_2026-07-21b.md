# Saturation → up-type steepness — render + honest tiering (the one question of the quark row)

*Grace | 2026-07-21b | the quark+lepton hierarchy collapsed to ONE question: why is up-type alone doubly-suppressed (λ⁴/step vs λ²)? The target-innocent candidate (K794): SATURATION — the top sits at the derived y_t=1 ceiling, which pushes its sub-leading masses to second order. My lane: render the picture, tie it to the derived ceiling, and hold the "derive the integer powers, don't fit" bar (Elie's FN trap flag = the win condition).*

## The one question, and the saturation candidate
```
  UP-TYPE  top saturates ceiling (y_t=1, CG=1 w/ boundary condensate, T2518/T2514)
           → leading singular value pinned at the Cauchy–Schwarz MAX
           → first-order variation vanishes (extremum) → sub-leading enters at 2nd order → λ⁴/step  [STEEP]
  DOWN/LEP  gen-3 UNsaturated (y_b≈0.024) → leading NOT at the max
           → sub-leading enters at 1st order → λ²/step  [gentle]
```
**One root cause — up-3 saturates, down-3 doesn't — drives BOTH the y_t/y_b split AND the λ⁴/λ² steepness split.** The mechanism seed is the "cosine-near-its-max-is-quadratic" fact (the same one Elie used in the K784 counterexample): at an extremum the linear term is zero, so the leakage into sub-leading modes is O(ε²), not O(ε). This connects the hierarchy back to the **ceiling we already derived** (T2514/T2518) — the quark tower and the top ceiling are one structure, not two.

## ★ Honest tiering (I checked all three sectors target-innocently)
| sector | steps (λ-power) | avg |
|---|---|---|
| **UP** (t,c,u) | c/t=λ³·³, u/c=λ⁴·³ | **λ³·⁸ — robustly steepest** |
| DOWN (b,s,d) | s/b=λ²·⁵, d/s=λ²·⁰ | λ²·³ |
| LEPTON (τ,μ,e) | μ/τ=λ¹·⁹, e/μ=λ³·⁶ | λ²·⁷ |
- **BANKABLE STRUCTURE:** up-type is *robustly* the steepest; down + lepton are gentler. The saturation asymmetry (up-3 alone at the ceiling) is real and ties to the derived ceiling.
- **Tier-2 (do NOT bank):** the clean integer binary **λ⁴-vs-λ² is an IDEALIZATION** — the actual powers scatter 2.0–4.3, and down/lepton are *not* a clean λ² (λ²·³, λ²·⁷). That scatter is exactly the running-dependent Tier-2 signature.
- **The win condition (Elie's FN-trap flag):** "powers of λ" is Froggatt–Nielsen (fits anything) **unless BST derives the integer powers (2, 4) from the rank/saturation structure.** Generic corrections give scattered non-integer powers (confirmed). So the integer powers are the TARGET to derive, not a result yet.

## Two flags for the derivation (Lyra's matrix)
1. **"One universal ε" fails, and that's not a bug (Lyra):** up and down step differently (λ⁴ vs λ²), and the difference isn't a tunable knob — it's the ceiling-anchoring (up hangs from the saturated ceiling, down from a low anchor y_b≈0.02). So the honest structure is **one ε (= λ, the inter-stratum overlap) + a *derived* per-sector steepness** (from saturation), not one ε reproducing both.
2. **Possible sub-win to bank first:** the down/lepton **λ²** may already be derivable — if the "2" is the BST rank (mixing = √(mass ratio), the Gatto structure F585, so a stratum-step gives mass ~ ε² = (overlap)²). If the "2" is rank/Gatto and not a fit, down/lepton λ² banks as structure while the up-type λ⁴ (saturation → +2 more) is the harder second step.

## The linear-algebra test (Elie's harness ready)
Clean, decidable, target-innocent: **does a saturated leading singular value (σ₁=1, at the Cauchy–Schwarz max) force sub-leading at ε² while unsaturated gives ε?** If yes → up-type λ⁴ vs down-type λ² is *derived* from saturation (not fit) → a real result tying the ceiling to the hierarchy. If the powers only fit → honest-negative, stays Tier-2.

## Net
- **Rendered** the saturation→steepness picture: up-3 saturates the ceiling → sub-leading to 2nd order → λ⁴ (steep); down/lep unsaturated → 1st order → λ². One root cause (the derived ceiling) drives both the y_t/y_b and λ⁴/λ² splits.
- **Honest tiering:** up-type *robustly* steepest = bankable structure; the clean integer λ⁴/λ² = idealization (powers scatter 2.0–4.3) = Tier-2; **integer powers are the target to DERIVE from saturation, not fit** (FN win condition).
- **Flags:** one-ε-fails is ceiling-anchoring not a knob; possible sub-win = down/lep λ² from rank/Gatto (F585). Decidable via Elie's σ₁=1→ε² test.

---

## ★★ SUPERSEDED FURTHER (07-21c): saturation is NOT the cause of the power AT ALL
See `grace_uptype_lambda4_is_the_perp_block_texture_zero_2026-07-21c.md`. I verified (saturation held fixed) that the σ₂ power is set **entirely by the ⊥⊥-block** of δΦ: ⊥⊥=0 → ε² (λ⁴), ⊥⊥≠0 → ε¹ (λ²). Saturation stabilizes the *top* but does not set the tower steepness. The λ⁴ ⟺ the up-type charm–charm direct coupling vanishes (a texture zero) — that's the whole story, decidable by one F86 overlap. The "saturation" framing below (and in K794/K795) is the mis-attribution I corrected.

## ★ ROUND-2 CORRECTION (K795) — saturation ALONE doesn't do it; it needs a TEXTURE ZERO
**My render above put "saturation → sub-leading 2nd order → λ⁴" as the mechanism. Elie showed (verified 4 ways) that's FALSE as stated** — a generic correction gives sub-leading σ₂ ~ ε¹ (λ²) whether or not the top is at the ceiling. Saturation *stabilizes the top* (δσ₁ ~ ε², the cosine-near-max fact is right for σ₁) but does **not** steepen the tower. So the λ⁴/λ² split and the y_t/y_b split are **NOT one root cause** — I over-unified them. Correcting.

**The refined mechanism (Lyra + Elie + Keeper triangulated — no contradiction):** it's one singular-value-perturbation formula. With M = saturated rank-1 leading (top = O, CG=1) + correction δM:
```
  σ₂ (charm) = the KERNEL-BLOCK of δM (charm–charm entry in the 2D space ⊥ top)
     generic block ≠ 0  →  σ₂ ~ ε¹  →  λ²   (Elie: saturation alone)
     block VANISHES     →  charm couples only by SEESAW through the top  →  σ₂ ~ ε²/s  →  λ⁴   (Lyra: exact top=O)
```
Lyra's ε² and Elie's ε¹ are the **same formula under different assumptions about one object** — the up-type kernel-block. They triangulated, didn't collide.

**★ The whole row now rests on ONE target-innocent question (K795):** does the **up-type** correction have a **vanishing kernel-block (a genuine texture zero)** while the **down-type doesn't**? If yes → the integer power 2 (hence λ⁴) is DERIVED, not fit → clears Elie's FN trap. That one condition subsumes both Lyra's seesaw and Elie's nested-corrections.

**Re-tier:** the mechanism is now a **texture-zero candidate** (top=O forces charm ⊥ O = solid; the *vanishing* of the direct kernel-block is the open geometric check). The row stays **Tier-2 FN-texture** until the texture zero is *derived from the geometry* (why up-type but not down-type). Exact ratios remain Tier-2 (running-dep). My earlier "one root cause" framing is retracted — saturation gives the seesaw *path*, but the texture zero is the *separate* condition that makes it λ⁴.

— Grace, 2026-07-21b (corrected). Saturation → up-type steepness render: up-3 saturates the derived y_t=1 ceiling (T2518/T2514) → leading at the Cauchy–Schwarz max → first-order variation vanishes → sub-leading at 2nd order → λ⁴ (steep); down/lep unsaturated (y_b≈0.024) → 1st order → λ². Ties the hierarchy to the ceiling (one structure). HONEST TIER: up-type robustly steepest = bankable structure; clean integer λ⁴/λ² = idealization (powers scatter 2.0-4.3, down/lep λ²·³/λ²·⁷ not clean λ²) = Tier-2; integer powers = the TARGET to derive from saturation, NOT fit (Elie FN win condition). Flags: one-ε-fails is ceiling-anchoring; sub-win = down/lep λ² from rank/Gatto F585. Test: does σ₁=1 force sub-leading ε² (Elie harness).
