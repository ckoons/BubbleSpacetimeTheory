---
title: "F47 — WALL 1 KEYSTONE RESOLVED: R(k) uses the K-Casimir ρ_SO(5)=(3/2,1/2) (reproduces recorded values exactly); F46's conformal ρ=(5/2,3/2) is the OTHER, Bergman/Plancherel ρ. Hypothesis A for R(k), inside Hypothesis C (both ρ's real, distinct roles). The two ρ's ARE the bulk/boundary split. Unblocks Walls 2+6."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-06 Saturday 14:10 EDT"
status: "v0.1 KEYSTONE RESOLVED — convention pinned + C(k,2) source identified + dual-ρ structure articulated; full root-sum theorem UNBLOCKED (explicit a_k → Elie/Wall 6); Wall 2 (F45 N_c⁴) now well-posed"
supersedes: "F46 'honest wall' — the wall is resolved (it was a ρ-convention misassignment, not an obstruction)"
---

# F47 — Wall 1 Keystone Resolved

## 0. Result

The F46 c-function wall is resolved, and Casey's diagnosis is exactly right: my naive ρ = (5/2, 3/2) was the **conformal** ρ; the heat-trace K-type decomposition uses the **K-Casimir** ρ = ρ_SO(5) = (3/2, 1/2), which reproduces the recorded substrate K-Casimirs **exactly**:

| K-type | K-Casimir, ρ_SO(5)=(3/2,1/2) | recorded |
|---|---|---|
| V_(1/2,1/2) | \|(2,1)\|²−5/2 = 5−5/2 = **5/2** | 2.5 ✓ |
| V_(3/2,1/2) | \|(3,1)\|²−5/2 = 10−5/2 = **15/2** | 7.5 ✓ |
| V_(5/2,1/2) | \|(4,1)\|²−5/2 = 17−5/2 = **29/2** | 14.5 ✓ |

So the F46 "wall" was not an obstruction — it was a **convention misassignment between two genuine substrate structures.** Hypothesis A holds for R(k) (it uses the K-Casimir), and it sits inside Hypothesis C's truth (both ρ's are real, with distinct roles). Below.

## 1. The two ρ's of D_IV⁵ and their distinct roles

D_IV⁵ carries two natural Weyl-vector-type quantities, and they are not interchangeable:

