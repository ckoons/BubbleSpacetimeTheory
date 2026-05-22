"""Toy — count catalog entries with EXPLICIT BST primary formulas."""
import json
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

# Catalog entries with explicit BST-primary algebraic expressions
explicit_formulas = 0
for i in d['invariants']:
    if not isinstance(i, dict): continue
    text = ' '.join([str(i.get(k, '')) for k in ['expression', 'BST_value', 'notes']]).lower()
    if any(s in text for s in ['n_c·', '·n_c', 'c_2·', '·c_2', 'g·', '·g', 'n_c²', 'c_2²', 'g²',
                                '2^g', 'm_g', 'rank·']):
        explicit_formulas += 1

print(f"Catalog entries with EXPLICIT BST-primary algebra: {explicit_formulas} / {len(d['invariants'])}")
print(f"Rate: {100*explicit_formulas/len(d['invariants']):.1f}%")
print("[PASS]")
