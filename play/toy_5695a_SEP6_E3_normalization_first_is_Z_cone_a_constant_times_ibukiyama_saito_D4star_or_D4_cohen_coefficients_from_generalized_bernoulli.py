#!/usr/bin/env python3
"""Toy 5695a — E3 step 0, 'state the normalization first' (Keeper handoff): is Z_cone(s) = sum r*(N) N^-s a CONSTANT
multiple of Ibukiyama–Saito's D*_4(s,1) = sum_d H(2,d,1) d^-s (coefficient at d = d_K f^2: C_4 d_K^{3/2} L(2,chi_K) c_K(f),
c_K from zeta(2s)zeta(2s-3)/L(2s-1,chi_K)), or of D_4(s,1) = sum H(2,4N,1) N^-s, or neither? r*(N) from toy 5693 (exact).
L(2,chi_K) for real even chi via generalized Bernoulli: L(2,chi) = pi^2 B_{2,chi} / d^{3/2}, B_{2,chi} = d sum chi(a) B_2(a/d)."""
import json, math, os
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__))
rs = {int(k): Fraction(v) for k, v in json.load(open(os.path.join(HERE, '.siegel_5693.json')))['rstar'].items()}
def squarefree_core(N):
    m = N; core = 1; p = 2
    while p * p <= m:
        e = 0
        while m % p == 0: m //= p; e += 1
        if e % 2: core *= p
        p += 1
    return core * m
def kron(d, n):   # Kronecker symbol (d/n), d a fundamental discriminant, n >= 1
    if n == 0: return 0
    res = 1; m = n
    while m % 2 == 0:
        m //= 2
        if d % 2 == 0: return 0
        res *= 1 if d % 8 in (1, 7) else -1
    if m == 1: return res
    # Jacobi symbol (d/m) for odd m
    a = d % m; j = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if m % 8 in (3, 5): j = -j
        a, m = m, a
        if a % 4 == 3 and m % 4 == 3: j = -j
        a %= m
    return res * j if m == 1 else 0
def L2(dK):        # L(2, chi_{dK}) for dK > 0 fundamental (dK = 1: zeta(2)); returns (rational, ) with L = pi^2 * rational / dK^{3/2}
    if dK == 1: return Fraction(1, 6)          # zeta(2) = pi^2/6 = pi^2 * (1/6) / 1
    B2 = sum(kron(dK, a) * (Fraction(a, dK) ** 2 - Fraction(a, dK) + Fraction(1, 6)) for a in range(1, dK + 1)) * dK
    return B2
def cK(dK, f):
    out = Fraction(1); m = f; p = 2
    while m > 1:
        if m % p == 0:
            a = 0
            while m % p == 0: m //= p; a += 1
            chi = kron(dK, p); s1 = sum(p ** (3 * j) for j in range(a + 1)); s0 = sum(p ** (3 * j) for j in range(a))
            out *= s1 - chi * p * s0
        p += 1
    return out
def H(d):          # coefficient of D*_4 at d, divided by C_4: dK^{3/2} L(2,chi_K) cK(f) = pi^2 * B * cK(f)  (the dK^{3/2} cancels!)
    if d % 4 in (2, 3): return None
    core = squarefree_core(d); dK = core if core % 4 == 1 else 4 * core
    if d % dK: return None
    q = d // dK; f = math.isqrt(q)
    if f * f != q: return None
    return L2(dK) * cK(dK, f)      # times pi^2
print("N  r*(N)      H(N)/pi^2   H(4N)/pi^2   r*/H(N)     r*/H(4N)")
r1 = {}; r4 = {}
for N in range(1, 61):
    hN = H(N); h4 = H(4 * N)
    r1[N] = (rs[N] / hN) if hN else None; r4[N] = rs[N] / h4
    print(f"{N:2d} {str(rs[N]):>8s}  {str(hN) if hN else '   -   ':>10s}  {str(h4):>10s}   {float(r1[N]) if r1[N] is not None else float('nan'):.6f}   {float(r4[N]):.6f}")
vals4 = {N: r4[N] for N in r4}; vals1 = {N: r1[N] for N in r1 if r1[N] is not None}
print("\ndistinct r*/H(4N) values:", sorted(set(float(v) for v in vals4.values()))[:12])
print("distinct r*/H(N)  values:", sorted(set(float(v) for v in vals1.values()))[:12])
# by 2-adic class
from collections import defaultdict
byc = defaultdict(set)
for N, v in vals4.items():
    e = 0; m = N
    while m % 2 == 0: m //= 2; e += 1
    byc[(e, m % 8)].add(float(v))
