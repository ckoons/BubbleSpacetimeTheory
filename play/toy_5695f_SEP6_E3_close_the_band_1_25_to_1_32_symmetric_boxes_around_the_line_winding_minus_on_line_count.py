#!/usr/bin/env python3
"""Toy 5695f — close the unsearched band 1.25 < Re s < 1.32 (R121): symmetric boxes [1.18, 1.32] x strips of height 6 up to 60;
winding = (#on-line zeros in the strip, each once) + 2*(#band pairs). On-line zeros from 5695b's sign changes. Arithmetic check:
N_total(60) = 39 = 13 on-line + 26 located off-line already forces zero in the band; this is the direct confirmation."""
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
online = [3.9, 8.55, 12.6, 17.75, 22.55, 26.9, 29.75, 35.75, 40.7, 45.2, 47.9, 53.9, 58.1]   # 5695b sign changes (±0.05)
band_pairs = 0; rows = []
for k in range(10):
    t1, t2 = 0.1 + 6*k, 0.1 + 6*(k+1)
    w, mx = wind(1.18, 1.32, t1, t2, 0.05); n_on = sum(1 for z in online if t1 < z <= t2)
    pairs = (w - n_on) / 2; band_pairs += pairs
    rows.append((t1, t2, w, n_on, pairs)); print(f"  strip ({t1:.1f}, {t2:.1f}]: winding {w}, on-line zeros {n_on}, band pairs {pairs:+.1f}  (max step {mx:.2f})  [{time.time()-t0:.0f}s]", flush=True)
print(f"\nband 1.25 < Re s < 1.32, 0 < t <= 60: {band_pairs:.0f} zero pairs; arithmetic check 39 - 13 - 26 = 0")
json.dump({'rows': rows, 'band_pairs': band_pairs}, open(os.path.join(HERE, '.band_5695f.json'), 'w'), indent=1)
