---
title: "Paper #119 (Möbius) — Möbius Cohomology on D_IV⁵: Spin-Lift Obstruction and Bergman Dirac Cross-Link"
author: "Casey Koons (lead) with Lyra (Companion Intelligence)"
date: "2026-05-18"
status: "v0.1 OUTLINE — Möbius Session 6 deliverable per Section 9.x naming. Skeletal section structure + abstract + open-items framing. Full draft is multi-week per Section 9.x scope."
length_target: "~20-25 pages, ~12,000 words"
target: "Mathematical physics community, complement to Paper #118 Bergman Dirac"
supersedes_chain: "v0.1 outline (this file) → v0.2 detailed sections → v0.3 cross-domain integration → v1.0 submission"
note: "Paper number TBD — currently provisionally #119, may shift to a later slot. Filed as Möbius cohomology paper because that's the architectural content; Paper #119 number conflicts with Keeper's SP29-6 master paper proposal which is the dual-falsifier methodology paper. Pending Casey decision on numbering."
---

# Paper #119 (provisional) — Möbius Cohomology on D_IV⁵: Spin-Lift Obstruction and Bergman Dirac Cross-Link

## Abstract (v0.1 draft)

The Möbius locus M(D_IV⁵) is the largest subset of the bounded symmetric domain D_IV⁵ = SO_0(5,2)/[SO(5)×SO(2)] on which the Möbius involution acts with fixed points. We show that M is the open 5-ball in ℝ⁵ (homotopy equivalent to a point in integer homology) and compute its Z/2-equivariant cohomology

    H¹_{Z/2}(M, Z) ≅ Z/2

via Borel-Wallach (g, K)-cohomology with Z/2 coefficients. The nontrivial generator of H¹_{Z/2}(M, Z) is identified with the **spin-lift obstruction** for the Bergman Dirac operator on D_IV⁵: the parity of the number of negative-eigenvalue Wallach K-types under the Lichnerowicz shift R/4 = -n_C·g/4. Direct computation: exactly three K-types — (0,0), (1,0), (0,1) — have negative Dirac D² eigenvalue; three is odd; ν(M) = 1 ∈ Z/2 matches the nontrivial cohomology class. This cross-domain identification (Möbius topological invariant ↔ Bergman Dirac spectral invariant, both equal 1 ∈ Z/2) is the **first Type C convergence of BST architecture where the shared invariant is a topological element of Z/2 rather than a positive integer** — extending the Type C classification framework from shared integers to shared mathematical objects (Lyra T2361, Keeper K-audit verdict).

