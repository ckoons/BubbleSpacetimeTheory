"""Toy — catalog domain coverage matrix (which BST domain has most entries)."""
import json
from collections import Counter
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
dom_counts = Counter(i.get('domain', '(none)') for i in d['invariants'] if isinstance(i, dict))
print(f"Total catalog: {sum(dom_counts.values())}")
print("\nTop 20 catalog domains:")
for d_, c in dom_counts.most_common(20):
    print(f"  {c:4d} — {d_}")
print("[PASS]")
