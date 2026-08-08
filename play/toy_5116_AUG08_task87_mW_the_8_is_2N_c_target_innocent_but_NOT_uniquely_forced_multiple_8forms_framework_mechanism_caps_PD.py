#!/usr/bin/env python3
"""
Toy 5116: TASK #87 (block-lift gate) -- is the "8" in m_W = n_C·m_p/(8α) FORCED? The 8 is 2^N_c (color-
Cartan base). Finding: 2^N_c is TARGET-INNOCENT (principled composite, matches to ~0.03%, not a fudge),
BUT it is NOT UNIQUELY forced -- at least SIX BST composites equal 8, and the mechanism that selects
2^N_c is framework-tier (K216), not a closed derivation. Per Cal's shown-not-assumed clause -> m_W's
Derived tier via THIS route is NOT established -> caps at PD/Structural-Identified until the 2^N_c
mechanism closes. Elie's independent support for Cal/Grace's task #87. (K1275.)
E / Elie -- I provide the target-innocence + uniqueness analysis; the TIER RULING is Cal/Keeper/Casey.
Same discipline that made me own "13 has FOUR Chern decompositions" on #85: a clean number with MANY
forms is identified, not uniquely forced.

CONTEXT: m_W = n_C·m_p/(8α) = n_C·m_p·N_max/2^N_c (α ≈ 1/N_max = 1/137), 0.02-0.04%. m_Z rides sin²θ_W
-> capped Structural/Identified (K1263). m_W's ONLY claim to survive-as-Derived is this INDEPENDENT route
-- but the monotonicity exception requires the route "SHOWN, not assumed" (Cal). Gate: is the "8" forced?

WHAT I COMPUTE:
  * arithmetic: the denominator that EXACTLY fits is X = n_C·m_p·N_max/m_W ≈ 7.997 ≈ 8 = 2^N_c (~0.03%).
    So 8 is target-CONSISTENT, and 2^N_c is a PRINCIPLED composite (not nearest-integer fudge). PASS target-innocence.
  * uniqueness: how many BST composites equal 8? {2^N_c, N_c+n_C, C_2+rank, g+1, rank^3, 2·rank^2, ...}
    -> at least SIX. So "8 = 2^N_c" is a CHOICE among 8-forms; the derivation must select 2^N_c by
    MECHANISM, not because 8 is the target. (Exactly the "13 has four Chern decompositions" flag on #85.)
  * mechanism status (K216 audit): the 2^N_c-into-m_W derivation is FRAMEWORK candidate (multi-week
    FORCING per Cal #189), NOT closed. So the selection of 2^N_c is IDENTIFIED, not DERIVED.

=> VERDICT (plain): the "8" is TARGET-INNOCENT (2^N_c is a principled recurring composite, matches ~0.03%,
not a fudge) -- that PASSES. But it is NOT UNIQUELY FORCED (>= 6 BST composites equal 8) and the mechanism
selecting 2^N_c is framework-tier, not closed. So per Cal's shown-not-assumed clause, m_W's Derived tier
via this route is NOT established -> m_W CAPS at PD / Structural-Identified (like m_Z) until the 2^N_c
mechanism closes. This is honest calibration: target-innocent-identification (good) != mechanism-forced
(required for Derived). Same pattern as Grace's α_s=7/20 (target-innocent form, but not mechanism-closed -> Identified).

=> DISPOSITION: support for task #87 -- I provide the target-innocence PASS + the non-uniqueness/mechanism
FLAG; the TIER RULING (cap m_W at PD, or keep Derived if the mechanism is judged closed) is Cal/Keeper/
Casey. If the 2^N_c mechanism closes (uniquely selects 2^N_c by a forced count), m_W keeps Derived; else
it caps PD. Confirmation vs observed m_W (0.03%) is unaffected -- accuracy ⊥ tier. Nothing pushed. Nothing banked.

Author: Elie (CI toy builder). Date: 2026-08-08.
"""

from fractions import Fraction as Fr

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

print("=" * 78)
print("Toy 5116: task #87 -- the '8' in m_W is 2^N_c: target-innocent but NOT uniquely forced -> caps PD")
print("=" * 78)

# BST integers + inputs
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
m_p = 938.272            # MeV (CODATA)
alpha = 1.0/N_max        # BST uses 1/N_max
m_W_obs_PDG = 80369.2    # MeV (PDG world average)
m_W_obs_CMS = 80360.2    # MeV (CMS 2024)

# ----------------------------------------------------------------------------
# 1. Arithmetic: the exact-fit denominator X ≈ 8 = 2^N_c (target-consistent, principled).
# ----------------------------------------------------------------------------
print("\n--- 1. arithmetic: exact-fit denominator X ≈ 8 = 2^N_c ---")
m_W_pred = n_C * m_p * N_max / (2**N_c)
X_exact_PDG = n_C * m_p * N_max / m_W_obs_PDG
dev_PDG = abs(m_W_pred - m_W_obs_PDG)/m_W_obs_PDG
check("m_W = n_C·m_p·N_max/2^N_c = 5·938.272·137/8 = 80,339.5 MeV; the denominator that EXACTLY fits "
      "m_W is X = n_C·m_p·N_max/m_W_obs ≈ 7.997, i.e. 8 = 2^N_c to ~0.03%. So 8 is target-CONSISTENT and "
      "2^N_c is a PRINCIPLED composite, NOT a nearest-integer fudge -> PASSES target-innocence",
      abs(X_exact_PDG - 8) < 0.02 and 2**N_c == 8,
      f"m_W_pred = {m_W_pred:.1f} MeV; X_exact(PDG) = {X_exact_PDG:.4f} ≈ 8; dev = {dev_PDG*100:.3f}% "
      f"(vs CMS: {abs(m_W_pred-m_W_obs_CMS)/m_W_obs_CMS*100:.3f}%). 2^N_c=8 is the color-Cartan base.")

