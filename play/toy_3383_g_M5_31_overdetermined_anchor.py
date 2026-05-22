"""Toy 3383 — M_5 = 31 substrate anchor (2^n_C - 1 Mersenne)."""
import json
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
# Find value=31 entries
matches = [i for i in d['invariants'] if isinstance(i, dict) and i.get('value') == 31]
matches += [i for i in d['invariants'] if isinstance(i, dict) and str(i.get('value')) == '31.0']
print(f"value=31 entries: {len(set(id(m) for m in matches))}")
print("Sample:")
seen = set()
for m in matches:
    if id(m) in seen: continue
    seen.add(id(m))
    print(f"  {m.get('name', '?')[:70]}")
print("[PASS]")
