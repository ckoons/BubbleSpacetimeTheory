import numpy as np
from math import pi, factorial
from fractions import Fraction as F
print("="*104)
print("TOY 5362 -- (A) bank C_2 = 2a.  (B) is there ANY critical point of the commitment flow's")
print("            action that selects n = 5?  Look for a vanishing slope; report wherever it lands.")
print("="*104)

print("\n--- (A) BANK: C_2 = 2a ---")
print("\nTABLE 1 -- the relation, verified across the family")
print("   n     a = n-2   C_2 = 2n-4   C_2 = 2a ?   Wallach a/2   N_c = a")
for n in range(3,10):
    a=n-2; c=2*n-4
    print("   %-5d %-9d %-12d %-12s %-13s %s"%(n,a,c,c==2*a,F(a,2),a))
print("   ==> *** C_2 = 2a, for every n. *** One 'a' now carries: the FK short-root multiplicity,")
print("       the Wallach point a/2 (5324), N_c = a (5344), and the Casimir C_2 = 2a. Four readings,")
print("       ONE object -- and per Bar 1 that is ONE line, not four.")

print("\n--- (B) THE CRITICAL-POINT HUNT ---")
print("\nTABLE 2 -- first, pin the volume formula from the corpus value, then use it as a function")
def Vol(n): return pi**n/(2**(n-1)*factorial(n))
print("   Vol(D_IV^n) = pi^n / (2^{n-1} n!)")
print("   check at n=5:  pi^5/(2^4 . 5!) = pi^5/%d   -- corpus says pi^5/1920: %s"%(2**4*factorial(5),2**4*factorial(5)==1920))

print("\nTABLE 3 -- candidate actions, and where each one's slope vanishes")
def spinor(n): return 2**n            # real dim 2n -> Dirac spinor 2^n
def R(n): return -n                   # non-compact symmetric space, Killing normalisation (5336)
cands=[
 ("Vol(n)",                 lambda n: Vol(n)),
 ("K(0,0) = 1/Vol",         lambda n: 1/Vol(n)),
 ("a_0 density = 2^n",      lambda n: spinor(n)),
 ("a_1 density = n 2^n/12", lambda n: n*spinor(n)/12.0),
 ("a_1/a_0 = n/12",         lambda n: n/12.0),
 ("C_2/n = 2 - 4/n",        lambda n: (2*n-4)/n),
 ("TOTAL a_1 = a_1dens x Vol", lambda n: (n*spinor(n)/12.0)*Vol(n)),
]
print("   action                          n=3      n=4      n=5      n=6      n=7      extremum at")
for nm,f in cands:
    vals={n:f(n) for n in range(2,12)}
    interior=[n for n in range(3,11) if (vals[n]-vals[n-1])*(vals[n+1]-vals[n])<0]
    ext = str(interior[0]) if interior else ("monotone" )
    print("   %-31s %-8.4g %-8.4g %-8.4g %-8.4g %-8.4g %s"%(nm,f(3),f(4),f(5),f(6),f(7),ext))

print("\nTABLE 4 -- *** the ONE candidate with a genuine competition, worked exactly ***")
print("   TOTAL a_1 = (n 2^n/12) x (pi^n/(2^{n-1} n!)) = n pi^n / (6 n!)")
print("   ratio f(n+1)/f(n) = pi/n  ->  increasing while n < pi, decreasing after")
for n in range(1,8):
    r=pi/n
    print("      f(%d+1)/f(%d) = pi/%d = %.4f   %s"%(n,n,n,r,"increasing" if r>1 else "DECREASING"))
print("   ==> *** the Einstein-Hilbert total is MAXIMISED AT n = 4, NOT n = 5. ***")

print("\n"+"="*104)
print("VERDICT")
print("="*104)
print(" (A) *** C_2 = 2a BANKED *** -- verified for all n (Table 1). And it CONSOLIDATES rather than")
print("     adds: the FK multiplicity a is now the single object behind the Wallach point (a/2),")
print("     the colour count (N_c = a), and the Casimir (C_2 = 2a). *** Four readings, ONE line. ***")
print()
print(" (B) *** I FOUND NO CRITICAL POINT AT n = 5. *** I checked seven natural actions (Table 3):")
print("     six are MONOTONE in n -- volume, Bergman kernel, a_0, a_1 density, a_1/a_0, C_2/n --")
print("     so their slopes never vanish anywhere, let alone at 5.")
print()
print(" (C) *** THE ONE ACTION WITH A REAL COMPETITION PEAKS AT n = 4. *** The total Einstein-Hilbert")
print("     term is n pi^n/(6 n!), whose step ratio is exactly pi/n -- increasing while n < pi,")
print("     decreasing after. *** Maximum at n = 4. *** That is a genuine stationary point of a")
print("     genuine action, and it does NOT select 5. I am reporting it because it is the honest")
print("     result of the search I was asked to run, and because a 4 is interesting on its own")
print("     terms -- but I am NOT dressing it up: nothing here says n = 4 either, since 'maximise")
print("     the EH term' is not a principle anyone has derived.")
print()
print(" (D) SO: the commitment flow's action does not supply a variational route to n_C = 5. Combined")
print("     with 5361 (Condition 5 is an identity), *** neither the uniqueness set nor the action")
print("     forces the dimension. *** That leaves @Lyra's correctability question (is N_c = 3 forced")
print("     by distance-3?) as the live route, exactly as @Keeper scoped it -- and it is a COUNTING")
print("     question, which is the right kind.")
print()
print(" (E) GUARD OBSERVED: I did not resurrect Condition 5, and I did not go looking for a function")
print("     that peaks at 5. I fixed the candidate actions first and reported where they landed.")
