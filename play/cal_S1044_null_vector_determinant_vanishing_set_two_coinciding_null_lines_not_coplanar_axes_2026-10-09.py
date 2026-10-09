#!/usr/bin/env python3
"""Cal Section 1044 — the exact vanishing set of det(ε1,ε2,ε3) for commit null vectors
ε(k,s) = e^{iφ}(a + i s b)/√2. Theorem: det = 0 iff two of the three null LINES coincide,
i.e. (k,s) ~ (k',s') with k' = ±k and s' = ±s (same sign choice); three distinct null lines
in C^3 are always independent (a plane meets the quadric ε^Tε = 0 in at most two lines).
Coplanarity of the axes is irrelevant (5880 N4); opposite helicity on the same axis is independent."""
import numpy as np
rng = np.random.default_rng(1044)
def eps(k, s, phi=0.0):
    k = k/np.linalg.norm(k); a = np.cross(k, [0.3, 0.2, 0.9])
    if np.linalg.norm(a) < 1e-6: a = np.cross(k, [1, 0, 0])
    a /= np.linalg.norm(a); b = np.cross(k, a); return np.exp(1j*phi)*(a + 1j*s*b)/np.sqrt(2)
def det(*v): return abs(np.linalg.det(np.array(v).T))
score = 0; total = 0
def check(name, ok, val):
    global score, total; total += 1; score += bool(ok); print(f"  [{'PASS' if ok else 'FAIL'}] {name}: |det| = {val:.3e}")
for trial in range(50):
    k, k2 = rng.normal(size=3), rng.normal(size=3); u, v = rng.normal(size=3), rng.normal(size=3)
    phis = rng.uniform(0, 2*np.pi, 3)
    if trial == 0:
        check("same axis, same helicity -> 0", det(eps(k,1), eps(k,1,phis[0]), eps(k2,1)) < 1e-12, det(eps(k,1), eps(k,1,phis[0]), eps(k2,1)))
        check("opposite axis, opposite helicity -> 0 (same null line)", det(eps(k,1), eps(-k,-1,phis[1]), eps(k2,1)) < 1e-12, det(eps(k,1), eps(-k,-1,phis[1]), eps(k2,1)))
        check("same axis, OPPOSITE helicity -> nonzero", det(eps(k,1), eps(k,-1), eps(k2,1)) > 1e-3, det(eps(k,1), eps(k,-1), eps(k2,1)))
        check("three COPLANAR distinct axes -> nonzero (5880 N4)", det(eps(u,1), eps(v,1), eps(0.3*u+0.8*v,1)) > 1e-6, det(eps(u,1), eps(v,1), eps(0.3*u+0.8*v,1)))
    else:
        assert det(eps(k,1), eps(k,1,phis[0]), eps(k2,1)) < 1e-12 and det(eps(k,1), eps(-k,-1,phis[1]), eps(k2,1)) < 1e-12
        assert det(eps(k,1), eps(k,-1), eps(k2,1)) > 1e-6 and det(eps(u,1), eps(v,1), eps(0.3*u+0.8*v,1)) > 1e-9
check("49 further random trials of all four cases agree", True, 0.0)
# conjugation flips helicity: eps(k,s)^* ∝ eps(k,-s)
k = rng.normal(size=3); c = np.vdot(eps(k,-1), np.conj(eps(k,1)))
check("complex conjugation (the circle's ORIENTATION reversal, c) maps ε(k,s) to the ε(k,-s) line", abs(abs(c)-1) < 1e-12, abs(c))
print(f"\nSCORE: {score}/{total}")
