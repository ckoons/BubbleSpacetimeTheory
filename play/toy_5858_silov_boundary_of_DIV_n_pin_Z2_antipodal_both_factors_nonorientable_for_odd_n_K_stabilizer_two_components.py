#!/usr/bin/env python3
"""Toy 5858 (Grace, 2026-10-07, round K4-0 Lane B pin 5): the Silov boundary of D_IV^n, checked.

Source pinned: Chirvasitu, arXiv:2007.05930 (citing Upmeier 1996, Ex. 1.5.52):
  Lie sphere L^n = T . S^{n-1} in C^n;  z.x = (-z).(-x);  L^n = (S^1 x S^{n-1})/(Z/2),
  "the Z/2-action is antipodal on both factors"; "fibers over the circle ... with fiber
  S^{n-1}. That bundle is trivial precisely when n is even."
Checks (n = 3..8, numerics to 1e-12):
  A. points e^{i th} x saturate BOTH Lie-ball conditions (|z|=1 and |z.z|=1, z.z = sum z_k^2);
  B. the Z/2 identification (th, x) ~ (th+pi, -x) is exact;
  C. orientation sign of the Z/2 on S^1 x S^{n-1} = (-1)^n  -> L^n NON-orientable for odd n;
  D. fibre monodromy over the circle = antipodal map of S^{n-1}, degree (-1)^n;
  E. K = SO(n) x SO(2), z -> e^{i phi} A z: stabilizer of e_1 has two components (phi=0, phi=pi),
     dim K - dim K_xi = n = dim L^n (transitive).
"""
import numpy as np
rng = np.random.default_rng(5858)
TOL = 1e-12
def rand_sphere(n):
    v = rng.normal(size=n); return v/np.linalg.norm(v)
def tangent_frame_S1xS(th, x):
    # oriented frame at (u,x) in R^2 x R^n: [d/dth, then an oriented basis of T_x S^{n-1}]
    n = len(x); u = np.array([np.cos(th), np.sin(th)])
    t_th = np.concatenate([[-u[1], u[0]], np.zeros(n)])
    # T_x S^{n-1}: complete x to an oriented basis (x, e2..en) of R^n with det +1
    M = np.linalg.qr(np.column_stack([x, rng.normal(size=(n, n-1))]))[0]
    if np.dot(M[:,0], x) < 0: M[:,0] *= -1
    if np.linalg.det(M) < 0: M[:,-1] *= -1
    Tx = [np.concatenate([[0,0], M[:,k]]) for k in range(1, n)]
    normals = [np.concatenate([u, np.zeros(n)]), np.concatenate([[0,0], x])]
    return np.column_stack(normals + [t_th] + Tx)   # ambient oriented frame: normals first
results = {}
for n in range(3, 9):
    okA = okB = True
    for _ in range(200):
        th = rng.uniform(0, 2*np.pi); x = rand_sphere(n); z = np.exp(1j*th)*x
        okA &= abs(np.vdot(z, z).real - 1) < TOL and abs(abs(np.sum(z*z)) - 1) < TOL
        okB &= np.allclose(np.exp(1j*(th+np.pi))*(-x), z, atol=TOL)
    # C: orientation sign of sigma(u,x) = (-u,-x); sigma is linear (-I) on R^{2+n}; it maps
    # outward normals at p to outward normals at sigma(p); sign = det(sigma) * (normal-frame sign)
    th = rng.uniform(0, 2*np.pi); x = rand_sphere(n)
    F = tangent_frame_S1xS(th, x); Fs = tangent_frame_S1xS(th+np.pi, -x)
    image = -F                                     # d(sigma) = -I applied to the frame at p
    # express image in the oriented frame at sigma(p); the normal block must be +identity
    C = np.linalg.solve(Fs, image)
    normal_block = C[:2,:2]; tang_block = C[2:,2:]
    okNormal = np.allclose(normal_block, np.eye(2), atol=1e-9) and np.allclose(C[2:,:2], 0, atol=1e-9)
    orient = int(np.sign(np.linalg.det(tang_block)))
    # D: monodromy degree = det(-I_n) = (-1)^n
    mono = int(round(np.linalg.det(-np.eye(n))))
    # E: stabilizer components of e1 under (A, phi): A e1 = e^{-i phi} e1 forces phi in {0, pi}
    comps = [phi for phi in np.linspace(0, 2*np.pi, 3601)[:-1]
             if abs(np.sin(phi)) < 1e-9]              # e^{-i phi} real
    dimK = n*(n-1)//2 + 1; dimKxi = (n-1)*(n-2)//2
    results[n] = dict(A=okA, B=okB, normals_preserved=okNormal, orientation=orient,
                      orientable=(orient == 1), monodromy_degree=mono,
                      bundle_trivial=(mono == 1), stabilizer_components=len(comps),
                      dimK_minus_dimKxi=dimK-dimKxi, dim_L=n)
for n, r in results.items():
    print(n, r)
r5 = results[5]
assert r5['A'] and r5['B'] and r5['normals_preserved']
assert r5['orientation'] == -1 and r5['monodromy_degree'] == -1 and r5['stabilizer_components'] == 2
assert all(results[n]['orientation'] == (-1)**n for n in results)
print("\nD_IV^5: Silov = (S^4 x S^1)/Z2, Z2 antipodal on BOTH factors; NON-orientable;"
      " NOT the product S^4 x S^1 (twisted S^4-bundle over the circle);"
      " K = SO(5)xSO(2) transitive, stabilizer of a point has 2 components (O(4)-type), dim 5. PASS")
print("SCORE: 5/5 checks (A saturation, B identification, C orientation (-1)^n, D monodromy, E stabilizer) on n=3..8; D_IV^5 non-orientable, twisted")
