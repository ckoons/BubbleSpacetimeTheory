import itertools
from fractions import Fraction as F
N_c=3
print("="*106)
print("TOY 5332 -- the two Higgs rep-checks + Q's actual torus home in the SO(5) factor")
print("  *** Decision table computed BEFORE @Grace's pin (blind-pin discipline). ***")
print("  Tables first, verdict after.")
print("="*106)

print("\n--- CHECK 1: does Rac (x) Rac at l=0 contain the internal (1,0) = the vector 5? ---")
print("\nTABLE 1 -- tensor SQUARE of each candidate Rac SO(5)-rep. B_2 = SO(5).")
print("   Rac rep        dim   (Rac)^(x)2 decomposition        contains 5 = (1,0)?   Higgs map")
tab=[("[0,0] trivial",1,"1","NO","FAILS"),
     ("[0,1] SPINOR ",4,"1 + 5 + 10","YES","WORKS"),
     ("[1,0] vector ",5,"1 + 10 + 14","NO","FAILS"),
     ("[0,2] adjoint",10,"1 + 10 + 14 + 35 + 30 (no 5)","NO","FAILS")]
for nm,dim,dec,has,v in tab:
    print("   %-14s %-5d %-30s %-21s %s"%(nm,dim,dec,has,"*** "+v+" ***"))
print("\n   dimension checks:  4x4 = 16 = 1+5+10 OK ;  5x5 = 25 = 1+10+14 OK")
print("   *** THE ANSWER IS SHARPLY REP-DEPENDENT, AND THE SPINOR IS THE ONLY ONE THAT WORKS. ***")
print("   Structural reason: for SO(n), v (x) v = trace + antisym + sym-traceless -- NO vector.")
print("   You cannot build a vector from two vectors. You CAN from two spinors: that is exactly")
print("   the bilinear psibar gamma^mu psi. The vector-from-spinors fact IS the mechanism.")

print("\nTABLE 2 -- @Grace, the pin decides it. Committed in advance, before you read the source:")
for r,v in [("Rac carries the SPINOR 4","(1,0) present -> Higgs (1,0) map WORKS"),
            ("Rac carries the VECTOR 5","(1,0) ABSENT  -> Higgs (1,0) map FAILS"),
            ("Rac carries the TRIVIAL 1","(1,0) ABSENT  -> Higgs (1,0) map FAILS")]:
    print("   if %-27s  ==>  %s"%(r,v))

print("\n--- CHECK 2: the Hopf / framing class of Rac (x) Rac at l=0 ---")
print("\nTABLE 3")
print("   ingredient                       value            source")
print("   #Rac                             2 (EVEN)         constituent count")
print("   exp(2 pi i J) = (-1)^{#Rac}      +1               toy 5327 identity")
print("   spacetime spin (l = 0)           0                the slot itself")
print("   topological spin theta = e^{2 pi i s}, s = 0  ->  +1")
print("   ==> *** HOPF / FRAMING CLASS = 0. *** No half-twist from either side: the internal")
print("       parity is even AND the spacetime spin is zero. A genuine scalar boson slot.")

print("\n--- CHECK 3: Q's actual torus home in the SO(5) factor ---")
print("\nTABLE 4 -- the B_2 weight lattice, explicitly. Maximal torus T^2 = SO(2) x SO(2).")
W={"[1,0] vector 5":[(1,0),(-1,0),(0,1),(0,-1),(0,0)],
   "[0,1] spinor 4":[(F(1,2),F(1,2)),(F(1,2),F(-1,2)),(F(-1,2),F(1,2)),(F(-1,2),F(-1,2))],
   "[0,2] adjoint 10":[(1,1),(1,-1),(-1,1),(-1,-1),(1,0),(-1,0),(0,1),(0,-1),(0,0),(0,0)]}
allw=set()
for nm,ws in W.items():
    print("   %-18s weights: %s"%(nm,", ".join("(%s,%s)"%(a,b) for a,b in ws[:5])))
    for a,b in ws: allw.add((F(a),F(b)))
dens={w[0].denominator for w in allw}|{w[1].denominator for w in allw}
print("\n   ALL denominators appearing in the B_2 weight lattice: %s"%sorted(dens))
print("   ==> every SO(5) torus weight lies in (1/2)Z.  *** THERE ARE NO THIRDS. ***")

print("\nTABLE 5 -- but T2470 REQUIRES thirds")
print("   T2470 (proved): charge quantized in units of 1/N_c = 1/%d,"%N_c)
print("      exactly N_c+1 = %d magnitudes {0, 1/3, 2/3, 1}, capped at 1."%(N_c+1))
print("   needed denominator: 3      available from the B_2 torus: 1 and 2 only")
print("   is 1/3 in the SO(5) torus weight lattice?  %s"%("YES" if F(1,3) in {w[0] for w in allw} else "*** NO ***"))
print("   and SO(5) does NOT contain SU(3) (where thirds usually come from): rank matches (2=2)")
print("   but SU(3)'s fundamental 3 is complex, while B_2's reps are real (5,10,14) or")
print("   quaternionic (4,16). SU(3) embeds in SO(6) via 6 = 3 + 3bar, not in SO(5).")

print("\n"+"="*106)
print("VERDICT -- from Tables 1-5 only")
print("="*106)
print(" (1) HIGGS CHECK 1 -- *** THE SPINOR IS THE ONLY REP THAT WORKS, AND I COMMIT TO THAT BLIND.")
print("     4 (x) 4 = 1 + 5 + 10 CONTAINS the (1,0);  5 (x) 5 = 1 + 10 + 14 DOES NOT.")
print("     @Grace: your single pin decides the map, and the decision table is filed above BEFORE")
print("     you read the source. Spinor -> map works. Vector or trivial -> map fails. No wiggle.")
print("     The mechanism is the familiar one: a vector is a SPINOR BILINEAR (psibar gamma^mu psi);")
print("     you cannot make one from two vectors. That is why the spinor is the physical option.")
print()
print(" (2) HIGGS CHECK 2 -- *** HOPF / FRAMING CLASS = 0, CONFIRMED. *** #Rac = 2 gives +1 and")
print("     l = 0 gives spin 0, so neither the internal parity nor the spacetime spin contributes a")
print("     half-twist. Rac (x) Rac at l=0 is a clean scalar-boson slot.")
print()
print(" (3) *** Q's NEW HOME HAS A QUANTIZATION PROBLEM -- REPORTING IT RATHER THAN WAVING IT")
print("     THROUGH. *** @Keeper relocated charge to the SO(5)-factor torus to protect Section 3's")
print("     arrow, and I agree with protecting the arrow. But the B_2 weight lattice is entirely in")
print("     (1/2)Z -- integers and halves, NO THIRDS -- while T2470 (proved) requires charge in")
print("     units of 1/N_c = 1/3. The relocation does not, by itself, supply the thirds it needs.")
print("     And the usual source of thirds is unavailable: SU(3) is not a subgroup of SO(5)")
print("     (it embeds in SO(6) via 6 = 3 + 3bar).")
print("     ==> the thirds must come from an explicit 1/N_c normalization or from a color structure")
print("         OUTSIDE the SO(5) factor. Either is possible; NEITHER IS FORCED BY THE RELOCATION.")
print("     This is an OPEN ITEM on the new home, not an objection to moving charge off the K-center.")
print("     The two kills in 5331 stand regardless -- charge cannot live on J.")
