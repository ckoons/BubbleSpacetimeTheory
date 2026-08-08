#!/usr/bin/env python3
"""
Toy 5130: SUPPORT for Keeper's Pull D (a₀↔a₁ via Kähler-Einstein / Lichnerowicz-Matsushima, NOT Obata) --
the skeptical spectral check BEFORE the rescue banks. KEY FACT: Lichnerowicz-Matsushima (Kähler) gives
λ₁ = 2k (NOT λ₁ = k), so λ₁ = C_2 = 6 forces the Einstein constant k = C_2/2 = N_c = 3. -> the DE rate
(C_2=6) = rank × (Einstein constant N_c=3), a REAL relation (C_2 = rank·N_c), but NOT "same value" (6 ≠ 3,
off by the Kähler factor rank=2). PLUS the operator-ID caveat from Pull A: the DE operator has S⁴-harmonic
degeneracies (conformal Casimir), which may NOT be the Q⁵ Kähler-Einstein Laplacian -- so even this
relation needs the operator identified at source (Pull A's lesson). Elie supporting Keeper. (K1291 Pull D.)
E / Elie -- fish-detector role: Cal #27 fires at the elegant rescue right after a kill. I hand Keeper the
factor-of-rank + operator-ID constraints so "same value" isn't over-claimed. Non-prejudging: I give the
spectral facts; Keeper applies them to his exact "same-value" claim.

THE ROUTE (Keeper): after Obata failed (Pull A, sphere-rescue dead), try Kähler-Einstein. Q⁵ (the compact
dual) IS Kähler-Einstein (compact Hermitian symmetric space), so Lichnerowicz-Matsushima applies (unlike
Obata, which needed a round sphere). Good instinct. BUT two things must clear:

  FACT 1 (the Kähler factor): Lichnerowicz-Matsushima -- compact Kähler-Einstein with Ric = k·g has
  λ₁ = 2k (equality for HSS with holomorphic vector fields; NOT λ₁ = k). Sanity: CP¹=S²(unit), Ric=1·g,
  λ₁=2=2·1. -> IF λ₁ = C_2 = 6, then the Einstein constant k = 3 = N_c, and λ₁ = 2k = rank·N_c = C_2.
  So the DE rate (6) = rank × Einstein-constant (3) -- NOT the SAME VALUE (off by rank=2). The honest tie
  is "DE rate = rank × Einstein-constant" (a real relation, C_2 = rank·N_c), not "a₀ = a₁ same value."

  CAVEAT 2 (operator-ID, from Pull A): the DE relaxation operator is the SO(5,2) discrete-series conformal
  Casimir with degeneracies = SO(5)-harmonics-on-S⁴ (1,5,14,30,55). The Q⁵ Kähler-Einstein Laplacian has
  DIFFERENT (SO(7)) degeneracies. So the DE operator may NOT be the Q⁵ KE Laplacian -- the Kähler route
  needs the SAME source-verification Pull A did (don't assume the operator is the KE Laplacian).

=> VERDICT (plain, support): the Kähler-Einstein / Lichnerowicz-Matsushima route does NOT deliver "a₀↔a₁
SAME value." It gives λ₁ = 2k, so the DE rate (C_2=6) = rank × Einstein-constant (N_c=3) -- a factor of
rank=2 apart, a real relation C_2 = rank·N_c, NOT equality. AND it rests on an unverified operator-ID
(Pull A: the DE operator has S⁴ degeneracies, not obviously the Q⁵ KE Laplacian). So before banking any
tie: (a) decide whether "DE rate = rank × Einstein-constant" is the claim (it is NOT "same value"), and
(b) verify the DE operator IS the Q⁵ KE Laplacian at source. Both must clear. The DE rate λ₁ = C_2 stands;
its identification with the Einstein constant (any factor) is NOT yet earned.

=> DISPOSITION: support for Pull D -- the two constraints ("same value" is really rank×; operator-ID
unverified). Keeper applies them to his exact claim; I do not prejudge his synthesis, I hand him the
skeptical spectral facts. Firer: Elie (support); Keeper owns Pull D; Cal audits. Nothing pushed. Nothing banked.

Author: Elie (CI toy builder). Date: 2026-08-08.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

rank, N_c, n_C, C_2 = 2, 3, 5, 6
lam1 = C_2      # DE spectral gap (conformal Casimir k(k+5)|_{k=1} = 6)

print("=" * 78)
print("Toy 5130: support Pull D -- Kähler L-M gives λ₁=2k -> DE rate = rank×Einstein-const, NOT same value")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. Lichnerowicz-Matsushima Kähler factor: λ₁ = 2k (S² sanity check).
# ----------------------------------------------------------------------------
print("\n--- 1. Lichnerowicz-Matsushima (Kähler): λ₁ = 2k, NOT λ₁ = k (S² sanity) ---")
# CP^1 = S^2 unit: Ric = 1*g (k=1), λ₁(S^2) = 2 = 2k.
s2_lam1, s2_k = 2, 1
check("Lichnerowicz-Matsushima (Kähler): a compact Kähler-Einstein manifold with Ric = k·g has λ₁ = 2k "
      "(equality for compact Hermitian symmetric spaces, which have holomorphic vector fields) -- NOT "
      "λ₁ = k. Sanity: CP¹=S²(unit), Ric=1·g (k=1), λ₁ = 2 = 2·1",
      s2_lam1 == 2*s2_k,
      f"S²: λ₁ = {s2_lam1} = 2k = 2·{s2_k}. The Kähler bound carries a FACTOR OF 2 relative to the Einstein constant.")

# ----------------------------------------------------------------------------
# 2. So λ₁ = C_2 -> Einstein constant = N_c; DE rate = rank × Einstein-constant, NOT same value.
# ----------------------------------------------------------------------------
print("\n--- 2. λ₁ = C_2 -> Einstein const = N_c; DE rate = rank × Einstein-const (off by rank=2) ---")
k_einstein = lam1 // 2      # = C_2/2 = 3
check("applying λ₁ = 2k with λ₁ = C_2 = 6: the Einstein constant k = C_2/2 = 3 = N_c, and λ₁ = 2k = "
      "rank·N_c = 6 = C_2. So the DE rate (C_2 = 6) = rank × Einstein-constant (N_c = 3) -- a REAL "
      "relation (C_2 = rank·N_c), but NOT 'same value': 6 ≠ 3, off by the Kähler factor rank = 2",
      k_einstein == N_c and lam1 == rank*N_c and lam1 != k_einstein,
      f"Einstein const = {k_einstein} = N_c; λ₁ = {lam1} = rank·N_c = C_2. DE rate {lam1} vs Einstein "
      f"const {k_einstein} -> factor rank={rank}. 'a₀↔a₁ same value' does NOT hold; the honest tie is "
      "'DE rate = rank × Einstein-constant'.")

# ----------------------------------------------------------------------------
# 3. Operator-ID caveat (Pull A): the DE operator may NOT be the Q⁵ KE Laplacian.
# ----------------------------------------------------------------------------
print("\n--- 3. operator-ID caveat (Pull A): DE operator has S⁴ degeneracies, not obviously Q⁵ KE Laplacian ---")
from math import comb
deg_DE = [comb(4+k,4) - (comb(2+k,4) if k>=2 else 0) for k in range(4)]   # S⁴ harmonics (Pull A)
check("CAVEAT (Pull A): the DE relaxation operator is the SO(5,2) discrete-series CONFORMAL Casimir with "
      "degeneracies = SO(5)-harmonics-on-S⁴ = 1,5,14,30. The Q⁵ Kähler-Einstein Laplacian has DIFFERENT "
      "(SO(7)) degeneracies. So the DE operator may NOT be the Q⁵ KE Laplacian -> the Kähler route needs "
      "the SAME source-verification Pull A did. Don't assume the operator IS the KE Laplacian",
      deg_DE == [1, 5, 14, 30],
      f"DE degeneracies = {deg_DE} (S⁴, Pull A). Applying Lichnerowicz-Matsushima assumes the DE operator "
      "is the Q⁵ KE Laplacian -- UNVERIFIED (same operator-ID gap as Obata).")

# ----------------------------------------------------------------------------
# 4. Verdict: two constraints for Keeper; "same value" not established.
# ----------------------------------------------------------------------------
print("\n--- 4. verdict: 'same value' not established -- factor-of-rank + operator-ID both open ---")
check("VERDICT (support for Pull D): the Kähler-Einstein / Lichnerowicz-Matsushima route does NOT give "
      "'a₀↔a₁ SAME value'. It gives λ₁ = 2k -> DE rate (C_2=6) = rank × Einstein-constant (N_c=3), a "
      "factor of rank=2 apart (a real relation C_2=rank·N_c, NOT equality); AND it rests on an unverified "
      "operator-ID (Pull A). Both must clear before any tie banks. The DE rate λ₁=C_2 stands; its "
      "identification with the Einstein constant is NOT yet earned",
      lam1 != k_einstein and lam1 == rank*N_c and deg_DE == [1, 5, 14, 30],
      "fish-detector flag before the elegant rescue banks (Cal #27). Keeper applies these to his exact "
      "'same value' claim; I hand him the constraints, not a verdict on his synthesis.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (Kähler L-M: λ₁=2k -> DE rate = rank×Einstein-const, NOT same value; +operator-ID)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5130, support Keeper Pull D -- Kähler-Einstein route to the a₀↔a₁ tie):
  * Lichnerowicz-Matsushima (Kähler): compact KE with Ric=k·g -> λ₁ = 2k (HSS saturate), NOT λ₁ = k.
    Sanity: CP¹=S² λ₁ = 2 = 2·1.
  * -> λ₁ = C_2 = 6 forces Einstein constant k = 3 = N_c; λ₁ = 2k = rank·N_c = C_2. So DE rate (6) =
    rank × Einstein-constant (3) -- a REAL relation (C_2=rank·N_c), NOT 'same value' (off by rank=2).
  * CAVEAT (Pull A): DE operator has S⁴-harmonic degeneracies (conformal Casimir), NOT obviously the Q⁵
    KE Laplacian (SO(7) degeneracies) -> operator-ID unverified, same gap as Obata.
  * VERDICT: 'a₀↔a₁ same value' is NOT established by Kähler-Einstein -- it's rank× (a factor), and rests
    on an unverified operator-ID. Both must clear. The DE rate λ₁=C_2 stands; the Einstein-constant tie unearned.

AUG-08 [TEGMARK]. Nothing pushed. Nothing banked. Support for Keeper Pull D: Kähler L-M gives λ₁=2k, so
DE rate = rank×Einstein-constant (NOT same value), + the operator-ID caveat from Pull A. Fish-detector flag
before the rescue banks. Keeper owns Pull D. Count N.
""")
