import numpy as np
from scipy.special import kv
from math import comb
print("="*104)
print("TOY 5386 -- THE KK CASIMIR ENERGY E(a) OF (S^4 x S^1_a)/Z_2. Does it have a MINIMUM?")
print("  *** SPACE, LINE ONE: the SHILOV BOUNDARY, S^4 radius FIXED = 1, S^1 radius a VARYING. ***")
print("  *** CAVEAT UP FRONT (@Keeper): runaway vs minimum is the whole question; other")
print("      contributions may be needed. Credential-tier target, NOT a promised derivation. ***")
print("="*104)

print("\nTABLE 0 -- FIRST, the boundary/continuum picture (@Casey's steer)")
print("   modes have omega^2 = k(k+3)/R_S^2 + m^2/a^2, two scales:")
print("     the S^4 tower  k(k+3)  -- FIXED by the sphere, the substrate-discrete side")
print("     the S^1 tower  m^2/a^2 -- set by the ruler a")
print("   ==> *** 1/a IS THE SEPARATOR. *** Probes below 1/a see only m=0: the theory looks")
print("       4-dimensional and CONTINUOUS. Probes above 1/a resolve the tower: the substrate's")
print("       discreteness becomes visible. The KK scale is exactly where continuum ends.")

print("\nTABLE 1 -- *** the Z_2 turns this into a SCHERK-SCHWARZ problem (the key structure) ***")
print("   Z_2 rule (my 5377): k + m EVEN.  So for each k, m is constrained by k's parity:")
print("     k EVEN -> m even = 2j  -> PERIODIC on a circle of radius a/2")
print("     k ODD  -> m odd  = 2j+1 -> ANTIPERIODIC on that circle")
print("   ==> *** periodic and antiperiodic Casimir contributions have OPPOSITE SIGNS. ***")
print("       That is a genuine competition -- so a minimum is POSSIBLE, not excluded a priori.")
print("   (a pure massless single-circle tower would be a bare power law and could NOT have one.)")

def deg(k):                      # S^4 harmonic degeneracy
    return comb(k+4,4)-(comb(k+2,4) if k>=2 else 0)
def mass(k):                     # S^4 radius 1
    return np.sqrt(k*(k+3))

def V(a,kmax=14,nmax=40):
    """Casimir potential, standard massive-KK form, up to a positive overall constant.
       sigma = +1 periodic (k even), -1 antiperiodic (k odd)."""
    tot=0.0
    for k in range(0,kmax+1):
        m=mass(k)
        if m==0:                 # massless k=0 tower: pure power law piece
            tot += -deg(k)*np.pi**4/(45.0*(a/2)**4)/(2*np.pi**2)
            continue
        s=0.0
        for n in range(1,nmax+1):
            x=2*np.pi*n*m*(a/2)
            if x>700: break
            s += ((-1)**k)**n * kv(2,x)/n**2
        tot += -deg(k)*(m**2/(4*np.pi**2*(a/2)**2))*s
    return tot

print("\nTABLE 2 -- scan V(a)")
print("   a          V(a)")
As=np.geomspace(0.05,3.0,28)
Vs=np.array([V(a) for a in As])
for a,v in list(zip(As,Vs))[::3]:
    print("   %-10.4f %+.6e"%(a,v))

i=int(np.argmin(Vs))
interior = 0 < i < len(As)-1
print("\nTABLE 3 -- *** IS THERE AN INTERIOR MINIMUM? ***")
print("   min of the scan at a = %.4f (index %d of %d)"%(As[i],i,len(As)-1))
print("   interior (not at an endpoint)? %s"%interior)
print("   V at small a (%.3f) = %+.4e"%(As[0],Vs[0]))
print("   V at large a (%.3f) = %+.4e"%(As[-1],Vs[-1]))
if interior:
    lo,hi=As[i-1],As[i+1]
    for _ in range(60):
        m1=lo+(hi-lo)/3; m2=hi-(hi-lo)/3
        if V(m1)<V(m2): hi=m2
        else: lo=m1
    astar=(lo+hi)/2
    print("   *** refined minimum at a* = %.6f (in units of the S^4 radius) ***"%astar)
    print("   *** KK scale 1/a* = %.6f in the same units ***"%(1/astar))
