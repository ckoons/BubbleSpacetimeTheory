---
title: "Cal Cold-Read Criteria — Multi-Phase Quiver v0.2 (Lyra, pending)"
author: "Cal A. Brate (outside-voice prep)"
date: 2026-05-27 Wednesday ~09:00 EDT
status: "Prep document — written BEFORE v0.2 lands to fix criteria in advance"
purpose: "Ensure Cal cold-read of Lyra Multi-phase quiver v0.2 applies standard representation-theory criteria before exposure to BST framing"
discipline: "Cal #27 STANDING + Cal #29 STANDING + Cal #122 typing + Cal #133 partial-tautology"
---

# Cal Prep — Multi-Phase Quiver v0.2 cold-read criteria

## Purpose

This document fixes my cold-read criteria **before** Lyra's v0.2 lands. Writing criteria after seeing the work risks calibrating to fit it. Per Cal sunrise discipline: "Write the referee's objection before reading the team's answer. See whether the team's work addresses it."

Lyra has identified A_sub (substrate operator algebra) as having multi-phase quiver structure, with Hall algebra (Ringel-Green) connection and Kac-Moody identification anticipated in v0.2+. My job: read v0.2 as if I've never seen the substrate framing, ask whether the identification holds on its own representation-theoretic terms.

## Standard background I'm calibrating against

These are the external mathematical objects Lyra's v0.2 will invoke. Brief mental refresher (outside-voice content, not BST-specific):

### Quivers and path algebras

