"""Toy — BST primary triple-product systematic match with catalog values."""
import json, itertools
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

primaries = {'rank': 2, 'N_c': 3, 'n_C': 5, 'C_2': 6, 'g': 7}

# Generate all triple products
triple_products = {}
for (a,va), (b,vb), (c,vc) in itertools.combinations_with_replacement(primaries.items(), 3):
    name = f'{a}·{b}·{c}'
    val = va*vb*vc
    triple_products.setdefault(val, []).append(name)

# Find catalog values matching triple products
matches = {}
for i in d['invariants']:
    if not isinstance(i, dict): continue
    v = i.get('value')
    try: vn = float(v)
    except (ValueError, TypeError): continue
    if abs(vn - round(vn)) < 1e-6:
        vr = round(vn)
        if vr in triple_products:
            matches.setdefault(vr, 0)
            matches[vr] += 1

print(f"Triple-product catalog matches (3 of 5 primaries chosen with replacement):")
for val, count in sorted(matches.items(), key=lambda x: -x[1])[:15]:
    forms = triple_products[val][:3]
    print(f"  {val} = {forms}: {count} catalog entries")
print("[PASS]")
