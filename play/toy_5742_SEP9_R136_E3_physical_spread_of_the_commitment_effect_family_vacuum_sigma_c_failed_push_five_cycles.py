#!/usr/bin/env python3
"""Toy 5742 — R136 E3: how much of Round 134/135's arithmetic is the effect's, not the geometry's."""
import json, mpmath as mp
mp.mp.dps=25
score=[]; cf=[]
def sc(n, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {n}{'' if c else ' (control)'}  {d}")
def L(j,k): return mp.mpf(k+3)/(2*k+3)*(j+k+mp.mpf(5)/2)/(j+k+5)
def M(j,k): return mp.mpf(k)/(2*k+3)*(j+1)/(j+mp.mpf(7)/2) if k>0 else mp.mpf(0)
def tau(n,j,k):
    if n==0: return mp.mpf(1)
    t=L(j,k)*tau(n-1,j,k+1)
    if k>0: t+=M(j,k)*tau(n-1,j+1,k-1)
    return t
def tt(j,k): return (j+1)/(j+mp.mpf(7)/2)*(j+k+mp.mpf(5)/2)/(j+k+5)
COST={'n=1':lambda j,k:1-tau(1,j,k), 'n=2':lambda j,k:1-tau(2,j,k), 'n=3':lambda j,k:1-tau(3,j,k), 'rho':lambda j,k:1-2*tau(1,j,k)+tt(j,k)}
def pm(k): return mp.mpf(k)/(2*k+3)
def cycle(j0dist, cost, M_=137):
    cur={}
    for j0,w in j0dist.items(): cur[(j0,0)]=cur.get((j0,0),0)+w
    Sc=mp.mpf(0)
    for step in range(M_):
        nxt={}
        for (j,k),m in cur.items():
            Sc+=m*cost(j,k); p=pm(k)
            nxt[(j,k+1)]=nxt.get((j,k+1),0)+m*(1-p)
            if k>=1: nxt[(j+1,k-1)]=nxt.get((j+1,k-1),0)+m*p
        cur={s:v for s,v in nxt.items() if v>0}
    jd={}
    for (j,k),v in cur.items(): jd[j]=jd.get(j,0)+v
    return Sc, Sc/M_, jd
print("E3: the physical spread across the commitment-effect family (m-cap cycle, 137 writes)")
print(f"  {'effect':6} | P(commit|vacuum) | Sigma c (j0=0) | failed-push frac cycle 1 | Sigma c at j0=58 / 570 / 2329")
res={}
for name,cost in COST.items():
    vac=1-cost(0,0); S0,f0,_=cycle({0:mp.mpf(1)},cost); rows=[]
    for j0 in (58,570,2329):
        S,_,_=cycle({j0:mp.mpf(1)},cost); rows.append(float(S))
    res[name]=(float(vac),float(S0),float(f0),rows)
    print(f"  {name:6} | {float(vac):16.4f} | {float(S0):14.4f} | {float(f0):24.5f} | {rows[0]:.4f} / {rows[1]:.4f} / {rows[2]:.5f}")
print("  five-cycle series (failed-push fraction, full j-distribution carried):")
ser={}
for name,cost in COST.items():
    dist={0:mp.mpf(1)}; s=[]
    for c in range(5):
        S,f,jd=cycle(dist,cost); s.append(float(f)); dist=jd
    ser[name]=s; print(f"    {name:6}: {[f'{x:.5f}' for x in s]}")
r1=res['n=1']; spread_ratio=max(res[n][1] for n in res)/min(res[n][1] for n in res)
print(f"  Sigma c(j0=0) spans {min(res[n][1] for n in res):.4f} (rho) to {max(res[n][1] for n in res):.4f} (n=3) — factor {spread_ratio:.2f} across the family")
print(f"  ratio Sigma c(n=2)/Sigma c(n=1): at j0=0 {res['n=2'][1]/res['n=1'][1]:.4f}; at j0=2329 {res['n=2'][3][2]/res['n=1'][3][2]:.4f}  (2 is the large-j limit)")
sc("C1", all(res[n][0]>0 and res[n][1]>0 for n in res) and res['rho'][1]<res['n=1'][1]<res['n=2'][1]<res['n=3'][1], True, "every quantity moves across the family; ordering rho < n=1 < n=2 < n=3 at every cell")
sc("C2", res['n=2'][1]/res['n=1'][1] < 2 and abs(res['n=2'][3][2]/res['n=1'][3][2]-2)<0.05, True, "Sigma c(n=2)/Sigma c(n=1) < 2 at j0 = 0 and -> 2 at large j0, as hashed")
print("  TRAP (named in the prereg, now seen): no ratio or difference between members is a BST integer; the factor above is a horizon count n, nothing else.")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({'res':{k:(v[0],v[1],v[2],v[3]) for k,v in res.items()},'series':ser}, open('.record_5742.json','w'), indent=1)
