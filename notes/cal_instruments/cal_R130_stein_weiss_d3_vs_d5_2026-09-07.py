# Cal: Stein–Weiss branching of a coordinate write (v·x)Y_k on S^{d-1}: frame-averaged norm fraction of the radial ("matter") piece
# r^2 ∂_v Y_k/(2k+d-2), by exact polynomial integration. Prediction (§898): d = 3 -> l/(2l+1) (QM's dipole l->l-1 weight); d = 5 -> k/(2k+3).
import sympy as sp
from sympy import Rational as R, binomial
def sphere_mean(exps):
    if any(e%2 for e in exps): return sp.Integer(0)
    d=len(exps); s=sum(exps)
    return sp.gamma(R(d,2))/sp.gamma(R(s+d,2))*sp.prod([sp.gamma(R(e+1,2))/sp.gamma(R(1,2)) for e in exps])
def inner(p,q,xs):
    poly=sp.Poly(sp.expand(p*q),*xs); return sp.simplify(sum(c*sphere_mean(mon) for mon,c in poly.terms()))
def Yk(xs,k):  # Re (x1 + i x2)^k, harmonic in every dimension
    return sp.expand(sum(binomial(k,j)*xs[0]**(k-j)*xs[1]**j*(-1)**(j//2) for j in range(0,k+1,2)))
def matter_fraction(d,k):
    xs=sp.symbols('x1:%d'%(d+1),real=True); Y=Yk(xs,k); r2=sum(x*x for x in xs)
    num=sp.Integer(0); den=sp.Integer(0)
    for v in xs:
        w=sp.expand(v*Y); m=sp.expand(r2*sp.diff(Y,v)/(2*k+d-2))
        num+=inner(m,m,xs); den+=inner(w,w,xs)
    return sp.nsimplify(sp.simplify(num/den))
for d in (3,5):
    print(f"d = {d}: computed", [(k, matter_fraction(d,k)) for k in (1,2,3)], " formula k/(2k+d-2):", [sp.Rational(k,2*k+d-2) for k in (1,2,3)])
