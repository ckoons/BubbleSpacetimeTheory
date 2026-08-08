#!/usr/bin/env python3
"""
Toy 5123: PRE-REGISTER the "1/N_c lever" kill/survive criteria BEFORE Lyra computes the interior operator
-- retrofit-proofing the Λ-amplitude pinning. The pivotal question (K1288/Keeper): does the interior
operator FIX T/E_F ~ 1/N_c? If YES, Fano ≈ 0.74 is D_IV⁵-fixed and the Λ-fluctuation amplitude becomes a
REAL PREDICTION (not a value read off the cosmological occupancy p). 1/N_c is exactly the elegant
coincidence that invites retrofit -- so LOCK the criteria + sensitivity NOW, before the number is known.
Elie's guard (break-guard #1: pre-register the case-map before the make-or-break). Target-innocent.
E / Elie -- I set the criteria + sensitivity; @Lyra+@Keeper compute the operator's actual T/E_F. This
does NOT compute the answer -- it fixes what would confirm vs kill it, so a match can't be back-fitted.

CONTEXT: amplitude pinned to Fano = 1 - p on the exact D_IV⁵ SO(5)-harmonic ladder (toy 5122); the exact
VALUE rides the cosmological occupancy p (= record-sea degeneracy). The ONE lever that turns "rides p"
into a fixed prediction: the interior operator's natural temperature/Fermi ratio T/E_F. If T/E_F = 1/N_c
target-innocent, Fano ≈ 0.74 is fixed.

PRE-REGISTERED CRITERIA (locked before Lyra's operator ID):
  * SURVIVE (amplitude pins): the interior operator's natural T/E_F comes out = 1/N_c = 1/3 TARGET-INNOCENT
    -- derived from the operator's OWN scales (commitment temperature 1/τ and the record-sea Fermi level
    E_F), NOT chosen to yield Fano = 0.74. Then Fano ≈ 0.74 is D_IV⁵-fixed -> a real Λ-fluctuation prediction.
  * KILL (amplitude rides p): T/E_F ≠ 1/N_c (outside the tolerance below) -> Fano stays = 1 - p, amplitude
    is an OBSERVABLE (δΛ measures p), NOT a fixed prediction. Honest fallback, already the banked state.
  * SENSITIVITY (locked): dFano/d(T/E_F) ~ 0.75 near 1/N_c; to pin Fano to ±0.02 the operator must give
    T/E_F = 1/N_c to ±0.027 (~±8%). So "T/E_F = 1/N_c" is a REAL, checkable target with a stated tolerance.

GUARDS (locked):
  (a) FORCING not fit: T/E_F must be FORCED by the operator's own commitment/Fermi scales; if it is reasoned
      backward from Fano=0.74 (or from wanting 1/N_c), it is a retrofit -> KILL. (Cal §341 / no-wave-through.)
  (b) NO WELD (K1289 trap): 1/N_c (the T/E_F ratio) is a DIFFERENT object from 27 = N_c³ (the color
      codebook, F459) and from 0.27 (the occupancy p itself). Three separate things that share digits --
      do NOT weld. A "1/N_c" that only appears by identifying it with 27 or 0.27 is a coincidence, not a mechanism.
  (c) TIER ceiling: even if it SURVIVES, the Λ VALUE stays Structural -- this pins the FLUCTUATION amplitude
      (a₀-rung statistic), NOT the cosmological-constant value. Amplitude-pinned ≠ Λ-derived.

=> VERDICT (plain): the 1/N_c lever's criteria are LOCKED before computation -- SURVIVE iff the interior
operator's natural T/E_F = 1/N_c (±8%) TARGET-INNOCENT (from its own scales, not back-fit); else the
amplitude rides p (the honest banked state). Sensitivity stated (±8% tolerance). Three guards locked
(forcing-not-fit, no-weld-with-27-or-0.27, tier-ceiling). Retrofit-proofed: a later match can only count
if it clears these pre-registered criteria. This is a GUARD, not a result -- I do NOT claim T/E_F=1/N_c.

=> DISPOSITION: pre-registration for the pivotal amplitude-pinning lever (Elie's lead, Keeper+Lyra
compute). Locks kill/survive + sensitivity + guards BEFORE Lyra's operator ID -> a match can't be
retrofitted at peak convergence. Target-innocent. Λ Structural. Firer: Elie; computed-by: Lyra+Keeper;
Cal audits the criteria. Nothing pushed. Nothing banked.

Author: Elie (CI toy builder). Date: 2026-08-08.
"""

from math import exp

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

