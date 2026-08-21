from fractions import Fraction as F
import numpy as np
rng=np.random.default_rng(31)
print("="*104)
print("TOY 5417 -- THE 6/5 PROVENANCE CHECK (@Lyra). *** IT DID NOT COME FROM THE −6 FORM. It came")
print("  from extrapolating a RANK-1 formula to a RANK-2 domain — and 5/4 dies with it. ***")
print("="*104)

print("\nTABLE 1 -- *** THE CHAIN, QUOTED FROM THE LANE-A NOTE ***")
print('  "the unit disk (complex dim n = 1) has Bergman exponent 2 = n+1, Szegő exponent 1 = n,')
print('   ratio 2/1 = (n+1)/n. The BST reading n = n_C = 5 gives 6/5 by the same rule."')
print("  *** THE DISC HAS RANK 1. D_IV^5 HAS RANK 2. *** 'genus = n+1' is the RANK-1 (ball) formula;")
print("  for the rank-2 type-IV family the genus is n (my 5415: bidisk + three isomorphisms).")
print("  ==> the disc 'control' does not control a rank-2 domain — it is a DIFFERENT FAMILY.")

print("\nTABLE 2 -- *** THE RIGHT CONTROL: rank-2 domains where the answer is classical ***")
print("  Szegő singularity exponent, from domains whose Šilov kernel is standard:")
print("   domain          rank  genus   Szegő exponent (classical)      genus/2   n-1")
rows=[("disk = I_{1,1}",1,2,"1  [S = 1/(2pi(1-u wbar))]",F(2,2),0),
      ("bidisk = D_IV^2",2,2,"1  [product of two disks]",F(2,2),1),
      ("I_{2,2} = D_IV^4",2,4,"2  [det(1-ZW*)^{-q}, q=2]",F(4,2),3),
      ("D_IV^5",2,5,"? (the question)",F(5,2),4)]
for a,b,c,d,e,f in rows:
    print("   %-16s %-5d %-7d %-31s %-9s %d"%(a,b,c,d,e,f))
print("   *** genus/2 MATCHES every classical case: 1, 1, 2. 'n−1' gives 0, 1, 3 — WRONG at I_{2,2}. ***")
print("   ==> *** Szegő exponent = genus/2 = n/2 = 5/2 for D_IV^5. NOT n_C − 1 = 4. ***")

print("\nTABLE 3 -- verify the bidisk Szegő factorization numerically (the rank-2 anchor)")
worst=0
for t in range(5):
    z=(rng.normal(size=2)+1j*rng.normal(size=2))*0.25
    zz=complex(np.dot(z,z)); n2=float(np.vdot(z,z).real)
    N=1-2*n2+abs(zz)**2
    u=z[0]+1j*z[1]; v=z[0]-1j*z[1]
    P=(1-abs(u)**2)*(1-abs(v)**2)
    worst=max(worst,abs(N-P))
print("   N(z,z) = (1-|u|^2)(1-|v|^2) to %.1e  ->  bidisk Szegő = (1/4pi^2) N^{-1}: exponent 1."%worst)
print("   Bergman exponent 2, Szegő exponent 1  ->  *** RATIO = 2, on a genuine RANK-2 domain. ***")

print("\nTABLE 4 -- ★★★ *** BOTH RATIOS DIE, AND THEY DIE AS ONE FAMILY ***")
print("   claimed reading                          value   built on                       verdict")
print("   weight ratio (n_C+1)/n_C                 6/5     disc rank-1 genus = n+1        *** DEAD ***")
print("   singularity ratio n_C/(n_C−1)            5/4     Szegő exponent = n−1 (wrong)   *** DEAD ***")
print("   corrected singularity ratio nu_B/nu_S    2       genus / (genus/2)              *** LIVES ***")
print()
print("   *** AND THE ROUND-30 FALSE-NEIGHBOR RULE FIRES EXACTLY AS WRITTEN: ***")
print("     (n+1)/n at n=5 = 6/5 ;  n/(n−1) at n=5 = 5/4 ;  (n+1)/n at n=4 = 5/4.")
print("   *** 6/5 and 5/4 are ONE family at shifted arguments — one relation wearing two labels,")
print("       not two independent maps. The bar predicted this shape before we found it. ***")

print("\nTABLE 5 -- what the provenance check was asked to test, answered")
print("   Q: 'if the chain touched the −6 form, 6/5 dies as an artifact.'")
print("   A: *** THE CHAIN DID NOT TOUCH THE −6 FORM. *** 6/5 came from the disc extrapolation, an")
print("      independent error. *** But 6/5 dies anyway — of a different cause. ***")
print("   ⟹ two distinct errors were live at once: (i) the corpus's N^-6 transcription [5415], and")
print("     (ii) a rank-1→rank-2 extrapolation [here]. *** Fixing one would NOT have caught the other. ***")

print("\n"+"="*104); print("VERDICT -- 6/5 provenance"); print("="*104)
print(" (1) ★★★★ *** 6/5 IS DEAD, BUT NOT AS A −6 ARTIFACT. *** The chain never touched N^-6. It came")
print("     from the disc control: 'genus = n+1' is the RANK-1 formula, and D_IV^5 is RANK 2, where")
print("     genus = n. *** A control from the wrong family is not a control. ***")
print()
print(" (2) *** 5/4 DIES TOO, AND HARDER — it rests on 'Szegő exponent = n_C − 1 = 4', which fails on")
print("     a domain where the answer is classical: I_{2,2} = D_IV^4 has Szegő exponent 2, not 3. ***")
print("     genus/2 matches all three classical cases (1, 1, 2). *** So nu_S = n/2 = 5/2. ***")
print()
print(" (3) *** THE SURVIVING NUMBER IS 2 — and Round 30 already tiered it correctly as")
print("     Derived-but-CLASS-LEVEL, not a BST number. *** nu_B/nu_S = genus/(genus/2) = 2 for EVERY")
print("     bounded symmetric domain. It is a property of the Bergman–Hardy relation, not of n_C = 5.")
print()
print(" (4) ★★ *** THE FALSE-NEIGHBOR RULE FIRED AS DESIGNED: 6/5 and 5/4 are (n+1)/n and n/(n−1) —")
print("     ONE family at shifted arguments, and (n+1)/n at n=4 IS 5/4. *** Two labels, one relation.")
print("     The bar predicted this shape one round before the sweep produced it.")
print()
print(" (5) ★ AND THE UNCOMFORTABLE PART: TWO INDEPENDENT ERRORS WERE LIVE SIMULTANEOUSLY — the")
print("     corpus's N^-6 (5415) and this rank-1 extrapolation. *** Fixing either alone would have")
print("     left the other standing, and both produced plausible n_C=5 numbers. ***")
