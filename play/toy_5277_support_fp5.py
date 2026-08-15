import numpy as np
rng=np.random.default_rng(55)
def height(R):
    n=R.shape[0]; h=np.ones(n,dtype=int)
    for b in range(n):
        pre=np.nonzero(R[:,b])[0]
        if len(pre): h[b]=1+h[pre].max()
    return h.max()
def sphere_case(N,k,T,rng):
    t=rng.uniform(0,T,N); x=rng.normal(size=(N,k+1)); x/=np.linalg.norm(x,axis=1)[:,None]
    o=np.argsort(t); t,x=t[o],x[o]
    dt=t[None,:]-t[:,None]; dth=np.arccos(np.clip(x@x.T,-1,1))
    R=(dt>0)&(dt>dth); return R.sum()/(N*(N-1)/2), height(R)
def box_case(N,d,a,rng):
    t=rng.uniform(0,a,N); x=rng.uniform(0,1,(N,d-1))
    o=np.argsort(t); t,x=t[o],x[o]
    dt=t[None,:]-t[:,None]; s=np.linalg.norm(x[None,:,:]-x[:,None,:],axis=2)
    R=(dt>0)&(dt>s); return R.sum()/(N*(N-1)/2), height(R)
def solve(fn,N,p,target,rng,lo,hi):
    for _ in range(24):
        mid=(lo*hi)**0.5
        r=np.mean([fn(N,p,mid,rng)[0] for _ in range(3)])
        if r<target: lo=mid
        else: hi=mid
    return (lo*hi)**0.5
N=800; tgt=0.10
print("PROPERLY MATCHED at r = %.2f, N = %d, both region shapes (I mis-set T on the first pass).\n"%(tgt,N))
print("   BST's own region  R x S^k :")
sph={}
for k in [2,3,4]:
    T=solve(sphere_case,N,k,tgt,rng,0.2,12.0)
    v=np.array([sphere_case(N,k,T,rng) for _ in range(20)]); sph[k+1]=v
    print("     k=%d (d=%d)  T*=%.3f   r=%.4f   h = %.2f +/- %.2f"%(k,k+1,T,v[:,0].mean(),v[:,1].mean(),v[:,1].std(ddof=1)))
print("\n   flat box (the usual calibration region):")
box={}
for d in [3,4,5]:
    a=solve(box_case,N,d,tgt,rng,0.05,20.0)
    v=np.array([box_case(N,d,a,rng) for _ in range(20)]); box[d]=v
    print("     d=%d        a*=%.3f   r=%.4f   h = %.2f +/- %.2f"%(d,a,v[:,0].mean(),v[:,1].mean(),v[:,1].std(ddof=1)))
print("\n  separation of d WITHIN each region (per-realisation sigma):")
for lbl,D in [("R x S^k",sph),("flat box",box)]:
    for d in [3,4]:
        a,b=D[d],D[d+1]
        s=(a[:,1].mean()-b[:,1].mean())/np.hypot(a[:,1].std(ddof=1),b[:,1].std(ddof=1))
        print("     %-9s d=%d vs d=%d : Dh = %.2f = %.1f sigma"%(lbl,d,d+1,a[:,1].mean()-b[:,1].mean(),s))
print("\n  cross-region transfer (same d, same r, different region shape):")
for d in [3,4,5]:
    print("     d=%d : h(R x S^k) = %.2f   vs   h(box) = %.2f   -> differ by %.2f"%(d,sph[d][:,1].mean(),box[d][:,1].mean(),abs(sph[d][:,1].mean()-box[d][:,1].mean())))
