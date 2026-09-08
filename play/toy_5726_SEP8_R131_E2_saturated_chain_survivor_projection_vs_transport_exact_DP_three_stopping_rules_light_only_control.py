#!/usr/bin/env python3
"""Toy 5726 — E2: the 3/7 chain to saturation; survivor under orthogonal projection (A) and K1860 transport (B)."""
import math, json
from fractions import Fraction as F
import mpmath as mp
mp.mp.dps=40
score=[]; cf=[]
def sc(n, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {n}{'' if c else ' (control)'}  {d}")
def pm(k, matter_on=True): return mp.mpf(k)/(2*k+3) if matter_on else mp.mpf(0)
def run_kcap(kmax, matter_on=True, jmax=20000):
    """distribution of j at first hitting of k = kmax; DP over k for each step is unbounded, so iterate by 'j-layers': state (j,k) with k<kmax; transitions light: (j,k+1), matter: (j+1,k-1)."""
    # process states in order of j (j never decreases); within fixed j, k increases only by light moves, so sweep k upward.
    cur = {0: mp.mpf(1)}  # mass at (j=current, k) for k<kmax, before propagating light moves
    out = {}
    for j in range(jmax+1):
        nxt = {}
        # propagate light moves upward within this j-layer
        layer = dict(cur)
        for k in range(0, kmax):
            if k not in layer: continue
            m = layer[k]
            if m == 0: continue
            if k+1 == kmax: out[j] = out.get(j, mp.mpf(0)) + m*(1-pm(k,matter_on))
            else: layer[k+1] = layer.get(k+1, mp.mpf(0)) + m*(1-pm(k,matter_on))
            if k>=1: nxt[k-1] = nxt.get(k-1, mp.mpf(0)) + m*pm(k,matter_on)
        cur = nxt
        if sum(cur.values()) < mp.mpf(10)**-30: break
    return out
def run_mcap(M, matter_on=True):
    cur={(0,0): mp.mpf(1)}
    for step in range(M):
        nxt={}
        for (j,k),m in cur.items():
            p=pm(k,matter_on); nxt[(j,k+1)] = nxt.get((j,k+1), mp.mpf(0)) + m*(1-p)
            if k>=1: nxt[(j+1,k-1)] = nxt.get((j+1,k-1), mp.mpf(0)) + m*p
        cur={s:m for s,m in nxt.items() if m>0}
    return cur
def entropy(d):
    tot=sum(d.values()); return float(-sum((v/tot)*mp.log(v/tot,2) for v in d.values() if v>0)), float(tot)
print("P0: light-only control (matter off)")
c1=run_kcap(68, False); c2=run_mcap(137, False)
jc2={}; 
for (j,k),m in c2.items(): jc2[j]=jc2.get(j,0)+m
e1,_=entropy(c1); e2,_=entropy(jc2)
print(f"  S-k68: j-dist {dict((j,float(v)) for j,v in c1.items())}, entropy {e1}; S-m137: j-dist keys {list(jc2)}, entropy {e2}")
sc("P0", set(c1)=={0} and set(jc2)=={0} and e1==0 and e2==0, True, "vacuum only, entropy 0, both stopping rules")
print("P1: orthogonal projection onto C[z.z] at the reset")
d137=run_mcap(137)
pk0=sum(m for (j,k),m in d137.items() if k==0)
print(f"  S-k68/S-k137: reset fires at k=k_max>0 -> projection onto k=0 is identically zero (exact by construction). S-m137: P(k=0 at m=137) = {float(pk0)} (m odd => k odd)")
sc("P1", pk0==0, True, "survivor under (A) is the zero vector for all three stopping rules")
print("P2: transport (j,k)->(j,0): winding spectra")
res={}
for name,dist in [("S-k68", run_kcap(68)), ("S-k137", run_kcap(137))]:
    H,tot=entropy(dist); Ej=float(sum(j*v for j,v in dist.items())/tot); pgt=float(sum(v for j,v in dist.items() if j>68)/tot)
    res[name]=(H,Ej,pgt,tot); print(f"  {name}: mass {tot:.15f}, E[j] = {Ej:.1f}, P(j>68) = {pgt:.6f}, H(j) = {H:.3f} bits")
jm={}
for (j,k),m in d137.items(): jm[j]=jm.get(j,0)+m
H,tot=entropy(jm); Ej=float(sum(j*v for j,v in jm.items())/tot); res["S-m137"]=(H,Ej,0.0,tot)
print(f"  S-m137: mass {tot:.15f}, E[j] = {Ej:.2f}, max j = {max(jm)}, H(j) = {H:.3f} bits")
ok2 = (3<=res["S-m137"][0]<=6) and (500<=res["S-k137"][1]<=5000) and res["S-k137"][2]>0.99 and (8<=res["S-k137"][0]<=14) and (100<=res["S-k68"][1]<=1500)
sc("P2", ok2, True, "hashed ranges")
cap0=math.log2(69)
print(f"P3: occupancy vs capacity: log2(69) = {cap0:.2f} bits; S-m137 H = {res['S-m137'][0]:.2f}; S-k68 H = {res['S-k68'][0]:.2f}; S-k137 H = {res['S-k137'][0]:.2f}; R2 = 483; T1292 = 1e4")
sc("P3", res['S-m137'][0] <= cap0 and res['S-k137'][0] < 483, False, "")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({k:[float(x) for x in v] for k,v in res.items()}, open('.record_5726.json','w'), indent=1)
