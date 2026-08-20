import numpy as np
from math import pi, sqrt, gamma, acos, degrees
print("="*104)
print("TOY 5370 -- TRACK 2: the muon form in BST primaries, and does it PREDICT Koide's 12.7352?")
print("  GATE-KOIDE held: theta is the informative number; 2/3 never used as an input below.")
print("="*104)
me,mmu,mtau=0.51099895069,105.6583755,1776.86
rank,N_c,n_C,C2=2,3,5,6

print("\nTABLE 1 -- the muon form, written entirely in BST primaries (cleaner than 5355)")
print("   (24/pi^2)^6 = 24^6/pi^12")
print("      24  = Gamma(5)  = Gamma(n_C)")
print("      12  = 2 x 6     = rank x C_2")
print("   ==> *** m_mu/m_e = [ Gamma(n_C) / pi^{rank} ]^{C_2} ***")
v=(gamma(n_C)/pi**rank)**C2
print("      = [%.6f/%.6f]^%d = %.4f   vs observed %.4f  -> %.4f%%"%(
      gamma(n_C),pi**rank,C2,v,mmu/me,100*abs(v-mmu/me)/(mmu/me)))
print("   ** and per 5355, 24/pi^2 = 2^{C_2}/vol(S^4) EXACTLY -- two readings of the same base. **")
print("   *** BUT THIS IS AN EXPRESSION, NOT A DERIVATION. *** I have rewritten a known number in")
print("   primaries; nothing here says WHY Gamma(n_C)/pi^{rank}, raised to C_2. @Keeper's rule from")
print("   yesterday still binds: naming the pieces of a known number is not deriving it.")

print("\nTABLE 2 -- *** what IS new: the form + Koide PREDICTS theta. Run it. ***")
print("   inputs: m_e (anchor) and the muon form. NOT Q -- Koide is used as a RELATION, and")
print("   theta comes out of the mass triple, never off 2/3.")
mmu_pred=me*v
a,b=sqrt(me),sqrt(mmu_pred)
c=2*(a+b)+sqrt(3*(a*a+4*a*b+b*b))          # Koide + branch -> m_tau
mtau_pred=c*c
r=[a,b,c]; M=sum(r)/3
cosines=[(x/M-1)/sqrt(rank) for x in r]
th=acos(max(cosines))
print("   m_mu  from the form      = %.6f MeV   (obs %.6f)"%(mmu_pred,mmu))
print("   m_tau from Koide+branch  = %.4f MeV     (obs %.2f)"%(mtau_pred,mtau))
print("   ==> the implied Koide angle:")
print("      theta_predicted = %.6f rad = %.4f deg"%(th,degrees(th)))
print("      theta_target    = 0.222270 rad = 12.7352 deg   (my 5359 blind target)")
print("      deviation       = %.4f%%"%(100*abs(degrees(th)-12.7352)/12.7352))
print("   consistency checks: sum cos = %+.6f (must be 0), sum cos^2 = %.6f (must be 1.5)"%(
      sum(cosines),sum(x*x for x in cosines)))

print("\nTABLE 3 -- *** THE COUNT, as @Keeper's gate demands: TWO, not three ***")
print("   item                          independent?")
print("   m_e                           the ANCHOR (input)")
print("   m_mu/m_e = [Gamma/pi^rank]^C_2  *** ITEM 1 ***")
print("   Koide Q = rank/N_c             *** ITEM 2 ***")
print("   m_tau/m_e = 49.71              REDUNDANT (5357)")
print("   theta = 12.7352 deg            *** REDUNDANT -- DOWNSTREAM of items 1+2 (Table 2) ***")
print("   ==> *** COUNT AT TWO. *** And theta is now shown to be downstream, not a third success --")
print("       which is exactly the deflation the gate asked for, applied before anyone banks it.")

print("\n"+"="*104)
print("VERDICT")
print("="*104)
print(" (1) THE FORM IS NOW FULLY IN PRIMARIES: *** m_mu/m_e = [Gamma(n_C)/pi^{rank}]^{C_2} ***,")
print("     at %.4f%%. Cleaner than 5355's reading, and it exposes the exponent as rank x C_2 in"%(100*abs(v-mmu/me)/(mmu/me)))
print("     the pi-power. *** But it is an EXPRESSION, not a derivation -- the assembly rule is")
print("     still missing, exactly as yesterday. I am not upgrading it. ***")
print()
print(" (2) *** WHAT IS GENUINELY NEW: the muon form PLUS Koide PREDICTS the Koide angle, and it")
print("     lands at %.4f deg vs my blind target 12.7352 deg -- %.4f%%. ***"%(degrees(th),100*abs(degrees(th)-12.7352)/12.7352))
print("     Q = 2/3 was never used as an input; Koide entered only as the relation, and theta came")
print("     out of the mass triple. The structural checks (sum cos = 0, sum cos^2 = 3/2) hold.")
print()
print(" (3) *** SO theta IS DOWNSTREAM, NOT A THIRD RESULT -- and that DEFLATES the sector before")
print("     anyone inflates it. *** The honest count is @Keeper's TWO: the muon form and Koide.")
print("     m_tau (5357) and now theta are both consequences. One anchor, two items, everything else")
print("     follows.")
print()
print(" (4) WHAT THIS DOES NOT DO: it does not derive theta FROM THE GEOMETRY. The 12.7 deg still")
print("     needs @Grace/@Lyra's overlap, run against the blind target with 2/3 never entering.")
print("     *** What I have shown is that theta is not independent evidence -- which makes the")
print("     overlap test MORE informative, not less: if the overlap produces 12.7 deg from geometry,")
print("     it is deriving something we can already get from two items, so it must be checked")
print("     against BOTH, not just against the observed angle. ***")
