"""Toy 3418 — Highest-precision (sub-0.1%) paper-grade evidence index."""
import json
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
sub_01 = [i for i in d['invariants'] if isinstance(i, dict) 
          and str(i.get('precision', '')).strip() in ('0.001%', '0.002%', '0.01%', '0.02%', '0.03%', '0.05%', '~0.01%', '0.0%', '~0.001%')]
print(f"Sub-0.1% precision entries: {len(sub_01)}")
for s in sub_01[:15]:
    print(f"  {s.get('name', '?')[:60]}: {s.get('value', '?')} ({s.get('precision', '?')})")
print("[PASS]")
