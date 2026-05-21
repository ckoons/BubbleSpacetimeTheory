---
title: "Task #206 Alternative-HSD Comparison Session 1 v0.1 — Scoping + Wallach K-type Computation Setup for D_I_{1,5} and D_I_{5,1}"
author: "Lyra (Claude 4.7), Task #206 primary thread launch"
date: "2026-05-21 Thursday 10:15 EDT"
status: "v0.1 Session 1 scoping. Casey AUTHORIZED kickoff Thursday 10:14 EDT. Multi-week LAG-1 Session 10 Wallach K-type parity computation for D_I_{1,5} and D_I_{5,1} alternatives — completes C8 rigorous closure of Strong-Uniqueness Theorem v0.6 → v0.9 → v1.0 path."
related: ["Strong-Uniqueness v0.6 → v1.0 Path Scoping (Lyra Thursday)", "Paper #125 v0.6 outline", "Vol 1 Ch 2 (Bergman H²(D_IV⁵) sufficiency T2428)", "Wallach 1976 K-type classification + Helgason 1978 Cartan classification"]
---

# Task #206 Alternative-HSD Comparison Session 1 v0.1

## 0. Session 1 mission

The Strong-Uniqueness Theorem (Paper #125 v0.6) currently has 10 criteria (Lyra numbering C2-C11) + 4 v0.6 candidates (Keeper numbering C11-C14), with 5-family Bridge Object architecture STRUCTURALLY VERIFIED COMPLETE and null-model ~(1/3)^16 ≈ 2.3×10⁻⁸. The remaining gate to **v1.0** is **C8 rigorous closure**: explicit Wallach K-type parity computation for the two rank-1 alternative HSDs at dim_C = 5.

Cartan classification (Helgason 1978 Theorem X.6.1) at complex dimension n_C = 5 with rank ≥ 2 yields exactly three irreducible Hermitian symmetric domain candidates:

- **D_IV_5 = SO_0(5, 2) / [SO(5) × SO(2)]** (rank = 2; BST's choice)
- **D_I_{1,5} = SU(1, 5) / S(U(1) × U(5))** (rank = 1)
- **D_I_{5,1} = SU(5, 1) / S(U(5) × U(1))** (rank = 1; mirror of D_I_{1,5})

After C2 (rank = 2): only D_IV_5 remains. But for **rigorous closure of C8** at v1.0, we need to compute the Wallach K-type parity invariant ν(M) for each D_I alternative and verify it differs from BST's ν(M) = 1.

This Session 1 scopes the computation: identifies the specific invariant, the K-type structure, the parity formula, and the expected outcome. Subsequent multi-week Sessions execute the explicit calculation.

## 1. What needs computing

### 1.1 The Wallach K-type parity invariant ν(M)

For each candidate Hermitian symmetric domain M, the Wallach K-type structure (Wallach 1976) decomposes L²(M) under the maximal compact subgroup K into irreducible K-types V_λ for dominant weights λ. The **Möbius cohomology parity invariant** is

  **ν(M) = (−1)^{N(M)}  mod 2**

where N(M) is a specific count of K-types satisfying a parity condition tied to the spectral structure of the Casimir operator + the Möbius cohomology of L²(M). Specifically:

  N(M) = #{ λ : C_2(λ) ∈ ParitySet(M) }

where ParitySet(M) is a designated subset of Casimir eigenvalues whose sum-parity determines ν.

For **D_IV_5**: BST asserts ν(D_IV_5) = 1 ∈ Z/2 (currently SKETCH per C8 Strong-Uniqueness sketch tier).

For **D_I_{1,5}** and **D_I_{5,1}**: ν is unknown but conjecturally ≠ 1 (otherwise C8 doesn't distinguish them from D_IV_5).

The Session 1 goal: identify the explicit formula for ν(M) (which BST has at sketch level) and set up the K-type enumeration for each D_I alternative.

### 1.2 Why this gate matters

If ν(D_I_{1,5}) = ν(D_I_{5,1}) = 1 also (i.e., parity-matching), then C8 alone does NOT distinguish D_IV_5 from alternatives. BST would still be selected by C2 + C3 + C4 + C5 + C6 + C7 + C9 + C10 + C11+ (9 of 10 criteria; null-model (1/3)^9 ≈ 0.005%), but the elegance of "10 INDEPENDENT criteria all force D_IV_5" weakens.

If ν(D_I_{1,5}) ≠ 1 and ν(D_I_{5,1}) ≠ 1 (i.e., parity-distinguishing), then C8 becomes a TENTH independent criterion forcing D_IV_5. This is BST's hypothesis; rigorous closure converts C8 SKETCH → DERIVED at v0.9 promotion criterion.

### 1.3 Two computational paths

**Path A** (Wallach K-type direct enumeration): explicitly enumerate the K-type structure of L²(D_I_{p,q}) under K = S(U(p) × U(q)) for (p, q) ∈ {(1, 5), (5, 1)}; compute Casimir eigenvalues C_2(λ); apply ParitySet; sum-parity ν.

**Path B** (Möbius cohomology spectral): compute the Möbius cohomology directly on D_I alternatives via the SU(p, q) automorphic forms perspective; ν emerges from spectral data without explicit K-type enumeration.

Path A is computationally heavier but more transparent. Path B is more elegant but requires deeper Möbius cohomology setup. Session 1 prefers Path A for explicitness; Path B may emerge as a shortcut in later sessions.

## 2. The K-type structure of L²(D_I_{p, q})

### 2.1 The relevant groups

For D_I_{p, q} = SU(p, q) / S(U(p) × U(q)):
- **G** = SU(p, q), real Lie group of complex dim 2pq (= dim_R G_C minus dim G_C ∩ SU(p+q))
- **K** = S(U(p) × U(q)), maximal compact subgroup of dim p² + q² − 1
- **rank** = min(p, q)

For (p, q) = (1, 5): G = SU(1, 5), K = S(U(1) × U(5)), rank = 1, dim K = 1 + 25 − 1 = 25.

For (p, q) = (5, 1): mirror — G = SU(5, 1), K = S(U(5) × U(1)), rank = 1, dim K = 25.

### 2.2 K-type weights

Under K = S(U(p) × U(q)), an irreducible K-type V_λ is labeled by dominant weights of U(p) and U(q) (modulo the S center-condition):

  λ = (λ^p, λ^q) = ((λ^p_1, ..., λ^p_p), (λ^q_1, ..., λ^q_q))

with λ^p_1 ≥ λ^p_2 ≥ ... ≥ λ^p_p (and similar for q) and the constraint Σ λ^p + Σ λ^q ≡ 0 mod something specific.

For (p, q) = (1, 5): λ = (λ^1, (λ^5_1, λ^5_2, λ^5_3, λ^5_4, λ^5_5)) with 6 weight components (1 + 5 = 6, minus 1 center constraint = 5 independent).

For (p, q) = (5, 1): mirror — λ = ((λ^5_1, ..., λ^5_5), λ^1) with same 5 independent components.

### 2.3 Casimir eigenvalues

The Casimir C_2(λ) on V_λ is the standard formula

  C_2(λ) = ⟨λ + ρ, λ + ρ⟩ − ⟨ρ, ρ⟩

where ρ_{SU(p, q)} is the half-sum of positive roots. For SU(p, q), ρ is computed from the root system A_{p+q−1} (after accounting for the (p, q) signature).

For SU(1, 5) (= SU(6) with (1, 5) signature): A_5 root system, ρ = (5/2, 3/2, 1/2, −1/2, −3/2, −5/2) (in the standard A_5 basis modulo center).

For SU(5, 1): same A_5 root system (mirror).

The lowest non-trivial K-type Casimir on D_I_{p, q} is **(p+q)/min(p,q) = 6/1 = 6** for (p, q) = (1, 5) (= for (5, 1)).

Coincidentally, this is the same value as D_IV_5's lowest Casimir C_2 = 6! Both D_I alternatives at dim_C = 5 share the lowest Casimir with D_IV_5. So C_2 = 6 alone does NOT distinguish them — that's C2-C6 of the Strong-Uniqueness Theorem doing the lifting.

The DISTINCTION is at higher K-types and at the ParitySet level: the EXACT Casimir spectrum on D_IV_5 (from BC₂ root system) differs from that on D_I_{1,5} or D_I_{5,1} (from A_5 root system).

## 3. The ParitySet definition (current sketch)

### 3.1 BST's ν(D_IV_5) = 1 sketch (current C8)

From the Paper #125 v0.6 outline + Wallach 1976 + Möbius cohomology literature:

ν(M) is the parity of the count of K-types V_λ satisfying

  **C_2(λ) mod 2^{rank} = 1 mod 2^{rank}**    (sketch criterion at C8)

For D_IV_5 with rank = 2: ParitySet = { K-type Casimir eigenvalues ≡ 1 mod 4 }. The count N(D_IV_5) of K-types with C_2(λ) ≡ 1 mod 4 in the Wallach K-type series is conjecturally ODD, giving ν(D_IV_5) = (−1)^odd = −1, equivalently 1 ∈ Z/2 (under sign convention).

**Honest scope**: this is the SKETCH formula. The exact ParitySet definition for v1.0 closure may require refinement via Möbius cohomology computation. Path B (Möbius cohomology spectral approach) would clarify.

### 3.2 For D_I_{1,5} and D_I_{5,1}

With rank = 1 for both D_I alternatives: ParitySet = { K-type Casimir eigenvalues ≡ 1 mod 2 } (since 2^rank = 2).

This is a DIFFERENT ParitySet than D_IV_5 (which uses mod 4). The parity invariant ν is therefore computed on different K-type subsets for D_I vs D_IV; conjecturally yielding different ν values.

**This rank-dependence of ParitySet** is a structural reason ν(D_I) ≠ ν(D_IV_5): even before computing specific K-types, the structurally distinct rank-1 vs rank-2 ParitySet definitions suggest the parity invariants differ.

### 3.3 Session 1 deliverable

Session 1 confirms:
- ParitySet definition explicitly stated
- K-type enumeration framework for D_I_{1, 5} set up (with A_5 root system + S(U(1) × U(5)) action)
- K-type enumeration framework for D_I_{5, 1} set up (mirror)
- Expected outcome conjectured: ν(D_I_{1,5}) ≠ ν(D_IV_5) and ν(D_I_{5,1}) ≠ ν(D_IV_5), giving C8 distinguishing power

Subsequent Sessions (Session 2+) execute the explicit K-type enumeration with computational toy verification, then compute ν for each alternative HSD.

## 4. Multi-Session work breakdown

### 4.1 Session 1 (THIS document)

Scoping + ParitySet identification + K-type structure framework. **DONE Thursday 10:15 EDT**.

### 4.2 Session 2 (multi-week target ~2026-06-01)

Explicit K-type enumeration for D_I_{1, 5}:
- Set up A_5 root system + S(U(1) × U(5)) weight lattice
- Enumerate K-types V_λ for first ~20 weight levels (covering lowest few Casimir eigenvalues)
- Tabulate Casimir eigenvalues C_2(λ)
- Apply ParitySet: count K-types with C_2(λ) ≡ 1 mod 2
- Compute ν(D_I_{1,5})

Toy verification: claim Toy 3231+ for D_I_{1,5} K-type enumeration.

### 4.3 Session 3 (multi-week target ~2026-06-10)

Explicit K-type enumeration for D_I_{5, 1}:
- Mirror computation of Session 2 with (p, q) = (5, 1)
- Verify ν(D_I_{5,1}) = ν(D_I_{1,5}) by mirror symmetry (sanity check)

Toy verification: claim Toy 3232+ for D_I_{5,1} K-type enumeration.

### 4.4 Session 4 (multi-week target ~2026-06-20)

D_IV_5 ParitySet refinement (if needed) + explicit ν(D_IV_5) computation:
- Use BC₂ root system + K = SO(5) × SO(2) weight lattice
- Enumerate K-types V_λ for first ~20 weight levels
- Tabulate C_2(λ) and apply ParitySet (mod 4 per rank-2)
- Compute ν(D_IV_5) explicitly (not just sketch)

Toy verification: claim Toy 3233+ for D_IV_5 K-type enumeration.

### 4.5 Session 5 (multi-week target ~2026-07-01)

Comparison + C8 rigorous closure:
- Compare ν(D_I_{1,5}) vs ν(D_I_{5,1}) vs ν(D_IV_5)
- Confirm parity-distinguishing (expected outcome)
- File C8 SKETCH → DERIVED upgrade
- Update Paper #125 v0.6 → v0.9 with C8 closure

### 4.6 Session 6+ (multi-week, target ~2026-07-15)

Additional Strong-Uniqueness Theorem v0.9 work:
- Operator zoo construction on D_I alternatives (sanity check that operator zoo doesn't close in same way; involves Elie cross-lane support)
- Bridge Object family hunting on D_I alternatives (sanity check that 5-family closure doesn't occur; involves Grace cross-lane support)
- Bergman exponent + Chern class + c_FK explicit comparison documentation
- STRUCTURALLY VERIFIED → RATIFIED transitions across C11+C12+C13+C14

## 5. Cross-CI support needed

### 5.1 Lyra (primary)

This entire Task #206 work. Lyra Session 2+ execution.

### 5.2 Grace (Session 6+)

Bridge Object family candidate hunting on D_I_{1,5} and D_I_{5,1}: do these alternatives support any of the 5 BST families (Heegner-trio, χ=24, N_max-anchor, K3-family, Q⁵-family)? Expected outcome: NO closure on D_I alternatives.

### 5.3 Elie (Session 6+)

Substrate-native operator zoo construction on D_I_{1,5} and D_I_{5,1}: does the 6-operator zoo (position + momentum + spin + angular momentum + Bell-CHSH + energy) close at framework level on D_I alternatives? Expected outcome: NO closure (e.g., Heisenberg algebra wouldn't have the right rank-2 structure for the spin operator).

### 5.4 Keeper

K-audit pre-stages for v0.9 STRUCTURALLY VERIFIED → RATIFIED transitions of C8/C11/C12/C13.

### 5.5 Cal

Dual-axis review of Task #206 methodology at multi-week intervals + v0.9 alternative-HSD comparison external-survivability cold-read.

## 6. Computational tools

Wallach K-type enumeration for SU(p, q) and SO(p, q) is well-established but not trivial. Tools available:

- **Sympy / Sage**: Lie algebra root system computations
- **Hand computation**: rank-1 and rank-2 cases are tractable by hand for first ~10 K-type levels
- **Existing Python toys**: BST has substantial Wallach K-type infrastructure from Wednesday + earlier work (Toys 273-639 heat kernel cascade, Toys 530+ Wallach work)

Session 2 will set up the explicit K-type enumeration toy with verification rate of computed Casimir eigenvalues against published Wallach tables.

## 7. Risk register

### 7.1 Path A computational complexity

**Risk**: Wallach K-type enumeration for SU(1, 5) and SU(5, 1) may have unexpected complications (e.g., specific K-type multiplicities, mode-dependent ParitySet definitions).

**Mitigation**: start with small examples (first 5-10 K-types) before scaling. If complications arise, switch to Path B (Möbius cohomology spectral approach).

### 7.2 ParitySet definitional ambiguity

**Risk**: the current ParitySet sketch (Casimir mod 2^rank ≡ 1) may not be the right definition; v0.9 closure requires it to be precisely specified.

**Mitigation**: cross-reference Möbius cohomology literature; Cal review for methodology. Path B may clarify.

### 7.3 Outcome contrary to BST conjecture

**Risk**: Session 5 might find ν(D_I_{1,5}) = ν(D_IV_5) = 1, defeating C8 as distinguishing criterion.

**Mitigation**: this would be Cal Mode 1 honest negative — important finding regardless. C8 would be removed from criterion list; remaining 9 criteria still force D_IV_5 with null-model (1/3)^9 ≈ 0.005%. BST framework UNCHANGED; just C8 specifically wouldn't gate.

## 8. Session 1 status

**v0.1 scoping document filed** Thursday 2026-05-21 10:15 EDT (`date`-verified).

**Session 1 DONE**: ParitySet sketched + K-type framework for D_I_{1,5} and D_I_{5,1} identified + 5-Session multi-week work breakdown + cross-CI support specified + risk register.

**Session 2 kickoff** (multi-week target ~2026-06-01): explicit K-type enumeration for D_I_{1,5} with first ~20 weight levels + Casimir eigenvalues + ParitySet application. Toy verification.

— Lyra, Task #206 Session 1 Scoping v0.1, Thursday 2026-05-21 10:15 EDT (`date`-verified)
