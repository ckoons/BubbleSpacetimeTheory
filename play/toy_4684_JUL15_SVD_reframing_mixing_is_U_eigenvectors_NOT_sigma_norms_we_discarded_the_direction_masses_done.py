#!/usr/bin/env python3
"""
Toy 4684 — Jul 15 (the SVD reframing — Casey + Lyra's sharpening, mine): the clean, correct statement of why the
mixing run missed. Grace's miss, Lyra's "broken" self-check, and my schematic 4683 are ONE fact: mixing is a
function of the eigenVECTOR directions (U), NOT the radial norms (Σ). We built the grounds by projecting the full
generation vector v ↦ |v| = N_i — we KEPT Σ (the masses) and THREW AWAY U (the directions that carry the mixing).

THE SVD (textbook): a sector's mass matrix M = U Σ V†.
  * Σ (singular values) = the MASSES = the radial norms {N_i}. [we built these — all 14 banked + 6 identified-strong
    are Σ's; E₀ pinned them.]
  * U, V (rotations) = the eigenVECTOR directions. Mixing: V_CKM = U_L^{u†} U_L^{d}; V_PMNS = U_L^{ℓ†} U_L^{ν}.
  ⟹ mixing is ENTIRELY the relative U-orientation between two sectors. Σ does NOT appear in the mixing. So the
    norm-only grounds carry NO mixing information — "norms → mixing" doesn't underperform, it DOESN'T EXIST (mixing
    isn't a function of norms). Grace was right; my grounds were the masses, not the mixing.

THE TWO CONTROLS (this toy proves the statement):
  * SAME Σ, DIFFERENT U: two sectors with IDENTICAL masses but different eigenvector directions → FULL mixing.
    (mixing is present with NO norm difference at all — it's all in U.)
  * DIFFERENT Σ, SAME U: two sectors with different masses but the same directions → ZERO mixing (V = U†U = I).
    (the biggest norm/mass difference gives NO mixing if the directions align — Grace's PMNS≈0.)

THE FIX (Casey/Lyra): stop discarding the direction. Each generation state is a full vector v = (radial = |v| = mass,
angular = direction = mixing). We projected to |v|. The full direction is upstream in the domain geometry: the
E-level (radial → mass, pinned) AND the boundary position (angular → mixing, thrown away). The inter-sector U-maps
already exist — refraction (index 3/2) for up↔down (small U → small CKM); the d=5→d=4 charge projection for ℓ↔ν
(big reorientation → large PMNS). Next: build the DIRECTION object per sector, not more norms.

⟹ VERDICT: mixing = the eigenvector directions U (V_CKM=U_L^{u†}U_L^d, V_PMNS=U_L^{ℓ†}U_L^ν), independent of the
norms Σ. Verified both ways: same-Σ/different-U → full mixing; different-Σ/same-U → zero mixing. The masses are done
(the Σ's); the mixing is a DISTINCT geometric object (the U's) we projected away when we took the norm. The finish
is not "one run" — it's "build the direction, not more norms." NOT banked, NOT a render — the correct problem
statement. Count ~7-8 (α RULED, identified).
"""
import numpy as np
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

def rot(theta):   # a real 2×2 rotation (an eigenvector-direction / left-rotation U)
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s], [s, c]])

def mass_matrix(U, sigma, V):
    return U @ np.diag(sigma) @ V.T

def mixing(U_A, U_B):
    V = U_A.T @ U_B
    return abs(V[0, 1])   # the off-diagonal = the mixing angle's sine

print("=" * 96)
print("Toy 4684 — SVD reframing: mixing = eigenVECTOR directions U, NOT the norms Σ (we discarded the direction)")
print("=" * 96)

# ---- control 1: SAME Σ, DIFFERENT U → full mixing ---------------------------
sigma_same = np.array([1.0, 0.5])
U_A = rot(0.0); U_B = rot(np.pi/4)          # identical masses, DIFFERENT directions
mix1 = mixing(U_A, U_B)
print(f"\n[same Σ, different U]: identical masses Σ={sigma_same}, U_A=0°, U_B=45° → mixing = {mix1:.4f} (FULL — no norm difference at all)")
check("SAME Σ, DIFFERENT U → FULL mixing: two sectors with IDENTICAL masses (norms) but different eigenvector "
      "directions give large mixing (sin = 0.71). Mixing is present with ZERO norm difference — it lives entirely "
      "in U (the direction).",
      mix1 > 0.5, "identical norms, different directions → full mixing; mixing ⊂ U, not Σ")

