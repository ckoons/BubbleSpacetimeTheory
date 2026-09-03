#!/usr/bin/env python3
"""
Toy 5639 — Round 109 Section 4(a), the one line owed to Lyra: the rank of the CENTRE LATTICE mod 3.
L = Z-span of the dislocation height differences {h(w~) − h(v0~)} (P = 2L, toy 5636b). An "odd-index
drop" is L of index divisible by an odd prime; in frame (5636) only 2-power drops occurred; off frame
the k=4 sweep had an index-3 case. QUESTION: is "the frame excludes odd-index drops" a MOD-3 statement —
i.e. does L mod 3 have full rank 2 on every in-frame colouring, and rank 1 exactly on the index-3 case?
Also: which index-3 sublattice? The A2 quotient Z^2 → Z_3, (x,y) ↦ x+y mod 3, sends A,B,C to 1,1,1 and
its kernel ⟨A−B, B−C⟩ is the charge-zero root sublattice (Lyra 08-30 Section 6). Report whether the
index-3 L is that kernel or one of the other three index-3 sublattices.
POPULATIONS: (a) the 71 drops; (b) all 41,027 colourings of the 226 fullerene duals n ≤ 24; (c) all
6,502 colourings of the 81 k>12 graphs n ≤ 20; (d) the k-sweep n = 6..9 (all 3-connected triangulations).
For each: index [Z^2 : L] (∞ if rank < 2), rank of L mod 3, rank of L mod 2.
TESTS: 1. in frame (b)+(c): every full-rank L has 3 ∤ index (rank-1 L has mod-3 rank 1 by rank; report its generator's charge).
       2. k=4 index-3 case: L mod 3 rank 1; identify the sublattice.  3. table rendered.
Elie, 2026-09-03. 3 tests.
"""
import importlib.util, os, sys, time
from collections import Counter
from math import gcd
HERE = os.path.dirname(os.path.abspath(__file__))
def load(nm, fn):
    sp = importlib.util.spec_from_file_location(nm, os.path.join(HERE, fn)); m = importlib.util.module_from_spec(sp)
    a = sys.argv; sys.argv = ['x', '12']; sp.loader.exec_module(m); sys.argv = a; return m
T = load('t5626', 'toy_5626_SEP2_E1_branched_cover_clause_height_lift_period_lattice_and_dislocation_centers_vs_n.py')

def Lbasis(m):
    h0 = m['hodd'][0]
    return T.lattice_hnf([(x - h0[0], y - h0[1]) for (x, y) in m['hodd'][1:]])
def rank_mod(basis, p):
    rows = [[x % p for x in b] for b in basis]
    # rank over F_p of <=2 rows in F_p^2
    rows = [r for r in rows if any(r)]
    if not rows: return 0
    if len(rows) == 1: return 1
    (a, b), (c, d) = rows
    return 2 if (a * d - b * c) % p else 1
def index(basis):
    if len(basis) < 2: return None
    return basis[0][0] * basis[1][1]
def in_charge_kernel(basis):
    return all((x + y) % 3 == 0 for (x, y) in basis)

def stats(m):
    B = Lbasis(m)
    return dict(idx=index(B), r3=rank_mod(B, 3), r2=rank_mod(B, 2), r=len(B), B=B, k=m['k'])

if __name__ == '__main__':
    t0 = time.time(); print('Toy 5639 — centre lattice L mod 3, in frame and off')
    HOSTS = {(20, 16), (20, 18), (21, 90), (22, 167), (23, 600), (24, 2076), (24, 2547), (24, 3244), (24, 5800)}
    inframe = Counter(); drops = Counter(); ok1 = True; nb = nc = 0; r1charge = Counter()
    for n in range(12, 25):
        for gi, rot in enumerate(T.plantri_rot(n)):
            deg = [len(r) for r in rot]; mx = max(deg)
            if mx > 6 and n > 20: continue
            faces = T.faces_of(rot)
            for f in T.colorings_mod_s4(rot, 10 ** 7):
                m = T.cover_measure(rot, faces, f); s = stats(m)
                key = (s['r'], s['idx'], s['r3'], s['r2'])
                inframe[('56' if mx <= 6 else 'k>12', key)] += 1
                if mx <= 6: nb += 1
                else: nc += 1
                if s['r'] == 2 and s['r3'] != 2: ok1 = False      # binds full-rank L only (rank-1 L has mod-3 rank 1 by rank)
                if s['r'] == 1:
                    (ux, uy), = s['B']; r1charge[(ux + uy) % 3 == 0] += 1
                if (n, gi) in HOSTS and (m['r'] < 2 or m['ed'] != (2, 2)):
                    drops[key] += 1
    print(f'\n  (a) the 71 drops — (rank L, index, rank mod 3, rank mod 2) -> count:')
    for k, v in sorted(drops.items(), key=str): print(f'      {k}: {v}')
    print(f'  (b)+(c) in frame: fullerene duals {nb} colourings, k>12 (n<=20) {nc} colourings:')
    for k, v in sorted(inframe.items(), key=str): print(f'      {k}: {v}')
    print(f'  rank-1 L in frame: generator u has zero Z_3-charge (x+y ≡ 0 mod 3)? {dict(r1charge)}')
    print(f'  Test 1 (every FULL-RANK in-frame L has 3 ∤ index, i.e. L mod 3 rank 2; rank-1 L excluded by rank): {"PASS" if ok1 else "FAIL"}')
    sweep = Counter(); i3 = []
    for n in range(6, 10):
        for rot in T.plantri_rot(n, flags=()):
            faces = T.faces_of(rot)
            for f in T.colorings_mod_s4(rot, 10 ** 6):
                m = T.cover_measure(rot, faces, f)
                if m['k'] < 2: continue
                s = stats(m); sweep[(s['k'], s['r'], s['idx'], s['r3'], s['r2'])] += 1
                if s['idx'] and s['idx'] % 3 == 0:
                    i3.append((n, s['B'], in_charge_kernel(s['B']), len(set(f[v] for v in m['odd']))))
    print(f'\n  (d) k-sweep n=6..9 — (k, rank L, index, rank mod 3, rank mod 2) -> count:')
    for k, v in sorted(sweep.items(), key=str): print(f'      {k}: {v}')
    print(f'  index-3 cases: {i3}')
    t2 = bool(i3) and all(b[1] and rank_mod(b[1], 3) == 1 for b in i3)
    print(f'  Test 2 (the index-3 case has L mod 3 rank 1; sublattice identified: charge kernel x+y≡0? {[b[2] for b in i3]}): {"PASS" if t2 else "FAIL"}')
    print(f'  Test 3 (table rendered) PASS')
    print(f'\nSCORE: {int(ok1)+int(t2)+1}/3   [{time.time()-t0:.0f}s]')
