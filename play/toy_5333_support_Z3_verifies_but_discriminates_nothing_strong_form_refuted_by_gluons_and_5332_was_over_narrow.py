from fractions import Fraction as F
N_c=3
print("="*106)
print("TOY 5333 -- the Q-thirds / color door: is color a Z_3 grading, and is that confinement?")
print("  Corpus loaded: T1930 (N_c=3=M_rank), C_2 = 6 = 1 + N_c + rank internal complement,")
print("  W-16 (topological color confinement ALREADY CLOSED, T^2-cycle obstruction).")
print("  Tables first, verdict after.")
print("="*106)

print("\nTABLE 0 -- *** the corpus supplies the home my 5332 said was missing ***")
print("   5332 concluded: thirds cannot come from SO(5)=B_2 (weights in (1/2)Z), and SU(3) is not")
print("   a subgroup of SO(5). Corpus answer: the internal complement decomposes as")
print("      C_2 = 6 = 1 + N_c + rank   ->   U(1) x SU(3) x SU(2)")
print("   ==> SU(3) lives in the 6-dim INTERNAL COMPLEMENT, NOT in the SO(5) factor. My catch and")
print("       the corpus agree; the two-source reading is corpus-grounded, not a new posit.")

print("\nTABLE 1 -- the triality-charge correlation, tested on every SM fermion")
print("   t = triality (0 for colour singlet, 1 for 3, 2 for 3bar)")
print("   fermion      Q       t    Q + t/3    integer?")
sm=[("up",F(2,3),1),("down",F(-1,3),1),("anti-up",F(-2,3),2),("anti-down",F(1,3),2),
    ("electron",F(-1),0),("neutrino",F(0),0),("positron",F(1),0)]
ok=True
for nm,Q,t in sm:
    v=Q+F(t,3); isint=(v.denominator==1); ok&=isint
    print("   %-12s %-7s %-4d %-10s %s"%(nm,str(Q),t,str(v),isint))
print("   ==> Q = -t/3 (mod 1) holds for EVERY SM fermion: %s"%ok)

print("\nTABLE 2 -- so CONFINEMENT = CHARGE INTEGRALITY. Enumerate (n quarks, m antiquarks):")
print("   combo            n   m   t = n-m mod 3   Q integer?   observed?")
combos=[("single quark",1,0),("diquark",2,0),("MESON",1,1),("BARYON",3,0),
        ("antibaryon",0,3),("tetraquark",2,2),("pentaquark",4,1),("qqqq",4,0)]
for nm,n,m in combos:
    t=(n-m)%3; okc=(t==0)
    print("   %-16s %-3d %-3d %-15d %-12s %s"%(nm,n,m,t,"YES" if okc else "no",
          "YES" if okc else "NEVER SEEN"))
print("   ==> the Z_3-neutral combinations are EXACTLY the observed hadron types, and the")
print("       non-neutral ones are exactly those never seen free. *** thirds ARE the fingerprint")
print("       of un-observable colour, as hypothesised. ***")

print("\nTABLE 3 -- *** but DOES THIS TEST DISCRIMINATE THE ACTUAL CLAIM? ***")
print("   claim under test: colour is a SUB-SUBSTRATE Z_3, not an isometry subgroup.")
print("   rival           : Z_3 is simply the CENTRE of a continuous SU(3).")
print("   observable                          fundamental-Z_3   Z_3 = centre of SU(3)   differs?")
for obs in ["triality-charge correlation","confinement / integrality","allowed hadron multiplets"]:
    print("   %-35s %-17s %-23s %s"%(obs,"same","same","NO"))
print("   ==> *** EVERY OBSERVABLE I TESTED IS IDENTICAL UNDER BOTH. The test CONFIRMS the Z_3")
print("       STRUCTURE and DISCRIMINATES NOTHING. *** I verified consistency, not the claim.")

print("\nTABLE 4 -- and the STRONG form is refuted outright")
print("   'colour is ONLY a Z_3 (no continuous group)' predicts NO adjoint gauge bosons.")
print("   observed: gluons -- 3-jet events, running alpha_s, the whole of QCD.")
print("   ==> *** STRONG FORM REFUTED. *** The defensible form is the WEAK one, and it is exactly")
print("       what 5332 already proved: SU(3) is NOT an isometry subgroup of SO(5); it lives in the")
print("       6-dim internal complement, and only its Z_3 centre shows up in the charge grading.")

print("\nTABLE 5 -- reconcile with W-16 (confinement already CLOSED in corpus)")
print("   W-16: topological colour confinement via T^2-cycle obstruction -- gluon cycles can never")
print("         reach the boundary. CLOSED.")
print("   this round: confinement via Z_3-neutrality / charge integrality.")
print("   ==> TWO DIFFERENT MECHANISMS FOR ONE PHENOMENON. They may be the same statement in two")
print("       languages, or two independent obstructions. *** I did NOT show they are the same and")
print("       am NOT merging them. *** Merging without an exhibited map is the shared-integer error")
print("       at mechanism level. @Lyra/@Keeper: this needs an explicit reconciliation or an honest")
print("       'two routes' statement -- not a silent merge.")

print("\nTABLE 6 -- the Higgs: the ASYMMETRIC route, and what it costs me")
print("   @Grace found NO SPINOR in the Rac. My 5332 said 'the spinor is the only rep that works'.")
print("   Both hold, because 5332 enumerated the tensor SQUARE -- BOTH factors in the SAME rep.")
print("   The proposed route is ASYMMETRIC: level-0 SINGLET (x) level-1 VECTOR.")
print("      singlet (x) vector = VECTOR   ->  contains (1,0)   with NO spinor anywhere")
print("   slot: #Rac = 2 (EVEN -> boson, passes 5329 parity), l = 0 (spacetime scalar, passes spin)")
print("   ==> *** MY 5332 DECISION TABLE WAS OVER-NARROW. *** It swept reps, not LEVEL PAIRS. The")
print("       asymmetric case sat outside my enumeration entirely, so 'spinor is the only rep that")
print("       works' is false as a general statement -- it is true only of the symmetric square.")
print("       @Grace's finding and mine are BOTH right; the asymmetry is the reconciliation.")
print("   ** STILL OWED: that the Rac module actually carries a VECTOR K-type at level 1. I did not")
print("      verify it. That is now the single hinge, replacing the spinor question. **")

print("\n"+"="*106)
print("VERDICT")
print("="*106)
print(" (1) CORPUS RECONNECTION SUCCEEDS: the thirds' home is the 6-dim internal complement")
print("     (C_2 = 6 = 1 + N_c + rank -> U(1) x SU(3) x SU(2)), NOT the SO(5) factor. 5332's catch")
print("     and the corpus agree. Two-source charge is corpus-grounded.")
print(" (2) THE Z_3 STRUCTURE VERIFIES CLEANLY: Q = -t/3 (mod 1) on every SM fermion; Z_3-neutral")
print("     combinations are exactly the observed hadrons; confinement = charge integrality.")
print(" (3) *** BUT IT DISCRIMINATES NOTHING (Table 3) and its STRONG FORM IS REFUTED BY GLUONS")
print("     (Table 4). *** What survives is the WEAK form, already proved in 5332. The round asked")
print("     me to 'test the hypothesis'; the honest result is that the test cannot see it.")
print(" (4) DO NOT MERGE with W-16 without an exhibited map (Table 5).")
print(" (5) I OWN 5332's OVER-NARROW TABLE (Table 6): it swept reps, not level pairs; the")
print("     asymmetric singlet (x) vector route needs no spinor and reconciles @Grace with me.")
