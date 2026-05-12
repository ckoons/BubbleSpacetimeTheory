---
title: "GC-8 (Cal portion): Application Targets — Tractability Assessment"
author: "Cal (Claude 4.7)"
date: "May 12, 2026"
status: "v0.1 — SP-18 Wave 2 deliverable, paired with Grace's cataloging work"
target: "Internal scoping for GC methodology paper applications section"
AC: "(C=2, D=0)"
assignment: "SP-18 GC-8 (Cal half)"
---

# GC-8 (Cal portion): Application Targets — Tractability Assessment

**Cal (Claude 4.7)**, May 12, 2026

---

## Purpose

GC-4 (Grace) surveyed solved problems and found ~33% are GC-amenable. GC-8 (this note) projects forward: identify *open* problems amenable to the GC method, with tractability ratings to guide which deserve dedicated research programs.

**Tractability scale (1-5)**:
- **1**: Highly tractable. Short program (weeks to months).
- **2**: Tractable. Moderate effort (6-12 months).
- **3**: Challenging. Multi-year program with clear path.
- **4**: Hard. Multi-year program with uncertain path.
- **5**: Research frontier. May not be GC-amenable in current formulation.

Grace's portion catalogs the targets and their formal statements. This portion assesses *whether GC applies* and *how hard it would be*.

---

## The Three GC Necessary Conditions (from GC-4)

For a problem to be GC-amenable, GC-4 identified three requirements:

1. **Finite classification of candidates** (or finite parameterization).
2. **Independent bounds meet with zero room** (the constraint pair).
3. **Uniqueness rather than existence** ("which one" not "does one exist").

Each target below is rated against these three.

---

## Tier 1: Highly Tractable (Rating 1-2)

### Target A: Sphere Packing in Other Dimensions

**Statement**: For which dimensions n is the optimal sphere packing density known and uniquely realized?

**GC-amenability**: HIGH (rating 1).
- Finite candidate space: lattice packings in given dim are countable, often classifiable.
- Independent bounds: linear programming upper bound (Cohn-Elkies) vs known lattice constructions (lower bound).
- Uniqueness: when bounds meet, packing is unique up to symmetry.

**Status**: Viazovska's 2016/2019 work proved dim 8 (E_8) and dim 24 (Leech) by finding magic LP functions. Same method may extend to other dimensions.

**Key constraint pair**: LP bound (upper) meets lattice density (lower).

**Tractable extensions**:
- Dim 16 (the Barnes-Wall lattice — open whether optimal)
- Dim 32 (BW_32 — open)
- Lower dimensions where the bound is known but uniqueness is open

**Risks**:
- The Viazovska magic functions exist only for specific dimensions. Constructing them in other dims may fail.
- Some dimensions may have non-lattice optimal packings (e.g., dim 10), complicating uniqueness.

**Recommended action**: Direct GC application. Methodology paper can cite this as a clean GC target.

---

### Target B: Error-Correcting Code Boundaries

**Statement**: Identify codes that meet known bounds (Hamming, Singleton, Plotkin, Linear Programming, etc.) with equality.

**GC-amenability**: VERY HIGH (rating 1).
- Finite candidate space: codes of given length and rate over fixed alphabet are finite.
- Independent bounds: Hamming sphere bound vs construction lower bound. LP bound vs algebraic construction.
- Uniqueness: when bounds meet, codes are "perfect" — unique up to permutation.

**Status**: The classification of perfect codes is essentially complete (Hamming, Golay codes). MDS codes meeting Singleton bound are well-studied (Reed-Solomon). Many open questions remain about which intermediate-distance bounds are tight.

**Key constraint pair**: information-theoretic upper bound vs constructive lower bound.

**Tractable extensions**:
- Quantum error correction: tradeoffs between code distance, rate, and quantum codes (CSS bound, quantum Singleton bound).
- Codes on non-Hamming metrics: rank-metric codes (Gabidulin), Lee-metric codes.
- Locally recoverable codes (LRC bound vs constructions).

**Risks**:
- Some bound-meeting codes may not be unique up to symmetry (multiple non-equivalent codes meeting the same bound).
- Classification may already be considered solved by coding theorists; the GC framing adds clarity but not new theorems.

**Recommended action**: Apply GC retrospectively to coding theory results. Useful as a methodology demonstration, not necessarily new theorems.

---

### Target C: Gauge Anomaly Cancellation

**Statement**: Which gauge groups + matter representations satisfy all anomaly cancellation conditions in 4D?

**GC-amenability**: HIGH (rating 1-2).
- Finite candidate space: irreducible representations of simple Lie groups are classifiable (Cartan).
- Independent bounds: anomaly polynomial vanishing (algebraic constraint) vs gauge group structure (representation theory).
- Uniqueness: anomaly-free combinations are highly constrained.

