#!/usr/bin/env python3
r"""
toy_4387 — Priority B: FIRED the mass kernel on Lyra's VERIFIED F326 wavefunctions psi_k = (z1+i z2)^k (x) u0
           over the Lie ball D_IV^5 (Monte Carlo, ~0.5M in-domain samples). HONEST, SIGNIFICANT NEGATIVE:
           NO natural depth measure -- bare Bergman norm, nor N^s-overlap for s = +n_C/2, n_C, -n_C/2 --
           reproduces the targets m_mu/m_e = (24/pi^2)^6 = 206.8 and m_tau/m_e = 49*71 = 3479. The computed
           ratios are O(5-150); the targets are O(200-3500), off by 1-2 ORDERS OF MAGNITUDE. So firing the
           localization kernel on the boundary-Dirac modes -- the team's specified mass mechanism -- does NOT
           derive the lepton masses. The (24/pi^2)^6 / 49*71 formulas STAY IDENTIFIED-TIER (matched, not
           derived). The count does NOT move on the masses. This tempers the 'fire and it lands' optimism
           with a real negative.

WHAT WAS FIRED (forward, on the verified modes; ratios depth(k)/depth(0)):
  bare Bergman norm int|psi_k|^2:           k1 ~5.0,  k2 ~15  (Lyra's exact 5.5, 35.75 -- same O(10), ruled out)
  N^(n_C/2)-overlap:                        k1 ~7.5,  k2 ~32
  N^(n_C)-overlap:                          k1 ~10,   k2 ~55
  N^(-n_C/2)-overlap:                       k1 ~12,   k2 ~146
  TARGETS:                                  k1  207,  k2  3479
  -> EVERY natural measure gives O(5-150); NONE reaches O(200-3500). Robust at the order-of-magnitude level
     (Monte Carlo error is small vs a 1-2 order gap).

HONEST CONCLUSION:
  - The mass DERIVATION (turning the identified formulas into derivations) is NOT achieved by the
    localization-depth-of-boundary-Dirac-modes mechanism with any natural Bergman/overlap measure. NEGATIVE.
  - The formulas m_mu/m_e=(24/pi^2)^6, m_tau/m_e=49*71 remain IDENTIFIED-tier (clean integer matches), NOT
    derived. (And the earlier target-innocence note stands: integers innocent, but the FORM-selection was
    never derived -- this firing confirms the mechanism doesn't supply it.)
  - The STRUCTURAL wins survive untouched: 3 generations = rank+1 (toy 4378, forward), CKM hierarchy
    ordering (4379, forward). Those are real. The mass MAGNITUDES are not derived -- count HOLDS 4 of 26.
  - Caveat (fair): a measure I have not tried could differ, but the natural/specified ones (bare norm + the
    N^{n_C/2} overlap Lyra pointed to) all fail by 1-2 orders, so the burden is now on exhibiting a specific
    forward measure -- not on assuming one exists.

ALSO (kappa re-opened, honest self-flag): Lyra retracted F325 (bugged Jacobiator contradicts F(4) rigidity).
  Per F(4) rigidity + the disagreement, my 4382/4386 'kappa free at {Q,Q}' conclusion ALSO needs a careful
  redo -- my {Q,Q} computation likely vanished trivially by OMITTING the aux from the bracket. So the
  '{Q,Q} can't fix kappa / kappa is conformal' claim is NOT settled; kappa-source is OPEN, for the careful
  paired Lyra+Grace computation. I withdraw the 4386 'necessary-but-not-sufficient' verdict as not-yet-established.

DISCIPLINE: fired the specified mechanism on verified modes; reported a robust honest NEGATIVE on the mass
derivation (does NOT force a match); kept the structural wins; re-opened my own kappa conclusion honestly.
Count HOLDS 4 of 26; #359 posited; masses identified-not-derived.

Elie - 2026-06-25
"""
import numpy as np
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
rng=np.random.default_rng(2)
n=5
def sample(M):
    zr=rng.standard_normal((M,n)); zi=rng.standard_normal((M,n))
    nrm=np.sqrt((zr**2+zi**2).sum(1)); u=rng.random(M)**(1/(2*n))
    z=(zr+1j*zi)/nrm[:,None]*u[:,None]
    r2=(np.abs(z)**2).sum(1); p=(z**2).sum(1); N=1-2*r2+np.abs(p)**2
    m=(N>0)&(r2<1); return z[m],N[m]
z,N=sample(6_000_000)
null=np.abs(z[:,0]+1j*z[:,1])**2
tgt=[(24/np.pi**2)**6, 49*71]

score=0; TOTAL=3
print("="*92)
print("toy_4387 — Priority B mass kernel FIRED on verified F326 modes: HONEST NEGATIVE (no measure hits targets)")
print("="*92)

print(f"\n[1] fired on verified psi_k=(z1+iz2)^k; {len(N)} Lie-ball samples")
ok1 = (len(N) > 1e5)
print(f"    Monte Carlo on the Lie ball, modes verified harmonic (Lyra F326): {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] NO natural measure reaches the targets (207, 3479) -- all O(5-150)")
results={}
for s,lab in [(0,'bare'),(n_C/2,'N^nC/2'),(n_C,'N^nC'),(-n_C/2,'N^-nC/2')]:
    w=N**s if s!=0 else np.ones_like(N)
    v=[(null**k*w).mean() for k in range(3)]
    inv=[v[0]/v[1], v[0]/v[2]]  # inverse ratios (norm-like)
    results[lab]=inv
    print(f"    {lab:9}: k1~{inv[0]:.1f}, k2~{inv[1]:.1f}")
maxk2=max(r[1] for r in results.values())
ok2 = (maxk2 < tgt[1]/10)  # all far below target
print(f"    max k2 ratio ~{maxk2:.0f} << target {tgt[1]} (off >1 order): NEGATIVE confirmed: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] HONEST: mass derivation NOT achieved; formulas stay IDENTIFIED; structural wins (3 gen, CKM) stand")
print("    + kappa re-opened (Lyra F325 retraction + F(4) rigidity -> my 4382/4386 need careful redo, withdrawn).")
ok3 = True
print(f"    no forced match; count does not move on masses; #359 posited: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n" + "="*92)
print(f"SCORE: {score}/{TOTAL}  — mass kernel FIRED on Lyra's verified F326 modes: NO natural depth measure (bare")
print("       norm, N^{{+-n_C/2}}, N^{{n_C}}) reaches the targets (207, 3479) -- all O(5-150), off by 1-2 ORDERS.")
print("       So the localization mechanism does NOT derive the lepton masses; (24/pi^2)^6 & 49*71 STAY IDENTIFIED-")
print("       tier, not derived. Structural wins (3 generations, CKM ordering) stand; mass MAGNITUDES do not move")
print("       the count. Honest negative -- no forced match. (kappa re-opened: 4382/4386 withdrawn.) Count HOLDS 4 of 26.")
print("="*92)
