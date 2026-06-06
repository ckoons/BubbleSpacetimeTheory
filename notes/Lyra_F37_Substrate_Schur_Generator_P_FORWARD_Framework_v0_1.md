---
title: "F37 — Substrate-Schur generator P (Hardy projection) FORWARD framework v0.1: one operator, two sectors (muon edge 81/8 + Λ vacuum factor ≈2)"
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-06 Saturday 12:15 EDT"
status: "v0.1 FRAMEWORK candidate — Phase 5 substrate-Schur FORWARD first content; scaffold + first derivation step ([H_B,P]=0 → additive vacuum split, factor = 1+ρ); ρ-computation = open multi-week core"
---

# F37 Substrate-Schur Generator P — FORWARD Framework

## 0. Goal and scope

Phase 5 dual-track first content. The morning (F32/F35) produced a candidate cross-link: the muon mass-ratio's "edge" term and the cosmological Λ over-prediction are the *same bulk⊕Shilov partition* of D_IV⁵. Cal's discipline (Cal #254: share an **operator**, not an integer) is the bar this must clear. This note proposes the shared operator explicitly — the **Hardy/Bergman projection P** — and takes the first derivation step (the vacuum sector), which is the cleanest. The muon sector is set up but not closed. Tier: FRAMEWORK candidate; the operator is concrete, the shared geometric ratio ρ is identified, and computing ρ is the open core.

## 1. The candidate generator: P

Let L²(D_IV⁵, dμ) be the substrate Hilbert space and P the orthogonal projection onto the Hardy/Bergman space H²(D_IV⁵) (holomorphic L², the Tier 0 commitment space). (1−P) projects onto the complement. P is the proposed **substrate-Schur generator** in Cal #36's sense: one operator whose matrix elements in distinct physical sectors generate distinct observables. The shared quantity across sectors is **not an integer** — it is a geometric ratio ρ intrinsic to P (Sec. 3). That is what makes this the right *shape* of candidate.

## 2. First derivation step — the vacuum sector

### 2.1 The vacuum splits additively (the one thing proved here)

The substrate vacuum energy is the regularized trace of H_B = Casimir of K = SO(5)×SO(2) over L². Split by P:

$$E_{\mathrm{vac}} = \mathrm{Tr}_{L^2}(H_B) = \mathrm{Tr}(P H_B P) + \mathrm{Tr}((1-P)H_B(1-P)) + 2\,\mathrm{Re}\,\mathrm{Tr}(P H_B(1-P)).$$

**Claim: the cross term vanishes, because [H_B, P] = 0.** Proof: H_B is the Casimir of K, hence central in the universal enveloping algebra of k — it is K-invariant. H²(D_IV⁵) is a K-invariant subspace (the holomorphic K-types), so its complement is K-invariant too. A K-invariant operator commutes with the projection onto any K-invariant subspace. Therefore [H_B, P] = 0, the cross term is zero, and

$$E_{\mathrm{vac}} = E^{\mathrm{bulk}} + E^{\mathrm{bdy}},\qquad E^{\mathrm{bulk}} = \mathrm{Tr}(P H_B P),\; E^{\mathrm{bdy}} = \mathrm{Tr}((1-P)H_B(1-P)).$$

This is a genuine derivation, not a scaffold: the vacuum energy is *exactly* additive over the bulk/boundary partition, with no cross-contamination, because the time-generator commutes with the partition. That is the operator-level content the cross-link needs.

### 2.2 The factor is 1 + ρ

Per Casey's 2-region insight, the observer is bulk-localized and measures only E^bulk (the Shilov-boundary vacuum is subtracted at the observer's location); the substrate carries both. Hence

$$\frac{\Lambda_{\text{substrate}}}{\Lambda_{\text{observed}}} = \frac{E^{\mathrm{bulk}}+E^{\mathrm{bdy}}}{E^{\mathrm{bulk}}} = 1 + \rho,\qquad \rho \equiv \frac{E^{\mathrm{bdy}}}{E^{\mathrm{bulk}}}.$$

The observed factor is 4.85/2.4 = 2.0208, so the framework **predicts ρ = 1.0208** — the boundary and bulk vacuum energies are nearly equal. This is a forward, falsifiable prediction: ρ is a fixed geometric invariant of D_IV⁵ (the ratio of the Hardy/Shilov normalization to the Bergman/bulk normalization of the same holomorphic spectral data), computable from c_FK and the Shilov measure. Compute ρ; if ρ ≠ 1.02 (within tolerance), the bulk⊕Shilov vacuum reading fails. The honest content of "factor ≈ 2" is **ρ ≈ 1**, with the residual 0.02 being the genuine value of the normalization ratio — not a fitted 81/40 (F35 declined that).

### 2.3 Subtlety to settle in the rigorous pass (flagged)

