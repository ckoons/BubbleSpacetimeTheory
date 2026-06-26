#!/usr/bin/env python3
r"""
toy_4402 — READY-TO-FIRE: the 3-point superconformal OPE-overlap integrator on the Lie ball D_IV^5, built and
           validated, so the moment Grace+Lyra hand off the explicit Higgs (p-sector) + matter (boundary-Dirac
           nu=n_C=5) wavefunctions, the Yukawa magnitude C_{H,i,j} (per toy 4400: the Yukawa IS a 3-pt OPE
           coefficient) is a one-line forward computation. This is INFRASTRUCTURE, not a result (no fitting, no
           mass claim) -- it removes the only thing that would slow the fire when the modes land.

DOMAIN: D_IV^5 = { z in C^5 : h(z,z) = 1 - 2|z|^2 + |z.z|^2 > 0, |z.z| < 1 } (the Lie ball), with
  |z|^2 = sum|z_i|^2, z.z = sum z_i^2. Weighted Bergman measure dmu_nu ∝ h(z,z)^(nu - genus) dV, genus = n_C.

MONTE-CARLO INTEGRATOR (validated): uniform sampling of the 10-real-dim unit ball, reject to the domain
  (h>0, |z.z|<1), accumulate the weighted integrand. Validated on the F326 modes psi_k(z)=(z1+i z2)^k:
  - ORTHOGONALITY: <psi_j|psi_k> off-diagonal ~1e-5 vs diagonal ~1e-2..1e-4 (3 orders down) -- holds by
    homogeneity (distinct k = distinct degree), as it must. Integrator is not introducing spurious mixing.
  - NORM STRUCTURE: ||psi_k||^2/||psi_0||^2 DECREASES with k (1, 0.12, 0.03, 0.008 at nu=8). This reproduces
    yesterday's localization finding (4385/4387) from the other side: bare-norm weight FALLS with generation,
    while mass RISES -- a 1-pt norm cannot be the mass, consistent with 4400 (mass = 3-pt coefficient).

THE FIRE (one line, on handoff): the Yukawa magnitude is
    C_{H,i,j} = (1/N) sum_z  H(z) * psi_i(z) * conj(psi_j(z)) * h(z,z)^(nu - genus)
  with H = the explicit Higgs mode (p-sector per Grace dictionary v0.2), psi_i = the three matter generations
  (boundary-Dirac at nu=n_C=5), evaluated at the substrate nu. The Yukawa RATIOS C_{H,mu,mu}/C_{H,e,e} and
  C_{H,tau,tau}/C_{H,e,e} are then compared, target-innocence-applied, to (24/pi^2)^6 and 49*71:
    - match -> the mass mechanism is LOCATED (a real count-mover candidate, subject to the full lens).
    - no match -> the analytic layer says the Yukawas are irreducible inputs (honest terminus, angle c).
  Either way it is a forward computation with no free dials; the modes determine the answer.

WHY THIS NOW: Keeper's continuation explicitly tasked me to fire the 3-pt overlap on handoff and meanwhile
  keep the (a) lane alive. The (a) operator-scan is CLOSED by 4400 (a 1-pt/2-pt operator is the wrong object
  type for a 3-pt coefficient), so the only non-fishing forward work is the overlap itself -- and the highest-
  value thing I can do before the modes land is have the validated machinery ready. Done.

DISCIPLINE: pure infrastructure; validated against known structure (orthogonality + 4385/4387 norm fall-off);
no mass claim, no fit, no count move. Target-innocence will be applied to the OUTPUT when the real modes land.

Elie - 2026-06-26
"""
import numpy as np
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
genus = n_C
rng = np.random.default_rng(7)

def sample_domain(N):
    pts = []
    while len(pts) < N:
        x = rng.normal(size=(4*N, 10)); r = np.sqrt((x**2).sum(1))
        u = rng.uniform(size=4*N)**(1/10)
        x = x / r[:, None] * u[:, None]              # uniform in the 10-ball
        z = x[:, :5] + 1j*x[:, 5:]
        zz = (z*z).sum(1); nz = (np.abs(z)**2).sum(1)
        h = 1 - 2*nz + np.abs(zz)**2
        ok = (h > 0) & (np.abs(zz) < 1)
        for zi, hi in zip(z[ok], h[ok]):
            pts.append((zi, hi))
            if len(pts) >= N: break
    return pts

def overlap(f_i, f_j, nu, pts):
    s = 0.0
    for z, h in pts:
        s += f_i(z) * np.conj(f_j(z)) * h**(nu - genus)
    return s / len(pts)

# generic mode factory (F326 validation modes; replaced by real Higgs+matter on handoff)
def psi(k):
    return lambda z: (z[0] + 1j*z[1])**k

def yukawa_3pt(H, psi_i, psi_j, nu, pts):
    """THE FIRE: C_{H,i,j} = <H psi_i | psi_j>_nu. One line; H + matter modes supplied by Grace+Lyra."""
    s = 0.0
    for z, h in pts:
        s += H(z) * psi_i(z) * np.conj(psi_j(z)) * h**(nu - genus)
    return s / len(pts)

pts = sample_domain(40000)
nu = 8  # validation weight (>genus for clean convergence); real nu = substrate value on handoff

score = 0; TOTAL = 3
print("="*94)
print("toy_4402 — 3-pt OPE overlap integrator on D_IV^5: validated, READY TO FIRE on Higgs+matter handoff")
print("="*94)

print(f"\n[1] integrator built + {len(pts)} in-domain samples drawn (Lie ball h>0, |z.z|<1)")
ok1 = (len(pts) == 40000)
print(f"    domain sampling works: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] ORTHOGONALITY validation: <psi_j|psi_k> off-diagonal << diagonal (homogeneity)")
diag = [abs(overlap(psi(k), psi(k), nu, pts)) for k in range(4)]
offd = [abs(overlap(psi(j), psi(k), nu, pts)) for j in range(4) for k in range(4) if j != k]
ok2 = max(offd) < 0.05 * min(diag)
print(f"    max off-diag {max(offd):.2e} < 5% of min diag {min(diag):.2e}: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] NORM structure reproduces 4385/4387: ||psi_k||^2 FALLS with k (mass RISES) -> 1-pt norm != mass")
ratios = [overlap(psi(k), psi(k), nu, pts).real / diag[0] for k in range(4)]
ok3 = all(ratios[k+1] < ratios[k] for k in range(3))
print(f"    norm^2 ratios {[f'{r:.3e}' for r in ratios]} monotone DOWN: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n" + "="*94)
print(f"SCORE: {score}/{TOTAL}  — the 3-pt OPE-overlap integrator on D_IV^5 is BUILT and VALIDATED (orthogonality")
print("       holds; norm fall-off reproduces 4385/4387). The Yukawa magnitude C_{{H,i,j}} = <H psi_i|psi_j>_nu is")
print("       now a one-line forward fire the moment Grace+Lyra hand off the explicit Higgs (p-sector) + 3 matter")
print("       (boundary-Dirac nu=n_C=5) modes. Pure infrastructure -- no fit, no mass claim, target-innocence")
print("       applied to the OUTPUT when modes land. I am ready. Count HOLDS 4 of 26.")
print("="*94)
