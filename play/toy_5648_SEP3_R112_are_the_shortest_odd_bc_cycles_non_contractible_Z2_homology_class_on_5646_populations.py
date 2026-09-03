#!/usr/bin/env python3
"""
Toy 5648 — Round 112 §4 (Grace, 2026-09-03).  Lyra's theorem-shaped claim: a theta-clean record's V-image lies in a
line <a> iff the b∪c graph has no NON-CONTRACTIBLE odd cycle.  One line asked of me: on 5646's populations, is every
shortest odd b∪c cycle non-contractible (homology class ≠ 0)?  A cycle on a closed surface is null-homologous over Z2
iff every Z2-cocycle vanishes on it; contractible ⟹ null-homologous, and on the torus a simple null-homologous cycle
bounds a disc.  Method: Z2 cocycle basis of H^1(T^2; Z2) = Z2^2 by GF(2) linear algebra (cocycles = kernel of the
face-sum map on edge functions, modulo coboundaries = image of vertex functions); the shortest odd cycle returned as an
explicit vertex list (BFS tree paths + closing edge); its class = the two cocycle values.  Control: every FACE (a
contractible 3-cycle) must evaluate to 0 on both cocycles — asserted per triangulation.
Populations: flip-family tori n = 10 (six 4-colorable), T(6,3) all labelings, T(9,3)/T(6,6)/T(12,3) sampled (5,000).
"""
import os, sys, json, time, random
from collections import Counter, deque
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib
t = importlib.import_module('toy_5627_SEP2_E2_bundle_law_torus_test_completions_per_sign_record_mod_A4_with_sphere_disc_controls')
t43 = importlib.import_module('toy_5643_SEP3_R111_sign_negation_pairs_on_realized_records_and_odd_girth_of_the_bc_graph_on_theta_clean_records')
t46 = importlib.import_module('toy_5646_SEP3_R111_odd_girth_of_bc_graph_on_rainbow_labelings_of_sparser_larger_tori_is_3_a_density_artifact')
HERE = os.path.dirname(os.path.abspath(__file__)); T0 = time.time(); random.seed(5648)

def gf2_nullspace(M):
    """basis of the kernel of M (rows x cols) over GF(2), as list of 0/1 vectors."""
    M = M.copy() % 2; rows, cols = M.shape; piv = []; r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if M[i, c]), None)
        if p is None: continue
        M[[r, p]] = M[[p, r]]
        for i in range(rows):
            if i != r and M[i, c]: M[i] ^= M[r]
        piv.append(c); r += 1
        if r == rows: break
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for f in free:
        v = np.zeros(cols, dtype=np.uint8); v[f] = 1
        for i, c in enumerate(piv):
            if M[i, f]: v[c] = 1
        basis.append(v)
    return basis

def cocycle_basis(faces, n):
    """two Z2-cocycles on the torus spanning H^1 (not coboundaries)."""
    E = sorted({frozenset((f[i], f[(i+1)%3])) for f in faces for i in range(3)}, key=lambda e: sorted(e)); idx = {e: i for i, e in enumerate(E)}
    # face-sum map: rows = faces, cols = edges
    A = np.zeros((len(faces), len(E)), dtype=np.uint8)
    for fi, f in enumerate(faces):
        for i in range(3): A[fi, idx[frozenset((f[i], f[(i+1)%3]))]] = 1
    Z = gf2_nullspace(A)                                         # cocycles
    # coboundaries: delta of vertex indicator = edges at v
    B = np.zeros((n, len(E)), dtype=np.uint8)
    for e, i in idx.items():
        for v in e: B[v, i] = 1
    # pick cocycles independent modulo the row space of B: reduce [B; z] and test rank increase
    def rank(Mx):
        Mx = Mx.copy() % 2; r = 0; rows, cols = Mx.shape
        for c in range(cols):
            p = next((i for i in range(r, rows) if Mx[i, c]), None)
            if p is None: continue
            Mx[[r, p]] = Mx[[p, r]]
            for i in range(rows):
                if i != r and Mx[i, c]: Mx[i] ^= Mx[r]
            r += 1
            if r == rows: break
        return r
    base = B.copy(); rb = rank(base); chosen = []
    for z in Z:
        M2 = np.vstack([base, z[None, :]])
        if rank(M2) > rb: chosen.append(z); base = M2; rb += 1
        if len(chosen) == 2: break
    assert len(chosen) == 2, "torus H^1(Z2) should have rank 2"
    return E, idx, chosen

