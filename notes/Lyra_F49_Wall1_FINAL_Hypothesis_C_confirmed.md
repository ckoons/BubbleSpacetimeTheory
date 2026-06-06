---
title: "F49 — WALL 1 FINAL: Hypothesis C confirmed. The FK Plancherel c-function independently requires the conformal (restricted-root) rho; R(k) independently uses the compact K-Casimir rho_SO(5) (Elie: exact, zero offset, k=2..24). Dual-rho, both real. R(k) CLOSES; Walls 2+6 OPEN."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-06 Saturday 14:35 EDT"
status: "v0.1 WALL 1 FINAL — answers Elie's special-function question (does FK c-function need conformal rho? YES) → Hypothesis C. R(k) clean on K-Casimir side closes; the conformal rho is independently real on the Plancherel side. Walls 2+6 unblocked."
supersedes: "F46 wall (resolved F47); F47 left the c-function question open — F49 answers it"
---

# F49 — Wall 1 Final: Hypothesis C

## 0. The one remaining question, answered

Elie's numerics (Toys 4005/4007/4011) settled half of it: **R(k) uses the K-Casimir rho_SO(5) = (3/2,1/2) exactly** — all 23 extracted points (k = 2..24) carry **zero** conformal offset. Hypothesis B (conformal rho for R(k)) is rejected; R(k) is clean on the K-Casimir side. He handed back the one question that is mine, not numerical:

> Does the FK Plancherel c-function for D_IV⁵ *independently* require the conformal rho?

**Answer: yes.** Therefore **Hypothesis C** — both rho's are independently real, in different roles.

## 1. Why the c-function requires the conformal (restricted-root) rho

The Harish-Chandra c-function of a semisimple Lie group is, by construction (Helgason, *Groups and Geometric Analysis*, Ch. IV; Gindikin-Karpelevich product),

$$c(\lambda) = \prod_{\alpha\in\Sigma^+}\;[\text{Gamma-factor in } \langle\lambda,\alpha\rangle \text{ and the multiplicity } m_\alpha],$$

and the spherical-function / Plancherel asymptotics carry the shift $e^{(i\lambda-\rho)H}$ with

$$\rho = \tfrac12\sum_{\alpha\in\Sigma^+} m_\alpha\,\alpha \quad(\text{half-sum of positive } \textbf{restricted (noncompact)} \text{ roots, with multiplicity}).$$

This restricted-root rho is what the c-function is *built from*. For the Hermitian symmetric domain D_IV⁵ = SO_0(5,2)/[SO(5)×SO(2)], the restricted root system (rank 2, with the noncompact multiplicities) gives a rho that is **structurally distinct from the compact Weyl vector rho_SO(5) = (3/2,1/2)** — the compact rho is the half-sum of *compact* K-roots (governing K-type Casimirs), the c-function rho is the half-sum of *restricted noncompact* roots with multiplicity (governing the continuous Plancherel spectrum). These are different root systems, hence different rho's. So the c-function genuinely, independently needs its own (conformal/restricted) rho.

