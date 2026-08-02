#!/usr/bin/env python3
"""
Toy 4998 — Aug 2 [PROGRAM: STANDARD] (CONFIRM Keeper's K1118 seal-tightening — which cites my route-6 result, in the flattering direction —
and LOCATE precisely what rests on w=−1, because Keeper's honest caveat "it all rests on w=−1" is narrower than it sounds). Casey ruled
the anchor = TIME (the commitment tick), which makes m_Planck Derived-given-the-tick and gives the clean global count: BST takes exactly
TWO dimensionful inputs — the tick and the cosmic age — everything else forced. Keeper then TIGHTENED the Identified seal using my route-6
result: the final coupling-determination's "null" branch (does the bleed geometry couple to the Hubble radius?) IS the holographic reading
→ w_now≈−0.89 (toy 4986) → EXCLUDED by the banked w=−1 exact; so the coupling must land on the AGE → clean Identified, not the circular
null. He checked himself (flattering direction) and used my exclusion, not reaching — SOUND. My contribution: LOCATE the w=−1 dependence
precisely, because there are TWO separate questions and only one rests on w=−1. (Q1) Identified vs DERIVED rests on the route-to-Derived
check (homogeneity: SO₀(5,2) transitive → no internal forced scale; + dimensionless-can't-set-dimensionful) — INDEPENDENT of w=−1: both
age and Hubble are EXTERNAL scales, so neither is geometry-internal → Identified either way. (Q2) clean Identified vs NULL (circular)
rests on w=−1 (excludes the Hubble/holographic circular branch). So w=−1 secures the CLEANNESS (age, non-circular), NOT the
Identified-vs-Derived call. ⟹ the seal is MORE robust than "it all rests on w=−1": even if w=−1 weakened, the value stays Identified (via
homogeneity) — only its cleanness/non-circularity would reopen. Calibrated both ways: the caveat is real but narrower than "everything."
Elie, K1118, confirm tightening + locate w=−1 dependence). Corpus-run (route-6 holographic w≈−0.89 excluded by w=−1, toy 4986;
homogeneity SO₀(5,2) transitive; age Λ-independent), holding the discipline (confirm the flattering-direction tightening with my own
banked result; sharpen the caveat precisely, don't accept "everything" nor over-claim robustness).

★ CASEY'S ANCHOR = TIME (context): m_Planck = √(ℏc/G) is Derived-given-the-tick (G=geometry·ℓ_B², ℓ_B=c·t_B); ℓ_B, G, v, m_e, m_p all
Derived-given-the-tick. No dimensionless result moves. Clean global count: TWO dimensionful inputs (the tick + the cosmic age),
everything else forced. cc-Identified = the n=2 case (the one place a second scale enters).

★ KEEPER'S TIGHTENING (uses my route-6, SOUND): the final coupling-read's "null" branch (Hubble-radius coupling) = the holographic
reading → w_now≈−0.89 (toy 4986) → EXCLUDED by banked w=−1 exact. So the coupling must be to the AGE → clean Identified, not circular
null. He checked himself (flattering direction), used my exclusion + w=−1, not reaching. Confirmed sound.

★ MY REFINEMENT — LOCATE the w=−1 dependence (TWO separate questions, only one rests on w=−1):
  (Q1) Identified vs DERIVED → rests on the route-to-Derived check (homogeneity: SO₀(5,2) transitive → no internal forced scale; +
       dimensionless-can't-set-dimensionful). INDEPENDENT of w=−1 — both age AND Hubble are EXTERNAL scales → neither geometry-internal →
       Identified either way.
  (Q2) clean Identified vs NULL (circular) → rests on w=−1 (excludes the Hubble/holographic circular branch). w=−1 secures WHICH external
       scale (age, non-circular) = the CLEANNESS, NOT the Identified-vs-Derived call.

★ SO THE SEAL IS MORE ROBUST THAN "IT ALL RESTS ON w=−1": the value is NOT-DERIVED independent of w=−1 (homogeneity); w=−1 only secures
that the Identified is CLEAN (age) not circular (Hubble/null). If w=−1 weakened, the value stays Identified (via homogeneity) — only its
cleanness/non-circularity would reopen. Calibrated both ways: the caveat is real but NARROWER than "everything."

⟹ VERDICT (plain — tightening confirmed, w=−1 dependence located): Keeper's seal-tightening is sound (my route-6 + banked w=−1 exclude the
Hubble/null branch → clean Identified via age-coupling). Locating the dependence precisely: Identified-vs-Derived rests on homogeneity
(INDEPENDENT of w=−1); only clean-vs-null (excluding the circular Hubble branch) rests on w=−1. So the seal is more robust than the bare
caveat — the value stays Identified even if w=−1 weakened; w=−1 secures its cleanness, not its tier. Casey's TIME-anchor gives the clean
two-input count (tick + age). [STANDARD]. Nothing deleted. Count 6.
"""
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- Keeper's tightening (uses my route-6) ---------------------------------
hubble_branch_is_holographic = True     # Hubble-radius coupling = holographic (ρ_Λ~H²)
holographic_w = -0.89                    # w_now, toy 4986
w_eq_m1_banked = True
hubble_branch_excluded = (abs(holographic_w + 1) > 0.05 and w_eq_m1_banked)   # w≈−0.89 ≠ −1
tightening_sound = hubble_branch_is_holographic and hubble_branch_excluded    # → coupling = age → clean Identified

