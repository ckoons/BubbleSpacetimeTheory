#!/usr/bin/env python3
"""Toy 5743 — R136: is the 5 in c ~ 5n/(2j) the dimension? Sweep n AND the weight parameter nu."""
import os, math, json, itertools
from fractions import Fraction as F
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy import QQ
src=open([f for f in os.listdir('.') if f.startswith('toy_5722_')][0]).read(); exec(src.split('t0 = time.time()')[0])
score=[]; cf=[]
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
def Lnu(n,nu,j,k): j=F(j); k=F(k); n=F(n); nu=F(nu); return (k+n-2)/(2*k+n-2)*(j+k+n/2)/(j+k+nu)
def Mnu(n,nu,j,k):
    if k==0: return F(0)
    j=F(j); k=F(k); n=F(n); nu=F(nu); return k/(2*k+n-2)*(j+1)/(j+nu-(n-2)/2)
def taunu(p,n,nu,j,k):
    if p==0: return F(1)
    t=Lnu(n,nu,j,k)*taunu(p-1,n,nu,j,k+1)
    if k>0: t+=Mnu(n,nu,j,k)*taunu(p-1,n,nu,j+1,k-1)
    return t
def c_nu(p,n,nu,j,k): return 1-taunu(p,n,nu,j,k)
print("G1: control — the family at nu = n reproduces 5724's matter word and 5730's twelve rationals")
fam={3:F(12,35),4:F(3,8),5:F(25,63),6:F(33,80),7:F(14,33)}
g1a=all(c_nu(1,n,n,1,1)==v for n,v in fam.items())
known={(0,0):F(1,2),(0,1):F(10,21),(0,2):F(45,98),(0,3):F(25,56),(1,0):F(5,12),(1,1):F(25,63),(1,2):F(55,144),(1,3):F(10,27),(2,0):F(5,14),(2,1):F(15,44),(2,2):F(65,198),(2,3):F(7,22)}
g1b=all(c_nu(1,5,5,j,k)==v for (j,k),v in known.items())
print(f"   c(1,1) at n = 3..7: {[str(c_nu(1,n,n,1,1)) for n in range(3,8)]}  (5724: 12/35, 3/8, 25/63, 33/80, 14/33)")
sc("G1", g1a and g1b, False, "family line and the twelve rationals both exact")
print("G2: control — c_1(j,0) = n/(2(j+n)) and j*c_p -> p*n/2")
g2a=all(c_nu(1,n,n,j,0)==F(n,2*(j+n)) for n in range(3,9) for j in range(0,60))
print("   n = 3..8, j = 0..59: c_1(j,0) = n/(2(j+n)) exactly:", g2a)
for n in (4,5,6):
    print(f"   n={n}: j*c_p(j,0) at j = 20000, p = 1,2,3: {[round(float(20000*c_nu(p,n,n,20000,0)),4) for p in (1,2,3)]}   (p*n/2 = {[p*n/2 for p in (1,2,3)]})")
g2b=all(abs(float(20000*c_nu(p,n,n,20000,0))-p*n/2)<0.02*p*n/2 for n in (4,5,6) for p in (1,2,3))
sc("G2", g2a and g2b, False, "exact k=0 line and the p*n/2 limit at three dimensions")
print("G3: THE DISCRIMINATOR — the k = 0 line at free weight parameter nu")
g3=True
for (n,nu) in [(5,5),(5,4),(5,3),(5,F(5,2)),(4,4),(6,6),(6,4)]:
    pred=[ (F(nu)-F(n,2))/(F(j)+F(nu)) for j in range(4)]
    got=[c_nu(1,n,nu,j,0) for j in range(4)]
    ok=all(a==b for a,b in zip(pred,got)); g3&=ok
    print(f"   n={n}, nu={nu}: constant nu - n/2 = {F(nu)-F(n,2)};  c_1(j,0), j=0..3 = {[str(x) for x in got]}  matches (nu-n/2)/(j+nu): {ok}")
sc("G3", g3, True, "c_1(j,0) = (nu - n/2)/(j + nu) exactly; at the Hardy point nu = n/2 the cost is identically ZERO")
print("G4: independent instrument — the kernel Gram at exponent -nu (not -n)")
def gram_nu(nv, nu, m):
    mons=mono_list(nv,m); C={}
    for al in mons:
        for be in mons:
            if any((al[i]-be[i])%2 for i in range(nv)): continue
            v=F(0)
            for b in range(0,m//2+1):
                N=m-b; a=N-b
                if a<0: continue
                v+=F(poch(F(nu),N))/math.factorial(N)*math.comb(N,b)*2**a*(-1)**b*kernel_coeff(nv,a,b,al,be)
            if v: C[(al,be)]=v
    blocks={}
    for e in mons: blocks.setdefault(tuple(x%2 for x in e),[]).append(e)
    G={}
    for par,es in blocks.items():
        Mx=DomainMatrix([[QQ(C.get((x,y),F(0)).numerator, C.get((x,y),F(0)).denominator) for y in es] for x in es],(len(es),len(es)),QQ)
        Mi=Mx.inv().to_Matrix()
        for i,x in enumerate(es):
            for jj,y in enumerate(es):
                if Mi[i,jj]!=0: G[(x,y)]=F(int(Mi[i,jj].p),int(Mi[i,jj].q))
    return G
def norm2_nu(pd,nv,nu,m):
    G=gram_nu(nv,nu,m); return sum(ca*cb*G[(a,b)] for a,ca in pd.items() for b,cb in pd.items() if (a,b) in G)
zs=sp.symbols('z0:5'); zz=sum(v**2 for v in zs); g4=True
for nu in (4,3):
    for (j,k) in [(0,0),(1,0),(0,1),(1,1)]:
        m=2*j+k; psi=sp.expand(zz**j*harmonic_part(zs[0]**k,k,zs)); pd=poly_dict(psi,zs); N0=norm2_nu(pd,5,nu,m)
        N1=sum(norm2_nu(poly_dict(sp.expand(zs[i]*psi),zs),5,nu,m+1) for i in range(5))
        gram_c=1-N1/N0; rec=c_nu(1,5,nu,j,k); ok=(gram_c==rec); g4&=ok
        print(f"   nu={nu} ({j},{k}): Gram c = {gram_c} ; recursion = {rec}  {'=' if ok else 'MISMATCH'}")
sc("G4", g4, True, "the nu-generalised kernel Gram confirms the recursion off the Bergman point")
print("VERDICT: rank = 2 throughout; for type IV genus = dimension = n so the D_IV sweep alone cannot separate them;")
print("  the nu sweep does: the constant is nu - n/2, the gap from the Wallach/Hardy point. At the Bergman point nu = n it equals n/2,")
print("  which is why it reads as '5/2' on D_IV^5. 'The dimension appears in the commitment law' is a shared-integer reading.")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({'nu_lines':{f"{n},{nu}":[str(c_nu(1,n,nu,j,0)) for j in range(4)] for (n,nu) in [(5,5),(5,4),(5,3),(4,4),(6,6)]}}, open('.record_5743.json','w'), indent=1)
