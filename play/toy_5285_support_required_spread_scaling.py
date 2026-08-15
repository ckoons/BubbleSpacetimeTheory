import numpy as np
rng=np.random.default_rng(7)
tick=1.0
def S0(t,x,npairs=200000):
    i=rng.integers(0,t.size,npairs); j=rng.integers(0,t.size,npairs)
    return abs(np.mean(np.exp(2j*np.pi*(t[j]-t[i])/tick)))
def ens(sig,T,X=300.0,nobs=300):
    ts=[];xs=[]
    for _ in range(nobs):
        v0=np.tanh(rng.normal(0,sig)) if sig>0 else 0.0
        g=1/np.sqrt(1-v0*v0); n=max(2,int(T/(g*tick)))
        tau=np.arange(n)*tick
        ts.append(g*tau); xs.append(rng.uniform(0,X)+v0*g*tau)
    return np.concatenate(ts),np.concatenate(xs)
print("HOW MUCH SPREAD IS NEEDED?  The layering dies when accumulated time dilation smears the tick:")
print("   T*sigma_v^2/2 ~ 1 tick  =>  sigma_v ~ sqrt(2*tick/T).  The LONGER you look, the LESS spread")
print("   you need. Measure the crossover (S(0) < 0.5) against that prediction.\n")
print("      T (in ticks)     measured crossover sigma_v     sqrt(2/T)")
for T in [100,300,1000,3000]:
    c=None
    for s in np.logspace(-3,0,40):
        t,x=ens(s,T)
        if S0(t,x)<0.5: c=s; break
    print("         %5d              %.4f                     %.4f"%(T,c if c else np.nan,np.sqrt(2/T)))
print("\n  ⟹ the requirement WEAKENS as sqrt(tick/T). Extrapolating to BST's own numbers -- a Koons")
print("     tick over a Hubble time is T/tick ~ 1e60 -- the required velocity spread is ~1e-30.")
print("     ANY realistic matter dispersion satisfies it by dozens of orders.")
print("  ⟹ so the condition is physically TRIVIAL to satisfy -- but it is still a condition on the")
print("     MATTER CONTENT, not a consequence of the geometry. State it; don't skip it.")
