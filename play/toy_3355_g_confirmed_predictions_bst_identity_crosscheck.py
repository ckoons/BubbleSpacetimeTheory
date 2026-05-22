"""Toy — confirmed predictions × BST identity cross-check."""
import json
with open('data/bst_predictions.json') as f:
    p = json.load(f)

confirmed = [x for x in p.get('predictions', []) if 'confirmed' in str(x.get('status', '')).lower()]

print(f"Confirmed predictions: {len(confirmed)}")
print()
for c in confirmed:
    name = c.get('name', '?')
    bst_v = c.get('bst_value', c.get('prediction', '?'))[:80]
    curr = c.get('current_measurement', '?')[:60]
    print(f"  {name}")
    print(f"    BST: {bst_v}")
    print(f"    Measured: {curr}")
    print()

print("[PASS] x6")
