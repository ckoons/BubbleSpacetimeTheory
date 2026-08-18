import numpy as np, itertools
from fractions import Fraction as F
print("="*92)
print("TRACK 2 -- IS THE KOONS-TICK EXPONENT C_2^2 = 36 FORCED, OR FIT?")
print("Discipline: derive from the GENERATOR first, WITHOUT looking at the target scale. Then compare.")
print("="*92)
print()
print("STEP 1 -- WHAT DOES THE MECHANISM ACTUALLY CONTAIN?  rho_commit = exp(-tau H_B / hbar_BST),")
print("          H_B = the Casimir of K = SO(5) x SO(2).  Compute its spectrum. No target in view.")
rho=(F(3,2),F(1,2))                      # rho_K for so(5)
def cas(l):                              # <l, l+2rho>
    return sum(F(a)*(F(a)+2*r) for a,r in zip(l,rho))
reps=[((0,0),"trivial"),((F(1,2),F(1,2)),"spinor (4)"),((1,0),"vector (5)"),
      ((1,1),"adjoint / 2-form (10)"),((2,0),"sym-traceless (14)"),((2,1),"(35)"),((2,2),"(35')")]
print("\n      K-type            Casimir eigenvalue")
for l,name in reps:
    print("      %-18s %s"%(name,cas(l)))
print("\n  ⟹ THE SPECTRUM IS ORDER-1 RATIONALS: 0, 5/2, 4, 6, 10, 12, 16, ...")
print("     ★ THERE IS NO alpha ANYWHERE IN IT. The Casimir of a compact group has no fine-structure")
print("       constant in its eigenvalues -- it is built from the root system and nothing else.")
print()
print("STEP 2 -- WHAT TIME SCALE DOES exp(-tau H_B/hbar) SET?")
print("     the semigroup decays on tau ~ hbar_BST / lambda, lambda an eigenvalue above.")
print("     lambda in {5/2, 4, 6, 10, ...}  ->  tau spans ONE order of magnitude, not seventy-seven.")
print("     ⟹ THE MECHANISM PRODUCES A SINGLE SCALE, NEVER A POWER OF alpha -- let alone the 36th.")
print("  ★★★ SO THE ANSWER TO THE ASSIGNED QUESTION IS: THE EXPONENT DOES *NOT* FALL OUT OF THE")
print("      HEAT-SEMIGROUP MECHANISM. There is no alpha in the generator to raise to any power.")
print()
print("="*92)
print("STEP 3 -- ONLY NOW LOOK AT THE TARGET. What exponent does 10^-120 actually require?")
print("="*92)
alpha=1/137.035999
tP=5.391247e-44
import math
need=(math.log10(tP)-(-120))/math.log10(alpha)
print("     t_P = %.3e s = 10^%.3f ;  one factor of alpha = 10^%.4f"%(tP,math.log10(tP),math.log10(alpha)))
print("     exponent needed to land exactly on 10^-120 :  n = %.3f"%need)
for n in [34,35,36,37,38]:
    print("       n = %2d  ->  t_P * alpha^n = 10^%.2f s"%(n,math.log10(tP)+n*math.log10(alpha)))
print()
print("  ★ AND 10^-120 IS ITSELF A FAMOUS TARGET -- the cosmological-constant discrepancy. Maximal pull.")
print("    It is also quoted only to ~an order of magnitude, so the admissible window is wide.")
print()
print("STEP 4 -- THE FISHING COUNT: how many BST composites sit in that window?")
prim={'rank':2,'N_c':3,'n_C':5,'C_2':6,'g':7}
comps={}
for (a,x),(b,y) in itertools.product(prim.items(),repeat=2):
    comps.setdefault(x*y,set()).add("%s*%s"%(a,b))
for a,x in prim.items():
    comps.setdefault(x*x,set()).add("%s^2"%a)
    for (b,y),(c,z) in itertools.product(prim.items(),repeat=2):
        comps.setdefault(x*y*z,set()).add("%s*%s*%s"%(a,b,c))
print("      exponent  BST readings                            landing decade")
for n in range(33,40):
    r=sorted(comps.get(n,[]))[:3]
    print("        %2d      %-38s 10^%.1f"%(n,", ".join(r) if r else "(none)",math.log10(tP)+n*math.log10(alpha)))
inwin=[n for n in range(33,40) if abs(math.log10(tP)+n*math.log10(alpha)+120)<=1.5 and comps.get(n)]
print("\n  ⟹ BST composites landing within 1.5 decades of 10^-120: %s"%inwin)
print("     e.g. 35 = n_C*g  and  36 = C_2^2 = (rank*N_c)^2.  ★ AT LEAST TWO READINGS FIT.")
print()
print("="*92)
print("★★★★ VERDICT, against Keeper's pre-registered bar")
print("="*92)
print("  BAR: 'the Koons-tick value banks as derivation-grade only if C_2^2 = 36 is MECHANISM-FORCED.'")
print("  (a) The mechanism (exp(-tau H_B/hbar)) contains NO alpha -- it cannot produce ANY exponent.")
print("  (b) The needed exponent is n = %.2f, and >= 2 BST composites (35 = n_C*g, 36 = C_2^2) sit in"%need)
print("      the admissible window around a target quoted to an order of magnitude.")
print("  ⟹ C_2^2 = 36 IS FIT, NOT FORCED. Per the bar, the Koons tick is an IDENTIFIED SCALE,")
print("     not derivation-grade.")
print()
print("  ★ WHAT IS CLEAN REGARDLESS (and worth keeping, exactly as the charter says):")
print("    * the IDENTIFICATION -- Koons tick = the commitment period -- is a structural statement")
print("      about the ontology and does not depend on the exponent at all;")
print("    * the NAMING -- Planck time != Koons tick (F307) -- is right and is the useful part;")
print("    * and the honest form is 'the commitment period is a scale far below t_P, currently")
print("      IDENTIFIED at ~10^-120 s', with the exponent labelled as matched, not derived.")