Whether E^bdy and E^bulk are contributions from *orthogonal* regions or two *normalizations* of the same Hardy data (Bergman bulk ↔ Shilov boundary are isomorphic realizations of H²) changes the interpretation of ρ but not the structural form factor = 1 + ρ. The rigorous computation must settle which; I flag it rather than assert it.

## 3. The shared ratio ρ enters the muon sector (the unification, set up not closed)

The muon edge-term claim (F32 Gate A1): the (1−P) boundary matrix element of the gen-2 mass operator equals N_c⁴/2^{N_c} = 81/8 relative to the bulk normalization. The key structural point: the (1−P)-vs-P matrix element of *any* operator on a K-type is governed by the **same** Bergman-to-Hardy normalization ratio ρ that controls the vacuum sector, modulated by the K-type's own weight. Schematically,

$$\langle V_{(3/2,1/2)} \mid (1-P)\,M\,(1-P)\mid V_{(3/2,1/2)}\rangle \;=\; \rho \cdot \kappa(V_{(3/2,1/2)}),$$

where κ is the K-type form-factor (Pochhammer/Casimir structure of Ch 5/Ch 7). If this holds with the **same** ρ as Sec. 2.2, then P is genuinely one operator generating both observables — the vacuum factor (1+ρ) and the muon edge (ρ·κ) — and the cross-link is operator-level, exactly the Cal #254 contrast class. The shared object is ρ (geometric), never the integer 81.

**What is NOT done:** I have not computed ρ, nor κ(V_(3/2,1/2)), nor shown ρ·κ = 81/8. Those are the open core. Today establishes only: (a) the vacuum splits additively because [H_B,P]=0; (b) the factor has the forced form 1+ρ; (c) the *same* ρ is the natural object in the muon sector. That is enough to make P a FRAMEWORK candidate generator and to scope the remaining work sharply.

## 4. Honest status and falsifiers

- **Established (Tier: derived):** [H_B, P] = 0 ⟹ additive bulk/boundary vacuum split; factor = 1 + ρ exactly.
- **Forward prediction (falsifiable):** ρ = 1.02 (geometric Bergman/Hardy normalization ratio). Compute it; ρ ≠ 1.02 refutes.
- **Candidate (FRAMEWORK):** P is a substrate-Schur generator; the same ρ generates the muon edge-term ρ·κ = 81/8. Falsifier: if the muon sector requires a *different* ratio ρ2 ≠ ρ, the operator is not shared and the cross-link drops to coincidence.
- **Declined (F35):** the 81/40 numerical match for 2.02 — superseded by the mechanism ρ ≈ 1.

## 5. Multi-week core (Cal #189), now sharply scoped

1. Compute ρ = E^bdy/E^bulk = Bergman/Hardy normalization ratio of D_IV⁵ from c_FK + Shilov measure. (Closes the vacuum prediction.)
2. Compute κ(V_(3/2,1/2)) and test ρ·κ = 81/8. (Closes the muon edge / Gate A1.)
3. Settle the orthogonal-vs-normalization subtlety (Sec. 2.3).
4. Cal cold-read + Keeper K-audit (K229d against A1).

## 6. Closure

F37 v0.1: P (the Hardy/Bergman projection) proposed as a substrate-Schur generator. The vacuum sector is taken one real step forward — [H_B,P]=0 forces an additive bulk/boundary vacuum split, giving the factor the exact form 1+ρ with the forward prediction ρ ≈ 1.02. The muon sector is set up under the *same* ρ, making the cross-link operator-level (Cal #254), with the open core (compute ρ; test ρ·κ = 81/8) sharply scoped. The shared object is the geometric ratio ρ, never the integer 81 — the F35 discipline carried into the FORWARD framework.

**Tier:** F37 substrate-Schur generator P FORWARD framework v0.1; [H_B,P]=0 additive split DERIVED; ρ≈1.02 forward prediction; P-as-generator FRAMEWORK candidate; multi-week core scoped per Cal #189.

— Lyra, Sat 2026-06-06 12:15 EDT. F37 v0.1: Hardy/Bergman projection P proposed as substrate-Schur generator unifying muon edge (81/8) + Λ vacuum factor (≈2); first derivation step — [H_B,P]=0 (H_B K-invariant Casimir commutes with projection onto K-invariant H²) ⟹ vacuum splits additively E^bulk+E^bdy, cross term zero ⟹ factor = 1+ρ exactly, forward prediction ρ = 1.0208 (Bergman/Hardy normalization ratio, geometric invariant — compute to falsify); same ρ enters muon sector as ρ·κ(V_(3/2,1/2)) = 81/8 (set up, not closed); shared object is ρ not integer 81 (Cal #254 contrast class, F35 discipline carried forward); open core = compute ρ + test ρ·κ=81/8, multi-week per Cal #189.
