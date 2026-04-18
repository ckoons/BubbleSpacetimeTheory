#!/usr/bin/env python3
"""
Toy 1264 — AC Graph Health Monitor
====================================
Quick intermediate status tool. Run anytime to see what the graph needs.

Reports:
  1. Node/edge counts and strong percentage
  2. Leaves and orphans
  3. Low-degree nodes (fragile)
  4. Domain sizes and thin domains
  5. Cross-domain coverage
  6. Edge type distribution and upgrade candidates
  7. Recent theorems (last 50) wiring quality
  8. Bridge deficit: domains with few cross-domain edges
  9. Missing sciences: domains that SHOULD exist but don't
  10. Actionable recommendations

Usage:
  python3 play/toy_1264_graph_health_monitor.py          # full report
  python3 play/toy_1264_graph_health_monitor.py --quick   # summary only
  python3 play/toy_1264_graph_health_monitor.py --thin    # thin domains detail
  python3 play/toy_1264_graph_health_monitor.py --fragile # fragile nodes detail
  python3 play/toy_1264_graph_health_monitor.py --bridges # bridge analysis

Elie — April 18, 2026

Copyright (c) 2026 Casey Koons. All rights reserved.
"""

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

# ── Load graph ──
GRAPH_PATH = Path(__file__).parent / "ac_graph_data.json"
with open(GRAPH_PATH) as f:
    data = json.load(f)

theorems = data.get("theorems", [])
edges = data.get("edges", [])
meta = data.get("meta", {})

# ── Build degree maps ──
degree = Counter()
in_degree = Counter()
out_degree = Counter()
for e in edges:
    src, tgt = e["from"], e["to"]
    degree[src] += 1
    degree[tgt] += 1
    out_degree[src] += 1
    in_degree[tgt] += 1

tid_map = {t["tid"]: t for t in theorems}
all_tids = set(tid_map.keys())

# ── Edge type counts ──
edge_types = Counter(e.get("source", "unknown") for e in edges)
strong_count = edge_types.get("derived", 0) + edge_types.get("isomorphic", 0)
strong_pct = 100 * strong_count / len(edges) if edges else 0

# ── Domain analysis ──
domain_of = {t["tid"]: t.get("domain", "unassigned") for t in theorems}
domain_sizes = Counter(domain_of.values())

# Cross-domain edges
cross_domain_edges = defaultdict(int)
domain_pair_edges = defaultdict(int)
for e in edges:
    d1 = domain_of.get(e["from"], "?")
    d2 = domain_of.get(e["to"], "?")
    if d1 != d2:
        pair = tuple(sorted([d1, d2]))
        domain_pair_edges[pair] += 1
        cross_domain_edges[d1] += 1
        cross_domain_edges[d2] += 1

cross_total = sum(1 for e in edges if domain_of.get(e["from"]) != domain_of.get(e["to"]))

# ── Low-degree analysis ──
low_degree_nodes = [(tid, degree.get(tid, 0)) for tid in all_tids if degree.get(tid, 0) <= 2]
low_degree_nodes.sort(key=lambda x: (x[1], x[0]))

# ── Recent theorems ──
recent_cutoff = max(all_tids) - 50
recent = [(t["tid"], t.get("name", "?")[:50], t.get("domain", "?"), degree.get(t["tid"], 0))
          for t in theorems if t["tid"] >= recent_cutoff]
recent.sort(key=lambda x: x[0])

# ── Fragile domains: domains where most nodes have low degree ──
domain_avg_degree = {}
for dom in domain_sizes:
    tids_in_dom = [tid for tid, d in domain_of.items() if d == dom]
    if tids_in_dom:
        avg = sum(degree.get(tid, 0) for tid in tids_in_dom) / len(tids_in_dom)
        domain_avg_degree[dom] = avg

# ── Bridge analysis: domain pairs with NO edges ──
all_domains = sorted(domain_sizes.keys())
n_domains = len(all_domains)
n_possible_pairs = n_domains * (n_domains - 1) // 2
n_connected_pairs = len(domain_pair_edges)
n_missing_pairs = n_possible_pairs - n_connected_pairs

# ── BST constants for classification ──
rank = 2
N_c = 3
n_C = 5
C_2 = 6
g = 7

# ═══════════════════════════════════════════════════════════════════════
# OUTPUT
# ═══════════════════════════════════════════════════════════════════════

mode = sys.argv[1] if len(sys.argv) > 1 else "--full"

