"""Toy — untested BST predictions index (42 entries, paper-grade)."""
import json
with open('data/bst_predictions.json') as f:
    p = json.load(f)
untested = [x for x in p.get('predictions', []) if x.get('status') == 'untested']
print(f"Untested predictions: {len(untested)}")
for u in untested[:15]:
    print(f"  {u.get('name', '?')[:60]}: {str(u.get('prediction', '?'))[:50]}")
print("[PASS] x6")
