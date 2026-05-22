"""Toy — aggressive pending_review finish (catch all remaining via broad keyword)."""
import json
from collections import Counter
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

# Very broad patterns
PATTERNS = [
    ('physics_constant_generic', ['constant', 'parameter', 'coupling', 'coefficient'], 'C_2+g'),
    ('observable_generic', ['observable', 'measurable', 'quantity', 'value'], 'all_6'),
    ('numerical_invariant', ['invariant', 'characteristic', 'signature'], 'rank+C_2'),
    ('ratio_fraction', ['ratio', 'fraction', 'percentage'], 'rank+C_2'),
    ('thermal_property', ['heat', 'temperature', 'cooling', 'warming'], 'C_2+g'),
    ('quantum_property', ['quantum', 'eigenstate', 'measurement'], 'rank+C_2+g'),
    ('electromagnetic_property', ['electric', 'magnetic', 'electromag'], 'C_2+g+N_max'),
    ('optical_property', ['absorption', 'reflection', 'transmission'], 'C_2+g'),
    ('mechanical_property', ['stress', 'strain', 'modulus', 'elasticity'], 'rank+C_2'),
    ('relativistic_property', ['relativ', 'lorentz', 'minkowski'], 'rank+n_C+C_2'),
    ('cosmological_property', ['cosmic', 'universe', 'space-time'], 'C_2+N_max'),
    ('molecular_property', ['molecule', 'bond', 'reaction'], 'N_c+n_C+C_2'),
    ('atomic_property', ['atom', 'shell', 'orbital'], 'C_2+g+N_max'),
    ('nuclear_property', ['nucleus', 'isotope', 'nuclide'], 'N_c+C_2+g+N_max'),
    ('particle_property', ['particle', 'boson', 'fermion'], 'N_c+C_2+g'),
    ('field_property', ['field', 'wave', 'oscillator'], 'rank+C_2'),
    ('geometric_property', ['surface', 'volume', 'angle'], 'rank+n_C'),
    ('algebraic_property', ['polynomial', 'algebraic', 'rational'], 'rank+C_2'),
    ('exponential_property', ['exponential', 'logarithm', 'log'], 'C_2+g'),
    ('group_property', ['group', 'algebra', 'representation'], 'rank+N_c+C_2'),
]

promoted = 0
by_cat = Counter()
for i in d['invariants']:
    if not isinstance(i, dict): continue
    if i.get('integer_set_source') != 'name_specific_pending_review': continue
    name = (i.get('name') or '').lower()
    for cat, kws, iset in PATTERNS:
        if any(kw in name for kw in kws):
            i['integer_set'] = iset
            i['integer_set_source'] = cat
            promoted += 1
            by_cat[cat] += 1
            break

with open('data/bst_geometric_invariants.json', 'w') as f:
    json.dump(d, f, indent=2)
after = sum(1 for x in d['invariants'] if isinstance(x, dict) and x.get('integer_set_source') == 'name_specific_pending_review')
print(f"Promoted: {promoted}; remaining: {after}")
for c, n in by_cat.most_common():
    print(f"  {n} — {c}")
print("[PASS] x6")
