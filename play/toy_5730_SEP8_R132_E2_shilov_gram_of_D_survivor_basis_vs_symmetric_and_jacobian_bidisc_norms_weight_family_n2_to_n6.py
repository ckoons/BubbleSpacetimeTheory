#!/usr/bin/env python3
"""Toy 5730 — E2: Gram of (z.z)^j (z.xi)^l on Š (Hardy) vs symmetric H^2(T^2) and Jacobian-weighted; weight |a-b|^{n-2} family."""
import json, itertools
from fractions import Fraction as F
import sympy as sp
score=[]; cf=[]
def sc(n, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {n}{'' if c else ' (control)'}  {d}")
phi=sp.symbols('phi', real=True)
def Mn(n_dim, p):   # ∫_{S^{n-1}} x1^p dσ (normalised)
    if p%2: return sp.Integer(0)
    return sp.gamma(sp.Rational(n_dim,2))*sp.gamma(sp.Rational(p+1,2))/(sp.gamma(sp.Rational(1,2))*sp.gamma(sp.Rational(p+n_dim,2)))
def gram_S(n_dim, m):
    """Gram of f_{jl} = e^{imt} x1^l, 2j+l=m, on Š of D_IV^n: entries M_n(l+l')."""
    basis=[(j,m-2*j) for j in range(m//2+1)]
    return basis, sp.Matrix([[sp.nsimplify(Mn(n_dim,l+l2)) for (_,l2) in basis] for (_,l) in basis])
def gram_T(m, weight_pow):
    """Gram of (ab)^j ((a+b)/2)^l on T^2 with weight |a-b|^w, a=e^{i(t+phi)}, b=e^{i(t-phi)}: f = e^{imt} cos^l(phi); weight = (2|sin phi|)^w; normalised."""
    basis=[(j,m-2*j) for j in range(m//2+1)]
    w=(2*sp.Abs(sp.sin(phi)))**weight_pow
    Z=sp.integrate(w,(phi,0,2*sp.pi)) if weight_pow>0 else 2*sp.pi
    def e(l,l2): return sp.nsimplify(sp.simplify(sp.integrate(sp.cos(phi)**(l+l2)*w,(phi,0,2*sp.pi))/Z))
    return basis, sp.Matrix([[e(l,l2) for (_,l2) in basis] for (_,l) in basis])
print("G1: isometry test, n=5: ||z.xi||^2 on Š vs ||(a+b)/2||^2 on T^2; control l=0")
b,GS=gram_S(5,1); b,GT=gram_T(1,0); print(f"  ||z.xi||^2_Š = {GS[0,0]},  ||(a+b)/2||^2_T2 = {GT[0,0]}")
ctrl=all(gram_S(5,2*j)[1][-1,-1]==1 and gram_T(2*j,0)[1][-1,-1]==1 for j in range(4))
sc("G1", GS[0,0]==sp.Rational(1,5) and GT[0,0]==sp.Rational(1,2) and ctrl, True, "1/5 vs 1/2: not an isometry; l=0 identity on both")
print("G2: Š Gram (n=5) == T^2 Gram with weight |a-b|^3, m<=6")
ok2=True
for m in range(0,7):
    b,GS=gram_S(5,m); b,GW=gram_T(m,3); eq=(GS-GW).applyfunc(sp.simplify)==sp.zeros(*GS.shape); ok2&=eq
    if m in (2,3,4): print(f"  m={m} basis {b}: Š {GS.tolist()} | T^2 weighted {GW.tolist()} | equal {eq}")
sc("G2", ok2, True, "weight |a-b|^3 reproduces the Š Gram exactly, m=0..6")
print("G3: family — Š Gram of D_IV^n == T^2 Gram with |a-b|^{n-2}, n=2..6, m<=4; literature norms: symmetric = weight 0 (n=2), Jacobian = weight 2 (n=4)")
ok3=True; rows={}
for n in range(2,7):
    eqs=[]
    for m in range(0,5):
        b,GS=gram_S(n,m); b,GW=gram_T(m,n-2); eqs.append((GS-GW).applyfunc(sp.simplify)==sp.zeros(*GS.shape))
    rows[n]=all(eqs); ok3&=rows[n]; print(f"  n={n}: weight |a-b|^{n-2}: {'exact' if rows[n] else 'FAILS'}")
b,G0=gram_T(2,0); b,G2=gram_T(2,2); b,G5=gram_S(5,2)
print(f"  n=5 vs symmetric (w=0) at m=2: Š {G5.tolist()} vs {G0.tolist()};  vs Jacobian (w=2): {G2.tolist()}")
sc("G3", ok3 and G5!=G0 and G5!=G2, True, "n=2 symmetric, n=4 Jacobian, n=5 neither")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({'family':{n:bool(v) for n,v in rows.items()}}, open('.record_5730.json','w'))
