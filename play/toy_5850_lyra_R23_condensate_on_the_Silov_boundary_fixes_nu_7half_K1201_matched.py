#!/usr/bin/env python3
"""
Lyra R23 (2026-09-29). Group/source: D_IV^5 Lie ball; generic norm h(z,w) = 1 - 2 z.conj(w) + (z.z) conj(w.w) (Faraut-Koranyi).
Silov boundary = the maximal tripotents u = e^{i theta} x, x in S^4 (real unit) (Loos; Lyra R5 item 9, Cal S990). The condensate O
is 'on the Shilov boundary' (K1197, verbatim). Coherent-state amplitude of a scalar H_nu module: A(z) = h(z,z)^(nu/2) (R22, toy 5849).
Predictions BEFORE the run:
 S1 for z = t u, u = e^{i theta} x a Silov point: h = (1 - t^2)^2 for every theta (checked at theta = 0, 0.4, pi/3, 1.1).
 S2 K1201's gap 1 - t^2 = 1/n_C^2 = 1/25 and matched Yukawa 5^-7: along the Silov ray A = (1/25)^nu = 5^-7 => nu = 7/2 exactly.
    CONTROL (rank-one tripotent e = (x0 + i y0)/2): A = (1/25)^(nu/2) = 5^-7 => nu = 7.
 S3 nu = 7/2 is half-odd => a spinor mode at nu = 7/2 is clock-spin MATCHED (z_t = z_s = -1); nu = 7 would be mismatched.
"""
import sympy as sp
t,th=sp.symbols('t theta',real=True); ok=[]
def h(z,w): return 1-2*sum(a*sp.conjugate(b) for a,b in zip(z,w))+sum(a*a for a in z)*sp.conjugate(sum(b*b for b in w))
S1=True
for th0 in (0,sp.Rational(2,5),sp.pi/3,sp.Rational(11,10)):
    u=[sp.exp(sp.I*th0),0,0,0,0]; z=[t*c for c in u]
    S1&= sp.simplify(sp.expand(h(z,z))-(1-t**2)**2)==0
ok.append(S1); print("S1 h(tu,tu) = (1-t^2)^2 for Silov points at several phases ->",S1)
nu=sp.symbols('nu',positive=True)
sil=sp.solve(sp.Eq(sp.Rational(1,25)**nu,sp.Integer(5)**-7),nu); r1=sp.solve(sp.Eq(sp.Rational(1,25)**(nu/2),sp.Integer(5)**-7),nu)
S2=sil==[sp.Rational(7,2)] and r1==[7]; ok.append(S2); print("S2 Silov ray nu =",sil,"; rank-one control nu =",r1,"->",S2)
zt=lambda n: sp.exp(2*sp.pi*sp.I*n)
S3=sp.simplify(zt(sp.Rational(7,2)))==-1 and sp.simplify(zt(7))==1; ok.append(S3); print("S3 z_t(7/2) = -1 = z_s(spinor): matched; z_t(7) = +1: mismatched ->",S3)
print(f"SCORE {sum(ok)}/{len(ok)}")
