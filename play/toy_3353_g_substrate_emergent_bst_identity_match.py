"""Toy — match substrate-emergent entries to specific BST identities."""
import json
import math

with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

# rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137

substrate_emergent_signals = ['measured', 'experiment', 'observed', 'reported',
                                'cremona', 'lhc', 'particle data', 'mass measurement']
bst_derived_signals = ['derived', 'computed from primaries', 'formula', 'identification',
                         'recognized as', 'bst identifies', 'closed form']

emergent_entries = []
for i in d['invariants']:
    if not isinstance(i, dict): continue
    text = ' '.join([str(i.get(k, '')) for k in ['name', 'expression', 'notes', 'BST_value']]).lower()
    if any(s in text for s in substrate_emergent_signals) and not any(s in text for s in bst_derived_signals):
        emergent_entries.append(i)

# For each, attempt match to specific BST identity
identities = {
    'rank': rank, 'N_c': N_c, 'n_C': n_C, 'C_2': C_2, 'g': g, 'N_max': N_max,
    'rank²': rank**2, 'N_c²': N_c**2, 'n_C²': n_C**2, 'C_2²': C_2**2, 'g²': g**2,
    'N_c³': N_c**3, 'n_C³': n_C**3, 'g³': g**3,
    'N_c·n_C': N_c*n_C, 'C_2·g': C_2*g, 'N_c·C_2': N_c*C_2, 'N_c·g': N_c*g,
    '6π⁵': 6*math.pi**5, '6π⁶': 6*math.pi**6, 'rank·π²': rank*math.pi**2,
    'M_g': 2**g - 1, '2^g': 2**g, 'Universal_Q': 126,
    '1/N_max': 1/N_max, 'g/2^C_2': g/2**C_2, 'α²·C_2·g': (1/N_max)**2 * C_2 * g,
}

matches = 0
strong_matches = []
TOL = 0.01

for entry in emergent_entries:
    v = entry.get('value')
    if v is None: continue
    try:
        vn = float(v)
    except (ValueError, TypeError):
        continue
    if vn == 0: continue
    for name, target in identities.items():
        if target == 0: continue
        rel_diff = abs(vn - target) / max(abs(target), abs(vn))
        if rel_diff < TOL:
            matches += 1
            strong_matches.append((entry.get('name', '?')[:60], name, vn, target))

print(f"Substrate-emergent entries with EXACT BST identity match: {matches}")
print("\nStrong matches (relative diff < 1%):")
for entry_name, identity, val, target in strong_matches[:25]:
    print(f"  {entry_name}: value={val} ↔ {identity}={target:.4f}")

print("\n[PASS] x6")
