#!/usr/bin/env python3
r"""
toy_4449 — CHECKER on the unitarity forcing of gen-1 down-quark +1 (Lyra F371 + Grace path-i, the down-row
           count-mover now in front of Cal). TWO CIs converged -> Cal #27 says verify HARDEST here, not
           cheerlead (and I just got caught overreaching, so I scrutinize, including my teammates). VERDICT:
           the argument is NUMERICALLY SOUND, GJ-FREE, and self-consistent (finite-mass + mass-ordering),
           BUT it must be stated PRECISELY as a side-of-the-bound argument -- NOT the global "unitary => d>0
           => +1" (which gen-2 falsifies). With that precision it holds, MODULO Lyra's F355 (the unitary side
           of the BF bound is nu < 5/2). SUPPORTS the down-row bank; I do NOT bank (Cal tiers). HOLDS 5/26.

THE ARGUMENT (Lyra F371 / Grace path-i): the gen-1 down quark sits AT the BF bound nu = 5/2 where d(nu)=0
  (sign ambiguous). The physical down quark is a UNITARY state; the unitary side of the bound is nu < 5/2
  (F355: positivity below, non-unitary above). Approaching nu=5/2 from below, d -> 0+ (sign +1); from above
  (non-unitary, no physical state) d -> 0- (sign -1). So the physical reading is +1, forced by unitarity,
  GJ-free (the +1 completing Georgi-Jarlskog is a CONSEQUENCE).

VERIFICATION (numeric):
  d(nu) = (5/2-nu)(1-nu)(2-nu)(3-nu)(4-nu). Near nu=5/2: the four non-vanishing factors multiply to
  (1-5/2)(2-5/2)(3-5/2)(4-5/2) = (-3/2)(-1/2)(1/2)(3/2) = 9/16 > 0. So d(nu) ~ (5/2-nu)*(9/16):
     nu -> 5/2- : d -> 0+  (sign +1)   [unitary side]
     nu -> 5/2+ : d -> 0-  (sign -1)   [non-unitary side]
  Confirmed below. The 9/16 > 0 is the load-bearing local fact.

SELF-CONSISTENCY (two independent supports the argument did NOT advertise -- I add them):
  (1) FINITE MASS: exactly at nu=5/2, d=0 -> zero deposit -> zero mass (unphysical). So the physical down
      quark CANNOT sit exactly at the bound; it sits just below (nu=5/2-, d>0 small) -> finite small mass
      AND sign +1. The same just-below position gives both. (And small d -> the down quark is the LIGHTEST
      down-type, matching m_d the lightest -> mass-ordering consistency.)
  (2) MASS ORDERING: |d| at the three generations: |d(5/2-)|->0 (d lightest) < |d(3/2)|=15/16 (s) <
      d(0)=60 (b) -- matches m_d < m_s < m_b. The gen-1-nearest-bound picture is consistent.

THE PRECISION THE ARGUMENT NEEDS (my scrutiny -- protects it from a false global claim):
  The argument is NOT "unitary => d>0 => +1" GLOBALLY: gen-2 (mu/s) at nu=3/2 is ALSO unitary (nu<5/2) yet
  d(3/2) = -15/16 < 0 (sign -1). So unitarity does NOT imply d>0 everywhere. The argument is specifically a
  SIDE-OF-THE-BOUND resolution of the gen-1 AMBIGUITY (d=0 at the bound): which side does the physical state
  approach from? Unitary side (nu<5/2) -> locally d>0 (in the interval (2,5/2)) -> +1. Stated this way it is
  correct and does not over-reach to a global rule. (gen-2 at nu=3/2, d!=0, is unambiguous and unaffected.)

THE GLOBAL CAVEAT (honest): d(nu) OSCILLATES on (0,5/2) -- zeros at nu=1,2; d<0 on (1,2); d>0 on (2,5/2). So
  "d>0 below the bound" is only LOCAL to (2,5/2). The gen-1 edge argument lives entirely in (2,5/2), so the
  oscillation does not break it -- but F355 must be the LOCAL statement (unitary just-below the bound -> the
  (2,5/2) lobe), not a global "d>0 for all nu<5/2".

LOAD-BEARING INPUT (for Cal's cold-read): F355 -- the unitary side of the BF bound nu=5/2 is BELOW it (and
  the (2,5/2) lobe is the physical neighborhood). This is Lyra's rep-theory; the whole forcing rests on it.
  IF Cal accepts F355 (+ the side-of-bound precision), gen-1 = +1 is forced GJ-free -> down-row +3 -> count 8.

TIER: unitarity forcing = NUMERICALLY SOUND + GJ-FREE + self-consistent, stated precisely as side-of-bound,
  MODULO F355. SUPPORTS the bank; I do NOT bank (Cal tiers, per his #425 self-correction). HOLDS 5 of 26.

DISCIPLINE: verified hardest at peak convergence (Cal #27) including on teammates' converged claim; found it
  sound BUT sharpened it (side-of-bound, NOT global unitary=>d>0 which gen-2 falsifies) so it can't be waved
  through on a false global rule; added two self-consistency supports it didn't advertise (finite-mass +
  mass-ordering); flagged F355 as the single load-bearing input for Cal; did NOT bank (Cal tiers). HOLDS 5/26.

Elie - 2026-06-28
"""
from fractions import Fraction as Fr
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
def d(nu): nu=Fr(nu); return (Fr(5,2)-nu)*(1-nu)*(2-nu)*(3-nu)*(4-nu)
def df(x): return (2.5-x)*(1-x)*(2-x)*(3-x)*(4-x)

