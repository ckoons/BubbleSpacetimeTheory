#!/usr/bin/env python3
"""Toy 5744 — R137 E1/E2: pin the zero of the commitment cost in nu; the sign fork between the two readings."""
import json
from fractions import Fraction as F
import sympy as sp
score=[]; cf=[]
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
n=5; NU_FLOOR=F(3,2); NU_HARDY=F(5,2); NU_BERG=F(5)
def Lnu(nu,j,k): j=F(j);k=F(k);nu=F(nu); return F(k+3,2*k+3)*(j+k+F(5,2))/(j+k+nu)
def Mnu(nu,j,k):
    if k==0: return F(0)
    j=F(j);k=F(k);nu=F(nu); return F(k,2*k+3)*(j+1)/(j+nu-F(3,2))
def cnu(nu,j,k): return 1-Lnu(nu,j,k)-Mnu(nu,j,k)
print("A1: is the zero at nu_Hardy = 5/2, and is it zero at EVERY (j,k)?")
z=[cnu(NU_HARDY,j,k) for j in range(6) for k in range(6)]
print("   c_{nu=5/2}(j,k) over j,k = 0..5:", "all exactly zero" if all(x==0 for x in z) else sorted(set(str(x) for x in z))[:5])
print("   at nu_floor = 3/2: M_nu has denominator j + nu - 3/2 = j, so (j,k) = (0,k>0) is a POLE ->", end=" ")
try:
    v=cnu(NU_FLOOR,0,1); print(f"c = {v}")
except ZeroDivisionError: print("undefined (division by zero) — the floor is singular, not a zero")
sc("A1", all(x==0 for x in z), True, "identically zero at nu_Hardy = 5/2 for all (j,k); L+M = (k+3)/(2k+3) + k/(2k+3) = 1")
print("A2: the constant across the admissible range, k = 0 line c_nu(j,0) = (nu - 5/2)/(j + nu)")
for nu in (F(5),F(4),F(3),F(5,2),F(2),F(7,4)):
    line=[cnu(nu,j,0) for j in range(4)]; pred=[(F(nu)-F(5,2))/(F(j)+F(nu)) for j in range(4)]
    print(f"   nu={str(nu):5}: constant {str(F(nu)-F(5,2)):5}  c(j,0) = {[str(x) for x in line]}  matches: {line==pred}  {'<- NEGATIVE: <|z|^2> > 1, impossible for a measure on the ball' if F(nu)<F(5,2) else ''}")
a2=all([cnu(nu,j,0) for j in range(4)]==[(F(nu)-F(5,2))/(F(j)+F(nu)) for j in range(4)] for nu in (F(5),F(4),F(3),F(5,2),F(2),F(7,4)))
sc("A2", a2, False, "positive above 5/2, zero at it, negative below it")
print("A3: where is the weight-nu norm an integral against a positive measure on D? nu > n - 1 = 4 (else no measure; nu_Hardy is L^2 on the Shilov boundary)")
sc("A3", True, False, "Born reading available at nu_Bergman = 5; not at 5/2 < nu < 4")
print("B1: the other reading — R_nu(j,k) = (nu)_{j+k}(nu-3/2)_j / [(5/2)_{j+k}(1)_j]")
def poch(a,m): return sp.prod([F(a)+i for i in range(m)]) if m else F(1)
def R(nu,j,k): return poch(nu,j+k)*poch(F(nu)-F(3,2),j)/(poch(F(5,2),j+k)*poch(1,j))
print("   R_5(j,k) at (0,0),(1,1),(2,3):", [str(R(5,j,k)) for (j,k) in ((0,0),(1,1),(2,3))], " and 1 - 1/R:", [f"{float(1-1/R(5,j,k)):.4f}" for (j,k) in ((0,0),(1,1),(2,3))], "(5721 P5: 1, 12, 12096/143; 0 -> 0.987)")
ratios_ok=True
for nu in (F(5),F(4),F(3),F(5,2),F(2)):
    rr=[R(nu,j+1,0)/R(nu,j,0) for j in range(4)]
    pred=[(F(nu)+j)*(F(nu)-F(3,2)+j)/((F(5,2)+j)*(1+j)) for j in range(4)]
    ratios_ok &= (rr==pred)
    dirn = "rises" if all(x>1 for x in rr) else ("falls" if all(x<1 for x in rr) else ("constant" if all(x==1 for x in rr) else "mixed"))
    print(f"   nu={str(nu):5}: R_nu(j+1,0)/R_nu(j,0) = {[str(x) for x in rr]}  -> {dirn}")
sc("B1", ratios_ok, True, "ratio formula exact; R_nu rises iff nu > 5/2, falls iff nu < 5/2, == 1 at 5/2")
print("B2: is there ANY admissible nu at which both readings are positive costs falling in j?")
rows=[]
for nu in [F(5),F(9,2),F(4),F(7,2),F(3),F(11,4),F(5,2),F(9,4),F(2),F(7,4)]:
    ca=[cnu(nu,j,0) for j in range(6)]; cb=[1-1/R(nu,j,0) for j in range(6)]
    a_pos=all(x>0 for x in ca); a_fall=all(ca[i]>ca[i+1] for i in range(5))
    b_pos=all(x>=0 for x in cb); b_fall=all(cb[i]>cb[i+1] for i in range(5))
    rows.append((nu,a_pos,a_fall,b_pos,b_fall))
    print(f"   nu={str(nu):5}: reading (a) positive {str(a_pos):5} falling {str(a_fall):5} | reading (b) 1-1/R positive {str(b_pos):5} falling {str(b_fall):5}")
both=[r for r in rows if r[1] and r[2] and r[3] and r[4]]
sc("B2", len(both)==0, True, f"NO admissible weight gives both as positive falling costs ({len(both)} found); above 5/2 they are exactly opposed, at 5/2 both are trivial, below 5/2 (a) is negative")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({'zero_at':'5/2','rows':[[str(r[0]),r[1],r[2],r[3],r[4]] for r in rows]}, open('.record_5744.json','w'), indent=1)
