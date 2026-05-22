"""Toy — catalog precision distribution audit."""
import json
from collections import Counter
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
prec_dist = Counter()
for i in d['invariants']:
    if not isinstance(i, dict): continue
    p = i.get('precision', 'no_field')
    if p is None: p = 'null'
    prec_dist[str(p)[:30]] += 1
print(f"Precision field distribution (top 10):")
for p, c in prec_dist.most_common(10):
    print(f"  {c:4d} — {p}")
print("[PASS]")
