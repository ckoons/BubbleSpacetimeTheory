import math, itertools
print("TWO CORRECTIONS TO MY OWN FIRST PASS, both caught by re-reading my own output:")
print("  (i) I printed n = -35.909. The SIGN was an artefact of my formula; the exponent is +35.91.")
print(" (ii) I wrote 'AT LEAST TWO READINGS FIT' citing 35 = n_C*g -- but my own filter returned")
print("      ONLY [36]. 35 lands at 10^-118.06, which is 1.94 decades away, outside the +-1.5 window.")
print("      Prose contradicting its own data. Recomputed honestly below.\n")
alpha=1/137.035999; tP=5.391247e-44
la=math.log10(alpha); lt=math.log10(tP)
n_need=(-120-lt)/la
print("="*92); print("THE FISHING COUNT, DONE PROPERLY -- it depends on how loosely 10^-120 is read")
print("="*92)
print("  exponent needed for exactly 10^-120 :  n = %.3f"%n_need)
prim={'rank':2,'N_c':3,'n_C':5,'C_2':6,'g':7}
comps={}
for (a,x),(b,y) in itertools.product(prim.items(),repeat=2): comps.setdefault(x*y,set()).add("%s*%s"%(a,b))
for a,x in prim.items():
    comps.setdefault(x*x,set()).add("%s^2"%a)
    for (b,y),(c,z) in itertools.product(prim.items(),repeat=2): comps.setdefault(x*y*z,set()).add("%s*%s*%s"%(a,b,c))
for tol in [1.0,1.5,2.0,2.5]:
    hits=[n for n in range(30,45) if abs(lt+n*la+120)<=tol and n in comps]
    print("     tolerance +-%.1f decades -> BST composites in window: %s"%(tol,hits))
print("\n  ⟹ HONEST COUNT: at +-1.5 decades ONLY n = 36 qualifies; widen to +-2.0 and n = 35 = n_C*g")
print("     joins it. So the count is 1 or 2, TOLERANCE-DEPENDENT -- WEAK evidence in either")
print("     direction. I should not have stacked this onto the real argument.")
print()
print("="*92); print("★ THE VERDICT RESTS ON (a) ALONE -- and (a) is untouched")
print("="*92)
print("  (a) THE MECHANISM CONTAINS NO alpha. H_B is the Casimir of the COMPACT group K = SO(5)xSO(2);")
print("      its spectrum is {0, 5/2, 4, 6, 10, 12, 16, ...} -- root-system rationals. exp(-tau H_B/hbar)")
print("      therefore sets ONE scale, tau ~ hbar/lambda, spanning less than one decade across the")
print("      whole K-type tower. IT CANNOT PRODUCE A POWER OF alpha AT ALL, for ANY exponent.")
print("      ⟹ the exponent is not merely un-derived; there is no channel in the stated mechanism")
print("        through which ANY exponent could arrive.")
print("  (b) the fishing count is 1-2 and tolerance-dependent -- I withdraw it as evidence.")
print()
print("  ⟹ AGAINST KEEPER'S BAR ('derivation-grade only if C_2^2 = 36 is MECHANISM-FORCED'):")
print("     NOT FORCED. The Koons tick is an IDENTIFIED SCALE. And the reason is structural, not")
print("     statistical -- which is the stronger form of the negative.")
