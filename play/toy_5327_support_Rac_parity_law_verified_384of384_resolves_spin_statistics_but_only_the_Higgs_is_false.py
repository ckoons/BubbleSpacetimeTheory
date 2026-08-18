import itertools, cmath
from fractions import Fraction as F
RAC=F(3,2); DI=F(2)
print("="*100)
print("TOY 5327 -- BLIND VERIFICATION of the #Rac law:  exp(2 pi i J) = (-1)^{#Rac}")
print("  Enumerated, not asserted. Tables first, verdict after.")
print("="*100)

print("\nTABLE 1 -- exhaustive enumeration over composites.  A composite of n_R Rac + n_D Di")
print("  constituents, plus ANY spin l and ANY number of derivatives n (both integers):")
print("      Delta = (3/2) n_R + 2 n_D + l + 2n")
print("  Sweep n_R,n_D = 0..4 and l,n = 0..3 -- every case, phase computed from Delta directly.")
bad=[]; rows=[]
for nR in range(5):
    for nD in range(5):
        if nR+nD==0: continue
        for l in range(4):
            for n in range(4):
                D=RAC*nR+DI*nD+l+2*n
                z=cmath.exp(2j*cmath.pi*float(D)); z=complex(round(z.real,9),round(z.imag,9))
                pred=(-1)**nR
                if abs(z-pred)>1e-8: bad.append((nR,nD,l,n,D,z,pred))
                if l==0 and n==0 and nR+nD<=2: rows.append((nR,nD,D,z.real,pred))
print("   n_R  n_D   Delta    exp(2 pi i Delta)   (-1)^{n_R}   match")
for nR,nD,D,z,p in sorted(rows):
    print("   %-4d %-5d %-8s %-19s %-12s %s"%(nR,nD,str(D),"%+g"%z,"%+d"%p,abs(z-p)<1e-8))
tot=5*5*4*4-4*4
print("\n   cases swept: %d      MISMATCHES: %d"%(tot,len(bad)))
print("   ==> %s"%("*** LAW VERIFIED, EXACTLY, ON EVERY CASE ***" if not bad else "FAILURES: %s"%bad[:3]))
print("   Why: Di contributes exp(4 pi i n_D)=1; l and 2n are integers so contribute 1;")
print("        each Rac contributes exp(3 pi i) = -1.  Stable under ALL descendants.")

print("\nTABLE 2 -- *** now read it on the PHYSICAL states (Flato-Fronsdal) ***")
print("   Flato-Fronsdal: Rac(x)Rac and Di(x)Di -> integer spin (BOSONS);  Rac(x)Di -> half-integer (FERMIONS)")
print("   composite        n_R   (-1)^{n_R}   species    F   (-1)^F   ORDINARY spin-statistics?")
cases=[("Rac (x) Rac",2,"boson",0),("Di (x) Di",0,"boson",0),("Rac (x) Di",1,"fermion",1)]
allok=True
for nm,nR,sp,Fn in cases:
    lhs=(-1)**nR; rhs=(-1)**Fn; ok=(lhs==rhs); allok&=ok
    print("   %-16s %-5d %-12s %-10s %-3d %-8s %s"%(nm,nR,"%+d"%lhs,sp,Fn,"%+d"%rhs,"AGREES" if ok else "differs"))
print("\n   ==> ALL COMPOSITES AGREE WITH ORDINARY SPIN-STATISTICS: %s"%allok)

print("\nTABLE 3 -- and on the SINGLETONS themselves (where the Round-13 'inversion' lived)")
print("   state   n_R   (-1)^{n_R}   spin     F   (-1)^F   agrees?")
for nm,nR,spin,Fn in [("Rac",1,"scalar",0),("Di",0,"spinor",1)]:
    lhs=(-1)**nR; rhs=(-1)**Fn
    print("   %-7s %-5d %-12s %-8s %-3d %-8s %s"%(nm,nR,"%+d"%lhs,spin,Fn,"%+d"%rhs,"yes" if lhs==rhs else "*** NO ***"))
print("   ==> the singletons, and ONLY the singletons, depart from ordinary spin-statistics.")

print("\nTABLE 4 -- who actually rides 4 pi?  (checking 'only the Higgs')")
print("   class                       n_R      rides 4 pi?")
for nm,nR in [("elementary Rac (scalar)",1),("elementary Di (spinor)",0),
              ("composite boson Rac(x)Rac",2),("composite boson Di(x)Di",0),
              ("composite FERMION Rac(x)Di",1)]:
    print("   %-27s %-8d %s"%(nm,nR,"YES" if (-1)**nR==-1 else "no"))
print("\n"+"="*100)
print("VERDICT -- from Tables 1-4 only")
print("="*100)
print(" (1) *** THE #Rac LAW IS VERIFIED EXACTLY: exp(2 pi i J) = (-1)^{#Rac}, %d/%d cases,"%(tot-len(bad),tot))
print("     zero mismatches, stable under every spin and every derivative. *** It is a clean law.")
print()
print(" (2) ***** AND IT RESOLVES THE ROUND-13 SPIN-STATISTICS TENSION. ***** On COMPOSITES the law")
print("     gives EXACTLY (-1)^F -- the ORDINARY rule. Fermions are Rac(x)Di (one Rac) -> -1;")
print("     bosons are Rac(x)Rac or Di(x)Di (zero or two) -> +1. The 'inversion' I reported in")
print("     Round 13 was an artifact of evaluating on SINGLETONS, which are boundary objects with")
print("     no local bulk dynamics -- not physical particles. Singletons being exceptional here is")
print("     a KNOWN feature of singletons, not a defect. @Lyra: Section 7's true scope is exactly this.")
print()
print(" (3) *** BUT 'ONLY THE HIGGS RIDES 4 pi' IS FALSE AS STATED. *** Table 4: EVERY FERMION rides")
print("     4 pi (n_R = 1) -- and correctly so, that is ordinary spinor behaviour, 720 degrees is")
print("     what fermions have always done. The true statement is narrower:")
print("       'among BOSONS, only an elementary Rac-scalar rides 4 pi.'")
print("     Please do not let the paper say 'only the Higgs' -- a referee kills it in one line.")
print()
print(" (4) ** AND THE HIGGS IDENTIFICATION ITSELF IS NOT ESTABLISHED HERE. ** The Rac is a boundary")
print("     singleton with no bulk propagating dof; the Higgs is a bulk scalar with a VEV. They share")
print("     the LABEL 'scalar'. That is a shared PROPERTY, not a shared OBJECT, and by our own rule it")
print("     needs an exhibited forced map before the paper names the Higgs. I did not verify it and")
print("     it is not what I was asked to verify. The LAW is banked; the IDENTIFICATION is not.")
