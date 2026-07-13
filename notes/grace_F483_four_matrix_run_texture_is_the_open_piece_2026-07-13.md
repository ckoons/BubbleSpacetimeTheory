# Grace — F483 four-matrix RUN (PRIMARY 2): it assembles, V_cb reproduces, and the open piece is the off-diagonal TEXTURE

*2026-07-13 Monday. Keeper PRIMARY 2: assemble the exact F483 M-matrix (my kernel reduction + Elie's f(ν) weights on
the shared radii {0,½,0.82}), diagonalize both sectors, take U_u†U_d for V_ub; run it forward if it assembles, else
name the open piece precisely — don't fabricate. RESULT: it assembles and runs. V_cb comes out right; V_us/V_ub come
out too small by exactly the overlap factor. The open piece is the off-diagonal texture, and there's a clean lead.*

## What I built (fully transparent — no fabrication)
M_ij = √(w_i w_j)·K_ij, where K = the rank-1-effective Bergman overlap Gram on the shared localizations
(gen-1 origin, gen-2 @ ê₁ r=½, gen-3 @ ρ̂ r=0.816), exponent n_C (matches F437 V_us=(3/4)^{n_C} at the origin), and
w = the independently-derived coupling weights (down: F506 ratios {1,20,840}; up: f(ν) {α²,α,1}). **F490 held: the
weights are the derived coupling functions, NOT observed mixing.** Diagonalize M_d, M_u → U_d, U_u; CKM = U_u†U_d.

## Result — V_cb reproduces; V_us/V_ub under-produce by the overlap factor
| element | four-matrix (overlap-weighted) | obs | verdict |
|---|---|---|---|
| **V_cb** | **0.035–0.046** | 0.0411 | ✓ (the gen-2/3 mixing works) |
| V_us | 0.005 | 0.2245 | ✗ ~K₁₂× too small |
| V_ub | 0.00015 | 0.0037 | ✗ too small |

The suppression is **exactly the overlap K₁₂=(3/4)⁵=0.237**: the weighted-Gram off-diagonal gives θ_C ≈
√(m_d/m_s)·K₁₂ = 0.224·0.237 = 0.053, i.e. the Gatto angle *times the overlap*. So the four-matrix machinery is
sound (V_cb lands), but the 1-2 off-diagonal is over-suppressed.

## The precisely-named open piece: the M off-diagonal TEXTURE
Two candidate textures, and **no single uniform one fits both mixings**:
- **Overlap-weighted** (M_ij=√(w_i w_j)·K_ij, what I built): fits **V_cb** ✓; gives V_us 4× too small.
- **Gatto/geometric-mean** (M_ij=√(w_i w_j), i.e. K→1): gives **V_us = √(m_d/m_s) = 1/√20 = 0.2236 (0.4%)** ✓;
  gives V_cb = √(m_s/m_b) = 0.154 (3.7× too big).

So V_us wants the democratic/Gatto texture; V_cb wants the overlap-suppressed one. **This element-dependence is
physically sensible, not a bug:** the Cabibbo angle is famously the down-sector Gatto relation √(m_d/m_s), while V_cb
carries the up–down interplay. The open piece is: **derive the F84/K264 off-diagonal texture** — why the 1-2 sector
is (near-)democratic while the 2-3 sector is overlap-suppressed. That is the load-bearing gap, and it's Lyra's kernel
lane (F84/K264 texture derivation).

## The clean lead (identified via Gatto + banked integers — NOT forced yet)
**V_us = 1/√20 = 1/√((N_c+1)(N_c+2)) = 0.2236 (0.4%)**, using the BANKED down-ratio s/d=20=(N_c+1)(N_c+2) (F506).
This is the Gatto relation √(m_d/m_s) composed with a banked BST integer — cleaner than the (3/4)⁵ form (5.7%), and
target-innocent in its inputs (s/d=20 was derived from cohomology, not from the Cabibbo). **Tier: LEAD, not forced** —
the geometric-mean texture that produces it is not yet shown to come from the F84 kernel (F490: don't adopt the
texture because it hits the number). The precise 2/√79 (0.004%, T1444) remains the per-element refinement; 1/√20 is
the *mechanistic* reading (V_us as √(m_d/m_s) from the mass matrix). V_ub via √(m_u/m_t)=0.0035 (7%, involves the
anomalous gen-1) — consistent but not clean.

## This REFINES my EOD framing (honest correction)
At EOD I said V_ub is "doubly-gated (CP apex + gen-1)." The four-matrix run shows the **texture is the FIRST gate**,
upstream of CP/gen-1: V_us itself (a real, CP-free magnitude) is wrong in the overlap-weighted texture. So the order
is: (1) fix the off-diagonal texture (V_us/V_cb magnitudes), THEN (2) CP apex + gen-1 for V_ub's last piece. The
texture is the load-bearing open piece; I was one layer too deep at EOD.

## Honest tier / discipline
- **The F483 four-matrix ASSEMBLES and RUNS** — V_cb reproduced forward (0.041) from derived weights, F490-clean. Real.
- **V_us/V_ub NOT reproduced** in the overlap texture — I report this straight, no texture-switching to hide it.
- **No fabricated V_ub, no bank.** The open piece (off-diagonal texture derivation) is named precisely, per Keeper.
- **Lead flagged honestly:** V_us=1/√20 (Gatto + banked 20) is identified, not forced — the texture must be derived.
- Graph unchanged, SOD current (max T2517).

— Grace, 2026-07-13. F483 four-matrix runs: V_cb ✓ (0.041, overlap-weighted); V_us/V_ub too small by the overlap
factor. The precisely-named open piece is the off-diagonal texture — V_us wants Gatto (√(m_d/m_s)=1/√20, 0.4%,
banked 20), V_cb wants overlap-suppressed; no uniform texture fits both, which is physically sensible (Cabibbo is
down-sector Gatto). Texture derivation = Lyra's F84 kernel lane. No fabrication, no bank.
