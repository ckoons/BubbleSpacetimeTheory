#!/usr/bin/env python3
import json, math
from fractions import Fraction as F
import mpmath as mp
mp.mp.dps=30
score=[]; cf=[]
def sc(n, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {n}{'' if c else ' (control)'}  {d}")
def cform(j,k): return 1 - mp.mpf(k+3)/(2*k+3)*(j+k+mp.mpf(5)/2)/(j+k+5) - mp.mpf(k)/(2*k+3)*(j+1)/(j+mp.mpf(7)/2)
def pm(k): return mp.mpf(k)/(2*k+3)
def run_m(j0dist, M=137):
    """chain from (j0,0), M writes; returns (Σc expectation, final j-distribution absolute, H(Δj), P(word=(1,1) after 3), ...)"""
    cur={}; 
    for j0,w in j0dist.items(): cur[(j0,0,j0)]=cur.get((j0,0,j0),0)+w    # (j,k,j0)
    tot=mp.mpf(0); p11=None
    for step in range(M):
        nxt={}
        for (j,k,j0),m in cur.items():
            tot+=m*cform(j,k); p=pm(k)
            nxt[(j,k+1,j0)]=nxt.get((j,k+1,j0),0)+m*(1-p)
            if k>=1: nxt[(j+1,k-1,j0)]=nxt.get((j+1,k-1,j0),0)+m*p
        cur={s:v for s,v in nxt.items() if v>0}
        if step==2: p11=sum(v for (j,k,j0),v in cur.items() if (j-j0,k)==(1,1))
    dj={}
    for (j,k,j0),v in cur.items(): dj[j-j0]=dj.get(j-j0,0)+v
    H=-sum(v*mp.log(v,2) for v in dj.values()); jd={}
    for (j,k,j0),v in cur.items(): jd[j]=jd.get(j,0)+v
    return tot,jd,H,p11
def run_k(j0dist, kmax, jmax=20000):
    cur={}
    for j0,w in j0dist.items(): cur[(0,j0)]=cur.get((0,j0),0)+w   # (k, j0) at Δj layer
    tot=mp.mpf(0); out={}; dj={}
    for dj_ in range(jmax+1):
        nxt={}; layer=dict(cur)
        for k in range(0,kmax):
            for (kk,j0),m in list(layer.items()):
                if kk!=k or m==0: continue
                tot+=m*cform(j0+dj_,k); p=pm(k)
                if k+1==kmax: out[(dj_,j0)]=out.get((dj_,j0),0)+m*(1-p)
                else: layer[(k+1,j0)]=layer.get((k+1,j0),0)+m*(1-p)
                if k>=1: nxt[(k-1,j0)]=nxt.get((k-1,j0),0)+m*p
        cur=nxt
        if sum(cur.values())<mp.mpf(10)**-25: break
    for (d,j0),v in out.items(): dj[d]=dj.get(d,0)+v
    H=-sum(v*mp.log(v,2) for v in dj.values()); jd={}
    for (d,j0),v in out.items(): jd[d+j0]=jd.get(d+j0,0)+v
    return tot,jd,H,None
print("E2: Σc(j0) at j0 = 0, 58, 570, 2329, three stopping rules")
res={}
for name,fn in [("m137",lambda d: run_m(d,137)),("k68",lambda d: run_k(d,68)),("k137",lambda d: run_k(d,137))]:
    row={}
    for j0 in (0,58,570,2329):
        tot,jd,H,p11=fn({j0:mp.mpf(1)}); Nw=137 if name=="m137" else float(sum((j-j0)*v for j,v in jd.items()))*2+int(name[1:])
        row[j0]=(float(tot),Nw); print(f"  {name}: j0={j0}: Σc = {float(tot):.5f}   (writes ≈ {Nw:.0f}; 5/2·N/j0 = {2.5*Nw/j0 if j0 else float('nan'):.5f})")
    res[name]=row
q1=all(res[n][0]>res[n][58]>res[n][570]>res[n][2329] for n in res) and abs(res["m137"][2329][0]/(2.5*137/2329)-1)<0.10
sc("Q1", q1, True, f"monotone decreasing; m-cap at j0=2329: {res['m137'][2329][0]:.5f} vs 5/2·137/2329 = {2.5*137/2329:.5f}")
print("E2: five successive cycles (m-cap, full j-distribution carried)")
dist={0:mp.mpf(1)}; sig=[]
for c in range(1,6):
    tot,jd,H,p11=run_m(dist,137); sig.append(float(tot)); ej=float(sum(j*v for j,v in jd.items())); print(f"  cycle {c}: E[j0] = {float(sum(j*v for j,v in dist.items())):.2f} -> Σc = {float(tot):.5f}; E[j] at end = {ej:.2f}; H(Δj) = {float(H):.4f}"); dist=jd
d=[sig[i+1]-sig[i] for i in range(4)]
sc("Q2", all(x<0 for x in d) and all(abs(d[i+1])<abs(d[i]) for i in range(3)), False, f"drifts {[f'{x:.4f}' for x in d]} — ratio cycle2/cycle1 = {sig[1]/sig[0]:.4f} (refused as an integer)")
print("E3: blindness control")
a=run_m({0:mp.mpf(1)},137); b=run_m({2329:mp.mpf(1)},137)
print(f"  H(Δj): {mp.nstr(a[2],20)} vs {mp.nstr(b[2],20)};  P(3-write word=(1,1)): {mp.nstr(a[3],20)} vs {mp.nstr(b[3],20)} (3/7 = {mp.nstr(mp.mpf(3)/7,20)})")
sc("E3", a[2]==b[2] and a[3]==b[3] and abs(a[3]-mp.mpf(3)/7)<mp.mpf(10)**-25, False, "identical to the digit; cannot fail")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({'sigma':{n:{str(j):v for j,v in r.items()} for n,r in res.items()},'cycles':sig}, open('.record_5736.json','w'), indent=1)
