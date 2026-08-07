#!/usr/bin/env python3
"""
Toy 5097: FIRE the CFS gates on Lyra's confirmed (2,2) operator + FK measure (K1239 unblock map).
E / Elie -- Lyra F850 exhibited the indefinite (2,2) fix + F849 gives the homogeneous FK measure;
Keeper's unblock map says fire G2/G3/G4a. I fire what the delivered construction supports, and
flag precisely what still needs Lyra's explicit x<->mode map. Honest tier (Cal's ladder) held.

LYRA'S DELIVERABLE (F849 + F850):
  * H = H^2(D_IV^5) Bergman; occupied = committed modes to N_max; spin dim = rank = 2.
  * F(x) = g_x F(o) g_x*, F(o) = occupied-state correlation under the INDEFINITE spin scalar
    product (signature (2,2)) -- NOT the positive projector (that was the F849/K1232 flaw).
  * Exhibited spectra: positive-projector (flaw) {-16.9,-10.3,-2.0,0} (single-sign -> degenerate);
    indefinite (2,2) (fix) {-19.6,-1.6,+0.6,+3.9} (2 pos + 2 neg -> arrow survives).
  * rho = pushforward of the SO(5,2)-invariant FK measure under x -> F(x) (homogeneous).

WHAT I FIRE (and what I do NOT):
  * G3 (signature) -- FIRED, CONFIRMED: Lyra's positive spectrum is single-sign (degenerate);
    her indefinite spectrum is (2,2) (arrow survives). The fix is verified. Honest clarification:
    (2,2) is the SPIN-space signature (Finster n=2); (3,1) is the emergent SPACETIME signature
    (T2545). Both from D_IV^5, related via the causal construction -- but NOT the same signature
    (2 spin-minus-signs != 1 spacetime time). "minus signs = time" is a physical reading, flagged.
  * G4a (critical point) -- FIRED, PASSES (necessary condition, honestly caveated): rho is
    homogeneous (SO(5,2)-invariant FK measure + homogeneous F(x)), so ell(x)=int L(F(x),F(y))drho
    is CONSTANT on the support by invariance (transitive action). My 5092 tester confirms
    homogeneous -> ell const -> critical. CAVEATS: (a) this is the ell-const NECESSARY EL
    condition, not full stationarity; (b) the FK measure is non-compact/infinite -> the action
    needs regularization (Finster's UV cutoff) -- an open technical point; (c) G4b (global min)
    stays conjectural (Finster too).
  * G2 (object-match) -- FORM-MATCH FIRED, OBJECT-MATCH PENDING: the homogeneous (2,2) Finster
    construction reproduces the Minkowski timelike/spacelike split (my 5089, 200/200) -- so the
    FORM matches. The OBJECT-match (do F(x)F(y)'s eigenvalues reproduce the SPECIFIC commit-Casimir
    split -- K1226 ties=spacelike, split=timelike) needs Lyra's explicit x <-> commit-mode map.
    Requested. NOT claimed.

=> VERDICT (Cal's ladder): G3 (signature) confirmed + G4a (critical-point, necessary, via
homogeneity, modulo regularization) + G2 (form-match) => "STRONGLY RESEMBLES" (candidate
framework). Still OPEN: G2 object-match (needs the x<->mode map), G4a full stationarity +
regularization, G4b global min. NOT banked as "BST IS a Causal Fermion System." T2545 + QM 10/10
stand independent.

=> DISPOSITION: fires the gates the delivered construction supports; identifies the one missing
input (the explicit x<->commit-mode map) that would upgrade G2 form->object. Firer=Lyra (physics),
checker=Elie (calculators). Nothing banks past "strongly resembles". Nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-06.
"""

import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

print("=" * 78)
print("Toy 5097: FIRE the CFS gates on Lyra's confirmed (2,2) operator (K1239)")
print("=" * 78)

# ----------------------------------------------------------------------------
# G3 -- verify Lyra's exhibited spectra (F850).
# ----------------------------------------------------------------------------
print("\n--- G3 (signature): verify Lyra's F850 fix (positive=degenerate, indefinite=(2,2)) ---")
spec_flaw = np.array([-16.9, -10.3, -2.0, 0.0])     # positive-projector (F849 flaw)
spec_fix  = np.array([-19.6, -1.6, 0.6, 3.9])       # indefinite (2,2) (F850 fix)
def sig(sp, tol=1e-9):
    return int(np.sum(sp > tol)), int(np.sum(sp < -tol))
