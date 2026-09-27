#!/usr/bin/env python3
"""
Lyra R11 (2026-09-27). Invariants first: 4D conserved spin-s <=> Delta = 2+s; massless ladder = lambda = 1 (D_IV^4
Wallach point). Wallach norms of H_lambda(D_IV^n) on Schmid K-type m=(m1,m2): (lambda)_{m1} (lambda-(n-2)/2)_{m2}.
Generic norm of the Lie ball: h(z,w) = 1 - 2 z.conj(w) + (z.z)(conj(w).conj(w)).  Predictions BEFORE the run:
 K1 (route a) KK on a circle of radius R: zero-mode correlator G0(x) = sum_n (x^2+(2 pi R n)^2)^-D.
    log-slope at x>>R is 1-2D (4D Delta = D - 1/2), at x<<R is -2D (5D).  D=3/2 (Rac): -2 / -3 -> Delta4 = 1 = lambda 1.
    D=5/2 (H2): -4 / -5 -> Delta4 = 2 (a GFF, not a particle).  CONTROL 4D->3D, D=1: -1 at x>>R (Delta3 = 1/2).
 K2 (route a) zero-mode bilinears 2*Delta4 + s vs 2 + s: Rac lift 0 (conserved currents AND a 4D T), H2 lift 2 (none).
 K3 (route b) h_5(z,w) at z5=w5=0 == h_4(z,w) exactly  => boundary-value (and holomorphic k=0) restriction keeps the
    exponent: h^-lambda -> H_lambda(D_IV^4), lambda unchanged (5/2 -> 5/2, 3/2 -> 3/2; the D_IV^4 Hardy exponent is 2).
 K4 (route c) n=5, lambda=1: (1-3/2)_{m2} < 0 for every m2>=1 -> negative-norm K-types (ghosts), m1-part positive.
    n=4, lambda=1: (0)_{m2} = 0 for m2>=1 -> null, quotient = the ladder.  CONTROLS: n=5 lambda=3/2 -> 0 (Rac quotient);
    n=5 lambda=5/2 -> all positive (H2 unitary).
"""
import numpy as np, sympy as sp
ok=[]
def G0(x,D,R=1.0,N=20000):
    n=np.arange(-N,N+1); return np.sum((x*x+(2*np.pi*R*n)**2)**(-D))
def slope(D,x1,x2): return (np.log(G0(x2,D))-np.log(G0(x1,D)))/(np.log(x2)-np.log(x1))
res={}
for D in (1.5,2.5,1.0):
    res[D]=(round(slope(D,400,800),3),round(slope(D,1e-3,2e-3),3))
K1=abs(res[1.5][0]+2)<0.01 and abs(res[1.5][1]+3)<0.01 and abs(res[2.5][0]+4)<0.01 and abs(res[2.5][1]+5)<0.01 and abs(res[1.0][0]+1)<0.01
ok.append(K1); print("K1 slopes (x>>R, x<<R):",res,"->",K1)
lift=lambda d4:2*d4-2
K2=lift(1)==0 and lift(2)==2; ok.append(K2); print("K2 zero-mode bilinear lifts: Rac",lift(1),"H2",lift(2),"->",K2)
z=sp.symbols('z1:6'); w=sp.symbols('w1:6')
def h(zz,ww):
    dot=sum(a*sp.conjugate(b) for a,b in zip(zz,ww)); q=lambda v:sum(a*a for a in v)
    return 1-2*dot+q(zz)*sp.conjugate(q(ww))
K3=sp.simplify(h(z,w).subs({z[4]:0,w[4]:0})-h(z[:4],w[:4]))==0; ok.append(K3); print("K3 h5 restricted == h4 ->",K3)
poch=lambda a,m: sp.prod([a+i for i in range(m)]) if m>0 else 1
nrm=lambda lam,n,m1,m2: poch(lam,m1)*poch(lam-sp.Rational(n-2,2),m2)
K4=all(nrm(1,5,m1,m2)<0 for m2 in range(1,6) for m1 in range(m2,8)) and all(nrm(1,5,m1,0)>0 for m1 in range(8)) \
   and all(nrm(1,4,m1,m2)==0 for m2 in range(1,6) for m1 in range(m2,8)) \
   and all(nrm(sp.Rational(3,2),5,m1,m2)==0 for m2 in range(1,6) for m1 in range(m2,8)) \
   and all(nrm(sp.Rational(5,2),5,m1,m2)>0 for m2 in range(0,6) for m1 in range(m2,8))
ok.append(K4); print("K4 n=5 lambda=1 ghosts for m2>=1; n=4 null; Rac null; H2 positive ->",K4)
print(f"SCORE {sum(ok)}/{len(ok)}  (run 2; run 1 sha 85d0de73 crashed on generator loop order before K4 printed; K1-K3 identical)")
