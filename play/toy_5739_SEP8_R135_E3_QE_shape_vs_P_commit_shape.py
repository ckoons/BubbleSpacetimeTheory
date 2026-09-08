#!/usr/bin/env python3
import json
from fractions import Fraction as F
score=[]; cf=[]
def sc(n, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {n}  {d}")
def cform(j,k): j=F(j);k=F(k); return 1-F(k+3,2*k+3)*(j+k+F(5,2))/(j+k+5)-F(k,2*k+3)*(j+1)/(j+F(7,2))
def QE(m):
    p=F(1)
    for k in range(m): p*=F(k+3,2*k+3)
    return 1-p
print("QE(m) (K1860 l.108) vs P(commit) = 1-c along the chain's two extreme paths")
rows=[]
for m in range(0,11):
    q=QE(m); light=1-cform(0,m); matter=1-cform(m//2, m%2)
    rows.append((m,float(q),float(light),float(matter))); print(f"  m={m}: QE = {float(q):.4f} (1-QE = {float(1-q):.2e});  P(commit) light word (0,m) = {float(light):.4f};  max-winding word = {float(matter):.4f}")
tail_qe=[float(1-QE(m)) for m in (10,20,40)]; tail_c=[float(cform(j,0)) for j in (10,20,40)]
print("  approach: 1-QE at m=10,20,40:", [f"{x:.2e}" for x in tail_qe], " (ratio per doubling ~", f"{tail_qe[1]/tail_qe[0]:.1e},{tail_qe[2]/tail_qe[1]:.1e})", "; c(j,0) at j=10,20,40:", [f"{x:.3f}" for x in tail_c], "(ratio per doubling", f"{tail_c[1]/tail_c[0]:.2f},{tail_c[2]/tail_c[1]:.2f})")
same_shape=all(rows[i][1]<rows[i+1][1] for i in range(10)) and all(float(1-cform(j,0))<float(1-cform(j+1,0)) for j in range(10))
diff_law=tail_qe[2]/tail_qe[1] < 0.01 and 0.4<tail_c[2]/tail_c[1]<0.7
sc("E3", same_shape and diff_law, True, "same monotone shape, same asymptote 1, different approach law (geometric vs 1/j); at m=3: QE 3/7 vs light 31/56 vs matter 38/63")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump(rows, open('.record_5739.json','w'))
