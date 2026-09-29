#!/usr/bin/env python3
"""
Toy 5847 — a clock label e^{2πiΔ} vs an action Z2 under an interacting fusion (Elie, 2026-09-29, round 21). Prereg 0e2b68d9.
Model (group/source stated): critical transverse-field Ising chain H = −Σ σᶻσᶻ − Σ σˣ on a ring; Z2: Q = ∏σˣ. Solved exactly by Jordan–Wigner
(sector assignment CHECKED against exact diagonalisation at L = 8). Δ = (E − E0)·L/(2πv), v measured from the dispersion.
Stand-in, not BST: it tests the mechanism (a clock phase vs an action symmetry across an interacting fusion), not BST's labels.
"""
import numpy as np
from functools import reduce
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
# (1) exact diagonalisation, L = 8
L = 8
sx = np.array([[0, 1], [1, 0.]]); sz = np.diag([1., -1.]); I2 = np.eye(2)
def site(op, i): return reduce(np.kron, [op if j == i else I2 for j in range(L)])
H = -sum(site(sz, i) @ site(sz, (i + 1) % L) for i in range(L)) - sum(site(sx, i) for i in range(L))
Q = reduce(np.kron, [sx]*L)
check("(1) [H, Q] = 0 exactly (L = 8): Q = ∏σˣ is a symmetry of the Hamiltonian (the 'action Z2')", np.abs(H @ Q - Q @ H).max() < 1e-12)
Pp, Pm = (np.eye(2**L) + Q)/2, (np.eye(2**L) - Q)/2
def sector_levels(P):
    ev, U = np.linalg.eigh(P @ H @ P + 1e3*(np.eye(2**L) - P)); return np.sort(ev[ev < 500])
Eev, Eodd = sector_levels(Pp), sector_levels(Pm)
# free-fermion spectrum: ε_k = 4|sin(k/2)|; NS k = 2π(n+½)/L, R k = 2πn/L; parity-projected many-body levels
def ff_levels(ks, parity):
    eps = 4*np.abs(np.sin(np.array(ks)/2)); E0 = -0.5*eps.sum(); lv = []
    for mask in range(2**len(ks)):
        occ = [(mask >> j) & 1 for j in range(len(ks))]
        if sum(occ) % 2 == parity: lv.append(E0 + sum(e for e, o in zip(eps, occ) if o))
    return np.sort(lv)
NS = [2*np.pi*(n + 0.5)/L for n in range(L)]; R = [2*np.pi*n/L for n in range(L)]
match = {}
for lab, ks in (("NS", NS), ("R", R)):
    for par in (0, 1):
        lv = ff_levels(ks, par)
        match[(lab, par)] = (np.allclose(lv[:10], Eev[:10]), np.allclose(lv[:10], Eodd[:10]))
ev_sec = [k for k, v in match.items() if v[0]]; od_sec = [k for k, v in match.items() if v[1]]
check("(1) Jordan–Wigner sectors CHECKED against ED: Q = +1 ↔ NS even-parity, Q = −1 ↔ R odd-parity (lowest 10 levels each)",
      ("NS", 0) in ev_sec and ("R", 1) in od_sec, f"Q+ ↔ {ev_sec}, Q− ↔ {od_sec}")
# (2) dimensions from exact finite-size gaps, large L (no many-body enumeration needed: ground states and few-particle levels)
def dims(L):
    ns = 2*np.pi*(np.arange(L) + 0.5)/L; r = 2*np.pi*np.arange(L)/L
    e_ns = 4*np.abs(np.sin(ns/2)); e_r = 4*np.abs(np.sin(r/2))
    E0 = -0.5*e_ns.sum(); E0R = -0.5*e_r.sum()                           # R odd-parity ground: the k = 0 zero mode (ε = 0) occupied
    v = 2.0*(np.sin(np.pi/L)/(np.pi/L))                                  # measured group velocity at the lowest mode, → 2
    kmin = np.pi/L; ek = 4*np.sin(kmin/2)
    u = L/(2*np.pi*2.0)
    return (E0R - E0)*u, 2*ek*u, ek*u
Ls = np.array([64, 128, 256, 512, 1024])
D = np.array([dims(l) for l in Ls])
fit = lambda y: np.polyfit(1/Ls**2, y, 1)[1]
ds, de, dpsi = fit(D[:, 0]), fit(D[:, 1]), fit(D[:, 2])
print(f"   extrapolated (1/L² fit): Δ_σ = {ds:.8f}, Δ_ε = {de:.8f}, Δ_ψ = {dpsi:.8f}   (L = 1024 raw: {np.round(D[-1], 8)})")
check("(2) dimensions from the exact spectrum: Δ_σ = 1/8, Δ_ε = 1, Δ_ψ = 1/2 (to 1e-6)", abs(ds - 0.125) < 1e-6 and abs(de - 1) < 1e-6 and abs(dpsi - 0.5) < 1e-6)
# (3) lattice fusion: σᶻσᶻ (two Q-odd operators) is a term of H: Q σᶻᵢσᶻᵢ₊₁ Q = +σᶻᵢσᶻᵢ₊₁ while Q σᶻ Q = −σᶻ
s1 = site(sz, 0); s12 = site(sz, 0) @ site(sz, 1)
check("(3) Q-charge multiplicative across σ×σ ∋ ε: Qσᶻ Q = −σᶻ, Q(σᶻσᶻ)Q = +σᶻσᶻ (the energy density, a term of H)",
      np.allclose(Q @ s1 @ Q, -s1) and np.allclose(Q @ s12 @ Q, s12))
c = lambda d: np.exp(2j*np.pi*d)
gap = abs(c(ds)**2 - c(de))
print(f"   clock label: c(σ)² = {np.round(c(ds)**2, 6)}, c(ε) = {np.round(c(de), 6)}  → |difference| = {gap:.4f}")
check("(4) the clock label e^{2πiΔ} is NOT multiplicative across the interacting fusion σ×σ ∋ ε (|c(σ)² − c(ε)| = √2)", abs(gap - np.sqrt(2)) < 1e-5)
gap0 = abs(c(dpsi)**2 - c(de))
check("(5) CONTROL free sector: ψ×ψ ∋ ε (fermion bilinear) — c(ψ)² = c(ε): the label IS multiplicative where fusion is free", gap0 < 1e-5, f"{gap0:.1e}")
print("\nREADING: in an interacting fusion (σ×σ ∋ ε with 2Δ_σ = 1/4 ≢ Δ_ε = 1 mod 1) a clock-phase label does not multiply, while the")
print("Hamiltonian's Z2 (Q) is exactly multiplicative; in the free fermion sector both hold. The mechanism Lyra's (b) names, computed.")
print(f"\nSCORE: {sum(score)}/{len(score)}")
