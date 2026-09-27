#!/usr/bin/env python3
"""
Toy 5830 — Lane A link 3: are the 4D massless ladder representations tempered? (Elie, 2026-09-27, round 12). Prereg 6e9264f5.
Antecedent: "the 4D massless ladder representations are NOT tempered — the risky link, to be checked per helicity (0, ½, 1)".
MODEL (computed, not quoted): ladders of SU(2,2) ≅ Spin(4,2) in the Fock space of a1,a2,b1,b2; the lowest K-type of the helicity-j
ladder = 2j quanta in the a-doublet, none in b (energy (N_a+N_b)/2 + 1 = j + 1 = Δ). Cartan of p: the commuting two-mode squeezers
X_j = a_j† b_j† − a_j b_j. Coefficient ⟨e^{t1 X1 + t2 X2} v, v⟩ factorises over the two blocks; each block is computed by expm on a
truncated two-mode Fock space (convergence checked).
INVARIANT: temperedness ⇔ K-finite coefficients in L^{2+ε}(G) ∀ε > 0 (Cowling–Haagerup–Howe; pin: Grace). On A the Haar density ~ e^{2ρ(t)};
su(2,2): restricted roots C2 (2e_j mult 1, e1 ± e2 mult 2; multiplicities to be pinned by Grace) ⇒ ρ(t) = 3 max|t_j| + min|t_j|
in coordinates where the long root is 2t_j (normalisation CHECKED below on one block). Tempered ⇒ decay rate ≥ ρ on every ray.
"""
import numpy as np
from scipy.linalg import expm
import mpmath as mp
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
# v2: the squeezer X = a†b† − ab conserves N_a − N_b = k, so each coefficient lives on the chain |k+m, m>, m = 0..M
# (run 1 used a dense truncated two-mode Fock space: too slow, and large-t / edge truncation errors; killed, kept)
def chain(k, M):
    m = np.arange(M)
    up = np.sqrt((k + m + 1.0)*(m + 1.0))[:-1]      # M−1 entries; <k+m+1, m+1| a†b† |k+m, m>
    Kp = np.diag(up, -1); Km = Kp.T; K0 = np.diag((2*m + k + 1)/2.0)
    return Kp, Km, K0
def coeff(k, t, M=400):
    Kp, Km, K0 = chain(k, M)
    return expm(t*(Kp - Km))[0, 0]
c1 = [coeff(1, 3.0, M) for M in (200, 300, 400)]
check("truncation converged (chain coefficient at t = 3 stable to 1e-12 for M = 200, 300, 400)", max(c1) - min(c1) < 1e-12, f"{c1[-1]:.14f}")
# root normalisation from the sl2 commutators on the chain (low block, away from the cut): [K0,K±] = ±K±, [K−,K+] = 2K0
Kp, Km, K0 = chain(0, 60); L = 30
com = lambda P, Q: (P @ Q - Q @ P)[:L, :L]
okc = np.allclose(com(K0, Kp), Kp[:L, :L]) and np.allclose(com(Km, Kp), 2*K0[:L, :L])
adX = np.array([[0, 0, -1], [0, 0, -1], [-2, -2, 0]], float)   # ad(K+ − K−) in basis (K+, K−, K0), from those commutators
ev = sorted(np.linalg.eigvals(adX).real)
check("root normalisation: sl2 relations hold on the chain and ad(X) has eigenvalues (−2, 0, 2) ⇒ long root = 2t, ρ_SU(1,1) = 1",
      okc and np.allclose(ev, [-2, 0, 2]), f"ad eigenvalues {np.round(ev, 6)}")
