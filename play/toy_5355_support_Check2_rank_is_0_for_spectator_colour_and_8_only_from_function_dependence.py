import numpy as np
from math import gamma, pi
np.set_printoptions(precision=3,suppress=True)
print("="*104)
print("TOY 5355 -- CHECK 2 (blind): rank[D, M_3] -- does D wobble in 8 gluon directions or 3?")
print("  Adjective stripped per the new discipline: the object is 'the commutant of D's colour-sector")
print("  action inside M_3(C)'. No 'our', no 'forced'. Tables first.")
print("="*104)

print("\nTABLE 0 -- the computation, stated exactly")
print("   rank[D, M_3] = dim M_3(C) - dim ker(ad_D)   where ker(ad_D) = COMMUTANT of D in M_3(C).")
print("   So the integer is fixed entirely by D's colour-sector action. Enumerate the candidates.")

# basis of u(3) (9 real dims) and su(3) (8)
def u3_basis():
    B=[]
    for i in range(3):
        M=np.zeros((3,3),complex); M[i,i]=1j; B.append(M)
    for i in range(3):
        for j in range(i+1,3):
            M=np.zeros((3,3),complex); M[i,j]=1; M[j,i]=-1; B.append(M)
            M=np.zeros((3,3),complex); M[i,j]=1j; M[j,i]=1j; B.append(M)
    return B
U3=u3_basis()
def rank_ad(Dc,B):
    rows=[(Dc@m-m@Dc).flatten() for m in B]
    R=np.array(rows)
    return np.linalg.matrix_rank(np.vstack([R.real,R.imag]).T.T if False else
                                 np.hstack([R.real,R.imag]))

print("\nTABLE 1 -- rank of ad_D on u(3), for each candidate colour-sector action of D")
cands=[]
cands.append(("D colour-BLIND  (spectator, D ~ 1 on colour)", np.eye(3,dtype=complex)))
Sreal=np.array([[2,0,0],[0,-1,0],[0,0,-1]],dtype=complex)          # real symmetric, non-degenerate-ish
cands.append(("D ~ real SYMMETRIC (generic, degenerate)", Sreal))
Sgen=np.diag([3.,1.,-4.]).astype(complex)                          # real symmetric, fully non-degenerate
cands.append(("D ~ real SYMMETRIC (fully non-degenerate)", Sgen))
A=np.array([[0,1,0],[-1,0,0],[0,0,0]],dtype=complex)               # real ANTIsymmetric = so(3) element
cands.append(("D ~ real ANTIsymmetric (so(3) element)", A))
H=np.array([[1,1j,0],[-1j,2,0],[0,0,-3]],dtype=complex)            # complex hermitian
cands.append(("D ~ complex HERMITIAN (uses J)", H))
print("   D colour-sector action                          rank[D,u(3)]   commutant dim   verdict")
for nm,Dc in cands:
    r=rank_ad(Dc,U3); k=9-r
    v = "*** 0 -> colour invisible ***" if r==0 else ("crosses (>=8)" if r>=8 else "*** <8 -> FLOOR STANDS ***")
    print("   %-46s %-14d %-15d %s"%(nm,r,k,v))

print("\nTABLE 2 -- *** the structural question this reduces to ***")
print("   The rank is NOT a property of 'D' in the abstract -- it is a property of D's COLOUR-SECTOR")
print("   ACTION, and Table 1 shows it ranges over 0, 4, 6 depending on that action.")
print("   ==> *** THE INTEGER IS NOT DETERMINED UNTIL D's COLOUR ACTION IS PINNED. ***")
print("   And the standard Dirac structure is  D = gamma^mu (x) (d_mu + A_mu)  on S (x) V:")
print("     gamma acts on S alone; colour acts on V alone; *** colour is a SPECTATOR tensor factor ***")
print("     -> for CONSTANT m in M_3,  [D, m] = gamma^mu (x) [A_mu, m], which vanishes when A = 0.")
print("   ==> *** FOR THE UNFLUCTUATED D WITH CONSTANT COLOUR MATRICES, THE RANK IS 0 -- row 1. ***")

