#!/usr/bin/env python3
"""Toy 5755 — R144 E1: the K1809 sibling test on the three flagged 'derived' rows (m_t/m_b = 42, sin²θ₁₃ = 1/45, λ_H = 1/8).
Menu named in the prereg (56b749a4): products/ratios of <= 3 of {2,3,5,6,7,137}, with and without sqrt. N reported, never the winner.
Targets pinned from PDG 2024 summary-table PDFs (notes/sources_R144/)."""
import itertools, math, json
from fractions import Fraction as F
score=[]; cf=[]
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
V=[2,3,5,6,7,137]; NAMES={2:'rank',3:'N_c',5:'n_C',6:'C_2',7:'g',137:'N_max'}
prods={}
for k in range(0,4):
    for m in itertools.combinations_with_replacement(V,k):
        v=math.prod(m) if m else 1
        prods.setdefault(v,[]).append('·'.join(NAMES[x] for x in m) or '1')
pool={}
for a,na in prods.items():
    for b,nb in prods.items():
        q=F(a,b); lab=f"{na[0]}/{nb[0]}" if b!=1 else na[0]
        for val,tag in ((float(q),lab),(math.sqrt(q),f"√({lab})")):
            key=round(val,12)
            if key not in pool or len(tag)<len(pool[key]): pool[key]=tag
vals=sorted(pool)
print(f"pool: {len(vals)} distinct values (products of <=3 of {{2,3,5,6,7,137}} over the same, with and without sqrt)")
def count(lo,hi): return [(v,pool[v]) for v in vals if lo<=v<=hi]
def chance(T,lo,hi,win):
    nwin=sum(1 for v in vals if T/win<=v<=T*win); return nwin*math.log(hi/lo)/(2*math.log(win))
# ---- targets (PDG 2024, pinned) ----
mt,smt=172.57,0.29; mb,smb=4.183,0.007
R=mt/mb; sR=R*math.hypot(smt/mt,smb/mb)
th,sth=2.19e-2,0.07e-2
mH,smH=125.20,0.11; v=246.22; lam=mH**2/(2*v**2); slam=lam*2*smH/mH
rows=[("m_t/m_b",R,sR,42.0,"C_2·g = 42"),("sin2_th13",th,sth,1/45,"1/(N_c²·n_C) = 1/45"),("lambda_H",lam,slam,0.125,"1/rank³ = 1/8")]
res={}
for nm,T,sT,pub,form in rows:
    tol=abs(pub-T)/T; z=(pub-T)/sT
    print(f"\n{nm}: target {T:.6g} ± {sT:.2g} (PDG 2024); published {form} = {pub:.6g}, {100*tol:.2f} % off, {z:+.1f}σ")
    out={}
    for lab,lo,hi in (("(a) 1σ band",T-sT,T+sT),("(a2) 2σ band",T-2*sT,T+2*sT),("(b) row's own tolerance",T*(1-tol),T*(1+tol))):
        inb=count(lo,hi); ch={w:chance(T,lo,hi,w) for w in (1.5,2,3)}
        print(f"   {lab:26} [{lo:.6g}, {hi:.6g}]: N = {len(inb):2d}   chance = {ch[1.5]:.2f} / {ch[2]:.2f} / {ch[3]:.2f} (windows ×1.5/×2/×3)   surprising: {'YES' if len(inb)>ch[2]+2*math.sqrt(max(ch[2],1e-9)) else 'no'}")
        print("      forms: "+", ".join(f"{t} = {x:.5g}" for x,t in inb[:14])+(" …" if len(inb)>14 else ""))
        out[lab]=(len(inb),ch)
    res[nm]=(out,tol,z)
Nb=lambda nm: res[nm][0]["(b) row's own tolerance"][0]; Na=lambda nm: res[nm][0]["(a) 1σ band"][0]
print()
sc("P1", Nb("m_t/m_b")>=2, True, f"m_t/m_b: N = {Nb('m_t/m_b')} at the row's tolerance; at 1σ N = {Na('m_t/m_b')} and the published 42 sits {res['m_t/m_b'][2]:+.1f}σ outside")
sc("P2", Na("sin2_th13")>=2 and Nb("sin2_th13")>=1, True, f"sin²θ₁₃: N = {Na('sin2_th13')} at 1σ, {Nb('sin2_th13')} at the row's tolerance")
sc("P3", Nb("lambda_H")>=3, True, f"λ_H: N = {Nb('lambda_H')} at the row's tolerance, {Na('lambda_H')} at 1σ")
surp=[(nm,lab) for nm in res for lab,(n,ch) in res[nm][0].items() if n>ch[2]+2*math.sqrt(max(ch[2],1e-9))]
sc("P4", not surp, False, f"density control: surprising rows = {surp if surp else 'none'} — the vocabulary supplies these counts by chance at this class")
print("\nVERDICT by the K1809 rule (N > 1 at the row's own tolerance ⟹ identified), applied mechanically:")
for nm,_,_,_,form in rows:
    print(f"   {nm:10} {form:22}: N(b) = {Nb(nm)}  ->  {'IDENTIFIED (N > 1)' if Nb(nm)>1 else 'stays (N = 1)'}")
print("\nADDENDUM (not predicted): the same counts in K1809's OWN class — Cal's reconstruction: a, √a, a/b, √(a/b), √a/b, a/√b, a·b, 1/(2√a), 1/(2√(a·b)), √(√a/b) over V with repeats")
small={}
for a in V:
    for b in V:
        for val,tag in ((a,f"{NAMES[a]}"),(math.sqrt(a),f"√{NAMES[a]}"),(a/b,f"{NAMES[a]}/{NAMES[b]}"),(math.sqrt(a/b),f"√({NAMES[a]}/{NAMES[b]})"),(math.sqrt(a)/b,f"√{NAMES[a]}/{NAMES[b]}"),(a/math.sqrt(b),f"{NAMES[a]}/√{NAMES[b]}"),(a*b,f"{NAMES[a]}·{NAMES[b]}"),(1/(2*math.sqrt(a)),f"1/(2√{NAMES[a]})"),(1/(2*math.sqrt(a*b)),f"1/(2√({NAMES[a]}·{NAMES[b]}))"),(math.sqrt(math.sqrt(a)/b),f"√(√{NAMES[a]}/{NAMES[b]})")):
            small.setdefault(round(val,12),tag)
sv=sorted(small); print(f"   K1809-class pool: {len(sv)} distinct values (Cal reported 219)")
for nm,T,sT,pub,form in rows:
    tol=res[nm][1]
    for lab,lo,hi in (("1σ",T-sT,T+sT),("row tol",T*(1-tol),T*(1+tol))):
        inb=[(x,small[x]) for x in sv if lo<=x<=hi]
        print(f"   {nm:10} {lab:8}: N = {len(inb)}  {[t for _,t in inb]}   (published form {'IN' if any(abs(x-pub)<1e-9 for x,_ in inb) else 'NOT IN'} this pool's band)")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({nm:{"target":T,"sigma":sT,"published":pub,"tol":res[nm][1],"z":res[nm][2],"counts":{k:v[0] for k,v in res[nm][0].items()},"chance_x2":{k:v[1][2] for k,v in res[nm][0].items()}} for nm,T,sT,pub,form in rows}|{"pool_size":len(vals)},open(".record_5755.json","w"),indent=1)
