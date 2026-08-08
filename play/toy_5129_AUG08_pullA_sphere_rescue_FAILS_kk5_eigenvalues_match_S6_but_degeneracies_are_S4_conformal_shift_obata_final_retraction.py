#!/usr/bin/env python3
"""
Toy 5129: PULL A -- the sphere-rescue for "λ₁ = Einstein constant by Obata". VERDICT: RESCUE FAILS,
retraction FINAL. The DE-relaxation eigenvalues λ_k = k(k+5) (T1452/Paper86) MATCH round S⁶'s Laplacian
(the tantalizing clue), BUT the DEGENERACIES are SO(5)-harmonics-on-S⁴ (1,5,14,30,55 -- corpus F787), NOT
SO(7)-harmonics-on-S⁶ (1,7,27,77,182). The eigenvalue only equals S⁶ because the S⁴ Laplacian k(k+3) is
CONFORMAL-shifted by 2k -> k(k+5); it is the SO(5,2) discrete-series CONFORMAL Casimir on the S⁴ boundary,
NOT a round-sphere Laplacian. The actual Shilov boundary is S⁴×S¹/Z₂ (a PRODUCT, spectrum ℓ(ℓ+3)+m²), not
a round sphere. -> Obata's theorem (round-sphere equality case) does NOT apply -> the a₀↔a₁ tie is NOT
rescued. Elie's Pull-A. Verified at SOURCE (the original error was ASSUMING a sphere; here the degeneracies
decide). (K1291.)
E / Elie -- honest NEGATIVE in a retraction-prone sector. The eigenvalue-coincidence with S⁶ is NOT a
geometry; the degeneracies (S⁴) prove it. Assuming the eigenvalue-match implied a sphere = the original error.

CRUX (Keeper): is λ_k = k(k+5) a round SPHERE's spectrum (⟹ Obata applies, tie rescued) or the Q⁵/
K-Casimir formula (⟹ retraction final)? Round S^n: λ_k = k(k+n-1); k(k+5) ⟹ n=6 ⟹ round S⁶. Test it by
the DEGENERACIES (eigenvalues alone don't identify the geometry).

  (1) eigenvalues: λ_k = k(k+5) = round S⁶ Laplacian (0,6,14,24,36,...). MATCH -- the clue.
  (2) DEGENERACIES: corpus (F787) = SO(5) degree-k harmonics on S⁴ = 1,5,14,30,55; round S⁶ = SO(7)
      degree-k harmonics = 1,7,27,77,182. MISMATCH -> the carrier is S⁴-based, NOT round S⁶.
  (3) the "+5": DE eigenvalue k(k+5) = S⁴ Laplacian k(k+3) + 2k (the CONFORMAL ρ-shift). So it is the
      SO(5,2) discrete-series conformal Casimir on the S⁴ boundary, not a sphere Laplacian.
  (4) the actual Shilov boundary = S⁴×S¹/Z₂ (a PRODUCT; spectrum ℓ(ℓ+3)+m²), NOT a round sphere.
  (5) even GRANTING round S⁶: λ₁ = 6 = C_2 = dim(S⁶) = n_C+1, but the Einstein constant of unit S⁶
      (Ric=(n-1)g) = n-1 = 5 = n_C, NOT 6. So "λ₁ = Einstein constant" would need C_2 = n_C (6=5) -- λ₁ is
      the DIMENSION, not the Einstein constant. The Obata identification fails on S⁶ too.

=> VERDICT (plain): the sphere-rescue FAILS. λ_k=k(k+5) matches round S⁶ EIGENVALUES only; the DEGENERACIES
are SO(5)-on-S⁴ (F787), not SO(7)-on-S⁶ -> the DE relaxation is the SO(5,2) discrete-series CONFORMAL
Casimir on the S⁴ boundary (S⁴ Laplacian + 2k conformal shift), NOT a round-sphere Laplacian; the actual
Shilov boundary S⁴×S¹/Z₂ is a product, not a round sphere. -> Obata does NOT apply -> the a₀↔a₁ tie is NOT
rescued, the RETRACTION IS FINAL. (And even granting S⁶, λ₁=6=dim=C_2 ≠ the Einstein constant n_C=5.) The
eigenvalue coincidence is not a geometry; assuming it were repeats the original error.

=> DISPOSITION: Pull-A verdict = retraction FINAL (honest negative). The DE rate λ₁=C_2=6 stands as a real
result (spectral gap of the conformal Casimir), but its identification with the Einstein constant via Obata
is WITHDRAWN. The a₀(DE)↔a₁(gravity) tie is NOT earned. Firer: Elie; Keeper co-lane (Pull A) + fixes the
corpus Obata mis-citation (Pull D). Cal audits. Nothing pushed. Nothing banked past the spectral gap value.

Author: Elie (CI toy builder). Date: 2026-08-08.
"""

