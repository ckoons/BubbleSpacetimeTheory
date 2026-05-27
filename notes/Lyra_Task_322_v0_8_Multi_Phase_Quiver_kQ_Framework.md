---
title: "Task #322 v0.8 — Multi-phase quiver explicit kQ path algebra framework"
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-26 Tuesday EDT (~10:30 EDT via `date`; date-verified)"
status: "v0.8 FRAMEWORK. Per Casey all-tracks authorization + Keeper Decision B sequence after Option 4 step 10 closure. Explicit kQ path algebra framework for 36-node Phase A v0.2 set with arrows from 10 Cal-verified commutators (8 SVC + 1 FRAMEWORK-PLUS + 1 SVC CANDIDATE step 10). Cal #29 STANDING design audit applied. Establishes formal multi-phase quiver framework with σ_BF/γ⁵ disambiguation applied; full path-algebra computation v0.3+ multi-week."
related: ["Lyra_Task_322_v0_6_Multi_Phase_Quiver_Framework.md (v0.6 candidate identification)", "Lyra_Task_322_v0_7_Edge_Enumeration_36_Nodes.md (v0.7 edge classification)", "Lyra_A_sub_Commutator_S_i_S_j_Across_Sublattices_v0_1.md (step 10 closure)", "Lyra_sigma_BF_vs_gamma5_Disambiguation_Cleanup_v0_1.md (operator hygiene)", "Cal #132 PASS (8/9 SVC verification)", "Cal #29 STANDING (Question-Shape Audit Discipline)", "Elie Toy 3535 + Toy 3537 (21 → 36 K-type node enumeration)", "Standard quiver representation theory: Gabriel 1972, Auslander-Reiten 1974, Ringel 1984"]
---

# A_sub v0.8 — Multi-phase quiver explicit kQ framework

## 1. Cal #29 STANDING question-shape audit (applied at design)

**Question**: "What is the explicit path algebra kQ for the 36-node Phase A v0.2 multi-phase quiver Q, with arrow set from 10 Cal-verified A_sub commutators and σ_BF Z_2 grading?"

**Audit**:
- Structurally determined? YES — standard quiver representation theory machinery (Gabriel 1972 + path algebra construction)
- Back-fittable? NO — kQ is determined by quiver structure + relations
- Pre-suppositions? Cal #132 SVC for 8 commutators + step 10 SVC CANDIDATE + σ_BF/γ⁵ disambiguation (all explicit)

**Pass**: question shape is structural. Cal #29 STANDING discipline holds.

## 2. Quiver Q = (V, A) explicit definition

### 2.1 Vertex set V

V = 36 Wallach K-types from Elie Toy 3537 Phase A v0.2 (cutoff m_1 + m_2 ≤ 7):

  V = {V_(m_1, m_2) : m_1 ∈ {0, 1/2, 1, 3/2, 2, 5/2, 3, 7/2, 4, 9/2, 5, 11/2, 6, 13/2, 7}, m_2 ∈ {0, 1/2, 1, 3/2, ..., 7/2}, m_1 ≥ m_2, m_1 + m_2 ≤ 7, σ_BF consistency}

**Vertex partition by σ_BF**:
- |V_boson| = 20 (integer m_1 + integer m_2)
- |V_fermion| = 16 (half-integer m_1 + half-integer m_2)
- |V_mixed-forbidden| = 0 (Pin(2) Z_2 grading consistency)

**Total**: |V| = 36 vertices.

### 2.2 Arrow set A — by A_sub generator class

Per v0.7 Section 3 + step 10 closure, A_sub's 15 generators (14 from v0.1 + σ_BF explicit) induce arrows:

