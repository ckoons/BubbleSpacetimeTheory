"""Toy — value=4 audit (rank² highest-frequency secondary)."""
import json
from collections import Counter
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
matches = [i for i in d['invariants'] if isinstance(i, dict) and i.get('value') in (4, 4.0)]
print(f"value=4 entries: {len(matches)}")
domains = Counter(i.get('domain', '(none)') for i in matches)
print("Top domains:")
for d_, c in domains.most_common(8):
    print(f"  {c:3d} — {d_}")
print("[PASS]")
