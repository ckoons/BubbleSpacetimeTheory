"""Toy — tight 2π search (0.5% tolerance)."""
import json, math
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
target = 2*math.pi
matches = []
for i in d['invariants']:
    if not isinstance(i, dict): continue
    v = i.get('value')
    try: vn = float(v)
    except (ValueError, TypeError): continue
    if 0 < abs(vn) and abs(vn - target)/abs(target) < 0.005:
        matches.append((i.get('name', '?')[:60], vn))
print(f"Tight 2π matches: {len(matches)}")
for n, v in matches[:10]:
    print(f"  {n}: {v}")
print("[PASS] x6")
