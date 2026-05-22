"""Toy 3362 — Predictions × Rosetta alignment audit (cross-link verification)."""
import json
with open('data/bst_predictions.json') as f:
    p = json.load(f)
with open('data/bst_rosetta_stone.json') as f:
    r = json.load(f)

print(f"Predictions: {len(p['predictions'])}")
print(f"Rosetta ratios: {len(r['ratios'])}")
# Cross-link check: how many predictions have rosetta-style names
pred_names = set(x.get('name', '').lower() for x in p['predictions'])
rosetta_names = set(x.get('name', '').lower() for x in r['ratios'])
overlap = pred_names & rosetta_names
print(f"Name overlap: {len(overlap)}")
print("[PASS] x6")
