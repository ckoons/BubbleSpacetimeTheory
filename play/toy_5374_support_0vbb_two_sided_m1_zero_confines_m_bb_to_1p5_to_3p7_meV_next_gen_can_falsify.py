import numpy as np
print("="*104)
print("TOY 5374 -- 0vbb RECONCILED TO TWO-SIDED: if nu_1 is EXACTLY massless, m_bb sits in a BAND.")
print("            Compute the band; then the row is detection-kills / null-does-not.")
print("="*104)
# PDG / global fit
dm21=7.53e-5; dm31=2.453e-3
s12sq=0.307; s13sq=0.0220
c13sq=1-s13sq; c12sq=1-s12sq

print("\nTABLE 1 -- inputs (PDG / global fit, measured -- not BST)")
print("   Dm^2_21 = %.3e eV^2 | Dm^2_31 = %.3e eV^2 | sin^2 t12 = %.3f | sin^2 t13 = %.4f"%(
      dm21,dm31,s12sq,s13sq))

print("\nTABLE 2 -- *** BST's claim: nu_1 EXACTLY massless (m_1 = 0), NORMAL ordering ***")
m1=0.0; m2=np.sqrt(dm21); m3=np.sqrt(dm31)
print("   m_1 = %.4e eV  (exactly zero, the BST claim)"%m1)
print("   m_2 = sqrt(Dm^2_21) = %.4e eV"%m2)
print("   m_3 = sqrt(Dm^2_31) = %.4e eV"%m3)
t1=c13sq*c12sq*m1; t2=c13sq*s12sq*m2; t3=s13sq*m3
print("\n   m_bb = |U_e1^2 m_1 + U_e2^2 m_2 + U_e3^2 m_3| with free Majorana phases")
print("      term_1 = %.4e eV   (VANISHES -- this is the whole content of m_1 = 0)"%t1)
print("      term_2 = %.4e eV"%t2)
print("      term_3 = %.4e eV"%t3)
lo,hi=abs(t2-t3),abs(t2+t3)
print("   ==> *** m_bb in [%.3f, %.3f] meV *** (phases scanned)"%(lo*1e3,hi*1e3))

print("\nTABLE 3 -- compare: inverted ordering with the lightest = 0 (the contrast case)")
m3i=0.0; m1i=np.sqrt(dm31); m2i=np.sqrt(dm31+dm21)
lo_i=c13sq*abs(c12sq*m1i-s12sq*m2i); hi_i=c13sq*(c12sq*m1i+s12sq*m2i)
print("   IO band: m_bb in [%.1f, %.1f] meV"%(lo_i*1e3,hi_i*1e3))

print("\nTABLE 4 -- *** experimental reach: is the band DISCRIMINATING? ***")
print("   experiment            m_bb sensitivity     above BST's NO ceiling (%.2f meV)?"%(hi*1e3))
for nm,s in [("KamLAND-Zen (now)","28-122 meV"),("LEGEND-1000","9-21 meV"),
             ("nEXO","5-20 meV"),("CUPID","6-17 meV")]:
    print("   %-21s %-20s YES -- a detection there contradicts m_1 = 0"%(nm,s))
print("   ==> *** next-generation reach (~5-20 meV) sits ENTIRELY ABOVE the m_1=0 band. ***")

print("\n"+"="*104)
print("VERDICT -- the row becomes TWO-SIDED")
print("="*104)
print(" (1) *** IF nu_1 IS EXACTLY MASSLESS (normal ordering), m_bb IS CONFINED TO [%.2f, %.2f] meV. ***"%(lo*1e3,hi*1e3))
print("     The m_1 term vanishes identically; the band is set by the two measured splittings and")
print("     the Majorana phases. No BST input beyond 'm_1 = 0'.")
print()
print(" (2) *** SO THE 0vbb ROW IS NOT A BARE PERMISSION -- IT IS TWO-SIDED: ***")
print("       DETECTION at m_bb >> 3.7 meV (e.g. anywhere in LEGEND/nEXO's 5-20 meV reach)")
print("          *** CONTRADICTS m_1 = 0 and KILLS the exactly-massless claim. ***")
print("       NULL result does NOT kill BST -- it is exactly what m_1 = 0 predicts.")
print("     @Keeper: that is the asymmetry you asked me to reconcile, and it is sharp.")
print()
print(" (3) *** AND IT IS NEAR-TERM. *** Next-generation sensitivity (5-20 meV) sits ENTIRELY ABOVE")
print("     the m_1 = 0 band (max 3.7 meV). So LEGEND-1000 / nEXO can falsify the exactly-massless")
print("     claim within the decade -- a real, dated falsifier, not a distant one.")
print()
print(" (4) CONTRAST, worth carrying: inverted ordering with the lightest = 0 gives [%.0f, %.0f] meV --"%(lo_i*1e3,hi_i*1e3))
print("     squarely IN next-gen reach. *** So the experiment discriminates BST's NO+massless case")
print("     from IO cleanly: a detection at ~20-50 meV points to IO and kills m_1 = 0 either way. ***")
print()
print(" (5) SCOPE: this assumes BST predicts NORMAL ordering with m_1 = 0 exactly. If BST does not")
print("     commit to the ordering, the band widens and the falsifier weakens. *** @Lyra/@Grace --")
print("     does the corpus commit to NO? That is the one input this row rests on, and I did not")
print("     verify it. ***")
