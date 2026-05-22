"""Toy — AC graph edge pattern analysis (substrate connectivity)."""
import json
from collections import Counter

with open('play/ac_graph_data.json') as f:
    g = json.load(f)

edges = g.get('edges', [])
print(f"Total edges: {len(edges)}")

# Edge type distribution
edge_types = Counter()
for e in edges:
    if isinstance(e, dict):
        edge_types[e.get('type', 'unknown')] += 1
print("\nEdge types:")
for t, c in edge_types.most_common(15):
    print(f"  {c:5d} — {t}")

# Edge source patterns (which nodes have most edges)
node_outdegree = Counter()
node_indegree = Counter()
for e in edges:
    if isinstance(e, dict):
        if 'from' in e: node_outdegree[e['from']] += 1
        if 'to' in e: node_indegree[e['to']] += 1

print("\nTop 10 high out-degree nodes (most-referenced from):")
for n, c in node_outdegree.most_common(10):
    print(f"  T{n}: {c} outgoing")

print("\nTop 10 high in-degree nodes (most-referenced to):")
for n, c in node_indegree.most_common(10):
    print(f"  T{n}: {c} incoming")

print("\n[PASS] x6 — AC graph edge structure analyzed")
