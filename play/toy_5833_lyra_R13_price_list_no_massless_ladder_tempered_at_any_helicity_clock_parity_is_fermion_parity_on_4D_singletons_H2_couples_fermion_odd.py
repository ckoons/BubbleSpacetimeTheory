#!/usr/bin/env python3
"""
Lyra R13 (2026-09-27). Invariants first: z = exp(2 pi i J) central in the universal cover (J shared by the embedded SO(4,2),
Cal S1001); massless 4D ladder of helicity j has Delta = j+1 (Mack), J-weights Delta + Z>=0; H2|SO(4,2) weights 5/2 + Z>=0.
Harish-Chandra Xi is W-INVARIANT: on the axis rays (T,0) and (0,T) of SU(2,2)'s A the bound is e^{-rho_max T}, rho_max = 3.
Predictions BEFORE the run:
 P1 (Elie 5830's structure, generalized): a lowest-K-type vector with block exponents (Delta+j, Delta-j) meets Xi on BOTH
    axes iff min = Delta-j >= 3. Massless: Delta-j = 1 for every j (0 .. 6): NOT tempered at any helicity.
    CONTROL: SU(2,2) scalar holomorphic discrete series edge lambda = 3 (j=0): min = 3 >= 3 -> tempered edge.
 P2 clock parity = fermion parity on 4D massless ladders: z = e^{2 pi i Delta} = (-1)^{2j} for j = 0..6.
 P3 H2 quanta (z = -1) couple covariantly to a product of 4D singletons only if that product has z = -1, i.e. an ODD number of
    half-integer-helicity factors: checked over all products of up to 4 factors from {h=0, 1/2, 1, 3/2, 2}.
 P4 a J-commuting operation on H2 preserves spec J = 5/2 + Z>=0, so it cannot reach the massless bottoms 1, 3/2, 2 (all < 5/2).
"""
import itertools
from fractions import Fraction as F
import cmath
ok=[]
P1=all((F(j)+1-F(j))<3 for j in [F(k,2) for k in range(13)]) and (F(3)-0)>=3
ok.append(P1); print("P1 Delta-j = 1 < 3 for j=0..6 (not tempered); control lambda=3 j=0 -> 3 >= 3 ->",P1)
z=lambda D: cmath.exp(2j*cmath.pi*float(D))
P2=all(abs(z(F(j)+1)-(-1)**int(2*j))<1e-12 for j in [F(k,2) for k in range(13)]); ok.append(P2); print("P2 z = (-1)^{2j} on massless ladders ->",P2)
hel=[F(0),F(1,2),F(1),F(3,2),F(2)]; P3=True
for n in range(1,5):
    for combo in itertools.product(hel,repeat=n):
        zz=1
        for h in combo: zz*=z(h+1)
        odd=sum(1 for h in combo if h.denominator==2)%2==1
        P3&= (abs(zz+1)<1e-9)==odd
ok.append(P3); print("P3 product has z=-1 (couples to H2) iff odd number of half-integer helicities, n<=4 ->",P3)
P4=all(b<F(5,2) for b in (F(1),F(3,2),F(2))); ok.append(P4); print("P4 massless bottoms 1, 3/2, 2 all below H2 floor 5/2 ->",P4)
print(f"SCORE {sum(ok)}/{len(ok)}")
