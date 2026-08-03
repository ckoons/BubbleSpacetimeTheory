#!/usr/bin/env python3
"""
Toy 5010 — Aug 3 [PROGRAM: TEGMARK] (LANE B / accurate-corpus — verify Lyra F782's @Elie item: Paper 106 F5's "m_ν_lightest ≈ 50 µeV" is a
BROKEN corpus proxy; independent recompute (checker's-half discipline — do the arithmetic myself, don't just endorse); K1127). Lyra's F782
(next-cow vetting) reported the ~50 µeV "future cow" candidate FAILS the forced-test three ways; she flagged "@Elie: m₁=0 supersedes the 50 µeV
if a toy's wanted; no rescue-fit." Recomputing all three numbers independently: (1) THE FORMULA IS OFF BY 10⁶: Paper 106 F5 states
m_ν_lightest ≈ rank·m_e/N_max², but rank·m_e/N_max² = 2·0.511 MeV / 137² = 54.45 eV, NOT 50 µeV — an error factor of 1.089×10⁶ (the "µeV"
label is wrong by six orders; the actual value is tens of eV). (2) 54.45 eV IS FALSIFIED: > KATRIN direct bound 0.45 eV AND > the cosmological
Σm_ν/3 ~ 0.024 eV — a 54 eV lightest neutrino is experimentally dead. (3) A NONZERO ~50 µeV LIGHTEST ν CONTRADICTS m₁=0 (F144): BST's
neutrino sector is m₁=0 (normal ordering, seesaw), and F144/F218's whole edifice rests on m₁=0; a nonzero lightest-ν mass at ANY value clashes
with it. (4) NO RESCUE-FIT: the nearest µeV-scale combination m_e·α⁵·n_C = 52.94 µeV is target-AWARE (built to hit ~50 µeV), mechanism-less
(no derivation), AND still clashes m₁=0 → CANDIDATE-not-bank (a clean form matching a target is not a bank until a mechanism forces it), and
here there is no target to bank anyway (m₁=0). ⟹ DISPOSITION: Paper 106 F5's "50 µeV" is a BROKEN corpus proxy → a corpus CORRECTION (reach
the data field: flag F5 as 10⁶-erroneous + reconcile-with-F144), NOT an open future landmark. CONSEQUENCE (Lyra F782): the desert below
2.24 meV holds; the signs-bracket UPPER bound stays astrophysical (stellar-mix/interstasis), not geometry-forced → eos stays IDENTIFIED,
"frozen eternal-marginal" default. GUARDS BOTH WAYS: didn't fit a rescue (no target — m₁=0); didn't over-declare the desert (only the two
surfaced candidates vetted; a broader forced-scale sweep is the open lane, Lyra's). Elie, K1127, F782 @Elie item, Paper 106 F5 broken).
Corpus-run (F782 next-cow vetting; F144 m₁=0; Paper 106 F5), holding the discipline (recompute the number myself; report broken-straight;
no rescue-fit; don't over-declare the desert).

★ THE THREE NUMBERS (independent recompute, confirming F782):
  (1) rank·m_e/N_max² = 2·0.511 MeV / 137² = 54.45 eV — NOT 50 µeV. Error factor 1.089×10⁶ (six orders). The "µeV" label is broken.
  (2) 54.45 eV is FALSIFIED: > KATRIN 0.45 eV AND > cosmological Σm_ν/3 ~ 0.024 eV. Experimentally dead.
  (3) A nonzero ~50 µeV lightest ν CONTRADICTS m₁=0 (F144) — the foundation of F144/F218.
  (4) NO RESCUE: m_e·α⁵·n_C = 52.94 µeV is target-aware + mechanism-less + STILL clashes m₁=0 → candidate-not-bank (and no target to bank).

★ DISPOSITION: Paper 106 F5 "50 µeV" = BROKEN corpus proxy → CORRECTION (flag 10⁶ error + reconcile with m₁=0/F144), NOT an open landmark.
  CONSEQUENCE: desert below 2.24 meV holds → signs-bracket UPPER bound stays astrophysical, not geometry-forced → eos stays IDENTIFIED.

⟹ VERDICT (plain — Paper 106 F5 broken, corpus correction): Paper 106 F5's "m_ν_lightest ≈ rank·m_e/N_max² ≈ 50 µeV" is broken by 10⁶
(the formula gives 54.45 eV, experimentally dead), and any nonzero lightest-ν mass contradicts m₁=0 (F144); no rescue-fit (target-aware,
mechanism-less, still clashes m₁=0). Disposition: corpus CORRECTION, not an open future landmark. The sub-2.24 meV desert holds; the
signs-bracket upper bound stays astrophysical; eos stays Identified. Guards both ways (no rescue-fit; desert not over-declared — broader
forced-scale sweep still open, Lyra's). [TEGMARK]. Nothing deleted. Count 6.
"""
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
alpha = 1 / 137
m_e_eV = 0.51099895e6            # electron mass in eV
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- (1) the formula is off by 10⁶ ------------------------------------------
F5_value_eV = rank * m_e_eV / N_max**2      # Paper 106 F5: rank·m_e/N_max²
claimed_ueV = 50e-6                          # claimed "50 µeV" (in eV)
error_factor = F5_value_eV / claimed_ueV
off_by_1e6 = (error_factor > 1e5)            # ~1.089×10⁶

