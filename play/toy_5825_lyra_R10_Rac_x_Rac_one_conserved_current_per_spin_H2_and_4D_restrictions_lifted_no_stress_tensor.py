#!/usr/bin/env python3
"""
Lyra R10 (2026-09-26). K-type mode picture (K1653): statements are about which bilinear K-type modes sit at the
conservation weight. Invariants: lowest J-weight Delta; conservation of a spin-s symmetric primary in d dims
<=> Delta = d-2+s (then the module is the quotient by the divergence submodule at (Delta+1, s-1)).
J-graded dims only (SO(5) collapsed to dims). Predictions BEFORE the run:
 C1  chi(Rac)^2 = t^3/(1-t)^5 [scalar s=0 at 3, generic] + sum_{s>=1} t^{3+s}[dim(s) - t*dim(s-1)]/(1-t)^5
     [one CONSERVED current per spin s at 3+s]  (Flato-Fronsdal in d=5), exact to weight 40.
     dim(s) = dim SO(5) symmetric traceless rank s = (s+1)(s+2)(2s+3)/6.
 C2  CONTROL (can fail): the same sum WITHOUT the conservation subtraction does NOT match chi(Rac)^2.
 C3  Lifts above conservation, spin s, bilinear lowest weight 2*Delta_phi + s vs d-2+s:
     5D: Rac 0, H2 2 (all s); 4D restrictions: Rac|->H_{3/2}(D4) lift 1, H2|->H_{5/2}(D4) lift 3; the 4D
     singleton lambda=1 lift 0.  => in 4D neither restriction carries a conserved current or stress tensor.
"""
from fractions import Fraction as F
import sympy as sp
t=sp.symbols('t'); ok=[]
dim=lambda s:(s+1)*(s+2)*(2*s+3)//6 if s>=0 else 0
T=40
rac=sp.sqrt(t)**3*(1+t)/(1-t)**4                      # t^{3/2}(1+t)/(1-t)^4
lhs=sp.series(sp.expand(rac**2),t,0,T).removeO()
rhs=t**3/(1-t)**5+sum(t**(3+s)*(dim(s)-t*dim(s-1))/(1-t)**5 for s in range(1,T))
rhs=sp.series(rhs,t,0,T).removeO()
C1=sp.expand(lhs-rhs)==0; ok.append(C1); print("C1 Rac^2 = scalar@3 + one conserved current per spin at 3+s ->",C1)
bad=sp.series(t**3/(1-t)**5+sum(t**(3+s)*dim(s)/(1-t)**5 for s in range(1,T)),t,0,T).removeO()
C2=sp.expand(lhs-bad)!=0; ok.append(C2); print("C2 control without conservation subtraction fails ->",C2)
lift=lambda dphi,d:2*dphi-(d-2)
L={'5D Rac':lift(F(3,2),5),'5D H2':lift(F(5,2),5),'4D Rac|':lift(F(3,2),4),'4D H2|':lift(F(5,2),4),'4D singleton':lift(1,4)}
C3=L=={'5D Rac':0,'5D H2':2,'4D Rac|':1,'4D H2|':3,'4D singleton':0}; ok.append(C3); print("C3 lifts",{k:str(v) for k,v in L.items()},"->",C3)
print(f"SCORE {sum(ok)}/{len(ok)}")
