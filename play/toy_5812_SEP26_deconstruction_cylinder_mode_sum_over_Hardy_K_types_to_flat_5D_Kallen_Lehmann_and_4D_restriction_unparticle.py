#!/usr/bin/env python3
"""
Toy 5812 — deconstruction: BST's boundary two-point function from the discrete clock ladder to the flat continuum (Elie, 2026-09-26).
Prereg bc903cb1.
INVARIANTS: the K-type content (λ1,λ2) of the module at weight Δ (Hardy Δ = 5/2: all λ, mult 1; Rac Δ = 3/2: λ2 = 0 only);
the clock weights Δ + n; the flat Källén–Lehmann exponent ρ(μ²) ∝ (μ²)^{Δ − D/2}.
(a) Compact realization, cylinder R x S^4 (R = 1, τ = log|x|):  (2cosh τ − 2cos θ)^{−Δ} = Σ_n e^{−(Δ+n)τ} C_n^Δ(cos θ),
    C_n^Δ = Σ_{ℓ ≡ n (2)} c_{nℓ} C_ℓ^{3/2}  (C^{3/2} = S^4 zonal harmonics; ℓ = λ1 − λ2, n − ℓ = 2λ2).
(b) Rac control: at Δ = 3/2 only ℓ = n.  (c) Wrong multiplicity (drop λ2 >= 1 at Δ = 5/2) fails.
(d) Flat 5D: ∫ dμ² (μ²)^{Δ−5/2} G5_μ(r) ∝ r^{−2Δ}; deconstructed (μ² = s(k+½)) sum converges as s -> 0.
(e) 4D restriction: G5_μ restricted = ∫ dM² w(M²,μ²) G4_M, so ρ4 ∝ (M²)^{Δ−2}: continuous, no gap.
"""
import sympy as sp, mpmath as mp
mp.mp.dps = 30
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
x = sp.Symbol('x')
def decomp(n, D):
    Cn = sp.expand(sp.gegenbauer(n, D, x))
    ls = list(range(n, -1, -2)); cs = sp.symbols(f'c0:{len(ls)}')
    ex = sp.expand(Cn - sum(c*sp.gegenbauer(l, sp.Rational(3, 2), x) for c, l in zip(cs, ls)))
    sol = sp.solve(sp.Poly(ex, x).coeffs(), cs, dict=True)[0]
    return {l: sol[c] for c, l in zip(cs, ls)}
H = sp.Rational(5, 2); Rac = sp.Rational(3, 2)
okH = all(all(v > 0 for v in decomp(n, H).values()) for n in range(13))
print("   Δ=5/2 level n=4: c_{4ℓ} =", decomp(4, H))
check("(a) Δ=5/2: every level n decomposes into ALL S^4 zonal harmonics ℓ = n, n−2, … with POSITIVE coefficients (each Hardy K-type once), n ≤ 12", okH)
okR = all(all((v == 0) == (l != n) for l, v in decomp(n, Rac).items()) for n in range(13))
check("(b) CONTROL Rac Δ=3/2: only ℓ = n survives (λ2 = 0: the Wallach K-types), coefficients of ℓ < n vanish exactly", okR)
# numeric mode sum vs closed form (finite R: τ = log|x| on the cylinder)
def closed(t, th, D): return (2*mp.cosh(t) - 2*mp.cos(th))**(-D)
def modesum(t, th, D, N, only_top=False):
    s = mp.mpf(0)
    for n in range(N):
        if only_top:   # keep only ℓ = n: coefficient (D)_n/(3/2)_n times C_n^{3/2}
            s += mp.e**(-(D+n)*t) * mp.rf(D, n)/mp.rf(1.5, n) * mp.gegenbauer(n, 1.5, mp.cos(th))
        else:
            s += mp.e**(-(D+n)*t) * mp.gegenbauer(n, D, mp.cos(th))
    return s
