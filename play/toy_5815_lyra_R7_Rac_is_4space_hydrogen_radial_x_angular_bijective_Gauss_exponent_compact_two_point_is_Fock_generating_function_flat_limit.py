#!/usr/bin/env python3
"""
Lyra R7 (2026-09-26). Invariants quoted first: J = K's centre (elliptic); the frame sl(2,R) on
(x0,x5,x6) with mutual centralizer so(4) on (x1..x4); K-types of H_nu(D_IV^5): SO(5) (a,0) at J-weight
nu+a+2b (Rac: b=0). Gegenbauer C_N^(D). Predictions written BEFORE the run:
 S1  d=4 Coulomb bound spectrum: nu = N + (d-1)/2 = N + 3/2, degeneracy sum_{l<=N} dim harm_l(R^4) =
     sum (l+1)^2 = 1,5,14,30,...  == Rac: weight 3/2+a, dim SO(5)(a,0).  CONTROL d=3: nu=N+1, (N+1)^2 == ladder of SO(4,2).
 S2  Rac | SL(2,R) x SO(4) = (+)_i D+_{3/2+i} (x) (i/2,i/2), EACH SO(4)-type ONCE (bijective, Howe-like):
     radial Bargmann index = l + 3/2 = l + (d-1)/2 (4-space hydrogen). On H^2 the same pairing is NOT
     bijective (i pairs with 5/2+i+2m, all m): the odd clock is the multiplicity.
 S3  Gauss: r^-(D-2) is harmonic in R^D (D=3,4,5) and r^-3 is NOT harmonic in R^4: 2*Delta_min = D-2
     with Delta_min = Wallach point (D-2)/2 : 3/2 (D=5), 1 (D=4). Restriction keeps the exponent.
 S4  compact two-point on the cylinder: t^D (1-2t cos th + t^2)^-D = sum_N t^{D+N} C_N^(D)(cos th)
     (Fock's generating function at D=1 is the d=3 hydrogen one); truncated sum at N<=400 matches closed
     form to 1e-10 at t=0.5 for D = 1, 3/2, 5/2.
 S5  C_N^(5/2) = sum_b c_b C_{N-2b}^(3/2) with ALL c_b > 0 and exactly floor(N/2)+1 terms (N<=12):
     Theorem B (H^2 = Rac x odd clock) in correlator form.
 S6  flat limit (Euclidean cylinder, Rtau->T, R th->X): R^{-2D}... : [2(cosh(T/R)-cos(X/R))]^-D * R^{-2D}
     -> (T^2+X^2)^-D as R->inf, rel. error < 1e-5 at R=1e3 (D=5/2). R enters only as the normalization R^{2D}.
"""
import numpy as np, sympy as sp
from math import comb
from fractions import Fraction as F
from collections import Counter
from scipy.special import eval_gegenbauer
ok=[]
harm=lambda l,m: comb(l+m-1,m-1)-(comb(l+m-3,m-1) if l>=2 else 0)   # harmonic polys deg l in m vars
dimSO5=lambda a:(a+1)*(a+2)*(2*a+3)//6
S1=all(sum(harm(l,4) for l in range(N+1))==dimSO5(N) for N in range(30)) and [dimSO5(a) for a in range(4)]==[1,5,14,30] \
   and all(sum(harm(l,3) for l in range(N+1))==(N+1)**2 for N in range(30))
ok.append(S1); print("S1 d=4 degeneracies",[sum(harm(l,4) for l in range(N+1)) for N in range(5)],"== SO(5)(a,0); d=3 control (N+1)^2 ->",S1)
W=40
def branch(nu,wall):
    c=Counter()
    for a in range(W+1):
        for b in range(1 if wall else W+1):
            w=nu+a+2*b
            if w>W: break
            for i in range(a+1): c[(i,w)]+=1
    return c
def sl2(pairs):
    c=Counter()
    for i,l in pairs:
        s=0
        while l+s<=W: c[(i,l+s)]+=1; s+=1
    return c
rac=branch(F(3,2),True); h2=branch(F(5,2),False)
S2a=rac==sl2([(i,F(3,2)+i) for i in range(W+1)])
S2b=h2==sl2([(i,F(5,2)+i+2*m) for i in range(W+1) for m in range(W) if F(5,2)+i+2*m<=W])
S2=S2a and S2b; ok.append(S2); print("S2 Rac = (+) D+_{3/2+i} x (i/2,i/2) once each:",S2a," ; H2 needs the 2m tower:",S2b,"->",S2)
r=sp.symbols('r',positive=True)
lap=lambda f,D: sp.simplify(sp.diff(f,r,2)+(D-1)/r*sp.diff(f,r))
S3=all(lap(r**-(D-2),D)==0 for D in (3,4,5)) and lap(r**-3,4)!=0
ok.append(S3); print("S3 r^-(D-2) harmonic in R^D; r^-3 in R^4 ->",lap(r**-3,4),"->",S3)
t=0.5; th=0.7; x=np.cos(th); S4=True
for D in (1.0,1.5,2.5):
    ser=sum(t**(D+N)*eval_gegenbauer(N,D,x) for N in range(401)); cl=t**D*(1-2*t*x+t*t)**(-D)
    S4&=abs(ser-cl)<1e-10
ok.append(S4); print("S4 compact two-point = Fock generating function ->",S4)
X=sp.symbols('x'); S5=True
for N in range(13):
    rem=sp.expand(sp.gegenbauer(N,sp.Rational(5,2),X)); coeffs=[]
    for k in range(N,-1,-1):
        ck=sp.Poly(rem,X).coeff_monomial(X**k) if rem!=0 else 0
        lead=sp.Poly(sp.gegenbauer(k,sp.Rational(3,2),X),X).coeff_monomial(X**k)
        c=sp.nsimplify(ck/lead); coeffs.append((k,c)); rem=sp.expand(rem-c*sp.gegenbauer(k,sp.Rational(3,2),X))
    nz=[(k,c) for k,c in coeffs if c!=0]
    S5&=rem==0 and all(c>0 for _,c in nz) and all((N-k)%2==0 for k,_ in nz) and len(nz)==N//2+1
ok.append(S5); print("S5 C^(5/2)_N = sum_b c_b C^(3/2)_{N-2b}, c_b>0, floor(N/2)+1 terms ->",S5)
D=2.5; T,Xf=0.8,1.3; Rr=1e3
cyl=(2*(np.cosh(T/Rr)-np.cos(Xf/Rr)))**(-D)*Rr**(-2*D); flat=(T*T+Xf*Xf)**(-D)
S6=abs(cyl/flat-1)<1e-5; ok.append(S6); print(f"S6 flat limit rel.err {abs(cyl/flat-1):.2e} ->",S6)
print(f"SCORE {sum(ok)}/{len(ok)}")