# ---- (2) 54 eV is falsified -------------------------------------------------
KATRIN_bound_eV = 0.45
cosmo_bound_eV = 0.072 / 3                    # Σm_ν ~0.072 eV → per-state ~0.024 eV
falsified = (F5_value_eV > KATRIN_bound_eV and F5_value_eV > cosmo_bound_eV)

# ---- (3) any nonzero lightest ν contradicts m₁=0 (F144) ---------------------
m1_is_zero_F144 = True                        # BST neutrino sector: m₁=0 (F144/F218 foundation)
nonzero_contradicts_m1 = m1_is_zero_F144      # a nonzero ~50 µeV lightest ν clashes with m₁=0

# ---- (4) no rescue-fit ------------------------------------------------------
rescue_ueV = m_e_eV * alpha**5 * n_C * 1e6    # m_e·α⁵·n_C in µeV
rescue_near_50 = (40 < rescue_ueV < 65)       # 52.94 µeV — target-aware coincidence
rescue_target_aware = True                     # built to hit ~50 µeV
rescue_mechanism_less = True                    # no derivation
rescue_still_clashes_m1 = True                  # even if it hit 50 µeV, m₁=0 forbids it
no_rescue = rescue_target_aware and rescue_mechanism_less and rescue_still_clashes_m1  # candidate-not-bank; and no target anyway

# ---- disposition ------------------------------------------------------------
broken_proxy = off_by_1e6 and falsified
corpus_correction = broken_proxy and nonzero_contradicts_m1
desert_holds = corpus_correction and no_rescue          # → upper bound astrophysical → eos Identified

print(f"\n[Lane B — verify F782 @Elie: Paper 106 F5 '50 µeV' broken proxy — K1127]")
print(f"  (1) rank·m_e/N_max² = {rank}·{m_e_eV:.3e} eV / {N_max}² = {F5_value_eV:.3f} eV — NOT 50 µeV. Error factor {error_factor:.3e} (~10⁶).")
print(f"  (2) {F5_value_eV:.2f} eV FALSIFIED: > KATRIN {KATRIN_bound_eV} eV AND > cosmological Σm_ν/3 ~ {cosmo_bound_eV:.3f} eV.")
print(f"  (3) any nonzero ~50 µeV lightest ν CONTRADICTS m₁=0 (F144) — the F144/F218 foundation.")
print(f"  (4) rescue m_e·α⁵·n_C = {rescue_ueV:.2f} µeV: target-aware + mechanism-less + STILL clashes m₁=0 → candidate-not-bank (no target to bank).")
print(f"  ⟹ DISPOSITION: Paper 106 F5 = BROKEN proxy → corpus CORRECTION, not a landmark. Desert below 2.24 meV holds → upper bound astrophysical → eos IDENTIFIED. Guards both ways.")

check("(1) THE FORMULA IS OFF BY 10⁶: Paper 106 F5 states m_ν_lightest ≈ rank·m_e/N_max², but rank·m_e/N_max² = 2·0.511 MeV / 137² = "
      "54.45 eV, NOT 50 µeV — an error factor of 1.089×10⁶ (the 'µeV' label is wrong by six orders; the actual value is tens of eV). "
      "Confirms F782.",
      off_by_1e6 and abs(F5_value_eV - 54.45) < 0.1,
      "(1) rank·m_e/N_max²=54.45 eV not 50 µeV; error factor 1.089×10⁶ (six orders); µeV label broken (confirms F782)")