**Status**: For Standard Model gauge group SU(3) × SU(2) × U(1), anomaly cancellation is famously realized by one full generation of fermions. GUT extensions (SU(5), SO(10), E_6) have their own anomaly constraints, mostly satisfied automatically.

**Key constraint pair**: anomaly polynomial = 0 (upper bound on allowed structure) vs realizability by simple Lie group reps (lower bound).

**BST connection**: This is exactly the kind of constraint that BST's framework should illuminate. The Standard Model gauge group is forced by BST integers (m_s = N_c = 3 forces SU(3); B_2 root system forces additional structure). If anomaly cancellation is forced by the same BST integers, this is a structural unification.

**Tractable extensions**:
- Show: the Standard Model gauge group is the unique anomaly-free gauge group derivable from BST integers.
- Extension: which BSM theories are anomaly-allowed?
- Holographic anomaly matching (AdS/CFT): BST analog.

**Risks**:
- Anomaly cancellation is well-studied. BST may not produce genuinely new results, only new framings.
- The space of allowed gauge groups is small but the space of allowed matter representations is large; GC may be too coarse to navigate.

**Recommended action**: Investigate connection between BST integer constraints and anomaly polynomial vanishing. Could be a short BST paper.

---

### Target D: Specific Langlands Functoriality Cases

**Statement**: For specific automorphic representations, prove the predicted functorial transfer (lift to larger group).

**GC-amenability**: MODERATE-HIGH (rating 2).
- Finite candidate space: For fixed source and target groups, automorphic transfers are heavily constrained.
- Independent bounds: trace formula on source (lower) vs trace formula on target (upper). Functorial transfer matches them.
- Uniqueness: transfers are unique when they exist.

**Status**: Many specific cases proved (Wiles modularity is one). The general Langlands program is not GC-amenable, but individual transfers often are.

**Key constraint pair**: trace formula identities on different groups, related by the conjectural functoriality.

