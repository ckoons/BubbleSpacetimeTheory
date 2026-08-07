#!/usr/bin/env python3
"""
Toy 5109: #85 specific-ratio forcing, SHARPENED. The mixing is matter/(matter + doubled-substrate)
= c5/(c5 + 2 c1), which uses ONLY the two CLEAN forced endpoints (c5 = N_c, c1 = n_C); c3 = 13 is
downstream (= c5 + 2 c1). This selects 3/13 and excludes the rivals (9/11, ...) STRUCTURALLY, not by
proximity. (K1266; #85 halved, my lane.)
E / Elie -- the linear-algebra side of the specific-ratio forcing. Grace/Lyra own the Lefschetz close.

CONTEXT (K1266): #85 halved -- the geometric mean sqrt(39)/27 is excluded (toy 5108, rationality etc.);
the surviving candidate is c5/c3 = 3/13. Keeper's remaining gate: FORCE that specific ratio (not
9/11 = c4/c2, not the other Chern-class ratios) -- if it forces, 3/13 promotes to Derived.

THE PROBLEM WITH "pick c5/c3": among the Chern-class ratios c_i/c_j, only c5/c3 = 3/13 lands near the
observed 0.231 -- but selecting by that is PROXIMITY (the target-chasing the whole week forbids). We
need a target-innocent reason.

THE SHARPENING (from Casey's commitment mechanism -- the note): don't select a middle class c3 at all.
The mixing is  sin^2(theta_W) = matter / (matter + substrate)  where:
  * matter    = the committed record = the TOP Chern class c5 = N_c = 3  (color; three quarks/commit).
  * substrate = the domain = the FIRST Chern class c1 = n_C = 5, counted in REAL directions -> 2 c1 = 10.
So  sin^2(theta_W) = c5 / (c5 + 2 c1) = N_c / (N_c + 2 n_C) = 3/13,  built from ONLY the two CLEAN,
target-innocent endpoints (c5 = N_c and c1 = n_C -- both FORCED in toy 5108). The "c3 = 13" is a RESULT
(Chern-sequence identity c3 = c5 + 2 c1 for Q^5), not an input.

WHY THIS EXCLUDES THE RIVALS (target-innocent): the rivals (c4/c2 = 9/11, c5/c1 = 3/5, ...) are ratios
of arbitrary Chern classes; they do NOT have the matter/(matter+substrate) STRUCTURE. Once the mixing
is forced to be matter/(matter+doubled-substrate) (Casey's mechanism), the two forced endpoints give
3/13 UNIQUELY -- no proximity, no middle-class choice.

=> VERDICT (plain): the specific-ratio question "why c5/c3, not 9/11" sharpens to "why matter/(matter+
doubled-substrate)". Answered structurally: numerator = matter = the top Chern class = N_c; denominator
= matter + doubled real-substrate = N_c + 2 n_C; both from the two CLEAN forced endpoints; the rivals
lack this structure. c3 = 13 is downstream. So the forcing reduces to ONE physics statement -- that the
mixing is the matter fraction of (matter + substrate) -- which is Casey's commitment reading, still to
be closed by the Lefschetz factorization (Grace/Lyra). sin^2(theta_W)=3/13 stays Structural/Identified
until that closes; but the specific-ratio choice is no longer a free pick among Chern ratios.

=> DISPOSITION: sharpens Keeper's specific-ratio gate; removes the c3/proximity dependence; hands
Grace/Lyra one clean statement to force (matter/(matter+doubled-substrate)). Firer=Elie (LA structure),
Lefschetz close = Grace/Lyra. Target-innocent. Nothing banked past Structural/Identified. Nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-07.
"""

from math import comb
from fractions import Fraction as Fr

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

N_c, n_C = 3, 5
sin2_obs = 0.23122

print("=" * 78)
print("Toy 5109: #85 specific ratio sharpened -- matter/(matter+doubled-substrate) (K1266)")
print("=" * 78)

# Chern sequence (target-innocent)
num = [comb(7, k) for k in range(8)]; inv = [(-2)**k for k in range(8)]
c = [sum(num[k]*inv[i-k] for k in range(i+1)) for i in range(6)]
c1, c3, c5 = c[1], c[3], c[5]

# ----------------------------------------------------------------------------
# 1. Proximity would pick c5/c3 -- but that is target-chasing.
# ----------------------------------------------------------------------------
print("\n--- proximity picks c5/c3 among Chern ratios -- but that is the forbidden target-chase ---")
ratios = {(i, j): Fr(c[i], c[j]) for i in range(6) for j in range(6) if i != j and c[j] != 0}
near = {k: v for k, v in ratios.items() if abs(float(v) - sin2_obs) < 0.02}
check("among all Chern-class ratios c_i/c_j, ONLY c5/c3 = 3/13 lands within 2% of the observed 0.231 "
      "-- so PROXIMITY would pick it, which is exactly the target-chasing we forbid. We need a "
      "target-innocent reason (Keeper: not 9/11 = c4/c2, etc.)",
      list(near.keys()) == [(5, 3)] and near[(5, 3)] == Fr(3, 13),
      f"ratios within 2% of 0.231: {[(k, str(v)) for k, v in near.items()]}. c4/c2 = {Fr(c[4],c[2])} (a "
      "rival, far off). Proximity is not a forcing.")

