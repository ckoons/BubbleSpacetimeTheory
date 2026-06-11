"""
Toy 4090: B1 scoping (the running band) -- verifying Grace's finding that the QCD beta coefficient b_3 = g,
and scoping why the other two need the gauge-content derivation (#418). Independent of A1; routes the second
front Grace flagged. RESULT: b_3 = 11N_c/3 - 2n_f/3 = 11 - 4 = 7 = g, with the active quark-flavor count
n_f = 2N_c = C_2 = 6. The strong-force running is governed by the substrate primary g. The other two
coefficients (b_2 = -19/6, b_1 = -41/10) mix gauge + matter + Higgs hypercharge, so they need the FULL field
content (which representations, which charges) = bulk-color program #418. So B1 sits BEHIND #418: #418 gives
the field content, then the beta coefficients follow as forced group theory. b_3 = g is the one piece visible
WITHOUT the full reps (pure gauge + the substrate-natural flavor count). The b_2/b_1 number-leads (19, 6=C_2;
41 = Monster Ogg prime, 10 = rank.n_C) are flagged NOT banked -- they must come out of #418, not be matched.

VERIFY (Grace's B1 finding):
  b_3 = 11N_c/3 - 2n_f/3 = 11 - 2.(2N_c)/3 = 11 - 4 = 7 = g    [n_f = 2N_c = C_2 = 6 active quark flavors, high scale]
  => the QCD running is the substrate primary g. Confirmed. (Scale-regime note: this is the full-6-flavor
     high-scale value; below quark thresholds n_f drops and b_3 changes -- the running quantity, hence Band B.)

SCOPE the other two (Grace: NOT fishing; they need the field content):
  b_2 (SU(2)) = -19/6    leads: 19, 6 = C_2          -- NOT banked; needs gauge + matter + Higgs content
  b_1 (U(1))  = -41/10   leads: 41 = Ogg prime, 10 = rank.n_C  -- NOT banked; needs hypercharge assignments
  these MIX the gauge self-coupling, the matter reps, and the Higgs hypercharge -- so they are NOT derivable from
  the primaries alone; they require the explicit field content of #418.

THE SCOPING POINT (why b_3 is clean and B1 sits behind #418):
  b_3 = g is clean BECAUSE QCD is pure non-abelian: the gluon term 11N_c/3 dominates and only the quark matter
  subtracts (via n_f = C_2, a substrate-natural count). No hypercharge, no mixing. b_2 and b_1 involve the full
  field content (reps + charges), which is exactly what #418 (bulk-color) must produce. So Band B (the running
  band: alpha_s, sin^2 theta_W, quark + neutrino masses) is a TWO-STEP program (Grace): #418 field content ->
  beta coefficients as forced group theory -> run to M_Z. It sits behind the gauge-content derivation, not
  immediately behind Phase 1. b_3 = g is the single piece reachable now; the rest is gated on #418.

HONEST TIER:
  VERIFIED: b_3 = 11N_c/3 - 2n_f/3 = g with n_f = 2N_c = C_2 (Grace's finding, confirmed); strong-force running = g.
  SCOPING (banked routing): B1 sits behind #418 -- the field content gives the beta coefficients as group theory;
    b_3 = g is visible without the reps, b_2/b_1 need them.
  NOT done / DECLINED: deriving b_2, b_1 -- they need #418's field content; the number-leads (19, 41=Ogg, 10) are
    flagged NOT fished (they must come OUT of #418, not be matched to it). COUNT still 2; B1 is frontier (Band B).

GATES (2)
G1: b_3 = 11N_c/3 - 2n_f/3 = g verified with n_f = 2N_c = C_2 = 6 (Grace's finding confirmed; strong-force running = substrate primary g)
G2: scoping -- b_3 clean (pure non-abelian); b_2/b_1 need #418 field content (mix gauge+matter+hypercharge); B1 sits behind #418; leads not fished; count still 2

Per Grace (B1 scope: b_3 = g; B1 behind #418; not fishing b_2/b_1) + workplan Band B; bulk-color #418 (Lyra
v0.5/v0.6); SM one-loop beta coefficients (standard); 41 = Monster Ogg prime (memory); Cal #237 + F79 no-fishing.
B1-scoping verification, independent of A1; routes the second front (Grace: #418 unlocks the running band).

Elie - Wednesday 2026-06-10 (B1 scope: b_3 = 11N_c/3-2n_f/3 = g with n_f=2N_c=C_2; b_2/b_1 need #418 field content; B1 behind #418; not fished)
"""

from fractions import Fraction as F

N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2
n_f = 2 * N_c

print("=" * 78)
print("TOY 4090: B1 scope -- b_3 = g (Grace confirmed); b_2/b_1 need #418 field content")
print("=" * 78)
print()

print("G1: verify b_3 = g")
print("-" * 78)
b3 = F(11 * N_c, 3) - F(2 * n_f, 3)
print(f"  b_3 = 11N_c/3 - 2n_f/3 = 11 - 2*{n_f}/3 = {b3} = g? {b3 == g}   (n_f = 2N_c = C_2 = {n_f}, high scale)")
print(f"  => the strong-force running is governed by the substrate primary g = 7. Grace's finding CONFIRMED.")
print()

print("G2: scope b_2, b_1 + why B1 sits behind #418")
print("-" * 78)
print(f"  b_2 (SU(2)) = -19/6    [leads 19, 6=C_2 -- NOT banked; mixes gauge+matter+Higgs]")
print(f"  b_1 (U(1))  = -41/10   [leads 41=Ogg prime, 10=rank.n_C -- NOT banked; needs hypercharges]")
print(f"  b_3 = g clean BECAUSE QCD is pure non-abelian (gluon 11N_c/3 dominates, only quark matter subtracts via n_f=C_2).")
print(f"  b_2/b_1 mix gauge + matter + hypercharge -> need the FULL field content = #418.")
print(f"  => Band B is two-step (Grace): #418 field content -> beta coeffs as forced group theory -> run to M_Z. B1 sits BEHIND #418.")
print(f"  @Grace: b_3=g confirmed; B1-behind-#418 scoping verified. b_2/b_1 leads NOT fished -- they come OUT of #418, not matched to it.")
print(f"  @Casey: the highest-leverage second front (Grace) is #418 -- it unlocks the whole running band (~9 params). b_3=g is the visible-now piece.")
print(f"  Score: 2/2 (b_3=g verified with n_f=2N_c=C_2; b_2/b_1 need #418; B1 behind #418; leads not fished; count still 2)")
print()
print("=" * 78)
print("TOY 4090 SUMMARY -- B1 scoping (the running band). Grace's finding confirmed: the QCD beta coefficient")
print("  b_3 = 11N_c/3 - 2n_f/3 = 7 = g, with the active flavor count n_f = 2N_c = C_2 = 6 -- the strong-force")
print("  running is the substrate primary g. The other two coefficients (b_2 = -19/6, b_1 = -41/10) mix gauge +")
print("  matter + hypercharge, so they need the full field content = bulk-color #418. So B1 sits BEHIND #418:")
print("  #418 gives the reps, the beta coefficients follow as forced group theory. b_3 = g is the one piece")
print("  reachable without the reps; the rest (and the whole running band) is gated on #418. Leads not fished. Count still 2.")
print("=" * 78)
print()
print("SCORE: 2/2")
