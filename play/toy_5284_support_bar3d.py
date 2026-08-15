import numpy as np
rng=np.random.default_rng(99)
tick=1.0
def S(t,x,v,npairs=200000):
    g=1/np.sqrt(1-v*v)
    i=rng.integers(0,t.size,npairs); j=rng.integers(0,t.size,npairs)
    dtp=g*((t[j]-t[i])-v*(x[j]-x[i]))
    return abs(np.mean(np.exp(2j*np.pi*dtp/tick)))
print("(A) HOW SHARPLY IS THE PREFERRED FRAME LOCATED?  Width of the S(v) peak vs region size.")
print("    (phase smears when v*Dx ~ tick, so the width should go like tick/X -- it gets SHARPER)")
print("      region X     v at which S drops below 0.5      predicted tick/X")
for X in [50,100,300,1000]:
    T=X; layers=np.arange(0,T,tick)
    t=rng.choice(layers,40000); x=rng.uniform(0,X,40000)
    vs=np.logspace(-5,-1,60); w=None
    for v in vs:
        if S(t,x,v,60000)<0.5: w=v; break
    print("      %6d          %.2e                     %.2e"%(X,w if w else np.nan,tick/X))
print("    ⟹ a BIGGER region locates the preferred frame MORE sharply. The violation does not wash")
print("       out at large scales -- it becomes easier to see. That is the BHS point, quantified.\n")
print("(B) THE ESCAPE ROUTE: a PER-WORLDLINE PROPER-TIME tick (local), not a global layering.")
print("    Each observer commits every tick of ITS OWN proper time; velocities spread over the ensemble.")
T,X=300.0,300.0
ts=[];xs=[]
for _ in range(400):
    v0=np.tanh(rng.normal(0,0.8))                 # a spread of worldline velocities
    g=1/np.sqrt(1-v0*v0)
    n=int(T/(g*tick))
    tau=np.arange(n)*tick
    x0=rng.uniform(0,X)
    ts.append(g*tau); xs.append(x0+v0*g*tau)
t=np.concatenate(ts); x=np.concatenate(xs)
print("      v        S(v)  (a preferred frame would show as a peak)")
for v in [0.0,0.02,0.1,0.3,0.6]:
    print("   %5.2f       %.4f"%(v,S(t,x,v)))
print("    ⟹ NO peak: proper-time ticking along worldlines is Lorentz-COVARIANT -- each observer has")
print("       its own clock, and no global layer exists to pick out a frame.")
