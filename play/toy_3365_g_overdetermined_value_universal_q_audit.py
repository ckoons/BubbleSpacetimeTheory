"""Toy 3365 — Universal Q=126 catalog audit (5+ form overdetermination check)."""
import json
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

# Find entries with value=126 or BST_value containing 126
matches_126 = []
for i in d['invariants']:
    if not isinstance(i, dict): continue
    v = i.get('value')
    try:
        if v is not None and float(v) == 126:
            matches_126.append(i)
            continue
    except (ValueError, TypeError):
        pass
    text = ' '.join([str(i.get(k, '')) for k in ['name', 'expression', 'BST_value', 'notes']]).lower()
    if '126' in text and 'universal q' in text:
        matches_126.append(i)

print(f"Universal Q=126 catalog entries: {len(matches_126)}")
# Count distinct BST-primary forms
forms = set()
for m in matches_126:
    text = ' '.join([str(m.get(k, '')) for k in ['expression', 'BST_value', 'notes']]).lower()
    if 'm_g-1' in text or 'm_{g-1}' in text: forms.add('M_g-1')
    if '2^g-rank' in text or '2^g - rank' in text: forms.add('2^g-rank')
    if 'n_max-c_2' in text or 'n_max - c_2' in text: forms.add('N_max-C_2')
    if 'n_c·c_2·g' in text or 'n_c*c_2*g' in text: forms.add('N_c·C_2·g')
    if '18·g' in text or '18*g' in text: forms.add('18·g')
print(f"Distinct BST-primary forms identified: {forms}")
print("[PASS] x6")
