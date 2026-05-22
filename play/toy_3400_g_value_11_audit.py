"""Toy — value=11 audit (β₀ pure YM Weitzenbock coefficient)."""
import json
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
matches = [i for i in d['invariants'] if isinstance(i, dict) and i.get('value') in (11, 11.0)]
print(f"value=11 entries: {len(matches)}")
for m in matches[:15]:
    print(f"  {m.get('name', '?')[:65]}")
print("[PASS]")
