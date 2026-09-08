#!/usr/bin/env python3
import json, mpmath as mp
mp.mp.dps=25
score=[]; cf=[]
def sc(n, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {n}{'' if c else ' (control)'}  {d}")
def cform(j,k): return 1 - mp.mpf(k+3)/(2*k+3)*(j+k+mp.mpf(5)/2)/(j+k+5) - mp.mpf(k)/(2*k+3)*(j+1)/(j+mp.mpf(7)/2)
def pm(k): return mp.mpf(k)/(2*k+3)
def stats_m(j0dist, M=137, czero=False):
    cur={}
    for j0,w in j0dist.items(): cur[(j0,0)]=cur.get((j0,0),0)+w
    Sc=mp.mpf(0); Sf=mp.mpf(0); Sp=mp.mpf(0)   # Σc, Σ c/(1-c), Σ 1/(1-c)
    for step in range(M):
        nxt={}
        for (j,k),m in cur.items():
            c=mp.mpf(0) if czero else cform(j,k); Sc+=m*c; Sf+=m*c/(1-c); Sp+=m/(1-c); p=pm(k)
            nxt[(j,k+1)]=nxt.get((j,k+1),0)+m*(1-p)
            if k>=1: nxt[(j+1,k-1)]=nxt.get((j+1,k-1),0)+m*p
        cur={s:v for s,v in nxt.items() if v>0}
    jd={}
    for (j,k),v in cur.items(): jd[j]=jd.get(j,0)+v
    return Sc/M, Sf/Sp, Sp/M, jd
def stats_k(j0, kmax, jmax=20000):
    cur={0:mp.mpf(1)}; Sc=Sf=Sp=mp.mpf(0); N=mp.mpf(0)
    for dj in range(jmax+1):
        nxt={}; layer=dict(cur)
        for k in range(0,kmax):
            m=layer.get(k,0)
            if m==0: continue
            c=cform(j0+dj,k); Sc+=m*c; Sf+=m*c/(1-c); Sp+=m/(1-c); N+=m; p=pm(k)
            if k+1<kmax: layer[k+1]=layer.get(k+1,0)+m*(1-p)
            if k>=1: nxt[k-1]=nxt.get(k-1,0)+m*p
        cur=nxt
        if sum(cur.values())<mp.mpf(10)**-22: break
    return Sc/N, Sf/Sp, Sp/N
print("E1 control: c ≡ 0 reproduces the chain (Σ 1/(1-c) per write = 1, failed fraction 0)")
a0,b0,t0,_=stats_m({0:mp.mpf(1)},137,czero=True); print(f"  a0={a0} b0={b0} t0={t0}"); sc("ctrl", a0==0 and b0==0 and abs(t0-1)<mp.mpf(10)**-20, False, "exact")
print("E1: failed-push fraction, (a) mean of c along landed chain | (b) fraction of all pushes failing | turns per commitment 137/(1-c) mean")
res={}
for name in ("m137","k68","k137"):
    row={}
    for j0 in (0,58,570,2329):
        if name=="m137": a,b,t,_=stats_m({j0:mp.mpf(1)},137)
        else: a,b,t=stats_k(j0,int(name[1:]))
        row[j0]=(float(a),float(b),float(137*t)); print(f"  {name} j0={j0}: (a) {float(a):.5f}  (b) {float(b):.5f}  turns/commit {float(137*t):.2f}")
    res[name]=row
mono=all(all(res[n][j][i]>res[n][j2][i] for j,j2 in ((0,58),(58,570),(570,2329)) for i in (0,1)) for n in res)
sc("E1-a", 0.09<=res["m137"][0][0]<=0.13 and mono, True, f"cycle-1 m-cap mean-of-c = {res['m137'][0][0]:.4f} (Keeper 0.1081); monotone {mono}")
sc("E1-b", 0.10<=res["m137"][0][1]<=0.15, True, f"fraction of pushes failing = {res['m137'][0][1]:.4f}")
print("E1: five cycles at the m-cap (full j-distribution carried)")
dist={0:mp.mpf(1)}; ser=[]
for c in range(1,6):
    a,b,t,fin=stats_m(dist,137); ser.append((float(a),float(b))); print(f"  cycle {c}: (a) {float(a):.5f}  (b) {float(b):.5f}  turns/commit {float(137*t):.2f}"); dist=fin
sc("E1-cycles", ser[3][0]>0.005, False, f"cycle 4 = {ser[3][0]:.4f}, not 1e-3")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({'rules':{n:{str(j):v for j,v in r.items()} for n,r in res.items()},'cycles':ser}, open('.record_5737.json','w'), indent=1)
