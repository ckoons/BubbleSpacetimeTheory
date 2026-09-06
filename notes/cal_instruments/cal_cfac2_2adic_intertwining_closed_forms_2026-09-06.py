# Numerical check of the closed forms for the 2-adic intertwining integral c_2(sigma) = int_{V0} max(1,|v|,|q0(v)|)^{-sigma} dv
# using the exact valuation distributions: aniso P(j=0)=4/7,P(j=1)=3/7 ; split P(j=0)=4/7, P(j=i)=(3/7)2^{-i}, i>=1.
from fractions import Fraction as F
def c_num(sigma, split, M=60, J=60):
    tot=1.0
    for m in range(1,M+1):
        mu=(7/8)*8**m
        if not split:
            E=(4/7)*2**(-2*m*sigma)+(3/7)*2**(-(2*m-1)*sigma)
        else:
            E=(4/7)*2**(-2*m*sigma)
            for i in range(1,J):
                p=(3/7)*2**(-i)
                E+=p*max(2**m,2**(2*m-i))**(-sigma)
        tot+=mu*E
    return tot
def c_closed(sigma, split):
    y=2**(-sigma)
    if not split: return (1+4*y)*(1-y)/(1-8*y*y)
    return (1-y)*(1-2*y)*(1+2*y)/((1-8*y*y)*(1-4*y))
for sigma in (2.3,2.7,3.1,4.0):
    print(f"sigma={sigma}: aniso num {c_num(sigma,False):.10f} closed {c_closed(sigma,False):.10f} | split num {c_num(sigma,True):.10f} closed {c_closed(sigma,True):.10f}")
# GK split-place factor in lambda with the dictionary sigma = lambda + 3/2
import math
def gk_split(lam):
    z=2**(-lam)
    return (1-z*z/2)*(1-z/2**1.5)/((1-z*z)*(1-math.sqrt(2)*z))
for lam in (0.7,1.1,2.0):
    print(f"lambda={lam}: GK split {gk_split(lam):.10f}  my split integral {c_closed(lam+1.5,True):.10f}")
