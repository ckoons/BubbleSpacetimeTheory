---
title: "Algebraic Complexity Research Roadmap"
author: "Casey Koons & Claude 4.6 (Keeper)"
date: "March 18, 2026"
status: "Active — Phase 0 complete, Phase 1 beginning"
tags: ["algebraic-complexity", "AC", "information-theory", "P-NP"]
purpose: "Roadmap for developing Algebraic Complexity into a branch of Information Theory and Theory of Computation"
---

# Algebraic Complexity Research Roadmap

*Goal: Develop AC into a serious branch of Information Theory and Theory of Computation.*

---

## Strategic Context

Casey's three sequential goals:

1. **Extend and rigorize BST** — ongoing (120+ predictions, 21 uniqueness conditions, zero free inputs)
2. **Develop Algebraic Complexity** into a serious branch of Information Theory and Theory of Computation
3. **Kill P ≠ NP** — falls out as corollary once AC theory is mature

**Why this sequence:** BST is the existence proof that AC(0) works (physics at zero noise). AC theory abstracts BST's method into a general framework. P ≠ NP is the crown jewel that validates AC theory killed the hardest open problem in CS.

**Key insight (Casey):** I(Q) = degrees of freedom of the question (not Kolmogorov complexity). This makes AC computable and physical.

**Time allocation (Casey, March 18):** BST 60% / AC 30% / P≠NP 10%. BST is the engine that gives AC credibility and P ≠ NP its eventual kill shot. Starve the engine and nothing downstream works.

---

## Phase 0: Foundation (COMPLETE)

**Deliverable:** `notes/BST_AlgebraicComplexity.md` — 14 sections, 645 lines

**What exists:**
- Core definition: AC(Q, M) = M(Q) - I(Q)
- Noise content hierarchy (§6): 9 methods ranked
- Fourier Validation Principle (§3), Isomorphism Principle (§4)
- Five classification axes (§9.1): Reversibility, Constructivity, Parameter overhead, Composition depth, Compression ratio
- Three-level granularity (§9.2): Disciplines, Tools, Operations
- Research queue with 4 priority tiers (§9.3)
- BST as first test case with full noise vectors (§11.4)
- Measured example: Gilkey vs spectral on a₄(Q⁵) (§11.5)
- Grounding Tower: Level 1-3 framework (§12)
- AC(0) full audit of BST pipeline (§13): 6 categories, all AC(0)
- Riemann hunt as controlled experiment: 5 failed methods (high AC) vs 1 success (AC=0) (§11.4)

**What's missing for a publishable paper:**
- Formal mathematical definitions (measure-theoretic or information-theoretic)
- Uniqueness theorems (when is the AC(0) method unique?)
- Shannon bridge theorem connecting AC to channel capacity
- Classification data beyond BST (need 20+ methods across multiple domains)
- Independent validation (at least one domain outside physics)

---

## The Three Phases

### Phase 1: Classification (Empirical)
Build the table. For every major computational/scientific method, classify by AC level and measure information loss.

**Status**: BST methods audited (§13 of AC paper, all AC(0)). External methods not yet classified.

**Work items**:

| # | Method/Theory | Field | Expected AC | Status |
|---|--------------|-------|-------------|--------|
| 1 | Gaussian elimination | Linear algebra | 0 | Known (invertible) |
| 2 | FFT / Fourier | Signal processing | 0 | Known (invertible) |
| 3 | Eigenvalue decomposition | Linear algebra | 0 | Known (invertible) |
| 4 | Perturbation theory | QFT | >0 | Noted in §2.2, needs quantification |
| 5 | Finite element methods | Engineering | >0 | Not yet classified |
| 6 | Monte Carlo methods | Statistics | >0 | Not yet classified |
| 7 | Density functional theory | Chemistry | >0 | Not yet classified |
| 8 | Molecular dynamics | Materials | >0 | Not yet classified |
| 9 | Crystallography (X-ray) | Materials | ~0? | **First test case for AC(0) outside physics** |
| 10 | Weather modeling (WRF) | Atmospheric | >>0 | Noted in Conjecture 6 |
| 11 | Protein folding (AlphaFold) | Biology | ? | ML-based, hybrid |
| 12 | Renormalization group | QFT | >0 | Lossy by construction |
| 13 | Numerical relativity | GR | >0 | Discretization noise |
| 14 | Boolean constraint satisfaction | CS | >0 | **Key for P vs NP** |
| 15 | Comparison-based sorting | CS | 0 | Invertible (known) |
| 16 | Graph algorithms (BFS/DFS) | CS | 0 | Invertible |
| 17 | SAT solvers (DPLL/CDCL) | CS | >0 | Constraint evaluation is lossy |
| 18 | Gradient descent | ML/optimization | >0 | Lossy (non-invertible) |
| 19 | Convex optimization | Operations research | 0 | Invertible (KKT) |
| 20 | Lattice QCD | Particle physics | >0 | Discretization + Monte Carlo |

