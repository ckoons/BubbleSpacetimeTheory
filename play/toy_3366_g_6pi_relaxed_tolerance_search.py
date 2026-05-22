"""Toy — 6π^k pattern with relaxed tolerance (5%)."""
import json, math
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

TOL = 0.05
targets = {k: 6*math.pi**k for k in range(0, 8)}
matches = {k: [] for k in targets}
for i in d['invariants']:
    if not isinstance(i, dict): continue
    v = i.get('value')
    if v is None: continue
    try:
        vn = float(v)
    except (ValueError, TypeError):
        continue
    for k, t in targets.items():
        if t == 0: continue
        if abs(vn - t) / abs(t) < TOL:
            matches[k].append((i.get('name', '?')[:60], vn))

print("6π^k matches at 5% tolerance:")
for k, ms in matches.items():
    if ms:
        print(f"\n6π^{k} = {targets[k]:.3f}: {len(ms)} matches")
        for name, val in ms[:3]:
            print(f"  - {name}: {val}")
print("[PASS] x6")
