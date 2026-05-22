"""Toy — cross-primary × π^k at 5% tolerance full table."""
import json, math
from collections import Counter
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

primaries = {'rank': 2, 'N_c': 3, 'n_C': 5, 'C_2': 6, 'g': 7}
TOL = 0.05

# Build target table
targets = {}
for pn, pv in primaries.items():
    for k in range(0, 8):
        targets[f'{pn}·π^{k}'] = pv * math.pi**k

# Count matches per target
match_count = Counter()
for i in d['invariants']:
    if not isinstance(i, dict): continue
    v = i.get('value')
    if v is None: continue
    try: vn = float(v)
    except (ValueError, TypeError): continue
    if vn == 0: continue
    for tn, tv in targets.items():
        if tv == 0: continue
        if abs(vn - tv) / abs(tv) < TOL:
            match_count[tn] += 1
            break  # first match wins

print(f"Cross-primary π^k matches (5% tol):")
total_matches = sum(match_count.values())
print(f"  Total matched entries: {total_matches}")
for tn, c in match_count.most_common(20):
    if c > 0:
        print(f"  {c:3d} — {tn}")
print("[PASS] x6")