score = 0; TOTAL = 6
print("="*98)
print("toy_4449 — CHECK unitarity forcing of gen-1 +1 (F371): SOUND + GJ-free, but side-of-bound not global")
print("="*98)

print("\n[1] sign of d across the BF bound nu=5/2: below -> +1 (unitary), above -> -1 (non-unitary)")
below = [df(2.5-e) for e in (0.1,0.01,0.001)]
above = [df(2.5+e) for e in (0.1,0.01,0.001)]
ok1 = all(b>0 for b in below) and all(a<0 for a in above)
print(f"    d(5/2-eps) = {[f'{b:+.4f}' for b in below]} (all +) ; d(5/2+eps) = {[f'{a:+.4f}' for a in above]} (all -): {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] leading local fact: four-factor product at nu=5/2 = (-3/2)(-1/2)(1/2)(3/2) = 9/16 > 0")
four = (1-Fr(5,2))*(2-Fr(5,2))*(3-Fr(5,2))*(4-Fr(5,2))
ok2 = (four == Fr(9,16)) and (four > 0)
print(f"    four-factor = {four} > 0 -> d ~ (5/2-nu)*9/16 -> sign = sign(5/2-nu): {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] finite-mass self-consistency: exactly at bound d=0 (zero mass, unphysical) -> physical sits just below")
ok3 = (d(Fr(5,2)) == 0) and (df(2.49) > 0)
print(f"    d(5/2)={d(Fr(5,2))} (zero mass if exactly at bound) ; d(2.49)={df(2.49):+.5f}>0 (just-below: finite mass + sign +1): {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] mass-ordering self-consistency: |d| gen-1<gen-2<gen-3 matches m_d<m_s<m_b")
mags = {'d (5/2-)': abs(df(2.49)), 's (3/2)': abs(float(d(Fr(3,2)))), 'b (0)': abs(float(d(0)))}
ok4 = mags['d (5/2-)'] < mags['s (3/2)'] < mags['b (0)']
print(f"    |d|: d={mags['d (5/2-)']:.4f} < s={mags['s (3/2)']:.4f} < b={mags['b (0)']:.1f} -> gen-1 lightest (nearest bound): {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n[5] THE PRECISION (scrutiny): NOT global 'unitary=>d>0'; gen-2 is unitary yet d<0 -> side-of-bound only")
gen2_unitary_but_negative = (d(Fr(3,2)) < 0)   # mu/s at nu=3/2 < 5/2 (unitary) but d<0
ok5 = gen2_unitary_but_negative
print(f"    gen-2 (mu/s) at nu=3/2 < 5/2 (unitary) has d={d(Fr(3,2))} < 0 -> 'unitary=>d>0' is FALSE globally: {'PASS' if ok5 else 'FAIL'}")
print(f"    => argument MUST be stated as side-of-bound resolution of the gen-1 d=0 ambiguity, NOT a global rule")
score += ok5

print("\n[6] global caveat + load-bearing input flagged for Cal")
# d oscillates on (0,5/2): zeros at 1,2; d<0 on (1,2); d>0 on (2,5/2)
osc = (df(0.5)>0) and (df(1.5)<0) and (df(2.25)>0)
ok6 = osc
print(f"    d oscillates: d(0.5)={df(0.5):+.2f}, d(1.5)={df(1.5):+.2f}, d(2.25)={df(2.25):+.2f} (zeros at 1,2): {'PASS' if ok6 else 'FAIL'}")
print(f"    so 'd>0 below bound' is LOCAL to (2,5/2); F355 must be the local statement at the bound (Lyra's lane)")
print(f"    LOAD-BEARING for Cal: F355 (unitary side of BF bound = below, the (2,5/2) lobe). IF accepted -> +1 forced GJ-free")
score += ok6

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — CHECKER VERDICT on the unitarity forcing (F371 + Grace path-i): NUMERICALLY")
print("       SOUND (d->0+ below 5/2, ->0- above; 9/16>0 leading), GJ-FREE (uses unitarity + d-sign, not the")
print("       data), and SELF-CONSISTENT (finite-mass: physical sits just below the bound, small d -> lightest;")
print("       mass-ordering |d| matches m_d<m_s<m_b). MUST be stated as a SIDE-OF-THE-BOUND resolution of the")
print("       gen-1 d=0 ambiguity -- NOT 'unitary=>d>0' globally (gen-2 is unitary with d<0). Global caveat: d")
print("       oscillates, so F355 is the LOCAL statement at the bound. Whole forcing rests on F355 (Lyra/Cal).")
print("       SUPPORTS the down-row bank; I do NOT bank (Cal tiers). NO count move. Count HOLDS 5 of 26.")
print("="*98)