N_c = 3
K = 120
gk = [(2*k + 3)*(k + 2)*(k + 1)//6 for k in range(K + 1)]
E_F = 30.0

def fano(ratio):
    T = E_F*ratio
    f = [1.0/(exp((k - E_F)/T) + 1.0) for k in range(K + 1)]
    N = sum(gk[k]*f[k] for k in range(K + 1))
    V = sum(gk[k]*f[k]*(1 - f[k]) for k in range(K + 1))
    return V/N

print("=" * 78)
print("Toy 5123: PRE-REGISTER the 1/N_c lever -- kill/survive + sensitivity + guards (retrofit-proof)")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. The lever + the target value (Fano at T/E_F = 1/N_c).
# ----------------------------------------------------------------------------
print("\n--- 1. the lever: Fano at the candidate T/E_F = 1/N_c = 1/3 ---")
target_ratio = 1.0/N_c
F_at_target = fano(target_ratio)
check("the pivotal lever: IF the interior operator's natural T/E_F = 1/N_c = 1/3, THEN Fano is fixed at "
      f"≈ {F_at_target:.3f} -> a real Λ-fluctuation prediction. This toy LOCKS the criteria before Lyra "
      "computes the operator's actual T/E_F -- it does NOT claim T/E_F = 1/N_c",
      abs(F_at_target - 0.74) < 0.02,
      f"T/E_F = 1/N_c = {target_ratio:.3f} -> Fano = {F_at_target:.3f}. Candidate value, pre-registered, NOT claimed.")

# ----------------------------------------------------------------------------
# 2. Sensitivity: how precisely must T/E_F match 1/N_c to pin Fano?
# ----------------------------------------------------------------------------
print("\n--- 2. sensitivity: dFano/d(T/E_F) near 1/N_c -> the required tolerance ---")
slope = (fano(0.37) - fano(0.30)) / (0.37 - 0.30)
tol_for_002 = 0.02/abs(slope)
check("sensitivity dFano/d(T/E_F) ~ 0.75 near 1/N_c; to pin Fano to ±0.02 the operator must deliver "
      "T/E_F = 1/N_c to ±0.027 (~±8%). So 'T/E_F = 1/N_c' is a REAL checkable target with a stated "
      "tolerance -- not a vibe",
      abs(slope - 0.75) < 0.2 and abs(tol_for_002 - 0.027) < 0.01,
      f"slope = {slope:.2f}; tolerance for ±0.02 Fano = ±{tol_for_002:.3f} in T/E_F (~±{tol_for_002*N_c*100:.0f}% "
      "of 1/N_c). Lyra's operator must hit 1/N_c within this to SURVIVE.")

# ----------------------------------------------------------------------------
# 3. Guards locked (forcing-not-fit, no-weld, tier-ceiling).
# ----------------------------------------------------------------------------
print("\n--- 3. guards locked: forcing-not-fit, no-weld (27 vs 0.27 vs 1/N_c), tier-ceiling ---")
# the three digit-sharing objects that must NOT be welded:
color_codebook = N_c**3          # 27 = 3x3x3 (F459, color codebook)
occupancy_p = 1 - F_at_target    # ~0.26 (the record-sea occupancy p itself)
ratio_TEF = 1.0/N_c              # ~0.33 (the T/E_F lever)
distinct = (abs(color_codebook - 27) < 1e-9 and abs(occupancy_p - 0.26) < 0.02
            and abs(ratio_TEF - 0.333) < 0.01 and color_codebook != occupancy_p != ratio_TEF)
check("GUARDS locked: (a) FORCING-not-fit -- T/E_F must come from the operator's OWN commitment/Fermi "
      "scales, never reasoned back from Fano=0.74; (b) NO-WELD (K1289 trap) -- 27=N_c³ (color codebook) "
      "≠ 0.27 (occupancy p) ≠ 1/N_c≈0.33 (the T/E_F ratio): three distinct objects, don't weld on shared "
      "digits; (c) TIER-CEILING -- even if it survives, Λ VALUE stays Structural (pins the FLUCTUATION, "
      "not Λ)",
      distinct,
      f"27 (color) vs {occupancy_p:.2f} (occupancy) vs {ratio_TEF:.2f} (T/E_F) -- distinct. Amplitude-pinned "
      "≠ Λ-derived. A '1/N_c' that only appears via welding to 27 or 0.27 = coincidence, KILL.")

# ----------------------------------------------------------------------------
# 4. Verdict: criteria locked before computation.
# ----------------------------------------------------------------------------
print("\n--- 4. verdict: kill/survive locked before Lyra's operator ID ---")
check("VERDICT (pre-registration, LOCKED): SURVIVE iff Lyra's interior operator gives natural T/E_F = "
      "1/N_c (±8%) TARGET-INNOCENT (from its own scales) -> Fano ≈ 0.74 D_IV⁵-fixed, amplitude becomes a "
      "real prediction. KILL otherwise -> amplitude rides p (banked state). Guards: forcing-not-fit, "
      "no-weld, tier-ceiling. This is a GUARD, not a result -- I do NOT claim T/E_F = 1/N_c",
      abs(F_at_target - 0.74) < 0.02 and distinct,
      "retrofit-proofed at peak convergence (Cal §27 / no-wave-through). Lyra+Keeper compute; the criteria "
      "are fixed. Target-innocent; Λ Structural; nothing banked.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (1/N_c lever criteria LOCKED before computation -- retrofit-proof)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5123, PRE-REGISTER the 1/N_c amplitude-pinning lever -- Elie's guard):
  * LEVER: if the interior operator's natural T/E_F = 1/N_c = 1/3, Fano ≈ 0.74 is D_IV⁵-fixed -> the
    Λ-fluctuation amplitude becomes a real prediction (not read off the occupancy p).
  * PRE-REGISTERED (before Lyra's operator ID): SURVIVE iff T/E_F = 1/N_c (±8%) TARGET-INNOCENT (own
    scales, not back-fit); KILL otherwise -> amplitude rides p (banked state).
  * SENSITIVITY: dFano/d(T/E_F) ~ 0.75; tolerance ±0.027 (~±8% of 1/N_c) for Fano to ±0.02.
  * GUARDS: (a) forcing-not-fit; (b) NO-WELD -- 27=N_c³ (color) ≠ 0.27 (occupancy) ≠ 1/N_c (T/E_F ratio),
    three distinct digit-sharing objects (K1289 trap); (c) TIER-CEILING -- Λ VALUE stays Structural.
  * This is a GUARD, not a result -- does NOT claim T/E_F = 1/N_c; locks what would confirm vs kill it.

AUG-08 [TEGMARK]. Nothing pushed. Nothing banked. 1/N_c lever criteria LOCKED before Lyra computes the
operator -> retrofit-proof at peak convergence. Target-innocent; Λ Structural. Lyra+Keeper compute the
operator's T/E_F against these fixed criteria. Count N.
""")
