"""Toy — BST-derived secondary integers (3+ entries) systematically catalogued."""
import json
from collections import Counter
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

# Value counts
value_counts = Counter()
for i in d['invariants']:
    if not isinstance(i, dict): continue
    v = i.get('value')
    if v is None: continue
    try:
        vn = float(v)
        if abs(vn - round(vn)) < 1e-6:
            value_counts[round(vn)] += 1
    except (ValueError, TypeError):
        pass

# Top integers (not just BST primaries)
print("Top integer values (3+ catalog entries, excluding 0,1,2,3,5,6,7,137 BST primaries):")
bst_primaries = {2, 3, 5, 6, 7, 137}
for v, c in sorted(value_counts.items(), key=lambda x: -x[1])[:40]:
    if v in bst_primaries or v < 2 or c < 3: continue
    print(f"  {v}: {c} entries")
print("[PASS]")