t0, th0 = mp.mpf('0.3'), mp.mpf('0.7')
err = abs(modesum(t0, th0, 2.5, 400)/closed(t0, th0, 2.5) - 1)
check("(a) finite-R mode sum over the clock ladder 5/2 + n reproduces (2cosh τ − 2cos θ)^{−5/2} (τ=0.3, θ=0.7, N=400)", err < 1e-12, f"rel err {mp.nstr(err, 3)}")
# (c) wrong multiplicity at Δ=5/2, approaching the flat (short-distance = R -> ∞) limit
rat = []
for eps in ('0.2', '0.1', '0.05'):
    e = mp.mpf(eps); N = int(60/e)
    rat.append(modesum(e, e, 2.5, N, only_top=True)/closed(e, e, 2.5))
print("   wrong multiplicity / true at separation ε = 0.2, 0.1, 0.05:", [mp.nstr(v, 6) for v in rat])
check("(c) CONTROL: dropping the λ2 ≥ 1 K-types at Δ = 5/2 does NOT reproduce the correlator, and the ratio does not → 1 as R→∞ (ε→0)",
      all(abs(v - 1) > 0.05 for v in rat) and abs(rat[-1] - 1) >= abs(rat[0] - 1) - 1e-6)
rac = [modesum(mp.mpf(e), mp.mpf(e), 1.5, int(60/mp.mpf(e)), only_top=True)/closed(mp.mpf(e), mp.mpf(e), 1.5) for e in ('0.2', '0.05')]
check("(b') at Δ = 3/2 the top-only sum IS the full correlator (the Rac has only λ2 = 0)", all(abs(v-1) < 1e-10 for v in rac))
# (d) flat 5D Källén–Lehmann
def G5(mu, r):   # Euclidean massive propagator in D = 5
    z = mu*r
    if z == 0: return mp.gamma(1.5)/(4*mp.pi**2.5*r**3)
    return (1/(2*mp.pi)**2.5) * (mu/r)**1.5 * mp.besselk(1.5, z)
def KL5(D, r):
    a = D - 2.5
    return mp.quad(lambda m2: m2**a * G5(mp.sqrt(m2), r), [0, 1/r**2, 10/r**2, mp.inf])
sl = [ (mp.log(KL5(2.5, 2.0)) - mp.log(KL5(2.5, 1.0)))/mp.log(2), (mp.log(KL5(3.5, 2.0)) - mp.log(KL5(3.5, 1.0)))/mp.log(2)]
check("(d) flat 5D: density (μ²)^{Δ−5/2} gives |x|^{−2Δ}: log-slopes −5 (Δ=5/2, FLAT density) and −7 (Δ=7/2)",
      abs(sl[0] + 5) < 1e-10 and abs(sl[1] + 7) < 1e-10, f"{[mp.nstr(v, 12) for v in sl]}")
# deconstruction: μ² = s(k + 1/2), k = 0..; converge as s -> 0 at fixed r = 1
exact = KL5(2.5, 1.0); errs = []
# run 1 stopped the tower at μ² = 60 (a 1.2 % TAIL error, not a spacing error) — sum to μ² = 2500 in floats (scipy)
import numpy as np
from scipy.special import kv
def G5f(mu, r): return (1/(2*np.pi)**2.5)*(mu/r)**1.5*kv(1.5, mu*r)
for s_ in (1.0, 0.1, 0.01):
    k = np.arange(int(2500/s_)); m2 = s_*(k+0.5)
    errs.append(abs(np.sum(s_*G5f(np.sqrt(m2), 1.0))/float(exact) - 1))
print("   deconstruction rel. error at spacing s = 1, 0.1, 0.01:", [mp.nstr(v, 3) for v in errs])
check("(d) the discrete tower (spacing s) converges to the continuum as s → 0 (errors decrease, last < 1e-3)",
      errs[0] > errs[1] > errs[2] and errs[2] < 1e-3)