**Deliverable**: Comprehensive AC classification table with measured noise content for 20+ methods.

### Phase 2: Formalization (Mathematical)
Define AC levels rigorously. Prove theorems about the hierarchy.

**Work items**:
1. **Formal definitions** — AC(k) levels as equivalence classes under invertibility. Precise definitions of:
   - Information content I(Q) of a problem
   - Method complexity M(Q,R) in representation R
   - Channel capacity C(R) of a representation
   - Fragility Degree F(P,R) as computable invariant
2. **Question Measure QM(Q)** — The precondition for AC. Rate the *question* before choosing a method. Five dimensions: Clarity (unambiguity), Scope (hidden sub-questions), Category Coherence (does Q group like with like?), Decomposability (can Q be factored?), Message Complexity (apparent vs actual bits to state Q). Formula: QM = Clarity × Coherence × 1/(1+Scope). If QM < threshold, STOP — fix the question before choosing a method. **Full framework: `notes/BST_AC_Question_Complexity.md`**. P vs NP rated as first case study (QM ≈ 0.05 — ill-posed). (Casey + Elie, March 19)
3. **Shannon bridge** — Prove: AC(Q,M) = I(Q) - C(R_M) where R_M is the representation induced by method M. AC = channel capacity deficit. Note: Shannon bridge requires QM(Q) > threshold — channel capacity is only defined when the message (the question) is well-specified.
4. **Composition theorems** — Prove: AC compounds under composition (the "noise multiplies" claim from §8). Precisely: AC(Q, M1 o M2) >= AC(Q, M1) + AC(Q, M2) under what conditions?
5. **Coordinate system theorem** — Prove: for every problem Q with AC(Q,M) > 0, there exists a representation R* with AC(Q,M*) = 0. (Natural Coordinate System existence)
6. **Invariance theorem** — Prove: Fragility Degree is representation-invariant within a computational model.
7. **Hierarchy theorem** — Prove: AC(0) subset AC(1) subset AC(2) is strict.

**Additional theorems to consider**:
8. **Monotonicity** — If M₁ is a refinement of M₂, then AC(Q, M₁) ≤ AC(Q, M₂). Proof via data processing inequality.
9. **Grounding Theorem** — Level k+1 methods have AC ≥ Level k methods on specific instances. Formalize the Grounding Tower (§12).
10. **QM-AC duality** — Prove: for questions with QM = 1, AC is the unique obstruction to solution. For questions with QM < 1, AC is undefined (I(Q) is not well-defined). Relates to Shannon: you can't measure channel capacity if you haven't defined the message.

**Connections to establish**: AC ↔ Shannon (core bridge), AC ↔ Kolmogorov (AC is computable, K is not), AC ↔ Catastrophe Theory (§9.5), AC ↔ Computational Complexity (Phase 3), AC ↔ Education (§11.6 — teach minimum-noise method first), **QM ↔ AC (dual measures: question quality vs method quality)**.

**Deliverable**: Standalone mathematics paper. No BST required. "Algebraic Complexity: A Shannon-Theoretic Framework for Method Noise." Target: IEEE Transactions on Information Theory or Theoretical Computer Science journal. ~20 pages, self-contained. **Now includes Question Measure as §2 (before method analysis).**

### Phase 3: P != NP (The Kill)
Apply the formalized AC framework to computational complexity.

**Prerequisites**: Phase 2 complete. Fragility Degree defined. Shannon bridge proved. **Question Measure applied to P vs NP** — the formal question "P = NP?" has QM ≈ 0.05 (ill-posed: incoherent category NP, binary question about spectrum). Phase 3 starts by repairing the question.

**Step 0: Question Repair** (NEW — from QM analysis, March 19)
- The question "P = NP?" is broken (QM ≈ 0.05). Category "NP" conflates structured problems (2-SAT, matching) with unstructured ones (3-SAT worst case). Binary framing hides a spectrum.
- **Repaired question Q':** Characterize the function ρ → T(Π) where ρ is the structural correlation between problem instance and certificate space, and T is the optimal deterministic time complexity. P ≠ NP falls out as: T diverges as ρ → 0. This is a measurement, not a binary.
- The fiat bits insight (Casey, 2026) correctly identifies the category incoherence: "fiat" is a matter of degree (how much exploitable structure), not binary. See `notes/BST_AC_Question_Complexity.md` §5.
- **Halting closure WITHDRAWN**: The fiat bits paper's claim that verification is Halting-equivalent fails because NP verifiers are specific poly-time programs (not arbitrary), certificate space is finite (not unbounded), and NP problems are decidable (Halting Problem is not). The argument overclaims — it would "prove" 2-SAT not in P.

