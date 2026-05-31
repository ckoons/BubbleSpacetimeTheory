---
title: "A2 L4 v0.2 — mass-ratios push with Elie's 3 bulk towers + Grace's intermediate-Casimir prediction. HONEST: naive Casimir-mass still fails (extending P4.3 finding); Grace's {0,4,6} channel prediction has TENSION with T190 exponent 6 (T190 uses C_2=6 as exponent for e→μ transition, which would be 'gen-3 channel' per Grace's mapping but is the gen-1→gen-2 ratio). Tower scaffold ready, but kernel-integral structure beyond Casimir^n is needed."
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-30 Saturday 10:38 EDT (date-verified)"
status: "L4 v0.2 PUSH (Lyra queue #6, Elie A2 Toy 3627 gate OPEN). Three bulk radial towers absorbed (vector, adjoint, spinor with closed-form Casimirs). Naive Casimir^n mass derivation STILL FAILS by 2 orders of magnitude (per P4.3). Grace's Pair α prediction {0,4,6} for spinor³ intermediate Casimirs is structurally clean but creates TENSION with T190 (exponent 6 = C_2 = 'gen-3 channel' per Grace, but T190 is gen-1→gen-2 ratio). Tower scaffold ready; explicit kernel-integral structure beyond Casimir spectrum is the remaining derivation work."
---

# A2 L4 v0.2 — mass ratios with bulk towers + intermediate-Casimir prediction

## 0. The gate opens

Elie Toy 3627 (A2 extended bulk radial towers) provided the THREE bulk K-type towers with closed-form Casimirs:

| Tower | Dynkin | Closed-form C_2 | First 4 values |
|---|---|---|---|
| **Vector** V_(k,0) | (k, 0) | k(k+3) | 0, 4, 10, 18 |
| **Adjoint** V_(k,k) | (0, 2k) | 2k(k+2) | 0, 6, 16, 30 |
| **Spinor** V_(k+1/2, k+1/2) | (0, 2k+1) | (k+1/2)(2k+5) | **5/2, 21/2, 45/2, 77/2** |

The spinor tower is the LEPTONIC matter channel (per dictionary lepton K-type V_(1/2, 1/2) at C = 5/2 = ρ₁).

## 1. The naive Casimir-mass test (still fails)

If mass² ∝ Casimir (the simplest possible mass mechanism):

  m_gen2/m_gen1 = √(21/5) ≈ **2.05** (observed m_μ/m_e ≈ **206.77**)
  m_gen3/m_gen2 = √(45/21) ≈ **1.46** (observed m_τ/m_μ ≈ **16.82**)

**Still fails by 2 orders of magnitude.** This is the same finding as P4.3 v0.1, now extended with the full bulk tower data. Naive Casimir^n mass derivation does NOT work for lepton mass ratios.

The existing BST closed forms (T190, T2003) DO match observed ratios precisely:
- T190: m_μ/m_e = (24/π²)^6 = (rank³·N_c/π²)^{C_2} ≈ 206.77 (0.004% precision)
- T2003: m_τ/m_e = 49·71 = g²·71 ≈ 3479 (~0.05%)
- T187: m_p/m_e = 6π⁵ = C_2·π^(n_C) ≈ 1836.12 (0.002%)

These closed forms use substrate primaries directly (rank³·N_c, g², C_2, etc.) — NOT simple Casimir spectra. The mass mechanism uses kernel-integral structure beyond bare Casimirs.

## 2. Grace's intermediate-Casimir prediction (Pair α from Two-Structures analysis)

Grace's 1.5 Two-Structures Mendeleev pair analysis identified:

> **Spinor³ contains spinor at multiplicity 3 via three E6 channels (spinor⊗{trivial, vector, adjoint}). Intermediate bosonic Casimirs are {0, 4, 6} = {0, rank², C_2} — arithmetic sequence in BST primaries.**
> 
> Prediction: Gen 1 ↔ trivial-channel (C_int = 0); Gen 2 ↔ vector-channel (C_int = 4); Gen 3 ↔ adjoint-channel (C_int = 6).

If correct, the mass hierarchy should correlate with intermediate Casimirs {0, 4, 6}.

## 3. TENSION between Grace's prediction and T190

T190 says m_μ/m_e = (24/π²)^{**C_2 = 6**} — the EXPONENT is C_2 = 6.

Per Grace's mapping:
- Exponent 6 = C_2 = "adjoint-channel intermediate Casimir" = "gen-3 channel."
- But T190 is the e → μ ratio (gen-1 → gen-2).
- If the gen-1 → gen-2 transition uses EXPONENT 6 = "gen-3 channel Casimir," there's a structural mismatch with Grace's prediction (gen-2 should be vector-channel = 4, not adjoint-channel = 6).

**Tension**: T190 exponent 6 ≠ Grace gen-2 = vector-channel 4.

