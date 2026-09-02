#!/usr/bin/env python3
"""
Toy 5636b — addendum to 5636 (same round). Two checks the D1 discriminator owes before it is posted.
 (i) STRUCTURE: is the period lattice P exactly 2·L, where L = Z-span of the odd-vertex height
     differences {h(w~) − h(v0~)}? (The pair loops α·(τα)^-1 have period 2(h(w~) − h(v0~)); if they
     generate H_1(T~) then P = 2L exactly.) Tested on all 1,550 colourings of the 9 hosts and on the
     k-sweep n = 6..9. If P = 2L: drop ⟺ L ≠ Z^2, and the two-colour rule is the mod-2 shadow of L.
 (ii) FALSE-NEIGHBOUR off the frame: the k=4 sweep had index-3 lattices (2,6). Their odd vertices — how
     many colours? If 3 or more, "two colours ⟺ drop" is a FRAME fact (only even-index drops occur
     there), not a theorem; the general discriminator is L ≠ Z^2.
TESTS: 1. P = 2L on the 1,550.  2. P = 2L on the k-sweep.  3. report colours-on-odd for every sweep
lattice type (no pass/fail; data).
Elie, 2026-09-02. 2 scored tests + 1 table.
"""
import importlib.util, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
def load(nm, fn):
    sp = importlib.util.spec_from_file_location(nm, os.path.join(HERE, fn)); m = importlib.util.module_from_spec(sp)
    a = sys.argv; sys.argv = ['x', '12']; sp.loader.exec_module(m); sys.argv = a; return m
T = load('t5626', 'toy_5626_SEP2_E1_branched_cover_clause_height_lift_period_lattice_and_dislocation_centers_vs_n.py')
HOSTS = [(20, 16), (20, 18), (21, 90), (22, 167), (23, 600), (24, 2076), (24, 2547), (24, 3244), (24, 5800)]
def twoL(m):
    h0 = m['hodd'][0]
    return T.lattice_hnf([(2 * (x - h0[0]), 2 * (y - h0[1])) for (x, y) in m['hodd'][1:]])
def same(b1, b2): return T.lattice_hnf(b1) == T.lattice_hnf(b2)
if __name__ == '__main__':
    print('Toy 5636b — P = 2L ? and the off-frame index-3 false neighbour')
    ok1 = True; n1 = 0; cache = {}
    for n, gi in HOSTS:
        if n not in cache: cache[n] = T.plantri_rot(n)
        rot = cache[n][gi]; faces = T.faces_of(rot)
        for f in T.colorings_mod_s4(rot, 10 ** 7):
            m = T.cover_measure(rot, faces, f); n1 += 1
            if not same(m['basis'], twoL(m)): ok1 = False
    print(f'  Test 1 (P = 2·span of odd-vertex height differences, all {n1} colourings of the 9 hosts): {"PASS" if ok1 else "FAIL"}')
    ok2 = True; n2 = 0; tab = Counter()
    for n in range(6, 10):
        for rot in T.plantri_rot(n, flags=()):
            faces = T.faces_of(rot)
            for f in T.colorings_mod_s4(rot, 10 ** 6):
                m = T.cover_measure(rot, faces, f); n2 += 1
                if m['k'] >= 2 and not same(m['basis'], twoL(m)): ok2 = False
                if m['k'] == 4:
                    tab[(m['r'], m['ed'], len(set(f[v] for v in m['odd'])))] += 1
    print(f'  Test 2 (P = 2L on the k-sweep n=6..9, {n2} colourings, k ≥ 2): {"PASS" if ok2 else "FAIL"}')
    print('  k=4 sweep: (rank, elementary divisors, colours on the 4 odd vertices) -> count')
    for key, c in sorted(tab.items(), key=str): print(f'    {key}: {c}')
    print(f'\nSCORE: {int(ok1)+int(ok2)}/2')
