#!/usr/bin/env python3
"""Toy 5740 — R136 E1: the commitment-effect family |z|^{2n}, exact, by the Schur recursion; validated on the kernel Gram."""
import os, time, json, itertools, math
from fractions import Fraction as F
import sympy as sp
src=open([f for f in os.listdir('.') if f.startswith('toy_5722_')][0]).read(); exec(src.split('t0 = time.time()')[0])
score=[]; cf=[]
def sc(n, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {n}{'' if c else ' (control)'}  {d}")
def L(j,k): j=F(j); k=F(k); return F(k+3,2*k+3)*(j+k+F(5,2))/(j+k+5)
def M(j,k): j=F(j); k=F(k); return F(k,2*k+3)*(j+1)/(j+F(7,2)) if k>0 else F(0)
def tau(n,j,k):
    if n==0: return F(1)
    t=L(j,k)*tau(n-1,j,k+1)
    if k>0: t+=M(j,k)*tau(n-1,j+1,k-1)
    return t
def cn(n,j,k): return 1-tau(n,j,k)
print("A1: n = 1 returns Round 130's twelve rationals")
known={(0,0):F(1,2),(0,1):F(10,21),(0,2):F(45,98),(0,3):F(25,56),(1,0):F(5,12),(1,1):F(25,63),(1,2):F(55,144),(1,3):F(10,27),(2,0):F(5,14),(2,1):F(15,44),(2,2):F(65,198),(2,3):F(7,22)}
sc("A1", all(cn(1,j,k)==v for (j,k),v in known.items()), False, "12/12 exact")
print("A2: independent route — <|z|^4> from the exact kernel Gram, no recursion")
zs=sp.symbols('z0:5'); zz=sum(v**2 for v in zs); t0=time.time(); ok2=True
for (j,k) in [(0,0),(1,0),(0,1),(1,1),(0,2)]:
    m=2*j+k; psi=sp.expand(zz**j*harmonic_part(zs[0]**k,k,zs)); pd=poly_dict(psi,zs); N0=norm2(pd,5,m); tot=F(0)
    for al in [e for e in itertools.product(range(3),repeat=5) if sum(e)==2]:
        coef=F(math.factorial(2)//math.prod(math.factorial(a) for a in al))
        mon=sp.Mul(*[v**a for v,a in zip(zs,al)])
        tot+=coef*norm2(poly_dict(sp.expand(mon*psi),zs),5,m+2)
    gram_val=tot/N0; rec=tau(2,j,k); ok2 &= (gram_val==rec)
    print(f"  ({j},{k}): Gram <|z|^4> = {gram_val} ;  recursion = {rec}  {'=' if gram_val==rec else '≠'}   [{time.time()-t0:.0f}s]")
sc("A2", ok2, False, "recursion validated on an instrument sharing none of its steps")
print("A3: Keeper's K1885-PRE columns, exact")
print("   j |    1-<|z|^2>    |    1-<|z|^4>    |    1-<|z|^6>     (K1885-PRE MC: 0.4997/0.7378/0.8569 at j=0)")
for j in range(4):
    r=[cn(n,j,0) for n in (1,2,3)]; print(f"   {j} | {str(r[0]):>9} {float(r[0]):.4f} | {str(r[1]):>9} {float(r[1]):.4f} | {str(r[2]):>9} {float(r[2]):.4f}")
mc={(1,0):0.4997,(2,0):0.7378,(3,0):0.8569,(1,1):0.4160,(2,1):0.6473,(3,1):0.7804,(1,2):0.3562,(2,2):0.5751,(3,2):0.7130,(1,3):0.3114,(2,3):0.5167,(3,3):0.6546}
dev=max(abs(float(cn(n,j,0))-v) for (n,j),v in mc.items())
sc("A3", cn(2,0,0)==F(31,42) and cn(3,0,0)==F(6,7) and dev<0.002, True, f"c2(0,0) = 31/42, c3(0,0) = 6/7; max deviation from Keeper's MC = {dev:.4f}")
print("A4: vacuum commitment probability across the family, and the k = 0 lines")
vac=[tau(n,0,0) for n in range(1,7)]; print("  P(commit | vacuum), n = 1..6:", [f"{str(v)} = {float(v):.4f}" for v in vac])
for n in (1,2,3):
    line=[cn(n,j,0) for j in range(6)]; print(f"  n={n}: c_n(j,0), j=0..5: {[str(x) for x in line]}")
sc("A4", vac[0]==F(1,2) and vac[1]==F(11,42) and vac[2]==F(1,7), False, "1/2, 11/42, 1/7 as hashed")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({'vac':[str(v) for v in vac],'cols':{f"{n},{j}":str(cn(n,j,0)) for n in (1,2,3) for j in range(6)}}, open('.record_5740.json','w'), indent=1)
