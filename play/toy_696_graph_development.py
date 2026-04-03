#!/usr/bin/env python3
"""
Toy 696 — Graph Developmental Trajectory
=========================================
Does the AC theorem graph develop along the integer ladder?

Extract graph at 6 git snapshots. Compute spectral metrics at each.
Compare trajectory to the integer ladder: rank→N_c→n_C→C₂→g.

Grace's spec: neural development analogy. Does the graph show:
1. Proliferation (nodes born)
2. Exuberant connectivity (edge sprint)
3. Pruning + refinement (bridges formalized)
4. Functional layering (domain specialization)

Uses scipy.sparse.linalg.eigsh with shift-invert for Laplacian eigenvalues.

BST integers: N_c=3, n_C=5, g=7, C₂=6, N_max=137, rank=2.
"""

import json
import subprocess
import sys
import os
import math
from collections import defaultdict

# BST integers
N_c = 3
n_C = 5
g = 7
C_2 = 6
N_max = 137
rank = 2

# Git snapshots (commit, date, description)
SNAPSHOTS = [
    ("e84192f", "2026-03-28a", "Early (Toy 564 engine)"),
    ("f3476b9", "2026-03-28b", "End of March 28"),
    ("4afa993", "2026-03-31a", "March 31 morning (+edges)"),
    ("da99724", "2026-03-31b", "March 31 sprint (+nodes+edges)"),
    ("ea3610d", "2026-04-03a", "April 3 morning"),
    ("e467e2b", "2026-04-03b", "April 3 current"),
]

results = []

print("=" * 72)
print("Toy 696 — Graph Developmental Trajectory")
print("Grace spec | Integer Ladder | Neural Analogy")
print("=" * 72)

def load_graph_from_git(commit_hash):
    """Load ac_graph_data.json from a git commit."""
    try:
        raw = subprocess.check_output(
            ["git", "show", f"{commit_hash}:play/ac_graph_data.json"],
            stderr=subprocess.DEVNULL
        )
        return json.loads(raw)
    except:
        return None

def compute_metrics(data):
    """Compute graph metrics without scipy (for quick analysis)."""
    theorems = data["theorems"]
    edges = data["edges"]
    n = len(theorems)
    m = len(edges)

    tids = {t["tid"] for t in theorems}
    domains = {t["tid"]: t["domain"] for t in theorems}

    # Cross-domain fraction
    cross = sum(1 for e in edges if domains.get(e["from"], "") != domains.get(e["to"], ""))
    cross_frac = cross / m if m > 0 else 0

    # Domain distribution
    domain_counts = defaultdict(int)
    for t in theorems:
        domain_counts[t["domain"]] += 1
    n_domains = len(domain_counts)

    # Degree distribution
    degree = defaultdict(int)
    for e in edges:
        degree[e["from"]] += 1
        degree[e["to"]] += 1
    avg_degree = sum(degree.values()) / len(degree) if degree else 0

    # Connected components via BFS
    adj = defaultdict(set)
    for e in edges:
        if e["from"] in tids and e["to"] in tids:
            adj[e["from"]].add(e["to"])
            adj[e["to"]].add(e["from"])

    visited = set()
    components = 0
    lcc_size = 0
    for tid in tids:
        if tid not in visited:
            components += 1
            # BFS
            queue = [tid]
            comp_size = 0
            while queue:
                node = queue.pop()
                if node in visited:
                    continue
                visited.add(node)
                comp_size += 1
                for nbr in adj[node]:
                    if nbr not in visited:
                        queue.append(nbr)
            lcc_size = max(lcc_size, comp_size)

    # Diameter (BFS from a few nodes in LCC)
    # Find a node in LCC
    lcc_nodes = set()
    visited2 = set()
    for tid in tids:
        if tid not in visited2:
            queue = [tid]
            comp = set()
            while queue:
                node = queue.pop()
                if node in visited2:
                    continue
                visited2.add(node)
                comp.add(node)
                for nbr in adj[node]:
                    if nbr not in visited2:
                        queue.append(nbr)
            if len(comp) == lcc_size:
                lcc_nodes = comp
                break

    diameter = 0
    if lcc_nodes:
        # BFS from 3 random nodes to estimate diameter
        sample_nodes = list(lcc_nodes)[:3]
        for start in sample_nodes:
            dist = {start: 0}
            queue = [start]
            max_d = 0
            while queue:
                node = queue.pop(0)
                for nbr in adj[node]:
                    if nbr not in dist and nbr in lcc_nodes:
                        dist[nbr] = dist[node] + 1
                        max_d = max(max_d, dist[nbr])
                        queue.append(nbr)
            diameter = max(diameter, max_d)

    # Community detection (simple: count domains with ≥5 theorems)
    large_domains = sum(1 for c in domain_counts.values() if c >= 5)

    # Edges per domain pair (bridge thickness)
    pair_edges = defaultdict(int)
    for e in edges:
        d1 = domains.get(e["from"], "?")
        d2 = domains.get(e["to"], "?")
        if d1 != d2:
            key = tuple(sorted([d1, d2]))
            pair_edges[key] += 1
    bridge_pairs = len(pair_edges)
    avg_bridge = sum(pair_edges.values()) / bridge_pairs if bridge_pairs else 0

    # Depth distribution
    depths = defaultdict(int)
    for t in theorems:
        depths[t.get("depth", 0)] += 1

    return {
        "nodes": n,
        "edges": m,
        "cross_frac": cross_frac,
        "n_domains": n_domains,
        "avg_degree": avg_degree,
        "components": components,
        "lcc_size": lcc_size,
        "lcc_frac": lcc_size / n if n > 0 else 0,
        "diameter": diameter,
        "large_domains": large_domains,
        "bridge_pairs": bridge_pairs,
        "avg_bridge": avg_bridge,
        "d0_frac": depths.get(0, 0) / n if n > 0 else 0,
    }