print("r*/H(4N) by (ord_2 N, odd part mod 8):", {k: sorted(v) for k, v in sorted(byc.items())})
byc1 = defaultdict(set)
for N, v in vals1.items():
    e = 0; m = N
    while m % 2 == 0: m //= 2; e += 1
    byc1[(e, m % 8)].add(float(v))
print("r*/H(N) by (ord_2 N, odd part mod 8):", {k: sorted(v) for k, v in sorted(byc1.items())})
json.dump({'r_over_H4N': {N: str(v) for N, v in vals4.items()}, 'r_over_HN': {N: str(v) for N, v in vals1.items()}}, open(os.path.join(HERE, '.norm_5695a.json'), 'w'), indent=1)

# ---- primitive part: Z_cone = zeta(2s) Z_prim, so r*_prim(N) = sum_{m^2 | N} mu(m) r*(N/m^2) ----
def mobius(m):
    r = 1; p = 2; mm = m
    while p * p <= mm:
        if mm % p == 0:
            mm //= p
            if mm % p == 0: return 0
            r = -r
        p += 1
    return -r if mm > 1 else r
rp = {}
for N in range(1, 61):
    rp[N] = sum(mobius(m) * rs[N // (m * m)] for m in range(1, 8) if N % (m * m) == 0)
print("\nPRIMITIVE part r*_prim(N) vs H(N), H(4N):")
c1 = defaultdict(set); c4 = defaultdict(set)
for N in range(1, 61):
    e = 0; m = N
    while m % 2 == 0: m //= 2; e += 1
    hN = H(N); h4 = H(4 * N)
    if hN: c1[(e, m % 8)].add(float(rp[N] / hN))
    c4[(e, m % 8)].add(float(rp[N] / h4))
    if N <= 24: print(f"{N:2d} prim {str(rp[N]):>8s}  /H(N) {float(rp[N]/hN) if hN else float('nan'):.6f}  /H(4N) {float(rp[N]/h4):.6f}")
print("prim/H(N)  by (e, odd mod 8):", {k: sorted(v) for k, v in sorted(c1.items())})
print("prim/H(4N) by (e, odd mod 8):", {k: sorted(v) for k, v in sorted(c4.items())})

# ---- Siegel–Weil test: is r*(N) = a*r5(N) + b*H(2,N) (weight-5/2 Eisenstein space on Gamma_0(4) is 2-dimensional)? ----
import numpy as np
r5 = np.zeros(61, dtype=np.int64); th = np.zeros(61, dtype=np.int64)
for x in range(-7, 8):
    if x*x <= 60: th[x*x] += 1
r5 = th.copy()
for _ in range(4): r5 = np.convolve(r5, th)[:61]
Hn = {N: (H(N) if H(N) is not None else Fraction(0)) for N in range(1, 61)}
# solve with N=1,2: r*(1) = a r5(1) + b H(1); r*(2) = a r5(2) + b H(2)=a r5(2)
a = rs[2] / r5[2]; b = (rs[1] - a * r5[1]) / Hn[1]
bad = [N for N in range(1, 61) if rs[N] != a * r5[N] + b * Hn[N]]
print(f"\nSIEGEL–WEIL 2-dim fit: a = {a}, b = {b} (H in units of pi^2: b*pi^2 = {float(b)*math.pi**2:.6f}); failures N<=60: {bad}")
if not bad: print("  r*(N) = a r5(N) + b H(2,N) EXACTLY for all N <= 60: Z_cone = a * Mellin(theta^5) + b*pi^2 * D*_4")
# also the pair (H(N), H(4N)) basis
a2s = None
M = np.array([[float(Hn[1]), float(H(4))], [float(Hn[2]), float(H(8))]]); v = np.array([float(rs[1]), float(rs[2])])
try:
    c1, c2 = np.linalg.solve(M, v)
    res = max(abs(float(rs[N]) - c1*float(Hn[N]) - c2*float(H(4*N))) for N in range(1, 61))
    print(f"  (H(N), H(4N)) basis: c1 = {c1:.6f}, c2 = {c2:.6f}, max residual N<=60 = {res:.2e}")
except Exception as ex: print("  (H(N),H(4N)) basis singular:", ex)
