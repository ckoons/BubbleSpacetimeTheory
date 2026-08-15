import numpy as np
rng=np.random.default_rng(1570)
tick=1.0; T,X=300.0,300.0
def S(t,x,v,npairs=300000):
    g=1/np.sqrt(1-v*v)
    i=rng.integers(0,t.size,npairs); j=rng.integers(0,t.size,npairs)
    return abs(np.mean(np.exp(2j*np.pi*g*((t[j]-t[i])-v*(x[j]-x[i]))/tick)))
def ensemble(sigma_v,nobs=400):
    ts=[];xs=[]
    for _ in range(nobs):
        v0=np.tanh(rng.normal(0,sigma_v)) if sigma_v>0 else 0.0
        g=1/np.sqrt(1-v0*v0); n=max(2,int(T/(g*tick)))
        tau=np.arange(n)*tick
        ts.append(g*tau); xs.append(rng.uniform(0,X)+v0*g*tau)
    return np.concatenate(ts),np.concatenate(xs)
print("="*90)
print("T2564 SAYS 'commit-energy = time function/foliation, boosts = re-foliations'. Does that reading")
print("DELIVER Lorentz safety by itself?  The distinction that matters is ONE foliation or MANY.")
print("="*90)
print("  A re-foliation is a change of DESCRIPTION -- it cannot un-layer a layered EVENT SET. So the")
print("  question is whether the commits share ONE global foliation or carry one each. I sweep the")
print("  spread of observer velocities and watch the preferred-frame signal S(0).\n")
print("     velocity spread sigma_v      S(0)  (1 = a preferred frame; ~0 = Lorentz-safe)")
for s in [0.0,0.001,0.003,0.01,0.03,0.1,0.3,0.8]:
    t,x=ensemble(s)
    print("            %.3f                    %.4f"%(s,S(t,x,0.0)))
print()
print("  ⟹ 'boosts = re-foliations' is CONSISTENT with safety but does NOT deliver it. Safety needs a")
print("     genuine SPREAD of observer velocities: at sigma_v = 0 (all observers comoving) the event")
print("     set is a single global layering and S(0) = 1 -- the violation is back at full strength.")
print("  ⟹ the condition is a statement about the MATTER CONTENT (no privileged observer velocity),")
print("     not about the geometry -- i.e. it reduces to the SAME Machian input as T2565.")
