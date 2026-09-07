#!/usr/bin/env python3
"""Toy 5714 — CORRECTION of 5709 H3 (Cal §871's re-read request). For primitive chi mod 137 and xi(s,chi) = (137/pi)^{(s+a)/2}
Gamma((s+a)/2) L(s,chi): d/ds log[xi(s,chi)/xi(s+1,chi)] = ½ψ((s+a)/2) − ½ψ((s+a+1)/2) + L'/L(s) − L'/L(s+1) — the conductor
constant ½ ln(137/π) CANCELS. 5709 asserted it as a surviving constant; here the full log-derivative is compared with the
psi + L'/L remainder alone at three points, and the difference is reported."""
import mpmath as mp
mp.mp.dps = 25; q = 137; a = 1
g = 3; idx = {}; x = 1
for k in range(q - 1): idx[x] = k; x = x * g % q
chi = lambda n: 0 if n % q == 0 else mp.exp(2j * mp.pi * idx[n % q] / (q - 1))
N = 6000
def L(s): return mp.fsum(chi(n) / mp.mpf(n) ** s for n in range(1, N))
def dL(s): return -mp.fsum(chi(n) * mp.log(n) / mp.mpf(n) ** s for n in range(1, N))
def xi_ld(s): return mp.mpf(1)/2 * mp.log(mp.mpf(q) / mp.pi) + mp.mpf(1)/2 * mp.digamma((s + a) / 2) + dL(s) / L(s)
print("s      full d/ds log[xi(s,chi)/xi(s+1,chi)]        psi+L'/L remainder only       difference (= surviving conductor constant)")
worst = 0
for s in (mp.mpf(3), mp.mpf(4), mp.mpc(3, 2)):
    full = xi_ld(s) - xi_ld(s + 1)
    rem = mp.mpf(1)/2 * mp.digamma((s + a) / 2) - mp.mpf(1)/2 * mp.digamma((s + a + 1) / 2) + dL(s) / L(s) - dL(s + 1) / L(s + 1)
    d = full - rem; worst = max(worst, abs(d))
    print(f"{mp.nstr(s,3):8s} {mp.nstr(full, 12):>32s} {mp.nstr(rem, 12):>32s} {mp.nstr(d, 3):>12s}")
print(f"\nsurviving conductor constant in the ratio: {mp.nstr(worst, 3)}  (5709 H3 claimed −½ ln(137/π) = {mp.nstr(-mp.log(mp.mpf(q)/mp.pi)/2, 8)}) -> the claim is WITHDRAWN: no ln 137 and no ln π constant in a twisted xi-RATIO.")
print("Where a ln 137 CAN sit: only in an FE-normalisation of the twisted operator (Λ(s,χ) = ε(s,χ)Λ(1−s,χ̄) with ε = w(χ)·137^{½−s} when the conductor power is not carried in Λ) — the same status as E11's ln 2 / ln 3: a convention of the normalised operator, not a value of the unnormalised ratio.")
