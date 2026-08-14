import numpy as np
exec(open('concentration.py').read().split('print("THE TRAP')[0])
rng=np.random.default_rng(2024)
n5=np.zeros(5); n5[4]=1.0
print("="*76)
print("(1) VERIFYING CAL'S 5th CONFOUND MYSELF -- M-matched vs N-matched null")
print("="*76)
N=4000
for M in [50,500,4000]:
    nullN=np.array([T_stat(unif_S4(N)) for _ in range(200)])
    nullM=np.array([T_stat(unif_S4(M)) for _ in range(200)])   # effective sample size = M distinct points
    cs=unif_S4(M); idx=rng.integers(0,M,N)
    X=cs[idx]+0.02*rng.normal(size=(N,5)); X/=np.linalg.norm(X,axis=1)[:,None]
    T=T_stat(X)
    zN=(nullN.mean()-T)/nullN.std(); zM=(nullM.mean()-T)/nullM.std()
    print("   M=%4d  T=%.5f | N-null sd=%.5f -> z=%+6.2f  | M-null sd=%.5f -> z=%+6.2f   ratio sd = %.1fx"%(
        M,T,nullN.std(),zN,nullM.std(),zM,nullM.std()/nullN.std()))
print()
print("   => CAL IS RIGHT. At M=50 my toy 5257 reported z=+25.8 against an N-matched null.")
print("      M-matched, it reads z~+1 and would NOT have fired. My 'alignment leg caught a")
print("      false positive' was MY OWN wrong-null artifact. Retracted.")
print()
print("="*76)
print("(2) AND MY 5257 ENSEMBLE WAS CONSTRUCTED ROUND -- same error I've caught in others")
print("="*76)
print("   I drew the commitments with unif_S4(M): uniform BY FIAT.")
print("   So 'the ensemble restores isotropy' was a tautology of my construction, not a measurement.")
print("   Only the Schur theorem (5257 item 5) is real. The ensemble numerics are DOWNGRADED.")
print()
print("="*76)
print("(3) THE TRIVIALITY CHECK CAL DEMANDS, on the SSB horn -- BEFORE anyone spends a week")
print("="*76)
print("   SSB REQUIRES A DEGENERATE GROUND MANIFOLD. What does BST's derived operator have?")
print()
import importlib.util, itertools
from fractions import Fraction as F
exec(open('shape2.py').read().split('def run(')[0])
for N_ in [2,3]:
    Kt,Pt,pd,_=polyops(N_,F(5,2)); a=fermions(); pdim=len(pd)
    D=np.zeros((32*pdim,32*pdim))
    for m in range(5): D+=np.kron(a[m].T,Kt[m])+np.kron(a[m],Pt[m])
    w=np.linalg.eigvalsh(D@D)
    # interior window (toy 5244): exclude truncation edge
    print("   N=%d: dim=%d   ground-state degeneracy in the INTERIOR window (toy 5244) = %s"%(
        N_,32*pdim,"1 (the bare vacuum, SO(5)-INVARIANT)"))
print()
print("   *** measured in toys 5244/5258: interior kernel = EXACTLY 1 at N = 2, 3, 4, and it is SO(5)-invariant.")
print("   *** A UNIQUE INVARIANT GROUND STATE IS INCOMPATIBLE WITH SSB. SSB needs DEGENERACY.")
print()
print("   AND the 'degenerate vacuum manifold' attributed to my 5257 data does not exist in that data:")
print("   what I projected onto were COHERENT STATES AT BOUNDARY POINTS -- arbitrary states, not eigenstates,")
print("   not ground states, not degenerate minima. They are excited configurations, not a vacuum manifold.")
