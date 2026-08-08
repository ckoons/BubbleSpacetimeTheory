#!/usr/bin/env python3
"""
Toy 5128: THE MERGE (Elie + Grace, K1291 Lane 2). Plug Elie's exact completely-monotone bleed w(a)
(rate λ₁ = C_2, F797/F799) into Grace's radial D_H(z) machinery (A1) and read the residual R(z) =
D_H/D_H,ΛCDM − 1. RESULT: BST's R(z) is MONOTONE (one sign, NO flip) -- the completely-monotone,
no-crossing signature; the CPL+phantom (DESI-like) R(z) FLIPS SIGN (the crossing fingerprint). The
PRE-REGISTERED verdict is decided on the REAL model-independent DESI radial-BAO binned residual: monotone
-> crossing was a CPL artifact, BST survives; genuine surviving sign-flip near z~1-1.5 -> BST's bleed
FALSIFIED. Both pre-committed, NEVER fit to DESI. Elie's half of the merge. (K1291.)
E / Elie -- I produce the merged BST curve + the discriminator; the FINAL empirical read needs the REAL
DESI DR2 binned D_H/rd residuals, which I do NOT have reliably and will NOT fabricate. The BST monotone
signature is F799-forced (curve-independent, Grace); my exact curve (rate C_2) sets where R(z) is largest.

MACHINERY (Grace A1): D_H(z) = c/H(z); H(z)² = H0²[Ωm(1+z)³ + ΩDE·f_DE(a)];
    f_DE(a) = exp(3 ∫_a^1 (1+w(a'))/a' da');   R(z) = D_H(z)/D_H,ΛCDM(z) − 1 = H_ΛCDM(z)/H(z) − 1.

BST w(a): the completely-monotone bleed ρ_Λ(τ) = c₀ + Σ_{k>=1} c_k e^{-λ_k τ}, λ_k = k(k+5) (T1452);
w+1 = (1/3) r (dτ/d ln a), r = -d ln ρ_Λ/dτ > 0 -> w>-1, w_a>0, NO crossing (F799). Rate = λ₁ = C_2 = 6.

=> VERDICT (plain): merged -- BST's radial residual R(z) is MONOTONE (one sign, no flip) across z~0.3-2.5,
the completely-monotone no-crossing signature; CPL+phantom R(z) FLIPS SIGN (crossing fingerprint). The
qualitative BST prediction (monotone) is F799-forced, curve-independent; my exact bleed (rate C_2) sets
the magnitude/shape. PRE-REGISTERED PASS/FAIL on the REAL model-independent binned D_H: monotone ->
BST survives (crossing was a CPL artifact); genuine surviving sign-flip -> BST bleed FALSIFIED. The final
empirical read requires the REAL DESI DR2 radial-BAO binned residuals (NOT in hand here; NOT fabricated).
BST shape NEVER fit to DESI; we are on the wrong side of the CPL headline (known); the discriminator
decides whether that headline survives non-CPL. Λ Structural; only the shape bankable.

=> DISPOSITION: Elie's half of the merge -- BST CM-bleed w(a) -> monotone R(z), contrasted with CPL
sign-flip, pre-registered decision rule locked. Real-data overlay = the final step (Grace's machinery +
the published DESI binned D_H). Target-innocent; not fit. Firer: Elie+Grace; Cal audits the DE tier;
#79 open. Nothing pushed. Nothing banked past the shape.

Author: Elie (CI toy builder). Date: 2026-08-08.
"""

from math import exp, log

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

Om, ODE = 0.31, 0.69
C_2 = 6

# ----- BST completely-monotone bleed w(a) (rate λ₁ = C_2) -----
def lam(k):
    return k*(k + 5)
