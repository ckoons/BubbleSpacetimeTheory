import numpy as np
from math import pi
print("="*104)
print("TOY 5367 -- DERIVE Delta FOR DECONFINEMENT (the surviving job). Tables first.")
print("="*104)
me=0.51099895069; rank,N_c,n_C,g_int=2,3,5,7

print("\nTABLE 0 -- *** first, I concede the charge/state point, because it lands on MY result ***")
print("   my 5364/5365 exponential was about a STATE (a decohering superposition).")
print("   @Casey's object is a CHARGE -- a superselection integer. No observable connects sectors,")
print("   so a superselection charge cannot change by ANY physical process: exactly conserved.")
print("   ==> *** my finite-tau_p price was computed for the wrong object. It is correctly RETIRED,")
print("       and the wording question I put to @Keeper is answered: 'no proton decay' can stand")
print("       as ABSOLUTE. *** Conceded cleanly -- the distinction is real and it is Casey's.")

print("\nTABLE 1 -- Delta from the corpus (W-18, banked; N_c-dependence is FINE here)")
L=(rank**2*pi**n_C/N_c)*me
print("   Lambda_QCD = rank^2 pi^{n_C} m_e / N_c = %.2f MeV"%L)
print("   ** the circularity that blocked 5366 does NOT apply now: there we used Delta to FORCE N_c;")
print("      here we use it to PREDICT an observable. Using N_c as an input to a prediction is fine. **")

print("\nTABLE 2 -- the deconfinement condition is a DEGREE-OF-FREEDOM COUNT (AC(0) mode)")
print("   Stefan-Boltzmann: p = g (pi^2/90) T^4.  Bag model: transition when p_QGP - B = p_hadron")
print("       (g_q - g_h)(pi^2/90) T_c^4 = B   ->   T_c = [90 B / ((g_q-g_h) pi^2)]^{1/4}")
print("\n   counting the degrees of freedom -- all from BST integers:")
print("      gluons          : 2 polarisations x (N_c^2 - 1) = 2 x %d = %d"%(N_c**2-1,2*(N_c**2-1)))
print("      quarks          : (7/8) x 2 spin x 2 particle/anti x N_c x N_f")
print("      hadron phase    : pions = %d (the N_c^2-1 = 3 light pseudoscalars at N_f=2)"%3)
gh=3
for Nf in (2,3):
    gq=2*(N_c**2-1)+ (7/8)*2*2*N_c*Nf
    print("      N_f = %d -> g_q = %d + %.1f = %.1f ;  g_q - g_h = %.1f"%(Nf,2*(N_c**2-1),(7/8)*2*2*N_c*Nf,gq,gq-gh))

print("\nTABLE 3 -- *** the prediction (identifying B^{1/4} = Lambda_QCD) ***")
print("   N_f   g_q-g_h   [90/((g_q-g_h) pi^2)]^{1/4}   T_c predicted   T_c observed   dev")
for Nf in (2,3):
    gq=2*(N_c**2-1)+(7/8)*2*2*N_c*Nf
    f=(90.0/((gq-gh)*pi**2))**0.25
    Tc=L*f
    print("   %-5d %-9.1f %-28.4f %-15.2f %-14s %.1f%%"%(Nf,gq-gh,f,Tc,"~155 MeV",100*abs(Tc-155)/155))
print("   ==> at the transition only u,d are light, so *** N_f = 2 is the physically right count ***")
print("       -- not chosen to fit. It gives T_c = 150.1 MeV vs ~155 observed.")

print("\nTABLE 4 -- ingredient audit (what is derived, what is identified)")
print("   ingredient                         status")
print("   Lambda_QCD = rank^2 pi^n_C m_e/N_c  DERIVED (W-18, banked)")
print("   gluon count 2(N_c^2-1) = 16         COUNTING from N_c = 3")
print("   quark count (7/8).4.N_c.N_f         COUNTING (7/8 = fermion SB factor, standard)")
print("   pion count 3                        COUNTING")
print("   bag-model / Stefan-Boltzmann form   STANDARD THERMODYNAMICS (not BST)")
print("   *** B^{1/4} = Lambda_QCD ***        *** IDENTIFICATION -- the one un-derived step ***")
print("   ==> one identification, everything else counting or standard. Stated, not buried.")

print("\n"+"="*104)
print("VERDICT")
print("="*104)
print(" (1) *** CONCEDED, AND IT COSTS ME A RESULT: my exponential was about a decohering STATE;")
print("     @Casey's protected object is a superselection CHARGE, which is exactly conserved. ***")
print("     So the finite-tau_p price is correctly retired and 'no proton decay' can stand as")
print("     ABSOLUTE. That answers the wording question I raised, and it answers it against me.")
print()
print(" (2) *** Delta FOR DECONFINEMENT DERIVES, AND THE PREDICTION LANDS: T_c = 150.1 MeV vs the")
print("     lattice ~155 MeV -- 3.2%%. *** Ingredients: BST's own Lambda_QCD (W-18) plus pure")
print("     degree-of-freedom COUNTING (16 gluon dof from N_c, the 7/8 fermion factor, 3 pions).")
print()
print(" (3) *** AND N_f = 2 IS FORCED BY THE PHYSICS, NOT CHOSEN: *** at T ~ 155 MeV only u and d")
print("     are light. N_f = 3 would give 140.3 MeV (9.5%%), so the better number is also the")
print("     physically correct one -- which is the right way round.")
print()
print(" (4) THE ONE UN-DERIVED STEP, stated plainly: *** B^{1/4} = Lambda_QCD is an IDENTIFICATION. ***")
print("     Everything else is counting or standard thermodynamics. A referee will go straight there,")
print("     so it belongs in the sentence, not a footnote.")
print()
print(" (5) NET: the deconfinement prediction is now QUANTITATIVE (3.2%%), not just qualitative")
print("     ('protection collapses near Lambda'). *** That is a real, checkable BST number in the")
print("     strong sector -- and it survived the circularity that killed the forcing use, because")
print("     predicting an observable with N_c is fine; forcing N_c with it is not. ***")
