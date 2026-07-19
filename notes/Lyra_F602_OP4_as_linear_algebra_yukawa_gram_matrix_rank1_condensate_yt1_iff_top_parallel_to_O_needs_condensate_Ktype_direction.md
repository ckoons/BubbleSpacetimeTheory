# F602 — OP-4 as linear algebra (Casey's steer). The Yukawa is a Gram matrix Y_ij=⟨f_L^i|Φ|f_R^j⟩; the single condensate makes it rank-1 (Y=a⊗b, the F585 Gatto texture), so the up-type hierarchy is ONE Gram column. **y_t=1 ⟺ the top mode is parallel to the condensate direction O.** The gap equation is dropped. The one missing input: O's K-type *direction* (F85 gives the scale, not the direction).

**Lyra, Sun 2026-07-19. Casey: "remember this should be linear algebra."** Right — the gap equation was the wrong layer. The Yukawa is an inner product; OP-4 is a Gram-matrix computation. Stripped down, it's clean and it unifies with the mixing work.

## The reframe (drop the gap equation)
A Yukawa is a Born overlap on H²(D_IV⁵):
$$ Y_{ij} = \langle f_L^i \,|\, \Phi \,|\, f_R^j\rangle. $$
Masses = singular values of Y (×v/√2); **y_t = ‖Y‖** (largest singular value); **y ≤ 1 = Cauchy–Schwarz** (Φ a contraction, the F598 ceiling). No NJL, no exponential, no RG, no compositeness scale — those were sophistication.

## Single condensate ⟹ Y is rank-1 (this IS the F585 Gatto texture)
The single Higgs condensate is one direction: Φ = |O⟩⟨O| (rank-1 projector, ‖O‖=1). Then
$$ Y_{ij} = \langle f_L^i|O\rangle\,\langle O|f_R^j\rangle = a_i\,b_j, \qquad Y = a\otimes b \ \ (\text{rank-1}), $$
with a_i=⟨f_L^i|O⟩, b_j=⟨O|f_R^j⟩. **One nonzero singular value** (verified: SVD of a⊗b = {σ,0,0}) → **the top gets all the leading mass; charm and up are exactly zero at leading order (corrections lift them).** This is precisely F585's "single condensate → rank-1 → Gatto texture," now read on the *mass* side. **Masses and mixing are the same rank-1 condensate O** — one Gram structure, the up-type mass hierarchy is one *column* of it (O's overlaps with the fermion modes). Nice consistency: flavor is overlaps all the way down.

## ★ y_t = 1, sharpened to a parallelism question (the decisive linear-algebra statement)
$$ y_t = \|a\|\,\|b\| = \|P_L\,O\|\cdot\|P_R\,O\| \;\le\; 1, $$
where P_L, P_R project onto the left/right fermion spans. **y_t = 1 ⟺ O lies entirely in both fermion spans ⟺ the top modes (t_L, t_R) are *parallel* to the condensate direction O.** That's the whole content: *is one vector (the condensate) parallel to another (the top mode)?* The geometry either forces it or it doesn't — no dynamics needed. The observed y_t = 0.992 reads cleanly as "nearly but not exactly parallel" (‖P O‖ ≈ 0.996).

This **replaces the gap equation entirely**: y_t=1 is not about a fixed point or a compositeness scale, it's about whether the condensate K-type coincides with the top K-type.

## Answer to "can we check it by hand from F85?" — not yet: F85 gives the scale, not the direction
You asked whether F85 already pins the condensate direction so we can check the top's overlap by hand. **F85 pins the condensate *scale* (the VEV magnitude, a_0=225, v=m_p²/(g·m_e)) — not its *direction* (which K-type).** To evaluate ⟨t|O⟩ we need O as a *vector* (its K-type address on H²), and that's the one input we don't have pinned. So the by-hand check is set up but blocked on **the condensate's K-type address.** That's the concrete missing piece — and it's a clean, well-posed target (compute Φ's K-type from the boundary structure), not a fog.

## Which way does it resolve? Two clean scenarios (decidable once O's direction is known)
1. **O defined self-consistently** as the fermion-bilinear direction that condenses (the boundary condensate forms *along* the maximal fermion overlap) → O is *by construction* a fermion mode → the top is parallel → **y_t = 1 exactly** (SUPPORTED becomes near-derived). The 0.992 is a small correction.
2. **O an independent geometric object** (fixed by the conformal boundary alone, not by the fermions) → the top's overlap ⟨t|O⟩ is a *computed* Clebsch–Gordan coefficient, generically < 1 → **y_t < 1**, its value the CG number.
The linear algebra makes this a *decidable* fork: compute O's K-type, project onto the top mode. **That is the whole of OP-4's y_t=1 question**, and it's the same intertwiner machinery as the mixing-numerator work.

## Tiers / verdict
- **Y = Gram matrix, rank-1 (single condensate), hierarchy = one column: DERIVED-structural** (this is F585 on the mass side; unifies masses + mixing under one O). Genuine clean gain from the reframe.
- **y ≤ 1 ceiling: DERIVED** (Cauchy–Schwarz, unchanged).
- **y_t = 1 ⟺ top ∥ O: exact characterization, SUPPORTED** — decidable once O's K-type direction is known; blocked on that one input (F85 gives scale, not direction). **Do NOT bank y_t=1** — but it's now a sharp parallelism question, not a fog.
- **Gap equation / NJL / RG / compositeness: DROPPED** (wrong layer, per Casey). N_c quark-selection survives only as a dimension count (color trace), which is linear algebra too.

## Handoffs
- **@Cal** — derived-only-if-forced gate: the rank-1 Gram structure (hierarchy = one column) is derived-structural (= F585); y_t=1 is the parallelism question ⟨t|O⟩=1, SUPPORTED until O's K-type forces it. No gap-equation content to referee (dropped).
- **@Elie** — verify the rank-1 structure numerically (SVD of a⊗b = one nonzero singular value; hierarchy = the column), and — the real target — **once O's K-type address is proposed, compute ⟨t|O⟩, ⟨c|O⟩, ⟨u|O⟩, ⟨τ|O⟩**: is the top the unique parallel mode (y_t=1) and do the others give the hierarchy? Pure overlaps.
- **@Keeper** — OP-4 close: the gap equation is superseded by the Gram-matrix reframe (K767). The blocking input is now precisely named: **the condensate's K-type direction** (F85 gives scale only). Bank the rank-1 mass/mixing unification (= F585 on the mass side); y_t=1 stays SUPPORTED, reframed to top∥O.
- **@Casey** — the by-hand check needs O's K-type direction first; F85 doesn't give it. If you want to pin O's direction from the boundary structure, that's the joint next step and it closes (or refutes) y_t=1 by a single projection.

Notes only; no toys/theorems claimed. — Lyra
