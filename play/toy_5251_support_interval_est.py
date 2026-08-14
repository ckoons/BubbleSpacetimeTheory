import numpy as np
exec(open('causet.py').read().split('print("STEP 1')[0])
exec(open('commit_order.py').read().split('print("=" *')[0].split('print("=')[0])
rng=np.random.default_rng(33)

def interval_r(R,minsize=25,maxpairs=400):
    """Myrheim-Meyer done RIGHT: ordering fraction INSIDE Alexandrov intervals [a,b].
       Region-matched by construction -- this is why the standard estimator uses intervals."""
    N=R.shape[0]; out=[]
    pairs=np.argwhere(R)
    if len(pairs)>maxpairs: pairs=pairs[rng.choice(len(pairs),maxpairs,replace=False)]
    for a,b in pairs:
        mid=np.nonzero(R[a,:]&R[:,b])[0]
        if len(mid)>=minsize:
            S=R[np.ix_(mid,mid)]; m=len(mid)
            out.append(S.sum()/(m*(m-1)/2))
    return (np.median(out),len(out)) if out else (np.nan,0)

print("="*76)
print("REGION-MATCHED DIMENSION ESTIMATOR (ordering fraction INSIDE Alexandrov intervals)")
print("="*76)
print("Toy 5250 calibrated on WHOLE diamonds. The ESU slab gives DIFFERENT r at the SAME d")
print("(d=4: diamond 0.1022 vs ESU-slab 0.0618) -- r is REGION-dependent, so my own")
print("pre-registered '0.102 => d=4' was region-specific and I did not say so. Fixing it:")
print()
print("CALIBRATION -- interval-r on sprinkled MINKOWSKI (known d):")
cal={}
for d in [2,3,4,5]:
    P=sprinkle_diamond(1400,d); R=relations(P)
    r,k=interval_r(R); cal[d]=r
    print("   d=%d   interval-r = %.4f   (from %d intervals)"%(d,r,k))
print()
print("MEASURED -- interval-r on BST's commit order (Shilov boundary R x S^4):")
for N in [1200,2000]:
    t,x=sprinkle_ESU(N,4,2.0); R=relations_ESU(t,x)
    r,k=interval_r(R)
    print("   N=%d  interval-r = %.4f  (from %d intervals)   whole-region r = %.4f  height = %d"%(
        N,r,k,ordering_fraction(R),height(R)))
print()
print("CONTROL -- interval-r on the KR pancake (the generic causal set):")
for N in [400,800]:
    n1,n2=N//4,N//2
    Rk=np.zeros((N,N),bool); Rk[:n1,n1:n1+n2]=True; Rk[n1:n1+n2,n1+n2:]=True; Rk[:n1,n1+n2:]=True
    r,k=interval_r(Rk)
    print("   N=%d  interval-r = %s  (from %d intervals)   whole-region r = %.4f  height = %d"%(
        N,("%.4f"%r) if k else "n/a",k,ordering_fraction(Rk),height(Rk)))
