#!/usr/bin/env python3
"""Toy 5695b — E3 instrument fixed: AFE with a ROTATED splitting point y0 = e^{i phi}, phi = pi/2 - 5/t, which removes
the e^{-pi t/2} cancellation (tested: 4e-30 at t=40, dps 30). P1 stands from 5695 (identity to N=200). Prereg 35921446."""
import numpy as np, math, time, json, os
import mpmath as mp
t0 = time.time(); HERE = os.path.dirname(os.path.abspath(__file__)); score = []
def sc(name, ok, detail=""): score.append(ok); print(f"  [{'HIT' if ok else 'MISS'}] {name}  {detail}", flush=True)
X = 2000; Bx = math.isqrt(X); th = np.zeros(X + 1, dtype=np.int64)
for x in range(-Bx, Bx + 1):
    if x * x <= X: th[x * x] += 1
r5 = th.copy()
for _ in range(4): r5 = np.convolve(r5, th)[:X + 1]
R5 = [int(v) for v in r5]
mp.mp.dps = 30
def Lam(s):
    s = mp.mpc(s); t = abs(float(mp.im(s)))
    phi = mp.pi / 2 - mp.mpf(5) / max(t, 5.0); y0 = mp.exp(1j * phi) if mp.im(s) >= 0 else mp.exp(-1j * phi)
    NT = int(4.5 * t) + 60; tot = mp.mpc(0)
    for N in range(1, NT + 1):
        x = mp.pi * N
        tot += R5[N] * (x ** (-s) * mp.gammainc(s, x * y0) + x ** (s - mp.mpf(5) / 2) * mp.gammainc(mp.mpf(5) / 2 - s, x / y0))
    return tot + y0 ** (s - mp.mpf(5) / 2) / (s - mp.mpf(5) / 2) - y0 ** s / s
def Lam_ref(s, dps=90, NT=70):
    with mp.workdps(dps):
        s = mp.mpc(s); tot = mp.mpc(0)
        for N in range(1, NT + 1):
            x = mp.pi * N; tot += R5[N] * (x ** (-s) * mp.gammainc(s, x) + x ** (s - mp.mpf(5) / 2) * mp.gammainc(mp.mpf(5) / 2 - s, x))
        return tot - 1 / s - 1 / (mp.mpf(5) / 2 - s)
print("P2: instrument checks", flush=True)
det = []; ok2 = True
for s0 in (mp.mpc(4, 0), mp.mpc(4, 2)):
    n = np.arange(1, X + 1); zd = complex((r5[1:] * n ** (-4.0) * np.exp(-1j * float(mp.im(s0)) * np.log(n))).sum())
    ld = complex(mp.pi ** (-s0) * mp.gamma(s0)) * zd; la = complex(Lam(s0)); rel = abs(la - ld) / abs(la); det.append(f"direct(X=2000) at {s0}: {rel:.1e}"); ok2 &= rel < 1e-4
for s0 in (mp.mpc(1.25, 40), mp.mpc(0.4, 33.3), mp.mpc(2.1, 20)):
    ref = Lam_ref(s0); la = Lam(s0); rel = abs(la - ref) / abs(ref); det.append(f"ref90 at {s0}: {mp.nstr(rel, 2)}"); ok2 &= rel < 1e-20
fe = max(abs(Lam(s) - Lam(mp.mpf(5) / 2 - s)) / abs(Lam(s)) for s in [mp.mpc(0.3, 7.1), mp.mpc(1.9, 13.4), mp.mpc(0.75, 25), mp.mpc(2.2, 33.3), mp.mpc(1.1, 48), mp.mpc(0.1, 58)])
det.append(f"FE max rel {mp.nstr(fe, 2)}"); ok2 &= fe < 1e-20
sc("P2", ok2, "; ".join(det) + f"  [{time.time()-t0:.0f}s]")
def winding(vals):
    ph = np.unwrap(np.angle(np.array(vals, dtype=complex))); return (ph[-1] - ph[0]) / (2 * np.pi), float(np.max(np.abs(np.diff(ph))))
def box(s1, s2, t1, t2, h):
    while True:
        nR = max(4, int((t2 - t1) / h)); nT = max(4, int((s2 - s1) / h))
        pts = ([mp.mpc(s2, t1 + (t2 - t1) * k / nR) for k in range(nR + 1)] + [mp.mpc(s2 - (s2 - s1) * k / nT, t2) for k in range(1, nT + 1)] +
               [mp.mpc(s1, t2 - (t2 - t1) * k / nR) for k in range(1, nR + 1)] + [mp.mpc(s1 + (s2 - s1) * k / nT, t1) for k in range(1, nT + 1)])
        w, mx = winding([complex(Lam(p)) for p in pts])
        if mx < 1.2 or h < 0.004: return int(round(w)), mx, h
        h /= 2
