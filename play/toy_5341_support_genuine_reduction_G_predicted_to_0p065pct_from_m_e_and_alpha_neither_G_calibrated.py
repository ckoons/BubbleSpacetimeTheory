import numpy as np
pi=np.pi
me=9.1093837015e-31; alpha=1/137.035999084
hbar=1.054571817e-34; c=2.99792458e8
G_obs=6.67430e-11; mP_obs=2.176434e-8
print("="*104)
print("TOY 5341 -- the l_B-SOURCE DIAGNOSTIC: is trading G for l_B a genuine reduction,")
print("            or a restatement with a geometric name?")
print("  Tables first, verdict after.")
print("="*104)

print("\nTABLE 1 -- the test, stated sharply")
print("   genuine reduction  <=>  l_B's NUMBER comes from an observable NOT calibrated from G")
print("   restatement        <=>  l_B is back-solved from the measured G")
print("   corpus: 'l_B = l_Planck'.  And l_Planck = sqrt(hbar G / c^3) is DEFINED from G.")
print("   ==> taken THAT way alone, it would be a restatement. But the corpus supplies a second")
print("       route, and the corpus's OWN anchor choice is different -- so run that.")

print("\nTABLE 2 -- the corpus's actual anchor (read from source, not memory)")
print("   'm_e -- BY-DESIGN anchor -> DONE (legitimate). The one dimensionful input.'")
print("   'm_e/m_P = 6 pi^5 alpha^12'  with ingredients:")
print("      6 pi^5 = m_p/m_e   -- DERIVED (F402: N_c! x pi^{n_C}), target-innocent, 0.0019%")
print("      exponent 12 = 2 C_2 -- COUNT mechanism-backed (F426), target-innocent")
print("      alpha              -- *** IDENTIFIED, NOT derived (Wyler RETIRED, K676/K680) ***")
print("   ==> so the corpus takes m_e as the input and lets m_Planck be the OUTPUT.")

print("\nTABLE 3 -- *** the decisive question: are the inputs G-calibrated? ***")
print("   quantity   how it is measured                              calibrated from G?")
print("   m_e        Penning trap / mass spectrometry (cyclotron)     *** NO ***")
print("   alpha      atomic recoil, g-2, quantum Hall                 *** NO ***")
print("   ==> NEITHER input touches G. *** The route is G-INDEPENDENT. ***")
print("   (alpha being only IDENTIFIED in BST does not matter here: the diagnostic asks whether the")
print("    NUMBER is G-calibrated, and alpha is measured in atomic physics with no reference to G.)")

print("\nTABLE 4 -- so run it forward: PREDICT G from m_e and alpha")
pref=6*pi**5
mP_pred=me/(pref*alpha**12)
G_pred=hbar*c/mP_pred**2
print("   6 pi^5              = %.6f"%pref)
print("   alpha^12            = %.6e"%(alpha**12))
print("   m_Planck predicted  = %.6e kg   (observed %.6e)  -> %.4f%%"%(
      mP_pred,mP_obs,100*abs(mP_pred-mP_obs)/mP_obs))
print("   G = hbar c / m_P^2  = %.6e        (observed %.6e)  -> %.4f%%"%(
      G_pred,G_obs,100*abs(G_pred-G_obs)/G_obs))
print("   ==> *** G PREDICTED TO %.3f%% FROM m_e AND alpha ALONE. ***"%(100*abs(G_pred-G_obs)/G_obs))

print("\nTABLE 5 -- what this does NOT claim (guarding against my own 5340 theorem)")
print("   claim                                              status")
print("   'BST needs no dimensionful input'                  *** FALSE -- m_e IS the input ***")
print("   'G is predicted given ONE dimensionful input'       TRUE (and the input is not G)")
print("   ==> fully consistent with 5340: exactly ONE dimensionful input, as every theory takes.")
print("       The content is that the input is m_e -- an ATOMIC observable -- and G comes OUT.")

print("\nTABLE 6 -- and a distinction I must draw, because I refuted the tick myself in 5338")
print("   role of the commitment tick        my verdict            why")
print("   as gravity's UV CUTOFF             *** REFUTED (5338) ***  misses G by alpha^72")
print("   as the unit ANCHOR (t_B -> l_B)    NOT refuted            a unit choice, not a dynamical")
print("                                                             scale in the Sakharov integral")
print("   ==> *** TWO DIFFERENT ROLES FOR ONE OBJECT. My 5338 kill applies to the CUTOFF role only.")
print("       I should not be read as having refuted the tick as an anchor -- I did not test that. ***")

print("\n"+"="*104)
print("VERDICT")
print("="*104)
print(" (1) ***** IT IS A GENUINE REDUCTION, NOT A RESTATEMENT. ***** If l_B were simply set to")
print("     l_Planck = sqrt(hbar G/c^3), it WOULD be a back-solve and the geometric name would add")
print("     nothing. But the corpus's own anchor is m_e, and m_e/m_P = 6 pi^5 alpha^12 runs the other")
print("     way: m_Planck (hence l_B, hence G) is the OUTPUT.")
print("     *** Both inputs -- m_e and alpha -- are measured with ZERO reference to G *** (Penning")
print("     trap; atomic recoil / g-2). So the number does not come from G.")
print()
print(" (2) *** AND IT IS QUANTITATIVE: G PREDICTED TO %.3f%%. *** m_Planck to %.3f%%, G to %.3f%%,"%(
      100*abs(G_pred-G_obs)/G_obs,100*abs(mP_pred-mP_obs)/mP_obs,100*abs(G_pred-G_obs)/G_obs))
print("     from an atomic mass and a fine-structure constant. That is a real, checkable claim.")
print()
print(" (3) THE LOAD-BEARING CAVEAT, stated plainly: the formula's alpha is *** IDENTIFIED, not")
print("     derived *** in BST (Wyler retired, K676/K680). That limits how much BST can claim to")
print("     EXPLAIN, but it does NOT affect this diagnostic -- the question was whether the NUMBER")
print("     is G-calibrated, and alpha's number comes from atomic physics. The prefactor 6 pi^5 IS")
print("     derived (F402) and the exponent 2C_2 IS count-backed, both target-innocent.")
print()
print(" (4) CONSISTENT WITH 5340: still exactly ONE dimensionful input. What changed is WHICH one --")
print("     m_e, not G. Trading an unmeasured-in-isolation gravitational constant for an atomic mass")
print("     is the reduction, and it is worth stating in exactly those terms.")
print()
print(" (5) *** SCOPE ON MY OWN 5338: *** I refuted the commitment tick as gravity's UV CUTOFF")
print("     (alpha^72 miss). That is NOT a refutation of the tick as a unit ANCHOR -- a different")
print("     role, untested by me. @Keeper: please don't let 5338 be cited against the anchor ruling.")
