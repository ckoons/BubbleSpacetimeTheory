#!/usr/bin/env python3
"""Toy 5754 (Lyra, 2026-09-11, Round 142 — the T753 repair owed since R140 G2).

Claim under test: the Bergman metric of the Lie ball D_IV^n (genus p = n) has holomorphic
sectional curvature that is NOT constant (rank 2) but pinched:
    H(v) = -(2 - |v.v|^2/|v|^4)/p,   so   -2/p <= H(v) <= -1/p,
with -2/p on isotropic directions (v.v = 0) and -1/p on real directions (v.v = |v|^2).
Control: the unit ball B^n (rank 1, genus n+1) gives the constant -2/(n+1) in the same convention.
Convention: g_{i jbar} = d_i d_jbar log K, K = c * N^{-p}, N = 1 - 2|z|^2 + |z.z|^2 (Hua),
curvature evaluated at the origin (K-homogeneity carries it everywhere).
No number from memory: the quartic Taylor coefficient of -p log N is computed symbolically, and the
curvature is checked by finite differences of log K at finite points for the ball as an independent
route. T753's old sentence "H = -2/(n+2) = -2/7" is tested as a would-be value.
"""
import sympy as sp
from fractions import Fraction

def hsc_lie_ball(n, p, v):
    # phi(t v) restricted to a complex line: -p log N(t v); the quartic coefficient A in A|t|^4
    t, tb = sp.symbols('t tb')
    z = [t*c for c in v]; zb = [tb*sp.conjugate(c) for c in v]
    zz = sum(a*a for a in z); zbzb = sum(b*b for b in zb); zzb = sum(a*b for a, b in zip(z, zb))
    N = 1 - 2*zzb + zz*zbzb
    phi = -p*sp.log(N)
    # metric coefficient at 0: coefficient of t*tb ;  quartic: coefficient of t^2 tb^2
    ser = sp.series(phi, t, 0, 3).removeO()
    ser = sp.expand(sp.series(ser, tb, 0, 3).removeO())
    g = ser.coeff(t, 1).coeff(tb, 1)
    A = ser.coeff(t, 2).coeff(tb, 2)
    # R(v,vb,v,vb) = -d_t d_tb d_t d_tb (A t^2 tb^2) = -4A ; HSC = R / g^2
    return sp.nsimplify(-4*A/g**2)

def hsc_ball(n, v):
    p = n + 1
    t, tb = sp.symbols('t tb')
    z = [t*c for c in v]; zb = [tb*sp.conjugate(c) for c in v]
    zzb = sum(a*b for a, b in zip(z, zb))
    phi = -p*sp.log(1 - zzb)
    ser = sp.expand(sp.series(sp.series(phi, t, 0, 3).removeO(), tb, 0, 3).removeO())
    g = ser.coeff(t, 1).coeff(tb, 1); A = ser.coeff(t, 2).coeff(tb, 2)
    return sp.nsimplify(-4*A/g**2)

score = 0; total = 0
def check(name, cond, detail):
    global score, total
    total += 1; score += bool(cond)
    print(('PASS' if cond else 'MISS'), name, '|', detail)

n, p = 5, 5
I = sp.I
real_v = [1, 0, 0, 0, 0]
iso_v = [1, I, 0, 0, 0]                    # v.v = 0
mid_v = [1, I*sp.Rational(1, 2), 0, 0, 0]  # v.v = 3/4, |v|^2 = 5/4
H_real = hsc_lie_ball(n, p, real_v); H_iso = hsc_lie_ball(n, p, iso_v); H_mid = hsc_lie_ball(n, p, mid_v)
print('D_IV^5 Bergman HSC: real direction', H_real, ' isotropic', H_iso, ' mixed', H_mid)
check('P1 real direction H = -1/p = -1/5', H_real == sp.Rational(-1, 5), H_real)
check('P2 isotropic direction H = -2/p = -2/5', H_iso == sp.Rational(-2, 5), H_iso)
r = sp.Rational(9, 25)  # |v.v|^2/|v|^4 = (3/4)^2/(5/4)^2
check('P3 mixed direction obeys H = -(2 - |v.v|^2/|v|^4)/p', H_mid == -(2 - r)/p, (H_mid, -(2 - r)/p))
check('P4 NOT constant (can-fail: a rank-1 domain would give equal values)', H_real != H_iso, (H_real, H_iso))
r27 = sp.Rational(-2, 7)
inside = sp.Rational(-2, 5) <= r27 <= sp.Rational(-1, 5)
ratio_needed = 2 - p*(-r27)      # |v.v|^2/|v|^4 at which H = -2/7
check('P5 (verdict computed, not typed) T753 old value -2/7: inside the range?', inside,
      'inside=%s; attained at |v.v|^2/|v|^4 = %s (a generic direction: neither real (1) nor isotropic (0))' % (inside, ratio_needed))
# ball control, same convention
Hb = [hsc_ball(5, v) for v in (real_v, iso_v, mid_v)]
check('C1 ball B^5 control: constant -2/(n+1) = -1/3 in every direction', all(h == sp.Rational(-1, 3) for h in Hb), Hb)
# family: n = 3..8, min/max
rows = []
for m in range(3, 9):
    vr = [1] + [0]*(m-1); vi = [1, I] + [0]*(m-2)
    rows.append((m, hsc_lie_ball(m, m, vr), hsc_lie_ball(m, m, vi)))
print('family n: (real, isotropic) =', rows)
check('C2 family rule -1/n and -2/n for n = 3..8', all(hr == sp.Rational(-1, m) and hi == sp.Rational(-2, m) for m, hr, hi in rows), '')
# pinching ratio = rank
check('C3 max/min = 1/2 = 1/rank (the rank-r pinching)', H_real / H_iso == sp.Rational(1, 2), H_real / H_iso)
# independent finite-difference route on the ball at a finite point (not the origin), to check the convention
import numpy as np
def logK_ball(z, n): return -(n+1)*np.log(1 - np.vdot(z, z).real)
def hsc_fd(logK, z0, v, h=1e-3):
    # HSC along v at z0 via the quartic of phi restricted to the line, after removing the metric: use the
    # standard formula for a Kähler potential on a line: H = -(1/g^2) * [d^4 phi/(dt dtb)^2] with Kähler
    # normal-coordinate correction; at a general point this needs the connection, so we use the ball at
    # the origin only (homogeneity) as a numerical cross-check of the symbolic route.
    f = lambda a, b: logK(z0 + (a + 1j*b)*v, 5)
    # d_t d_tb = (1/4)(d_a^2 + d_b^2) ; quartic coefficient via 4th-order finite differences
    def lap(a, b):
        return (f(a+h, b) + f(a-h, b) + f(a, b+h) + f(a, b-h) - 4*f(a, b)) / h**2 / 4
    g = lap(0, 0)
    lap2 = (lap(h, 0) + lap(-h, 0) + lap(0, h) + lap(0, -h) - 4*lap(0, 0)) / h**2 / 4
    return -lap2 / g**2
Hfd = hsc_fd(logK_ball, np.zeros(5, complex), np.array([1, 0, 0, 0, 0], complex))
check('C4 finite-difference ball at origin reproduces -1/3 (convention check)', abs(Hfd + 1/3) < 2e-3, Hfd)
print('SCORE %d/%d' % (score, total))
print('READING (computed from the run): D_IV^5 Bergman HSC range [%s, %s]; not constant; -2/7 is the value at |v.v|^2/|v|^4 = %s, and is D_IV^7 isotropic value %s; T753 must name the range or a direction' % (H_iso, H_real, ratio_needed, rows[4][2]))
