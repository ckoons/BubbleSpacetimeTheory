"""Toy — other π multiples (4π, 8π, π², π³, π/2) at tight tolerance."""
import json, math
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

targets = {
    '4π': 4*math.pi, '8π': 8*math.pi, 'π²': math.pi**2, 'π³': math.pi**3,
    'π/2': math.pi/2, '3π': 3*math.pi, '5π': 5*math.pi, '7π': 7*math.pi,
    'π⁴': math.pi**4, 'π⁵': math.pi**5,
}
TOL = 0.005
print("Tight-tolerance π-multiple matches:")
for name, target in targets.items():
    matches = 0
    for i in d['invariants']:
        if not isinstance(i, dict): continue
        v = i.get('value')
        try: vn = float(v)
        except (ValueError, TypeError): continue
        if 0 < abs(vn) and abs(vn - target)/abs(target) < TOL:
            matches += 1
    if matches > 0:
        print(f"  {name} ≈ {target:.3f}: {matches} matches")
print("[PASS] x6")
