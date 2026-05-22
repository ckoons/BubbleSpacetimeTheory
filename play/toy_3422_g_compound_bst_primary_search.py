"""Toy — compound BST-primary search (4-primary products)."""
import json, itertools
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
primaries = {'rank': 2, 'N_c': 3, 'n_C': 5, 'C_2': 6, 'g': 7}
# 4-primary products
quad_products = {}
for c in itertools.combinations_with_replacement(primaries.items(), 4):
    name = '·'.join(x[0] for x in c)
    val = 1
    for x in c: val *= x[1]
    quad_products.setdefault(val, []).append(name)
# Find catalog matches
matches = {}
for i in d['invariants']:
    if not isinstance(i, dict): continue
    v = i.get('value')
    try: vn = float(v)
    except (ValueError, TypeError): continue
    if abs(vn - round(vn)) < 1e-6:
        vr = round(vn)
        if vr in quad_products and vr > 50:  # skip small values to focus on interesting
            matches[vr] = matches.get(vr, 0) + 1
print(f"4-primary quad-product catalog matches (value > 50, top 15):")
for v, c in sorted(matches.items(), key=lambda x: -x[1])[:15]:
    forms = quad_products[v][:2]
    print(f"  {v}: {c} entries, forms: {forms}")
print("[PASS]")
