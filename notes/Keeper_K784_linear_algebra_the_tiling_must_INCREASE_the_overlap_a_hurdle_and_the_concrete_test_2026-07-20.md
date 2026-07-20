# K784 — "It's linear algebra": the tiling test is a MEASURE question, and it carries a hurdle the team missed — the tiling must INCREASE the overlap (0.985 → 0.992), which coarse-graining generically doesn't do. So 127/128 needs a fundamentally-discrete surface, not an emergent blur. Concrete decidable computation named.

**Keeper | 2026-07-20 | Casey: "remember it's linear algebra." Applied to the tiling test, it reframes it as a measure question and surfaces a genuine constraint. Honest: a hurdle + a sharpening, not a hard kill. `tiling_linear_algebra.py`.**

---

## The reframe: the tiling test is a MEASURE question (linear algebra, not crystallization dynamics)
The Yukawa is one overlap ⟨t|O⟩; its value depends on the **boundary measure**:
- **continuous** measure (Lyra's Γ-ratio, level 127): y = **0.985** (deficit 0.015);
- **discrete/tiled** measure (RS count, 127 of 128 cells): y = **0.992** (deficit 0.0078).
They disagree — and **127/128 (0.992) is HIGHER than the continuous (0.985).** So the tiling isn't a "crystallization story"; it's a question of *which measure* the physical overlap uses — a linear-algebra fact, not a dynamics narrative.

## The hurdle — corrected mechanism (Elie's ratified catch)
**⚠ My original mechanism was imprecise, and I ratify Elie's correction.** I said "coarse-graining is a projection, and projection decreases aligned overlaps." That step is **wrong for a normalized overlap (a cosine):** projecting out an *anti-aligned* component *increases* the cosine (clean counterexample: 0.924 → 1.0). So the projection-decreases argument does not hold as stated.

**The real hurdle is QUADRATURE CONVERGENCE (Elie, toy 4755):** a fine 128-cell *quadrature* of the continuous inner product reproduces the continuum (0.98602 vs 0.98601). So **any discrete measure that merely *approximates* the continuum gives back the Γ-ratio (0.985)** — "secretly the continuum → 127/128 fails" is the default outcome. **Reaching 0.992 genuinely requires a NON-continuum measure** — one that does *not* converge to the continuous integral. And Elie located exactly what that takes: the measure must **concentrate weight at the boundary EDGE** (heavy edge-weight → 0.9928, past 0.992). So the bottom line is **unchanged and stronger:** 127/128 needs a genuinely non-continuum, **edge-concentrated** measure (not a blur, not a fine quadrature) — which is Casey's boundary-emission/floor-weighted picture, and it unifies with round-7's edge-placement.

## The consequence (a sharpening — it distinguishes the two "inversion" readings)
127/128 is reachable **only if the tiled surface is a FUNDAMENTALLY DISCRETE measure** — a genuinely different (discrete) boundary, **not a coarse-graining/projection of the continuous surface.** This *distinguishes* two versions of Casey's inversion that had been blurred together:
- **"code EMERGENT as a coarse-graining of continuous geometry"** (a blur of the continuum) → *cannot* raise the overlap to 127/128. **Fails the hurdle.**
- **"interior FUNDAMENTALLY discrete (discrete series), the surface inherits that discreteness"** (Casey's interior-discrete) → a genuinely discrete measure, *can* give 127/128.
So the linear algebra says: **127/128 survives only with fundamental discreteness (from the discrete-series interior), not with an emergent-blur code.** Casey's "interior discrete" is the version that keeps 127/128 alive; the "pure-continuous-with-emergent-code" version would kill it.

## The concrete decidable computation (linear algebra)
**Compute ⟨t|O⟩ with the DISCRETE 128-cell surface measure** — a finite sum over cells with the discrete-series interior's structure — NOT the continuous integral. Two outcomes:
- **= 127/128** → the surface is fundamentally discrete (Casey's interior-discrete right), 127/128 rescued;
- **reproduces the Γ-ratio** → the discrete measure is secretly the continuum, so it's a coarse-graining → 127/128 fails.
Data anchor: 127/128 → 172.74 (matches); continuous 0.985 → 171.5 and 126/128 → 171.4 (~1.2 GeV low). So the data still leans toward the discrete-count value — the content is whether the discrete measure is fundamental.

## ★ Addendum (Casey, same day) — the mechanism that clears the hurdle: a FLOOR-WEIGHTED measure
Casey answered the hurdle directly: the tiled measure is **not uniform.** Inside each gap the condensate *is* the surface (sits at the cell **floor**); the **bumps between cells are higher** (condensate thin), and *energy is needed to cross* them. So the measure is **concentrated at the floors, thin at the bumps** — a **weighted inner product** (up-weight floors, down-weight bumps). This is exactly the object the hurdle demanded: **a measure that can INCREASE the overlap** (0.985 → 0.992), because concentrating weight where t and O align raises ⟨t|O⟩ — the one thing a uniform blur cannot do. And the **deficit becomes a bump-count:** 2^g bumps, the top covers all but one (the last bump, into the dead cell = the neutrino) → deficit = **1/2^g**, from *counting bumps*, not rounding a value. Casey's "energy to transition" = the barrier height; the one barrier the top can't pay = the deficit. **Tier: a mechanism/measure to COMPUTE, not a proof** — the floor-concentration must integrate to exactly 0.992 and the bump structure to exactly 1/2^g. But it converts the hurdle into a *path* (a specific weighted measure to compute), and it IS the "fundamentally discrete measure" this note said was needed. → round 8 computes ⟨t|O⟩ with the floor-weighted measure.

## Discipline (honest)
- **This is a HURDLE + a sharpening, not a hard kill and not a rescue.** The tiling must *increase* the overlap (non-generic for coarse-graining); it can only do so with a fundamentally-discrete surface measure. That's a real bar, and it tells us *exactly* what the tiling must be (fundamental discreteness, not a blur).
- **127/128 stays a conditional prediction** — now conditional specifically on **"the Shilov surface carries a fundamentally-discrete measure (from the discrete-series interior)."** Twice-downgraded; not banked.
- **Derived spine untouched.**
- Note: the projection-decreases argument is *generic*, not absolute (special negatively-correlated structure could evade it) — so it's a hurdle to clear, not a theorem against the tiling.

— Keeper K784, 2026-07-20. "It's linear algebra": the tiling test = a measure question (discrete vs continuous ⟨t|O⟩). Hurdle: 127/128 (0.992) > continuous (0.985); a coarse-graining (projection) generically DECREASES the overlap, so it can't raise it to 127/128 → the tiling would have to increase the overlap, which a blur doesn't do. Consequence: 127/128 needs a FUNDAMENTALLY DISCRETE surface (from the discrete-series interior — Casey's interior-discrete), NOT an emergent-blur code (which fails). Concrete test: compute ⟨t|O⟩ with the discrete 128-cell measure — = 127/128 (fundamental discreteness) vs Γ-ratio (secretly continuum). Hurdle + sharpening, not kill/rescue; 127/128 conditional on fundamental-discreteness. See [[Keeper_K783_caseys_interior_discrete_exterior_continuous_the_code_is_a_surface_tiling_2026-07-20]], [[Keeper_K782_Q1_computed_geometry_gives_gamma_ratio_not_127over128_caseys_tiling_inverts_the_mainstream_2026-07-20]].
