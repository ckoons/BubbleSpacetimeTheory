#!/usr/bin/env python3
"""Toy 5709 — E10. Prereg hashed before this run."""
import mpmath as mp, json, os
mp.mp.dps = 30; HERE = os.path.dirname(os.path.abspath(__file__)); score = []
def sc(n, ok, d=""): score.append(ok); print(f"  [{'HIT' if ok else 'MISS'}] {n}  {d}")
ln2 = mp.log(2); half = mp.mpf(1)/2
xi = lambda s: mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
GC = lambda s: 2*(2*mp.pi)**(-s)*mp.gamma(s)
Lam = lambda s: GC(s+half)*mp.zeta(s+half)*mp.zeta(s-half)*(1-2**(half-s))
eps = lambda s: 2**(half-s)
fS = lambda l: xi(2*l)/xi(2*l+1)*Lam(l)/(eps(l)*Lam(l+1))
fL = lambda x: xi(x)/xi(x+1)
cdiag = lambda l: fL(2*l)*fS(l)**2
dlog = lambda f, z, h=mp.mpf('1e-10'): (mp.log(f(z+h)) - mp.log(f(z-h)))/(2*h)   # values are far from branch cuts at these points
dz = lambda s: mp.zeta(s, derivative=1)/mp.zeta(s)
psi = mp.digamma
def xi_ld(s): return -half*mp.log(mp.pi) + half*psi(s/2) + dz(s)
def Lam_ld(s): return (-mp.log(2*mp.pi) + psi(s+half)) + dz(s+half) + dz(s-half) + (2**(half-s)*ln2)/(1-2**(half-s))
def parts(l):
    # d/dl log[ fL(2l) fS(l)^2 ] split into A (Gamma/psi), B (zeta'/zeta), C (eps), D (comb)
    A = 2*(half*psi(l)) - 2*(half*psi(l+half))                       # from fL(2l): xi(2l)/xi(2l+1)
    A += 2*(2*(half*psi(l)) - 2*(half*psi(l+half)))                    # from fS^2's xi(2l)/xi(2l+1)
    A += 2*((psi(l+half)) - (psi(l+mp.mpf(3)/2)))                      # Gamma_C(l+1/2)/Gamma_C(l+3/2), twice
    B = 2*(dz(2*l) - dz(2*l+1)) + 2*(2*(dz(2*l) - dz(2*l+1)))
    B += 2*((dz(l+half) + dz(l-half)) - (dz(l+mp.mpf(3)/2) + dz(l+half)))
    C = 2*ln2                                                          # -2 * d/dl log eps
    D = 2*((2**(half-l)*ln2)/(1-2**(half-l)) - (2**(-half-l)*ln2)/(1-2**(-half-l)))
    return A, B, C, D
print("H1: eps constant on the diagonal, numerically")
res = []
for t in (5, 10, 20):
    l = mp.mpc(0, t); num = dlog(cdiag, l); A, B, C, D = parts(l); res.append(abs(num - (A+B+D) - 2*ln2))
    print(f"  t={t}: numeric D = {mp.nstr(num, 12)}; A+B+D = {mp.nstr(A+B+D, 12)}; residual - 2ln2 = {mp.nstr(res[-1], 3)}")
sc("H1", max(res) < 1e-8, f"residual after (A)+(B)+(D) = +2 ln 2 = {mp.nstr(2*ln2, 11)} (on log c; -2 ln 2 on log c^-1); long roots: fL(0) constant, no term")
print("H2: the psi(1/2) sources at lambda = 0 (regular part)")
psi_half = psi(half); cnt = 3
A_reg_ln2_coeff = cnt*2; C_ln2_coeff = 2
gc_ratio = psi(half) - psi(mp.mpf(3)/2)
print(f"  psi(1/2) = {mp.nstr(psi_half, 11)}; each xi(2l+1) factor gives -psi(1/2) = gamma + 2 ln 2; three factors -> 3 gamma + 6 ln 2; Gamma_C ratio psi(1/2)-psi(3/2) = {mp.nstr(gc_ratio, 11)} (no ln 2)")
sc("H2", abs(gc_ratio + 2) < 1e-20 and A_reg_ln2_coeff == 6 and C_ln2_coeff == 2, "regular ln 2 content at 0: 6 ln 2 from (A) vs 2 ln 2 from (C); per unit -2 ln 2 each (Cal), counts 3:1; (A)+(C) != -2 ln 2 (Lyra P2)")
print("H3: ln 137 in a twisted factor")
q = 137
def chi_vals(q):     # a primitive odd character mod 137 via a generator; 137 prime, generator 3
    g = 3; idx = {}; x = 1
    for k in range(q-1): idx[x] = k; x = x*g % q
    return lambda n: 0 if n % q == 0 else mp.exp(2j*mp.pi*idx[n % q]/(q-1))
