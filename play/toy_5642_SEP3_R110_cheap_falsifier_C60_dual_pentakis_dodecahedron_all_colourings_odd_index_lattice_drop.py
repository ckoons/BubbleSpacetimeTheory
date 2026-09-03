#!/usr/bin/env python3
"""
Toy 5642 — Round 110 §3, THE CHEAP FALSIFIER (Lyra's prediction, pre-registered by Keeper 07:30):
Lyra's derivation of the odd-index exclusion holds where two dislocations are ADJACENT; every fullerene
dual n ≤ 24 has adjacent pentagons; the C₆₀ dual (pentakis dodecahedron, T2221: 32 vertices, 12 of degree 5
pairwise NON-adjacent, 20 of degree 6, 90 edges, 60 faces, 5-connected, in frame) is the first frame graph
where adjacency stops protecting. PREDICTION: a colouring whose dislocation-height lattice L has ODD index
(index 3, the charge-zero sublattice {x+y ≡ 0 mod 3}) EXISTS — never seen in frame. KILL: none among ALL its
colourings mod S₄.
Construction: icosahedron (plantri -c5 12) → vertices = 12 apexes; faces = 20 hexavalent vertices; apex–face
if incident, face–face if edge-adjacent; rotation system from the geometric embedding (unit-sphere
positions, angular sort of neighbours about the outward normal); checked: 60 triangular faces, Euler,
degrees 5¹²6²⁰, twelve degree-5 vertices pairwise non-adjacent, 5-connected (no cut of size ≤ 4).
Controls through the same lattice code: icosahedron (n=12: all colourings full index — 5626/5632), and the
k=4 off-frame index-3 case (n=8 sweep: MUST be found).
Report: the number of colourings mod S₄ FIRST; then the lattice table (rank, index, mod-3 rank, mod-2 rank)
and the colour pattern on the twelve (colour count and class sizes) per lattice type.
TESTS: 1. construction checks. 2. icosahedron control (all index 1). 3. k=4 index-3 control found.
4. THE FALSIFIER: an index-3 (odd-index) colouring exists on the C₆₀ dual — PASS = Lyra's prediction
   confirmed; FAIL = killed on one graph (both pre-scored; either is the result).
Elie, 2026-09-03. 4 tests.
"""
import importlib.util, os, sys, time, math, json, hashlib
from itertools import combinations
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
def load(nm, fn):
    sp = importlib.util.spec_from_file_location(nm, os.path.join(HERE, fn)); m = importlib.util.module_from_spec(sp)
    a = sys.argv; sys.argv = ['x', '12']; sp.loader.exec_module(m); sys.argv = a; return m
T = load('t5626', 'toy_5626_SEP2_E1_branched_cover_clause_height_lift_period_lattice_and_dislocation_centers_vs_n.py')
T39 = load('t5639', 'toy_5639_SEP3_R109_centre_lattice_mod_3_rank_on_the_71_drops_the_frame_and_the_k4_index3_case.py')

def pentakis():
    phi = (1 + 5 ** 0.5) / 2
    P = []
    for a in (-1, 1):
        for b in (-phi, phi):
            P += [(0, a, b), (a, b, 0), (b, 0, a)]
    P = [tuple(x / math.sqrt(1 + phi * phi) for x in p) for p in P]      # 12 unit vectors
    def dot(u, v): return sum(a * b for a, b in zip(u, v))
    ico_adj = {i: [j for j in range(12) if j != i and dot(P[i], P[j]) > 0.4] for i in range(12)}
    assert all(len(v) == 5 for v in ico_adj.values())
    faces = sorted({tuple(sorted((i, j, k))) for i in range(12) for j in ico_adj[i] for k in ico_adj[i] if j < k and k in ico_adj[j]})
    assert len(faces) == 20
    # vertices: 0..11 apexes (icosa vertices, pushed out), 12..31 = icosa faces (centroids)
    pos = list(P)
    for F in faces:
        c = [sum(P[v][t] for v in F) / 3 for t in range(3)]; nrm = math.sqrt(dot(c, c)); pos.append(tuple(x / nrm for x in c))
    n = 32; adj = {i: set() for i in range(n)}
    for fi, F in enumerate(faces):
        for v in F: adj[v].add(12 + fi); adj[12 + fi].add(v)
    for fi, F in enumerate(faces):
        for gj, G in enumerate(faces):
            if fi < gj and len(set(F) & set(G)) == 2: adj[12 + fi].add(12 + gj); adj[12 + gj].add(12 + fi)
    # rotation: angular sort of neighbours in the tangent plane at each vertex
    rot = []
    for v in range(n):
        nv = pos[v]
        # tangent basis
        t = (1, 0, 0) if abs(nv[0]) < 0.9 else (0, 1, 0)
        e1 = [t[i] - dot(t, nv) * nv[i] for i in range(3)]; l = math.sqrt(dot(e1, e1)); e1 = [x / l for x in e1]
        e2 = [nv[1] * e1[2] - nv[2] * e1[1], nv[2] * e1[0] - nv[0] * e1[2], nv[0] * e1[1] - nv[1] * e1[0]]
        ang = []
        for w in adj[v]:
            d = [pos[w][i] - nv[i] for i in range(3)]
            ang.append((math.atan2(dot(d, e2), dot(d, e1)), w))
        rot.append([w for _, w in sorted(ang)])
    return rot

