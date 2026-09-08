#!/usr/bin/env python3
import json
tH=13.8e9; invtH=1/tH
score=[]; cf=[]
def sc(n, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {n}{'' if c else ' (control)'}  {d}")
def c0(j): return 5/(2*(j+5))
def drift(j): return c0(j)/(1-c0(j))*invtH * (j/(j+5))   # d/dt[ln(1-c)] with j linear in t: ċ = -c·(j̇/(j+5)) = -c/(j+5)·j/t ; α̇/α = -ċ/(1-c)
print("E2 forward: j_min = (5/2)/(B t_H) for three bound conventions (Lange 2021: α̇/α = 1.0(1.1)e-18 /yr)")
fw={}
for lab,B in (("1σ width 1.1e-18",1.1e-18),("central+1σ 2.1e-18",2.1e-18),("2σ 3.2e-18",3.2e-18)):
    jmin=2.5/(B*tH); fw[lab]=jmin; print(f"  {lab}: j_min = {jmin:.3e}; cycles at k-cap (2329/cycle) = {jmin/2329:.2e}; at m-cap (58/cycle) = {jmin/58:.2e}")
sc("fwd", abs(fw["1σ width 1.1e-18"]/1.65e8-1)<0.02, True, "Keeper's 1.65e8 reproduced at B = 1.1e-18")
print("E2 inverse: predicted α̇/α under R2 at j = 58, 2329, 1e4, 1e6")
inv={j:drift(j) for j in (58,2329,10**4,10**6)}
for j,v in inv.items(): print(f"  j={j}: α̇/α = +{v:.2e} /yr   (excess over 1.1e-18: {v/1.1e-18:.1e})")
sc("inv", 1e-15<inv[2329]<1e-13 and inv[58]>1e-13, False, "hashed 3e-12 at 58, 8e-14 at 2329")
print("E2 R1 control: the word's own j resets per interaction -> drift = 0 identically"); sc("R1", True, False, "")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({'forward':fw,'inverse':{str(j):v for j,v in inv.items()}}, open('.record_5738.json','w'), indent=1)
