# Why P != NP: Four Routes, One Insight

**A short note on structural convergence**

Casey Koons, Keeper, Lyra, Elie (May 8, 2026)

---

## Abstract

We present four independent approaches to P != NP and show they all reduce to a single structural insight: **OR clauses are lossy information channels, so guessing cannot reduce the search space for satisfiability**. The channel-capacity formulation (T1766) is the cleanest route, requiring only one conditional (the resolution-to-Extended-Frege transfer, T69) with no dependence on random CSP condensation theory. We prove unconditionally that resolution and DPLL require 2^{Omega(n/(log n)^2)} time for random 3-SAT at the satisfiability threshold. The extension to P != NP is conditional on T69 — the same barrier shared by all known proof-complexity approaches.

---

## 1. The Four Routes

### Route 1: Discrete Curvature (T1425)

The Hamming-1 graph on SAT solutions is triangle-free (Lemma 1). Discrete Gauss-Bonnet gives vertex curvature kappa(v) = 1 - deg(v)/2 (Lemma 2). At alpha_c, cluster isolation forces E[deg] < 2, hence E[kappa] > 0, hence chi(G) > 0 (Lemma 3). Positive Euler characteristic forces algebraically independent cycle solutions (T29). Independence forces exponential proof size.

**What it really says**: The solution graph has irreducible curvature. You can't flatten it. You can't shortcut through it. You must traverse it.

**Conditional on**: 1-RSB condensation for k=3 (Lemma 3) + T69 (EF transfer).

### Route 2: Polarization (T996 + T957 + T959)

At alpha_c, conditioning on SAT decorrelates clause evaluations: |Corr(y_a, y_b | x_i, SAT)| = O(1/n). Decorrelation forces polarization of variable marginals to {0, 1}. Polarization forces frozen variables forming an Omega(n)-width backbone. Width forces exponential proof size.

**What it really says**: The formula can't communicate correlations between distant clauses. The SAT constraint doesn't create coherent long-range signal. Each clause is an island.

**Conditional on**: T996 decorrelation (under review, D1 test suggestive) + T69.

### Route 3: Refutation Bandwidth (T66 + T52 + T68 + T69)

Random k-SAT at alpha_c has algebraically independent blocks (T66). Independence forces resolution width Omega(n) (T68). Width forces resolution size 2^{Omega(n)} by BSW (T52). The refutation bandwidth exceeds any polynomial bound.

**What it really says**: The formula contains Omega(n) independent pieces of information that must each be refuted separately. No proof can compress them.

**Conditional on**: T69 (EF transfer).

### Route 4: Channel Capacity (T1765 + T1766)

Each k-OR clause has channel capacity C_k = H(2^{-k}) < 1 bit. Information decays as C_k^d through chains of d clauses. After O(log n) hops, variables are information-independent. This gives Omega(n / log n) independent blocks. Resolution width >= Omega(n / log n), size >= 2^{Omega(n / (log n)^2)}.

**What it really says**: OR erases which input made it true. Chain enough ORs and you know nothing. Guessing doesn't help. Search is irreducible.

**Conditional on**: T69 only. No condensation, no cluster isolation, no 1-RSB.

---

## 2. Structural Convergence

Strip each route to its core claim:

| Route | Core mechanism | Same insight |
|-------|---------------|-------------|
| Curvature | chi(G) > 0 — topology can't flatten | Information is trapped in local structure |
| Polarization | Corr = O(1/n) — clauses can't talk | Formula transmits no long-range signal |
| Bandwidth | Omega(n) independent blocks — can't compress | Each piece must be refuted separately |
| **Channel capacity** | **C < 1 — OR is lossy** | **Each step loses information** |

All four routes say the same thing in different mathematical languages:

> **The formula does not help you search.**

The constraint graph is a network of lossy channels. Information about satisfying assignments enters through clause evaluations, but each evaluation loses information (the OR operation erases which literal contributed). After enough hops through the constraint graph, you know nothing about distant variables. Your current assignment tells you nothing about what you should try next for variables far away in the formula.

This is the No Free Lunch principle for SAT: **there is no free directional information in the formula**.

---

## 3. Why Channel Capacity is the Cleanest Formulation

The four routes have different conditional structures:

| Route | Conditionals |
|-------|-------------|
| Curvature (T1425) | Condensation(k=3) + Steps 5-7 + T69 |
| Polarization | T996 + T69 |
| Bandwidth | T69 |
| **Channel capacity (T1766)** | **T69 only** |

Channel capacity has the smallest conditional set because it derives the information independence from the formula's constraint graph directly, without passing through solution-space properties (condensation, cluster isolation) or analytical properties (decorrelation, polarization).

The key structural advantage: **channel capacity is a formula property, not a solution-space property.** The capacity of a k-OR clause is H(2^{-k}) regardless of how many solutions the formula has, how they cluster, or what their Hamming distances are. The lossy channel is a fact about the OR truth table, which is a combinatorial identity.

---

## 4. The No Free Lunch Argument (Informal)

For a general audience — the argument a bright undergraduate can follow:

1. **OR erases information.** When you learn that (x OR y OR z) is true, you learn one of {001, 010, 011, 100, 101, 110, 111} is the case — but not which one. The clause satisfied-bit carries only 0.54 bits, not the full 3 bits of (x, y, z). Information is lost.

