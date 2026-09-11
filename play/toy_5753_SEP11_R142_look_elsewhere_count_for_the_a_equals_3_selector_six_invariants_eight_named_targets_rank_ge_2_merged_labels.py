#!/usr/bin/env python3
"""Toy 5753 — R142 item 4: the look-elsewhere count for the a = 3 selector. Menu named in the prereg (37ba3ff9): 6 root-data invariants x 8 measured
integers over the rank >= 2 classification with isomorphic labels merged; singleton pairs at cap 30 and cap 400."""
import json
score=[]; cf=[]
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
def fams(cap):
    out=[]
    for p in range(2,60):                                  # type I_{p,q}, p<=q, rank p, (a,b) = (2, q-p)
        for q in range(p,cap+1):
            if p*q<=cap: out.append((f"I_{{{p},{q}}}",p,2,q-p))
    for m in range(4,60):                                  # type II_m, rank floor(m/2), a = 4, b = 0/2
        if m*(m-1)//2<=cap: out.append((f"II_{m}",m//2,4,0 if m%2==0 else 2))
    for m in range(2,60):                                  # type III_m, rank m, (a,b) = (1,0)
        if m*(m+1)//2<=cap: out.append((f"III_{m}",m,1,0))
    for m in range(3,cap+1): out.append((f"IV_{m}",2,m-2,0))   # type IV_m, rank 2, (a,b) = (m-2, 0)
    if 16<=cap: out.append(("V(E6)",2,6,4))
    if 27<=cap: out.append(("VI(E7)",3,8,0))
    merged={"III_2":"IV_3","I_{2,2}":"IV_4","II_4":"IV_6"}    # low-dimensional coincidences: one domain, two labels
    return [x for x in out if x[0] not in merged]
def inv(r,a,b): return {"rank":r,"a":a,"b":b,"genus":(r-1)*a+b+2,"dim_C":r+a*r*(r-1)//2+b*r,"v":a*(r-1)+b}
INV=["rank","a","b","genus","dim_C","v"]; T=[2,3,4,6,8,12,15,16]
def table(cap):
    FA=fams(cap); FA=[x for x in FA if inv(*x[1:])["dim_C"]<=cap]
    return FA,{(k,t):[n for (n,r,a,b) in FA if inv(r,a,b)[k]==t] for k in INV for t in T}
FA30,H30=table(30); FA400,H400=table(400)
print(f"population: rank >= 2, labels merged — {len(FA30)} domains at dim_C <= 30, {len(FA400)} at dim_C <= 400")
print(f"{'inv \\ target':14}"+"".join(f"{t:>9}" for t in T))
for k in INV:
    row=[]
    for t in T:
        n30=len(H30[(k,t)]); n400=len(H400[(k,t)])
        cell=f"{n30}" if n30!=1 else ("1*" if n400==1 else "1(x)")
        row.append(f"{cell:>9}")
    print(f"{k:14}"+"".join(row))
print("   (1* = singleton at cap 30 that SURVIVES at cap 400; 1(x) = singleton only because of the cap)")
S30=[(k,t) for k in INV for t in T if len(H30[(k,t)])==1]; Sst=[(k,t) for (k,t) in S30 if len(H400[(k,t)])==1]
print(f"\n   N_pairs = {len(INV)*len(T)};  singleton pairs at cap 30: S30 = {len(S30)};  cap-stable singletons: S_stable = {len(Sst)}")
for (k,t) in Sst: print(f"     {k} = {t:2}  ->  {H30[(k,t)][0]}")
doms=sorted(set(H30[(k,t)][0] for (k,t) in Sst)); print(f"   distinct domains selected by some stable story: {len(doms)} -> {doms}")
print(f"   IV_5's share: selected by {[ (k,t) for (k,t) in Sst if H30[(k,t)][0]=='IV_5']}")
sc("P1", H30[("a",3)]==["IV_5"] and H400[("a",3)]==["IV_5"], True, "a = 3 is a singleton (IV_5) at cap 30 and cap 400, labels merged, rank >= 2")
a_single=[t for t in T if len(H400[("a",t)])==1]
sc("P2", a_single==[3,12,15,16], True, f"within a, the cap-stable singleton targets are {a_single} — every target not in {{1,2,4,6,8}}: 4 of 8")
sc("P3", all(len(H400[(k,t)])!=1 for k in ("rank","b") for t in T), True, "rank and b give no cap-stable singleton at any target")
others=[(k,t) for (k,t) in Sst if k in ("genus","dim_C","v")]
sc("P4", True, False, f"genus / dim_C / v stable singletons: {[(k,t,H30[(k,t)][0]) for (k,t) in others]}")
print("\n   CONTROL — the invariant a against EVERY integer 2..30 (29 targets), cap 400:")
FAc=[x for x in fams(400)]; a_all={t:[n for (n,r,a,b) in FAc if a==t] for t in range(2,31)}
sing=[t for t in range(2,31) if len(a_all[t])==1]; nons=[t for t in range(2,31) if len(a_all[t])!=1]
print(f"   singleton at {len(sing)} of 29 targets; NOT singleton at {nons} -> {[ (t,a_all[t][:4]+(['...'] if len(a_all[t])>4 else [])) for t in nons]}")
sc("P5", len(sing)==24 and nons==[2,4,6,8], False, "a = t is a singleton for 24 of 29 integers in 2..30; 3 is not special to the invariant, the invariant is special")
print("\n   the same control for the other five invariants (cap 400, targets 2..30): stable singletons")
for k in ("rank","b","genus","dim_C","v"):
    allk={t:[n for (n,r,a,b) in FAc if inv(r,a,b)[k]==t] for t in range(2,31)}
    print(f"     {k:6}: {[(t,allk[t][0]) for t in range(2,31) if len(allk[t])==1]}")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({"N_pairs":len(INV)*len(T),"S30":S30,"S_stable":Sst,"domains":doms,"a_singleton_targets":a_single,"control_a_2_30":sing},open(".record_5753.json","w"),indent=1)