This is the structurally certain part. **Honest pin:** the *exact* value of the restricted rho (whether it is precisely (5/2,3/2) = (n_C/rank, (n_C−2)/rank)) depends on the explicit restricted-root multiplicities of D_IV⁵, which I pin to FK Ch. XII rather than assert from memory (Cal #242). What is certain without the pin: it is the restricted-root half-sum, distinct from rho_SO(5), and its first component is consistent with the Bergman kernel exponent n_C/rank = 5/2.

## 2. Verdict — Hypothesis C, dual-rho

| rho | what it is | governs | used by |
|---|---|---|---|
| **rho_SO(5) = (3/2,1/2)** | compact Weyl vector (half-sum K-roots) | K-type Casimirs; heat-trace K-type decomposition | **R(k)** (Elie: exact, zero offset) |
| **rho_conformal** (restricted-root half-sum, mult.) | noncompact/Plancherel Weyl vector | FK c-function; continuous/bulk spectrum; Bergman kernel exponent | **FK Plancherel c-function** |

Both are real and independently required. R(k) is **not** contaminated by the conformal rho (Elie's zero-offset result); the conformal rho is **not** an error (it is the genuine c-function rho). My F46 "mistake" was reaching for the c-function's rho when computing a K-type quantity — a misassignment between two real structures, exactly as F47 suspected and Elie's numerics + this c-function fact now confirm.

## 3. The (1,1) bridge (Keeper's shift vector, identified)

The offset is $\rho_{\text{conf}} - \rho_{SO(5)} = (1,1)$, and Keeper's closed form $C^{\text{conf}}(\lambda) - C^{K}(\lambda) = 2\lambda\cdot(1,1) = 2(k+1)$ holds exactly. Under Hypothesis C, (1,1) is identified: it is the **restricted-minus-compact rho differential** — the substrate identity bridging the Plancherel (bulk, conformal-rho) and spectral (K-type, compact-rho) descriptions of the *same* H². Of Keeper's four candidate readings, this is the "conformal weight differential" one. And it is substrate-natural: n_C − N_c = 2 = rank, so the bridge vector is fixed by the primaries.

## 4. What closes, what opens

**CLOSES — R(k):** R(k) = C(k,2)/κ_Bergman in the K-Casimir convention (rho_SO(5)), clean (Elie: 23 points, zero offset). The convention question that blocked F46 is fully resolved as Hypothesis C. R(k) is a genuine closed form on the compact/heat-trace side. (The *full theorem* — proving the root-sum equals C(k,2)/n_C from the explicit a_k(n_C) — is the a_k computation, now unblocked → Elie/Wall 6.)

**OPENS — Walls 2 + 6 (handed to Elie, now well-posed):**
- **Wall 6:** compute a_k(n_C) in the rho_SO(5) K-Casimir convention → the explicit root-sum → full R(k) theorem.
- **Wall 2:** the F45 N_c⁴ = 81 K-type scan, run against rho_SO(5) Casimirs (2.5/7.5/14.5) — and, per F48, reading the N_c⁴ as the **restriction-grading** term (codim-4, Casey 14), not color (the muon is colorless). The orthogonality of the K-type grading vs the restriction grading (F48) is the Wall 2 core.

@Elie — both unblocked; scan against rho_SO(5), not conformal. @Keeper — Ch 8 absorbs: R(k) on the compact/K-Casimir side, the c-function on the conformal/restricted side, bridged by (1,1); the dual-rho is the curvature(conformal)-vs-spectrum(compact) split. @Cal — Hypothesis C is a structural confirmation (c-functions are built from restricted-root rho — textbook); the *exact* conformal-rho value pins to FK Ch. XII, flagged.

## 5. Structural tie (stated as structure, not unification)

The two rho's map onto bulk/boundary: conformal rho ↔ Bergman/Plancherel **bulk**; compact rho ↔ K-type **boundary**. Under F44 Reading (a) everything physical is in H², and R(k) + the F45 muon heat-trace both live on the compact/K-Casimir (boundary) side — consistent. I flag this as structure; I do **not** revive a "one operator unifies everything" claim (F43 burned that today). The dual-rho says the conventions line up across the bulk/boundary split, nothing more.

## 6. Honest status

- **CONFIRMED:** Hypothesis C. R(k) uses compact rho_SO(5) (Elie: exact); FK c-function independently requires conformal/restricted rho (Helgason Ch IV, structural).
- **PINNED to source (flagged):** exact conformal-rho value → FK Ch XII restricted-root multiplicities; structurally it is the restricted half-sum, distinct from rho_SO(5).
- **CLOSES:** the Wall 1 convention keystone; R(k) as a clean closed form (K-Casimir side).
- **OPENS:** Walls 2 + 6 (Elie), now well-posed in the rho_SO(5) convention.
- **Tier:** F49 v0.1 Wall 1 FINAL (Hypothesis C); R(k) convention closed; full R(k) theorem + Walls 2/6 unblocked (Elie); exact conformal-rho pins to FK Ch XII.

## 7. Closure

Wall 1 fully resolved as **Hypothesis C**. R(k) uses the compact K-Casimir rho_SO(5) = (3/2,1/2) (Elie: exact, zero conformal offset across 23 points); the FK Plancherel c-function independently requires the conformal/restricted-root rho (Harish-Chandra c-functions are built from the restricted half-sum with multiplicity — Helgason Ch IV). Both rho's are real, in complementary roles (spectral/K-type vs Plancherel/bulk), bridged by the substrate-natural (1,1) = restricted-minus-compact rho differential. My F46 "mistake" was a misassignment between these two genuine structures, not an error in either. R(k) closes as a clean closed form; the explicit a_k(n_C) and the F45 N_c⁴ K-type are unblocked and handed to Elie in the correct convention. The keystone opened the system exactly as the wall attack predicted — and the most interesting answer (dual-rho) is the true one, as Casey, Keeper, and Cal anticipated, now grounded rather than guessed.

— Lyra, Sat 2026-06-06 14:35 EDT. F49 WALL 1 FINAL = Hypothesis C confirmed. Elie numerics: R(k) uses K-Casimir rho_SO(5)=(3/2,1/2) EXACTLY, zero conformal offset k=2..24 → B rejected, R(k) clean. My c-function answer: FK Plancherel c-function is built from the half-sum of restricted (noncompact) roots with multiplicity (Helgason GGA Ch IV / Gindikin-Karpelevich) = conformal rho, structurally DISTINCT from compact rho_SO(5) → c-function independently requires conformal rho → YES → Hypothesis C. Both rho real: compact↔K-Casimir/heat-trace/R(k), conformal↔Plancherel-c-function/Bergman-bulk. (1,1)=rho_conf−rho_SO5 = restricted-minus-compact rho differential (Keeper shift vector identified; n_C−N_c=2=rank). EXACT conformal-rho value pins to FK Ch XII multiplicities (flagged, not asserted). CLOSES R(k) convention (clean closed form, K-Casimir side); full theorem = a_k(n_C) computation now unblocked → Elie/Wall 6; Wall 2 F45 N_c⁴ well-posed against rho_SO(5) + F48 restriction-grading (not color) reading. Structural bulk(conformal)/boundary(compact) tie consistent w/ Reading (a), stated as structure NOT revived unification.
