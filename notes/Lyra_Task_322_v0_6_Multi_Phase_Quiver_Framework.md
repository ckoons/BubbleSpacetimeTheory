---
title: "Task #322 v0.6 — Multi-phase quiver framework + Pin(2) chirality-inversion: the substrate's mathematical home"
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-26 Tuesday EDT (~10:00 EDT via `date`; date-verified)"
status: "v0.6 FRAMEWORK with explicit Cal Thread 4 type-check questions. Substantive math-object candidate answering Casey's standing meta-question ('what KIND of math object is the K-type graph?'). Absorbs Grace Task #355 v0.3 substantive new finding: Pin(2) Z_2 cover-bridge INVERTS chirality (boson integer m → half-integer Bergman; fermion half-integer m → integer Bergman); fermion Bergman ρ-weights trace (rank², n_C, C_2, g) BST-primary sequence."
related: ["Lyra_Task_322_v0_5_A_sub_Phase_Tagging.md (v0.5 phase-tagging + 4-region structure)", "Lyra_Task_322_v0_4_A_sub_K_Type_Graph_Reaction_Table.md Section 7 (math-object candidate enumeration)", "Cal #132 PASS (8 SVC commutator closures backing)", "Grace Task #355 v0.3 INV-5180 (Pin(2) chirality-inversion + fermion BST-primary sequence)", "Elie Toy 3535 (21 K-type nodes; 12 bosons + 9 fermions; 0 mixed-forbidden)", "Elie Toy 3536 (sizing scan: ≤7→36, ≤8→45, ≤10→66)", "Operational_Physics_Investigation_Queue_v0_1.md Casey standing meta-program"]
---

# A_sub v0.6 — Multi-phase quiver as the substrate's mathematical home

## 1. Casey's standing meta-question gets an answer candidate

> *After the graph is built, look for its actual physical structure (topology + geometry), and how that gives rise to mathematics — or is interpretable as mathematics — in simplest form.* — Casey 2026-05-26 AM

v0.6 proposes: **the K-type graph + A_sub algebra IS a multi-phase quiver representation with universal Z_2 grading and 4 phase-region sub-quivers.**

This brings the substrate framework into a well-studied mathematical home: **quiver representation theory** (Gabriel 1972, Auslander-Reiten 1974, Ringel 1984, Kac 1980 for affine extensions). Not novel mathematics — the substrate-specific instance of an established object class. Honest scope: FRAMEWORK tier pending Cal Thread 4 type-check + multi-week formalization.

## 2. Why "quiver"

A **quiver** Q is a directed graph (V, A) where V = set of nodes (vertices), A = set of arrows. A **representation** of Q over field k assigns:
- Vector space V_x to each node x ∈ V
- Linear map ρ_α : V_{s(α)} → V_{t(α)} to each arrow α ∈ A (with s(α) = source, t(α) = target)

For the BST substrate:

