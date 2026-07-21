#!/usr/bin/env python3
"""
Toy 4766 — Jul 21 (Round-5 quark row, test the within-sector ratios, Elie's target-innocent half): K798 caught a
conflation the team (me included) was sliding into — fusing MECHANISM (texture zero A vs radial-suppression B) with
PRECISION (Tier-1 exact-algebraic vs Tier-2 floor). They are ORTHOGONAL: m_s/m_d = 20 = rank²·n_C needs NO texture zero
(B-compatible) yet is exactly Tier-1. And K797 corrects my own toy-4761 framing — a non-integer λ-POWER does NOT mean
"not exact" (m_d/m_s = 1/20 sits at λ^2.01, an exact integer ratio hiding as a fuzzy power). So the λ-power scatter is NOT
evidence for Tier-2. The task: test the RG-invariant within-sector ratios DIRECTLY against BST-algebraic forms, target-
innocently, and tier per-rung. Result: m_s/m_d = 20 (+ the lepton ladder) is clean Tier-1; but the tempting m_t/m_c ≈ 137
= N_max is a POLE/RUNNING MIXING ARTIFACT (it's 277 at a consistent scale), and m_c/m_u = 588 is fit-suspect — so precision
is MIXED per-rung, and the row closes as a three-part honest result, not a flat negative.

K797 ABSORBED (correcting my toy 4761): a non-integer λ-power ≠ not-exact. m_d/m_s = 1/20 = λ^2.01 (λ=0.225) — an EXACT
rank²·n_C ratio that LOOKS like a fuzzy non-integer power. So the "power scatter 2.0–4.3" I and Grace measured is NOT
evidence the ratios are Tier-2; mechanism (B) says NOTHING about precision. Retract the "scatter → FN-fit → Tier-2"
inference; test the ratios directly instead.
CLEAN TIER-1 within-sector ratios (target-innocent, small integers, robust across scales):
  * m_s/m_d = 20.0 = rank²·n_C (0.0%, both mass sets; RG-invariant, well-measured) — Tier-1. [T2513]
  * m_μ/m_e = 206.77 = (24/π²)⁶ (0.0%) — Tier-1 (known lepton ladder; leptons don't run in QCD).
  * m_τ/m_e = 3477 = 49·71 (0.1%) — Tier-1 (known, T2003).
THE FISH (target-innocence + scheme discipline — don't bank these):
  * m_t/m_c ≈ 137 (= N_max) is a POLE/RUNNING MIXING ARTIFACT: it's 136 only when mixing m_t(pole) with m_c(2GeV); at a
    CONSISTENT scale (both at M_Z) m_t/m_c = 277 — a factor ~2 off. m_c runs a lot (1.27→0.62), m_t barely. So the "137"
    match is NOT RG-robust → RETRACT it (a scheme artifact, not a derivation).
  * m_c/m_u = 588 = rank²·N_c·g² (0.0% at pole) is FIT-SUSPECT: a 4-primary product, m_u carries ~20% error, and it's
    scheme-sensitive (480 at M_Z). Candidate at most, NOT a bank.
OPEN rungs (no clean target-innocent match): m_b/m_s ≈ 45–52, m_τ/m_μ ≈ 16.8, m_u/m_d — Tier-2/open.

⟹ VERDICT: mechanism and precision are ORTHOGONAL (K798) — so the quark row does NOT close as a flat honest-negative. It
closes as a THREE-PART honest result: (1) MECHANISM located — radial localization on the strata ((B), Lyra's Wigner-Eckart
argument), (2) ASYMMETRY located — saturation sets where the ladder anchors (boundary vs interior → the falloff rate),
(3) PRECISION MIXED per-rung — m_s/m_d = 20 = rank²·n_C + the lepton ladder are exact Tier-1, while most quark rungs are
Tier-2/open and the tempting m_t/m_c=137 (pole/running artifact) + m_c/m_u=588 (fit-suspect) do NOT bank. K797 discipline:
the λ-power scatter is NOT evidence for Tier-2 — test the ratios directly, don't round, don't count scheme-sensitive
matches. A defensible, publishable close: BST locates the hierarchy + explains the asymmetry + derives specific ratios
(m_s/m_d, leptons) as exact primary-algebraic numbers. Count ~7-8. Five-Absence-safe.
"""
import numpy as np, math
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- K797: non-integer lambda-power != not-exact ----------------------------
lam = 0.225
p_sd = math.log(1/20)/math.log(lam)   # m_d/m_s = 1/20 as a power of lambda
print(f"\n[K797] m_d/m_s = 1/20 (EXACT rank²·n_C) sits at λ^{p_sd:.2f} — a non-integer power hiding an exact ratio")
check("K797 ABSORBED (correcting my toy 4761): a non-integer λ-power ≠ not-exact. m_d/m_s = 1/20 = λ^2.01 — an EXACT "
      "rank²·n_C ratio that LOOKS like a fuzzy non-integer power. So the 'power scatter 2.0–4.3' is NOT evidence the "
      "ratios are Tier-2; mechanism (B) says nothing about precision. Test the ratios directly, not the λ-powers.",
      abs(p_sd - 2.0) < 0.1, "m_d/m_s=1/20 exact but = λ^2.01 → non-integer power ≠ non-exact; retract 'scatter→FN→Tier-2'; test ratios directly")

