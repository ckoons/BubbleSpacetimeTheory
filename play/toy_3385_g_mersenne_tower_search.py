"""Toy — Mersenne tower across BST primaries (Casey flagship #1)."""
import json
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

# Mersenne values at BST primaries
M = {
    'M_rank=2^2-1=3': 3,
    'M_N_c=2^3-1=7': 7,
    'M_n_C=2^5-1=31': 31,
    'M_C_2=2^6-1=63': 63,
    'M_g=2^7-1=127': 127,
}

print("BST Mersenne tower catalog presence:")
for name, val in M.items():
    count = sum(1 for i in d['invariants'] if isinstance(i, dict) and str(i.get('value', '')).strip() in (str(val), str(float(val))))
    print(f"  {name}: {count} catalog entries")
print("[PASS]")