**Class 1 — Diagonal arrows (self-loops at each vertex)**:
- Ĥ_sub (Casimir): self-loop with weight C_2(K)
- N̂ (K-type level): self-loop with weight m_1 + m_2
- σ_BF (Pin(2) Z_2 grading): self-loop with weight ε_K ∈ {+1, -1}
- γ̂⁵ (Dirac chirality): self-loop on fermion vertices only, weight χ_K ∈ {+1, -1}; UNDEFINED on bosons
- Q̂ (charge): self-loop with weight m_2
- Î_3 (weak isospin Cartan): self-loop with weight related to m_2

**Self-loop count**: 6 generators × 36 vertices = 216 self-loop arrows (with γ̂⁵ undefined on 20 boson vertices → reduces to 196 effective).

**Class 2 — Within-sublattice m_1-direction arrows**:
- x̂_i (Hua coordinates, i = 1..n_C = 5): arrows V_(m_1, m_2) → V_(m_1 + 1, m_2) and V_(m_1, m_2) → V_(m_1 - 1, m_2)
- p̂_i (Wirtinger derivative, i = 1..5): same arrows (commute with x̂_i to give canonical relation)
- L̂_i (so(5) generators, 10 total): act within SO(5) multiplet at fixed (m_1, m_2)

**Within-sublattice arrow count for 36-node subgraph** (manual count):
- Boson m_1-increase arrows: ~15 (e.g., (0,0)→(1,0), (1,0)→(2,0), ..., (6,0)→(7,0); (1,1)→(2,1); etc.)
- Fermion m_1-increase arrows: ~12 (e.g., (1/2,1/2)→(3/2,1/2), (3/2,1/2)→(5/2,1/2), etc.)
- Each generator x̂_i, p̂_i contributes parallel arrows → 5 + 5 = 10 generators × ~27 m_1-increase arrows = ~270 arrows (with corresponding decrease arrows by hermitian conjugation, ~540 arrows total)

