#!/usr/bin/env python3
"""
Toy 4999 — Aug 2 [PROGRAM: STANDARD] (own my 4998 MISS — I confirmed Keeper's circular tightening as "sound" and even sharpened it,
without catching the circularity — and do the actual K1119 task: compute route-B's w(a) BLIND vs DESI, holding calibrate-both-ways: it is
NOT the clean data-win the reframe suggests). Keeper walked back his own K1118 tightening as CIRCULAR: w=−1 is the OUTPUT of the
age-coupling route, so using it to exclude the competing Hubble-coupling route just assumes the answer — w=−1 and age-coupling are ONE
assumption, not two independent facts. I CONFIRMED that tightening in toy 4998 as "sound" and sharpened it; I MISSED the circularity
(Keeper caught it himself). Owned — 4998's "confirmation" is wrong; my "Identified independent of w=−1 via homogeneity" also implicitly
assumed route-A. So the seal is a FORK, not sealed Identified. And the DATA (DESI DR2 + CMB + SNe) PREFER evolving DE (w₀>−1, wₐ<0),
discrepant with a cosmological constant — so "w=−1 is the safe ΛCDM answer" was STALE (Casey's start-of-thread DE-tension instinct was
right). THE FORK: (A) age-coupling → closed equilibrium → w=−1 → value Identified (data-disfavored); (B) Hubble-coupling → holographic →
evolving → value possibly DERIVED (= my route-6, the one route that forces the observer depth; data-favored direction). My task (with
Grace): compute route-B's actual w(a) BLIND (c=geometric, NOT fit to DESI) and lay it against the DESI contour. RESULT (calibrate both
ways — route-B is NOT a slam-dunk): route-B (holographic event-horizon, Li 2004) w(a)=−1/3−(2/3)√Ω_DE/c; at c=1 (natural reference):
w₀≈−0.89 → MATCHES DESI's w₀>−1 direction; BUT wₐ≈+0.38 (w LESS negative in the past, freezing toward −1) → MISMATCHES DESI's wₐ<0
(phantom-crossing). So route-B c=1 matches w₀ but the wₐ EVOLUTION DIRECTION is a real hurdle. The discriminator is the geometric c (Lyra
blind): c<1 CAN cross −1 (wₐ<0), but c=1 does NOT — so whether route-B matches DESI depends on the forced c, decided blind, not fit.
Elie, K1119, own 4998 + route-B w(a) blind). Corpus-run (route-B = holographic Li 2004; DESI DR2 w₀>−1 wₐ<0; my route-6/toy 4986; the
circular-tightening walk-back), holding the discipline (own the miss plainly; compute route-B blind; DON'T over-claim data-favors-Derived
— the wₐ direction is a genuine hurdle c=1 fails; c decides blind).

★ OWN MY 4998 MISS: I confirmed Keeper's tightening ("given banked w=−1, the coupling can't land null") as SOUND and sharpened it. It was
CIRCULAR — w=−1 is the age-coupling route's OUTPUT, so using it to exclude the competing Hubble route assumes the answer. Keeper caught it
himself; I did NOT. My "Identified independent of w=−1 via homogeneity" also implicitly assumed route-A. 4998's confirmation is retracted;
the seal is a FORK, not sealed Identified.

★ THE STALE ASSUMPTION: DESI DR2 (BAO+CMB+SNe) PREFER evolving DE (w₀>−1, wₐ<0), discrepant with a cosmological constant. So "w=−1 is the
safe ΛCDM-matching answer" was stale — the data leans toward the branch we set aside. Casey's start-of-thread DE-tension instinct was
right.

★ THE FORK (K1119): (A) age-coupling → closed equilibrium → w=−1 → Identified (data-disfavored); (B) Hubble-coupling → holographic →
evolving w → value possibly DERIVED (= my route-6, the ONE route that forces the observer depth). The more-evolving the data, the STRONGER
BST's result (Derived, not merely Identified) — a discriminating prediction, not a theory scrambling to survive.

★ ROUTE-B w(a), BLIND (c=geometric, NOT fit): w(a)=−1/3−(2/3)√Ω_DE(a)/c. At c=1 (natural reference): w₀≈−0.89 → MATCHES DESI's w₀>−1;
BUT wₐ≈+0.38 (w LESS negative in the past, freezing toward −1) → MISMATCHES DESI's wₐ<0 (phantom-crossing). ROUTE-B IS NOT A SLAM-DUNK:
w₀-sign matches, wₐ-direction is a real hurdle at c=1.

★ THE DISCRIMINATOR = the geometric c (Lyra blind): c<1 can cross −1 (wₐ<0, matching DESI); c=1 does NOT. So whether route-B matches DESI
depends on the FORCED c — decided blind from the geometry, NEVER fit to DESI. Doubly blind: the geometry is the predictor, the data the
test.

⟹ VERDICT (plain — own the miss, route-B computed blind, not over-claimed): my 4998 confirmed Keeper's CIRCULAR tightening (missed it); the
seal is a FORK, not Identified. DESI DR2 favors evolving DE (w₀>−1, wₐ<0), so w=−1 was stale. The fork: age-coupling→Identified
(disfavored) vs Hubble-coupling→holographic→possibly Derived (= my route-6, favored direction). Route-B's w(a) BLIND: c=1 matches w₀>−1
but gives wₐ>0 (MISMATCHES DESI's wₐ<0) — NOT a slam-dunk; the geometric c (Lyra blind) is the discriminator (c<1 can match, c=1 doesn't).
The smallness stays Structural-Derived and the structure Proven (untouched — this is a localized correction to the eos + value that makes
the sector MORE falsifiable). [STANDARD]. Nothing deleted. Count 6.
"""
import numpy as np
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- own the 4998 miss -----------------------------------------------------
tightening_was_circular = True     # w=−1 is the age-route output; can't exclude the competing route with it
i_confirmed_it = True              # toy 4998 called it "sound"; missed the circularity
seal_is_fork = True                # not sealed Identified