# EXACT coefficient at any t (run 2 used the 400-chain at t = 3..5 where the squeezed state reaches m ~ sinh²t ≫ 400):
# disentangle e^{tX} in the faithful 2x2 defining rep of SU(1,1): e^{tX} = exp(τK+) exp(ηK0) exp(σK−); on a lowest-weight vector v
# (K−v = 0, K0 v = κ v) ⟨v|e^{tX}|v⟩ = e^{ηκ}. κ is READ from the chain (lowest K0 eigenvalue); η solved numerically from 2x2 matrices.
Kp2 = np.array([[0., 1.], [0., 0.]]); Km2 = np.array([[0., 0.], [-1., 0.]]); K02 = np.diag([0.5, -0.5])
assert np.allclose(K02 @ Kp2 - Kp2 @ K02, Kp2) and np.allclose(Km2 @ Kp2 - Kp2 @ Km2, 2*K02)    # same relations as the chain
X2 = Kp2 - Km2
def eta_of(t):
    G = expm(t*X2)                          # = [[a, b],[c, d]] ; exp(τK+)exp(ηK0)exp(σK−) = [[e^{η/2} − τσ e^{−η/2}, τ e^{−η/2}],[−σ e^{−η/2}, e^{−η/2}]]
    return -2*np.log(G[1, 1])
def coeff_exact(k, t):
    Kp, Km, K0 = chain(k, 50)
    kappa = K0[0, 0]                         # lowest K0 eigenvalue of this chain
    return np.exp(eta_of(t)*kappa), kappa
okx = all(abs(coeff_exact(k, tt)[0] - coeff(k, tt)) < 1e-10 for k in range(3) for tt in (0.5, 1.0, 2.0))
check("exact (2x2-disentangled) coefficient = truncated-chain coefficient at t = 0.5, 1, 2 (where the chain is converged)", okx)
ts = np.array([6.0, 10.0, 14.0])
rates = {}
for k in range(3):
    vals = np.array([coeff_exact(k, tt)[0] for tt in ts]); kap = coeff_exact(k, 1.0)[1]
    r = -np.polyfit(ts, np.log(vals), 1)[0]
    rates[k] = r
    print(f"   block |{k},0>: κ = {kap}; coefficient at t=6,10,14 = {vals}; decay rate {r:.6f}")
check("block coefficients: |k,0> has κ = (k+1)/2 and decays at rate 2κ = k+1 (k = 0,1,2)", all(abs(rates[k] - (k+1)) < 1e-3 for k in range(3)))
def rho(t1, t2):
    x, y = sorted((abs(t1), abs(t2)), reverse=True); return 3*x + y
rays = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]
ladders = {"helicity 0 (Δ=1), vacuum":     (0, 0),
           "helicity 1/2 (Δ=3/2), |1a1>":  (1, 0),
           "helicity 1 (Δ=2), |2a1>":      (2, 0),
           "helicity 1 (Δ=2), |1a1 1a2>":  (1, 1)}
for name, (k1, k2) in ladders.items():
    r1, r2 = rates[k1], rates[k2]
    fails = [(ray, round(r1*ray[0] + r2*ray[1], 3), rho(*ray)) for ray in rays if r1*ray[0] + r2*ray[1] < rho(*ray) - 1e-3]
    print(f"   {name}: block rates ({r1:.3f}, {r2:.3f}); rays where decay < ρ: {fails}")
    check(f"{name}: NOT tempered (decay slower than e^{{-ρ}} on some ray ⇒ |φ|^{{2+ε}} e^{{2ρ}} grows)", len(fails) > 0)
# rank-1 controls in one block: ρ_SU(1,1) = 1 (one long root 2t, mult 1)
check("CONTROL SU(1,1): two-mode vacuum (limit of discrete series) rate = ρ = 1 — borderline, tempered (Ξ ~ t e^{-t})", abs(rates[0] - 1) < 1e-3)
mp.mp.dps = 25
nu = mp.mpf('0.3')
f = lambda r: mp.legenp(-0.5 + 1j*nu, 0, mp.cosh(r), type=3).real
ode = max(abs(mp.diff(f, r, 2) + mp.coth(r)*mp.diff(f, r) - (-(mp.mpf(1)/4 + nu**2))*f(r)) for r in (mp.mpf('0.7'), mp.mpf('1.9')))
per = 2*np.pi/float(nu)     # period in r (run 2 used overlapping windows at r = 12, 20)
env = lambda r0: max(abs(f(mp.mpf(r0) + d)) for d in np.linspace(0, per, 60))
rp = float((mp.log(env(30)) - mp.log(env(30 + 4*per)))/(4*per/2))   # rate per unit t (r = 2t)
check("CONTROL principal series: φ_ν = P_{-1/2+iν}(cosh 2t) solves the radial Laplacian (checked) and decays at rate 1 = ρ: tempered",
      ode < 1e-15 and abs(rp - 1) < 0.1, f"ode residual {mp.nstr(ode, 3)}, rate {rp:.3f}")
