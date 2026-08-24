# TOY 5498 -- THE ONE-SHOT CROSS, MY HALF. Elie, 2026-08-24. Independent of Grace's
# computation (hers unseen). Exact arithmetic on the AV-graded calibrator modules.
# Protocol: exponents FIRST, verdict against the frozen biconditional LAST.
from fractions import Fraction as F
BAR="="*100
def head(s): print("\n"+BAR); print(s); print(BAR)
print(BAR); print("TOY 5498 -- the cross, exact-arithmetic half"); print(BAR)

head("PIN AND GATE (before any exponent)")
def E(k,w): return F(k)*(F(k)+3) + F(w)**2     # pinned 755 operator on harmonic (k,0) x SO(2) w
print("  Operator: the 755-pinned E = k(k+3) + w^2 on K-type (harmonic k, SO(2) weight w).")
print("  GATE (C2 anchor): E on the SO(5) type (1,1) at w=0 must be 6: m1(m1+3)+m2(m2+1) =")
print("  4+2 = %s -> %s"%(F(1)*4+F(1)*2,"PASS" if F(1)*4+F(1)*2==6 else "FAIL"))
print("  W-CONVENTION, pinned not chosen: the 755 pin fixes the two factors' relative scale by")
print("  the R79-GATED B3 EUCLIDEAN FRAME, where e1 IS the SO(2)/nu direction -- the ABSOLUTE")
print("  weight: a K-type at FK-degree d in the Wallach module H_nu carries w = nu + d")
print("  (physical label, Family B, book-day-ruled). The relative alternative (w measured from")
print("  each module's own bottom) is STATED and evaluated below as robustness -- not chosen.")
print("  MODULE CONTENTS: from Grace's gated truncation table, GK-verified exactly in 5497.")

head("THE THREE EXPONENTS (posted first, per protocol)")
print("  E_j = min over the module's K-types of E(k, nu+d):")
rows=[]
# tau / AV rank 0 / KW Shilov: nu=0, only (0,0): k=0,d=0
rows.append(("AV rank 0  (KW Shilov, tau)",  min(E(0,0+0) for _ in [0])))
# muon / AV rank 1 / KW Cartan: nu=3/2, (m1,0): k=m1, d=m1
rows.append(("AV rank 1  (KW Cartan, muon)", min(E(m1,F(3,2)+m1) for m1 in range(0,20))))
# electron / AV rank 2 / KW bulk: nu=5/2, all (m1,m2): k=m1-m2, d=m1+m2
rows.append(("AV rank 2  (KW bulk, electron)",min(E(m1-m2,F(5,2)+m1+m2) for m1 in range(0,20) for m2 in range(0,m1+1))))
for name,e in rows:
    print("   %-32s E = %-8s (= nu^2 at the bottom K-type: pattern noted below)"%(name,e))
print("\n  ROBUSTNESS (the relative convention, stated not chosen): w = d from each bottom gives")
print("   E = (0, 0, 0) -- fully DEGENERATE. Under NEITHER convention does the frozen order hold.")

head("THE VERDICT, against the frozen biconditional (LAST, as staged)")
print("""  FROZEN (Grace's dictionary + Lyra's order-only lemma + the 4/4 physical control):
     Shilov-first freeze-out  <==>  E_{AV rank 0} > E_{AV rank 1} > E_{AV rank 2}
  MY EXPONENTS: E = (0, 9/4, 25/4).
     Required:  0 > 9/4 > 25/4   -- FALSE.
     Observed:  0 < 9/4 < 25/4   -- THE EXACT STRICT REVERSE, both inequalities.
  *** THE ZERO-KNOB FALSIFIER FIRES NEGATIVE. THE THERMAL GENERATION MECHANISM, AS FROZEN,
  DIES AT THE ORDER LEVEL. *** By the order-only lemma the E-descending leader sequence is
  bulk -> Cartan -> Shilov: the ELECTRON channel would dominate the commit flow first (hot),
  the TAU last (cold) -- the reverse of the 4/4 control (heaviest-first, top-at-Shilov).
  No clock, no map, no parameter can repair an inverted ORDER -- that was the lemma's point.

  OBSERVATIONS, logged not composed (after the verdict, touching nothing):
  (1) E_min(module) = nu^2 EXACTLY (bottom K-type: k=0, w=nu). The three exponents are the
      squared Wallach addresses. Clean, target-innocent, unclaimed.
  (2) The ordering E ~ nu^2 is INVERSE to the mass ordering -- the 5487 inversion shape,
      surfacing again from the spectral side: the heaviest lepton's channel has the SMALLEST
      exponent and dominates the flow LATEST. Whatever that means, it is not this lane's
      frozen claim, and it is logged for whoever owns the inversion question next.
  ONE SHOT, TAKEN. Nothing re-read, nothing re-scaled. Grace's half unseen at this writing.""")
