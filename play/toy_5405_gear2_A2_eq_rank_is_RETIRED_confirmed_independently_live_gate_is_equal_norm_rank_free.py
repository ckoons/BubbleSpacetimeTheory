import numpy as np
from math import cos, pi, sqrt
print("="*104)
print("TOY 5405 -- GEAR 2 (mass sector). ASSIGNED: 'does A^2 = rank fall out of the mass operator?'")
print("  *** RECONNECT FIRST (yesterday's lesson). THE ASSIGNED TARGET IS RETIRED. ***")
print("    K1624 (2026-08-16): \"A^2=rank is RETIRED -- a rank-2 coincidence (equal-norm reads")
print("    A^2=2 at every rank); the honest statement is 'A^2=2 from equal-norm'.\"")
print("    Cal §544: \"EQUAL-NORM *IS* theta=45deg ... A^2=2 AT EVERY RANK, so 'A^2=rank' is a")
print("    COINCIDENCE at r=2, not a structural identity.\"")
print("  *** You cannot derive a coincidence. Confirm it, then restate the LIVE gate. ***")
print("="*104)

print("\nTABLE 1 -- *** CONFIRM THE RETIREMENT MYSELF (do not take it on citation) ***")
print("  Parametrise sqrt(m_k) = M(1 + A cos(delta + 2 pi k / N)), k = 0..N-1, N = N_gen.")
print("  Then Sum sqrt(m) = N M ; Sum m = M^2 (N + A^2 N/2) ; Q = Sum m / (Sum sqrt m)^2.")
def Q_of(N,A,delta=0.0):
    r=[1+A*cos(delta+2*pi*k/N) for k in range(N)]
    return sum(x*x for x in r)/sum(r)**2
print("   N_gen  rank=N-1   A^2 solving Q = 2/N   A^2 solving Q = rank/N_c(=2/3)   equal-norm A^2")
for N in range(3,8):
    # A^2 from equal-norm: |democratic| = |hierarchy|
    # |dem|^2 = N ; |hier|^2 = A^2 N/2  ->  A^2 = 2
    Aen=2.0
    # A^2 that reproduces Q = 2/N
    A2_target=2.0
    # A^2 that would reproduce a FIXED Q = 2/3 (the rank/N_c reading)
    from scipy.optimize import brentq
    f=lambda a2: Q_of(N,sqrt(max(a2,0)))-2.0/3.0
    try: A2_23=brentq(f,1e-9,50)
    except Exception: A2_23=float('nan')
    print("   %-6d %-10d %-21.4f %-32.4f %.4f"%(N,N-1,A2_target,A2_23,Aen))
print("   *** A^2 = 2 AT EVERY N_gen -- equal-norm is a statement about TWO ORTHOGONAL PARTS of ONE")
print("       vector and never mentions rank. *** So 'A^2 = rank' is true only because rank = 2 here.")

print("\nTABLE 2 -- *** THE TWO READINGS DIVERGE OFF r = 2 (Cal's pre-registered discriminator) ***")
print("   rank r   N_gen=r+1   Q = 2/N_gen (equal-norm)   Q = (1+r/2)/(r+1) ('A^2=rank')   agree?")
for r in range(1,7):
    N=r+1; q1=2.0/N; q2=(1+r/2)/N
    print("   %-8d %-11d %-25.4f %-33.4f %s"%(r,N,q1,q2,"*** YES ***" if abs(q1-q2)<1e-12 else "no"))
print("   *** They agree ONLY at r = 2 (both 2/3) and diverge everywhere else -- r=3 gives 0.500 vs")
print("       0.625. *** Retirement CONFIRMED independently. And note the SECOND conflation Cal")
print("       flagged: 'Q = rank/N_c' also needs N_gen <-> N_c, two different objects sharing a 3.")

print("\nTABLE 3 -- *** WHAT THE DATA ACTUALLY SAYS (target-innocent check of equal-norm) ***")
me,mmu,mtau=0.51099895000,105.6583755,1776.86      # MeV, PDG
v=np.array([sqrt(me),sqrt(mmu),sqrt(mtau)])
dem=np.full(3,v.mean()); hier=v-dem
Q=(v**2).sum()/v.sum()**2
theta=np.degrees(np.arctan2(np.linalg.norm(hier),np.linalg.norm(dem)))
A2_direct=2*np.sum(hier**2)/(3*v.mean()**2)
print("   Q_observed              = %.8f   (2/3 = %.8f, dev %.4f%%)"%(Q,2/3,100*abs(Q-2/3)/(2/3)))
print("   |democratic| = %.6f ,  |hierarchy| = %.6f"%(np.linalg.norm(dem),np.linalg.norm(hier)))
print("   ratio |hier|/|dem|      = %.6f   (equal-norm predicts 1)"%(np.linalg.norm(hier)/np.linalg.norm(dem)))
print("   tilt theta              = %.4f deg (equal-norm predicts 45)"%theta)
print("   A^2 (from |hier|^2)     = %.4f   (equal-norm predicts 2)"%A2_direct)
print("   *** THE DATA SITS ON EQUAL-NORM TO ~0.02%. That is the FACT to be explained -- and it is")
print("       ONE fact in three languages (equal-norm = 45deg = A^2=2), NOT three checks. ***")

print("\n"+"="*104)
print("VERDICT -- Gear 2, morning reconnect")
print("="*104)
print(" (1) ★★★ *** THE ASSIGNED TARGET IS RETIRED AND I CONFIRMED IT INDEPENDENTLY. *** 'A^2 = rank'")
print("     was settled in the NEGATIVE on 2026-08-16 (K1624 + Cal §544): equal-norm forces A^2 = 2")
print("     at EVERY rank, so the identity holds at r=2 by coincidence. *** A coincidence cannot be")
print("     derived, so the gate 'derive A^2 = rank from the Bergman overlap' is ILL-POSED. ***")
print()
print(" (2) *** AND THE OLD FORM CARRIES A SECOND CONFLATION: 'Q = rank/N_c' needs BOTH A^2<->rank")
print("     AND N_gen<->N_c -- two different objects that happen to share a 3. *** The clean form is")
print("     Q = 2/N_gen, which is what equal-norm actually gives.")
print()
print(" (3) *** THE LIVE GATE, CORRECTLY STATED -- and it is rank-free: ***")
print("       *** DOES THE GEOMETRY FORCE EQUAL-NORM (|democratic| = |hierarchy|) AT THE THREE")
print("       STRATA, WITHOUT MASS INPUT? *** Win: equal-norm falls out -> theta=45 -> A^2=2 ->")
print("       Q = 2/N_gen = 2/3, and Koide moves C -> D. Lose: it doesn't, and that is a clean 'not yet'.")
print()
print(" (4) THE DATA SITS ON IT AT 0.02%% (theta = %.4f deg vs 45). *** That is the fact to explain."%theta)
print("     And it is ONE fact in three languages -- equal-norm, 45 degrees, A^2 = 2 -- so it must be")
print("     counted ONCE, not as three passing checks. ***")
print()
print(" (5) ★ MISS OWNED IN ONE LINE: I would have spent the morning deriving a claim my own corpus")
print("     retired five days ago. The grep cost two minutes. *** Reconnect before you derive. ***")
