import numpy as np
from math import pi, gamma
from fractions import Fraction as F
print("="*104)
print("TOY 5389 -- THE RULER-SHAPE, TWO ROUTES. *** RETRACTION CHECK FIRST (standing rule). ***")
print("  SPACE, LINE ONE: the SHILOV BOUNDARY (S^4 x S^1)/Z_2 -- a dimensionless RATIO, not a length.")
print("="*104)

print("\nTABLE 0 -- *** GREP THE RETRACTION BEFORE COMPUTING -- and it fires ***")
print("   instrument validated first (control 'alpha' -> 8 hits in the scoreboard).")
print("   corpus, BST_26_Scoreboard_current_tiers_2026-07-18.md, verbatim:")
print('      "Wyler RETIRED**; 4pi = descent Coulomb solid angle"')
print('      "Wyler route are retired fits"')
print("   ==> *** 8 pi^4 IS WYLER'S DENOMINATOR (his alpha formula carries 9/(8 pi^4)). ***")
print("       The prompt's 'the same ratio in alpha's 8 pi^4' therefore reconnects to a RETIRED")
print("       route. *** Flagging before I compute, not after. ***")

def volS(n): return 2*pi**((n+1)/2)/gamma((n+1)/2)
print("\nTABLE 1 -- *** and the volume identification does not hold. Check it directly. ***")
for n in range(1,8):
    print("   vol(S^%d) = %.6f"%(n,volS(n)))
r=volS(4)/volS(1)
print("\n   claimed: 8 pi^4 = vol(S^4)/vol(S^1)")
print("   vol(S^4)/vol(S^1) = (8 pi^2/3)/(2 pi) = %.6f   [= 4 pi/3 = %.6f]"%(r,4*pi/3))
print("   8 pi^4            = %.6f"%(8*pi**4))
print("   equal? %s   -- off by a factor %.1f"%(abs(r-8*pi**4)<1e-9, 8*pi**4/r))
print("   ==> *** 8 pi^4 IS NOT vol(S^4)/vol(S^1). *** The ratio is 4 pi/3.")
print("   sweep other pairs for 8 pi^4 = %.4f:"%(8*pi**4))
found=False
for a_ in range(1,9):
    for b_ in range(1,9):
        v=volS(a_)/volS(b_)
        if abs(v-8*pi**4)<1e-6: print("      vol(S^%d)/vol(S^%d) = %.4f  MATCH"%(a_,b_,v)); found=True
print("      %s"%("(matches found above)" if found else "*** NO sphere-volume ratio equals 8 pi^4. ***"))

print("\nTABLE 2 -- route 1: the Bergman/kappa_eff number, checked on its own terms")
g,n_C,rank=7,5,2
k=F(2*g,n_C)
print("   kappa_eff = 2g/n_C = %s = %.4f"%(k,float(k)))
print("   and g = n_C + rank, so 2g/n_C = 2 + 2 rank/n_C = 2 + %s = %s   (identity, holds for all n)"%(
      F(2*rank,n_C),k))
print("   is kappa_eff a sphere-volume ratio? sweep:")
hits=[(a_,b_) for a_ in range(1,9) for b_ in range(1,9) if abs(volS(a_)/volS(b_)-float(k))<1e-6]
print("      %s"%(hits if hits else "*** none -- 14/5 is NOT a sphere-volume ratio. ***"))

print("\nTABLE 3 -- *** so can the two routes even be COMPARED? ***")
print("   route                     number      type")
print("   1  Bergman kappa_eff      14/5 = 2.8  a RATIONAL from BST integers (2g/n_C)")
print("   2  'alpha's 8 pi^4'       779.27      a TRANSCENDENTAL, and Wyler-retired")
print("   ==> *** THEY ARE NOT THE SAME KIND OF OBJECT, let alone the same number. *** One is a")
print("       rational built from g and n_C; the other is a transcendental from a retired fit.")
print("       *** No agreement to check -- the comparison as posed is ill-formed. ***")

print("\n"+"="*104)
print("VERDICT")
print("="*104)
print(" (1) *** THE RETRACTION FIRES, AND I CHECKED IT BEFORE COMPUTING. *** 8 pi^4 is Wyler's")
print("     denominator, and the corpus says verbatim 'Wyler RETIRED' and 'Wyler route are retired")
print("     fits'. *** Building the ruler-shape on alpha's 8 pi^4 reconnects to a retired route ***,")
print("     which is exactly what the grep-the-retraction rule exists to stop.")
print()
print(" (2) *** AND THE VOLUME IDENTIFICATION IS FALSE ON ITS OWN TERMS: vol(S^4)/vol(S^1) = 4 pi/3")
print("     = 4.189, NOT 8 pi^4 = 779.27 *** -- off by a factor of 186. I swept every sphere-volume")
print("     ratio up to S^8 and *** none equals 8 pi^4. ***")
print()
print(" (3) *** THE TWO ROUTES CANNOT AGREE BECAUSE THEY ARE DIFFERENT KINDS OF NUMBER: *** 14/5 is")
print("     a RATIONAL from BST integers (and 2g/n_C = 2 + 2 rank/n_C is an identity, so it carries")
print("     no dimensional information); 8 pi^4 is a transcendental from a retired fit. There is no")
print("     agreement to test -- *** the comparison as posed is ill-formed, and I would rather say")
print("     so than manufacture one. ***")
print()
print(" (4) WHAT SURVIVES: the QUESTION is good -- a dimensionless S^4/S^1 shape ratio IS the right")
print("     target, and it IS §578-clean in principle (a ratio needs no length). *** What does not")
print("     survive is this pair of routes. *** @Grace/@Casey: route 2 needs a non-Wyler derivation")
print("     of the boundary/continuum matching before it can be compared to anything.")
print()
print(" (5) AND A NOTE ON ROUTE 1: 2g/n_C = 2 + 2 rank/n_C holds identically in n -- so like 25/4 and")
print("     Condition 5, *** it is dimension-generic and cannot by itself select n_C = 5. *** If it is")
print("     the ruler-shape, that is a separate claim needing its own mechanism.")
