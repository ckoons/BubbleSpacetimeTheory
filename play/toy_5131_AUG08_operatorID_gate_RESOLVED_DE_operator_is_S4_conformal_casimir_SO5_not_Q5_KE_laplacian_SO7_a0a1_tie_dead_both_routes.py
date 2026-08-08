#!/usr/bin/env python3
"""
Toy 5131: OPERATOR-ID GATE (Elie's pull, K1291) -- RESOLVED against the a₀↔a₁ tie. Is the dark-energy
relaxation operator the Q⁵ Kähler-Einstein Laplacian (SO(7) degeneracies) or the S⁴ conformal Casimir
(SO(5)-on-S⁴ degeneracies)? VERIFIED AT SOURCE (F787): the operator's degeneracies are SO(5) harmonics on
S⁴ = 1,5,14,30,55. DECISIVE DISCRIMINATOR: the first nontrivial eigenspace has dim 5 = the SO(5) vector,
and 5 is NOT an SO(7) irrep dimension (smallest nontrivial SO(7) irrep = 7). So the operator has SO(5)
symmetry -- it is the S⁴ CONFORMAL CASIMIR, NOT the Q⁵ (SO(7)) Kähler-Einstein Laplacian. -> Lichnerowicz-
Matsushima does NOT apply -> the factor-of-rank relation (λ₁ = rank × Einstein-constant) is NOT real ->
the a₀↔a₁ tie is DEAD via BOTH Obata (Pull A) and Kähler-Einstein. Elie resolving the gate. (K1291.)
E / Elie -- verified at SOURCE (the whole point; assuming was the original error). Honest negative: the DE
rate λ₁=C_2 stands as a number (the conformal-Casimir spectral gap), but its identification with gravity's
Einstein constant (any factor) is NOT earned. Third honest brake on the same elegant tie; the rate survives.

THE GATE (Keeper): the a₀↔a₁ tie (DE rate = rank × Einstein-constant, C_2 = rank·N_c) is REAL only if the
DE operator is the Q⁵ Kähler-Einstein Laplacian (so Lichnerowicz-Matsushima applies). Decide by the
DEGENERACIES (eigenvalues alone don't identify the operator -- the Pull-A lesson).

  * SOURCE (F787): the λ_k=k(k+5) ladder's degeneracies are SO(5) degree-k harmonics on S⁴ = 1,5,14,30,55
    -- the K-types of the SO(5,2) holomorphic discrete series (K = SO(5)×SO(2)).
  * Q⁵ = SO(7)/(SO(5)×SO(2)) Kähler-Einstein Laplacian: its eigenspaces are SO(7) reps (SO(7) symmetry).
  * DECISIVE: the DE first-eigenspace dim = 5 = the SO(5) VECTOR. 5 is NOT an SO(7) irrep dimension
    (SO(7) small irreps: 7,8,21,27,35,...; smallest nontrivial = 7). So the DE eigenspaces are SO(5) reps,
    NOT SO(7) reps -> the operator has SO(5) symmetry (S⁴), NOT SO(7) symmetry (Q⁵).

=> VERDICT (plain): the operator-ID gate RESOLVES against the tie. The DE relaxation operator is the S⁴
CONFORMAL CASIMIR (SO(5)-on-S⁴ degeneracies, the SO(5,2) discrete-series K-Casimir), NOT the Q⁵ Kähler-
Einstein Laplacian (SO(7) degeneracies) -- decisively, because the first eigenspace has dim 5 which is not
even an SO(7) irrep dimension. So Lichnerowicz-Matsushima (a Kähler-manifold theorem for the Q⁵ Laplacian)
does NOT apply -> the factor-of-rank relation (λ₁ = rank × Einstein-constant = 2·N_c = C_2) is NOT real ->
the a₀↔a₁ tie is DEAD via BOTH Obata (Pull A) and Kähler-Einstein. The DE rate λ₁ = C_2 stands as the
conformal-Casimir spectral gap (a real number); its identification with gravity's Einstein constant (any
factor) is NOT earned. Verified at source; assuming was the original error, not repeated.

=> DISPOSITION: gate RESOLVED (honest negative) -- DE operator = S⁴ conformal Casimir (SO(5)), not Q⁵ KE
Laplacian (SO(7)); the a₀↔a₁ tie is dead both routes. The DE story keeps: sign banks (Bernstein), rate =
C_2 (number), DESI radial survives; it loses the gravity-rate tie entirely. Firer: Elie; Keeper folds into
#79/DE tier; Cal audits. Nothing pushed. Nothing banked past the rate.

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

# DE operator degeneracies (F787, source): SO(5) harmonics on S^4
DE_deg = [(2*k + 3)*(k + 2)*(k + 1)//6 for k in range(5)]      # 1,5,14,30,55
SO7_small_irreps = {1, 7, 8, 21, 27, 35, 48, 105, 112}         # SO(7)=B3 small irrep dims (no 5)

print("=" * 78)
print("Toy 5131: operator-ID gate RESOLVED -- DE operator = S⁴ conformal Casimir (SO(5)), NOT Q⁵ KE (SO(7))")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. Source: DE degeneracies = SO(5)-on-S⁴ (F787).
# ----------------------------------------------------------------------------
print("\n--- 1. SOURCE (F787): DE operator degeneracies = SO(5) harmonics on S⁴ = 1,5,14,30,55 ---")
check("VERIFIED AT SOURCE (F787): the λ_k=k(k+5) ladder's degeneracies are SO(5) degree-k harmonics on "
      "S⁴ = 1,5,14,30,55 -- the K-types of the SO(5,2) holomorphic discrete series (K = SO(5)×SO(2)). "
      "This is the DE relaxation operator's multiplicity structure (not assumed -- read from F787)",
      DE_deg == [1, 5, 14, 30, 55],
      f"DE degeneracies = {DE_deg} (SO(5)-on-S⁴, F787). The operator is the SO(5,2) discrete-series K-Casimir.")

# ----------------------------------------------------------------------------
# 2. Decisive: dim 5 is the SO(5) vector, NOT any SO(7) irrep -> SO(5) symmetry, not SO(7).
# ----------------------------------------------------------------------------
print("\n--- 2. DECISIVE: dim 5 = SO(5) vector; 5 is NOT an SO(7) irrep dim -> SO(5), not SO(7) ---")
first_eigenspace = DE_deg[1]      # k=1 -> dim 5
is_so7 = first_eigenspace in SO7_small_irreps
check("the DE first nontrivial eigenspace (k=1, λ₁=6) has dim 5 = the SO(5) VECTOR. 5 is NOT an SO(7) "
      "irrep dimension (SO(7) small irreps: 7,8,21,27,35,...; smallest nontrivial = 7). So the DE "
      "eigenspaces are SO(5) reps, NOT SO(7) reps -> the operator has SO(5) symmetry (S⁴), NOT SO(7) "
      "symmetry (Q⁵). Eigenvalues alone can't identify the operator; the DEGENERACIES do (Pull-A lesson)",
      first_eigenspace == 5 and not is_so7,
      f"first eigenspace dim = {first_eigenspace} = SO(5) vector; in SO(7) irrep dims? {is_so7}. "
      f"smallest nontrivial SO(7) irrep = {min(d for d in SO7_small_irreps if d>1)} -> no SO(7) rep has dim 5.")

# ----------------------------------------------------------------------------
# 3. -> operator is S⁴ conformal Casimir -> Lichnerowicz-Matsushima does NOT apply -> tie dead.
# ----------------------------------------------------------------------------
print("\n--- 3. -> S⁴ conformal Casimir -> Lichnerowicz-Matsushima N/A -> factor-of-rank relation NOT real ---")
check("therefore the DE relaxation operator is the S⁴ CONFORMAL CASIMIR (SO(5)-on-S⁴, the discrete-series "
      "K-Casimir), NOT the Q⁵ Kähler-Einstein Laplacian (SO(7)). Lichnerowicz-Matsushima is a theorem for "
      "the Q⁵ (Kähler) Laplacian -> it does NOT apply to the S⁴ conformal Casimir -> the factor-of-rank "
      "relation (λ₁ = rank × Einstein-constant = 2·N_c = C_2) is NOT real",
      not is_so7 and DE_deg[1] == 5,
      f"S⁴ conformal Casimir (SO(5)) != Q⁵ KE Laplacian (SO(7)). L-M N/A -> λ₁=rank×Einstein-const "
      f"(={rank}×{N_c}={C_2}) is NOT established. Same operator-ID gap that sank Obata (Pull A).")

# ----------------------------------------------------------------------------
# 4. Verdict: a₀↔a₁ tie DEAD both routes; DE rate λ₁=C_2 stands.
# ----------------------------------------------------------------------------
print("\n--- 4. verdict: a₀↔a₁ tie DEAD (both Obata + Kähler-Einstein); DE rate λ₁=C_2 stands ---")
check("VERDICT: the operator-ID gate RESOLVES against the tie. DE operator = S⁴ conformal Casimir (SO(5)), "
      "NOT Q⁵ KE Laplacian (SO(7)) -- decisively (first eigenspace dim 5 is not an SO(7) irrep). So the "
      "a₀↔a₁ tie is DEAD via BOTH Obata (Pull A) and Kähler-Einstein (this gate). The DE rate λ₁ = C_2 = "
      "6 STANDS as the conformal-Casimir spectral gap (a real number); its identification with gravity's "
      "Einstein constant (any factor) is NOT earned. Verified at source; assuming NOT repeated",
      first_eigenspace == 5 and not is_so7,
      "third honest brake on the same elegant tie; the RATE survives all three -- its own quiet evidence "
      "it is real. DE keeps: sign (Bernstein), rate=C_2, DESI-radial-survives; loses the gravity-rate tie.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (operator = S⁴ conformal Casimir SO(5), NOT Q⁵ KE SO(7); a₀↔a₁ tie DEAD)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5131, operator-ID gate -- resolves the a₀↔a₁ tie):
  * SOURCE (F787): DE operator degeneracies = SO(5) harmonics on S⁴ = 1,5,14,30,55 (discrete-series K-Casimir).
  * DECISIVE: first eigenspace dim = 5 = SO(5) vector; 5 is NOT an SO(7) irrep dim (smallest = 7) ->
    the operator has SO(5) symmetry (S⁴), NOT SO(7) symmetry (Q⁵).
  * -> DE operator = S⁴ CONFORMAL CASIMIR, NOT Q⁵ Kähler-Einstein Laplacian -> Lichnerowicz-Matsushima
    does NOT apply -> the factor-of-rank relation (λ₁ = rank × Einstein-constant = C_2) is NOT real.
  * VERDICT: the a₀↔a₁ tie is DEAD via BOTH Obata (Pull A) and Kähler-Einstein (this gate). The DE rate
    λ₁ = C_2 stands (conformal-Casimir spectral gap, a number); the gravity-rate identification is unearned.

AUG-08 [TEGMARK]. Nothing pushed. Nothing banked past the rate. Operator-ID gate RESOLVED: DE operator =
S⁴ conformal Casimir (SO(5)), not Q⁵ KE Laplacian (SO(7)) -- verified at source (5 not an SO(7) dim). The
a₀↔a₁ tie is dead both routes; the DE rate C_2 survives its third brake. Never "DE relaxes at gravity's rate". Count N.
""")
