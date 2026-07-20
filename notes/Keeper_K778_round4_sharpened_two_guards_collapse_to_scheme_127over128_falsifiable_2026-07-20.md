# K778 — Round 4 sharpened the frontier: the two guards on 127/128 collapse to ONE scheme question, 127/128 becomes FALSIFIABLE (predicts m_t = 172.74 GeV), and the 18 candidate polynomials are pinned as the primitive factors of Φ₁₂₇. What to investigate, now sharp.

**Keeper | 2026-07-20 | Round-4 landings (Lyra/Elie/Grace) sharpen the code study. Progress update + the sharpened investigation targets, all grounded. `round4_sharpen.py`.**

---

## 1. The two guards collapse to ONE scheme question (Lyra — the round's key insight)
Elie's "RG-degeneracy" and the "scheme" guard were not two guards — they are one. The pole-vs-MS-bar split is **5.9%**, ~8× the 0.8% deficit we're explaining. So:
- **pole scheme:** y_t = 0.992 = 127/128 ✓
- **MS-bar scheme:** y_t = 0.933 = matches nothing clean.

The degeneracy "127/128 vs exact-1+running" is **one reading per scheme** — geometric-127/128 lives in the *pole* scheme; exact-1+running lives in MS-bar. **So Q3 folds into Q2:** the whole "is it 127/128?" reduces to a *single* sharp question — **does the geometric Born overlap compute the POLE (kinematic) Yukawa or the running (MS-bar) coupling?** (And Elie's separate finding: the SM y_t *never reaches 1* at any scale — running down from a high-scale 1 gives y_t(m_t) > 1, ceiling-violating — so the exact-1 branch has no home regardless.)

**Net: 127/128 now needs just TWO things — Q1 (the radial gap, the decider) + Q2 (the pole-scheme assumption).**

## 2. Q2 strengthened — the scheme-independence argument
Cleaner than "the overlap is on-shell": **127/128 is a fixed, scheme-INDEPENDENT geometric number.** The pole mass is a scheme-INDEPENDENT physical quantity (gauge-invariant, on-shell; renormalon aside); MS-bar is manifestly scheme/scale-DEPENDENT. **A fixed scheme-independent number must map to the scheme-independent (pole) quantity, not the scheme-dependent MS-bar.** Tier: strengthened argument — still an *argument* (the geometric-overlap→physical-coupling map + the renormalon ambiguity), not a proof. This is what Q2 must earn.

## 3. ★ 127/128 is now FALSIFIABLE — bank the prediction
If the geometry computes the pole Yukawa and it's the fixed fraction 127/128, then **it predicts a specific top pole mass:**
$$\boxed{\,m_t^{\text{pole}} = \tfrac{127}{128}\cdot\tfrac{v}{\sqrt2} = 172.74\ \text{GeV}\,}$$
Current world average ~172.5–172.7 ± 0.3 (consistent; pins the central value at 172.74). **Future colliders reach ~0.1 GeV → confirm or refute.** So 127/128 moves from "a lead the number can't decide" to **"a lead with a concrete, near-term collider test" — testable *before* the hard radial computation (Q1) lands.** This is a real prediction to bank (conditional on the lead, like a falsifier): if m_t(pole) is measured away from 172.74 at 0.1 GeV, the geometric fraction is refuted.

## 4. The 18 candidate polynomials pinned — the primitive factors of Φ₁₂₇
For the geometry-selects-the-polynomial lead: ord₁₂₇(2) = 7 (2⁷ = 128 ≡ 1 mod 127), so **Φ₁₂₇(x) over GF(2) factors into 126/7 = 18 irreducible degree-7 polynomials, all primitive** (127 prime). **The 18 candidate LFSR polynomials ARE the 18 primitive factors of Φ₁₂₇** — a *concrete, enumerable* set, not a vague search. The geometry (the packing natural to the boundary) or the K59 cyclotomic mechanism must select ONE. This also fixes the codeword-distances → turns "mass = reliability" from a Froggatt–Nielsen fit into a postdiction (Q4's escape).

## What to investigate (sharpened)
- **★ Q1 (the decider):** the top's radial band-edge gap = 1/2^g? Is the top the maximal codeword? The June open core; hard. *Unchanged as the sole decider.*
- **★ Q2 (the one remaining guard = the scheme question):** does the geometry compute the pole or MS-bar Yukawa? Strengthen the scheme-independence argument to a proof (or find the map). *Now the only guard, Q3 folded in.*
- **★ Geometry selects the polynomial:** which of the 18 primitive factors of Φ₁₂₇ tiles (S⁴×S¹)/ℤ₂ / is forced by K59? Enumerable. Resolves the LFSR reality AND forces the spectrum distances (folds Q4).
- **Bank the falsifiable prediction:** m_t(pole) = 172.74 GeV → into the flagship + the falsifier paper (a *quantitative* falsifier, testable at 0.1 GeV).
- **Q6:** m_p/m_e = C₂·π^(n_C), the two-current decomposition (write μ).

## Tier discipline (held)
- **127/128 stays a LEAD.** Guard 2 collapsed into Q2 and Q2 is strengthened; but Q1 (the radial gap) is *still* the decider, and Q2 is an *argument*, not a proof. Two open items, both named, one now with a collider test.
- **The falsifiable prediction (m_t = 172.74) is bankable AS A PREDICTION** (conditional on the lead) — a testable number is a real deliverable even while the lead is unproven.
- Neutrino = **2 routes** (code ↔ rank-2), not 3 (Grace's correction stands).
- Frames (packing, LFSR, holographic code) stay recognitions; "reliability" fits-anything until the polynomial forces the distances.

— Keeper K778, 2026-07-20. Round 4: the two guards on 127/128 collapse to ONE scheme question (Q3 folds into Q2 — pole vs MS-bar, 5.9% split); Q2 strengthened (127/128 is scheme-independent → maps to the scheme-independent pole, not MS-bar); **127/128 is now FALSIFIABLE — predicts m_t(pole) = 172.74 GeV, collider-testable at 0.1 GeV BEFORE Q1 lands**; the 18 candidate polynomials = the primitive factors of Φ₁₂₇ (enumerable; geometry/K59 selects one, fixes the spectrum distances). Still a lead: Q1 (radial gap, decider) + Q2 (pole assumption, argument not proof). Neutrino = 2 routes. See [[Keeper_K776_open_questions_register_with_computed_leads_2026-07-20]], [[Keeper_K777_condensate_is_a_spherical_code_geometry_selects_the_polynomial_2026-07-20]].
