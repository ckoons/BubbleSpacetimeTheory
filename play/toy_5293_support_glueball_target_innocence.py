import numpy as np
print("="*92)
print("(C) THE GLUEBALL TIER: Delta = c_2 * pi^5 * m_e with c_2 = 11 (2-form K-type Casimir)")
print("="*92)
me=0.511; pi5=np.pi**5
print("  pi^5 = %.5f ;  pi^5 * m_e = %.4f MeV per unit of c_2"%(pi5,pi5*me))
print("  c_2 = 11  =>  Delta = %.2f MeV"%(11*pi5*me))
print("\n  the comparison value: quenched-lattice 0++ glueball, Morningstar-Peardon 1999:")
obs,stat,syst=1730.0,50.0,80.0
tot=np.hypot(stat,syst)
print("     1730 +- 50 (stat) +- 80 (syst) MeV  =>  combined +-%.0f MeV"%tot)
pred=11*pi5*me
print("     BST %.1f vs 1730 -> deviation %.2f%% , %.2f sigma"%(pred,100*abs(pred-obs)/obs,abs(pred-obs)/tot))
print()
print("  ★ TARGET-INNOCENCE CHECK -- how discriminating is that agreement, really?")
print("     the formula's allowed values form an INTEGER GRID of spacing %.1f MeV."%(pi5*me))
print("     the comparison window is +-%.0f MeV, i.e. %.0f MeV wide."%(tot,2*tot))
ratio=2*tot/(pi5*me)
print("     window / grid spacing = %.2f"%ratio)
for c in range(9,14):
    v=c*pi5*me
    print("       c_2=%2d -> %8.1f MeV   %s"%(c,v,"INSIDE the window" if abs(v-obs)<tot else ""))
print()
if ratio>=1:
    print("  ⟹ THE WINDOW IS WIDER THAN THE GRID SPACING. SOME integer c_2 is GUARANTEED to land in it.")
    print("     ⟹ THE 0.6%% AGREEMENT CARRIES ESSENTIALLY NO DISCRIMINATING WEIGHT. It is not evidence.")
else:
    print("  ⟹ window narrower than the grid: the hit is %.0f%% likely by chance."%(100*ratio))
print("     THE ENTIRE CONTENT IS WHETHER c_2 = 11 IS DERIVED TARGET-INNOCENTLY (Lyra: the 2-form")
print("     K-type Casimir). If it is, the result is the DERIVATION of 11; the 0.6%% is decoration.")
print("     If it is not, there is nothing here at all.")
print()
print("  ★★ AND THE SECOND TIER CAUTION: 1730 IS ITSELF A LATTICE COMPUTATION, NOT A MEASUREMENT.")
print("     The 0++ glueball has never been unambiguously observed; f_0(1710) is a candidate that")
print("     MIXES with q-qbar states. So this is a computation-to-computation comparison, and it")
print("     cannot carry the tier an experimental match would. I-tier is right; I would add the")
print("     word 'lattice' to the claim line so no referee mistakes it for data.")