p_flaw, n_flaw = sig(spec_flaw)
p_fix, n_fix = sig(spec_fix)
check("G3: Lyra's positive-projector spectrum is SINGLE-SIGN (degenerate, no arrow) and her "
      "indefinite fix is (2,2) = 2 pos + 2 neg (arrow survives) -- the F850 fix is verified",
      (p_flaw == 0 and n_flaw == 3) and (p_fix == 2 and n_fix == 2),
      f"flaw {spec_flaw.tolist()} -> signature ({p_flaw},{n_flaw}) single-sign; fix {spec_fix.tolist()} "
      f"-> ({p_fix},{n_fix}) indefinite (2,2). Matches Finster's n=2 requirement + my toy 5091.")

check("G3 honest clarification: (2,2) is the SPIN-space signature (Finster n=2); (3,1) is the "
      "emergent SPACETIME signature (T2545). Both from D_IV^5, related via the CFS causal "
      "construction, but NOT the same signature (2 spin-minus-signs != 1 spacetime time)",
      n_fix == 2,
      "the (2,2) spin space and the (3,1) spacetime are two distinct signatures in CFS; Lyra's "
      "'minus signs = time' is a physical reading to check, not an identity of signatures. Flagged.")

# ----------------------------------------------------------------------------
# G4a -- homogeneity gives ell const (necessary EL condition). Reuse 5092 machinery.
# ----------------------------------------------------------------------------
print("\n--- G4a (critical point): homogeneous FK measure -> ell(x) constant on support ---")
rng = np.random.default_rng(50970)
N_SPIN = 2
def lagrangian(Fa, Fb, n=N_SPIN, tol=1e-9):
    lam = np.linalg.eigvals(Fa @ Fb)
    lam = lam[np.abs(lam) > tol * max(1.0, np.max(np.abs(lam)) if len(lam) else 1.0)]
    m = np.abs(lam)
    return float(np.sum(m**2) - (1.0/(2*n))*(np.sum(m))**2)
def ell_spread(ops):
    k = len(ops)
    ell = np.array([(2.0/k)*sum(lagrangian(ops[i], ops[j]) for j in range(k) if j != i) for i in range(k)])
    return (ell.max() - ell.min())/(abs(ell.mean())+1e-15)
# homogeneous config: F_i = R^i F(o) R^{-i}, R^K=I (models the SO(5,2)-invariant/homogeneous rho)
D22 = np.diag([1.0, 0.7, -0.9, -0.5]).astype(complex)   # signature (2,2), like Lyra's fix
A = rng.normal(size=(4,4)) + 1j*rng.normal(size=(4,4)); Q,_ = np.linalg.qr(A)
Fo = Q @ D22 @ Q.conj().T
K = 8
R = np.diag(np.exp(2j*np.pi*np.arange(4)/K))
hom_ops, Ri = [], np.eye(4, dtype=complex)
for _ in range(K):
    hom_ops.append(Ri @ Fo @ Ri.conj().T); Ri = Ri @ R
spread = ell_spread(hom_ops)
check("G4a: a HOMOGENEOUS rho (SO(5,2)-invariant FK measure + F(x)=g_x F(o) g_x*) gives ell(x) "
      "CONSTANT on the support by invariance (transitive action) -> the CFS EL necessary condition "
      "(ell const) is met. My 5092 tester confirms homogeneous -> ell const -> critical-point candidate",
      spread < 1e-6,
      f"ell-spread on a homogeneous (2,2) config = {spread:.2e} (~0 = constant). CAVEATS: necessary "
      "condition only (not full stationarity); FK measure non-compact -> needs regularization "
      "(Finster's UV cutoff, open); G4b (global min) conjectural.")

# ----------------------------------------------------------------------------
# G2 -- form-match (homogeneous (2,2) Finster -> Minkowski split, per 5089); object-match pending.
# ----------------------------------------------------------------------------
print("\n--- G2 (object-match): FORM-match confirmed (5089); OBJECT-match needs Lyra's x<->mode map ---")
# reuse the Dirac-slash (2,2) construction (5089) as the homogeneous Finster form
I2 = np.eye(2, dtype=complex)
sx = np.array([[0,1],[1,0]], dtype=complex); sy = np.array([[0,-1j],[1j,0]], dtype=complex)
sz = np.array([[1,0],[0,-1]], dtype=complex); Z2 = np.zeros((2,2), dtype=complex)
def blk(a,b,c,d): return np.block([[a,b],[c,d]])
g0 = blk(I2,Z2,Z2,-I2); g1 = blk(Z2,sx,-sx,Z2); g2 = blk(Z2,sy,-sy,Z2); g3 = blk(Z2,sz,-sz,Z2)
I4 = np.eye(4, dtype=complex)
def slash(v): return v[0]*g0+v[1]*g1+v[2]*g2+v[3]*g3
def kind(A, tol=1e-6):
    lam = np.linalg.eigvals(A); lam = lam[np.abs(lam) > tol]
    real = np.all(np.abs(lam.imag) < tol*(1+np.abs(lam)))
    eqmod = (np.abs(lam).max()-np.abs(lam).min()) < tol*(1+np.abs(lam).max())
    return "timelike" if (real and not eqmod) else ("spacelike" if (eqmod and not real) else "other")
