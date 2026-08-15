import numpy as np
rng=np.random.default_rng(1567)
print("EDGE-EFFECT BUG IN MY FIRST PASS: after boosting, the region is a sheared parallelogram and my")
print("cells partly fell OUTSIDE it -- empty cells inflated the variance, so even POISSON read")
print("Fano 3.85 at v=0.9. That is a region-matching failure, not physics. Fixed: accept a cell only")
print("if all four corners inverse-boost back INSIDE the source rectangle.\n")
T,X,rho=600.0,600.0,1.0
def poisson_events():
    N=rng.poisson(rho*T*X); return rng.uniform(0,T,N), rng.uniform(0,X,N)
def regular_tick(dtau=1.0):
    layers=np.arange(0,T,dtau); per=int(round(rho*X*dtau))
    return np.repeat(layers,per), rng.uniform(0,X,layers.size*per)
def fixed_N():
    N=int(rho*T*X); return rng.uniform(0,T,N), rng.uniform(0,X,N)
def fano(t,x,v,cell,ncell=3000):
    g=1/np.sqrt(1-v*v)
    tp=g*(t-v*x); xp=g*(x-v*t)
    idx=np.argsort(tp); tps,xps=tp[idx],xp[idx]
    lo_t,hi_t=tps[0],tps[-1]; lo_x,hi_x=xps.min(),xps.max()
    counts=[]; tries=0
    while len(counts)<ncell and tries<ncell*60:
        tries+=1
        a=rng.uniform(lo_t,hi_t-cell); b=rng.uniform(lo_x,hi_x-cell)
        # inverse boost the four corners; require all inside [0,T]x[0,X]
        cs=np.array([[a,b],[a+cell,b],[a,b+cell],[a+cell,b+cell]])
        tt=g*(cs[:,0]+v*cs[:,1]); xx=g*(cs[:,1]+v*cs[:,0])
        if tt.min()<0 or tt.max()>T or xx.min()<0 or xx.max()>X: continue
        lo=np.searchsorted(tps,a); hi=np.searchsorted(tps,a+cell)
        seg=xps[lo:hi]
        counts.append(((seg>=b)&(seg<b+cell)).sum())
    c=np.array(counts,float)
    return (c.var()/c.mean() if c.mean()>0 else np.nan), len(c)
tp_,xp_=poisson_events(); tr,xr=regular_tick(); tf,xf=fixed_N()
for cell in (3.0,1.0):
    print("  cell side = %.1f  (tick = 1.0).  Fano = var/mean of counts in interior cells."%cell)
    print("     v       Poisson       regular tick      fixed-N")
    for v in [0.0,0.3,0.6,0.9]:
        a,_=fano(tp_,xp_,v,cell); b,_=fano(tr,xr,v,cell); c,_=fano(tf,xf,v,cell)
        print("   %5.2f      %.4f         %.4f           %.4f"%(v,a,b,c))
    print()
