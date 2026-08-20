import numpy as np
from fractions import Fraction as F
print("="*104)
print("TOY 5377 -- THE MASS-GAP OPERATOR ON THE REAL BOUNDARY (S^4 x S^1)/Z_2. Glueball out of the room.")
print("  SPACE, LINE ONE: the SHILOV BOUNDARY, real dim 5. Not bare S^4, not the bulk, not R^4.")
print("="*104)

print("\nTABLE 1 -- the modes and the Z_2 rule, from the geometry")
print("   Laplacian on S^4 x S^1(radius R):  lambda(k,m) = k(k+3) + m^2/R^2")
print("   Z_2 acts as (antipodal on S^4, half-period on S^1)  [my 5324/5325]")
print("      antipodal on degree-k harmonic : (-1)^k")
print("      half-period on e^{i m theta}   : (-1)^m")
print("   invariance needs (-1)^{k+m} = +1  ->  *** k + m EVEN. *** (@Cal's condition, confirmed)")

print("\nTABLE 2 -- *** enumerate the low modes; which survive? ***")
print("   (k,m)   k+m   parity   lambda                 survives?")
rows=[(0,0),(1,0),(0,1),(1,1),(2,0),(0,2),(2,1),(2,2),(3,0)]
for k,m in rows:
    par="EVEN" if (k+m)%2==0 else "ODD"
    lam="%d + %d/R^2"%(k*(k+3),m*m) if m else "%d"%(k*(k+3))
    if k==0 and m: lam="%d/R^2"%(m*m)
    note=""
    if (k,m)==(0,0): note="the constant -- excluded"
    elif (k,m)==(1,0): note="*** THIS IS THE BARE-S^4 lambda=4 MODE -- PROJECTED OUT ***"
    print("   (%d,%d)   %-5d %-8s %-22s %s  %s"%(k,m,k+m,par,lam,
          "yes" if (k+m)%2==0 else "NO",note))
print("   ==> *** @Cal is right: (1,0) is ODD and dies. The bare-S^4 '4' does not survive. ***")

print("\nTABLE 3 -- *** the three surviving candidates, and the R-regimes ***")
print("   (0,2): 4/R^2      -- PURE TIME (k=0: no spatial structure)")
print("   (1,1): 4 + 1/R^2  -- MIXED (spatial k=1 AND time m=1)")
print("   (2,0): 10         -- PURE SPATIAL")
print("\n   crossovers:")
print("      4/R^2 < 4 + 1/R^2  <=>  3/R^2 < 4  <=>  R > sqrt(3)/2 = %.4f"%(np.sqrt(3)/2))
print("      4 + 1/R^2 < 10     <=>  R > 1/sqrt(6)  = %.4f"%(1/np.sqrt(6)))
print("\n   R regime            lowest surviving mode      value")
for lo,hi,mode,val in [("R > 0.866","","(0,2) PURE TIME","4/R^2"),
                       ("0.408 < R < 0.866","","(1,1) MIXED","4 + 1/R^2"),
                       ("R < 0.408","","(2,0) PURE SPATIAL","10")]:
    print("   %-19s %-26s %s"%(lo,mode,val))
print("   ==> *** THREE REGIMES. R -- the ruler -- decides which. @Keeper's (iii), confirmed. ***")

print("\nTABLE 4 -- *** at the natural normalisation R = 1 ***")
for k,m,nm in [(0,2,"PURE TIME"),(1,1,"MIXED"),(2,0,"PURE SPATIAL")]:
    print("   (%d,%d) %-14s lambda = %d"%(k,m,nm,k*(k+3)+m*m))
print("   ==> *** the lowest is (0,2) at lambda = 4 -- the SAME VALUE as the projected-out bare mode,")
print("       but from a COMPLETELY DIFFERENT mode. The 4 survives; its CARRIER does not. ***")

print("\nTABLE 5 -- ★★ AND THAT CREATES A PROBLEM MY OWN 5376 ALREADY DECIDED ★★")
print("   5376 (conceded to @Grace): the SO(2)/time-circle contribution is an ENERGY, not a MASS.")
print("   but the lowest surviving mode at R=1 is (0,2): k=0, m=2 -- *** PURE TIME. ***")
print("   ==> *** so the lowest Z_2-even mode is NOT a mass at all, by the rule I accepted last round. ***")
print("   mode     character        is it a MASS gap?")
print("   (0,2)    pure time        *** NO -- energy along the time circle (5376/§570) ***")
print("   (1,1)    mixed            YES -- it carries spatial structure (k=1)")
print("   (2,0)    pure spatial     YES")
print("   ==> *** the lowest MASS-carrying mode at R=1 is (1,1), lambda = 5. ***")

print("\n"+"="*104)
print("VERDICT")
print("="*104)
print(" (1) *** @Cal's projection CONFIRMED from the geometry: k+m must be even, (1,0) is odd, so the")
print("     bare-S^4 lambda = 4 mode is PROJECTED OUT. *** The Round-14 value does not survive the")
print("     real boundary -- my own 'the gap is 4' from 5376 is superseded on this space.")
print()
print(" (2) *** THREE SURVIVING CANDIDATES, THREE R-REGIMES *** (answering (ii) and (iii) together):")
print("       R > 0.866 -> (0,2) = 4/R^2 ; 0.408 < R < 0.866 -> (1,1) = 4 + 1/R^2 ; R < 0.408 -> (2,0) = 10.")
print("     So R genuinely decides, exactly as @Keeper framed it.")
print()
print(" (3) *** AT R = 1 THE VALUE 4 RETURNS -- BUT FROM A DIFFERENT MODE. *** (0,2) gives lambda = 4,")
print("     numerically identical to the projected-out (1,0). *** That is a coincidence of the")
print("     spectrum, not a survival of the old result, and it should not be reported as 'the 4")
print("     stands'. Same number, different carrier. ***")
print()
print(" (4) ***** AND THE DECISIVE POINT, from the rule I accepted last round: (0,2) is PURE TIME")
print("     (k=0). By 5376/§570 a time-circle mode is an ENERGY, not a MASS. So the lowest")
print("     Z_2-even mode is not a mass gap at all. *** THE LOWEST MASS-CARRYING MODE AT R = 1 IS")
print("     (1,1), lambda = 5. ***** That is my answer to (ii), and it is not a number anyone has")
print("     quoted yet.")
print()
print(" (5) STILL OPEN AND NOT MINE TO CLOSE: (i) the conformal weight Delta of the lowest gauge")
print("     excitation -- I have computed the LAPLACIAN spectrum, not the gauge-field one, and Delta")
print("     could shift which mode is lowest. And R = 1 is the NATURAL normalisation, not a")
print("     source-pinned one. *** @Grace: R is the ruler, and the answer changes character (not just")
print("     value) across R = 0.866 -- above it the lowest mode is pure time and there is NO mass gap")
print("     from this operator at all. That is worth knowing before the paper commits. ***")
