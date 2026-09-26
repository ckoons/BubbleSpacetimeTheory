"""Cal Section 992: rerun of Section 989's A2 kaon kill line on CONVENTION-MATCHED inputs (written 11:47 EDT, hashed before running).
Kill line (Section 989, unchanged): FIRED on a route iff that route is > 3 sigma from A2 AND the route is not itself > 3 sigma
from another route measuring the same ratio. Section 989's QB3 (3.58 sigma split) paired the isospin-limit product 0.27679 (PDG 67.15)
with FLAG's CHARGED 1.1934: a convention mismatch (Grace R164 Section 3 owned the same pairing in R163).
Inputs: vv26.txt 67.15 iso product 0.27679(28)(20); 67.16/67.17 iso F_K/F_pi 1.1978(22), ratio 0.23108(51);
Grace R164 Section 3 charged product 0.27599 (error taken equal to the iso product's, stated as an assumption) and FLAG 2+1+1 charged 1.1934(19);
semileptonic ratio 0.21656(35)/0.9698(17)/0.97367(32).
Prediction (direction first): matched splits 2.2-2.8 sigma (< 3); A2 route pulls 3.2-3.8 sigma; by the unchanged line: FIRED on the K_mu2 route.
"""
import numpy as np
s19 = 1/np.sqrt(19)
ep = np.hypot(0.00028, 0.00020)
semi = 0.21656/0.9698/0.97367
esemi = semi*np.sqrt((0.00035/0.21656)**2 + (0.0017/0.9698)**2 + (0.00032/0.97367)**2)
for name, prod, f, ef in [("isospin-limit", 0.27679, 1.1978, 0.0022), ("charged", 0.27599, 1.1934, 0.0019)]:
    r = prod/f; er = r*np.hypot(ep/prod, ef/f)
    pull = (s19 - r)/er; split = (r - semi)/np.hypot(er, esemi)
    fk = prod/s19; efk = ep/s19
    print(f"{name:14s} lep ratio {r:.5f}({er*1e5:.0f})  A2 pull {pull:+.2f}  fK/fpi A2 {fk:.4f} vs {f}: {(fk-f)/np.hypot(ef,efk):+.2f}  split vs semi {split:+.2f}  -> {'FIRED' if abs(pull)>3 and abs(split)<=3 else 'not fired'}")
print(f"semileptonic ratio {semi:.5f}({esemi*1e5:.0f}), A2 {s19:.5f}")
