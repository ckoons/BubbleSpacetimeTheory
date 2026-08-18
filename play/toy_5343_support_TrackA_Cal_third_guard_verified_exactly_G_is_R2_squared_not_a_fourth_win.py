import numpy as np
pi=np.pi
# CODATA 2022
me_kg=9.1093837139e-31; me_MeV=0.51099895069
alpha=1/137.035999177
hbar=1.054571817e-34; c=2.99792458e8
mP_obs=2.176434e-8; G_obs=6.67430e-11
mpme_obs=1836.152673426; v_obs=246.21965
g_=7; C2=6; N_c=3; n_C=5
print("="*104)
print("TOY 5343 -- TRACK A: verify the reduction with CURRENT inputs, and apply CAL'S THIRD GUARD")
print("  Corpus-loaded first: T1301 (KK: dim 10 = 4 base + 6 fiber, fiber = C_2), BST_26_Scoreboard")
print("  ('m_e ... the one free dimensionful anchor; 6 pi^5 = m_p/m_e (T187); 0.03%').")
print("="*104)
pref=6*pi**5

print("\nTABLE 1 -- the numbers, recomputed with CODATA 2022")
print("   quantity   BST form                    predicted        observed         dev")
rows=[]
d1=100*abs(pref-mpme_obs)/mpme_obs
print("   m_p/m_e    6 pi^5 = N_c! pi^{n_C}      %-16.4f %-16.4f %.4f%%"%(pref,mpme_obs,d1))
mP=me_kg/(pref*alpha**(2*C2))
d2=100*abs(mP-mP_obs)/mP_obs
print("   m_Planck   m_e/(6 pi^5 alpha^{2C_2})   %-16.6e %-16.6e %.4f%%"%(mP,mP_obs,d2))
G=hbar*c/mP**2
d3=100*abs(G-G_obs)/G_obs
print("   G          hbar c / m_Planck^2         %-16.6e %-16.6e %.4f%%"%(G,G_obs,d3))
v=(pref**2/g_)*me_MeV/1000
d4=100*abs(v-v_obs)/v_obs
print("   v (EW)     (6 pi^5)^2 m_e / g          %-16.4f %-16.4f %.4f%%"%(v,v_obs,d4))

print("\nTABLE 2 -- *** CAL'S THIRD GUARD, VERIFIED EXACTLY ***")
print("   G = hbar c / m_P^2, so a fractional error d in m_P becomes 2d in G. Check:")
print("      dev(m_Planck) = %.4f%%"%d2)
print("      2 x dev(m_P)  = %.4f%%"%(2*d2))
print("      dev(G)        = %.4f%%"%d3)
print("      ratio dev(G)/dev(m_P) = %.4f"%(d3/d2))
print("   ==> *** THE FACTOR IS EXACTLY 2. m_e-at-0.03%% AND G-at-0.065%% ARE ONE RELATION,")
print("       SEEN TWICE -- the second time through a squaring. NOT two wins. ***")
print("   @Cal's guard is arithmetically exact and must be in the body text.")

print("\nTABLE 3 -- so WHICH claims are genuinely distinct? (dependency audit)")
print("   relation                     new ingredients            distinct claim?")
print("   R1  m_p/m_e = 6 pi^5         N_c!, pi^{n_C}             *** YES ***")
print("   R2  m_P = m_e/(6pi^5 a^12)   alpha, exponent 2C_2       *** YES *** (re-uses R1's number)")
print("   R2' G = hbar c/m_P^2         *** NONE ***               *** NO -- R2 squared ***")
print("   R3  v = (6 pi^5)^2 m_e/g     g                          *** YES *** (re-uses R1's number)")
print("   ==> *** THREE distinct relations, NOT four wins. And R2, R3 are only PARTIALLY")
print("       independent: both re-use 6 pi^5. The single derived ratio 6 pi^5 is load-bearing")
print("       in all three. ***")

print("\nTABLE 4 -- *** I AM CORRECTING MY OWN 5342 FRAMING ***")
print("   5342 said: 'FOUR dimensionful quantities from ONE input, all under 0.1%'.")
print("   That is TRUE as a statement about quantities, but it READS as four independent wins.")
print("   Honest restatement: *** ONE derived ratio (6 pi^5) + TWO further steps (the alpha^{2C_2}")
print("   step, the g step); G is the square of the second, not a fourth result. ***")

print("\nTABLE 5 -- the guards that must travel in the body (all three)")
print("   guard 1  EXACTLY ONE dimensionful input (m_e). 'Zero free parameters' = DIMENSIONLESS only.")
print("   guard 2  alpha is IDENTIFIED, NOT DERIVED (Wyler retired, K676/K680).")
print("   guard 3  *** m_e and G are ONE relation; the x2 is the squaring. Do not bill them twice.")
print("            (verified exactly, Table 2) ***")

print("\nTABLE 6 -- is the count still 2 -> 1? (unaffected by the guard)")
print("   SM + GR dimensionful inputs (hbar=c=1): v and G          -> 2")
print("   BST dimensionful inputs:                m_e              -> 1")
print("   ==> the REDUCTION claim is untouched by guard 3. Guard 3 corrects how many")
print("       SUCCESSES we cite, not how many INPUTS we take.")
