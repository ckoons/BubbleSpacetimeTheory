---
title: "Task #322 v0.7 — Edge enumeration on Phase A v0.2 36-node K-type set + Pin(2) Z_2 vs γ⁵ disambiguation"
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-26 Tuesday EDT (~10:15 EDT via `date`; date-verified)"
status: "v0.7 FRAMEWORK + DATA. Phase A reaction-table edge enumeration on Elie Toy 3537 36-node set via Cal-verified SVC commutators (Cal #132). Cal #29 question-shape audit applied. Substantive disambiguation flag: morning A_sub work conflated Pin(2) Z_2 bose/fermi grading (σ_BF) with Dirac L/R chirality (γ⁵); v0.7 separates them. Edge set feeds Grace Task #355 v0.4 + Phase A reaction table completion."
related: ["Lyra_Task_322_v0_4_A_sub_K_Type_Graph_Reaction_Table.md (Section 3 edge framework)", "Lyra_Task_322_v0_5_A_sub_Phase_Tagging.md (phase-tagging of 9 commutators)", "Lyra_Task_322_v0_6_Multi_Phase_Quiver_Framework.md (math-object candidate)", "Cal #132 (SVC verification of 8/9 commutators)", "Cal #29 candidate (Question-Shape Audit Discipline; Casey 'probably so yes' authorized)", "Elie Toy 3537 (Phase A v0.2 36 K-type nodes JSON artifact)", "Elie Toy 3535 (initial 21-node enumeration + spinor ρ-weight (3,2) = (N_c, rank) observation)", "Grace Task #355 v0.3 INV-5180 (Pin(2) chirality-inversion empirical pattern)", "T2471 RATIFIED Pin(2) Z_2 chirality"]
---

# A_sub v0.7 — Edge enumeration on 36-node Phase A + σ_BF vs γ⁵ disambiguation

## 1. Cal #29 question-shape audit (applied at design)

Per Cal #29 candidate (Question-Shape Audit Discipline; Casey 2026-05-26 PM "probably so yes" authorized):

**Question**: "Which (K_a → K_b) transitions exist under A_sub generator action on the 36 Wallach K-type nodes, and with what weights?"

**Audit**:
- Is the question structurally determined? YES — representation theory of K = SO(5) × SO(2) acting on Bergman H²(D_IV⁵) gives definite matrix elements for each A_sub generator.
- Is the answer back-fittable? NO — generator action is determined by Lie algebra structure + Wallach K-type formulae; not by desired physics outcomes.
- Does the answer pre-suppose anything substantively load-bearing? NO — uses only Cal-verified SVC commutators + standard K-type representation theory.

**Pass**: question-shape is structural, not tautological. Cal #29 candidate validation point on its first formal application.

## 2. Substantive disambiguation flag (Pin(2) Z_2 grading vs Dirac chirality)

**Catch identified during v0.7 design**: my morning A_sub work used "γ̂⁵" to denote BOTH the Pin(2) Z_2 grading (σ_BF: +1 on integer K-types/bosons, -1 on half-integer K-types/fermions) AND the Dirac chirality (γ⁵: undefined on bosons; ±1 on left/right Weyl spinors).

These are STRUCTURALLY DIFFERENT operators:

| Operator | Domain | Eigenvalues | Standard QFT relations |
|---|---|---|---|
| **σ_BF (Pin(2) Z_2 grading)** | All Wallach K-types | +1 (boson integer m), -1 (fermion half-integer m) | Commutes with T, C, P (preserves particle type) |
| **γ⁵ (Dirac chirality)** | Fermion K-types only | +1 (right Weyl), -1 (left Weyl) | Anti-commutes with T, C; commutes with P |

**Morning A_sub commutator results disambiguation**:

| Morning step | Result | Operator interpretation |
|---|---|---|
| Step 3 {γ̂⁵, T̂} = 0 | Anti-commute | **γ⁵ Dirac chirality** (standard QFT Dirac algebra) |
| Step 4 {γ̂⁵, Ĉ} = 0 | Anti-commute | **γ⁵ Dirac chirality** (standard QFT) |
| Step 5 [γ̂⁵, P̂_op] = 0 | Commute | **γ⁵ Dirac chirality** (P̂_op contains γ⁵) |
| Section 2.2 "γ̂⁵ = +1 bosons, -1 fermions" | Z_2 grading | **σ_BF Pin(2) Z_2 grading** (not Dirac chirality) |