else:
    print("   *** NO INTERIOR MINIMUM IN THE SCANNED RANGE -- runaway. ***")

print("\n"+"="*104)
print("VERDICT")
print("="*104)
print(" (1) THE BOUNDARY/CONTINUUM PICTURE (@Casey): *** 1/a is the separator. *** Below it only the")
print("     m = 0 modes are accessible and the theory looks 4D and continuous; above it the KK tower")
print("     resolves and the substrate's discreteness appears. The ruler IS the continuum/discrete line.")
print()
print(" (2) *** THE Z_2 MAKES THIS A SCHERK-SCHWARZ PROBLEM, and that is the structural point: ***")
print("     k+m even forces even-k towers PERIODIC and odd-k towers ANTIPERIODIC on a circle of")
print("     radius a/2. Their Casimir contributions carry OPPOSITE SIGNS. *** So a minimum is not")
print("     excluded a priori -- which a single massless circle tower WOULD have been. ***")
print()
print(" (3) THE COMPUTATION: see Table 3 for whether the scan finds an interior minimum. Reported")
print("     as computed, either way -- this was flagged credential-tier, not a promised derivation.")
print()
print(" (4) HONEST LIMITS, STATED WHATEVER THE ANSWER: (a) I included only the SCALAR tower; the")
print("     physical content (fermions, the gauge field) contributes with its own signs and would")
print("     shift or destroy any minimum. (b) The overall normalisation is dropped -- only the SHAPE")
print("     in a is meaningful here. (c) A minimum in a scalar-only toy is a CANDIDATE mechanism,")
print("     *** not a stabilised ruler. *** The real calculation needs the full content.")
import numpy as np
from scipy.special import kv
from math import comb
def deg(k): return comb(k+4,4)-(comb(k+2,4) if k>=2 else 0)
def mass(k): return np.sqrt(k*(k+3))
def V(a,kmin=0,kmax=16,nmax=60):
    tot=0.0
    for k in range(kmin,kmax+1):
        m=mass(k)
        if m==0:
            tot += -deg(k)*np.pi**4/(45.0*(a/2)**4)/(2*np.pi**2); continue
        s=0.0
        for n in range(1,nmax+1):
            x=2*np.pi*n*m*(a/2)
            if x>700: break
            s += ((-1)**k)**n * kv(2,x)/n**2
        tot += -deg(k)*(m**2/(4*np.pi**2*(a/2)**2))*s
    return tot
print("="*104)
print("TOY 5386b -- THE SAME COMPUTATION WITH THE k=0 TOWER REMOVED (as gauge invariance requires)")
print("="*104)
print("\n  *** WHY: my 5379 showed the A_theta modes with m =/= 0 are PURE GAUGE (eaten). The k=0")
print("      tower IS those modes. So the physical gauge field does NOT have the tower that drove")
print("      the runaway. This is a MOTIVATED removal (from my own prior result), not a fit. ***")
for lab,kmin in [("scalar toy: ALL k (5386)",0),("gauge field: k >= 1 (k=0 eaten)",1)]:
    As=np.geomspace(0.05,6.0,40); Vs=np.array([V(a,kmin=kmin) for a in As])
    i=int(np.argmin(Vs)); interior = 0<i<len(As)-1
    print("\n  %s"%lab)
    print("    V(0.05) = %+.4e   V(6.0) = %+.4e"%(Vs[0],Vs[-1]))
    print("    scan min at a = %.4f  |  interior minimum? %s"%(As[i],interior))
    if interior:
        lo,hi=As[i-1],As[i+1]
        for _ in range(80):
            m1=lo+(hi-lo)/3; m2=hi-(hi-lo)/3
            if V(m1,kmin=kmin)<V(m2,kmin=kmin): hi=m2
            else: lo=m1
        ast=(lo+hi)/2
        print("    *** MINIMUM at a* = %.6f  (S^4 radii)   ->  KK scale 1/a* = %.4f ***"%(ast,1/ast))
        print("    V(a*) = %+.6e"%V(ast,kmin=kmin))
    else:
        print("    *** RUNAWAY -- no interior minimum. ***")
