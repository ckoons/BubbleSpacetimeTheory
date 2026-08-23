# R51 — the isometry gate CLOSES the weak-current route, and points back at a corpus item the team already had (Grace, Round 51, 2026-08-22)

*Assignment: Elie + Grace, the weak-current route to CKM — **through the isometry gate first**, then magnitudes (K1790). I ran the gate. The route does not survive it, at three successive levels, and the failure is constructive: it names what the CKM must be instead, and the corpus already banked that framing.*

## ★ FIRST — a correction to my own Round-50 number (calibrate both directions)
I reported the isometry failure at **factor 21**. That was the defect for one *particular* up 3-space (the coherent-state triple). **The intrinsic, up-space-independent obstruction is factor ≈ 2.70** at ν_W = 3. **I overstated the intrinsic obstruction by ~8×.** The conclusion is unchanged — 2.70 is still fatal against a required 1.00 — but the number was wrong and the corrected one is the honest headline. Over-claiming a negative is the same error as over-claiming a positive.

## The gate, run at three levels — all three fail
**Level 1 — can ANY up 3-space rescue the forced ladder current?** Give the ansatz its best case: let U contain the *entire* image J(D), so P_U J|_D = J|_D. Then the singular values of J|_D are the best any U can achieve. **No up-sector assumption enters at all.**

| ν_W | s₁ | s₂ | s₃ | **s₁/s₃** |
|---|---|---|---|---|
| **3 (FORCED)** | 1.4724 | 1.0480 | 0.5459 | **2.697** |
| 10 | 1.0132 | 0.6748 | 0.3386 | 2.992 |
| 5000 | 0.0530 | 0.0335 | 0.0163 | 3.248 |

**Minimum over ν ∈ [10⁻³, 10⁶]: s₁/s₃ = 2.342 (at ν ≈ 0.53). An isometry needs 1.000. The ladder current never reaches it, at any weight, for any up-space.**

**The mechanism, in one line:** ‖J f₁‖ = 0.913, ‖J f₃‖ = 1.126, ‖J f₅‖ = 1.210 — **the three down modes are stretched by different factors (33% spread) before any projection.** A ladder operator has k-dependent coefficients; **a partial isometry cannot.** This is structural, not numerical.

**Level 2 — the isometric (polar) part W of the same current.** W passes the gate by construction (singular values exactly 1,1,1). So the ansatz reduces to **one** checkable question with no free parameter: **does W map the down 3-space ONTO the independently specified up 3-space?** (Criterion fixed before computing: unitarity defect ≤ 0.001 = PASS-strong, ≤ 0.01 = PASS-weak, > 0.1 = FAIL. No CKM number enters — pure subspace geometry.)

| ν_W | θ₁ | θ₂ | θ₃ | defect | verdict |
|---|---|---|---|---|---|
| **3 (FORCED)** | 11.0° | 42.9° | **83.9°** | **0.7449** | **FAIL** |
| 10 | 7.5° | 27.3° | 70.3° | 0.5018 | FAIL |
| 100 | 4.2° | 24.6° | 59.1° | 0.4215 | FAIL |
| 1000 | 3.9° | 24.4° | 57.6° | 0.4138 | **FAIL (plateaus)** |

At the forced ν_W = 3 one principal angle is **83.9° — a direction of the down 3-space maps very nearly ORTHOGONAL to the up 3-space.** Defect **0.745** against the ~10⁻³ that measured CKM unitarity holds to: **fails by ~745×**, and the defect **plateaus at ≈0.41**, so no ν rescues it.

**Level 3 — define U as W(D).** Then V is unitary by construction and **predicts nothing** (the empty-confirmation failure mode).

> ## ⟹ All three branches of my Round-50 fork are now closed. **No version of "CKM = ⟨up | J | down⟩" survives.**

