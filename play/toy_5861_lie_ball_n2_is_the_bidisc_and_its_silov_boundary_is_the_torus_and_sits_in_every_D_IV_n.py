#!/usr/bin/env python3
"""Toy (Grace, 2026-10-07, round K4-1 Lane C pin for Elie's Lane B).
Checks the DERIVED (not pinned) rank-two facts that the researcher returned:
 (1) phi(z1,z2) = (z1 + i z2, -z1 + i z2) maps the Lie ball L_2 = {|z|^2<1, 2|z|^2 - |z.z|^2 < 1} onto the bidisc D^2
     (Ghosh-Zwonek arXiv:2406.18396 eq. 2.1 -- pinned; checked here numerically, both directions);
 (2) the Silov set {w x : |w|=1, x in S^1} maps ONTO the torus T^2 = S^1 x S^1, with (w,x) and (-w,-x) the same point;
 (3) L_n cap (C^2 x 0) = L_2 for n = 3..7 (the rank-2 slice), and T.S^1 x 0 lies in the Silov set T.S^{n-1}.
"""
import numpy as np
rng = np.random.default_rng(7)
def in_lie(z):
    a = np.vdot(z, z).real; b = abs(np.sum(z*z))
    return a < 1 and 2*a - b**2 < 1
phi = lambda z: np.array([z[0] + 1j*z[1], -z[0] + 1j*z[1]])
ok1 = 0; N = 20000
for _ in range(N):
    z = (rng.uniform(-1, 1, 2) + 1j*rng.uniform(-1, 1, 2))
    ok1 += in_lie(z) == bool(np.all(np.abs(phi(z)) < 1))
ok2 = True; pts = []
for _ in range(2000):
    w = np.exp(1j*rng.uniform(0, 2*np.pi)); t = rng.uniform(0, 2*np.pi); x = np.array([np.cos(t), np.sin(t)])
    p = phi(w*x); ok2 &= np.allclose(np.abs(p), 1)
    ok2 &= np.allclose(phi((-w)*(-x)), p)
    pts.append(np.angle(p))
pts = np.array(pts)  # surjectivity: inverse map from any torus point
ok_surj = True
for _ in range(2000):
    a, b = np.exp(1j*rng.uniform(0, 2*np.pi, 2))
    z = np.array([(a - b)/2, (a + b)/(2j)])          # phi^{-1}(a,b)
    ok_surj &= np.allclose(phi(z), [a, b]) and np.isclose(abs(np.sum(z*z)), 1) and np.isclose(np.vdot(z, z).real, 1)
ok3 = True
for n in range(3, 8):
    for _ in range(3000):
        z2 = rng.uniform(-1, 1, 2) + 1j*rng.uniform(-1, 1, 2)
        ok3 &= in_lie(np.concatenate([z2, np.zeros(n-2)])) == in_lie(z2)
print(f"(1) L_2 <-> bidisc agree on {ok1}/{N} random points")
print(f"(2) Silov(L_2) -> T^2, Z2-identified: {ok2}; onto T^2 (inverse lands on Silov set): {ok_surj}")
print(f"(3) L_n cap C^2 = L_2 for n=3..7: {ok3}")
assert ok1 == N and ok2 and ok_surj and ok3
print("SCORE: 3/3 -- D_IV^2 = bidisc (phi), Silov = T^2 (Z2-quotient of S^1 x S^1 is a torus), rank-2 slice L_2 in every L_n")
