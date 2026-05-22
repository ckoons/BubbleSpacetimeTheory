"""Toy — sub-1% precision entries domain distribution."""
import json
from collections import Counter
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
high_prec = [i for i in d['invariants'] if isinstance(i, dict) 
             and str(i.get('precision', '')).strip() in ('0.001%', '0.002%', '0.01%', '0.02%', '0.03%', '0.05%', '0.1%', '0.2%', '0.3%', '0.5%', '~0.001%', '~0.01%', '~0.1%')]
doms = Counter(i.get('domain', '(none)') for i in high_prec)
print("Sub-1% precision by domain:")
for d_, c in doms.most_common(10):
    print(f"  {c:3d} — {d_}")
print("[PASS]")
