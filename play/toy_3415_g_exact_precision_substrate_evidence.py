"""Toy — Exact-precision catalog entries (substrate evidence at highest precision)."""
import json
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)
exact = [i for i in d['invariants'] if isinstance(i, dict) and str(i.get('precision', '')).lower() == 'exact']
print(f"Exact-precision entries: {len(exact)}")
# Sample 10
print("\nSample exact-precision entries (first 10):")
for e in exact[:10]:
    print(f"  {e.get('name', '?')[:60]}: {e.get('value', '?')}")
# How many have BST-primary algebraic expressions?
bst_algebraic = 0
for e in exact:
    text = ' '.join([str(e.get(k, '')) for k in ['expression', 'BST_value', 'notes']]).lower()
    if any(s in text for s in ['n_c', 'c_2', 'g·', '·g', 'n_max', 'rank', '2^g', 'm_g']):
        bst_algebraic += 1
print(f"\nOf {len(exact)} exact entries, {bst_algebraic} have explicit BST-primary algebra ({100*bst_algebraic/max(len(exact),1):.0f}%)")
print("[PASS]")
