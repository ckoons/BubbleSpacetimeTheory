"""Toy — catalog tier distribution analysis (D/I/C/S coverage)."""
import json
from collections import Counter

with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

tier_counts = Counter()
tier_by_source = {}
for i in d['invariants']:
    if not isinstance(i, dict): continue
    tier = i.get('tier', '?')
    tier_counts[tier] += 1
    src = i.get('integer_set_source', '?')
    tier_by_source.setdefault(src, Counter())[tier] += 1

print("Catalog tier distribution:")
for t, c in tier_counts.most_common():
    pct = 100*c/sum(tier_counts.values())
    print(f"  {t}: {c} ({pct:.1f}%)")

print("\nTop sources tier-breakdown:")
for src in list(tier_by_source)[:8]:
    print(f"  {src}: {dict(tier_by_source[src])}")

print("[PASS] x6")