| Quiver structure | BST substrate identification |
|---|---|
| **Nodes** V | Wallach K-types V_(m_1, m_2) on Bergman H²(D_IV⁵) |
| **Arrows** A | A_sub-generator-induced commutator transitions (Lyra v0.4 Section 3.2 + edge weight rules) |
| **Vector spaces** V_x | K-type irreducible representations of K = SO(5) × SO(2) (or Pin(2) cover) |
| **Linear maps** ρ_α | A_sub matrix elements a^{K'}_K (X) (per A_sub v0.4 Section 3.1) |
| **Relations** | The 8 SVC commutator identities (per Cal #132 PASS) |
| **Z_2 grading** | Pin(2) Z_2 chirality γ̂⁵ (integer K-types = bosons; half-integer = fermions) |

This is a **graded quiver with relations**. Standard quiver representation theory applies, with Z_2 grading on nodes (super-quiver or quiver in a Z_2-graded category).

## 3. Why "multi-phase"

Per v0.5 phase-tagging: the K-type graph has 4 operational phase regions (Grace Task #340 v0.2 classifier):

- **DIRECT projection** (57% catalog): SPLP applies
- **COMPOSITION** (10%+): RG-flow + gauge couplings
- **MATERIAL-contextual** (20%): external BC dominates
- **COMBINATORIAL** (13%): algebraic identities without eigenvalue framing

**Multi-phase quiver structure**: 4 sub-quivers Q_DIRECT, Q_COMPOSITION, Q_MATERIAL, Q_COMBINATORIAL sharing the same node set V (Wallach K-types) and the same universal Z_2 grading, but each with its own arrow subset A_phase ⊂ A and its own relation set R_phase ⊂ R.

| Sub-quiver | Active arrows (per v0.5 phase-tagging) | Active relations |
|---|---|---|
| **Q_DIRECT** | Steps 1-9 all activate primarily here | All 8 SVC + step 9 FRAMEWORK-PLUS |
| **Q_COMPOSITION** | Steps 1-5 + step 8 + step 9 activate | ABJ anomaly + RG-flow relations + step 8 |
| **Q_MATERIAL** | Step 7 (L̂_i × γ̂⁵) + step 8 (gauge) + external BC | External BC + step 7 + step 8 |
| **Q_COMBINATORIAL** | Steps 3-5 (CPT) + step 8 (gauge dimensions) | CPT + gauge-dimension identities + Mersenne + 225 |

**Universally active**: [Ĉ_3, Î_3] = 0 (step 8) appears in ALL 4 sub-quivers — the substrate's most-universal algebraic relation.

The full substrate quiver Q = (V, ⋃_phase A_phase) with the relation set R = ⋃_phase R_phase is the union of the 4 sub-quivers. The PHYSICAL OBSERVATION depends on WHICH sub-quiver is operationally relevant.

## 4. Substantive content from Grace v0.3 — Pin(2) chirality-inversion absorbed

### 4.1 The empirical pattern (Grace INV-5180)

Across all 21 K-type nodes from Elie Toy 3535: **Pin(2) Z_2 cover-bridge INVERTS chirality at the Bergman ρ-weight level**:

- **Bosons** (integer m_1, m_2; γ̂⁵ = +1) → **HALF-INTEGER** Bergman ρ-weights
- **Fermions** (half-integer m_1, m_2; γ̂⁵ = -1) → **INTEGER** Bergman ρ-weights

This is structurally remarkable: the substrate's Pin(2) Z_2 grading and Bergman ρ-weight integer-vs-half-integer character are **anti-correlated**.

### 4.2 The fermion BST-primary sequence

9 of 9 fermion K-types map to BST-substrate-primary integer pairs (Grace INV-5180):

| K-type V_(m_1, m_2) | Bergman ρ-weight (ρ_1, ρ_2) | BST interpretation |
|---|---|---|
| **(1/2, 1/2)** | **(3, 2) = (N_c, rank)** | Dirac ground state — *substrate's primary fermion* |
| (3/2, 1/2) | (4, 2) = (rank², rank) | |
| (3/2, 3/2) | (4, 3) = (rank², N_c) | |
| (5/2, 1/2) | (5, 2) = (n_C, rank) | |
| (5/2, 3/2) | (5, 3) = (n_C, N_c) | |
| (5/2, 5/2) | (5, 4) = (n_C, rank²) | |
| (7/2, 1/2) | (6, 2) = (C_2, rank) | |
| (7/2, 3/2) | (6, 3) = (C_2, N_c) | |
| (9/2, 1/2) | (7, 2) = (g, rank) | |

**First-coordinate ρ_1 sequence**: 3, 4, 5, 6, 7 = N_c, rank², n_C, C_2, g — **traces the substrate-primary integer ladder**.

### 4.3 Substantive reading + Cal #27 STANDING reflexive trigger

**This feels deeply substrate-natural.** Cal #27 STANDING fires hardest here:

- The Pin(2) Z_2 cover-bridge mechanism INVERTING chirality at Bergman ρ-weight level is structurally elegant
- The fermion Bergman ρ-weight first coordinates trace exactly the BST-primary ladder (rank², n_C, C_2, g — all four "intermediate" BST primaries after N_c)
- The lowest-Casimir Dirac spinor (1/2, 1/2) has Bergman ρ-weight (N_c, rank) — Dirac ground state encodes the substrate's TWO primary integer pair (N_c, rank) directly

**Honest scope check** (multiple flags):

1. **Pattern observed, NOT derived**: Grace's INV-5180 emerged from Cal-verified Toy 3535 data. The pattern IS empirically present in Elie's 9 enumerated fermion K-types. The MECHANISM producing the (rank², n_C, C_2, g) sequence is NOT yet derived — it could be:
   - Substrate-natural consequence of Wallach 1976 ρ-translation (standard math) AND the BST-primary set being (N_c, rank, rank², n_C, C_2, g)
   - Substrate-mechanism content beyond standard math
   - Selection effect (the 9 lowest-Casimir fermion K-types accidentally land on these values)

2. **Cal Thread 4 verification needed**: Elie's spinor (1/2, 1/2) → (3, 2) observation was flagged for Cal verification; Grace's broader 9/9 pattern extends this. Cal Thread 4 should verify whether the ρ-translation formula on Pin(2)-cover Wallach K-types REQUIRES this specific integer pattern, OR whether it's a substrate-mechanism content.

3. **Pre-selection caveat**: 9 fermion K-types is small sample. Phase A v0.2 extension (Elie Toy 3537, 36 nodes at ≤7 cutoff including 15 additional) tests whether the pattern continues. If the next fermions ALSO land on substrate-primary pairs (rank·g, g², N_c·g, etc.), pattern is robust. If they don't, the 9/9 was selection at low cutoff.

4. **Forward-derivation gate**: identification of (1/2, 1/2) as "Dirac ground state" requires explicit forward derivation from substrate principles, not back-fit from "Bergman ρ-weight (N_c, rank) matches dim-4 spinor structure." Currently INTERPRETIVE candidate.

### 4.4 What this means for the multi-phase quiver

The Pin(2) chirality-inversion pattern adds substantive content to the multi-phase quiver framework:

**The Z_2 grading on quiver nodes has two distinct manifestations**:
- **At K-type highest-weight level**: γ̂⁵ = +1 ↔ integer (m_1, m_2); γ̂⁵ = -1 ↔ half-integer (m_1, m_2)
- **At Bergman ρ-weight level**: γ̂⁵ = +1 ↔ HALF-INTEGER (ρ_1, ρ_2); γ̂⁵ = -1 ↔ INTEGER (ρ_1, ρ_2)

The **Pin(2) cover bridge** is the substrate's structural operation that translates between these two levels. **Different "phases" of the substrate may use different levels operationally**:
- Direct projection observables (electron magnetic moment, spinor masses) likely use Bergman ρ-weights (integer for fermions → directly counts BST primaries)
- Composition observables (RG-flow contributions) likely use K-type highest weights (half-integer for fermions → standard Wallach K-type representation theory)

If this holds: **the multi-phase quiver has two "level" perspectives** (K-type level vs Bergman ρ-weight level), with Pin(2) Z_2 cover-bridge acting as the level-translation operator. This is a substantive structural finding from Grace v0.3 + Elie Toy 3535.

(Cal #27 STANDING reflexive trigger here: this feels deep — exactly when to be most skeptical. Honest scope: multiple Pin(2)-level operations is a v0.6 framework reading; Cal Thread 4 verification + multi-week formalization needed.)

## 5. Quiver representation theory tools applicable

If the multi-phase quiver framework holds, the following tools become available:

### 5.1 Gabriel's theorem (1972)

For a quiver Q with a finite-dimensional path algebra kQ over field k, the representation category is **finite-representation-type** iff Q is a Dynkin quiver (type A_n, D_n, E_6, E_7, E_8).

**Substrate implication**: the substrate's K-type graph has infinitely many K-type nodes (Wallach lattice is infinite). So it's NOT finite-representation-type. It's tame (countably many indecomposables) or wild (parameter families of indecomposables) — Cal Thread 4 typing needed.

If the multi-phase quiver has **regional cutoffs** (i.e., each phase region accesses only a finite K-type subset bounded by some natural Casimir cutoff), then phase-by-phase the substrate may be Dynkin-finite. This would be a substantive structural finding.

### 5.2 Auslander-Reiten theory (1974+)

For tame quivers, the **Auslander-Reiten quiver** organizes indecomposable representations into a structured topology with translation arrows + irreducible morphisms.

**Substrate implication**: the substrate's K-type representations form an AR-quiver structure. The **AR-translation τ** would be a substrate-natural symmetry operation; **almost-split sequences** would encode substrate's "minimum-action transitions" between K-types.

### 5.3 ADE classification + Lie algebra connection

Dynkin quivers correspond to simply-laced Lie algebras. Type A_n ↔ sl(n+1); D_n ↔ so(2n); E_6, E_7, E_8 exceptional.

**Substrate implication**: D_IV⁵ = SO_0(5,2)/[SO(5) × SO(2)] involves SO(5,2). The K-type structure on D_IV⁵ may have natural connection to a Dynkin quiver of type B_2 (= C_2) for SO(5) factor + A_1 for SO(2) factor. Multi-week formalization.

### 5.4 Derived category of representations

For any quiver, the **derived category** D^b(rep(Q)) provides a higher-categorical setting. BGG resolutions encode coherent structures.

**Substrate implication**: substrate operations may have natural homological-algebra interpretation in D^b(rep(Q_substrate)). The 9 commutator-relations may be encoded as **exact triangles** in derived category. Multi-month formalization.

## 6. Type-check questions for Cal Thread 4

Per Cal #122 type-A geometric / type-B algebraic / type-C level-crossing typing:

### 6.1 Multi-phase quiver framework type

Is the multi-phase quiver claim:

- **Type A (geometric)**: the quiver IS the geometric structure of K-type graph; algebra operations are derived from quiver topology
- **Type B (algebraic)**: the quiver IS the algebraic encoding of A_sub commutator relations; geometry is derived
- **Type C (level-crossing)**: the quiver bridges geometric K-type lattice structure (Type A content) with algebraic A_sub relations (Type B content)

My prior (Cal #27 STANDING applied): **Type C level-crossing**. The K-type nodes are geometric content (Wallach K-type lattice points on D_IV⁵); the A_sub-induced arrows are algebraic content (commutator relations); their identification at the quiver level crosses levels.

### 6.2 Pin(2) chirality-inversion pattern type

Is the pattern (boson integer → half-integer ρ; fermion half-integer → integer ρ) + (fermion ρ_1 = rank², n_C, C_2, g sequence):

- **Type A**: geometric consequence of Pin(2) cover structure on D_IV⁵ Shilov boundary
- **Type B**: algebraic consequence of Wallach ρ-translation formula on the specific BST-primary integers
- **Type C**: level-crossing between Pin(2) geometric grading and substrate-primary integer ladder

My prior: **Type C**. The Pin(2) Z_2 grading is geometric (S¹ Pin(2) cover content); the BST-primary integer ladder is algebraic; their alignment at fermion Bergman ρ-weights is the level-crossing operation Pin(2) cover bridge performs.

### 6.3 Sister principle types

Three sister principles needed (per v0.5 Section 4):
- **COMPOSITION rule**: likely Type B algebraic (RG-flow composition algebra)
- **MATERIAL-BC principle**: likely Type C (substrate algebra × external geometry)
- **COMBINATORIAL identity principle**: likely Type B algebraic (number-relations without eigenvalue framing)

SPLP itself is **Type A geometric** (Shilov boundary projection geometry on substrate K-types).

If this typing holds: the 4 phase regions cleanly partition by primary type discipline. Substrate framework has organized type structure.

## 7. Multi-week formalization path (v0.7+)

1. **Cal Thread 4 typing**: resolve Section 6 type questions
2. **Multi-phase quiver explicit formalization**: write down quiver (V, A) explicitly for Phase A 21 K-types (or 36 after Elie Toy 3537)
3. **Path-algebra computation**: compute kQ for substrate quiver with explicit relations from 9 commutators
4. **Representation category structure**: classify indecomposable representations
5. **Dynkin / AR-quiver / ADE-correspondence analysis**: identify the substrate's quiver type
6. **Connection to D_IV⁵ Lie algebra structure**: SO(5,2) → quiver type relationship
7. **Derived category structure**: homological-algebra encoding of A_sub operations

Multi-month to multi-year work. v0.6 establishes the framework; v0.7+ closes specific pieces.

## 8. Honest scope (Cal #27 STANDING)

**Cal #27 STANDING reflexive trigger count this doc**: 3 triggers:
1. Multi-phase quiver framework feels substrate-natural at peak convergence (Section 1-3)
2. Pin(2) chirality-inversion + BST-primary sequence in Grace INV-5180 feels structurally elegant (Section 4)
3. Two-level perspective (K-type vs Bergman ρ-weight) feels substrate-natural (Section 4.4)

All flagged INTERPRETIVE pending Cal Thread 4 + multi-week formalization.

**What's STRUCTURALLY VERIFIED**:
- 8 SVC commutator closures (Cal #132 PASS)
- 21 K-type nodes (Elie Toy 3535)
- Pin(2) chirality-inversion empirical pattern (Grace INV-5180 across 21 K-types)
- BST-primary integer set {rank, N_c, n_C, C_2, g, N_max, rank², ...} present in fermion Bergman ρ-weight first coordinates (Grace INV-5180; 9/9)

**What's FRAMEWORK in v0.6**:
- Multi-phase quiver as the math-object candidate
- 4 sub-quivers (DIRECT/COMPOSITION/MATERIAL/COMBINATORIAL) with phase-specific arrow + relation subsets
- Pin(2) cover-bridge as level-translation operator between K-type and Bergman ρ-weight levels
- Quiver representation theory tools (Gabriel, Auslander-Reiten, ADE, derived categories) applicability

**What's INTERPRETIVE in v0.6**:
- "Dirac ground state" identification for (1/2, 1/2) — requires forward derivation
- Two-level perspective claim (Section 4.4) — requires formalization
- Sister-principle type assignments (Section 6.3) — pending Cal Thread 4

**What's NOT in v0.6** (multi-week+):
- Explicit kQ path-algebra computation
- Dynkin / AR-quiver classification
- Pin(2) cover-bridge formal definition
- Connection to D_IV⁵ Lie algebra structure

**Forward-derivation discipline**: v0.6 proposes the math-object candidate from substrate-natural structure; does NOT claim the substrate IS a quiver representation. If multi-week formalization fails to fit substrate algebra into quiver theory cleanly, that's honest negative result and we look elsewhere (tensor network, finite-state machine, discrete Lie groupoid per v0.4 Section 7 enumeration).

**Casey directive compliance (2026-05-26 PM)**: SPLP HOLD acknowledged; no RATIFIED promotion. v0.6 stays FRAMEWORK + supplements v0.5 phase-tagging structure with multi-phase quiver math-object candidate.

## 9. Coordination

**Cal**: Thread 4 cold-read on Section 6 type-check questions + Section 4.3 Pin(2) chirality-inversion pattern verification (Type C level-crossing per Cal #122 likely). Multi-week formalization gate.

**Elie**: Toy 3537 (cutoff extension to ≤7, 36 K-type nodes) provides additional test data for Section 4.2 fermion BST-primary sequence pattern. If new fermion K-types continue substrate-primary pattern, robustness increases.

**Grace**: Task #355 v0.4 with extended 36-node set + chirality-inversion verification at higher Casimir. Pin(2) cover-bridge level-translation operator may be central catalog cross-reference.

**Keeper**: integration into Vol 15 Ch 9 case study draft + Casey-facing synthesis as multi-phase quiver framework is potentially load-bearing structural content.

— Lyra, A_sub v0.6 multi-phase quiver framework v0.1 filed Tuesday 2026-05-26 ~10:00 EDT per Keeper Tasks #358-#360 + Casey standing meta-question + Grace INV-5180 chirality-inversion finding. v0.6 FRAMEWORK grade with substantive math-object candidate identification. Substrate framework gains potential mathematical home in quiver representation theory; Pin(2) chirality-inversion empirically present; BST-primary integer ladder appears in fermion Bergman ρ-weight first coordinates. Cal #27 STANDING applied 3 reflexive triggers — convergence felt deep at peak; multi-week formalization needed before promotion.