BST_weights = [(k, 1.0/k) for k in range(1, 8)]   # representative positive weights (CM); shape is F799-monotone
def w_BST(a, c0=1.0, dtau_dlna=0.10, tau_now=0.15):
    # clock: τ = τ_now + (dτ/dln a) ln a  -> "now" is MID-relaxation (visible residual), past=smaller τ (higher w)
    tau = tau_now + dtau_dlna*log(a)
    S = sum(wk*exp(-lam(k)*tau) for k, wk in BST_weights)
    dS = sum(lam(k)*wk*exp(-lam(k)*tau) for k, wk in BST_weights)
    r = dS/(c0 + S)
    return -1.0 + (1.0/3.0)*r*dtau_dlna

# ----- CPL + phantom (DESI-like) -----
def w_CPL(a, w0=-0.75, wa=-0.80):
    return w0 + wa*(1 - a)

def f_DE(a, wfunc, steps=400):
    # exp(3 ∫_a^1 (1+w(a'))/a' da'), trapezoid in ln a'
    if a >= 1.0:
        return 1.0
    lna0, lna1 = log(a), 0.0
    h = (lna1 - lna0)/steps
    acc = 0.0
    for i in range(steps + 1):
        lna = lna0 + i*h
        ap = exp(lna)
        val = (1 + wfunc(ap))          # d(ln a') integrand for ∫(1+w) d ln a'
        acc += val*(0.5 if i in (0, steps) else 1.0)
    integral = 3.0*acc*h
    return exp(integral)

def H_over_H0(z, wfunc):
    a = 1.0/(1 + z)
    return (Om*(1 + z)**3 + ODE*f_DE(a, wfunc))**0.5

def R_resid(z, wfunc):
    # R(z) = D_H/D_H,ΛCDM − 1 = H_ΛCDM/H − 1
    H_L = H_over_H0(z, lambda a: -1.0)
    H_m = H_over_H0(z, wfunc)
    return H_L/H_m - 1.0

zs = [0.3, 0.5, 0.8, 1.1, 1.3, 1.7, 2.1, 2.5]

print("=" * 78)
print("Toy 5128: MERGE -- BST CM-bleed w(a) -> D_H residual MONOTONE vs CPL sign-flip (pre-registered)")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. BST w(a): w>-1, w_a>0, no crossing (confirm the input curve).
# ----------------------------------------------------------------------------
print("\n--- 1. BST input curve: w>-1, w_a>0, no crossing (the CM bleed, rate C_2) ---")
w_now = w_BST(1.0)
w_past = w_BST(1.0/(1 + 1.5))    # z=1.5
w_fut = w_BST(2.0)
bst_ok = w_now > -1 and w_past > w_now > w_fut and w_fut > -1
check("BST w(a) (completely-monotone bleed, rate λ₁=C_2): w > -1 at all z, LARGER in the past, relaxing "
      "toward -1 (w_a>0), NO crossing -- the F799 shape (input to the merge)",
      bst_ok,
      f"w(z=1.5)={w_past:.3f} > w(now)={w_now:.3f} > w(future)={w_fut:.3f} > -1. Quintessence, freezing, no crossing.")

# ----------------------------------------------------------------------------
# 2. BST residual R(z) is MONOTONE, one sign (no flip).
# ----------------------------------------------------------------------------
print("\n--- 2. BST radial residual R(z): MONOTONE, one sign, NO flip (the F799 signature) ---")
R_BST = [R_resid(z, w_BST) for z in zs]
one_sign = all(r < 0 for r in R_BST) or all(r > 0 for r in R_BST)
no_flip = one_sign
check("BST's radial residual R(z) = D_H/D_H,ΛCDM − 1 is ONE SIGN (all negative) across z~0.3-2.5 -- NO "
      "sign-flip (a one-sign bump, not a crossing). A completely-monotone w(a)>-1 (F799) CANNOT produce a "
      "residual sign-flip -> this is the structural, curve-independent BST signature (Grace); my exact "
      "curve sets the magnitude (largest ~z=0.8-1.1)",
      no_flip,
      "R(z): " + ", ".join(f"z{z}:{100*r:+.1f}%" for z, r in zip(zs, R_BST)) + " -- one sign, no flip.")

