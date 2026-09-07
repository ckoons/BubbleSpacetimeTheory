# Cal: which ternary is the MAXIMAL ORDER's trace-zero lattice, and which comb does it give? Direct computation, both primes.
# Maximal order of (-1,-3)_Q: O = Z<1, i, (1+j)/2, (i+k)/2>. Trace-zero elements: (b + d/2) i - a j + (d/2) k, a,b,d in Z; reduced norm
#   q3(a,b,d) = b^2 + b d + d^2 + 3 a^2   (Gram det 9/4 -> discriminant class 9 ~ 1 in Q_3*/Q_3*^2, NOT 3).
# Candidates at p=3: <1,1,3> (Lyra L10), <1,3,3> (Cal §865), q3 (maximal order). At p=5: <1,1,5>, <1,5,5>, Lyra's q5 = 2x^2+2y^2+2z^2-xy-yz-zx (maximal order, prereg de24bf05).
# For each: a = P(p | q(u), u primitive), the rational function c_p(y), and the comb of c_p/GK: Steinberg iff a = 1/(p^2+p+1).
from fractions import Fraction as F
import sympy as sp
def count(form,p,k):
    if k==0: return 1
    M=p**k; c=0
    for x in range(M):
        for y in range(M):
            for z in range(M):
                if form(x,y,z)%M==0: c+=1
    return c
def a_of(form,p):
    ps=[]
    for j in range(0,3):
        tot=count(form,p,j); nonprim=count(form,p,j-2)*p**3 if j>=2 else (1 if j==1 else 0)
        ps.append(F(tot-nonprim,(p**3-1)*(p**3)**(j-1)) if j>=1 else F(1))
    return ps
forms={3:{"<1,1,3> (Lyra L10)":lambda x,y,z:x*x+y*y+3*z*z, "<1,3,3> (Cal §865)":lambda x,y,z:x*x+3*y*y+3*z*z, "maximal order q3=b^2+bd+d^2+3a^2":lambda a,b,d:b*b+b*d+d*d+3*a*a},
       5:{"<1,1,5>":lambda x,y,z:x*x+y*y+5*z*z, "<1,5,5>":lambda x,y,z:x*x+5*y*y+5*z*z, "Lyra q5 (maximal order)":lambda x,y,z:2*x*x+2*y*y+2*z*z-x*y-y*z-z*x}}
y=sp.symbols('y')
for p in (3,5):
    print(f"=== p = {p}: Steinberg iff a = 1/(p^2+p+1) = 1/{p*p+p+1} ===")
    for name,form in forms[p].items():
        ps=a_of(form,p)
        if ps[2]!=0:
            print(f"  {name}: P(val>=1)={ps[1]}, P(val>=2)={ps[2]} -> isotropic or val>1: not the anisotropic maximal case; skipped")
            continue
        a=ps[1]; B=1+(p**3-1)*a
        # c = (1-y)(1+B y)/(1-p^3 y^2); R = c/GK = Steinberg * (1+B y)/(1+p y)
        verdict = "STEINBERG (2π/ln p)" if B==p else f"partner survives: comb at π/ln {p} (all k)"
        print(f"  {name}: a = {a}, B = {B}; c_p = (1-y)(1+{B}y)/(1-{p**3}y^2) -> {verdict}")
