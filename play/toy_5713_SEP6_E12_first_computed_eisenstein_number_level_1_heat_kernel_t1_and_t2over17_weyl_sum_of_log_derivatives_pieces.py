#!/usr/bin/env python3
"""Toy 5713 — E12 (prereg shape b7164474; h from Lyra L12 fb411aef): E0[h] = -(1/4pi^2)(1/8) ∫ Σ_w ∂log c(w,iτ) h_t(τ) d²τ,
∂ = ∂1+∂2, h_t(τ) = exp(-t(|τ|²+17/2)) (heat-kernel spectral function; ∫h = (π/t)e^{-17t/2}). Pieces reported separately:
eps (exact ln 2·∫h·(Weyl weight)), psi (A), zeta'/zeta (B), comb (D). Symmetric grid (PV-symmetric about the singular lines)."""
import mpmath as mp, numpy as np, json, os, time, itertools
mp.mp.dps = 20; HERE = os.path.dirname(os.path.abspath(__file__)); t0 = time.time()
half = mp.mpf(1)/2; ln2 = mp.log(2)
psi = mp.digamma
def dz(s): return mp.zeta(s, derivative=1)/mp.zeta(s)
def xi_ld_parts(s):    # (A, B) parts of xi'/xi(s)
    return (-half*mp.log(mp.pi) + half*psi(s/2), dz(s))
def fL_parts(x):       # d/dx log fL(x), fL = xi(x)/xi(x+1): returns (A,B,C,D)
    a1, b1 = xi_ld_parts(x); a2, b2 = xi_ld_parts(x+1); return (a1-a2, b1-b2, mp.mpf(0), mp.mpf(0))
def fS_parts(l):       # d/dl log fS(l); the zeta(l+1/2) ratio cancels analytically
    a1, b1 = xi_ld_parts(2*l); a2, b2 = xi_ld_parts(2*l+1)
    A = 2*(a1-a2) + (psi(l+half) - psi(l+mp.mpf(3)/2))
    B = 2*(b1-b2) + (dz(l-half) - dz(l+mp.mpf(3)/2))
    C = ln2
    D = (2**(half-l)*ln2)/(1-2**(half-l)) - (2**(-half-l)*ln2)/(1-2**(-half-l))
    return (A, B, C, D)
# Weyl group of B2 as signed permutations; inversion sets of the positive roots e1-e2, e1+e2, e1, e2
roots = {'e1-e2': (1,-1), 'e1+e2': (1,1), 'e1': (1,0), 'e2': (0,1)}
def w_apply(w, v):
    (s1, s2, perm) = w; u = (v[perm[0]], v[perm[1]]); return (s1*u[0], s2*u[1])
def is_neg(v):  # negative root test in B2 positive system: first nonzero coordinate negative
    return (v[0] < 0) or (v[0] == 0 and v[1] < 0)
W = [(s1, s2, perm) for s1 in (1,-1) for s2 in (1,-1) for perm in ((0,1),(1,0))]
inv = [[name for name, v in roots.items() if is_neg(w_apply(w, v))] for w in W]
print("inversion sets:", inv)
def sum_w_parts(l1, l2):
    tot = [mp.mpf(0)]*4
    for I in inv:
        for name in I:
            if name == 'e1-e2': continue                       # (∂1+∂2) kills it
            if name == 'e1+e2': p = fL_parts(l1+l2); p = tuple(2*q for q in p)
            elif name == 'e1': p = fS_parts(l1)
            else: p = fS_parts(l2)
            tot = [tot[i] + p[i] for i in range(4)]
    return tot
results = {}
for t, n in ((mp.mpf(1), 40), (mp.mpf(1), 56), (mp.mpf(2)/17, 40), (mp.mpf(2)/17, 56)):
    R = 6/mp.sqrt(t); hstep = 2*R/n
    # symmetric grid avoiding τ1=0, τ2=0, τ1+τ2=0 exactly: offsets at half-steps
    pts = [(-R + (i+half)*hstep, -R + (j+mp.mpf(1)/4)*hstep) for i in range(n) for j in range(n)]   # quarter offset on τ2: avoids τ1=0, τ2=0, τ1+τ2=0 exactly
    acc = [mp.mpf(0)]*4; inth = mp.mpf(0)
    for (a, b) in pts:
        hv = mp.exp(-t*(a*a + b*b + mp.mpf(17)/2)); inth += hv*hstep*hstep
        p = sum_w_parts(mp.mpc(0, a), mp.mpc(0, b))
        for i in range(4): acc[i] += p[i]*hv*hstep*hstep
    pref = -1/(4*mp.pi**2)/8
    E = [pref*acc[i] for i in range(4)]
    inth_exact = mp.pi/t*mp.exp(-mp.mpf(17)*t/2)
    eps_exact = pref*(8*ln2)*inth_exact          # each short root inverted by 4 of 8 elements: Σ_w C = 8 ln2
    print(f"\nt = {mp.nstr(t,6)}: ∫h (grid) = {mp.nstr(inth,10)}  exact (π/t)e^(-17t/2) = {mp.nstr(inth_exact,10)}")
    print(f"  E_eps = {mp.nstr(E[2],10)} (exact {mp.nstr(eps_exact,10)}) = -(ln 2/4π²)·∫h")
    print(f"  E_psi = {mp.nstr(E[0],10)}   E_zeta = {mp.nstr(E[1],10)}   E_comb = {mp.nstr(E[3],10)}")
    tot = sum(E); print(f"  E0[h_t] (level 1, ∂=∂1+∂2, grid {n}x{n}, |τ|<={mp.nstr(R,4)}) = {mp.nstr(tot,10)}  (imag {mp.nstr(mp.im(tot),3)})  [{time.time()-t0:.0f}s]", flush=True)
    results[f'{mp.nstr(t,6)}_n{n}'] = {'inth_exact': mp.nstr(inth_exact,12), 'E_eps': mp.nstr(mp.re(E[2]),12), 'E_psi': mp.nstr(mp.re(E[0]),12), 'E_zeta': mp.nstr(mp.re(E[1]),12), 'E_comb': mp.nstr(mp.re(E[3]),12), 'E_total': mp.nstr(mp.re(tot),12), 'imag': mp.nstr(mp.im(tot),3)}
json.dump(results, open(os.path.join(HERE, '.eisenstein_5713.json'), 'w'), indent=1)
print("\nlevel 137: the ln 137 coefficient per unit ∫h is −(1/4π²)·(1/8)·Σ_w Σ_{twisted ξ-ratios in inverted factors}(−½)·(block average) — the block structure is L1 §4a's and is not evaluated here; the level-1 numbers above are the computed replacement.")
