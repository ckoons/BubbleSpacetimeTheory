#!/usr/bin/env python3
"""
Toy 5784 (RUN 3: de-aliased + F0 in log space; run 1 aliased, run 2 F0 overflow sum spectrum; run 1 binned an E1xE2 lattice into mismatched T bins — peak positions were aliasing) — 2nbb of 100Mo, SSD: electron sum spectrum for FERMIONIC vs BOSONIC antineutrinos.
(Elie, 2026-09-25; round 2 item 4 / round 3 item 4 — instrument for Lyra's residue-sign mapping.)

FORMULAS — all from Grace's pin data/sources_grace_2026-09-25/r3/barabash_dolgov_2007_arXiv0704.2944.txt
(Barabash, Dolgov, Dvornicky, Simkovic, NPB 783 (2007) 90):
  Eq. (9)  bosonic:   K^b = [D + Ee1 + Ev1]^-1 - [D + Ee2 + Ev2]^-1,  L^b = [D + Ee2 + Ev1]^-1 - [D + Ee1 + Ev2]^-1
  Eq. (10) fermionic: same with '+'.     D = E_m - E_i (intermediate 1+ minus initial).
  Eq. (39) SSD, 0+ -> 0+: g = (1/3)(K K + L L + K L)   (the p1.p2 term, Eq. 34, integrates to 0 over cos theta)
  Eq. (38) I = int F0(Ee1) p1 Ee1 dEe1 int F0(Ee2) p2 Ee2 dEe2 int Ev2^2 Ev1^2 dEv1 g,  Ev2 = E0 - Ee1 - Ee2 - Ev1,
           Ee total energies (from m_e), E0 = E_i - E_f.
  Eq. (8)  W_tot = cos^4 chi W_f + sin^4 chi W_b  (no interference).
REPRODUCTION TARGETS (same paper): Eq. (41) r0 = W_b/W_f = 0.076 (SSD, 100Mo);
  text after Fig. 1: bosonic sum-spectrum maximum shifted DOWN by ~15 % relative to fermionic.
INPUTS:
  Q_bb(100Mo) = 3.034 MeV  (CUPID-Mo 2307.14086 l.218, '... measured at 3034 keV'); E0 = Q + 2 m_e.
  Z_f = 44 (Ru).  m_e = 0.51100 MeV.
  D = E_m - E_i: NOT PINNED (NEMO-3 1903.08084 says only 'lying close to the ground state of 100Mo').
      Scanned; the value that reproduces r0 = 0.076 is REPORTED as an output, and the peak shift at that
      D is the independent check. Pin owed: Q_EC(100Tc) (AME) -> Grace.
  F0: relativistic Coulomb factor — the paper names it, does not print it. Two versions run:
      F0_rel (point-nucleus textbook form, R = 1.2 A^1/3 fm — FLAGGED, not pinned) and F0 = 1 (no Coulomb).
      Conclusions must hold under both or are reported as Coulomb-dependent.

DIRECTION BEFORE NUMBERS:
  P1 bosonic sum spectrum is SOFTER (peak at lower T) for every D scanned and both F0 versions.
  P2 there is a D with D + m_e in (0, 1) MeV where r0 = 0.076 is reproduced (bisection).
  P3 at that D the peak shift is 15 % +- 5 % (independent of the r0 fit).
  P4 SSD fermionic spectrum is wider than the D -> large (HSD-like, K = L = const) fermionic spectrum.
  P5 (control) g_b = 0 identically at Ee1 = Ee2, Ev1 = Ev2 (both K^b and L^b vanish).
"""
import numpy as np
from math import pi, sqrt, lgamma
import cmath

me = 0.51100
Q = 3.034
E0 = Q + 2*me
Zf, A = 44, 100
alpha = 1/137.035999
R = 1.2*A**(1/3)/386.159   # fm -> units of hbar/(m_e c) (386.159 fm), FLAGGED

