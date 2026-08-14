# B1 / CFS — Living Status (does D_IV⁵ satisfy Finster's causal action principle?)

*Single source of truth for the B1/CFS edge-testing lane. Edge-tester (Elie ± Cal) updates this; team reviews ~half-hourly. Keeper owns the tier/honesty column. Last update: 2026-08-14 ~08:20, Elie (toy 5249 — edge-test CLOSED).*

**One-line honest state:** BST **carries** a genuine self-adjoint Dirac + spectral triple on D_IV⁵ (credentialed), but on the current object it **does NOT reproduce** Finster's causal-eigenvalue classification — and as of 2026-08-14 (Elie 5249) that gap is **STRUCTURAL, not a distance**: no J is both a symmetry of D and an internal involution, because D_IV⁵'s indefinite involutions are *geometric* (they move points) while Finster's chain needs an *internal* Krein structure on the spinor index. A bounded negative, not a refutation. External line: *"one geometry carries both Connes' and Finster's structures,"* NEVER *"realizes / satisfies / solves the causal action."*

## The ladder (rung → gate → status → what it earns)

| Rung | Gate | Status (2026-08-14) | Earns |
|---|---|---|---|
| 0 | Finiteness | ✅ BANKED (bounded ball, §7438) | action finite on D_IV⁵ |
| 1a | Operator credential | ✅ **EARNED** (K1487: Kostant cubic Dirac, self-adjoint 1e-15, bare-vacuum ground, spectrum→∞) | BST carries a real self-adjoint Dirac |
| 1b | Same-object / G2 (A_xy causal signature) | ❌ **FAILS on this object, STRUCTURALLY** (Elie 5248: 0% spacelike, PSD chain → timelike-everywhere is a *theorem*. Elie 5249: the 0.465 blocker is a **mismatch of type**, not a distance — geometric vs internal indefiniteness; **edge-test CLOSED, outcome (b)**) | would earn "realizes the causal structure" — **not available on this object** |
| — | (P²=P / P‡=P) | ✅ but VACUOUS (wood; auto-satisfied by any equivariant P — the 9th empty pass, Elie 5247). NOT the same-object test. | nothing (construction/signature only) |
| 2 | Boundedness | ⛔ scoped (Grace: reduces to a boundary Forelli-Rudin moment on the g=7 kernel = the same \|K\|²) | action well-defined |
| 3 | Boost-criticality | ⛔ UNRUN (Krein non-compact → Palais compact-group assumption fails; boosts earned, not cited) | critical point |
| 4 | Constrained δ²S ≥ 0 | ⛔ UNRUN — **the minimum, the mountain** (min-not-saddle; does κ lift the saddle?) | "D_IV⁵ satisfies the causal action" |
| C4 | Weighted spectral = causal | ⛔ UNSTARTED (base-camp idempotent trivial; the weighting is 100% of the physics) | the summit |

## The one open edge-test thread (bounded ~1 day, 1–2 CIs)

**Q: Is the two-point Krein symmetry closable, or is 0.465 structural?** — **ANSWERED 2026-08-14 (Elie 5249): STRUCTURAL, outcome (b). No J is both a symmetry of D and an internal involution; the operator symmetry is a reflected-point relation, Finster's is a same-point relation. See the top Log entry.**
- Finster's causal classification presupposes P(y,x) = J P(x,y)†J. Current median rel error **0.465** (was 1.401 in Aug/5209; the credentialed operator earned the 3× improvement).
- Grace's factorization (Direction-A, **verified**): A_xy = \|K(x,y)\|² · (γ·u)(γ·v). The Bergman \|K\|² is a signature-blind positive prefactor; the causal structure lives **entirely in the spinor factor** (γ·u)(γ·v) in the (2,2) Krein metric. So the wall is precisely the two-point Krein symmetry, not the Bergman part.
- **Decidable outcomes:** (a) the symmetry closes → re-run G2, the spinor factor may deliver the signature; (b) 0.465 is structural → honest verdict "BST *wears* but does NOT *satisfy* Finster's causal action on this object." Either is a real, reportable answer.
- Guard (K1492 blind pre-reg): a genuine G2 needs the split geometry-dependent + non-trivial (both spacelike & timelike) + object-match (BST's actual eigenvalues = Finster's) + blind. Operator-level P‡=P ≠ the two-point condition — conflating them = the 10th empty address.

## What's fire-independent of B1 (does NOT ride these gates)
- T2545 (3,1) signature (fire-independent).
- The operator credential (rung 1a) — stands regardless of G2.
- The neutrino spine, the QM axioms, the masses/mixings, DE — all independent of the CFS credential.

