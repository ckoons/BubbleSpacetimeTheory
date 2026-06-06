---
title: "Vol 16 Chapter 7 — Bergman Kernel as Matrix-Coefficient Sum: v0.6 Reading (a) framing (two realizations of one H²; muon edge = color factor)"
authors: "Lyra + Elie joint (Elie primary v0.6 — Reading (a) constructive framing + Toy 4009 narrowing)"
date: "2026-06-06 Saturday ~13:25 EDT (date-verified)"
status: "v0.6 SUBSTANTIVE — Reading (a) framing applied; Szegő/Bergman machinery retained; muon edge re-posed as color-factor question"
volume: "Vol 16 Substrate Algebra"
chapter: "Ch 7 Bergman Kernel as Matrix-Coefficient Sum"
prior: "v0.4 (Szegő constant) → v0.5 (Cal #259/F43 walk-back)"
toy: "toy_4009_muon_edge_81_8_reading_a_ktype_scan.py (SCORE 5/5)"
---

# Vol 16 Chapter 7 v0.6 — Reading (a) framing

## 0. v0.6 Purpose

v0.5 withdrew the operator-unification (Cal #259/F43). v0.6 applies **Lyra F44
Reading (a)** constructively: states what bulk/boundary mean once "(1−P)" is fixed,
retains the genuinely-valid machinery, and re-poses the muon edge as the narrowed
rep-theory question (Toy 4009). This keeps the curriculum chapter Reading-(a)-clean
before EOD.

## 1. Reading (a): bulk and boundary are TWO REALIZATIONS of ONE H²

Reading (a) (Lyra F44): everything physical lives in H²(D_IV⁵); there is **no physical
(1−P) complement**. The "bulk" (Bergman volume realization) and the "Shilov boundary"
(Cauchy–Szegő realization) are **two realizations of the same Hardy space H²**, related
by the holomorphic-extension isometry — not two physically distinct regions.

Consequence (retires v0.4 §1 + the F38 line): the Hardy isometry proves E[P] = E[P]
about P; it does **not** pin ρ = E[(1−P)]/E[P]. There is no additive "bulk + boundary"
split of one K-type's content — that would double-count the same H² vector in its two
realizations. **Withdrawn permanently** (not just for the vacuum): any "bulk-term +
boundary-term" for a single K-type.

## 2. What machinery REMAINS valid (standalone tools)

These do not depend on a (1−P) complement and survive Reading (a) intact:
- **Szegő / Bergman constants**: c_FK = 225/π^(9/2); Bergman exp 7/2, Cauchy–Szegő exp
  5/2; Shilov volume vol(S⁴×S¹/Z₂) = 8π³/3. (Toy 4006 G1.) These are FK normalization
  facts about the two realizations of H², usable as computational tools.
- **K-type Bergman/Pochhammer norm ladder** + gen-step ratios 7/4 = g/rank², 27/16 =
  N_c³/rank⁴ (Ch 7 v0.3, Toy 4004). Properties of H² K-types, realization-independent.
- **Product structure of the Shilov realization** (S⁴×S¹/Z₂) — a fact about the
  boundary realization, fine to use; it just does not license a complement-split.

## 3. The muon edge 81/8, re-posed under Reading (a) (Toy 4009)

Under Reading (a), m_μ/m_e = 207 = 1575/8 + 81/8 can only be additive if 1575/8 and
81/8 are **two distinct H² structures**, not two realizations of one. Toy 4009 scan:
- **1575/8 = n_C·(5/2)₃** = clean native gen-2 V_(3/2,1/2) spinor K-type term. ✓
- **81/8 is NOT a spinor-ladder Pochhammer** and **NOT a clean dim/Casimir K-type
  coefficient** (only a contrived C₂·N_c³/rank⁴ hit). It is intrinsically the
  **color-tensor form N_c⁴/2^{N_c}** (note 2^{N_c} = 8 = rank^{N_c}), living in the
  **SU(N_c) color factor**, NOT the K=SO(5)×SO(2) spinor ladder.

**Narrowed question (the load-bearing next-session decision):**
> Does the substrate Hilbert space factorize as **H²(D_IV⁵) ⊗ ℂ^{color}** for the muon?
- **Option A (factorizes):** spinor K-type (1575/8) and color factor (81/8) are distinct
  tensor factors → additive, no double-count → **Composite v0.5 rescued under Reading (a)**.
- **Option B (entangled):** color not independent → additive **fails**; m_μ/m_e=207 needs
  a non-additive substrate form (honest negative).

This is a representation-theory call (does the muon's substrate state factorize?), not a
numerical one — Toy 4009 removed the single-spinor-K-type possibility.

## 4. v0.6 status

- **Withdrawn (permanent under Reading (a))**: single-K-type bulk+boundary split; Hardy-
  isometry-pins-ρ (v0.4 §1).
- **Retained (valid tools)**: Szegő/Bergman constants, K-type norm ladder, Shilov product.
- **Re-posed**: muon edge 81/8 = color-tensor form → Option A/B rep-theory decision (Lyra).
- **Survivor headline** (from v0.5, strengthened): R(k) = −C(k,2)/n_C = C(k,2)/κ_Bergman —
  the heat-trace sum-of-roots as Bergman curvature (Ch 8 cross-link, next).

— Elie, Saturday 2026-06-06 ~13:25 EDT (date-verified). Toy 4009 SCORE 5/5.
