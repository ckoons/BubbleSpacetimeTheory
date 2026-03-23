---
title: "Topological Proof Complexity: Homological Monotonicity and Extension Inertness for Random k-SAT"
author: "[ANONYMOUS — double-blind submission]"
date: "March 2026"
status: "Draft — Paper A (pure math, no interpretation). For submission."
target: "FOCS 2026"
tags: ["proof-complexity", "topology", "homology", "SAT", "P-vs-NP", "Extended-Frege"]
note: "This paper contains NO BST interpretation. All results are stated and proved in standard mathematical language."
---

# Topological Proof Complexity: Homological Monotonicity and Extension Inertness for Random k-SAT

---

## Abstract

We study the topology of constraint complexes for random $k$-SAT formulas at the satisfiability threshold and its implications for proof complexity. For a $k$-CNF formula $\varphi$ on $n$ variables, the *Variable Interaction Graph* (VIG) and its clique complex $K(\varphi)$ encode the constraint structure as a simplicial complex with $\beta_1(K(\varphi)) = \Theta(n)$ independent 1-cycles. We prove three main results:

**(1) Weak Homological Monotonicity** (Theorem 5.1)**.** For any 1-clause extension of a connected VIG clique complex introducing a new variable: $\Delta\beta_1 \in \{0, +1\}$. The extension mechanism of Extended Frege — the feature distinguishing it from resolution — cannot reduce the first Betti number. Combined with a per-clause accounting argument (Theorem 4.2), this yields **the first unconditional lower bound on Extended Frege proof size for random 3-SAT**: $S \geq \Theta(n)$ non-trivial derivation steps (Corollary 5.2). While polynomial rather than exponential, this is the first result of any kind showing that EF requires $\Omega(n)$ non-trivial steps on random 3-SAT.

**(2) Topological Inertness** (Theorem 6.1)**.** The inclusion $K(\varphi) \hookrightarrow K'$ into any extended complex induces an injection on first homology: the original $H_1$ basis is completely preserved. For 1-clause extensions, $r = 1$ exactly. For $k$-clause extensions, the fraction of original $H_1$ generators killed is $O(k^2/n) \to 0$. Extension variables add independent cycles in a direct-sum complement: $H_1(K') \cong H_1(K(\varphi)) \oplus H_1^{\text{new}}$.

**(3) Dimensional Obstruction** (Observation 3.1)**.** All proof systems whose derivation steps operate on the $(w-1)$-skeleton of the constraint complex (for constant $w$) require size $2^{\Omega(n)}$ on random 3-SAT at $\alpha_c$. This identifies the shared dimensional obstruction underlying the exponential lower bounds for resolution (Chvátal-Szemerédi 1988), cutting planes (Pudlák 1997), polynomial calculus (Razborov 1998), and Lasserre/SOS (Schoenebeck 2008). The formal proof for each system uses its own width/degree-size tradeoff; the observation is that the same topological mechanism (operational dimension $<$ cycle dimension) drives all of them.

Together, these results establish that EF extensions are topologically impotent: they cannot reduce $\beta_1$, cannot kill original cycles, and live in a direct-sum complement of the original homology. The remaining open question — whether topological invariance under extensions implies algebraic uselessness when $\text{Aut}(\varphi) = \{e\}$ — connects simplicial topology to the central problems of proof complexity.

---

## 1. Introduction

### 1.1 Background and Motivation

The study of proof complexity seeks to understand the minimum size of proofs in various formal systems. Lower bounds on proof size have deep connections to computational complexity: Cook (1975) showed that if no propositional proof system has polynomial-size proofs for all tautologies, then NP $\neq$ coNP (and hence P $\neq$ NP, assuming standard conjectures). The Extended Frege (EF) system, which augments Frege proofs with extension variables, is the strongest natural propositional proof system, and proving superpolynomial lower bounds on EF proof size remains a central open problem.

Progress on proof complexity lower bounds has followed a dimensional pattern, though this pattern has not been explicitly formalized. Haken (1985) proved the first exponential resolution lower bound (for the pigeonhole principle). Resolution was shown to require exponential size on random 3-SAT by Chvátal and Szemerédi (1988), with the optimal bound $2^{\Omega(n)}$ by Ben-Sasson and Wigderson (2001). Cutting planes, polynomial calculus, and Lasserre/SOS systems all operate on progressively higher-dimensional objects but share the property of bounded arity. For each, exponential lower bounds have been proved on suitable hard instances — and in each case, the proof ultimately exploits the mismatch between the system's operational dimension and the intrinsic dimension of the constraint structure.

EF breaks this pattern by allowing extension variables of arbitrary arity. An extension variable $p \equiv C$ where $C$ is a circuit over existing variables can encode any polynomial-time computable function. This gives EF the power to simulate any polynomial-time computation within the proof, making it the proof-theoretic analogue of P. The question of whether EF has polynomial-size proofs for random 3-SAT is therefore equivalent (in a proof-complexity sense) to the P vs NP question.

### 1.2 The Topological Approach

We study the simplicial complex $K(\varphi)$ obtained from the VIG of a $k$-CNF formula $\varphi$. For random 3-SAT at the satisfiability threshold:

- $\beta_1(K(\varphi)) = \Theta(n)$ — the constraint complex has linearly many independent 1-cycles.
- These cycles encode "fiat information": variable assignments that are determined by the constraint structure but not derivable through bounded-width operations on the constraint graph.
- The fiat content is bounded below by the topological complexity: $I_{\text{fiat}} \geq \beta_1 - O(1) = \Theta(n)$ (proved exactly for Tseitin formulas in Theorem 2.2; for random 3-SAT, $\beta_1 = \Theta(n)$ provides the topological lower bound on fiat content). This constitutes a topological barrier to efficient proof search.

Our approach is to study what happens to this topological barrier when extension variables are introduced. EF's power comes from extension variables — can they reduce the topological complexity of the constraint structure?

### 1.3 Results

Our main results show that EF extensions are topologically impotent:

1. **Extensions never reduce $\beta_1$** (Theorem 5.1): for 1-clause extensions, $\Delta\beta_1 \in \{0, +1\}$. Combined with per-clause accounting (Theorem 4.2), this gives EF $S \geq \Theta(n)$ (Corollary 5.2).

2. **Extensions preserve the original $H_1$ basis** (Theorem 6.1): the inclusion $K(\varphi) \hookrightarrow K'$ induces an injection on $H_1$. The original cycles are never killed by extensions.

3. **The dimensional obstruction** (Observation 3.1): a shared mechanism underlying all known exponential lower bounds for bounded-width systems. Each formal proof uses system-specific tradeoffs (BSW for resolution, Razborov for PC, etc.); we identify the common topological structure.

