"""Toy — catalog value histogram (integer distribution)."""
import json
from collections import Counter
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
int_values = []
for i in d['invariants']:
    if not isinstance(i, dict): continue
    v = i.get('value')
    try: vn = float(v)
    except (ValueError, TypeError): continue
    if abs(vn - round(vn)) < 1e-6 and 0 < vn < 1000:
        int_values.append(round(vn))
# Bin in ranges
ranges = [(0, 10), (10, 30), (30, 100), (100, 300), (300, 1000)]
print(f"Integer-value catalog distribution:")
for lo, hi in ranges:
    count = sum(1 for v in int_values if lo <= v < hi)
    print(f"  {lo}-{hi}: {count}")
# Top integer values
c = Counter(int_values)
print(f"\nTop 20 by frequency:")
for v, n in c.most_common(20):
    print(f"  {v}: {n}")
print("[PASS]")