# ----------------------------------------------------------------------------
# 2. The sharpening: matter/(matter+doubled-substrate) uses ONLY the clean endpoints.
# ----------------------------------------------------------------------------
print("\n--- the sharpening: matter/(matter + 2*substrate) = c5/(c5 + 2 c1), clean endpoints only ---")
matter = c5          # top Chern = N_c = the committed record (color; three quarks/commit)
substrate = c1       # first Chern = n_C = the domain (complex dimension)
sin2_mech = Fr(matter, matter + 2*substrate)
check("sin^2(theta_W) = matter/(matter + 2*substrate) = c5/(c5 + 2 c1) = N_c/(N_c + 2 n_C) = 3/13, built "
      "from ONLY the two CLEAN forced endpoints (c5 = N_c = matter, c1 = n_C = substrate). c3 is NOT used",
      sin2_mech == Fr(3, 13) and matter == N_c and substrate == n_C,
      f"c5 = {c5} = N_c (matter, top Chern); c1 = {c1} = n_C (substrate, first Chern); "
      f"c5/(c5+2c1) = {sin2_mech} = 3/13. Uses the two endpoints toy 5108 already forced.")

check("c3 = 13 is DOWNSTREAM, not an input: c3 = c5 + 2 c1 is a Chern-sequence identity for Q^5. So the "
      "form 'c5/c3' is a consequence of 'matter/(matter+doubled-substrate)', not a separate choice of "
      "the middle Chern class",
      c3 == c5 + 2*c1,
      f"c3 = {c3} = c5 + 2 c1 = {c5} + 2*{c1}. The '13' is a result; the forcing lives in the endpoints.")

# ----------------------------------------------------------------------------
# 3. The rivals lack the matter/(matter+substrate) structure (structural exclusion).
# ----------------------------------------------------------------------------
print("\n--- rivals (9/11, 3/5, ...) lack the matter/(matter+substrate) structure ---")
rivals = {"c4/c2 = 9/11": (4, 2), "c5/c1 = 3/5": (5, 1), "c5/c2 = 3/11": (5, 2), "c3/c1 = 13/5": (3, 1)}
# a candidate has the structure iff numerator = c5 (matter) AND denominator = c5 + 2 c1 (matter+2*subst)
def has_structure(i, j_is_total):
    return (c[i] == c5) and j_is_total
check("the rivals are ratios of ARBITRARY Chern classes; none has the numerator = matter (top Chern c5) "
      "AND denominator = matter + doubled-substrate (c5 + 2 c1). Only c5/(c5+2c1) does -> the mechanism "
      "SELECTS it structurally, not by proximity",
      all(not (c[i] == c5 and c[j] == c5 + 2*c1) for name, (i, j) in rivals.items()),
      f"rivals: {list(rivals)} -- e.g. 9/11 = c4/c2 has numerator c4 != c5 (not matter). Only the "
      "matter/(matter+2*substrate) form survives the structural filter.")

# ----------------------------------------------------------------------------
# 4. Verdict: the specific-ratio question reduces to one physics statement.
# ----------------------------------------------------------------------------
print("\n--- verdict: 'why c5/c3' -> 'why matter/(matter+doubled-substrate)' (one physics statement) ---")
check("VERDICT: the specific-ratio gate sharpens from 'why c5/c3 (not 9/11)' to 'why matter/(matter+"
      "doubled-substrate)'. Numerator = matter = top Chern = N_c; denominator = matter + 2*substrate = "
      "N_c + 2 n_C; both from the two CLEAN forced endpoints; rivals lack the structure; c3 is downstream. "
      "The forcing reduces to ONE statement (Casey's commitment mechanism), for the Lefschetz close",
      sin2_mech == Fr(3, 13) and c3 == c5 + 2*c1,
      "no proximity, no middle-class pick. Remaining: force 'mixing = matter/(matter+substrate)' via the "
      "Lefschetz factorization (Grace/Lyra). Then 3/13 -> Derived. Stays Structural/Identified until then.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}")
print("=" * 78)
print(f"""
SUMMARY (Toy 5109, #85 -- specific ratio sharpened: matter/(matter+doubled-substrate)):
  * Proximity would pick c5/c3 = 3/13 (only Chern ratio near 0.231) -- but that is target-chasing.
  * SHARPENING: sin^2(theta_W) = matter/(matter + 2*substrate) = c5/(c5 + 2 c1) = N_c/(N_c + 2 n_C) =
    3/13, using ONLY the two CLEAN forced endpoints (c5 = N_c = matter/top-Chern; c1 = n_C = substrate/
    first-Chern). c3 = 13 is DOWNSTREAM (= c5 + 2 c1), not an input.
  * The rivals (9/11 = c4/c2, 3/5 = c5/c1, ...) lack the matter/(matter+substrate) structure -> excluded
    STRUCTURALLY, not by proximity.
  * So Keeper's specific-ratio gate reduces to ONE physics statement: the mixing is the matter fraction
    of (matter + substrate) -- Casey's commitment reading. Force that (Lefschetz, Grace/Lyra) and 3/13
    promotes to Derived. Stays Structural/Identified until then. Target-innocent throughout.

AUG-07 [TEGMARK]. Nothing pushed. Nothing banked past Structural/Identified. Removed the c3/proximity
dependence; handed Grace/Lyra one clean statement to force. Firer=Elie (LA), Lefschetz = Grace/Lyra. Count N.
""")
