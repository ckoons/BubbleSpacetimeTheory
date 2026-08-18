import numpy as np
from math import factorial, exp, sqrt
from scipy.optimize import brentq
print("="*92)
print("LANE 1 -- DOES D_IV^5 CONTAIN A MASS-FREE GEOMETRIC QUANTITY THAT FORCES THE CENTER p_u?")
print("Cal's (c)-guard: the center-setter must use NO mass/Yukawa input. Every candidate below is")
print("built only from the five integers and derived domain data. No observable enters.")
print("="*92)
def c(k,p):
    z=sqrt(p) if p>0 else 1e-12
    return exp(-p/2)*z**k/sqrt(factorial(k))
def cab(p): return (c(2,p)+c(4,p))/(c(0,p)+c(2,p))
tgt=0.2243/0.9743
need=brentq(lambda x: cab(x)-tgt,1e-9,3.0)
print("\n  observed |V_us|/|V_ud| = %.4f  ->  requires p_u = %.4f  (blind-posted in my 5314)"%(tgt,need))
d=1e-4; sens=(cab(need+d)-cab(need-d))/(2*d)
print("  sensitivity dV/dp = %.3f  ->  to match V_us to PDG precision (~0.001) the center must be"%sens)
print("  right to  dp ~ %.4f, i.e. %.2f%% .  THE CENTER-SETTER MUST BE EXACT, not approximate."%(0.001/sens,100*(0.001/sens)/need))
print()
print("  THE CANDIDATES -- every mass-free geometric quantity I can construct, reported IN FULL:")
rank,N_c,n_C,C_2,g=2,3,5,6,7
a=n_C-2                    # FK multiplicity, type IV
cands=[
 ("k_u  (peak-on-shelf, T1929)",       0.0),
 ("1/g",                                1/g),
 ("1/C_2",                              1/C_2),
 ("rank/g",                             rank/g),
 ("1/N_c",                              1/N_c),
 ("rank/n_C",                           rank/n_C),
 ("N_c/g",                              N_c/g),
 ("1/rank",                             1/rank),
 ("a/n_C",                              a/n_C),
 ("rank/N_c",                           rank/N_c),
 ("1/a",                                1/a),
 ("N_c/n_C",                            N_c/n_C),
 ("rho_2/rho_1 = (3/2)/(5/2)",          1.5/2.5),
 ("a/(rank*n_C)",                       a/(rank*n_C)),
 ("rank",                               float(rank)),
 ("a/rank = 3/2",                       a/rank),
 ("n_C/rank = 5/2",                     n_C/rank),
]
print("\n      candidate                          p        V_us/V_ud    dev vs %.4f"%tgt)
best=None
for name,p in cands:
    v=cab(p); dev=abs(v-tgt)/tgt
    print("      %-33s %7.4f   %9.4f    %6.1f%%"%(name,p,v,100*dev))
    if best is None or dev<best[2]: best=(name,p,dev)
print("\n  nearest candidate: %-28s p = %.4f, off by %.1f%%"%(best[0],best[1],100*best[2]))
print()
print("="*92)
print("★★★ THE VERDICT")
print("="*92)
print("  * the CANONICAL center-setter -- 'the coherent state peaks on its T1929 shelf', p_u = k_u = 0")
print("    -- is the one I already fired in 5313, and it gives V_us/V_ud = 0.0000. IT FAILS.")
print("    That is the answer to the assignment's first reading: the natural geometric center is")
print("    the shelf itself, and the shelf gives ZERO.")
print("  * of %d mass-free candidates, the closest misses by %.0f%%, against a required precision of"%(len(cands),100*best[2]))
print("    %.2f%%. NONE lands. And several BRACKET the target (1/N_c = %.4f below, rank/n_C = %.4f"%(100*(0.001/sens)/need,1/N_c,rank/n_C))
print("    above) -- which is the bracketing signature, not a hit.")
print()
print("  ⟹ NOTHING IN THE GEOMETRY I CAN CONSTRUCT FORCES p_u = %.4f."%need)
print("     Per Keeper's own framing, I report the honest finding plainly:")
print("     ★★ THE COHERENT-STATE CENTER IS A GENUINE FREE INPUT OF THE MIXING SECTOR. ★★")
print("     It is not a missing lookup and not a harder computation -- it is a parameter the")
print("     geometry does not supply, and the mixing magnitudes rest on it.")
print()
print("  ★ AND THAT LOCATES THE BOUNDARY EXACTLY, which is what the round asked for:")
print("     FORCED (banked)  : the shelves (T1929), the parity selection rule, the one-rung current,")
print("                        the hierarchy ORDERING (each rung ~ one power of lambda).")
print("     FREE (named now) : the coherent-state center p_j -- three real numbers, one per")
print("                        generation, on which every mixing MAGNITUDE depends.")
print("     ⟹ 'skeleton derived / magnitudes open' is not a hedge. The open part has a name, a")
print("        count (3), and a required precision (%.2f%%)."%(100*(0.001/sens)/need))