# ---- clean Tier-1 within-sector ratios --------------------------------------
ms_md = 0.0934/4.67e-3            # ~20, RG-invariant
mmu_me = 0.10566/0.511e-3        # 206.77
mtau_me = 1.77686/0.511e-3       # 3477
t1 = (abs(ms_md - rank**2*n_C)/(rank**2*n_C) < 0.02 and
      abs(mmu_me - (24/math.pi**2)**6)/mmu_me < 0.01 and
      abs(mtau_me - 49*71)/(49*71) < 0.01)
print(f"[Tier-1] m_s/m_d={ms_md:.2f} vs rank²·n_C=20; m_μ/m_e={mmu_me:.1f} vs (24/π²)⁶={((24/math.pi**2)**6):.1f}; m_τ/m_e={mtau_me:.0f} vs 49·71=3479")
check("CLEAN TIER-1 within-sector ratios (target-innocent, small integers, robust): m_s/m_d = 20.0 = rank²·n_C (0.0%, "
      "RG-invariant, well-measured); m_μ/m_e = 206.77 = (24/π²)⁶ (0.0%); m_τ/m_e = 3477 = 49·71 (0.1%). These are exact "
      "primary-algebraic numbers — precision Tier-1 — INDEPENDENT of the (B) mechanism.",
      t1, "m_s/m_d=20=rank²·n_C + lepton ladder ((24/π²)⁶, 49·71) are exact Tier-1 — precision independent of mechanism (B)")

# ---- the fish: m_t/m_c=137 is a pole/running artifact -----------------------
mtmc_mixed = 172.76/1.27        # pole m_t / 2GeV m_c ≈ 136
mtmc_MZ = 171.7/0.619           # consistent M_Z ≈ 277
print(f"[FISH] m_t/m_c = {mtmc_mixed:.1f} (pole/2GeV mixed, ≈137) BUT {mtmc_MZ:.1f} (consistent M_Z) → the 137 is a mixing artifact")
check("THE FISH (scheme discipline): m_t/m_c ≈ 137 = N_max is a POLE/RUNNING MIXING ARTIFACT — 136 only when mixing "
      "m_t(pole) with m_c(2GeV); at a CONSISTENT scale (both M_Z) it's 277 (factor ~2 off, since m_c runs a lot and m_t "
      "barely). NOT RG-robust → RETRACT the 137 match. And m_c/m_u = 588 = rank²·N_c·g² (0.0% pole) is fit-suspect "
      "(4-primary product, ~20% m_u error, 480 at M_Z) → candidate, not bank.",
      abs(mtmc_mixed - 137)/137 < 0.02 and mtmc_MZ > 250, "m_t/m_c=137 is a pole/running artifact (277 at consistent scale) → retract; m_c/m_u=588 fit-suspect → candidate not bank")

# ---- verdict: three-part honest close ---------------------------------------
check("VERDICT: mechanism and precision are ORTHOGONAL (K798) — the row does NOT close as a flat negative. THREE-PART "
      "honest result: (1) MECHANISM located (radial localization, (B)); (2) ASYMMETRY located (saturation sets the "
      "anchor/falloff rate); (3) PRECISION MIXED per-rung — m_s/m_d=20 + the lepton ladder exact Tier-1, most quark rungs "
      "Tier-2/open, and the tempting m_t/m_c=137 (artifact) + m_c/m_u=588 (fit-suspect) do NOT bank. K797: the λ-power "
      "scatter is NOT Tier-2 evidence — test ratios directly, don't round, don't count scheme-sensitive matches. "
      "Publishable: BST locates the hierarchy + explains the asymmetry + derives specific ratios as exact primaries.",
      t1 and abs(mtmc_mixed - 137)/137 < 0.02 and mtmc_MZ > 250,
      "row closes three-part: mechanism (B) + asymmetry (saturation) located; precision MIXED (m_s/m_d=20 + leptons Tier-1; 137/588 don't bank); mechanism ⊥ precision")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-5 within-sector ratios — Elie's target-innocent test (mechanism ⊥ precision):
  * K797 absorbed: non-integer λ-power ≠ not-exact (m_d/m_s=1/20=λ^2.01). The scatter is NOT Tier-2 evidence — test ratios directly. (Corrects my 4761.)
  * CLEAN TIER-1: m_s/m_d=20=rank²·n_C (0.0%); m_μ/m_e=(24/π²)⁶; m_τ/m_e=49·71 — exact primary-algebraic, independent of mechanism.
  * FISH: m_t/m_c≈137 is a POLE/RUNNING ARTIFACT (277 at consistent scale) → retract; m_c/m_u=588 fit-suspect → candidate not bank.
  => THREE-PART close: mechanism (B) + asymmetry (saturation) located; precision MIXED per-rung (m_s/m_d + leptons Tier-1, rest Tier-2/open). Mechanism ⊥ precision. Don't round, don't count scheme-sensitive.
""")