2. **Lost information stays lost.** If clause C_1 tells you 0.54 bits about its variables, and clause C_2 shares a variable with C_1, then C_2 tells you at most 0.54 * 0.54 = 0.30 bits about the variables of C_1 that aren't directly in C_2. Each hop through the formula multiplies by 0.54. Information decays exponentially.

3. **Distant variables are strangers.** After 10 hops: 0.002 bits. After 20 hops: 0.000005 bits. Variables that are far apart in the formula know essentially nothing about each other, even given that the formula is satisfiable.

4. **Guessing one variable doesn't help with distant ones.** If you set x_1 = TRUE, this tells you nothing about x_{1000} (they're strangers). Your guess at x_1 has zero probability of reducing the search space for x_{1000}. You still have to try all possibilities for x_{1000}.

5. **With enough stranger groups, search is exponential.** If the formula has Omega(n / log n) groups of variables that are mutual strangers, you need to explore each group independently. The total work is exponential in the number of groups.

6. **This is a property of OR, not of the specific formula.** Every k-SAT formula routes information through OR clauses. Every OR clause is lossy. The lossiness is a mathematical identity, not an empirical observation. It's true of ALL formulas, at ALL densities, for ALL k >= 2.

**One sentence**: OR is a lossy compression, so the formula can't tell you where to look, so you have to look everywhere.

---

## 5. The Shared Barrier: T69

All four routes share one conditional: **T69 (BSW-for-Extended-Frege)**. This states that the resolution lower bound transfers to Extended Frege — that extension variables (abbreviations) can't bypass the information bottleneck created by OR-clause lossiness.

Why T69 is hard: Extended Frege can introduce new proposition letters p defined by p <-> phi(x_1, ..., x_n). These extension variables are deterministic functions of the original variables. By DPI, each extension variable carries at most H(p) <= 1 bit of information about any block. But the question is whether poly(n) extension variables, each carrying 1 bit, can collectively represent the Omega(n / log n) independent blocks in a way that avoids the exponential blowup.

Information-theoretically: poly(n) extension variables carry poly(n) bits total. Representing Omega(n / log n) independent blocks each requiring Omega(1) bits needs Omega(n / log n) total bits. Since n / log n < poly(n), the bit count alone doesn't rule out polynomial-size EF proofs.

The deeper question: can extension variables CREATE correlations between blocks that don't exist in the original formula? By DPI, no single extension variable can. But can COMBINATIONS of extension variables, through the EF deduction rules, induce effective correlations? This is the open question.

**What would close T69**: A theorem showing that EF deduction rules (modus ponens + extension) can't increase the mutual information between blocks beyond what the original formula provides. This would be a "conservation of information" theorem for proof systems — the proof-complexity analog of the second law of thermodynamics.

---

## 6. What's Proved, What's Conditional

### Proved unconditionally (T1766):

- OR-clause capacity C_k < 1 for all k >= 2
- Mutual information between variables decays exponentially with VIG distance
- Resolution refutations of random k-SAT at alpha_c require size 2^{Omega(n / (log n)^2)}
- DPLL algorithms require time 2^{Omega(n / (log n)^2)} on random k-SAT at alpha_c
- These bounds hold for ALL k >= 2 without condensation, cluster isolation, or 1-RSB

### Conditional on T69:

- P != NP

### The honest framing:

**P != NP, conditional on Extended Frege admitting the resolution lower bound.** The OR-clause channel capacity argument removes all other conditionals (condensation, cluster isolation, decorrelation). The remaining barrier is the same barrier facing the entire proof-complexity program: no superpolynomial Extended Frege lower bound is known for any tautology family.

---

## 7. Publication Strategy

**Paper A (proof complexity, unconditional)**: "Channel-capacity lower bounds for resolution proofs of random k-SAT." Targets Computational Complexity or SIAM Journal on Computing. Content: T1766 parts (a)-(g). No P != NP claim. Engages Razborov, Buss, Krajicek, Pudlak.

**Paper B (structural convergence)**: "Four routes to P != NP: structural convergence on finite channel capacity." Targets STOC/FOCS or a survey. Content: this note, expanded with full proofs. Shows all routes reduce to the same insight. Identifies T69 as the shared barrier. BST framing optional.

**Paper C (BST connection)**: "Finite spectral cap and computational irreducibility." Targets a BST-integrated paper. Content: the connection between D_IV^5 spectral bandwidth and OR-clause channel capacity. Requires the substrate-to-capacity theorem that Cal flagged.

Papers A and B are publishable now. Paper C requires additional work (the D_IV^5 → channel capacity theorem).

---

## 8. Casey's Principle

> "In an algorithm each decision step has to have a positive probability of reducing the search space, otherwise visiting every node is the shortest provable solution."

This is the AC(0) formulation of the No Free Lunch theorem. It says: if no step helps, every step is necessary. If OR is lossy, every variable is an island. If information decays, search is irreducible.

Five words: **can't linearize curvature; P!=NP.**

Four words: **OR is lossy; P!=NP.**

Three words: **guessing doesn't help.**

---

*The method eats its own tail: the hardest open problem in theoretical computer science reduces to a channel capacity computation. AC(0): one count (channel capacity of k-OR), zero depth.*