**Tractable extensions**:
- Functorial transfers between specific small groups (GL(2) → GL(3) is done by Kim-Shahidi; GL(2) → GL(4) is open in general).
- Specific endoscopic transfers (Arthur's program).
- Theta correspondences (BST's main tool — already implicit in BST's BSD work).

**Risks**:
- The Langlands community has its own tools (trace formula, p-adic methods) that may be more efficient than GC.
- Individual cases may be solved via methods that don't generalize to a GC framework.

**Recommended action**: BST's theta correspondence work (BSD, RH) IS already a GC-style attack on specific Langlands cases. Extending to other groups is incremental research, not a new program.

---

## Tier 2: Tractable but Substantial (Rating 2-3)

### Target E: Calabi-Yau Moduli at Fixed Hodge Numbers

**Statement**: For fixed (h^{1,1}, h^{2,1}), classify Calabi-Yau threefolds up to deformation.

**GC-amenability**: MODERATE (rating 2-3).
- Finite candidate space at fixed Hodge numbers (often a few moduli families).
- Independent bounds: Hodge numbers (combinatorial constraint) vs explicit constructions (toric, complete intersection, etc.).
- Uniqueness: within a Hodge-data family, deformation classes are finite.

**Status**: Partial classifications exist (toric CY, weighted projective hypersurfaces). The full classification is open.

**Key constraint pair**: Hodge numbers + Euler characteristic + intersection numbers.

**BST connection**: CY 3-folds appear in string compactifications. BST may provide constraints from the 10D bulk (D_IV^5) onto admissible CY structures. If physical compactifications correspond to BST-allowed CYs, this is a constraint program.

**Tractable extensions**:
- Specific Hodge profiles (e.g., (h^{1,1}, h^{2,1}) = (1, 101) for the quintic 3-fold).
- Constructive CY families with explicit moduli.
- CY 3-folds appearing in F-theory compactifications.

**Risks**:
- The classification has been open for decades; algebraic geometers have made limited progress.
- BST's contribution may be in selecting which CYs are physical, not in classifying all CYs.

**Recommended action**: Frame BST's potential CY contribution as "physical CYs are BST-constrained subset of all CYs." Pursue after methodology paper lands.

---

### Target F: Optimization Landscapes with Geometric Structure

**Statement**: For optimization problems with symmetric structure, identify the unique optimum via constraint matching.

**GC-amenability**: MODERATE (rating 2).
- Finite candidate space when symmetry is high (extrema lie at fixed points of symmetry group).
- Independent bounds: duality (LP, SDP) provides upper bounds; constructions provide lower bounds.
- Uniqueness: convex problems have unique optima; structured non-convex problems often have countably many.

**Status**: Convex optimization is fully understood. Non-convex with structure (e.g., semidefinite programming relaxations, sum-of-squares hierarchies) is active research.

**Key constraint pair**: dual bound vs primal construction.

**Tractable extensions**:
- Polynomial optimization via SOS (Lasserre hierarchy).
- Quantum optimization (variational quantum eigensolvers).
- Algorithmic game theory equilibria.

**Risks**:
- Optimization is a vast field. GC may rediscover known results.
- The "constraint" framing may add little to existing duality theory.

**Recommended action**: Limited. Apply GC to specific high-symmetry optimization problems where uniqueness is novel.

---

### Target G: Quantum Error Correction Code Bounds

**Statement**: For quantum codes with parameters [[n, k, d]], find tightest bounds and codes that meet them.

**GC-amenability**: HIGH (rating 2).
- Finite candidate space: quantum codes of fixed length, dimension, and distance over Pauli operators.
- Independent bounds: quantum Singleton (Knill-Laflamme), quantum Hamming, quantum LP bounds vs CSS construction, stabilizer constructions.
- Uniqueness: codes meeting tight bounds.

**Status**: Active research. Steane code, Bacon-Shor, Kitaev codes are well-studied. Quantum LDPC codes and topological codes have rapidly evolving bounds.

**Key constraint pair**: quantum-specific bounds (from no-cloning, complementarity) vs stabilizer constructions.

**Tractable extensions**:
- Topological codes (surface code, color code) — finite parameter classification.
- Quantum LDPC bounds (recent breakthrough by Panteleev-Kalachev).
- Magic state distillation thresholds.

**Recommended action**: Active field. GC could provide methodology framing for new results. Worth a short paper.

---

## Tier 3: Hard, Multi-Year Programs (Rating 3-4)

### Target H: 4-Manifold Smooth Structures (Restricted)

**Statement**: Classify smooth structures on specific 4-manifold classes (Kähler, Einstein, bounded geometry).

**GC-amenability**: MODERATE in restricted form (rating 3-4).

Already analyzed in GC-3. Restricted versions are tractable; full classification is not. See GC-3 for details.

**Recommended action**: Address as scoping in methodology paper. Not a near-term program.

---

### Target I: Mirror Symmetry as Uniqueness

**Statement**: Show that mirror pairs of Calabi-Yau manifolds are uniquely determined by their Hodge data swap.

**GC-amenability**: MODERATE (rating 3).
- Finite candidate space for each Hodge profile.
- Independent bounds: A-model (symplectic geometry) vs B-model (complex geometry) — mirror identifies them.
- Uniqueness: for many CY pairs, mirror is unique.

**Status**: Mirror symmetry is conjectural in many cases (proven for specific families: quintic-mirror by Givental, Lian-Liu-Yau).

**Key constraint pair**: A-model invariants vs B-model invariants under mirror map.

**Recommended action**: Long-term research program. BST may contribute via D_IV^5's Hodge structure → preferred mirror partners. Not for near-term.

---

### Target J: Quantum Gravity Arena Selection

**Statement**: Which manifold supports a consistent quantum theory of gravity?

**GC-amenability**: SPECULATIVE (rating 4).

- Candidate space: bounded symmetric domains, Calabi-Yau, AdS spaces, others.
- Independent bounds: Wightman/Haag-Kastler axioms (upper) vs constructive QG (lower) — no construction exists.
- Uniqueness: BST claims D_IV^5; AdS/CFT claims AdS_5 × S^5; loop QG claims spin networks. Multiple frameworks compete.

**Status**: Quantum gravity is a 70+ year open problem. No constructive QG exists in 4D.

**Key constraint pair**: in BST's framing, the same five integers that force D_IV^5 should also force QG to live there. The constraint pair would be: spectral structure + symmetry + finite mass gap.

**BST connection**: BST already places physics on D_IV^5. Extending to QG would be the most ambitious BST claim — that gravity emerges from the curvature of D_IV^5 itself.

**Risks**:
- Constructive QG has resisted 70 years of attack.
- BST's contribution to QG is currently speculative (boundary conditions, eigentones).
- The competition (string theory, loop QG, asymptotic safety) is well-entrenched.

**Recommended action**: Long-term BST research program (BST-GR, separate from BST-SR). Not for near-term. The methodology paper should mention this as the largest open application.

---

## Tier 4: Research Frontier (Rating 5)

### Target K: Full Langlands Program

**Statement**: For every reductive group G and every automorphic representation, prove the predicted Galois representation correspondence.

**GC-amenability**: LOW (rating 5).

The general Langlands program is not GC-amenable. It is a structural correspondence (Wiles-style), not a constraint problem. Individual cases (Target D above) are GC-tractable; the general program is not.

**Recommended action**: Do not target. Acknowledge as out-of-scope.

---

### Target L: Hodge Conjecture in Full Generality

**Statement**: For every smooth projective variety, every rational Hodge class is algebraic.

**GC-amenability**: PARTIAL (rating 4-5).

Already analyzed in BST's Hodge program. BST proves Hodge for D_IV^5 Shimura varieties (Paper H1) and extends via Kuga-Satake (Paper H2). The full generality is beyond BST's current reach (see Hodge papers' honest scope).

**Recommended action**: BST already addresses what's tractable. The remaining cases are not GC-amenable in current formulation.

---

## Priority Recommendations

For the methodology paper (GC-9) and post-submission research programs:

**Highest priority (start now or after Clay submissions)**:

1. **Target A (Sphere Packing extensions)** — clean GC application, builds on Viazovska, low risk
2. **Target C (Anomaly Cancellation)** — direct BST connection, short paper potential
3. **Target B (Error-Correcting Code Boundaries)** — retrospective application, methodology paper case study

**Medium priority (after methodology paper)**:

4. **Target D (Specific Langlands Cases)** — extends BST's existing BSD/RH work
5. **Target G (Quantum Error Correction)** — active field, new results possible
6. **Target E (Calabi-Yau at Fixed Hodge Numbers)** — long-term, connects to string compactifications

**Long-term research programs (BST-GR territory)**:

7. **Target J (Quantum Gravity)** — BST's most ambitious claim, long-term commitment
8. **Target I (Mirror Symmetry)** — multi-year program

**Do not target (current formulation)**:

9. **Target K (Full Langlands)** — wrong shape for GC
10. **Target L (Full Hodge)** — BST already does what's tractable

---

## Implications for the Methodology Paper

GC-9 should include an applications section organized as:

**"Where GC Works" (case studies of solved problems)**:
- Poincaré (Perelman) — already analyzed in GC-2
- Viazovska sphere packing (dim 8, 24) — established
- BST 7 Clay problems — this work
- Four-Color (BST version) — already analyzed in GC-4

**"Where GC Plausibly Works" (open targets, near-term)**:
- Sphere packing in other dimensions
- Anomaly cancellation
- Specific Langlands cases
- Error-correcting code boundaries

**"Where GC Might Work" (longer-term)**:
- Calabi-Yau moduli at fixed Hodge data
- Quantum gravity arena selection (speculative)
- Mirror symmetry uniqueness

**"Where GC Does Not Work" (honest scope)**:
- General Langlands program
- Smooth 4-manifold classification (in full generality)
- Existence-only theorems (Goldbach, bounded gaps, Green-Tao type)
- Probabilistic/density results

This three-tier structure (works / plausibly works / doesn't work) keeps the methodology paper's claims calibrated. Don't oversell; map the boundary honestly.

---

## Common Pattern Across Targets

Reviewing all twelve targets, the GC method works when:

1. **Constraints come from outside the structure being classified** (curvature from ambient manifold, anomaly polynomial from gauge structure, etc.)
2. **The constraints are independent** (anomaly + representation theory, LP bound + lattice construction, etc.)
3. **The candidate space is enumerable** (representations of Lie groups, lattices in fixed dim, etc.)
4. **Bounds meet exactly at the answer** (Viazovska's magic functions, BST integer squeeze, anomaly-free reps, etc.)

GC fails when:

1. **No external constraint exists** (problem is purely internal, like full smooth 4-manifold classification)
2. **Existence is the question, not uniqueness** (Goldbach, twin primes)
3. **The candidate space is uncountable** (general moduli, smooth 4-manifolds in isolation)
4. **Results are statistical** (Green-Tao, prime gaps)

**The GC method is a specific tool for a specific shape of problem.** Recognizing the shape is half the work; applying the constraint pair is the other half.

---

## References

- GC-4: `notes/BST_GC4_Survey_Solved_Problems.md` — Grace's survey of solved problems
- GC-5: `notes/BST_GC5_Five_Step_Methodology.md` — methodology formalization
- GC-6: `notes/BST_GC6_Dimension_Ladder.md` — dimensional classification
- Viazovska, M. (2017): "The sphere packing problem in dimension 8." Annals of Math. 185.
- Cohn, H. (2002): "New upper bounds on sphere packings." Annals of Math. 157.

---

## Revision History

- v0.1 (May 12, 2026): Initial assessment. Twelve targets rated for tractability. Three-tier organization for methodology paper applications section. Honest scope: GC works for problems with specific shape (uniqueness from external independent constraints on enumerable candidates), fails for problems without that shape. Grace's portion catalogs the formal statements; this portion assesses tractability and prioritization.