print("\nTABLE 3 -- so where could 8 come from? (be fair to the crossing case)")
print("   In Connes' setup the algebra is FUNCTION-valued, C^inf(M) (x) M_3, not constant M_3.")
print("   Then [D, m] = gamma^mu (x) d_mu m =/= 0 for every non-constant m -> all 8 directions appear.")
print("   *** BUT that 8 is supplied by the FUNCTION dependence (the d_mu m term), not by D's")
print("       colour structure. *** The gluons then come from C^inf(M), i.e. from putting a")
print("       spacetime-dependent colour field in by hand -- which is the import Check 1 was")
print("       designed to rule out at the algebra level, reappearing one level down.")

print("\nTABLE 4 -- consistency with the day's other two results (Bar 1: ONE line, not three)")
print("   route                          finding")
print("   isometry (toy 5350)            gluon spin-2 generators absent from the isometry algebra")
print("   heat trace (toy 5352)          gluon LOOP absent from the fermionic Dirac heat trace")
print("   this (toy 5355)                colour is a spectator factor -> [D, const M_3] = 0")
print("   ==> *** SAME BOUNDARY, THIRD ROUTE. Per @Cal's Bar 1 these are ONE LINE, not three")
print("       confirmations. I am counting them as one. ***")

print("\nTABLE 5 -- the mass map: what (24/pi^2)^6 is actually made of (partial, honest)")
print("   Gamma(5) = %d  -> and 5 = n_C, so 24 = Gamma(n_C) = (n_C - 1)!"%gamma(5))
print("   exponent 6 = C_2 ;  pi^2 = the S^4-volume factor (vol(S^4) = 8pi^2/3)")
print("   check: (24/pi^2)^6 = %.4f   vs observed 206.7683  -> %.4f%%"%(
      (24/pi**2)**6, 100*abs((24/pi**2)**6-206.7683)/206.7683))
print("   ==> the INGREDIENTS are corpus objects (Gamma(n_C), C_2, S^4 volume). *** What is missing")
print("       is still the MAP: why a K-type address produces Gamma(n_C)/pi^2 raised to C_2. I can")
print("       identify the pieces; I cannot yet derive the assembly, and identifying pieces of a")
print("       known number is not deriving it. ***")

print("\n"+"="*104)
print("VERDICT -- Check 2")
print("="*104)
print(" (1) *** THE 8-OR-3 QUESTION HAS NO ANSWER UNTIL D's COLOUR ACTION IS PINNED. *** rank[D,u(3)]")
print("     computes to 0, 4, or 6 across the natural candidates (Table 1) -- it never reaches 8 for")
print("     any single colour-sector operator, because ad_D always has a commutant of dimension >= 3.")
print()
print(" (2) *** AND FOR THE STANDARD STRUCTURE THE ANSWER IS 0, NOT 3 AND NOT 8. *** In")
print("     D = gamma^mu (x) (d_mu + A_mu), colour is a SPECTATOR tensor factor: [D, m] = gamma (x)")
print("     [A_mu, m], which vanishes at A = 0 for constant m. The unfluctuated D does not wobble in")
print("     ANY colour direction.")
print()
print(" (3) *** THE 8 IS AVAILABLE ONLY FROM THE FUNCTION-VALUED ALGEBRA *** (C^inf (x) M_3), where")
print("     [D,m] = gamma (x) d_mu m. But then the 8 comes from the SPACETIME DEPENDENCE, not from")
print("     D's colour structure -- the gluon field is being supplied by hand one level below the")
print("     algebra. *** That is the same import Check 1 ruled out, migrating down a level -- exactly")
print("     the pattern the standing rule warns about. @Keeper: I think Check 2 as posed cannot")
print("     cross; it can only relocate the assumption. ***")
print()
print(" (4) BAR 1 APPLIED TO MYSELF: this is the THIRD route to the same boundary today (isometry,")
print("     heat trace, spectator factor). *** ONE LINE, not three confirmations. ***")
print()
print(" (5) MASS MAP: I can name the ingredients of (24/pi^2)^6 -- Gamma(n_C) = 24, exponent C_2 = 6,")
print("     pi^2 from the S^4 volume -- and the form reproduces 206.77 to 0.02%%. *** But naming the")
print("     pieces of a known number is not deriving it. The assembly rule is still missing and I am")
print("     not going to reverse-engineer one. ***")
