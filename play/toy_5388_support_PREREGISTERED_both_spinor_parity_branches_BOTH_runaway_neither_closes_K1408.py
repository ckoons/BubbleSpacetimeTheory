import numpy as np
from scipy.special import kv
from math import comb
print("="*104)
print("TOY 5388 -- PRE-REGISTERING BOTH BRANCHES of the spinor-periodicity fork, BEFORE @Grace's pin.")
print("  SPACE, LINE ONE: the SHILOV BOUNDARY, S^4 radius = 1, S^1 radius a varying.")
print("  *** I am BLOCKED on Grace. So I commit both answers now -- neither can be fitted after. ***")
print("="*104)

print("\nTABLE 1 -- the fork, and why branch B is well-motivated (not a hedge)")
print("   BRANCH A: fermion towers carry the SAME Z_2 k-parity as bosons  (what 5387 assumed)")
print("   BRANCH B: fermion towers carry the OPPOSITE parity (an extra spinor-lift sign)")
print("   *** motivation for B, from my own 5325: on this boundary the spinor tower's Z_2 generator")
print("       SQUARES TO -1 -- it carries a Z_4, not a Z_2. So spinors genuinely need not inherit the")
print("       scalar parity rule. B is a real candidate, not a hedge. ***")

def deg(k): return comb(k+4,4)-(comb(k+2,4) if k>=2 else 0)
def mass(k): return np.sqrt(k*(k+3))
def tower(a,dof,stat,flip=False,kmax=16,nmax=60):
    tot=0.0
    for k in range(0,kmax+1):
        m=mass(k); par = (k+1) if flip else k          # flip -> opposite periodicity
        if m==0:
            sgn = -1 if (par%2) else +1
            tot += -stat*dof*sgn*np.pi**4/(45.0*(a/2)**4)/(2*np.pi**2); continue
        s=0.0
        for n in range(1,nmax+1):
            x=2*np.pi*n*m*(a/2)
            if x>700: break
            s += ((-1)**par)**n * kv(2,x)/n**2
        tot += -stat*dof*(m**2/(4*np.pi**2*(a/2)**2))*s
    return tot

print("\nTABLE 2 -- *** BOTH BRANCHES, COMPUTED AND COMMITTED NOW ***")
As=np.geomspace(0.05,8.0,44)
results={}
for bname,flip in [("A: fermions SAME parity (5387)",False),("B: fermions OPPOSITE parity",True)]:
    for cname,(nv,ns,nf) in {"GEOMETRIC (7 vec, 45 Weyl)":(7*2,0,45*2),
                             "OBSERVED (12 vec, 4 sc, 45 Weyl)":(12*2,4,45*2)}.items():
        V=lambda a: tower(a,nv,+1)+tower(a,ns,+1)+tower(a,nf,-1,flip=flip)
        Vs=np.array([V(a) for a in As]); i=int(np.argmin(Vs)); interior=0<i<len(As)-1
        star=""
        if interior:
            lo,hi=As[i-1],As[i+1]
            for _ in range(80):
                m1=lo+(hi-lo)/3; m2=hi-(hi-lo)/3
                if V(m1)<V(m2): hi=m2
                else: lo=m1
            star=" -> a* = %.5f, 1/a* = %.4f"%((lo+hi)/2,1/((lo+hi)/2))
        verdict = "*** MINIMUM ***"+star if interior else "runaway (%s)"%("a->inf" if Vs[0]>Vs[-1] else "a->0")
        results[(bname,cname)]=verdict
        print("   %-32s %-34s %s"%(bname,cname,verdict))

print("\nTABLE 3 -- *** THE PRE-REGISTERED FORK, committed before the pin lands ***")
print("   if @Grace's pin says...        then Track B's answer is...")
for b in ["A: fermions SAME parity (5387)","B: fermions OPPOSITE parity"]:
    g=results[(b,"GEOMETRIC (7 vec, 45 Weyl)")]
    print("   %-30s GEOMETRIC row: %s"%(b.split(':')[0],g))
print("   *** the GEOMETRIC row is the only one that can close K1408 (§578: the observed row's")
print("       12 vectors and 4 scalars are imported). ***")

print("\n"+"="*104)
print("VERDICT")
print("="*104)
print(" (1) *** BOTH BRANCHES ARE NOW ON THE RECORD BEFORE THE PIN. *** Whatever @Grace returns, the")
print("     Track-B answer is already determined by Table 2 and cannot be adjusted afterwards.")
print("     That is the whole point of posting while blocked rather than waiting.")
print()
print(" (2) BRANCH B IS MOTIVATED, NOT A HEDGE: my own 5325 found that on this boundary the spinor")
print("     tower's Z_2 generator *** squares to -1 *** -- a Z_4, not a Z_2. So spinors have no")
print("     obligation to inherit the scalar k-parity rule, and the fork is real physics.")
print()
print(" (3) *** THE DECIDING ROW IS 'GEOMETRIC'. *** Only 7 vectors + 45 Weyl is §578-clean; the")
print("     observed row imports SU(3)'s 8 gluons and D_F's scalars, so a minimum there would not")
print("     close K1408 even if it appeared.")
print()
print(" (4) HONEST EITHER WAY, as instructed: if the pin gives a minimum in the geometric row, the")
print("     ruler has a candidate derivation and K1408 moves. If it gives runaway, *** the ruler")
print("     stays the one input and we say so *** -- and the bracketing result from 5387 (the two")
print("     runaways come from opposite sides) remains the useful structural finding.")
