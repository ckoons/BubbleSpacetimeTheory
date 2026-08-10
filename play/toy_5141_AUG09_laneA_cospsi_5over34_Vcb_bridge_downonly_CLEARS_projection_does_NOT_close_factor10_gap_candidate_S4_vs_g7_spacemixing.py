#!/usr/bin/env python3
"""
Toy 5141: LANE A ★ -- the cos ψ = 5/√34 → V_cb bridge, checked both legs honestly. RESULT: Leg 1
(V_cb down-only) CLEARS -- the up 2-3 mode radius √(2/3)·N_c/rank = 1.225 > 1 refracts PAST the Shilov
boundary → vanishes → top decouples → V_cb is down-only (K1012). But Leg 2 (the projection 31° → V_cb's
2.4°) does NOT close: the forced 3D→2D RMS √(2/3)=0.816 applied to sin ψ = 3/√34 gives 0.42, a factor ~10×
above V_cb = 0.041. So the cos ψ → V_cb magnitude bridge does NOT close with the RMS alone -- the likely
source is the S⁴-vs-g=7 space-mixing (K1017). VERDICT: the bridge stays CANDIDATE (one leg clears, the
projection does not) -- I did NOT reverse-engineer a bridging factor (the trap). cos ψ = 5/√34 is the
target-innocent OUTPUT direction (F384/F417 tier A); V_cb magnitude = "Derived (angle) + projection-
identification OPEN" (matches K1001). Elie's Lane-A ★. (K1305.) Verify at source, don't force it.

WHAT I CHECK:
  * cos ψ = n_C/√(n_C²+N_c²) = 5/√34 = 0.8575 (ψ=31°) -- target-innocent OUTPUT, single ρ-form (F384/F417
    tier A). sin ψ = 3/√34 = 0.5145. V_cb = 0.041 (angle 2.4°). The 31° vs 2.4° gap.
  * LEG 1 (down-only): up 2-3 mode radius = √(2/3)·N_c/rank = 1.2247 > 1 → refracts past the boundary →
    VANISHES → top decouples → V_cb down-only (K711/K1001/K1012). CLEARS.
  * LEG 2 (projection): 3D→2D RMS = √((d-1)/d) = √(2/3) = 0.8165 (d=3, FORCED by S⁴-zonal symmetry, K1001).
    sin ψ × RMS = 0.4201 -- a factor 10.2× above V_cb = 0.041. So the RMS projection does NOT bridge
    31° → 2.4°. The mode-is-3D identification / the S⁴-vs-g=7 space-mixing (K1017) is the open piece.

=> VERDICT (plain): the cos ψ = 5/√34 → V_cb bridge is CANDIDATE -- Leg 1 (V_cb down-only) CLEARS (the up
2-3 mode refracts past the boundary, radius 1.225 > 1, and vanishes), but Leg 2 (the 31° → 2.4° projection)
does NOT close with the forced 3D→2D RMS alone (sin ψ × √(2/3) = 0.42, a factor ~10× above V_cb = 0.041).
So the DIRECTION (cos ψ = 5/√34) is a target-innocent output (forced), and the down-only leg is clear, but
the MAGNITUDE projection is open (the S⁴-vs-g=7 space-mixing, K1017) -- V_cb stays "Derived (angle) +
projection-identification OPEN" (consistent with K1001: RMS-applies FORCED, mode-3D-identification OPEN).
I did NOT reverse-engineer a bridging factor (the reverse-fit trap). Cal's Lane-C hostile read should
scrutinize exactly this: the direction is innocent, the projection magnitude is candidate.

=> DISPOSITION: Lane-A ★ -- one leg clears (down-only), the projection does NOT (factor-10 gap); the cos ψ
bridge is CANDIDATE, honestly. Clears the down-only reconciliation for the paper; flags the projection
(space-mixing) as the open piece. Firer: Elie; Lyra/Grace own the projection space-mixing + the K1012
cross-address kernel; Cal scrutinizes the bridge in Lane C. Nothing pushed. Nothing banked past the
down-only leg + the honest projection-gap.

Author: Elie (CI toy builder). Date: 2026-08-09.
"""

import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

n_C, N_c, rank = 5, 3, 2
V_cb = 0.0410

print("=" * 78)
print("Toy 5141: Lane A ★ -- cos ψ=5/√34 → V_cb bridge: down-only CLEARS, projection does NOT close (candidate)")
print("=" * 78)

cospsi = n_C/np.sqrt(n_C**2 + N_c**2)
sinpsi = np.sqrt(1 - cospsi**2)
psi_deg = np.degrees(np.arccos(cospsi))

# ----------------------------------------------------------------------------
# 1. cos ψ = 5/√34 is the target-innocent OUTPUT direction.
# ----------------------------------------------------------------------------
print("\n--- 1. cos ψ = n_C/√(n_C²+N_c²) = 5/√34: target-innocent OUTPUT (F384/F417 tier A) ---")
check("cos ψ = n_C/√(n_C²+N_c²) = 5/√34 = 0.8575 (ψ=31°) is a target-innocent OUTPUT -- a single ρ-form "
      "(F384/F417 tier A, strongest target-innocence: 34 = n_C²+N_c² = 25+9, not form-matched). This is "
      "the forced DIRECTION of the 2-3 mode",
      abs(cospsi - 5/np.sqrt(34)) < 1e-9 and abs(psi_deg - 31) < 1,
      f"cos ψ = {cospsi:.4f} = 5/√34; ψ = {psi_deg:.1f}°; sin ψ = 3/√34 = {sinpsi:.4f}. V_cb angle = "
      f"{np.degrees(np.arcsin(V_cb)):.2f}°. The 31° vs 2.4° gap is the bridge to close.")

