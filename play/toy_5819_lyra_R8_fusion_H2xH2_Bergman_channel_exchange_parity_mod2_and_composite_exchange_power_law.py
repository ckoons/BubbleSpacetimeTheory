#!/usr/bin/env python3
"""
Lyra R8 (2026-09-26). Invariants first: J = K's centre (elliptic); exp(2 pi i J) is CENTRAL in the universal
cover G~ of SO_0(5,2) (it lies over the identity) => a Schur scalar on every irreducible and it commutes with
every G~-intertwiner. H^2 = H_{5/2}; Schmid: P(C^5) = (+)_{m1>=m2>=0} tau_m, tau_m = SO(5) (a,0) x q^b,
a = m1-m2, b = m2, |m| = a + 2b. Fusion (Repka/JV; Kobayashi 8.10 multiplicity-free, pinned by Grace):
H_l (x) H_l = (+)_m H(2l; tau_m), lowest J-weight 2l + |m|.  Predictions BEFORE the run
(J-graded dimensions only; SO(5) information collapsed to dims; 'generalized Verma = the module' assumed):
 F1  chi(H2)^2 = sum_m dim(tau_m) t^{5+|m|} * chi(P)       (the decomposition, graded dims, to t^40)
 F2  Sym^2 H2 = the |m| EVEN summands, Lambda^2 H2 = the |m| ODD summands (graded dims).
     => lowest antisymmetric two-body channel: m=(1,0), SO(5) vector, J-weight 6; lowest symmetric: m=0,
     scalar, J-weight 5 = genus = the BERGMAN module (Szego^2 = h^-5 = Bergman kernel).
 F3  mod-2: J-weights of H2^{(x)k} lie in 5k/2 + Z; exp(2 pi i J) = (-1)^k, k = 1..6.
 F4  static exchange of a local composite of 4D dimension D between static sources:
     V(r) ∝ int dt (t^2+r^2)^-D ∝ r^{1-2D}.  D=1 -> 1/r (Coulomb control); D=3 -> 1/r^5 (Feinberg-Sucher
     two-neutrino control); D=5/2 -> 1/r^4 (k=4); D=5 -> 1/r^9 (k=9).  Fitted slope within 1e-6.
"""
import numpy as np
from math import comb
from scipy.integrate import quad
from collections import Counter
ok=[]; T=40
d=lambda j: comb(j+4,4)                                  # graded dims of P(C^5)
dso5=lambda a:(a+1)*(a+2)*(2*a+3)//6
H=Counter({2*j+5:d(j) for j in range(T)})               # keys = 2*weight (integers)
def mul(A,B):
    C=Counter()
    for x,u in A.items():
        for y,v in B.items():
            if x+y<=4*T//2+10: C[x+y]+=u*v
    return C
LIM=2*T
sq=Counter({k:v for k,v in mul(H,H).items() if k<=LIM})
def summ(par=None):
    C=Counter()
    for a in range(T):
        for b in range(T):
            M=a+2*b
            if par is not None and M%2!=par: continue
            for j in range(T):
                k=2*(5+M+j)
                if k<=LIM: C[k]+=dso5(a)*d(j)
    return C
F1=sq==summ(); ok.append(F1); print("F1 chi(H2)^2 = sum_m dim tau_m t^{5+|m|} chi(P) ->",F1)
H2sq=Counter({2*k:v for k,v in H.items() if 2*k<=LIM})  # chi(t^2)
sym=Counter({k:(sq[k]+H2sq.get(k,0))//2 for k in sq}); alt=Counter({k:(sq[k]-H2sq.get(k,0))//2 for k in sq})
F2=all(((sq[k]+H2sq.get(k,0))%2==0) for k in sq) and +sym==+summ(0) and +alt==+summ(1)
ok.append(F2); print("F2 Sym^2 = |m| even, Lambda^2 = |m| odd ->",F2,"; lowest Sym weight",min(k for k,v in sym.items() if v)/2,"lowest Lambda weight",min(k for k,v in alt.items() if v)/2)
F3=True; A=Counter({0:1})
for k in range(1,7):
    A=Counter({x:v for x,v in mul(A,H).items() if x<=60})
    F3&=all((x-5*k)%2==0 for x in A)          # 2w - 5k even  <=> w in 5k/2 + Z
    F3&=all(np.isclose(np.exp(1j*np.pi*x),(-1)**k) for x in A)   # exp(2 pi i w), x = 2w
ok.append(F3); print("F3 H2^{(x)k} weights in 5k/2+Z, exp(2 pi i J)=(-1)^k, k=1..6 ->",F3)
def slope(D):
    rs=np.array([1.0,2.0,4.0]); V=[quad(lambda t:(t*t+r*r)**(-D),-np.inf,np.inf)[0] for r in rs]
    return np.polyfit(np.log(rs),np.log(V),1)[0]
F4=all(abs(slope(D)-(1-2*D))<1e-6 for D in (1,3,2.5,5)); ok.append(F4)
print("F4 slopes",{D:round(slope(D),8) for D in (1,3,2.5,5)},"-> k = 2D-1-... (1/r^{2D-1}): k=4 at 5/2, k=9 at 5 ->",F4)
print(f"SCORE {sum(ok)}/{len(ok)}")
