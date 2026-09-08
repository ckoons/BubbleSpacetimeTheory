#!/usr/bin/env python3
import math, json, itertools
import sympy as sp
from fractions import Fraction as F
score=[]; cf=[]
def sc(n, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {n}{'' if c else ' (control)'}  {d}")
cells=sum(138-2*j for j in range(69)); hol=math.log2(cells); occ=(cells-1)*math.log2(138)
print(f"T1: (C) twirl capacity under 2j+k<=137: cells {cells}, Holevo {hol:.2f} bits, presence {cells-1}, occupancy 0..137: {occ:.0f} bits")
sc("T1", cells==4830, False, "hashed 4830 / 12.24 / 34,313")
rec=json.load(open('.record_5726.json'))
print("T2: chain occupancy under (C) = H(j) since k is a function of j at each stop:", {k:round(v[0],2) for k,v in rec.items()})
sc("T2", all(v[0] < hol+8 for v in rec.values()) and rec['S-m137'][0] < hol, True, "4.0 / 10.2 / 12.2 bits; (C)'s extra capacity unoccupied by one chain")
# T3: on S^4, Y_1 = x0: vector average over SO(5) is 0; twirl keeps trace 1
xs=sp.symbols('x0:5'); r2=sum(v**2 for v in xs)
def moment(alpha):
    if any(a%2 for a in alpha): return F(0)
    d=len(alpha); num=sp.gamma(sp.Rational(d,2))*sp.prod([sp.gamma(sp.Rational(a+1,2)) for a in alpha]); den=sp.gamma(sp.Rational(1,2))**d*sp.gamma(sp.Rational(sum(alpha)+d,2)); r=sp.nsimplify(num/den); return F(int(r.p),int(r.q))
avg_Y1 = moment((1,0,0,0,0))     # <x0> over S^4 = the SO(5)-average of Y1 (a constant function) 
tr_twirl = moment((2,0,0,0,0))*5  # trace of twirled |Y1><Y1| in the S^4-normalised basis: sum_i <x_i^2> = 1
print(f"T3: SO(5)-average of Y1=x0 as a function: {avg_Y1}; trace of twirl(|Y1><Y1|): {tr_twirl}")
sc("T3", avg_Y1==0 and tr_twirl==1, False, "projection 0, twirl trace 1")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c)}/{sum(cf)} can-fail hit")
json.dump({'cells':cells,'holevo':hol,'occupancy_bits':occ}, open('.record_5727.json','w'), indent=1)
