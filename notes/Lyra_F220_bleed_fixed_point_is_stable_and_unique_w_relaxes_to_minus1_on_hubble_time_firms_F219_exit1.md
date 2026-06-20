---
title: "F220 — The computation Casey asked for: the bleed fixed point (F219 Exit 1) is STABLE and UNIQUE. For any increasing outflow + flat inflow, d(ρ̇)/dρ < 0 always → one stable attractor at constant ρ_Λ → w=−1. Perturbations decay at rate (3/2)H → w(z) returns to −1 within ~1 Hubble time (~12 Gyr). Numerical convergence confirmed from both 1/4× and 4× the fixed point. Upgrades F219 Exit 1 from LEAD toward result: the prediction is now SIGNED and TIMED — w(z)→−1 with deviations damping on a Hubble time."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-19 Friday 11:53 EDT"
status: "v0.1 — heat-bleed LEAD (Cal #50, INTERNAL). Firms F219 Exit 1. Stability result is robust (model-independent: holds for any monotone-increasing outflow + ρ-flat inflow). Relaxation rate ~(3/2)H is the model-specific number. No reverse-reading. Count HOLDS 4 of 26."
---

# F220 — The bleed self-regulates: w=−1 is a stable attractor, relaxation ~ Hubble time

Casey: *"Yes we need the computation."* Here it is. F219 Exit 1 argued the de Sitter horizon is a thermostat (inflow=outflow → w=−1); this firms it from "fixed point exists" to "**stable, unique, and it relaxes on a measurable timescale.**"

## The flow

Interior un-committed-sea density ρ (the bled energy that hasn't frozen out, F216):

  **dρ/dt = B − k·ρ^{3/2}**

- **Inflow B** — set by the slowly-varying host boundary temperature; ρ-flat on cosmological timescales.
- **Outflow k·ρ^{3/2}** — expansion/horizon outflow ~ H·ρ with H = √(ρ/3)/M_Pl, so ∝ ρ^{3/2}.

## Result 1 — stability, and it is model-independent

Fixed point: B = k·ρ*^{3/2}. Linearizing,

  **d(ρ̇)/dρ |_* = −(3/2)k·ρ*^{1/2} < 0.**

The sign is negative for *any* outflow that increases with ρ against an inflow that doesn't — so the conclusion does not depend on the exponent 3/2: **a self-regulating bleed has exactly one stable fixed point.** Numerically, starting at ¼× and 4× the fixed-point density both converge to it (→ 1.0000 in 8 normalized time units). So w=−1 is not one option among many — it is the **attractor**.

## Result 2 — the relaxation timescale (the new falsifiable number)

The perturbation decay rate is `γ = (3/2)k·ρ*^{1/2} = (3/2)·(B/ρ*) = (3/2)H_*` (since at the fixed point inflow = outflow = H_*·ρ*). With H_* = 1.19×10⁻³³ eV (Hubble time 17.5 Gyr):

  **a deviation of w from −1 damps back in ~12 Gyr — about one Hubble time.**

So the sharpened, signed, *timed* prediction: **w(z) tracks −1, and any excursion relaxes on a Hubble time.** A measured w drifting *away* from −1, or relaxing much faster/slower than ~H, falsifies the thermostat.

## Where this leaves the interstasis chain

| note | claim | status now |
|---|---|---|
| F218 | interstasis onset ≈ now (ρ_Λ^(1/4) = 0.26·m₂) | LEAD |
| F219 Exit 1 | horizon thermostat → w=−1 | was LEAD |
| **F220** | thermostat fixed point is **stable, unique, relaxes at (3/2)H** | **firms it: signed+timed prediction** |
| F219 Exit 2 | Shilov reconnection re-seeds (cyclic) | LEAD (orthogonal escape) |

## Net (Result | Confidence | Next)

| Result | Confidence | Next |
|---|---|---|
| fixed point stable & unique (any increasing outflow + flat inflow) | SOLID (sign argument + numerics) | — |
| w=−1 is the attractor, not just an option | Med-High | derive B (host-boundary T) from first principles |
| perturbations relax at (3/2)H → w(z)→−1 on ~12 Gyr | Med (model-specific rate) | tighten the outflow power → exact rate |
| sharpened falsifier: w(z) relaxing toward −1 on a Hubble time | — | the decisive cosmology measurement |

**NOT a count motion. Count HOLDS 4 of 26.** Heat-bleed LEAD, INTERNAL (Cal #50). No reverse-reading.

@Cal/@Keeper — the upgrade to audit: F219 Exit 1 was "fixed point exists"; F220 shows it is **stable and unique** (model-independent sign argument) and gives a relaxation rate (3/2)H (model-specific). The signed prediction w(z)→−1-on-a-Hubble-time is the new falsifiable content. @Elie — scoreable: stability for any monotone outflow; the ρ^{3/2} model gives γ=(3/2)H; a w(z) drifting away from −1 kills it.

— Lyra, Fri 2026-06-19 11:53 EDT (date-verified). F220: bleed fixed point STABLE & UNIQUE (d(ρ̇)/dρ=−(3/2)kρ^{1/2}<0 for any increasing outflow+flat inflow; numerics converge from ¼× and 4×). Relaxation rate (3/2)H → w(z)→−1 on ~12 Gyr (~Hubble time). Firms F219 Exit 1 from "exists" to signed+timed prediction. No reverse-reading. Count HOLDS 4.
