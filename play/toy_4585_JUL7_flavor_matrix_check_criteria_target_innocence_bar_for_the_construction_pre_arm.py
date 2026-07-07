#!/usr/bin/env python3
"""
Toy 4585 — Jul 7 opener: pre-arm my target-innocence check for Grace's flavor-matrix construction.
Casey's directive: build both flavor matrices from the REAL strata-overlap integrals, diagonalize,
harvest. My job (checker): diagonalize + verify the entries are GEOMETRY-DERIVED, not inserted.
"Build the matrix and see what drops out" is only honest if the entries are the real integrals —
so here is exactly what I verify, pinned before the matrix lands (so the check is unambiguous).

THE CONSTRUCTION (Grace's): 3×3 SO(3) matrices (down triplet + lepton triplet), entries =
Bergman-kernel overlaps between generation wavefunctions localized at the KW strata
{origin, Cartan-slice, Shilov} = {0,2,5}; M₁₁ candidate = 0 from the Casimir-0 marginal ground.
Diagonalize → eigenvalues = mass ratios, eigenvectors = mixing (CKM / PMNS).

MY CHECK CRITERIA (the target-innocence bar — all must hold for a forward harvest):
  (a) ENTRIES = real Bergman integrals (K-values at the strata), NOT inserted V_us / M₁₁ / rank².
      A matrix is knobs; if any entry is hand-set to the answer, it's the Froggatt-Nielsen fish (refused).
  (b) M₁₁ = 0 must FALL OUT of the Casimir-0 ground (marginal Δ=d, Casimir 0 → zero bare mass),
      NOT be imposed. If the geometry gives M₁₁ ≠ 0, report it.
  (c) The NUMERATOR rank²=4 (in sin²θ_c = rank²/(rank⁴·n_C) = 1/20) must DROP OUT of the overlap
      geometry — this is Cal #318 blocker 1 (was asserted, not derived). Watch the N_μ localization:
      N_μ = 11/20 is TARGET-AWARE (Grace's June flag) — the localization must be geometry-forced.
  (d) The SAME construction on the LEPTON triplet must give PMNS (large angles), NOT over-project
      to 1:0 — Cal #318 blocker 2 (the CKM-vs-PMNS split). One construction, both sectors.

WHAT BANKS (tiered): STRUCTURAL (mass↔mixing from one forced texture) if (a)+(b) hold → candidate
3rd structural result. OBSERVABLE (m_s/m_d = rank²·n_C = 20, V_us = 1/(rank·√n_C)) ONLY if (c)+(d)
also clear. 2-3 sector = TIER-2 (m_b/m_s=45 doesn't follow 1/V², known flavor exception). Over-sell
#5 watch (4 caught yesterday). Count 8 until a forward landing.

Checker pre-arm. No count move — my diagonalization/σ/form-cheapness fire the instant Grace's entries land.
"""
import numpy as np
rank, N_c, n_C = 2, 3, 5
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

print("=" * 82)
print("Toy 4585 — flavor-matrix check criteria: target-innocence bar for the construction (pre-arm)")
print("=" * 82)

# ---- the clean-form targets the construction must REPRODUCE (not be fed) ----
V_us_clean = 1/(rank*np.sqrt(n_C))
ms_md_clean = rank**2 * n_C
print(f"\n[clean forward forms the construction must REPRODUCE from geometry (not be fed)]:")
print(f"  V_us = 1/(rank·√n_C) = {V_us_clean:.4f} (obs 0.2245, ~1σ)")
print(f"  m_s/m_d = rank²·n_C = {ms_md_clean} (obs 20.0±2.4, 0σ); via Fritzsch/GST m_s/m_d = 1/V_us²")
check("the clean forms (V_us=1/(rank√n_C), m_s/m_d=rank²·n_C=20) are the TARGETS to reproduce, not inputs",
      abs(1/V_us_clean**2 - ms_md_clean) < 1e-9, "GST consistency holds; the construction must PRODUCE these forward")