def cycle_class(cyc, idx, cocycles):
    m = len(cyc); cls = []
    for z in cocycles:
        s = 0
        for i in range(m): s ^= int(z[idx[frozenset((cyc[i], cyc[(i+1) % m]))]])
        cls.append(s)
    return tuple(cls)

def shortest_odd_cycle(n, edges):
    adj = {v: set() for v in range(n)}
    for u, v in edges: adj[u].add(v); adj[v].add(u)
    best = None
    for root in range(n):
        dist = {root: 0}; par = {root: None}; q = deque([root])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if w not in dist: dist[w] = dist[u] + 1; par[w] = u; q.append(w)
        for u in dist:
            for w in adj[u]:
                if w in dist and dist[u] == dist[w]:
                    L = dist[u] + dist[w] + 1
                    if best is None or L < best[0]:
                        pu = []; x = u
                        while x is not None: pu.append(x); x = par[x]
                        pw = []; x = w
                        while x is not None: pw.append(x); x = par[x]
                        # closed walk u..root..w then edge w-u; trim common tail to get a simple cycle
                        k = 0
                        while k < len(pu) and k < len(pw) and pu[-1-k] == pw[-1-k]: k += 1
                        cyc = pu[:len(pu)-k+1] + pw[:len(pw)-k][::-1]
                        best = (L, cyc)
    return best

def scan(name, faces, n, cap=None):
    E, idx, coc = cocycle_basis(faces, n)
    for f in faces: assert cycle_class(list(f), idx, coc) == (0, 0), "a face is not null-homologous"
    labs = t46.rainbow_labelings(faces, cap)
    h = Counter()
    for lab in labs:
        for a in (1, 2, 3):
            res = shortest_odd_cycle(n, t43.bc_graph_edges(faces, lab, a))
            if res is None: continue
            L, cyc = res
            cls = cycle_class(cyc, idx, coc)
            h[(L, 'non-contractible' if cls != (0, 0) else 'NULL-HOMOLOGOUS')] += 1
    print(f"  {name}: n={n} labelings {len(labs)}{' (sample)' if cap else ''}; shortest odd b∪c cycles by (length, class): {dict(sorted(h.items()))}   [{time.time()-T0:.0f}s]")
    return {str(k): v for k, v in h.items()}

def main():
    out = {}
    fam = t.torus_family(10); done = 0
    for key, faces in fam[10].items():
        if not t.all_4colorings(t.adjacency(faces), 10): continue
        out[f'flip10_{done}'] = scan(f"flip torus n=10 #{done}", faces, 10); done += 1
        if done >= 6: break
    for a, b, cap in ((6, 3, None), (9, 3, 5000), (6, 6, 5000), (12, 3, 5000)):
        faces, n = t.ms_torus(a, b); out[f'T{a}x{b}'] = scan(f"T({a},{b})", faces, n, cap)
    null = sum(v for d in out.values() for k, v in d.items() if 'NULL' in k); tot = sum(v for d in out.values() for v in d.values())
    print(f"\nTOTAL shortest odd b∪c cycles: {tot}; NULL-HOMOLOGOUS (contractible): {null}; non-contractible: {tot - null}")
    json.dump(out, open(os.path.join(HERE, '.out_5648.json'), 'w'), indent=1)
    print("SCORE: REPORTED — faces null-homologous asserted; cycle classes by population")

if __name__ == '__main__':
    main()
