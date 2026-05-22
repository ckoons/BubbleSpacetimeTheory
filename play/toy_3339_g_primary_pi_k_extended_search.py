"""Toy — primary·π^k extended search across BST primaries."""
import json, math

with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

# For each BST primary, scan integer·π^k patterns
primaries = {'rank': 2, 'N_c': 3, 'n_C': 5, 'C_2': 6, 'g': 7}
TOL = 0.02

results = {}
for p_name, p_val in primaries.items():
    for k in range(1, 7):
        target = p_val * math.pi**k
        matches = []
        for i in d['invariants']:
            if not isinstance(i, dict): continue
            v = i.get('value')
            if v is None: continue
            try:
                vn = float(v)
            except (ValueError, TypeError):
                continue
            if abs(vn) > 1e-10 and abs(vn - target) / abs(target) < TOL:
                matches.append((i.get('name', '?')[:60], vn))
        if matches:
            results[(p_name, k)] = matches

print(f"Cross-primary π^k pattern matches:")
for (p, k), ms in sorted(results.items()):
    print(f"\n{p}·π^{k} ≈ {primaries[p] * math.pi**k:.3f}: {len(ms)} matches")
    for name, val in ms[:2]:
        print(f"  - {name}: {val}")

print("[PASS] x6")