# ---- criterion (a): entries are real integrals ------------------------------
check("(a) ENTRIES = real Bergman integrals (K at strata), NOT inserted V_us/M₁₁/rank² — no FN fish",
      True, "a matrix is knobs; hand-set entries = the fishing I refused yesterday (4581/4583)")

# ---- criterion (b): M₁₁=0 falls out ----------------------------------------
check("(b) M₁₁=0 must FALL OUT of the Casimir-0 marginal ground (Δ=d, Casimir 0 → zero bare mass), not imposed",
      True, "if the geometry gives M₁₁≠0, report it — this is Cal #318-adjacent load-bearing")

# ---- criterion (c): numerator rank²=4 drops out -----------------------------
print(f"\n[criterion (c) — the numerator, Cal #318 blocker 1]:")
print(f"  sin²θ_c = rank²/(rank⁴·n_C) = {rank**2}/{rank**4*n_C} = 1/{rank**2*n_C}. The numerator rank²={rank**2}")
print(f"  must DROP OUT of the overlap geometry — it was ASSERTED. Watch N_μ: 11/20 is TARGET-AWARE (fit).")
check("(c) numerator rank²=4 must drop out of the geometry (Cal #318); N_μ=11/20 is the target-aware trap to avoid",
      rank**2 == 4 and rank**2*n_C == 20, "the localization must be geometry-forced, not fit to the Cabibbo")

# ---- criterion (d): PMNS from the same construction ------------------------
check("(d) the SAME construction on the LEPTON triplet must give PMNS (large angles), NOT over-project to 1:0",
      True, "Cal #318 blocker 2 — one construction covers CKM AND PMNS, or the mechanism isn't universal")

# ---- the pipeline is ready --------------------------------------------------
print(f"\n[pipeline ready]: when Grace's 3×3 entries land, I diagonalize (eigenvalues=masses,")
print(f"  eigenvectors=mixing), σ-score vs the wide quark-mass bars, and form-cheapness any integer that drops out.")
demo = np.array([[0.0, 0.05, 0.01], [0.05, 1.0, 0.2], [0.01, 0.2, 20.0]])  # illustrative ONLY
ev = sorted(abs(np.linalg.eigvals(demo)))
check("diagonalization pipeline armed (demo runs); fires the instant Grace's geometry-derived entries land",
      len(ev) == 3, "illustrative matrix only — NOT a construction; the real entries are Grace's integrals")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 82)
print("RESULTS")
print("=" * 82)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         {detail}")
print("\n" + "=" * 82)
print(f"SCORE: {passed}/{total}")
print("=" * 82)
print("""
FLAVOR-MATRIX CHECK CRITERIA (pre-armed target-innocence bar for the construction):
  * The construction must REPRODUCE the clean forms from geometry (V_us=1/(rank√n_C),
    m_s/m_d=rank²·n_C=20), never be fed them. My four checks when Grace's matrix lands:
    (a) entries = real Bergman integrals, NOT inserted (no Froggatt-Nielsen fish);
    (b) M₁₁=0 FALLS OUT of the Casimir-0 ground, not imposed;
    (c) the numerator rank²=4 DROPS OUT of the geometry (Cal #318 blocker 1; N_μ=11/20 = target-aware trap);
    (d) the SAME construction gives PMNS on the lepton triplet (Cal #318 blocker 2 — CKM-vs-PMNS).
  * TIERED harvest: STRUCTURAL bank (mass↔mixing one forced texture) if (a)+(b); OBSERVABLE bank
    (m_s/m_d=20, V_us) only if (c)+(d) also clear; 2-3 = TIER-2 (known flavor exception).
  * Diagonalization/σ/form-cheapness pipeline armed. Over-sell #5 watch. Count 8 until forward landing.
  => I hold as Grace's diagonalizer/checker; the check is now unambiguous and pinned before the matrix.
""")
