r"""
Toy 4171: scrutiny + support for Lyra's F120 (the tau as a cone-tip with a pi-free conical deficit). This is a
peak-convergence moment (F112 pi-free + F119 sqrt-pi-fails + cone all "point the same way"), so it's where Cal #27
fires hardest. Verdict: F120's CHARACTER argument is right and a real improvement -- but the cone still has to FORCE a
unique value, and even then the tau mass alone cannot confirm it (data floor). The way to actually bank the tau is
over-determination: find a SECOND observable carrying the same deficit. Count stays 2 of 26.

WHAT F120 GETS RIGHT (verified, real improvement):
  - the -1.77 is REAL: gap = 49*71 - m_tau/m_e = 1.772 +/- 0.235 = 7.5 sigma. so 49*71 = 3479 is excluded as the EXACT
    value; there genuinely is a correction to account for. (the cone does NOT dissolve it -- correct.)
  - the CHARACTER argument is sound: a conical-deficit RATIO (solid-angle/angle ratio) is pi-FREE, and the tau is
    pi-free (F112: bulk/vertex = integer 49*71). so the correction must be pi-free -- which is exactly why sqrt(pi)
    (pi-CARRYING) failed (F119). the cone explains the failure on character, not just frame. genuine insight.
  - the FRAME argument is sound: a cone TIP is a point-coupling, not a bulk Weyl count -- so there was never a g^1
    Weyl term to carry the correction (F119's wrong machine). a tip has a deficit, not a Weyl expansion.

WHAT THE CONE STILL HAS TO DO (the honest gate -- Cal #27):
  1. FORCE a unique value. "pi-free rational near 1.77" is NOT a prediction by itself: there are 13 pi-free rationals
     (denominator <= 9) within 1 sigma of the gap -- 5/3, 7/4, 8/5, 9/5, 11/6, 11/7, 12/7, 13/7, 13/8, 14/9, 15/8,
     16/9, 17/9. the cone deficit must come out a SPECIFIC one from the geometry, with NO targeting of 1.77.
  2. survive the DATA FLOOR. even a forced cone value near 1.77 is only CONSISTENT, not CONFIRMED: m_tau is 13%-precise
     on the gap, so the data cannot distinguish the cone's value from a dozen neighbors. a forced cone deficit near
     1.77 would be supportive evidence, not a clean bank, from m_tau alone.

THE WAY TO ACTUALLY BANK THE TAU (beat the data floor with over-determination):
  the single m_tau gives only 13% on the gap -- that ceiling is intrinsic. but if the SAME cone-tip deficit appears in
  a SECOND tau observable (e.g. a tau-sector ratio, a width, or the cone deficit showing up in another lepton/quark
  vertex), then two independent appearances of one forced value beat the single-observable floor -- the same
  over-determination logic that makes the muon triangle strong. so the productive tau program is: (a) Lyra computes the
  forced D_IV^5 Lorentz-cone tip deficit (pi-free, no fitting); (b) find a second place that deficit must appear. (b)
  is what converts "consistent with 1.77" into "confirmed," which m_tau alone never can.

HONEST STATUS:
  F120 is the cleanest tau FRAME so far (pi-free character + tip-not-Weyl) and correctly explains F119's failure. it is
  NOT a closure: the deficit value is uncomputed, "pi-free near 1.77" is 13-fold degenerate at the data floor, and the
  tau mass alone can't confirm a forced value. the tau remains OPEN, now with the right frame and a clear two-step path
  (force the deficit + find its second appearance). count stays 2 of 26; muon F118 candidate 2->3 (mod FK) unaffected.
"""

import math
me, mtau, dmtau = 0.51099895, 1776.86, 0.12

print("=" * 96)
print("TOY 4171: F120 cone reframe -- character RIGHT (pi-free), but cone must FORCE a value + beat the data floor")
print("=" * 96)
print()

mratio, dratio = mtau/me, dmtau/me
gap = 49*71 - mratio
print("what F120 gets right (verified):")
print("-" * 96)
print(f"  -1.77 is REAL: gap = 49*71 - m_tau/m_e = {gap:.3f} +/- {dratio:.3f} = {gap/dratio:.1f} sigma -> 49*71 excluded as EXACT (cone doesn't dissolve it).")
print(f"  CHARACTER: a conical-deficit ratio is pi-FREE; the tau is pi-free (F112) -> correction must be pi-free -> why sqrt(pi) (pi-carrying) failed (F119). real insight.")
print(f"  FRAME: a cone TIP is a point-coupling, not a bulk Weyl count -> no g^1 Weyl term to carry it (F119 wrong machine). sound.")
print()

