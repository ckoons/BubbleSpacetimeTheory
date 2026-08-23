import numpy as np, itertools
K=8; lam=np.array([0.0]+[k*(k+5) for k in range(1,K+1)])
def B_of(c,tau):
    w=c*np.exp(-lam*tau); p=w/w.sum(); r=(p*lam).sum()
    return (p*lam**2).sum()/r - r, r
# pre-registered knob space (C7): tau_now in [0.10,0.30]; three c_k profiles; plus c0 weight scan
profs={'equipartition':[1.0]*K,'decreasing':[1.0/k**2 for k in range(1,K+1)],
       'single-mode':[1.0]+[0.0]*(K-1)}
rows=[]
for nm,ck in profs.items():
    for c0 in [0.1,0.3,1.0,3.0,10.0,30.0,100.0]:
        for tau in np.linspace(0.10,0.30,21):
            B,r=B_of(np.array([c0]+ck),tau); rows.append((B,nm,c0,tau,r))
rows.sort()
print("PRE-REGISTERED KNOB SPACE (tau in [0.10,0.30], 3 profiles, c0 in [0.1,100]):")
print(f"  B_min = {rows[0][0]:.3f}   at {rows[0][1]}, c0={rows[0][2]}, tau={rows[0][3]:.2f}")
print(f"  B_max = {rows[-1][0]:.3f}  at {rows[-1][1]}, c0={rows[-1][2]}, tau={rows[-1][3]:.2f}")
print(f"  fraction of scan with B < 6 : {np.mean([r[0]<6 for r in rows]):.1%}")
print(f"  fraction of scan with B < 1 : {np.mean([r[0]<1 for r in rows]):.1%}")
print("\n  lowest 8 corners:")
for B,nm,c0,tau,r in rows[:8]: print(f"    B={B:7.3f}  {nm:<14} c0={c0:<6} tau={tau:.2f}  r={r:.4f}")

# does the observational constraint |w+1|<~0.1 today cut the dangerous corners?
print("\nWith the observational cut |w+1| = (1/3) r tau' <= 0.1 and tau' = kappa/H:")
for tp,lab in [(1.0,"tau'=1 (horizon clock, tau=ln a)"),(0.46,"tau'=0.46")]:
    ok=[x for x in rows if (1/3)*x[4]*tp<=0.1]
    if ok: print(f"   {lab:<34} surviving B_min = {min(o[0] for o in ok):.3f}  ({len(ok)}/{len(rows)} corners survive)")
    else:  print(f"   {lab:<34} no corners survive")
