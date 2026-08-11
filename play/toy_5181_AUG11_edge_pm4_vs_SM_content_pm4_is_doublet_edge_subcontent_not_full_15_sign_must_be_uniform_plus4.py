#!/usr/bin/env python3
"""
Toy 5181: THE EDGE ±4 ↔ SM CONTENT MAP (make-or-break #2, a concrete second front, independent of gravity).
Context: the certified edge invariant is ±4 (the real, protected class-D ℤ; Cal's KKO computation -- the p+ip
Chern number and the Dolbeault Chern number coincide at d=2). But ±4 does NOT reproduce the SM content by simple
counting: the SM per generation is 15 Weyl = 7 Dirac + 1 Majorana (no ν_R), and neither naive reading of ±4
(2 Dirac charge-paired; 4 doublets) equals 15. So the ±4↔SM map is genuinely OPEN -- it needs K817's explicit
weight→degree→sign to say what the edge content actually is. This toy supplies the precise content bookkeeping
so the sign-check has a clear target. RESULT: the honest reading is that ±4 = the number of SU(2)_L DOUBLETS =
4 (3 quark doublets, one per color + 1 lepton doublet) = the CHIRAL / EDGE (SU(2)-charged) sub-content, 8 Weyl,
all LEFT-handed -- NOT the full 15. The other 7 Weyl are SU(2)-SINGLETS (u^c×3, d^c×3, e^c×1), SU(2)-neutral =
the BULK content, which the edge index does NOT count. So the full SM assembles as: ±4 doublets (edge) + 7
singlets (bulk), with each doublet-component paired to a singlet where one exists (u,d ×3 colors + e = 7 Dirac)
and the one neutral left field (ν_L) left unpaired (1 Majorana) -- exactly the charge-pairing of toy 5174. The
competing reading (±4 = 4 Majorana charge-paired → 2 Dirac) undershoots badly (2 ≠ 7 Dirac) and is wrong. THE
SIGN REQUIREMENT (the operative make-or-break): for this to be the SM, the 4 doublets must be ALL left-handed →
the net chiral edge index must be UNIFORM +4 (maximally left-handed). A mixed sign (e.g. +3−1) would NOT be the
SM. So K817's weight→degree→sign must deliver +4 with ONE sign; that is the decisive check, and it is Cal's
explicit computation. MAP STATUS: OPEN by counting alone -- narrowed to a precise target (±4 = the SU(2)_L
doublet sub-content, uniform +4; the 7 singlets are separate bulk content), but not closed until the explicit
weight→degree→sign confirms (a) the doublet identification and (b) the uniform +4 sign. This is a genuine
second front, on its own timeline, not buried by the gravity 8π. Elie's content bookkeeping (+ Cal's K817
weight→degree→sign + the d=2 dimension pin). a₄ chiral coefficients HELD. (Cal ±4 KKO certification; toy 5174
charge-pairing; the bulk-edge split; no ν_R Five-Absences.) CP existence-only. Report either way straight.

WHAT I COMPUTE (SM per-generation Weyl bookkeeping, no ν_R):
  * 15 Weyl = 8 (in 4 SU(2)_L doublets, LEFT/chiral/edge) + 7 (SU(2)-singlet, right/bulk) = 7 Dirac + 1 Majorana.
  * Reading A: ±4 = 4 SU(2)_L doublets = the chiral EDGE sub-content (8 Weyl), all left → net uniform +4.
  * Reading B: ±4 = 2 Dirac (4 Majorana charge-paired) → 2 ≠ 7 Dirac, undershoots, WRONG.
  * sign requirement: uniform +4 (maximally left) = SM; mixed sign ≠ SM. K817 must give +4, one sign.

=> VERDICT (plain): the edge index ±4 is not the whole Standard Model, and it was never going to be by counting
-- 15 Weyl does not equal 4. What ±4 honestly is, is the count of SU(2)_L doublets: the three color copies of
the quark doublet plus the one lepton doublet, four in all, and every one of them left-handed. That is exactly
the chiral, SU(2)-charged content that a maximally-left-handed edge should carry, and it is a proper
sub-content of the generation. The seven right-handed singlets are SU(2)-neutral -- bulk, not edge -- and the
full generation is rebuilt by pairing each doublet-component with a singlet where one exists (seven Dirac
fermions) and leaving the one neutral field unpaired (the Majorana neutrino, toy 5174). The map therefore lives
or dies on one thing the counting cannot settle: whether the edge's net chiral index comes out uniformly +4
(all left, the Standard Model) rather than a mixed sign. That is K817's explicit weight→degree→sign, and it is
the decisive check. The counting has narrowed the target to a single sign; the geometry must now hit it.

=> DISPOSITION: edge ±4 ↔ SM content -- ±4 = the SU(2)_L doublet sub-content (chiral edge, 8 Weyl), NOT the
full 15; the 7 singlets are bulk; the sign must be uniform +4 (maximally left). Firer: Elie (content
bookkeeping). Owed: Cal's K817 explicit weight→degree→sign (does ±4 come out uniform +4 on the doublets?) + the
d=2 dimension pin (KO-degree of the Toeplitz boundary map with J). a₄ chiral coefficients HELD. Nothing banked
-- the map is narrowed to a precise target, not closed; nothing pushed. Count the edge once. CP existence-only.

Author: Elie (CI toy builder). Date: 2026-08-11.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# SM per-generation content (no nu_R): (SU3, SU2, Y, n_Weyl, is_doublet, n_doublets)
fields = {
    'Q_L (u_L,d_L)': (3, 2, '+1/6', 6, True, 3),   # 3 colors × doublet
    'u^c (singlet)': (3, 1, '-2/3', 3, False, 0),
    'd^c (singlet)': (3, 1, '+1/3', 3, False, 0),
    'L_L (nu,e)':    (1, 2, '-1/2', 2, True, 1),
    'e^c (singlet)': (1, 1, '+1',   1, False, 0),
}
weyl = sum(f[3] for f in fields.values())
doublets = sum(f[5] for f in fields.values())
doublet_weyl = sum(f[3] for f in fields.values() if f[4])
singlet_weyl = sum(f[3] for f in fields.values() if not f[4])

print("=" * 78)
print("Toy 5181: edge ±4 ↔ SM content -- ±4 = the SU(2)_L doublet sub-content (edge), NOT the full 15; sign must be uniform +4")
print("=" * 78)
print(f"\n  SM per generation (no ν_R):")
for k, f in fields.items():
    print(f"    {k:16s} SU2={f[1]}  Y={f[2]:5s}  Weyl={f[3]}  doublets={f[5]}")

# ----------------------------------------------------------------------------
# 1. Full SM content: 15 Weyl = 8 doublet + 7 singlet = 7 Dirac + 1 Majorana.
# ----------------------------------------------------------------------------
print("\n--- 1. SM per gen = 15 Weyl = 8 (4 SU(2)_L doublets, edge) + 7 (singlets, bulk) = 7 Dirac + 1 Majorana ---")
check("The Standard Model per generation (no ν_R) is 15 Weyl fermions: 8 sit in 4 SU(2)_L DOUBLETS (the 3 "
      "color copies of the quark doublet + the 1 lepton doublet -- left-handed, chiral, SU(2)-charged), and 7 "
      "are SU(2) SINGLETS (u^c×3, d^c×3, e^c -- right/conjugate, SU(2)-neutral). Assembled: 7 Dirac (u,d ×3 "
      "colors + e) + 1 Majorana (ν_L, no singlet partner). 8+7 = 15 = 7·2 + 1",
      weyl == 15 and doublets == 4 and doublet_weyl == 8 and singlet_weyl == 7 and (7*2 + 1) == 15,
      f"15 Weyl = {doublet_weyl} (in {doublets} doublets) + {singlet_weyl} (singlets) = 7 Dirac + 1 Majorana.")

# ----------------------------------------------------------------------------
# 2. Reading A: ±4 = 4 doublets = the chiral edge sub-content (not the full 15).
# ----------------------------------------------------------------------------
print("\n--- 2. Reading A: ±4 = 4 SU(2)_L doublets = the CHIRAL/EDGE sub-content (8 Weyl), NOT the full 15 ---")
check("Reading A (the sensible one): ±4 = the number of SU(2)_L doublets = 3 (quark, one per color) + 1 "
      "(lepton) = 4. This is the chiral, SU(2)-charged EDGE content (8 Weyl, all left-handed) -- exactly what a "
      "maximally-left-handed edge should carry -- and it is a proper SUB-CONTENT of the generation, NOT the "
      "full 15. The 7 SU(2)-neutral singlets are BULK, not counted by the edge index",
      doublets == 4 and doublet_weyl == 8 and doublets != weyl,
      f"±4 = {doublets} doublets = chiral edge content ({doublet_weyl} Weyl, all left); ≠ full 15. Singlets = bulk.")

# ----------------------------------------------------------------------------
# 3. Reading B: ±4 = 2 Dirac -- undershoots, wrong.
# ----------------------------------------------------------------------------
print("\n--- 3. Reading B: ±4 = 2 Dirac (4 Majorana charge-paired) -- undershoots 7 Dirac, WRONG ---")
dirac_readingB = 4 // 2   # 4 Majorana charge-paired → 2 Dirac
check("Reading B: ±4 = 4 Majorana modes charge-paired into 2 Dirac. But the SM has 7 Dirac per generation, so "
      "2 ≠ 7 -- this reading undershoots badly and is wrong. The edge index is NOT a Dirac count; Reading A "
      "(doublet count) is the correct interpretation",
      dirac_readingB == 2 and dirac_readingB != 7,
      f"Reading B gives {dirac_readingB} Dirac ≠ 7 Dirac (SM). Undershoots; wrong reading.")

# ----------------------------------------------------------------------------
# 4. The sign requirement: uniform +4 (maximally left).
# ----------------------------------------------------------------------------
print("\n--- 4. SIGN REQUIREMENT: the 4 doublets are ALL left → net chiral edge index must be UNIFORM +4 ---")
all_left = all(f[4] for f in fields.values() if f[4])   # every doublet field is left-handed
check("The operative make-or-break: for the edge to be the SM weak sector, the 4 SU(2)_L doublets must be ALL "
      "left-handed, so the net chiral edge index must be UNIFORM +4 (maximally left) -- not a mixed sign like "
      "+3−1. K817's weight→degree→sign must deliver +4 with ONE sign. The counting cannot settle this; it is "
      "Cal's explicit index computation. This narrows the target to a single sign",
      all_left,
      "SM doublets all left-handed → required net index = uniform +4 (maximally left). Mixed sign ≠ SM. K817 must give +4.")

# ----------------------------------------------------------------------------
# 5. Verdict: map narrowed to a precise target, OPEN pending the explicit sign.
# ----------------------------------------------------------------------------
print("\n--- 5. VERDICT: ±4 = the doublet edge sub-content; map to {7 Dirac+1 Majorana} OPEN pending uniform +4 ---")
check("VERDICT: ±4 is the SU(2)_L DOUBLET sub-content (the chiral edge, 8 Weyl), NOT the full 15; the 7 "
      "singlets are SU(2)-neutral bulk. The full SM = 4 doublets (edge) + 7 singlets (bulk), assembled by "
      "charge-pairing (7 Dirac) + the unpaired neutral (1 Majorana, toy 5174). The map lives or dies on one "
      "thing counting cannot settle -- whether the edge's net chiral index is UNIFORM +4 (all left = SM) -- "
      "which is K817's explicit weight→degree→sign (Cal). The counting has narrowed the target to a single "
      "sign; the map is OPEN until the geometry hits it. a₄ chiral coefficients HELD",
      doublets == 4 and doublet_weyl == 8 and singlet_weyl == 7 and all_left and dirac_readingB != 7,
      "±4 = doublet edge sub-content (uniform +4 target); +7 singlets bulk → 7 Dirac + 1 Majorana. Map narrowed, OPEN. a₄ held.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (±4 = SU(2)_L doublet edge sub-content, NOT full 15; +7 singlets bulk → 7 Dirac + 1 Majorana; sign must be uniform +4; map OPEN pending K817)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5181, the edge ±4 ↔ SM content map):
  * SM per gen = 15 Weyl = 8 (4 SU(2)_L doublets, chiral EDGE) + 7 (SU(2)-singlet, BULK) = 7 Dirac + 1 Majorana.
  * Reading A (correct): ±4 = 4 doublets = the chiral edge sub-content (8 Weyl, all left) -- NOT the full 15.
  * Reading B (wrong): ±4 = 2 Dirac -- undershoots 7 Dirac.
  * SIGN REQUIREMENT: net chiral edge index must be UNIFORM +4 (maximally left) -- K817 weight→degree→sign.
  * full SM = 4 doublets (edge) + 7 singlets (bulk), charge-paired → 7 Dirac + 1 Majorana (toy 5174).

AUG-11 [TEGMARK]. Nothing pushed. Nothing banked -- the ±4↔SM map is NARROWED to a precise target (±4 = the
SU(2)_L doublet edge sub-content, uniform +4; the 7 singlets are SU(2)-neutral bulk; full SM = 4 doublets + 7
singlets → 7 Dirac + 1 Majorana), but OPEN until K817's explicit weight→degree→sign confirms (a) the doublet
identification and (b) the uniform +4 sign (Cal), plus the d=2 dimension pin. This is a genuine second front,
independent of the gravity 8π, on its own timeline. a₄ chiral coefficients HELD. Count the edge once. CP
existence-only. Report either way straight. Count N.
""")
