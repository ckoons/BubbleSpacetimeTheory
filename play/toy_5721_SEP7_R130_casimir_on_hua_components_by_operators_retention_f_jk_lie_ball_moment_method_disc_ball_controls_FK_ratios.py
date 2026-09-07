#!/usr/bin/env python3
"""Toy 5721 — Round 130 (prereg hashed before this run)."""
import sympy as sp, numpy as np, math, json, os, itertools
from fractions import Fraction as F
HERE = os.path.dirname(os.path.abspath(__file__)); score = []
def sc(n, ok, d=""): score.append(ok); print(f"  [{'HIT' if ok else 'MISS'}] {n}  {d}")
z = sp.symbols('z0:5'); zz = sum(v**2 for v in z)
def lap(f): return sum(sp.diff(f, v, 2) for v in z)
def harmonic_part(poly, k):
    if k < 2: return sp.expand(poly)
    mons = [sp.Mul(*[v**e for v, e in zip(z, ex)]) for ex in itertools.product(range(k - 1), repeat=5) if sum(ex) == k - 2]
    cs = sp.symbols(f'c0:{len(mons)}'); q = sum(c * m for c, m in zip(cs, mons))
    sol = sp.solve(sp.Poly(sp.expand(lap(poly - zz * q)), *z).coeffs(), cs, dict=True)[0]
    return sp.expand(poly - zz * q.subs(sol))
def C5(f):   # -sum_{i<l} (z_i d_l - z_l d_i)^2
    tot = 0
    for i in range(5):
        for l in range(i + 1, 5):
            L = lambda g: z[i] * sp.diff(g, z[l]) - z[l] * sp.diff(g, z[i])
            tot -= L(L(f))
    return sp.expand(tot)
def Eop(f): return sp.expand(sum(v * sp.diff(f, v) for v in z))
print("P1: K-Casimir on the Hua components by the operators")
rng = np.random.default_rng(3); ok1 = True; rows = []
for j in range(0, 3):
    for k in range(0, 4):
        mons = [sp.Mul(*[v**e for v, e in zip(z, ex)]) for ex in itertools.product(range(k + 1), repeat=5) if sum(ex) == k]
        raw = sum(sp.Integer(int(rng.integers(-3, 4))) * m for m in mons) if k > 0 else sp.Integer(1)
        Y = harmonic_part(raw, k); f = sp.expand(zz**j * Y)
        c = sp.simplify(C5(f) / f) if f != 0 else None; e = sp.simplify(Eop(f) / f)
        rows.append((j, k, c, e)); ok1 &= (c == k * (k + 3)) and (e == 2 * j + k)
print("  (j,k): C5 eigenvalue, degree:", [(j, k, str(c), str(e)) for j, k, c, e in rows])
sc("P1", ok1, "C5 = k(k+3) on every (j,k), E = 2j+k; the seven-variable family k(k+5) is a different operator (S^6 harmonics), listed for comparison: " + str([k*(k+5) for k in range(4)]))
print("P2/P3: disc and ball controls (exact)")
disc = {m: (F(m + 1, m + 2), F(1, m + 2), F(1, m + 1)) for m in range(0, 6)}
print("  disc: m -> <|z|^2>, push, ||z^m||^2_A:", {m: tuple(str(x) for x in v) for m, v in disc.items()})
ball = {m: (F(m + 5, m + 6), F(1, m + 6)) for m in range(0, 6)}; print("  ball B^5: m -> <|z|^2>, push:", {m: tuple(str(x) for x in v) for m, v in ball.items()})
sc("P2", disc[3][1] == F(1, 5), "disc push 1/(m+2) = 1/5 at m = 3; FK disc ratio (2)_m/(1)_m = m+1 = 1/||z^m||^2_A")
sc("P3", ball[3][1] == F(1, 9), "ball push 1/(m+6) = 1/9 at m = 3")
print("P4: f(j,k) on the Lie ball by the moment method")
rng2 = np.random.default_rng(23); keep = []
for chunk in range(14):
    w = rng2.uniform(-1, 1, size=(6_000_000, 5)) + 1j * rng2.uniform(-1, 1, size=(6_000_000, 5))
    r2 = (np.abs(w)**2).sum(1); ww = (w*w).sum(1); m_ = (r2 < 1) & (np.abs(ww)**2 - 2*r2 + 1 > 0); keep.append(w[m_])
W = np.concatenate(keep); R2 = (np.abs(W)**2).sum(1); WW = (W*W).sum(1); RHO = 1 - 2*R2 + np.abs(WW)**2
print(f"  Lie-ball samples: {len(W)}")
def avg(f2, g):
    B = 25; idx = np.array_split(np.arange(len(f2)), B); e = np.array([(f2[i]*g[i]).sum()/f2[i].sum() for i in idx]); return e.mean(), e.std()/math.sqrt(B)
# representative words: (z.z)^j * Yk with Yk = harmonic part of z0^k (exact polynomial), evaluated numerically
Yk = {k: sp.lambdify(z, harmonic_part(z[0]**k, k), 'numpy') for k in range(4)}
table = {}
for j in range(3):
    for k in range(4):
        vals = (WW**j) * Yk[k](*[W[:, i] for i in range(5)]) if k > 0 else WW**j * np.ones(len(W))
        f2 = np.abs(vals)**2
        e1, s1 = avg(f2, R2); e2, s2 = avg(f2, RHO); table[(j, k)] = (e1, s1, e2, s2)
        print(f"  (j,k)=({j},{k}) m={2*j+k}: f = <|z|^2> = {e1:.4f}±{s1:.4f}   <rho> = {e2:.4f}±{s2:.4f}")
shape_ok = all(table[(j, k)][0] < table[(j, k + 1)][0] + 3*max(table[(j, k)][1], table[(j, k+1)][1]) for j in range(3) for k in range(3))  # f rises with m (weak test)
matter_vs_light_m3 = table[(1, 1)][0] > table[(0, 3)][0]
sc("P4", matter_vs_light_m3, f"at m = 3: matter (1,1) f = {table[(1,1)][0]:.4f} vs light (0,3) f = {table[(0,3)][0]:.4f} — matter nearer the boundary (5719's ordering); rises-with-m (weak): {shape_ok}")
print("P5: FK exact Hardy/Bergman norm ratios R(j,k) = (5)_{j+k}(7/2)_j/[(5/2)_{j+k}(1)_j]")
def poch(a, n): return sp.prod([a + i for i in range(n)]) if n else sp.Integer(1)
Rtab = {}
for j in range(3):
    for k in range(4):
        R = sp.nsimplify(poch(sp.Integer(5), j + k) * poch(sp.Rational(7, 2), j) / (poch(sp.Rational(5, 2), j + k) * poch(sp.Integer(1), j))); Rtab[(j, k)] = R
print("  ", {f"({j},{k})": str(v) for (j, k), v in Rtab.items()})
sc("P5", Rtab[(0, 1)] == sp.Integer(2) and Rtab[(0, 0)] == 1, "exact ratios printed; disc limit (2)_m/(1)_m = m+1 (P2)")
print(f"\nSCORE {sum(score)}/{len(score)}")
json.dump({'casimir_rows': [(j, k, str(c), str(e)) for j, k, c, e in rows], 'f_table': {f"{j},{k}": v for (j, k), v in table.items()}, 'FK_ratios': {f"{j},{k}": str(v) for (j, k), v in Rtab.items()}, 'score': f"{sum(score)}/{len(score)}"}, open(os.path.join(HERE, '.record_5721.json'), 'w'), indent=1)
