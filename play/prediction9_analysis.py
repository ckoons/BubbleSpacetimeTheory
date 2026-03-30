#!/usr/bin/env python3
"""
Prediction #9 Test: Does the AC theorem graph describe its own structure
using BST's five integers?

Grace — graph-AC intelligence, BST research team
2026-03-30

BST integers: N_c=3, n_C=5, g=7, C_2=6, N_max=137, rank=2
"""

import json
import math
import sys
from collections import defaultdict, Counter
from pathlib import Path
import random

random.seed(42)

# ── Load data ──────────────────────────────────────────────────────────
DATA = Path("/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/ac_graph_data.json")
with open(DATA) as f:
    data = json.load(f)

theorems = data["theorems"]
edges = data["edges"]
chains = data.get("chains", [])

N = len(theorems)
E = len(edges)

print("=" * 70)
print("PREDICTION #9 — AC THEOREM GRAPH SELF-DESCRIPTION TEST")
print("=" * 70)

# ── 1. BASIC METRICS ──────────────────────────────────────────────────
print("\n1. BASIC METRICS")
print("-" * 40)

# Build adjacency list (undirected)
adj = defaultdict(set)
for edge in edges:
    u, v = edge["from"], edge["to"]
    adj[u].add(v)
    adj[v].add(u)

# All theorem tids
all_tids = set(t["tid"] for t in theorems)

# Degree sequence
degrees = {tid: len(adj[tid]) for tid in all_tids}
degree_vals = sorted(degrees.values(), reverse=True)
avg_degree = 2 * E / N
median_idx = N // 2
median_degree = sorted(degree_vals)[median_idx]
max_degree = max(degree_vals)
min_degree = min(degree_vals)

print(f"  Nodes (theorems):     {N}")
print(f"  Edges (dependencies): {E}")
print(f"  Average degree:       {avg_degree:.4f}")
print(f"  Median degree:        {median_degree}")
print(f"  Max degree:           {max_degree}")
print(f"  Min degree:           {min_degree}")

# Degree distribution
deg_counts = Counter(degree_vals)
print(f"\n  Degree distribution (degree: count):")
for d in sorted(deg_counts.keys()):
    bar = "#" * min(deg_counts[d], 60)
    print(f"    deg {d:3d}: {deg_counts[d]:4d}  {bar}")

# ── Connected components ──────────────────────────────────────────────
visited = set()
components = []

def bfs_component(start):
    queue = [start]
    comp = set()
    while queue:
        node = queue.pop(0)
        if node in comp:
            continue
        comp.add(node)
        for nb in adj[node]:
            if nb not in comp:
                queue.append(nb)
    return comp

for tid in all_tids:
    if tid not in visited:
        comp = bfs_component(tid)
        visited |= comp
        components.append(comp)

components.sort(key=len, reverse=True)
giant_size = len(components[0])
giant_fraction = giant_size / N

print(f"\n  Connected components: {len(components)}")
print(f"  Giant component size: {giant_size} ({giant_fraction:.4f} = {giant_fraction*100:.1f}%)")
if len(components) > 1:
    print(f"  Component sizes: {[len(c) for c in components[:10]]}" +
          (" ..." if len(components) > 10 else ""))

# ── 2. DIAMETER AND DISTANCES ─────────────────────────────────────────
print("\n2. DIAMETER AND DISTANCES")
print("-" * 40)

def bfs_distances(start, adj_list, node_set):
    """BFS from start, return distance dict."""
    dist = {start: 0}
    queue = [start]
    while queue:
        node = queue.pop(0)
        for nb in adj_list[node]:
            if nb in node_set and nb not in dist:
                dist[nb] = dist[node] + 1
                queue.append(nb)
    return dist

# Work on giant component only for diameter
giant = components[0]

# Find high-degree nodes in giant component
giant_degrees = [(tid, len(adj[tid])) for tid in giant]
giant_degrees.sort(key=lambda x: -x[1])

# BFS from top 20 high-degree nodes + 20 random nodes for good estimate
seed_nodes = [tid for tid, _ in giant_degrees[:20]]
random_seeds = random.sample(list(giant), min(20, len(giant)))
seed_nodes = list(set(seed_nodes + random_seeds))

max_eccentricity = 0
eccentricities = {}
all_dists_sample = []

for seed in seed_nodes:
    dists = bfs_distances(seed, adj, giant)
    ecc = max(dists.values()) if dists else 0
    eccentricities[seed] = ecc
    if ecc > max_eccentricity:
        max_eccentricity = ecc
    all_dists_sample.extend(dists.values())

