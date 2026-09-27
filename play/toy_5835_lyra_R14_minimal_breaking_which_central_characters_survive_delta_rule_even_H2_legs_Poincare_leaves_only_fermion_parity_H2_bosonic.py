#!/usr/bin/env python3
"""
Lyra R14 (2026-09-27). Invariants first. Two central elements of the universal cover of SO_0(4,2) (both in Z(K~), K~ = Spin(4) x R):
 z_t = exp(2 pi J) (clock; chi_t = e^{2 pi i Delta}) and z_s = spatial 2pi, (-1,-1) in Spin(4) (chi_s = (-1)^{2(j1+j2)}).
 z_s acts trivially on p = R^4 (x) R^2 (it is the kernel of Spin(4) -> SO(4)), so it is central in G~ (premise P1).
 delta := chi_t * chi_s (the 'spin-statistics defect'), multiplicative.
 Which characters a vertex must conserve depends on the symmetry it keeps:
   G~ (conformal) or K~ (ruler as the compact RADIUS; J and SO(4) kept): both chi_t and chi_s (both central in K~).
   Poincare cover (ruler as a MASS; J = (P0+K0)/2 broken): only chi_s (spatial 2pi is central; the clock is not in the group).
Predictions BEFORE the run:
 Q1 characters: massless ladder (Delta=j+1, SO(4) spin (j,0)): chi_t = chi_s -> delta = +1 (j = 0..4).
    H2's 4D pieces H_{5/2+k}(D4), K-types (l/2,l/2): (chi_t, chi_s) = (-1,+1) -> delta = -1.
 Q2 conformal/K~: a vertex with n_H H2 legs and a massless multiset M is allowed by the characters iff
    chi_t: (-1)^{n_H} * prod = 1 AND chi_s: prod = 1.  => n_H = 1: FORBIDDEN for every M (Keeper Part 2, single leg);
    n_H = 2: ALLOWED iff M is fermion-even; n_H = 1 + fermion-odd M (my R13 'fermion-odd' vertex): FORBIDDEN by chi_s.
 Q3 Poincare only (chi_s): n_H = 1 + fermion-EVEN M ALLOWED; n_H = 1 + fermion-odd M FORBIDDEN  => H2 couples as a BOSON;
    my R13 fermion-odd rule is reversed once the clock is broken.
 Q4 Keeper's 'no covariant vertex connects H2 to any number of massless' holds for ODD n_H only (n_H = 1, 3), not n_H = 2.
All over massless multisets of up to 4 legs from j in {0,1/2,1,3/2,2} and n_H in {1,2,3}.
"""
import itertools, cmath
from fractions import Fraction as F
ok=[]
chi_t=lambda D: round(cmath.exp(2j*cmath.pi*float(D)).real)
def ml(j): D=j+1; return chi_t(D), (-1)**int(2*j)
Q1=all(ml(F(k,2))[0]==ml(F(k,2))[1] for k in range(9)) and all((chi_t(F(5,2)+k+l+2*m), (-1)**int(l)) == (-1, 1) for k in range(4) for l in range(0,8,2) for m in range(3)) \
   and all(chi_t(F(5,2)+k+l+2*m)==-1 for k in range(4) for l in range(6) for m in range(3))
# note: (l/2,l/2) has j1+j2 = l, so chi_s = (-1)^{2l} = +1 for every l
Q1 = Q1 and all((-1)**int(2*l)==1 for l in range(8))
ok.append(Q1); print("Q1 massless delta=+1; H2 4D pieces (chi_t,chi_s)=(-1,+1) ->",Q1)
hel=[F(0),F(1,2),F(1),F(3,2),F(2)]
def allowed(nH,M,keep_t):
    pt=(-1)**nH; ps=1
    for j in M: t,s=ml(j); pt*=t; ps*=s
    return (pt==1 or not keep_t) and ps==1
Ms=[M for n in range(0,5) for M in itertools.product(hel,repeat=n)]
ferm_odd=lambda M: sum(1 for j in M if j.denominator==2)%2==1
Q2=all(not allowed(1,M,True) for M in Ms) and all(allowed(2,M,True)==(not ferm_odd(M)) for M in Ms)
ok.append(Q2); print("Q2 conformal/K~: single H2 leg forbidden for every M; two legs allowed iff M fermion-even ->",Q2)
Q3=all(allowed(1,M,False)==(not ferm_odd(M)) for M in Ms)
ok.append(Q3); print("Q3 Poincare only: single H2 leg allowed iff M fermion-EVEN (H2 couples as a boson) ->",Q3)
Q4=all(not allowed(n,M,True) for n in (1,3) for M in Ms) and any(allowed(2,M,True) for M in Ms if len(M)>0)
ok.append(Q4); print("Q4 prohibition holds for odd numbers of H2 legs only ->",Q4)
print(f"SCORE {sum(ok)}/{len(ok)}")