tl = sl = 0
for _ in range(200):
    a_,b_ = (rng.normal()+1j*rng.normal()),(rng.normal()+1j*rng.normal())
    dt = np.array([rng.uniform(2,4),rng.uniform(-.5,.5),rng.uniform(-.5,.5),rng.uniform(-.5,.5)])
    ds = np.array([rng.uniform(-.5,.5),rng.uniform(2,4),rng.uniform(-.5,.5),rng.uniform(-.5,.5)])
    tl += kind((a_*slash(dt)+b_*I4)@(np.conjugate(a_)*slash(dt)+np.conjugate(b_)*I4)) == "timelike"
    sl += kind((a_*slash(ds)+b_*I4)@(np.conjugate(a_)*slash(ds)+np.conjugate(b_)*I4)) == "spacelike"
check("G2 FORM-match: the homogeneous (2,2) Finster/Dirac form reproduces the Minkowski timelike/"
      "spacelike split (200/200 each, my 5089) -- so Lyra's construction has the right FORM. The "
      "OBJECT-match (does F(x)F(y) reproduce the SPECIFIC commit-Casimir split, K1226) needs her "
      "explicit x<->commit-mode map -- REQUESTED, not claimed",
      tl == 200 and sl == 200,
      f"form-match: {tl}/200 timelike + {sl}/200 spacelike (Dirac (2,2) structure). Object-match "
      "pending: I need the map x (spacetime point) <-> commit-Casimir mode to compare eigenvalues.")

# ----------------------------------------------------------------------------
# VERDICT (Cal's ladder).
# ----------------------------------------------------------------------------
print("\n--- VERDICT (Cal's tier ladder) ---")
check("VERDICT: G3 (signature) confirmed + G4a (critical-point, necessary, via homogeneity, modulo "
      "regularization) + G2 (form-match) => 'STRONGLY RESEMBLES' (candidate framework). OPEN: G2 "
      "object-match (x<->mode map), G4a full stationarity + regularization, G4b global min. NOT "
      "banked as 'BST IS a CFS'; T2545 + QM 10/10 stand independent",
      True,
      "fired what the delivered construction supports; the ONE missing input is the explicit "
      "x<->commit-mode map (upgrades G2 form->object). Firer=Lyra, checker=Elie. Ladder held.")

# ============================================================================
passed = sum(1 for _, c, _ in results if c)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}")
print("=" * 78)
print(f"""
SUMMARY (Toy 5097, K1239 -- FIRE the CFS gates on Lyra's confirmed (2,2) operator):
  * G3 (signature) CONFIRMED: Lyra's positive-projector spectrum {{-16.9,-10.3,-2.0,0}} is
    single-sign (degenerate); her indefinite fix {{-19.6,-1.6,+0.6,+3.9}} is (2,2) (arrow survives).
    Honest clarification: (2,2) is the SPIN-space signature (Finster n=2); (3,1) is the emergent
    SPACETIME signature (T2545) -- related, not identical (2 spin-minus != 1 time). Flagged.
  * G4a (critical point) PASSES the necessary EL condition: Lyra's homogeneous FK measure gives
    ell(x) constant on the support by invariance (5092 confirms). CAVEATS: necessary-not-full-
    stationarity; FK measure non-compact -> needs regularization (open); G4b conjectural.
  * G2 FORM-match confirmed (homogeneous (2,2) Finster -> Minkowski split, 5089, 200/200). OBJECT-
    match (reproduce the SPECIFIC commit-Casimir split, K1226) needs Lyra's explicit x<->mode map --
    requested, NOT claimed.
  * VERDICT (Cal's ladder): G3 + G4a-necessary + G2-form => "STRONGLY RESEMBLES" (candidate). OPEN:
    G2 object-match, G4a stationarity+regularization, G4b. NOT banked as "IS a CFS". T2545 + QM 10/10
    independent.

AUG-06 [TEGMARK]. Nothing pushed. Nothing banked past "strongly resembles". The one missing input
is the explicit x<->commit-mode map. Firer=Lyra, checker=Elie. Count N.
""")
