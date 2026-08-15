import numpy as np
rng=np.random.default_rng(1551)

print("="*84)
print("LEG A -- does T2564's DERIVED causal-order adjacency deliver the <1e-4 rad per-tick step?")
print("="*84)
print("T2564's order (F989-confirmed object): conformal Lorentzian order on the Shilov boundary,")
print("unwrapped S^1 -> R, i.e. on R x S^4:   a < b  iff  Dt > Dtheta  (geodesic dist on unit S^4).")
print()

def sprinkle(N,T,rng):
    t=rng.uniform(0,T,N)
    x=rng.normal(size=(N,5)); x/=np.linalg.norm(x,axis=1)[:,None]
    return t,x

def rel(t,x):
    dt=t[None,:]-t[:,None]
    dth=np.arccos(np.clip(x@x.T,-1,1))
    return (dt>0)&(dt>dth), dth

def links(R):
    # covering relations: a<b with no c strictly between
    return R & ~((R.astype(np.int8)@R.astype(np.int8))>0)

# ---- A1: links are NEARLY NULL -> the step SATURATES the light-cone bound, it does not sit far below it
print("A1. For COVERING relations (links = one tick apart), how big is Dtheta relative to Dt?")
N,T=1400,0.60
t,x=sprinkle(N,T,rng); R,dth=rel(t,x); L=links(R)
i,j=np.nonzero(L)
dt=t[j]-t[i]; ang=dth[i,j]
print("    n_links = %d   <Dtheta/Dt> = %.4f   median = %.4f   (1.0 = exactly null)"%(len(i),(ang/dt).mean(),np.median(ang/dt)))
print("    <Dtheta> = %.5f rad   <Dt> = %.5f"%(ang.mean(),dt.mean()))
print("    => causal adjacency bounds the step by Dt, and the bound is very nearly SATURATED.")
print("       The order does NOT make the step small COMPARED TO THE TICK; it makes it comparable.")
print()

# ---- A2: the step magnitude is set by the DENSITY (number), not by the order
print("A2. Where does the magnitude come from? Sprinkle at three densities, measure the link step.")
print("    Sorkin: number = volume. Discreteness length l ~ rho^(-1/5) in 5 dims.")
rows=[]
for N in [500,1500,4500]:
    t,x=sprinkle(N,0.60,rng); R,dth=rel(t,x); L=links(R)
    i,j=np.nonzero(L); a=dth[i,j].mean()
    rho=N/0.60
    rows.append((N,rho,a))
    print("      N=%5d  rho=%8.1f   <link Dtheta> = %.5f rad"%(N,rho,a))
r1,r2=rows[0],rows[2]
obs=r1[2]/r2[2]; pred=(r2[1]/r1[1])**(1/5)
print("    ratio of steps (N=500 vs 4500) = %.3f   predicted rho^(-1/5) scaling = %.3f"%(obs,pred))
print("    => the step tracks the DENSITY (the NUMBER), with the 5-dimensional exponent.")
print()

# ---- A3: the order is CONFORMAL => scale-free => it CANNOT fix an absolute step
print("A3. Decisive: the order is conformal (scale-invariant), so it fixes only the RATIO, never the step.")
print("    Work in a small patch (S^4 ~ R^4 locally). Scale (t,x) -> (lam t, lam x).")
n=300
tt=rng.uniform(0,1,n); xx=rng.uniform(-1,1,(n,4))
def ordflat(tt,xx):
    dt=tt[None,:]-tt[:,None]
    d=np.linalg.norm(xx[None,:,:]-xx[:,None,:],axis=2)
    return (dt>0)&(dt>d)
O1=ordflat(tt,xx)
for lam in [1e-3,1.0,1e3]:
    O=ordflat(lam*tt,lam*xx)
    step=np.linalg.norm(xx[None,:,:]-xx[:,None,:],axis=2)[np.nonzero(links(O))].mean()*lam
    print("      lam=%7.0e : order identical to lam=1 ? %s   mean link step = %.4e"%(lam,np.array_equal(O,O1),step))
print("    => IDENTICAL ORDER, steps differing by 10^6. The order alone gives NO radian number.")
print()

# ---- A4: so what does supply it? the scale ratio l_B / R_S4 -- an ANCHOR PAIR
print("A4. The step in radians = l / R  (discreteness length over S^4 radius). Both are ANCHORS.")
lP=1.616255e-35            # Planck length; corpus: l_B = Planck length (F64/K258)
sig,fmax=1e-2,156.0
need=sig/fmax
print("    requirement (per tick): step < sigma/f_max = %.3e rad"%need)
print("    step = l_B/R  <  %.3e   <=>   R > %.3e * l_B = %.3e m"%(need,1/need,lP/need))
print("    => satisfied by ANY S^4 radius above ~1e4 Planck lengths (~2.5e-31 m).")
Rh=1.30e26                 # Hubble radius c/H0, the standard identification for the bubble radius
print("    with R = Hubble radius %.2e m:  step = %.3e rad  -> passes by %.1e"%(Rh,lP/Rh,need/(lP/Rh)))
print("    *** PASSES -- but on a SCALE RATIO supplied by two anchors, not by the derived order. ***")