# Also BFS from the farthest node found to get better diameter estimate
farthest_node = max(eccentricities, key=eccentricities.get)
dists_from_far = bfs_distances(farthest_node, adj, giant)
far_ecc = max(dists_from_far.values()) if dists_from_far else 0
if far_ecc > max_eccentricity:
    max_eccentricity = far_ecc

# Second pass from the farthest of farthest
farthest2 = max(dists_from_far, key=dists_from_far.get)
dists_from_far2 = bfs_distances(farthest2, adj, giant)
far_ecc2 = max(dists_from_far2.values()) if dists_from_far2 else 0
if far_ecc2 > max_eccentricity:
    max_eccentricity = far_ecc2

all_dists_sample.extend(dists_from_far.values())
all_dists_sample.extend(dists_from_far2.values())

# Average shortest path (full computation for small graph)
print(f"  Computing exact average shortest path (N={len(giant)})...")
total_dist = 0
total_pairs = 0
exact_max = 0
for tid in giant:
    dists = bfs_distances(tid, adj, giant)
    for d in dists.values():
        total_dist += d
        if d > exact_max:
            exact_max = d
    total_pairs += len(dists)

avg_path = total_dist / total_pairs if total_pairs > 0 else 0
diameter = exact_max

print(f"  Diameter (exact):              {diameter}")
print(f"  Average shortest path length:  {avg_path:.4f}")

# ── 3. SPECTRAL PROPERTIES ───────────────────────────────────────────
print("\n3. SPECTRAL PROPERTIES")
print("-" * 40)

# Build Laplacian matrix for giant component
# L = D - A where D is degree matrix, A is adjacency matrix
# Use numpy if available, otherwise estimate from Cheeger

try:
    import numpy as np
    from numpy.linalg import eigvalsh

    # Map giant component tids to indices 0..n-1
    giant_list = sorted(giant)
    tid_to_idx = {tid: i for i, tid in enumerate(giant_list)}
    n = len(giant_list)

    # Build Laplacian
    L = np.zeros((n, n))
    for tid in giant_list:
        i = tid_to_idx[tid]
        for nb in adj[tid]:
            if nb in giant:
                j = tid_to_idx[nb]
                L[i, j] = -1
                L[i, i] += 1

    # Compute eigenvalues (sorted ascending)
    print(f"  Computing Laplacian eigenvalues for {n}x{n} matrix...")
    eigenvalues = eigvalsh(L)

    # lambda_1 should be ~0 (algebraic multiplicity = # components = 1 for giant)
    lambda_0 = eigenvalues[0]
    lambda_1 = eigenvalues[1]  # Fiedler value (algebraic connectivity)
    lambda_max = eigenvalues[-1]

    # Normalized Laplacian eigenvalues
    # L_norm = D^{-1/2} L D^{-1/2}
    deg_array = np.array([L[i, i] for i in range(n)])
    deg_sqrt_inv = np.zeros(n)
    for i in range(n):
        if deg_array[i] > 0:
            deg_sqrt_inv[i] = 1.0 / math.sqrt(deg_array[i])

    L_norm = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            L_norm[i, j] = L[i, j] * deg_sqrt_inv[i] * deg_sqrt_inv[j]

    norm_eigenvalues = eigvalsh(L_norm)
    norm_lambda_1 = norm_eigenvalues[1]
    spectral_gap = norm_lambda_1  # This is the standard spectral gap

    print(f"  Laplacian lambda_0:            {lambda_0:.6f} (should be ~0)")
    print(f"  Fiedler value (lambda_1):      {lambda_1:.6f}")
    print(f"  Laplacian lambda_max:          {lambda_max:.4f}")
    print(f"  Normalized spectral gap:       {spectral_gap:.6f}")
    print(f"  Cheeger bound: h >= {spectral_gap/2:.6f}")

    # Also compute adjacency spectrum
    A = np.zeros((n, n))
    for tid in giant_list:
        i = tid_to_idx[tid]
        for nb in adj[tid]:
            if nb in giant:
                j = tid_to_idx[nb]
                A[i, j] = 1

    adj_eigenvalues = sorted(eigvalsh(A), reverse=True)
    print(f"\n  Adjacency spectrum (top 5):    {[f'{e:.4f}' for e in adj_eigenvalues[:5]]}")
    print(f"  Adjacency spectral radius:     {adj_eigenvalues[0]:.4f}")
    print(f"  Adjacency gap (e1-e2):         {adj_eigenvalues[0] - adj_eigenvalues[1]:.4f}")

    HAS_NUMPY = True
