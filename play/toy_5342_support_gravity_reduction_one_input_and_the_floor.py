import numpy as np
pi=np.pi
me_MeV=0.51099895; me_kg=9.1093837015e-31
alpha=1/137.035999084; g_=7
hbar=1.054571817e-34; c=2.99792458e8
G_obs=6.67430e-11; mP_obs=2.176434e-8
mp_me_obs=1836.15267343; v_obs=246.21965
print("="*104)
print("TOY 5342 -- the gravity reduction, verified end-to-end from ONE input, and the floor question")
print("="*104)
pref=6*pi**5
print("\nTABLE 1 -- everything below takes m_e as the ONLY dimensionful input")
print("   quantity   BST form                         predicted        observed         dev")
mp_pred=pref
print("   m_p/m_e    6 pi^5 = N_c! pi^{n_C}           %-16.4f %-16.4f %.4f%%"%(
      mp_pred,mp_me_obs,100*abs(mp_pred-mp_me_obs)/mp_me_obs))
mP_pred=me_kg/(pref*alpha**12)
print("   m_Planck   m_e/(6 pi^5 alpha^{2C_2})        %-16.6e %-16.6e %.4f%%"%(
      mP_pred,mP_obs,100*abs(mP_pred-mP_obs)/mP_obs))
G_pred=hbar*c/mP_pred**2
print("   G          hbar c / m_Planck^2              %-16.6e %-16.6e %.4f%%"%(
      G_pred,G_obs,100*abs(G_pred-G_obs)/G_obs))
v_pred=(pref**2/g_)*me_MeV/1000
print("   v (EW)     (6 pi^5)^2 m_e / g               %-16.4f %-16.4f %.4f%%"%(
      v_pred,v_obs,100*abs(v_pred-v_obs)/v_obs))
print("   ==> *** FOUR dimensionful quantities from ONE input, all under 0.1%. ***")

print("\nTABLE 2 -- the reduction, counted honestly (natural units hbar = c = 1)")
print("   theory        dimensionful inputs           count")
print("   SM + GR       v (electroweak) and G          *** 2 ***")
print("   BST           m_e                            *** 1 ***")
print("   ==> the reduction is 2 -> 1. Both v and G become OUTPUTS of the single atomic anchor.")

print("\nTABLE 3 -- *** THE FLOOR QUESTION: can anything fix m_e in absolute terms? ***")
print("   BST's content: 5 integers + a geometry + dimensionless ratios -- ALL dimensionless.")
print("   A dimensionless set cannot produce a quantity with units. (Toy 5340.)")
print("   ==> *** NO. PROVABLY NO. The door from 'input' to 'prediction' DOES NOT EXIST. ***")
print("   and the floor is not 0, it is 1:")
print("      minimum dimensionful inputs for ANY theory that predicts a dimensionful quantity = 1")
print("   ==> *** BST IS AT THE FLOOR. You cannot do better than one, and BST takes one. ***")
print("       That reframes the whole question: 'm_e is an input' is not a gap to be closed --")
print("       it is the theoretical MINIMUM, already achieved.")

print("\nTABLE 4 -- the two guards that must travel with the claim")
print("   guard 1  EXACTLY ONE INPUT. m_e is an input, not a prediction. 'Zero free parameters'")
print("            refers to the DIMENSIONLESS content only. Never write it unqualified.")
print("   guard 2  alpha is IDENTIFIED, NOT DERIVED (Wyler retired, K676/K680). It enters the")
print("            m_Planck formula as a measured number. BST does not currently explain it.")
print("   (guard 2 does not weaken the REDUCTION -- alpha is measured G-independently, toy 5341 --")
print("    but it does bound what may be claimed as EXPLAINED.)")
print("\n   ingredient audit of  m_e/m_P = 6 pi^5 alpha^{2 C_2}:")
print("      6 pi^5 = N_c! pi^{n_C}   DERIVED (F402), target-innocent, 0.0019%%")
print("      exponent 2 C_2 = 12      COUNT mechanism-backed (F426), target-innocent")
print("      alpha                    *** IDENTIFIED -- the one open ingredient ***")
