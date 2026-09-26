#!/usr/bin/env python3
"""
Lyra R6 item 2 (2026-09-26). Invariants: conjugacy type of an element of sl(2,R) (sign of -det:
elliptic <0, parabolic =0, hyperbolic >0), preserved by every REAL conjugation. The sl(2,R)=so(2,1) on
(x0, x5, x6) has commutant so(4) (x1..x4) and contains K's centre J = M06.  Predictions written first:
 R1  No real conjugation maps J (elliptic) to P0 (parabolic): -det(J)=-1, -det(P0)=0.
 R2  The complex Cayley element c = (1/sqrt2)[[1,i],[i,1]] maps J to i*(hyperbolic), not to P0:
     c J c^-1 = i * H with H real, -det(H) > 0.  (Cayley changes the REALIZATION, disc -> half-plane,
     and in the half-plane picture J = (P0 + K0)/2 up to sign convention: a combination, not a conjugate.)
 R3  In the half-plane realization the elliptic element is (P0 + K0)/2 with P0=[[0,1],[0,0]],
     K0=[[0,0],[-1,0]]: (P0+K0)/2 is elliptic.  CONTROL: (P0 - K0)/2 is hyperbolic (Keeper's first-run sign error).
 R4  K-character identity: H^2(D_IV^5) | SL(2,R) x SO(4) = (+)_{i,m>=0} D+_{5/2+i+2m} (x) (i/2,i/2),
     exact to J-weight 40 (D+_l contributes weights l, l+1, ...).
 R5  Same for the D_IV^4 summand H_{5/2+k}: (+)_{i,m} D+_{5/2+k+i+2m} (x) SO(3)-type i (dim 2i+1), k=0..3.
 R6  lowest sl(2) weight on H^2 is 5/2 (the ground weight of item 1): every D+ summand has lambda >= 5/2,
     so on each summand P0 has spectrum (0,inf) absolutely continuous and no P0-invariant vector
     (standard for D+_lambda; checked here only as: lambda > 0 on every summand).
"""
import numpy as np
from fractions import Fraction as F
from collections import Counter
ok=[]; typ=lambda M: -np.linalg.det(M)
J=np.array([[0,1],[-1,0]],float); P0=np.array([[0,1],[0,0]],float); K0=np.array([[0,0],[-1,0]],float)
R1=typ(J)<0 and abs(typ(P0))<1e-15; ok.append(R1); print("R1 -det J",typ(J)," -det P0",typ(P0),"->",R1)
c=np.array([[1,1j],[1j,1]])/np.sqrt(2); X=c@J@np.linalg.inv(c); H=X/1j
R2=np.allclose(H.imag,0) and typ(H.real)>0 and not np.allclose(X,P0); ok.append(R2); print("R2 cJc^-1 =",np.round(X,6).tolist(),"= i*H, -det H =",round(typ(H.real),6),"->",R2)
E=(P0+K0)/2; Hm=(P0-K0)/2
R3=typ(E)<0 and typ(Hm)>0; ok.append(R3); print("R3 -det (P0+K0)/2 =",typ(E)," -det (P0-K0)/2 =",typ(Hm),"->",R3)
W=40
def H2char(nu,n):  # SO(n) (a,0) at nu+a+2b -> branched to SO(n-1): types i<=a
    c=Counter()
    for a in range(W+1):
        for b in range(W+1):
            w=nu+a+2*b
            if w>W: break
            for i in range(a+1): c[(i,w)]+=1
    return c
def sl2sum(nu):
    c=Counter()
    for i in range(W+1):
        for m in range(W+1):
            l=nu+i+2*m
            if l>W: break
            for s in range(W+1):
                if l+s>W: break
                c[(i,l+s)]+=1
    return c
R4=H2char(F(5,2),5)==sl2sum(F(5,2)); ok.append(R4); print("R4 H2 = sum D+_{5/2+i+2m} x (i/2,i/2) ->",R4)
R5=all(H2char(F(5,2)+k,4)==sl2sum(F(5,2)+k) for k in range(4)); ok.append(R5); print("R5 D_IV^4 summands k=0..3 ->",R5)
R6=min(F(5,2)+i+2*m for i in range(3) for m in range(3))==F(5,2); ok.append(R6); print("R6 min lambda = 5/2 > 0 ->",R6)
print(f"SCORE {sum(ok)}/{len(ok)}")
