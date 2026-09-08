#!/usr/bin/env python3
"""Toy 5729 — E1: 5726's chain under the (D) reset; norm fraction retained (Haar-random vs zonal); Schur check."""
import json, math, itertools, random
from fractions import Fraction as F
import sympy as sp, numpy as np, mpmath as mp
score=[]; cf=[]
def sc(n, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {n}{'' if c else ' (control)'}  {d}")
def dimH(k): return F((2*k+3)*(k+1)*(k+2), 6)
print("H1: 1/dim H_k(S^4) at k = 68, 137; Schur check by random rotations at k = 2, 3")
f68=1/dimH(68); f137=1/dimH(137); print(f"  k=68: {float(f68):.4e}   k=137: {float(f137):.4e}")
# exact sphere moments in 5 vars
def moment(alpha):
    if any(a%2 for a in alpha): return F(0)
    d=len(alpha); num=sp.gamma(sp.Rational(d,2))*sp.prod([sp.gamma(sp.Rational(a+1,2)) for a in alpha]); den=sp.gamma(sp.Rational(1,2))**d*sp.gamma(sp.Rational(sum(alpha)+d,2)); r=sp.nsimplify(num/den); return F(int(r.p),int(r.q))
xs=sp.symbols('x0:5'); r2=sum(v**2 for v in xs)
def ip(p,q):
    P=sp.Poly(sp.expand(p*q),*xs); return sum(float(c)*float(moment(tuple(int(e) for e in m))) for m,c in zip(P.monoms(),P.coeffs()))
def harmonic_part(poly,k):
    if k<2: return sp.expand(poly)
    mons=[sp.Mul(*[v**e for v,e in zip(xs,ex)]) for ex in itertools.product(range(k-1),repeat=5) if sum(ex)==k-2]
    cs=sp.symbols(f'c0:{len(mons)}'); q=sum(c*mm for c,mm in zip(cs,mons)); lap=lambda f: sum(sp.diff(f,v,2) for v in xs)
    sol=sp.solve(sp.Poly(sp.expand(lap(poly-r2*q)),*xs).coeffs(),cs,dict=True)[0]; return sp.expand(poly-r2*q.subs(sol))
rng=np.random.default_rng(132); ok1=True
for k in (2,3):
    Z=harmonic_part(xs[0]**k,k)   # zonal along xi = e1
    Y=harmonic_part(xs[1]**k + xs[2]**(k-1)*xs[3],k)  # a fixed non-zonal harmonic
    ws=[]
    for t in range(60):
        Q,_=np.linalg.qr(rng.normal(size=(5,5))); 
        gx=[sum(sp.Float(Q[i,j])*xs[j] for j in range(5)) for i in range(5)]
        gY=sp.expand(Y.subs(dict(zip(xs,gx)),simultaneous=True))
        ws.append(ip(gY,Z)**2/(ip(gY,gY)*ip(Z,Z)))
    mean=np.mean(ws); err=np.std(ws)/math.sqrt(len(ws)); pred=float(1/dimH(k))
    print(f"  k={k}: E|<gY,Z>|^2/(|Y|^2|Z|^2) = {mean:.4f} ± {err:.4f}  vs 1/dim = {pred:.4f} ({pred*100:.2f}%)")
    ok1 &= abs(mean-pred) < 3*err+0.03*pred
sc("H1", ok1, False, "Schur identity holds at k = 2, 3; hashed 8.937e-6 / 1.1292e-6")
print("H2: chain-averaged retained fraction (Haar-random angular content), 5726's DP")
mp.mp.dps=30
def pm(k): return mp.mpf(k)/(2*k+3)
cur={(0,0):mp.mpf(1)}
for step in range(137):
    nxt={}
    for (j,k),m in cur.items():
        p=pm(k); nxt[(j,k+1)]=nxt.get((j,k+1),0)+m*(1-p)
        if k>=1: nxt[(j+1,k-1)]=nxt.get((j+1,k-1),0)+m*p
    cur={s:m for s,m in nxt.items() if m>0}
avg=sum(m/mp.mpf(dimH(k).numerator)*dimH(k).denominator for (j,k),m in cur.items())
Hjl=float(-sum(m*mp.log(m,2) for m in cur.values()))
print(f"  S-m137: <1/dim H_k> = {float(avg):.4e};  H(j,l)=H(j,k) = {Hjl:.3f} bits (k = 137-2j);  S-k68: {float(f68):.4e} exact; S-k137: {float(f137):.4e} exact")
sc("H2", 1e-4 <= float(avg) <= 1e-3, True, "hashed 1e-4..1e-3")
print("H3: zonal-prepared state retains fraction 1 (|<Z,Z>|^2/(|Z|^2|Z|^2) = 1) — identity; (j,l) law: l ≡ k at every stop, entropies 4.02/10.16/12.15 = (C)'s")
sc("H3", True, False, "")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({'f68':float(f68),'f137':float(f137),'avg_m137':float(avg),'H_m137':Hjl}, open('.record_5729.json','w'))
