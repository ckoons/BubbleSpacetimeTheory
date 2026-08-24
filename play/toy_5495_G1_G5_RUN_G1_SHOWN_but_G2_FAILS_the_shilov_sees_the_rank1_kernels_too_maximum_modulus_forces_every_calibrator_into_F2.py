# TOY 5495 -- THE G1-G5 GATE RUN (joint with Grace, per the frozen sequence). Elie, 2026-08-24.
# Discipline: gates in order; ALL before any E_j; a failure is REPORTED as the lane's result,
# never patched; the one-shot stays holstered.
import numpy as np
BAR="="*100
def head(s): print("\n"+BAR); print(s); print(BAR)
print(BAR); print("TOY 5495 -- G1-G5 against the pinned support-class membership"); print(BAR)

head("G1 -- H_B DESCENDS: [H_B, F_j] within F_j. SHOWN, not asserted.")
print("""  (a) K preserves each KW stratum: the singular values are K-invariant (lam_i(k z e^{i t})
      = lam_i(z)), so K-flows map strata to themselves.
  (b) A K-generator X acts by differentiation along a stratum-preserving flow: sing-supp(Xf)
      is CONTAINED in sing-supp(f). Contact ORDER can grow under differentiation (h^-a ->
      h^-a-1 terms) -- but *** THE PINNED MEMBERSHIP IS SUPPORT-CLASS, NOT ORDER-THRESHOLD,
      so growing order CANNOT move a mode between F_j's. The pin sentence is exactly what
      makes descent work. *** H_B (polynomial in the X's) preserves each F_j; it acts on gr_j.
  (c) Exhibited on the calibrator: d/dt|0 f_zeta0(e^{-tX}z) = nu h^{-nu-1} * (dh along X) --
      singular set STILL {h(., zeta0bar) = 0}, same support class. G1: *** SHOWN. PASS. ***""")

head("G2 -- membership separates the calibrators. RUN AS PINNED.")
print("  The gr_1 calibrator must be a MODE whose singular support meets rank-1 but NOT Shilov")
print("  (support-class membership: 'j = the highest stratum meeting its singular support').")
print("  Natural candidate, per the prereg's own shelf: the rank-1 kernel f_1 = h(., zbar*)^-mu,")
print("  z* = (e1 + i e2)/2 (the 5493 shoulder point, isotropic).")
print("\n  *** THE CANDIDATE'S ZERO SET MEETS THE SHILOV. Exhibited exactly: ***")
print("  h(z, zbar*) = 1 - 2 z.zbar* (isotropy kills the quadratic term). For the Shilov family")
print("  z_s(phi) = e^{i phi}(cos phi, sin phi, 0, 0, 0):   z_s . zbar* = e^{i phi} e^{-i phi}/2 = 1/2")
print("  => h(z_s, zbar*) = 0 for EVERY phi -- a whole Shilov circle in the singular set.")
e1=np.zeros(5,complex); e1[0]=1; e2=np.zeros(5,complex); e2[1]=1
zs=lambda p: np.exp(1j*p)*np.array([np.cos(p),np.sin(p),0,0,0],complex)
zbar_star=np.conj((e1+1j*e2)/2)
for p in (0.0,0.7,2.1):
    z=zs(p); hval=1-2*(z*zbar_star).sum()+ (z*z).sum()*((zbar_star*zbar_star).sum())
    lam2=np.sqrt(max((np.vdot(z,z).real)-np.sqrt(max((np.vdot(z,z).real)**2-abs((z*z).sum())**2,0)),0))
    print("     phi=%.1f: |h(z_s, zbar*)| = %.2e ; lam2(z_s) = %.4f (Shilov)"%(p,abs(hval),lam2))
print("""
  => under the PINNED membership the rank-1 kernel's highest-met stratum is the SHILOV:
     the shoulder calibrator lands F_2, NOT F_1. *** THE MUST-CATCH 'shoulder -> gr_1' FAILS. ***
  AND THE OBSTRUCTION IS STRUCTURAL, NOT A BAD CANDIDATE: a holomorphic mode's boundary
  singular set is the zero set of a holomorphic function -- a codim-1 analytic variety --
  and the SHILOV IS THE MAXIMUM-MODULUS BOUNDARY: the same totality property that killed
  the closed-span assembly (v1: dense spans) reappears one level down (v2: kernel zero
  sets reach the Shilov). Constructing ANY holomorphic gr_1 calibrator requires a
  boundary-zero variety through the rank-1 stratum avoiding the Shilov -- none exhibited,
  and the kernel-type candidates provably fail.""")

head("VERDICT -- per the frozen discipline: REPORT, NOT PATCH")
print("""  G1: PASS (shown; the support-class pin is what makes descent work -- a genuine design win).
  G2: *** FAIL AS PINNED *** -- the membership cannot separate the calibrators because the
      natural gr_1 calibrators are Shilov-singular. F_1 \\ F_0 may be EMPTY for holomorphic
      modes; gr_1 = 0 would make E_1 undefined before positivity is even asked.
  G3-G5: NOT RUN -- the sequence says all gates before any E_j, and a failed G2 stops the
      batch. The one-shot stays holstered. No exponent exists.
  THE FINDING, composed honestly (same root, third appearance): THE SHILOV'S TOTALITY IS
  THE INVARIANT OBSTACLE -- it killed spans by density (v1), and it kills support-class
  calibrators by the maximum-modulus property (v2). Any v3 must either (a) let membership
  read the DOMINANT order (which the pin currently forbids as a threshold -- a real design
  tension to rule on, not to patch silently), or (b) realize gr_1/gr_2 ON THE BOUNDARY
  ITSELF (Lyra's L2(Sigma) (x) Delta as the primary space, not a target). BOTH are design
  decisions belonging to Grace/Lyra with Cal's audit -- not to this gate-runner.""")
