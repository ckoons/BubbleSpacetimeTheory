# G1 RESULT — the FK cross-parity overlap matrix: a PROVED CEILING on the radial route (Grace, Round 50, 2026-08-22)

*Built against Elie's FILED address list (board 07:58, toy 5443), forward-only, pre-registered in `grace_PREREG_FK_overlap_matrix_construction_2026-08-22.md` BEFORE the compute (Cal B4, Keeper G3). No CKM number, no quark mass, no measured ratio enters the construction. **The result is a NEGATIVE, and it is the strongest form of negative: a ceiling, not a miss.***

## The headline
> **The cross-parity FK current overlap ⟨up even-coherent | J_W | down single-row⟩ CANNOT produce the Wolfenstein hierarchy — at ANY radius, at ANY weight ν. Exhaustive scan of the full radius cube: max achievable V_us/V_cb ≈ 1.95. Physics needs ≈ 5.4 (or ≈ 1/λ = 4.47 structurally). The mechanism falls short by a factor ≳ 2.3, and no dial closes it.**

This is the same SHAPE as Elie's O7 result today (discreteness forces at most rank = 2 addresses, ever). Two lanes, two proved ceilings, one round. **The mixing MAGNITUDES do not live in the radial overlap.**

## The instrument was validated first (my own standing rule — a negative needs a positive control)
The SAME FK metric, same code path, reproduces the banked down ladder **EXACTLY**: (ν_W)_k at ν_W = N_c = 3, k = 1,3,5 → 3 : 60 : 2520 → **1 : 20 : 840** ✓ (T2513/T2529). The tool works. So the negative is about the OVERLAP, not about a broken instrument.

## The construction (zero free parameters — the r_i are OUTPUTS)
ν-orthonormal single-row basis f_k (‖z^k‖²_ν = k!/(ν)_k); M f_k = √((k+1)/(ν+k)) f_{k+1}; J_W = M + M†.
Up modes = parity-even coherent states (F889), **A_r(m) = √((ν)_m/m!) r^m / √(S_+(r))**, S_+(r) = ½[(1−r²)^{−ν}+(1+r²)^{−ν}].
Shelves {0,2,4} fix the radii by the peak condition — **r⁴ = (m+1)(m+2)/[(ν+m)(ν+m+1)]** → **r = (0.6389, 0.7953, 0.8556)**. No dial.

★ **A real corpus-forced correction on the way in:** toy 5313 used the **FOCK** profile e^{−|z|²/2} z^k/√(k!) — a flat-space object. T2572 says explicitly the ladder's carrier is a **Wallach/kernel** object, not a Casimir/Fock one. The correct profile carries √((ν)_k) — the same weighting that gives 1:20:840. **That fix rescues 5313 from catastrophe (V_us: 7e-19 → 0.33) and still does not reach the hierarchy.** Fixing the profile was necessary and insufficient — which is what makes the ceiling meaningful rather than a repeat of a known bug.

## The numbers (ALL NINE, at the forced point; not the flattering ones)
| | pred (SVD-unitarized) | pred (row-normalized) | PDG | ratio |
|---|---|---|---|---|
| V_ud | 0.9386 | 0.6360 | 0.97435 | 0.96 |
| V_us | **0.3285** | 0.6445 | 0.22500 | **1.46** |
| V_ub | 0.1058 | 0.4245 | 0.00373 | **28.4** |
| V_cd | 0.2868 | 0.4324 | 0.22486 | 1.28 |
| V_cs | 0.9130 | 0.6371 | 0.97349 | 0.94 |
| V_cb | **0.2900** | 0.6381 | 0.04182 | **6.9** |
| V_td | 0.1919 | 0.3653 | 0.00857 | 22.4 |
| V_ts | 0.2418 | 0.6103 | 0.04110 | 5.9 |
| V_tb | 0.9512 | 0.7029 | 0.99912 | 0.95 |

**Round-trip anchor (Keeper G3):** banked V_us = 1/√20 = 0.2236 vs predicted 0.3285 → **1.47×. MISS** against my declared 20% bar. Right ORDER, wrong VALUE.
**The diagnosis is not the 47%. It is the shape:** the predicted matrix is **too democratic** — every off-diagonal is O(0.1–0.3), where Wolfenstein needs λ, λ², λ³.

## THE CEILING (the actual deliverable) — exhaustive, not a fit
Scanned the **entire radius cube** r ∈ (0,1)³ (~275k–300k triples per ν) and the weight ν over four decades. Among all triples that are raw-diagonally-dominant:

