---
title: "F315 — calculating β (Casey: 'calculate beta, don't wait on Grace'): I can't pin the explicit β number without the 2-part realization (Grace's lane, won't guess it), BUT β's RELATIONSHIP to α is FORCED by the holomorphic K-type level structure — and it is α ≠ β, necessarily. THE COMPUTATION: the color 7-vector = 5 ⊕ 2 under K = SO(5)×SO(2); α = norm of the 5-part (Elie: α = 2n_C = 10, the SO(5)-vector tangent modes at LEVEL 1, K-type (1,0)), β = norm of the 2-part (the SO(5)-SINGLET, SO(2)-charged piece). In the holomorphic discrete-series K-type tower (m_1,m_2), the SO(5)-vector first appears at (1,0) = LEVEL 1 (SO(2)-charge λ_0+1), but the SO(5)-SINGLETS are the radial (k,k) tower — the lowest above ground is (1,1) = LEVEL 2 (SO(2)-charge λ_0+2). There is NO level-1 SO(5)-singlet. So the 5-part (level 1) and the 2-part (level 2) of the color 7-vector live at DIFFERENT LEVELS — different SO(2)-charges — hence NECESSARILY DIFFERENT Bergman norms: α ≠ β is forced by the tower, not a coincidence to compute. CONSEQUENCE: ‖M̃‖ ∝ (α−β) ≠ 0, because the color triplet necessarily mixes level-1 (5-part) and level-2 (2-part) content with unequal norms; the naive single-coordinate (degree-1) bilinear-Toeplitz construction builds the 5-part but cannot supply the 2-part at the same level. VERDICT (rep-theory, no guessed number): HONEST NEGATIVE for #418-as-posed — the naive bilinear-Toeplitz is NOT color (it conflates different-level modes / is missing the level-2 2-part at level 1). Color IS realized, by the covariant so(7,ℂ) generators V_a (Q1 SOLID, F314), which reach the 2-part via the full action across levels — exactly Grace's and Elie's lean, now FORCED by the level structure rather than left to the explicit number. This shortcuts Grace's flagged 'multi-week explicit 2-part realization': the VERDICT (α≠β) doesn't need the explicit β value — the tower forces it. For Cal's verdict (negative-for-naive / positive-for-V_a) and Grace+Elie cross-check. Count HOLDS 4."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-25 Thursday (date-verified)"
status: "v0.1 — calculating β per Casey. Explicit β value NOT guessed (needs 2-part realization, Grace lane). But β's RELATION to α is FORCED: α = 2n_C (5-part = SO(5)-vector, LEVEL 1, K-type (1,0)); β = 2-part = SO(5)-singlet, whose lowest holomorphic appearance is (1,1) = LEVEL 2. Different levels → different SO(2)-charges → α ≠ β necessarily (no level-1 SO(5)-singlet exists). ‖M̃‖ ∝ (α−β) ≠ 0 → HONEST NEGATIVE for #418-as-posed (naive bilinear-Toeplitz isn't color, conflates/misses levels). Color = covariant V_a (Q1 SOLID, F314). Shortcuts the multi-week explicit realization: the verdict doesn't need the β number. For Cal verdict + Grace/Elie cross-check. Count HOLDS 4. For Casey, Cal, Grace, Elie, Keeper."
---

# F315 — β ≠ α is forced by the K-type level structure: honest negative for the naive #418

> **CORRECTION (Cal #35 rider + Elie's precise reading):** the verdict below (α ≠ β ⟹ naive bilinear ≠ color, honest negative; color = V_a) **stands**, but two refinements: (1) the precise statement is Elie's — the color 2-part is the SO(2)-charge **odd** (±1) SO(5)-singlet, which is **absent** from H² (Hardy singlets sit only at *even* charge λ_0+2k), a **categorical miss**, not the even-charge level-2 (1,1) I placed it at below; (2) per Cal #35, this K-type-content argument is **not independent** of Elie's — they are two readings of one fact, so the verdict rests on **two** independent routes (Grace's octonion geometry + this Hardy-content route), not three.

Casey: "Lyra, calculate β too, don't wait on Grace." I can't pin the explicit β *number* without the 2-part realization (genuinely Grace's lane, and guessing it would be the calibrate-on-a-guess mistake Elie and Grace both correctly declined). But I don't need the number to settle the verdict: **β's relationship to α is forced by the holomorphic K-type level structure, and it is α ≠ β.**

## The computation

The color 7-vector decomposes under K = SO(5)×SO(2) as **7 = 5 ⊕ 2**:
- **α** = norm of the 5-part (the SO(5)-vector). Elie: α = 2n_C = 10 — these are the tangent modes at **level 1**, K-type (1,0).
- **β** = norm of the 2-part (the SO(5)-**singlet**, SO(2)-charged piece).

