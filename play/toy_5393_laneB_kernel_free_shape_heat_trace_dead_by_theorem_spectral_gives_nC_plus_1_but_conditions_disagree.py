import numpy as np
from fractions import Fraction as F
print("="*104)
print("TOY 5393 -- LANE B RE-AIMED: is there a KERNEL-FREE forced shape on Silov = (S^4 x S^1)/Z_2?")
print("  SPACE: Silov boundary of D_IV^5, product metric, S^4 radius R4, S^1 radius R1.")
print("  SHAPE = t := R4^2/R1^2.  Route 1 (14/5) DEAD (K1213). Bergman/Szego FORBIDDEN.")
print("="*104)

print("\nPART A -- the heat-trace candidate: *** test the ROUTE before running the search ***")
print("  Heat-kernel coefficients integrate LOCAL curvature invariants (my 5382 criterion).")
print("  On the PRODUCT S^4 x S^1 the circle is FLAT with no mixed components:  Riem = Riem(S^4) (+) 0.")
print("  ==> every dimension-2k invariant is a PURE S^4 invariant ~ R4^(-2k); R1 enters ONLY as volume:")
print("        a_k ~ R4^(-2k) * [Vol(S^4) R4^4] * [2 pi R1]  =  c_k R4^(4-2k) R1")
print("  ==> in ANY ratio a_j/a_k the factor R1 CANCELS IDENTICALLY.")
print("     corpus a0 = 225, a1 = -1875 -> a1/a0 = -25/3 = %.5f, dimension 1/length^2."%(-1875/225))
print("  *** THE HEAT-TRACE ROUTE IS DEAD BY THEOREM. a1/a0 is a SCALE, not a shape; no a_k depends")
print("      on t at all, so no ratio of them can EVER fix t. Closed by mechanism, no search run. ***")

print("\nPART B -- the spectral route (NONLOCAL, so it CAN see t). General S^d x S^1, d = n_C - 1.")
print("  S^d: lambda_k = k(k+d-1).  S^1: m^2.  Z_2 = (antipodal, half-period) -> (-1)^(k+m) -> k+m EVEN.")
print("  FIXED VOLUME (Vol ~ R^d R1 = 1) -> R1 = R^-d, and  t = R^2/R1^2 = R^(2d+2).")
print("     lambda_1(R) = min over allowed (k,m) != (0,0) of [ k(k+d-1)/R^2 + m^2 R^(2d) ]")
print("  MAX-MIN: lambda_1 is a min of falling (m=0) and rising (m>0) branches -> unique interior max.")

def run(d,z2,KM=9):
    modes=[(k,m) for k in range(KM) for m in range(KM) if (k,m)!=(0,0) and ((k+m)%2==0 or not z2)]
    f=lambda R: min(k*(k+d-1)/R**2 + m*m*R**(2*d) for k,m in modes)
    Rs=np.linspace(0.6,1.6,200001); v=np.array([f(R) for R in Rs]); i=int(np.argmax(v))
    Rb=Rs[i]; t=Rb**(2*d+2)
    act=[(k,m) for k,m in modes if abs(k*(k+d-1)/Rb**2+m*m*Rb**(2*d)-v[i])<3e-4]
    return t,sorted(act)

print("\n  TABLE B1 -- *** which two modes actually bind at the max-min? (n_C = 5, d = 4) ***")
t,act=run(4,True)
print("     numeric t* = %.5f    binding modes: %s"%(t,act))
print("     ==> the binding pair is (2,0) x (1,1), NOT the two PURE modes.")
print("     exact:  10/R^2 = 4/R^2 + R^(2d)  ->  6/R^2 = R^8  ->  R^10 = 6  ->  *** t = 6 ***")
print("     (I first mislabeled this crossing as (0,2)x(1,1) -> 4/3. The numeric max caught it: the")
print("      (0,2) mode sits at 16.77 there, far above. *** The exact answer is 6, not 4/3. ***)")

print("\n  TABLE B2 -- *** SWEEP THE FAMILY before naming the 6 (standing rule). ***")
print("     n_C   d    t* (numeric)   t* exact   d+2   C_2 = 2n_C-4   n_C+1")
for nC in range(4,9):
    d=nC-1; tn,_=run(d,True)
    print("     %-5d %-4d %-13.5f %-10d %-5d %-14d %d"%(nC,d,tn,d+2,d+2,2*nC-4,nC+1))
