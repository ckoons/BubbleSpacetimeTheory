---
title: "B8 — cross-domain bounded-symmetric-domain uniqueness v0.1: explicit per-domain check showing D_IV⁵ is the UNIQUE irreducible bounded symmetric domain satisfying (rank=2, complex dim=5, spatial-compact-factor h^∨=3). All other classical + exceptional types excluded with specific reasons. Strong-Uniqueness Theorem v1.2 anchor."
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-30 Saturday 10:38 EDT (date-verified)"
status: "B8 v0.1 (Lyra queue #7). Explicit per-domain comparison check anchoring the Strong-Uniqueness theorem's domain-selection criterion. D_IV⁵ uniquely satisfies rank=2 AND complex dim=5 AND spatial-compact-factor h^∨=3."
---

# B8 — Cross-domain bounded-symmetric-domain uniqueness v0.1

## 0. The question

Why D_IV⁵ specifically? BST has Strong-Uniqueness Theorem v1.2 (13 operational criteria + META T2467) selecting D_IV⁵ uniquely. B8 v0.1 gives the explicit per-domain comparison check against ALL irreducible bounded symmetric domains.

## 1. Cartan classification

The irreducible bounded symmetric domains (Cartan 1935):

| Type | Group G | K (max compact) | Rank | Complex dim |
|---|---|---|---|---|
| I_(p,q) | SU(p,q) | U(p)×U(q) | min(p,q) | p·q |
| II_n | SO*(2n) | U(n) | ⌊n/2⌋ | n(n−1)/2 |
| III_n | Sp(n,R) | U(n) | n | n(n+1)/2 |
| **IV_n** | **SO(2,n)** | **SO(n)×SO(2)** | **2** | **n** |
| V | E_6(−14) | Spin(10)×SO(2) | 2 | 16 |
| VI | E_7(−25) | E_6×SO(2) | 3 | 27 |

## 2. Substrate-specific constraints (selection criteria)

The substrate is forced by:
- **rank = 2** (forced by Coxeter h−1 = 3 generations + h^∨ = N_c = 3 colors fitting only at B_2 = SO(5)).
- **complex dim = 5** (= n_C, the substrate's complex spatial dim).
- **spatial-compact-factor's h^∨ = 3** (= N_c, the dual Coxeter / color count).
- **signature p+q = 7** (= g, the substrate's embedding/signature dim).

## 3. Per-domain exclusion check

| Type | Rank=2? | Complex dim=5? | Spatial-compact h^∨=3? | Verdict |
|---|---|---|---|---|
| I_(2,q) | only if min(2,q)=2 → all q≥2 | p·q = 2q = 5 → q=2.5, IMPOSSIBLE | — | **EXCLUDED** (no integer (p,q)) |
| II_4 | ⌊4/2⌋=2 ✓ | 6 ≠ 5 | — | **EXCLUDED** |
| II_5 | ⌊5/2⌋=2 ✓ | 10 ≠ 5 | — | **EXCLUDED** |
| III_2 | 2 ✓ | 3 ≠ 5 | — | **EXCLUDED** |
| IV_4 | 2 ✓ | 4 ≠ 5 | SO(4) not simple — h^∨ ambiguous | **EXCLUDED** by dim |
| IV_5 | 2 ✓ | **5 ✓** | h^∨(SO(5)) = **3 ✓** | **SUBSTRATE** |
| IV_6 | 2 ✓ | 6 ≠ 5 | h^∨(SO(6))=4 ≠ 3 | **EXCLUDED** |
| IV_n (n>6) | 2 ✓ | n ≠ 5 | h^∨ grows | **EXCLUDED** by both dim and h^∨ |
| V | 2 ✓ | 16 ≠ 5 | h^∨(Spin(10))=8 ≠ 3 | **EXCLUDED** by dim and h^∨ |
| VI | **3 ≠ 2** | 27 | h^∨(E_6)=12 | **EXCLUDED** by rank |

## 4. Conclusion

**D_IV⁵ is the UNIQUE irreducible bounded symmetric domain satisfying (rank=2, complex dim=5, spatial-compact-factor h^∨=3).**

The signature constraint (g = p+q = 2+5 = 7) is automatically satisfied by Type IV_5.

This is the operational form of the Strong-Uniqueness Theorem's domain-selection criterion: given the three substrate primary anchors (rank, n_C, N_c), D_IV⁵ is forced uniquely.

## 5. Honest scope + tier

**RIGOROUS** (Cartan classification + Lie-algebra dual Coxeter numbers):
- Cartan classification of irreducible bounded symmetric domains (complete).
- h^∨ values for SO(n), Sp(n), etc. (standard).
- The per-domain comparison check (computed).

**DERIVED (this v0.1)**: D_IV⁵ is uniquely selected by (rank=2, complex dim=5, spatial h^∨=3) — anchors the Strong-Uniqueness criteria for domain selection.

**Note**: this v0.1 doesn't argue WHY the substrate criteria are (rank=2, n_C=5, N_c=3) — those are the substrate primaries themselves (other criteria in Strong-Uniqueness v1.2 derive them). B8 anchors the DOMAIN selection given the primary constraints.

**Cal #27 / honesty**: this is a clean per-domain check, not a new derivation. It confirms what Strong-Uniqueness v1.2 already encodes: D_IV⁵ is uniquely forced by the three substrate primary anchors (rank, n_C, N_c). The criteria themselves are derived elsewhere (Strong-Uniqueness v1.2 C1-C13).

**Routed**: → Keeper: B8 v0.1 confirms the Strong-Uniqueness theorem's domain selection via explicit per-domain check. → Grace: catalog entry candidate — D_IV⁵ uniqueness sheet. → me: continuing to Lyra Queue #8 = B2 Macdonald-Koornwinder other corners.

— Lyra, B8 cross-domain uniqueness v0.1. Cartan classification of bounded symmetric domains: 4 classical (I/II/III/IV) + 2 exceptional (V/VI). Per-domain check against (rank=2, complex dim=5, spatial h^∨=3): I_(p,q) excluded (no integer fit); II_n excluded (wrong dim); III_n excluded (wrong dim); IV_n for n≠5 excluded (dim or h^∨); V excluded (dim and h^∨); VI excluded (rank). **D_IV⁵ is the UNIQUE irreducible bounded symmetric domain** satisfying the three substrate primary anchors. Strong-Uniqueness Theorem v1.2 domain-selection criterion explicitly confirmed.
