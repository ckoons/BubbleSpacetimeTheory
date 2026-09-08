#!/usr/bin/env python3
import os, json, time
from fractions import Fraction as F
import sympy as sp
src=open([f for f in os.listdir('.') if f.startswith('toy_5722_')][0]).read(); exec(src.split('t0 = time.time()')[0])
score=[]; cf=[]
def sc(n, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {n}{'' if c else ' (control)'}  {d}")
def cform(j,k):
    j=F(j); k=F(k); return 1 - F(k+3,2*k+3)*(j+k+F(5,2))/(j+k+5) - F(k,2*k+3)*(j+1)/(j+F(7,2))
known={(0,0):F(1,2),(0,1):F(10,21),(0,2):F(45,98),(0,3):F(25,56),(1,0):F(5,12),(1,1):F(25,63),(1,2):F(55,144),(1,3):F(10,27),(2,0):F(5,14),(2,1):F(15,44),(2,2):F(65,198),(2,3):F(7,22)}
sc("P1", all(cform(j,k)==v for (j,k),v in known.items()), False, "twelve Round 130 rationals reproduced by the closed form")
t0=time.time(); new=[(3,0),(4,0),(3,1),(3,2),(0,4),(1,4),(2,3),(0,5)]; ok=True
for (j,k) in new:
    g=cost(5,j,k); f=cform(j,k); ok&=(g==f); print(f"  ({j},{k}) m={2*j+k}: Gram {g}  closed form {f}  {'=' if g==f else '≠'}   [{time.time()-t0:.0f}s]")
sc("P2", ok, True, "kernel-Gram at eight unseen cells equals the closed form exactly")
k0=[cform(j,0)==F(5,2*(j+5)) for j in range(0,3000)]
print("  k=0 line: c(j,0) = 5/(2(j+5)) for j=0..2999:", all(k0))
for j in (58,570,2329):
    print(f"  j={j}: c(j,0) = {cform(j,0)} = {float(cform(j,0)):.6f};  c(j,1) = {float(cform(j,1)):.6f};  c(j,2) = {float(cform(j,2)):.6f};  5/(2j) = {2.5/j:.6f}")
sc("P3", all(k0), False, "Keeper's guess is the exact k = 0 line")
asym=all(abs(float(cform(10**6,k))*10**6/2.5 - 1) < 1e-4 for k in range(0,6)); largek=[sp.nsimplify(sp.limit(1 - sp.Rational(1,2)*(1) - sp.Rational(1,2)*(sp.Integer(j)+1)/(sp.Integer(j)+sp.Rational(7,2)), sp.Symbol('x'), 0)) for j in range(3)]
print("  j*c(j,k)/(5/2) at j=1e6, k=0..5:", [f"{float(cform(10**6,k))*10**6/2.5:.6f}" for k in range(6)], "; large-k line (5/4)/(j+7/2) at j=0,1,2:", [str(F(5,4)/(F(j)+F(7,2))) for j in range(3)], "check:", [str(1-F(1,2)-F(1,2)*(F(j)+1)/(F(j)+F(7,2))) for j in range(3)])
sc("P4", asym, False, "leading 5/(2j) for every k")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({f"{j},{k}":str(cform(j,k)) for j in (0,1,2,3,4,5,6,7,8,9,10,58,570,2329) for k in range(4)}, open('.record_5735.json','w'), indent=1)
