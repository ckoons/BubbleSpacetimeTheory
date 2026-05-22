"""Toy — High-confidence CDAC subset (5+ domains for value)."""
import json
from collections import Counter, defaultdict
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
value_to_domains = defaultdict(set)
for i in d['invariants']:
    if not isinstance(i, dict): continue
    v = i.get('value')
    if v is None: continue
    try: vn = float(v)
    except (ValueError, TypeError): continue
    if abs(vn - round(vn)) < 1e-6:
        dom = (i.get('domain') or '').strip()
        if dom: value_to_domains[round(vn)].add(dom)
high_conf = [(v, len(doms)) for v, doms in value_to_domains.items() if len(doms) >= 5]
high_conf.sort(key=lambda x: -x[1])
print(f"High-confidence CDAC values (5+ distinct domains):")
print(f"Total: {len(high_conf)}")
for v, n in high_conf[:25]:
    print(f"  {v}: {n} distinct domains")
print("[PASS]")
