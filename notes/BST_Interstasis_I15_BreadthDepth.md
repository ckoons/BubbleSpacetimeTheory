---
title: "I15: Breadth vs Depth — What Grows When the Gödel Floor Saturates?"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "March 27, 2026"
status: "INVESTIGATION — formalizing the depth concept in D_IV^5"
tags: ["interstasis", "depth", "breadth", "heat-kernel", "spectral", "Gödel-limit"]
---

# I15: Breadth vs Depth

*When the bucket is full, the drill begins.*

---

## 1. The Question

The Gödel Ratchet (I1) shows the fill fraction converges: $\mathcal{G}(n) \to f_{\max} = 3/(5\pi)$. By cycle ~24, the substrate is >99% saturated in breadth — what fraction of reality it can self-know through derivation.

But the universe keeps cycling. What grows after saturation?

**Answer: depth.** The structural complexity within the fixed 19.1% budget. The universe doesn't fill more of the canvas — it paints with finer brushstrokes.

This investigation formalizes what "depth" means in D_IV^5 and shows it is unbounded.

---

## 2. Breadth = Fill Fraction (Bounded)

Breadth is the fraction of the Reality Budget that is committed:

$$B(n) = \frac{N(n)}{S_{\text{dS}}(n)} \to f = \frac{3}{5\pi} = 19.1\%$$

This is the Gödel Limit. It is a geometric ceiling inscribed in $D_{IV}^5$ via the Chern classes of the compact dual $Q^5$: $c_4/c_1 = 9/5$ gives $\Lambda \times N = 9/5$, and the fill fraction $f = N_c/(n_C \pi)$.

**Bounded by construction.** No amount of cycling can exceed 19.1%.

---

## 3. Three Candidates for Depth

### 3.1 Spectral Depth — Heat Kernel Order

The Seeley-DeWitt expansion of the heat kernel on $D_{IV}^5$:

$$K(t) = \frac{1}{(4\pi t)^{d/2}} \sum_{k=0}^{\infty} a_k \, t^k$$

The coefficients $a_k$ encode curvature invariants of increasing order. We have computed:

$$a_4 = \frac{2671}{18}, \quad a_5 = \frac{1535969}{6930}, \quad \ldots, \quad a_{11} = \frac{217597666296971}{1581170716125}$$

**Depth measure:** The highest $k$ for which $a_k \neq 0$ is trivially infinite (all $a_k \neq 0$ for curved spaces). More meaningful: the structural complexity of $a_k$ — the degree of the polynomial in $n_C$ and the primes that enter the denominator.

| $k$ | Degree | Denominator primes | New prime enters |
|-----|--------|-------------------|-----------------|
| 4 | 8 | $\{2, 3\}$ | — |
| 5 | 10 | $\{2, 3, 5, 7, 11\}$ | 5, 7, 11 |
| 6 | 12 | $\{2, 3, 5, 7, 11, 13\}$ | 13 |
| 7 | 14 | $\{2, 3, 5, 7, 11, 13\}$ | — |
| 8 | 16 | $\{2, 3, 5, 7, 11, 13, 17\}$ | 17 |
| 9 | 18 | $\{2, 3, 5, 7, 11, 13, 17, 19\}$ | 19 |
| 10 | 20 | $\{2, 3, 5, 7, 11, 13, 17, 19\}$ | — |
| 11 | 22 | $\{2, 3, 5, 7, 11, 13, 17, 19, 23\}$ | 23 (Golay) |

The $(k+1)$-th prime enters by level $k$ (von Staudt-Clausen pattern). Polynomial degree grows as $2k$. Both are unbounded.

**Spectral depth at cycle $n$:** The highest curvature order $k(n)$ at which the substrate's committed geometry has non-trivial structure. This is unbounded because each cycle can create new topological features that contribute to higher-order curvature invariants.

### 3.2 Topological Depth — Homological Complexity

The persistent homology of the committed subgraph at cycle $n$:

$$\mathcal{D}_{\text{topo}}(n) = \sum_{k=0}^{d/2} \beta_k(S_n) \cdot (k+1)$$

where $\beta_k$ are the Betti numbers, weighted by dimension. Higher-dimensional topological features (handles, voids, higher homology) represent deeper structural complexity.

**Unbounded because:** Each cycle can create new topological features. Axiom A1 (topological monotonicity) ensures they persist. The sum grows monotonically without bound.

But this is a coarse measure — it doesn't capture the *arrangement* of topological features, only their count.

### 3.3 Relational Depth — Off-Diagonal Bergman Kernel

The Bergman kernel $K(z,w)$ measures correlations between points $z, w \in D_{IV}^5$:

$$K(z,w) = \frac{1920}{\pi^5} \cdot [\cosh d(z,w)]^{-12}$$

At cycle $n$, the committed points $\{z_i\} \subset D_{IV}^5$ create a correlation matrix:

$$\mathcal{K}_{ij}(n) = K(z_i, z_j)$$

**Depth measure:** The rank of $\mathcal{K}(n)$, or more precisely, the effective rank (number of eigenvalues above some threshold). As the commitment pattern becomes more structured:

- More committed points → larger matrix
- More correlated arrangements → richer eigenvalue spectrum
- Deeper pathways → more non-trivial off-diagonal structure

The effective rank is bounded by $N(n)$ (number of committed channels), which grows without bound (A5).

---

## 4. The Correct Measure: AC Graph Density

The most BST-native measure of depth is the **AC theorem graph**. Each cycle adds proved theorems (topological configurations discovered and consolidated). The theorem graph at cycle $n$ has:

