#!/usr/bin/env python3
"""
Lyra R18 Lane D (2026-09-28). Invariant first: in 4D a local vertex  g * prod(fields) * (derivatives)^d  has
[g] = 4 - sum(Delta_i) - d.  chi_t(vertex) = exp(2 pi i sum Delta_i) = exp(-2 pi i [g])  (d integer).
Families/sources: H2's 4D pieces Delta = 5/2 + k (K1927, unitary scalar highest-weight of SO(4,2)); massless bosons Delta = 1 (scalar),
2 (field strength), 3 (conserved current), fermions Delta = 3/2 (Mack), Lorentz invariance => even number of fermion legs.
Predictions BEFORE the run:
 D1 over vertices with n_H in 1..4 H2 legs (k in 0..3), up to 3 bosons, 0/2 fermions, d in 0..3:
    [g] is half-integer  <=>  n_H odd.   (Equivalently chi_t = -1 <=> n_H odd.)
 D2 the scales BST has, the ruler m_e and H, have mass dimension 1; every monomial m_e^a H^b (a,b integers) has integer dimension
    => no analytic (integer-power) combination supplies a half-integer-dimension coupling.  CONTROL: m_e^(1/2) has dimension 1/2.
 D3 charge vertex H2 H2bar A_mu with a current: n_H = 2 -> integer [g] (not forbidden by this invariant).
"""
from fractions import Fraction as F
import itertools
ok=[]
H=[F(5,2)+k for k in range(4)]; B=[F(1),F(2),F(3)]; Fm=F(3,2)
D1=True; cnt=0
for nH in range(1,5):
    for hs in itertools.product(H,repeat=nH):
        for nb in range(0,4):
            for bs in itertools.product(B,repeat=nb):
                for nf in (0,2):
                    for d in range(4):
                        g=4-sum(hs)-sum(bs)-nf*Fm-d; cnt+=1
                        D1 &= ((g.denominator==2)==(nH%2==1))
ok.append(D1); print(f"D1 {cnt} vertices: [g] half-integer iff odd number of H2 legs ->",D1)
D2=all(((a+b)*F(1)).denominator==1 for a in range(-6,7) for b in range(-6,7)) and F(1,2).denominator==2
ok.append(D2); print("D2 m_e^a H^b always integer dimension; sqrt(m_e) is 1/2 ->",D2)
D3=(4-(F(5,2)+F(5,2))-F(1)).denominator==1; ok.append(D3); print("D3 H2 H2bar A: [g] =",4-(F(5,2)+F(5,2))-F(1),"integer ->",D3)
print(f"SCORE {sum(ok)}/{len(ok)}")