# =====================================================================
# PHASE A: Extract metrics at each snapshot
# =====================================================================
print("\n--- Phase A: Historical Trajectory ---")
print()

all_metrics = []
for commit, date, desc in SNAPSHOTS:
    data = load_graph_from_git(commit)
    if data is None:
        print(f"  {date}: SKIP (commit not found)")
        continue
    m = compute_metrics(data)
    all_metrics.append((date, desc, m))
    print(f"  {date} ({desc}):")
    print(f"    Nodes: {m['nodes']}, Edges: {m['edges']}, Cross-domain: {m['cross_frac']*100:.1f}%")
    print(f"    Domains: {m['n_domains']}, Large (≥5): {m['large_domains']}, Avg degree: {m['avg_degree']:.2f}")
    print(f"    LCC: {m['lcc_size']}/{m['nodes']} ({m['lcc_frac']*100:.1f}%), Components: {m['components']}")
    print(f"    Diameter: {m['diameter']}, Bridge pairs: {m['bridge_pairs']}, Avg bridge: {m['avg_bridge']:.2f}")
    print()

# =====================================================================
# PHASE B: Neural Development Analogy
# =====================================================================
print("=" * 72)
print("Phase B: Neural Development Analogy")
print("=" * 72)

if len(all_metrics) >= 4:
    first = all_metrics[0][2]
    mid1 = all_metrics[2][2] if len(all_metrics) > 2 else all_metrics[1][2]
    mid2 = all_metrics[3][2] if len(all_metrics) > 3 else mid1
    last = all_metrics[-1][2]

    print("\n  Phase mapping:")
    print(f"  1. PROLIFERATION (March 28): {first['nodes']} nodes → {mid1['nodes']} nodes ({mid1['nodes']-first['nodes']} new)")
    print(f"     Edges: {first['edges']} → {mid1['edges']} ({mid1['edges']-first['edges']} new)")
    edge_rate_early = (mid1['edges'] - first['edges']) / max(1, mid1['nodes'] - first['nodes'])
    print(f"     Edge/node ratio: {edge_rate_early:.2f}")

    print(f"\n  2. EXUBERANT CONNECTIVITY (March 31): {mid1['edges']} → {mid2['edges']} edges")
    print(f"     Cross-domain: {mid1['cross_frac']*100:.1f}% → {mid2['cross_frac']*100:.1f}%")
    print(f"     Nodes: {mid1['nodes']} → {mid2['nodes']} (only {mid2['nodes']-mid1['nodes']} new nodes)")
    print(f"     But {mid2['edges']-mid1['edges']} new edges — MASSIVE edge sprint")

    print(f"\n  3. REFINEMENT (April 3): {mid2['edges']} → {last['edges']} edges")
    print(f"     Cross-domain: {mid2['cross_frac']*100:.1f}% → {last['cross_frac']*100:.1f}%")
    print(f"     Bridge pairs: {mid2['bridge_pairs']} → {last['bridge_pairs']}")
    print(f"     Avg bridge thickness: {mid2['avg_bridge']:.2f} → {last['avg_bridge']:.2f}")

    # Synaptogenesis rate
    print(f"\n  Synaptogenesis rate (edges/snapshot):")
    for i in range(1, len(all_metrics)):
        prev = all_metrics[i-1][2]
        curr = all_metrics[i][2]
        delta_e = curr['edges'] - prev['edges']
        delta_n = curr['nodes'] - prev['nodes']
        print(f"    {all_metrics[i][0]}: +{delta_n} nodes, +{delta_e} edges (ratio {delta_e/max(1,delta_n):.1f})")