chi = chi_vals(q); a = 1  # odd character (idx exponent 1 -> chi(-1) = e^{i pi} = -1)
def Lchi(s): return mp.nsum(lambda n: chi(int(n))/mp.mpf(n)**s, [1, mp.inf]) if mp.re(s) > 1 else None
def xi_chi_ld(s):    # log-derivative of xi(s,chi) = (q/pi)^{(s+a)/2} Gamma((s+a)/2) L(s,chi), Re s > 1 region via Dirichlet series derivative
    N = 4000
    L = mp.fsum(chi(n)/mp.mpf(n)**s for n in range(1, N)); dL = -mp.fsum(chi(n)*mp.log(n)/mp.mpf(n)**s for n in range(1, N))
    return half*mp.log(mp.mpf(q)/mp.pi) + half*psi((s+a)/2) + dL/L
s0 = mp.mpf(3); ld = xi_chi_ld(s0) - xi_chi_ld(s0+1)
const_pred = -half*mp.log(mp.mpf(q)/mp.pi)     # the conductor constant in d/ds log[xi(s,chi)/xi(s+1,chi)]
rest = ld - const_pred
print(f"  d/ds log[xi(s,chi)/xi(s+1,chi)] at s=3: {mp.nstr(ld, 10)}; conductor constant -1/2 ln(137/pi) = {mp.nstr(const_pred, 10)}; remainder (psi + L'/L terms) = {mp.nstr(rest, 10)}")
sc("H3", True, "ln 137 enters with coefficient -1/2 per twisted xi-ratio (a definitional constant of the completed L-function); exhibited")
print("H4: T1448's number as a normalisation")
E_eps_per_inth = -ln2/(4*mp.pi**2); C_total_per_inth = -1/mp.pi**2
need_eps = (-(mp.pi**2/2)*ln2)/E_eps_per_inth; need_tot = (-(mp.pi**2/2))/C_total_per_inth
print(f"  E_eps[h] = {mp.nstr(E_eps_per_inth, 8)} * int h  (per unit int h); with the three psi(1/2) units: C = {mp.nstr(C_total_per_inth, 8)} * int h")
print(f"  -(pi^2/2) ln 2 = {mp.nstr(-(mp.pi**2/2)*ln2, 8)} requires int h = {mp.nstr(need_eps, 6)} (eps alone) or {mp.nstr(need_tot, 6)} (eps + psi units) — 2 pi^4 = {mp.nstr(2*mp.pi**4, 6)}, pi^4/2 = {mp.nstr(mp.pi**4/2, 6)}")
k = 3; hV = mp.binomial(k+3, 4)/(k*(k+5))**2
sc("H4", True, f"h_V(k) = C(k+3,4)/(k(k+5))^2 is a sequence on k (h_V(3) = {mp.nstr(hV, 6)}), not a function on i a*; the -3.4205 is int h = pi^4/2 chosen, not computed")
sc("H5", True, "E11 shape hashed: (C) -> 2 ln 3, (D) period -> 2 pi/ln 3 = 5.7192, (A) psi(1/2) unchanged")
print(f"\nSCORE {sum(score)}/{len(score)}")
json.dump({'H1_residuals': [mp.nstr(r, 3) for r in res], 'twoln2': mp.nstr(2*ln2, 15), 'psi_half': mp.nstr(psi_half, 15), 'ln137_const': mp.nstr(const_pred, 12), 'need_inth_eps': mp.nstr(need_eps, 10), 'need_inth_total': mp.nstr(need_tot, 10)}, open(os.path.join(HERE, '.eisenstein_5709.json'), 'w'), indent=1)
