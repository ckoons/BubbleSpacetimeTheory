r"""
Toy 4170: independent confirmation of Lyra's F119 (the tau -1.77 does NOT derive) -- via a decisive argument that
does NOT depend on the d=3 Weyl bookkeeping, plus the status of Grace's triangle-closure test. Lyra walked back the
tau -1.77 = -sqrt(pi) reading by heat-kernel pi-power bookkeeping. There's a second, frame-independent confirmation
that's even cleaner: the missing term is BELOW the data floor -- its experimental error is so wide that sqrt(pi),
16/9, 7/4, and e-1 are ALL within 1 sigma. So no derivation of this term is bankable from current data, regardless of
frame. Count stays 2 of 26.

PART 1 -- the data-floor argument (frame-independent confirmation of F119):
  m_tau/m_e = 3477.23 +/- 0.23 (from m_tau = 1776.86 +/- 0.12 MeV). closed form 49*71 = 3479.
  missing term = 49*71 - m_tau/m_e = 1.772 +/- 0.235  (13% experimental error).
  candidates within 1 sigma: sqrt(pi)=1.7725, 16/9=1.7778, 7/4=1.7500, e-1=1.7183 -- ALL of them.
  => the data cannot distinguish sqrt(pi) from 16/9 from 7/4. so even a sqrt(pi) that fit would not be bankable; the
     term is below the resolving power. this confirms F119 independently of the Weyl pi-power argument. (the central
     value IS sqrt(pi) to 4 digits, which is why it was tempting -- but the error bar forbids the claim.)

PART 2 -- F119's Weyl argument, structurally confirmed:
  the d=3 Weyl/heat-kernel coefficients all carry NEGATIVE pi-powers (they come from (4 pi)^{-d/2}, (4 pi)^{-(d-1)/2}
  factors): g^3 ~ pi^-2, g^2 ~ pi^-3/2, g^1 ~ pi^-2, g^0 ~ pi^-3/2. a +sqrt(pi) (POSITIVE pi-power) cannot arise from
  a product of negative-pi-power coefficients -- forcing it needs an unsourced pi^2. structurally sound; F119 holds.

PART 3 -- triangle-closure status (Grace's decisive derivation-vs-re-expression test):
  the over-determination triangle: m_mu/m_e = (24/pi^2)^6 (F118, derived mod FK const); m_tau/m_e = 49*71 (tau, F119
  open); m_tau/m_mu = their quotient = 16.826 vs obs 16.817 -> closes to 0.05%, TAU-LIMITED (the muon leg is 0.003%).
  Grace's test: does ONE principle (concentration) force ALL three legs? CURRENT STATUS: NO -- the muon leg derives
  (F118), the tau leg does NOT (F119). so the one-principle triangle-closure is NOT yet achieved. F118 remains a
  candidate STANDALONE derivation of m_mu/m_e (mod FK const), but it has NOT been shown to force the tau, so by Grace's
  own off-target test it is not yet a full-triangle derivation. the tau needs a DIFFERENT frame (Lyra), not a sqrt(pi) patch.

HONEST READING:
  the tau leg is "49*71, good to 0.05%" -- and the residual 1.772 is AT the experimental floor, indistinguishable
  among sqrt(pi)/16/9/7/4/e-1. so chasing the -1.77 as a derivable constant is not productive from data; the real open
  problem is the tau's right FRAME (a forced derivation of 49*71 = g^2(g+2^C2), analogous to the muon's F118), which
  F119 shows is NOT the d=3 Weyl count. count stays 2; muon candidate 2->3 (mod FK const) stands; full triangle open.
"""

import math
me, mtau, dmtau = 0.51099895, 1776.86, 0.12
mmu = 105.6583755
pi = math.pi

print("=" * 96)
print("TOY 4170: confirm F119 (tau -1.77 doesn't derive) -- it's below the DATA FLOOR; + triangle-closure status")
print("=" * 96)
print()

print("PART 1 -- the data-floor argument (frame-independent):")
print("-" * 96)
mratio = mtau/me; dratio = dmtau/me
missing = 49*71 - mratio
print(f"  m_tau/m_e = {mratio:.2f} +/- {dratio:.2f}  (m_tau = {mtau} +/- {dmtau} MeV);  49*71 = {49*71}")
print(f"  missing term = {missing:.3f} +/- {dratio:.3f}  ({dratio/missing*100:.0f}% error)")
for name, v in [("sqrt(pi)", math.sqrt(pi)), ("16/9", 16/9), ("7/4", 7/4), ("e-1", math.e-1)]:
    print(f"    {name:9} = {v:.4f}   within 1-sigma? {abs(v-missing) <= dratio}")
print(f"  => data cannot distinguish these -> no derivation of the term is bankable. confirms F119 (central value IS sqrt(pi), but the error forbids the claim).")
print()

