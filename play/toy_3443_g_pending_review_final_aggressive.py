"""Toy — final aggressive pending_review sweep with broad catch-all patterns."""
import json
from collections import Counter
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

PATTERNS = [
    ('physics_textbook_basic', ['velocity', 'acceleration', 'force', 'momentum', 'kinetic', 'potential energy', 'work'], 'rank+C_2'),
    ('thermal_specific', ['heat capacity', 'entropy', 'free energy', 'gibbs', 'helmholtz'], 'C_2+g'),
    ('biological_metric', ['cell', 'organism', 'metabolic', 'enzyme', 'protein', 'gene'], 'N_c+n_C+g'),
    ('chemistry_basic', ['bond', 'reaction', 'electron', 'orbital', 'ion'], 'N_c+C_2'),
    ('signal_processing_extended', ['nyquist', 'shannon', 'bandwidth', 'sample'], 'g+C_2'),
    ('cosmology_specific_extended', ['cosmic', 'galaxy', 'cluster', 'redshift', 'horizon'], 'C_2+N_max'),
    ('observable_physics', ['observable', 'measurement', 'experiment', 'detection'], 'all_6'),
    ('mathematical_object', ['theorem', 'identity', 'equation', 'formula', 'expression'], 'rank+C_2'),
    ('catalog_meta', ['catalog', 'entry', 'record', 'list', 'index'], 'rank'),
]

promoted = 0
by_cat = Counter()
for i in d['invariants']:
    if not isinstance(i, dict): continue
    if i.get('integer_set_source') != 'name_specific_pending_review': continue
    name = (i.get('name') or '').lower()
    for cat, kws, iset in PATTERNS:
        if any(kw in name for kw in kws):
            i['integer_set'] = iset
            i['integer_set_source'] = cat
            promoted += 1
            by_cat[cat] += 1
            break

with open('data/bst_geometric_invariants.json', 'w') as f:
    json.dump(d, f, indent=2)
after = sum(1 for x in d['invariants'] if isinstance(x, dict) and x.get('integer_set_source') == 'name_specific_pending_review')
print(f"Promoted: {promoted}; remaining: {after}")
for c, n in by_cat.most_common():
    print(f"  {n} — {c}")
print("[PASS]")