def F0_rel(E):
    p = np.sqrt(np.maximum(E**2 - me**2, 1e-12))/me
    W = E/me
    g = sqrt(1 - (alpha*Zf)**2)
    y = alpha*Zf*W/p
    out = np.empty_like(p)
    for i, (pp, yy) in enumerate(zip(p.flat, y.flat)):
        lg = cmath.log(complex(1, 0))  # placeholder
        # |Gamma(g + i y)|^2 via complex loggamma (mpmath-free): use scipy if present
        out.flat[i] = np.exp(np.log(4) + 2*(g - 1)*np.log(2*pp*R) + pi*yy + logabsgamma2(g, yy) - 2*lgamma(2*g + 1))
    return out

try:
    from scipy.special import loggamma
    def logabsgamma2(g, y):
        return float(2*np.real(loggamma(complex(g, y))))
except ImportError:
    import mpmath
    def logabsgamma2(g, y):
        return float(2*mpmath.re(mpmath.loggamma(mpmath.mpc(g, y))))

def F0_one(E):
    return np.ones_like(E)

NE = 160
NV = 48
xg, wg = np.polynomial.legendre.leggauss(NV)

def gfun(D, E1, E2, v1, v2, kind):
    a = 1/(D + E1 + v1); b = 1/(D + E2 + v2)
    c = 1/(D + E2 + v1); d = 1/(D + E1 + v2)
    if kind == "f":
        K, L = a + b, c + d
    else:
        K, L = a - b, c - d
    return (K*K + L*L + K*L)/3

NT = 240
def spectrum(D, F0, kind):
    """RUN 2 (de-aliased): dW/dT computed directly at fixed T = Ee1 + Ee2 - 2me by
    Gauss-Legendre over Ee1 (Ee2 = T + 2me - Ee1) and over Ev1 (Ev2 = E0 - Ee1 - Ee2 - Ev1).
    Returns T grid, dW/dT, total W (trapezoid in T)."""
    Tc = np.linspace(1e-4, Q - 1e-4, NT)
    xe, we = np.polynomial.legendre.leggauss(64)
    out = np.zeros(NT)
    for i, T in enumerate(Tc):
        E1 = me + T*(xe + 1)/2; E2 = T + 2*me - E1
        Fe = F0(E1)*np.sqrt(np.maximum(E1**2 - me**2, 0))*E1*F0(E2)*np.sqrt(np.maximum(E2**2 - me**2, 0))*E2
        rem = E0 - E1 - E2          # = Q - T > 0
        acc = np.zeros_like(E1)
        for x, w in zip(xg, wg):
            v1 = rem*(x + 1)/2; v2 = rem - v1
            acc += w*gfun(D, E1, E2, v1, v2, kind)*v1**2*v2**2*rem/2
        out[i] = (we*Fe*acc).sum()*T/2
    W = np.trapz(out, Tc)
    return Tc, out, W

def peak(Tc, h):
    i = int(np.argmax(h))
    if 0 < i < len(h) - 1:   # parabolic refinement
        y0, y1, y2 = h[i-1], h[i], h[i+1]
        den = y0 - 2*y1 + y2
        off = 0.5*(y0 - y2)/den if den != 0 else 0
        return Tc[i] + off*(Tc[1] - Tc[0])
    return Tc[i]

checks = []
def check(name, ok, can_fail=True):
    checks.append((name, bool(ok), can_fail))
    print(f"  [{'PASS' if ok else 'FAIL'}]{'' if can_fail else ' (control)'} {name}")

print("Toy 5784 — 100Mo 2nbb SSD, fermionic vs bosonic antineutrinos\n")
print("DIRECTION: P1 bosonic softer everywhere; P2 a physical D reproduces r0=0.076; P3 shift 15+-5 % there;")
print("           P4 SSD fermionic wider than HSD-like; P5 control g_b=0 on the symmetric point.\n")

# P5
E1 = E2 = 1.2; v = 0.5; D = -0.3
Kb = 1/(D + E1 + v) - 1/(D + E2 + v); Lb = 1/(D + E2 + v) - 1/(D + E1 + v)
check("P5 control: K^b = L^b = 0 at Ee1 = Ee2, Ev1 = Ev2", Kb == 0 and Lb == 0, can_fail=False)

