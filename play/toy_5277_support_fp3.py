import numpy as np
rng=np.random.default_rng(1234)
def height(R):
    n=R.shape[0]; h=np.ones(n,dtype=int)
    for b in range(n):
        pre=np.nonzero(R[:,b])[0]
        if len(pre): h[b]=1+h[pre].max()
    return h.max()
def one(N,d,a,rng):
    t=rng.uniform(0,a,N); x=rng.uniform(0,1,(N,d-1))
    o=np.argsort(t); t,x=t[o],x[o]
    dt=t[None,:]-t[:,None]; s=np.linalg.norm(x[None,:,:]-x[:,None,:],axis=2)
    R=(dt>0)&(dt>s)
    return R.sum()/(N*(N-1)/2), height(R)
def stats(N,d,a,rng,reps):
    v=np.array([one(N,d,a,rng) for _ in range(reps)])
    return v[:,0].mean(), v[:,1].mean(), v[:,1].std(ddof=1)
def solve_a(N,d,target,rng):
    lo,hi=0.05,20.0
    for _ in range(26):
        mid=(lo*hi)**0.5
        r,_,_=stats(N,d,mid,rng,3)
        if r<target: lo=mid
        else: hi=mid
    return (lo*hi)**0.5

print("INSTRUMENT CHARACTERISATION: is (r, height) a STRETCH-PROOF dimension discriminator?")
print("At matched r, separation of d measured in sigma of the height fluctuation.\n")
for N in [400,800,1600]:
  print("  N = %d"%N)
  for target in [0.10,0.20]:
    out=[]
    for d in [3,4,5]:
        a=solve_a(N,d,target,rng); r,h,sd=stats(N,d,a,rng,24); out.append((d,a,r,h,sd))
    print("    target r=%.2f :"%target)
    for d,a,r,h,sd in out:
        print("       d=%d  a=%.3f  r=%.4f  h = %.2f +/- %.2f"%(d,a,r,h,sd))
    for k in range(len(out)-1):
        d1,_,_,h1,s1=out[k]; d2,_,_,h2,s2=out[k+1]
        print("       d=%d vs d=%d : Dh = %.2f  =  %.1f sigma"%(d1,d2,h1-h2,(h1-h2)/np.hypot(s1,s2)))
  print()
