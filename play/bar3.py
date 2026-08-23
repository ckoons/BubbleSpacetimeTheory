import numpy as np
K=8; lam=np.array([0.0]+[k*(k+5) for k in range(1,K+1)])
def rB(c,tau):
    w=c*np.exp(-lam*tau); p=w/w.sum(); r=(p*lam).sum()
    return r,(p*lam**2).sum()/r-r

# (1) VERIFY the exact identity  tau''/tau'^2 = v[(3/2)(1+w_tot) - dlnT/dlna],  v = H*T
# build an explicit clock: T(a) = T0 * a^s  (s = dlnT/dlna), LCDM H(a)
Om,OL=0.31,0.69
H=lambda a: np.sqrt(Om*a**-3+OL)                       # units H0=1
def tau_prime(a,T0,s): return 1.0/(H(a)*T0*a**s)       # tau' = kappa/H = 1/(H T)
for T0,s in [(1.0,0.0),(1.0,-1.0),(0.5,2.4),(1e-3,0.0)]:
    a=1.0; h=1e-5; x=np.log(a)
    tp  = tau_prime(np.exp(x),T0,s)
    tpp = (tau_prime(np.exp(x+h),T0,s)-tau_prime(np.exp(x-h),T0,s))/(2*h)   # d tau'/dlna
    num = tpp/tp**2
    wtot=-OL/(Om*a**-3+OL); v=H(a)*T0*a**s
    ana = v*(1.5*(1+wtot)-s)
    print(f"  T0={T0:<6} s={s:<5}  numeric {num: .6f}   analytic {ana: .6f}   match={abs(num-ana)<1e-6}")

# (2) sensitivity of the data-rescue: surviving B_min vs the |w+1| cut
print("\n(2) data-rescue sensitivity  (tau' = 1, horizon-clock normalisation):")
profs={'equi':[1.0]*K,'decr':[1.0/k**2 for k in range(1,K+1)],'single':[1.0]+[0.0]*(K-1)}
rows=[]
for nm,ck in profs.items():
  for c0 in np.geomspace(0.05,300,25):
    for tau in np.linspace(0.10,0.30,21):
        r,B=rB(np.array([c0]+ck),tau); rows.append((B,r))
for cut in (0.30,0.20,0.10,0.05,0.02):
    ok=[B for B,r in rows if (1/3)*r*1.0<=cut]
    print(f"   |w+1| <= {cut:<5} -> surviving B_min = {min(ok):6.3f}   ({len(ok):>4}/{len(rows)} corners)")
print("\n(3) the mechanism: is small B tied to large r?  corr(B, r) over scan =",
      f"{np.corrcoef([x[0] for x in rows],[x[1] for x in rows])[0,1]:+.3f}")
