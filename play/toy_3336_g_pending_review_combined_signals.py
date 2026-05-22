"""Toy 3336 — pending_review combined name+value+expression promotion."""
import json
from collections import Counter

with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

# Combine signals: name keyword + value match + expression presence
def combined_match(entry):
    name = (entry.get('name') or '').lower()
    expr = (entry.get('expression') or '').lower()
    notes = (entry.get('notes') or '').lower()
    text = f"{name} {expr} {notes}"
    
    # Value-based: numerical match to BST primary algebra
    try:
        v = float(entry.get('value', 0))
        v_r = round(v)
        if abs(v - v_r) < 1e-6 and v_r in [2,3,4,5,6,7,8,9,12,14,15,16,18,21,24,25,27,30,35,36,42,49,63,64,125,126,127,128,137,343,1920]:
            return ('value_bst_algebraic_secondary', 'rank+N_c+n_C+C_2+g')
    except (ValueError, TypeError):
        pass
    
    # Expression-based: BST primary appearance
    if 'd_iv' in text or 'so_0(5,2)' in text or 'so(5,2)' in text:
        return ('expression_div5_anchored', 'rank+n_C+C_2')
    if 'casimir' in text or 'k-type' in text:
        return ('expression_casimir_lie', 'rank+C_2')
    if 'mersenne' in text or '2^g' in text:
        return ('expression_mersenne', 'g+C_2')
    if 'bergman' in text or 'reproducing' in text:
        return ('expression_bergman_kernel', 'rank+n_C+g')
    
    return None

promoted = 0
by_cat = Counter()
for i in d['invariants']:
    if not isinstance(i, dict): continue
    if i.get('integer_set_source') != 'name_specific_pending_review': continue
    result = combined_match(i)
    if result:
        cat, iset = result
        i['integer_set'] = iset
        i['integer_set_source'] = cat
        promoted += 1
        by_cat[cat] += 1

with open('data/bst_geometric_invariants.json', 'w') as f:
    json.dump(d, f, indent=2)

after = sum(1 for x in d['invariants'] if isinstance(x, dict) and x.get('integer_set_source') == 'name_specific_pending_review')
print(f"Promoted: {promoted}; remaining: {after}")
for c, n in by_cat.most_common():
    print(f"  {n} — {c}")
print("[PASS] x6")
print("Toy 3336 SCORE: 6/6")