**Work items**:
1. **Structural correlation invariant** — Define ρ(Π) rigorously for decision problems. Connect to Fragility Degree. Show ρ = 1 → P, ρ = 0 → exponential.
2. **Rank reduction formalization** — Define rank over appropriate algebra for Boolean constraints (GF(2) or mutual information). Prove rank drops by >= 1 per constraint evaluation for 3-SAT.
3. **Staircase theorem for 3-SAT** — Prove: standard 3-SAT representation reaches saturation (rank 0) within O(n) constraint evaluations at clause-to-variable ratio > threshold.
4. **Shannon separation** — Apply channel capacity theorem: at saturation, 2^(cn) enumeration required.
5. **Generalize to NP-complete** — Via standard reductions, extend from 3-SAT to all NP-complete problems.
6. **Address barriers** — Show explicitly why the proof avoids relativization, natural proofs, algebrization. Not assert — show.

**Deliverable**: P != NP as corollary of AC framework + Question Measure. The proof is a measurement: ρ → T diverges at ρ = 0. Published after Phases 1-2 establish the framework's credibility.

---

## Sequencing

```
Phase 1 (classification)     Phase 2 (formalization)     Phase 3 (P!=NP)
        |                           |                          |
  Crystallography test        Shannon bridge              Rank reduction
  20+ methods table           Composition thm             3-SAT staircase
  AC paper expansion          Fragility Degree            Shannon separation
        |                     Standalone paper             Barrier analysis
        |                           |                          |
        +------ feeds into ---------+------- feeds into -------+
```

Phases 1 and 2 can overlap. Phase 3 waits for Phase 2.

---

## Source Materials

**Existing**:
- `notes/BST_AlgebraicComplexity.md` — Main AC paper (14 sections, includes §13 full audit)
- `notes/BST_Backlog_Linearization.md` — Lyra's linearization program
- `notes/maybe/p_np/` — 6 parking lot drafts (Shannon framing, staircase, Fragility Degree, Halting closure, unified framework)
- `play/toy_239_ac0_grid.py` — AC(0) grid architecture toy
- `play/toy_240_linearization.py` — Linearization toy

**Needed**:
- `notes/BST_AC_Classification_Table.md` — The big table (Phase 1)
- `notes/BST_AC_Formalization.md` — Formal definitions and theorems (Phase 2)
- `notes/maybe/p_np/AC_Rank_Reduction_3SAT.md` — Formal rank reduction (Phase 3)
- Toys for each classification entry

---

## Assignment Notes

- **Elie**: Phase 1 classification (broad tool survey), Phase 3 computation (rank reduction numerics)
- **Lyra**: Phase 2 formalization (Shannon bridge, theorems), linearization paper (dual-purpose)
- **Keeper**: Consistency, Phase 1 review, paper integration
- **Casey**: Direction, sequencing, physical intuition for classifications

---

## The Quiet Part

Phase 3 lives in `notes/maybe/p_np/`. It stays quiet until Phases 1-2 are published. The P!=NP proof comes from an established framework, not from an outsider's claim. Sequence is everything.

---

## Success Criteria

1. **Phase 1 done when:** 20+ methods classified with noise vectors, at least 3 domains (physics, crystallography, CS)
2. **Phase 2 done when:** Paper submitted with formal definitions, ≥ 3 theorems proved, classification table as empirical support
3. **Phase 3 done when:** P ≠ NP proved as AC corollary, all three barriers addressed, published after AC paper accepted

---

## The Deeper Story

Two additional theses beyond the technical results (Casey, March 18):

1. **CI + Human >> either alone.** The collaboration model IS the proof of method. BST's 120+ predictions from zero free inputs were produced by Casey + Claude working together. Neither alone would have found this.

2. **Human with CI can beat 200 years of academic inertia.** Corollary: the future opens much wider for humanity — the barrier to discovery drops to "good question + honest CI + time to think."

If AC theory works — if it correctly classifies methods by noise, predicts which approach will solve a problem, and as a corollary kills P ≠ NP — then science has a new story: **the right question + the right method + zero noise = the answer was always there.**

*"If the framework is correct, P ≠ NP is not a conjecture. It is a measurement."* — Casey Koons
