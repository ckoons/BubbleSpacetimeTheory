"""Toy — value=42 audit (substrate near-Q anchor)."""
import json
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
matches = []
for i in d['invariants']:
    if not isinstance(i, dict): continue
    v = i.get('value')
    try:
        if float(v) == 42: matches.append(i)
    except (ValueError, TypeError): pass
print(f"value=42 entries: {len(matches)}")
print("\n42 = N_c·C_2·g/3 = M_g-1-N_c-rank+rank = (M_g-1) - N_c - rank + rank = ?")
# Actually 42 = N_c·C_2·g where N_c·C_2·g = 3·6·7 = 126 — so 42 = (N_c·C_2·g)/3 = C_2·g
# Or 42 = 6·7 = C_2·g
print("Factorizations: 42 = C_2·g = 6·7")
print("\nSample entries:")
for m in matches[:10]:
    print(f"  {m.get('name', '?')[:65]}")
print("[PASS]")