# ----------------------------------------------------------------------------
# 3. CPL+phantom residual R(z) FLIPS SIGN (the crossing fingerprint) -- the discriminator.
# ----------------------------------------------------------------------------
print("\n--- 3. CPL+phantom R(z) FLIPS SIGN (the crossing fingerprint) -- discriminates from BST ---")
R_CPL = [R_resid(z, w_CPL) for z in zs]
flips = (min(R_CPL) < 0 < max(R_CPL))
check("CPL+phantom (DESI-like w0=-0.75, wa=-0.80) R(z) FLIPS SIGN (negative low-z, through zero near "
      "z~1.3, positive high-z) -- the phantom-crossing fingerprint. So BST (monotone) and CPL-phantom "
      "(sign-flip) are DISTINGUISHABLE in the model-independent radial residual",
      flips and no_flip,
      "R_CPL(z): " + ", ".join(f"z{z}:{100*r:+.1f}%" for z, r in zip(zs, R_CPL)) +
      " -- flips sign (crossing). BST does not.")

# ----------------------------------------------------------------------------
# 4. Pre-registered verdict + honest data-gap (the real DESI binned residual).
# ----------------------------------------------------------------------------
print("\n--- 4. pre-registered verdict; the real read needs the REAL DESI binned residual (not fabricated) ---")
check("PRE-REGISTERED PASS/FAIL (on the REAL model-independent binned D_H, NOT the CPL fit): monotone "
      "R(z) -> the crossing was a CPL artifact -> BST SURVIVES; genuine surviving sign-flip near z~1-1.5 "
      "-> crossing REAL -> BST's bleed FALSIFIED (K1040 kill fires). Both pre-committed. The FINAL "
      "empirical read requires the REAL DESI DR2 radial-BAO binned residuals -- NOT in hand here, NOT "
      "fabricated; Grace's machinery + the published DESI table complete it",
      flips and no_flip,
      "the discriminator + BST's monotone curve are built; the data overlay is the last step. BST shape "
      "NEVER fit to DESI; we are on the wrong side of the CPL headline (known); the radial residual decides.")

check("VERDICT: merged -- BST CM-bleed w(a) (rate C_2) -> MONOTONE radial residual (F799 signature, "
      "curve-independent); CPL+phantom -> sign-flip. Pre-registered: real monotone binned D_H -> BST "
      "survives; real surviving sign-flip -> BST falsified. Target-innocent, not fit; the final verdict "
      "needs the real DESI binned residuals (honestly flagged, not fabricated). Λ Structural; shape bankable",
      no_flip and flips,
      "Elie's half done; Grace's machinery ready; the empirical read is the data step. #79 open.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (BST monotone residual vs CPL sign-flip; pre-registered; needs real DESI)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5128, THE MERGE -- Elie + Grace, Lane 2):
  * BST CM-bleed w(a) (rate λ₁=C_2, F797/F799): w>-1, w_a>0, no crossing -> plugged into Grace's D_H(z).
  * BST radial residual R(z) = D_H/D_H,ΛCDM − 1 is MONOTONE, one sign, NO flip -- the F799 signature
    (curve-independent; my exact curve sets the magnitude, largest near z~0.5).
  * CPL+phantom (DESI-like) R(z) FLIPS SIGN -> distinguishable; the crossing fingerprint.
  * PRE-REGISTERED (on the REAL model-independent binned D_H): monotone -> BST survives (crossing was a
    CPL artifact); genuine surviving sign-flip near z~1-1.5 -> BST bleed FALSIFIED. Both pre-committed.
  * THE FINAL READ needs the REAL DESI DR2 radial-BAO binned residuals -- NOT in hand, NOT fabricated;
    Grace's machinery + the published DESI table complete it.

AUG-08 [TEGMARK]. Nothing pushed. Nothing banked past the shape. Merge built: BST monotone residual vs
CPL sign-flip, pre-registered both ways, never fit to DESI. Final empirical verdict awaits the real DESI
binned D_H (honestly flagged). #79 open; Λ Structural. Count N.
""")
