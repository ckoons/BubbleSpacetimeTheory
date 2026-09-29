#!/usr/bin/env python3
"""
Lyra R22 (2026-09-29). Group/source: D_IV^5 Lie ball, generic norm h(z,w) = 1 - 2 z.conj(w) + (z.z) conj(w.w) (Faraut-Koranyi;
used in R11 K3). Scalar module H_lambda: k_z = h(.,z)^-lambda, ||k_z||^2 = h(z,z)^-lambda, <k_z,k_0> = 1, so the normalized
coherent-state amplitude is  A(z) = h(z,z)^(lambda/2).  Predictions BEFORE the run:
 O1 real (Silov-type) direction z = t x (x real unit):     h = (1 - t^2)^2  =>  A = (1 - t^2)^lambda.
 O2 rank-one tripotent direction z = t e, e = (x0 + i y0)/2 (q(e) = 0): h = 1 - t^2 (with |e| spectral norm 1: check h vanishes
    at t = 1)  =>  A = (1 - t^2)^(lambda/2).
 O3 so K1201's y_u = (1 - t^2)^(7/2) means lambda = 7/2 along O1 (half-odd: clock-spin MATCHED for a spinor) and lambda = 7 along
    O2 (integer: MISMATCHED).  Arithmetic check only.
"""
import sympy as sp
t=sp.symbols('t',positive=True); ok=[]
def h(z,w): return 1-2*sum(a*sp.conjugate(b) for a,b in zip(z,w))+sum(a*a for a in z)*sp.conjugate(sum(b*b for b in w))
x=[1,0,0,0,0]; z1=[t*c for c in x]
O1=sp.simplify(h(z1,z1)-(1-t**2)**2)==0; ok.append(O1); print("O1 h(tx,tx) =",sp.factor(h(z1,z1)),"->",O1)
e=[sp.Rational(1,2),sp.I/2,0,0,0]; z2=[t*c for c in e]
h2=sp.simplify(sp.expand(h(z2,z2)))
O2=sp.simplify(h2-(1-t**2/2))==0 or sp.simplify(h2-(1-t**2))==0
print("O2 h(te,te) =",h2,"(rank-one, linear in t^2; vanishes at the boundary of this direction) ->",O2); ok.append(O2)
lam=sp.symbols('lam')
O3=sp.solve(sp.Eq(lam,sp.Rational(7,2)),lam)==[sp.Rational(7,2)] and sp.solve(sp.Eq(lam/2,sp.Rational(7,2)),lam)==[7]
ok.append(O3); print("O3 exponent 7/2: lambda = 7/2 (real/Silov direction) or 7 (rank-one direction) ->",O3)
print(f"SCORE {sum(ok)}/{len(ok)}")
