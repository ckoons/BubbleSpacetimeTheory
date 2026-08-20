from fractions import Fraction as F
print("="*104)
print("TOY 5390 -- LANE E: does beta-decay PRESERVE the 27 = N_c^3 colour record? Theorem or picture?")
print("="*104)
N_c=3
print("\nTABLE 1 -- the object, from the corpus")
print("   27 = N_c^3 = 3 (x) 3 (x) 3, the committed colour CODEBOOK")
print("   decomposition: 10 + 8 + 8 + 1 = %d   (the singlet = the observable baryon)"%(10+8+8+1))

print("\nTABLE 2 -- *** the decisive question: does the U<->D swap ACT on colour at all? ***")
print("   particle   flavour   colour rep   beta-decay changes...")
for nm,fl in [("neutron (udd)","udd"),("proton (uud)","uud")]:
    print("   %-10s %-9s 3 (x) 3 (x) 3   --"%(nm,fl))
print("   n -> p + e- + nubar :  ONE d -> u.  That is a FLAVOUR operation.")
print("   is flavour SU(2)_L-ish acting on the colour index?  *** NO -- they are different indices. ***")
print("   ==> *** the 27 is preserved because the operation DOES NOT TOUCH IT. ***")

print("\nTABLE 3 -- so test whether the claim can FAIL (the can't-fail check)")
print("   process                       changes flavour?  changes colour rep?  27 preserved?")
for p,fl,co,pres in [("beta decay n -> p","yes","no","YES"),
                ("any weak decay","yes","no","YES"),
                ("pion emission","yes","no","YES"),
                ("electron capture","yes","no","YES"),
                ("ANY flavour-changing process","yes","no","YES")]:
    print("   %-29s %-17s %-20s %s"%(p,fl,co,pres))
print("   ==> *** THE CLAIM CANNOT FAIL. Every flavour-changing process preserves the 27, because")
print("       27 is a COLOUR object and flavour operations act on a DIFFERENT INDEX. ***")

print("\nTABLE 4 -- what a real theorem here would have to say")
print("   candidate content                                          does the 27-claim supply it?")
print("   'colour is conserved in weak decays'                        yes -- but that is standard QCD")
print("   'the baryon stays a colour SINGLET'                         yes -- also standard")
print("   'something SPECIFIC to 27 rather than to colour generally'  *** NO ***")
print("   ==> the statement is true, standard, and carries no BST-specific content.")

print("\n"+"="*104)
print("VERDICT -- LANE E")
print("="*104)
print(" (1) *** PICTURE, NOT THEOREM -- and worse, it is a CAN'T-FAIL claim. *** The 27 is a COLOUR")
print("     codebook; beta-decay is a FLAVOUR operation. They act on different indices, so the 27 is")
print("     preserved *** because the operation never touches it ***, not because anything is conserved.")
print()
print(" (2) *** IT CANNOT FAIL FOR ANY FLAVOUR-CHANGING PROCESS *** (Table 3) -- beta decay, pion")
print("     emission, electron capture, all of them. A test that cannot fail proves nothing when it")
print("     passes. That is the construction-guaranteed shape we have retired repeatedly.")
print()
print(" (3) WHAT IS TRUE IN IT IS STANDARD: colour is conserved in weak decays and the baryon stays a")
print("     singlet. *** Both are textbook QCD, and neither is BST-specific. ***")
print()
print(" (4) @Casey -- the INTUITION may still be pointing somewhere real (the record surviving a")
print("     transformation is a good instinct, and it is the same instinct that made the")
print("     superselection-charge fix work). But *** the 27 is the wrong invariant to hang it on ***,")
print("     because flavour cannot move it. A record-preservation claim needs an operation that")
print("     COULD have broken the invariant and doesn't.")
print()
print(" (5) SUGGESTION, not a result: the interesting version would be an operation that DOES act on")
print("     colour -- gluon exchange, or hadronisation -- and asking what survives THERE. That one")
print("     can fail, so it can carry content.")
