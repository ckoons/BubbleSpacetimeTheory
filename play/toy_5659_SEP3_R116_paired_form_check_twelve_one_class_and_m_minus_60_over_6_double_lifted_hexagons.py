#!/usr/bin/env python3
"""
Toy 5659 — Round 116 §1: the paired-form check (hashed 15:07, sha256 5fa22314…). On each confined IPR isomer
C60…C120 (92 graphs; [c] = 0 so the ℤ₃ potential φ on the branched double cover Σ is well-defined up to a
constant): (P7a) the twelve dislocation lifts carry one φ value; (P7b) the number of degree-6 vertices whose
two lifts BOTH carry the dislocation value equals (m − 60)/6. Also reported (not predicted): the distribution
of the pair (φ(u), φ(ιu)) over hexagon vertices, and the check that φ(ιu) = κ − φ(u) with κ ≡ 2·(dislocation
value) (Lyra's deck-involution identity). Elie, 2026-09-03.
"""
import importlib.util, os, sys, json
from collections import Counter, deque
HERE = os.path.dirname(os.path.abspath(__file__))
def load(nm, fn):
    sp = importlib.util.spec_from_file_location(nm, os.path.join(HERE, fn)); m = importlib.util.module_from_spec(sp)
    a = sys.argv; sys.argv = ['x', '12']; sp.loader.exec_module(m); sys.argv = a; return m
T = load('t5626', 'toy_5626_SEP2_E1_branched_cover_clause_height_lift_period_lattice_and_dislocation_centers_vs_n.py')
T44 = load('t5644', 'toy_5644_SEP3_R111_pentagon_adjacency_series_C46_C58_fullerene_duals_lattice_index_vs_Np_and_C70_replication.py')

def potential_and_lifts(rot):
    n = len(rot); faces = T.faces_of(rot); deg = [len(r) for r in rot]
    fidx = {}
    for i, F in enumerate(faces):
        for j in range(3): fidx[(F[j], F[(j + 1) % 3])] = i
    fan = [[fidx[(v, w)] for w in rot[v]] for v in range(n)]
    cv = {}; ncv = 0
    for v in range(n):
        for pos, fi in enumerate(fan[v]):
            for s in (1, -1):
                base = s * (1 if pos % 2 == 0 else -1); key = (v, 0) if deg[v] % 2 else (v, base)
                if key not in cv: cv[key] = ncv; ncv += 1
                cv[(v, fi, s)] = cv[key]
    edges = {}
    for i, F in enumerate(faces):
        for s in (1, -1):
            for j in range(3):
                u, v = F[j], F[(j + 1) % 3]; cu, cvv = cv[(u, i, s)], cv[(v, i, s)]; c = s % 3
                key, desc = ((u, v, s), (cu, cvv, c)) if u < v else ((v, u, -s), (cvv, cu, (-c) % 3))
                edges.setdefault(key, desc)
    adj = [[] for _ in range(ncv)]
    for cu, cvv, c in edges.values(): adj[cu].append((cvv, c)); adj[cvv].append((cu, (-c) % 3))
    phi = [None] * ncv; phi[0] = 0; dq = deque([0])
    while dq:
        x = dq.popleft()
        for y, c in adj[x]:
            if phi[y] is None: phi[y] = (phi[x] + c) % 3; dq.append(y)
    charged = sum(1 for cu, cvv, c in edges.values() if (phi[cu] + c - phi[cvv]) % 3)
    disl = [cv[(v, 0)] for v in range(n) if deg[v] % 2]
    hexes = [(cv[(v, 1)], cv[(v, -1)]) for v in range(n) if deg[v] % 2 == 0]
    return phi, charged, disl, hexes

if __name__ == '__main__':
    rows51 = json.load(open(os.path.join(HERE, '.census_5651_sealed.json')))
    rows58 = json.load(open(os.path.join(HERE, '.p6_5658_rows.json')))
    conf = [(r['m'], r['ipr'], r['idx']) for r in rows51 if r['class_zero'] and (r['ipr'] or r['m'] == 60)] + [(r['m'], True, r['idx']) for r in rows58 if r['confined']]
    print(f'Toy 5659 — paired-form check on {len(conf)} confined isomers')
    cache = {}; ok_a = ok_b = ok_inv = True; bym = Counter(); fails = []; pairdist = Counter()
    for m, ipr, gi in conf:
        if (m, ipr) not in cache: cache[(m, ipr)] = T44.fullgen_duals(m, ipr=ipr)
        phi, charged, disl, hexes = potential_and_lifts(cache[(m, ipr)][gi])
        assert charged == 0
        dv = {phi[d] for d in disl}
        if len(dv) != 1: ok_a = False; fails.append(('P7a', m, gi, dv)); continue
        d0 = dv.pop(); kappa = (2 * d0) % 3
        inv = all((phi[a] + phi[b]) % 3 == kappa for a, b in hexes); ok_inv &= inv
        dl = sum(1 for a, b in hexes if phi[a] == d0 and phi[b] == d0)
        for a, b in hexes: pairdist[tuple(sorted(((phi[a] - d0) % 3, (phi[b] - d0) % 3)))] += 1
        bym[(m, dl)] += 1
        if dl != (m - 60) // 6: ok_b = False; fails.append(('P7b', m, gi, dl, (m - 60) // 6))
    print('  (m, double-lifted hexagons) -> isomer count: ' + ' · '.join(f'{m}: {dl} ×{c}' for (m, dl), c in sorted(bym.items())))
    print(f'  hexagon-vertex pair classes (φ(u)−d₀, φ(ιu)−d₀) pooled: {dict(sorted(pairdist.items()))}   [(0,0) = double-lifted into the dislocation class; (1,2) = the involution-swapped pair]')
    print(f'  Test 1 (P7a: twelve in one φ-class, {len(conf)}/{len(conf)}): {"PASS" if ok_a else "FAIL"}')
    print(f'  Test 2 (deck identity φ(ιu) = κ − φ(u), κ = 2·d₀, every hexagon vertex): {"PASS" if ok_inv else "FAIL"}')
    print(f'  Test 3 (P7b: double-lifted count = (m−60)/6 on every confined isomer; failures {fails[:6]}): {"PASS" if ok_b else "FAIL"}')
    print(f'\nSCORE: {int(ok_a)+int(ok_inv)+int(ok_b)}/3')
