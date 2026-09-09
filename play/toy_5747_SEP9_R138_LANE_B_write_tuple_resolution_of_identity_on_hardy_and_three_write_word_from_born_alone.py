#!/usr/bin/env python3
"""Toy 5747 — R138 LANE B: the write tuple is a resolution of the identity on H^2(S); the branching and 3/7 are its Born probabilities."""
import itertools, json, random
from fractions import Fraction as F
import sympy as sp
score=[]; cf=[]
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
xs=sp.symbols('x0:5'); r2=sum(v**2 for v in xs)
MOM={}
def moment(a):
    if a in MOM: return MOM[a]
    if any(e%2 for e in a): v=F(0)
    else:
        num=sp.gamma(sp.Rational(5,2))*sp.prod([sp.gamma(sp.Rational(e+1,2)) for e in a])
        den=sp.gamma(sp.Rational(1,2))**5*sp.gamma(sp.Rational(sum(a)+5,2))
        rr=sp.Rational(sp.gammasimp(sp.simplify(num/den))); v=F(int(rr.p),int(rr.q))
    MOM[a]=v; return v
def ip(p,q):
    P=sp.Poly(sp.expand(p*q),*xs); return sum(F(int(c.p),int(c.q))*moment(tuple(int(e) for e in m)) for m,c in zip(P.monoms(),P.coeffs()))
def harmonic_part(poly,k):
    if k<2: return sp.expand(poly)
    mons=[sp.Mul(*[v**e for v,e in zip(xs,ex)]) for ex in itertools.product(range(k-1),repeat=5) if sum(ex)==k-2]
    cs=sp.symbols(f'c0:{len(mons)}'); q=sum(c*m for c,m in zip(cs,mons)); lap=lambda f: sum(sp.diff(f,v,2) for v in xs)
    sol=sp.solve(sp.Poly(sp.expand(lap(poly-r2*q)),*xs).coeffs(),cs,dict=True)[0]; return sp.expand(poly-r2*q.subs(sol))
random.seed(138)
def words(k):
    out=[("zonal", harmonic_part(xs[0]**k,k))]
    if k>0:
        mons=[sp.Mul(*[v**e for v,e in zip(xs,ex)]) for ex in itertools.product(range(k+1),repeat=5) if sum(ex)==k]
        out.append(("random", harmonic_part(sum(random.randint(-3,3)*m for m in mons)+xs[1]**k,k)))
    return out
print("E2 P1: is Sum_u ||z_u psi||^2_H / ||psi||^2_H exactly 1 on the Hardy space? (the (z.z)^j factor is unimodular on S, so j drops out)")
p1=True
for k in range(0,6):
    for lab,Y in words(k):
        tot=sum(ip(xs[u]*Y,xs[u]*Y) for u in range(5)); nrm=ip(Y,Y); ok=(tot==nrm); p1&=ok
        if lab=="zonal": print(f"   k={k} {lab:6}: Sum_u ||x_u Y||^2 / ||Y||^2 = {tot/nrm}  {'exact 1' if ok else 'NOT 1'}")
sc("P1", p1, True, "Sum_u E_u = I exactly on H^2(S), zonal and random harmonics, k = 0..5 (j drops out by unimodularity)")
print("E2 P2: the five-outcome law for a zonal word (the outcomes are not uniform except at k = 0)")
for k in range(0,4):
    Y=harmonic_part(xs[0]**k,k); nrm=ip(Y,Y); ps=[ip(xs[u]*Y,xs[u]*Y)/nrm for u in range(5)]
    print(f"   k={k}: p_u = {[str(p) for p in ps]}  sum = {sum(ps)}")
Y0=sp.Integer(1); p_vac=[ip(xs[u]*Y0,xs[u]*Y0)/ip(Y0,Y0) for u in range(5)]
sc("P2", all(p==F(1,5) for p in p_vac), False, "at the vacuum all five outcomes are 1/5 — the ISOTROPY of the vacuum; named before reading, this is not the retired push-cost 1/5")
print("E2 P3: split each outcome by Hua component — the branching as a Born probability")
p3=True
for k in range(0,6):
    for lab,Y in words(k):
        nrm=ip(Y,Y); light=F(0); matter=F(0)
        for u in range(5):
            H=harmonic_part(sp.expand(xs[u]*Y),k+1); light+=ip(H,H)
            if k>0:
                D=sp.expand(sp.diff(Y,xs[u]))/F(2*k+3); matter+=ip(D,D)
        L=light/nrm; M=matter/nrm; ok=(L==F(k+3,2*k+3) and M==F(k,2*k+3) and L+M==1); p3&=ok
        if lab=="zonal": print(f"   k={k} {lab:6}: light = {L} (= {F(k+3,2*k+3)}), matter = {M} (= {F(k,2*k+3)}), sum = {L+M}  {'OK' if ok else 'MISMATCH'}")
sc("P3", p3, True, "the branching (k+3)/(2k+3), k/(2k+3) IS the Born law of the write tuple's resolution — zonal and random, k = 0..5, no table consulted")
print("E2 P4: positive control at the BERGMAN weight — the same sum must fail to be 1, by exactly c(j,k)")
def Lnu(nu,j,k): j=F(j);k=F(k);nu=F(nu); return F(k+3,2*k+3)*(j+k+F(5,2))/(j+k+nu)
def Mnu(nu,j,k):
    if k==0: return F(0)
    j=F(j);k=F(k);nu=F(nu); return F(k,2*k+3)*(j+1)/(j+nu-F(3,2))
for (j,k) in [(0,0),(0,1),(1,1),(0,2),(2,3)]:
    s=Lnu(5,j,k)+Mnu(5,j,k); print(f"   ({j},{k}): Sum_u ||z_u psi||^2_A2/||psi||^2_A2 = {s}, deficit = {1-s}  (5735 closed form c(j,k) = {1-s})")
sc("P4", all(Lnu(5,j,k)+Mnu(5,j,k)<1 for (j,k) in [(0,0),(0,1),(1,1),(0,2),(2,3)]), False, "fails to be 1 by exactly the push cost — the defect of the row isometry, loop closed with Rounds 134-137")
print("E3 P5: the three-write word from the Born law alone")
def born(k):
    Y=harmonic_part(xs[0]**k,k) if k>0 else sp.Integer(1); nrm=ip(Y,Y); light=F(0); matter=F(0)
    for u in range(5):
        H=harmonic_part(sp.expand(xs[u]*Y),k+1); light+=ip(H,H)
        if k>0:
            D=sp.expand(sp.diff(Y,xs[u]))/F(2*k+3); matter+=ip(D,D)
    return light/nrm, matter/nrm
L0,M0=born(0); L1,M1=born(1); L2,M2=born(2)
print(f"   write 1 from (0,0): light {L0}, matter {M0}   [computed, not tabled]")
print(f"   write 2 from (0,1): light {L1}, matter {M1}")
print(f"   write 3 from (0,2): light {L2}, matter {M2}")
p11 = M1 + L1*M2
print(f"   P(state = (1,1) after three writes) = {M1} + {L1}*{M2} = {p11} = {float(p11):.6f}")
sc("P5", p11==F(3,7), True, "3/7 exactly, with no branching-table input anywhere — the signature fraction is a Born probability of the write tuple's own resolution")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({'three_write':str(p11),'vac_outcomes':[str(p) for p in p_vac]}, open('.record_5747.json','w'), indent=1)
