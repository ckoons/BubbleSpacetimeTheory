#!/usr/bin/env python3
"""Toy 5695 — E3 (T-DH). (P1) r*(N)·3840 = r5(N) for N <= 200 (chamber + BFS stabilizers as 5693). (P2) AFE for
Lambda(s) = pi^-s Gamma(s) Z5(s), Z5 = sum r5(N) N^-s, checked against direct sums / quadrature and the FE s <-> 5/2-s.
(P3) zero count in the strip by the argument principle. (P4) on-line sign-change count; off-line zeros located if the
counts differ. Prereg hashed before run."""
import numpy as np, math, time, json, os, sys
from fractions import Fraction
from itertools import combinations
import mpmath as mp
t0 = time.time(); HERE = os.path.dirname(os.path.abspath(__file__))
score = []
def sc(name, ok, detail=""): score.append(ok); print(f"  [{'HIT' if ok else 'MISS'}] {name}  {detail}", flush=True)

# ---------- P1: chamber count to N = 200 ----------
J = np.diag([1, -1, -1, -1, -1]); E = np.eye(5, dtype=np.int64)
def ip(x, y): return int(x @ J @ y)
roots = [E[2]-E[1], E[3]-E[2], E[4]-E[3], -E[4], E[0]+E[1]+E[2]+E[3]]
S = [np.eye(5, dtype=np.int64) - (2 * np.outer(r, r @ J)) // ip(r, r) for r in roots]
_cache = {}
def stab_order(idx):
    idx = tuple(sorted(idx))
    if idx in _cache: return _cache[idx]
    gens = [S[i] for i in idx]; I5 = np.eye(5, dtype=np.int64); seen = {I5.tobytes()}; fr = [I5]
    while fr:
        nx = []
        for M in fr:
            for g in gens:
                Pm = g @ M; b = Pm.tobytes()
                if b not in seen: seen.add(b); nx.append(Pm)
        fr = nx
    _cache[idx] = len(seen); return len(seen)
def rstar(N):
    tot = Fraction(0)
    for x1 in range(0, N // 2 + 2):
        b2 = min(x1, N // (2 * x1) if x1 else N)
        for x2 in range(0, b2 + 1):
            b3 = min(x2, N // (2 * x1) if x1 else N)
            for x3 in range(0, b3 + 1):
                for x4 in range(0, x3 + 1):
                    s = N + x1*x1 + x2*x2 + x3*x3 + x4*x4; x0 = math.isqrt(s)
                    if x0 * x0 == s and x0 >= x1 + x2 + x3:
                        x = np.array([x0, x1, x2, x3, x4], dtype=np.int64)
                        tot += Fraction(1, stab_order([i for i in range(5) if ip(x, roots[i]) == 0]))
    return tot
NM = 200
B = math.isqrt(NM); th = np.zeros(NM + 1, dtype=np.int64)
for x in range(-B, B + 1):
    if x * x <= NM: th[x * x] += 1
r5 = th.copy()
for _ in range(4): r5 = np.convolve(r5, th)[:NM + 1]
bad = []
for N in range(1, NM + 1):
    if rstar(N) * 3840 != r5[N]: bad.append(N)
sc("P1", not bad, f"r*(N)*3840 = r5(N) for N<=200; failures {bad[:8]}  [{time.time()-t0:.0f}s]")
print("  r5(1..12):", r5[1:13].tolist(), flush=True)

# ---------- the Epstein zeta of Z^5 via the AFE ----------
mp.mp.dps = 30
NT = 22
R5 = [int(v) for v in r5[:NT + 1]]
def Lam(s):
    s = mp.mpc(s); tot = mp.mpc(0)
    for N in range(1, NT + 1):
        x = mp.pi * N
        tot += R5[N] * (x ** (-s) * mp.gammainc(s, x) + x ** (s - mp.mpf(5) / 2) * mp.gammainc(mp.mpf(5) / 2 - s, x))
    return tot - 1 / s - 1 / (mp.mpf(5) / 2 - s)
def Z5_direct(s, X=200000):
    s = mp.mpc(s); n = np.arange(1, X + 1)
    # r5 to X by convolution (int64)
    Bx = math.isqrt(X); t = np.zeros(X + 1, dtype=np.int64)
    for x in range(-Bx, Bx + 1):
        if x * x <= X: t[x * x] += 1
    r = t.copy()
    for _ in range(4): r = np.convolve(r, t)[:X + 1]
    vals = r[1:] * n.astype(float) ** (-float(mp.re(s))) * np.exp(-1j * float(mp.im(s)) * np.log(n))
    return complex(vals.sum()), r
print("P2: AFE vs direct / quadrature / functional equation", flush=True)
ok2 = True; det = []
for s0 in (mp.mpf('4.0'), mp.mpc(4, 2)):
    zd, _ = Z5_direct(s0); lam_d = complex(mp.pi ** (-s0) * mp.gamma(s0)) * zd
    la = complex(Lam(s0)); rel = abs(la - lam_d) / abs(la); det.append(f"s={s0}: rel {rel:.1e}")
    ok2 &= rel < 1e-6           # direct sum truncated at 2e5: tail ~ X^{-3/2}
# quadrature check at a high point: Lambda(s) = int_1^inf (theta^5(iy)-1)(y^{s-1}+y^{3/2-s}) dy - 1/s - 1/(5/2-s)
def theta5m1(y):
    return sum(R5[N] * mp.exp(-mp.pi * N * y) for N in range(1, NT + 1))
sq = mp.mpc(1.25, 40)
quad = mp.quad(lambda y: theta5m1(y) * (y ** (sq - 1) + y ** (mp.mpf(3) / 2 - sq)), [1, 2, 4, 8, mp.inf]) - 1 / sq - 1 / (mp.mpf(5) / 2 - sq)
la = Lam(sq); relq = abs(la - quad) / abs(la); det.append(f"quad at 5/4+40i: rel {mp.nstr(relq, 3)}"); ok2 &= relq < 1e-15
fe = max(abs(Lam(s) - Lam(mp.mpf(5) / 2 - s)) / abs(Lam(s)) for s in [mp.mpc(0.3, 7.1), mp.mpc(1.9, 13.4), mp.mpc(0.75, 25), mp.mpc(2.2, 33.3), mp.mpc(1.1, 48), mp.mpc(0.1, 61), mp.mpc(2.4, 70), mp.mpc(1.6, 85), mp.mpc(0.5, 92), mp.mpc(1.3, 99)])
det.append(f"FE max rel {mp.nstr(fe, 3)}"); ok2 &= fe < 1e-20
sc("P2", ok2, "; ".join(det) + f"  [{time.time()-t0:.0f}s]")

# ---------- argument principle ----------
def winding(z_vals):
    ph = np.unwrap(np.angle(np.array(z_vals, dtype=complex)))
    return (ph[-1] - ph[0]) / (2 * np.pi), np.max(np.abs(np.diff(ph)))
def path_vals(pts): return [complex(Lam(p)) for p in pts]
def box_count(s1, s2, t1, t2, h=0.05, depth=0):
    """zeros minus poles of Lambda inside the rectangle [s1,s2]x[t1,t2] (t1>0 so no poles), adaptive step."""
    while True:
        nR = max(4, int((t2 - t1) / h)); nT = max(4, int((s2 - s1) / h))
        pts = ([mp.mpc(s2, t1 + (t2 - t1) * k / nR) for k in range(nR + 1)] + [mp.mpc(s2 - (s2 - s1) * k / nT, t2) for k in range(1, nT + 1)] +
               [mp.mpc(s1, t2 - (t2 - t1) * k / nR) for k in range(1, nR + 1)] + [mp.mpc(s1 + (s2 - s1) * k / nT, t1) for k in range(1, nT + 1)])
        w, mx = winding(path_vals(pts))
        if mx < 1.5 or h < 0.003: return round(w), mx, h
        h /= 2
print("P3: zero count in the strip by the argument principle", flush=True)
T = 100.0
# real segment (-1/2, 3): sign changes of Lambda excluding the poles at 0 and 5/2
xs = [x for x in np.arange(-0.45, 3.0, 0.01) if abs(x) > 0.02 and abs(x - 2.5) > 0.02]
vr = [float(mp.re(Lam(mp.mpf(x)))) for x in xs]
real_zeros = sum(1 for i in range(1, len(xs)) if vr[i] * vr[i - 1] < 0 and not (xs[i-1] < 0 < xs[i]) and not (xs[i-1] < 2.5 < xs[i]))
# strip box: Re s in [-1/2, 3], Im s in (0.1, T]  (t1 = 0.1 keeps the poles out; zeros with 0<t<0.1 would be missed — checked by the real-segment scan and a tiny box)
counts = {}
for TT in (50.0, 100.0):
    w, mx, h = box_count(-0.5, 3.0, 0.1, TT); counts[TT] = w
    rvm = (TT / math.pi) * math.log(TT / (2 * math.pi * math.e)) + 0.5 * math.log(TT) / math.pi  # rough RvM-type for this gamma factor (degree-2-like), sanity only
    print(f"  T={TT}: winding (zeros in box) = {w}  (max step {mx:.2f} rad, h={h}); RvM-type rough {rvm:.1f}  [{time.time()-t0:.0f}s]", flush=True)
tiny, mxt, _ = box_count(-0.5, 3.0, 0.005, 0.1, h=0.02)
print(f"  real-segment sign changes {real_zeros}; box 0.005<t<0.1 winding {tiny}")
sc("P3", abs(counts[100.0] - ((100 / math.pi) * math.log(100 / (2 * math.pi * math.e)))) < 12, f"N_total(50) = {counts[50.0]}, N_total(100) = {counts[100.0]}")

# ---------- P4: on-line count ----------
print("P4: sign changes of Lambda(5/4+it) on (0,100]", flush=True)
ts = np.arange(0.1, T + 1e-9, 0.02)
lv = [float(mp.re(Lam(mp.mpc(1.25, t)))) for t in ts]
imax = max(abs(float(mp.im(Lam(mp.mpc(1.25, t))))) / (abs(v) + 1e-300) for t, v in zip(ts[::50], lv[::50]))
Nline = {50.0: sum(1 for i in range(1, len(ts)) if ts[i] <= 50 and lv[i] * lv[i-1] < 0), 100.0: sum(1 for i in range(1, len(ts)) if lv[i] * lv[i-1] < 0)}
print(f"  Lambda real on the line: max |Im/Re| sampled {imax:.1e}; N_line(50) = {Nline[50.0]}, N_line(100) = {Nline[100.0]}  [{time.time()-t0:.0f}s]", flush=True)
off = counts[100.0] - Nline[100.0]
found = []
if off > 0:
    print(f"  {off} zeros unaccounted on the line up to T=100 -> hunting off-line zeros in 1.25 < Re s < 3, 0.1 < t < 100", flush=True)
    stack = [(1.25, 3.0, 0.1, 100.0)]
    while stack and len(found) < 6:
        s1, s2, t1, t2 = stack.pop()
        w, mx, h = box_count(s1, s2, t1, t2, h=0.05)
        if w <= 0: continue
        if (s2 - s1) < 0.05 and (t2 - t1) < 0.05:
            z0 = mp.mpc((s1 + s2) / 2, (t1 + t2) / 2)
            try:
                z = mp.findroot(Lam, z0, tol=1e-24, maxsteps=60)
                wz, _, _ = box_count(float(mp.re(z)) - 0.01, float(mp.re(z)) + 0.01, float(mp.im(z)) - 0.01, float(mp.im(z)) + 0.01, h=0.002)
                found.append({'re': mp.nstr(mp.re(z), 17), 'im': mp.nstr(mp.im(z), 17), 'abs_Lam': mp.nstr(abs(Lam(z)), 3), 'box_winding': wz})
                print(f"  ZERO: s = {mp.nstr(z, 17)}  |Lambda| = {mp.nstr(abs(Lam(z)), 3)}  certificate winding {wz}", flush=True)
            except Exception as ex: print("  findroot failed at", z0, ex)
            continue
        if (t2 - t1) >= (s2 - s1): tm = (t1 + t2) / 2; stack += [(s1, s2, t1, tm), (s1, s2, tm, t2)]
        else: sm = (s1 + s2) / 2; stack += [(s1, sm, t1, t2), (sm, s2, t1, t2)]
sc("P4", off > 0 and len(found) > 0, f"N_total(100) = {counts[100.0]}, N_line(100) = {Nline[100.0]}, off-line pairs = {off}; located {len(found)}")
print(f"\nSCORE {sum(score)}/{len(score)} (P5 literature after the run)   [{time.time()-t0:.0f}s]")
json.dump({'counts': counts, 'Nline': Nline, 'real_zeros': real_zeros, 'found': found, 'r5': R5, 'score': f"{sum(score)}/{len(score)}"},
          open(os.path.join(HERE, '.epstein_5695.json'), 'w'), indent=1)
