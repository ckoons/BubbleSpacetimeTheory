import numpy as np
exec(open('concentration.py').read().split('print("THE TRAP')[0])
rng=np.random.default_rng(1313)
n5=np.zeros(5); n5[4]=1.0
N=4000
null=np.array([T_stat(unif_S4(N)) for _ in range(200)]); mu,sd=null.mean(),null.std()
print("="*76)
print("NEW PRE-REGISTRATION -- the commitment-projection candidate (K1509)")
print("="*76)
print("Committed BEFORE computing, and NOT carrying the old test's assumptions:")
print("  H1  the commitment projection selects a preferred R^5 direction   -> ensemble T << null, A > 0.917")
print("  H0  it breaks SO(5) only per-commitment, ensemble restores it     -> T at null, A at chance")
print("  bar: z > 5 AND A > 0.917 (Cal's reconciled p99, N-matched). Both outcomes readable.")
print()
print("N-matched null at N=%d: T = %.5f +- %.5f"%(N,mu,sd))
print()
print("--- (a) is a SINGLE commitment anisotropic?  (it should be -- maximally so) ---")
c=unif_S4(1)[0]
X=np.tile(c,(N,1))+0.02*rng.normal(size=(N,5)); X/=np.linalg.norm(X,axis=1)[:,None]
C=(X.T@X)/N; ev,V=np.linalg.eigh(C)
print("   single commitment at a point: T = %.5f  (z = %.1f)  -> maximally anisotropic, as expected"%(ev[0],(mu-ev[0])/sd))
print()
print("--- (b) is the ENSEMBLE over commitments anisotropic?  (the actual question) ---")
for M,tag in [(50,"50 commitments"),(500,"500 commitments"),(4000,"4000 commitments")]:
    cs=unif_S4(M)                       # commitments drawn SO(5)-equivariantly: no direction preferred
    idx=rng.integers(0,M,N)
    X=cs[idx]+0.02*rng.normal(size=(N,5)); X/=np.linalg.norm(X,axis=1)[:,None]
    C=(X.T@X)/N; ev,V=np.linalg.eigh(C); A=abs(V[:,0]@n5)
    z=(mu-ev[0])/sd
    print("   %-16s T = %.5f   z = %+6.2f   A = %.3f   -> %s"%(tag,ev[0],z,A,"H1 (selects)" if z>5 and A>0.917 else "H0 (ensemble round)"))
print()
print("="*76)
print("AND THE THEOREM THAT COVERS EVERY CANDIDATE, NOT JUST THIS ONE:")
print("="*76)
print("  Suppose a construction is SO(5)-EQUIVARIANT and its inputs are SO(5)-INVARIANT.")
print("  If it outputs a distinguished direction n in R^5, then n must be fixed by all of SO(5).")
print("  The ONLY SO(5)-fixed vector in R^5 is 0.  =>  CONTRADICTION.")
print("  => NO SO(5)-equivariant construction from invariant inputs can produce a preferred R^5 direction.")
print()
print("  SO(5) is part of the ISOTROPY group K = SO(5)xSO(2) of D_IV^5. So every object built")
print("  equivariantly from the geometry alone -- Casimir, Bergman kernel, generic norm, bare vacuum,")
print("  commitment ensemble -- is direction-blind. Individual commitments break it; the orbit restores it.")
print("  => a DERIVED descent needs an input that is NOT SO(5)-equivariant, i.e. from OUTSIDE the isotropy group.")