# ----------------------------------------------------------------------------
# 2. Uniqueness: how many BST composites equal 8? If many, "8=2^N_c" is a CHOICE, not forced by the target.
# ----------------------------------------------------------------------------
print("\n--- 2. uniqueness: is 2^N_c the UNIQUE BST composite = 8? (the '13 has four Chern forms' test) ---")
eight_forms = {
    "2^N_c":       2**N_c,
    "N_c + n_C":   N_c + n_C,
    "C_2 + rank":  C_2 + rank,
    "g + 1":       g + 1,
    "rank^3":      rank**3,
    "2·rank^2":    2*rank**2,
}
n_eight = sum(1 for v in eight_forms.values() if v == 8)
check("at least SIX BST composites equal 8: 2^N_c, N_c+n_C, C_2+rank, g+1, rank^3, 2·rank^2. So '8 = "
      "2^N_c' is a CHOICE among 8-forms -- the derivation must SELECT 2^N_c by MECHANISM, not because 8 "
      "is the target. (Exactly the flag I raised on #85: '13 has FOUR Chern decompositions'.)",
      n_eight >= 6,
      f"8-forms found = {n_eight}: {{k:v for matching}} = " +
      ", ".join(f"{k}={v}" for k, v in eight_forms.items() if v == 8) +
      ". Multiplicity => the number alone does not privilege 2^N_c.")

# ----------------------------------------------------------------------------
# 3. Mechanism status (K216): the 2^N_c-into-m_W derivation is FRAMEWORK-tier, not closed.
# ----------------------------------------------------------------------------
print("\n--- 3. mechanism status: K216 = framework candidate (multi-week FORCING), NOT closed ---")
mechanism_closed = False   # per K216 audit: FRAMEWORK candidate, multi-week FORCING per Cal #189
check("the derivation that puts 2^N_c into m_W (Lyra L16 / K216) is at FRAMEWORK candidate tier -- a "
      "'multi-week substrate-mechanism FORCING derivation per Cal #189', NOT a closed forcing. So the "
      "SELECTION of 2^N_c (vs the other 8-forms) is IDENTIFIED, not DERIVED",
      mechanism_closed is False,
      "K216: 2^N_c tagged 'substrate-Cartan-base substrate-color' -- an IDENTIFICATION of what 8 is, not "
      "a mechanism forcing 2^N_c specifically into m_W. Not closed.")

# ----------------------------------------------------------------------------
# 4. Verdict: target-innocent PASS, but not uniquely forced -> caps m_W at PD (tier ruling = Cal/Keeper/Casey).
# ----------------------------------------------------------------------------
print("\n--- 4. verdict: target-innocent, but not mechanism-forced -> m_W caps PD (ruling deferred) ---")
target_innocent = abs(X_exact_PDG - 8) < 0.02
uniquely_forced = (n_eight == 1) and mechanism_closed
check("VERDICT: the '8' PASSES target-innocence (2^N_c principled, ~0.03% match, not a fudge) BUT is NOT "
      "uniquely forced (>=6 BST composites = 8) AND the selecting mechanism is framework-tier (not closed). "
      "Per Cal's shown-not-assumed clause -> m_W's Derived tier via this route is NOT established -> CAPS "
      "at PD / Structural-Identified (like m_Z), pending the 2^N_c mechanism. Tier ruling = Cal/Keeper/Casey",
      target_innocent and not uniquely_forced,
      "target-innocent-identification (good) != mechanism-forced (needed for Derived). Same pattern as "
      "α_s=7/20 (Grace). If the 2^N_c mechanism closes (uniquely selects 2^N_c by a forced count) -> m_W "
      "keeps Derived; else caps PD. Confirmation vs observed (0.03%) unaffected -- accuracy ⊥ tier.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (the '8'=2^N_c: target-innocent PASS, uniqueness/mechanism FLAG)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5116, task #87 -- is the '8' in m_W forced?  Elie's support for Cal/Grace):
  * The '8' = 2^N_c (color-Cartan base); m_W = n_C·m_p·N_max/2^N_c = 80,339.5 MeV (~0.03% vs PDG/CMS).
  * TARGET-INNOCENCE: the exact-fit denominator X ≈ 7.997 ≈ 8; 2^N_c is a principled recurring composite,
    NOT a nearest-integer fudge. PASSES.
  * UNIQUENESS: >= 6 BST composites equal 8 (2^N_c, N_c+n_C, C_2+rank, g+1, rank^3, 2·rank^2) -> '8=2^N_c'
    is a CHOICE among forms; the number alone does not privilege 2^N_c. (Same flag as '13 has four Chern forms'.)
  * MECHANISM: K216 = framework candidate (multi-week FORCING), NOT closed -> the selection of 2^N_c is
    IDENTIFIED, not DERIVED.
  * VERDICT: target-innocent PASS, but not uniquely mechanism-forced -> per Cal's shown-not-assumed clause,
    m_W's Derived tier via this route is NOT established -> CAPS at PD/Structural-Identified until the
    2^N_c mechanism closes. Tier ruling deferred to Cal/Keeper/Casey.

AUG-08 [TEGMARK]. Nothing pushed. Nothing banked. Task-#87 support: the '8'=2^N_c is target-innocent but
not uniquely forced (>=6 forms + framework mechanism) -> caps m_W at PD pending the mechanism. Same
discipline as the #85 four-Chern-forms self-catch. Ruling = Cal/Keeper/Casey. Count N.
""")
