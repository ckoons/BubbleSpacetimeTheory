import numpy as np
from math import pi, sqrt
print("="*104)
print("TOY 5357 -- CAN ONE OBJECT PRODUCE BOTH LEPTON FORMS? Testing the corpus's own candidate.")
print("  Tables first, verdict after.")
print("="*104)
me=0.51099895069; mmu=105.6583755; mtau_obs=1776.86
rank=2; N_c=3; C2=6

print("\nTABLE 1 -- the candidate the corpus already has: KOIDE, Q = rank/N_c = 2/3")
Q=lambda ms: sum(ms)/sum(sqrt(m) for m in ms)**2
qobs=Q([me,mmu,mtau_obs])
print("   Q_observed = (sum m)/(sum sqrt m)^2 = %.9f"%qobs)
print("   rank/N_c   = %.9f"%(rank/N_c))
print("   deviation  = %.4f%%   *** ONE equation relating ALL THREE masses ***"%(100*abs(qobs-rank/N_c)/(rank/N_c)))

print("\nTABLE 2 -- *** so run it as a PREDICTOR: does Koide give m_tau from m_e and m_mu? ***")
a,b=sqrt(me),sqrt(mmu)
disc=3*(a*a+4*a*b+b*b)
cp=2*(a+b)+sqrt(disc); cm=2*(a+b)-sqrt(disc)
for lbl,c in [("+ branch",cp),("- branch",cm)]:
    m=c*c
    print("   %-10s m_tau = %-12.4f MeV   vs observed %.2f   -> %.4f%%"%(lbl,m,mtau_obs,100*abs(m-mtau_obs)/mtau_obs))
print("   ==> *** THE + BRANCH PREDICTS m_tau TO %.4f%% FROM m_e AND m_mu ALONE. ***"%(100*abs(cp*cp-mtau_obs)/mtau_obs))
print("       So a SINGLE object DOES cover the lepton tower -- at the level of NUMBERS.")

print("\nTABLE 3 -- but does it produce the two closed FORMS?")
print("   Koide outputs a NUMBER (1776.89 MeV). It does not output '(24/pi^2)^{C_2}' or '49.71'.")
print("   form                what produces it")
print("   (24/pi^2)^{C_2}     a separate identification of m_mu/m_e")
print("   49 . 71             a separate identification of m_tau/m_e")
print("   Koide Q = rank/N_c  a RELATION among the three, producing no closed form at all")
print("   ==> *** ONE OBJECT PRODUCES THE NUMBERS; NO OBJECT PRODUCES THE FORMS. *** The forms are")
print("       independent identifications layered on top of a tower Koide already ties together.")

print("\nTABLE 4 -- *** AND THAT EXPOSES A DOUBLE-COUNT IN THE LEPTON SECTOR ***")
mmu_pred=me*(24/pi**2)**C2
a2,b2=sqrt(me),sqrt(mmu_pred)
c2=2*(a2+b2)+sqrt(3*(a2*a2+4*a2*b2+b2*b2))
mtau_chain=c2*c2
print("   chain:  m_e (anchor)  ->  x (24/pi^2)^{C_2}  ->  m_mu  ->  Koide  ->  m_tau")
print("     m_mu  from the form  = %.6f MeV   (obs %.6f, %.4f%%)"%(mmu_pred,mmu,100*abs(mmu_pred-mmu)/mmu))
print("     m_tau from the chain = %.4f MeV     (obs %.2f, %.4f%%)"%(mtau_chain,mtau_obs,100*abs(mtau_chain-mtau_obs)/mtau_obs))
print("     m_tau from 49 . 71   = %.4f MeV     (obs %.2f, %.4f%%)"%(49*71*me,mtau_obs,100*abs(49*71*me-mtau_obs)/mtau_obs))
print("   ==> *** m_tau IS ALREADY DETERMINED by m_e + the muon form + Koide. So 49.71 is a SECOND")
print("       determination of a number the chain already fixes -- a RE-DESCRIPTION, not an")
print("       independent success. ***")

print("\nTABLE 5 -- the honest count for the charged-lepton sector")
print("   item                          status")
print("   m_e                           the one dimensionful ANCHOR (input)")
print("   m_mu/m_e = (24/pi^2)^{C_2}    ONE identification (ingredients corpus-banked)")
print("   Koide Q = rank/N_c            ONE relation (derived from rank-2 per corpus)")
print("   m_tau/m_e = 49 . 71           *** REDUNDANT -- fixed by the two above ***")
print("   ==> *** 1 anchor + 2 independent items => the whole charged-lepton tower. NOT three")
print("       successes; two. ***")

print("\n"+"="*104)
print("VERDICT")
print("="*104)
print(" (1) *** THE ANSWER TO THE ASSIGNED QUESTION IS SPLIT, AND THE SPLIT IS THE POINT: ***")
print("     a single object DOES produce both masses -- *** KOIDE, Q = rank/N_c, which predicts")
print("     m_tau from m_e and m_mu to %.4f%%. *** But NO object produces both closed FORMS."%(100*abs(cp*cp-mtau_obs)/mtau_obs))
print("     The forms are independent identifications; the NUMBERS are unified.")
print()
print(" (2) *** SO I REFINE MY OWN 5356 VERDICT. *** I wrote 'the tower is a patchwork'. More")
print("     precisely: *** the closed FORMS are a patchwork; the NUMBERS are unified by Koide. ***")
print("     That is a real correction in the corpus's favour, and I would rather state it than")
print("     leave my harsher sentence standing.")
print()
print(" (3) *** AND IT EXPOSES A DOUBLE-COUNT: m_tau is already determined by m_e + the muon form")
print("     + Koide (chain gives %.2f MeV, %.4f%%). So 49.71 is a RE-DESCRIPTION, not a third"%(mtau_chain,100*abs(mtau_chain-mtau_obs)/mtau_obs))
print("     independent success. *** @Cal -- same shape as the gravity cluster, in the lepton")
print("     sector: the honest count is 1 anchor + 2 items, not 3 predictions.")
print()
print(" (4) WHAT REMAINS GENUINELY OPEN: why (24/pi^2)^{C_2} for the SECOND rung specifically. Koide")
print("     ties the tower together but needs TWO masses as input; the muon form is what supplies")
print("     the second. Derive that and the sector closes on m_e alone. *** That is now the single")
print("     open question in the charged-lepton sector -- much sharper than 'the tower is a patchwork'. ***")