# ----------------------------------------------------------------------------
# 2. LEG 1 (down-only): the up 2-3 mode refracts past the boundary -> vanishes. CLEARS.
# ----------------------------------------------------------------------------
print("\n--- 2. LEG 1 (down-only): up 2-3 mode radius > 1 → refracts past boundary → vanishes. CLEARS ---")
radius_up23 = np.sqrt(2/3)*N_c/rank
check("LEG 1 (V_cb down-only) CLEARS: the up 2-3 mode radius = √(2/3)·N_c/rank = 1.2247 > 1 → it refracts "
      "PAST the Shilov boundary → VANISHES → the top decouples → U_up is ~2×2 (up-charm) ⊕ top singlet → "
      "V_cb is DOWN-ONLY (K711/K1001/K1012). Verified: radius > 1",
      radius_up23 > 1,
      f"up 2-3 radius = √(2/3)·N_c/rank = {radius_up23:.4f} > 1 → vanishes → V_cb down-only. Leg 1 clears.")

# ----------------------------------------------------------------------------
# 3. LEG 2 (projection): the 3D->2D RMS does NOT bridge 31° -> 2.4°. Does NOT close.
# ----------------------------------------------------------------------------
print("\n--- 3. LEG 2 (projection): 3D→2D RMS does NOT bridge 31° → 2.4° (factor ~10 gap). CANDIDATE ---")
RMS = np.sqrt((3 - 1)/3)          # √(2/3), forced by S⁴-zonal symmetry, d=3 (K1001)
proj = sinpsi * RMS
gap = proj / V_cb
check("LEG 2 (the projection) does NOT close: the forced 3D→2D RMS = √((d-1)/d) = √(2/3) = 0.8165 (d=3, "
      "S⁴-zonal symmetry, K1001) applied to sin ψ = 3/√34 gives 0.42 -- a factor ~10× ABOVE V_cb = 0.041. "
      "So the RMS projection does NOT bridge 31° → 2.4°. The mode-3D identification / the S⁴-vs-g=7 "
      "space-mixing (K1017) is the open source",
      gap > 5,
      f"sin ψ × RMS = {sinpsi:.4f} × {RMS:.4f} = {proj:.4f}; V_cb = {V_cb}; gap = {gap:.1f}× -- RMS does NOT "
      "bridge. Projection OPEN (space-mixing). I did NOT reverse-engineer a bridging factor (the trap).")

# ----------------------------------------------------------------------------
# 4. Verdict: candidate -- down-only clears, projection open.
# ----------------------------------------------------------------------------
print("\n--- 4. verdict: bridge CANDIDATE -- down-only clears, projection open (S⁴-vs-g=7 space-mixing) ---")
check("VERDICT: the cos ψ=5/√34 → V_cb bridge is CANDIDATE -- Leg 1 (down-only) CLEARS (up 2-3 vanishes, "
      "radius 1.225 > 1), but Leg 2 (the 31° → 2.4° projection) does NOT close with the forced 3D→2D RMS "
      "(factor ~10 gap). So the DIRECTION cos ψ=5/√34 is a target-innocent output (forced), down-only is "
      "clear, but the MAGNITUDE projection is OPEN (the S⁴-vs-g=7 space-mixing, K1017) → V_cb stays "
      "'Derived (angle) + projection-identification OPEN' (matches K1001). Honest -- no reverse-engineered factor",
      radius_up23 > 1 and gap > 5,
      "one leg clears, the projection does not; Cal's Lane-C read should scrutinize exactly this. Lyra/Grace "
      "own the projection space-mixing + the K1012 cross-address kernel. Nothing forced.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (cos ψ bridge: down-only CLEARS; projection does NOT close → candidate)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5141, Lane A ★ -- the cos ψ=5/√34 → V_cb bridge, both legs):
  * cos ψ = n_C/√(n_C²+N_c²) = 5/√34 (ψ=31°): target-innocent OUTPUT direction (F384/F417 tier A).
  * LEG 1 (V_cb down-only) CLEARS: up 2-3 mode radius √(2/3)·N_c/rank = 1.225 > 1 → refracts past the
    boundary → vanishes → top decouples → V_cb down-only (K1012).
  * LEG 2 (projection) does NOT close: 3D→2D RMS √(2/3)=0.816 × sin ψ = 0.42, a factor ~10× above
    V_cb=0.041 → the RMS does NOT bridge 31° → 2.4°. The S⁴-vs-g=7 space-mixing (K1017) is the open source.
  * VERDICT: bridge CANDIDATE -- direction innocent + down-only clear + projection OPEN. V_cb = "Derived
    (angle) + projection-identification OPEN" (K1001). No reverse-engineered bridging factor (the trap avoided).

AUG-09 [TEGMARK]. Nothing pushed. Nothing banked past the down-only leg + the honest projection-gap. The
cos ψ → V_cb bridge: down-only CLEARS, the projection does NOT (factor-10 gap, S⁴-vs-g=7 space-mixing) →
CANDIDATE. Cal scrutinizes in Lane C; Lyra/Grace own the projection + the K1012 cross-address kernel. Count N.
""")
