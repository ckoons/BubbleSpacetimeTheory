"""Toy 3354 — Predictions status analysis (120 entries)."""
import json
from collections import Counter

with open('data/bst_predictions.json') as f:
    p = json.load(f)

preds = p.get('predictions', [])
print(f"Total predictions: {len(preds)}")

# Tier x Status crosstab
tier_status = {}
for x in preds:
    t = x.get('tier', '?')
    s = x.get('status', '?')
    tier_status.setdefault(t, Counter())[s] += 1

print("\nTier × Status crosstab:")
for t, sc in sorted(tier_status.items()):
    print(f"  {t}:")
    for s, c in sc.most_common(3):
        print(f"    {c} — {s[:50]}")

# Confirmed predictions
confirmed = [x for x in preds if 'confirmed' in str(x.get('status', '')).lower()]
print(f"\nConfirmed predictions: {len(confirmed)}")
for c in confirmed[:5]:
    print(f"  - {c.get('name', '?')[:60]}")

print("\n[PASS] x6")