print("     *** t* = d + 2 = n_C + 1 EXACTLY, for every n_C. ***")
print("     *** AND AT n_C = 5 THAT COLLIDES WITH C_2 = 2n_C - 4 = 6 -- and NOWHERE ELSE. ***")
print("     This is the SAME false identity 'C_2 = n+1' that my 5361 retired (it killed Condition 5).")
print("     *** The honest label is t = n_C + 1. Calling it C_2 would re-import a retired error. ***")

print("\n  TABLE B3 -- does the Z_2 (the one structure BST forces) change the answer? YES.")
for z2 in [True,False]:
    tn,act=run(4,z2)
    print("     Z_2 %-9s t* = %.5f  (exact %d)  binding %s"%("ENFORCED" if z2 else "OFF",tn,6 if z2 else 4,act))
print("     with Z_2: t = d+2 = 6 ; without: t = d = 4. *** The Z_2 does real work -- it shifts the")
print("     shape by exactly 2, because it projects out (1,0) and promotes (2,0). ***")

print("\n  TABLE B4 -- *** do other natural conditions AGREE? (enumerate before 'therefore') ***")
print("     condition                                             t        on target list?")
L=[5/3,5/2,4,3]
for nm,tv in [("MAX-MIN gap at fixed volume  [variational]",6.0),
              ("degenerate the two PURE modes (2,0)x(0,2)",2.5),
              ("degenerate (0,2)x(1,1)  [at fixed R4]",4/3),
              ("no Z_2: max-min at fixed volume",4.0),
              ("equal first-mode contributions 4/R4^2 = 1/R1^2",4.0)]:
    print("     %-53s %-8.4f %s"%(nm,tv,"YES" if any(abs(tv-q)<1e-9 for q in L) else "no"))
print("     *** FIVE conditions, FOUR distinct values, and the two that DO hit the list hit")
print("         DIFFERENT members (5/2 and 4). The conditions do not agree. ***")

print("\n"+"="*104)
print("VERDICT")
print("="*104)
print(" (A) *** HEAT-TRACE ROUTE: DEAD BY THEOREM, not by search. *** On a product with a flat factor")
print("     every local invariant is R1-blind; a_k ~ R4^(4-2k) R1, so R1 cancels in every ratio.")
print("     a1/a0 = -25/3 is a SCALE (1/length^2). *** No heat-kernel ratio can ever carry a shape. ***")
print()
print(" (B) *** SPECTRAL ROUTE: it CAN see t, and the variational condition gives a CLEAN EXACT")
print("     answer -- t = R4^2/R1^2 = n_C + 1 = 6 *** (max-min spectral gap at fixed volume, binding")
print("     pair (2,0) x (1,1), verified numerically to 5 digits and exactly at every n_C in 4..8).")
print()
print(" (C) *** BUT 6 IS NOT ON THE TARGET LIST {5/3, 5/2, 4, 3}, AND THE CONDITIONS DISAGREE. ***")
print("     Five natural spectral conditions give four distinct values. So the round's OTHER honest")
print("     outcome is the one that holds: *** NO FORCED BOUNDARY SHAPE. *** The shape is not fixed")
print("     by kernel-free geometry -- it is handed to @Casey's physics-matching, as the round allowed.")
print()
print(" (D) *** THE Z_2 IS NOT A SPECTATOR: it shifts t from d to d+2. *** That is a real BST-forced")
print("     structure changing a geometric answer -- worth keeping even though the shape stays open.")
print()
print(" (E) ★ TWO TRAPS I WALKED INTO AND OUT OF, BOTH CAUGHT BY MY OWN STANDING RULES:")
print("     1. I mislabeled the binding crossing and got 4/3. *** The numeric max-min disagreed with")
print("        my algebra, and the numerics were right. *** Post the table before the verdict.")
print("     2. t = 6 at n_C = 5 equals C_2 = 6. *** The family sweep says t = n_C + 1, NOT 2n_C - 4 --")
print("        the exact false identity my 5361 retired. *** A shared integer is not a shared object.")
print()
print(" (F) NOT BANKED AS A FORCING: t = 6 is an extremum of a functional I CHOSE (fixed volume).")
print("     A different functional moves it. *** Reported as a conditional extremum, not a shape. ***")
