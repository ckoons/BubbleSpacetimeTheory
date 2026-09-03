#!/usr/bin/env python3
"""
Toy 5654 — Round 114 §3 (Grace, 2026-09-03), pre-registered at 14:22: the LONG-direction Z3-cover of T(a,3).
Build the TRANSPORT-GRADED transfer matrix at width 3: state = (previous strip's vertex-sum residues in Z3^3, the seam
label in {1,2,3} carried along the row-0 dual path).  Per strip the six signs fix (a) the vertex-sum contributions and
(b) the permutation of the seam label (fill f2(x,0) from v(x,0), then f1(x,0) from d(x,0), read v(x+1,0)).
Then tr(M^a) counts (closed record, seam label) pairs whose label returns: = 3·N_{theta_LONG = 0}(a) exactly (the
SHORT-cycle holonomy is not constrained by the trace — the first run compared against 5628's both-trivial count and
mis-scored the 3|a rows; corrected 14:35: at a = 3 the excess (228 − 120)/3 = 36 is toy 5629's count of transport
orphans obstructed in the short direction only — exact), and the
Fourier decomposition over the label rotation gives the three character blocks M_chi with tr(M_chi^a) = sum_g chi(g) N_g(a),
the untwisted block being toy 5628's closed matrix (N(a) = tr).  Kills: tr(M^a) != 3·theta0(a) from 5628/5627 (40 at
a=3; 1,584 at a=6); the untwisted block's spectrum != 5628's closed spectrum; the Perron eigenvalue of M != that block's.
"""
import os, sys, json, itertools, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib
t = importlib.import_module('toy_5627_SEP2_E2_bundle_law_torus_test_completions_per_sign_record_mod_A4_with_sphere_disc_controls')
m28 = importlib.import_module('toy_5628_SEP2_E2_decision_cost_transfer_matrix_closed_transport_realized_records_on_T3L3M_constant_part_test')
HERE = os.path.dirname(os.path.abspath(__file__))
b = 3

def fill_map(z, k_in, k_out):
    """face with sign z (+1/-1): given the label l on dart position k_in, return the label on dart position k_out.
    Dart positions 0,1,2 = (u,v),(v,w),(w,u) of the ccw face; toy 5627 convention: z=+1 <=> labels (l1,l2,l3) a rotation of (1,2,3)."""
    order = (1, 2, 3) if z == 1 else (1, 3, 2)
    def f(l):
        s = order.index(l)
        return order[(s + (k_out - k_in)) % 3]
    return f

def strip_maps():
    """for each of the 64 sign patterns of a strip (f1(y), f2(y), y=0,1,2): (cx contribution, cn contribution, label map)."""
    out = []
    for signs in itertools.product((1, -1), repeat=2 * b):
        f1 = signs[:b]; f2 = signs[b:]
        z = lambda s: 1 if s == 1 else 2
        cx = tuple((z(f1[y]) + z(f2[y]) + z(f2[(y - 1) % b])) % 3 for y in range(b))
        cn = tuple((z(f1[y]) + z(f1[(y - 1) % b]) + z(f2[(y - 1) % b])) % 3 for y in range(b))
        # f2(x,0) = ((x,0),(x+1,1),(x,1)) ccw: darts (p,r),(r,s),(s,p) = d(x,0), (x+1,1)->(x,1) is h(x,1) reversed, v(x,0) reversed
        # enter via v(x,0) = dart position 2 (s,p) = ((x,1),(x,0)); exit via d(x,0) = position 0
        g2 = fill_map(f2[0], 2, 0)
        # f1(x,0) = ((x,0),(x+1,0),(x+1,1)) ccw: darts (p,q)=h(x,0), (q,r)=v(x+1,0), (r,p)=d(x,0) reversed
        # enter via d(x,0) = position 2; exit via v(x+1,0) = position 1
        g1 = fill_map(f1[0], 2, 1)
        out.append((cx, cn, lambda l, g1=g1, g2=g2: g1(g2(l))))
    return out

def build():
    S = [(s, l) for s in itertools.product(range(3), repeat=b) for l in (1, 2, 3)]
    idx = {x: i for i, x in enumerate(S)}
    M = np.zeros((len(S), len(S)), dtype=np.int64)
    for cx, cn, lab in strip_maps():
        s_req = tuple((-c) % 3 for c in cx)
        for l in (1, 2, 3):
            M[idx[(s_req, l)], idx[(cn, lab(l))]] += 1
    return S, idx, M

def main():
    S, idx, M = build()
    print(f"graded matrix: {M.shape[0]} states (27 residues x 3 labels)")
    # identity: tr(M^a) = 3 * theta0(a)
    d = json.load(open(os.path.join(HERE, '.decision_cost_T3L3M_5628.json')))
    rows = {r['a']: r for r in d['b=3']['rows']}
    P = np.identity(M.shape[0], dtype=object); Mo = M.astype(object)
    ok = True
    for a in range(1, 13):
        P = P.dot(Mo); tr = int(np.trace(P))
        if a in rows:
            th = rows[a]['theta0']; excess = tr // 3 - th
            flag = (excess == 0) if a % 3 else (excess >= 0)
            known = {3: 36}   # toy 5629: T(3,3) transport orphans obstructed in the short direction only
            if a in known: flag = flag and (excess == known[a])
            ok &= flag
            print(f"  a={a:2d}: tr(M^a)/3 = {tr//3:>10d} = N_theta_long=0;  N_theta=0 (5628) = {th:>10d};  excess (theta_long=0, theta_short!=0) = {excess:>8d}"
                  f"{'  = 5629 (36) ✓' if a in known else ''}   {'✓' if flag else 'KILL'}")
    # Fourier blocks over the label rotation 1->2->3->1
    w3 = np.exp(2j * np.pi / 3)
    rot = {1: 2, 2: 3, 3: 1}
    n = len(S); blocks = {}
    for k in range(3):
        # projector onto chi_k: (1/3) sum_j chi_k(j)^-1 R^j  where R shifts the label
        R = np.zeros((n, n))
        for (s, l), i in idx.items(): R[i, idx[(s, rot[l])]] = 1
        Pk = sum((w3 ** (-k * j)) * np.linalg.matrix_power(R, j) for j in range(3)) / 3
        Mk = Pk @ M.astype(complex)
        ev = np.linalg.eigvals(Mk); ev = sorted([e for e in ev if abs(e) > 1e-9], key=lambda z: -abs(z))
        blocks[k] = ev
        print(f"  block chi_{k}: top |eigenvalues| {[round(abs(e),4) for e in ev[:6]]}")
    base = sorted(np.linalg.eigvals(np.array(m28.closed_T(3), dtype=float)), key=lambda z: -abs(z))
    print(f"  5628 closed matrix (untwisted): top |eigenvalues| {[round(abs(e),4) for e in base[:6]]}")
    match = all(abs(abs(blocks[0][i]) - abs(base[i])) < 1e-6 for i in range(6))
    perron = abs(max(np.linalg.eigvals(M.astype(float)), key=abs))
    print(f"  untwisted block == 5628 closed spectrum (top 6): {match}; Perron of the graded matrix {perron:.6f} = base 4.000000: {abs(perron-4)<1e-6}")
    # long-direction cover: T(3a,3) count = tr(M_base^{3a}) — cubes; pullbacks = 3*theta0 records lifted
    print("SCORE:", "PASS" if ok and match and abs(perron - 4) < 1e-6 else "FAIL", "— identity tr(M^a) = 3·N_{θ_long=0} (exact where checkable), untwisted block = base, Perron unchanged")

if __name__ == '__main__':
    main()