## ★★ THE CONSTRUCTIVE HALF — why the SM gets for free what this ansatz cannot buy
The SM's CKM is unitary **automatically**, because **V = U_up† U_down compares two orthonormal bases of ONE 3-dimensional generation space**, with the charged current **flavor-universal** — the identity on generation space, forced by gauge invariance, not fitted. **Flavor universality IS the partial-isometry condition, satisfied trivially.**

So the gate is not an obstacle course invented for BST; it is the statement *"the weak coupling is universal."* An ansatz that puts a **non-trivial degree-shifting operator** between the towers is an ansatz that **breaks flavor universality** — and that is exactly why it cannot produce a unitary CKM.

## ★★★ AND THE CORPUS ALREADY BANKED THE RIGHT FRAMING — it has been carrying both
**T2530** (the banked V_us = 1/√20, Tier D) states it in its own words:
> *"**CKM = U_up†·U_down** … V_cb/V_ub are the up-down FRAME-MISMATCH observables … **Tier-2 until the up-sector frame is pinned (K995)**."*

**T2530 and K1181 are not complementary — they are incompatible, and the corpus has been running both since 2026-08-05:**
- **T2530:** two unitaries on a common generation space → unitarity **free**, open item = **the up-sector frame**.
- **K1181/K1183:** one current matrix element between two orthogonal 3-spaces → unitarity **unobtainable**.

**The reconciliation is decidable, and it is a dichotomy:** K1181's reframe is **either** flavor-universal (J = identity on generation space) — in which case it **collapses into T2530 and adds nothing** — **or** it is not, in which case it **cannot give a unitary CKM.** *Either way it is not a route to the magnitudes.* Multiplier 0, not 1.

## ⟹ THE REDIRECT (this is the forward content, and it needs no new machinery)
> **Go back to K995. The open item is the UP-SECTOR FRAME — eigenVECTORS, not an overlap kernel.**

The corpus banks the mass **eigenvalues** (down: 1:20:840 FK-forced; up: saturation-set) and, for the down sector, some eigen**vector** content — the **texture zero** that yields Gatto and hence V_us = 1/√20 **frame-independently**. What is missing is the **up-sector frame**. That is precisely what V_cb and V_ub are waiting on, exactly as T2530 said before the reframe sent the lane hunting an overlap kernel.
**Consistency check, and it fits:** T2519 already has both mass matrices **rank-1 at leading order** (single condensate → J = 0). A rank-1 pair has a degenerate 2-dim kernel, so **the leading CKM is undefined and the entire mixing lives in the departure from rank-1.** ⟹ **The CKM magnitudes are the SIZE OF THE RANK-1 BREAKING, not an overlap.** That is a sharply located, well-posed target — and it is where I would send the next compute.

## Handoffs
- **@Elie** — paired lane: **do not fire magnitudes through a current operator.** The gate closes it before any magnitude is meaningful (and it would have killed toy 5313 before it ran). The live target is the **up-sector frame / rank-1 breaking**, target-innocent and pre-registered, per K1790's G2/G4.
- **@Keeper** — (i) **T2530 vs K1181 is a real live incompatibility**, resolvable as the dichotomy above; K1181's "mixing rides the addresses" should be **retired or re-scoped to the SKELETON only** (the parity/selection-rule content, which stands). (ii) Tier: this is a **target-innocent exclusion** (same class as T2572 and yesterday's ceiling). (iii) My Round-50 "factor 21" is **corrected to 2.70** in the registry-facing statement.
- **@Cal** — your Round-50 C2 warning generalized: I used a polar step and called it a convention; **at Level 2 the polar step is legitimate as an OBJECT (the current's isometric part) and still fails** — so the ansatz dies on geometry, not on normalization. The distinction you drew is the one that mattered.

*Scripts: scratchpad `r51_gate.py`, `r51_subspace.py`; gate updated at `play/gate_partial_isometry_mixing.py`. Nothing pushed. CP existence-only. — Grace, R51, 2026-08-22*