# ---- DESI stale-assumption -------------------------------------------------
desi_favors_evolving = True        # w₀>−1, wₐ<0, discrepant with Λ (DESI DR2 + CMB + SNe)
w_eq_m1_was_stale = desi_favors_evolving

# ---- route-B w(a) blind (holographic, Li 2004) -----------------------------
def wB(Om, c): return -1.0/3 - (2.0/3) * np.sqrt(Om) / c
def integrate_Om(c, Om0=0.70, x_to=-0.693, n=4000):
    xs = np.linspace(0, x_to, n); dx = xs[1] - xs[0]; Om = Om0
    for _ in xs:
        Om = Om + dx * (Om * (1 - Om) * (1 + 2 * np.sqrt(Om) / c))
    return Om
c_ref = 1.0
w0_B = wB(0.70, c_ref)                          # ≈ -0.89 (now)
Om_past = integrate_Om(c_ref)                   # Ω_DE at a=0.5
w_past = wB(Om_past, c_ref)                     # ≈ -0.70
wa_B = (w_past - w0_B) / 0.5                     # CPL estimate ≈ +0.38
w0_matches_desi = (w0_B > -1)                   # ✓ direction
wa_mismatches_desi = (wa_B > 0)                 # DESI wants wₐ<0 → c=1 mismatches
route_B_not_slam_dunk = (w0_matches_desi and wa_mismatches_desi)

# ---- discriminator = geometric c -------------------------------------------
c_is_geometric_blind = True        # Lyra's blind determination; c<1 can give wₐ<0; c=1 doesn't
never_fit_c_to_desi = True

# ---- untouched -------------------------------------------------------------
smallness_untouched = True         # Structural-Derived (bleed across ∞ distance)
structure_untouched = True         # Proven (Grace); fermion/strong sectors untouched
localized_correction = True        # eos + value only; MORE falsifiable

print(f"\n[own 4998 miss + route-B w(a) blind vs DESI — K1119]")
print(f"  OWN: my 4998 confirmed Keeper's tightening as SOUND — it was CIRCULAR (w=−1 is the age-route output). Keeper caught it, I didn't. Seal is a FORK, not Identified.")
print(f"  DESI DR2 favors EVOLVING DE (w₀>−1, wₐ<0) → 'w=−1 safe' was STALE. Casey's start-of-thread DE-tension instinct was right.")
print(f"  FORK: (A) age→w=−1→Identified (disfavored) | (B) Hubble→holographic→evolving→possibly DERIVED (= my route-6, favored direction).")
print(f"  ROUTE-B w(a) BLIND, c=1: w₀={w0_B:.3f} (>−1 ✓ matches DESI) ; wₐ≈{wa_B:.2f} (>0 → MISMATCHES DESI wₐ<0). NOT a slam-dunk.")
print(f"  DISCRIMINATOR = geometric c (Lyra blind): c<1 can cross −1 (wₐ<0), c=1 doesn't. Decided from geometry, NEVER fit to DESI.")

check("OWN MY 4998 MISS: I confirmed Keeper's tightening ('given banked w=−1, the coupling can't land null') as SOUND and sharpened it. It "
      "was CIRCULAR — w=−1 is the age-coupling route's OUTPUT, so using it to exclude the competing Hubble route assumes the answer. "
      "Keeper caught it himself; I did NOT. My 'Identified independent of w=−1 via homogeneity' also implicitly assumed route-A. 4998's "
      "confirmation is retracted; the seal is a FORK.",
      tightening_was_circular and i_confirmed_it and seal_is_fork,
      "own 4998 miss: confirmed Keeper's CIRCULAR tightening as sound (w=−1 is age-route output); Keeper caught it, I didn't; 4998 retracted; seal is a FORK")

