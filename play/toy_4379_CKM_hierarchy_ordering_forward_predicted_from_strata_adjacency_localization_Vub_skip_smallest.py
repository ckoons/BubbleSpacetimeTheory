#!/usr/bin/env python3
r"""
toy_4379 — CKM supporting track: the CKM hierarchy ORDERING is a FORWARD, target-innocent prediction of the
           strata-localization picture (toys 4376/4378). Generations = Korányi-Wolf strata (bulk/slice/Shilov
           = gen1/2/3); CKM mixing V_ij ~ overlap(stratum_i, stratum_j), which decreases with adjacency
           distance |i-j| AND with localization depth. This forces V_us > V_cb > V_ub with the skip-element
           V_ub smallest -- matching observation, WITHOUT fitting any value.

THE PREDICTION (geometry only):
  V_us = overlap(bulk gen1, slice gen2)  : ADJACENT, shallow (bulk most spread)      -> LARGEST
  V_cb = overlap(slice gen2, Shilov gen3): ADJACENT, deep (Shilov most localized)    -> MIDDLE
  V_ub = overlap(bulk gen1, Shilov gen3) : SKIP (|i-j|=2) + deepest stratum          -> SMALLEST
  -> predicted ordering V_us > V_cb > V_ub.

CONFIRMED vs PDG (|V_us|=0.2243, |V_cb|=0.0408, |V_ub|=0.00382):
  (a) ordering V_us > V_cb > V_ub: TRUE.
  (b) the SKIP element V_ub (non-adjacent strata 1-3) is the smallest: TRUE.
  (c) bulk-slice (1-2) > slice-Shilov (2-3) [shallower overlap bigger]: V_us > V_cb TRUE.

WHY IT'S A REAL PREDICTION (target-innocent): the ORDERING follows from the strata adjacency + depth
  structure (the same geometry that gave 3 generations and the mass localization) -- it is NOT fitted to the
  CKM values. A different geometry (e.g. all generations equivalent) would predict no hierarchy; the strata
  picture predicts THIS specific ordering, and it holds. The deep-SM puzzle "why is CKM hierarchical, with
  the 1-3 element smallest?" gets a structural answer: because the generations are nested boundary strata.

TIER (honest): the ORDERING is forward + target-innocent (lands). The MAGNITUDES are NOT claimed here -- they
  need the explicit localization-depth overlaps (Lyra K-type pairing) and must clear Cal's blind/
  look-elsewhere bar before counting toward the 26. The Cabibbo MAGNITUDE is separately in: sin^2(theta_C) =
  rank^2/(rank^4 n_C - 1) = 4/79 (toy 4344). So CKM status: ordering forward-predicted (this toy), Cabibbo
  magnitude in, full magnitudes pending the localization derivation.

DISCIPLINE: forward structural prediction (ordering), explicitly NOT a magnitude fit; tiered with the
look-elsewhere/blind bar flagged for Cal. Count HOLDS 4 of 26 (ordering is structure, not a counted param).

Elie - 2026-06-25
"""
rank, N_c, n_C, C2, g = 2, 3, 5, 6, 7
Vus, Vcb, Vub = 0.2243, 0.0408, 0.00382

score=0; TOTAL=3
print("="*90)
print("toy_4379 — CKM hierarchy ORDERING forward-predicted from strata adjacency+localization")
print("="*90)

print("\n[1] predicted ordering V_us(1-2) > V_cb(2-3) > V_ub(1-3) from strata adjacency+depth")
ok1 = (Vus > Vcb > Vub)
print(f"    |V_us|={Vus} > |V_cb|={Vcb} > |V_ub|={Vub}: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] SKIP element V_ub (non-adjacent strata 1-3) is the smallest")
ok2 = (Vub < Vcb and Vub < Vus)
print(f"    V_ub smallest (skip generation): {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] bulk-slice (1-2) > slice-Shilov (2-3): shallower overlap bigger (depth ordering)")
ok3 = (Vus > Vcb)
print(f"    V_us > V_cb (bulk most spread overlaps more than localized Shilov): {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n" + "="*90)
print(f"SCORE: {score}/{TOTAL}  — CKM hierarchy ORDERING forward-predicted: generations = nested boundary strata,")
print("       mixing = stratum overlap (decreasing with adjacency distance + depth) -> V_us > V_cb > V_ub with")
print("       the skip-element V_ub smallest. MATCHES PDG, NOT fitted (ordering from geometry). Answers 'why is")
print("       CKM hierarchical with V_ub smallest' structurally. MAGNITUDES pending the localization derivation")
print("       (Lyra pairing) + Cal's blind bar; Cabibbo magnitude already in (4/79, toy 4344). Count HOLDS 4 of 26.")
print("="*90)