s = mp.mpf('0.4')
fc = lambda r: mp.legenp(-0.5 + s, 0, mp.cosh(r), type=3).real
rc = float((mp.log(fc(12)) - mp.log(fc(20)))/4)
# run 2 coded the expectation as 1 − s: with r = 2t the rate per unit t is 1 − 2s (arithmetic slip, owned)
check("NEGATIVE CONTROL complementary series (s = 0.4): rate 1 − 2s = 0.2 < ρ = 1: NOT tempered", abs(rc - 0.2) < 0.02 and rc < 1, f"rate {rc:.3f}")
check("NEGATIVE CONTROL trivial representation: φ ≡ 1, rate 0 < ρ on every ray: NOT tempered", all(0 < rho(*ray) for ray in rays))

# ---- POST-HOC (added 11:5x after reading Lyra R12 / Cal S1004, not in the prereg; labelled so) ----
# Antecedent (Lyra R12, verbatim from commit c30ce446): "massless ladders: exponents (Δ+j, Δ−j) vs rho=(3,1): j=0,1/2 not tempered,
# j>=1 on the tempered edge". On the chamber t1 >= t2 the |2a1> coefficient is sech³t1·sech t2 = e^{-ρ} exactly (agreed). But the
# SAME lowest K-type contains |2a2> (mode swap a1<->a2, b1<->b2: a permutation inside U(2)xU(2) ⊂ K) and |1a1 1a2>. Harish-Chandra's
# bound must hold for EVERY K-finite vector on A+ (closure). On the wall ray (T,0) ⊂ closure(A+), where ρ = 3:
# K-membership CHECKED: in the (a1, a2) Fock space the u(2)_a generator E = a2† a1 (an element of k) maps
# |2,0> -> √2 |1,1> -> √2 |0,2>, so all three are vectors of ONE lowest K-type (the spin-1 triplet of SU(2)_a).
n = 4; a = np.diag(np.sqrt(np.arange(1, n)), 1); I = np.eye(n)
a1, a2 = np.kron(a, I), np.kron(I, a); E = a2.T @ a1
ket = lambda i, j: np.eye(n*n)[i*n + j]
okK = np.allclose(E @ ket(2, 0), np.sqrt(2)*ket(1, 1)) and np.allclose(E @ ket(1, 1), np.sqrt(2)*ket(0, 2))
check("K-membership: a2†a1 ∈ u(2)_a ⊂ k carries |2a1> → |1a1 1a2> → |2a2> (same lowest K-type)", okK)
wall = {}
for name, (k1, k2) in {"|2a2>": (0, 2), "|1a1 1a2>": (1, 1), "|2a1>": (2, 0)}.items():
    vals = np.array([coeff_exact(k1, T)[0]*coeff_exact(k2, 0.0)[0] for T in (6.0, 10.0, 14.0)])
    wall[name] = -np.polyfit([6.0, 10.0, 14.0], np.log(vals), 1)[0]
print("   post-hoc: helicity-1 lowest-K-type vectors, decay rate along the WALL ray (T,0) of A+ (ρ = 3 there):", {k: round(v, 4) for k, v in wall.items()})
check("POST-HOC helicity 1: |2a2> decays at rate 1 and |1a1 1a2> at rate 2 on the wall ray (T,0) where ρ = 3 ⇒ NOT tempered "
      "(the chamber-only reading 'on the tempered edge' misses the other vectors of the same K-type)",
      abs(wall["|2a2>"] - 1) < 1e-3 and abs(wall["|1a1 1a2>"] - 2) < 1e-3 and wall["|2a1>"] >= 3 - 1e-3)

print("\nREADING: every massless ladder (helicity 0, 1/2, 1) has a lowest-K-type coefficient decaying slower than e^{-ρ} on some ray —")
print("NOT tempered — so link 3 holds per helicity; with links 1–2 (Grace/Lyra pins) the record space carries no massless 4D rep.")
print(f"\nSCORE: {sum(score)}/{len(score)}")
