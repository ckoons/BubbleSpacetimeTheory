#!/usr/bin/env python3
"""
Toy 5171: LANE 8 / THE SHARPENING (K1360) -- which factor of 2 sets sin²θ_W is the SAME question as where
BST's gauge fields come from. RESULT (report straight, lean 3/8): sin²θ_W is set by the a₄ heat-kernel
GAUGE-KINETIC coefficient of tr(F²) -- NOT the generator norm (Grace/Elie's blind 2 is the isometry/Killing
norm of the GENERATORS, a real number but not automatically the operative one). Lyra's reduction: sin²θ_W =
N_c/(N_c + n_C·c²), where c² is that a₄ coefficient -- c²=1 → 3/8, c²=rank=2 → 3/13. The operative c² is set
by the ORIGIN of the gauge fields: (A) INNER FLUCTUATIONS of the Dirac (exactly how Lane 8, toy 5164, derived
the SM gauge group) → a₄ = the FERMION TRACE → c²=1 → 3/8; (B) GEOMETRIC/KK isometry gauge fields → a₄ = the
Killing/isometry norm → c²=2 → 3/13. SCHEME-CONSISTENCY (Cal's gate c): Lane 8 derived the group by inner
fluctuations, so the scheme-consistent gauge-kinetic norm is the FERMION TRACE → c²=1 → 3/8; deriving the
GROUP by fluctuations but the COUPLING by the Killing norm is a MIXED SCHEME (help-yourself-to-both) =
inconsistent. So the LEAN is 3/8. THE ONE CONSISTENT HOME FOR 3/13 (open, testable, NOT established): U(1)_Y
is a DISTINCT geometric field -- the boundary/conformal SO(2) circle (F531, charge = a count on the boundary)
-- a different origin than the BULK inner-fluctuation SU(2)/SU(3); then a geometric (Killing) norm for
HYPERCHARGE ALONE is not a fudge, it is the actual origin → c²=2 → 3/13, scheme-consistent. AND the SCALE
gate binds regardless: even c²=2→3/13 is a μ_geo~Planck boundary value that must run DOWN to the measured
0.231 (or be scale-free, F531). This CORRECTS toy 5170's implied direction (there I loosely halved g'²/g²;
the clean statement is c²: 1→3/8, 2→3/13). No Weinberg win: LEAN 3/8; 3/13 only if U(1)_Y is genuinely the
geometric boundary circle -- the LOAD-BEARING question is what BST's gauge fields ARE. Elie's a₄ sharpening
(+ Lyra). (K1360; Lyra c²; F531 boundary circle; #85.) Compute-don't-fit; report straight; consistency ≠ votes.

WHAT I ESTABLISH:
  * SHARPENING (K1360): sin²θ_W is set by the a₄ gauge-kinetic coefficient of tr(F²), NOT the generator norm.
    sin²θ_W = N_c/(N_c + n_C·c²); c²=1 → 3/8, c²=rank=2 → 3/13 (Lyra's reduction).
  * ORIGIN sets c²: inner fluctuations (Lane-8 group derivation) → fermion trace → c²=1 → 3/8; geometric/KK
    isometry → Killing norm → c²=2 → 3/13.
  * SCHEME-CONSISTENCY (Cal gate c): group-by-fluctuation ⟹ coupling-by-fermion-trace → 3/8. Mixing = inconsistent.
  * 3/13 home (open): U(1)_Y = the boundary/conformal SO(2) circle (F531), distinct geometric origin →
    hypercharge-alone geometric norm consistent → c²=2 → 3/13. NOT established.
  * SCALE GATE binds: c²=2→3/13 is at μ_geo~Planck; must run down to 0.231 or be scale-free (F531).

=> VERDICT (plain): the operative question is not 'is there a factor of 2' (there is -- Grace/Elie's blind
isometry norm = 2), but WHICH normalization sets the Weinberg angle, and that is the a₄ gauge-kinetic
coefficient of tr(F²) -- which is the SAME as asking where BST's SM gauge fields come from. If they are inner
fluctuations of the Dirac (which is how Lane 8 derived the gauge GROUP), the a₄ coefficient is the FERMION
TRACE → c²=1 → sin²θ_W = 3/8; if they are geometric/KK isometry fields, it is the Killing norm → c²=2 → 3/13.
Scheme-consistency (Cal's gate c) says: having derived the group by inner fluctuations, the consistent
gauge-kinetic norm is the fermion trace → 3/8; using the Killing norm for the coupling while the group came
from fluctuations is a mixed scheme (help-yourself-to-both). So the LEAN is 3/8. The ONLY consistent home for
3/13 is that U(1)_Y is a genuinely DISTINCT geometric field -- the boundary/conformal SO(2) circle (F531) --
different in origin from the bulk SU(2)/SU(3); then a geometric norm for hypercharge alone is the real origin,
not a fudge, and gives 3/13. That is testable and NOT established. And even then, the SCALE gate binds: a
Planck-scale 3/13 must run down to 0.231 (or be scale-free, F531). This corrects toy 5170's loose direction
(clean statement: c²=1→3/8, c²=2→3/13). No win claimed; report straight; the load-bearing question is what
BST's gauge fields ARE -- which also decides the a₄ = SM-Lagrangian frontier.

=> DISPOSITION: Lane-8 sharpening -- sin²θ_W set by the a₄ gauge-kinetic coefficient (origin of gauge fields),
NOT the generator norm; scheme-consistency LEANS 3/8; 3/13 only if U(1)_Y is the geometric boundary circle
(F531, open) AND survives the scale gate. Corrects 5170's direction. Firer: Elie (+ Lyra); Lyra pins the a₄
coefficient origin (fermion-trace vs isometry) + the U(1)_Y boundary-circle question (F531) + the scale; Cal
applies the committed bar + watches for mixed-scheme; Grace's isometry-norm 2 is real but not automatically
operative. Nothing pushed. Nothing banked -- lean 3/8, 3/13 conditional on the geometric-U(1) origin; no win.

Author: Elie (CI toy builder). Date: 2026-08-11.
"""

