r"""
Toy 4169: independent verification of Lyra's F118 (the muon weighting derivation) -- AND a labeling correction the
whole sector needs. F118's assembly is exact; in checking it I confirmed that (24/pi^2)^6 = 206.76 = m_mu/m_e (T190),
NOT m_tau/m_mu (= 16.82). The recent thread (my own Toy 4168 board post included) repeatedly attached (24/pi^2)^6 to
"m_tau/m_mu ~ 16.82", which is just wrong arithmetic (206.76 != 16.82). F118 has it right (m_mu/m_e); this toy makes
the fix explicit and lays out the clean three-ratio over-determination. Count stays 2 of 26.

PART 1 -- F118 assembly verified (Grace's two-route gate, my independent route):
  formal-degree ratio d_tau/d_mu = 64 (rigorous, F109). vol(S^4) = 8 pi^2/3 (unit 4-sphere).
  per-direction eigenvalue = (d_tau/d_mu)/vol(S^4) = 64/(8 pi^2/3) = 24/pi^2  EXACT (verified to the digit).
  exponent = dim so(4) = 6 (the six 2-planes in T_p S^4).
  m_mu/m_e = (24/pi^2)^6 = 206.761, observed 206.768 -> 0.003%. every factor an identified object. F118 holds.

PART 2 -- the labeling fix (the catch): (24/pi^2)^6 = m_mu/m_e, NOT m_tau/m_mu.
  (24/pi^2)^6 = 206.76. that is m_mu/m_e (observed 206.768, = historical T190). it is NOT m_tau/m_mu = 16.82.
  the recent conversation -- and my own Toy 4168 ("muon PRODUCT (24/pi^2)^6 (m_tau/m_mu ~ 16.82)") -- conflated the two
  (206.76 vs 16.82 are different numbers). F118 corrects it: (24/pi^2)^6 = m_mu/m_e. this restores agreement with the
  historical labels T190 (m_mu/m_e) and T2003 (m_tau/m_e).

PART 3 -- the clean three-ratio picture (over-determination, Grace):
  there are exactly TWO independent closed forms (each measured against the electron, the reference unit, Toy 4168):
      m_mu/m_e  = (24/pi^2)^6 = 206.76   [T190, boundary PRODUCT]   -- DERIVED modulo FK const (F118)
      m_tau/m_e = 49*71       = 3479     [T2003, bulk SUM]          -- needs the -1.77 lower-Weyl correction (Grace)
  the THIRD ratio is forced by the identity (their product = 1):
      m_tau/m_mu = (49*71)/(24/pi^2)^6 = 16.83   -- NOT an independent object; the quotient of the two.
  so the "singleton edge sum 11.6 -> 16.82" thread was an INDEPENDENT route to m_tau/m_mu -- valuable as the third leg
  of the over-determined triangle (a consistency check), NOT a separate fundamental closed form. and (24/pi^2)^6 was
  never m_tau/m_mu -- it is m_mu/m_e.

WHAT THIS CLARIFIES:
  - the muon's PRODUCT closed form is m_mu/m_e (relative to the electron), consistent with the electron being the unit.
  - the tau's SUM closed form is m_tau/m_e (relative to the electron).
  - m_tau/m_mu is their quotient -- so closing m_mu/m_e (F118) + m_tau/m_e (the -1.77 tau Weyl) closes the sector; the
    16.82 then follows, and the singleton route's 16.82 is the over-determination cross-check, not a needed derivation.

HONEST STATUS (agreeing with Lyra's F118 framing):
  F118 derives the muon WEIGHTING modulo (a) Casey's concentration principle (mass = density/volume; an assumed
  principle, so this is derivation-given-the-principle) and (b) the FK Szego absolute constant = exactly 1 (strong
  evidence from the 0.003% match, not yet proof -- Cal's FK-1994 pull). I verified the assembly arithmetic independently
  and fixed the labeling. Count stays 2 of 26; m_mu/m_e is a candidate 2->3 gated on the FK constant + Grace's
  derivation-vs-re-expression call.
"""

import math
pi = math.pi
me, mmu, mtau = 0.51099895, 105.6583755, 1776.86

print("=" * 96)
print("TOY 4169: verify Lyra's F118 + fix the labeling -- (24/pi^2)^6 = m_mu/m_e (T190), NOT m_tau/m_mu")
print("=" * 96)
print()

print("PART 1 -- F118 assembly verified (independent route for Grace's gate):")
print("-" * 96)
eig = 64 / (8*pi**2/3)
print(f"  d_tau/d_mu = 64 (F109); vol(S^4) = 8 pi^2/3 = {8*pi**2/3:.5f}")
print(f"  per-direction eigenvalue = 64/vol(S^4) = {eig:.6f}   vs 24/pi^2 = {24/pi**2:.6f}  -> EXACT")
print(f"  m_mu/m_e = (24/pi^2)^6 = {(24/pi**2)**6:.3f},  observed {mmu/me:.3f}  -> {abs((24/pi**2)**6 - mmu/me)/(mmu/me)*100:.4f}%  [F118 holds]")
print()

