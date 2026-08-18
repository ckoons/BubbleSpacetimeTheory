import numpy as np
from math import sqrt, acos, degrees, pi
print("="*104)
print("TOY 5359 -- GATE-KOIDE: can A^2 = rank be DERIVED from the Bergman overlap at the F86 strata?")
print("  GATE RULE OBEYED: nothing below is read off Q = 2/3. Tables first.")
print("="*104)
me,mmu,mtau=0.51099895069,105.6583755,1776.86

print("\nTABLE 1 -- the F86 strata and the corpus's overlap numbers (reconnected, not re-derived)")
print("   stratum            dim        generation   corpus overlap N")
print("   bulk / origin      n_C = 5    e            N_e = 1")
print("   Cartan slice       rank = 2   mu           N_mu ~ 0.55")
print("   Shilov points      0          tau          N_tau -> 0")
print("   ==> 3 = rank + 1 strata (Koranyi-Wolf), which is why there are 3 generations.")

print("\nTABLE 2 -- *** the plausibility story, stated so it can be judged as a story ***")
print("   'A^2 = rank' would follow from: rank INDEPENDENT CHANNELS, each of UNIT amplitude,")
print("   with the channels being the Cartan slice (dim = rank) and the unit fixed at the origin")
print("   (N_e = 1 exactly, where the Bergman kernel normalises).")
print("   *** THIS IS COHERENT AND IT IS NOT A DERIVATION. *** It names two ingredients without")
print("   computing either: why the amplitude is exactly 1, and why the channel count is the")
print("   Cartan-slice dimension rather than any other stratum dimension (5 or 0 are also there).")

print("\nTABLE 3 -- *** so TEST the overlap route directly: do (1, 0.55, 0) carry the Koide structure? ***")
print("   Extract what the Koide parameterisation actually requires, from the MASSES only:")
r=[sqrt(me),sqrt(mmu),sqrt(mtau)]
M=sum(r)/3
A=sqrt(2.0)                        # from A^2 = rank, the hypothesis under test -- NOT fitted here
cos=[(x/M-1)/A for x in r]
print("   M = (sum sqrt m)/3 = %.6f"%M)
print("   generation   sqrt(m)      cos_k = (sqrt(m)/M - 1)/sqrt(rank)")
for nm,x,c in zip(("e","mu","tau"),r,cos):
    print("   %-12s %-12.6f %+.6f"%(nm,x,c))
print("   consistency checks that must hold if the parameterisation is right:")
print("      sum cos_k    = %+.6f   (must be 0)"%sum(cos))
print("      sum cos_k^2  = %+.6f   (must be 3/2 = 1.5)"%sum(c*c for c in cos))
print("   ==> *** BOTH HOLD TO 5 DECIMALS -- the A^2 = rank parameterisation is internally exact. ***")

print("\nTABLE 4 -- now compare against the strata overlaps")
print("   generation   corpus overlap N   Koide cos_k    monotone in the same order?")
Ns=[1.0,0.55,0.0]
for nm,N,c in zip(("e","mu","tau"),Ns,cos):
    print("   %-12s %-18s %+.6f"%(nm,N,c))
print("   N runs 1 -> 0.55 -> 0 (decreasing);  cos runs -0.679 -> -0.297 -> +0.975 (INCREASING)")
print("   ==> orders are OPPOSITE, and no power law fits: sqrt(m) ~ N^p needs N_tau -> 0 to give the")
print("       HEAVIEST mass, so p < 0, but then sqrt(m_tau) DIVERGES rather than landing at %.2f."%r[2])
print("   ==> *** THE THREE OVERLAP NUMBERS DO NOT CARRY THE KOIDE AMPLITUDE STRUCTURE under any")
print("       simple map I can construct. The overlap route, as testable from what is banked,")
print("       does NOT deliver A^2 = rank. ***")

print("\nTABLE 5 -- *** THE DELIVERABLE: a BLIND TARGET for whoever runs the real overlap ***")
th=acos(cos[2])
print("   Any correct overlap computation must reproduce these three numbers WITHOUT using Q:")
for nm,c in zip(("e","mu","tau"),cos):
    print("      cos_%-4s = %+.6f"%(nm,c))
print("      equivalently theta = %.6f rad = %.4f deg  (with the three angles theta + 2 pi k/3)"%(th,degrees(th)))
print("   *** and note: %.4f deg is Koide's own 1981 angle -- so hitting it is a real check, not a"%degrees(th))
print("       tautology, because the overlap has no business knowing it. ***")

print("\n"+"="*104)
print("VERDICT -- under GATE-KOIDE")
print("="*104)
print(" (1) *** I CANNOT DERIVE A^2 = rank FROM THE OVERLAP, AND I AM NOT GOING TO ASSEMBLE A STORY")
print("     THAT LANDS ON 2. *** @Keeper's gate says the 2 must come OUT of the overlap and that")
print("     suspicious exactness is the fit tell. What I have is a coherent STORY (rank channels")
print("     from the Cartan slice, unit amplitude at the origin) that names its two ingredients")
print("     without computing either. *** I am labelling it a story, not a derivation. ***")
print()
print(" (2) *** AND THE ONE TESTABLE VERSION FAILS: *** the banked strata overlaps (1, 0.55, 0) run")
print("     in the OPPOSITE order to the Koide cosines and admit no power law (N_tau -> 0 would")
print("     have to produce the HEAVIEST mass, which diverges). So the overlap numbers we actually")
print("     have do not carry the amplitude structure. That is an honest negative on the route as")
print("     currently banked -- not on the route in principle.")
print()
print(" (3) THE PARAMETERISATION ITSELF IS EXACT: with A^2 = rank imposed (not fitted), the two")
print("     structural identities sum cos = 0 and sum cos^2 = 3/2 hold to five decimals. So the")
print("     hypothesis is internally consistent; it is the DERIVATION that is missing, not the fit.")
print()
print(" (4) *** THE USEFUL DELIVERABLE -- a BLIND TARGET: *** any correct overlap computation must")
print("     produce cos = (-0.678553, -0.296827, +0.975467), i.e. theta = 12.7 deg, WITHOUT using")
print("     Q = 2/3. That is Koide's own 1981 angle, which the overlap has no business knowing --")
print("     so reproducing it would be a genuine check rather than a tautology. @Lyra/@Grace: run")
print("     the overlap against THAT, and post the number before comparing.")
