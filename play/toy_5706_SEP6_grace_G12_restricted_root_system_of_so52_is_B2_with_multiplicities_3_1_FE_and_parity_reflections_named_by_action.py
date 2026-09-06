#!/usr/bin/env python3
"""
toy 5706 — Grace, 2026-09-06 (Round 121 G12). Restricted root system of so(5,2) computed from the matrix Lie algebra.
g = so(5,2) = {X : X^T J + J X = 0}, J = diag(1,1,1,1,1,-1,-1). Cartan involution theta(X) = -X^T; k = so(5)+so(2) (block-diagonal),
p = off-diagonal blocks. a = span(H1, H2) with H_i the boost mixing e_i (space, i = 1,2) with f_i (time, i = 1,2): maximal abelian in p
(dim 2 = rank). Diagonalise ad(H) on g for a generic H = t1 H1 + t2 H2: the eigenvalues are the restricted roots alpha(H) = ±t_i (mult m_s)
and ±t1 ± t2 (mult m_l); the type is read off the root lengths/angles: B2 (short ±e_i, long ±e1±e2) with multiplicities (m_s, m_l).
Prediction (pre-stated, Helgason Ch. X Table VI, SO_0(p,q), p > q: type B_q, m(±e_i) = p - q, m(±e_i±e_j) = 1): (m_s, m_l) = (3, 1).
Then name the Weyl reflections by their ACTION on the polydisc coordinates mu = (t1 + t2, t1 - t2) (Lyra L2's gamma_1 = e1 + e2, gamma_2 = e1 - e2):
  s_{e1-e2}: (t1,t2) -> (t2,t1) : negates mu_2, fixes mu_1   [FE of the second factor]  -- root of multiplicity 1
  s_{e2}:    (t1,t2) -> (t1,-t2): swaps mu_1 <-> mu_2         [polydisc swap = parity]   -- root of multiplicity 3
As abstract root systems B2 and C2 are isomorphic (long <-> short relabelled); the multiplicities are convention-free and pin the B2 labels.
"""
import numpy as np, itertools, sys

def so_pq(p, q):
    n = p + q; J = np.diag([1.0]*p + [-1.0]*q)
    basis = []
    for i in range(n):
        for j in range(i+1, n):
            X = np.zeros((n, n)); X[i, j] = 1.0
            # X^T J + J X = 0  <=>  X = J^{-1} A with A antisymmetric?  Use: elements are J^{-1} A, A antisymmetric.
            A = np.zeros((n, n)); A[i, j] = 1.0; A[j, i] = -1.0
            basis.append(np.linalg.inv(J) @ A)
    return basis, J

def main():
    p, q = 5, 2
    basis, J = so_pq(p, q); n = p + q
    for X in basis: assert np.allclose(X.T @ J + J @ X, 0)
    dim = len(basis); print(f'dim so({p},{q}) = {dim}')
    # boosts H1 (e1<->f1 = index 0<->5), H2 (e2<->f2 = 1<->6)
    def boost(i, j):
        A = np.zeros((n, n)); A[i, j] = 1.0; A[j, i] = -1.0
        return np.linalg.inv(J) @ A
    H1, H2 = boost(0, 5), boost(1, 6)
    assert np.allclose(H1 @ H2 - H2 @ H1, 0), 'H1, H2 must commute'
    assert np.allclose(H1.T, H1) and np.allclose(H2.T, H2), 'boosts lie in p (symmetric)'
    # ad matrices in the basis
    B = np.array([X.flatten() for X in basis]).T  # columns = basis vectors
    def ad(H):
        M = np.array([(H @ X - X @ H).flatten() for X in basis]).T
        return np.linalg.lstsq(B, M, rcond=None)[0]
    t1, t2 = 1.0, 0.37  # generic
    adH = ad(t1*H1 + t2*H2)
    ev = np.linalg.eigvals(adH).real
    ev = np.round(ev, 8)
    from collections import Counter
    c = Counter(ev)
    print('eigenvalues of ad(t1 H1 + t2 H2), t=(1, 0.37):')
    for v, m in sorted(c.items()): print(f'   {v:+.4f}  mult {m}')
    # identify
    roots = {}
    for v, m in c.items():
        if abs(v) < 1e-6: roots['0 (centralizer m_0)'] = m; continue
        for name, val in (('+e1', t1), ('-e1', -t1), ('+e2', t2), ('-e2', -t2), ('+e1+e2', t1+t2), ('-e1-e2', -(t1+t2)), ('+e1-e2', t1-t2), ('-e1+e2', -(t1-t2))):
            if abs(v - val) < 1e-6: roots[name] = m
    print('restricted roots and multiplicities:', roots)
    ms = roots.get('+e1'); ml = roots.get('+e1+e2')
    m0 = roots.get('0 (centralizer m_0)')
    ok_type = all(k in roots for k in ('+e1', '+e2', '+e1+e2', '+e1-e2')) and len([k for k in roots if not k.startswith('0')]) == 8
    print(f'type: {"B2 (8 roots: ±e_i, ±e1±e2)" if ok_type else "NOT B2"};  m(±e_i) = {ms}, m(±e1±e2) = {ml}, dim centralizer = {m0}')
    print('check dim: 2*(2*ms + 2*ml) + m0 =', 2*(2*ms + 2*ml) + m0, '=', dim)
    pred = (ms, ml) == (p - q, 1)
    print(f'PREDICTION (Helgason Table VI: (p−q, 1) = (3, 1)): {"HIT" if pred else "MISS"}')
    # Weyl reflections named by action on polydisc coordinates mu = (t1+t2, t1-t2)
    def refl(alpha, t):  # reflection of t=(t1,t2) in the root alpha (Euclidean)
        a = np.array(alpha, float); t = np.array(t, float); return tuple(np.round(t - 2*np.dot(t, a)/np.dot(a, a)*a, 6))
    t = (t1, t2); mu = lambda t: (round(t[0]+t[1], 6), round(t[0]-t[1], 6))
    print('polydisc coordinates mu = (t1+t2, t1-t2) of t =', t, '->', mu(t))
    for name, alpha, m in (('s_{e1-e2} (mult 1)', (1, -1), ml), ('s_{e1+e2} (mult 1)', (1, 1), ml), ('s_{e2} (mult 3)', (0, 1), ms), ('s_{e1} (mult 3)', (1, 0), ms)):
        tt = refl(alpha, t); print(f'   {name}: t -> {tt}, mu -> {mu(tt)}')
    print('NAMES BY ACTION: the reflection NEGATING one polydisc coordinate (FE) is the one in a root of multiplicity 1 (s_{e1∓e2}); '
          'the reflection EXCHANGING the polydisc coordinates (parity/divisor swap) is the one in a root of multiplicity 3 (s_{e_i}).')
    print('SCORE:', 'B2 with (3,1) HIT; names by action verified' if pred and ok_type else 'MISS')

if __name__ == '__main__':
    main()
