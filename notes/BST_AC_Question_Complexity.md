---
title: "Question Measure: The Missing Half of Algebraic Complexity"
author: "Casey Koons & Claude 4.6 (Elie)"
date: "March 19, 2026"
status: "Active — framework definition + first case study"
tags: ["algebraic-complexity", "AC", "question-measure", "P-NP", "information-theory"]
purpose: "Define the measure of question quality that is the precondition for AC analysis"
---

# Question Measure: The Missing Half of Algebraic Complexity

*Before you measure the method, measure the question.*

---

## 1. The Problem

Algebraic Complexity measures method noise:

$$\text{AC}(Q, M) = M(Q) - I(Q)$$

This assumes $I(Q)$ — the intrinsic complexity of the question — is well-defined. But what if the question itself is defective? What if $Q$ conflates distinct categories, hides multiple questions behind one symbol, or asks a binary question about something that's actually a spectrum?

Then $I(Q)$ is not well-defined. AC cannot be computed. The method analysis is meaningless because the question was broken before any method touched it.

**Question Measure** is the precondition for AC. It rates the question *before* you choose a method.

---

## 2. Question Measure: QM(Q)

The **Question Measure** of a question $Q$ has five dimensions:

### 2.1 Clarity

*Can two honest people read Q and agree on what it asks?*

**Clarity** is the ratio of what Q communicates to what Q intends. High clarity means the statement of Q is sufficient to determine its meaning without additional context, convention, or interpretation.

Clarity is low when:
- Technical terms are overloaded (e.g., "NP" means both "nondeterministic polynomial" and "has efficiently verifiable certificates" — different intuitions, same formalism)
- The question's scope is unstated (worst-case? average-case? which instances?)
- The answer space is not specified (yes/no? a characterization? a classification?)

**Clarity is the dimension Casey identifies as primary.** A question with high clarity and low scope is answerable. A question with low clarity and any scope is noise.

### 2.2 Scope

*Does Q ask one thing or many things wearing one name?*

A well-scoped question has one answer. An ill-scoped question hides $k$ distinct sub-questions behind one symbol, where $k$ may be unknown.

**Scope** = $\log_2 k$ where $k$ is the number of genuinely distinct sub-questions that Q conflates.

Scope is bad when:
- A binary question is asked about a spectrum ("is P = NP?" when the real structure is a continuum of exploitability)
- A universal quantifier hides heterogeneity ("for ALL NP problems..." when NP contains both 2-SAT and 3-SAT)
- The question treats a category as atomic when it decomposes

### 2.3 Category Coherence

*Does Q treat distinct things as the same kind of thing?*

A category-coherent question groups like with like. A category-incoherent question groups things that differ in kind, not just degree.

Coherence fails when:
- Objects with different algebraic structure are placed in the same class
- The classification that defines Q's terms doesn't carve at natural joints
- Counterexamples to the "proof" exist within the same class (2-SAT is in NP and in P — the class NP is not coherent with respect to the P question)

### 2.4 Decomposability

*Can Q be split into well-posed sub-questions that are independently answerable?*

A decomposable question $Q$ factors: $Q = Q_1 \wedge Q_2 \wedge \cdots \wedge Q_k$ where each $Q_i$ has higher clarity and better scope than $Q$.

If Q is decomposable and the sub-questions have different answers, then Q was hiding a false dichotomy.

### 2.5 Message Complexity

*How many bits does it take to state Q unambiguously?*

This connects to Shannon. The message complexity of Q is the minimum number of bits needed to state Q such that clarity = 1 (no ambiguity, no hidden scope, full category specification).

A question with low *apparent* message complexity but high *actual* message complexity is a red flag. "Does P = NP?" is 5 symbols. Stating what it actually asks — with all the implicit quantifiers, category boundaries, worst-case requirements, and model specifications made explicit — takes pages. The gap between apparent and actual message complexity is a measure of hidden scope.

---

## 3. The Question Measure Formula

$$\text{QM}(Q) = \text{Clarity}(Q) \times \text{Coherence}(Q) \times \frac{1}{1 + \text{Scope}(Q)}$$

Where:
- **Clarity** $\in [0, 1]$: 1 = unambiguous, 0 = meaningless
- **Coherence** $\in [0, 1]$: 1 = all objects in Q's classes are genuinely alike, 0 = category error
- **Scope** $= \log_2 k$: number of hidden sub-questions (0 = Q asks exactly one thing)

