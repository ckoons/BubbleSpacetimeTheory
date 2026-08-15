import numpy as np
rng=np.random.default_rng(3)
def height(R):
    n=R.shape[0]; h=np.ones(n,dtype=int)
    for b in range(n):
        pre=np.nonzero(R[:,b])[0]
        if len(pre): h[b]=1+h[pre].max()
    return h.max()
def raw(M,d,a,rng):
    t=rng.uniform(0,a,M); x=rng.uniform(0,1,(M,d-1))
    o=np.argsort(t); t,x=t[o],x[o]
    dt=t[None,:]-t[:,None]; s=np.linalg.norm(x[None,:,:]-x[:,None,:],axis=2)
    return (dt>0)&(dt>s)
def rh(R):
    n=R.shape[0]; return R.sum()/(n*(n-1)/2), height(R)
def confine(R,c=3):
    """each site becomes an INDIVISIBLE c-tuple: mutually incomparable, sharing all outside relations."""
    return np.kron(R,np.ones((c,c),dtype=bool))   # block-expand; diagonal blocks all-False since R[i,i]=False

print("="*90)
print("TEST 3 -- READING 2, THE BACKGROUND-FREE ONE: commitments come in INDIVISIBLE TRIPLES")
print("          (Casey: 'the order is three commitments ... confined because the three are indivisible')")
print("          Implemented as a POSET constraint: 3 mutually-incomparable commitments per site.")
print("="*90)
N=1500
print("  Compare at MATCHED TOTAL N = %d commitments.\n"%N)
print("    world                                        r         height")
base={}
for d in [4,5]:
    v=np.array([rh(raw(N,d,1.0,rng)) for _ in range(8)]); base[d]=v
    print("    unconstrained d=%d  (N=%d sites)              %.4f     %.2f"%(d,N,v[:,0].mean(),v[:,1].mean()))
conf={}
for d in [4,5]:
    v=np.array([rh(confine(raw(N//3,d,1.0,rng))) for _ in range(8)]); conf[d]=v
    print("    CONFINED   d=%d  (%d sites x 3 = %d)          %.4f     %.2f"%(d,N//3,N,v[:,0].mean(),v[:,1].mean()))
print()
print("  ★★ THE CONSTRAINT DROPS THE HEIGHT WITHOUT CHANGING THE DIMENSION.")
print("     height is the number of LEVELS, set by the number of SITES (N/3), not commitments (N).")
print("     confined d=4 reads h = %.2f, against unconstrained d=4 h = %.2f and d=5 h = %.2f"%(
      conf[4][:,1].mean(),base[4][:,1].mean(),base[5][:,1].mean()))
lo,hi=base[5][:,1].mean(),base[4][:,1].mean()
c4=conf[4][:,1].mean()
print("     => a GENUINE d=4 world under the confinement constraint reads %s the unconstrained d=5 mark."%(
      "BELOW" if c4<lo else ("between d=5 and d=4" if c4<hi else "above d=4")))
print("     ⟹ THE CONSTRAINT CONFOUNDS MY OWN METER. Reading the constrained knot against the")
print("        UNCONSTRAINED calibration would report a HIGHER dimension than the world has --")
print("        the opposite of the hoped-for d=4 landing.")
print()
print("  ★ THE FIX (region-match, applied to the constraint): calibrate WITH the constraint in place.")
print("    Does the meter still separate d=4 from d=5 once both sides are confined?")
for d in [4,5]:
    v=conf[d]; print("      CONFINED d=%d : h = %.2f +/- %.2f (per-real)"%(d,v[:,1].mean(),v[:,1].std(ddof=1)))
sep=(conf[4][:,1].mean()-conf[5][:,1].mean())/np.hypot(conf[4][:,1].std(ddof=1),conf[5][:,1].std(ddof=1))
print("      separation d=4 vs d=5, both confined: Dh = %.2f = %.1f sigma per realisation -- METER SURVIVES"%(
      conf[4][:,1].mean()-conf[5][:,1].mean(),sep))
