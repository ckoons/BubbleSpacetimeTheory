---
title: "P4.3 — holomorphic discrete series K-type framework v0.1 (bulk/spinor towers, Casimirs, mass-mechanism honest assessment). Bulk tower V_(k,0) and spinor radial tower V_(1/2+k, 1/2) computed; CRITICAL FINDING: simple Casimir-squared mass ratios do NOT match observed lepton ratios (m_μ/m_e ≈ 207, m_τ/m_μ ≈ 17). L4 v0.2 must connect existing BST mass closed-forms (T190, T2003, T187) to the dictionary, not derive ratios from naive Casimir towers."
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-30 Saturday 12:20 EDT"
status: "FRAMEWORK + HONEST FINDING (P4.3). Bulk K-type tower structure of L²_hol(D_IV⁵) set up: V_(k,0) at SO(2) charge k with Casimir k(k+3), dim (k+1)(k+2)(2k+3)/6. Spinor radial tower V_(1/2+k, 1/2) Casimirs = (k+1/2)(k+7/2) + 3/4 = 5/2, 15/2, 29/2, 47/2 (arithmetic +2 spacings). Critical finding: simple mass²∝Casimir gives ratios ~1.73 (k=1/k=0), 1.39 (k=2/k=1) — NOT m_μ/m_e ≈ 207 or m_τ/m_μ ≈ 17. So L4 v0.2 must connect existing BST mass mechanisms (T190 (24/π²)^6, T2003 49·71, T187 6π⁵) to the dictionary, NOT re-derive via Casimir towers."
---

# P4.3 — holomorphic discrete series K-type framework v0.1

## 0. The setup

The bulk Hilbert space L²_hol(D_IV⁵) decomposes under K = SO(5)×SO(2) as a direct sum of K-types. The holomorphic tangent at the origin is T^(1,0) = 5_(+1) (vector of SO(5) at SO(2) charge +1); the bulk K-types come from Sym(T^(1,0)*).

## 1. The bulk symmetric tower V_(k,0)

Sym^k(5) of SO(5) decomposes as ⊕_{j=0}^{floor(k/2)} V_(k−2j, 0) (symmetric tensors of decreasing trace). The LOWEST K-types in each Sym^k are V_(k, 0).

| k | K-type | Weyl dim (SO(5)) | Casimir = k(k+3) |
|---|---|---|---|
| 0 | V_(0,0) | 1 | 0 |
| 1 | V_(1,0) | 5 = n_C | 4 = rank² |
| 2 | V_(2,0) | 14 | 10 = dim so(5) |
| 3 | V_(3,0) | 30 | 18 |
| 4 | V_(4,0) | 55 | 28 |
| 5 | V_(5,0) | 91 | 40 |

The bulk Casimir spacings are 4, 6, 8, 10, 12, ... (arithmetic +2). The dims also follow a clean polynomial pattern.

**Substrate-primary anchors on the bulk tower**:
- V_(0,0) Casimir 0 = vacuum/Higgs scalar.
- V_(1,0) dim 5 = n_C, Casimir 4 = rank² → photon (vector).
- V_(2,0) Casimir 10 = dim so(5) → next bulk excitation (potentially a higher gauge mode).

## 2. The spinor radial tower V_(1/2+k, 1/2) (lepton lane)

Leptons live on the Shilov boundary at lowest K-type V_(1/2, 1/2). The "radial" extension (generation tower candidate) is V_(1/2+k, 1/2) for k = 0, 1, 2, ...:

| k | K-type | Casimir |
|---|---|---|
| 0 | V_(1/2, 1/2) | 5/2 = ρ₁ (lepton) |
| 1 | V_(3/2, 1/2) | 15/2 |
| 2 | V_(5/2, 1/2) | 29/2 |
| 3 | V_(7/2, 1/2) | 47/2 |

Casimir spacings: 5, 7, 9, ... (arithmetic +2).

**Substrate-primary anchor**: V_(1/2, 1/2) Casimir 5/2 = ρ₁ = Bergman kernel singularity exponent — the "natural mass-setting" alignment (L4 v0.1). The HIGHER spinor K-types could carry the generations (e/μ/τ) — IF the mass mechanism is the radial tower.

## 3. THE CRITICAL FINDING — simple Casimir²-mass doesn't match observation

If mass² ∝ Casimir, the lepton mass ratios would be:

- m(k=1)/m(k=0) = √(15/2 / 5/2) = √3 ≈ **1.73**
- m(k=2)/m(k=1) = √(29/15) ≈ **1.39**

But observed:
- m_μ/m_e ≈ **206.77**
- m_τ/m_μ ≈ **16.82**

**Simple Casimir²-mass DOES NOT match observed lepton mass ratios** by 2 orders of magnitude. The radial tower's Casimirs grow too slowly to produce the SM lepton hierarchy.

## 4. The right mechanism: existing BST mass closed-forms

The existing BST mass derivations use DIFFERENT mechanisms, not naive Casimir squared:

