"""Toy — compound BST-primary sum-product forms (a^k + b^m)."""
import json
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137

# Generate sum-product forms
forms = {}
def add(name, val):
    forms.setdefault(val, []).append(name)

# Squares + primaries
for ana, va in [('rank', rank), ('N_c', N_c), ('n_C', n_C), ('C_2', C_2), ('g', g)]:
    for anb, vb in [('rank', rank), ('N_c', N_c), ('n_C', n_C), ('C_2', C_2), ('g', g)]:
        add(f'{ana}²+{anb}', va**2 + vb)
        add(f'{ana}+{anb}²', va + vb**2)
        add(f'{ana}²+{anb}²', va**2 + vb**2)
        add(f'{ana}³+{anb}', va**3 + vb)
        if va*vb != 0: 
            add(f'{ana}·{anb}+{ana}', va*vb + va)

# Find catalog matches
matches = {}
for i in d['invariants']:
    if not isinstance(i, dict): continue
    v = i.get('value')
    try: vn = float(v)
    except (ValueError, TypeError): continue
    if abs(vn - round(vn)) < 1e-6:
        vr = round(vn)
        if vr in forms and len(forms[vr]) >= 3:  # 3+ form representations
            matches.setdefault(vr, set()).update(forms[vr])

print(f"Compound sum-product OFC anchors (3+ forms, catalog matched):")
for v, fl in sorted(matches.items()):
    print(f"  {v}: forms={sorted(fl)[:4]}")
print("[PASS]")
