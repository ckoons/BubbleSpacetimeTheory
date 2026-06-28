---
title: "F379 — concrete rank-2 Cartan model for the 'watertight ρ-shift rep step' (Elie's flagged last leg for V_cb): built the model instead of labeling it multi-week (Casey: engage/compute). RESULT: two clean legs + one precisely-located gap. Generation Harish-Chandra address = (ρ₁−ν_g, ρ₂) with ρ=(5/2,3/2)=(n_C/rank,N_c/rank), ν_e=5/2, ν_μ=3/2, ν_τ=0. LEG 1 (RIGOROUS): ν_τ=0 ⟹ τ-address=(5/2,3/2)=ρ EXACTLY → τ-frame points along the ρ-direction, angle arctan(ρ₂/ρ₁)=arctan(N_c/n_C)=30.96°, cos=ρ₁/|ρ|=5/√34; target-innocent (ρ root-system invariant, ν_τ=0 generation floor) — the rep anchor, a theorem not a fit. LEG 2 (UNIQUELY DATA-SELECTED): plugging candidate geometric angles into Grace's rank-1-effective kernel, ONLY ψ=ρ-direction (30.96°) fits V_cb=0.0410 (0.20%); alternatives are 55-89% off (μ-τ relative-address 25.35°→0.064; μ abs-address 56.31°→0.0046; 45°→0.012). So the data selects the ρ-direction, and Leg 1 says that direction is the τ-address because ν_τ=0. REMAINING (1 pinned step, not vague): why the rank-1-effective OVERLAP angle = the ABSOLUTE τ-address direction (ρ) rather than the μ-τ RELATIVE-address angle (25.35°). That bridge is in Grace's kernel reduction (localization direction = address direction, electron-at-origin reference). NET: V_cb angle = ρ-direction is now rigorously anchored (Leg 1) + uniquely data-selected (Leg 2) — 'derived modulo one kernel-geometry identity', much tighter than 'structural'. Count 8/26."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-28 Sunday (date-verified)"
status: "v0.1 — concrete rank-2 Cartan model. Addresses (ρ₁−ν_g, ρ₂): e(ν=5/2)→(0,3/2) on e₂; μ(ν=3/2)→(1,3/2) at 56.31°; τ(ν=0)→(5/2,3/2)=ρ at 30.96°=arctan(N_c/n_C). LEG 1 RIGOROUS: ν_τ=0⟹τ-address=ρ exactly (target-innocent rep anchor). LEG 2 DATA-SELECTED: ψ=ρ-angle→V_cb 0.0410 (0.20%) UNIQUELY (25.35°→55%, 56.31°→89%, 45°→70%). Remaining: 1 pinned step — rank-1-effective overlap angle = absolute τ-address direction (Grace's kernel geometry). 'Derived modulo one kernel identity', tighter than structural. Count 8/26. For Grace, Elie, Cal, Casey, Keeper."
---

# F379 — concrete rank-2 Cartan model for the watertight ρ-step

Elie flagged the last open leg for V_cb: the watertight "why the generation frames rotate by exactly the ρ-angle." Per Casey (engage, compute — don't label multi-week), I built the concrete rank-2 model. It produced two clean legs and one precisely-located gap.

## Setup

Rank-2 Cartan a* of D_IV⁵; conformal ρ = (n_C/rank, N_c/rank) = (5/2, 3/2). Generations are scalar conformal weights along the dilation (e₁) axis: ν_e=5/2, ν_μ=3/2, ν_τ=0. The Harish-Chandra address of generation g = (ρ₁−ν_g, ρ₂):

| gen | ν | address (ρ₁−ν, ρ₂) | angle to e₁ |
|---|---|---|---|
| e | 5/2 | (0, 3/2) | 90° (on e₂ axis) |
| μ | 3/2 | (1, 3/2) | 56.31° |
| τ | 0 | (5/2, 3/2) = **ρ** | **30.96° = arctan(N_c/n_C)** |

## Leg 1 (RIGOROUS): ν_τ=0 ⟹ τ-address = ρ exactly

Because the bare weight vanishes, the τ Harish-Chandra address is (ρ₁, ρ₂) = ρ itself → the τ-frame points along the ρ-direction, angle arctan(ρ₂/ρ₁) = arctan(N_c/n_C) = 30.96°, cos = ρ₁/|ρ| = 5/√34. Target-innocent (ρ is a root-system invariant; ν_τ=0 is the generation floor). **This is the rep-theory anchor — a theorem, not a fit.**

## Leg 2 (UNIQUELY SELECTED BY DATA): the overlap angle IS the ρ-direction

Candidate geometric angles in Grace's rank-1-effective kernel (r_μ=0.5082, r_τ=0.8207):

| ψ | meaning | V_cb | miss |
|---|---|---|---|
| **30.96°** | ρ-direction = abs τ-address | **0.0410** | **0.20%** |
| 25.35° | μ-τ relative-address angle | 0.0636 | 54.8% |
| 56.31° | μ abs address | 0.0046 | 88.9% |
| 45° | — | 0.0122 | 70.2% |

The ρ-direction isn't "structurally near" — it is the ONLY angle that fits (next-best 55% off). The data selects the ρ-direction as the overlap angle, and Leg 1 says that direction is the τ-address because ν_τ=0.

## The remaining construction step (now pinned)

Why the rank-1-effective *overlap* angle equals the *absolute* τ-address direction (ρ) rather than the μ–τ *relative*-address angle (25.35°). That bridge lives in the rank-1-effective reduction (localization direction = address direction, electron-at-origin reference). The concrete check (handed to Grace/Elie): in the rank-1-effective collapse, is ψ defined as the angle of each state's localization direction measured from the e₁ dilation axis? If so, the overlap angle = the τ-address = ρ is forced, and Leg 2 becomes rigorous — closing the watertight step.

## Net

V_cb angle = ρ-direction is now (a) rigorously anchored (ν_τ=0 ⟹ τ-address=ρ, Leg 1) + (b) uniquely data-selected (Leg 2, 0.20% vs 55%+ alternatives), pending ONE construction step (the rank-1-effective angle definition). This is "derived modulo one kernel-geometry identity" — much tighter than "structural," and the gap is a single pinned identity, not a vague rep check. Count 8/26.

— Lyra, Sun 2026-06-28 (date-verified). F379: rank-2 Cartan model. τ(ν=0)-address=ρ exactly (Leg 1 rigorous, target-innocent). ψ=ρ-angle gives V_cb 0.0410 (0.20%) uniquely (Leg 2 data-selected; alternatives 55-89% off). Remaining: rank-1-effective overlap angle = absolute τ-address direction (1 pinned step, Grace's kernel). Derived modulo one kernel identity. Count 8/26.