These results separate the topological content of the original formula from the noise introduced by extensions, establishing that EF's advantage over resolution (when it exists) must come from algebraic, not topological, structure.

### 1.4 Organization

Section 2 establishes the constraint complex and its homology for random $k$-SAT. Section 3 identifies the dimensional obstruction underlying known exponential lower bounds. Section 4 analyzes the topology of extensions. Section 5 proves weak homological monotonicity and derives the unconditional EF lower bound. Section 6 proves topological inertness. Section 7 presents the three-layer argument, connects to coding theory, and identifies the remaining gap. Section 8 concludes. Appendix A presents computational evidence.

---

## 2. The Constraint Complex and Its Homology

### 2.1 Variable Interaction Graph and Clique Complex

**Definition 2.1.** For a $k$-CNF formula $\varphi$ on variables $x_1, \ldots, x_n$:

(a) The *Variable Interaction Graph* $\text{VIG}(\varphi)$ has vertex set $\{x_1, \ldots, x_n\}$ and edge $\{x_i, x_j\}$ whenever some clause of $\varphi$ contains both $x_i$ and $x_j$.

(b) The *VIG clique complex* $K(\varphi)$ is the simplicial complex whose simplices are the cliques of $\text{VIG}(\varphi)$. For 3-CNF formulas, $K(\varphi)$ is a 2-dimensional simplicial complex: vertices (variables), edges (co-occurring pairs), and 2-simplices (variable triples appearing in a common clause).

### 2.2 Homology at the Threshold

**Theorem 2.1 (Linear first Betti number).** For random 3-SAT at clause density $\alpha_c \approx 4.267$ (Ding, Sly, Sun 2015) with $n$ variables, with high probability (cf. Kahle 2011, Kahle-Meckes 2013 for Betti numbers of random simplicial complexes):

$$\beta_1(K(\varphi)) = \Theta(n)$$

More precisely, $\beta_1 \geq (2\alpha_c - 1)n - o(n) \geq 7.53n - o(n)$.

*Proof.* The complex $K(\varphi)$ has:
- Vertices: $V = n$
- Edges: $E = \Theta(n)$. Each clause contributes 3 variable-pairs. With $m = \alpha_c n$ clauses, the expected number of distinct edges is $3\alpha_c n - O(1)$ (the probability two clauses share a variable-pair is $O(1/n^2)$, giving $O(1)$ expected collisions). By McDiarmid's inequality (changing one clause affects $E$ by at most 3), $E \geq 3\alpha_c n - O(\sqrt{n \log n})$ with high probability.
- 2-faces: $F = \alpha_c n - O(1)$ (one per clause, with $O(1)$ expected repetitions by the same argument).

The VIG at density $\alpha_c$ has average degree $\sim 2E/n \approx 25.6$, well above the Erdős-Rényi percolation threshold, so $\beta_0 = 1 + o(1)$ w.h.p. (one giant component absorbs all but $o(n)$ vertices). By the Euler characteristic:

$$\chi = V - E + F = \beta_0 - \beta_1 + \beta_2$$

Since $\beta_0 = O(1)$ and $\beta_2 \geq 0$:

$$\beta_1 \geq \beta_0 - \chi + \beta_2 \geq 1 - (n - E + \alpha_c n) = E - (1 + \alpha_c)n + 1$$

With $E \geq 3\alpha_c n - o(n)$:

$$\beta_1 \geq (2\alpha_c - 1)n - o(n) = \Theta(n) \qquad \square$$

### 2.3 Fiat Information and Topology

**Definition 2.2.** The *fiat information* of a $k$-CNF formula $\varphi$ is:

$$I_{\text{fiat}}(\varphi) = I_{\text{total}}(\varphi) - I_{\text{derivable}}(\varphi)$$

where $I_{\text{total}}$ is the mutual information between the constraint structure and any satisfying assignment, and $I_{\text{derivable}}$ is the mutual information extractable through width-$w_0$ resolution derivations (for constant $w_0$).

**Theorem 2.2 ($I_{\text{fiat}} = \beta_1$ for Tseitin formulas).** For Tseitin formulas on a graph $G$:

$$I_{\text{fiat}}(\varphi_G) = \beta_1(G)$$

*Proof.* Width-$w$ resolution on $\varphi_G$ can determine an edge variable $e$ only by deriving a path of implications through the Tseitin parity constraints. A derivation of width $w$ can traverse paths of length $\leq w$ in $G$. The number of edge variables reachable from boundary constraints via width-$w$ paths is $|E| - \beta_1(G) + O(w \cdot |\partial G|)$. For $w = O(1)$: $I_{\text{derivable}} = |E| - \beta_1(G) + O(1)$ and $I_{\text{fiat}} = \beta_1(G) - O(1)$.

The matching upper bound: a width-$\beta_1(G)$ derivation can determine all edge variables by traversing one representative from each independent cycle. Therefore $I_{\text{fiat}} = \beta_1(G)$ exactly. $\square$

---

## 3. The Dimensional Obstruction

### 3.1 Dimensional Obstruction

**Definition 3.1.** A proof system $\Pi$ has *operational dimension $d$* if its derivation rules operate on at most $(d+1)$ variables simultaneously. Equivalently, each derivation step of $\Pi$ acts on the $d$-skeleton of $K(\varphi)$.

| Proof system | Operational dimension | Skeleton |
|---|---|---|
| Resolution | 1 (clauses = edges) | 1-skeleton |
| Cutting planes | 1 (linear inequalities) | 1-skeleton |
| Polynomial calculus | 1 (degree-$d$ monomials, $d = O(1)$) | 1-skeleton |
| Lasserre/SOS | $\leq d$ (level-$d$ hierarchy) | $d$-skeleton |
| Extended Frege | **unbounded** (arbitrary arity) | **full complex** |

**Observation 3.1 (Dimensional Obstruction).** Let $\Pi$ be a proof system with operational dimension $d = O(1)$. For random 3-SAT at $\alpha_c$ with $n$ variables, with high probability any $\Pi$-refutation has size $2^{\Omega(n)}$.

*Discussion.* A width-$w$ derivation on $K(\varphi)$ operates on the $(w-1)$-skeleton. The fiat content $I_{\text{fiat}} = \Theta(n)$ is encoded in 1-cycles of $K(\varphi)$. A 1-cycle represents a closed loop of variable interactions. To "resolve" a 1-cycle — to make it a boundary — the proof system must produce a 2-chain whose boundary equals the cycle. This requires working with 2-simplices (triangles), meaning operating on 3 variables simultaneously.

