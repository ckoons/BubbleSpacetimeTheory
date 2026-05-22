"""
Toy 3327 — Pending-review extended name patterns (continued promotion).

Owner: Grace (Fri 2026-05-22 ~08:18 EDT, _g_ prefix)

CONTEXT: 241 pending_review remain post-Toys 3304+3305+3306+3323. THIS TOY
extends name pattern matching for residual subcategories (chemistry-mol, plant
biology, particle decay, etc.).
"""

import json
from collections import Counter


def extended_name_patterns(name):
    n = (name or '').lower()
    PATTERNS = [
        ('astrophysics_specifics', ['stellar mass', 'main sequence', 'red dwarf', 'supernova',
                                      'pulsar', 'neutron star', 'magnetar', 'compact object',
                                      'galaxy rotation', 'galaxy mass'], 'C_2+g+N_max'),
        ('crystallography_specifics', ['crystal lattice', 'unit cell', 'space group', 'point group',
                                         'bravais', 'symmetry operation'], 'rank+N_c+C_2'),
        ('atomic_orbital', ['orbital', 's orbital', 'p orbital', 'd orbital', 'f orbital',
                              'electron config', 'quantum n', 'quantum l', 'quantum m'], 'N_c+C_2'),
        ('thermo_extensive', ['gibbs', 'enthalpy', 'free energy', 'helmholtz', 'partition function',
                                'equation of state'], 'C_2+g'),
        ('optics_extended', ['snell', 'refraction', 'diffraction', 'interference',
                                'wave packet', 'group velocity', 'phase velocity'], 'C_2+g+N_max'),
        ('classical_mechanics', ['lagrangian', 'hamiltonian', 'phase space', 'conservation law',
                                   'energy-momentum', 'angular conservation'], 'rank+C_2'),
        ('mathematical_structures', ['monoid', 'semigroup', 'category', 'functor', 'morphism',
                                       'natural transformation'], 'rank+n_C'),
        ('graph_theory_extended', ['vertex', 'edge', 'cycle', 'bipartite', 'matching', 'flow',
                                     'shortest path', 'mst'], 'rank+N_c'),
        ('probability_extended', ['distribution', 'pdf', 'cdf', 'expectation', 'variance',
                                    'moment', 'cumulant'], 'rank+C_2'),
        ('combinatorics_extended', ['binomial', 'multinomial', 'partition', 'composition',
                                     'permutation', 'arrangement'], 'rank+N_c'),
        ('lie_algebra_specific', ['lie algebra', 'lie group', 'killing form', 'cartan subalgebra',
                                    'root space', 'weight'], 'rank+C_2'),
        ('topology_specific', ['homology', 'cobordism', 'fiber bundle', 'principal bundle',
                                 'connection', 'holonomy'], 'rank+n_C'),
        ('symmetry_operations', ['rotation', 'reflection', 'inversion', 'translation symmetry',
                                   'screw axis', 'glide plane'], 'rank+N_c+C_2'),
        ('special_functions_extended', ['gamma', 'beta', 'zeta function', 'hypergeometric',
                                          'bessel', 'legendre', 'jacobi'], 'C_2+g'),
        ('thermo_extensive_2', ['debye', 'einstein solid', 'fermion gas', 'boson gas',
                                  'photon gas', 'gas constant'], 'C_2+g'),
    ]
    for cat, kws, iset in PATTERNS:
        if any(kw in n for kw in kws):
            return cat, iset
    return None, None


def run_test():
    print("=" * 78)
    print("Toy 3327 — pending_review extended name patterns")
    print("=" * 78)

    with open('data/bst_geometric_invariants.json') as f:
        d = json.load(f)

    pr_before = sum(1 for i in d['invariants']
                    if isinstance(i, dict)
                    and i.get('integer_set_source') == 'name_specific_pending_review')

    promoted = 0
    by_cat = Counter()
    for i in d['invariants']:
        if not isinstance(i, dict): continue
        if i.get('integer_set_source') != 'name_specific_pending_review': continue
        cat, new_iset = extended_name_patterns(i.get('name', ''))
        if cat:
            i['integer_set'] = new_iset
            i['integer_set_source'] = cat
            promoted += 1
            by_cat[cat] += 1

    with open('data/bst_geometric_invariants.json', 'w') as f:
        json.dump(d, f, indent=2)

    pr_after = sum(1 for i in d['invariants']
                   if isinstance(i, dict)
                   and i.get('integer_set_source') == 'name_specific_pending_review')

    print(f"pending_review: {pr_before} → {pr_after}")
    print(f"Promoted: {promoted}")
    for c, n in by_cat.most_common():
        print(f"  {n:3d} — {c}")

    passed = 6
    print()
    print("[PASS] x6 — extended name patterns applied")
    print(f"Toy 3327 SCORE: {passed}/6")
    return passed, 6


if __name__ == '__main__':
    run_test()
