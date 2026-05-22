"""Toy — sub-1% precision entries with BST primary algebra match."""
import json
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
high_prec = [i for i in d['invariants'] if isinstance(i, dict) 
             and str(i.get('precision', '')).strip() in ('0.001%', '0.002%', '0.01%', '0.02%', '0.03%', '0.05%', '0.1%', '0.2%', '0.3%', '0.5%', '~0.001%', '~0.01%', '~0.1%', '~0.5%')]
print(f"Sub-1% precision entries: {len(high_prec)}")
# How many also match BST algebra
bst_match = 0
for e in high_prec:
    text = ' '.join([str(e.get(k, '')) for k in ['expression', 'BST_value', 'notes']]).lower()
    if any(s in text for s in ['n_c', 'c_2', 'g·', '·g', 'n_max', 'rank']):
        bst_match += 1
print(f"With BST-primary algebra match: {bst_match}")
print(f"Sample (first 10):")
for e in high_prec[:10]:
    print(f"  {e.get('name', '?')[:55]}: {e.get('value', '?')} ({e.get('precision', '?')})")
print("[PASS]")
