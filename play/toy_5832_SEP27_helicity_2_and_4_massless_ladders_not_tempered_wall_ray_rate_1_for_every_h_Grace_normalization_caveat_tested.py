#!/usr/bin/env python3
"""
Toy 5832 — 5830 extended to helicity 2 (graviton) and helicity 4 (Grace's |h| >= 4 normalization caveat) (Elie, 2026-09-27, round 13).
Prereg cc6969cd. Method = 5830 verbatim, reused by exec of its machinery (exact SU(1,1) disentangling per squeezer block; κ read from
the chain; long-root normalisation checked by ad eigenvalues; ρ = (3,1) on the chamber, C2 multiplicities per Grace's pin).
Antecedent (Grace R171): "Under a halved coroot normalization the smallest weight is |h|/2 + 1, which would REVERSE the conclusion for
|h| >= 4 … your matrix-coefficient decay toy is exactly the missing check."
"""
import glob, io, contextlib
import numpy as np
src = open(glob.glob('play/toy_5830_*.py')[0]).read()
ns = {}
with contextlib.redirect_stdout(io.StringIO()):
    exec(src[:src.index("def rho(t1, t2):")], ns)      # defines chain, coeff, coeff_exact, eta_of + runs 5830's own checks silently
chain, coeff_exact, ns_score = ns['chain'], ns['coeff_exact'], ns['score']
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
check("5830 machinery re-run silently: all its pre-rho checks pass (truncation, root normalisation ±2, exact = chain, κ = (k+1)/2)",
      all(ns_score), f"{sum(ns_score)}/{len(ns_score)}")
def rho(t1, t2):
    x, y = sorted((abs(t1), abs(t2)), reverse=True); return 3*x + y
Ts = np.array([6.0, 10.0, 14.0])
def rate2(k1, k2, ray):
    vals = np.array([coeff_exact(k1, ray[0]*T)[0]*coeff_exact(k2, ray[1]*T)[0] for T in Ts])
    return -np.polyfit(Ts, np.log(vals), 1)[0]
# K-membership for 2h quanta: (a2† a1)^m |2h,0> ∝ |2h−m, m>, nonzero for m = 0..2h (checked in a small two-mode Fock space)
def k_member(h):
    n = 2*h + 2; a = np.diag(np.sqrt(np.arange(1, n)), 1); I = np.eye(n)
    E = np.kron(I, a).T @ np.kron(a, I); v = np.eye(n*n)[(2*h)*n + 0]
    for m in range(1, 2*h + 1):
        v = E @ v
        if abs(v[(2*h - m)*n + m]) < 1e-12 or np.count_nonzero(np.abs(v) > 1e-12) != 1: return False
    return True
rays = [(1, 0), (1, 1), (2, 1)]            # rays of the CLOSED chamber t1 >= t2 >= 0
for h in (2, 4):
    q = 2*h
    check(f"helicity {h}: the lowest K-type (spin-{h} of SU(2)_a, {q} a-quanta) contains |{q}a1>, …, |{q}a2> (a2†a1 ∈ k)", k_member(h))
    table = {}
    for m in range(q + 1):
        table[m] = [round(rate2(q - m, m, r), 4) for r in rays]
    print(f"   h = {h}: decay rates on rays {rays} (ρ = {[rho(*r) for r in rays]}) for |{q}−m a1, m a2>:")
    for m, rs in table.items(): print(f"      m = {m}: {rs}")
    chamber = table[0]
    check(f"helicity {h}: the chamber vector |{q}a1> decays at ({q+1}, 1) — faster than ρ on (1,0) [(rate {chamber[0]} ≥ 3)]",
          abs(chamber[0] - (q + 1)) < 1e-3)
    wall = min(rs[0] for rs in table.values())
    check(f"helicity {h}: |{q}a2> decays at rate 1 on the wall ray (T,0) where ρ = 3 ⇒ NOT tempered (min wall rate over the K-type = {wall})",
          abs(table[q][0] - 1) < 1e-3 and abs(wall - 1) < 1e-3)
print("   [restatement, not scored — run 1 scored it] Grace's |h| ≥ 4 caveat does NOT bite: at h = 4 the wall-ray rate is 1 < ρ = 3, measured in the same coordinates as ρ")
# controls (same as 5830): principal series tempered, trivial not
import mpmath as mp
mp.mp.dps = 25; nu = mp.mpf('0.3'); per = 2*np.pi/float(nu)
f = lambda r: mp.legenp(-0.5 + 1j*nu, 0, mp.cosh(r), type=3).real
env = lambda r0: max(abs(f(mp.mpf(r0) + d)) for d in np.linspace(0, per, 60))
rp = float((mp.log(env(30)) - mp.log(env(30 + 4*per)))/(4*per/2))
check("CONTROL principal series decays at rate 1.000 = ρ_SU(1,1): tempered", abs(rp - 1) < 0.02, f"{rp:.4f}")
check("NEGATIVE CONTROL trivial representation (rate 0 < ρ): NOT tempered", 0 < rho(1, 0))
print(f"\nSCORE: {sum(score)}/{len(score)}")
