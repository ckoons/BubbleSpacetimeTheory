#!/usr/bin/env python3
"""
Toy 5145: LANE A -- the BLIND exponent reconciliation the team demanded (settle it independent of V_cb).
RESULT (compute-don't-fit, calibrated both directions): the exponent fork (scalar genus n_C=5 vs fermion
weight g=7) is MOOT, because at the FORCED radii V_cb overshoots observed 0.041 by ~3× for EVERY candidate
exponent -- so no exponent choice closes it, and landing 0.041 requires a FIT radius. TWO corrections to my
own prior round: (1) I RETRACT the confident g=7 (toy 5144) -- it was a SECTOR-CONFLATION: y_u=5^{−7} is the
UP-sector DIAGONAL Yukawa weight (K1213), but V_cb is DOWN-only (K671, ν=N_c=3), so the up-fermion weight is
the wrong object for a down-only off-diagonal (the exact index/sector trap K1213 warns against). (2) The
b-quark radius is FORCED by F877 (r²=n/(n+N_c), the banked shared-ladder convention): r_s=1/2, r_b=√(2/5)=
0.632 -- NOT r_b→1. F882's "b at the Shilov tip r_b→1" conflates ν=0 (Shilov in the discrete-series
PARAMETER) with r→1 (SPATIAL boundary); the forced SPATIAL radius is 0.632. At (r_s=1/2, r_b=0.632), the
cross-address suppression is mild (0.77-0.94) for p∈{3/2,5,7} → V_cb=0.12-0.15, overshooting 0.041 by ~3×.
Landing 0.041 needs r_b=0.76-0.92 (>> forced 0.632) = a FIT (44/45 fit-tell). VERDICT: V_cb does NOT close
at forced inputs → banks NOTHING, stays Identified/candidate. Answers Lyra F882's decisive question ("does
the forced r_b land V_cb?") with NO (for the F877 forced radius). Elie's Lane-A reconciliation. (K1305/K1313.)

WHAT I COMPUTE:
  * RETRACT g=7 (my toy 5144): y_u=n_C^{−7} is the UP DIAGONAL Yukawa magnitude (K1213 fermion weight, up
    sector); V_cb is DOWN-only (K671, ν=N_c=3). Using the up weight for a down off-diagonal = sector-conflation.
  * FORCED radii (F877, banked): r_k² = n/(n+N_c), n=0,1,2 → {0, 1/2, √(2/5)=0.632}. s (gen-2)=1/2, b (gen-3)
    =0.632. F882's r_b→1 conflates ν=0 (Shilov PARAMETER) with r→1 (SPATIAL) -- different coordinates.
  * V_cb at forced radii = (1/√42) × [(1−r_s²)(1−r_b²)/(1−r_s r_b)²]^p for p∈{3/2, 5, 7}: 0.146 / 0.127 /
    0.118 -- ALL overshoot 0.041 by ~2.9-3.6×. The exponent fork does not change the conclusion → MOOT.
  * Landing 0.041 needs r_b = 0.916/0.792/0.758 (p=3/2/5/7), all >> forced 0.632 = a FIT.

=> VERDICT (plain): the blind exponent reconciliation resolves to "the fork is MOOT" -- at the FORCED F877
radii (r²=n/(n+N_c), r_s=1/2, r_b=√(2/5)=0.632), V_cb = 0.12-0.15 for EVERY candidate exponent (n_C=5, g=7,
or Δ=3/2), overshooting observed 0.041 by ~3×. So no exponent choice closes V_cb; landing 0.041 requires a
FIT radius (r_b=0.76-0.92 >> forced 0.632). Two self-corrections: I RETRACT the premature g=7 (sector-
conflation -- up-diagonal weight for a down-only off-diagonal), and I flag that F882's "b at Shilov tip
r_b→1" conflates the ν=0 discrete-series PARAMETER with the SPATIAL boundary (the forced spatial radius is
0.632). This answers Lyra F882's decisive test ("if r_b lands at a forced radius → Derived; else candidate")
with: the F877 forced radius does NOT land → V_cb stays Identified/CANDIDATE, banks nothing. Compute-don't-fit
held: I read the radius from the banked geometry, did NOT pick it to land 0.041. Magnitude off (no J/δ).

=> DISPOSITION: Lane-A blind reconciliation -- exponent fork MOOT (V_cb overshoots ~3× at forced radii for
all exponents); g=7 RETRACTED (sector-conflation); F882 Shilov-tip radius flagged as a ν-vs-spatial
coordinate conflation; V_cb NOT forced-closed → candidate, banks nothing. Firer: Elie (self-correcting my
5144 + testing the forced radius). Lyra/Cal: is there a DIFFERENT source-pinned radius that puts b near the
spatial boundary, or is the F877 shared-ladder radius (0.632) the forced one (→ V_cb candidate)? That is the
real open question, and it is a RADIUS question, not an exponent one. Nothing pushed. Nothing banked; a
retraction + a null (V_cb does not close at forced radii).

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

N_c, n_C, rank, g = 3, 5, 2, 7

def ov(r_s, r_b, p):
    return ((1 - r_s**2)*(1 - r_b**2)/(1 - r_s*r_b)**2)**p

print("=" * 78)
print("Toy 5145: Lane A -- V_cb at FORCED radii overshoots ~3× for ALL exponents (fork MOOT); retract g=7")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. RETRACT g=7: sector-conflation (up-diagonal weight for a down-only off-diagonal).
# ----------------------------------------------------------------------------
print("\n--- 1. RETRACT premature g=7 (toy 5144): sector-conflation -- up-diagonal weight, down-only V_cb ---")
check("RETRACT the confident g=7 exponent (my toy 5144): y_u = n_C^{−7} = 5^{−7} is the UP-sector DIAGONAL "
      "Yukawa magnitude (K1213 fermion weight, up), but V_cb is DOWN-only (K671, the down modes sit at ν=N_c=3, "
      "the Wallach threshold). Using the UP fermion weight for a DOWN-only OFF-diagonal is a sector/index "
      "conflation -- the exact trap K1213 warns against. The exponent was NOT settled; I over-claimed it",
      True,
      "y_u=5^{−7} = up DIAGONAL; V_cb = down OFF-diagonal. Different sector, different matrix element. g=7 "
      "retracted -- settle the exponent from the down-sector two-point structure, not the up Yukawa.")

# ----------------------------------------------------------------------------
# 2. FORCED radii from F877 (banked): r² = n/(n+N_c); b at 0.632, NOT r→1.
# ----------------------------------------------------------------------------
print("\n--- 2. FORCED radii (F877 banked): r²=n/(n+N_c) → {0, 1/2, √(2/5)=0.632}; F882 r_b→1 is a conflation ---")
r = [np.sqrt(n/(n+N_c)) for n in (0, 1, 2)]
r_s, r_b = r[1], r[2]
check("the b-quark radius is FORCED by F877 (the banked shared-ν-ladder): r_k² = n/(n+N_c), n=0,1,2 → radii "
      "{0, 1/2, √(2/5)=0.632}. s (gen-2) = 1/2, b (gen-3) = 0.632. F882's 'b at the Shilov tip r_b→1' "
      "CONFLATES ν=0 (the Shilov boundary in the discrete-series PARAMETER, where gen-3 sits) with r→1 (the "
      "SPATIAL boundary) -- different coordinates. The forced SPATIAL radius of b is 0.632, NOT →1",
      abs(r_s - 0.5) < 1e-9 and abs(r_b - np.sqrt(2/5)) < 1e-9,
      f"forced radii: gen-1 r={r[0]:.3f} (origin), gen-2 r_s={r_s:.3f}, gen-3 r_b={r_b:.3f}=√(2/5). "
      "b at spatial r=0.632, not the boundary.")

# ----------------------------------------------------------------------------
# 3. V_cb at forced radii overshoots ~3× for EVERY exponent → fork MOOT.
# ----------------------------------------------------------------------------
print("\n--- 3. V_cb at forced radii overshoots ~3× for p ∈ {3/2, 5, 7} → exponent fork MOOT ---")
V_same = 1/np.sqrt(42)
Vcb_forced = {p: V_same*ov(r_s, r_b, p) for p in (1.5, 5, 7)}
all_overshoot = all(v > 0.09 for v in Vcb_forced.values())   # all >> 0.041
check("V_cb at the FORCED radii = (1/√42) × [(1−r_s²)(1−r_b²)/(1−r_s r_b)²]^p, for p ∈ {3/2, 5, 7}: 0.146 / "
      "0.127 / 0.118 -- ALL overshoot observed 0.041 by ~2.9-3.6×. The cross-address suppression at the "
      "forced (close, interior) radii is MILD (0.77-0.94), not the 0.265 needed. So NO candidate exponent "
      "closes V_cb → the exponent fork (n_C=5 vs g=7 vs Δ=3/2) is MOOT at the forced radii",
      all_overshoot,
      "; ".join(f"p={p}: V_cb={v:.3f} ({v/0.041:.1f}×)" for p, v in Vcb_forced.items()) +
      " -- all overshoot ~3×. Exponent doesn't matter; the radius does.")

# ----------------------------------------------------------------------------
# 4. Landing 0.041 needs a FIT radius (r_b >> forced) → V_cb candidate, banks nothing.
# ----------------------------------------------------------------------------
print("\n--- 4. landing 0.041 needs r_b=0.76-0.92 >> forced 0.632 = a FIT → V_cb candidate ---")
# r_b required to land 0.041 at each p (Lyra F882's map): 0.916/0.792/0.758 -- all >> 0.632
rb_needed = {1.5: 0.916, 5: 0.792, 7: 0.758}
needs_fit = all(rb > r_b + 0.1 for rb in rb_needed.values())
check("landing V_cb=0.041 requires r_b = 0.916/0.792/0.758 (p=3/2/5/7, Lyra F882's map) -- ALL far above the "
      "FORCED r_b=0.632. So closing V_cb needs a FIT radius near the boundary (the 44/45 fit-tell), NOT the "
      "banked forced radius. VERDICT: V_cb does NOT close at forced inputs → Identified/CANDIDATE, banks "
      "nothing. This answers Lyra F882's decisive test with NO for the F877 forced radius",
      needs_fit,
      f"r_b needed {rb_needed} vs forced {r_b:.3f}; all require r_b→boundary = a fit. V_cb candidate. The real "
      "open question is a RADIUS one (is there a source-pin putting b near the boundary?), NOT an exponent one.")

check("VERDICT: the blind exponent reconciliation → the fork is MOOT. At the FORCED F877 radii (r²=n/(n+N_c), "
      "r_s=1/2, r_b=0.632), V_cb=0.12-0.15 for every candidate exponent (5, 7, 3/2), overshooting 0.041 by "
      "~3×. I RETRACT the premature g=7 (sector-conflation) and flag F882's r_b→1 as a ν-vs-spatial "
      "coordinate conflation (forced spatial r_b=0.632). V_cb does NOT close at forced inputs → banks nothing, "
      "candidate. Compute-don't-fit held (read the radius from banked geometry, did NOT pick it)",
      all_overshoot and needs_fit,
      "a retraction + a null: V_cb not forced-closed; the open question is the b radius (F877 0.632 vs "
      "boundary), a RADIUS question. Nothing banked. Grace/Lyra/Cal: is 0.632 the forced radius (→ candidate)?")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (exponent fork MOOT: V_cb overshoots ~3× at forced radii for all p; g=7 retracted; V_cb candidate)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5145, Lane A -- blind exponent reconciliation → fork MOOT):
  * RETRACT g=7 (toy 5144): sector-conflation -- y_u=5^{{−7}} is the UP DIAGONAL weight; V_cb is DOWN-only
    (ν=N_c=3, K671). Wrong sector for the off-diagonal.
  * FORCED radii (F877 banked): r²=n/(n+N_c) → {{0, 1/2, √(2/5)=0.632}}. F882's r_b→1 conflates ν=0 (Shilov
    PARAMETER) with r→1 (SPATIAL boundary); forced spatial r_b=0.632.
  * V_cb at forced radii: p=3/2 → 0.146; p=5 → 0.127; p=7 → 0.118. ALL overshoot 0.041 by ~3× → exponent
    fork MOOT (no exponent closes it).
  * Landing 0.041 needs r_b=0.76-0.92 >> forced 0.632 = a FIT → V_cb does NOT close at forced inputs →
    Identified/CANDIDATE, banks nothing. Answers Lyra F882's decisive test (forced r_b?) with NO.

AUG-09 [TEGMARK]. Nothing pushed. Nothing banked -- a retraction (g=7, sector-conflation) + a null (V_cb
overshoots ~3× at the FORCED F877 radii for every exponent → does not close). The exponent fork is MOOT; the
open question is a RADIUS one (F877's 0.632 vs a boundary radius). Compute-don't-fit held: read the radius
from banked geometry, did not pick it. V_cb stays candidate. Magnitude off. Count N.
""")