| ν | diag-dominant triples | meeting V_us/V_cb ≥ 3 | **MAX achievable V_us/V_cb** |
|---|---|---|---|
| 3 (FORCED) | 36 100 | **0** | 1.501 |
| 5 | 49 140 | **0** | 1.712 |
| 10 | 49 020 | **0** | 1.915 |
| 30 | 11 590 | **0** | **1.950 ← global max** |
| 100 | 4 818 | **0** | 1.733 |
| 300 | 1 920 | **0** | 1.643 |
| 1000 | 672 | **0** | 1.086 |

**The ceiling TURNS OVER near ν ≈ 30 at ≈ 1.95 and falls.** So it is not "the wrong ν" — **there is no ν.** Required ≈ 4.47–5.38. **Zero of ~1.1M scanned configurations meet the bar.**
Structural reason, plainly: a radial coherent state's amplitude ratio between adjacent even shelves is O(0.8) near its peak; Wolfenstein needs O(λ) = 0.22 per generation step. **A radial profile is intrinsically too broad to be a λ-generator.**

## Empty-confirmation guard (P4) — and it disarms my own "passes"
- Random increasing r-triples, **SVD-unitarized**: P2 (V_ub smallest) **35.7%**, P3 (diagonal dominance) **62.9%**, both **19.3%**.
- SVD-unitarized **uniform random 3×3**: diagonal dominance **14.3%** — *this prices the polar step alone.*
- **⟹ P3 passing at the forced point is NOT evidence.** Worse: the **raw** (un-unitarized) matrix FAILS diagonal dominance outright (V_ud = 0.636 < V_us = 0.645). **The diagonal dominance is manufactured by the polar decomposition, which is a convention choice** — exactly Cal's C2 warning ("the projection is a choice that can absorb tension"), realized. I report this against my own result.

## ★ CONVENTION-PIN OWED on a BANKED item (@Keeper — flag, NOT a contradiction claim)
**K1324 banks "V_ub uniquely smallest is FORCED"** via bidiagonal degree-1 selection (1-3 is |Δdeg| = 5). That was derived on **SINGLE SHELVES**. F889 (banked later) replaced single shelves with **coherent superpositions** — which have support on *every* even degree, so the |Δdeg| = 5 suppression has nothing to bite on. Computed both ways:
- current **J_W = M** (raising-only, the literal cup-with-h): **V_ub uniquely smallest ✓ holds** (all ν tested).
- current **J_W = M + M†** (Hermitian completion) or **M†**: **FAILS** — the minimum moves to **V_td**, at every ν tested.
**⟹ the claim is CURRENT-CONVENTION-DEPENDENT once the up-modes are coherent, where on single shelves it was not.** Per standing discipline (convention-collision check BEFORE contradiction) this is a **convention pin owed**, not a withdrawal. Keeper's call. I was one of the three blind routes on K1324, so I flag it against my own credit.

## Reconciliation with Elie's genus-5 refutation — MULTIPLIER 1, and mine subsumes
K1635 refuted Elie's rigid map r*² = 5/(2b+5) (missed at b = ν and b = 2ν). That is "**the predicted radius is wrong.**" Mine is "**no radius works.**" These are **not two votes** — mine is the general statement and Elie's is a special case of it. **Multiplier 1.** (My own R35 template, applied to my own result.)

## What SURVIVES, stated at its honest strength
- **The SKELETON — untouched and now EXPLICIT.** Bare cross-parity overlap = 0 ⟹ mixing MUST be a current matrix element. I now have that matrix element in closed form. Still structure-Derived.
- **Near-diagonality** (V_ud, V_cs, V_tb ≈ 0.94, 0.91, 0.95) — **but priced at 62.9% null, so weak.** Not a vote.
- **The magnitudes remain OPEN**, and are now open in a *located* way: **not in the radius.** Per K1635's fork, the remaining named candidate is the weak current's **Clebsch–Gordan coefficients between strata** — an angular/rep-theoretic object, not a radial one. That is where I would send the next compute.

## Tiering (Keeper G6 — address vs magnitude, separately)
- The **CEILING** (this note): a target-innocent exhaustive-scan negative on a mechanism. Proposed **DERIVED (exclusion)** — same class as T2572, which is also a growth-rate/reachability exclusion. Keeper gates.
- The **MAGNITUDES**: stay **IDENTIFIED**. Nothing here promotes them, and nothing here demotes the banked V_us (T2529/T2530) or V_cb (K1002), which ride mass-ratio routes, not this one.

*Scripts: scratchpad `fk_overlap.py`, `fk_guards.py`, `fk_exhaust.py` (+ `_hi`). Nothing pushed. CP existence-only. — Grace, G1, 2026-08-22*

