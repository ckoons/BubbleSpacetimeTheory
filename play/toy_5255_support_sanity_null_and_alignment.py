import numpy as np
exec(open('concentration.py').read().split('print("THE TRAP')[0])
rng=np.random.default_rng(909)

print("STEP 0 -- SANITY NULL (K1504): the ROUND measure at data-N must read UNIFORM.")
print("  positive control that the pipeline does not manufacture concentration.")
print("   N       T(round)    N-matched null    z      verdict")
for N in [500,2000,10000]:
    null=np.array([T_stat(unif_S4(N)) for _ in range(300)])
    T=T_stat(unif_S4(N)); z=(null.mean()-T)/null.std()
    print("   %5d   %.5f     %.5f +- %.5f   %+.2f   %s"%(N,T,null.mean(),null.std(),z,"UNIFORM (correct)" if abs(z)<3 else "FAILS"))
print()
print("="*76)
print("STEP 2's OWN NULL -- @Keeper's K1505 alignment check needs one too.")
print("="*76)
print("  alignment A = |<v_min | n_named>|.  Under ISOTROPY v_min is a RANDOM direction in R^5,")
print("  so E[A^2] = 1/5 => A ~ 0.45 BY CHANCE. An alignment of 0.45 is NOT evidence.")
print()
n=np.zeros(5); n[4]=1.0
print("   N       A(uniform)  mean    p95     p99     => threshold to beat")
for N in [500,2000,10000]:
    As=[]
    for _ in range(400):
        X=unif_S4(N); C=(X.T@X)/N
        w,V=np.linalg.eigh(C); As.append(abs(V[:,0]@n))
    As=np.array(As)
    print("   %5d               %.3f   %.3f   %.3f   A must exceed ~%.2f"%(N,As.mean(),np.percentile(As,95),np.percentile(As,99),np.percentile(As,99)))
print()
print("POWER -- when is v_min reliably aligned? (band about the n-axis equator, N=2000)")
print("   delta    T        z(magnitude)   A(alignment)   both fire?")
N=2000
null=np.array([T_stat(unif_S4(N)) for _ in range(300)]); mu,sd=null.mean(),null.std()
for delta in [1.2,1.0,0.8,0.6,0.4,0.25]:
    Ts=[];As=[]
    for _ in range(15):
        X=band_S4(N,delta); C=(X.T@X)/N; w,V=np.linalg.eigh(C)
        Ts.append(w[0]); As.append(abs(V[:,0]@n))
    z=(mu-np.mean(Ts))/sd; A=np.mean(As)
    print("   %.2f     %.5f  %8.1f      %.3f          %s"%(delta,np.mean(Ts),z,A,"YES" if z>5 and A>0.9 else ("magnitude only" if z>5 else "no")))