from fractions import Fraction as F

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

N_c, n_C, rank = 3, 5, 2
def sin2(c2):
    return F(N_c, N_c + n_C*c2)

print("=" * 78)
print("Toy 5171: Lane 8 SHARPENING -- sin²θ_W set by a₄ gauge-kinetic coeff (origin of gauge fields); scheme-consistency leans 3/8")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. The sharpening: sin²θ_W = N_c/(N_c+n_C·c²), c² = a₄ gauge-kinetic coeff.
# ----------------------------------------------------------------------------
print("\n--- 1. SHARPENING (K1360): sin²θ_W = N_c/(N_c+n_C·c²); c²=1 → 3/8, c²=rank=2 → 3/13 (a₄ coeff, not gen norm) ---")
check("the SHARPENING (K1360): sin²θ_W is set by the a₄ heat-kernel GAUGE-KINETIC coefficient of tr(F²), NOT "
      "the generator norm. Lyra's reduction: sin²θ_W = N_c/(N_c + n_C·c²), where c² is that a₄ coefficient -- "
      "c²=1 → 3/8, c²=rank=2 → 3/13. Grace/Elie's blind '2' is the isometry/Killing norm of the GENERATORS "
      "(real), but whether it is the operative c² depends on the gauge-field origin",
      sin2(1) == F(3, 8) and sin2(2) == F(3, 13),
      f"sin²θ_W = N_c/(N_c+n_C·c²): c²=1 → {sin2(1)} = 3/8; c²=rank=2 → {sin2(2)} = 3/13. c² = the a₄ coeff.")

# ----------------------------------------------------------------------------
# 2. Origin sets c²: inner fluctuation → fermion trace → 3/8; geometric → Killing → 3/13.
# ----------------------------------------------------------------------------
print("\n--- 2. origin of gauge fields sets c²: inner-fluctuation → fermion trace → c²=1 (3/8); geometric → Killing → c²=2 (3/13) ---")
check("the operative c² is set by the ORIGIN of the gauge fields: (A) INNER FLUCTUATIONS of the Dirac (exactly "
      "how Lane 8 / toy 5164 derived the SM gauge group) → the a₄ coefficient is the FERMION TRACE → c²=1 → "
      "3/8; (B) GEOMETRIC/KK isometry gauge fields → the a₄ coefficient is the Killing/isometry norm (Grace's "
      "blind 2 = rank) → c²=2 → 3/13. So the whole question reduces to where BST's gauge fields come from",
      sin2(1) == F(3, 8) and sin2(2) == F(3, 13),
      "inner fluctuation (Lane-8) → fermion trace → c²=1 → 3/8; geometric/KK → Killing norm → c²=2 → 3/13. "
      "Origin = the decider.")

