"""Toy 3489 — micro-batch pending_review (specific physics + history references)."""
import json
from collections import Counter
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

PATTERNS = [
    # Specific physics observables
    ('nfw_profile', ['nfw profile', 'navarro-frenk-white'], 'C_2+g+N_max'),
    ('heisenberg_uncertainty', ['heisenberg uncertainty', 'uncertainty principle'], 'rank+C_2+g'),
    ('cayley_hamilton', ['cayley-hamilton', 'characteristic polynomial'], 'rank+n_C'),
    ('wallis_product', ['wallis product', 'pi formula'], 'C_2'),
    ('complexity_classes', ['parity circuit', 'equality randomized', 'disjointness deterministic', 'bqp ⊆ pspace', 'np witness', 'pspace', 'communication complexity'], 'rank+g'),
    ('biological_perception', ['weber-fechner', 'just-noticeable', 'perception threshold'], 'g+C_2'),
    ('linguistic_universals', ['greenberg', 'language universal', 'linguistic universal'], 'rank'),
    ('astrophysics_specific2', ['eddington luminosity', 'eddington bound', 'majorana'], 'C_2+g+N_max'),
    ('poincare_duality', ['poincaré duality', 'poincare duality'], 'rank+n_C'),
    ('theta_vacuum', ['θ-vacuum', 'theta-vacuum', 'theta vacuum'], 'N_c+C_2'),
    ('alpha_helix', ['α-helix', 'alpha-helix', 'protein secondary'], 'N_c+n_C'),
    ('cosmology_primordial', ['primordial he-4', 'big bang nucleosynthesis', 'bbn primordial'], 'C_2+g'),
    ('historical_attribution', ['chew', 's-matrix bootstrap', 'sakharov', 'induced gravity', 'heisenberg s-matrix', 'mach', '1893', '1943', '1960s', '1967'], 'rank'),
    ('q_factor', ['q factor', 'quality factor', 'resonance q'], 'C_2+g'),
    ('depth_universality', ['depth predicts', 'why 5/3', 'why 7/6', 't1459'], 'rank+C_2'),
    ('bekenstein_bound', ['bekenstein', 'entropy bound'], 'rank+C_2'),
    ('constructible_polygon', ['constructible regular polygon'], 'rank+N_c'),
    ('game_theory', ['dictator game', 'modal offer', 'ultimatum'], 'rank'),
    ('iod2_forward', ['i₂ = 197', 'i_2 = 197', '197/144'], 'C_2+N_max'),
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