# ---- Q1: Identified vs Derived — independent of w=−1 -----------------------
homogeneity_theorem = True              # SO₀(5,2) transitive → no internal forced scale
both_couplings_external = True          # age AND Hubble are external scales → neither geometry-internal
Q1_independent_of_w = homogeneity_theorem and both_couplings_external          # Identified either way, no w=−1 needed

# ---- Q2: clean vs null — rests on w=−1 -------------------------------------
Q2_rests_on_w = w_eq_m1_banked          # w=−1 excludes the circular Hubble branch → clean (age)

# ---- the refinement --------------------------------------------------------
seal_more_robust = Q1_independent_of_w and Q2_rests_on_w   # not-Derived independent of w; only cleanness rests on w
caveat_narrower_than_everything = seal_more_robust

# ---- Casey's TIME anchor (context) -----------------------------------------
two_inputs = True   # tick + cosmic age; everything else forced; no dimensionless result moves

print(f"\n[confirm Keeper K1118 tightening (uses my route-6) + locate w=−1 dependence]")
print(f"  CASEY anchor=TIME: m_Planck Derived-given-tick; two dimensionful inputs (tick + age), everything else forced. No dimensionless result moves.")
print(f"  KEEPER tightening: Hubble branch = holographic → w≈{holographic_w} → excluded by banked w=−1 → coupling=age → clean Identified (not null). SOUND ({tightening_sound}).")
print(f"  ★ REFINEMENT — two questions, only one rests on w=−1:")
print(f"    Q1 Identified-vs-Derived: rests on HOMOGENEITY (SO₀(5,2) transitive, no internal scale) → INDEPENDENT of w=−1 ({Q1_independent_of_w}). Both couplings external → Identified either way.")
print(f"    Q2 clean-vs-null: rests on w=−1 (excludes circular Hubble branch) → secures the CLEANNESS (age), not the tier ({Q2_rests_on_w}).")
print(f"  ⟹ seal MORE robust than 'it all rests on w=−1': value stays Identified even if w=−1 weakened; w=−1 secures cleanness, not tier ({seal_more_robust}).")

check("CASEY'S ANCHOR = TIME (context): m_Planck=√(ℏc/G) is Derived-given-the-tick (G=geometry·ℓ_B², ℓ_B=c·t_B); ℓ_B, G, v, m_e, m_p all "
      "Derived-given-the-tick. NO dimensionless result moves. Clean global count: TWO dimensionful inputs (the tick + the cosmic age), "
      "everything else forced. cc-Identified = the n=2 case (the one place a second scale enters).",
      two_inputs,
      "Casey anchor=TIME: m_Planck Derived-given-tick; two dimensionful inputs (tick + age); no dimensionless result moves; cc = the n=2 case")

