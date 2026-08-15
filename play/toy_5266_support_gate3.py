import numpy as np
from math import comb
rng=np.random.default_rng(1)
print("="*80)
print("GATE 3 -- does idempotency force ONE projection, not 5->4->3->2->1 ?")
print("="*80)
print("CAL'S HANDLE: P^2 = P, so applying it twice = applying it once.")
print()
print("★ BUT THAT IS NECESSARY, NOT SUFFICIENT -- and I have to say so.")
print("  P^2=P constrains applying the SAME projection twice. The iteration worry is about a")
print("  DIFFERENT projection afterwards: P_2 P_1 with P_2 dropping a second direction.")
print("  Idempotency of P_1 says nothing about P_2. Demonstration, 5x5 rank-4 projectors:")
P1=np.eye(5); P1[4,4]=0
P2=np.eye(5); P2[3,3]=0
print("   ||P1^2-P1|| = %.1e   ||P2^2-P2|| = %.1e   rank(P1)=%d  rank(P2 P1)=%d"%(
    np.abs(P1@P1-P1).max(),np.abs(P2@P2-P2).max(),
    np.linalg.matrix_rank(P1),np.linalg.matrix_rank(P2@P1)))
print("   => both idempotent, and the composite still drops a SECOND dimension (4 -> 3).")
print("   => IDEMPOTENCY DOES NOT BLOCK ITERATION. Gate 3 does not fall this way.")
print()
print("="*80)
print("★ BUT IT DOES FALL -- by the residual-symmetry Schur argument (my own 5257, one level down)")
print("="*80)
print("  SO(n) acting on its VECTOR rep R^n has NO nonzero fixed vector, for every n >= 2.")
print("  (that is exactly 5257's engine: the only SO(5)-fixed vector in R^5 is 0.)")
print()
print("   step   symmetry   acts on   fixed vectors?   a direction available to project?")
for n in [5,4,3,2]:
    print("          SO(%d)      R^%d       %s              %s"%(n,n,"NO (only 0)","NO"))
print()
print("  observer at Omega_0 in S^4 BREAKS SO(5) -> SO(4). Omega_0 ITSELF is the fixed direction")
print("  -- the radial one -- and that is the one dropped. ONE datum, ONE direction.")
print("  RESIDUAL SO(4) on the remaining R^4 (the tangent/sky): NO fixed vector => NO SECOND")
print("  direction is available => THE ITERATION STOPS AFTER ONE.")
print()
print("  ⟹ GATE 3 FALLS -- but NOT by idempotency. By the same Schur argument as 5257, applied")
print("     to the residual symmetry. That is a stronger answer than the proposed handle.")
print()
print("  ★ AND THE PRECISE CONDITION: one projection per OBSERVER DATUM. If the observer supplies")
print("    only a POSITION, exactly one direction drops. Supplying a further datum (a frame, a")
print("    velocity) would break SO(4) further and license a second drop. So Gate 3 falls IFF the")
print("    observer is characterised by position alone -- which is a claim about Principle #16,")
print("    not about linear algebra. @Lyra: that is the precise thing owed.")
print()
print("="*80)
print("RADIAL vs ANGULAR -- the structure is already in my toy 5243 harmonic decomposition")
print("="*80)
print("  Sym^d(C^5) = (+)_k  Q^k H_{d-2k},  Q = sum z_j^2 (RADIAL invariant), H_m (ANGULAR harmonics).")
print("  'commitment records angle not depth' = the eigenstate carries m, not k.")
print()
print("   keep    modes up to N                       -> d (Weyl, lam~2N^2)")
tot=lambda N: sum(comb(m+4,4)-(comb(m+2,4) if m>=2 else 0) for m in range(N+1))
for N in [64,256,1024]:
    pass
prev=None
for N in [64,256,1024,4096]:
    lm=2*N**2; md=32*tot(N)
    if prev: d=2*np.log(md/prev[1])/np.log(lm/prev[0]); print("   k=0 only (pure angular): N=%5d  modes=%12d   d = %.4f"%(N,md,d))
    prev=(lm,md)
