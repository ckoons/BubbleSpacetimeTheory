# Cal: the 2-adic rank-one intertwining integral for the CORPUS lattice <1,-1> + I_3 (odd at 2), vs the even model H + I_3.
# Odd lattice, null coords: Q = 4ab + q0(v), l1=(1,0), l2=(0,1); w = n(v) l2 = l2 + v - (q0(v)/4) l1; in lattice coords (x,y,v):
#   x = 1 - q0/4, y = -1 - q0/4.  Norm = max(|1-q0/4|_2, |1+q0/4|_2, |v|_2).  c(sigma) = int ||w(v)||^{-sigma} dv.
# Exact finite sum: v in 2^{-M} Z_2^3 / 2^N Z_2^3 (cells of measure 2^{-3N}); beyond |v|>2^M the tail is (8 y^2)^{M+1}-small.
from fractions import Fraction as F
import itertools, math
def v2(n):
    if n==0: return 10**9
    c=0
    while n%2==0: n//=2; c+=1
    return c
def absval(fr):  # 2-adic absolute value of a Fraction
    if fr==0: return 0.0
    return 2.0**(v2(fr.denominator)-v2(fr.numerator))
def c_odd(sigma,M=4,N=3):
    tot=0.0; step=F(1,2**M); cells=2**(M+N)
    for ijk in itertools.product(range(cells),repeat=3):
        v=[F(t,2**M) for t in ijk]
        q=sum(t*t for t in v)
        nv=max(absval(t) for t in v)
        nrm=max(absval(1-q/4),absval(1+q/4),nv)
        tot+=nrm**(-sigma)
    return tot*2.0**(-3*N)
def c_odd_closed(sigma):
    y=2.0**(-sigma)
    return (1-y)*(1+2*y)/(16*y*(1-8*y*y))
for s in (3.5,4.0,5.0):
    print(f"sigma={s}: odd-lattice integral {c_odd(s):.6f}  closed form {c_odd_closed(s):.6f}")
