"""Toy — value=126 (Universal Q) and 127 (M_g) catalog audits."""
import json
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
for tv in (126, 127):
    matches = [i for i in d['invariants'] if isinstance(i, dict) and i.get('value') in (tv, float(tv))]
    print(f"\nvalue={tv} entries: {len(matches)}")
    for m in matches[:10]:
        print(f"  {m.get('name', '?')[:60]}")
print("[PASS]")