print("=" * 70)
print("AC Graph Health Monitor — Toy 1264")
print("=" * 70)

# ── Section 1: Summary ──
print(f"\n── Summary ──")
print(f"  Theorems:        {len(theorems)}")
print(f"  Edges:           {len(edges)}")
print(f"  Strong edges:    {strong_count} ({strong_pct:.1f}%)")
print(f"  Avg degree:      {sum(degree.values()) / len(degree):.1f}" if degree else "  Avg degree: 0")
print(f"  Domains:         {n_domains}")
print(f"  Cross-domain:    {cross_total}/{len(edges)} ({100*cross_total/len(edges):.1f}%)")
print(f"  Low-degree (≤2): {len(low_degree_nodes)}")
print(f"  Domain pairs:    {n_connected_pairs}/{n_possible_pairs} connected ({n_missing_pairs} missing)")

# ── Health score ──
# Weighted: strong% (40), avg_degree (20), cross-domain% (20), low-degree penalty (20)
avg_deg = sum(degree.values()) / len(degree) if degree else 0
cross_pct = 100 * cross_total / len(edges) if edges else 0
low_pct = 100 * len(low_degree_nodes) / len(theorems) if theorems else 100

health = (
    0.40 * min(strong_pct / 85, 1.0) * 100 +   # target 85% strong
    0.20 * min(avg_deg / 12, 1.0) * 100 +        # target avg degree 12
    0.20 * min(cross_pct / 70, 1.0) * 100 +      # target 70% cross-domain
    0.20 * max(0, 100 - low_pct * 5)              # penalize low-degree nodes
)
grade = "A+" if health >= 95 else "A" if health >= 90 else "A-" if health >= 85 else \
        "B+" if health >= 80 else "B" if health >= 75 else "B-" if health >= 70 else \
        "C+" if health >= 65 else "C" if health >= 60 else "C-" if health >= 55 else "D"
print(f"\n  HEALTH SCORE: {health:.1f}/100 ({grade})")

# ── Edge type breakdown ──
print(f"\n── Edge Types ──")
for etype, count in edge_types.most_common():
    pct = 100 * count / len(edges)
    bar = "█" * int(pct / 2)
    label = "STRONG" if etype in ("derived", "isomorphic") else "weak"
    print(f"  {etype:15s} {count:5d} ({pct:5.1f}%) {bar} [{label}]")

if mode == "--quick":
    print("\n" + "=" * 70)
    sys.exit(0)

# ── Thin domains ──
print(f"\n── Thin Domains (≤ 10 nodes) ──")
thin = [(d, c) for d, c in domain_sizes.items() if c <= 10]
thin.sort(key=lambda x: x[1])
for dom, count in thin:
    avg = domain_avg_degree.get(dom, 0)
    cross = cross_domain_edges.get(dom, 0)
    print(f"  {dom:30s} nodes={count:3d}  avg_deg={avg:.1f}  cross_edges={cross}")

if mode == "--thin":
    # Show what each thin domain contains
    for dom, count in thin:
        print(f"\n  {dom} ({count} nodes):")
        tids = sorted([tid for tid, d in domain_of.items() if d == dom])
        for tid in tids:
            t = tid_map.get(tid, {})
            d = degree.get(tid, 0)
            print(f"    T{tid}: {t.get('name', '?')[:55]} [deg={d}]")
    print("\n" + "=" * 70)
    sys.exit(0)

# ── Low-degree detail ──
if mode == "--fragile":
    print(f"\n── Fragile Nodes (degree ≤ 2) — {len(low_degree_nodes)} total ──")
    for tid, deg in low_degree_nodes[:50]:
        t = tid_map.get(tid, {})
        print(f"  T{tid:4d}: deg={deg} [{t.get('domain', '?'):20s}] {t.get('name', '?')[:45]}")
    if len(low_degree_nodes) > 50:
        print(f"  ... and {len(low_degree_nodes) - 50} more")
    print("\n" + "=" * 70)
    sys.exit(0)

