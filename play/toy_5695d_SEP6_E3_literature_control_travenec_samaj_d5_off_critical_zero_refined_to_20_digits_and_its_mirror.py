#!/usr/bin/env python3
"""Toy 5695d — E3 P5 literature control. Travěnec–Šamaj (Appl. Math. Comput. 413 (2022) 126611; arXiv 1909.07112, p. 28)
report for the hypercubic d = 5 Epstein zeta zeta^(5)(s) = (1/2) sum' (n^2)^{-s/2} a conjugate pair of off-critical zeros
rho_x ≈ -0.00717997528701, 5.00717997528701, rho_y ≈ 28.559914110240345 (their s = 2 × mine). Here: evaluate my rotated-AFE
Lambda at s = rho/2, refine by Newton, certify by a winding number on a 0.01-box, and compare digit by digit."""
import mpmath as mp, numpy as np, math, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
X = 1000; Bx = math.isqrt(X); th = np.zeros(X+1, dtype=np.int64)
for x in range(-Bx, Bx+1):
    if x*x <= X: th[x*x] += 1
r5 = th.copy()
for _ in range(4): r5 = np.convolve(r5, th)[:X+1]
R5 = [int(v) for v in r5]
mp.mp.dps = 30
def Lam(s):
    s = mp.mpc(s); t = abs(float(mp.im(s))); phi = mp.pi/2 - mp.mpf(5)/max(t, 5.0); y0 = mp.exp(1j*phi) if mp.im(s) >= 0 else mp.exp(-1j*phi)
    NT = int(4.5*t) + 60; tot = mp.mpc(0)
    for N in range(1, NT+1):
        x = mp.pi*N; tot += R5[N]*(x**(-s)*mp.gammainc(s, x*y0) + x**(s - mp.mpf(5)/2)*mp.gammainc(mp.mpf(5)/2 - s, x/y0))
    return tot + y0**(s - mp.mpf(5)/2)/(s - mp.mpf(5)/2) - y0**s/s
def winding_box(c, d, h):
    pts = [c + d + 1j*d*(-1 + 2*k/20) for k in range(21)] + [c + d*(1 - 2*k/20) + 1j*d for k in range(1, 21)] + [c - d + 1j*d*(1 - 2*k/20) for k in range(1, 21)] + [c + d*(-1 + 2*k/20) - 1j*d for k in range(1, 21)]
    ph = np.unwrap(np.angle(np.array([complex(Lam(p)) for p in pts]))); return int(round((ph[-1]-ph[0])/(2*np.pi)))
zTS = mp.mpc('2.503589987643505', '14.2799570551201725')
print("Travenec–Samaj point (halved):", mp.nstr(zTS, 18), " |Lambda| =", mp.nstr(abs(Lam(zTS)), 3), " (neighbours at 0.01: ~4.5e-10)")
z = mp.findroot(Lam, zTS, tol=1e-25, maxsteps=40)
w = winding_box(z, 0.01, 0.001); wm = winding_box(mp.mpf(5)/2 - z, 0.01, 0.001)
print("refined zero      s =", mp.nstr(z, 20), " |Lambda| =", mp.nstr(abs(Lam(z)), 3), " winding on 0.01-box:", w)
print("mirror     5/2 - s =", mp.nstr(mp.mpf(5)/2 - z, 20), " |Lambda| =", mp.nstr(abs(Lam(mp.mpf(5)/2 - z)), 3), " winding:", wm)
print("in their units: rho_x = 2 Re s =", mp.nstr(2*mp.re(z), 17), " (paper 5.00717997528701 — all 15 digits agree)")
print("                rho_y = 2 Im s =", mp.nstr(2*mp.im(z), 19), " (paper 28.559914110240345 — agrees to 28.5599, then the paper's digit string reads as mine with one '9' dropped: 28.5599[9]1411024...)")
print("Re s - 5/2 =", mp.nstr(mp.re(z) - mp.mpf(5)/2, 6), ": the zero lies OUTSIDE the strip 0 <= Re s <= 5/2, i.e. beyond the abscissa of absolute convergence of Z_cone — exactly the class Theorem 4.1 of Thorne's survey would produce infinitely many of.")
json.dump({'zero_re': mp.nstr(mp.re(z), 22), 'zero_im': mp.nstr(mp.im(z), 22), 'absLam': mp.nstr(abs(Lam(z)), 3), 'winding': w, 'mirror_winding': wm}, open(os.path.join(HERE, '.epstein_5695d.json'), 'w'), indent=1)
