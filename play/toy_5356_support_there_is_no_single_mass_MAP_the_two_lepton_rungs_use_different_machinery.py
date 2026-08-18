import numpy as np
from math import pi, gamma, log
print("="*104)
print("TOY 5356 -- THE MASS MAP: is there a MAP, or are there per-rung FORMS?")
print("  Before deriving the assembly rule, test that an assembly rule EXISTS. Tables first.")
print("="*104)
C2=6; n_C=5
me=0.51099895069; mmu=105.6583755; mtau=1776.86
obs_mu, obs_tau = mmu/me, mtau/me

print("\nTABLE 1 -- first, the assembly of 24/pi^2 IS already exact and corpus-banked")
vS4=8*pi**2/3
print("   vol(S^4) = 8 pi^2/3 = %.6f"%vS4)
print("   2^{C_2} / vol(S^4) = %d / %.6f = %.8f"%(2**C2,vS4,2**C2/vS4))
print("   24/pi^2                             = %.8f"%(24/pi**2))
print("   exact? %s"%(abs(2**C2/vS4 - 24/pi**2)<1e-12))
print("   ==> *** 24/pi^2 = 2^{C_2}/vol(S^4), EXACTLY. *** (corpus-banked, not new here.)")
print("       and 24 = Gamma(n_C) = (n_C-1)!  -- so the muon form is")
print("       m_mu/m_e = (2^{C_2}/vol(S^4))^{C_2},  every ingredient a corpus object.")

print("\nTABLE 2 -- *** but the exponent 6 has THREE readings. Which is load-bearing? ***")
for nm,v in [("C_2 (quadratic Casimir)",6),("dim SO(4)",6),("KK fibre dim (T1301: 10 = 4+6)",6)]:
    print("   %-34s = %d"%(nm,v))
print("   ==> three corpus objects, one integer. *** Shared-integer situation: the form does not")
print("       tell us WHICH 6 it is, and they have different mechanisms. Flagging, not choosing. ***")

print("\nTABLE 3 -- *** THE DECISIVE TEST: does the FORM give the OTHER rung? ***")
print("   A MAP produces every rung from one rule. Check the corpus's two lepton rungs:")
print("   rung        corpus form            value        observed     dev")
mu_pred=(24/pi**2)**C2; tau_pred=49*71
print("   m_mu/m_e    (24/pi^2)^{C_2}        %-12.4f %-12.4f %.4f%%"%(mu_pred,obs_mu,100*abs(mu_pred-obs_mu)/obs_mu))
print("   m_tau/m_e   49 . 71                %-12.4f %-12.4f %.4f%%"%(tau_pred,obs_tau,100*abs(tau_pred-obs_tau)/obs_tau))
print("   ==> *** TWO COMPLETELY DIFFERENT FORMS. One is (X)^{C_2} with X a volume ratio; the other")
print("       is a product of two primes. They share NO structure. ***")

print("\nTABLE 4 -- try to force the tau into the muon's form (does X exist?)")
X=pi**2*tau_pred**(1.0/C2)
print("   if m_tau/m_e = (X/pi^2)^{C_2} then X = pi^2 (m_tau/m_e)^{1/C_2} = %.4f"%X)
print("   is X a corpus object?  Gamma(5)=24, Gamma(6)=120, 2^{C_2}=64, N_max=137, 6pi^5=1836 ...")
for nm,v in [("Gamma(5)",gamma(5)),("Gamma(6)",gamma(6)),("2^C_2",64),("N_max",137)]:
    print("      %-12s = %-10.4f   ratio X/%s = %.4f"%(nm,v,nm,X/v))
print("   ==> *** X = %.4f matches no corpus object. The muon form does NOT extend to the tau. ***"%X)

print("\nTABLE 5 -- and the reverse: does the tau's form give the muon?")
print("   49 . 71 is a product of two primes. The muon would need a comparable pair:")
print("   m_mu/m_e = %.4f -- factor it: nearest prime products"%obs_mu)
for p in [2,3,5,7,11,13]:
    q=obs_mu/p
    print("      %-3d x %-10.4f  (integer? %s)"%(p,q,abs(q-round(q))<0.02))
print("   ==> no clean two-prime form for the muon either. *** The two rungs genuinely use")
print("       different machinery. ***")

print("\n"+"="*104)
print("VERDICT")
print("="*104)
print(" (1) *** I CANNOT DERIVE THE ASSEMBLY RULE, AND I NOW THINK THAT IS THE RIGHT ANSWER RATHER")
print("     THAN A FAILURE: THERE IS NO SINGLE MAP TO DERIVE. *** The corpus has")
print("       m_mu/m_e = (2^{C_2}/vol(S^4))^{C_2}   -- a volume ratio raised to a power")
print("       m_tau/m_e = 49 . 71                    -- a product of two primes")
print("     These share no structure (Table 3), the muon's form does not extend to the tau")
print("     (Table 4, X = %.2f matches nothing), and the tau's does not extend to the muon"%X)
print("     (Table 5). *** 'Derive the map' presupposes a map; the evidence says there isn't one yet. ***")
print()
print(" (2) WHAT *IS* SOLID: 24/pi^2 = 2^{C_2}/vol(S^4) EXACTLY, and 24 = Gamma(n_C). So the muon")
print("     form's INGREDIENTS are all corpus objects -- that part is real and already banked.")
print("     What is missing is why THOSE ingredients, in THAT arrangement, for THIS rung.")
print()
print(" (3) *** AND THE EXPONENT CARRIES A SHARED-INTEGER AMBIGUITY: 6 = C_2 = dim SO(4) = the KK")
print("     fibre dimension (T1301). Three corpus objects, one integer, different mechanisms. ***")
print("     The form cannot tell us which; a derivation would have to.")
print()
print(" (4) SO THE MASS TOWER'S REAL FRONTIER IS NOT 'DERIVE THE MUON ASSEMBLY' -- it is")
print("     *** UNIFY THE PER-RUNG FORMS. *** Until one rule produces both rungs, deriving either")
print("     one in isolation would be explaining a coincidence. @Lyra/@Grace: that is the question")
print("     I would put on the board -- what single object degenerates to (X)^{C_2} at gen-2 and to")
print("     49 . 71 at gen-3? If nothing does, the tower is a patchwork and we should say so.")
print()
print(" (5) I did NOT reverse-engineer an assembly, and I am not going to. @Keeper was right that")
print("     naming pieces of a known number is not deriving it -- and the same rule says inventing")
print("     an assembly that reaches 206.77 would be worse.")