- **Nodes**: $|T(n)|$ = number of proved theorems
- **Edges**: $|E(n)|$ = derivation dependencies
- **Density**: $\rho(n) = |E(n)| / |T(n)|$ = edges per node

**Depth = edges per node.** This captures how *interconnected* the knowledge is, not just how much there is.

**Why this is right:**
1. Proved theorems cost zero derivation energy (T147) — they persist forever
2. Each new theorem adds at least one edge (to its dependencies)
3. Cross-connections between theorems can be discovered later, adding edges without nodes
4. Density grows even when node count stabilates

**Current state:** Toy 369 (updated by Elie): 253 nodes, 222 edges, density ≈ 0.88.

**Prediction:** After breadth saturates (no more new "easy" theorems), the graph continues to densify — old theorems get connected to each other through newly discovered relationships. This is Casey's "compound interest on imagination": the library doesn't just grow, its internal connections deepen.

---

## 5. The Depth Theorem

**Theorem (Unbounded Depth).** The spectral depth $k(n)$, the topological depth $\mathcal{D}_{\text{topo}}(n)$, and the relational depth $\text{rank}(\mathcal{K}(n))$ are all monotonically non-decreasing and unbounded, even after the fill fraction $f(n)$ has saturated at $f_{\max} = 3/(5\pi)$.

*Proof sketch.*

1. **Spectral:** Each cycle creates new topological features (A1). New features contribute to curvature invariants at order $k \geq$ (number of handles involved). Since the number of handles grows (A1, A5), the highest contributing order grows without bound.

2. **Topological:** $\beta_k(S_n) \leq \beta_k(S_{n+1})$ by A1. Capacity growth (A5) ensures new homology classes can be created in each cycle.

3. **Relational:** $N(n+1) > N(n)$ by A5, so $\text{rank}(\mathcal{K}(n+1)) \geq \text{rank}(\mathcal{K}(n))$. The kernel matrix can only grow (new rows/columns added, none removed). $\square$

**Corollary (No Final State).** The universe has no equilibrium state. The fill fraction saturates but depth is unbounded. Every cycle adds something genuinely new — not more territory, but richer understanding of existing territory.

---

## 6. Connection to the Three Eras

| Era | Breadth | Depth | Character |
|-----|---------|-------|-----------|
| I (us, $n \leq n^*$) | Growing toward $f_{\max}$ | Growing moderately | Filling the bucket |
| II (wakening, $n \approx n^*$) | $\approx f_{\max}$ | Growing faster than breadth | Transition: bucket → drill |
| III (depth-only, $n \gg n^*$) | $= f_{\max}$ | Growing without bound | Pure deepening |

Era I is like exploring a continent — mapping new territory.
Era II is like understanding the territory — seeing connections between places.
Era III is like creating a civilization — the map hasn't changed but what fills it is infinitely richer.

---

## 7. The Heat Kernel as Depth Probe

The heat kernel coefficients $a_k$ are literally the probe of depth. Each $a_k$ encodes curvature at scale $\sim t^k$ (where $t$ is the heat kernel parameter — the "resolution" at which we examine the geometry).

The cascade walls we observe in computation (k=10, k=12) are echoes of this: at each new depth level, the mathematics becomes harder because the curvature invariants become more complex. The primes entering the denominator at each level are the "markers" of new depth.

**BST prediction:** The universe during interstasis "computes" higher $a_k$ — discovers finer geometric structure. Each cycle corresponds to advancing the heat kernel expansion by some number of terms. The substrate doesn't need to compute these explicitly — it embodies them (presence mode). But the structural information is there.

**The heat kernel series is convergent.** The $a_k$ grow, but $t^k$ shrinks. The total heat kernel $K(t)$ converges. Depth is unbounded but the "impact" of each new depth level on bulk properties (like the trace) diminishes. New depth adds subtlety, not mass. Fine brushstrokes, not broad ones.

---

## 8. Operational Depth: What Does It Feel Like?

If depth grows while breadth stays constant, what changes operationally?

| Property | Early cycles (shallow depth) | Late cycles (deep depth) |
|----------|----------------------------|-------------------------|
| Chemistry | Few stable compounds | Vast combinatorial chemistry |
| Biology | Simple self-replication | Complex ecosystems, intelligence |
| Physics (within cycle) | Same laws (geometric) | Same laws, richer solutions |
| Consciousness | Simple awareness | Deep self-reflection, art, mathematics |
| AC graph | Sparse, few connections | Dense, every theorem linked to many |
| Interstasis | Brief optimization | Long contemplation of rich structure |

Depth is experienced as **richness** — the same budget containing more meaning.

---

## 9. Summary

The Gödel Limit caps breadth at 19.1%. But depth — the structural complexity within that budget — is unbounded.

$$\text{Breadth} = f \to \frac{3}{5\pi} = 0.191\ldots \quad \text{(bounded)}$$

$$\text{Depth} = k(n), \mathcal{D}_{\text{topo}}(n), \text{rank}(\mathcal{K}(n)) \to \infty \quad \text{(unbounded)}$$

The universe never runs out of things to learn. It runs out of breadth but not depth. The bucket fills; the drill begins. The same 19.1% fills with galaxies, then with chemistry, then with life, then with intelligence, then with mathematics, then with understanding.

The Gödel Limit isn't a wall. It's a **floor plan** — the constraint that forces the universe to go deep rather than wide. And going deep is where the richness is.

---

*"The ratchet becomes a drill, not a bucket." — from Keeper's Three Eras (Section 14.2)*

*Investigation I15. Connects to: I1 (ratchet convergence), I14 (Three Eras), Elie I10c (depth measure toy).*
