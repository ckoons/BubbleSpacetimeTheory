"""Toy — pending_review final sweep with name+expression unified pattern matching."""
import json
from collections import Counter

with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

# Final sweep: combine ALL signals (name + expression + notes + value text)
def comprehensive_match(entry):
    name = (entry.get('name') or '').lower()
    expr = (entry.get('expression') or '').lower()
    notes = (entry.get('notes') or '').lower()
    bst_val = (entry.get('BST_value') or '').lower() if entry.get('BST_value') else ''
    text = f"{name} {expr} {notes} {bst_val}"
    
    # Comprehensive pattern catalog
    PATTERNS = [
        # Each pattern: (category, keywords, integer_set)
        ('rosetta_named_ratio', ['rosetta', 'named ratio'], 'all_6'),
        ('lyra_theorem_anchor', ['t2443', 't2444', 't2445', 't2446', 't2447', 't2448', 't2449'], 'all_6'),
        ('observer_alpha_ci', ['α_ci', 'alpha_ci', 'observer coupling 19.1', 'f = 3/(5π)'], 'rank+C_2'),
        ('cardinality_invariant', ['cardinality', 'number of', 'count of'], 'rank'),
        ('aspect_ratio', ['ratio', 'aspect', 'proportion'], 'rank+C_2'),
        ('exponent_observation', ['exponent', 'power of', 'index'], 'rank+C_2'),
        ('density_observable', ['density', 'concentration', 'volume fraction'], 'rank+C_2'),
        ('rate_observable', ['rate', 'velocity', 'flux'], 'C_2+g'),
        ('threshold_observable', ['threshold', 'cutoff', 'critical value'], 'C_2'),
        ('coefficient_observable', ['coefficient', 'prefactor', 'normalization'], 'rank+C_2'),
        ('dimension_observable', ['dimension', 'dim ', 'dim('], 'rank+n_C'),
        ('group_order', ['group order', 'order of', 'cardinal'], 'N_c+C_2'),
        ('lattice_observable', ['lattice', 'crystal', 'unit'], 'rank+N_c'),
        ('spectral_invariant', ['eigenvalue', 'spectrum', 'frequency'], 'C_2+g'),
        ('topology_invariant', ['betti', 'cohomology dim', 'euler character'], 'rank+n_C'),
    ]
    
    for cat, kws, iset in PATTERNS:
        if any(kw in text for kw in kws):
            return cat, iset
    return None, None

promoted = 0
by_cat = Counter()
for i in d['invariants']:
    if not isinstance(i, dict): continue
    if i.get('integer_set_source') != 'name_specific_pending_review': continue
    cat, new_iset = comprehensive_match(i)
    if cat:
        i['integer_set'] = new_iset
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