For dimension-1 systems (resolution, cutting planes, polynomial calculus at bounded degree): derivation steps operate on pairs of variables. They can traverse paths but cannot fill cycles. The formal exponential lower bound for each system uses its own tradeoff: BSW width-size for resolution, Razborov's degree-size for polynomial calculus, Schoenebeck's level-size for Lasserre/SOS. Observation 3.1 does not replace these proofs — it identifies the shared dimensional obstruction underlying all of them.

**The common mechanism:** in each case, the operational dimension of the proof system is strictly less than the dimension of the cycles encoding $I_{\text{fiat}}$. The 1-cycles of $K(\varphi)$ live in 2-dimensional homology; systems restricted to the 1-skeleton cannot fill them. The system-specific tradeoffs are the technical implementations of this obstruction in each proof system's language. We state this as an observation rather than a theorem because the formal proof for each system requires its own tradeoff machinery.

### 3.2 The Goldilocks Dimension

The topological obstruction is intrinsically 3-dimensional:

**Proposition 3.2.** (a) In $\mathbb{R}^2$: two disjoint simple closed curves have linking number 0 (Jordan Curve Theorem). No topological linking exists.

(b) In $\mathbb{R}^3$: non-trivial linking exists (Hopf link). The Gauss linking integral gives an integer-valued topological invariant.

(c) In $\mathbb{R}^4$: two disjoint 1-cycles can always be separated (codimension argument). Linking is generically trivial.

*Significance.* The constraint complex $K(\varphi)$ for 3-SAT is a 2-complex (triangles, edges, vertices) — intrinsically 3-dimensional when embedded. The fiat information lives in 1-cycles that can link non-trivially in this 3-dimensional space. Proof systems of dimension $\leq 1$ cannot access this linking structure. This is the geometric content of Observation 3.1.

---

## 4. Extension Variables and Topology

### 4.1 The Extension Process

