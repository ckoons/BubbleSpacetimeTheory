#!/usr/bin/env python3
"""
Toy 5844 — round 19: once interactions give γ ≠ 0, is an odd-H² operator generated? (Elie, 2026-09-29). Prereg c1cb2ded.
Family/sources: φ = 4D scalar GFF Δ = 5/2 (H²'s 4D piece, class (χ_t,χ_s) = (−1,+1), toy 5834); σ = massless scalar ladder Δ = 1 (+,+);
ψ = Weyl ladder Δ = 3/2 (−,−). Integer-[g] vertices: gφ²σ, hσ³, λφ⁴ (+ μσ⁴ for convergence); Yukawa yψψσ.
"""
import numpy as np, itertools
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
# (1) 0-dimensional model, non-perturbative (numerical integration on an ASYMMETRIC grid, so φ -> −φ symmetry is not imposed by the grid)
phi = np.linspace(-7.9, 8.3, 2601); sig = np.linspace(-6.0, 7.1, 2201)
P, S_ = np.meshgrid(phi, sig, indexing='ij'); dA = (phi[1] - phi[0])*(sig[1] - sig[0])
def moments(g, h, lam, mu, eps=0.0):
    S = P**2/2 + S_**2/2 + g*P**2*S_ + h*S_**3 + lam*P**4 + mu*S_**4 + eps*P*S_**2
    w = np.exp(-(S - S.min())); Z = w.sum()*dA
    m = lambda f: (f*w).sum()*dA/Z
    return {'phi': m(P), 'phi_sig': m(P*S_), 'phi3': m(P**3), 'phi_sig2': m(P*S_**2), 'phi2': m(P**2)}
free = moments(0, 0, 0, 0)
inter = moments(0.3, 0.2, 0.1, 0.1)
gam = inter['phi2'] - free['phi2']
odd = max(abs(inter[k]) for k in ('phi', 'phi_sig', 'phi3', 'phi_sig2'))
print(f"   free <φ²> = {free['phi2']:.10f};  interacting <φ²> = {inter['phi2']:.10f}  (renormalisation {gam:+.6f})")
print(f"   interacting odd moments: " + ", ".join(f"<{k}> = {inter[k]:.2e}" for k in ('phi', 'phi_sig', 'phi3', 'phi_sig2')))
check("(1) interactions DO renormalise φ (the γ-analogue ⟨φ²⟩ − 1 ≠ 0)", abs(gam) > 1e-3, f"{gam:+.4f}")
check("(1) KILL NOT FIRED: every odd-φ moment vanishes (≤ 1e-12) at finite coupling, non-perturbatively, on an asymmetric grid", odd < 1e-12, f"max {odd:.1e}")
for eps in (0.02, 0.05):
    o = moments(0.3, 0.2, 0.1, 0.1, eps)
    print(f"   with an explicit odd vertex ε φσ², ε = {eps}: <φ> = {o['phi']:.4e}, <φσ²> = {o['phi_sig2']:.4e}")
o1, o2 = moments(0.3, 0.2, 0.1, 0.1, 0.02), moments(0.3, 0.2, 0.1, 0.1, 0.05)
check("(1) SENSITIVITY: an explicitly added odd vertex makes odd moments nonzero and ∝ ε (ratio ≈ 2.5)",
      abs(o1['phi']) > 1e-4 and abs(o2['phi']/o1['phi'] - 2.5) < 0.05, f"ratio {o2['phi']/o1['phi']:.3f}")
# (2) diagram leg parity, all orders: E = Σ v − 2I for the field in question
def parities(vertex_legs, maxv=6):
    out = set()
    for n in range(1, maxv + 1):
        for combo in itertools.combinations_with_replacement(vertex_legs, n):
            tot = sum(combo)
            for I in range(0, tot//2 + 1): out.add((tot - 2*I) % 2)
    return out
check("(2) even-φ vertex set {φ²σ, σ³, φ⁴}: only EVEN external φ counts at every order (≤ 6 vertices)", parities([2, 0, 4]) == {0})
check("(2) CONTROL fermion number: Yukawa ψψσ and (ψψ)² give only EVEN external ψ counts", parities([2, 4]) == {0})
check("(2) SENSITIVITY: adding one odd vertex (φσ²) produces odd external φ counts", 1 in parities([2, 0, 4, 1]))
# (3) the central-element distinction, from 5834's computed classes
H2 = (-1, +1); ladders = {(+1, +1), (-1, -1)}
h2parity = {H2: 1, (+1, +1): 0, (-1, -1): 0}           # number of H² quanta mod 2 for one H² quantum vs ladder products
chis_only = {}
for cls, par in h2parity.items(): chis_only.setdefault(cls[1], set()).add(par)
check("(3) fermion parity = χ_s (the spatial 2π rotation, central in Lorentz): the ladders' fermion parity IS χ_s (5834: χ_t = χ_s on ladders)",
      all(c[0] == c[1] for c in ladders))
check("(3) H²-parity is NOT a function of χ_s: χ_s = +1 carries both H² (odd) and boson products (even). Once the clock χ_t is broken "
      "(Cal S1011), no Lorentz-central element enforces it", chis_only[+1] == {0, 1})
print("\nREADING: interactions renormalise the fields (γ ≠ 0) but never generate an odd-H² amplitude from an even vertex set, at any order —")
print("Keeper's 'broken at the order where γ enters' is FALSE as stated. The protection is not a surviving central element (unlike fermion")
print("parity = χ_s): it is the Z2 of the leading vertex set, an ACCIDENTAL symmetry, exact to all orders in those couplings, violable only by")
print("an explicitly added odd vertex. Beyond the free point, dimensional analysis no longer forbids that vertex — nor any other.")
print(f"\nSCORE: {sum(score)}/{len(score)}")
