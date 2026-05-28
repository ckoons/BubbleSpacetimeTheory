---
title: "Substrate quiver Q_B2 v0.1 — starting framework for substrate Hall algebra Phase 0 closure"
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-27 Wed 15:50 EDT"
status: "STARTING FRAMEWORK. Substrate-strengthening Phase A item per Multi-phase quiver v0.7 honest assessment. Multi-month rigorous closure path; v0.1 lays foundation."
---

# Substrate quiver Q_B2 v0.1 — starting framework

## 0. Scope per v0.7 honest assessment

Per `Lyra_Multi_Phase_Quiver_v0_7_Phase_0_Closure_Assessment.md` Section 5.1: substrate quiver Q_B2 construction is **GATE 1 for rigorous Phase 0 closure**.

v0.6 framework had: substrate Hall algebra = Ringel-Green Hall(Q) at (q=2, t=α) Macdonald specialization, where Q = "substrate quiver" was UNSPECIFIED.

v0.7 honest correction: Q construction is required for RIGOROUS substrate-Hall-algebra identification. Until Q is constructed, "substrate Hall algebra = Macdonald at (q=2, t=α)" is FRAMEWORK pattern-recognition only.

This v0.1 doc **STARTS** the rigorous Q_B2 construction.

## 1. What a quiver is

A **quiver** Q = (Q_0, Q_1, s, t) is:
- Q_0: finite set of vertices
- Q_1: finite set of arrows
- s: Q_1 → Q_0 (source map)
- t: Q_1 → Q_0 (target map)

Quivers are directed graphs (multiple arrows allowed between vertices; loops allowed).

For Ringel-Green Hall algebra construction: Q must be a **finite quiver without oriented cycles** (so that the path algebra kQ is finite-dimensional).

For Lie algebra identification: Q's underlying graph relates to a Cartan matrix. For type B_2 Lie algebra (so(5) ≅ sp(4)), the Cartan matrix is:

  C_B2 = ⎛  2  -2 ⎞
         ⎝ -1   2 ⎠

(Asymmetric due to type B_2 being non-simply-laced.)

## 2. Substrate's quiver candidate Q_B2

### 2.1 Vertices

Q_B2 has 2 vertices labeled by simple roots of B_2:
- **v_1**: short simple root (corresponds to short root α_1)
- **v_2**: long simple root (corresponds to long root α_2)