# Rac control in flat 5D: density eps*(μ²)^{-1+eps} -> δ(μ²): KL -> massless G5(0,r) ∝ r^{-3}
# run 1 integrated ε m^{-1+ε} directly (quadrature missed the endpoint mass) — substitute u = m^ε on [0,1]: ε m^{-1+ε} dm = du
def rac_ratio(e):
    low = mp.quad(lambda u: G5(mp.sqrt(u**(1/e)), 1.0) if u > 0 else G5(0, 1.0), [0, mp.mpf('0.5'), 1])
    high = mp.quad(lambda m2: e*m2**(-1+e)*G5(mp.sqrt(m2), 1.0), [1, 10, mp.inf])
    return (low + high)/G5(0, 1.0)
rc = [rac_ratio(e) for e in (mp.mpf('0.1'), mp.mpf('0.01'), mp.mpf('0.001'))]
print("   Rac: ε(μ²)^{−1+ε} density / massless propagator:", [mp.nstr(v, 6) for v in rc])
check("(b'') CONTROL Rac in flat 5D: the density concentrates at μ² = 0 and the correlator → the free massless field (ratio → 1)",
      abs(rc[-1] - 1) < abs(rc[0] - 1) and abs(rc[-1] - 1) < 0.02)
# (e) 4D restriction: G5_μ(r) = c ∫_{μ²}^∞ dM² (M²−μ²)^{−1/2} G4_M(r)  (KK: integrate the 5th momentum)
def G4(M, r): return (1/(4*mp.pi**2)) * (M/r) * mp.besselk(1, M*r)
def G5_from_4(mu, r):
    return mp.quad(lambda M2: (M2 - mu**2)**(-0.5) * G4(mp.sqrt(M2), r), [mu**2, mu**2 + 1, mu**2 + 20, mp.inf])
cs = [G5(mu, r)/G5_from_4(mu, r) for mu, r in ((mp.mpf(1), mp.mpf(1)), (mp.mpf(2), mp.mpf('0.5')), (mp.mpf('0.5'), mp.mpf(2)))]
# NOTE (run 1, kept as scored): the identity holds with ONE constant at all three points; my guessed constant 1/π is wrong — it is 1/(2π)
check("(e) restriction identity: G5_μ = c·∫_{μ²}^∞ (M²−μ²)^{−1/2} G4_M with ONE constant c (= 1/π) at three (μ, r)",
      max(cs) - min(cs) < 1e-15*abs(cs[0]) + 1e-20 and abs(cs[0] - 1/mp.pi) < 1e-12, f"c = {[mp.nstr(v, 15) for v in cs]}")
# ⇒ ρ4(M²) = (1/π) ∫_0^{M²} (μ²)^{Δ−5/2} (M²−μ²)^{−1/2} dμ² = (1/π) B(Δ−3/2, 1/2) (M²)^{Δ−2}
def rho4(M2, D): return mp.quad(lambda m2: m2**(D-2.5) * (M2 - m2)**(-0.5), [0, M2])/(2*mp.pi)
ex4 = (mp.log(rho4(4, 2.5)) - mp.log(rho4(1, 2.5)))/mp.log(4)
check("(e) 4D density ρ4 ∝ (M²)^{Δ−2} = (M²)^{1/2} at Δ = 5/2: continuous from 0, NO gap (the restricted tower is an unparticle-type continuum)",
      abs(ex4 - 0.5) < 1e-12 and rho4(mp.mpf('1e-6'), 2.5) > 0, f"exponent {mp.nstr(ex4, 12)}")
print("\nREADING: the compact (cylinder) realization is a discrete clock ladder 5/2 + n whose levels carry EXACTLY the Hardy K-types;")
print("the flat realization is its R → ∞ (short-distance) limit, a continuous 5D density (flat in μ² at Δ = 5/2), and on the 4D")
print("hyperplane a (M²)^{1/2} continuum with no gap. The Rac is the massless free field. A gap needs a scale (5804, Lyra R6 item 4).")
print(f"\nSCORE: {sum(score)}/{len(score)}")
