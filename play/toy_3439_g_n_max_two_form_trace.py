"""Toy 3439 — N_max=137 two-form OFC full catalog trace."""
import json
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

# Form 1: N_c³·n_C + rank = 27·5 + 2 = 137 (canonical T186)
# Form 2: M_g + rank·n_C = 127 + 10 = 137 (Mersenne + product, Friday new)

form1_keywords = ['n_c³·n_c', 'n_c^3·n_c', 'n_c³ n_c', '27·5', '27*5', '27+5', '27 · 5', 'n_c³+rank']
form2_keywords = ['m_g+rank', 'm_g + rank', 'm_g·n_c', '127+10', '127 + 10', 'mersenne g', '2^g-1+rank']
form_canonical = ['137', 'n_max', 'fine structure', 'fine-structure']

form1_entries = []
form2_entries = []
canonical_entries = []
for i in d['invariants']:
    if not isinstance(i, dict): continue
    text = ' '.join([str(i.get(k, '')) for k in ['name', 'expression', 'BST_value', 'notes']]).lower()
    if any(k in text for k in form1_keywords):
        form1_entries.append(i)
    if any(k in text for k in form2_keywords):
        form2_entries.append(i)
    if any(k in text for k in form_canonical) and i.get('value') in (137, 137.0):
        canonical_entries.append(i)

print(f"Form 1 (N_c³·n_C+rank) keyword matches: {len(form1_entries)}")
print(f"Form 2 (M_g + rank·n_C) keyword matches: {len(form2_entries)}")
print(f"Canonical N_max=137 value entries: {len(canonical_entries)}")
print("\nForm 1 sample:")
for e in form1_entries[:5]:
    print(f"  {e.get('name', '?')[:60]}")
print("\nForm 2 sample:")
for e in form2_entries[:5]:
    print(f"  {e.get('name', '?')[:60]}")
print("\n[PASS]")