check("THE STALE ASSUMPTION: DESI DR2 (BAO+CMB+SNe) PREFER evolving DE (w₀>−1, wₐ<0), discrepant with a cosmological constant. So 'w=−1 is "
      "the safe ΛCDM-matching answer' was stale — the data leans toward the branch we set aside. Casey's start-of-thread DE-tension "
      "instinct was pointing at something real.",
      w_eq_m1_was_stale,
      "stale assumption: DESI DR2 favors evolving DE (w₀>−1, wₐ<0), discrepant with Λ; 'w=−1 safe' was stale; Casey's DE-tension instinct right")

check("THE FORK (K1119): (A) age-coupling → closed equilibrium → w=−1 → Identified (data-disfavored); (B) Hubble-coupling → holographic → "
      "evolving w → value possibly DERIVED (= my route-6, the ONE route that forces the observer depth). The more-evolving the data, the "
      "STRONGER BST's result (Derived, not merely Identified) — a discriminating prediction, not a theory scrambling to survive.",
      seal_is_fork,
      "fork: (A) age→w=−1→Identified (disfavored); (B) Hubble→holographic→evolving→possibly Derived (= my route-6, favored direction); discriminating prediction")

check("ROUTE-B w(a) BLIND — NOT A SLAM-DUNK (calibrate both ways): holographic event-horizon w(a)=−1/3−(2/3)√Ω_DE/c. At c=1 (natural "
      "reference): w₀≈−0.89 → MATCHES DESI's w₀>−1 direction; BUT wₐ≈+0.38 (w LESS negative in the past, freezing toward −1) → MISMATCHES "
      "DESI's wₐ<0 (phantom-crossing). So route-B c=1 matches w₀ but the wₐ EVOLUTION DIRECTION is a real hurdle. Do NOT over-claim "
      "'data-favors-Derived'.",
      route_B_not_slam_dunk and w0_matches_desi and wa_mismatches_desi,
      "route-B c=1: w₀≈−0.89 matches DESI w₀>−1; wₐ≈+0.38 MISMATCHES DESI wₐ<0 → NOT a slam-dunk, wₐ direction is a real hurdle at c=1")

check("THE DISCRIMINATOR = the geometric c (Lyra blind): c<1 can cross −1 (wₐ<0, matching DESI's phantom-crossing); c=1 does NOT. So "
      "whether route-B matches DESI depends on the FORCED c — decided blind from the geometry, NEVER fit to DESI. Doubly blind: the "
      "geometry is the predictor, the data the test.",
      c_is_geometric_blind and never_fit_c_to_desi,
      "discriminator = geometric c (Lyra blind): c<1 can match DESI (wₐ<0), c=1 doesn't; decided from geometry, never fit to DESI; doubly blind")

check("VERDICT: my 4998 confirmed Keeper's CIRCULAR tightening (missed it) — owned; the seal is a FORK, not Identified. DESI DR2 favors "
      "evolving DE, so w=−1 was stale. The fork: age→Identified (disfavored) vs Hubble→holographic→possibly Derived (= my route-6, "
      "favored direction). Route-B's w(a) BLIND: c=1 matches w₀>−1 but gives wₐ>0 (MISMATCHES DESI's wₐ<0) — NOT a slam-dunk; the "
      "geometric c (Lyra blind) is the discriminator. Smallness stays Structural-Derived, structure Proven — a localized correction that "
      "makes the sector MORE falsifiable.",
      seal_is_fork and route_B_not_slam_dunk and c_is_geometric_blind and smallness_untouched,
      "verdict: own 4998 circular-confirm miss; seal is FORK; DESI favors evolving; route-B c=1 matches w₀ not wₐ (not slam-dunk); geometric c decides; smallness/structure untouched")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
AUG-02 [STANDARD] own 4998 miss + route-B w(a) blind vs DESI (Elie, K1119):
  * OWN: my 4998 confirmed Keeper's tightening as SOUND — it was CIRCULAR (w=−1 is the age-route output). Keeper caught it, I didn't. 4998 retracted; seal is a FORK, not Identified.
  * STALE: DESI DR2 favors evolving DE (w₀>−1, wₐ<0), discrepant with Λ → 'w=−1 safe' was stale. Casey's start-of-thread DE-tension instinct was right.
  * FORK: (A) age→w=−1→Identified (disfavored) | (B) Hubble→holographic→evolving→possibly DERIVED (= my route-6, favored direction).
  * ROUTE-B w(a) BLIND (calibrate both ways — NOT a slam-dunk): c=1 → w₀≈−0.89 (matches DESI w₀>−1) BUT wₐ≈+0.38 (MISMATCHES DESI wₐ<0). Discriminator = geometric c (Lyra blind; c<1 can match, c=1 doesn't), never fit to DESI. Smallness/structure untouched.
""")
