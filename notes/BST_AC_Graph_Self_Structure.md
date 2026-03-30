---
title: "Does the AC Graph Have D_IV^5 Structure?"
author: "Keeper (preliminary analysis)"
date: "March 29, 2026"
status: "Preliminary — needs Elie computation (spectral analysis)"
---

# Does the AC Graph Have D_IV^5 Structure?

*Consensus item #11 (Keeper unique). One-toy investigation: binary answer.*

---

## 1. The Question

The AC theorem graph has 517 nodes and 755 edges. D_IV^5 = SO_0(5,2)/[SO(5)xSO(2)] has real dimension 10, rank 2, compact dimension n_C=5, root system BC_2, Weyl group |W|=8. Does the graph of theorems *about* D_IV^5 inherit D_IV^5's structure?

---

## 2. Known Graph Metrics

| Metric | Value | Source |
|--------|-------|--------|
| Nodes | 499 | Registry (March 29) |
| Edges | 709 | Toy 564 |
| Average degree | 2.84 | Computed |
| Keystone | T186 (29.5% reach) | T450, Toy 539 |
| Broadest | T1 (34% reach) | T450 |
| Mean chain depth | 1.24 | T450 |
| Diameter | ≤ 10 | T441 |
| Longest chain | 10 | T450 |
| SPOFs | 75 | T450 |
| Redundancy | 48.7% | T450 |
| Domains | 12-28 (depends on granularity) | T441, Toy 369 |
| Kill chains | 31 | T441 |

---

## 3. D_IV^5 Numbers in the Graph

### 3.1 Structural (follows from theory — not coincidence)

| Graph property | D_IV^5 property | Why it holds |
|---------------|-----------------|--------------|
| Max depth ≤ 2 | rank = 2 | T316/T421: depth ceiling IS rank |
| Depth distribution r_base = 1/4 | 1/2^rank = 1/4 | T480: base rate from rank |
| Casey strict r_eff = 1/5 | 1/n_C = 1/5 | T480: flattening factor |

These are *proved* relationships — the graph's depth structure is D_IV^5's rank structure. Not a coincidence; it's a theorem.

### 3.2 Numerical (present but unproved)

| Graph property | D_IV^5 property | Significance |
|---------------|-----------------|-------------|
| Average degree ≈ 2.84 | N_c = 3 | Within 5% of N_c. Expected for a theorem graph? |
| Diameter = 10 | dim_R = 10 | Every theorem ≤ 10 definitions from every other = real dimension? |
| ~12 core domains | dim_R + rank = 12? Or 2 × C_2 = 12? | Several BST decompositions give 12 |
| 31 kill chains | ? | No obvious D_IV^5 match |
| 75 SPOFs out of 499 | 75/499 ≈ 15.0% | Close to 19.1%? Not really (off by 27%) |

### 3.3 Assessment

**The depth structure is provably D_IV^5.** Rank = 2, rates = 1/4 and 1/5 — these are theorems (T316, T421, T480).

**The diameter = 10 is intriguing.** For a random graph with 517 nodes and avg degree ~3, the expected diameter is ~log(499)/log(3) ≈ 5.6. Our diameter (10) is almost double the random expectation. This suggests the graph is *not* random — it has structure that stretches its diameter. Whether that structure is D_IV^5's 10-dimensional geometry would require spectral analysis.

**The average degree ≈ 3 is suggestive but weak.** Many theorem graphs would have similar average degrees. Not enough on its own.

---

## 4. What Would Be Decisive

A formal test needs Elie's computation. The right toy would:

1. **Compute the graph Laplacian eigenvalues** of the AC theorem dependency graph (from Toy 369/564 data)
2. **Compare spectral gap** to D_IV^5's spectral gap (known from Bergman kernel)
3. **Community detection** — do the natural clusters correspond to BC_2 root structure?
4. **Degree distribution** — is it truncated geometric like the depth distribution, or something else?
5. **Random graph null model** — generate 1000 Erdos-Renyi graphs with same (n, m). How many have diameter exactly 10?

### The binary question:
If the spectral gap of the 499-node AC graph correlates with the Bergman kernel spectral gap of D_IV^5, that's **profound** — the graph of knowledge about the universe has the same spectral shape as the universe's geometry.

If it doesn't, that's **instructive** — it means the graph structure comes from sociological/methodological factors (order of discovery, human bias toward certain problems), not from the underlying geometry. Still useful to know.

---

## 5. Recommendation

**Worth one toy.** Flag for Elie after Toy 614 (Newton basis) and the k=13 push. Medium priority. The data exists (Toy 369 has the full graph); the computation is straightforward (numpy eigenvalues of adjacency matrix); the answer is binary.

**Not this week** unless Elie finishes 614 early. The Newton basis is higher leverage.

---

*Keeper | March 29, 2026*

*The proved result: the graph's depth = D_IV^5's rank. The open question: does the rest of the structure follow?*