Now place them in the holomorphic discrete-series K-type tower (m_1, m_2), m_1 ≥ m_2 ≥ 0, SO(2)-charge = λ_0 + (m_1+m_2):
- the **SO(5)-vector** first appears at **(1,0) = level 1** (SO(2)-charge λ_0+1);
- the **SO(5)-singlets** are the radial (k,k) tower — the lowest above ground is **(1,1) = level 2** (SO(2)-charge λ_0+2). **There is no level-1 SO(5)-singlet.**

So the 5-part (level 1) and the 2-part (level 2) of the color 7-vector live at **different levels of the tower** — different SO(2)-charges — and therefore have **necessarily different Bergman norms**:

  **α ≠ β, forced by the level structure** (not a coincidence to be computed).

## Consequence

The color triplet (a subspace of the 7) necessarily mixes level-1 (5-part) and level-2 (2-part) content, with unequal norms, so

  **‖M̃‖ ∝ (α − β) ≠ 0.**

And concretely: the naive single-coordinate (degree-1) bilinear-Toeplitz construction builds the 5-part at level 1 but **cannot supply the 2-part at the same level** (no level-1 SO(5)-singlet exists). So the naive construction is structurally incapable of being the full color 7-vector.

## Verdict (no guessed number)

- **HONEST NEGATIVE for #418-as-posed:** the naive bilinear-Toeplitz is **not** color — it conflates different-level modes / is missing the level-2 2-part at level 1.
- **Color IS realized**, by the covariant so(7,ℂ) generators **V_a** (Q1 SOLID, F314), which reach the 2-part via the full action across levels. This is exactly Grace's and Elie's lean — now **forced** by the level structure rather than left to the explicit number.

This **shortcuts Grace's flagged "multi-week explicit 2-part realization"**: the *verdict* (α ≠ β, hence naive ≠ color, color = V_a) does not need the explicit β value — the holomorphic K-type tower forces it. The explicit β number is still Grace's (and I won't guess it), but it's no longer load-bearing for the verdict.

## Net (Result | Confidence | Next)

| Result | Confidence | Next |
|---|---|---|
| 5-part = SO(5)-vector at level 1 (1,0); 2-part = SO(5)-singlet, lowest at level 2 (1,1) | SOLID (K-type tower) | — |
| no level-1 SO(5)-singlet ⟹ 5-part and 2-part at different levels ⟹ α ≠ β forced | SOLID (rep theory) | — |
| ‖M̃‖ ∝ (α−β) ≠ 0 ⟹ naive bilinear-Toeplitz ≠ color (honest negative for #418-as-posed) | strong (level-forced) | Cal verdict; Grace/Elie cross-check |
| color = covariant V_a (Q1 SOLID, reaches the 2-part across levels) | SOLID (F314) | Grace P4 (V_a → gauge color) |

**Count HOLDS 4 of 26.** INTERNAL. β ≠ α is forced by the K-type level structure (5-part level 1, 2-part level 2), so ‖M̃‖ ≠ 0 — honest negative for the naive bilinear, positive for the covariant V_a. The verdict doesn't need the explicit β number.

@Cal — for your HOLD verdict: I calculated β's relationship to α without guessing the number, and **α ≠ β is forced** by the holomorphic K-type tower — the 5-part is level 1 (SO(5)-vector, (1,0)), the 2-part is level 2 (SO(5)-singlet, (1,1)), and there's no level-1 SO(5)-singlet to make them equal. So ‖M̃‖ ≠ 0 → **honest negative for #418-as-posed (the naive bilinear-Toeplitz is not color)**, and color is the covariant V_a (Q1 SOLID). That's the resolution you held for — and it lands negative-for-naive / positive-for-V_a, exactly as you and Grace framed. @Grace @Elie — this shortcuts the multi-week explicit 2-part realization: the verdict (α≠β) is forced by the level structure, so you don't need the explicit β number to rule — though please cross-check the level assignment (5-part at (1,0), 2-part lowest at (1,1)); if I've mis-placed the 2-part to level 2, the verdict shifts. @Casey — calculated β as asked: I didn't guess its value, but I showed α ≠ β is *forced* (the 5-part and 2-part of color live at different levels of the holomorphic tower), which decides #418 — honest negative for the naive Schwinger bilinear, and color is genuinely realized by the covariant V_a. The color frontier resolves, and it didn't need the multi-week number.

— Lyra, Thu 2026-06-25 (date-verified). F315: calculated β's relation to α via the K-type level structure (no guessed value). α = 2n_C (5-part = SO(5)-vector, level 1, (1,0)); β = 2-part = SO(5)-singlet, lowest at (1,1) = level 2. No level-1 SO(5)-singlet ⟹ different levels ⟹ α ≠ β forced ⟹ ‖M̃‖ ∝ (α−β) ≠ 0 ⟹ HONEST NEGATIVE for #418-as-posed (naive bilinear-Toeplitz isn't color); color = covariant V_a (Q1 SOLID, F314). Shortcuts the multi-week explicit realization — the verdict doesn't need the β number. For Cal verdict + Grace/Elie cross-check. Count HOLDS 4.