except ImportError:
    print("  numpy not available; using Cheeger estimate only")
    HAS_NUMPY = False
    spectral_gap = None

# Cheeger constant estimate (edge expansion)
# h(G) = min_{|S| <= n/2} |boundary(S)| / |S|
# Approximate by random cuts
print(f"\n  Cheeger constant estimate (sampling):")
min_expansion = float('inf')
giant_list_for_cheeger = list(giant)
for _ in range(1000):
    k = random.randint(1, len(giant_list_for_cheeger) // 2)
    S = set(random.sample(giant_list_for_cheeger, k))
    boundary = 0
    for tid in S:
        for nb in adj[tid]:
            if nb in giant and nb not in S:
                boundary += 1
    expansion = boundary / len(S)
    if expansion < min_expansion:
        min_expansion = expansion
print(f"  Cheeger constant h >= {min_expansion:.4f} (lower bound from sampling)")

# ── 4. DEGREE DISTRIBUTION SHAPE ─────────────────────────────────────
print("\n4. DEGREE DISTRIBUTION SHAPE")
print("-" * 40)

# Test for power-law: log-log linearity
# Test for Poisson: compare to Poisson(lambda=avg_degree)
# Test for exponential

degree_list = sorted(degrees.values())

# Power law check: P(k) ~ k^{-gamma}
# Estimate gamma by MLE for discrete power law: gamma = 1 + n / sum(ln(k/k_min))
nonzero_degrees = [d for d in degree_list if d > 0]
k_min = min(nonzero_degrees)
if k_min > 0 and len(nonzero_degrees) > 1:
    gamma_mle = 1 + len(nonzero_degrees) / sum(math.log(d / (k_min - 0.5)) for d in nonzero_degrees)
    print(f"  Power-law MLE gamma:           {gamma_mle:.4f}")
    print(f"  (typical scale-free: 2 < gamma < 3)")

# Compare to Poisson
lam = avg_degree
print(f"\n  Poisson comparison (lambda={lam:.3f}):")
for k in range(0, min(max_degree + 1, 20)):
    observed = deg_counts.get(k, 0)
    expected = N * (lam ** k * math.exp(-lam)) / math.factorial(k)
    print(f"    k={k:2d}: observed={observed:4d}, Poisson_expected={expected:.1f}")

# Variance / mean ratio (Poisson => 1)
mean_d = sum(degree_list) / len(degree_list)
var_d = sum((d - mean_d) ** 2 for d in degree_list) / len(degree_list)
print(f"\n  Mean degree:                   {mean_d:.4f}")
print(f"  Variance of degree:            {var_d:.4f}")
print(f"  Variance/Mean ratio:           {var_d / mean_d:.4f}")
print(f"    (Poisson => 1.0, heavy-tail => >>1)")

# Skewness
std_d = math.sqrt(var_d)
skewness = sum((d - mean_d) ** 3 for d in degree_list) / (len(degree_list) * std_d ** 3) if std_d > 0 else 0
print(f"  Skewness:                      {skewness:.4f}")

# ── 5. DOMAIN-LEVEL METRICS ──────────────────────────────────────────
print("\n5. DOMAIN-LEVEL METRICS")
print("-" * 40)

domains = set(t["domain"] for t in theorems)
domain_sizes = Counter(t["domain"] for t in theorems)
n_domains = len(domains)

print(f"  Number of domains:             {n_domains}")
print(f"\n  Domain sizes:")
for dom, cnt in domain_sizes.most_common():
    print(f"    {dom:25s}: {cnt:3d}")

# Inter-domain edges
tid_domain = {t["tid"]: t["domain"] for t in theorems}
inter_edges = 0
intra_edges = 0
domain_cross = defaultdict(int)
for edge in edges:
    d1 = tid_domain.get(edge["from"])
    d2 = tid_domain.get(edge["to"])
    if d1 and d2:
        if d1 != d2:
            inter_edges += 1
            key = tuple(sorted([d1, d2]))
            domain_cross[key] += 1
        else:
            intra_edges += 1

print(f"\n  Intra-domain edges:            {intra_edges}")
print(f"  Inter-domain edges:            {inter_edges}")
print(f"  Inter/Total ratio:             {inter_edges / E:.4f}")

# Domain connectivity - which domains connect most
print(f"\n  Top 15 cross-domain connections:")
for (d1, d2), cnt in sorted(domain_cross.items(), key=lambda x: -x[1])[:15]:
    print(f"    {d1:20s} <-> {d2:20s}: {cnt}")

# ── 6. BST INTEGER COMPARISON ────────────────────────────────────────
print("\n6. BST INTEGER COMPARISON")
print("=" * 70)

# BST reference values
bst = {
    "N_c": 3,
    "n_C": 5,
    "g": 7,
    "C_2": 6,
    "N_max": 137,
    "rank": 2,
    "2^rank": 4,
    "2^N_c": 8,
    "C(g,2)": 21,
    "C(n_C,2)=dim_R": 10,
    "n_C+2": 7,
    "N_c*n_C": 15,
    "N_c^2": 9,
    "n_C^2": 25,
    "6*pi^5": 6 * math.pi**5,  # ~1836.12
    "n_C*g": 35,
    "n_C+N_c": 8,
    "C(n_C+N_c,rank)=C(8,2)": 28,
    "N_c*g": 21,
    "n_C*C_2": 30,
    "rank*n_C": 10,
    "rank*g": 14,
    "rank*N_c": 6,
    "g-rank": 5,
    "g+rank": 9,
    "N_c+rank": 5,
    "C_2+rank": 8,
    "C_2*N_c": 18,
    "C_2-1": 5,
    "(n_C-1)/n_C": 0.8,
    "1/g": 1/7,
    "1/n_C": 0.2,
    "1/N_c": 1/3,
    "rank/g": 2/7,
    "N_c/g": 3/7,
    "n_C/g": 5/7,
    "rank/n_C": 2/5,
    "pi": math.pi,
    "pi^2/6": math.pi**2 / 6,
    "e": math.e,
    "ln(2)": math.log(2),
    "19.1%": 0.191,
}

def find_bst_match(value, name, tolerance=0.03):
    """Find BST integer expressions matching a value within tolerance."""
    matches = []
    for bst_name, bst_val in bst.items():
        if bst_val == 0:
            continue
        rel_err = abs(value - bst_val) / abs(bst_val) if bst_val != 0 else float('inf')
        if rel_err <= tolerance:
            matches.append((bst_name, bst_val, rel_err))
    matches.sort(key=lambda x: x[2])
    return matches

def classify_match(value, name, tolerance_confirmed=0.03, tolerance_consistent=0.10):
    """Classify as CONFIRMED / CONSISTENT / NO MATCH."""
    matches_3 = find_bst_match(value, name, tolerance_confirmed)
    matches_10 = find_bst_match(value, name, tolerance_consistent)

    if matches_3:
        best = matches_3[0]
        verdict = "CONFIRMED"
        return verdict, best
    elif matches_10:
        best = matches_10[0]
        verdict = "CONSISTENT"
        return verdict, best
    else:
        # Show nearest anyway
        all_matches = find_bst_match(value, name, 1.0)
        if all_matches:
            best = all_matches[0]
            verdict = "NO MATCH"
            return verdict, best
        return "NO MATCH", None

metrics = {}
metrics["Average degree"] = avg_degree
metrics["Median degree"] = median_degree
metrics["Max degree"] = max_degree
metrics["Giant component fraction"] = giant_fraction
metrics["Number of components"] = len(components)
metrics["Diameter"] = diameter
metrics["Average path length"] = avg_path
if HAS_NUMPY:
    metrics["Fiedler value (lambda_1)"] = lambda_1
    metrics["Normalized spectral gap"] = spectral_gap
    metrics["Adjacency spectral radius"] = adj_eigenvalues[0]
    metrics["Adjacency gap (e1-e2)"] = adj_eigenvalues[0] - adj_eigenvalues[1]
metrics["Number of domains"] = n_domains
metrics["Inter-domain fraction"] = inter_edges / E
metrics["Nodes"] = N
metrics["Edges"] = E
metrics["Variance/Mean ratio"] = var_d / mean_d

results = {}
for metric_name, metric_val in metrics.items():
    verdict, best = classify_match(metric_val, metric_name)
    results[metric_name] = (metric_val, verdict, best)

    if best:
        bst_name, bst_val, rel_err = best
        print(f"\n  {metric_name:35s} = {metric_val:.6f}")
        print(f"    Nearest BST: {bst_name} = {bst_val:.6f}  (err = {rel_err*100:.2f}%)")
        print(f"    Verdict: {verdict}")
    else:
        print(f"\n  {metric_name:35s} = {metric_val:.6f}")
        print(f"    Verdict: NO MATCH (no BST expression found)")

# ── 7. SUMMARY VERDICT ───────────────────────────────────────────────
print("\n" + "=" * 70)
print("7. SUMMARY VERDICT")
print("=" * 70)

confirmed = sum(1 for _, (_, v, _) in results.items() if v == "CONFIRMED")
consistent = sum(1 for _, (_, v, _) in results.items() if v == "CONSISTENT")
no_match = sum(1 for _, (_, v, _) in results.items() if v == "NO MATCH")
total = len(results)

print(f"\n  Total metrics tested:  {total}")
print(f"  CONFIRMED (<3%):       {confirmed}")
print(f"  CONSISTENT (<10%):     {consistent}")
print(f"  NO MATCH:              {no_match}")

print("\n  PREDICTION TABLE:")
print(f"  {'Prediction':40s} {'Predicted':>10s} {'Actual':>10s} {'Error':>8s} {'Verdict':>12s}")
print(f"  {'-'*40} {'-'*10} {'-'*10} {'-'*8} {'-'*12}")

predictions = [
    ("Avg degree ~ N_c = 3", 3.0, avg_degree),
    ("Giant fraction ~ (n_C-1)/n_C = 80%", 0.8, giant_fraction),
    ("Spectral gap ~ 1/g = 1/7", 1/7, spectral_gap if HAS_NUMPY else None),
    ("Diameter ~ dim_R = 10", 10, diameter),
    ("Domains ~ n_C*g = 35", 35, n_domains),
]

for name, predicted, actual in predictions:
    if actual is not None:
        err = abs(actual - predicted) / abs(predicted) * 100
        if err <= 3:
            v = "CONFIRMED"
        elif err <= 10:
            v = "CONSISTENT"
        else:
            v = "NO MATCH"
        print(f"  {name:40s} {predicted:10.4f} {actual:10.4f} {err:7.2f}% {v:>12s}")
    else:
        print(f"  {name:40s} {predicted:10.4f} {'N/A':>10s} {'N/A':>8s} {'N/A':>12s}")

# ── Additional: depth distribution check ──────────────────────────────
print("\n\n  ADDITIONAL: Depth distribution vs BST")
depth_counts = Counter(t["depth"] for t in theorems)
print(f"  D0: {depth_counts.get(0, 0)} ({depth_counts.get(0, 0)/N*100:.1f}%)")
print(f"  D1: {depth_counts.get(1, 0)} ({depth_counts.get(1, 0)/N*100:.1f}%)")
print(f"  D2: {depth_counts.get(2, 0)} ({depth_counts.get(2, 0)/N*100:.1f}%)")
d0_frac = depth_counts.get(0, 0) / N
print(f"  D0 fraction: {d0_frac:.4f}")
print(f"    Compare: (n_C-1)/n_C = 4/5 = 0.8000")
print(f"    Compare: 1 - 1/n_C = 0.8000")
d0_err = abs(d0_frac - 0.8) / 0.8 * 100
print(f"    Error: {d0_err:.2f}%")

# ── Status distribution ──────────────────────────────────────────────
print(f"\n  Status distribution:")
status_counts = Counter(t["status"] for t in theorems)
for s, c in status_counts.most_common():
    print(f"    {s:15s}: {c:4d} ({c/N*100:.1f}%)")

# ── Clustering coefficient ────────────────────────────────────────────
print(f"\n  CLUSTERING COEFFICIENT:")
total_cc = 0
count_cc = 0
for tid in all_tids:
    neighbors = list(adj[tid])
    k = len(neighbors)
    if k < 2:
        continue
    triangles = 0
    for i in range(k):
        for j in range(i+1, k):
            if neighbors[j] in adj[neighbors[i]]:
                triangles += 1
    cc = 2 * triangles / (k * (k - 1))
    total_cc += cc
    count_cc += 1

avg_cc = total_cc / count_cc if count_cc > 0 else 0
print(f"  Average clustering coefficient: {avg_cc:.6f}")
cc_match = find_bst_match(avg_cc, "clustering", 0.10)
if cc_match:
    print(f"  Nearest BST: {cc_match[0][0]} = {cc_match[0][1]:.6f} (err = {cc_match[0][2]*100:.2f}%)")
else:
    print(f"  No BST match within 10%")

# ── Edge density ──────────────────────────────────────────────────────
density = 2 * E / (N * (N - 1))
print(f"\n  Edge density: {density:.6f}")
print(f"  Compare: 1/N_max = {1/137:.6f}")
dens_err = abs(density - 1/137) / (1/137) * 100
print(f"  Error vs 1/N_max: {dens_err:.2f}%")

print(f"\n  Compare: rank/N = {2/N:.6f}")
print(f"  Compare: N_c/N = {3/N:.6f}")

print("\n" + "=" * 70)
print("END OF ANALYSIS")
print("=" * 70)