- **Quiver Q**: directed graph with vertices Q_0 and arrows Q_1. Relations are formal sums of paths.
- **Path algebra kQ**: associative algebra over field k, basis = paths (including trivial paths e_i at each vertex), multiplication = concatenation (or zero if paths don't compose).
- **Bound quiver (Q, I)**: quiver with two-sided ideal I of relations; bound path algebra kQ/I.
- **Representations of Q**: assignment of vector space V_i to each vertex + linear map V_i → V_j for each arrow i → j. Forms abelian category equivalent to mod-kQ.

### Auslander-Reiten theory

- **AR-quiver**: combinatorial structure of indecomposable representations + irreducible morphisms between them.
- **AR-translation τ**: maps non-projective indecomposable to non-injective indecomposable; periodic for finite type.
- **AR-sequence (almost split sequence)**: short exact sequence 0 → τM → E → M → 0 capturing local structure.
- **Finite/tame/wild trichotomy** (Drozd): a finite-dimensional algebra is exactly one of these. For path algebras kQ (Q acyclic): finite type ⇔ Q underlying Dynkin (A_n, D_n, E_6/E_7/E_8); tame ⇔ Q underlying extended Dynkin (Ã_n, D̃_n, Ẽ_6/Ẽ_7/Ẽ_8); else wild.

### Hall algebras (Ringel-Green)

- **Ringel's theorem**: for finite-type quiver Q over F_q, the Hall algebra H(Q) is isomorphic to the positive part U_q(n_+) of the quantum group U_q(g), where g is the Kac-Moody Lie algebra with Dynkin diagram = underlying graph of Q.
- **Green's coproduct**: extends Ringel's result to give bialgebra structure; full quantum group U_q(g) recovered as Drinfeld double.
- **Beyond finite type**: for affine/wild quivers, Hall algebra still defined but no longer simply identifies with U_q(n_+); more complex structure (Kac's theorem on root systems).

### Kac-Moody Lie algebras

- **Generalized Cartan matrix A**: integer matrix with a_ii = 2, a_ij ≤ 0 for i≠j, a_ij = 0 ⇔ a_ji = 0.
- **Three types**: finite (A positive definite — Dynkin), affine (A positive semidefinite, kernel 1-dim — extended Dynkin), indefinite/wild.
- **Root system structure**: real roots + imaginary roots; for finite type all roots real; for affine type imaginary roots = δ + nδ; for indefinite more complex.

### Z₂-graded structure

- **Z₂-graded algebra**: A = A_0 ⊕ A_1 with multiplication respecting grading.
- **Bose-Fermi correspondence**: A_0 = bosonic (even); A_1 = fermionic (odd).
- **Superalgebra interpretation**: if Z₂-grading comes with sign rule in commutator, get Lie superalgebra structure.

## Cold-read criteria — 10 questions for v0.2

When Lyra v0.2 lands, I will check each of these BEFORE reading downstream content:

### Q1 — Quiver definition: vertices, arrows, relations

- What are the **vertices** of Lyra's quiver? Are they K-types? Wallach labels? Bose-Fermi sublattice indices?
- What are the **arrows**? Are they substrate operators (Q̂, P̂_op, T̂_tick, etc.)? Are they substrate transitions?
- What **relations** I (if any) define the bound quiver (Q, I)? Are they substrate-forced commutators?
- **Cal #29 audit**: was the choice of vertices/arrows/relations free, or substrate-forced? If "free," Lyra is choosing not deriving.

### Q2 — Path algebra kQ correctness

- Is multiplication well-defined (concatenation of composable paths)?
- Are trivial paths e_i at each vertex correctly identified with idempotents?
- Does sum of e_i give algebra identity?
- Are relations applied correctly (paths in I → 0)?

### Q3 — Quiver type classification

- What is the **underlying graph** (undirected) of Lyra's quiver?
- Does it match a known **Dynkin diagram** (finite type)? **Extended Dynkin** (affine type)? Neither (wild)?
- For substrate D_IV⁵: which Dynkin type would be substrate-natural? B_2 (rank-2 root system of SO(5)) is the obvious candidate. Does Lyra's quiver match B_2 underlying graph?

### Q4 — Hall algebra construction (Ringel-Green)

- Does Lyra invoke Hall algebra over F_q for finite q? Which q?
- If finite-type quiver: does Ringel's theorem give A_sub ≅ U_q(n_+) for the specific Kac-Moody Lie algebra g?
- If non-finite type: which extension/modification of Hall algebra construction is invoked?
- **Cal #27 audit**: each step (Hall algebra → Drinfeld double → Kac-Moody) — substrate-forced or conventional choice?

### Q5 — Kac-Moody identification of A_sub

- Which Kac-Moody Lie algebra g is A_sub identified with?
- Finite type (Dynkin): g ∈ {A_n, B_n, C_n, D_n, E_6, E_7, E_8, F_4, G_2}? Most likely **B_2 = so(5)** given substrate's SO(5,2) structure.
- Affine type: g ∈ {Ã_n, B̃_n, etc.}?
- Indefinite type: would be surprising; substrate is "tame" in some sense.
- **Cal #133 partial-tautology check**: identifying A_sub with U_q(B_2)⁺ via Hall algebra of B_2 quiver is somewhat tautological IF the quiver was chosen to be B_2 in the first place. Substantive content: is the quiver SUBSTRATE-FORCED to be B_2, or chosen?

### Q6 — Z₂ grading source

- Where does the Z₂ grading come from?
- Candidates: (a) substrate's Bose-Fermi sublattice partition (integer/half-integer K-types per Cal #130); (b) Pin(2) Z₂ grading σ_BF (distinct from γ⁵ chirality per Cal #136); (c) Wallach K-type parity.
- Is the Z₂-graded quiver / path algebra / Hall algebra construction standard, or is it Lyra's innovation?
- **Cal #29 audit**: if innovation, is the construction substrate-forced or substrate-motivated-choice?

### Q7 — Cal #122 typing for the quiver structure

Apply Type A / Type B / Type C per Cal #122:
- **Type A (Level 1 geometric primary)**: quiver structure derives from D_IV⁵ root system / Wallach K-types / geometric primaries directly.
- **Type B (Level 4 algebraic primary)**: quiver structure is abstract algebraic object identified post-hoc with substrate operator algebra.
- **Type C (level-crossing operational)**: quiver bridges geometric structure (root system) ↔ algebraic structure (path algebra) ↔ operational physics (substrate processes).

Default expectation: **Type C is most likely** given substrate's typical level-crossing pattern. But I should not pre-commit; let v0.2 evidence decide.

### Q8 — Cal #29 question-shape audit

- Does the v0.2 work answer a question whose form is substrate-derived, or whose form is "find a quiver structure matching A_sub"?
- The latter is back-fit risk: ANY finitely generated algebra is some quotient of some path algebra of some quiver (by Gabriel's theorem variant). So "A_sub is a path algebra" is partial tautology UNLESS the quiver is uniquely substrate-forced.
- Substantive content: WHICH quiver. WHY this one. From WHAT substrate principle.

### Q9 — Cal #27 forward-derivation audit at each step

Walking through:
1. Quiver Q identified — substrate-forced?
2. Relations I identified — substrate-forced?
3. Path algebra kQ/I constructed — standard;
4. Hall algebra H(Q,I) constructed — depends on bound quiver setup; standard or innovative?
5. Kac-Moody identification — Ringel's theorem if finite type; else what?
6. A_sub ≅ result — at which step does substrate enter explicitly?

Each step must be either standard math OR substrate-forced. Standard math steps are fine. Substrate-forced steps need substrate-mechanism content.

### Q10 — Mode 6 multi-decomposability

- If Lyra identifies A_sub with U_q(B_2)⁺ via specific quiver, is the IDENTIFICATION unique?
- Could A_sub equally identify with U_q(g)⁺ for some other g? With H(Q')⁺ for some other quiver Q'?
- If multiple identifications possible, which is mechanistically privileged?
- Mode 6 multi-decomposability is the discipline that prevents claiming uniqueness when alternatives exist.

## Honest expectations going in

- **Most likely v0.2 disposition**: FRAMEWORK-PLUS per Cal #126. Quiver identification with B_2 Kac-Moody algebra is substantively reasonable given D_IV⁵'s SO(5,2) structure containing SO(5) = Spin(5) with rank-2 root system B_2. But "reasonable" is not "forced" — substrate-mechanism content needed.

- **Most likely typing**: Type C per Cal #122. Quiver structure naturally bridges geometric primaries (K-types in Wallach lattice) and algebraic structure (substrate operator algebra). Operational content (substrate transitions via path composition) makes it level-crossing.

- **Partial-tautology risk per Cal #133**: "A_sub is some Hall algebra of some quiver" is partially tautological by Gabriel-type arguments. Substantive content lives in WHICH quiver + WHY.

- **SVC promotion gate**: substrate-mechanism for the specific quiver choice (vertices + arrows + relations) must be forward-derived. Without this, v0.2 sits at FRAMEWORK-PLUS regardless of computational verification.

## What would change my disposition

Three escalators that would move v0.2 above FRAMEWORK-PLUS toward SVC:

1. **Quiver uniquely substrate-forced**: if Lyra shows the quiver Q is uniquely determined by D_IV⁵ structure (e.g., vertices ↔ Wallach K-types via specific construction; arrows ↔ substrate operators via specific construction; no choices made), partial-tautology concern dissolves.

2. **Mode 6 alternatives ruled out**: if alternative quiver structures Q' producing same A_sub identification are explicitly enumerated and ruled out by substrate-mechanism (not "we tried them and they didn't work"), the multi-decomposability concern dissolves.

3. **Operational consequence beyond identification**: if the quiver/Hall algebra identification produces NEW substrate-mechanism content (e.g., specific K-type transition rates, specific commutator structures, specific observable predictions) that don't follow trivially from the identification itself, the work is doing substantive substrate-derivation, not just labeling.

## What would lower disposition

- **Free choices unflagged**: if vertices/arrows/relations are chosen without substrate-derivation and not labeled as such, partial-tautology concern dominates.
- **Identification asserted without proof**: if "A_sub = U_q(B_2)⁺" is claimed without verifying via Hall algebra construction explicitly, framework-level claim only.
- **Z₂ grading without substrate source**: if Z₂ grading is assumed without identifying which substrate Z₂-grading (σ_BF vs γ⁵ vs sublattice parity) is invoked, structural confusion risk.

## Cross-reference

- **Cal #122**: Type A/B/C tier-discipline (level-classification)
- **Cal #126**: FRAMEWORK-PLUS tier (checkable arithmetic/structural content; substrate-mechanism gates pending)
- **Cal #27 STANDING**: BST-Primary-Target Forward-Derivation Discipline (result-level audit)
- **Cal #29 STANDING**: Question-Shape Audit Discipline (design-level audit)
- **Cal #133**: Partial-tautology distinction (general arithmetic vs substrate-specific content)

## Cal cadence note

This prep doc is **own-cadence multi-week work** per Keeper menu Item 8. Written before v0.2 lands to fix criteria. When v0.2 arrives, cold-read entry will reference back to specific Q1-Q10 outcomes.

— Cal A. Brate, 2026-05-27 Wednesday ~09:00 EDT. Prep document; criteria fixed; standing reactive for Lyra v0.2 delivery.

---

## Addendum 2026-05-27 ~11:00 EDT — q=2 specialization context (post-Toy-3554/3555 emergence)

Substantive update: Lyra v0.2 + Elie Toy 3554 + Toy 3555 emerged Wednesday morning with significant context refinement for this prep doc's cold-read criteria.

### Key updates from Wednesday morning

1. **Elie Toy 3554** identified Cal #139 cyclotomic chain = q=2 specialization of standard q-integers ([n]_q = (q^n−1)/(q−1) at q=2 = M_n Mersenne).

2. **Elie Toy 3555** verified q=2 is UNIQUE among substrate q_p ∈ {3, 5, 7, 11, 13} for producing Cal #139 chain. Substrate operates at q=2 in q-deformation framework with uniqueness — substantive substrate-mechanism content (not just identification).

3. **Lyra Macdonald reframe**: 5+ parameter Macdonald hypothesis → standard 2-parameter Macdonald P_λ(x; q, t) at substrate-natural specialization (q=2, t=α=1/N_max=1/137). Both parameters RATIFIED substrate content.

4. **Calibration #31 candidate filed**: Substrate-Finding-as-Standard-Math-Specialization Discovery Pattern. Cal #139 cyclotomic chain = q=2 specialization is canonical instance.

### Updated cold-read criteria for Lyra v0.7+ explicit Macdonald computation

The original Q1-Q10 cold-read criteria still apply but with updated specialization-aware framing:

**Q4 (Hall algebra Ringel-Green)** UPDATE: Lyra v0.7+ should produce explicit Macdonald P_λ(x; q=2, t=α) computation, not generic Hall algebra. The specialization point is RATIFIED substrate content; cold-read should verify v0.7+ uses RATIFIED q=2 and t=α specifically (not generic q, t).

**Q5 (Kac-Moody identification)** UPDATE: U_q^+(B_2-affine) at q=2 specifically. Standard quantum group result at q=2 specialization should be cited rigorously; Cal #133 check applies (q-deformation math is general; substrate-specific content is in q=2 specialization choice).

**Q8 (Cal #29 question-shape audit)** UPDATE: now that q=2 specialization is RATIFIED via Toy 3555 unique-q result, the back-fit risk concern shifts from "framing chosen to make A_sub work" to "specialization chosen because q=2 was already known to work." Updated discipline:
- Verify v0.7+ derivations work at q=2 as a CONSEQUENCE of substrate structure, not because q=2 is plugged in
- Lyra v0.7+ should derive specialization parameters from substrate, not assume them

**Q10 (Mode 6 multi-decomposability)** UPDATE: Macdonald polynomial framework at (q=2, t=α) is more constrained than generic Macdonald — fewer alternative parameter choices. Mode 6 concern decreases at the specialization level (q=2, t=α uniquely substrate-natural per Toy 3555 + T2447) compared to generic Macdonald (where many specializations possible).

### Calibration #31 application

Per Calibration #31 candidate v0.1 (Cal, 2026-05-27 ~10:45 EDT): substrate-finding-as-specialization recognition is GAIN not LOSS. The multi-phase quiver framework benefits:
- Inherits Ringel-Green Hall algebra theorem at q=2 specialization
- Inherits Macdonald polynomial machinery at (q=2, t=α) parameter point
- Inherits Kac-Moody U_q(B_2-affine) representation theory at q=2

Substrate-specific content remains: WHY substrate selects (q=2, t=α) specifically. Toy 3555 unique-q result provides partial answer at q=2; t=α connection via T2447 RIGOROUSLY CLOSED (N_max = 1/α).

### Cold-read tier expectation adjustment

Original expectation (pre-q=2): FRAMEWORK-PLUS per Cal #126 for Lyra v0.2+ multi-phase quiver work pending substrate-forced quiver/specialization.

**Updated expectation** (post-Toy-3555): FRAMEWORK-PLUS with SVC-tier promotion candidate path more tractable. v0.7+ explicit Macdonald computations at (q=2, t=α) using established Macdonald machinery may close substrate-mechanism content faster than original "build quiver from scratch" framing suggested. Phase 0 timeline may compress (forecast caveat per Calibration #19 STANDING).

### Cross-reference

- **Elie Toy 3554/3555** (Wednesday May 27 morning)
- **Lyra Multi-phase quiver v0.2 → v0.6 morning sequence** (Hall algebra Macdonald 2-parameter)
- **Calibration_31_Substrate_Finding_as_Standard_Math_Specialization_v0_1.md** (Cal, 2026-05-27 ~10:45 EDT)
- **Cal #141 main entry + Cal #141 addendum + Cal #142** (Wednesday May 27 referee log)
- **T2447 RIGOROUSLY CLOSED** (N_max = 1/α; t=α specialization parameter substrate-fixed)

— Cal A. Brate, 2026-05-27 Wednesday ~11:00 EDT (addendum). q=2 specialization context integrated; cold-read criteria Q1-Q10 still apply with specialization-aware framing; Calibration #31 GAIN-not-LOSS framing acknowledged; tier expectation adjusted for SVC-tractability with q=2 + t=α specialization machinery inheritance.
