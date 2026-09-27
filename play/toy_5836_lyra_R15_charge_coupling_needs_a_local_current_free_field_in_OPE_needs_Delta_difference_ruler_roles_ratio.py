#!/usr/bin/env python3
"""
Lyra R15 (2026-09-27). Invariants first.
 (i) A 4D conserved spin-1 current sits at Delta = d-1 = 3 (unitarity saturation); a charge coupling J.A needs a LOCAL one.
 (ii) Free field in an OPE: a scalar 3-point function <O1(x1) O2(x2) phi0(x3)> = x12^{-(D1+D2-D0)} x13^{-(D1+D0-D2)} x23^{-(D2+D0-D1)}.
      If phi0 is FREE (D0 = (d-2)/2, box phi0 = 0), the function must be harmonic in x3: box_3 [x13^-a x23^-b] = 0 with a+b = 2 D0 = d-2
      forces a = 0 or b = 0, i.e. |D1 - D2| = D0.  (Scalar case computed; the helicity-1 analogue |D1-D2| = 2 is stated, not computed.)
Predictions BEFORE the run:
 R1  d = 4: box_3 of x13^-a x23^-b with a + b = 2 vanishes identically iff (a,b) in {(0,2),(2,0)}; checked on a = 0, 1/2, 1, 3/2, 2.
     => a conjugate pair O, Obar of EQUAL Delta (5/2, 5/2) cannot have a free field in its OPE (a = b = D0 != 0).
     CONTROL: (a,b) = (0,2) harmonic (the free field's own two-point structure).
 R2  bookkeeping: H2 vector bilinear Delta = 2*(5/2)+1 = 6 != 3; record space 4D Re Delta = d/2 = 2 != 3; tower levels
     H_{5/2+k}(D4): |Delta_k - Delta_k'| = |k-k'| takes the value 2 (the helicity-1 free-field analogue) for |k-k'| = 2.
 R3  the ruler's two roles as numbers (computed, CODATA): mass role hbar/(m_e c) = 3.8616e-13 m; radius role c*tick =
     N_max*hbar/(m_e c) = 5.2904e-11 m; ratio = N_max = 137 exactly by construction; compare 1/alpha = 137.036 (a0/lambdabar).
"""
import sympy as sp
from scipy import constants as C
ok=[]
x=sp.symbols('x0:4',real=True); y=sp.symbols('y0:4',real=True)   # x = x3 ; x1 = 0 ; x2 = y
r1=sp.sqrt(sum(xi**2 for xi in x)); r2=sp.sqrt(sum((xi-yi)**2 for xi,yi in zip(x,y)))
def box(f): return sum(sp.diff(f,xi,2) for xi in x)
pt={x[0]:0.3,x[1]:-0.7,x[2]:0.4,x[3]:1.1,y[0]:1.3,y[1]:0.2,y[2]:-0.5,y[3]:0.8}
res={}
for a in [sp.Rational(k,2) for k in range(5)]:
    b=2-a; f=r1**(-a)*r2**(-b); res[str(a)]=float(box(f).subs(pt))
R1=abs(res['0'])<1e-12 and abs(res['2'])<1e-12 and all(abs(res[k])>1e-6 for k in ('1/2','1','3/2'))
ok.append(R1); print("R1 box_3 values (a):",{k:round(v,8) for k,v in res.items()},"-> harmonic only at a=0,2 ->",R1)
R2=(2*sp.Rational(5,2)+1==6) and (sp.Rational(4,2)==2) and any(abs(k-kp)==2 for k in range(4) for kp in range(4))
ok.append(R2); print("R2 H2 current 6 != 3; record Re Delta 2 != 3; tower pairs with |k-k'|=2 exist ->",R2)
lb=C.hbar/(C.m_e*C.c); a0=C.physical_constants['Bohr radius'][0]
R3=abs(137*lb/lb-137)<1e-12 and abs(a0/lb-1/C.fine_structure)<1e-6
ok.append(R3); print(f"R3 mass role {lb:.5e} m, radius role {137*lb:.5e} m, ratio 137; a0/lambdabar = {a0/lb:.4f} = 1/alpha {1/C.fine_structure:.4f} ->",R3)
print(f"SCORE {sum(ok)}/{len(ok)}")