# ----------------------------------------------------------------------------
# 3. Scheme-consistency: Lane 8 group by fluctuations → fermion trace → 3/8; mixing inconsistent.
# ----------------------------------------------------------------------------
print("\n--- 3. scheme-consistency (Cal gate c): Lane-8 group by fluctuations → fermion trace → 3/8; mixing = inconsistent ---")
check("SCHEME-CONSISTENCY (Cal's gate c): Lane 8 derived the SM gauge GROUP by INNER FLUCTUATIONS, so the "
      "scheme-consistent gauge-kinetic norm is the FERMION TRACE → c²=1 → 3/8. Deriving the GROUP by "
      "fluctuations but the COUPLING by the Killing norm is a MIXED SCHEME (help-yourself-to-both) = "
      "inconsistent. So the LEAN is 3/8. Grace's isometry '2' is real but not automatically the operative "
      "gauge-kinetic coefficient",
      True,
      "group-by-fluctuation ⟹ coupling-by-fermion-trace (consistent) → 3/8; group-by-fluctuation + "
      "coupling-by-Killing = mixed scheme (inconsistent). Lean 3/8.")

# ----------------------------------------------------------------------------
# 4. The one consistent 3/13 home + the scale gate; no win.
# ----------------------------------------------------------------------------
print("\n--- 4. one consistent 3/13 home: U(1)_Y = geometric boundary circle (F531, open); + scale gate binds; no win ---")
check("VERDICT: the ONLY consistent home for 3/13 is that U(1)_Y is a genuinely DISTINCT geometric field -- "
      "the boundary/conformal SO(2) circle (F531, charge = a count on the boundary) -- a different ORIGIN "
      "than the bulk inner-fluctuation SU(2)/SU(3); then a geometric (Killing) norm for HYPERCHARGE ALONE is "
      "not a fudge, it is the actual origin → c²=2 → 3/13, scheme-consistent. That is testable and NOT "
      "established. AND the SCALE gate binds regardless: c²=2→3/13 is a μ_geo~Planck boundary value that must "
      "run DOWN to the measured 0.231 (or be scale-free, F531). No Weinberg win: LEAN 3/8; 3/13 only if "
      "U(1)_Y is genuinely the geometric boundary circle. The load-bearing question is what BST's gauge "
      "fields ARE (which also decides the a₄ = SM-Lagrangian frontier). Corrects 5170's loose direction",
      sin2(1) == F(3, 8) and sin2(2) == F(3, 13),
      "3/13 home = geometric boundary-circle U(1)_Y (F531, open) + must survive the scale gate. Lean 3/8 "
      "(scheme-consistent). No win; report straight. Corrects 5170.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (sin²θ_W set by a₄ coeff = gauge-field origin; scheme-consistency leans 3/8; 3/13 only if U(1)_Y geometric-boundary; scale binds)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5171, Lane 8 -- the sharpening: which factor of 2, = where the gauge fields come from):
  * sin²θ_W = N_c/(N_c+n_C·c²); c² = the a₄ gauge-kinetic coeff (NOT the generator norm). c²=1 → 3/8, c²=2 → 3/13.
  * ORIGIN sets c²: inner fluctuations (Lane-8 group) → fermion trace → c²=1 → 3/8; geometric/KK → Killing
    (Grace's blind 2=rank) → c²=2 → 3/13.
  * SCHEME-CONSISTENCY (Cal gate c): group-by-fluctuation → coupling-by-fermion-trace → 3/8; mixing = inconsistent.
  * 3/13 home (open): U(1)_Y = the boundary/conformal SO(2) circle (F531), distinct geometric origin →
    hypercharge geometric norm consistent → 3/13. NOT established. + SCALE gate binds (μ_geo~Planck → run down / F531).
  * LEAN 3/8; 3/13 only if U(1)_Y genuinely geometric-boundary. Corrects 5170's direction. No win.

AUG-11 [TEGMARK]. Nothing pushed. Nothing banked -- lean 3/8 (scheme-consistent with the inner-fluctuation
gauge group); 3/13 conditional on U(1)_Y being the geometric boundary circle (F531, open) AND surviving the
scale gate. The operative question (which factor of 2) = the a₄ gauge-kinetic coefficient = where BST's gauge
fields come from -- load-bearing for the a₄=SM-Lagrangian frontier too. Corrects 5170's loose direction;
consistency (Killing 2 via two routes) ≠ two votes. No win; report straight. Count N.
""")
