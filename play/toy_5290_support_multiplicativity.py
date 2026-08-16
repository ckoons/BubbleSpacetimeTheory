import numpy as np
from collections import Counter
print("="*92)
print("(1) WHERE DOES Re = 1/2 ACTUALLY COME FROM?  It is derivable -- and it is NOT a cone intersection.")
print("="*92)
print("  Mellin-Plancherel: for f in L^2(0,inf) with dx, F(s) = INT f(x) x^{s-1} dx satisfies")
print("      INT_0^inf |f(x)|^2 dx  =  (1/2pi) INT_-inf^inf |F(sigma + i t)|^2 dt   ONLY at sigma = 1/2.")
print("  Test it: take f, compute both sides at several sigma.")
x=np.exp(np.linspace(-12,12,200001)); dlog=np.log(x[1])-np.log(x[0])
f=np.exp(-x)*x**0.25                       # a decent L^2 function
lhs=np.trapz(np.abs(f)**2, x)
ts=np.linspace(-400,400,160001)
print("\n      sigma      (1/2pi) INT |F(sigma+it)|^2 dt        INT |f|^2 dx        ratio")
for sig in [0.30,0.45,0.50,0.55,0.70]:
    # F(s) = INT f x^{s-1} dx = INT f(x) x^s dlog(x)
    F=np.array([np.sum(f*x**(sig+1j*t)*x*dlog) for t in ts[::40]])
    rhs=np.trapz(np.abs(F)**2, ts[::40])/(2*np.pi)
    print("      %.2f          %18.6f       %14.6f     %8.4f"%(sig,rhs,lhs,rhs/lhs))
print("\n  ⟹ the isometry holds at sigma = 1/2 and FAILS at every other sigma. The 1/2 is the L^2")
print("     half-density normalisation of the MULTIPLICATIVE measure dx/x -- the unitarity axis of")
print("     the dilation group. That is a real derivation, and it is classical.")
print("  ★ BUT IT SAYS NOTHING ABOUT WHERE THE ZEROS ARE. Unitarity puts the CHARACTERS on the line;")
print("    the zeros are RESONANCES, not characters. 'Re=1/2 is self-dual' is TRUE and is NOT RH.")
print()
print("="*92)
print("(2) THE EULER-PRODUCT PRECONDITION: is the quadratic-form count MULTIPLICATIVE?")
print("="*92)
print("  RH-type theorems live on objects with EULER PRODUCTS <=> multiplicative coefficients.")
print("  r_k(n) = #{x in Z^k : |x|^2 = n}. Test a(mn) = a(m)a(n) for coprime m,n.")
def rk(k,NMAX):
    c=Counter({0:1})
    for _ in range(k):
        d=Counter()
        L=int(NMAX**0.5)+1
        for n,v in c.items():
            for j in range(-L,L+1):
                s=n+j*j
                if s<=NMAX: d[s]+=v
        c=d
    return c
NM=400
for k in [2,3,4,5,8]:
    c=rk(k,NM)
    a=lambda n: c.get(n,0)/c.get(1,1)      # normalised so a(1)=1
    bad=[]
    from math import gcd
    for m in range(2,15):
        for n in range(2,15):
            if gcd(m,n)==1 and m*n<=NM:
                if abs(a(m*n)-a(m)*a(n))>1e-9: bad.append((m,n))
    print("    k=%d : r_k(1)=%3d   multiplicative on coprime pairs? %-5s  (%d violations found)"%(
        k,c.get(1,0),len(bad)==0,len(bad)))
    if bad[:3]: print("           e.g. %s : a(mn)=%.3f  a(m)a(n)=%.3f"%(bad[0],a(bad[0][0]*bad[0][1]),a(bad[0][0])*a(bad[0][1])))
print("\n  ⟹ EVEN k are multiplicative; ODD k are NOT. And BST's cone is FIVE-dimensional -- ODD.")
print("     No multiplicativity => NO EULER PRODUCT => the RH machinery does not even start.")
print("     THIS is why a Shimura lift is needed: it is a REPAIR for the missing Euler product,")
print("     not a bonus.")