Possible reconciliations:
1. T190's exponent 6 is NOT the gen-2 intermediate Casimir; it's the C_2 of the underlying GAUGE STRUCTURE mediating the e → μ transition (the adjoint Casimir of so(5) governing the weak interaction). In that case T190's 6 is a gauge-sector factor, independent of Grace's spinor³ channel assignment.
2. Grace's mapping (Gen 2 = vector-channel, Gen 3 = adjoint-channel) might be reversed — Gen 2 could actually be the ADJOINT-channel if mass corresponds to MORE excitation rather than less. Testing: m_μ ≫ m_e suggests gen-2 has MORE excitation; adjoint (C=6) is more excited than vector (C=4). So Gen 2 = adjoint-channel might be the right mapping.
3. The intermediate-Casimir prediction is not directly the mass mechanism; it's a STRUCTURAL LABEL of the channels, not a quantitative mass formula.

The TENSION is real and useful: it sharpens what Grace's prediction means + what T190 is structurally saying. Neither is wrong; the relation between them is subtle.

## 4. The deeper read of T190 (suggestive)

  **T190: m_μ/m_e = (rank³ · N_c / π²)^{C_2}**

Structural interpretation:
- **rank³ · N_c = 24** = the dimension of some natural substrate-derived object (rank³ = 8 = dim of some sub-rep? × N_c = 3 colors? or rank³·N_c = 8·3 = 24 = dim octonions/maximally-symmetric structure?).
- **π² in denominator** = radial kernel integral factor (BST Bergman kernel involves π powers).
- **Exponent C_2 = 6** = the adjoint Casimir of B_2, suggesting the e → μ transition mediated by the adjoint (gauge) sector.

So T190's structural reading: lepton mass ratios come from the (substrate-primary)^{adjoint-Casimir} closed form, with the (24/π²) base being a substrate-natural ratio and the exponent being the gauge-sector Casimir.

This is the kind of closed form that L4 v0.2 derivation aims to obtain explicitly from the kernel-integral structure on the radial tower — but it's NOT a simple Casimir^n formula.

## 5. v0.2 deliverable + remaining work

**Delivered (v0.2)**:
- Three bulk radial towers absorbed (Elie Toy 3627).
- Naive Casimir-mass test re-confirmed to fail.
- Grace's intermediate-Casimir prediction absorbed; TENSION with T190 exponent identified.
- Deeper structural read of T190 = (rank³·N_c/π²)^{C_2} (substrate primaries + adjoint exponent).

**Remaining (multi-week)**:
- Explicit kernel-integral computation on the spinor radial tower V_(k+1/2, k+1/2) — derive the (24/π²)^{C_2} closed form from substrate kernel structure.
- Reconcile Grace's intermediate-Casimir prediction with T190's exponent (adjoint = 6 vs vector = 4).
- Extend to T2003 (m_τ/m_e = 49·71); identify the 71 substrate-natural origin.
- Quark masses (require bulk-color mechanism — separate gate).
- Higgs / W / Z absolute masses (L5 absolute scale — separate gate).

## 6. Honest scope + tier

**RIGOROUS** (Elie + standard rep theory):
- Three bulk radial towers' closed-form Casimirs (Elie Toy 3627, verified).
- Naive Casimir-mass test fails by 2 orders of magnitude (extends P4.3).

**STRUCTURAL** (this v0.2):
- T190 = (rank³·N_c/π²)^{C_2} substrate-primary closed form (existing, anchor).
- Tension between Grace's intermediate-Casimir prediction and T190 exponent identified.

**OPEN (multi-week)**:
- Explicit kernel-integral derivation of T190 closed form from spinor radial tower.
- Grace prediction vs T190 reconciliation.
- T2003's 71 substrate-natural identification.

**Cal #27 / honesty**: v0.2 honestly extends the naive Casimir-mass failure (P4.3 finding intact) and identifies a real TENSION between Grace's intermediate-Casimir prediction and T190's exponent. The deeper structural read of T190 = substrate-primary closed form is the right direction; explicit derivation is multi-week. NOT a closed lepton mass derivation.

**Routed**: → Elie: kernel-integral computation on spinor radial tower would derive T190 closed form from substrate kernel structure (multi-week). → Grace: T190 exponent 6 = C_2 might suggest gen-2 = ADJOINT-channel (not vector-channel) — possible reordering of your Pair α mapping. → Keeper: L4 v0.2 finds real TENSION (Grace prediction vs T190) that's structurally productive — sharpens what each piece is saying. → me: continuing to Lyra Queue #7 = B8 cross-domain bounded-symmetric-domain uniqueness.

— Lyra, A2 L4 v0.2 mass-ratios push. Three bulk radial towers absorbed (Elie 3627); naive Casimir-mass STILL fails (P4.3 extended). Grace's intermediate-Casimir prediction {0,4,6} has TENSION with T190 exponent 6 = C_2 (adjoint, gen-3 channel per Grace, but T190 is gen-1→gen-2 ratio). Deeper structural read: T190 = (rank³·N_c/π²)^{C_2} = substrate-primary closed form; explicit kernel-integral derivation from spinor radial tower is multi-week. Tension productive — sharpens both pieces.