| theorem | mass relation | precision | mechanism |
|---|---|---|---|
| T190 | m_μ / m_e = (24/π²)^6 ≈ 206.77 | 0.004% | closed form via 24 = rank³·N_c (rank-cube color product) and π² (radial kernel power); 6 = C_2 |
| T2003 | m_τ / m_e = 49·71 = 3479 | ~0.05% | BST primary product: 49 = g², 71 = some BST combination |
| T187 | m_p / m_e = 6·π⁵ = 1836.12 | 0.002% | adjoint Casimir × Bergman volume (boundary→bulk bridge) |

The leptonic radial tower's "spacing" is NOT a Casimir difference. It involves the Bergman kernel integral structure (Track BC's hydrogen 1s) and BST-primary closed forms like (24/π²)^6 — products and powers of substrate integers, not simple Casimir spectra.

## 5. What L4 v0.2 must do

L4 v0.2 (explicit per-particle lepton mass derivation, gated on Elie's bulk K-type radial tower per affine pin B₂⁽¹⁾) should:

1. **Connect the dictionary** (lepton at K-type V_(1/2,1/2)) to the **existing closed-forms** (T190, T2003). The dictionary places the lepton at Casimir 5/2 = ρ₁ (kernel exponent — "natural unit," L4 v0.1 alignment); the EXPLICIT mass ratios come from the radial Bergman kernel integral structure that gives (24/π²)^6 etc.
2. **Derive the closed forms from the K-type tower + kernel structure**: this is the multi-week work. Why does m_μ/m_e factor as (24/π²)^6? The 24 = rank³·N_c is a BST primary product; the π² is the radial kernel power; the 6 = C_2 is the Casimir exponent. A dictionary-level derivation would show all three emerge from the K-type structure + Bergman kernel.
3. **NOT just compute Casimir ratios** — those are off by orders of magnitude.

## 6. The honest scope (what v0.1 does NOT do)

- Does NOT derive lepton mass ratios from naive Casimir towers (explicitly shown not to work).
- Does NOT re-derive T190/T2003/T187 (existing BST results, anchors).
- DOES set up the K-type tower structure as the framework (bulk + spinor radial towers, Casimirs, dims, substrate-primary anchors).
- DOES IDENTIFY the right mechanism for L4 v0.2 (connect dictionary K-type to existing closed forms, not derive ratios from scratch via Casimirs).

This is a useful honest negative: it tells the team that Elie's bulk K-type radial tower computation, when ready, must aim at deriving the EXISTING closed forms (T190's (24/π²)^6, etc.) from the K-type structure + Bergman kernel — NOT at the naive Casimir²-mass approach.

## 7. Honest scope + tier

**RIGOROUS** (rep theory): Sym(5) decomposition under SO(5) into harmonic summands; V_(k,0) Weyl dims and Casimirs (computed, checked); spinor radial tower Casimirs (computed); arithmetic +2 spacing pattern.

**HONEST NEGATIVE**: simple Casimir²-mass tower DOES NOT match observed lepton mass ratios. By 2 orders of magnitude. L4 v0.2 cannot use this naive approach.

**FRAMEWORK GUIDANCE**: L4 v0.2 must connect the dictionary K-type placement (lepton at Casimir 5/2 = ρ₁ = kernel exponent) to the EXISTING BST mass closed-forms (T190, T2003, T187), via the Bergman kernel integral structure that gives those closed forms — NOT derive ratios from scratch via Casimir spectra.

**Cal #27 / honesty**: this v0.1 is a HONEST NEGATIVE plus FRAMEWORK guidance, not a derivation. I checked the naive mass-from-Casimir approach explicitly and it fails by orders of magnitude; reporting that clearly so Elie's L4 v0.2 work targets the right mechanism (kernel-integral closed forms, not Casimir spectra).

**Routed**: → Elie: when affine pin (B₂⁽¹⁾) ratifies and you start the bulk K-type radial tower, the TARGET is to derive T190's (24/π²)^6 and T2003's 49·71 from the kernel-integral structure on the spinor radial tower V_(1/2+k, 1/2) — NOT to use simple Casimir²-mass (which fails). The dictionary's role: place each generation's K-type and provide the kernel structure that yields the closed-form ratios. → Keeper: this honest-negative framework prevents L4 v0.2 from chasing a dead end (naive Casimir²-mass). → me: continuing to other items (bulk-color v0.3 / further study items / consolidation).

— Lyra, P4.3 holomorphic discrete series K-type framework v0.1. Bulk tower V_(k,0) (Casimirs 0, 4, 10, 18, …) and spinor radial tower V_(1/2+k, 1/2) (Casimirs 5/2, 15/2, 29/2, 47/2) computed cleanly. CRITICAL FINDING: simple Casimir²-mass ratios = 1.73 (k=1/k=0), 1.39 (k=2/k=1) — DO NOT MATCH observed m_μ/m_e ≈ 207 or m_τ/m_μ ≈ 17 by orders of magnitude. L4 v0.2 must connect dictionary K-type placement (lepton at C=5/2=ρ₁) to EXISTING BST mass closed forms (T190 (24/π²)^6, T2003 49·71, T187 6π⁵) via the kernel-integral structure — NOT naive Casimir spectra. Useful framework + honest negative; prevents L4 v0.2 from chasing a dead end.
