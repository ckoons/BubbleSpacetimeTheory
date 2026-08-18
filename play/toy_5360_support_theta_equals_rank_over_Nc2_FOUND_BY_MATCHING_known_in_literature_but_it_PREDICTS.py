import numpy as np
from math import sqrt, cos, pi, acos, degrees
print("="*104)
print("TOY 5360 -- THE THETA TARGET: I could NOT compute the overlap. What I did instead, labelled.")
print("="*104)
me,mmu,mtau=0.51099895069,105.6583755,1776.86
rank,N_c=2,3
r=[sqrt(me),sqrt(mmu),sqrt(mtau)]; M=sum(r)/3
th_obs=acos((r[2]/M-1)/sqrt(2))

print("\nTABLE 0 -- *** WHAT I DID NOT DO, STATED FIRST ***")
print("   I did NOT derive theta from a Bergman overlap. I do not have explicit stratum")
print("   wavefunctions, and the banked strata route is dead (5359: they run backwards).")
print("   *** So this does NOT satisfy GATE-KOIDE. What follows is a FORM found by MATCHING,")
print("   and I am labelling it that way before showing it. ***")

print("\nTABLE 1 -- the target (from 5359, masses only, Q never used)")
print("   theta_observed = %.6f rad = %.4f deg"%(th_obs,degrees(th_obs)))

print("\nTABLE 2 -- BST-integer forms near it (found by SEARCHING near the target -- not derived)")
cands=[("rank/N_c^2",rank/N_c**2),("1/(rank*N_c-1)",1/(rank*N_c-1)),
       ("N_c/(rank*g)",N_c/(rank*7.0)),("rank/(N_c^2)",2/9),
       ("1/(rank+rank*N_c-1)",1/7.0),("C_2/(N_c^3)",6/27.0)]
seen=set(); print("   form                    value (rad)   deg        dev vs target")
for nm,v in cands:
    if round(v,9) in seen: continue
    seen.add(round(v,9))
    print("   %-23s %-13.6f %-10.4f %.4f%%"%(nm,v,degrees(v),100*abs(v-th_obs)/th_obs))

print("\nTABLE 3 -- *** the closest is theta = rank/N_c^2 = 2/9. Run MY OWN discipline on it. ***")
th=rank/N_c**2
print("   (a) FAMILY SWEEP (is rank/N_c^2 dimension-generic, like 25/4 and sqrt(pi^n/n)?)")
print("       rank/N_c^2 is built from two DIFFERENT primaries, not from one dimension parameter,")
print("       so there is no n-family to sweep -- the 5336/5340 test does not apply here.")
print("   (b) *** LITERATURE CHECK -- and this is the one that matters: ***")
print("       theta ~ 2/9 rad is a KNOWN observation in the Koide literature (often quoted as")
print("       theta ~ 0.2222). *** SO THIS IS NOT A BST DISCOVERY. *** If we report it we report it")
print("       as 'the known Koide angle happens to equal rank/N_c^2 in BST primaries' -- an")
print("       IDENTIFICATION, and one anyone could have written down. I am flagging this myself")
print("       because presenting it as new would be the worst move available.")
print("   (c) FOUND-BY-MATCHING: I searched forms NEAR the target. That is the numerology mode,")
print("       and it is exactly what GATE-KOIDE was written to stop.")

print("\nTABLE 4 -- *** BUT IT MAKES A FALSIFIABLE PREDICTION -- so run it. ***")
print("   Fix A^2 = rank and theta = rank/N_c^2 EXACTLY. Fix the overall M from m_e alone.")
print("   Then m_mu and m_tau are PREDICTED (2 outputs from 1 input + 2 fixed integers).")
c=[cos(th+2*pi*k/3) for k in range(3)]
order=np.argsort(c)                       # smallest cos -> lightest
Me=sqrt(me)/(1+sqrt(rank)*c[order[0]])
pred=[(Me*(1+sqrt(rank)*c[i]))**2 for i in order]
obs=[me,mmu,mtau]
print("   particle   predicted (MeV)   observed (MeV)   deviation")
for nm,p,o in zip(("e (input)","mu","tau"),pred,obs):
    print("   %-10s %-17.6f %-16.6f %s"%(nm,p,o,"(anchor)" if "input" in nm else "%.3f%%"%(100*abs(p-o)/o)))

print("\nTABLE 5 -- how sharp is the test? (what theta precision would decide it)")
for dth in (0.0005,0.0001,0.00005):
    cc=[cos(th_obs+dth+2*pi*k/3) for k in range(3)]
    oo=np.argsort(cc); Mx=sqrt(me)/(1+sqrt(rank)*cc[oo[0]])
    mt=(Mx*(1+sqrt(rank)*cc[oo[2]]))**2
    print("   d(theta) = %-8.5f rad -> m_tau shifts by %.4f%%"%(dth,100*abs(mt-mtau)/mtau))
print("   ==> m_tau is a SENSITIVE probe of theta -- so 2/9 is a genuinely testable claim, not a")
print("       loose fit. Its %.3f%% tau miss IS the discriminating number."%(100*abs(pred[2]-mtau)/mtau))

print("\n"+"="*104)
print("VERDICT")
print("="*104)
print(" (1) *** I DID NOT SATISFY THE GATE. *** No overlap computation: I lack the stratum")
print("     wavefunctions and the banked route is dead. @Lyra/@Grace still own the real run.")
print()
print(" (2) *** WHAT I HAVE IS theta = rank/N_c^2 = 2/9 rad, FOUND BY MATCHING (%.4f%% from the"%(100*abs(th-th_obs)/th_obs))
print("     target). Three things must travel with it, or it is numerology: ***")
print("       (a) it was found by SEARCHING near the answer -- the mode GATE-KOIDE forbids;")
print("       (b) *** theta ~ 2/9 is ALREADY KNOWN in the Koide literature -- NOT a BST discovery; ***")
print("       (c) it is an IDENTIFICATION (BST primaries happen to compose to it), not a mechanism.")
print()
print(" (3) THE ONE THING THAT MAKES IT MORE THAN A COINCIDENCE: it PREDICTS. Fixing A^2 = rank and")
print("     theta = 2/9 exactly, with M set by m_e alone, gives m_mu at %.3f%% and m_tau at %.3f%%."%(
       100*abs(pred[1]-mmu)/mmu,100*abs(pred[2]-mtau)/mtau))
print("     Two outputs, one input, two integers. *** That is falsifiable and it is the number worth")
print("     reporting -- not the angle match. ***")
print()
print(" (4) AND THE TEST IS SHARP (Table 5): m_tau moves ~1%% per 5e-4 rad of theta, so the fit")
print("     cannot hide. If someone derives theta from the geometry, THIS is what it must beat.")
print()
print(" (5) @Keeper -- my honest recommendation: do NOT bank 2/9. It is a known literature")
print("     observation wearing BST primaries, found by matching. Bank instead the PREDICTION as a")
print("     falsifiable candidate, and keep the gate open for a real overlap derivation.")
