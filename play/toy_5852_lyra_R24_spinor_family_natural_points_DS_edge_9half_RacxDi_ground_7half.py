#!/usr/bin/env python3
"""
Lyra R24 (2026-09-30). Group: SO_0(5,2), g_C = so(7,C) = B3. Compact Cartan coords (e1 = the SO(2) clock, e2,e3 = SO(5)).
Roots: +-e_i +- e_j, +-e_i. Compact = those without e1 (B2 = so(5)). Holomorphic positive noncompact p+ = {e1+-e2, e1+-e3, e1}
(5 roots = dim_C D_IV^5). rho(B3) = (5/2, 3/2, 1/2).  Convention: a highest-weight module with lowest K-type of SO(5) highest
weight mu and clock weight lambda has Lambda = (-lambda, mu).  Harish-Chandra: holomorphic discrete series iff
<Lambda + rho, beta> < 0 for all beta in p+.  Predictions BEFORE the run:
 N1 CONTROL scalar (mu = 0): DS iff lambda > 4 = p - 1 (genus p = 5).  N2 spinor (mu = (1/2,1/2)): DS iff lambda > 9/2.
 N3 the shift-by-1/2 table of natural points: scalar {Wallach 3/2, Hardy 5/2, DS edge 4, Bergman 5} ; spinor {Di 2 (standard, K956),
    Hardy-analog 3 (shift, NOT derived here), DS edge 9/2 (computed), Bergman-analog 11/2 (shift, not derived)} : 7/2 is NOT among them.
 N4 Rac (x) Di: lowest K-type = trivial (x) spinor = spinor, lowest clock weight 3/2 + 2 = 7/2; z_t(7/2) = -1 = z_s(spinor): matched.
 N5 (flagged coincidence, NOT used): 2*(7/2) = (n-2)+(n-1) = 2n-3 equals n+rank = n+2 only at n = 5.
"""
from fractions import Fraction as F
import itertools
ok=[]
rho=(F(5,2),F(3,2),F(1,2))
pplus=[(1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(1,0,0)]
def ds_threshold(mu):
    # smallest lambda with <(-lam,mu)+rho, beta> < 0 for all beta: need lam > max_beta ( <(0,mu)+rho,beta> ) / beta_1
    best=None
    for b in pplus:
        val=sum(((F(0) if i==0 else mu[i-1])+rho[i])*b[i] for i in range(3))   # <(0,mu)+rho, b>, with b_1 = 1
        best=val if best is None else max(best,val)
    return best
t0=ds_threshold((F(0),F(0))); t1=ds_threshold((F(1,2),F(1,2)))
N1=t0==4; N2=t1==F(9,2); ok+= [N1,N2]
print("N1 scalar DS threshold",t0,"->",N1,"; N2 spinor DS threshold",t1,"->",N2)
spin=[F(2),F(3),t1,F(11,2)]; N3=F(7,2) not in spin and F(7,2) not in [F(3,2),F(5,2),F(4),F(5)]
ok.append(N3); print("N3 natural spinor points",[str(x) for x in spin],"; 7/2 among them?",F(7,2) in spin,"->",N3)
g0=F(3,2)+F(2); import cmath
zt=round(cmath.exp(2j*cmath.pi*float(g0)).real); N4=(g0==F(7,2)) and zt==-1
ok.append(N4); print("N4 Rac x Di ground weight",g0,"z_t =",zt,"= z_s(spinor) = -1 ->",N4)
N5=all(((2*n-3)==(n+2))==(n==5) for n in range(3,12)); ok.append(N5); print("N5 2n-3 = n+2 only at n=5 (flag, not used) ->",N5)
print(f"SCORE {sum(ok)}/{len(ok)}")
