#!/usr/bin/env python3
"""Toy 5725 — E1: capacity of the winding spectrum under 2j <= 137, by named rules; Hardy norms of (z.z)^j."""
import math, json, os
from fractions import Fraction as F
import sympy as sp
score=[]; cf=[]
def sc(n, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {n}{'' if c else ' (not can-fail)'}  {d}")
NMAX=137; modes=[j for j in range(0, NMAX+1) if 2*j<=NMAX]; n=len(modes)
print(f"H1: modes j with 2j<=137: j=0..{modes[-1]} -> {n} modes = {n-1} + vacuum")
sc("H1", n==69, False, "69 = 68 + vacuum (Keeper's figure)")
R0=math.log2(n); R1=n-1; R2=(n-1)*math.log2(NMAX+1); R3_params=2*(n-1); bits_needed=1e4/R3_params
print(f"H2: R0 Holevo log2(69) = {R0:.3f} bits; R1 presence = {R1} bits; R2 occupancy 0..137 = {R2:.1f} bits; R3 real params = {R3_params}, per-param resolution for 1e4 bits = {bits_needed:.1f} bits = 2^-{bits_needed:.1f}")
sc("H2", True, False, f"range {R0:.1f} .. {R2:.0f} bits; 1e4 only at {bits_needed:.1f} bits/parameter")
# H3: Hardy norms of (z.z)^j on the Shilov boundary S = (S^1 x S^4)/Z2: z = e^{i t} x, x in S^4 -> z.z = e^{2it}, |z.z|=1 -> every winding has Hardy norm 1 (!) ; and Bergman norms via the 5722 Gram instrument
print("H3: Hardy norms of (z.z)^j on Š: z = e^{it} x, |x|=1 => |z.z|^2 = 1 => ||(z.z)^j||_H2 = 1 for every j (exact, by the parametrisation)")
# Bergman norms ratio via kernel Gram (reuse 5722 machinery)
src=open([f for f in os.listdir('.') if f.startswith('toy_5722_')][0]).read(); _sc, _score, _cf = sc, score, cf; exec(src.split('t0 = time.time()')[0]); sc, score, cf = _sc, _score, _cf
zs=sp.symbols('z0:5'); zz=sum(v**2 for v in zs)
bn={}
for j in range(0,5):
    pd=poly_dict(sp.expand(zz**j), zs); bn[j]=norm2(pd,5,2*j)
rat={j: bn[j]/bn[0] for j in bn}
print("  Bergman norm ratios ||(z.z)^j||^2/||1||^2 (kernel-Gram, exact):", {j:str(v) for j,v in rat.items()})
hardy_equal=True
sc("H3", hardy_equal and all(rat[j]!=rat[0] for j in range(1,5)), True, "Hardy norms all equal (=1 on Š); Bergman norms differ — 'one bit per mode' is the Hardy normalisation's, not the Bergman's; a seam, printed")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c)}/{sum(cf)} can-fail hit")
json.dump({'modes':n,'R0':R0,'R1':R1,'R2':R2,'R3_params':R3_params,'bits_per_param_for_1e4':bits_needed,'bergman_ratios':{j:str(v) for j,v in rat.items()}}, open('.record_5725.json','w'), indent=1)
