---
title: "Vol 16 Chapter 7 — Bergman Kernel as Matrix-Coefficient Sum: v0.3 bulk⊕Shilov matrix-element machinery (F37 support)"
authors: "Lyra + Elie joint (Elie primary v0.3 — Bergman matrix-element machinery for F37 ρ-computation)"
date: "2026-06-06 Saturday ~11:55 EDT (date-verified)"
status: "v0.3 SUBSTANTIVE — bulk⊕Shilov matrix-element decomposition; supplies F37 (ρ) + K229d (81/8) machinery"
volume: "Vol 16 Substrate Algebra"
chapter: "Ch 7 Bergman Kernel as Matrix-Coefficient Sum"
prior: "v0.1 → v0.2 (Hua-Schmidt + Mehler)"
toy: "toy_4004_ch7_bergman_matrix_element_support_for_F37.py (SCORE 6/6)"
---

# Vol 16 Chapter 7 v0.3 — bulk⊕Shilov matrix-element machinery

## 0. v0.3 Purpose

v0.2 gave the Bergman kernel = K-type matrix-coefficient sum + Mehler family. v0.3
supplies the **bulk⊕Shilov matrix-element machinery** Lyra needs for the F37
ρ-computation (Λ^(1/4) vacuum over-prediction) and the K229d 81/8 boundary
matrix-element gate. Discipline: VERIFY what is checkable (norm ladder, FK constants),
SET UP what is open (81/8, ρ) without evaluating — the evaluations are Lyra's FORCING
steps (K229d / F37), weighing 0 in any FORCING inventory until forced (Cal #189).

## 1. Bergman K-type norm ladder (verified, Toy 4004 G1)

The Pochhammer norms of the spinor K-types and their gen-step ratios (exact):

| K-type | norm (×π) | gen-step ratio | identity |
|---|---|---|---|
| V_(1/2,1/2) gen1 | 3/128 | — | 3π/2^g |
| V_(3/2,1/2) gen2 | 21/512 | 7/4 | **g/rank²** |
| V_(5/2,1/2) gen3 | 567/8192 | 27/16 | **N_c³/rank⁴** |

Honest note (Cal #34): the two gen-steps are NOT one clean multiplicative law —
g/rank² then N_c³/rank⁴ (numerators g=7 vs N_c³=27 differ in form; denominators
rank^(2·step)). The cascade is step-dependent; do not over-read it as a single rule.

## 2. FK normalization + the two kernel exponents (verified, Toy 4004 G2)

- Bergman (bulk) kernel: K_B = c_FK · h(z,w̄)^{-(n_C+rank)/2} = c_FK · h^{-7/2},
  c_FK = 225/π^(9/2) (T2442; 225 = (N_c·n_C)²).
- Cauchy–Szegő (Shilov boundary) kernel: exponent **n_C/2 = 5/2** (genus/2, type IV).
- **Exponent gap bulk − Shilov = rank/2 = 1.** This single-unit gap is the geometric
  seam between the two regions (Section 3).

## 3. The bulk⊕Shilov 2-region partition (machinery, Toy 4004 G3)

Hardy space H²(D_IV⁵) splits via the Cauchy–Szegő projection **P** (ONE operator):
- **P** → bulk: holomorphic extension of boundary data (Bergman volume, exponent 7/2)
- **(1−P)** → Shilov boundary defect (Cauchy–Szegő boundary integral, exponent 5/2)

Operator matrix-element decomposition:
$$\langle V_\lambda | O | V_\lambda\rangle = \underbrace{\langle V_\lambda|P\,O\,P|V_\lambda\rangle}_{\text{bulk}} + \underbrace{\langle V_\lambda|(1{-}P)\,O\,(1{-}P)|V_\lambda\rangle}_{\text{Shilov}}.$$

**This is the source of the "vacuum region count = 2"**: bulk + Shilov = two regions
through the single projection P (Casey's 2-region insight; Lyra A2). The shared object
across the mass-sector (81/8) and the vacuum-sector (factor 2) is the **operator P**,
not an integer (Cal #254 — the strong contrast class).

## 4. Boundary matrix-element scaffold → 81/8 (SETUP; Lyra K229d gate, OPEN)

A1 claim (Lyra): the muon Hardy-(1−P) boundary matrix element = N_c⁴/2^{N_c} = **81/8**.
v0.3 supplies the integral form:
$$M_{\rm bdy}({\rm gen2}) = \langle V_{(3/2,1/2)} | (1{-}P) | V_{(3/2,1/2)}\rangle = \frac{1}{\mathcal{N}}\int_{\partial_S D_{IV}^5} m^{(3/2,1/2)}(b,\bar b)\,d\sigma(b),$$
over the Shilov boundary ∂_S D_IV⁵ = S⁴×S¹/Z₂, with Cauchy–Szegő exponent 5/2 and the
gen-2 norm 21π/512 (Section 1). Numerator N_c⁴ = 81 (color⁴), denominator 2^{N_c} = 8
(Hardy boundary 2^{N_c}). **STATUS: OPEN** — evaluation = 81/8 is Lyra's K229d FORCING
step (falsifier: the boundary matrix element equals 81/8 or it does not). Weighs 0
until forced.

## 5. ρ-computation scaffold (SETUP; Lyra F37 gate, OPEN)

The Λ^(1/4) over-prediction: 2.02 = 4.85/2.4 (substrate-predicted/observed). Reading
(Lyra A2): factor ≈ 2 = bulk+Shilov region count (Section 3); residual ρ is the
per-region correction:
$$\Lambda^{1/4}_{\rm pred} = (\text{region count}=2)\cdot \rho \cdot \Lambda^{1/4}_{\rm base}, \qquad \rho = 2.02/2 \approx 1.01\ (\text{target band }1.01\text{–}1.02).$$
F37 forward target: compute ρ from the bulk/Shilov Bergman-norm ratio (schematically
ρ = [∫_bulk K_B^{7/2}] / [2·∫_Shilov S^{5/2}]). All ingredients supplied: c_FK (Sec 2),
exponents 7/2 vs 5/2 (Sec 2), K-type norms (Sec 1), projection P (Sec 3). **STATUS:
OPEN** — the explicit ρ is Lyra's F37 derivation. If ρ ∈ [1.00, 1.04], it closes the
Λ^(1/4) over-prediction as (2 regions) × (small per-region ρ); ρ outside the band or
no closed form removes the 2-region reading (Cal #237 elimination semantics).

## 6. v0.3 status + handoff

- **Verified** (Toy 4004 G1–G2): norm ladder (7/4, 27/16), c_FK, bulk/Shilov exponents.
- **Machinery** (G3): bulk⊕Shilov 2-region partition via single projection P.
- **Handed to Lyra, OPEN**: 81/8 boundary matrix element (K229d, G4); ρ scaffold (F37, G5).

→ Lyra: the matrix-element machinery for F37 ρ + K229d 81/8 is in place (toy_4004).
Both are set up with explicit integrals; the FORCING evaluations are yours. Cross-anchor:
Ch 4 v0.7 σ-distance tiering applies to whatever observable values F37 produces.

— Elie, Saturday 2026-06-06 ~11:55 EDT (date-verified). Continuing per long-run cadence.
