import numpy as np
rng=np.random.default_rng(7)
print("CONTROL (region-matched, flat 5D Minkowski R^{1,4}, FIXED box, refine density only):")
print("separate the two quantities -- link PROPER TIME vs link SPATIAL separation.\n")
def links_ok(R): return R & ~((R.astype(np.float64)@R.astype(np.float64))>0.5)
print("   N     n_links   <link proper time>   <link |dx|>    <|dx|/dt>")
pt=[];sp=[]
for N in [500,1000,2000,4000,8000]:
    t=rng.uniform(0,1,N); x=rng.uniform(0,1,(N,4))
    dt=t[None,:]-t[:,None]
    d=np.linalg.norm(x[None,:,:]-x[:,None,:],axis=2)
    R=(dt>0)&(dt>d); L=links_ok(R); i,j=np.nonzero(L)
    tau=np.sqrt((t[j]-t[i])**2-d[i,j]**2); dx=d[i,j]
    pt.append(tau.mean()); sp.append(dx.mean())
    print("  %5d  %8d      %.5f            %.5f        %.3f"%(N,L.sum(),tau.mean(),dx.mean(),(dx/(t[j]-t[i])).mean()))
print()
print("  proper time  500->8000 (16x density): %.5f -> %.5f  ratio %.3f   [16^(-1/5)=%.3f]"%(pt[0],pt[-1],pt[-1]/pt[0],16**-0.2))
print("  SPATIAL sep  500->8000 (16x density): %.5f -> %.5f  ratio %.3f   [ FLAT ]"%(sp[0],sp[-1],sp[-1]/sp[0]))
print()
print("  => PROPER TIME shrinks with density (the discreteness scale).")
print("  => SPATIAL SEPARATION does NOT. Links are near-null and boost-invariance spreads them")
print("     over the whole light cone: NEAREST-IN-ORDER IS NOT NEAREST-IN-SPACE.")
