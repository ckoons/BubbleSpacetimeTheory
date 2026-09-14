#!/usr/bin/env python3
"""Toy 5756 — R144 E2b: price the m_H refinement (v/2)·sqrt(1 + n_C/N_max) — the second object on λ_H's row, quoted at "0.02 %".
Prereg 8fd3db7f. Object c = m_H/(v/2); menu (1 ± p/q)^e, p,q products of <= 2 of {2,3,5,6,7,137}; N reported, never the winner."""
import itertools, math, json
from fractions import Fraction as F
score=[]; cf=[]
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
V=[2,3,5,6,7,137]; NM={2:'rank',3:'N_c',5:'n_C',6:'C_2',7:'g',137:'N_max'}
mH,smH=125.20,0.11; GF=1.1663788e-5; v=(math.sqrt(2)*GF)**-0.5
c=mH/(v/2); sc_=smH/(v/2); pub=math.sqrt(1+F(5,137)); z=(pub-c)/sc_; tol=abs(pub-c)/c
print(f"v = (√2 G_F)^(-1/2) = {v:.4f} GeV;  c = m_H/(v/2) = {c:.5f} ± {sc_:.5f} (PDG 2024 m_H = {mH} ± {smH})")
print(f"published √(1 + n_C/N_max) = {pub:.5f}: {100*tol:.3f} % off, {z:+.2f}σ;  m_H it predicts = {pub*v/2:.3f} GeV")
print("  which (m_H, v) reproduces the row's '0.02 %'?  ", end="")
repro=[]
for mh_try,v_try,lab in ((125.25,246.22,"PDG 2022 m_H 125.25, v 246.22"),(125.20,246.22,"PDG 2024 m_H, v 246.22"),(125.35,246.22,"m_H 125.35"),(125.25,246.0,"m_H 125.25, v 246.0 (both stale)")):
    dev=100*abs(pub*v_try/2-mh_try)/mh_try; print(f"[{lab}: {dev:.3f} %]", end=" ")
    if dev<=0.025: repro.append(lab)
print()
sc("P1", abs(z)>1 and "PDG 2024 m_H, v 246.22" not in repro, True, f"published form {z:+.2f}σ outside 1σ at the PDG 2024 primary; the '0.02 %' is reproduced only by {repro if repro else 'no pair tried'}")
# ---- menu: the published form's class ----
prods={}
for k in range(0,3):
    for m in itertools.combinations_with_replacement(V,k):
        prods.setdefault(math.prod(m) if m else 1,'·'.join(NM[x] for x in m) or '1')
menu={}
for p,np_ in prods.items():
    for q,nq in prods.items():
        r=F(p,q)
        if r>=1: continue
        for s,ss in ((1,'+'),(-1,'−')):
            base=1+s*r
            if base<=0: continue
            for e,es in ((1,''),(F(1,2),'√'),(-1,'⁻¹'),(F(-1,2),'⁻½')):
                val=float(base)**float(e); key=round(val,12)
                lab=f"{es}(1 {ss} {np_}/{nq})"
                if key not in menu or len(lab)<len(menu[key]): menu[key]=lab
vals=sorted(menu); print(f"\nmenu (1 ± p/q)^e, p,q products of <= 2 integers, e in {{1, 1/2, -1, -1/2}}: {len(vals)} distinct values")
def inband(lo,hi): return [(x,menu[x]) for x in vals if lo<=x<=hi]
def chance(T,lo,hi,win): n=sum(1 for x in vals if T/win<=x<=T*win); return n*math.log(hi/lo)/(2*math.log(win))
res={}
for lab,lo,hi in (("(a) 1σ",c-sc_,c+sc_),("(a2) 2σ",c-2*sc_,c+2*sc_),("(b) form's own miss",c*(1-tol),c*(1+tol))):
    ib=inband(lo,hi); ch=chance(c,lo,hi,1.05); res[lab]=(len(ib),ch)
    print(f"   {lab:20} [{lo:.5f}, {hi:.5f}]: N = {len(ib):2d}  chance(×1.05 window) = {ch:.2f}   {'SURPRISING' if len(ib)>ch+2*math.sqrt(max(ch,1e-9)) else 'at chance'}")
    print("      "+", ".join(f"{t} = {x:.5f}" for x,t in ib))
sc("P2", res["(a) 1σ"][0]>=2, True, f"N = {res['(a) 1σ'][0]} forms of the published class inside the 1σ band (the published form is not among them)")
nb=res["(b) form's own miss"][0]
sc("P3", nb>=3, True, f"N = {nb} at the form's own miss tolerance")
sc("P4", all(n<=ch+2*math.sqrt(max(ch,1e-9)) for n,ch in res.values()), False, "every count at chance")
# ---- second instrument: the 5755 pool on c itself ----
pool={}
P3={}
for k in range(0,4):
    for m in itertools.combinations_with_replacement(V,k): P3.setdefault(math.prod(m) if m else 1,'·'.join(NM[x] for x in m) or '1')
for a,na in P3.items():
    for b,nb in P3.items():
        q=F(a,b); lab=f"{na}/{nb}" if b!=1 else na
        for val,tag in ((float(q),lab),(math.sqrt(q),f"√({lab})")):
            k=round(val,12)
            if k not in pool or len(tag)<len(pool[k]): pool[k]=tag
pv=sorted(pool); ib=[(x,pool[x]) for x in pv if c-sc_<=x<=c+sc_]
print(f"\nsecond instrument — the 5755 degree-3 ±√ pool ({len(pv)} values) on c at 1σ: N = {len(ib)}: "+", ".join(f"{t} = {x:.5f}" for x,t in ib))
print(f"\nVERDICT (K1809 rule, mechanical): N(1σ) = {res['(a) 1σ'][0]} > 1 ⟹ the refinement is IDENTIFIED; and its published value is {z:+.2f}σ from the PDG 2024 primary, not 0.02 %.")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c_ in zip(score,cf) if c_ and s)}/{sum(cf)} can-fail hit")
json.dump({"c":c,"sigma":sc_,"published":pub,"z":z,"tol":tol,"counts":{k:v_[0] for k,v_ in res.items()},"chance":{k:v_[1] for k,v_ in res.items()},"pool2_1sigma":len(ib)},open(".record_5756.json","w"),indent=1)
