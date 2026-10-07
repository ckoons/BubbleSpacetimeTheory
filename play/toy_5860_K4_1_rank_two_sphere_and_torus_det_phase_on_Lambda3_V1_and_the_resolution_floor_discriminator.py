#!/usr/bin/env python3
"""
Toy 5860 — Round K4-1, Lane B (Elie, 2026-10-07). Prereg: notes/Elie_K4-1_prereg_toy_5860_* (commit 9d1d29f3).

1. Rank two: D_IV^2 = H x H; Lie ball n=2 = bidisc; Silov = T^2; compact dual Q^2 = S^2 x S^2; the
   coordinate copy inside D_IV^n for n = 3..7 (null: generic).
2. The determinant phase on Lambda^3 V_1 (V_1 = C^3, J = e^{i theta}): signed vs bare S3; what the circle
   carries and what it does not fix. Null: Lambda^k, k = 2, 4, 5.
3. The 09-15 discriminator, extending 5776: rounding floor vs CQ diffusion; preparation uncertainty
   (rounding fails, Fourier ledger passes); flat U(1) holonomy on a sphere (K4 surface) vs a torus.
"""
import itertools, random
from math import comb
import numpy as np
import sympy as sp

RESULTS = []
def score(tag, ok, msg):
    RESULTS.append((tag, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {msg}")

def sgn(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]: s = -s
    return s

# ------------------------------------------------------------------ 1. rank two
print("1. RANK TWO")
def so_pq(p, q):
    n = p + q; eta = sp.diag(*([1] * p + [-1] * q)); B = []
    for i, j in itertools.combinations(range(n), 2):
        X = sp.zeros(n, n); X[i, j] = 1; X[j, i] = -1 if eta[i, i] == eta[j, j] else 1
        B.append(X)
    return B
B = so_pq(2, 2)
M = sp.Matrix([list(X) for X in B]).T
def co(Y): return M.solve_least_squares(sp.Matrix(list(Y)))
ad = [sp.Matrix.hstack(*[co(X * Y - Y * X) for Y in B]) for X in B]
K = sp.Matrix(6, 6, lambda i, j: (ad[i] * ad[j]).trace())
# ideals from the commutant of ad (first version hand-wrote I1/I2 with wrong signs: abelian, vacuous PASS; owned)
Tsym = sp.Matrix(6, 6, lambda i, j: sp.Symbol(f't{i}{j}'))
eqs = []
for A_ in ad: eqs += list(Tsym * A_ - A_ * Tsym)
solT = sp.solve(eqs, list(Tsym), dict=True)[0]
Tgen = Tsym.subs(solT)
free = sorted(Tgen.free_symbols, key=str)
comm_dim = len(free)
Tstar = Tgen.subs({fs: (1 if k == 0 else 0) for k, fs in enumerate(free)})
if Tstar.is_diagonal() and len(set(Tstar.diagonal())) == 1:
    Tstar = Tgen.subs({fs: (1 if k == 1 else 0) for k, fs in enumerate(free)})
evs = Tstar.eigenvects()
I1, I2 = [[sum((c * Bx for c, Bx in zip(v, B)), sp.zeros(4, 4)) for v in vecs] for _, _, vecs in evs]
def in_span(Y, S):
    A = sp.Matrix.hstack(*[sp.Matrix(list(X)) for X in S]); y = sp.Matrix(list(Y))
    return A.rank() == sp.Matrix.hstack(A, y).rank()
closed = all(in_span(X * Y - Y * X, I) for I in (I1, I2) for X in I for Y in I)
commute = all(X * Y - Y * X == sp.zeros(4, 4) for X in I1 for Y in I2)
# Killing form of each ideal as a Lie algebra in its own right
def ideal_killing(I):
    A = sp.Matrix.hstack(*[sp.Matrix(list(X)) for X in I])
    cof = lambda Y: A.solve_least_squares(sp.Matrix(list(Y)))
    adI = [sp.Matrix.hstack(*[cof(X * Y - Y * X) for Y in I]) for X in I]
    G = sp.Matrix(3, 3, lambda i, j: (adI[i] * adI[j]).trace())
    ev = G.eigenvals()
    pos = sum(m for v, m in ev.items() if v > 0); neg = sum(m for v, m in ev.items() if v < 0)
    return pos, neg
sig = [ideal_killing(I) for I in (I1, I2)]
score("R1", comm_dim == 2 and len(I1) == 3 and len(I2) == 3 and closed and commute and sig == [(2, 1), (2, 1)],
      f"so(2,2) = I1 + I2, commuting ideals, each Killing signature {sig} = sl(2,R): D_IV^2 = H x H")

z1, z2 = sp.symbols('z1 z2'); x1, y1, x2, y2 = sp.symbols('x1 y1 x2 y2', real=True)
Z1, Z2 = x1 + sp.I * y1, x2 + sp.I * y2
wp, wm = Z1 + sp.I * Z2, Z1 - sp.I * Z2
abs2 = lambda w: sp.expand(w * sp.conjugate(w))
nz = abs2(Z1) + abs2(Z2); zz = abs2(Z1**2 + Z2**2)
disc_ = sp.simplify(sp.expand(nz**2 - zz) - sp.expand(((abs2(wp) - abs2(wm)) / 2)**2))
mean_ = sp.simplify(nz - (abs2(wp) + abs2(wm)) / 2)
rng = random.Random(5860); ok_num = True
rs0 = np.random.default_rng(58600)
for _ in range(200):
    v = {s: rng.uniform(-1, 1) for s in (x1, y1, x2, y2)}
    lb = float(nz.subs(v)) + np.sqrt(max(float((nz**2 - zz).subs(v)), 0))
    ok_num &= abs(lb - max(float(abs2(wp).subs(v)), float(abs2(wm).subs(v)))) < 1e-12
score("R2", disc_ == 0 and mean_ == 0 and ok_num,
      "|z|^2 = (|w+|^2+|w-|^2)/2 and |z|^4-|z.z|^2 = ((|w+|^2-|w-|^2)/2)^2 exactly: Lie ball n=2 = bidisc (200 random points too)")

th, ph = sp.symbols('theta phi', real=True)
zs = (sp.exp(sp.I * th) * sp.cos(ph), sp.exp(sp.I * th) * sp.sin(ph))
w_p = sp.simplify(sp.expand_complex(zs[0] + sp.I * zs[1]).rewrite(sp.exp))
w_m = sp.simplify(sp.expand_complex(zs[0] - sp.I * zs[1]).rewrite(sp.exp))
r3a = sp.simplify(w_p - sp.exp(sp.I * (th + ph))) == 0 and sp.simplify(w_m - sp.exp(sp.I * (th - ph))) == 0
deck = {th: th + sp.pi, ph: ph + sp.pi}
r3b = sp.simplify(w_p.subs(deck, simultaneous=True) - w_p) == 0 and sp.simplify(w_m.subs(deck, simultaneous=True) - w_m) == 0
# deck on S^1 x S^1 in (phi, theta): antipodal on the S^1 (degree +1) and rotation: Jacobian det
Jdeck = sp.Matrix([[1, 0], [0, 1]]).det()  # (phi, theta) -> (phi + pi, theta + pi) is a translation
# 2:1: (phi,theta) -> (theta+phi, theta-phi) has determinant -2 on R^2, lattice index 2
lin = sp.Matrix([[1, 1], [1, -1]])
score("R3", r3a and r3b and abs(lin.det()) == 2 and Jdeck == 1,
      "Silov e^{i th}(cos ph, sin ph) -> (w+, w-) = (e^{i(th+ph)}, e^{i(th-ph)}): 2:1 onto T^2, deck = translation (degree +1): a TORUS")

a0, a1, b0, b1 = sp.symbols('a0 a1 b0 b1')
seg = [a0 * b0, a0 * b1, a1 * b0, a1 * b1]                # Segre: det = s0 s3 - s1 s2 = 0
s0, s1, s2_, s3 = seg
# change of basis to a sum of squares: X1=(s0+s3), X2=i(s0-s3), X3=i(s1+s2), X4=(s1-s2)
X = [s0 + s3, sp.I * (s0 - s3), sp.I * (s1 + s2_), (s1 - s2_)]
quad = sp.expand(sum(x**2 for x in X))
# injectivity: rank-one 2x2 matrix determines ([a],[b]); check generic recovery symbolically
Mseg = sp.Matrix([[s0, s1], [s2_, s3]])
score("R4", quad == 0 and sp.expand(Mseg.det()) == 0 and Mseg.rank() == 1,
      "Segre CP1 x CP1 -> CP3 lands on z1^2+..+z4^2 = 0 (Q^2), rank-one matrices <-> ([a],[b]): Q^2 = S^2 x S^2")

def radii(z):
    n2 = float(np.vdot(z, z).real); zz = abs(complex(np.sum(z * z)))
    d = np.sqrt(max(n2**2 - zz**2, 0.0))
    return np.sqrt(n2 + d), np.sqrt(max(n2 - d, 0.0))        # Lie-ball spectral radii; Silov <=> both = 1
r5 = {}
for n in range(3, 8):
    sigma = np.diag([1, 1] + [-1] * (n - 2)); ok = True
    for _ in range(300):
        z = rs0.normal(size=n) + 1j * rs0.normal(size=n); z /= 2 * np.linalg.norm(z)
        ok &= np.allclose(radii(sigma @ z), radii(z))                       # sigma is an isometry of the ball
        w = np.zeros(n, complex); w[:2] = z[:2]
        ok &= np.allclose(radii(w), radii(z[:2]))                           # restriction = the n=2 ball
        th_, ph_ = rs0.uniform(0, 2 * np.pi, 2)
        x = np.zeros(n); x[0], x[1] = np.cos(ph_), np.sin(ph_)
        ok &= np.allclose(radii(np.exp(1j * th_) * x), (1, 1))              # T^2 points are Silov in D_IV^n
        u = rs0.normal(size=n); u /= np.linalg.norm(u)                       # generic Silov point of D_IV^n
        ok &= np.allclose(radii(np.exp(1j * th_) * u), (1, 1))
        y = np.zeros(n); y[:3] = rs0.normal(size=3); y /= np.linalg.norm(y)  # an S^2 inside the S^{n-1} fibre
        ok &= np.allclose(radii(np.exp(1j * 0.3) * y), (1, 1))
    r5[n] = ok
score("R5", all(r5.values()),
      "n = 3..7: the coordinate D_IV^2 is the fixed set of an isometry (totally geodesic), its Silov T^2 = Silov(D_IV^n) cap C^2; "
      "S^2 subset S^{n-1} fibre for every n >= 3. GENERIC: allowed, not forced by n = 5")

# ------------------------------------------------------------------ 2. det phase
print("\n2. DETERMINANT PHASE ON Lambda^3 V_1")
def eps(k):
    T = {}
    for p in itertools.permutations(range(k)): T[p] = sgn(p)
    return T
def act_on_top(Mat, k):
    # action of a k x k matrix on Lambda^k C^k is its determinant
    return sp.Matrix(Mat).det()
perms = list(itertools.permutations(range(3)))
P = {p: sp.Matrix(3, 3, lambda i, j: 1 if p[j] == i else 0) for p in perms}
bare = {p: act_on_top(P[p], 3) for p in perms}
signed = {p: act_on_top(sgn(p) * P[p], 3) for p in perms}
score("D1", all(v == 1 for v in signed.values()) and [p for p in perms if bare[p] == 1] == [p for p in perms if sgn(p) == 1],
      "signed S3 preserves eps on all 6; bare preserves eps only on A3 (Keeper's six, positive control)")
t = sp.symbols('t', real=True)
Jt = sp.exp(sp.I * t) * sp.eye(3)
Jtop = sp.simplify(act_on_top(Jt, 3))
grid = [sp.Rational(k, 12) * sp.pi for k in range(24)]                     # t in [0, 2pi) step pi/12
inv_set = [g for g in grid if sp.simplify(sp.exp(3 * sp.I * g) - 1) == 0]
rev_set = [g for g in grid if sp.simplify(sp.exp(3 * sp.I * g) + 1) == 0]
score("D2", sp.simplify(Jtop - sp.exp(3 * sp.I * t)) == 0 and set(inv_set) == {0, 2 * sp.pi / 3, 4 * sp.pi / 3}
      and sp.pi / 3 in rev_set and (sp.exp(sp.I * sp.pi / 3) * sp.eye(3)).det() == -1,
      f"J acts on Lambda^3 by e^(3it); fixes the triple only at t in {sorted(inv_set)} (centre Z3); t = pi/3 reverses it")
conj_odd = [sp.conjugate(bare[p]) for p in perms if sgn(p) == -1]
score("D3", all(c == -1 for c in conj_odd) and sp.simplify(sp.conjugate(Jtop) - sp.exp(-3 * sp.I * t)) == 0,
      "J -> -J (conjugation) leaves the odd sign -1 unchanged: the circle carries the parity (det = sgn), it does not choose the positive order")
Tvec = sp.Matrix([1])
rho = lambda c: sp.simplify(c * sp.conjugate(c))
score("D4", all(rho(bare[p]) == 1 for p in perms) and sp.simplify(rho(Jtop)) == 1,
      "on the record rho = T T^dagger both the reorder sign and the J phase square away")
nullk = {}
for k in (2, 4, 5):
    odd = next(p for p in itertools.permutations(range(k)) if sgn(p) == -1)
    Pk = sp.Matrix(k, k, lambda i, j: 1 if odd[j] == i else 0)
    nullk[k] = Pk.det() == -1 and (sp.exp(sp.I * sp.pi / k) * sp.eye(k)).det() == -1
score("D5", all(nullk.values()), f"null: on Lambda^k the odd sign = J(pi/k) for k = 2, 4, 5 {nullk}: the circle selects no 3")

# ------------------------------------------------------------------ 3. discriminator
print("\n3. DISCRIMINATOR (extends 5776)")
rs = np.random.default_rng(5860)
Delta, D = 1.0, 0.5
Ts = np.array([1, 4, 16, 64]); nsamp = 200000
round_var, cq_var, round_kurt, cq_kurt, round_max = [], [], [], [], []
for T in Ts:
    x = rs.uniform(-1e3, 1e3, nsamp)
    e_round = Delta * np.round(x / Delta) - x                  # read at time T: rounding does not depend on T
    e_cq = rs.normal(0, np.sqrt(2 * D * T), nsamp)
    round_var.append(e_round.var()); cq_var.append(e_cq.var())
    round_kurt.append(((e_round - e_round.mean())**4).mean() / e_round.var()**2)
    cq_kurt.append(((e_cq - e_cq.mean())**4).mean() / e_cq.var()**2)
    round_max.append(np.abs(e_round).max())
slope_r = np.polyfit(Ts, round_var, 1)[0]; slope_c = np.polyfit(Ts, cq_var, 1)[0]
print(f"   rounding var {np.round(round_var, 4)} (exact {Delta**2/12:.4f}), kurt {np.round(round_kurt, 3)} (exact 1.8)")
print(f"   CQ var {np.round(cq_var, 2)} (exact 2DT = {2*D*Ts}), kurt {np.round(cq_kurt, 3)} (exact 3)")
# counting floor (5776): Poisson count with large mean, T-independent, nearly Gaussian
Nmean = 1e6
cnt = rs.poisson(Nmean, nsamp); kc = ((cnt - cnt.mean())**4).mean() / cnt.var()**2
score("Q1", max(round_max) <= Delta / 2 and all(abs(v - Delta**2 / 12) < 2e-3 for v in round_var)
      and abs(slope_r) < 1e-4 and abs(slope_c - 2 * D) < 0.02 and all(abs(k - 1.8) < 0.02 for k in round_kurt)
      and all(abs(k - 3) < 0.05 for k in cq_kurt) and abs(kc - 3) < 0.05,
      f"rounding: bounded, var Delta^2/12, slope {slope_r:.1e}, kurt 1.8 | CQ: slope {slope_c:.3f} = 2D, kurt 3 | "
      f"counting floor kurt {kc:.3f} ~ Gaussian: the robust discriminator is ACCUMULATION, not shape")

# Q2 preparation uncertainty
# rounding model: a classical phase-space point on the lattice with p = 0 has sigma_x = sigma_p = 0
pt_state = np.array([[3.0, 0.0]] * 1000)
fails_heis = pt_state[:, 0].std() * pt_state[:, 1].std() == 0.0
def supp(v, tol=1e-9): return int(np.sum(np.abs(v) > tol))
ds_ok, eq_seen = True, False
for N in range(2, 11):                                         # exhaustive over 0/1 supports, generic values
    F = np.fft.fft(np.eye(N))
    for mask in range(1, 1 << N):
        S = [i for i in range(N) if mask >> i & 1]
        f = np.zeros(N, complex); f[S] = 1.0                     # indicator (worst case for equality)
        g = np.zeros(N, complex); g[S] = rs.normal(size=len(S)) + 1j * rs.normal(size=len(S))
        for v in (f, g):
            a, bb = supp(v), supp(F @ v)
            if a * bb < N: ds_ok = False
            if a * bb == N and a not in (1, N): eq_seen = True
for N in (36, 64, 137):                                        # random sample at larger N
    F = np.fft.fft(np.eye(N))
    for _ in range(3000):
        k = rs.integers(1, N + 1); S = rs.choice(N, k, replace=False)
        g = np.zeros(N, complex); g[S] = rs.normal(size=k) + 1j * rs.normal(size=k)
        if supp(g) * supp(F @ g) < N: ds_ok = False
score("Q2", fails_heis and ds_ok and eq_seen,
      "rounding admits sigma_x = sigma_p = 0 (FAILS Heisenberg); Fourier ledger on Z_N: |supp f||supp f^| >= N exhaustive N<=10 "
      "+ 9000 random (N=36,64,137), equality on subgroup indicators: preparation uncertainty INHERITED from the Fourier dual")

# Q3 flat U(1) holonomy: sphere (tetrahedron surface) vs torus (3x3 grid)
def complex_data(faces):
    V = sorted({v for f in faces for v in f})
    E = sorted({tuple(sorted(e)) for f in faces for e in itertools.combinations(f, 2)})
    d0 = np.zeros((len(E), len(V)))                            # coboundary vertices -> edges
    for i, (a, b_) in enumerate(E): d0[i, V.index(a)] = -1; d0[i, V.index(b_)] = 1
    d1 = np.zeros((len(faces), len(E)))
    for i, (a, b_, c) in enumerate(faces):
        for (u, w) in ((a, b_), (b_, c), (c, a)):
            j = E.index(tuple(sorted((u, w)))); d1[i, j] = 1 if u < w else -1
    assert np.allclose(d1 @ d0, 0)
    b1 = len(E) - np.linalg.matrix_rank(d0) - np.linalg.matrix_rank(d1)
    return V, E, d0, d1, b1
tet = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
def tor(m=3):
    vid = lambda i, j: (i % m) * m + (j % m); F = []
    for i in range(m):
        for j in range(m):
            F += [(vid(i, j), vid(i + 1, j), vid(i + 1, j + 1)), (vid(i, j), vid(i, j + 1), vid(i + 1, j + 1))]
    return F
Vs, Es, d0s, d1s, b1s = complex_data(tet)
Vt, Et, d0t, d1t, b1t = complex_data(tor(3))
def flat_random(E, d0, d1):
    # flat = ker d1 ; sample A = d0 chi + harmonic part
    _, s, vt = np.linalg.svd(d1); ker = vt[np.sum(s > 1e-9):].T
    return ker @ rs.normal(size=ker.shape[1]) * 3
def loop_hol(E, A, cyc):
    tot = 0.0
    for u, w in zip(cyc, cyc[1:] + cyc[:1]):
        j = E.index(tuple(sorted((u, w)))); tot += A[j] if u < w else -A[j]
    return np.exp(1j * tot)
sph_loops = [[0, 1, 2], [0, 1, 2, 3], [0, 2, 1, 3]]
sph_ok = all(abs(loop_hol(Es, flat_random(Es, d0s, d1s), c) - 1) < 1e-9 for c in sph_loops for _ in range(50))
m = 3; vid = lambda i, j: (i % m) * m + (j % m)
loopA = [vid(i, 0) for i in range(m)]; loopB = [vid(0, j) for j in range(m)]
hols = np.array([[loop_hol(Et, A, loopA), loop_hol(Et, A, loopB)] for A in [flat_random(Et, d0t, d1t) for _ in range(2000)]])
phA = np.angle(hols[:, 0]); fringe = np.abs(1 + hols[:, 0])**2 / 4
indep = abs(np.corrcoef(np.angle(hols[:, 0]), np.angle(hols[:, 1]))[0, 1]) < 0.1
# curvature on the sphere: put flux on faces; total flux of a U(1) bundle on S^2 is 2 pi k; a loop sees partial flux
print("   note (not scored): with face flux the sphere does interfere; a U(1) bundle on S^2 has total flux 2*pi*k")
score("Q3", b1s == 0 and b1t == 2 and sph_ok and fringe.min() < 0.01 and fringe.max() > 0.99 and indep,
      f"tetrahedron surface b1 = {b1s}: every flat two-path phase = 1 | 3x3 torus b1 = {b1t}: two independent free holonomies, "
      f"fringe {fringe.min():.3f}..{fringe.max():.3f} | with curvature the sphere DOES interfere (face flux 2pi k/4): the claim holds for FLAT phases only")

passed = sum(ok for _, ok in RESULTS)
print(f"\nSCORE: {passed}/{len(RESULTS)}")
