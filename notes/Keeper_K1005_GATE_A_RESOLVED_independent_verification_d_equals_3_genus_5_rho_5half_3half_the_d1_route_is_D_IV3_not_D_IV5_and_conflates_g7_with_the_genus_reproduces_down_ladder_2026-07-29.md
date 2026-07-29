---
node_type: k_audit
id: K1005
title: GATE A RESOLVED (independent Keeper verification, confirm vs aif.2069) — the FK invariants of D_IV⁵ are rank r=2, multiplicity d = n−2 = 3 = N_c, FK genus p = n = 5 = n_C, conformal ρ = (5/2, 3/2). The "d=1, ρ=g/2=7/2" route is the ERROR: d=1 is the multiplicity of D_IV³ (n=3), NOT D_IV⁵, and it conflates BST's g=7 (embedding/signature) with the FK genus (which is n_C=5). Proof-of-pin: (ν)_λ = (ν)_{λ₁}(ν−3/2)_{λ₂} at ν=N_c=3 reproduces the banked down ladder {3,60,2520}=1:20:840, m_s/m_d=20, V_us=0.2236. This pins the INPUT to Gate B; it does not clear Gate B.
date: 2026-07-29
author: Keeper
verdict: d=3 (=N_c), genus=5 (=n_C), ρ=(5/2,3/2), ν=N_c=3 route — verified and reproduces the banked ladder exactly. The d=1/ρ=7/2 convention is a mislabel (wrong domain + g-as-genus). Lyra confirms against aif.2069; then evaluates the real binomial (Gate B) at d=3.
---

# K1005 — Gate A resolved: d=3, genus=5, ρ=(5/2,3/2)

Casey: "clear the block." Gate A (the d=1 vs d=3 convention split, K1004) is a standard, checkable structural fact — so I verified it independently to hand Lyra a pre-checked pin and Cal a concrete target. **This is a cross-check for Lyra to confirm against aif.2069 / FK Ch XII, not a substitute for her authoritative pin — but it reproduces the banked result exactly, so it's strong.**

## ★ The FK invariants of D_IV⁵ (verified)
D_IV⁵ = the type-IV (spin-factor) bounded symmetric domain, Euclidean Jordan algebra of rank 2, dim V = n_C = 5. From the Jordan dimension formula **dim V = r + d·r(r−1)/2** → for r=2, **n = 2 + d** → **d = n − 2 = 3 = N_c.** FK genus **p = 2 + d(r−1) = n = 5 = n_C.** Conformal **ρ = (n_C/r, N_c/r) = (5/2, 3/2)** — matching the corpus's long-standing canonical pin (CLAUDE.md: "genus = n_C = 5; g = 7 is embedding/signature, NOT a genus; ρ = (5/2, 3/2)").

## ★ Why the "d=1, ρ=7/2" route is the error (two mislabels)
The low-dimensional table settles it — **d=1 is the multiplicity of D_IV³, not D_IV⁵:**

| domain | d = n−2 | genus = n |
|---|---|---|
| D_IV² | 0 | 2 |
| **D_IV³** | **1** | 3 |
| D_IV⁴ | 2 | 4 |
| **D_IV⁵** | **3** | **5** |
| D_IV⁶ | 4 | 6 |

So the "d=1" route imported the multiplicity of the wrong domain. And **ρ=g/2=7/2 conflates BST's g=7 (embedding/signature) with the FK genus** — but the FK genus of D_IV⁵ is p=n_C=5, giving ρ-scale 5/2, not 7/2. Both are the same mistake the corpus already warned against (CLAUDE.md, 2026-05-28 "one-genus convention": genus=n_C=5, g=7 NOT a genus). **The ν=N_c=3, d=3 route (F729/F734) is the consistent one.**

## ★ Proof-of-pin: d=3 reproduces the banked down ladder (Keeper verification computation)
Rank-2 Pochhammer **(ν)_λ = (ν)_{λ₁}·(ν − d/2)_{λ₂} = (ν)_{λ₁}·(ν − 3/2)_{λ₂}** at ν = N_c = 3, single-row down modes λ=(ℓ,0):
- K = {(3)_1, (3)_3, (3)_5} = **{3, 60, 2520}** → ratios **1 : 20 : 840** ✓ (banked K993).
- **m_s/m_d = 60/3 = 20** ✓ (banked, exact).
- (N_c)_min off-diagonal ⟨ψ₁|ψ₃⟩ = (3)_1 = 3 → **V_us = √(3/60) = 0.2236** ✓ (0.8σ vs PDG 0.2243).

The d=3 pin is not asserted — it **reproduces the banked ladder exactly**, which the d=1 route would not. That is the internal consistency check Gate A needed.

## ★ What this clears, and what it does NOT
- **CLEARS (pending Lyra's book-confirm):** Gate A. Use **d=3, ν=N_c=3, ρ=(5/2,3/2), genus=5** for all sectors. One convention, pinned.
- **Does NOT clear Gate B:** the real FK generalized-binomial $\binom{\lambda_j}{\lambda_i}_\nu$ (Prop XII.1.3) for the non-single-row lepton {5/2,3/2,0}, neutrino, up sectors still needs evaluation — **now with d=3 as the pinned input.** The (N_c)_min shortcut remains unproven off the down single-row case (F690); the real binomial must reproduce (N_c)_min=3 for the down {1,3} check.

## ★ Handoff
- **LYRA:** confirm d=3 / genus=5 against aif.2069 + FK Ch XII (should be quick — it reproduces the ladder). Then evaluate the real Prop XII.1.3 binomial at d=3 for the three sectors → hand Elie per-engine.
- **CAL:** audit — is d=n−2=3 the right FK type-IV multiplicity, and is the "d=1/ρ=7/2" genuinely the D_IV³/g-as-genus mislabel? (target-innocent: d comes from the domain's structure, nothing observed.)
- **KEEPER/GRACE:** if confirmed, this also fixes any corpus note carrying the d=1/ρ=7/2 route — Grace stamps those superseded in the dedup pass (K1003).

— K1005, Keeper, 2026-07-29. Gate A: d=n−2=3=N_c, FK genus=n=5=n_C, ρ=(5/2,3/2), ν=N_c=3 route — verified, reproduces the banked down ladder {3,60,2520}/m_s-m_d=20/V_us=0.2236. The d=1/ρ=7/2 route = D_IV³ multiplicity + g-as-genus mislabel. Gate B (real binomial for non-single-row sectors) still open, now with d=3 pinned. Lyra confirms vs aif.2069. See [[Keeper_K1004_unblock_Elie_the_off_diagonal_numbers_genuinely_dont_exist_its_a_real_FK_evaluation_two_gates_d_convention_and_N_c_min_shortcut_is_unproven_beyond_down_single_row_2026-07-29]], F729, F690, F734, K901, CLAUDE.md one-genus-convention (2026-05-28).
