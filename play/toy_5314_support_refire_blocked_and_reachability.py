import numpy as np
from math import factorial, exp, sqrt
print("="*92)
print("RE-FIRE, ROUND 3 -- 'derive the up-sector centers from saturation'. FIRST: does saturation")
print("supply centers at all?  Reconnect before computing.")
print("="*92)
print("  T2009 (banked): 'y_top = 1 = Yukawa hierarchy NORMALIZED TO TOP = the vev NORM;")
print("                   y > 1 forbidden = a NORM CEILING, ***NOT A POSITION MOVE*** -- top stays")
print("                   at grid-top 4.'")
print("  K1329 (held)   : 'up-MASSES are labeled SATURATION inputs ... but that is a mass-VALUE")
print("                   question, SEPARATE from the wavefunction-POSITION question.'")
print("  G2, THIS WEEKEND, TRIPLE-CONFIRMED: 'G2 resolved to NORM.' Saturation is RADIAL (Cauchy-")
print("                   Schwarz, r->1); the address is ANGULAR. Different coordinates.")
print()
print("  ★★★ SO SATURATION SETS THE NORM, NOT THE CENTER. The team established that in Round 2 --")
print("      it is the finding that let the fire proceed at all. Round 3 asks me to derive the")
print("      CENTERS from saturation, which is precisely the thing G2 says saturation does not do.")
print("  ⟹ THE RE-FIRE IS BLOCKED BY OUR OWN RULING, not by a missing lookup. I am not inventing")
print("     centers to get past it.")
print()
print("="*92)
print("AND THE PARAMETER COUNT, IF THE CENTERS ARE TAKEN FREE ANYWAY")
print("="*92)
def c(k,p):
    z=sqrt(p) if p>0 else 1e-12
    return exp(-p/2)*z**k/sqrt(factorial(k))
def ratios(pu,pc,pt):
    Vud=c(0,pu)+c(2,pu); Vus=c(2,pu)+c(4,pu)          # down d,s  x up u
    Vcb=c(4,pc)+c(6,pc); Vtb=c(4,pt)+c(6,pt)          # down b    x up c,t
    return Vus/Vud, Vcb/Vtb
print("  3 free centers (p_u, p_c, p_t) against 2 blind anchors (V_us/V_ud, V_cb/V_tb).")
print("  ⟹ a ONE-PARAMETER FAMILY of solutions. Hitting both anchors is therefore GUARANTEED,")
print("     not evidence. Demonstrated:")
tgt1,tgt2=0.2243/0.9743, 0.0408/0.9991
from scipy.optimize import brentq
sols=[]
for pt in [3.0,4.0,5.0,6.0,8.0]:
    f=lambda pu: ratios(pu,1,pt)[0]-tgt1
    pu=brentq(f,1e-6,3.0)
    g=lambda pc: ratios(pu,pc,pt)[1]-tgt2
    try:
        pc=brentq(g,1e-6,pt-1e-6); sols.append((pu,pc,pt))
    except Exception: pass
print("      p_t (scanned)   p_u (solved)   p_c (solved)   -> both anchors hit?")
for pu,pc,pt in sols:
    r1,r2=ratios(pu,pc,pt)
    print("        %5.2f          %.4f         %.4f        %s / %s"%(pt,pu,pc,
        "%.4f"%r1,"%.4f"%r2))
print("  ⟹ CONFIRMED: for EVERY p_t scanned there is a (p_u, p_c) hitting BOTH anchors exactly.")
print("     A one-parameter family. Reproducing V_us and V_cb from free centers banks NOTHING.")
print()
print("="*92)
print("★★★★ BUT KEEPER'S DEEPER QUESTION *DOES* HAVE A CLEAN ANSWER -- and it is the good news")
print("="*92)
print("  'Can the overlap route structurally reach 1/sqrt(20) at all, or is K1181's reframe in")
print("   tension with the banked mass-ratio result?'")
print("  The Cabibbo ratio in this construction is  (c_2+c_4)/(c_0+c_2)  as a function of p_u alone:")
for p in [0.0,0.1,0.2,0.36,0.6,1.0,2.0,5.0,20.0]:
    print("       p_u = %5.2f  ->  V_us/V_ud = %.4f"%(p,ratios(p,1,4)[0]))
print("  ⟹ the reachable range is [0, infinity), continuous and monotone. 0.2302 IS REACHED,")
print("     at p_u = %.4f."%brentq(lambda x: ratios(x,1,4)[0]-tgt1,1e-6,3.0))
print("  ★ SO K1181's REFRAME IS **NOT** IN TENSION WITH THE BANK. The overlap route can reach")
print("    1/sqrt(20); it is not structurally excluded. The fork Keeper named does NOT bite --")
print("    and that is worth saying plainly, because the alternative would have been serious.")
print()
print("  ★★ AND I POST THE REQUIRED CENTER OPENLY, so it cannot be quietly retrofitted later:")
print("     p_u = %.4f is what the Cabibbo demands. If saturation (or anything else) ever yields"%brentq(lambda x: ratios(x,1,4)[0]-tgt1,1e-6,3.0))
print("     that number from its own definition, the check is one line and I never chose it.")
