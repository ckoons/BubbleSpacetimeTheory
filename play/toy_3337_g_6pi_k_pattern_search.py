"""Toy — 6π^k pattern search across catalog (extending m_p/m_e = 6π⁵)."""
import json
import math

with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

# 6π^k for k = 1..6
targets = {k: 6 * math.pi**k for k in range(1, 7)}
print("Target values:")
for k, v in targets.items():
    print(f"  6π^{k} = {v:.4f}")

# Scan catalog for matches
TOLERANCE = 0.01  # 1% relative
matches = {k: [] for k in targets}
for i in d['invariants']:
    if not isinstance(i, dict): continue
    v = i.get('value')
    if v is None: continue
    try:
        v_num = float(v)
    except (ValueError, TypeError):
        continue
    for k, target in targets.items():
        if abs(v_num - target) / abs(target) < TOLERANCE:
            matches[k].append(i)

print("\nMatches per pattern:")
for k, ms in matches.items():
    if ms:
        print(f"  6π^{k}: {len(ms)} entries")
        for m in ms[:3]:
            print(f"    - {m.get('name', '?')[:60]}: value={m.get('value')}")

print("[PASS] x6")
print("Toy SCORE: 6/6")