print("P3: argument-principle count in [-1/2, 3] x (0.1, T]", flush=True)
counts = {}
for TT in (30.0, 60.0):
    w, mx, h = box(-0.5, 3.0, 0.1, TT, 0.1); counts[TT] = w
    rvm = (TT / math.pi) * math.log(TT / (math.pi * math.e))
    print(f"  T={TT}: N_total = {w} (max step {mx:.2f}, h={h}); (T/pi)log(T/(pi e)) = {rvm:.1f}  [{time.time()-t0:.0f}s]", flush=True)
xs = [x for x in np.arange(-0.45, 3.0, 0.01) if abs(x) > 0.02 and abs(x - 2.5) > 0.02]
vr = [float(mp.re(Lam(mp.mpf(x)))) for x in xs]
real_zeros = sum(1 for i in range(1, len(xs)) if vr[i] * vr[i - 1] < 0 and not (xs[i-1] < 0 < xs[i]) and not (xs[i-1] < 2.5 < xs[i]))
print(f"  real zeros on (-1/2,3) excluding the poles: {real_zeros}", flush=True)
sc("P3", abs(counts[60.0] - (60 / math.pi) * math.log(60 / (math.pi * math.e))) < 8, f"N_total(30) = {counts[30.0]}, N_total(60) = {counts[60.0]}; prereg's sanity formula had 2pi in the log where the Gamma(s) factor gives pi — owned; correct formula quoted")
print("P4: on-line sign changes of Lambda(5/4+it), t in (0.1, 60]", flush=True)
ts = np.arange(0.1, 60.0 + 1e-9, 0.05); lv = []
for t in ts:
    v = Lam(mp.mpc(1.25, t)); lv.append(float(mp.re(v)))
imax = max(abs(float(mp.im(Lam(mp.mpc(1.25, t))))) / (abs(v) + 1e-300) for t, v in list(zip(ts, lv))[::100])
Nline = {30.0: sum(1 for i in range(1, len(ts)) if ts[i] <= 30 and lv[i] * lv[i-1] < 0), 60.0: sum(1 for i in range(1, len(ts)) if lv[i] * lv[i-1] < 0)}
line_zeros = [float(ts[i]) for i in range(1, len(ts)) if lv[i] * lv[i-1] < 0]
print(f"  max |Im/Re| on the line {imax:.1e}; N_line(30) = {Nline[30.0]}, N_line(60) = {Nline[60.0]}; on-line zeros: {np.round(line_zeros, 2).tolist()}  [{time.time()-t0:.0f}s]", flush=True)
off = counts[60.0] - Nline[60.0]; found = []
if off > 0:
    print(f"  {off} zeros not on the line below 60 -> hunting in 1.25 < Re s < 3, 0.1 < t < 60", flush=True)
    stack = [(1.25 + 1e-6, 3.0, 0.1, 60.0)]
    while stack and len(found) < 8:
        s1, s2, t1, t2 = stack.pop()
        w, mx, h = box(s1, s2, t1, t2, min(0.1, max(0.01, (t2 - t1) / 8)))
        if w <= 0: continue
        if (s2 - s1) < 0.03 and (t2 - t1) < 0.03:
            z0 = mp.mpc((s1 + s2) / 2, (t1 + t2) / 2)
            try:
                z = mp.findroot(Lam, z0, tol=1e-18, maxsteps=40)
                wz, _, _ = box(float(mp.re(z)) - 0.005, float(mp.re(z)) + 0.005, float(mp.im(z)) - 0.005, float(mp.im(z)) + 0.005, 0.001)
                found.append({'re': mp.nstr(mp.re(z), 18), 'im': mp.nstr(mp.im(z), 18), 'abs_Lam': mp.nstr(abs(Lam(z)), 3), 'box_winding': wz, 'multiplicity_in_box': w})
                print(f"  ZERO s = {mp.nstr(z, 18)}   |Lambda(s)| = {mp.nstr(abs(Lam(z)), 3)}   certificate: winding {wz} on the 0.01-box  [{time.time()-t0:.0f}s]", flush=True)
            except Exception as ex: print("  findroot failed at", z0, ex, flush=True)
            continue
        if (t2 - t1) >= 2 * (s2 - s1): tm = (t1 + t2) / 2; stack += [(s1, s2, t1, tm), (s1, s2, tm, t2)]
        else: sm = (s1 + s2) / 2; stack += [(s1, sm, t1, t2), (sm, s2, t1, t2)]
sc("P4", off > 0 and len(found) > 0, f"N_total(60) = {counts[60.0]}, N_line(60) = {Nline[60.0]}, off-line = {off}; located and certified {len(found)}")
print(f"\nSCORE (P1 from 5695 HIT) {1 + sum(score)}/{1 + len(score)}   [{time.time()-t0:.0f}s]")
json.dump({'counts': counts, 'Nline': Nline, 'line_zeros': line_zeros, 'real_zeros': real_zeros, 'found': found, 'score': f"{1+sum(score)}/{1+len(score)}"},
          open(os.path.join(HERE, '.epstein_5695b.json'), 'w'), indent=1)