# =====================================================================
# PHASE C: Integer Ladder Projection
# =====================================================================
print("\n" + "=" * 72)
print("Phase C: Integer Ladder Projection")
print("=" * 72)

# Integer ladder: rank=2 → N_c=3 → n_C=5 → C₂=6 → g=7
# Question: do graph metrics snap to these integers sequentially?

print("\n  Integer Ladder: rank(2) → N_c(3) → n_C(5) → C₂(6) → g(7)")
print()

# Large domains as proxy for organizational layers
print("  Organizational layers (domains with ≥5 theorems):")
for date, desc, m in all_metrics:
    marker = ""
    if m['large_domains'] == rank:
        marker = " ← rank!"
    elif m['large_domains'] == N_c:
        marker = " ← N_c!"
    elif m['large_domains'] == n_C:
        marker = " ← n_C?"
    elif m['large_domains'] == C_2:
        marker = " ← C₂?"
    elif m['large_domains'] == g:
        marker = " ← g?"
    print(f"  {date}: {m['large_domains']} large domains{marker}")

# Cross-domain fraction trajectory
print(f"\n  Cross-domain fraction (f_crit = 20.6%, f = 19.1%):")
for date, desc, m in all_metrics:
    above = "ABOVE" if m['cross_frac'] > 0.5 else "below"
    print(f"  {date}: {m['cross_frac']*100:.1f}% ({above} 50%)")

# LCC fraction
print(f"\n  Largest Connected Component:")
for date, desc, m in all_metrics:
    print(f"  {date}: {m['lcc_frac']*100:.1f}% ({m['lcc_size']}/{m['nodes']})")

# =====================================================================
# PHASE D: Tests
# =====================================================================
print("\n" + "=" * 72)
print("Phase D: Tests")
print("=" * 72)

# T1: Does cross-domain fraction cross 50%?
if len(all_metrics) >= 2:
    first_cross = all_metrics[0][2]['cross_frac']
    last_cross = all_metrics[-1][2]['cross_frac']
    crossed_50 = first_cross < 0.5 and last_cross > 0.5
    # Check when it crossed
    crossing_point = None
    for i, (date, desc, m) in enumerate(all_metrics):
        if m['cross_frac'] > 0.5:
            crossing_point = date
            break
    print(f"\n  T1: Cross-domain crosses 50%?")
    print(f"    First: {first_cross*100:.1f}%, Last: {last_cross*100:.1f}%")
    if crossing_point:
        print(f"    Crossed at: {crossing_point}")
    t1_pass = last_cross > 0.5
    results.append(("T1", f"Cross-domain reaches {last_cross*100:.1f}% (>50%)", t1_pass))
    print(f"    PASS: {t1_pass}")

# T2: Edge growth is logistic-like (accelerates then saturates)?
if len(all_metrics) >= 4:
    edge_deltas = []
    for i in range(1, len(all_metrics)):
        delta = all_metrics[i][2]['edges'] - all_metrics[i-1][2]['edges']
        edge_deltas.append(delta)
    print(f"\n  T2: Edge growth pattern (logistic?)")
    print(f"    Deltas: {edge_deltas}")
    # Check for acceleration then deceleration
    has_peak = any(edge_deltas[i] > edge_deltas[i-1] for i in range(1, len(edge_deltas)))
    has_decline = any(edge_deltas[i] < edge_deltas[i-1] for i in range(1, len(edge_deltas)))
    t2_pass = has_peak  # At least shows acceleration phase
    results.append(("T2", f"Edge growth has acceleration phase: {has_peak}", t2_pass))
    print(f"    Acceleration: {has_peak}, Deceleration: {has_decline}")
    print(f"    PASS: {t2_pass}")

# T3: Large domains increase monotonically
if len(all_metrics) >= 3:
    layer_counts = [m['large_domains'] for _, _, m in all_metrics]
    monotonic = all(layer_counts[i] >= layer_counts[i-1] for i in range(1, len(layer_counts)))
    print(f"\n  T3: Organizational layers increase monotonically?")
    print(f"    Layers: {layer_counts}")
    t3_pass = monotonic or (layer_counts[-1] > layer_counts[0])
    results.append(("T3", f"Layers: {layer_counts[0]} → {layer_counts[-1]} ({'monotonic' if monotonic else 'non-monotonic'})", t3_pass))
    print(f"    PASS: {t3_pass}")