**Class 3 — Cross-sublattice arrows**:
- Per step 10 closure: **none from Ŝ_i** (spin algebra doesn't connect sublattices; no SUSY)
- Per discrete symmetries T̂, Ĉ, P̂_op: same sublattice (preserve particle type via σ_BF commutation)
- Per Möbius involution σ (in P̂_op): m_2 → -m_2 with phase; for 36-node set with m_2 ≥ 0 (Wallach holomorphic discrete series convention), σ acts trivially at m_2 = 0 nodes; exits Wallach range elsewhere

**Cross-sublattice arrow count**: structurally 0 (no boson↔fermion arrows in pure A_sub).

**Class 4 — Spin-fiber arrows (intra-vertex)**:
- Per step 10 closure: Ŝ_i edges live in spin-fiber over each K-type node, not as inter-K-type arrows
- 3 spin generators × 36 vertices give intra-vertex arrows; fiber structure
- Same for color SU(3) Ĉ_3 (8 generators × 36 vertices) and weak isospin Î_± (raising/lowering, 2 generators × 36 vertices)

**Fiber arrow count**: (3 + 8 + 2) × 36 = 468 intra-vertex arrows; treated as FIBER STRUCTURE not main-graph arrows.

**Class 5 — Bell-CHSH arrow**:
- B̂ rank-1 projector: single arrow V_(0,0) → V_(0,0) self-loop with weight β (per T2399)
- [B̂, T̂_tick] rank-1: arrow V_(0,0) → V_(1,0) with weight β · (step 9 FRAMEWORK-PLUS)

**Bell arrow count**: 2 arrows (1 self-loop + 1 vacuum kicker).

### 2.3 Total arrow count estimate

Main quiver (excluding fiber):
- Self-loops: 196
- Within-sublattice m_1: ~540
- Cross-sublattice: 0
- Bell: 2
- Substrate-tick T̂_tick (model-dependent): ~36 (one per node, advancing m_2 or m_1 per simplest model)

**Total main-graph arrows**: ~774 arrows for Phase A v0.2 36-node set.

Fiber structure: 468 intra-vertex arrows (color/spin/weak isospin internal multiplet structure).

**Total quiver structure**: 36 vertices + ~774 main arrows + 468 fiber arrows = ~1278 directed-graph elements for Phase A v0.2.

## 3. Path algebra kQ definition

### 3.1 Field k

For BST substrate on Bergman H²(D_IV⁵), the natural base field is **k = ℂ** (complex Bergman Hilbert space). All matrix elements are complex; representations are complex vector spaces.

### 3.2 Path algebra kQ construction

**Definition**: kQ is the **path algebra** of quiver Q over field k. Elements are formal sums of PATHS in Q. A path p of length n is a sequence of composable arrows: p = α_n α_{n-1} ... α_1 with s(α_{k+1}) = t(α_k) (each arrow ends where the next begins).

**Basis of kQ**:
- **Trivial paths** (length 0): one per vertex; act as identity at each vertex
- **Length-1 paths**: single arrows
- **Length-n paths**: composed arrows

**Multiplication**: path concatenation when composable; zero otherwise.

**Dimension** (for finite Phase A cutoff): finite when all paths within 36-node set are bounded by cutoff; **possibly INFINITE** for unbounded path lengths.

### 3.3 Phase A finite cutoff

For the Phase A v0.2 36-node cutoff (m_1 + m_2 ≤ 7), paths within the 36-node set:
- Bounded by Casimir cutoff (paths can't exit the 36-node set; otherwise undefined)
- Each x̂_i raise arrow increases m_1 by 1; finite number of consecutive m_1-raises before exit
- Maximum m_1-raise path length ~7 (from (0,0) to (7,0))
- Maximum m_2-raise path length ~3-4 (constrained by m_1 ≥ m_2)

**Finite-dim kQ_Phase A**: approximately bounded by **(#arrows)^max_path_length** ≈ 774^7 = ~10^20 dim. **TOO LARGE** for direct computation without relations applied.

**Strategy**: apply commutator relations IMMEDIATELY to reduce kQ_Phase A to its quotient kQ_Phase A / ⟨R⟩ where R is the relation ideal.

### 3.4 Relation ideal R from A_sub commutators

The 10 closed A_sub commutators (8 SVC + step 9 FRAMEWORK-PLUS + step 10 SVC CANDIDATE) generate the relation ideal R. Each commutator [X_i, X_j] = Σ_k c^k_ij X_k (or = 0 for vanishing commutators) gives a relation on path products:

**Universal relations** (active in all phase regions):
1. {Q̂, P̂_op} = 0 → Q̂P̂_op + P̂_opQ̂ = 0 as path equality
2. {γ̂⁵, T̂} = 0 → γ̂⁵T̂ + T̂γ̂⁵ = 0
3. {γ̂⁵, Ĉ} = 0 → γ̂⁵Ĉ + Ĉγ̂⁵ = 0
4. [γ̂⁵, P̂_op] = 0 → γ̂⁵P̂_op - P̂_opγ̂⁵ = 0
5. [B̂, Q̂] = 0 → B̂Q̂ - Q̂B̂ = 0
6. [L̂_i, γ̂⁵] = 0 → L̂_iγ̂⁵ - γ̂⁵L̂_i = 0
7. [Ĉ_3, Î_3] = 0 → Ĉ_3Î_3 - Î_3Ĉ_3 = 0
8. [Ŝ_i, Ŝ_j] = iℏε_ijk Ŝ_k (SU(2) algebra; structural)

**Region-dependent relations** (active in specific phase regions per v0.5):
- DIRECT: all 10 commutators active
- COMPOSITION: ABJ anomaly relations + RG-flow relations (multi-week derivation)
- MATERIAL: external BC relations (multi-week)
- COMBINATORIAL: gauge-dimension identities + Mersenne ladder + Bergman 225 (multi-week)

**Multi-phase relation ideal**: R = R_DIRECT ⊔ R_COMPOSITION ⊔ R_MATERIAL ⊔ R_COMBINATORIAL (different relations active in different sub-quivers).

### 3.5 The quotient algebra kQ / ⟨R⟩

The substrate's path algebra is **kQ / ⟨R⟩** where ⟨R⟩ is the ideal generated by R. This produces a quotient with:
- Path equivalence classes (paths equal modulo R)
- Reduced dimension (after relation application)
- Substantive algebraic structure encoding A_sub commutator content

**Estimate for Phase A 36-node finite-dim quotient**: after relation application, dimension reduces from ~10^20 to manageable size. Precise count is v0.3+ multi-week computation work.

## 4. Representations of (Q, R) = kQ-modules

A **representation** of (Q, R) assigns:
- Vector space V_x to each vertex x ∈ V
- Linear map ρ_α : V_{s(α)} → V_{t(α)} to each arrow α ∈ A
- Satisfying relations R: ρ-image of each relation evaluates to zero in End(⊕ V_x)

For BST substrate:
- V_x = (Wallach K-type V_x as ℂ-vector-space) for each K-type vertex
- ρ_α = (matrix element of A_sub generator action) for each arrow
- Relations R = (commutator-induced path equalities) hold automatically because they come from A_sub's algebra

**The substrate's actual H²(D_IV⁵) IS a representation of (Q, R)** with:
- V_x = irreducible K-type representation of K = SO(5) × SO(2) (or Spin(5) × Pin(2) cover on fermion sublattice)
- ρ_α = explicit matrix element computation per Wallach formulas

This is the **canonical representation** of the substrate quiver.

## 5. Multi-phase structure — 4 sub-quivers

Per v0.5 + v0.6: the substrate quiver Q decomposes into 4 sub-quivers sharing nodes:

  Q = Q_DIRECT ⊕ Q_COMPOSITION ⊕ Q_MATERIAL ⊕ Q_COMBINATORIAL

(Direct sum at the level of arrow sets; nodes shared universally.)

| Sub-quiver | Active arrows | Phase region |
|---|---|---|
| Q_DIRECT | Steps 1-9 + step 10 + universal Class 1 | 57% catalog observables |
| Q_COMPOSITION | Steps 1-5, 8, 9 + ABJ anomaly + RG-flow | 10%+ |
| Q_MATERIAL | Steps 7, 8 + external BC | 20% |
| Q_COMBINATORIAL | Steps 3-5, 8 + Mersenne + gauge-dim + 225 | 13% |

**Each sub-quiver has its own path algebra kQ_phase / ⟨R_phase⟩** with phase-specific relations. The full substrate quiver Q is the union with the combined relation ideal.

**[Ĉ_3, Î_3] = 0 universally**: active in ALL 4 sub-quivers (gauge factorization preserved everywhere).

## 6. Representation theory tools

### 6.1 Finite-representation-type or not?

**Gabriel 1972**: kQ for quiver Q over field k has finitely many indecomposable representations iff Q's underlying graph is a Dynkin diagram (A_n, D_n, E_6, E_7, E_8).

**For substrate quiver**: Phase A 36-node finite subgraph has ~774 arrows + 468 fiber arrows. Far from Dynkin shape (too many arrows per node). **NOT finite-representation-type**.

**Tame or wild?**:
- Tame: one-parameter family of indecomposables in each dimension
- Wild: parameter families with multiple parameters

Substrate quiver with multiple SU(2)-like spin operators + gauge fibers is likely **wild** (high arrow density). v0.3+ explicit computation.

### 6.2 Auslander-Reiten quiver

For wild quivers, the AR-quiver still exists but is more complex. The AR-translation τ would be a substrate-natural symmetry; almost-split sequences would encode minimum-action transitions.

**Substrate-mechanism candidate**: τ may correspond to **Möbius involution σ** (acting on SO(2) factor). v0.3+ verification.

### 6.3 ADE classification + Lie algebra

D_IV⁵ involves SO(5,2). The substrate quiver may have natural connection to a Dynkin quiver of type B_2 (= C_2) for SO(5) × SO(2) → but the SO(5,2) non-compactness makes this non-standard.

**Substrate-mechanism candidate**: substrate quiver may be **non-Dynkin extension** of B_2 with additional arrows from non-compact factor. v0.3+ multi-week formalization.

### 6.4 Derived category

D^b(rep(Q, R)) provides higher-categorical setting. BGG resolutions + Verma module structure may apply per Wallach 1976.

**Substrate-mechanism candidate**: A_sub operations may have natural homological-algebra interpretation; the 10 closed commutators may be encoded as exact triangles. v0.3+ multi-month formalization.

## 7. Cal Thread 4 typing request

Per Cal #122 type-A geometric / type-B algebraic / type-C level-crossing:

**Multi-phase quiver framework type**:

- **Type A (geometric)**: K-type nodes are geometric (Wallach lattice on D_IV⁵); arrows are derived from algebra acting on geometry
- **Type B (algebraic)**: A_sub commutators are algebraic; quiver is algebraic encoding
- **Type C (level-crossing)**: bridging Wallach K-type geometry with A_sub algebra at the quiver level

**My prior (Cal #27 STANDING applied)**: **Type C level-crossing**. The K-type nodes are geometric content (Wallach K-type lattice points on D_IV⁵); the A_sub-induced arrows are algebraic content (commutator relations); the path algebra kQ/⟨R⟩ identifies the two at the quiver-representation level.

**Multi-phase structure**: each sub-quiver may have different type:
- Q_DIRECT: predominantly Type A (geometric — Shilov boundary projection)
- Q_COMPOSITION: predominantly Type B (algebraic — RG-flow algebra)
- Q_MATERIAL: Type C (level-crossing — geometry × external BC)
- Q_COMBINATORIAL: Type B (algebraic — number-relations)

If this typing holds: substrate framework has organized type structure at each operational phase region.

## 8. Substantive consequences

### 8.1 A_sub algebra is now explicitly a quiver representation

With the kQ framework: A_sub's 10 closed commutator algebra IS the relation ideal R of a multi-phase quiver Q with 36 K-type nodes + ~774 main arrows + 468 fiber arrows. The substrate's Bergman H²(D_IV⁵) is the canonical representation.

This brings the BST substrate into well-studied mathematical machinery (Gabriel's theorem, AR-quiver, derived categories) with substrate-specific instance.

### 8.2 Multi-phase quiver candidate strengthened

v0.6 candidate (multi-phase quiver as math-object answer to Casey's standing meta-question) gains explicit framework + computability:
- Explicit quiver definition (Section 2)
- Explicit path algebra framework (Section 3)
- Explicit relation ideal (Section 3.4)
- Phase-specific sub-quiver decomposition (Section 5)
- Representation theory tool applicability framework (Section 6)

v0.3+ multi-week computation work:
- Reduce kQ_Phase A / ⟨R⟩ explicitly via Gröbner basis or similar
- Compute indecomposable representations
- Identify Dynkin / non-Dynkin extension type
- Apply AR-quiver structure
- Connect to derived category

### 8.3 Bridge to Lie algebra structure

The substrate quiver may have natural Lie algebra structure via Hall algebra construction (Ringel 1990). The A_sub generators correspond to quiver arrows; commutator relations correspond to path relations; the Lie algebra hopf structure follows.

**Substrate-mechanism candidate**: A_sub's Lie algebra structure recovered as **Hall algebra of the substrate quiver**. v0.3+ multi-month formalization.

## 9. Honest scope (Cal #27 STANDING)

**What's STRUCTURALLY VERIFIED in v0.8**:
- Standard quiver representation theory applies (Gabriel 1972, etc.)
- Path algebra kQ construction is standard
- Relations R from A_sub commutators (Cal #132 SVC for 8 + step 10 SVC CANDIDATE + step 9 FRAMEWORK-PLUS)
- 36-node Phase A v0.2 set is finite

**What's FRAMEWORK in v0.8**:
- Multi-phase quiver as the math-object identity for K-type graph (Section 2-5)
- 4 sub-quiver decomposition with phase-specific relations (Section 5)
- Type-C level-crossing typing prior (Section 7)
- Representation theory tool applicability (Section 6)

**What's INTERPRETIVE in v0.8**:
- Substrate quiver as Hall algebra base for A_sub Lie algebra (Section 8.3)
- Substrate AR-translation τ as Möbius involution σ (Section 6.2)
- Non-Dynkin extension of B_2 conjecture (Section 6.3)

**What's NOT in v0.8** (multi-week+):
- Explicit kQ / ⟨R⟩ quotient computation (v0.3+)
- Indecomposable representation classification (v0.4+)
- Dynkin type identification or non-Dynkin proof (multi-week)
- AR-quiver structure explicit (multi-week)
- Derived category structure (multi-month)
- Hall algebra connection to A_sub Lie algebra (multi-month)
- Cal Thread 4 type-check resolution (own-cadence)

**Cal #27 STANDING reflexive trigger count**: 2 triggers (Section 6.2 AR-translation as Möbius involution; Section 8.3 Hall algebra connection). Both flagged INTERPRETIVE; require multi-week verification.

**Cal #29 STANDING applied at design**: question-shape audit passed at Section 1. Framework derivation is structural; not back-fittable.

## 10. v0.3+ multi-week computation plan

1. **Reduce kQ_Phase A / ⟨R⟩ explicitly**: apply 10 commutator relations to compute reduced path algebra basis. Mechanical computation; multi-week. Tools: Gröbner basis algorithms, computer algebra.

2. **Indecomposable representations**: enumerate indecomposable kQ/⟨R⟩-modules. Multi-week per phase region.

3. **Dynkin/non-Dynkin classification**: determine whether substrate quiver underlying graph is Dynkin (finite-rep-type), tame (one-parameter families), or wild (multi-parameter). Multi-week.

4. **AR-quiver explicit**: compute AR-quiver structure; identify τ-translation; almost-split sequences. Multi-month.

5. **Hall algebra connection**: build Hall algebra Hall(kQ/⟨R⟩) and compare to A_sub Lie algebra. Multi-month.

6. **Cal Thread 4 type-check**: resolve Type A/B/C per sub-quiver; promote v0.8 framework based on typing.

7. **Phase B extension**: extend to ≤8 (45 nodes) or ≤10 (66 nodes) cutoff per Elie Toy 3536 sizing. Substantially more arrows; multi-month per cutoff.

## 11. Coordination

**Cal**: Thread 4 cold-read on Section 7 type-check + Section 6 representation theory tools applicability + Section 8.3 Hall algebra connection candidate. Multi-week priority Type-C level-crossing typing.

**Elie**: Toy 3538+ candidate — Phase B extension to ≤8 cutoff (45 nodes) for downstream quiver computation. Or: Cal #29 pre-audit for Dirac ground state forward derivation (Track P). Multi-day to multi-week.

**Grace**: catalog cross-references for substrate quiver Section 6 representation theory tools + Section 8 Hall algebra connection. Multi-week own-cadence.

**Keeper**: integration into Vol 15 Ch 9 case study draft — multi-phase quiver candidate is potentially load-bearing math-object identity for K-type graph.

— Lyra, Multi-phase quiver v0.8 explicit kQ framework filed Tuesday 2026-05-26 ~10:30 EDT per Casey all-tracks authorization + Keeper Task #358 + Decision B sequence after step 10. FRAMEWORK grade with substantive math-object formalization. Substrate quiver = (36 K-type vertices + ~774 main arrows + 468 fiber arrows) with 10-commutator relation ideal R; canonical representation IS Bergman H²(D_IV⁵). Multi-phase decomposition Q = Q_DIRECT ⊕ Q_COMPOSITION ⊕ Q_MATERIAL ⊕ Q_COMBINATORIAL; phase-specific relations encode substrate operational regions. Multi-week v0.3+ computation path identified. Cal Thread 4 type-check queued for Type-C level-crossing prior.