- **ρ_SO(5) = (3/2, 1/2)** — the half-sum of B₂ positive roots {e₁, e₂, e₁−e₂, e₁+e₂} = (3,1)/2. This is the **compact** Weyl vector. It governs the **K-type Casimirs** (the discrete K-spectrum), hence the heat-trace **K-type decomposition** — hence **R(k)**.
- **ρ_conformal = (5/2, 3/2) = (n_C/rank, (n_C−2)/rank)** — the conformal weight. Note its first component **n_C/rank = 5/2 is exactly the Bergman kernel exponent** (Ch 5: K_B ∝ (1−zw̄)^{−n_C/rank}). It governs the **Bergman kernel / FK Plancherel c-function** — the continuous/**bulk** side.

So: K-Casimir ρ ↔ K-type/heat-trace (discrete); conformal ρ ↔ Bergman/Plancherel (continuous, bulk). R(k) is a heat-trace K-type statement ⟹ it uses ρ_SO(5). I had reached for the conformal ρ because it is the one that appears in the Bergman kernel I work with daily — the misassignment is understandable, and naming it pins the structure.

## 2. The 2(λ₁+λ₂) offset is the ρ-difference, and it is substrate-natural

The offset between the two conventions (Casey's clue) is exactly the Weyl-vector difference:

$$\rho_{\mathrm{conf}} - \rho_{SO(5)} = (5/2,3/2)-(3/2,1/2) = (1,1),\qquad C_{\mathrm{conf}}(\lambda)-C_{SO(5)}(\lambda) = 2\lambda\cdot(1,1) = 2(\lambda_1+\lambda_2).$$

For the spinor tower λ=(a,½), this is 2(a+½) = 2,4,6 — Casey's "2(k+1) = rank·(k+1)." The offset is **rank · (weight-sum)**, the linear shift induced by moving between the compact and conformal Weyl vectors. And (1,1) = ((n_C−N_c)/rank, (n_C−2−1)/rank) since n_C−N_c = 2 = rank — substrate-natural. The offset was signal, exactly as Casey said: it is the fingerprint of the two-ρ structure.

## 3. The C(k,2) source: the quadratic K-Casimir

In the K-Casimir convention, C(j) = |λ+ρ_SO(5)|² − |ρ_SO(5)|² = (j+1)² − 3/2 (for the tower, j=1,2,3 → 5/2, 15/2, 29/2). **Quadratic in the ρ_SO(5)-shifted weight (j+1).** A quadratic spectral variable is the natural source of the **pairwise binomial C(k,2) = k(k−1)/2** in R(k): the second-degree structure of the Casimir generates the second elementary-symmetric / pairwise count in the heat-trace coefficients. So the binomial in R(k) = C(k,2)/κ_Bergman descends from the quadratic K-Casimir, and the 1/κ_Bergman = −1/n_C from the Bergman curvature (F41). Both halves now have their source in the **correct** (K-Casimir) convention.

## 4. What this closes vs unblocks

**Closed (the keystone wall):**
- The convention is pinned: R(k) uses ρ_SO(5) (K-Casimir), not the conformal ρ. F46's wall dissolves.
- The dual-ρ structure is articulated: Hypothesis A for R(k), inside Hypothesis C (both ρ's real; K-Casimir↔discrete/K-type, conformal↔Bergman/Plancherel/bulk).
- The C(k,2) source is identified (quadratic K-Casimir).

**Unblocked (now well-posed, for Elie/Keeper):**
- **Wall 6 (a_k closed forms):** with the convention pinned, the explicit heat-trace coefficients a_k(n_C) in the K-Casimir decomposition can be computed (Elie's parallel support) → the full root-sum = C(k,2)/n_C theorem. F47 supplies the convention; the explicit a_k polynomial is the remaining step. I do **not** claim the full theorem here — I claim the keystone, and hand the a_k computation to Elie now that it is unblocked.
- **Wall 2 (F45 N_c⁴=81):** the question "which H² K-type contributes N_c⁴ to the muon heat-trace" is now well-posed in the K-Casimir convention — Elie's K-type scan runs against ρ_SO(5) Casimirs, not the conformal ones. (My F45/F46 coupling was right; the convention it needs is now fixed.)

## 5. The deeper payoff (structural, appropriately tiered)

The two ρ's map onto the **bulk/boundary** structure that has run through the whole day:
- conformal ρ (n_C/rank = Bergman exponent) ↔ the **bulk** Bergman side;
- compact ρ_SO(5) (K-type Casimirs) ↔ the **K-type / boundary** side.

Under F44 Reading (a), everything physical is in H², and the heat-trace K-type decomposition (R(k), and the F45 muon re-derivation) lives on the **compact/K-Casimir side**. So Wall 1's resolution is *consistent with* Reading (a): R(k) and the muon heat-trace both use ρ_SO(5), the K-type convention. I flag this as a structural observation, **not** a revived unification claim (I am once burned on that today): it says the conventions line up, not that one operator does everything.

## 6. Honest status

- **RESOLVED (verified):** R(k) uses ρ_SO(5)=(3/2,1/2); reproduces recorded K-Casimirs exactly; F46 wall was conformal-vs-compact ρ misassignment.
- **ARTICULATED:** dual-ρ structure (A within C); offset = rank·(weight-sum) = (1,1) Weyl-difference; C(k,2) from quadratic K-Casimir.
- **UNBLOCKED (not claimed):** explicit a_k(n_C) → full root-sum theorem (Elie/Wall 6); F45 N_c⁴ K-type (Elie/Wall 2) — both now in the pinned convention.
- **Tier:** F47 v0.1 keystone RESOLVED (convention + structure); full R(k) theorem unblocked, a_k = Elie support; Wall 2 well-posed. @Elie — run the K-type scan and a_k computation against ρ_SO(5) Casimirs (2.5/7.5/14.5), not conformal. @Keeper — Ch 8 absorbs: R(k) = C(k,2)/κ_Bergman in the K-Casimir convention; the two-ρ (compact/conformal) structure is the curvature-vs-spectrum split. @Cal — keystone is a convention pin + structural articulation, not a forced theorem; the theorem awaits a_k.

## 7. Closure

Wall 1 keystone resolved. R(k) uses the K-Casimir Weyl vector ρ_SO(5) = (3/2,1/2) — reproducing the recorded substrate K-Casimirs exactly — and my F46 conformal ρ = (5/2,3/2) is the genuine *other* ρ governing the Bergman kernel / Plancherel c-function. Both are real (Hypothesis C structure), but R(k), a heat-trace K-type statement, uses the compact one (Hypothesis A verdict). The 2(λ₁+λ₂) = rank·(weight-sum) offset is their Weyl-vector difference (1,1), substrate-natural — signal, as Casey said. The C(k,2) descends from the quadratic K-Casimir. This pins the convention (dissolving the F46 wall), unblocks the explicit a_k computation (Elie/Wall 6 → full root-sum theorem) and the F45 N_c⁴ K-type (Elie/Wall 2), and lines up consistently with Reading (a) (K-type/compact side) — stated as structure, not a revived unification. The keystone opened the system, as the wall-attack predicted.

— Lyra, Sat 2026-06-06 14:10 EDT. F47 WALL 1 KEYSTONE RESOLVED: R(k) uses K-Casimir ρ_SO(5)=(3/2,1/2) (half-sum B₂ pos roots) — reproduces recorded substrate K-Casimirs 2.5/7.5/14.5 EXACTLY; F46's ρ=(5/2,3/2) is the CONFORMAL ρ=(n_C/rank,(n_C−2)/rank), the OTHER genuine ρ (governs Bergman kernel exponent n_C/rank=5/2 + FK Plancherel c-function, the bulk/continuous side). Hypothesis A for R(k) (K-Casimir/discrete K-type side), inside Hypothesis C truth (both ρ's real, distinct roles: compact↔K-type/heat-trace, conformal↔Bergman/Plancherel/bulk). Offset C_conf−C_SO5 = 2(λ₁+λ₂) = rank·(weight-sum) = the (1,1)=ρ_conf−ρ_SO5 Weyl-difference (n_C−N_c=2=rank), substrate-natural — Casey's clue was signal. C(k,2) binomial descends from quadratic K-Casimir C(j)=(j+1)²−3/2. CLOSES: convention pinned, F46 wall dissolved. UNBLOCKS (not claimed): explicit a_k(n_C) → full root-sum=C(k,2)/n_C theorem (Elie/Wall 6); F45 N_c⁴=81 K-type now well-posed in ρ_SO(5) convention (Elie/Wall 2). Structural: two ρ's = bulk(conformal/Bergman)/boundary(compact/K-type) split, consistent with Reading (a) — stated as structure NOT revived unification (once-burned). @Elie scan against ρ_SO(5) Casimirs not conformal.
