import numpy as np
from math import pi
print("="*104)
print("TOY 5366 -- DERIVE THE GAP, DON'T BORROW IT. Is BST's own Lambda_QCD N_c-free?")
print("="*104)
me=0.51099895069; rank,N_c,n_C=2,3,5

print("\nTABLE 1 -- *** first: 'borrowed' was too harsh. The corpus DERIVES the gap. ***")
print("   W-18 (CLOSED, toy 2425):  Lambda_QCD = (rank^2 . pi^{n_C} / N_c) . m_e")
L=(rank**2*pi**n_C/N_c)*me
print("   = (4 . pi^5 / 3) . m_e = %.4f . %.6f MeV = %.2f MeV"%(rank**2*pi**n_C/N_c,me,L))
print("   observed Lambda_QCD ~ 200-220 MeV (scheme-dependent)  ->  lands in range: %s"%(200<=L<=220))
print("   ==> *** so Delta IS derivable from the anchor m_e plus BST integers -- I should not have")
print("       said 'borrowed from QCD' in 5365. Correcting my own wording. ***")

print("\nTABLE 2 -- *** BUT: does the derivation contain N_c? (the circularity test) ***")
print("   Lambda_QCD = rank^2 . pi^{n_C} . m_e / N_c")
print("                                              ^^^^  *** N_c IS IN THE FORMULA ***")
print("   ==> *** using this gap to FORCE N_c = 3 is circular. @Keeper's warning fires exactly here,")
print("       one level down, and it fires on the corpus's own banked result. ***")

print("\nTABLE 3 -- can it be written N_c-free? (the escape, if there is one)")
print("   The corpus separately banks N_c = a = n - 2 (FK multiplicity, 5344).")
print("   Substituting, the gap becomes a PURE FUNCTION OF THE DIMENSION n:")
print("       Delta/m_e = rank^2 . pi^n / (n - 2)")
print("   n     Delta/m_e = 4 pi^n/(n-2)    Delta (MeV)   monotone?")
prev=None
for n in range(3,9):
    v=4*pi**n/(n-2); d=v*me
    print("   %-5d %-27.3f %-13.2f %s"%(n,v,d,"increasing" if prev is None or v>prev else "DECREASING"))
    prev=v
print("   ==> *** strictly monotone in n. So the MEASURED value picks n UNIQUELY. ***")

print("\nTABLE 4 -- so run it as a DETERMINATION: what n does the measured gap give?")
for Lobs in (200.0,208.0,220.0):
    # solve 4 pi^n/(n-2) = Lobs/me
    tgt=Lobs/me
    ns=np.linspace(3.0,7.0,400001)
    vals=4*np.pi**ns/(ns-2)
    n_star=ns[np.argmin(np.abs(vals-tgt))]
    print("   Lambda_obs = %-6.1f MeV -> n = %.3f"%(Lobs,n_star))
print("   ==> the measured confinement scale lands on *** n ~ 5 *** across the plausible range.")

print("\n"+"="*104)
print("VERDICT")
print("="*104)
print(" (1) *** I CORRECT MY OWN 5365 WORDING: the gap is NOT 'borrowed from QCD'. *** BST derives")
print("     it (W-18, banked): Lambda_QCD = rank^2 pi^{n_C} m_e/N_c = %.1f MeV, in the observed"%L)
print("     range. Saying 'borrowed' understated the corpus. Owned.")
print()
print(" (2) *** BUT THE DERIVATION CONTAINS N_c EXPLICITLY -- so it cannot force N_c. *** Using this")
print("     gap to justify N_c = 3 is circular, and @Keeper's warning fires on our own banked result,")
print("     one level down from where it was aimed. That is the honest status of owed-item 3.")
print()
print(" (3) *** THE N_c-FREE REWRITE EXISTS, and it is informative: *** substituting the banked")
print("     N_c = a = n-2 gives Delta/m_e = rank^2 pi^n/(n-2), a pure function of the DIMENSION,")
print("     strictly monotone. So the measured gap picks n uniquely -- and it picks *** n ~ 5 ***")
print("     across the whole plausible Lambda range (200-220 MeV).")
print()
print(" (4) *** BUT THAT IS A DETERMINATION, NOT A FORCING -- and the distinction is the whole point")
print("     of today. *** The measured confinement scale MEASURES n_C = 5; it does not derive it.")
print("     Which is exactly the boundary the day has converged on from four independent directions:")
print("     Condition 5 (identity), the action (no critical point), the uniqueness set (~6-8")
print("     selections), and now the gap. *** n_C = 5 is an input, and a well-measured one. ***")
print()
print(" (5) THE OWED THREE, updated: (a) finite tau_p -- STANDS; (b) the rate bound p < 8.2e-82 --")
print("     STANDS, underived; (c) derive Delta -- *** PARTIALLY DISCHARGED: derivable but not")
print("     N_c-free, so it cannot serve the forcing argument. *** Net: the escape route still does")
print("     not close, and it does not close for the reason @Keeper predicted.")