# ── Bridge analysis ──
if mode == "--bridges":
    print(f"\n── Domain Bridge Analysis ──")
    print(f"  Connected pairs: {n_connected_pairs}/{n_possible_pairs}")
    print(f"  Missing pairs:   {n_missing_pairs}")

    # Strongest bridges (most cross-domain edges)
    print(f"\n  Top 20 bridges (by edge count):")
    for pair, count in sorted(domain_pair_edges.items(), key=lambda x: -x[1])[:20]:
        print(f"    {pair[0]:25s} ↔ {pair[1]:25s}  edges={count}")

    # Domains most isolated
    print(f"\n  Most isolated domains (fewest cross-domain edges):")
    for dom in sorted(domain_sizes.keys(), key=lambda d: cross_domain_edges.get(d, 0)):
        cross = cross_domain_edges.get(dom, 0)
        total = sum(degree.get(tid, 0) for tid, d in domain_of.items() if d == dom)
        if total > 0:
            ratio = cross / total
            print(f"    {dom:30s} cross={cross:4d}  total={total:4d}  ratio={ratio:.2f}")
    print("\n" + "=" * 70)
    sys.exit(0)

# ── Recent theorems wiring quality ──
print(f"\n── Recent Theorems (T{recent_cutoff}+) ──")
thin_recent = [r for r in recent if r[3] <= 5]
print(f"  Total recent: {len(recent)}, Thin (≤5 edges): {len(thin_recent)}")
if thin_recent:
    print(f"  Thin recent theorems:")
    for tid, name, dom, deg in thin_recent:
        print(f"    T{tid}: deg={deg} [{dom:20s}] {name}")

# ── Upgrade candidates ──
print(f"\n── Upgrade Candidates ──")
print(f"  Observed → derived/isomorphic: {edge_types.get('observed', 0)} edges")
print(f"  Analogical (audit needed):     {edge_types.get('analogical', 0)} edges")
print(f"  If all observed upgraded:      strong would be {100*(strong_count + edge_types.get('observed', 0))/len(edges):.1f}%")

# ── Recommendations ──
print(f"\n── Actionable Recommendations ──")
recs = []
if strong_pct < 80:
    recs.append(f"1. STRONG%: {strong_pct:.1f}% < 80% target. Upgrade {int((0.80*len(edges) - strong_count))} observed→derived edges.")
if len(low_degree_nodes) > 50:
    recs.append(f"2. FRAGILE: {len(low_degree_nodes)} nodes with ≤2 edges. Run --fragile for list.")
if n_missing_pairs > 100:
    recs.append(f"3. BRIDGES: {n_missing_pairs} domain pairs unconnected. Run --bridges for detail.")
thin_count = len([d for d, c in domain_sizes.items() if c <= 3])
if thin_count > 5:
    recs.append(f"4. THIN DOMAINS: {thin_count} domains with ≤3 nodes. Merge or expand.")
if len(thin_recent) > 10:
    recs.append(f"5. RECENT WIRING: {len(thin_recent)} recent theorems with ≤5 edges. Wire them.")
if avg_deg < 10:
    recs.append(f"6. DENSITY: avg degree {avg_deg:.1f} < 10 target. Add edges to hubs.")

if not recs:
    recs.append("Graph is healthy! Focus on new theorems and cross-domain bridges.")

for r in recs:
    print(f"  {r}")

# ── Score section ──
print(f"\n── Tests ──")
passed = 0
total_tests = 12
tests = [
    ("Graph loaded", len(theorems) > 0 and len(edges) > 0),
    ("No orphan nodes", all(degree.get(t["tid"], 0) > 0 for t in theorems)),
    (f"Strong ≥ 75%", strong_pct >= 75),
    (f"Strong ≥ 80% (stretch)", strong_pct >= 80),
    (f"Avg degree ≥ 8", avg_deg >= 8),
    (f"Cross-domain ≥ 60%", cross_pct >= 60),
    (f"Low-degree < 10% of nodes", len(low_degree_nodes) < 0.10 * len(theorems)),
    (f"Domains ≥ 30", n_domains >= 30),
    (f"Domain connectivity ≥ 80%", n_connected_pairs / n_possible_pairs >= 0.80 if n_possible_pairs > 0 else False),
    (f"No domain with avg degree < 3", all(v >= 3 for v in domain_avg_degree.values())),
    (f"Recent theorems avg degree ≥ 6", sum(r[3] for r in recent) / len(recent) >= 6 if recent else False),
    (f"Health score ≥ 75", health >= 75),
]

for name, cond in tests:
    status = "PASS" if cond else "FAIL"
    if cond:
        passed += 1
    print(f"  [{status}] {name}")

print(f"\n{'=' * 70}")
print(f"SCORE: {passed}/{total_tests} PASS")
print(f"HEALTH: {health:.1f}/100 ({grade})")
print(f"{'=' * 70}")
