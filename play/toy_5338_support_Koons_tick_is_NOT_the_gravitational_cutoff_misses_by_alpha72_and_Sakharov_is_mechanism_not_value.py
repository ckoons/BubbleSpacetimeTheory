import numpy as np
alpha=1/137.035999; C2=6; g_=7; N_max=137
lP=1.616255e-35; tP=5.391247e-44; c=2.99792458e8; G_N=6.67430e-11
print("="*104)
print("TOY 5338 -- the UV cutoff 1/G computation: does the Koons tick give the right Newton constant?")
print("  Tables first, verdict after.")
print("="*104)

print("\nTABLE 1 -- the Sakharov relation, stated before any number")
print("   induced EH term ~ a_1density x Int_eps dt t^{-n/2};  in 4D this is 1/G ~ Lambda^2")
print("   equivalently  *** G  ~  (cutoff length)^2 ***   -- smaller cutoff => weaker gravity")

print("\nTABLE 2 -- the candidate cutoffs")
tK=tP*alpha**(C2**2)                       # Koons tick, T2405
lK=c*tK
print("   cutoff                         length (m)        source")
print("   Planck length  l_P             %.4e      standard"%lP)
print("   Koons tick     l_K = c t_K     %.4e      T2405: t_P x alpha^{C_2^2} = t_P x alpha^%d"%(lK,C2**2))
print("      (t_Koons = %.3e s -- matches the corpus '~1e-120 s')"%tK)

print("\nTABLE 3 -- *** run each cutoff through G ~ l^2 and compare to the measured G ***")
print("   cutoff        G_induced / G_Newton = (l_cut / l_P)^2      verdict")
for nm,l in [("l_Planck",lP),("l_Koons",lK)]:
    r=(l/lP)**2
    print("   %-13s %.4e%s"%(nm,r,"                              MATCHES by construction" if nm=="l_Planck"
          else "                     *** MISSES ***"))
miss=(lK/lP)**2
print("\n   miss factor with the Koons tick: %.3e  ->  about %.0f ORDERS OF MAGNITUDE too small"%(miss,-np.log10(miss)))
print("   and the miss is exactly alpha^{2 C_2^2} = alpha^%d = %.3e   (check: %.3e)"%(2*C2**2,alpha**(2*C2**2),miss))
print("   ==> *** THE KOONS TICK IS NOT THE GRAVITATIONAL UV CUTOFF. It misses by alpha^72. ***")

print("\nTABLE 4 -- can N_max = 137 serve as the cutoff instead?")
print("   N_max is a DIMENSIONLESS spectral cap (a mode number).")
print("   a heat-kernel cutoff eps needs dimensions of LENGTH^2.")
print("   ==> N_max alone cannot set eps: it needs a companion length L, and then eps ~ (L/N_max)^2.")
print("       *** Whatever supplies L is the actual cutoff; N_max only rescales it. ***")
print("       So 'N_max is the cutoff' is not yet a computation -- it is a missing length.")

print("\nTABLE 5 -- *** and the deeper problem with claiming Sakharov PREDICTS G ***")
print("   Sakharov gives   1/G ~ Lambda^2.")
print("   'G comes out right'  <=>  Lambda = m_Planck.")
print("   but m_Planck is DEFINED by  m_P = sqrt(hbar c / G).")
print("   ==> *** CIRCULAR. *** Setting the cutoff to the Planck scale and then recovering G is not")
print("       a prediction; it is the definition of the Planck scale read backwards. Induced gravity")
print("       explains the MECHANISM (gravity need not be fundamental); it does NOT supply G's VALUE")
print("       unless the cutoff is fixed INDEPENDENTLY.")

print("\n"+"="*104)
print("VERDICT")
print("="*104)
print(" (1) *** THE COMPUTATION RUNS, AND IT RETURNS A CLEAN NEGATIVE. *** With G ~ l_cutoff^2, the")
print("     Koons tick gives G_induced/G_Newton = alpha^{2 C_2^2} = alpha^72 ~ 1.4e-154 --")
print("     *** about 154 ORDERS OF MAGNITUDE too small. *** The Koons tick is NOT the")
print("     gravitational UV cutoff. I ran it because I named that shelf in 5337; it is empty.")
print()
print(" (2) *** AND THIS IS THE SHARED-PROPERTY TRAP IN ITS SCALE FORM. *** 'The substrate tick' and")
print("     'the gravitational UV cutoff' are both 'the shortest time', and they are NOT the same")
print("     object. Conflating them costs 154 orders. Same error the program has caught nine times")
print("     on integers -- this is its units-and-scales cousin, and I nearly walked into it by")
print("     nominating the tick myself last round.")
print()
print(" (3) N_max CANNOT REPAIR IT (Table 4): it is dimensionless, so it cannot BE a cutoff. It needs")
print("     a companion length, and whatever supplies that length is the real cutoff.")
print()
print(" (4) *** THE HONEST CEILING ON THE WHOLE INDUCED-GRAVITY ROUTE (Table 5): Sakharov gives")
print("     1/G ~ Lambda^2, so recovering G requires Lambda = m_Planck -- which is CIRCULAR, since")
print("     m_Planck is defined by G. *** Induced gravity is a MECHANISM claim, not a VALUE claim.")
print("     BST can honestly say 'gravity need not be fundamental; the EH density falls out of the")
print("     Kostant heat trace with a definite sign'. It CANNOT say 'BST predicts G' until some")
print("     independent BST quantity fixes the cutoff -- and the one candidate the corpus offered")
print("     is off by alpha^72.")
print("     @Lyra/@Keeper: this is a ceiling on the gravity program, found by running the")
print("     computation rather than by arguing about it. The paper's Section 11 wording already")
print("     sits below this ceiling and needs no change.")
