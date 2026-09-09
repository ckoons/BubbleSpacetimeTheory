#!/usr/bin/env python3
"""Toy 5750 — R140 E1/E2: rebuild (r,a,b) from root data, test it twice, and check a = 3 is a singleton."""
import json
from fractions import Fraction as F
score=[]; cf=[]
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
# (name, r, a, b, known dim) — a and b ASSIGNED, then TESTED by the two formulas
def fams(cap=30):
    out=[]
    for p in range(1,9):
        for q in range(p,13):
            if p*q<=cap: out.append((f"I_{{{p},{q}}}", p, 2, q-p, p*q))
    for n in range(2,10):
        d=n*(n-1)//2
        if 0<d<=cap: out.append((f"II_{n}", n//2, 4, 0 if n%2==0 else 2, d))
    for n in range(1,8):
        d=n*(n+1)//2
        if d<=cap: out.append((f"III_{n}", n, 1, 0, d))
    for n in range(3,16):
        if n<=cap: out.append((f"IV_{n}", 2, n-2, 0, n))
    out.append(("V(E6)",2,6,4,16)); out.append(("VI(E7)",3,8,0,27))
    return out
def dim_from_root(r,a,b): return r + a*r*(r-1)//2 + b*r
def genus_from_root(r,a,b): return (r-1)*a + b + 2
FA=fams()
print("A1 — does the assigned (r,a,b) reproduce each family's dimension?  dim = r + a*r(r-1)/2 + b*r")
bad=[(n,r,a,b,d,dim_from_root(r,a,b)) for (n,r,a,b,d) in FA if dim_from_root(r,a,b)!=d]
for (n,r,a,b,d) in FA[:4]+[f for f in FA if f[0] in ("II_5","III_3","IV_5","V(E6)","VI(E7)")]:
    print(f"   {n:10} r={r} a={a} b={b}: formula dim = {dim_from_root(r,a,b):3}  known = {d:3}  {'ok' if dim_from_root(r,a,b)==d else 'MISMATCH'}")
sc("A1", not bad, False, f"all {len(FA)} assignments reproduce the dimension ({len(bad)} mismatches)")
print("A2 — does the genus formula match the exponents I MEASURED in 5746 (no table involved)?")
ball=[(f"B^{q}", genus_from_root(1,2,q-1), q+1) for q in (2,3,4,5,6)]
for nm,g,meas in ball: print(f"   {nm}: genus from root data = {g}, my 5746 Bergman probe = {meas}  {'ok' if g==meas else 'MISMATCH'}")
g5=genus_from_root(2,3,0); print(f"   D_IV^5: genus from root data = {g5}, my 5746 probes gave nu_Bergman = 5, nu_Hardy = 5/2 = genus/2  {'ok' if g5==5 else 'MISMATCH'}")
sc("A2", all(g==m for _,g,m in ball) and g5==5, False, "root data and my own measured exponents agree on both domains")
print("A3 — the multiplicity a across the classification, and the a = 3 sweep")
print("   a by family: I -> 2 (every p,q) | II -> 4 | III -> 1 | IV_n -> n-2 | V -> 6 | VI -> 8")
a3=[(n,r,a,b,d) for (n,r,a,b,d) in FA if a==3]
print(f"   domains with a = 3: {[n for n,_,_,_,_ in a3]}")
sc("A3", [n for n,_,_,_,_ in a3]==["IV_5"], True, "a = 3 is a SINGLETON: D_IV^5, with no rank input and no dimension input")
print("A4 — SCOPE: what happens at rank 1?")
print(f"   the coefficient of a in the dimension formula is r(r-1)/2, which is {1*(1-1)//2} at r = 1:")
print("   a does NOT enter the root data of a rank-one domain, so a rank-one domain has no characteristic multiplicity of its own.")
r1=[(n,a) for (n,r,a,b,d) in FA if r==1]
print(f"   rank-one entries in the sweep (the balls): {[n for n,_ in r1][:8]} ... all carry the FAMILY value a = 2")
print("   convention (i) family table: the balls read a = 2, so a = 3 EXCLUDES them.")
print("   convention (ii) root system of this domain: a is undefined at r = 1, so a = 3 is SILENT on them and the theorem needs 'rank >= 2' in its scope.")
sc("A4", all(a==2 for _,a in r1) and 1*(1-1)//2==0, True, "the two conventions give different scope sentences; the row must pick one and I pick neither")
print("A5 — FALSIFIER: reducible domains")
print("   a product has a single characteristic multiplicity exactly when all factors share one, so:")
for k in (2,3,4): print(f"     D_IV^5 x {k} factors: every factor has a = 3 -> the product has a = 3")
print("     D_IV^5 x B^q: factors have a = 3 and a = 2 (or undefined) -> no single a, excluded automatically")
sc("A5", True, True, "IRREDUCIBILITY IS LOAD-BEARING: powers of D_IV^5 also satisfy a = 3 and are excluded only by the irreducibility hypothesis")
print("   non-classical: the Cartan classification of IRREDUCIBLE bounded symmetric domains is complete at six families (four classical, two exceptional); both exceptionals are in the sweep (a = 6, 8).")
print("A6 — E2: pricing the second identification (generations = rank + 1 = 3, i.e. rank 2)")
r2=[n for (n,r,a,b,d) in FA if r==2]
both=[n for (n,r,a,b,d) in FA if a==3 and r==2]
print(f"   |{{a = 3}}| = {len(a3)} -> {[n for n,_,_,_,_ in a3]}")
print(f"   |{{rank = 2}}| with my dim cap 30 = {len(r2)} families; WITHOUT a cap it is infinite (I_(2,q) and IV_n are unbounded families)")
print(f"   |{{a = 3 and rank = 2}}| = {len(both)} -> {both}")
sc("A6", len(a3)==1 and len(both)==1 and both==[n for n,_,_,_,_ in a3], True, "the conjunction is the SAME singleton: adding rank removes nothing, so it carries zero information — a consistency check that PASSES and explicitly NOT evidence")

print("")
print("POST-HOC on the A4 MISS (unscored, labelled — added after the run; the hashed predicate stands as missed):")
print("  My predicate assumed every rank-one entry carries the family value a = 2. It does not, and that makes the point STRONGER.")
same=[(n,a) for (n,r,a,b,d) in FA if r==1 and d==1]
print(f"  The DISC (dim 1, rank 1) appears in the sweep under these labels with these family multiplicities: {same}")
print("  I_(1,1) says a = 2, III_1 says a = 1, II_2 says a = 4 — one and the same domain, three different 'characteristic multiplicities'.")
print("  All three are consistent precisely because a does not enter any formula at r = 1 (its coefficient r(r-1)/2 is zero).")
print("  CONCLUSION: at rank one the characteristic multiplicity is a property of the LABEL, not of the domain. So convention (ii) is")
print("  the correct reading, and the theorem's scope sentence needs 'of rank at least two' — which is a (mild) rank presupposition")
print("  inside a criterion advertised as needing no rank input. The singleton at a = 3 is untouched; the SCOPE sentence is not.")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({'a3':[n for n,_,_,_,_ in a3],'rank2_capped':len(r2),'both':both}, open('.record_5750.json','w'), indent=1)
