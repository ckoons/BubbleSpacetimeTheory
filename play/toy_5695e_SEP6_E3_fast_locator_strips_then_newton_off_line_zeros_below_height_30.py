#!/usr/bin/env python3
"""Toy 5695e — E3 second locator (independent of 5695b's bisection): horizontal strips of height 3 in 1.25 < Re s < 3,
winding per strip, subdivide only where the winding is positive, Newton from the box centre, certify on a 0.01-box."""
import mpmath as mp, numpy as np, math, json, os, time
t0 = time.time(); HERE = os.path.dirname(os.path.abspath(__file__))
X = 1000; Bx = math.isqrt(X); th = np.zeros(X+1, dtype=np.int64)
for x in range(-Bx, Bx+1):
    if x*x <= X: th[x*x] += 1
r5 = th.copy()
for _ in range(4): r5 = np.convolve(r5, th)[:X+1]
R5 = [int(v) for v in r5]; mp.mp.dps = 30
def Lam(s):
    s = mp.mpc(s); t = abs(float(mp.im(s))); phi = mp.pi/2 - mp.mpf(5)/max(t, 5.0); y0 = mp.exp(1j*phi) if mp.im(s) >= 0 else mp.exp(-1j*phi)
    NT = int(4.5*t) + 60; tot = mp.mpc(0)
    for N in range(1, NT+1):
        x = mp.pi*N; tot += R5[N]*(x**(-s)*mp.gammainc(s, x*y0) + x**(s - mp.mpf(5)/2)*mp.gammainc(mp.mpf(5)/2 - s, x/y0))
    return tot + y0**(s - mp.mpf(5)/2)/(s - mp.mpf(5)/2) - y0**s/s
def wind(s1, s2, t1, t2, h):
    nR = max(3, int((t2-t1)/h)); nT = max(3, int((s2-s1)/h))
    pts = [mp.mpc(s2, t1+(t2-t1)*k/nR) for k in range(nR+1)] + [mp.mpc(s2-(s2-s1)*k/nT, t2) for k in range(1, nT+1)] + [mp.mpc(s1, t2-(t2-t1)*k/nR) for k in range(1, nR+1)] + [mp.mpc(s1+(s2-s1)*k/nT, t1) for k in range(1, nT+1)]
    ph = np.unwrap(np.angle(np.array([complex(Lam(p)) for p in pts]))); return int(round((ph[-1]-ph[0])/(2*np.pi))), float(np.max(np.abs(np.diff(ph))))
found = []
def refine(s1, s2, t1, t2, w):
    if (s2-s1) <= 0.12 and (t2-t1) <= 0.12:
        z0 = mp.mpc((s1+s2)/2, (t1+t2)/2)
        try:
            z = mp.findroot(Lam, z0, tol=1e-22, maxsteps=40)
            wz, _ = wind(float(mp.re(z))-0.01, float(mp.re(z))+0.01, float(mp.im(z))-0.01, float(mp.im(z))+0.01, 0.002)
            found.append({'re': mp.nstr(mp.re(z), 18), 'im': mp.nstr(mp.im(z), 18), 'absLam': mp.nstr(abs(Lam(z)), 3), 'winding': wz, 'box_w': w})
            print(f"  ZERO s = {mp.nstr(z, 18)}  |Lambda| = {mp.nstr(abs(Lam(z)), 3)}  0.01-box winding {wz}  (box count {w})  [{time.time()-t0:.0f}s]", flush=True)
        except Exception as ex: print("  findroot failed", z0, ex, flush=True)
        return
    if (t2-t1) >= (s2-s1): parts = [(s1, s2, t1, (t1+t2)/2), (s1, s2, (t1+t2)/2, t2)]
    else: parts = [(s1, (s1+s2)/2, t1, t2), ((s1+s2)/2, s2, t1, t2)]
    for p in parts:
        wp, mx = wind(*p, h=min(0.05, max(0.005, (p[3]-p[2])/6)))
        if wp > 0: refine(*p, wp)
for k in range(20):
    t1, t2 = 0.1 + 3*k, 0.1 + 3*(k+1)
    w, mx = wind(1.32, 3.0, t1, t2, 0.1)
    print(f"strip t in ({t1:.1f}, {t2:.1f}]: winding {w} (max step {mx:.2f})  [{time.time()-t0:.0f}s]", flush=True)
    if w > 0: refine(1.32, 3.0, t1, t2, w)
print(f"\nlocated {len(found)} off-line zeros below height 60 in 1.32 < Re s < 3 (counts say 13 pairs; the band 1.25 < Re s < 1.32 is not searched)  [{time.time()-t0:.0f}s]")
json.dump(found, open(os.path.join(HERE, '.epstein_5695e.json'), 'w'), indent=1)
