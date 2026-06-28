---
title: "F389 — the f(ν) constraint map + a structural insight: the rank-k Korányi-Wolf fiber integral (F385) IS the regulator that makes the up-type boundary concentration finite. The correct up-type f(ν) must satisfy THREE constraints simultaneously: (C1) heavier=boundary (f increases toward r→1), (C2) finite saturation f(boundary)=1 (top y_t=1, not divergent), (C3) up steeper than down (m_t/m_u~8e4 vs m_b/m_d~9e2). Every simple SINGLE-POINT kernel form fails C1 or C2: amplitude forms (1−r²)^{q/2}, N^{q/2} → 0 at the boundary (origin-max, fail C1, = F375's falsification); the Poisson peak [(1+r)/(1−r)]^{q/2} → ∞ at the boundary (fail C2, top would be infinite). No single-point kernel power satisfies both. THE INSIGHT: the rank-k fiber integral (F385) is EXACTLY the regulator — it tames the single-point Poisson divergence to a finite value: top (rank-0 POINT fiber) nothing to integrate → bare boundary value normalized = 1 (C2); lighter (rank-1 disk, rank-2 bulk fibers) the fiber integral SPREADS the concentration → finite <1 (C1+C2). So F385's fiber-spread MECHANISM and the C2 finiteness (y_t=1) are the SAME fact — the fiber-integration is what makes the boundary concentration finite. f(ν) NEEDS the fiber (it's the regulator, not an optional refinement). The object to compute is the FIBER-REGULATED boundary concentration (regularization automatic from the fiber geometry, no ad-hoc cutoff); the steepness (C3) comes from the fiber dimension growing 0→1→2 (Grace's n_C/rank ratio). The inherited weight q′ is still Grace's FK pin. HONEST: structure (the constraint map + the regulator identification), NOT a banked value; exact f still the bounded fiber computation (Grace weight + Elie integral). Count 8/26."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-28 Sunday (date-verified)"
status: "v0.1 — f(ν) constraint map + fiber-regulator insight. THREE constraints: (C1) heavier=boundary (f↑ to r→1), (C2) finite f(boundary)=1, (C3) up steeper than down. Every simple single-point form fails C1 or C2: amplitude (1−r²)^{q/2}, N^{q/2} →0 at boundary (origin-max, fail C1); Poisson peak [(1+r)/(1−r)]^{q/2} →∞ (fail C2). INSIGHT: rank-k fiber integral (F385) IS the regulator — top (rank-0 point fiber) nothing to integrate → bare boundary value normalized =1 (C2); lighter (rank>0 fiber) integral spreads → finite <1. F385 mechanism ≡ C2 finiteness (SAME fact). f NEEDS the fiber (it's the regulator). Target sharpened: compute fiber-regulated boundary concentration (auto-finite), NOT single-point kernel power; steepness (C3) from fiber dim 0→1→2 (Grace n_C/rank). q′ still Grace's FK pin. Structure not banked value; exact f = bounded fiber computation. Count 8/26. For Grace, Elie, Cal, Casey, Keeper."
---

# F389 — the f(ν) constraint map; the fiber-integration is the regulator

Mapped the constraint space the correct up-type f(ν) must satisfy (geometry/definition lane). It rules out the simple forms cleanly AND reveals why the fiber is essential — a structural insight, not just a negative.

## Three constraints the correct f(ν) must satisfy simultaneously

- **(C1) heavier = boundary:** f increases toward r→1 (the boundary/top).
- **(C2) finite saturation:** f(boundary) = 1, finite (top y_t=1, not divergent).
- **(C3) up steeper than down** (m_t/m_u ~ 8×10⁴ vs m_b/m_d ~ 9×10²).

## Every simple single-point kernel form fails C1 or C2

| form | r→1 (boundary) | C1 | C2 |
|---|---|---|---|
| (1−r²)^{q/2} (bulk-to-bdy amp) | → 0 | ✗ (origin-max) | ✓ |
| constant-mode overlap | → 0 | ✗ (origin-max) | ✓ |
| N^{q/2} | → 0 | ✗ (origin-max) | ✓ |
| Poisson peak [(1+r)/(1−r)]^{q/2} | → ∞ | ✓ | ✗ (diverges) |

The amplitude-type forms decrease to the boundary (would make the *origin* fermion heaviest — F375's falsification); the Poisson peak increases to the boundary (C1) but diverges (top would be ∞, not 1 — fails C2). No single-point kernel power satisfies both.

## The insight: the fiber integral is the regulator

The single-point Poisson peak's boundary divergence is regulated by integrating the concentration over the rank-k Korányi-Wolf fiber (F385):
- **top** (rank-0 *point* fiber): nothing to integrate → the bare boundary value, normalized = **1** (C2 satisfied, finite);
- **lighter** (rank-1 disk, rank-2 bulk fibers): the fiber integral **spreads** the concentration over a positive-dimensional fiber → **finite < 1** (C1 + C2).

So **F385's fiber-spread mechanism and the C2 finiteness (y_t=1) are the SAME fact** — the fiber-integration is what makes the boundary concentration finite. This is why f(ν) *needs* the fiber: it is the regulator, not an optional refinement. The object to compute is the **fiber-regulated boundary concentration** (regularization automatic from the fiber geometry, no ad-hoc cutoff); the steepness (C3) comes from the fiber dimension growing 0→1→2 (Grace's n_C/rank ratio). The inherited weight q′ is still Grace's FK pin.

## Net

The same structure that makes the top unique (rank-0 point fiber, F385/F387) also makes its coupling finite (C2: nothing to spread → normalized 1) — one mechanism, two consequences. The exact f(ν) is still the bounded fiber computation (Grace's weight + Elie's integral); structure mapped, value not fished. Count 8/26.

— Lyra, Sun 2026-06-28 (date-verified). F389: f(ν) constraint map + fiber-regulator insight. (C1) heavier=boundary, (C2) finite f(boundary)=1, (C3) up steeper. Simple single-point forms fail C1 or C2 (amplitude forms →0 origin-max; Poisson peak →∞). INSIGHT: rank-k fiber integral (F385) IS the regulator — top rank-0 point fiber → bare value normalized 1 (C2); lighter rank>0 fiber → spread finite <1. F385 mechanism ≡ C2 finiteness. f needs the fiber (regulator). Compute fiber-regulated boundary concentration (auto-finite), not single-point power. q′ = Grace's FK pin. Count 8/26.