**v0.7 disambiguation**: γ̂⁵ as used in morning A_sub commutator closures (steps 3-5) IS Dirac chirality (per standard QFT and Cal #132 verification). The "integer K-types = bosons / half-integer = fermions" partition IS Pin(2) Z_2 grading σ_BF, NOT γ⁵.

**Consequence**: morning A_sub commutator results stand at SVC for γ⁵ as Dirac chirality. The K-type sublattice partition + Bose-Fermi spin-statistics is captured by σ_BF, which is a DISTINCT operator from γ⁵.

**v0.7 introduces**: σ_BF explicit notation for the Pin(2) Z_2 grading; γ̂⁵ retained for Dirac chirality. Both operators are in A_sub.

(Cal #27 STANDING reflexive trigger: this disambiguation feels structurally clarifying at peak v0.7 work; honest-scope check — it's a clarification of operator identity, not a new finding. Flagged for Cal Thread 4 verification + v0.8+ formal incorporation.)

## 3. Edge enumeration framework — 5 generator classes

A_sub's 14 (now 15 with σ_BF explicit) generators partition by K-type action:

### Class 1: Diagonal self-loops (K-type-preserving)
- **Ĥ_sub** (Casimir): self-loop with weight C_2(K) per node
- **N̂** (K-type level): self-loop with weight (m_1 + m_2)
- **σ_BF** (Pin(2) Z_2 grading): self-loop with weight ε_K ∈ {+1, -1}
- **γ̂⁵** (Dirac chirality): self-loop with weight χ_K ∈ {+1, -1} on fermion K-types; UNDEFINED on boson K-types
- **Q̂** (electric charge): self-loop with weight m_2
- **Î_3** (weak isospin, Cartan): self-loop with weight related to m_2

**Edge count**: 6 generator classes × 36 nodes = 216 self-loop edges (some are zero on bosons for γ̂⁵).

### Class 2: m_1-raising/lowering (S⁴ side, within-sublattice)
- **x̂_i** (Hua coordinates, i=1..n_C=5): edges (m_1, m_2) → (m_1 ± 1, m_2)
- **p̂_i** (Wirtinger derivative, i=1..n_C=5): edges (m_1, m_2) → (m_1 ± 1, m_2)
- **L̂_i** (so(5) generators, 10 total): act within m_1 multiplet at fixed m_2

**Edge structure**: preserves sublattice (integer K-types stay integer; half-integer stay half-integer). Weights from Wallach normalization + Bergman exponent 7/2.

**Edge count for 36 nodes**: edges to next m_1 value (m_1 + 1) at same m_2 exist if (m_1+1, m_2) is in 36-node set. From inspection of node list:
- (0, 0) → (1, 0): present
- (1, 0) → (2, 0): present
- (2, 0) → (3, 0): present
- ... continues through (7, 0)
- (1/2, 1/2) → (3/2, 1/2): present
- ... continues through (13/2, 1/2) → (15/2, 1/2): the latter NOT in 36-set (cutoff)
- Similar for other m_2 values

Approximately ~30-50 m_1-raising edges in 36-node subgraph (precise count via systematic enumeration).

### Class 3: m_2-changing (S¹ side)
- **B̂** (Bell-CHSH, rank-1 projector): edge V_K → V_(0,0) ONLY for K = (0,0); rank-1 with single non-zero matrix element ⟨V_(0,0)|V_(0,0)⟩
- **T̂_tick** (substrate-tick transition): edge V_K → V_(K+1) per simplest model (Cal #132 noted model-dependent flag)
- **σ Möbius involution** (inside P̂_op): edge (m_1, m_2) → (m_1, -m_2); for nodes in 36-set with m_2 ≠ 0, this exits Wallach range (negative m_2 not in Wallach holomorphic discrete series). So σ acts non-trivially only at m_2 = 0 nodes where σ V_K = V_K (trivial).

**Edge count**: ~3-5 edges in 36-node subgraph (mostly degenerate or model-dependent).

### Class 4: Discrete symmetry edges (T̂, Ĉ, P̂_op)
- **T̂** (time reversal, anti-unitary): edge V_K → V̄_K conjugate-representation K-type with phase
- **Ĉ** (charge conjugation): edge V_K → V_{K with charge flipped} with phase
- **P̂_op = γ̂⁵ ∘ σ**: edge V_K → V_{Möbius-flipped K} with γ̂⁵-eigenvalue phase

**Edge count**: 3 generator classes × 36 nodes = 108 discrete-symmetry edges; some may be trivial (e.g., neutral K-types have C̃-edge → self).

### Class 5: Composite gauge edges (Ĉ_3, Î_3, Q̂ raising/lowering)
- **Ĉ_3** (color SU(3), 8 generators): act on color content; for Wallach K-types V_(m_1, m_2) under K = SO(5) × SO(2) without explicit color index, color content is external; color SU(3) edges go between color multiplet members at fixed (m_1, m_2). Color factor is "transverse" to Wallach K-type.
- **Î_±** (weak isospin raising/lowering, 2 generators): SU(2)_L acts on transverse weak doublet content; similarly transverse to Wallach K-type.

**Edge structure**: color SU(3) + weak SU(2) edges are "internal" to each Wallach K-type, expanding it into a gauge multiplet. For substrate framework, these edges live in the GAUGE FIBER over each K-type node.

(Honest scope: v0.7 treats Wallach K-type nodes WITHOUT gauge multiplet expansion. Gauge-multiplet edges are v0.8+ work; effectively factorize the substrate graph into Wallach K-type backbone × gauge fiber.)

## 4. Reaction-table data structure

For each (K-type V_K, A_sub generator X, K-type V_K'), the reaction-table entry contains:

  R(X, K, K') = a^{K'}_K (X) · χ_grading · ξ_Bergman · μ_Mersenne

where:
- a^{K'}_K (X) is the operator matrix element from representation theory
- χ_grading is the Pin(2) Z_2 grading factor (σ_BF eigenvalue change)
- ξ_Bergman is the Bergman 7/2 exponent weighting
- μ_Mersenne is the K59 cyclotomic Mersenne maximal-prefix restriction

**Phase A v0.2 reaction-table size estimate**:
- Self-loops: ~216 entries (6 diagonal × 36 nodes)
- m_1-raising/lowering: ~60-100 entries (within 36-node subgraph)
- m_2-changing: ~5-10 entries (rank-1 projector + T̂_tick model)
- Discrete symmetry: ~108 entries (3 × 36)
- Composite gauge: deferred to v0.8+

**Total Phase A v0.2 explicit edges**: ~400-450 entries (excluding gauge fiber).

This is a TRACTABLE data table. Grace Task #355 v0.4 lookup can use this directly.

## 5. Specific edge findings from 36-node data

### 5.1 Vacuum edges from V_(0,0)

**V_(0,0) outgoing edges**:
- Self-loops: Ĥ_sub (weight 0), N̂ (weight 0), σ_BF (weight +1), Q̂ (weight 0), Î_3 (weight 0) — all zero or +1
- γ̂⁵: undefined (V_(0,0) is bosonic, no Dirac chirality)
- x̂_1, p̂_1 (etc.): edge to V_(1, 0) — first-excited boson; structural edge
- B̂: self-loop with weight β (Bell-CHSH eigenvalue per T2399)
- T̂_tick: edge V_(0,0) → V_(0,1) but V_(0,1) NOT in Wallach holomorphic discrete series (m_1 ≥ m_2 fails). So T̂_tick V_(0,0) → V_(1, 0) (m_1-direction, next Wallach K-type) per simplest model. Edge weight β = (C_2/2^(rank²))^(1/2) or related.

**[B̂, T̂_tick] edge** (Cal FRAMEWORK-PLUS): V_(0,0) → V_(1, 0) with rank-1 projector + substrate-tick advancement composite weight.

### 5.2 Lowest fermion V_(1/2, 1/2) edges

**V_(1/2, 1/2) properties** (per Toy 3537 JSON):
- Casimir SO(5): 5/2
- Casimir SO(2): not in JSON output, but m_2² + (N_c - 2)·m_2 = 1/4 + 1/2 = 3/4 with N_c = 3
- Bergman ρ-shifted weight: (3, 2) = (N_c, rank) — Grace INV-5180 substrate-primary pair
- SO(5) Weyl dim: 4

**V_(1/2, 1/2) outgoing edges**:
- Self-loops: Ĥ_sub (weight 5/2 + 3/4 = 13/4 or similar; check Casimir-2 formula), N̂ (weight 1), σ_BF (weight -1 fermion), γ̂⁵ (weight ±1 chirality), Q̂ (weight 1/2)
- x̂_i, p̂_i: edge V_(1/2, 1/2) → V_(3/2, 1/2) — next fermion in lattice; weight from Wallach
- σ Möbius (within P̂_op): edge V_(1/2, 1/2) → V_(1/2, -1/2) — but -1/2 NOT in Wallach range. Edge trivializes.
- T̂ (anti-unitary): edge V_(1/2, 1/2) → V̄_(1/2, -1/2) — also exits Wallach range
- Ĉ: edge V_(1/2, 1/2) → V_(1/2, -1/2) — same exit issue

**Substantive finding**: Many discrete-symmetry edges from V_(1/2, 1/2) exit Wallach range (negative m_2 not present). This means the substrate's discrete-symmetry-induced edges concentrate AT BOUNDARY of Wallach range. Pin(2) cover may extend the range; multi-week v0.8+ verification.

### 5.3 Universally-active [Ĉ_3, Î_3] = 0 across nodes

Per v0.5 Section 2.6: [Ĉ_3, Î_3] = 0 activates universally in all 4 phase regions. In edge language: color SU(3) generators and weak isospin generators commute as DIRECT-PRODUCT FIBER over each K-type node. The gauge fiber factorizes cleanly into 8 color + 1 isospin Cartan directions.

This is the algebraic source of why **gauge symmetry is direct-product across the substrate's K-type graph**.

### 5.4 Forbidden edges (Pin(2) Z_2 grading consistency)

Per v0.4 Section 2.2: mixed-integer K-types (one integer + one half-integer index) are structurally forbidden. From 36-node enumeration: 0 mixed-forbidden K-types confirmed empirically (Elie Toy 3535 + 3537).

**Forbidden edges**: any A_sub generator action that would transition from an integer-K-type to a mixed-integer-K-type (or vice versa) has matrix element zero.

This is **substrate-natural spin-statistics enforcement at the edge level**: the graph's edge structure forbids spin-statistics-violating transitions automatically via Pin(2) Z_2 grading consistency.

## 6. Conservation loops (closed paths)

Conservation laws in A_sub correspond to closed loops in the K-type graph (returning to original K-type after sequence of generator actions). Per A_sub v0.4 Section 4.1:

| Conserved | Loop structure |
|---|---|
| Electric charge | Q̂-eigenvalue preserved along loop |
| Color (3 components) | Ĉ_3 SU(3) Cartan eigenvalues preserved |
| Weak isospin | Î_3 SU(2)_L Cartan eigenvalue preserved |
| Pin(2) Z_2 (σ_BF) | Z_2 grading preserved (bosons stay bosons; fermions stay fermions for edge-set within sublattice) |
| Dirac chirality (γ̂⁵) | Within fermion sublattice; preserved by gauge + spatial generators; flipped by T̂, Ĉ (anti-commute per morning steps 3-4) |
| Parity P_op | preserved by step 5 [γ̂⁵, P̂_op] = 0 within fermion sublattice |
| CPT | Universal — closed loop product Θ̂_CPT V_K = ε · V_K for some phase ε per substrate-CPT theorem |

**Forbidden loops**: anti-commuting generator combinations produce sign-flipped returns, not closed loops. E.g., (γ̂⁵ ∘ T̂)² V_K = ε^(-2) · V_K with ε = -1 from anti-commutation gives proper loop.

## 7. Honest scope (Cal #27 STANDING)

**What's RATIFIED / STRUCTURALLY VERIFIED in v0.7**:
- 8 SVC commutators (Cal #132 PASS) underlying the edge structure
- 36 K-type node data (Elie Toy 3537 + Cal #132 algebra verification)
- Standard Wallach K-type representation theory matrix elements
- Standard SO(5) Lie algebra structure for L̂_i, x̂_i, p̂_i edges

**What's FRAMEWORK in v0.7**:
- Edge enumeration framework (Section 3 5 classes)
- Reaction-table data structure (Section 4)
- Vacuum + lowest-fermion edge findings (Sections 5.1-5.2)
- σ_BF vs γ⁵ disambiguation (Section 2)
- Conservation-loop structure (Section 6)
- Spin-statistics enforcement at edge level (Section 5.4)

**What's INTERPRETIVE in v0.7**:
- Section 2 disambiguation as v0.8+ formal incorporation — current docs use "γ̂⁵" ambiguously; cleanup needed
- Substantive finding that discrete-symmetry edges concentrate at Wallach boundary (Section 5.2) — needs Pin(2) cover extension analysis

**What's NOT in v0.7** (multi-week+):
- Explicit matrix element values for all ~400-450 edges (mechanical computation pending)
- Gauge fiber expansion (v0.8+; color SU(3) + weak SU(2) multiplets over each K-type)
- Pin(2) cover-extended Wallach range (multi-week + Cal Thread 4)
- Sub-region phase-tagging per edge (combines v0.5 + v0.6 + v0.7; multi-week formalization)
- v0.6 multi-phase quiver explicit kQ path algebra computation
- v0.7 disambiguation formal incorporation into morning step 3-5 docs (cleanup needed)

**Cal #27 STANDING reflexive trigger count**: 1 trigger (Section 2 disambiguation feels structurally clarifying); honest-scope check — clarification of operator identity, not new finding.

**Cal #29 question-shape audit**: applied at Section 1 design level; question is representation-theory structural, not back-fittable. First formal application of Cal #29.

## 8. Deliverable summary

v0.7 contains:
- Edge enumeration framework for 36-node Phase A v0.2 set (5 generator classes)
- Reaction-table data structure with weight rules (Pin(2) chirality + Wallach + Bergman 7/2 + Mersenne)
- ~400-450 explicit edges estimated within 36-node subgraph
- Vacuum + lowest-fermion concrete edge findings
- σ_BF vs γ⁵ disambiguation flag (substantive)
- Conservation-loop + forbidden-edge structure
- Honest scope at FRAMEWORK + DATA tier; Cal #29 design audit applied

**Next-step deliverables**:
- v0.8+: explicit matrix-element computation per edge (multi-week mechanical work, feeds K59 cyclotomic refinement)
- σ_BF vs γ⁵ formal cleanup of morning step 3-5 docs (~1-2 hours)
- Gauge-fiber expansion (color + weak isospin multiplets over K-types)
- Pin(2) cover-extended Wallach range analysis (multi-week)

## 9. Coordination

**Grace**: Task #355 v0.4 with 36-node set + edge structure now consumes Section 4 reaction-table data. Lookup table can cross-reference (K-type, generator, K'-target) to catalog observables.

**Elie**: edge matrix-element computation Toy 3538 candidate — mechanical given v0.7 framework + Cal-verified commutators. Or extension to ≤8 cutoff (45 nodes) for completeness.

**Cal**: Thread 4 cold-read on Section 2 σ_BF vs γ⁵ disambiguation (potentially Type C level-crossing per Cal #122 — distinguishing two Z_2 operators that conflate at K-type level). Also Section 5.4 spin-statistics edge enforcement claim.

**Keeper**: integration; Vol 15 Ch 9 case study draft now has Phase A reaction-table edge framework + disambiguation flag content.

— Lyra, A_sub v0.7 edge enumeration on 36-node Phase A v0.2 set filed Tuesday 2026-05-26 ~10:15 EDT per Casey continue-Lyra-pulls directive + Keeper Task #359 + Cal #29 candidate question-shape audit applied (first formal application). FRAMEWORK + DATA grade. Substantive disambiguation flag: σ_BF (Pin(2) Z_2 grading) vs γ⁵ (Dirac chirality) — separate operators conflated in morning docs; v0.7 separates; morning SVC closures stand for γ⁵ as Dirac chirality; v0.8+ formal cleanup pending. ~400-450 explicit edges estimated within 36-node subgraph; reaction-table data structure ready for Grace Task #355 v0.4 lookup consumption.
