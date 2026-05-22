import json, math
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
# 2nπ for n=1..10
print("(2n)π scan at 0.5% tolerance:")
for n in range(1, 11):
    target = 2 * n * math.pi
    count = 0
    sample = None
    for i in d['invariants']:
        if not isinstance(i, dict): continue
        v = i.get('value')
        try: vn = float(v)
        except (ValueError, TypeError): continue
        if 0 < abs(vn) and abs(vn - target)/abs(target) < 0.005:
            count += 1
            if not sample: sample = i.get('name', '?')[:50]
    if count > 0:
        print(f"  {2*n}π = {target:.3f}: {count} matches (e.g., {sample})")
print("[PASS]")
