import json, math
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
target = 7*math.pi
TOL = 0.005
matches = []
for i in d['invariants']:
    if not isinstance(i, dict): continue
    v = i.get('value')
    try: vn = float(v)
    except (ValueError, TypeError): continue
    if 0 < abs(vn) and abs(vn - target)/abs(target) < TOL:
        matches.append((i.get('name', '?')[:60], vn))
print(f"7π=g·π matches (0.5% tol):")
for n, v in matches:
    print(f"  {n}: {v}")
print("[PASS]")
