import numpy as np
from math import factorial, exp, sqrt
from scipy.optimize import brentq
print("="*92)
print("GATE A -- THE nu-STRATUM CANDIDATES. Scope stated first, honestly.")
print("="*92)
print("  The literal assignment ('compute the center ON the nu-stratum') needs the nu -> RADIUS map,")
print("  which @Keeper assigned to @Lyra and which does not exist yet. I will not invent it -- that")
print("  is the fit trap, and it is the same unexhibited-map block I hit in 5310 (nu-indexed vs")
print("  lambda-indexed labels).")
print("  WHAT I CAN DO, AND IT IS THE PART MY 5315 GENUINELY MISSED: sweep the nu-DERIVED candidates")
print("  built from {5/2, 3/2, 0} alone, report IN FULL, and check every one against the 0.49% bar.")
print()
def c(k,p):
    z=sqrt(p) if p>0 else 1e-12
    return exp(-p/2)*z**k/sqrt(factorial(k))
def cab(p): return (c(2,p)+c(4,p))/(c(0,p)+c(2,p))
tgt=0.2243/0.9743
need=brentq(lambda x: cab(x)-tgt,1e-9,3.0)
bar=0.0049
print("  REQUIRED: p_u = %.4f, to within %.2f%% (my 5315 price). Anything outside that FAILS."%(need,100*bar))
print()
n1,n2,n3=2.5,1.5,0.0
cands=[
 ("nu_1 itself",                 n1),
 ("1/nu_1  (= rank/n_C, swept)", 1/n1),
 ("nu_1 - nu_2",                 n1-n2),
 ("nu_2/nu_1",                   n2/n1),
 ("1/(nu_1+nu_2)",               1/(n1+n2)),
 ("(nu_1-nu_2)/(nu_1+nu_2)",     (n1-n2)/(n1+n2)),
 ("nu_2/(nu_1+nu_2)",            n2/(n1+n2)),
 ("1/nu_1^2 * nu_2",             n2/n1**2),
 ("(nu_1-nu_2)/nu_1",            (n1-n2)/n1),
 ("nu_2/nu_1^2",                 n2/(n1*n1)),
 ("1/(nu_1*nu_2)",               1/(n1*n2)),
 ("(nu_2/nu_1)^2",               (n2/n1)**2),
 ("nu_1*nu_2/(nu_1+nu_2)^2",     n1*n2/(n1+n2)**2),
 ("1/(2*nu_2)",                  1/(2*n2)),
 ("nu_2 - 1",                    n2-1),
]
print("      nu-derived candidate               p        V_us/V_ud    dev vs p_u    passes 0.49%?")
best=None
for name,p in cands:
    dev=abs(p-need)/need
    print("      %-33s %7.4f   %9.4f    %7.2f%%       %s"%(name,p,cab(p),100*dev,"YES" if dev<bar else "no"))
    if best is None or dev<best[1]: best=(name,dev,p)
print("\n  nearest nu-derived candidate: %s (p = %.4f), off by %.2f%%"%(best[0],best[2],100*best[1]))
print()
print("="*92)
print("★★★ AND THE SHARPEST SINGLE NUMBER I CAN CONTRIBUTE: GRACE'S 0.378 AGAINST THE BAR")
print("="*92)
g=0.378
print("     Grace's shelf-derived tweak-radius : p = %.4f"%g)
print("     required                            : p = %.4f"%need)
print("     deviation                           : %.2f%%   -- the bar is %.2f%%"%(100*abs(g-need)/need,100*bar))
print("     resulting Cabibbo                   : %.4f  vs observed %.4f  (%.2f%% off)"%(cab(g),tgt,100*abs(cab(g)-tgt)/tgt))
print("     ⟹ %s THE 0.49%% BAR."%("PASSES" if abs(g-need)/need<bar else "**FAILS**"))
print("     ⟹ and in Cabibbo terms 0.378 gives |V_us| ~ %.4f against 0.2243 -- a %.1f-sigma miss"%(
    cab(g)*0.9743, abs(cab(g)*0.9743-0.2243)/0.00085))
print("       on a quantity measured to 0.4%%.")
print()
print("="*92)
print("VERDICT ON GATE A")
print("="*92)
print("  * NO nu-derived candidate I can construct passes the 0.49%% bar; the nearest misses by %.1f%%."%(100*best[1]))
print("  * Grace's shelf-derived 0.378 also FAILS the bar (%.1f%% off) and is a %.0f-sigma miss on V_us."%(
    100*abs(g-need)/need, abs(cab(g)*0.9743-0.2243)/0.00085))
print("  * So on everything currently on the table, the center is STILL a free input -- my 5315")
print("    finding stands, and the nu-stratum sweep does not overturn it.")
print()
print("  ★ WHAT WOULD OVERTURN IT, stated precisely so the next round is decidable:")
print("    @Lyra's nu -> RADIUS map must produce %.4f (not 0.378, not 0.4, not 1/N_c) to within"%need)
print("    0.49%%, FROM ITS OWN DEFINITION. The target has been public since my 5314. If the map")
print("    lands there, I never chose it and the Gatto prize is real. If it lands at 0.378 or 0.4,")
print("    it is a near-neighbour and the sector's magnitudes stay open.")
print("  ★★ AND A CAUTION FOR GATE B, since it is mine to flag: 0.378 and 0.4 and 0.3713 are all")
print("     within 8%% of each other. At that density, 'my map gives ~0.37' is NOT a hit -- the bar")
print("     is 0.49%%, and near-neighbours are exactly what Cal's null (10 routes within 1%%) predicts.")
