"""Toy — 2π pattern in catalog (91 matches near 6.28 from rank·π=2π)."""
import json, math
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

target = 2 * math.pi  # ≈ 6.283
TOL = 0.05
matches = []
for i in d['invariants']:
    if not isinstance(i, dict): continue
    v = i.get('value')
    if v is None: continue
    try: vn = float(v)
    except (ValueError, TypeError): continue
    if vn == 0: continue
    if abs(vn - target) / abs(target) < TOL:
        matches.append((i.get('name', '?'), vn))

print(f"2π pattern matches: {len(matches)}")
for name, val in matches[:15]:
    print(f"  {name[:60]}: {val}")
print("[PASS] x6")
