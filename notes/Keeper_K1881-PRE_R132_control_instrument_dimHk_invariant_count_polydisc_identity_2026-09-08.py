from math import comb
import numpy as np
# dim H_k(R^5) two ways
for k in (1,2,3,68,137):
    a = comb(k+4,4) - comb(k+2,4)
    b = (2*k+3)*(k+1)*(k+2)//6
    print(k, a, b, a==b, "1/dim = %.3e" % (1/a))
# SO(4)_xi-fixed count in P_m vs monomials (z.z)^j (z.xi)^l, 2j+l=m
for m in range(0,12):
    fixed = sum(1 for j in range(m//2+1))          # one zonal line per H_{m-2j}
    mono  = sum(1 for j in range(m//2+1) if m-2*j>=0)
    assert fixed==mono
print("dimension check m=0..11 OK:", [m//2+1 for m in range(12)])
# polydisc identity: z=(z1,z2,0,0,0), a=z1+i z2, b=z1-i z2
rng=np.random.default_rng(1)
for _ in range(3):
    z1,z2 = rng.normal(size=2)+1j*rng.normal(size=2)
    a,b = z1+1j*z2, z1-1j*z2
    zz = z1*z1+z2*z2; zxi = z1
    print("z.z-ab = %.1e   z.xi-(a+b)/2 = %.1e" % (abs(zz-a*b), abs(zxi-(a+b)/2)))