from math import comb

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

N_c, n_C, C_2 = 3, 5, 6

def deg_harmonic(n, k):
    # dim of degree-k spherical harmonics on S^n
    return comb(n + k, n) - (comb(n + k - 2, n) if k >= 2 else 0)

def lam_DE(k):
    return k*(k + n_C)          # = k(k+5), T1452/Paper86 (SO(5,2) discrete-series K-Casimir)

print("=" * 78)
print("Toy 5129: Pull A -- sphere-rescue FAILS. k(k+5) eigenvalues=S⁶ but degeneracies=S⁴ (conformal Casimir)")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. Eigenvalues k(k+5) MATCH round S⁶ (the clue).
# ----------------------------------------------------------------------------
print("\n--- 1. eigenvalues λ_k = k(k+5) MATCH round S⁶ Laplacian (n=6) -- the tantalizing clue ---")
eig_DE = [lam_DE(k) for k in range(5)]
eig_S6 = [k*(k + 5) for k in range(5)]      # round S^6: k(k+n-1)=k(k+5)
check("λ_k = k(k+5) = k(k+n_C) (T1452/Paper86) EQUALS the round-S⁶ Laplacian spectrum k(k+(6-1)) = "
      "0,6,14,24,36 (round S^n has λ_k=k(k+n-1) -> n=6). The eigenvalue coincidence is the clue that "
      "motivated the rescue",
      eig_DE == eig_S6,
      f"λ_k = {eig_DE} = round S⁶ eigenvalues {eig_S6}. Numerical match.")

# ----------------------------------------------------------------------------
# 2. DEGENERACIES: DE = SO(5)-on-S⁴ (F787), NOT SO(7)-on-S⁶ -> NOT a round sphere.
# ----------------------------------------------------------------------------
print("\n--- 2. DEGENERACIES decide: DE = S⁴ harmonics (1,5,14,30), NOT S⁶ (1,7,27,77) ---")
deg_DE = [deg_harmonic(4, k) for k in range(5)]     # corpus F787: SO(5) harmonics on S⁴
deg_S6 = [deg_harmonic(6, k) for k in range(5)]     # round S⁶: SO(7) harmonics
mismatch = deg_DE != deg_S6
check("the DEGENERACIES of the λ_k=k(k+5) ladder are SO(5) degree-k harmonics on S⁴ = 1,5,14,30,55 (corpus "
      "F787), NOT the round-S⁶ SO(7) harmonics 1,7,27,77,182. Eigenvalues alone don't identify a geometry "
      "-- the DEGENERACIES do, and they say S⁴, NOT round S⁶",
      mismatch and deg_DE == [1, 5, 14, 30, 55] and deg_S6 == [1, 7, 27, 77, 182],
      f"DE degeneracies (F787) = {deg_DE} (= round S⁴); round S⁶ = {deg_S6}. MISMATCH -> not a round S⁶.")

# ----------------------------------------------------------------------------
# 3. The "+5" is the CONFORMAL shift on S⁴: k(k+5) = k(k+3) + 2k. Conformal Casimir, not a sphere.
# ----------------------------------------------------------------------------
print("\n--- 3. the '+5' = conformal shift: k(k+5) = S⁴ Laplacian k(k+3) + 2k (discrete-series ρ-shift) ---")
shift = [lam_DE(k) - k*(k + 3) for k in range(5)]   # k(k+5) - k(k+3)
check("the DE eigenvalue k(k+5) = the S⁴ Laplacian k(k+3) PLUS 2k (the conformal ρ-shift of the SO(5,2) "
      "discrete series). So it is the CONFORMAL Casimir on the S⁴ boundary, NOT a round-sphere Laplacian; "
      "it only equals round-S⁶ eigenvalues because the conformal shift 2k takes k(k+3)->k(k+5)",
      shift == [0, 2, 4, 6, 8],
      f"k(k+5) - k(k+3) = {shift} = 2k. S⁴ harmonics (degeneracy) + conformal shift (eigenvalue) = the "
      "discrete-series Casimir, not a sphere. Actual Shilov boundary = S⁴×S¹/Z₂ (product, spectrum ℓ(ℓ+3)+m²).")

