#!/usr/bin/env python3
"""Toy 5731 — E3: axis ratchet. Zonal weight along xi under aligned vs random-direction writes, exact sphere integration."""
import json, itertools, random
from fractions import Fraction as F
import sympy as sp, numpy as np
score=[]; cf=[]
def sc(n, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {n}{'' if c else ' (control)'}  {d}")
xs=sp.symbols('x0:5'); r2=sum(v**2 for v in xs)
def moment(alpha):
    if any(a%2 for a in alpha): return F(0)
    d=len(alpha); num=sp.gamma(sp.Rational(d,2))*sp.prod([sp.gamma(sp.Rational(a+1,2)) for a in alpha]); den=sp.gamma(sp.Rational(1,2))**d*sp.gamma(sp.Rational(sum(alpha)+d,2)); r=sp.Rational(sp.gammasimp(sp.simplify(num/den))); return F(int(r.p),int(r.q))
MC={}
def ip(p,q):
    P=sp.Poly(sp.expand(p*q),*xs); tot=F(0)
    for m,c in zip(P.monoms(),P.coeffs()):
        key=tuple(int(e) for e in m)
        if key not in MC: MC[key]=moment(key)
        tot+=F(int(c.p),int(c.q))*MC[key]
    return tot
def harmonic_part(poly,k):
    if k<2: return sp.expand(poly)
    mons=[sp.Mul(*[v**e for v,e in zip(xs,ex)]) for ex in itertools.product(range(k-1),repeat=5) if sum(ex)==k-2]
    cs=sp.symbols(f'c0:{len(mons)}'); q=sum(c*mm for c,mm in zip(cs,mons)); lap=lambda f: sum(sp.diff(f,v,2) for v in xs)
    sol=sp.solve(sp.Poly(sp.expand(lap(poly-r2*q)),*xs).coeffs(),cs,dict=True)[0]; return sp.expand(poly-r2*q.subs(sol))
Zc={}
def zonal(k):
    if k not in Zc: Zc[k]=harmonic_part(xs[0]**k,k)
    return Zc[k]
def w(Y,k):
    Z=zonal(k); return ip(Y,Z)**2/(ip(Y,Y)*ip(Z,Z))
print("R1: aligned writes u = xi from Z_2, light and matter branches, 5 steps")
Y=zonal(2); k=2; ok1=True
for s in range(5):
    L=harmonic_part(xs[0]*Y,k+1); M=sp.expand(sp.diff(Y,xs[0]))
    wl=w(L,k+1); wm=w(M,k-1) if k>=1 else F(1)
    ok1 &= (wl==1 and wm==1); Y=L; k+=1
sc("R1", ok1, False, "zonal weight stays exactly 1 on both branches")
print("R2: random-direction writes from Z_2, light path, 6 steps, 24 walks (exact per walk, rational directions)")
random.seed(5731); walks=[]
for t in range(24):
    Y=zonal(2); k=2; path=[]
    for s in range(6):
        u=[random.randint(-3,3) for _ in range(5)]
        if all(v==0 for v in u): u[1]=1
        L=harmonic_part(sum(ui*xi for ui,xi in zip(u,xs))*Y,k+1); Y=L; k+=1; path.append(float(w(Y,k)))
    walks.append(path)
A=np.array(walks); means=A.mean(0); errs=A.std(0)/np.sqrt(len(A))
print("  mean zonal weight after writes 1..6:", [f"{m:.3f}±{e:.3f}" for m,e in zip(means,errs)])
mono=all(means[i+1] < means[i] for i in range(5)); below=means[-1] < 0.5
sc("R2", mono and below, True, f"monotone shrink {mono}; after 6 writes {means[-1]:.3f} < 0.5: {below}")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({'means':means.tolist(),'errs':errs.tolist()}, open('.record_5731.json','w'))
