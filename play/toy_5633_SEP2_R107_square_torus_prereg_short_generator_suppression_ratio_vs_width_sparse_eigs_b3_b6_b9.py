#!/usr/bin/env python3
"""
Toy 5633 — toward the SQUARE-TORUS pre-registration (Keeper K1850 amended; Grace 16:25): on T(a,b) the constant
D -> log2 12 because the FIXED-length generator's nonzero-holonomy sectors are exponentially suppressed per column
(second eigenvalue lambda_2 < lambda_1 of the closed-record transfer matrix).  If both generators are free (square
tori) the constant should read log2 144.  Pre-registered here before the run: the suppression ratio
r(b) = lambda_2/lambda_1 of the closed-record transfer matrix RISES toward 1 with width b (0.683 at b=3, 0.811 at b=6
from toy 5628), and the leading eigenvalue of the closed matrix equals that of the coloring matrix at b = 9 too.
Grace, 2026-09-02.  Sparse transfer matrices (3^b states), scipy eigs for the top eigenvalues; b = 3, 6, 9.
"""
import itertools, time, json, os
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sla
HERE = os.path.dirname(os.path.abspath(__file__)); T0 = time.time()

def closed_sparse(b):
    S = list(itertools.product(range(3), repeat=b)); idx = {s: i for i, s in enumerate(S)}
    rows, cols, vals = [], [], []
    cnt = {}
    for signs in itertools.product((1, 2), repeat=2 * b):
        f1 = signs[:b]; f2 = signs[b:]
        cx = tuple((f1[y] + f2[y] + f2[(y - 1) % b]) % 3 for y in range(b))
        cn = tuple((f1[y] + f1[(y - 1) % b] + f2[(y - 1) % b]) % 3 for y in range(b))
        s = tuple((-c) % 3 for c in cx)
        k = (idx[s], idx[cn]); cnt[k] = cnt.get(k, 0) + 1
    for (i, j), v in cnt.items(): rows.append(i); cols.append(j); vals.append(v)
    return sp.csr_matrix((vals, (rows, cols)), shape=(len(S), len(S)), dtype=float)

def coloring_sparse(b):
    S = [c for c in itertools.product(range(4), repeat=b) if all(c[y] != c[(y + 1) % b] for y in range(b))]
    idx = {s: i for i, s in enumerate(S)}
    # neighbours: c' with c'(y) != c(y) and c'(y) != c(y+1): build by DFS over y
    rows, cols = [], []
    for c in S:
        i = idx[c]
        opts = [[x for x in range(4) if x != c[y] and x != c[(y + 1) % b]] for y in range(b)]
        for cn in itertools.product(*opts):
            if all(cn[y] != cn[(y + 1) % b] for y in range(b)):
                rows.append(i); cols.append(idx[cn])
    return sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(len(S), len(S)))

def top(T, k=6):
    w = sla.eigs(T, k=k, which='LM', return_eigenvectors=False, maxiter=5000, tol=1e-10)
    return sorted([abs(x) for x in w], reverse=True)

def main():
    out = {}
    for b in (3, 6, 9):
        Z = closed_sparse(b); C = coloring_sparse(b)
        wz = top(Z); wc = top(C)
        r = wz[1] / wz[0]
        print(f"b={b}: closed states {Z.shape[0]} nnz {Z.nnz} | top |eig| closed {[round(x,4) for x in wz]} | coloring "
              f"{[round(x,4) for x in wc]} | lambda1 equal: {abs(wz[0]-wc[0])<1e-6} | r(b)=lambda2/lambda1 = {r:.4f} "
              f"| per-column log2 suppression {np.log2(wz[0]/wz[1]):.4f}   [{time.time()-T0:.0f}s]")
        out[b] = dict(closed=wz, coloring=wc, ratio=r)
    json.dump(out, open(os.path.join(HERE, '.square_torus_prereg_5633.json'), 'w'), indent=1)
    rs = [out[b]['ratio'] for b in (3, 6, 9)]
    print("ratios r(3), r(6), r(9) =", [round(x, 4) for x in rs], "monotone rising:", rs[0] < rs[1] < rs[2])
    print("SCORE:", "PASS" if rs[0] < rs[1] < rs[2] and all(abs(out[b]['closed'][0]-out[b]['coloring'][0])<1e-6 for b in (3,6,9)) else "FAIL",
          "— pre-registered: ratio rises with width and lambda1(closed) = lambda1(coloring)")

if __name__ == '__main__':
    main()
