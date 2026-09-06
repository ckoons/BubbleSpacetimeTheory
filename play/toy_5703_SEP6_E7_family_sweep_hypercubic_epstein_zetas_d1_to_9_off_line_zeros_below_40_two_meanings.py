#!/usr/bin/env python3
"""Toy 5703 — E7: zeta_{Z^d}, d = 1..9. Rotated-splitting AFE (5695b) with d/2 for 5/2. Per d: instrument checks, N_total(40)
by the argument principle, N_line(40) by sign changes, right-half strip search for off-line zeros, classified (a) in-strip / (b)
beyond the abscissa. Prereg df6d85c6."""
import mpmath as mp, numpy as np, math, json, os, time
t0 = time.time(); HERE = os.path.dirname(os.path.abspath(__file__)); T = 40.0
X = 400; Bx = math.isqrt(X); th = np.zeros(X + 1, dtype=np.int64)
for x in range(-Bx, Bx + 1):
    if x * x <= X: th[x * x] += 1
mp.mp.dps = 30
def coeffs(d):
    r = np.zeros(X + 1, dtype=np.int64); r[0] = 1
    for _ in range(d): r = np.convolve(r, th)[:X + 1]
    return [int(v) for v in r]
def make_Lam(d, R):
    k = mp.mpf(d) / 2
    def Lam(s):
        s = mp.mpc(s); t = abs(float(mp.im(s))); phi = mp.pi / 2 - mp.mpf(5) / max(t, 5.0); y0 = mp.exp(1j * phi) if mp.im(s) >= 0 else mp.exp(-1j * phi)
        NT = min(X, int(4.5 * t) + 60); tot = mp.mpc(0)
        for N in range(1, NT + 1):
            if R[N] == 0: continue
            x = mp.pi * N; tot += R[N] * (x ** (-s) * mp.gammainc(s, x * y0) + x ** (s - k) * mp.gammainc(k - s, x / y0))
        return tot + y0 ** (s - k) / (s - k) - y0 ** s / s
    def Lam_ref(s, dps=90, NT=80):
        with mp.workdps(dps):
            s = mp.mpc(s); tot = mp.mpc(0)
            for N in range(1, NT + 1):
                if R[N] == 0: continue
                x = mp.pi * N; tot += R[N] * (x ** (-s) * mp.gammainc(s, x) + x ** (s - k) * mp.gammainc(k - s, x))
            return tot - 1 / s - 1 / (k - s)
    return Lam, Lam_ref
def winding(vals):
    ph = np.unwrap(np.angle(np.array(vals, dtype=complex))); return (ph[-1] - ph[0]) / (2 * np.pi), float(np.max(np.abs(np.diff(ph))))
def box(Lam, s1, s2, t1, t2, h):
    while True:
        nR = max(3, int((t2 - t1) / h)); nT = max(3, int((s2 - s1) / h))
        pts = [mp.mpc(s2, t1 + (t2 - t1) * kk / nR) for kk in range(nR + 1)] + [mp.mpc(s2 - (s2 - s1) * kk / nT, t2) for kk in range(1, nT + 1)] + [mp.mpc(s1, t2 - (t2 - t1) * kk / nR) for kk in range(1, nR + 1)] + [mp.mpc(s1 + (s2 - s1) * kk / nT, t1) for kk in range(1, nT + 1)]
        w, mx = winding([complex(Lam(p)) for p in pts])
        if mx < 1.2 or h < 0.004: return int(round(w)), mx
        h /= 2
