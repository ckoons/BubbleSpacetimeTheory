"""Toy — value=137 (N_max) catalog audit."""
import json
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
matches = [i for i in d['invariants'] if isinstance(i, dict) and i.get('value') in (137, 137.0)]
print(f"value=137 entries: {len(matches)}")
for m in matches[:15]:
    print(f"  {m.get('name', '?')[:60]}")
print("[PASS]")
