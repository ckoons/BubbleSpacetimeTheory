# Cal, C11 instrument: rank-one intertwining integral at p = 3 for the kernel q0 = x^2 + 3y^2 + 3z^2 (trace-zero norm form of (-1,-3)_Q,
# ramified at {3, inf}; anisotropic at 3), even planes H over Z_3 (hyperspecial), sigma = lambda + 3/2. Same method as cal_cfac2 (§854) at p = 3.
# Also the 2-adic side: at 2 this kernel is isotropic, so with EVEN planes the 2-factor is the split GK one (no comb); with ODD planes <1,-1>
# the §861 n=3-type level comb persists. Here: the 3-adic factor.
from fractions import Fraction as F
p=3; K=8
def dist(k, coeffs):
    M=p**k; d={0:1}
    for c in coeffs:
        nd={}
        sq={}
        for a in range(M): sq[(c*a*a)%M]=sq.get((c*a*a)%M,0)+1
        for r,cnt in d.items():
            for s,cs in sq.items(): nd[(r+s)%M]=nd.get((r+s)%M,0)+cnt*cs
        d=nd
    return d
def zero_count(k,coeffs):
    return 1 if k==0 else dist(k,coeffs).get(0,0)
def prim_frac(j,coeffs):
    m=3
    if j==0: return F(1)
    total=zero_count(j,coeffs)
    nonprim = zero_count(j-2,coeffs)*p**m if j>=2 else 1
    return F(total-nonprim,(p**m-1)*(p**m)**(j-1))
coeffs=(1,3,3)
ps=[prim_frac(j,coeffs) for j in range(K)]
print("q0 = x^2+3y^2+3z^2 over Z_3: P(val>=j | primitive) =",[str(x) for x in ps])
pj=[ps[j]-ps[j+1] for j in range(K-1)]
# integral: c_3(sigma)=1+sum_{m>=1} mu_m * sum_j p_j * max(3^m, 3^{2m-j})^{-sigma}, mu_m = 3^{3m}(1-3^{-3}); y = 3^{-sigma}
# closed form via geometric sums per j (finite support assumed for anisotropic kernel):
assert ps[K-1]==0, "not finite support"
import sympy as sp
y=sp.symbols('y')
c=sp.Integer(1)
for j,pjv in enumerate(pj):
    if pjv==0: continue
    # for m>=1 and j<=1<=m: max = 3^{2m-j}; general: if j<=m: e=2m-j else e=m
    # split the m-sum: m>=j (or m>=1 if j<=1): term 27^m * y^{2m-j}; m<j: term 27^m * y^m
    m0=max(1,j)
    tail=sum(sp.Integer(27)**m * y**(2*m-j) for m in range(m0, 0)) # placeholder (empty)
    geo = (sp.Integer(27)*y**2)**m0 / (1-27*y**2) * y**(-j)
    head=sum(sp.Integer(27)**m * y**m for m in range(1,m0))
    c += sp.Rational(26,27)*sp.Rational(pjv.numerator,pjv.denominator)*(geo+head)
c=sp.factor(sp.simplify(c))
print("c_3(y) =",c)
z=sp.symbols('z')  # z = 3^{-lambda}; y = 3^{-sigma} = z * 3^{-3/2}
c_z=sp.factor(sp.simplify(c.subs(y, z*sp.Rational(1,1)/sp.sqrt(27))))
print("in z = 3^{-lambda}: c_3 =", c_z)