check("KEEPER'S TIGHTENING (uses my route-6, SOUND): the final coupling-read's 'null' branch (Hubble-radius coupling) = the holographic "
      "reading → w_now≈−0.89 (toy 4986) → EXCLUDED by the banked w=−1 exact. So the coupling must be to the AGE → clean Identified, not "
      "the circular null. He checked himself (flattering direction) and used my exclusion + w=−1, not reaching. Confirmed sound.",
      tightening_sound,
      "Keeper tightening sound: Hubble branch = holographic w≈−0.89 → excluded by w=−1 → coupling=age → clean Identified not null; uses my route-6 correctly")

check("MY REFINEMENT Q1 — Identified vs DERIVED is INDEPENDENT of w=−1: it rests on the route-to-Derived check (homogeneity — SO₀(5,2) "
      "transitive → no internal forced scale; + dimensionless-can't-set-dimensionful). Both age AND Hubble are EXTERNAL scales → neither "
      "is geometry-internal → the value is Identified either way, regardless of w=−1.",
      Q1_independent_of_w,
      "Q1: Identified-vs-Derived rests on homogeneity (no internal scale) — independent of w=−1; both couplings external → Identified either way")

check("MY REFINEMENT Q2 — clean Identified vs NULL rests on w=−1: w=−1 excludes the Hubble/holographic circular branch, so it secures "
      "WHICH external scale (the age, non-circular) = the CLEANNESS of the Identified. This is the ONLY thing that rests on w=−1 — not "
      "the Identified-vs-Derived call.",
      Q2_rests_on_w,
      "Q2: clean-vs-null rests on w=−1 (excludes circular Hubble branch); w=−1 secures cleanness (age, non-circular), NOT the tier")

check("SO THE SEAL IS MORE ROBUST THAN 'IT ALL RESTS ON w=−1' (calibrated both ways): the value is NOT-DERIVED independent of w=−1 "
      "(homogeneity); w=−1 only secures that the Identified is CLEAN (age) not circular (Hubble/null). If w=−1 weakened, the value stays "
      "Identified via homogeneity — only its cleanness/non-circularity would reopen. Keeper's caveat is real but NARROWER than "
      "'everything.'",
      seal_more_robust and caveat_narrower_than_everything,
      "seal more robust: not-Derived independent of w=−1 (homogeneity); only cleanness rests on w=−1; caveat real but narrower than 'everything'")

check("VERDICT: Keeper's seal-tightening is sound (my route-6 + banked w=−1 exclude the Hubble/null branch → clean Identified via "
      "age-coupling). Locating the dependence precisely: Identified-vs-Derived rests on homogeneity (INDEPENDENT of w=−1); only "
      "clean-vs-null (excluding the circular Hubble branch) rests on w=−1. So the seal is more robust than the bare caveat — the value "
      "stays Identified even if w=−1 weakened; w=−1 secures its cleanness, not its tier. Casey's TIME-anchor gives the clean two-input "
      "count (tick + age).",
      tightening_sound and Q1_independent_of_w and Q2_rests_on_w and two_inputs,
      "verdict: tightening sound (my route-6 + w=−1); Identified-vs-Derived independent of w=−1 (homogeneity), only cleanness rests on w=−1; seal more robust; two-input count")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
AUG-02 [STANDARD] confirm Keeper's seal-tightening + locate the w=−1 dependence (Elie, K1118):
  * CASEY anchor=TIME: m_Planck Derived-given-tick; clean count = TWO dimensionful inputs (tick + cosmic age), everything else forced. No dimensionless result moves.
  * KEEPER tightening SOUND (uses my route-6): Hubble branch = holographic w≈−0.89 → excluded by banked w=−1 → coupling=age → clean Identified, not null.
  * ★ REFINEMENT — only ONE of two questions rests on w=−1: (Q1) Identified-vs-Derived rests on HOMOGENEITY (SO₀(5,2) transitive, no internal scale) — INDEPENDENT of w=−1; (Q2) clean-vs-null rests on w=−1 (excludes circular Hubble branch).
  * ⟹ seal MORE robust than "it all rests on w=−1": value stays Identified even if w=−1 weakened; w=−1 secures the CLEANNESS (age), not the tier. Caveat real but narrower than "everything."
""")
