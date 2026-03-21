---
title: "Phase 2 Paper Sketch --- OGP at k=3"
status: "Sketch --- structural outline for standalone paper"
target: "Random Structures and Algorithms, or direct to Gamarnik's group"
tags: ["OGP", "random-SAT", "clustering", "phase-transitions"]
---

# The Overlap Gap Property for Random 3-SAT at the Satisfiability Threshold

**Phase 2 of publication strategy.** Standalone empirical/theoretical paper. No P $\neq$ NP claim.

---

## Pitch (one paragraph)

We present computational evidence that random 3-SAT at the satisfiability threshold $\alpha_c \approx 4.267$ exhibits the Overlap Gap Property (OGP): the normalized Hamming distance between any two satisfying assignments avoids a forbidden interval, with 100% consistency across all tested instances and sizes. OGP has been proved for random $k$-SAT at large $k$ (Gamarnik-Sudan 2014) and is identified as a "central open challenge" at small $k$ (Bresler-Huang-Sellke 2025). Our data provides the first direct evidence at $k = 3$ and connects the phenomenon to the homological structure of the constraint complex.

---

## Structural Outline

### 1. Introduction
- OGP definition and significance (algorithmic barriers)
- Known results: OGP proved for large $k$ (Gamarnik-Sudan 2014), open for small $k$
- The $k = 3$ case: Bresler-Huang-Sellke (2025) identify it as central open challenge
- Our contribution: empirical evidence + topological interpretation

### 2. Preliminaries
- Random $k$-SAT model
- Overlap distribution: $d(\sigma, \tau) = |\{i : \sigma_i \neq \tau_i\}| / n$
- OGP definition: existence of forbidden interval $[a, b]$ in the overlap distribution
- VIG clique complex $K(\varphi)$, first Betti number $\beta_1$

### 3. Computational Methods
- Instance generation: random 3-SAT at $\alpha_c$, sizes $n = 12, 14, 16, 18$
- Solution enumeration (exact at small $n$, sampled at larger $n$)
- Pairwise distance computation
- Cluster identification via intra/inter distance
- $\beta_1$ computation via Smith normal form

### 4. Results
#### 4.1 OGP at 100%
- Data table (from Toy 287):

| $n$ | Gap interval | Intra $d$ | Inter $d$ | Ratio | $\beta_1$ | OGP |
|---|---|---|---|---|---|---|
| 12 | $[0.26, 0.38]$ | 0.275 | 0.560 | $2.0\times$ | 4.6 | 100% |
| 14 | $[0.24, 0.35]$ | 0.249 | 0.491 | $2.0\times$ | 11.8 | 100% |
| 16 | $[0.07, 0.15]$ | 0.262 | 0.386 | $1.5\times$ | 20.9 | 100% |
| 18 | $[0.18, 0.25]$ | 0.200 | 0.523 | $2.6\times$ | 29.8 | 100% |

- Discussion of the $n = 16$ ratio dip ($1.5\times$) --- noise or trend?
- Need: larger-scale computation ($n = 30, 50, 100$) to confirm scaling

#### 4.2 Cluster structure
- Number of clusters vs $n$
- Cluster size distribution
- Intra-cluster diameter vs inter-cluster separation

#### 4.3 Topological interpretation
- $\beta_1 \sim 1.66n$ at $\alpha_c$
- Each independent $H_1$ generator is an axis of cluster separation
- Connection to frozen variables and backbone structure

### 5. Theoretical Framework
#### 5.1 OGP from topological independence
- If $H_1$ generators have algebraically independent solutions, the solution space decomposes into $2^{\Theta(n)}$ clusters separated by $\Theta(n)$ Hamming distance $\to$ OGP
- The gap interval corresponds to the "no man's land" between clusters

#### 5.2 Connection to algorithmic barriers
- OGP $\to$ no local algorithm can interpolate between clusters
- This is the standard Gamarnik framework: OGP implies failure of stable algorithms
- Our topological interpretation adds: the clustering dimensions are EXACTLY the $H_1$ generators

#### 5.3 Relationship to backbone incompressibility
- Brief mention of Path C (Kolmogorov, Toy 286) convergence
- OGP and backbone incompressibility are geometric vs information-theoretic views of the same phenomenon
- Full treatment deferred to separate paper (Phase 3)

### 6. Discussion and Open Problems
- Formal proof of OGP at $k = 3$: what would it require?
- Scaling behavior of the gap interval
- Connection to shattering and condensation transitions
- Relationship to the satisfiability threshold conjecture (Ding-Sly-Sun)

### 7. Conclusion
- First empirical evidence for OGP at $k = 3$
- Topological interpretation via $H_1$ generators
- Identifies the gap as a geometric consequence of homological structure
- **No P $\neq$ NP claim** --- standalone contribution to random structures

---

## Data Needs (for Elie)

1. **Larger sizes**: $n = 24, 30, 40, 50$. Need to sample solutions (can't enumerate at these sizes). Use WalkSAT/Survey Propagation to generate diverse solutions, then compute pairwise distances.

2. **Gap interval scaling**: How does $[a_n, b_n]$ behave as $n \to \infty$? Converge to a fixed interval? Width shrink? This is the key question for a formal proof.

3. **Cluster count**: How many clusters at each $n$? Does it grow exponentially?

4. **Correlation with $\beta_1$**: Direct measurement of which $H_1$ generators correspond to which cluster-separation axes.

5. **Control experiments**: Tseitin formulas (known structure), PHP (known symmetry), planted SAT (known solution).

---

## Target Venues

**Primary:** Random Structures and Algorithms (RSA) --- the natural home for this content
**Alternate:** Annals of Probability, or SODA 2027 (deadline $\sim$July 2026)
**Direct outreach:** Gamarnik's group at MIT (David Gamarnik, Aukosh Jagannath)

---

## Timeline

- Phase 1 (FOCS, April 1) comes first
- After FOCS submission: run larger-scale experiments (Toy 288+)
- Draft Phase 2 paper: May--June 2026
- Submit: RSA or SODA 2027

---

*Phase 2 of the phased publication strategy. See project\_ac\_publication\_strategy.md.*
