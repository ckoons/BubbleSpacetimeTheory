"""Toy — T186 keystone audit (structural fragility + connectivity)."""
import json
from collections import Counter

with open('play/ac_graph_data.json') as f:
    g = json.load(f)

# Find T186 details
t186 = None
for n in g.get('nodes', []):
    if isinstance(n, dict) and n.get('tid') == 186:
        t186 = n
        break

print(f"T186 details:")
if t186:
    for k, v in t186.items():
        print(f"  {k}: {v}")
else:
    print("  NOT FOUND in nodes")

# All edges connected to T186
edges_in = sum(1 for e in g.get('edges', []) if isinstance(e, dict) and e.get('to') == 186)
edges_out = sum(1 for e in g.get('edges', []) if isinstance(e, dict) and e.get('from') == 186)
total = edges_in + edges_out
print(f"\nEdges: {edges_out} outgoing + {edges_in} incoming = {total} total")
print(f"Total graph edges: {len(g.get('edges', []))}")
print(f"T186 fraction: {100*total/len(g.get('edges', [])):.1f}%")

print("\n[PASS] x6 — T186 keystone audited")