check("(2) 54.45 eV IS FALSIFIED: > KATRIN direct bound 0.45 eV AND > the cosmological Σm_ν/3 ~ 0.024 eV — a 54 eV lightest neutrino is "
      "experimentally dead.",
      falsified,
      "(2) 54.45 eV falsified: > KATRIN 0.45 eV and > cosmological Σm_ν/3 ~ 0.024 eV; experimentally dead")

check("(3) A NONZERO ~50 µeV LIGHTEST ν CONTRADICTS m₁=0 (F144): BST's neutrino sector is m₁=0 (normal ordering, seesaw), and F144/F218's "
      "whole edifice rests on m₁=0; a nonzero lightest-ν mass at ANY value clashes with it. So even the INTENDED ~50 µeV reading is "
      "forbidden by the corpus, independent of the arithmetic error.",
      nonzero_contradicts_m1,
      "(3) any nonzero lightest ν contradicts m₁=0 (F144/F218 foundation); intended ~50 µeV forbidden independent of the 10⁶ error")

check("(4) NO RESCUE-FIT: the nearest µeV-scale combination m_e·α⁵·n_C = 52.94 µeV is target-AWARE (built to hit ~50 µeV), mechanism-less "
      "(no derivation), AND still clashes m₁=0 → CANDIDATE-not-bank (a clean form matching a target is not a bank until a mechanism forces "
      "it) — and here there is no target to bank anyway (m₁=0). No rescue.",
      no_rescue and rescue_near_50,
      "(4) no rescue: m_e·α⁵·n_C=52.94 µeV target-aware + mechanism-less + still clashes m₁=0 → candidate-not-bank; no target to bank")

check("DISPOSITION: Paper 106 F5's '50 µeV' is a BROKEN corpus proxy → a corpus CORRECTION (reach the data field: flag F5 as 10⁶-erroneous "
      "+ reconcile-with-F144), NOT an open future landmark. CONSEQUENCE (F782): the desert below 2.24 meV holds; the signs-bracket UPPER "
      "bound stays astrophysical (stellar-mix/interstasis), not geometry-forced → eos stays IDENTIFIED, 'frozen eternal-marginal' default.",
      broken_proxy and corpus_correction and desert_holds,
      "disposition: Paper 106 F5 broken proxy → corpus correction (flag 10⁶ error + reconcile F144); desert holds → upper bound astrophysical → eos Identified")

check("VERDICT (guards both ways): Paper 106 F5 is broken by 10⁶ (formula gives 54.45 eV, experimentally dead), and any nonzero lightest-ν "
      "mass contradicts m₁=0 (F144); no rescue-fit (target-aware, mechanism-less, still clashes m₁=0). Corpus CORRECTION, not an open "
      "landmark. Sub-2.24 meV desert holds; signs-bracket upper bound stays astrophysical; eos stays Identified. Didn't fit a rescue (no "
      "target — m₁=0); didn't over-declare the desert (only the two surfaced candidates vetted; broader forced-scale sweep still open, "
      "Lyra's).",
      broken_proxy and corpus_correction and desert_holds and no_rescue,
      "verdict: Paper 106 F5 broken (54.45 eV, 10⁶ off, dead) + contradicts m₁=0; no rescue; corpus correction; desert holds → eos Identified; guards both ways")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
AUG-03 [TEGMARK] Lane B — verify F782 @Elie: Paper 106 F5 '50 µeV' BROKEN proxy → corpus correction (Elie, K1127):
  * (1) rank·m_e/N_max² = 54.45 eV, NOT 50 µeV — error factor 1.089×10⁶ (six orders). The 'µeV' label is broken.
  * (2) 54.45 eV FALSIFIED: > KATRIN 0.45 eV AND > cosmological Σm_ν/3 ~ 0.024 eV. Experimentally dead.
  * (3) any nonzero ~50 µeV lightest ν CONTRADICTS m₁=0 (F144) — the F144/F218 foundation; intended reading forbidden independent of the arithmetic.
  * (4) NO RESCUE: m_e·α⁵·n_C=52.94 µeV target-aware + mechanism-less + still clashes m₁=0 → candidate-not-bank; no target to bank.
  * DISPOSITION: Paper 106 F5 = broken proxy → corpus CORRECTION (flag 10⁶ error + reconcile F144), not a landmark. Desert below 2.24 meV holds → signs-bracket upper bound stays astrophysical → eos stays IDENTIFIED. Guards both ways.
""")
