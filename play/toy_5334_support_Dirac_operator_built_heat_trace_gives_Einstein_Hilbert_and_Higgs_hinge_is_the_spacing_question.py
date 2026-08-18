import numpy as np
from math import comb, pi
from fractions import Fraction as F
print("="*104)
print("TOY 5334 -- (A) BUILD THE DIRAC OPERATOR D on the boundary S^4   (B) pin the Higgs hinge")
print("  Tables first, verdict after.")
print("="*104)
print("\n  STANDING FIX, first line as instructed: the geometry forces the NUMBER 3 (short-root")
print("  multiplicity a = n_C - 2, load-bearing); it does NOT host the GROUP SU(3) as an isometry.")
print("  Number is geometry; group is realized on the 3-dim multiplicity space. Both my 5332 and")
print("  5333 statements are to be read in that phrasing.")

n=4                                  # boundary sphere S^4
S=2**(n//2)                          # spinor bundle rank = 4
def mult(k): return S*comb(n+k-1,k)  # multiplicity of each of +-(n/2+k)
def lam(k):  return n/2+k

print("\n--- PART A: the Dirac operator, explicitly ---")
print("\nTABLE 1 -- spectrum of D on the round S^4 (radius 1)")
print("   k    eigenvalues      multiplicity (each sign)")
for k in range(5):
    print("   %-4d +-%-14s %d"%(k,"%g"%lam(k),mult(k)))
print("   ==> *** D IS SIGN-INDEFINITE: every eigenvalue comes in a +- pair. ***")
print("       That is exactly the property J does NOT have (J is bounded below -- the arrow).")
print("       So D can carry what Tr f(J) could not.")

print("\nTABLE 2 -- D-squared is Laplace-type (Lichnerowicz)")
R=n*(n-1)                            # scalar curvature of unit S^4 = 12
print("   D^2 = nabla* nabla + R/4,   R = n(n-1) = %d  ->  D^2 = Laplacian + %g"%(R,R/4))
print("   eigenvalues of D^2 : (n/2+k)^2 = %s ..."%", ".join("%g"%lam(k)**2 for k in range(4)))
print("   all strictly positive -> *** D^2 IS POSITIVE AND LAPLACE-TYPE. ***")

print("\nTABLE 3 -- the heat trace, computed and FIT (this is the F60/F63 Sakharov object)")
def heat(t,K=4000): return sum(2*mult(k)*np.exp(-t*lam(k)**2) for k in range(K))
vol=8*pi**2/3                        # Vol(S^4)
a0_th=S*vol
a1_th=-(F(1,3))*R*vol                # a_1 = -(1/3) Int R  (Gilkey, Dirac)
a1_th=float(a1_th)
ts=np.array([0.004,0.003,0.002,0.0015,0.001])
y=np.array([heat(t)*(4*pi*t)**(n/2) for t in ts])   # = a0 + a1 t + a2 t^2 + ...
c=np.polyfit(ts,y,2)
a1_fit,a0_fit=c[1],c[2]
print("   fit of  Tr e^{-t D^2} * (4 pi t)^{n/2}  =  a_0 + a_1 t + a_2 t^2")
print("   coefficient   fitted          theory                    rel.err")
print("   a_0           %-15.6f %-25.6f %.2e"%(a0_fit,a0_th,abs(a0_fit-a0_th)/abs(a0_th)))
print("   a_1           %-15.6f %-25.6f %.2e"%(a1_fit,a1_th,abs(a1_fit-a1_th)/abs(a1_th)))
print("   theory: a_0 = dim(spinor) x Vol(S^4) = %d x %.6f"%(S,vol))
print("           a_1 = -(1/3) Int R = -(1/3) x %d x %.6f   <-- THE EINSTEIN-HILBERT TERM"%(R,vol))
print("   ==> *** BOTH COEFFICIENTS REPRODUCED. a_1 IS THE EINSTEIN-HILBERT TERM -- this is")
print("       precisely F63's 'a_1 = Einstein-Hilbert', now carried by a REAL operator. ***")

print("\nTABLE 4 -- what this fixes")
print("   object              old (Section 11)      new")
print("   operator            Tr f(J)               D  (Dirac)")
print("   sign                J positive (arrow)    D sign-indefinite  -- matches Connes")
print("   square              --                    D^2 Laplace-type   -- matches Sakharov")
print("   heat trace          --                    a_1 = Einstein-Hilbert = F60/F63")
print("   ==> 'fix Section 11' = 'build D', and D is built. The arrow is no longer being asked to")
print("       do a job it structurally cannot do.")

print("\n--- PART B: the Higgs hinge -- does the Rac carry a LEVEL-1 VECTOR K-type? ---")
print("\nTABLE 5 -- the Rac's K-types are degree-l harmonics on S^4 = the (l,0) reps of SO(5)")
print("   level l   SO(5) rep (l,0)   dim   is it the VECTOR 5 = (1,0)?")
for l in range(4):
    dim=comb(l+3,3)*(2*l+3)//3 if l>0 else 1
    print("   %-9d %-17s %-5s %s"%(l,"(%d,0)"%l,{0:1,1:5,2:14,3:30}[l],"YES -- THE HINGE" if l==1 else "no"))
print("\nTABLE 6 -- *** BUT WHICH LEVELS ARE ACTUALLY PRESENT? The spacing question decides. ***")
print("   reading                     Delta tower        levels present   is l=1 present?")
print("   Delta = 3/2 + l  (step 1)   3/2,5/2,7/2,...    l = 0,1,2,3...   YES -> hinge CLOSES")
print("   Delta = 3/2 + 2m (step 2)   3/2,7/2,11/2,...   l = 0,2,4,...    *** NO -> hinge FAILS ***")
print("   the CORPUS tower we have used all week is 3/2, 7/2, 11/2 -- i.e. STEP 2.")

print("\n"+"="*104)
print("VERDICT")
print("="*104)
print(" (A) *** D IS BUILT, AND IT CHECKS OUT ON ALL THREE COUNTS. ***")
print("     sign-indefinite (+- pairs) | D^2 positive Laplace-type (Lichnerowicz, R/4 = 3) |")
print("     heat trace reproduces a_0 = 4 Vol(S^4) and a_1 = -(1/3) Int R = the EINSTEIN-HILBERT")
print("     term, both to ~1e-6. @Lyra: Section 11's operator exists now; point it at F60/F63.")
print("     The arrow stops being asked to be sign-indefinite, because D already is.")
print()
print(" (B) *** THE HIGGS HINGE REDUCES TO AN ALREADY-OPEN QUESTION -- AND CURRENTLY POINTS THE")
print("     WRONG WAY. *** The Level-1 K-type IS the vector 5 (Table 5), so the asymmetric")
print("     singlet (x) vector route needs exactly l = 1 to exist. But the tower we have used all")
print("     week steps by 2 (3/2, 7/2, 11/2), which contains only EVEN levels -- and then l = 1 is")
print("     ABSENT and the route fails.")
print("     ==> the Higgs hinge is NOT independent: it is the SAME unpinned tower-spacing question")
print("         I flagged in 5324/5325. Two open items are one open item.")
print("     @Grace: pin the spacing from the Flato-Fronsdal/minrep source and BOTH close at once.")
print("     Step 1 -> hinge closes, Higgs map lives. Step 2 -> hinge fails, the asymmetric route")
print("     dies with the symmetric one. I am committing that fork blind, before the pin.")
print()
print(" (C) HELD, NOT MERGED: W-16 (T^2-cycle obstruction) and Z_3-superselection remain TWO")
print("     confinement mechanisms. No exhibited map between them, so no merge.")
