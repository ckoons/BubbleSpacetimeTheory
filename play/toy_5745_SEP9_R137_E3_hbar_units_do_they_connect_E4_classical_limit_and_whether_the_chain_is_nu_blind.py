#!/usr/bin/env python3
"""Toy 5745 — R137 E3/E4: does nu connect to a physical hbar, and what happens in the classical limit."""
import json
from fractions import Fraction as F
score=[]; cf=[]
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
def Lnu(nu,j,k): j=F(j);k=F(k);nu=F(nu); return F(k+3,2*k+3)*(j+k+F(5,2))/(j+k+nu)
def Mnu(nu,j,k):
    if k==0: return F(0)
    j=F(j);k=F(k);nu=F(nu); return F(k,2*k+3)*(j+1)/(j+nu-F(3,2))
def cnu(nu,j,k): return 1-Lnu(nu,j,k)-Mnu(nu,j,k)
HBAR=1.054571817e-34
print("C1: the Berezin parameter is dimensionless; the physical hbar is not")
for nu in (F(5),F(5,2)):
    print(f"   nu = {nu}: hbar_Berezin = 1/nu = {float(1/nu):.4f} (dimensionless, order one — maximally quantum)")
print(f"   physical hbar = {HBAR:.6e} J s;  1/hbar in SI = {1/HBAR:.4e}")
print(f"   gap between nu_Bergman = 5 and 1/hbar_SI: factor {1/HBAR/5:.3e}")
print("   To equate them the domain needs an ACTION unit. The corpus's own floor (T2623 negative row; K1879) says there is")
print("   no record->spacetime map, no momentum and no energy in the dictionary — so no action unit exists to fix one.")
sc("C1", True, False, "the units do not connect; the SI gap is ~2e33 and unbridged by anything in the corpus")
print("C2: if the reading were inherited literally — two rows at nu = 5 and nu = 5/2 assert two Berezin constants in ratio 2")
print("   A factor 2 in a physical hbar rescales every atomic transition; the Rydberg constant is measured to ~1e-12 relative.")
print("   So the literal inheritance is excluded by about twelve orders of magnitude. The surviving reading is TWO SPACES, not two values.")
sc("C2", True, False, "literal two-hbar reading is dead on arrival; the collision is of spaces")
print("D1: the classical limit nu -> infinity")
for nu in (5,50,500,5000,50000):
    print(f"   nu = {nu:6}: c_nu(0,0) = {float(cnu(nu,0,0)):.6f}   c_nu(1,1) = {float(cnu(nu,1,1)):.6f}   <|z|^2> at (0,0) = {float(1-cnu(nu,0,0)):.6f}")
d1 = float(cnu(50000,0,0))>0.9999 and float(cnu(50000,1,1))>0.999
sc("D1", d1, False, "c_nu -> 1 and <|z|^2> -> 0: the states concentrate at the origin, the coherent-state classical limit")
print("D2: is the write branching nu-independent, as I hashed?")
print("   the NORM split at weight nu: M_nu/(L_nu+M_nu) at k = 1, j = 0:")
splits=[(nu, Mnu(nu,0,1)/(Lnu(nu,0,1)+Mnu(nu,0,1))) for nu in (F(5),F(4),F(3),F(5,2),F(2))]
for nu,s in splits: print(f"     nu = {str(nu):5}: {str(s):12} = {float(s):.5f}")
moves = len(set(splits and [s for _,s in splits]))>1
print(f"   the norm split MOVES with nu: {moves}  -> my hashed reason ('the branching is nu-independent') is WRONG as stated.")
print("   What is true, and it is sharper: at nu = 5/2 exactly, L = (k+3)/(2k+3) and M = k/(2k+3) — which ARE K1860-A's branching")
hardy_is_branching = all(Lnu(F(5,2),j,k)==F(k+3,2*k+3) and Mnu(F(5,2),j,k)==F(k,2*k+3) for j in range(4) for k in range(1,5))
print(f"   probabilities, at every (j,k): {hardy_is_branching}. So the corpus's write chain is ALREADY NORMALISED AT THE HARDY POINT,")
print("   and the push cost is a Bergman-point object. The two weights are not in two rows — they are in one sentence.")
sc("D2", not moves, True, f"MISS as hashed: the norm split moves with nu ({[f'{float(s):.4f}' for _,s in splits]}); the branching is nu-free only because it IS the nu = 5/2 split — the chain lives at the Hardy point")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({'splits':[[str(a),str(b)] for a,b in splits],'classical':[float(cnu(nu,0,0)) for nu in (5,50,500,5000,50000)]}, open('.record_5745.json','w'), indent=1)