---
# ★ CORRECTION (Round 51, same day) — the factor-21 below is the wrong NUMBER
The addendum reports the isometry failure at **factor 21**. That is the defect for one *particular* up 3-space (the coherent-state triple), **not** the intrinsic obstruction. Giving the ansatz its best case (let U contain the entire image J(D)) the **intrinsic, up-space-independent** ratio is **s₁/s₃ = 2.697 at ν_W = 3**, with a floor of **2.342** over ν ∈ [10⁻³,10⁶]. **I overstated the intrinsic obstruction by ~8×.** The conclusion is unchanged — 2.70 against a required 1.00 is still fatal, and now it is fatal *independently of any up-sector assumption*, which is strictly stronger. **Over-claiming a negative is the same error as over-claiming a positive.** Full run: `grace_R51_isometry_gate_closes_the_current_route_and_redirects_to_the_up_frame_2026-08-22.md`.

# ★★ ADDENDUM (same session) — THE PARTIAL-ISOMETRY GATE: a stronger, more general obstruction

The ratio ceiling above is about *magnitudes*. This is about **unitarity**, and it is prior to any magnitude.

## The theorem (three lines, exact)
CKM is unitary — not as a measured number but as a **theorem of three-generation quark field redefinition**, and BST derives the three generations in-corpus (Q⁵ truncation, T1929/K730). Write the reframe as **V = A†JB**, A and B orthonormal bases of the up 3-space U and the down 3-space D. Then
> **V†V = B†J†P_U J B = I  ⟺  ‖P_U J x‖ = ‖x‖ for all x ∈ D  ⟺  J restricted to D is a PARTIAL ISOMETRY onto U.**

So: **"CKM = a weak-current matrix element" is not free. It REQUIRES the current to act as a partial isometry between the two 3-spaces.** Equivalently: the three singular values of P_U J|_D must be **equal**.

## The test (positive-controlled)
| ν_W | s₁ | s₂ | s₃ | **s₁/s₃** | verdict |
|---|---|---|---|---|---|
| **3 (FORCED)** | 1.3183 | 0.7729 | **0.0628** | **20.99** | NOT an isometry |
| 5 | 1.1996 | 0.6943 | 0.1051 | 11.41 | NOT an isometry |
| 10 | 0.9758 | 0.5320 | 0.1323 | 7.38 | NOT an isometry |
| 30 | 0.6236 | 0.3288 | 0.1116 | 5.59 | NOT an isometry |

**Positive control:** a constructed partial isometry returns singular values (1, 1, 1), ratio 1.000000 ✓ — the test can succeed, so the negative is real.

## What this changes
1. **The SVD/polar step was not a convention — it was a falsification patch.** At the forced ν_W = 3 it discards a **factor-21** distortion. I used it above and labelled it a convention; that was too generous, and I correct it here: **the un-unitarized matrix is not nearly-unitary, and no re-parameterization makes it so.**
2. **It is stronger and more general than the ratio ceiling.** The ceiling rules out the Wolfenstein *hierarchy* for radial coherent states. This rules out *a unitary CKM at all*, for **this current**, independent of the up-state profile, before any magnitude is examined.
3. ★ **An unpriced structural cost of the K1181 reframe.** The SM gets CKM unitarity **for free**, because V = U_up† U_down is a product of two unitaries. BST's reframe (CKM = one current matrix element) does **not** get it for free — it must be **earned**. The corpus has never charged for this.

## ★ THE FORK (sharp, and it prices the whole reframe)
> **Either** J is not a partial isometry between the two 3-spaces — and then **CKM unitarity fails and the ansatz is dead**;
> **or** the up-states are *defined* as (normalized) J applied to the down-states — and then **unitarity holds by construction and the ansatz predicts nothing** (the empty-confirmation failure mode).
**A live version of the reframe must exhibit a third option: two INDEPENDENTLY specified 3-spaces between which the forced current happens to be an isometry.** That is a strong, checkable demand, and it is where I would aim the next attempt.

## STANDING GATE (mine to own, alongside the C₂↔n_C and ℝ⁴-signature gates)
> **Before any candidate mixing mechanism of the form ⟨up | J | down⟩ is fired for magnitudes, compute the three singular values of P_U J|_D. If s₁/s₃ ≠ 1, the candidate cannot produce a unitary CKM and the magnitude comparison is meaningless.**
Cheap, prior to every magnitude test, and it would have killed toy 5313 before it ran. Script: scratchpad `fk_isometry.py`. @Keeper for second-party verification.

*— Grace, addendum, 2026-08-22*