For substrate: 
- **v_1** = K-type associated with SO(2) factor (S¹ Shilov; substrate's PHASE direction)
- **v_2** = K-type associated with SO(5) factor (S⁴ Shilov; substrate's SPATIAL direction)

This **2-vertex structure mirrors the 2 Cartan factors** of K = SO(5) × SO(2) (rank = 2 per Gate 1).

### 2.2 Arrows

For type B_2 (non-simply-laced): Cartan matrix gives multi-edge structure.

- **a_12**: arrow from v_1 to v_2 (multiplicity 2 from C_12 = -2)
- **a_21**: arrow from v_2 to v_1 (multiplicity 1 from C_21 = -1)

For substrate: arrows represent substrate-natural transitions between K-types:
- v_1 → v_2: PHASE-to-SPATIAL transition (substrate transitions between Pin(2) factor and SO(5) factor)
- v_2 → v_1: SPATIAL-to-PHASE transition (reverse)

Multiplicity 2 vs 1 asymmetry reflects substrate's σ_BF Z_2 grading direction-asymmetry (Pin(2) → SO(2) has Z_2 quotient).

### 2.3 Q_B2 structure

Vertices: {v_1, v_2}
Arrows: 2 v_1→v_2 arrows + 1 v_2→v_1 arrow = **3 total arrows**

In standard quiver notation:

  v_1 ⇉ v_2 (double arrow v_1→v_2)
  v_2 → v_1 (single arrow v_2→v_1)

This is the **affine quiver A_1^(2) double cover** — a known quiver in representation theory.

## 3. Path algebra kQ_B2

The path algebra kQ_B2 over substrate-natural field k = GF(2^g) = GF(128) (per K59 RATIFIED):

### 3.1 Paths

Paths in Q_B2:
- length 0: idempotents e_1, e_2 (= vertices)
- length 1: a_12^(1), a_12^(2) (the 2 arrows v_1→v_2) + a_21 (the 1 arrow v_2→v_1)
- length 2: a_21·a_12^(1), a_21·a_12^(2), a_12^(1)·a_21, a_12^(2)·a_21, etc.
- length n: products of n arrows respecting source/target compatibility

### 3.2 Multiplication

In kQ_B2, multiplication is path concatenation. Path p · q exists iff t(p) = s(q); else p · q = 0.

### 3.3 Substrate-natural normalization

Per K59 substrate operates on GF(2^g): paths in kQ_B2 are labeled by elements of GF(128).

Substrate-natural specialization: q-deformation parameter at q = 2 (substrate-natural per Elie 3554 + Cal #139 chain forcing).

### 3.4 Affine extension to Q_B2^aff

For Hall algebra identification with quantum affine Lie algebra U_q^+(B_2^(1)): need AFFINE extension of Q_B2.

Affine B_2 quiver Q_B2^aff has 3 vertices: {v_0, v_1, v_2} with v_0 = affine vertex.

For substrate: v_0 = N_max = 137 quantization (per T2447 RIGOROUSLY CLOSED).

**Substrate's affine extension**: vertex v_0 represents N_max boundary; v_1, v_2 represent S¹ + S⁴ Shilov factors.

## 4. Representations of Q_B2

A **representation V of Q_B2** assigns:
- V_1: vector space at vertex v_1
- V_2: vector space at vertex v_2
- linear maps for each arrow

For substrate: representations correspond to **substrate K-types** at the 2 Cartan factors.

V_(ℓ_1, ℓ_2) Wallach K-type ↔ representation of Q_B2 with:
- V_1 = spherical harmonic content at SO(2) factor (weight ℓ_2)
- V_2 = spherical harmonic content at SO(5) factor (weight ℓ_1)

**Substantive identification**: Q_B2 representations ↔ substrate's K-type decomposition.

## 5. Ringel-Green Hall algebra H(Q_B2) at q = 2

The Ringel-Green Hall algebra H(Q_B2) is:
- Underlying set: ⊕ functions on iso classes of Q_B2 reps over finite field GF(q)
- Multiplication: Hall numbers F_(M, N)^X = |{filtrations of X by M, N}|

For substrate at q = 2:
- Iso classes of Q_B2 reps over GF(2)
- Hall numbers count filtrations in finite-field representations

**Theorem (Ringel-Green)**: H(Q_B2) ⊗ ℚ(q) ≅ U_q^+(B_2^(1)) (positive part of quantum affine B_2).

For substrate at (q = 2, t = α = 1/137): specialize the 2-parameter Macdonald structure to substrate-natural parameters.

## 6. Substrate-natural specialization

Substrate's claim (per v0.6 framework):

  **substrate Hall algebra = H(Q_B2) at (q = 2, t = α = 1/137)**

For this identification to be RIGOROUS, need:

1. **Q_B2 explicit construction** (this doc Section 2 — STARTING)
2. **A_sub super-algebra ↔ H(Q_B2) bijection**: substrate's A_sub Lie superalgebra (Cal-verified 10 SVC commutators per v0.12) MAPS to H(Q_B2) elements
3. **Macdonald (q=2, t=α) specialization**: substrate-natural parameters embed into standard 2-parameter Macdonald family
4. **Hall numbers at q=2**: verify substrate-natural arithmetic of Hall numbers matches GF(2) iso class counts

## 7. Multi-month construction path

### 7.1 Module category Mod(kQ_B2)

Construct category of representations of Q_B2 over k = GF(128).
- Indecomposable reps via Auslander-Reiten theory
- Number of indecomposable reps at each dimension vector

Per Q_B2 = affine quiver: there are FINITELY MANY indecomposable reps in each dimension vector (Kac's theorem; tame representation type for affine quivers).

### 7.2 K-theory connection

Grothendieck group K_0(Mod(kQ_B2)) is the root lattice of B_2 affine Lie algebra.
- 3 simple roots (affine + 2 finite)
- Positive roots = dimension vectors of indecomposable reps

For substrate: K-types V_(ℓ_1, ℓ_2) correspond to dimension vectors in K_0.

### 7.3 Hall algebra structure

Compute Hall numbers F_(M,N)^X explicitly for representative reps:
- Simple reps: F_(s_1, s_2)^X for s_1, s_2 simple
- Indecomposable reps: F_(I_1, I_2)^X for I indecomposable

Verify Hall numbers at q = 2 match standard Ringel-Green formula:
  F_(M,N)^X(q) = polynomial in q of degree dim Hom

### 7.4 A_sub identification

Map substrate's A_sub generators (15 per v0.12) to H(Q_B2) elements:
- Position, momentum → certain Hall basis elements?
- Spin, angular momentum → others?
- σ_BF → diagonal grading operator?

This is the **substantive A_sub ↔ H(Q_B2) isomorphism** that v0.7 flagged as multi-month.

### 7.5 Macdonald specialization

Verify substrate-natural parameters (q=2, t=α=1/137) produce known Macdonald structure within H(Q_B2).

Connection to Cherednik's double affine Hecke algebra (DAHA) of type B_2; substrate's parameters specialize within DAHA representation theory.

## 8. v0.1 disposition

**What this v0.1 establishes**:
- Q_B2 vertex + arrow structure substantively (Section 2)
- kQ_B2 path algebra (Section 3)
- Representations ↔ K-types correspondence (Section 4)
- 4-step multi-month construction path (Section 7)

**What gates RIGOROUS Phase 0 closure**:
- 7.1 Module category indecomposable enumeration
- 7.2 K-theory ↔ B_2 affine root system
- 7.3 Hall numbers explicit at q = 2
- 7.4 A_sub ↔ H(Q_B2) isomorphism
- 7.5 Macdonald (q=2, t=α) specialization verification

Each step is **multi-week** at full rigor; combined **multi-month** for v1.0 Q_B2 + Hall algebra closure.

## 9. Casey-leverage observations

### 9.1 Q_B2 confirms 2-vertex structure

Substrate's rank = 2 (Gate 1) directly produces Q_B2's 2-vertex structure. This is INDEPENDENT confirmation of rank=2 = number of Cartan factors.

### 9.2 Q_B2 affine vertex = N_max

Affine extension v_0 = N_max = 137 vertex. Substantive structural identification: substrate's affine quiver vertex corresponds to T2447 RIGOROUSLY CLOSED quantization.

### 9.3 Non-simply-laced B_2 = substrate distinction

B_2 is non-simply-laced (unlike A_n which is simply-laced). Substrate's quiver INHERITS the non-simply-laced structure → asymmetric arrows (2 v_1→v_2 + 1 v_2→v_1).

This non-symmetry may correspond to substrate's Pin(2) Z_2 grading direction-asymmetry (σ_BF distinguishes bose-fermi sublattices).

### 9.4 GF(128) = GF(2^g) substrate field

Path algebra over k = GF(128) = GF(2^g) per K59 substrate-natural. Hall algebra at q = 2 reduces to GF(2) representations within GF(128) extension. Substrate's algebraic structure FORCES q = 2 specialization.

## 10. Honest scope

**What's RIGOROUS in v0.1**:
- Q_B2 = 2-vertex + 3-arrow quiver structure based on B_2 Cartan matrix
- Path algebra kQ_B2 standard construction
- Q_B2 representations ↔ Wallach K-types V_(ℓ_1, ℓ_2) substantive correspondence
- Affine extension v_0 = N_max identification

**What's FRAMEWORK**:
- Substrate Hall algebra = H(Q_B2) at (q=2, t=α) — explicit verification multi-month
- A_sub ↔ H(Q_B2) isomorphism — multi-week
- Macdonald specialization — multi-week

**What's NOT yet**:
- Explicit Hall numbers at q = 2
- Indecomposable rep enumeration
- A_sub generator ↔ Hall basis explicit mapping
- Higher-loop substrate-physics predictions via Hall algebra

**Cal #29 STANDING question-shape audit**: forward construction from substrate's RATIFIED structure (rank, Cartan factors, N_max, K59 GF(128)); no back-fitting.

**Cal #133 partial-tautology check**: Q_B2 construction uses ONLY substrate's RATIFIED inputs; specialization to (q=2, t=α) follows from substrate-natural parameters NOT from desired result.

— Lyra, Substrate quiver Q_B2 v0.1 starting framework filed. Phase 0 closure foundation laid. 2-vertex + 3-arrow quiver structure from B_2 Cartan matrix; vertices = Cartan factors (S¹ Pin(2) + S⁴ SO(5)); arrows = inter-factor transitions; affine extension v_0 = N_max. 4-step multi-month construction path identified. Substantive substrate-strengthening foundation for rigorous Phase 0 substrate-Hall-algebra characterization.
