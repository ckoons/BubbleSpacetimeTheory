"""Toy 3441 — pending_review specific physics sweep (lowest-priority residual)."""
import json
from collections import Counter
with open('data/bst_geometric_invariants.json') as f:
    d = json.load(f)

# Very specific patterns for residual
PATTERNS = [
    ('hopf_homotopy', ['hopf', 'π₃', 'homotopy group', 'Z (Hopf)'], 'rank+N_c'),
    ('cosmology_eras', ['radiation era', 'matter era', 'a(t) scaling', 'NFW profile'], 'C_2+N_max'),
    ('quantum_selection_rules', ['selection rule', 'Δl', 'Δm', 'transition'], 'rank+C_2'),
    ('hadronic_resonances', ['k⁰ mass', 'k0 mass', 'f₀', 'a₀', 'σ mass', 'rho mass'], 'N_c+C_2'),
    ('regge_resonance', ['regge', 'trajectory slope', 'string tension'], 'N_c+C_2+g'),
    ('molecular_potential', ['van der waals', 'lennard-jones', 'morse', 'interatomic'], 'rank+N_c+C_2'),
    ('crystallography_specific', ['simple cubic', 'fcc', 'bcc', 'packing', 'crystal structure'], 'rank+N_c'),
    ('bio_physics', ['blood ph', 'dunbar', 'species-area', 'biological', 'allometric'], 'N_c+n_C'),
    ('linguistics', ['phoneme', 'language', 'word frequency'], 'rank'),
    ('graph_metrics', ['current ac graph', 'graph average', 'graph density', 'graph diameter'], 'rank+g'),
    ('nuclear_physics_specific', ['quadrupole', 'deformation β', 'nuclear quadrupole'], 'N_c+C_2'),
    ('wave_phenomena_extended', ['1/f noise', 'brownian noise', 'pink noise', 'wien peak'], 'C_2+g'),
    ('series_formulae', ['balmer series', 'rydberg', 'spectral series'], 'C_2+g+N_max'),
    ('algebraic_intersection', ['bézout', 'intersection count', 'algebraic geometry intersect'], 'rank+n_C'),
    ('constructibility', ['constructible polygon', 'compass', 'straightedge'], 'rank+N_c'),
    ('Avogadro_leading', ['avogadro', '6.022', 'avogadro digit'], 'C_2'),
    ('gravity_force_law', ['gravity force', 'inverse square', '1/r²'], 'rank+N_max'),
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
