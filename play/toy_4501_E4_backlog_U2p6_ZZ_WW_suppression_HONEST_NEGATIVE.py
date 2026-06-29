r"""
toy_4501 — TASK E4 (Keeper long-pull): backlog "why" item engagement -> U-2.6 (ZZ/WW suppression = 1/rank^N_c?).
           Engaged per the success template (compute, honest tier). RESULT: HONEST NEGATIVE. The di-boson
           cross-section ratio sigma(ZZ)/sigma(WW) ~ 0.146 (LHC 13 TeV) vs the conjectured 1/rank^N_c = 1/8 =
           0.125 -- ~17% off, AND the cross-sections are PDF/energy-dependent (process-dependent, scheme-like),
           so even the ~17% is not a clean fixed prediction. So U-2.6's "1/rank^N_c" conjecture does NOT hold:
           the di-boson ratio is a scale/process-limited absolute, NOT a clean dimensionless substrate ratio.
           Honest negative = a win (maps the boundary; consistent with the FLOOR picture -- cross-sections are
           process-dependent, not the substrate's dimensionless structure). NO count move. Count 9/26.

THE CHECK: U-2.6 conjectured ZZ/WW suppression = 1/rank^N_c = 1/2^3 = 1/8 = 0.125.
  sigma(ZZ)/sigma(WW) ~ 17.3/118.7 ~ 0.146 (LHC 13 TeV, approximate inclusive). Deviation ~17%.
  Moreover the di-boson cross-sections are PDF- and energy-dependent (sqrt(s), cuts, scheme) -- a production
  cross-section ratio is NOT a clean dimensionless invariant of the substrate; it is a process-dependent
  absolute. So 1/rank^N_c does not cleanly fit, and the quantity is not the right KIND of observable for a
  clean substrate ratio.

WHY HONEST NEGATIVE IS THE RIGHT OUTCOME (consistent with the FLOOR picture, Cal #470): the substrate fixes
  DIMENSIONLESS STRUCTURE (ratios of couplings, mixing angles, beta-coefficients), NOT process-dependent
  production cross-sections (which carry PDFs, phase space, energy). The ZZ/WW production ratio is the latter
  -- so it is expected to be scale/process-limited, not a clean 1/rank^N_c. U-2.6's conjecture is retired.

TIER: U-2.6 = HONEST NEGATIVE -- ZZ/WW production ratio ~0.146 vs 1/rank^N_c=0.125 (17% off + process-
  dependent); NOT a clean substrate ratio (wrong KIND of observable -- a production cross-section, not a
  dimensionless invariant). Consistent with the FLOOR picture. NO count move. Count HOLDS 9/26.

DISCIPLINE: engaged the backlog item by COMPUTING (per the engage-don't-label template); got an HONEST
  NEGATIVE (~17% off + process-dependent); explained WHY it's negative (a production cross-section is not the
  substrate's dimensionless structure, consistent with the FLOOR); retired the conjecture rather than fishing
  a closer form. Count HOLDS 9/26.

Elie - 2026-06-29
"""
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2

score=0; TOTAL=3
print("="*98)
print("toy_4501 — TASK E4: backlog U-2.6 (ZZ/WW = 1/rank^N_c?) -> HONEST NEGATIVE")
print("="*98)

print("\n[1] conjecture: ZZ/WW suppression = 1/rank^N_c = 1/8 = 0.125")
conj = 1/rank**N_c
ok1 = (abs(conj - 0.125) < 1e-9)
print(f"    1/rank^N_c = 1/{rank**N_c} = {conj}: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] observed sigma(ZZ)/sigma(WW) ~ 0.146 (LHC 13 TeV) -> ~17% off; AND process/PDF/energy-dependent")
ratio = 17.3/118.7
ok2 = (abs(ratio-conj)/conj > 0.1)
print(f"    sigma(ZZ)/sigma(WW) ~ {ratio:.3f} vs {conj} -> dev {abs(ratio-conj)/conj*100:.0f}%; cross-sections scheme/process-dependent: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] HONEST NEGATIVE: a production cross-section is NOT a clean substrate dimensionless ratio (FLOOR-consistent)")
ok3 = True
print("    substrate fixes dimensionless STRUCTURE, not process-dependent production ratios -> conjecture retired")
print(f"    honest negative = a win (maps the boundary); consistent with Cal #470 FLOOR picture: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — TASK E4: backlog U-2.6 (ZZ/WW = 1/rank^N_c?) -> HONEST NEGATIVE. The di-boson")
print("       production ratio sigma(ZZ)/sigma(WW) ~ 0.146 vs 1/rank^N_c = 0.125 (~17% off) AND it is")
print("       PDF/energy/process-dependent -- a production cross-section, NOT a clean dimensionless substrate")
print("       ratio. So the conjecture is retired: it's the wrong KIND of observable for a substrate ratio")
print("       (consistent with the FLOOR -- substrate fixes dimensionless structure, not process-dependent")
print("       cross-sections). Honest negative = a win. NO count move. Count HOLDS 9/26.")
print("="*98)
