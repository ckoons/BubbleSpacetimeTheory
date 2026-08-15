import numpy as np
rng=np.random.default_rng(1567)
print("="*90)
print("BAR-3: is BST's event structure SPRINKLING-LIKE (Poisson, Lorentz-invariant) or")
print("       DETERMINISTIC-REGULAR (a clock, frame-dependent)?  Bombelli-Henson-Sorkin.")
print("="*90)
print("The corpus does NOT hand me a point process -- it hands me a MEASURE (uniform on S^4, forced by")
print("the Casimir, my 5256/5272) plus a TICK and a CAP (N_max, F865). So I test the HYPOTHESES the")
print("corpus's own features imply, and report what each costs. Not a sprinkling by assumption.\n")
T,X=400.0,400.0; rho=1.0
def poisson_events():
    N=rng.poisson(rho*T*X)
    return rng.uniform(0,T,N), rng.uniform(0,X,N)
def regular_tick(dtau=1.0):
    """Casey's 'the commitment tick IS time': one layer per tick, sites uniform in space."""
    layers=np.arange(0,T,dtau)
    per=int(round(rho*X*dtau))
    t=np.repeat(layers,per); x=rng.uniform(0,X,t.size)
    return t,x
def fixed_N():
    """the N_max cap: a FIXED total count, not a random one."""
    N=int(rho*T*X)
    return rng.uniform(0,T,N), rng.uniform(0,X,N)
def fano_at_boost(t,x,v,cell=2.0,ncell=4000):
    g=1/np.sqrt(1-v*v)
    tp=g*(t-v*x); xp=g*(x-v*t)
    lo_t,hi_t=np.quantile(tp,[0.25,0.75]); lo_x,hi_x=np.quantile(xp,[0.25,0.75])
    ct=rng.uniform(lo_t,hi_t-cell,ncell); cx=rng.uniform(lo_x,hi_x-cell,ncell)
    idx=np.argsort(tp); tps,xps=tp[idx],xp[idx]
    counts=np.empty(ncell)
    for i,(a,b) in enumerate(zip(ct,cx)):
        lo=np.searchsorted(tps,a); hi=np.searchsorted(tps,a+cell)
        seg=xps[lo:hi]
        counts[i]=((seg>=b)&(seg<b+cell)).sum()
    return counts.var()/counts.mean()
print("  Fano factor (variance/mean of counts in cells of FIXED PROPER AREA) vs boost rapidity.")
print("  Poisson is the ONLY Lorentz-invariant discrete distribution => Fano = 1 in EVERY frame.\n")
print("     v       Poisson      regular tick     fixed-N")
tp_,xp_=poisson_events(); tr,xr=regular_tick(); tf,xf=fixed_N()
for v in [0.0,0.3,0.6,0.9,0.99]:
    a=fano_at_boost(tp_,xp_,v); b=fano_at_boost(tr,xr,v); c=fano_at_boost(tf,xf,v)
    print("   %5.2f      %.4f        %.4f          %.4f"%(v,a,b,c))
print()
print("  Now the sharpest cell size -- comparable to the tick (where discreteness shows):")
print("     v       Poisson      regular tick")
for v in [0.0,0.3,0.6,0.9,0.99]:
    a=fano_at_boost(tp_,xp_,v,cell=0.8); b=fano_at_boost(tr,xr,v,cell=0.8)
    print("   %5.2f      %.4f        %.4f"%(v,a,b))