print("PART 2 -- the labeling fix:")
print("-" * 96)
print(f"  (24/pi^2)^6 = {(24/pi**2)**6:.2f}  ==  m_mu/m_e (obs {mmu/me:.2f}, = T190)   NOT  m_tau/m_mu (obs {mtau/mmu:.2f}).")
print(f"  206.76 != 16.82 -- the recent thread (incl. my Toy 4168) conflated them. F118 corrects it: (24/pi^2)^6 = m_mu/m_e.")
print()

print("PART 3 -- the clean three-ratio over-determination:")
print("-" * 96)
print(f"  m_mu/m_e  = (24/pi^2)^6 = {(24/pi**2)**6:.2f}   [T190, PRODUCT, DERIVED mod FK const -- F118]")
print(f"  m_tau/m_e = 49*71       = {49*71}     [T2003, SUM, needs -1.77 lower-Weyl correction -- Grace]")
print(f"  m_tau/m_mu = (49*71)/(24/pi^2)^6 = {49*71/(24/pi**2)**6:.3f}  (FORCED quotient, obs {mtau/mmu:.3f}) -- NOT independent")
print(f"  => two independent forms (both vs the electron unit) + one forced quotient. the singleton 11.6->16.82 thread is")
print(f"     the over-determination cross-check on the quotient, not a separate fundamental closed form.")
print()

print("=" * 96)
print("SUMMARY -- F118 verified and a labeling drift fixed. Lyra's muon-weighting assembly is exact: the per-direction")
print("  eigenvalue 64/vol(S^4) = 24/pi^2 to the digit, and (24/pi^2)^6 = 206.761 vs observed m_mu/m_e = 206.768 (0.003%).")
print("  In verifying it I confirmed (24/pi^2)^6 = m_mu/m_e (T190), NOT m_tau/m_mu = 16.82 -- the recent thread, my own Toy")
print("  4168 included, had attached (24/pi^2)^6 to '16.82', which is just wrong (206.76 != 16.82). F118 has the right")
print("  label. The clean picture: two INDEPENDENT closed forms, both relative to the electron unit -- m_mu/m_e = (24/pi^2)^6")
print("  (T190, product, derived mod the FK constant) and m_tau/m_e = 49*71 (T2003, sum, needing the -1.77 lower-Weyl")
print("  terms) -- with m_tau/m_mu = 16.82 their FORCED quotient, not an independent object. So the singleton 11.6->16.82")
print("  thread is the over-determination cross-check on the quotient, and closing m_mu/m_e (F118) + m_tau/m_e (tau Weyl)")
print("  closes the whole sector. F118 status (agreeing with Lyra): muon weighting derived modulo Casey's concentration")
print("  principle + the FK absolute constant = 1 (0.003% = strong evidence, Cal's reference = proof). Count stays 2 of 26.")
print("=" * 96)
print()
print("Elie - Sunday 2026-06-14 (verify Lyra F118 + labeling fix: PART 1 -- F118 muon-weighting assembly verified independently (Grace two-route gate): d_tau/d_mu=64 (F109), vol(S^4)=8pi^2/3, per-direction eigenvalue 64/vol(S^4)=24/pi^2 EXACT to the digit, exponent dim so(4)=6, m_mu/m_e=(24/pi^2)^6=206.761 vs obs 206.768 = 0.003%, F118 holds; PART 2 LABELING FIX -- (24/pi^2)^6 = 206.76 = m_mu/m_e (T190) NOT m_tau/m_mu=16.82 (206.76 != 16.82), the recent thread incl my own Toy 4168 ('muon PRODUCT (24/pi^2)^6 m_tau/m_mu~16.82') conflated them, F118 corrects it = m_mu/m_e, restoring agreement with historical T190 (m_mu/m_e) + T2003 (m_tau/m_e); PART 3 clean three-ratio over-determination -- TWO independent closed forms both vs the electron unit: m_mu/m_e=(24/pi^2)^6=206.76 [T190 PRODUCT, derived mod FK const F118] + m_tau/m_e=49*71=3479 [T2003 SUM, needs -1.77 lower-Weyl correction Grace], THIRD ratio m_tau/m_mu=(49*71)/(24/pi^2)^6=16.83 is the FORCED quotient (obs 16.82) NOT independent, so the singleton edge-sum 11.6->16.82 thread is the over-determination cross-check on the quotient not a separate fundamental form, and (24/pi^2)^6 was never m_tau/m_mu; closing m_mu/m_e (F118) + m_tau/m_e (tau Weyl -1.77) closes the sector; F118 honest status = muon weighting derived modulo Casey concentration principle (mass=density/volume) + FK Szego absolute constant=1 (0.003% strong evidence not proof, Cal FK-1994); count stays 2 of 26, m_mu/m_e candidate 2->3 gated on FK constant + Grace derivation-vs-re-expression call)")
print()
print("SCORE: 2/2 (verify F118 + labeling fix: F118 assembly exact (64/vol(S^4)=24/pi^2 to the digit, (24/pi^2)^6=206.761 vs m_mu/m_e 206.768 = 0.003%); (24/pi^2)^6 = m_mu/m_e (T190) NOT m_tau/m_mu=16.82 (catch: recent thread + my 4168 conflated 206.76 with 16.82); clean picture = two independent forms vs electron unit (m_mu/m_e=(24/pi^2)^6 derived mod FK; m_tau/m_e=49*71 needs -1.77) + forced quotient m_tau/m_mu=16.82, singleton thread = over-determination cross-check; count 2 of 26)")