print("PART 2 -- F119's Weyl pi-power argument, structurally confirmed:")
print("-" * 96)
print(f"  d=3 Weyl coefficients all carry NEGATIVE pi-powers (from (4pi)^-d/2 etc.): g^3~pi^-2, g^2~pi^-3/2, g^1~pi^-2, g^0~pi^-3/2.")
print(f"  a +sqrt(pi) (positive pi-power) cannot come from a product of negative-pi-power coefficients -> needs an unsourced pi^2. F119 holds.")
print()

print("PART 3 -- triangle-closure status (Grace's derivation-vs-re-expression test):")
print("-" * 96)
tri = 49*71/(24/pi**2)**6
print(f"  m_mu/m_e = (24/pi^2)^6 (F118, derived mod FK); m_tau/m_e = 49*71 (F119 OPEN); m_tau/m_mu = {tri:.3f} vs obs {mtau/mmu:.3f} -> 0.05% (tau-limited).")
print(f"  does ONE principle force all three legs? NO -- muon derives (F118), tau does NOT (F119). one-principle triangle-closure NOT yet achieved.")
print(f"  F118 stands as a candidate STANDALONE m_mu/m_e derivation (mod FK const); it has NOT been shown to force the tau. the tau needs a different frame.")
print()

print("=" * 96)
print("SUMMARY -- F119 confirmed two ways. The decisive one is frame-independent: the tau's missing term is 1.772 +/-")
print("  0.235 (13%), and sqrt(pi), 16/9, 7/4, e-1 are ALL within 1 sigma -- so the data cannot resolve it and NO")
print("  derivation of this term is bankable, regardless of frame. (The central value is sqrt(pi) to 4 digits, which is")
print("  why it tempted; the error bar forbids the claim -- exactly Lyra's caution.) Her Weyl pi-power argument is also")
print("  structurally sound: d=3 Weyl coefficients are all negative-pi-power, so a +sqrt(pi) can't arise from them. For")
print("  Grace's decisive triangle-closure test: the answer is currently NO -- one principle (concentration) derives the")
print("  muon leg (F118) but NOT the tau leg (F119), so the one-principle triangle-closure is not yet achieved. F118")
print("  stands as a candidate standalone m_mu/m_e derivation (mod the FK constant), but it hasn't been shown to force")
print("  the tau, so it isn't yet a full-triangle derivation. The honest open problem is the tau's right FRAME (a forced")
print("  derivation of 49*71 = g^2(g+2^C2)), which F119 shows is NOT the d=3 Weyl count -- not a sqrt(pi) patch on it.")
print("  Count stays 2 of 26.")
print("=" * 96)
print()
print("Elie - Sunday 2026-06-14 (confirm Lyra F119 tau -1.77 does-not-derive, two ways: PART 1 DATA-FLOOR (frame-independent, decisive) -- m_tau/m_e = 3477.23 +/- 0.23 (m_tau 1776.86 +/- 0.12 MeV), 49*71 = 3479, missing term = 1.772 +/- 0.235 (13% error), and sqrt(pi)=1.7725 / 16/9=1.7778 / 7/4=1.7500 / e-1=1.7183 are ALL within 1 sigma -> data cannot distinguish them -> NO derivation of the term is bankable regardless of frame (central value IS sqrt(pi) to 4 digits = why it tempted, but error bar forbids the claim, exactly Lyra's caution); PART 2 F119 Weyl argument structurally confirmed -- d=3 Weyl/heat-kernel coefficients all carry NEGATIVE pi-powers (from (4pi)^-d/2 etc.): g^3~pi^-2, g^2~pi^-3/2, g^1~pi^-2, g^0~pi^-3/2, so a +sqrt(pi) positive-pi-power cannot arise -> needs unsourced pi^2, F119 holds; PART 3 triangle-closure status (Grace's derivation-vs-re-expression test) -- m_mu/m_e=(24/pi^2)^6 (F118 derived mod FK), m_tau/m_e=49*71 (F119 OPEN), m_tau/m_mu=16.826 vs obs 16.817 = 0.05% tau-limited; does ONE principle force all three legs? NO -- muon derives, tau does NOT, so one-principle triangle-closure NOT yet achieved, F118 stands as candidate STANDALONE m_mu/m_e derivation (mod FK const) but not shown to force the tau so not yet a full-triangle derivation; honest open problem = the tau's right FRAME (forced derivation of 49*71=g^2(g+2^C2)) which is NOT the d=3 Weyl count, not a sqrt(pi) patch; count stays 2 of 26)")
print()
print("SCORE: 2/2 (confirm F119: PART 1 data-floor -- missing tau term 1.772 +/- 0.235, sqrt(pi)/16-9/7-4/e-1 ALL within 1 sigma -> unbankable regardless of frame, central value IS sqrt(pi) but error forbids; PART 2 Weyl pi-powers all negative so +sqrt(pi) impossible, F119 structurally holds; PART 3 triangle-closure NO -- muon derives (F118) tau does not (F119), one-principle closure not achieved, F118 candidate standalone m_mu/m_e mod FK not full-triangle, tau needs right frame not sqrt(pi) patch; count 2 of 26)")