## Log (edge-tester appends; newest first)
- **2026-08-14 ~08:20 (Elie 5249) — EDGE-TEST CLOSED: STRUCTURAL. Outcome (b).**
  **The 0.465 is not a distance; it is a mismatch of type.**
  1. **The condition reduces.** P(x,y) = Σ_k ψ_k(x)ψ_k(y)† ⟹ **P(y,x) = P(x,y)† identically**, by
     construction. So Finster's P(y,x) = J P(x,y)†J is not a symmetry to be arranged — it collapses to
     **[J_f , P(x,y)] = 0**: the two-point kernel must *commute* with the Krein operator at each point pair.
     (That reduction should have preceded quoting 0.465 as a closable distance — my own 5248 included.)
  2. **What the operator symmetry actually delivers is a *reflected-point* relation.** J = J_f ⊗ J_poly, and
     J_poly reflects the point (z_μ → −z_μ, μ < r), so [J,P] = 0 gives **J_f P(Rx, Ry) J_f = P(x,y)** —
     verified exact to **≤ 2.8e-15 at every r = 0…5**. Real symmetry, *different pair of points*.
  3. **The same-point condition fails at every non-trivial r:** 0.375, 0.480, 0.514, 0.531, 0.552 for
     r = 1…5 — closing **only at r = 0**, i.e. J = 1: positive definite, **not a Krein operator**.
  4. **THE DICHOTOMY (the result).** A **point-acting** J commutes with D but answers about reflected points.
     A **purely internal** J is same-point by construction but **fails [J,D] = 0** — measured
     **5.29, 5.29, 6.23, 6.45, 6.45** for r = 1…5. ⟹ **NO J CAN BE BOTH.**
     Finster's chain needs an **internal** Krein structure on the spinor index; **D_IV⁵'s indefinite
     involutions are geometric — they move points.**
  - **Against @Cal's blind criteria (§485):** *no knob was tuned* — nothing was driven toward 0.465→0. The
    finding is that the two conditions are inequivalent for every candidate J, with the only closer being the
    non-indefinite identity. That is **structural**, outcome (b).
  - **VERDICT: "BST *wears* but does not *satisfy* the causal action on this object."** Bounded, real, done.
  - **Guard now has its mechanism, not just its assertion:** operator-level P‡ = P is a **reflected-point**
    statement; the two-point condition is a **same-point** statement. They were never going to merge, so
    "symmetry restored" was never available. Stronger than yesterday's guard because it says *why*.
  - Support: `play/toy_5249_*`, `play/toy_5249_support_b1_edge_reduction.py`, `..._b1_dichotomy.py`.
- **2026-08-14 ~13:00 (Elie 5248 / Keeper K1493):** G2 NEGATIVE on this object (0% spacelike, theorem; blocker two-point Krein symmetry 0.465). Grace's factorization localizes the wall to the spinor factor. Bounded to ~1 day per Casey.
- **2026-08-14 ~08:10 (Cal §485):** G2 negative RATIFIED — timelike-everywhere is a THEOREM (PSD chain = §437 Landmine-#1), not an accident; "wears but does not satisfy" is the honest bound. Grace's factorization COLD-READ **PASS**: |K(x,y)|² = K(x,y)K(y,x) is real ≥0 (Bergman Hermitian) → positive prefactor → causal signature lives entirely in the spinor factor; wall = two-point Krein symmetry only. (Count-once: one FK/Bergman object in 3 sectors = one object's triple-duty, not 3 locks.) Edge-test criteria committed BLIND: **closable** iff gap→0 under a GEOMETRY-FORCED correction (a tuned knob driving 0.465→0 is REJECTED) → re-run G2 needing split-geom-dependent + both-spacelike-&-timelike + object-match + blind; **structural** → honest "wears not satisfies." GUARD held: operator-level P‡=P ≠ the two-point condition — no false "symmetry restored" (would be the 10th empty address).
- **2026-08-14 ~08:15 (Elie theorem / Cal §486):** Edge-test RESOLVED = **STRUCTURAL** (not closable). Elie's proof: no single J is both geometric AND internal — Finster needs an internal (spectral) J; BST's indefiniteness is geometric (in the order), so the two-point Krein symmetry is structurally unsatisfiable (0.465 is a dichotomy, not a tuned-knob gap). **Rung 1b = STRUCTURAL NEGATIVE, final.** Honest verdict: **"BST wears but does not satisfy Finster's causal action on this object."** Gates 2–4 now MOOT for the Finster question (object-match fails upstream). Positive result: geometric-vs-internal = order-vs-spectral ⟹ **BST's causality is the commitment order = a causal set** (Lyra formulates; continuum-limit → (3,1) Minkowski the one honest open). Cal wrote the one-page Finster courtesy matrix (`BST_CFS_Finster_Agreement_OnePager_Cal_2026-08-14.md`). **B1 CFS lane CLOSED, clean structural answer.**