def connected_without(rot, S):
    rest = [v for v in range(len(rot)) if v not in S]; seen = {rest[0]}; st = [rest[0]]
    while st:
        x = st.pop()
        for y in rot[x]:
            if y not in S and y not in seen: seen.add(y); st.append(y)
    return len(seen) == len(rest)

if __name__ == '__main__':
    t0 = time.time(); print('=' * 78); print('Toy 5642 — the C60 dual: all colourings, odd-index lattice drop?'); print('=' * 78)
    rot = pentakis(); n = len(rot); faces = T.faces_of(rot)
    deg = Counter(len(r) for r in rot); m = sum(len(r) for r in rot) // 2
    d5 = [v for v in range(n) if len(rot[v]) == 5]
    nonadj = all(w not in rot[v] for v in d5 for w in d5)
    tri = len(faces) == 60 and all(len(F) == 3 for F in faces)
    euler = n - m + len(faces) == 2
    conn5 = all(connected_without(rot, set(S)) for s in range(1, 5) for S in combinations(range(n), s))
    t1 = tri and euler and dict(deg) == {5: 12, 6: 20} and m == 90 and nonadj and conn5
    print(f'  construction: n={n}, m={m}, faces={len(faces)} triangles={tri}, Euler={euler}, degrees={dict(deg)}, twelve deg-5 pairwise non-adjacent={nonadj}, 5-connected={conn5}')
    print(f'  Test 1 (construction) {"PASS" if t1 else "FAIL"}')
    # controls
    ico = T.plantri_rot(12)[0]; fi = T.faces_of(ico)
    icos = Counter()
    for f in T.colorings_mod_s4(ico, 10 ** 7):
        s = T39.stats(T.cover_measure(ico, fi, f)); icos[(s['r'], s['idx'], s['r3'])] += 1
    t2 = set(icos) == {(2, 1, 2)}
    print(f'  Test 2 (icosahedron control, (rank, index, r3) -> count {dict(icos)}; all index 1): {"PASS" if t2 else "FAIL"}')
    found3 = 0
    for g in T.plantri_rot(8, flags=()):
        fg = T.faces_of(g)
        for f in T.colorings_mod_s4(g, 10 ** 6):
            mm = T.cover_measure(g, fg, f)
            if mm['k'] == 4:
                s = T39.stats(mm)
                if s['idx'] and s['idx'] % 3 == 0: found3 += 1
    t3 = found3 >= 1
    print(f'  Test 3 (k=4 off-frame index-3 control found through this code: {found3}): {"PASS" if t3 else "FAIL"}')
    sys.stdout.flush()
    # the falsifier
    cols = T.colorings_mod_s4(rot, 10 ** 8)
    print(f'\n  C60 dual: proper 4-colourings mod S4 = {len(cols)}  [{time.time()-t0:.0f}s]'); sys.stdout.flush()
    tab = Counter(); pat = Counter(); wit = []
    for i, f in enumerate(cols):
        mm = T.cover_measure(rot, faces, f); s = T39.stats(mm)
        key = (s['r'], s['idx'], s['r3'], s['r2'])
        n5 = len(set(f[v] for v in d5)); part = tuple(sorted(Counter(f[v] for v in d5).values(), reverse=True))
        tab[key] += 1; pat[(key, n5, part)] += 1
        if s['idx'] and s['idx'] % 2 == 1 and s['idx'] > 1 and len(wit) < 5: wit.append((i, ''.join(map(str, f)), s['B']))
        if s['r'] < 2 and len(wit) < 5: wit.append((i, ''.join(map(str, f)), s['B']))
    print('  lattice table (rank L, index, rank mod 3, rank mod 2) -> count:')
    for k, v in sorted(tab.items(), key=str): print(f'    {k}: {v}')
    print('  colour pattern on the twelve degree-5 vertices, per lattice type: (type, #colours, class sizes) -> count:')
    for k, v in sorted(pat.items(), key=str): print(f'    {k}: {v}')
    odd = sum(v for k, v in tab.items() if k[1] and k[1] % 2 == 1 and k[1] > 1)
    t4 = odd > 0
    print(f'\n  ODD-INDEX colourings: {odd}; witnesses (index in enumeration, colouring, L basis): {wit[:5]}')
    print(f'  Test 4 (THE FALSIFIER — an odd-index lattice exists on the C60 dual): {"PASS — Lyra\'s prediction confirmed" if t4 else "FAIL — prediction killed on one graph (kill condition met)"}')
    rows = sorted((str(k), v) for k, v in pat.items()); h = hashlib.sha256(json.dumps(rows).encode()).hexdigest()[:8]
    json.dump(dict(table={str(k): v for k, v in tab.items()}, pattern={str(k): v for k, v in pat.items()}, witnesses=wit, ncol=len(cols)), open(os.path.join(HERE, '.c60_5642.json'), 'w'), indent=1)
    print(f'  table play/.c60_5642.json sha256 {h}')
    print(f'\nSCORE: {int(t1)+int(t2)+int(t3)+int(t4)}/4   [{time.time()-t0:.0f}s]')