results = {}
for d in range(1, 10):
    R = coeffs(d); Lam, Lam_ref = make_Lam(d, R); k = d / 2; line = d / 4
    print(f"\n=== d = {d}: line Re s = {line}, abscissa {k} ===", flush=True)
    fe = max(abs(Lam(s) - Lam(k - s)) / abs(Lam(s)) for s in [mp.mpc(line + 0.3, 7.1), mp.mpc(line - 0.2, 21.4), mp.mpc(line + 0.1, 33.3)])
    ref = Lam_ref(mp.mpc(line + 0.2, 20)); rel = abs(Lam(mp.mpc(line + 0.2, 20)) - ref) / abs(ref)
    print(f"  FE residual {mp.nstr(fe, 2)}, reference agreement {mp.nstr(rel, 2)}", flush=True)
    Nt, mx = box(Lam, -0.5, k + 0.5, 0.1, T, 0.1)
    ts = np.arange(0.1, T + 1e-9, 0.05); lv = [float(mp.re(Lam(mp.mpc(line, t)))) for t in ts]
    Nl = sum(1 for i in range(1, len(ts)) if lv[i] * lv[i - 1] < 0)
    print(f"  N_total(40) = {Nt} (max step {mx:.2f}); N_line(40) = {Nl}; density (T/pi)log(T/(pi e)) = {(T/math.pi)*math.log(T/(math.pi*math.e)):.1f}  [{time.time()-t0:.0f}s]", flush=True)
    found = []
    def refine(s1, s2, t1, t2, w):
        if (s2 - s1) <= 0.12 and (t2 - t1) <= 0.12:
            z0 = mp.mpc((s1 + s2) / 2, (t1 + t2) / 2)
            try:
                z = mp.findroot(Lam, z0, tol=1e-20, maxsteps=40)
                wz, _ = box(Lam, float(mp.re(z)) - 0.01, float(mp.re(z)) + 0.01, float(mp.im(z)) - 0.01, float(mp.im(z)) + 0.01, 0.002)
                cls = 'b' if float(mp.re(z)) > k else 'a'
                found.append({'re': mp.nstr(mp.re(z), 16), 'im': mp.nstr(mp.im(z), 16), 'absLam': mp.nstr(abs(Lam(z)), 3), 'winding': wz, 'class': cls})
                print(f"    ZERO ({cls}) s = {mp.nstr(z, 16)}  |Lambda| = {mp.nstr(abs(Lam(z)), 3)}  winding {wz}  [{time.time()-t0:.0f}s]", flush=True)
            except Exception as ex: print("    findroot failed", z0, ex, flush=True)
            return
        if (t2 - t1) >= (s2 - s1): parts = [(s1, s2, t1, (t1 + t2) / 2), (s1, s2, (t1 + t2) / 2, t2)]
        else: parts = [(s1, (s1 + s2) / 2, t1, t2), ((s1 + s2) / 2, s2, t1, t2)]
        for p in parts:
            wp, _ = box(Lam, *p, min(0.05, max(0.005, (p[3] - p[2]) / 6)))
            if wp > 0: refine(*p, wp)
    sL, sR = line + 0.05, k + 0.6
    for j in range(10):
        t1, t2 = 0.1 + 4 * j, 0.1 + 4 * (j + 1)
        w, _ = box(Lam, sL, sR, t1, t2, 0.1)
        if w > 0: refine(sL, sR, t1, t2, w)
    na = sum(1 for f in found if f['class'] == 'a'); nb = sum(1 for f in found if f['class'] == 'b')
    rem = Nt - Nl - 2 * len(found)
    print(f"  d={d}: located right-half zeros {len(found)} -> (a)-count {2*na}, (b)-count {2*nb} (pairs counted both halves); unlocated remainder {rem}  [{time.time()-t0:.0f}s]", flush=True)
    results[d] = {'FE': mp.nstr(fe, 3), 'ref': mp.nstr(rel, 3), 'N_total': Nt, 'N_line': Nl, 'a_count': 2 * na, 'b_count': 2 * nb, 'remainder': rem, 'zeros_right_half': found}
    json.dump(results, open(os.path.join(HERE, '.family_5703.json'), 'w'), indent=1)
print("\nSUMMARY (a)/(b) per d:", {d: (results[d]['a_count'], results[d]['b_count']) for d in results})
nob = sorted(d for d in results if results[d]['b_count'] == 0)
print("d with no (b)-zero below 40:", nob, " (P4 predicts [1, 2, 4, 8])")
print(f"[{time.time()-t0:.0f}s]")