print("what the cone still has to do (Cal #27 gate):")
print("-" * 96)
lo, hi = gap-dratio, gap+dratio
rats = [(p, q) for q in range(2, 10) for p in range(3, 20) if math.gcd(p, q) == 1 and lo <= p/q <= hi]
print(f"  1. FORCE a unique value: there are {len(rats)} pi-free rationals (denom<=9) within 1 sigma -> {', '.join(f'{p}/{q}' for p,q in rats)}")
print(f"     'pi-free near 1.77' is {len(rats)}-fold degenerate -- the cone must give a SPECIFIC one from geometry, no targeting of 1.77.")
print(f"  2. DATA FLOOR: m_tau is {dratio/gap*100:.0f}%-precise on the gap -> even a forced cone value is CONSISTENT, not CONFIRMED, from m_tau alone.")
print()

print("the way to actually bank the tau (over-determination beats the floor):")
print("-" * 96)
print(f"  (a) Lyra computes the FORCED D_IV^5 Lorentz-cone tip deficit (pi-free, no fitting).")
print(f"  (b) find a SECOND observable carrying the same deficit -> two independent appearances of one forced value beat the 13%% single-m_tau floor.")
print(f"  (b) is what turns 'consistent with 1.77' into 'confirmed' -- the same over-determination logic that makes the muon triangle strong.")
print()

print("=" * 96)
print("SUMMARY -- F120 is a real improvement on the tau, and the scrutiny confirms its good parts while pinning the gap.")
print("  RIGHT: the -1.77 is a real 7.5-sigma effect (49*71 is not exact); a conical deficit is pi-free, the tau is pi-free")
print("  (F112), so the correction must be pi-free -- which explains why sqrt(pi) failed on CHARACTER (F119), not just")
print("  frame; and a cone tip is a point-coupling, not a Weyl count, so there was never a g^1 term to carry it. That's")
print("  the cleanest tau frame yet. NOT YET CLOSURE: 'pi-free rational near 1.77' is 13-fold degenerate at the data floor")
print("  (5/3, 7/4, ..., 17/9 all within 1 sigma), so the cone must FORCE a specific value from geometry (no targeting),")
print("  and even then m_tau's 13% precision can't confirm it against neighbors. The way to actually bank it is over-")
print("  determination: compute the forced cone-tip deficit AND find a second observable carrying the same deficit -- two")
print("  appearances of one forced value beat the single-m_tau floor (the logic that makes the muon triangle strong). The")
print("  tau stays OPEN with the right frame and a concrete two-step path. Count 2 of 26; muon F118 (cand 2->3) unaffected.")
print("=" * 96)
print()
print("Elie - Sunday 2026-06-14 (scrutiny+support for Lyra F120 tau-as-cone-tip-deficit, Cal #27 at peak convergence: RIGHT -- (i) the -1.77 is REAL, gap = 49*71 - m_tau/m_e = 1.772 +/- 0.235 = 7.5 sigma, 49*71=3479 excluded as EXACT (cone does NOT dissolve it); (ii) CHARACTER argument sound -- a conical-deficit ratio is pi-FREE and the tau is pi-free (F112 bulk/vertex integer 49*71), so the correction must be pi-free, which is exactly why sqrt(pi) (pi-carrying) failed (F119) = explains the failure on CHARACTER not just frame, genuine insight; (iii) FRAME argument sound -- a cone TIP is a point-coupling not a bulk Weyl count, so no g^1 Weyl term to carry it (F119 wrong machine); NOT YET CLOSURE (the gate) -- (1) the cone must FORCE a UNIQUE value: there are 13 pi-free rationals (denom<=9) within 1 sigma (5/3,7/4,8/5,9/5,11/6,11/7,12/7,13/7,13/8,14/9,15/8,16/9,17/9), so 'pi-free near 1.77' is 13-fold degenerate, the cone deficit must come out a SPECIFIC one from geometry with NO targeting of 1.77; (2) DATA FLOOR -- m_tau is 13% precise on the gap so even a forced cone value is CONSISTENT not CONFIRMED from m_tau alone; THE WAY TO BANK -- over-determination: (a) Lyra computes the forced D_IV^5 Lorentz-cone tip deficit (pi-free, no fit), (b) find a SECOND observable carrying the same deficit -> two independent appearances of one forced value beat the single-m_tau 13% floor (same logic as the muon triangle), (b) converts 'consistent with 1.77' into 'confirmed' which m_tau alone never can; tau stays OPEN with the right frame + concrete two-step path; count 2 of 26, muon F118 cand 2->3 mod FK unaffected)")
print()
print("SCORE: 2/2 (F120 cone reframe scrutiny: RIGHT -- -1.77 real (7.5 sigma, 49*71 not exact); conical deficit pi-free matches tau pi-free (F112) -> explains sqrt(pi) failure on CHARACTER (F119); tip = point-coupling not Weyl count (right frame); NOT CLOSURE -- 13 pi-free rationals within 1 sigma so cone must FORCE a unique value (no targeting), and data floor (13%) can't confirm vs neighbors; BANK via over-determination = forced cone deficit + a SECOND observable carrying it; tau open with right frame + two-step path; count 2 of 26)")