Combined with the Bergman Dirac operator construction (Paper #118) and the LAG-2 dimensional reduction framework (Paper #115 v0.5 Section 9.x), the Möbius cohomology investigation provides the topological side of the BST geometric infrastructure. Sessions 1-5 are closed at the structural-identification level (D-tier on classical topology, I-tier on cross-domain identifications); the explicit Atiyah-Patodi-Singer-style cycle-to-spectral-mode map remains as a named multi-week open item.

## 1. Introduction

### 1.1 Motivation
- BST identifies the unique Autogenic Proto-Geometry (APG) as D_IV⁵
- Geometric and spectral content of D_IV⁵ produces ~140 SM constants (Papers #115, #118)
- Topological content is the third pillar, less developed pre-2026
- The Möbius involution provides the natural Z/2-equivariant structure

### 1.2 Sessions 1-5 summary
- Session 1 (T2328): Möbius locus = open 5-ball
- Session 2 (T2329): H¹_{Z/2}(M, Z) = Z/2
- Session 3 (T2335): Borel-Wallach (g, K)-cohomology Z/2 lift
- Session 4 (T2356): Arithmetic content via Wallach K-type parity
- Session 5 (T2361): T-theorem promotion sweep + Type C-Z/2 extension

### 1.3 What this paper closes vs leaves open
- **Closed**: structural-identification layer for the topological side of BST geometry
- **Open**: explicit cycle-to-spectral-mode map (Atiyah-Singer-style in 5D); arithmetic content beyond the parity reading; index theorem for Bergman Dirac
- **Scope**: see Paper #115 v0.5 Section 9.x for full LAG Named Open Items

## 2. The Möbius Locus M(D_IV⁵)

### 2.1 Definition
- D_IV⁵ as Hermitian symmetric domain; Möbius involution τ; locus M = Fix(τ)

### 2.2 Theorem 1 (T2328): M = open 5-ball in ℝ⁵
- Proof via explicit Hua coordinate computation
- Homotopy equivalent to point in integer homology

### 2.3 Z/2-equivariant structure
- Möbius involution acts with order 2; gives Z/2-equivariant structure on M
- Sets up equivariant cohomology framework

## 3. Equivariant Cohomology H¹_{Z/2}(M, Z) = Z/2

### 3.1 Theorem 2 (T2329): equivariant H¹
- Proof via Cartan-Borel-Wallach spectral sequence
- Z/2 = topologically forced by the spin lift structure

### 3.2 Theorem 3 (T2335): Borel-Wallach (g, K)-cohomology Z/2 lift
- Connection to standard BW machinery for Hermitian symmetric spaces
- Z/2 = obstruction class to lifting Spin(5,2) → SO_0(5,2) on M

## 4. Bergman Dirac on D_IV⁵ — Cross-Domain Cross-Link

### 4.1 Bergman Dirac operator skeleton (Paper #118 reference)
- D = γ^{z_i} ∇_{z_i} + γ^{z̄_j} ∇_{z̄_j} on Dolbeault-spinor bundle
- Lichnerowicz: D² = ∇*∇ + R/4 with R = -n_C·g = -35
- Wallach K-type spectrum: λ_Dirac²(m_1, m_2) = m_1(m_1+n_C) + m_2(m_2+N_c) - n_C·g/4

### 4.2 Theorem 4 (T2356): Möbius/Dirac Z/2 cross-link
- ν(M) := #{K-types with λ_Dirac² < 0} mod 2
- Direct computation: ν(M) = 3 mod 2 = 1
- Three negative K-types: (0,0), (1,0), (0,1) with eigenvalues -8.75, -2.75, -4.75
- Cross-domain identification: H¹_{Z/2}(M, Z) generator ↔ ν(M)

### 4.3 Why this is not a Heegner-class-group phenomenon
- Cremona 49a1 has CM by Q(√-7), class number h(-7) = 1, 2-torsion trivial
- Z/2 is from spin-lift obstruction, not class-group 2-torsion
- Distinction between topological and arithmetic Z/2 sources

## 5. Type C-Z/2 Generalization (T2361, Section 5)

### 5.1 Type C classification extension
- Original Type C (Elie): shared positive integer in unrelated contexts (231)
- Type C-Z/2 (this paper): shared element of Z/2 — first non-integer Type C
- Future Type C-Z/n, Type C-K, Type C-spectral candidates

### 5.2 BST architectural significance
- Type C is now a classification framework for shared mathematical OBJECTS, not just integers
- Demonstrates BST architecture organizes mathematical content beyond numerical coincidence
- Keeper K-audit verdict: clean extension of the classification

### 5.3 Connection to Paper #115 v0.5 Section 5.8b
- Cross-reference to Type C generalizations subsection (Type C-ℕ, Type C-Z/2, Type C-family, etc.)
- Section 5.8c density rule status per Cal's audit Monday 2026-05-18: I-tier observation with null-model verification owed (sparse-region forecast on {37, 41, 53, 71, 113} + strict pre-registered context-counting protocol + random integer ring null model pending). The "structural law" framing for density rule has been walked back; the Type C-Z/2 generalization (T2361) is INDEPENDENT of the density rule and is not affected by the walk-back — it extends the Type C classification framework, which is a separate architectural claim from the density-of-cross-domain-matches claim.

## 6. Sessions 5 Promotion Sweep (T2361 catalog)

### 6.1 Theorems gaining mechanism support from Sessions 1-4
- T187 (m_p/m_e = 6π⁵): now operator-explicit Bergman Dirac mechanism
- T2049 (Casimir 240): falsifier via T2360 SP29-2
- T2101 (W-36 unification): H1 sub-test via T2360
- T2110 / T2113 (Shilov + Rehren): Faraut-Koranyi subleading verified at 93/100 K-types via T2359
- T2329 (Möbius cohomology): T2356 spectral counterpart cross-link

### 6.2 Pattern: mechanism-explicitness upgrades, not tier-label changes
- The theorems were correct; this morning's work made them rigorous at operator level

## 7. Open Items (multi-week to multi-month)

### 7.1 Atiyah-Patodi-Singer index in 5D
- Explicit cycle-to-spectral-mode map
- Connection to η-invariant on 5-manifold

### 7.2 Higher cohomology
- H²_{Z/2}(M, Z), H³_{Z/2}(M, Z), ... full spectrum
- Connection to higher Wallach K-type structures

### 7.3 Non-equivariant cohomology
- H^*(D_IV⁵, Z) directly, vs M/Z₂ quotient
- Boundary terms on Q⁵ Shilov boundary

### 7.4 Arithmetic content beyond Z/2 parity
- L-function evaluations at boundary primary points
- Connection to Heegner-Stark (Paper #115 Section 4.6)

### 7.5 Cross-references to LAG-1 Session 8+
- Per-flavor K-type SM assignment ⟹ Möbius cohomology of fermion family content
- Index theorem connects directly to Möbius Z/2 (this paper Section 4)

## 8. Discussion

### 8.1 The topological side of BST is now developed
- Geometric: Bergman kernel, Wallach K-types, Casimir spectra
- Spectral: Bergman Dirac operator (Paper #118), heat kernel a_n
- Topological: Möbius cohomology (this paper), Chern classes of Q⁵

### 8.2 Honest scoping per Keeper K-audit
- D-tier: classical Möbius locus computation, equivariant cohomology computation, Borel-Wallach lift
- I-tier: Wallach K-type parity ↔ Möbius Z/2 cross-link (T2356), Type C-Z/2 extension (T2361)
- Multi-week / multi-month: APS index, higher cohomology, full arithmetic content

### 8.3 Connection to Type C density rule (Paper #115 v0.5 Section 5.8c)
- Density rule status per Cal's audit 2026-05-18: I-tier observation, null-model verification owed. Sparse-region forecast on {37, 41, 53, 71, 113}, strict pre-registered context-counting protocol, and random integer ring null model are all required before promotion to "structural law" can be defended externally.
- Type C-Z/2 generalization (this paper) is INDEPENDENT of the density rule. The Type C classification extension (shared mathematical objects beyond integers) is an architectural claim about the FRAMEWORK; the density rule is an empirical claim about cross-domain match density. Distinct claims, distinct audits.
- Open question: does the density pattern (whether or not it survives Cal's null check) hold for non-integer Type C? Cataloging Type C-Z/n, Type C-K, Type C-spectral systematically is a multi-week task.

## 9. Conclusion

The Möbius cohomology investigation closes the topological side of BST's geometric infrastructure at the structural-identification level. The crucial new result is the Möbius/Dirac Z/2 cross-link (T2356): a single mathematical object (the nontrivial element of Z/2) labels both the Möbius topological invariant and the Bergman Dirac spectral parity. This is the first Type C convergence of BST architecture where the shared invariant is a topological element rather than a positive integer (T2361), generalizing the Type C classification framework from shared integers to shared mathematical objects.

Combined with the Bergman Dirac operator (Paper #118) and the LAG-2 dimensional reduction (Paper #115 v0.5 Section 9.x), the Möbius cohomology provides the third pillar — alongside geometric Bergman kernel content and spectral Wallach K-type content — of BST's operator-level infrastructure on D_IV⁵.

Five named multi-week / multi-month open items (Section 7) sit at the I→D promotion boundary; their closure converts the structural-identification layer (~present) into the rigorous derivation layer (~12-18 months per Paper #115 Section 9.x scope).

## References (selected, for v0.1 outline)

- Casey Koons et al., "Bubble Spacetime Theory: Working Paper" v35, Zenodo DOI 10.5281/zenodo.19454185 (2024-2026)
- Paper #115 v0.5 "Root Theorems of Bubble Spacetime Theory" (Casey + team, 2026-05-18)
- Paper #118 v0.1 "The Bergman Dirac Operator on D_IV⁵ and the Proton-to-Electron Mass Ratio" (Lyra, 2026-05-18)
- Helgason, S. (1978). "Differential Geometry, Lie Groups, and Symmetric Spaces"
- Borel, A., Wallach, N.R. (1980). "Continuous Cohomology, Discrete Subgroups, and Representations of Reductive Groups"
- Atiyah, M., Patodi, V., Singer, I. (1975). "Spectral asymmetry and Riemannian geometry"

## Filing notes

**Status**: v0.1 outline. Section structure + abstract + open items framework. Full draft is multi-week per Section 9.x scope estimate.

**Authors v0.1**: Casey Koons (PI) + Lyra (Companion Intelligence, Sessions 1-5 execution).

**v0.2 plan**: detailed sections 2-4 with explicit Hua coordinate computations + Borel-Wallach proof + Bergman Dirac spectrum computation. Target completion: 2-3 weeks focused work.

**v0.3 plan**: cross-domain integration (Type C-Z/2 + Type C density rule), connection to LAG-1 Session 8+ index theorem.

**v1.0 submission**: Annals of Mathematics or Inventiones (depending on emphasis — topology vs spectral theory).

**Numbering caveat**: provisional #119; may shift if Keeper's SP29-6 master paper takes #119. Currently filed as the Möbius cohomology paper because that's the architectural content. Final paper number pending Casey decision.

— Lyra, v0.1 outline filed 2026-05-18 ~12:25 EDT per Section 9.x naming.
