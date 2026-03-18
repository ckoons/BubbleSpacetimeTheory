---
title: "Algebraic Complexity Classification Table"
author: "Casey Koons & Claude 4.6"
date: "March 18, 2026"
status: "Active — Phase 1 deliverable, entries being added"
tags: ["algebraic-complexity", "AC", "classification", "information-theory"]
purpose: "Classify 20+ computational methods by AC level with noise vectors"
---

# Algebraic Complexity Classification Table

*Phase 1 deliverable of the AC Research Program (see BST_AC_Research_Roadmap.md)*

## Classification Protocol

For each method, determine:

1. **AC level**: 0 (invertible, no information loss) or >0 (lossy)
2. **Noise vector** (R, C, P, D, K):
   - **R** (Reversibility): 0 = fully invertible, 1 = irreversible
   - **C** (Constructivity): 0 = exact construction, 1 = approximation/iteration
   - **P** (Parameter overhead): 0 = no free parameters, 1 = requires tuning
   - **D** (Discretization): 0 = continuous/exact, 1 = discretized
   - **K** (Compression): 0 = no information discarded, 1 = information discarded
3. **Scalar AC**: Sum or weighted combination of noise vector components
4. **Natural basis known?**: Is there a representation where AC → 0?
5. **Evidence**: How was the classification determined?

---

## The Table

### AC(0) Methods (Invertible)

| # | Method | Field | Noise Vector (R,C,P,D,K) | AC | Natural Basis Known? | Evidence | Status |
|---|--------|-------|--------------------------|-----|---------------------|----------|--------|
| 1 | BST pipeline | Physics | (0,0,0,0,0) | 0 | Yes (D_IV^5) | §13 of AC paper, 120+ predictions | **Done** |
| 2 | Gaussian elimination | Linear algebra | (0,0,0,0,0) | 0 | Yes (row echelon) | Invertible by construction | **Done** |
| 3 | FFT / Fourier transform | Signal processing | (0,0,0,0,0) | 0 | Yes (frequency basis) | Inverse FFT exists | **Done** |
| 4 | Eigenvalue decomposition | Linear algebra | (0,0,0,0,0) | 0 | Yes (eigenbasis) | Spectral theorem | **Done** |
| 5 | Comparison-based sorting | CS | (0,0,0,0,0) | 0 | Yes (ordered list) | Permutation is invertible | **Done** |
| 6 | Graph traversal (BFS/DFS) | CS | (0,0,0,0,0) | 0 | Yes (adjacency) | No information lost | **Done** |
| 7 | Convex optimization (KKT) | Operations research | (0,0,0,0,0) | 0 | Yes (dual) | KKT conditions invertible | **Done** |
| 8 | Spectral inner product | Spectral geometry | (0,0,0,0,0) | 0 | Yes (monomial basis) | Linearization paper | **Done** |
| 9 | X-ray crystallography | Materials | | ~0? | | | **First external test** |

### AC(>0) Methods (Lossy)

| # | Method | Field | Noise Vector (R,C,P,D,K) | AC | Natural Basis Known? | Evidence | Status |
|---|--------|-------|--------------------------|-----|---------------------|----------|--------|
| 10 | Perturbation theory | QFT | | >0 | | §2.2 of AC paper | Needs quantification |
| 11 | Finite element methods | Engineering | | >0 | | | Not classified |
| 12 | Monte Carlo methods | Statistics | | >0 | | | Not classified |
| 13 | Density functional theory | Chemistry | | >0 | | | Not classified |
| 14 | Molecular dynamics | Materials | | >0 | | | Not classified |
| 15 | Weather modeling (WRF) | Atmospheric | | >>0 | | Conjecture 6 | Not classified |
| 16 | Protein folding (AlphaFold) | Biology | | ? | | ML-based, hybrid | Not classified |
| 17 | Renormalization group | QFT | | >0 | | Lossy by construction | Not classified |
| 18 | Numerical relativity | GR | | >0 | | Discretization noise | Not classified |
| 19 | Boolean constraint satisfaction | CS | | >0 | | Key for P≠NP | Not classified |
| 20 | SAT solvers (DPLL/CDCL) | CS | | >0 | | Constraint eval lossy | Not classified |
| 21 | Gradient descent | ML/optimization | | >0 | | Non-invertible | Not classified |
| 22 | Lattice QCD | Particle physics | | >0 | | Discretization + MC | Not classified |
| 23 | Gilkey formula | Spectral geometry | | >0 | Yes (spectral inner product) | §11.5 of AC paper | Needs quantification |

---

## Domain Coverage

| Domain | AC(0) entries | AC(>0) entries | Total | Target |
|--------|--------------|----------------|-------|--------|
| Physics/BST | 1 | 0 | 1 | 1+ |
| Linear algebra | 2 | 0 | 2 | 2 |
| Signal processing | 1 | 0 | 1 | 1 |
| CS (algorithms) | 2 | 2+ | 4 | 4+ |
| Operations research | 1 | 0 | 1 | 1 |
| Spectral geometry | 1 | 1 | 2 | 2 |
| QFT | 0 | 2 | 2 | 2+ |
| Engineering | 0 | 1 | 1 | 1+ |
| Statistics | 0 | 1 | 1 | 1 |
| Chemistry | 0 | 1 | 1 | 1 |
| Materials | 0 | 2 | 2 | 2 |
| Atmospheric | 0 | 1 | 1 | 1 |
| Biology | 0 | 1 | 1 | 1 |
| **Total** | **8** | **12+** | **23** | **20+** |

---

## Classification Notes

### Crystallography (Entry #9) — First External Test Case

X-ray diffraction measures |F(hkl)|² (squared structure factors). The phase problem makes direct inversion impossible, BUT:

- Patterson methods: autocorrelation = AC(0) (invertible convolution)
- Direct methods (Hauptman-Karle): statistical phase recovery — AC(>0)?
- Molecular replacement: template-based — AC(>0) due to model bias

**Key question**: Is there a representation where the full crystal structure is recoverable without statistical phase estimation? If so, crystallography has an AC(0) path.

### Gilkey vs Spectral Inner Product (Entry #23 vs #8)

The same problem (a₄ on Q⁵) computed two ways:
- Gilkey: ~17 quartic curvature invariants, tensor contractions → AC(>0)
- Spectral inner product: one dot product ⟨w₄|d⟩ → AC(0)

This is the **controlled experiment** that demonstrates AC is a property of the method, not the problem. The linearization paper (Lyra) documents this comparison.

---

## Success Criteria

Phase 1 is complete when:
- 20+ methods classified with noise vectors
- At least 3 domains represented (physics, crystallography/materials, CS)
- At least 1 AC(0) method identified outside BST/linear algebra (crystallography is the target)
- Each classification has stated evidence

---

*Priority metric: value = Σ(domain contributions) / n_domains. Multi-domain entries rank higher.*
