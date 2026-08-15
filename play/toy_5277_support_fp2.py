import numpy as np
rng=np.random.default_rng(991)
def order(t,x):
    dt=t[None,:]-t[:,None]; s=np.linalg.norm(x[None,:,:]-x[:,None,:],axis=2)
    return (dt>0)&(dt>s)
def height(R):
    n=R.shape[0]; h=np.ones(n,dtype=int)
    for b in range(n):
        pre=np.nonzero(R[:,b])[0]
        if len(pre): h[b]=1+h[pre].max()
    return h.max()
def stats(N,d,a,rng,reps=4):
    rs=[];hs=[]
    for _ in range(reps):
        t=rng.uniform(0,a,N); x=rng.uniform(0,1,(N,d-1))
        o=np.argsort(t); t,x=t[o],x[o]; R=order(t,x)
        rs.append(R.sum()/(N*(N-1)/2)); hs.append(height(R))
    return np.mean(rs),np.mean(hs)

N=600
print("="*88)
print("PART 2 -- THE STRETCH DEGENERACY (Lyra F991) AND WHETHER A SECOND INVARIANT BREAKS IT")
print("="*88)
print("a = T/L (aspect ratio of the region). N = %d fixed.\n"%N)
print("   a       d=3  (r,h)        d=4  (r,h)        d=5  (r,h)")
for a in [0.25,0.5,0.75,1.0,1.5,2.0,3.0]:
    row="  %4.2f "%a
    for d in [3,4,5]:
        r,h=stats(N,d,a,rng); row+="   %.4f,%5.1f "%(r,h)
    print(row)
print()
print("★ r ALONE IS DEGENERATE: sweeping the aspect ratio sweeps r continuously in each d, so for")
print("  EVERY target r there is an aspect realising it in EVERY d. Lyra's F991 caution is exact.")
print()
print("NOW MATCH r ACROSS d AND ASK WHETHER THE HEIGHT SEPARATES THEM:")
target=0.1063
def solve_a(d,target,rng):
    lo,hi=0.05,20.0
    for _ in range(28):
        mid=(lo*hi)**0.5
        r,_=stats(N,d,mid,rng,reps=3)
        if r<target: lo=mid
        else: hi=mid
    return (lo*hi)**0.5
print("   target ordering fraction r = %.4f  (the d=5 cube value)"%target)
print("     d    aspect a solving r=target     r achieved     HEIGHT h")
res=[]
for d in [3,4,5]:
    a=solve_a(d,target,rng); r,h=stats(N,d,a,rng,reps=8); res.append((d,a,r,h))
    print("    %2d          %.4f                  %.4f          %5.1f"%(d,a,r,h))
print()
hs=[x[3] for x in res]
print("  => at MATCHED r = %.4f the heights are %s"%(target," / ".join("%.1f"%h for h in hs)))
print("     separation d=3 vs d=5: factor %.2f ; d=4 vs d=5: factor %.2f"%(hs[0]/hs[2],hs[1]/hs[2]))
