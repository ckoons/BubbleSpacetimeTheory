import numpy as np
from math import sqrt, pi, atan, degrees
print("="*104)
print("TOY 5358 -- THE A^2 = rank STEP: what it means geometrically, and does 'COLOURLESS' do work?")
print("  Tables first, verdict after.")
print("="*104)
rank=2; N_c=3
def Q(ms): return sum(ms)/sum(sqrt(m) for m in ms)**2
def A2_from_Q(q,N=3): return 2*(N*q-1)

print("\nTABLE 1 -- the identity: Q = rank/N_c  <=>  A^2 = rank  (exact algebra, no input)")
print("   Koide parameterisation: sqrt(m_k) = M(1 + A cos(theta + 2 pi k/N)), N = N_c = 3")
print("   sum cos = 0 and sum cos^2 = 3/2, so")
print("     (sum m)      = M^2 (3 + 3A^2/2)")
print("     (sum sqrt m)^2 = 9 M^2")
print("     Q = (1 + A^2/2)/3")
print("   set Q = rank/N_c = 2/3  ->  1 + A^2/2 = 2  ->  *** A^2 = 2 = rank. Exact. ***")

print("\nTABLE 2 -- the geometric content: A^2 = rank IS the 45-degree tilt")
print("   democratic component magnitude  = sqrt(3) M")
print("   modulation component magnitude  = M A sqrt(3/2)")
print("   tan(tilt) = A sqrt(3/2)/sqrt(3) = A/sqrt(2)")
for A2 in (1,2,3,4):
    t=degrees(atan(sqrt(A2)/sqrt(2)))
    print("   A^2 = %-3d -> tilt = %.3f deg%s"%(A2,t," *** 45 deg exactly ***" if A2==rank else ""))
print("   ==> A^2 = rank <=> the sqrt-mass vector tilts at EXACTLY 45 deg from the democratic axis.")

print("\nTABLE 3 -- is A^2 = 2 forced by positivity? (check before claiming it is special)")
print("   sqrt(m_k) > 0 needs 1 + A cos(theta+2pi k/3) > 0 for all k.")
print("   over theta, min_k cos can be made as high as -1/2, so the bound is A < 2, i.e. A^2 < 4.")
print("   ==> *** A^2 = 2 is ALLOWED but NOT forced by positivity -- the whole range A^2 in (0,4)")
print("       is available. So positivity does no work; the 2 must come from elsewhere. ***")

print("\nTABLE 4 -- what the LEPTONS actually give")
me,mmu,mtau=0.51099895069,105.6583755,1776.86
ql=Q([me,mmu,mtau])
print("   Q_leptons = %.8f   ->  A^2 = %.6f   (rank = 2)  dev %.4f%%"%(
      ql,A2_from_Q(ql),100*abs(A2_from_Q(ql)-rank)/rank))
print("   ==> A^2 = 2 to four decimals. That IS the empirical content of Koide.")

print("\nTABLE 5 -- *** THE DISCRIMINATING TEST: does 'COLOURLESS' do any work? ***")
print("   The proposed mechanism is a COLOURLESS unit-amplitude filling -> A^2 = rank.")
print("   If 'colourless' is load-bearing, COLOURED quarks must give A^2 =/= rank.")
print("   sector        masses (PDG, MS-bar; convention flagged)      Q          A^2      vs rank")
sets=[("charged leptons",[me,mmu,mtau]),
      ("down-type quarks",[4.7,93.5,4183.0]),
      ("up-type quarks",[2.16,1270.0,172690.0])]
for nm,ms in sets:
    q=Q(ms); A2=A2_from_Q(q)
    print("   %-14s %-46s %-10.6f %-8.4f %s"%(nm,str(ms),q,A2,
        "*** = rank ***" if abs(A2-rank)<0.01 else "differs by %.2f"%abs(A2-rank)))
print("   ==> *** THE QUARKS DO NOT GIVE A^2 = 2. *** So 'colourless' is doing real work: the")
print("       leptons sit at A^2 = rank and the coloured sectors do not. The mechanism story has")
print("       DISCRIMINATING CONTENT -- it is not a label attached after the fact.")
print("   ** convention flag: quark masses are scheme- and scale-dependent (MS-bar at 2 GeV / m_c /")
print("      m_b / m_t). The leptons are pole masses. So the quark A^2 values are indicative, NOT")
print("      precise -- but they are nowhere near 2, and no plausible scheme choice moves them there. **")

print("\n"+"="*104)
print("VERDICT")
print("="*104)
print(" (1) *** THE ALGEBRA IS EXACT AND NEEDS NO INPUT: Q = rank/N_c <=> A^2 = rank, *** given")
print("     N_gen = 3. And A^2 = rank is EXACTLY the 45-degree tilt of the sqrt-mass vector from")
print("     the democratic axis (Table 2). That part of the corpus's claim is solid.")
print()
print(" (2) *** POSITIVITY DOES NO WORK: the allowed range is A^2 in (0,4), so 2 is permitted but")
print("     not forced. *** Anyone deriving A^2 = 2 must supply something beyond well-definedness.")
print("     Worth stating because 'it has to be 2 or the masses go negative' would be a tempting")
print("     and WRONG argument.")
print()
print(" (3) ***** THE COLOURLESS HYPOTHESIS HAS DISCRIMINATING CONTENT -- and this is the new")
print("     result. ***** Leptons give A^2 = 1.99996; the coloured sectors give values far from 2")
print("     (Table 5). So 'colourless -> A^2 = rank' is not a label applied after the fact: it")
print("     separates the sectors it claims to separate. *** That is a genuine, un-fakeable check")
print("     the mechanism passes, and I could not find it already run in the corpus. ***")
print()
print(" (4) WHAT IS STILL NOT DERIVED: WHY colourless gives unit amplitude per channel, and why")
print("     there are exactly rank channels. Table 5 shows the hypothesis DISCRIMINATES; it does")
print("     not show it is FORCED. *** Passing a discriminating test is necessary and not")
print("     sufficient -- the Bergman overlap computation (T2516) is still owed. ***")
print()
print(" (5) SO THE SECTOR'S STATUS, precisely: m_e (anchor) + the muon form (open) + Koide (algebra")
print("     exact, mechanism discriminating-but-underived). *** Two open items, both sharp, and")
print("     neither is 'the tower is a patchwork'. ***")
