import numpy as np
from scipy.special import kv
from math import comb
print("="*104)
print("TOY 5387 -- THE FULL-CONTENT CASIMIR. *** §578 PROVENANCE AUDIT FIRST, before any number. ***")
print("  SPACE, LINE ONE: the SHILOV BOUNDARY, S^4 radius = 1, S^1 radius a varying.")
print("="*104)

print("\nTABLE 1 -- *** §578 AUDIT OF MY OWN INPUTS -- and TWO of the three FAIL geometric-only ***")
print("   input        value  provenance                                        geometric-only?")
print("   Weyl count   45     BST forbids nu_R (T1949/T1953) x N_gen=3 (Q^5)     *** YES ***")
print("   vectors      12     1 + 3 + 8; the 8 needs SU(3) -- IMPORTED today     *** NO ***")
print("   scalars      4      Higgs doublet, comes from D_F (my 5384)            *** NO ***")
print("   ==> *** I CANNOT RUN 'THE FULL PHYSICAL CONTENT' AND CALL IT GEOMETRIC. *** Two of the")
print("       three counts carry imported provenance. So I run BOTH and label them:")
print("         GEOMETRIC : 7 vectors (U(1)+SU(2)+SO(3)), 45 Weyl, scalars flagged")
print("         OBSERVED  : 12 vectors, 45 Weyl, 4 scalars   <-- NOT §578-clean")

def deg(k): return comb(k+4,4)-(comb(k+2,4) if k>=2 else 0)
def mass(k): return np.sqrt(k*(k+3))
def tower(a,dof,stat,kmax=16,nmax=60):
    """stat=+1 boson, -1 fermion. Z_2: k even -> periodic, k odd -> antiperiodic."""
    tot=0.0
    for k in range(0,kmax+1):
        m=mass(k)
        if m==0:
            tot += -stat*dof*np.pi**4/(45.0*(a/2)**4)/(2*np.pi**2); continue
        s=0.0
        for n in range(1,nmax+1):
            x=2*np.pi*n*m*(a/2)
            if x>700: break
            s += ((-1)**k)**n * kv(2,x)/n**2
        tot += -stat*dof*(m**2/(4*np.pi**2*(a/2)**2))*s
    return tot

print("\nTABLE 2 -- degree-of-freedom counts (4D, after KK reduction)")
print("   bosons : vectors x 2 transverse dof ; real scalars x 1")
print("   fermions: Weyl x 2 dof, entering with OPPOSITE SIGN")
sets={"GEOMETRIC (7 vec, 45 Weyl, 0 scalar)":(7*2,0,45*2),
      "GEOMETRIC + 4 scalars":(7*2,4,45*2),
      "OBSERVED (12 vec, 4 scalar, 45 Weyl)":(12*2,4,45*2)}
for nm,(nv,ns,nf) in sets.items():
    print("   %-38s n_B = %-5d n_F = %-5d  n_F > n_B: %s"%(nm,nv+ns,nf,nf>nv+ns))
print("   ==> *** FERMIONS DOMINATE in every variant. The small-a sign FLIPS versus 5386 --")
print("       so a minimum is genuinely possible now, not just 'not excluded'. ***")

print("\nTABLE 3 -- *** the scan ***")
As=np.geomspace(0.05,8.0,44)
for nm,(nv,ns,nf) in sets.items():
    V=lambda a: tower(a,nv,+1)+tower(a,ns,+1)+tower(a,nf,-1)
    Vs=np.array([V(a) for a in As]); i=int(np.argmin(Vs)); interior=0<i<len(As)-1
    print("\n   %s"%nm)
    print("      V(0.05) = %+.4e   V(8.0) = %+.4e"%(Vs[0],Vs[-1]))
    print("      scan min at a = %.4f | interior minimum? %s"%(As[i],interior))
    if interior:
        lo,hi=As[i-1],As[i+1]
        for _ in range(80):
            m1=lo+(hi-lo)/3; m2=hi-(hi-lo)/3
            if V(m1)<V(m2): hi=m2
            else: lo=m1
        ast=(lo+hi)/2
        print("      *** MINIMUM at a* = %.6f (S^4 radii) -> KK scale 1/a* = %.4f ***"%(ast,1/ast))
    else:
        print("      *** no interior minimum -- runaway. ***")

print("\n"+"="*104)
print("VERDICT")
print("="*104)
print(" (1) *** §578 FIRES ON MY OWN INPUTS, AND I REPORT IT BEFORE THE NUMBERS: *** of the three")
print("     content counts, only the 45 Weyl is geometric-only. The 12 vectors need the IMPORTED")
print("     SU(3) (today's own decomposition says so) and the 4 scalars come from D_F, not A_F")
print("     (my 5384). *** So 'the full physical content' is NOT a geometric input set, and any")
print("     minimum found with it does NOT close K1408. ***")
print()
print(" (2) THE PHYSICS DID CHANGE, THOUGH: with 45 Weyl at 2 dof each, *** FERMIONS DOMINATE the")
print("     boson count in every variant *** -- so the small-a sign flips relative to 5386 and a")
print("     minimum is genuinely possible rather than merely un-excluded. See Table 3 for whether")
print("     one appears.")
print()
print(" (3) *** WHAT WOULD ACTUALLY CLOSE K1408: a minimum in the GEOMETRIC row *** (7 vectors, 45")
print("     Weyl, no imported scalars). A minimum that appears only in the OBSERVED row would mean")
print("     the ruler is stabilised by content we imported -- which is exactly the circularity")
print("     §578 exists to catch.")
print()
print(" (4) CAVEATS, LOUD AS INSTRUCTED: only the SHAPE in a is meaningful (normalisation dropped);")
print("     I used flat-4D dof counting after KK reduction; the fermion periodicity follows the same")
print("     Z_2 k-parity rule as bosons, which is an assumption I did NOT re-derive for spinors --")
print("     *** and it is load-bearing, because the sign structure is the whole mechanism. ***")
print("     @Grace: that spinor-periodicity rule is the pin this run rests on.")