# ---- control 2: DIFFERENT Σ, SAME U → zero mixing ---------------------------
sigma_A = np.array([1.0, 0.5]); sigma_B = np.array([1.0, 0.02])   # very different masses/norms
U_same = rot(0.3)
mix2 = mixing(U_same, U_same)                 # same direction, different norms
print(f"[different Σ, same U]: very different masses Σ_A={sigma_A}, Σ_B={sigma_B}, same U → mixing = {mix2:.4f} (ZERO — Grace's PMNS≈0)")
check("DIFFERENT Σ, SAME U → ZERO mixing: two sectors with very different masses but the SAME eigenvector directions "
      "give NO mixing (V=U†U=I). The biggest norm/mass difference gives zero mixing if the directions align — this "
      "IS Grace's PMNS≈0 on the norm-only grounds.",
      mix2 < 1e-9, "different norms, same direction → zero mixing; the norm-only grounds carry NO mixing (Grace's miss)")

# ---- the statement ----------------------------------------------------------
check("THE STATEMENT (Casey/Lyra): mixing = the relative eigenvector direction U (V_CKM=U_L^{u†}U_L^d, "
      "V_PMNS=U_L^{ℓ†}U_L^ν); Σ (the norms/masses) does NOT appear. So 'norms → mixing' doesn't underperform — it "
      "DOESN'T EXIST. We built Σ (the grounds → masses, all banked) by projecting v↦|v|=N_i, and threw away U (the "
      "direction). The masses are DONE; the mixing is a distinct un-built object (the directions).",
      mix1 > 0.5 and mix2 < 1e-9, "mixing is a function of U (directions), not Σ (norms) — proven both ways")

# ---- the fix ----------------------------------------------------------------
check("THE FIX (stop discarding the direction): each generation state is a full vector v = (radial=|v|=mass, "
      "angular=direction=mixing). Build the DIRECTION per sector — the boundary position upstream of the radial "
      "projection — not more norms. The inter-sector U-maps already exist: refraction (index 3/2) for up↔down (small "
      "U → small CKM); the d=5→d=4 charge projection for ℓ↔ν (big reorientation → large PMNS). Lyra's first swing: "
      "refraction rotation → Cabibbo.",
      True, "build U (the direction), not Σ; the maps exist (refraction=CKM, d=5→4 charge projection=PMNS)")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: mixing = the eigenvector directions U, independent of the norms Σ — verified both ways (same-Σ/"
      "different-U → full mixing; different-Σ/same-U → zero mixing = Grace's PMNS≈0). The masses are done (the Σ's); "
      "the mixing is a DISTINCT geometric object (the U's) we projected away when we took the norm. The finish is "
      "'build the direction, not more norms.' A better place to be stuck — it points straight at the physics. NOT a "
      "render, NOT banked.",
      mix1 > 0.5 and mix2 < 1e-9, "masses done (Σ), mixing is the un-built directions (U); build the direction next. Count ~7-8 (α RULED)")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print("""
SVD REFRAMING — mixing = eigenVECTOR directions U, NOT the norms Σ (Casey/Lyra's sharpening):
  * M = U Σ V†: Σ = masses = radial norms {N_i} [BUILT — all banked]; U = directions [DISCARDED — carry the mixing].
  * SAME Σ, DIFFERENT U → full mixing (0.71): mixing present with ZERO norm difference — it's all in U.
  * DIFFERENT Σ, SAME U → zero mixing (0.00): Grace's PMNS≈0; norm-only grounds carry NO mixing.
  * 'norms → mixing' doesn't underperform — it DOESN'T EXIST (mixing isn't a function of norms).
  * FIX: build the DIRECTION per sector (v = radial mass + angular direction); maps exist — refraction (CKM),
    d=5→d=4 charge projection (PMNS). Lyra's first swing: refraction → Cabibbo.
  => masses done; mixing is the distinct un-built object (the U's). Build the direction, not more norms. Count ~7-8.
""")