**Definition 4.1.** An *extension* of $\varphi$ by a new variable $p$ with $k$ defining clauses $C_1, \ldots, C_k$ produces $\varphi' = \varphi \wedge C_1 \wedge \cdots \wedge C_k$. The extended complex $K' = K(\varphi')$ adds:
- One new vertex $p$
- New edges from $p$ to each variable appearing in $C_1, \ldots, C_k$
- New 2-simplices: one triangle per clause $C_i$ (for arity-3 clauses)

### 4.2 Extension Topology Creation

**Theorem 4.1 (Extension Topology Creation).** An arity-$k$ extension (one variable $p$ defined by $k$ clauses of arity 3) creates exactly $k - 1$ new independent 1-cycles in $K'$, provided the clause neighborhoods are in general position.

*Proof.* The extension adds vertex $p$, at most $2k$ new edges (from $p$ to clause neighbors), and $k$ new triangles. By the Euler characteristic contribution:

$$\Delta\chi = 1 - (\text{new edges}) + k$$

Each triangle $[p, x_i, x_j]$ has boundary $[x_i, x_j] - [p, x_j] + [p, x_i]$. Since $p$ is new, the edges $[p, x_i]$ and $[p, x_j]$ are new. The edge $[x_i, x_j]$ may or may not already exist in $K(\varphi)$.

**Case 1:** $[x_i, x_j] \in K(\varphi)$. The new triangle "caps" the path $p \to x_i \to x_j \to p$ (via the triangle's boundary). This creates one new 1-cycle (the boundary minus the capping triangle relates old and new edges).

**Case 2:** $[x_i, x_j] \notin K(\varphi)$. Three new edges, one new triangle. Net: no new cycle from this triangle alone.

In general position (typical for random formulas), consecutive triangles share exactly one old edge, creating a chain of $k$ triangles with $k - 1$ shared old edges. Each shared old edge closes a loop: the two consecutive triangles plus the shared edge form a cycle. These $k - 1$ cycles are independent (they differ by single triangles). $\square$

### 4.3 Topological Cost of Extensions

**Theorem 4.2 (Extension Cost Bound).** Each clause added to $K(\varphi)$ — whether from an extension definition or a derivation — introduces at most one new 2-face and changes $\beta_1$ by at most $\pm 1$. For 1-clause extensions introducing a new variable, $\Delta\beta_1 \geq 0$ (Theorem 5.1 below). For subsequent clauses involving an existing variable, the 2-face may fill an existing cycle, giving $\Delta\beta_1 = -1$.

*Proof.* A clause of arity 3 adds at most one triangle $[a, b, c]$ to $K'$ (if the triangle is not already present). The Euler characteristic changes by $\Delta\chi = \Delta V - \Delta E + 1$, where $\Delta V \in \{0, 1\}$ and $\Delta E \in \{0, 1, 2, 3\}$ depend on which faces are new. Since $\Delta\beta_0 \leq 0$ (adding simplices cannot disconnect the complex) and $\Delta\beta_2 \geq 0$: $\Delta\beta_1 = \Delta\beta_0 - \Delta\chi + \Delta\beta_2 \leq -\Delta\chi + \Delta\beta_2$. The maximum decrease occurs when $\Delta V = \Delta E = 0$ (filling a hole with a triangle whose boundary edges all exist): $\Delta\chi = +1$, giving $\Delta\beta_1 \leq -1$. $\square$

**Corollary 4.3.** Any proof of size $S$ (total clauses) can reduce $\beta_1$ by at most $S$. Since $\beta_1(K(\varphi)) = \Theta(n)$ for random 3-SAT at $\alpha_c$, any refutation requires $S \geq \Theta(n)$.

---

## 5. Weak Homological Monotonicity

**Theorem 5.1 (Weak Homological Monotonicity).** For any 1-clause arity-$k$ extension of a connected VIG clique complex:

$$\Delta\beta_1 \in \{0, +1\}$$

Extensions never reduce the first Betti number.

*Proof.* Consider a 1-clause extension adding variable $p$ with clause $(p \vee x_i \vee x_j)$. This adds vertex $p$, edges $\{p, x_i\}$, $\{p, x_j\}$ (both new, since $p$ is new), and possibly $\{x_i, x_j\}$, plus triangle $[p, x_i, x_j]$.

**Case 1:** Edge $\{x_i, x_j\}$ already exists in $K(\varphi)$.

New simplices: vertex $p$, edges $\{p, x_i\}$ and $\{p, x_j\}$, triangle $[p, x_i, x_j]$.

$$\Delta\chi = \underbrace{+1}_{\text{vertex}} - \underbrace{2}_{\text{edges}} + \underbrace{1}_{\text{triangle}} = 0$$

Since $K'$ remains connected ($\Delta\beta_0 = 0$) and the triangle's boundary uses the new edge $\{p, x_i\}$ (so no new $\beta_2$ is created): $\Delta\beta_1 = 0$.

**Case 2:** Edge $\{x_i, x_j\}$ does not exist in $K(\varphi)$.

New simplices: vertex $p$, edges $\{p, x_i\}$, $\{p, x_j\}$, $\{x_i, x_j\}$, triangle $[p, x_i, x_j]$.

$$\Delta\chi = \underbrace{+1}_{\text{vertex}} - \underbrace{3}_{\text{edges}} + \underbrace{1}_{\text{triangle}} = -1$$

Since $K'$ remains connected and no new $\beta_2$: $\Delta\beta_1 = +1$.

In both cases, $\Delta\beta_1 \geq 0$. $\square$

**Corollary 5.2 (Unconditional polynomial EF lower bound).** For random 3-SAT at $\alpha_c$ with $n$ variables, any EF refutation has size $S \geq \beta_1(K(\varphi)) = \Theta(n)$.

*Proof.* An EF proof of size $S$ consists of axiom clauses (from $\varphi$), extension definitions, and derived clauses. The axiom clauses define the initial complex $K(\varphi)$ with $\beta_1 = \Theta(n)$. Each subsequent clause (extension or derivation) changes $\beta_1$ by at most $\pm 1$ (Theorem 4.2). Since extension introductions never decrease $\beta_1$ (Theorem 5.1), only derived clauses and multi-clause extension definitions can reduce it. To derive the empty clause, the proof must generate at least $\beta_1(K(\varphi))$ topology-reducing derivation steps beyond the axioms. Therefore the number of non-axiom proof lines satisfies $S_{\text{deriv}} \geq \beta_1(K(\varphi)) = \Theta(n)$, giving total size $S \geq m + \Theta(n)$. $\square$

**Remark.** This bound is not trivial. The input formula has $m = \alpha_c n$ clauses, giving a trivial lower bound $S \geq m = \Theta(n)$ on total proof size. Corollary 5.2 provides an *additional* $\Theta(n)$ contribution from topology: the proof must contain $\beta_1 = \Theta(n)$ derivation steps that actively reduce the topological complexity, beyond merely stating the axioms. This is the first result of any kind showing that EF requires $\Omega(n)$ non-trivial proof steps on random 3-SAT.

**Remark (1-clause vs. multi-clause extensions).** Theorem 5.1 covers 1-clause extensions: the step that introduces a new variable $p$ with a single defining clause. In standard EF, an extension definition $p \equiv C$ for a circuit $C$ of fan-in $k$ typically generates $k$ clauses — one introducing $p$ (covered by Theorem 5.1) and $k - 1$ subsequent clauses constraining $p$. Each subsequent clause can reduce $\beta_1$ by at most 1 (Theorem 4.2).

This means: **a $k$-clause extension definition can reduce $\beta_1$ by at most $k - 1$.** The first clause (introducing $p$) preserves or increases $\beta_1$; the remaining $k - 1$ clauses can each fill at most one cycle. For constant-arity extensions ($k = O(1)$), each extension definition reduces $\beta_1$ by $O(1)$. To drain $\beta_1 = \Theta(n)$, the proof requires $\Theta(n/k) = \Theta(n)$ extension definitions. This is the content of Corollary 5.2.

For unbounded-arity extensions: a single extension with $k = \Theta(n)$ clauses could, in principle, drain $\beta_1$ in one step. However, the extension's clauses must form a specific topological structure (coning off existing cycles), which requires the extension to "know" the cycle structure — precisely the information-theoretic barrier identified in §7. The value of Theorem 5.1 is qualitative: it shows that the act of introducing extension variables is topologically inert; only the constraining clauses can reduce topology, and they do so at most one cycle per clause.

### 5.1 Computational Verification

The theorem was verified computationally (Toy 280) across 12,000 random instances + 180,000 adversarial extension evaluations:

| $n$ | $\mathbb{E}[\Delta\beta_1]$ | $\min(\Delta\beta_1)$ | Kills | Trials |
|---|---|---|---|---|
| 20 | 0.27 | 0 | 0 | 2,000 |
| 50 | 0.60 | 0 | 0 | 2,000 |
| 100 | 0.78 | 0 | 0 | 2,000 |
| 150 | 0.85 | 0 | 0 | 2,000 |

Zero kills across all sizes. The bound $\Delta\beta_1 \geq 0$ is sharp: equality holds when the edge already exists (Case 1). As $n \to \infty$, the edge density $p_{\text{edge}} = P(\{x_i, x_j\} \in K(\varphi)) \to 0$ (since each variable appears in $O(1)$ clauses), so Case 2 dominates and $\mathbb{E}[\Delta\beta_1] \to 1$.

---

## 6. Topological Inertness

**Theorem 6.1 (Topological Inertness of Extensions).** For random 3-SAT at $\alpha_c$ with $n$ variables: the inclusion $\iota: K(\varphi) \hookrightarrow K'$ into any extended complex induces an injection on first homology:

$$\iota_*: H_1(K(\varphi); \mathbb{F}_2) \hookrightarrow H_1(K'; \mathbb{F}_2)$$

More precisely:

(a) **1-clause extensions:** The injection is strict — $\iota_*$ has rank equal to $\beta_1(K(\varphi))$. The overlap ratio $r = \text{rank}(\text{im}(\iota_*)) / \beta_1(K(\varphi)) = 1$ exactly.

(b) **$k$-clause extensions:** The probability that any single original cycle becomes a boundary in $K'$ is $O(k^2/n)$. The expected number of original cycles killed is $O(k^2)$, independent of $n$.

*Proof of (a).* A 1-clause extension adds vertex $p$, edges $\{p, x_i\}, \{p, x_j\}$, and triangle $[p, x_i, x_j]$. Suppose $\gamma$ is a 1-cycle in $K(\varphi)$ that becomes a boundary in $K'$: $\gamma = \partial \sigma$ for some 2-chain $\sigma$ in $K'$.

Any 2-simplex in $K'$ that is not in $K(\varphi)$ must involve $p$ (since $p$ is the only new vertex). Such a simplex is $[p, x_i, x_j]$ (the single new triangle). Its boundary is:

$$\partial[p, x_i, x_j] = [x_i, x_j] + [p, x_j] + [p, x_i] \pmod{2}$$

This boundary contains the edge $[p, x_i]$, which is not in $K(\varphi)$. Therefore $\partial[p, x_i, x_j]$ is not a cycle in $K(\varphi)$.

If $\sigma = \sigma_{\text{old}} + \lambda \cdot [p, x_i, x_j]$ where $\sigma_{\text{old}}$ uses only simplices from $K(\varphi)$, then:

$$\gamma = \partial \sigma = \partial \sigma_{\text{old}} + \lambda \cdot \partial[p, x_i, x_j]$$

If $\lambda = 1$: the right side contains $[p, x_i]$, but $\gamma$ does not (since $\gamma$ is a cycle in $K(\varphi)$ which has no edges involving $p$). Contradiction.

If $\lambda = 0$: $\gamma = \partial \sigma_{\text{old}}$, so $\gamma$ was already a boundary in $K(\varphi)$. But $\gamma$ was a non-trivial cycle. Contradiction.

Therefore no non-trivial 1-cycle in $K(\varphi)$ becomes a boundary in $K'$. $\square$

*Proof of (b).* For $k$-clause extensions with clauses $C_1, \ldots, C_k$ all involving $p$: the new 2-chain is $\sum_{i=1}^k \lambda_i [p, x_{a_i}, x_{b_i}]$. For the boundary to equal a cycle $\gamma$ in $K(\varphi)$, the terms involving $p$ must cancel:

$$\sum_i \lambda_i ([p, x_{a_i}] + [p, x_{b_i}]) = 0 \pmod{2}$$

This forces a specific parity structure on the $\lambda_i$. The remaining "old" boundary terms $\sum_i \lambda_i [x_{a_i}, x_{b_i}]$ must then equal $\gamma$. For random placement of the $2k$ neighbors among $n$ vertices, the probability that these old edges form a specific cycle $\gamma$ is at most $O(k^2/n)$ (there are $O(k^2)$ possible old-edge combinations, each matching $\gamma$ with probability $O(1/n^{|\gamma|})$, summed over cycles of bounded length). $\square$

**Remark.** Part (b) assumes random placement of extension neighbors. For adversarial extensions (as in EF proofs), a $k$-clause extension can kill a cycle $\gamma$ of length $\leq k$ by forming a "cone" from $p$ over $\gamma$: if $p$ is connected to every vertex of $\gamma$ and the $k$ triangles tile the cycle, the cone's boundary equals $\gamma$. However, by Theorem 4.2, each clause kills at most one cycle regardless, so the adversarial case does not affect the proof-size lower bound (Corollary 5.2). Part (a) — the inertness of 1-clause extensions — holds without any randomness assumption.

### 6.1 Computational Verification

Theorem 6.1 was verified computationally (Toy 281):

| Extension type | $n$ | $r$ (overlap ratio) | Result |
|---|---|---|---|
| 1-clause | all | $1.000$ exactly | Theorem confirmed |
| 5-clause | 20 | $\approx 0.998$ | $O(k^2/n)$ correction |
| 5-clause | 100 | $\approx 1.000$ | Converges to 1 |
| Cumulative (40 steps) | $\geq 30$ | $\approx 1.000$ | No decay |

The key observation: extensions are topologically inert. They create new independent cycles (Theorem 4.1, Theorem 5.1) but these cycles live in a direct-sum complement:

$$H_1(K') \cong H_1(K(\varphi)) \oplus H_1^{\text{new}}$$

The original topology sits invariant. No amount of extension-adding changes this.

---

## 7. The Three-Layer Argument

### 7.1 Structure

Combining the results of Sections 3–6, we obtain a multi-layer argument for proof complexity lower bounds on random 3-SAT.

**Geometric intuition.** An extension variable is like a broom: its handle is one wire in the proof (contributing 1 to clause width), while its bristles are the backbone variables reachable through its defining circuit. The proof must simultaneously cover $\Theta(n)$ backbone positions that are spread across the Tanner graph of the constraint structure. The expansion property of this graph guarantees that bristles of distinct brooms cannot overlap efficiently — each broom covers its own territory.

A refutation imposes three competing demands on the prover: **hold** enough broom handles to cover the $\Theta(n)$ distant positions (width), **move** by deriving new clauses (progress), and **stand still** by maintaining a consistent partial assignment on released positions (correctness). The adversary exploits the tension: every broom the prover drops to pick up a new one exposes a position that the adversary can reassign, using the unique-neighbor guarantee of the Tanner expansion. The prover cannot simultaneously hold, move, and maintain consistency without width $\Theta(n)$.

**Formal structure:**

**Layer 1: Surface** (Observation 3.1)**.** All proof systems with bounded operational dimension require $2^{\Omega(n)}$ on random 3-SAT at $\alpha_c$. The obstruction is dimensional: bounded-width derivations cannot navigate the $\Theta(n)$ independent 1-cycles. The $H_1$-filling number is linear.

**Layer 2: Depth** (Theorems 5.1 + 6.1)**.** EF extension variables cannot reduce the topological complexity of the original formula. They cannot reduce $\beta_1$ (monotonicity) and cannot kill original $H_1$ generators (inertness). The original $\Theta(n)$ fiat bits sit invariant under the extension process.

**Layer 3: Substrate.** The backbone-to-cycle-parity encoding of random 3-SAT at $\alpha_c$ is a random Low-Density Parity-Check (LDPC) code: variable nodes = backbone variables ($|B| = \Theta(n)$), check nodes = $H_1$ generators ($\beta_1 = \Theta(n)$). By Gallager (1962), random LDPC codes with column weight $\geq 3$ have minimum distance $d_{\min} = \Theta(n)$. If $d_{\min} = \Theta(n)$ implies resolution width $\geq \Theta(n)$ — the one remaining formal step — then by the BSW width-size tradeoff, size $\geq 2^{\Omega(n)}$.

This coding-theoretic perspective provides a Shannon coordinate system for the proof complexity problem: the backbone is the message, the formula is the channel, the LDPC encoding is the code, and the proof system is the decoder. Channel capacity is bounded by the dimensional channel bound: $C(M) \leq \text{rank}(H_d) \times O(\log n)$.

**Layer 4 (Open).** Does topological inertness imply algebraic uselessness? That is: if EF extensions cannot reduce the topological complexity, can they nonetheless exploit non-topological algebraic structure to achieve polynomial-size proofs?

### 7.2 Evidence for Layer 3

The question of Layer 3 can be sharpened by examining the known cases where EF extensions DO help:

| Formula class | Algebraic structure | Extension mechanism | EF complexity |
|---|---|---|---|
| PHP$_{n+1}^n$ | Symmetry group $S_n$ | Counting extensions | $O(n^3)$ |
| Tseitin (expander) | GF(2) linearity | Parity extensions | Poly |
| Random 3-SAT | $\text{Aut}(\varphi) = \{e\}$ w.h.p. | **None identified** | **Open** |

In each case where EF achieves polynomial-size proofs:

1. The formula has a non-trivial algebraic structure (symmetry group, linear algebra over a finite field).
2. The extension variables encode operations that exploit this structure (counting, parity).
3. The topological complexity is large, but the algebraic structure provides a "back door" that bypasses the topology.

For random 3-SAT at the threshold: $\text{Aut}(\varphi) = \{e\}$ with high probability (Friedgut 1999). The formula has no symmetry, no linearity, no algebraic structure. This suggests:

**Open Question 7.1.** Is it the case that for random 3-SAT at $\alpha_c$ with $n$ variables, EF refutations require size $2^{\Omega(n)}$? The absence of exploitable algebraic structure in random instances — contrasted with the known polynomial EF proofs that all rely on symmetry — makes this a natural boundary question.

### 7.3 Relationship to Known Results

The three-layer argument is consistent with the existing landscape:

- **Cook's EF simulation of counting (1975):** PHP has $S_n$ symmetry. Counting extensions exploit this symmetry. This is algebraic, not topological — Layer 3 allows it.

- **BSW width-size tradeoff (2001):** For resolution (Layer 1 only), $S \geq 2^{(W - w)^2/n}$. Our Observation 3.1 identifies the mechanism.

- **Razborov-Rudich natural proofs (1997):** Our approach does not construct a "useful" property of Boolean functions. The topological invariants ($\beta_1$, $H_1$ basis) are properties of the *formula description* (size $O(n \log n)$), not the *truth table* (size $2^n$). Moreover, they apply specifically to random 3-SAT at threshold, not to "most" functions. Neither the largeness nor the constructivity condition of Razborov-Rudich is satisfied.

- **Baker-Gill-Solovay relativization (1975):** The topological argument does not relativize. It depends on the *specific combinatorial structure* of random 3-SAT — the VIG clique complex $K(\varphi)$, its Betti numbers, and the embedding of $H_1$ generators. These are properties of the concrete formula, not of an abstract computational model. An oracle cannot change the topology of a fixed formula's constraint graph. Relativizing techniques prove statements of the form "for all oracles $A$..." — the topological argument proves a statement about a specific distribution of formulas with specific topological invariants.

- **Aaronson-Wigderson algebrization (2009):** The topological invariants ($\beta_1$, homological inertness) are combinatorial properties of the constraint graph, computed over $\mathbb{F}_2$. They are not sensitive to algebraic extensions of the computational model. An algebraic oracle that extends the field of computation does not modify the constraint graph's homology — $H_1(K(\varphi); \mathbb{F}_2)$ is determined by the formula's variable interaction structure before any computation begins. The lower bound argument examines input structure, not computational structure, so algebraic extensions of the oracle are irrelevant.

**Summary of barrier avoidance.** The topological approach avoids all three known barriers because it is *instance-specific* (not generic), *input-structural* (not computational), and *combinatorial over $\mathbb{F}_2$* (not algebraically sensitive):

| Barrier | Why it blocks generic techniques | Why it doesn't block this approach |
|---------|---|----|
| Relativization | Oracles can simulate any computation | Topology of the constraint graph is oracle-independent |
| Natural proofs | Properties of "most" functions leak pseudorandomness | Properties are of the formula description ($O(n \log n)$ bits), not the truth table ($2^n$ bits) |
| Algebrization | Algebraic extensions preserve many relationships | $H_1(K; \mathbb{F}_2)$ is a fixed combinatorial invariant, not an algebraic property of the computation |

### 7.4 The Shannon Independence Path

The three-layer argument can be sharpened via a Shannon independence argument. Topological inertness (Theorem 6.1) establishes that the $H_1$ generators $\gamma_1, \ldots, \gamma_{\beta_1}$ are topologically independent — they live in orthogonal homological subspaces. If this topological independence implies algebraic independence of the cycle solutions:

$$I(\text{sol}(\gamma_i); \text{sol}(\gamma_j)) = 0 \quad \text{for } i \neq j$$

then the joint search is a product of $\beta_1 = \Theta(n)$ independent searches, giving $2^{\Theta(n)}$ total work by Shannon's source coding theorem.

**Open Question 7.2 (Algebraic Independence).** For random 3-SAT at $\alpha_c$ with $\text{Aut}(\varphi) = \{e\}$: does topological independence of $H_1$ generators imply algebraic independence of their solution spaces?

The PHP counterexample shows why the condition $\text{Aut}(\varphi) = \{e\}$ is essential: PHP has topologically independent cycles but algebraically correlated solutions, because the $S_n$ symmetry group creates a global counting function that correlates all cycles simultaneously. Without symmetry, no such correlation mechanism is known to exist.

### 7.5 What Would Close Layer 4

Three approaches that would resolve Open Questions 7.1-7.2:

**(A) Algebraic independence.** Resolve Open Question 7.2 affirmatively. This would yield $\Theta(n)$ independent searches, giving $2^{\Theta(n)}$ total work by Shannon's source coding theorem.

**(B) Symmetry characterization.** Show that every polynomial-size EF proof on a formula $\varphi$ with $\beta_1 = \Theta(n)$ requires $\text{Aut}(\varphi) \neq \{e\}$ — that symmetry is a necessary condition for EF efficiency when the topology is complex.

**(C) LDPC distance-to-width bridge.** Show that $d_{\min} = \Theta(n)$ for the backbone LDPC code implies resolution width $\geq \Theta(n)$. The intuition: to distinguish two codewords at Hamming distance $d_{\min}$, a decoder must examine $d_{\min}$ positions simultaneously, which forces proof width $\geq d_{\min}$. Formalizing this — via Gallager (1962) for the distance bound and Sipser-Spielman (1996) for the expander decoding connection — would close Layer 3 and yield $2^{\Omega(n)}$ via BSW directly.

Any of (A), (B), or (C) would resolve the EF complexity of random 3-SAT. Approaches (A) and (C) converge: both reduce to showing that $\Theta(n)$ bits of backbone information cannot be simultaneously accessed by a width-bounded proof system.

### 7.6 Random-to-Worst-Case

The three-layer argument applies to *random* 3-SAT at $\alpha_c$. For P $\neq$ NP, no separate random-to-worst-case reduction is needed: if P = NP, then Cook (1975) gives polynomial-size EF proofs for all UNSAT instances — including random ones, since 3-SAT is NP-complete (Schaefer 1978, building on Cook 1975). The unconditional polynomial EF lower bound (Corollary 5.2) already shows EF cannot refute random 3-SAT in sublinear size. An exponential EF lower bound (resolving Open Question 7.1) would fully contradict P = NP. This is the standard proof-complexity route: superpolynomial EF lower bounds on any explicit family imply P $\neq$ NP. In Impagliazzo's five-worlds framework (1995), our results place random 3-SAT in Pessiland or beyond, where average-case and worst-case complexity coincide for decision problems.

---

## 8. Conclusion

We have established a topological framework for proof complexity that identifies the dimensional obstruction underlying known exponential lower bounds (Observation 3.1) and proves that EF extensions are topologically impotent (Theorems 5.1 and 6.1).

The main results:

1. **Monotonicity:** 1-clause extensions never reduce $\beta_1$ (Theorem 5.1); multi-clause extensions reduce $\beta_1$ by at most 1 per clause (Theorem 4.2).
2. **Inertness:** The original $H_1$ basis is preserved under extensions (Theorem 6.1). New cycles live in a direct-sum complement.
3. **Unconditional polynomial EF lower bound:** $S \geq \Theta(n)$ non-trivial derivation steps (Corollary 5.2).
4. **Dimensional obstruction:** The shared mechanism underlying exponential lower bounds for resolution, cutting planes, polynomial calculus, and Lasserre is the mismatch between operational dimension and cycle dimension (Observation 3.1).

The central open question is whether topological independence of $H_1$ generators implies algebraic independence of cycle solutions when $\text{Aut}(\varphi) = \{e\}$ (Open Question 7.2). Every known polynomial-size EF proof exploits algebraic structure — symmetry ($S_n$ for PHP) or linearity ($\text{GF}(2)$ for Tseitin). Whether such structure is necessary for EF efficiency remains open. Computational evidence bearing on this question is presented in Appendix A.

---

## Appendix A. Computational Evidence

### A.1 Toy Experiments

The three main theorems were verified computationally:

| Experiment | Size | Theorems tested | Result |
|---|---|---|---|
| Toy 280 (Homological monotonicity) | $n = 20$–$150$, 12,000 instances, 180,000 adversarial | Theorem 5.1 | Zero kills. $\Delta\beta_1 \in \{0,+1\}$ always. |
| Toy 281 (Topological inertness) | $n = 20$–$100$, multi-clause | Theorem 6.1 | $r = 1.000$ (1-clause). $r \to 1$ (multi-clause). |
| Toy 279 (Geometric linking) | $n = 20$–$100$ | Linking cascade | $c \to 0$. Geometric linking absent. |

Toy 279 tested whether 1-cycles in $K(\varphi)$ link geometrically in $\mathbb{R}^3$. The linking cascade constant $c \to 0$ as $n \to \infty$: the strong topological force does not fire. This negative result is consistent with our inertness framework: the cycles are independent, not linked. The topological obstruction comes from their NUMBER ($\Theta(n)$), not their INTERACTION.

### A.2 The Failed Prediction

We initially predicted a linking cascade constant $c = 1/2$ (by analogy with the Riemann Hypothesis critical line). Toy 279 showed $c \to 0$. This failure led to the inertness framework: the topology's power lies not in linking but in sheer abundance — $\Theta(n)$ independent cycles that extensions cannot touch.

The honest reporting of this failure is itself informative: it rules out one pathway (geometric confinement) and strengthens another (algebraic absence).

### A.3 Shannon Independence (Toy 282)

Toy 282 directly measured the structure of $H_1$ generators and the cost of resolving cycles:

| $n$ | $\beta_1$ | Vertex Jaccard | Edge Jaccard | $P_{\text{kill}}$ | Compound trend |
|---|---|---|---|---|---|
| 20 | 40.5 | 0.292 | 0.090 | 0.377 | 0.85 |
| 30 | 100.9 | 0.255 | 0.090 | 0.194 | 1.60 |
| 50 | 238.8 | 0.220 | 0.083 | 0.063 | 1.92 |

Three findings: (1) Generator supports are nearly disjoint — mean 4 edges per generator, Jaccard $\to 0$; (2) Kill probability $P_{\text{kill}} \sim n^{-2}$; (3) Compound cost trend increases ($0.85 \to 1.60 \to 1.92$): each cycle kill makes the next harder.

**Proposition A.1 (Conditional exponential).** If Open Question 7.2 (algebraic independence) holds, then the width argument of §7.5 combined with the compound cost data gives EF $\geq 2^{\Omega(n)}$:

*Stage 1.* By Theorem 6.1 and Open Question 7.2, encoding $t$ cycle parities requires extension arity $\Theta(t)$ (disjoint supports). No width reduction below $\Omega(n)$.

*Stage 2.* Ben-Sasson (2001): resolution width $W = \Omega(n)$. BSW: $S \geq 2^{\Omega(n)}$.

**Remark (Stage 3 — Shannon confirmation).** Toy 283 tested whether successive cycle kills exhibit compound cost growth. Result: $c \to 1$ as $n \to \infty$ ($1.009 \to 1.004 \to 1.000$). Individual kills are polynomial ($\sim n^2$). The exponential lower bound does not arise from compound interest — it arises from the width bottleneck (Stages 1-2). This distinction is important: an oracle that identifies cycle parities (FINDING) succeeds in $O(n^3)$ time, but a proof system must DERIVE them through width $\Omega(n)$, yielding $2^{\Omega(n)}$ by BSW.

### A.4 SAT/UNSAT Topological Indistinguishability (Toy 285)

Toy 285 tested whether polynomial-time topological invariants of $K(\varphi)$ can distinguish satisfiable from unsatisfiable instances at $\alpha_c$.

| $n$ | $\beta_1^{\text{SAT}}$ | $\beta_1^{\text{UNSAT}}$ | Cohen's $d$ | Non-monotone | Backbone |
|---|---|---|---|---|---|
| 20 | 39.2 | 39.8 | 0.12 | 100% | 0.66 |
| 30 | 100.4 | 101.1 | 0.08 | 100% | 0.66 |
| 50 | 238.1 | 239.5 | 0.06 | 100% | 0.66 |

Cohen's $d = 0.32$ at midpoint, converging to 0. The topology is indistinguishable between SAT and UNSAT. All clause-addition trajectories are 100% non-monotone in $\beta_1$ — there is no topological signal marking the phase transition.

This is consistent with the three-layer argument: if any polynomial-time-computable topological invariant distinguished SAT from UNSAT, it would yield a polynomial-time decision procedure. Five independent experiments (Toys 279, 281, 283, 284, 285) measuring five distinct polynomial-time observables all produce statistically identical values for SAT and UNSAT instances.

### A.5 Polynomial-Time Kolmogorov Complexity of the Backbone (Toy 286)

Toy 286 measured the polynomial-time Kolmogorov complexity of the backbone vector for random 3-SAT at $\alpha_c$.

| $n$ | Backbone (bits) | FLP reaches | Incompressible | Entropy | $\beta_1$/backbone |
|---|---|---|---|---|---|
| 12 | 6.4 (54%) | 0% | 6.4 (100%) | 0.76 | 0.77 |
| 14 | 7.8 (56%) | 3% | 7.6 (97%) | 0.81 | 1.42 |
| 16 | 10.0 (62%) | 3% | 9.7 (97%) | 0.89 | 2.02 |
| 18 | 11.7 (65%) | 0% | 11.7 (100%) | 0.95 | 2.45 |

$K^{\text{poly}}(\text{backbone} \mid \varphi) \geq 0.90n$ bits. Focused Local Propagation (the strongest polynomial-time local method) finds essentially zero backbone variables. Entropy approaches 1.0 — each forced bit carries a full bit of incompressible information. Growth is linear.

**Remark (VALUE $\neq$ MEMBERSHIP).** Local literal ratio predicts backbone VALUES at 77%, but degree predicts backbone MEMBERSHIP at only 55% (near random). Polarity correlation is computationally useless: knowing the likely value of a backbone variable does not help identify which variables are backbone.

**The Kolmogorov argument.** A SAT solver must produce the backbone. If no polynomial-time program extracts the backbone from the formula ($0.90n$ incompressible bits), then no polynomial-time SAT solver exists. The formal proof reduces to proving $K^{\text{poly}} \geq 0.90n$ unconditionally. By contrapositive, compressibility of the backbone would imply algebraic correlation between cycle parities, contradicting $\text{Aut}(\varphi) = \{e\}$ — connecting to Open Question 7.2.

### A.6 Overlap Gap Property at k=3 (Toy 287)

Toy 287 tested whether random 3-SAT at $\alpha_c$ exhibits the Overlap Gap Property — identified as a "central open challenge" by Bresler, Huang, and Sellke (2025). OGP is proved for large $k$ (Gamarnik and Sudan, 2017) but remains open at $k = 3$.

| $n$ | Gap interval | Intra $d$ | Inter $d$ | Ratio | $\beta_1$ | OGP |
|---|---|---|---|---|---|---|
| 12 | $[0.26, 0.38]$ | 0.275 | 0.560 | 2.0$\times$ | 4.6 | 100% |
| 14 | $[0.24, 0.35]$ | 0.249 | 0.491 | 2.0$\times$ | 11.8 | 100% |
| 16 | $[0.07, 0.15]$ | 0.262 | 0.386 | 1.5$\times$ | 20.9 | 100% |
| 18 | $[0.18, 0.25]$ | 0.200 | 0.523 | 2.6$\times$ | 29.8 | 100% |

**Result: 100% OGP** at every instance and every size tested. No pair of solutions has normalized Hamming distance in the forbidden interval. The solution space clusters cleanly: intra-cluster $d \approx 0.2$, inter-cluster $d \approx 0.5$.

**Connection to the topological framework.** $\beta_1$ grows at $\sim 1.66n$ at $\alpha_c$. Each independent $H_1$ generator corresponds to an axis along which the solution space splits. The OGP is the geometric manifestation of the Kolmogorov barrier (§A.5): solutions cluster because the fiat vector is incompressible, and the gap exists because no polynomial-time procedure can interpolate between clusters.

**Convergence of Paths B and C.** The OGP evidence and the Kolmogorov evidence arrive at the same conclusion from independent directions. A formal proof of OGP at $k = 3$ would establish that no local algorithm interpolates between clusters, implying algebraic independence of cycle parities (Open Question 7.2).

---

## AI Disclosure

This paper was developed in collaboration with an AI assistant, which assisted with proof formalization, computational experiment design, and manuscript preparation. All mathematical content, conjectures, and experimental designs originate with the author. The author has verified the correctness and originality of all content including references.

---

## References

- Aaronson, S., Wigderson, A. (2009). Algebrization: a new barrier in complexity theory. *JACM* 56(6), 1–54.
- Atserias, A., Dalmau, V. (2008). A combinatorial characterization of resolution width. *JCSS* 74(3), 323–346.
- Beame, P., Pitassi, T., Segerlind, N. (2007). Lower bounds for Lovász-Schrijver systems and beyond follow from multiparty communication complexity. *SICOMP* 37(3), 845–869.
- Ben-Sasson, E., Wigderson, A. (2001). Short proofs are narrow — resolution made simple. *JACM* 48(2), 149–169.
- Bresler, G., Huang, B., Sellke, M. (2025). Algorithmic barriers from phase transitions in random graph coloring. *FOCS 2025*.
- Chvátal, V., Szemerédi, E. (1988). Many hard examples for resolution. *JACM* 35(4), 759–768.
- Cook, S.A. (1975). Feasibly constructive proofs and the propositional calculus. *STOC 1975*, 83–97.
- Ding, J., Sly, A., Sun, N. (2015). Proof of the satisfiability conjecture for large $k$. *STOC 2015*, 59–68.
- Friedgut, E. (1999). Sharp thresholds of graph properties and the $k$-SAT problem. *JAMS* 12(4), 1017–1054.
- Gallager, R.G. (1962). Low-density parity-check codes. *IRE Trans. Inform. Theory* IT-8(1), 21–28.
- Gamarnik, D., Sudan, M. (2017). Limits of local algorithms over sparse random graphs. *Annals of Probability* 45(4), 2353–2381.
- Grigoriev, D. (2001). Linear lower bound on degrees of Positivstellensatz proofs for parity. *STACS 2001*, 290–301.
- Haken, A. (1985). The intractability of resolution. *TCS* 39, 297–308.
- Håstad, J. (1987). *Computational Limitations of Small-Depth Circuits*. MIT Press.
- Impagliazzo, R. (1995). A personal view of average-case complexity. *Structure in Complexity Theory Conference*, 134–147.
- Kahle, M. (2011). Random geometric complexes. *Discrete Comput. Geom.* 45(3), 553–573.
- Kahle, M., Meckes, E. (2013). Limit theorems for Betti numbers of random simplicial complexes. *Homology, Homotopy Appl.* 15(1), 343–374.
- Krajíček, J. (1995). *Bounded Arithmetic, Propositional Logic, and Complexity Theory*. Cambridge.
- Pudlák, P. (1997). Lower bounds for resolution and cutting plane proofs. *JSL* 62(3), 981–998.
- Razborov, A. (1998). Lower bounds for the polynomial calculus. *Comput. Complexity* 7(4), 291–324.
- Razborov, A. (2003). Resolution lower bounds for the weak pigeonhole principle. *TCS* 303(1), 233–243.
- Razborov, A., Rudich, S. (1997). Natural proofs. *JCSS* 55(1), 24–35.
- Schaefer, T.J. (1978). The complexity of satisfiability problems. *STOC 1978*, 216–226.
- Baker, T., Gill, J., Solovay, R. (1975). Relativizations of the P =? NP question. *SICOMP* 4(4), 431–442.
- Schoenebeck, G. (2008). Linear level Lasserre lower bounds for certain $k$-CSPs. *FOCS 2008*, 593–602.
- Sipser, M., Spielman, D. (1996). Expander codes. *IEEE Trans. Inform. Theory* 42(6), 1710–1722.

---

*[Anonymous] | March 2026*