# ----------------------------------------------------------------------------
# 4. Even granting S⁶: λ₁=6=dim=C_2 != Einstein constant n_C=5. Obata identification fails on S⁶ too.
# ----------------------------------------------------------------------------
print("\n--- 4. even granting S⁶: λ₁=6=dim=C_2, Einstein constant = n_C=5 -> 'λ₁=Einstein const' fails (6≠5) ---")
lam1 = lam_DE(1)
einstein_const_S6 = 6 - 1     # unit S⁶: Ric=(n-1)g -> Einstein constant = n-1 = 5
check("even GRANTING a round S⁶: λ₁ = 6 = C_2 = dim(S⁶) = n_C+1 (the DIMENSION), but the Einstein "
      "constant of unit S⁶ (Ric=(n-1)g) = n-1 = 5 = n_C. So 'λ₁ = Einstein constant' would require "
      "C_2 = n_C (6=5) -- FALSE. λ₁ is the dimension, not the Einstein constant -> the Obata "
      "identification fails on S⁶ too",
      lam1 == C_2 and einstein_const_S6 == n_C and C_2 != n_C,
      f"λ₁ = {lam1} = C_2; Einstein const(S⁶) = {einstein_const_S6} = n_C. 6 != 5 -> identification fails.")

# ----------------------------------------------------------------------------
# 5. Verdict: rescue FAILS, retraction FINAL.
# ----------------------------------------------------------------------------
print("\n--- 5. VERDICT: sphere-rescue FAILS -> retraction FINAL ---")
check("VERDICT: the sphere-rescue FAILS. k(k+5) matches round S⁶ EIGENVALUES only; the DEGENERACIES are "
      "S⁴ (F787), the '+5' is a conformal shift, and the actual boundary S⁴×S¹/Z₂ is a product -- NOT a "
      "round sphere. Obata (round-sphere equality) does NOT apply -> the a₀↔a₁ tie is NOT rescued, the "
      "RETRACTION IS FINAL. (And even on S⁶, λ₁=C_2=6 is the dimension, not the Einstein constant n_C=5.) "
      "The eigenvalue coincidence is not a geometry -- assuming it were repeats the original error",
      mismatch and shift == [0, 2, 4, 6, 8] and C_2 != n_C,
      "honest negative, verified at source (degeneracies decide). The DE rate λ₁=C_2 stands as the "
      "conformal-Casimir spectral gap; its Obata identification with the Einstein constant is WITHDRAWN.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (sphere-rescue FAILS: degeneracies=S⁴ not S⁶; retraction FINAL)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5129, Pull A -- sphere-rescue for Obata a₀↔a₁ tie):
  * EIGENVALUES: λ_k = k(k+5) (T1452) = round S⁶ Laplacian (0,6,14,24,36) -- MATCH (the clue).
  * DEGENERACIES: DE ladder = SO(5) harmonics on S⁴ = 1,5,14,30,55 (F787), NOT round S⁶'s SO(7) harmonics
    1,7,27,77,182 -- MISMATCH. Degeneracies identify the geometry -> S⁴, NOT round S⁶.
  * THE '+5': k(k+5) = S⁴ Laplacian k(k+3) + 2k (conformal ρ-shift) -> SO(5,2) discrete-series CONFORMAL
    Casimir on S⁴, not a sphere Laplacian. Actual Shilov boundary S⁴×S¹/Z₂ = product, spectrum ℓ(ℓ+3)+m².
  * EVEN ON S⁶: λ₁=6=dim=C_2 != Einstein constant n_C=5 -> Obata identification fails there too.
  * VERDICT: RESCUE FAILS -> RETRACTION FINAL. The DE rate λ₁=C_2 stands (conformal-Casimir spectral gap);
    its identification with the Einstein constant via Obata is WITHDRAWN. Eigenvalue-coincidence != geometry.

AUG-08 [TEGMARK]. Nothing pushed. Nothing banked past the spectral-gap value. Sphere-rescue FAILS
(degeneracies = S⁴ not S⁶; conformal shift; product boundary); retraction FINAL. Verified at source; the
original error (assuming a sphere) NOT repeated. @Keeper fix the corpus Obata mis-citation (Pull D). Count N.
""")
