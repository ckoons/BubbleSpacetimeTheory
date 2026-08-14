import numpy as np
rng=np.random.default_rng(3)

def sprinkle_diamond(N,d):
    """Uniform sprinkle into the Alexandrov interval (causal diamond) of d-dim Minkowski."""
    pts=[]
    while len(pts)<N:
        m=4*N
        t=rng.uniform(0,1,m); x=rng.uniform(-1,1,(m,d-1))
        r=np.linalg.norm(x,axis=1)
        ok=(r<t)&(r<1-t)                      # inside past+future light cones of the two tips
        for i in np.nonzero(ok)[0]:
            pts.append(np.concatenate(([t[i]],x[i])))
            if len(pts)>=N: break
    return np.array(pts[:N])

def relations(P):
    """causal matrix: i < j iff future-timelike separated"""
    N=len(P); dt=P[:,0][None,:]-P[:,0][:,None]
    dx=P[:,1:][None,:,:]-P[:,1:][:,None,:]
    s2=dt**2-np.sum(dx**2,axis=2)
    return (dt>0)&(s2>0)

def ordering_fraction(R):
    N=R.shape[0]; return R.sum()/(N*(N-1)/2)

def height(R):
    """longest chain, via DAG longest path"""
    N=R.shape[0]; order=np.argsort(-R.sum(axis=1))
    h=np.ones(N,dtype=int)
    idx=np.argsort(np.argsort([np.sum(R[:,i]) for i in range(N)]))
    for i in np.argsort([R[:,i].sum() for i in range(N)]):
        pred=np.nonzero(R[:,i])[0]
        if len(pred): h[i]=1+h[pred].max()
    return int(h.max())

print("STEP 1 -- CALIBRATE the estimator on sprinkled Minkowski (known answer).")
print("  d    ordering fraction r      height (longest chain)   N")
cal={}
for d in [2,3,4,5]:
    rs=[];hs=[]
    for _ in range(3):
        P=sprinkle_diamond(400,d); R=relations(P)
        rs.append(ordering_fraction(R)); hs.append(height(R))
    cal[d]=np.mean(rs)
    print("  %d    %.4f +- %.4f          %.1f                    400"%(d,np.mean(rs),np.std(rs),np.mean(hs)))
print()
print("  => r DECREASES monotonically with dimension -> invertible estimator. d=4 target r = %.4f"%cal[4])
print()
print("STEP 2 -- THE OBSTRUCTION: Kleitman-Rothschild orders (the generic causal set).")
print("  KR: 3 layers, sizes ~ N/4, N/2, N/4, all cross-relations present. Height = 3 ALWAYS.")
for N in [200,400,800]:
    n1,n2,n3=N//4,N//2,N-N//4-N//2
    R=np.zeros((N,N),bool)
    R[:n1,n1:n1+n2]=True; R[n1:n1+n2,n1+n2:]=True; R[:n1,n1+n2:]=True
    print("   N=%3d  KR ordering fraction = %.4f   height = %d"%(N,ordering_fraction(R),height(R)))
print()
print("  => KR r -> 5/8 = 0.625 and height = 3, FLAT in N.")
print("  => sprinkled (3,1) Minkowski: r = %.4f and height GROWS as N^(1/4)."%cal[4])
print("  => the two are trivially separable. THE TEST HAS TEETH.")
print()
print("STEP 3 -- height scaling for manifoldlike d=4 (the discriminator KR cannot fake):")
for N in [100,200,400,800]:
    P=sprinkle_diamond(N,4); R=relations(P)
    print("   N=%3d  height=%2d   N^(1/4)=%.2f"%(N,height(R),N**0.25))
