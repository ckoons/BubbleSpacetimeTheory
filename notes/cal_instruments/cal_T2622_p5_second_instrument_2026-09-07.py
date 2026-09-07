# Cal: second instrument for T2622 at p = 5 on LYRA'S pinned lattice (prereg de24bf05): K5 = maximal-order trace-zero lattice of (-2,-5)_Q,
# q5(x,y,z) = 2x^2+2y^2+2z^2 - xy - yz - zx, planes hyperbolic over Z_5 (odd p). Rank-one intertwining integral c_5(sigma) = int max(1,|w|,|q5(w)|)^{-sigma},
# sigma = lambda + 3/2 (dictionary validated at p = 2, 3). Exact rational function in y = 5^{-sigma}; correction vs split GK at 5; comb read off.
from fractions import Fraction as F
import sympy as sp, itertools
p=5
def q(x,y,z): return 2*x*x+2*y*y+2*z*z-x*y-y*z-z*x
def zero_count(k):
    if k==0: return 1
    M=p**k; c=0
    for x in range(M):
        for y in range(M):
            base=2*x*x+2*y*y-x*y
            for z in range(M):
                if (base+2*z*z-y*z-z*x)%M==0: c+=1
    return c
def prim_frac(j):
    if j==0: return F(1)
    total=zero_count(j); nonprim=zero_count(j-2)*p**3 if j>=2 else 1
    return F(total-nonprim,(p**3-1)*(p**3)**(j-1))
ps=[prim_frac(j) for j in range(0,4)]
print("q5 over Z_5: P(val>=j | primitive) j=0..3:",[str(v) for v in ps])
assert ps[3]==0 and ps[2]==0, "expected val<=1 for the anisotropic maximal lattice"
pj=[ps[0]-ps[1], ps[1]]
y=sp.symbols('y')
# shells m>=1: measure p^{3m}(1-p^{-3}); j in {0,1}: norm p^{2m-j} (>= p^m for m>=1)
c=sp.Integer(1)
for j,pjv in enumerate(pj):
    c+= sp.Rational(p**3-1,p**3)*sp.Rational(pjv.numerator,pjv.denominator)*( (sp.Integer(p**3)*y**2)/(1-sp.Integer(p**3)*y**2) )*y**(-j)
c=sp.factor(sp.simplify(c))
print("c_5(y) =",c)
z=sp.symbols('z')  # z = 5^{-lambda}; y = z*5^{-3/2}
c_z=sp.simplify(c.subs(y, z/(p*sp.sqrt(p))))
GK=(1-z**2/p)*(1-z/(p*sp.sqrt(p)))/((1-z**2)*(1-sp.sqrt(p)*z))
R=sp.factor(sp.simplify(c_z/GK))
print("R(z) = c_5 / GK_split (z = 5^{-lambda}) =",R)
# Steinberg candidate: (1 - 5^{1/2-lambda})/(1 - 5^{-1/2-lambda}) = (1 - sqrt5 z)/(1 - z/sqrt5)
St=(1-sp.sqrt(p)*z)/(1-z/sp.sqrt(p))
print("R / Steinberg =", sp.factor(sp.simplify(R/St)))
