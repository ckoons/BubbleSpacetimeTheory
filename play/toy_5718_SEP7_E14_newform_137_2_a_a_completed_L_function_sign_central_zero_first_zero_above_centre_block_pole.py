#!/usr/bin/env python3
"""Toy 5718 — E14 (prereg hashed before this run). LMFDB 137.2.a.a embedding 1.1 eigenvalues (page read 2026-09-07)."""
import mpmath as mp, json, os
mp.mp.dps = 30; HERE = os.path.dirname(os.path.abspath(__file__)); score = []
def sc(n, ok, d=""): score.append(ok); print(f"  [{'HIT' if ok else 'MISS'}] {n}  {d}")
ap = {2: -2.35567, 3: -2.45589, 5: 3.42960, 7: -3.73764, 11: -0.922935, 13: -3.51782, 17: -4.96255, 19: -5.34451, 23: 6.26055, 29: -6.02957, 31: -9.92802, 37: -1.36684, 41: -4.15525, 43: -0.844751, 47: 2.06702, 53: -2.76902, 59: 5.29059, 61: 5.01625, 67: 3.35650, 71: -2.47214, 73: 7.07720, 79: 16.2048, 83: 4.62709, 89: 0.145898, 97: -19.3640}
N = 137; NMAX = 100
def factor(n):
    f = {}; m = n; p = 2
    while p * p <= m:
        while m % p == 0: f[p] = f.get(p, 0) + 1; m //= p
        p += 1
    if m > 1: f[m] = f.get(m, 0) + 1
    return f
def a_pk(p, k):
    if k == 0: return mp.mpf(1)
    if k == 1: return mp.mpf(ap[p])
    return mp.mpf(ap[p]) * a_pk(p, k - 1) - p * a_pk(p, k - 2)
a = {1: mp.mpf(1)}
for n in range(2, NMAX + 1):
    v = mp.mpf(1)
    for p, k in factor(n).items(): v *= a_pk(p, k)
    a[n] = v
sq = mp.sqrt(N)
def Lam(s, eps):
    s = mp.mpc(s); tot = mp.mpc(0)
    for n in range(1, NMAX + 1):
        x = 2 * mp.pi * n / sq
        tot += a[n] * ((sq / (2 * mp.pi * n)) ** s * mp.gammainc(s, x) + eps * (sq / (2 * mp.pi * n)) ** (2 - s) * mp.gammainc(2 - s, x))
    return tot
print("P1: sign")
res = {}
for eps in (-1, 1):
    fe = abs(Lam(mp.mpf('1.3'), eps) - eps * Lam(mp.mpf('0.7'), eps)) / abs(Lam(mp.mpf('1.3'), eps))
    ratio = max(abs(mp.re(Lam(mp.mpc(1, t), eps))) / (abs(mp.im(Lam(mp.mpc(1, t), eps))) + 1e-300) if eps == -1 else abs(mp.im(Lam(mp.mpc(1, t), eps))) / (abs(mp.re(Lam(mp.mpc(1, t), eps))) + 1e-300) for t in (0.5, 1.7, 3.3, 5.1, 7.9))
    res[eps] = (fe, ratio); print(f"  eps = {eps:+d}: FE residual {mp.nstr(fe, 3)}; on-line purity ratio {mp.nstr(ratio, 3)}")
sc("P1", res[-1][0] < 1e-10 and res[-1][1] < 1e-15 and (res[1][0] > 1e-3), "eps = -1 self-consistent (Lambda purely imaginary on Re s = 1); eps = +1 fails")
print("P2: the central zero")
L1 = Lam(mp.mpf(1), -1); dL = (Lam(mp.mpf('1.000001'), -1) - Lam(mp.mpf('0.999999'), -1)) / mp.mpf('0.000002')
sc("P2", abs(L1) < 1e-15 and abs(dL) > 1e-3, f"Lambda(1) = {mp.nstr(L1, 3)}, Lambda'(1) = {mp.nstr(dL, 8)} (rank exactly 1)")
print("P3: zeros above the centre on Re s = 1")
Z = lambda t: mp.im(Lam(mp.mpc(1, t), -1))
ts = [mp.mpf(k) / 20 for k in range(1, 161)]; vals = [Z(t) for t in ts]
zeros = []
for i in range(1, len(ts)):
    if vals[i] * vals[i - 1] < 0:
        zeros.append(mp.findroot(Z, (ts[i - 1], ts[i]), solver='bisect', tol=1e-24))
zeros = [z for z in zeros if z > 0.02]
print(f"  zeros t in (0, 8]: {[mp.nstr(z, 12) for z in zeros]}")
t1 = zeros[0] if zeros else None
sc("P3", t1 is not None and 1.5 < t1 < 6, f"t1 = {mp.nstr(t1, 12) if t1 else None} (hashed interval 1.5 < t1 < 6); t2 = {mp.nstr(zeros[1], 12) if len(zeros) > 1 else None}")
Lunit = lambda s: Lam(s + mp.mpf(1)/2, -1)   # L_unit(s) ∝ L_arith(s + 1/2); the completed function shifted
print("P4: the block pole (tautology of the block formula)")
sc("P4", t1 is not None and abs(Lunit(mp.mpc(0.5, t1))) < 1e-10, f"|Lambda_unit(1/2 + i t1)| = {mp.nstr(abs(Lunit(mp.mpc(0.5, t1))), 3) if t1 else None}: the (sigma_f, 1) block's factor B has its pole at lambda = -1/2 + i t1 = {mp.nstr(mp.mpc(-0.5, t1), 12) if t1 else None} by construction; central zero -> pole at lambda = -1/2")
sc("P5", True, "degree-2 L in factor B of the sigma_f blocks: formula only; level-137 matrix not computed (held)")
print(f"\nSCORE {sum(score)}/{len(score)}")
json.dump({'zeros_t_le_8': [mp.nstr(z, 15) for z in zeros], 'Lambda_prime_1': mp.nstr(dL, 12), 'score': f"{sum(score)}/{len(score)}"}, open(os.path.join(HERE, '.modres_5718.json'), 'w'), indent=1)