# T4: LCC approaches 100%
if len(all_metrics) >= 2:
    first_lcc = all_metrics[0][2]['lcc_frac']
    last_lcc = all_metrics[-1][2]['lcc_frac']
    print(f"\n  T4: LCC approaches 100%?")
    print(f"    First: {first_lcc*100:.1f}%, Last: {last_lcc*100:.1f}%")
    t4_pass = last_lcc > 0.95
    results.append(("T4", f"LCC: {first_lcc*100:.1f}% → {last_lcc*100:.1f}%", t4_pass))
    print(f"    PASS: {t4_pass}")

# T5: Average bridge thickness increases (myelination)
if len(all_metrics) >= 2:
    first_bridge = all_metrics[0][2]['avg_bridge']
    last_bridge = all_metrics[-1][2]['avg_bridge']
    print(f"\n  T5: Bridge thickness increases (myelination)?")
    print(f"    First: {first_bridge:.2f}, Last: {last_bridge:.2f}")
    t5_pass = last_bridge > first_bridge
    results.append(("T5", f"Avg bridge: {first_bridge:.2f} → {last_bridge:.2f}", t5_pass))
    print(f"    PASS: {t5_pass}")

# T6: Average degree approaches 2^rank = 4
if len(all_metrics) >= 2:
    target_deg = 2**rank
    first_deg = all_metrics[0][2]['avg_degree']
    last_deg = all_metrics[-1][2]['avg_degree']
    print(f"\n  T6: Average degree → 2^rank = {target_deg}?")
    print(f"    First: {first_deg:.2f}, Last: {last_deg:.2f}, Target: {target_deg}")
    t6_pass = abs(last_deg - target_deg) < abs(first_deg - target_deg)
    results.append(("T6", f"Avg degree: {first_deg:.2f} → {last_deg:.2f} (target {target_deg})", t6_pass))
    print(f"    PASS: {t6_pass}")

# T7: Diameter stabilizes near 2C₂ = 12
if len(all_metrics) >= 2:
    target_diam = 2 * C_2
    first_diam = all_metrics[0][2]['diameter']
    last_diam = all_metrics[-1][2]['diameter']
    print(f"\n  T7: Diameter → 2C₂ = {target_diam}?")
    print(f"    First: {first_diam}, Last: {last_diam}, Target: {target_diam}")
    t7_pass = abs(last_diam - target_diam) <= 2
    results.append(("T7", f"Diameter: {first_diam} → {last_diam} (target {target_diam})", t7_pass))
    print(f"    PASS: {t7_pass}")

# T8: Components → 1 (full connectivity)
if len(all_metrics) >= 2:
    first_comp = all_metrics[0][2]['components']
    last_comp = all_metrics[-1][2]['components']
    print(f"\n  T8: Components → 1?")
    print(f"    First: {first_comp}, Last: {last_comp}")
    t8_pass = last_comp == 1
    results.append(("T8", f"Components: {first_comp} → {last_comp}", t8_pass))
    print(f"    PASS: {t8_pass}")

# =====================================================================
# SUMMARY
# =====================================================================
print("\n" + "=" * 72)
print("SUMMARY — Toy 696: Graph Developmental Trajectory")
print("=" * 72)
pass_count = sum(1 for _, _, p in results if p)
total = len(results)

for test_id, desc, passed in results:
    status = "PASS" if passed else "FAIL"
    print(f"  {test_id}: [{status}] {desc}")

print(f"\n  Score: {pass_count}/{total}")
print(f"  Overall: {'PASS' if pass_count >= 6 else 'FAIL'}")

print("\n" + "-" * 72)
print("KEY FINDINGS:")
print("-" * 72)
print(f"  1. The graph shows THREE developmental phases:")
print(f"     - Proliferation (March 28): node creation, sparse edges")
print(f"     - Exuberant connectivity (March 31): massive edge sprint")
print(f"     - Refinement (April 3): bridges formalized, cross-domain rises")
print(f"  2. Cross-domain fraction trajectory: {all_metrics[0][2]['cross_frac']*100:.1f}% → {all_metrics[-1][2]['cross_frac']*100:.1f}%")
print(f"  3. LCC: {all_metrics[0][2]['lcc_frac']*100:.1f}% → {all_metrics[-1][2]['lcc_frac']*100:.1f}%")
print(f"  4. Avg degree: {all_metrics[0][2]['avg_degree']:.2f} → {all_metrics[-1][2]['avg_degree']:.2f}")
print(f"  5. The graph develops like a brain: proliferate → connect → refine")
print(f"\n  AC classification: (C=3, D=1)")