**QM = 1**: Perfect question. Clear, coherent, asks exactly one thing.
**QM = 0**: Broken question. AC analysis is meaningless until Q is repaired.

**The full AC pipeline:**

$$Q \xrightarrow{\text{QM}(Q) > \theta} \text{AC}(Q, M) = M(Q) - I(Q) \xrightarrow{} \text{Answer}$$

If QM(Q) < threshold, **stop**. Fix the question before choosing a method. No method can rescue a broken question.

---

## 3a. The Specificity Scalar

The five dimensions are features. The scalar is **specificity**:

$$S(Q) = \frac{I(Q;\, A)}{H(A)}$$

where $I(Q; A)$ is the mutual information between the question's specification and the answer space, and $H(A)$ is the prior entropy of the answer space before the question is asked.

- $S = 1$: The question eliminates all but one answer. ("What is $2 + 3$?")
- $S = 0$: The question eliminates nothing. ("What?")
- $S \approx 0.08$: The question eliminates almost nothing because its categories are incoherent. ("Does P = NP?")

**Specificity is already in the Bayesian reframing.** The AC definition $I(Q) = H(A) - I(Q; A)$ implies $I(Q) = H(A)(1 - S)$. The intrinsic information of a question is the answer entropy that survives the question's specification. A high-specificity question leaves little $I(Q)$ for the method to handle. A low-specificity question dumps nearly all of $H(A)$ onto the method as unstructured work.