Ds = [-0.45, -0.40, -0.35, -0.30, -0.20, -0.10, 0.0, 0.2, 0.5]
rows = {}
for fname, F0 in (("F0_rel", F0_rel), ("F0=1", F0_one)):
    print(f"  Coulomb: {fname}")
    for D in Ds:
        Tc, hf, Wf = spectrum(D, F0, "f")
        _, hb, Wb = spectrum(D, F0, "b")
        pf, pb = peak(Tc, hf), peak(Tc, hb)
        rows[(fname, D)] = (Wb/Wf, pf, pb)
        print(f"    D={D:+.2f} (D+me={D+me:.3f}): r0 = {Wb/Wf:.4f}   peak_f = {pf:.3f}  peak_b = {pb:.3f}  "
              f"shift = {100*(pf - pb)/pf:5.1f} %")
check("P1 bosonic peak below fermionic for every D and both Coulomb versions",
      all(v[2] < v[1] for v in rows.values()))

def solve_D(F0, target=0.076):
    lo, hi = -me + 0.02, 0.49   # D + me in (0.02, 1.0)
    rl = spectrum(lo, F0, "b")[2]/spectrum(lo, F0, "f")[2] - target
    rh = spectrum(hi, F0, "b")[2]/spectrum(hi, F0, "f")[2] - target
    if rl*rh > 0:
        return None
    for _ in range(30):
        mid = 0.5*(lo + hi)
        rm = spectrum(mid, F0, "b")[2]/spectrum(mid, F0, "f")[2] - target
        if rl*rm <= 0:
            hi = mid
        else:
            lo, rl = mid, rm
    return 0.5*(lo + hi)

print()
Dstar = {}
for fname, F0 in (("F0_rel", F0_rel), ("F0=1", F0_one)):
    Dstar[fname] = solve_D(F0)
    print(f"  {fname}: D reproducing r0 = 0.076 -> {Dstar[fname]}")
check("P2 a D with D + m_e in (0,1) MeV reproduces r0 = 0.076 (F0_rel), all r0 finite", Dstar["F0_rel"] is not None and all(np.isfinite(v[0]) for v in rows.values()) and Dstar["F0_rel"] < 0.48)
shift = None
if Dstar["F0_rel"] is not None:
    Tc, hf, _ = spectrum(Dstar["F0_rel"], F0_rel, "f"); _, hb, _ = spectrum(Dstar["F0_rel"], F0_rel, "b")
    pf, pb = peak(Tc, hf), peak(Tc, hb)
    shift = 100*(pf - pb)/pf
    print(f"  at D* = {Dstar['F0_rel']:+.4f} MeV (D*+me = {Dstar['F0_rel']+me:.4f}): peak_f {pf:.3f}, peak_b {pb:.3f}, shift {shift:.1f} %")
    # mixed spectra, NEMO-3 parametrisation, normalised
    print("  mixed (Eq. 8), normalised peak position vs sin^2 chi:")
    Wf_ = hf.sum(); Wb_ = hb.sum()
    for s2 in (0.0, 0.25, 0.5, 0.75, 1.0):
        mix = (1 - s2)**2*hf + s2**2*hb
        print(f"    sin^2chi = {s2:.2f}: peak {peak(Tc, mix):.3f} MeV")
check("P3 peak shift at D* is 15 +- 5 %", shift is not None and 10 <= shift <= 20)

# P4: HSD-like = large D (K = L = const) fermionic width vs SSD at D*
def width(Tc, h):
    m = (Tc*h).sum()/h.sum()
    return sqrt(((Tc - m)**2*h).sum()/h.sum())
Tc, hs, _ = spectrum(Dstar["F0_rel"] if Dstar["F0_rel"] is not None else -0.3, F0_rel, "f")
_, hh, _ = spectrum(50.0, F0_rel, "f")
print(f"\n  fermionic sum-spectrum rms width: SSD {width(Tc, hs):.4f} MeV vs HSD-like (D=50) {width(Tc, hh):.4f} MeV")
check("P4 SSD fermionic spectrum wider than HSD-like (paper: 'slightly wider')", width(Tc, hs) > width(Tc, hh))

n = len(checks); k = sum(ok for _, ok, _ in checks)
cf = [c for c in checks if c[2]]; kcf = sum(ok for _, ok, _ in cf)
print(f"\nSCORE {k}/{n}  (can-fail {kcf}/{len(cf)}; {n-len(cf)} controls)")