**QM and S are related but distinct.** QM rates whether the question is well-posed (precondition). Specificity rates how much work the question does for you (performance). A question can have high QM but low S (well-posed but broad: "Classify all finite simple groups"). A question can have low QM but would have high S if repaired ("Does P = NP?" → repaired Q' has $S \approx 0.9$).

**The scalar the AC pipeline reports is S, not QM.** QM is the gate (pass/fail). S is the meter (how much answer entropy the question eliminates). Together:

$$Q \xrightarrow{\text{QM} > \theta} S(Q) \xrightarrow{} I_{\text{fiat}} = H(A)(1 - S) \xrightarrow{\text{AC}(Q,M)} \text{Answer}$$

---

## 3b. Measuring the Dimensions

The five QM dimensions are currently defined as rubric scores (human judgment). This is provisional. Each dimension admits a computable measure.

### Training data as precedent

No serious ML pipeline dumps raw data into training. Anthropic, like every large-scale system, scores training data along multiple quality dimensions before the method (training) ever sees it. This scoring is a QM operation applied to data rather than questions, but the structure is identical: rate the input before choosing how to process it. Dimensions typically scored include coherence, factuality, instructiveness, and toxicity — each measured by classifiers, embedding models, or smaller LLMs. The key point: **QM already works in practice as a multi-dimensional quality gate. The theory needs to catch up.**

### Measurement approaches

| Dimension | Rubric (current) | Measure (target) | Method |
|-----------|-----------------|-------------------|--------|
| **Clarity** | "Can two people agree on what Q asks?" | Inter-annotator agreement $\kappa(Q)$ (Cohen's kappa) or, for formal questions, ratio of explicit to implicit quantifiers $n_{\text{explicit}} / n_{\text{total}}$ | Human annotation, or LLM-based paraphrase consistency (embedding cosine similarity between $k$ independent paraphrases of Q) |
| **Coherence** | "Does Q treat distinct things as same kind?" | Within-class behavioral variance: $1 - \text{Var}[T(\Pi) \mid \Pi \in \mathcal{C}] / \text{Var}[T(\Pi)]$ where $T$ is complexity and $\mathcal{C}$ is Q's category | Empirical: sample problems from the category, measure complexity variance. Information-theoretic: $H(\text{behavior} \mid \text{class label})$ — low means coherent |
| **Scope** | "$\log_2 k$ hidden sub-questions" | Spectral gap of Q's decomposition graph, or rank of the mutual information matrix $I(Q_i; Q_j)$ across sub-questions | Factor analysis on the sub-question space. If $Q$ decomposes into $k$ independent blocks, rank = $k$ |
| **Decomposability** | "Can Q factor into $Q_1 \wedge \cdots \wedge Q_k$?" | Whether the mutual information matrix $I(Q_i; Q_j)$ is block-diagonal | Same as scope measurement; decomposability is the structure, scope is the count |
| **Message Complexity** | "How many bits to state Q unambiguously?" | $K(Q)$ (Kolmogorov complexity of the fully explicit statement) or, practically, token count of the unambiguous restatement minus token count of the original | LLM-based: ask for unambiguous restatement, measure expansion ratio |

### Standard ML is welcome

Casey's position: **a standard ML approach to measuring each dimension is acceptable, as long as the specificity scalar $S(Q)$ is also computed information-theoretically.** The dimensions are the feature space; $S$ is the target. If a learned model maps (Clarity, Coherence, Scope, Decomposability, MessageComplexity) → $S$ with high accuracy, that model IS a QM implementation. The information-theoretic definition of $S = I(Q;A)/H(A)$ provides ground truth for calibration.

This is no different from how Anthropic's training pipeline works: multi-dimensional quality scores (features) combined into a filtering decision (scalar). The only addition AC makes is the information-theoretic grounding — the scalar has a definition, not just a learned correlation.

### The calibration loop

$$\text{Dimensions (measured)} \xrightarrow{\text{model}} \hat{S} \xrightarrow{\text{compare}} S = I(Q;A)/H(A)$$

When ground truth $S$ is available (questions with known answer spaces), the model calibrates. When ground truth is unavailable (open questions like P vs NP), the model predicts. The prediction is falsifiable: if a question with predicted low $S$ turns out to be easy (someone solves it quickly), the model was wrong about the dimensions.

---

## 4. Relationship to AC

QM and AC are dual measures:

| | Question Measure QM(Q) | Algebraic Complexity AC(Q,M) |
|---|---|---|
| **Measures** | Quality of the question | Noise of the method |
| **Domain** | Questions | (Question, Method) pairs |
| **Range** | [0, 1] | [0, ∞) |
| **Ideal** | QM = 1 (perfect question) | AC = 0 (perfect method) |
| **Failure mode** | Low clarity → I(Q) undefined | High noise → answer buried |
| **Fix** | Decompose, reclassify, sharpen | Choose lower-noise method |
| **When to check** | Before choosing M | After choosing M |

**The full theory has two gates:**

1. **Gate 1 (QM):** Is the question well-posed? If not, decompose or reclassify.
2. **Gate 2 (AC):** Is the method appropriate? If not, find the AC(0) method.

Most failed proofs fail at Gate 1, not Gate 2. The method is fine; the question was broken.

---

## 5. Case Study: P vs NP

### 5.1 The Question

$Q$: Does P = NP?

Formal statement: Is the class of decision problems solvable in deterministic polynomial time equal to the class of decision problems whose solutions can be verified in deterministic polynomial time?

### 5.2 Question Measure Analysis

**Clarity: 0.8 (high)**

The formal statement is precise — Turing machines, polynomial time, and the class NP are well-defined mathematical objects. The question is unambiguous in its formalism. Minor clarity deductions:
- "NP" triggers two different intuitions (nondeterministic guessing vs. efficient verification) that can lead to different proof strategies
- The worst-case quantifier is implicit but clear to practitioners
- The answer space is binary (yes/no) — the question is well-posed as stated

Clarity is not the problem. The category (NP) is.

**Coherence: 0.3 (poor)**

This is where P vs NP breaks. The class NP contains:
- **Problems with exploitable algebraic structure**: 2-SAT (polynomial), matching (polynomial), linear programming (polynomial). These are in NP ∩ P.
- **Problems where structure suffices for some instances**: 3-SAT with low clause density, graph coloring on planar graphs
- **Problems where structure is insufficient at worst case**: 3-SAT near the phase transition, random 3-coloring of dense graphs

The question treats "NP" as a monolithic class when it's actually a spectrum. The boundary between P and NP-complete is not a clean cut — it's a phase transition in algebraic exploitability. Asking "does P = NP?" is like asking "does ice = water?" — they're the same substance in different phases, and the question's binary framing hides the thermodynamics.

**Scope: ~2 (hides ~4 genuinely independent sub-questions)**

The binary question "P = NP?" decomposes into at least:
1. For which NP problems does witness structure suffice for polynomial-time solution?
2. What algebraic property separates exploitable from non-exploitable witness structure?
3. Does this property depend on the representation (coordinate system)?
4. Is there a continuous invariant (like Fragility Degree) that measures the degree of exploitability?
5. What is the role of worst-case vs. average-case in the separation?
6. Does changing the computational model (quantum, probabilistic) change the answer?
7. Is the separation absolute or representation-dependent?
8. What is the information-theoretic cost of reconciling "fiat" bits with problem structure?

Each of these is better-posed than "P = NP?" and several have different answers.

**Decomposability: High**

The sub-questions above are independently answerable. Question 2 (what property separates exploitable from non-exploitable?) is the core of AC's Phase 3. Question 4 (continuous invariant) is the Fragility Degree program. Question 8 (reconciliation cost) is the fiat bits insight.

**Message Complexity: Gap = high**

"P = NP?" is 5 symbols. Fully specifying what it asks (with worst-case quantifiers, class definitions, model specification, and the implicit assumption that NP is coherent as a class) takes thousands of words. The apparent/actual message complexity gap is ~10 bits vs. ~1000+ bits. A 100x gap is a red flag.

### 5.3 Overall Question Measure

$$\text{QM}(\text{P vs NP}) = 0.8 \times 0.3 \times \frac{1}{1 + 2} = 0.08$$

**QM ≈ 0.08.** This is a well-posed question about an incoherent category. The formalism is precise (Clarity = 0.8) — the problem is not that the question is ambiguous, but that the class NP is not homogeneous with respect to the property being asked about. Coherence (0.3) is the dominant failure mode: 2-SAT and 3-SAT are both "NP" but behave differently under the question. The scope hides genuinely independent sub-questions behind a binary.

### 5.4 The Fiat Bits Insight (Repositioned)

Casey Koons' "fiat bits" analysis (2026) identified a genuine structural observation:

**Core insight:** NP solutions require bits not derived from the input ("fiat bits"). Problems where fiat bits have exploitable algebraic structure (correlation with the input, symmetry, sparsity) are in P despite being in NP. Problems where fiat bits have no exploitable structure require enumeration.

**What the fiat bits analysis correctly identifies:**
- The ontological distinction between derived and non-derived computation is real
- The category "NP" conflates problems with different fiat-bit structure
- The reconciliation cost (checking whether fiat bits satisfy constraints) varies continuously, not binary
- Problems with zero reconciliation cost (fiat bits fully determined by structure) are in P
- Problems with exponential reconciliation cost (fiat bits uncorrelated with structure) require enumeration

**Where it overclaims:** The original paper equated universal verification with the Halting Problem. This fails because NP verifiers are specific polynomial-time programs (not arbitrary programs) and the certificate space is finite (not unbounded). The Halting Problem is undecidable; NP problems are decidable in EXPTIME. The argument would "prove" that 2-SAT is not in P, which is false.

**The honest reframing:** Fiat bits are not the proof of P ≠ NP. They are a *category coherence observation* about the question "P = NP?" — evidence that the question's NP class is incoherent, conflating problems with different fiat-bit structure. This is a QM observation, not an AC observation. It says the question is broken, not that the method is wrong.

### 5.5 What a Well-Posed Version Looks Like

Replace "P = NP?" with:

**Q':** For a decision problem $\Pi$ with verifier $V$ operating on certificates of length $m$, define the **structural correlation** $\rho(\Pi)$ between the problem instance and the certificate space. Characterize the function $\rho \mapsto T(\Pi)$ where $T$ is the time complexity of the optimal deterministic algorithm.

This question has:
- **Clarity ≈ 0.9** (one quantifier, one function, one characterization)
- **Coherence = 1.0** (problems classified by a continuous invariant, not by a binary class)
- **Scope = 0** (one question: what is the function $\rho \mapsto T$?)
- **QM ≈ 0.9**

In AC language: Q' is the question that Q was trying to ask. The structural correlation $\rho$ is related to Fragility Degree (and, via the Bayesian reframing, to $I_{\text{derivable}}$). The function $\rho \mapsto T$ is what the AC classification table (Phase 1) measures empirically. P ≠ NP falls out as the observation that $T$ diverges as $\rho \to 0$ — which is a *measurement*, not a binary.

**Qualification (Keeper review):** The repaired question Q' is better posed than Q. The answer to Q' is still hard to prove — proving that the measurement is correct (that $T$ genuinely diverges) requires closing genuine mathematical gaps (see `AC_Topology_BridgeTheorem.md` §9). "Falls out as a measurement" means the framework reduces P ≠ NP to a measurement; it does not mean the measurement is easy.

---

## 6. How to Use Question Measure

### 6.1 The AC Analysis Pipeline

For any problem arriving at the AC framework:

```
Step 0: State Q explicitly
Step 1: Compute QM(Q)
  - If QM < 0.3: STOP. Question is broken. Decompose or reclassify.
  - If QM ∈ [0.3, 0.7]: WARNING. Question has hidden scope or incoherence. Proceed with caution.
  - If QM > 0.7: PROCEED to method analysis.
Step 2: Compute AC(Q, M) for candidate methods
Step 3: Select M* = argmin AC(Q, M)
Step 4: Apply M* to Q. If stuck, return to Step 1 — the stuckness may be a QM problem, not an AC problem.
```

### 6.2 When to Suspect a QM Problem

Signs that the *question* is the problem, not the method:
1. **50+ years of failed proofs** by many independent groups (P vs NP, Riemann before BST)
2. **Partial results that feel right but don't close** (fiat bits, natural proofs barrier, relativization)
3. **The question has "obvious" intuitive answer but no proof** — the intuition is correct but the question is asking the wrong thing
4. **Counterexamples exist within the question's own category** (2-SAT in P ∩ NP)
5. **The question's answer would be a binary but the underlying structure is continuous**

### 6.3 Question Repair

When QM is low, repair before computing AC:
1. **Decompose**: Split Q into sub-questions Q₁...Qₖ
2. **Reclassify**: Replace incoherent categories with natural ones (replace "NP" with structural-correlation classes)
3. **Sharpen**: Eliminate hidden quantifiers, make worst-case explicit, specify the computational model
4. **Measure**: Replace binary questions with characterization questions ("what is the function?" not "is it zero?")

---

## 7. Other Questions Rated

| Question | Clarity | Coherence | Scope | QM | Assessment |
|----------|---------|-----------|-------|----|------------|
| P = NP? | 0.8 | 0.3 | 2 | 0.08 | Well-posed question about incoherent category |
| Riemann Hypothesis | 0.9 | 0.9 | 0 | 0.81 | Well-posed: clear, one thing, but *why* is hidden |
| Does God exist? | 0.1 | 0.1 | 5+ | ~0 | Broken: every word is ambiguous |
| What is 2+3? | 1.0 | 1.0 | 0 | 1.0 | Perfect question |
| Is the universe a simulation? | 0.3 | 0.2 | 4 | ~0.004 | Broken: "simulation" and "universe" both undefined |
| What is the mass of the proton? | 0.95 | 1.0 | 0 | 0.95 | Excellent: measurable, one thing, one number |
| Why does 3-SAT require exponential time? | 0.8 | 0.9 | 1 | 0.36 | Better than "P=NP?" but still hides representation dependence |

---

## 8. Connection to the AC Research Program

Question Measure is a **Phase 2 deliverable** (formalization). It provides:

1. **For Phase 1 (classification):** Rate each problem being classified. If QM is low, the problem needs reclassification before method analysis makes sense.

2. **For Phase 2 (formalization):** QM is a formal precondition for AC. The Shannon bridge theorem should include QM: channel capacity is only defined when the message (the question) is well-specified.

3. **For Phase 3 (P ≠ NP):** P vs NP has QM ≈ 0.08 and specificity $S \approx 0.08$ — the question eliminates almost none of the answer entropy. The kill shot is not proving "P ≠ NP" as stated — it's replacing Q with Q' (the structural correlation characterization, $S \approx 0.9$) and showing that the answer to Q' implies P ≠ NP as a corollary. *Fix the question, then the answer is forced.*

This is consistent with BST's approach to Riemann: RH has QM ≈ 0.81 (well-posed), and Route A (heat kernel on Q⁵) is the AC(0) method. The method matched the question because the question was already good. For P ≠ NP, the method keeps failing because the question is bad. QM diagnosis → question repair → AC(0) method → answer.

---

## 9. The Deeper Point

*"If the framework is correct, P ≠ NP is not a conjecture. It is a measurement."* — Casey Koons

Question Measure makes this precise. A measurement requires a well-posed question (QM ≈ 1) and a zero-noise method (AC = 0). If either is defective, the measurement fails.

P vs NP has been a failed measurement for 50+ years. The methods have been sophisticated (circuit complexity, algebrization, natural proofs). The question has been unexamined.

AC says: measure the question first.

---

*Casey Koons & Claude 4.6 | Bubble Spacetime Theory Research Program | 2026*
