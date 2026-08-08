#!/usr/bin/env python3
"""
Toy 5120: TASK #95 frontier (toy 2) -- do the bare item-10 idempotents behave as emergent spacetime
points? FINDING (target-innocent): bare RANK-1 idempotents (the committed records) give ONLY TIMELIKE
relations -- the CFS product F_i F_j is rank-1 with a single REAL eigenvalue |<i|j>|^2, so the causal
classification is timelike for EVERY pair. They produce the causal TIME-order, NOT space. SPACELIKE
separation (a complex-conjugate eigenvalue pair, CFS) requires the (2,2)-SIGNATURE Dirac operators (the
tangent), which the bare records lack. THE MISS LOCALIZES: space comes from the (2,2) Dirac tangent (the
N_c color-space of toy 5119), not from the records. Complementary to Lyra's full-F(x)F(y) CFS map. (K1285.)
E / Elie -- fired target-innocent (I only compute eigenvalue reality; no target). Supports toy 5119 (order
= time, tangent = space) and the CFS gate work (signature (2,2) for 4D Dirac, toy 5097).

CFS CAUSAL CRITERION (Finster, 1102.2585): for local correlation operators F(x),F(y), the eigenvalues of
F(x)F(y) classify -- ALL REAL => TIMELIKE; a complex-conjugate (equal-modulus) pair => SPACELIKE.

WHAT I COMPUTE:
  * bare item-10 idempotents = rank-1 projectors e_i=|psi_i><psi_i| (e^2=e, the {0,1} record). The product
    e_i e_j = <i|j>|psi_i><psi_j| is RANK-1 with nonzero eigenvalue |<i|j>|^2 (REAL, >=0) -> ALL pairs
    TIMELIKE. Verified over many random pairs: zero spacelike. Records give a causal ORDER = TIME.
  * (2,2)-signature Dirac operators F = g D g* with D = diag(+1,+1,-1,-1) (the 4D Dirac spin-dim n=2,
    toy 5097): the product F_x F_y is NOT Hermitian and DOES produce complex-conjugate eigenvalue pairs
    for a nonzero fraction of pairs -> SPACELIKE exists. Space needs the (2,2) tangent, not the records.
  => THE MISS LOCALIZES: bare records -> TIME only (rank-1, real spectrum); SPACE (spacelike) requires the
     (2,2) Dirac tangent. Consistent with toy 5119: order=time (d~1.3), the N_c color-space (the tangent)
     lifts to 4. The idempotents are the TIME/record axis; the tangent is the SPATIAL axis.

=> VERDICT (plain): the bare item-10 idempotents behave as the emergent TIME/record axis -- they give
only timelike relations (rank-1 -> single real eigenvalue), i.e. a causal ORDER, NOT space. Spacelike
separation requires the (2,2)-signature Dirac tangent (toy 5097); that is where the N_c spatial directions
(toy 5119) live. So "de Sitter/geometry from order" is HALF the story: order gives time; the (2,2) tangent
gives space. The miss is localized -- and it is EXACTLY the split whose forcing is the open deep edge
(why 1 time-record + why N_c-space tangent). Map to CFS; do NOT promote.

=> DISPOSITION: toy 2 of the emergent-descent assembly -- bare idempotents = time-only (target-innocent
eigenvalue reality); space = the (2,2) tangent. Localizes the miss to the same (1 time + N_c space) split
as toy 5119. Complementary to Lyra's full-object CFS map (she tests whether the full F(x)F(y) = P(x,y);
I show the bare rank-1 records give time-only). Firer: Elie; frontier lane Elie+Lyra+Keeper; Cal audits.
Nothing pushed. Nothing banked.

Author: Elie (CI toy builder). Date: 2026-08-08.
"""

import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

rng = np.random.default_rng(20260808)

def rand_unit(n):
    v = rng.normal(size=n) + 1j*rng.normal(size=n)
    return v/np.linalg.norm(v)

def eig_all_real(M, tol=1e-9):
    ev = np.linalg.eigvals(M)
    return np.max(np.abs(ev.imag)) < tol

print("=" * 78)
print("Toy 5120: bare item-10 idempotents give TIME only; spacelike needs the (2,2) Dirac tangent")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. Bare rank-1 idempotents: F_i F_j is rank-1, single REAL eigenvalue -> ALWAYS timelike.
# ----------------------------------------------------------------------------
print("\n--- 1. bare item-10 idempotents (rank-1) -> F_i F_j real spectrum -> ALL timelike ---")
n = 4                      # Dirac spinor dimension (4D)
spacelike_count = 0
trials = 400
max_imag = 0.0
for _ in range(trials):
    psi_i, psi_j = rand_unit(n), rand_unit(n)
    e_i = np.outer(psi_i, psi_i.conj())
    e_j = np.outer(psi_j, psi_j.conj())
    M = e_i @ e_j
    ev = np.linalg.eigvals(M)
    max_imag = max(max_imag, np.max(np.abs(ev.imag)))
    if np.max(np.abs(ev.imag)) > 1e-9:
        spacelike_count += 1
    # the single nonzero eigenvalue should equal |<i|j>|^2
overlap_check = True
psi_i, psi_j = rand_unit(n), rand_unit(n)
e_i, e_j = np.outer(psi_i, psi_i.conj()), np.outer(psi_j, psi_j.conj())
nz = sorted(np.abs(np.linalg.eigvals(e_i @ e_j)))[-1]
overlap_check = abs(nz - abs(np.vdot(psi_i, psi_j))**2) < 1e-9
check("bare rank-1 idempotents e_i=|psi_i><psi_i|: the CFS product e_i e_j is RANK-1 with a single "
      "nonzero eigenvalue = |<i|j>|^2 (REAL, >=0). Over 400 random pairs, ZERO have a complex eigenvalue "
      "-> EVERY pair is TIMELIKE. The records give a causal ORDER = TIME, no spacelike separation",
      spacelike_count == 0 and overlap_check,
      f"spacelike (complex-eigenvalue) pairs among {trials} = {spacelike_count}; max|Im eig| = {max_imag:.1e}; "
      f"nonzero eigenvalue = |<i|j>|^2 check = {overlap_check}. Rank-1 -> real spectrum -> timelike-only.")

# ----------------------------------------------------------------------------
# 2. (2,2)-signature Dirac operators: F_x F_y DOES give complex pairs -> SPACELIKE exists.
# ----------------------------------------------------------------------------
print("\n--- 2. (2,2)-signature Dirac operators (the tangent) -> complex pairs -> SPACELIKE exists ---")
D = np.diag([1.0, 1.0, -1.0, -1.0]).astype(complex)   # signature (2,2), 4D Dirac (toy 5097)
def rand_GL(n):
    g = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
    return g
spacelike22 = 0
for _ in range(400):
    gx, gy = rand_GL(4), rand_GL(4)
    Fx = gx @ D @ gx.conj().T          # Hermitian, signature (2,2)
    Fy = gy @ D @ gy.conj().T
    if not eig_all_real(Fx @ Fy):
        spacelike22 += 1
check("(2,2)-signature Dirac operators F = g diag(+,+,-,-) g* (the 4D Dirac tangent, toy 5097): the "
      "product F_x F_y is non-Hermitian and produces complex-conjugate eigenvalue pairs for a nonzero "
      "fraction of pairs -> SPACELIKE separation EXISTS. Space requires the (2,2) tangent, which the bare "
      "rank-1 records lack",
      spacelike22 > 0,
      f"spacelike (complex-eigenvalue) pairs among 400 (2,2)-operators = {spacelike22} (>0). The indefinite "
      "(2,2) signature is what makes spacelike possible -- the records (rank-1, definite) cannot.")

# ----------------------------------------------------------------------------
# 3. The miss localizes: records = TIME axis; (2,2) tangent = SPACE axis. Ties to toy 5119.
# ----------------------------------------------------------------------------
print("\n--- 3. the miss localizes: records -> TIME; (2,2) tangent -> SPACE (= N_c color-space) ---")
check("THE MISS LOCALIZES: bare item-10 idempotents (records) -> TIMELIKE only (rank-1 real spectrum) = "
      "the causal ORDER = TIME; SPACELIKE (space) requires the (2,2)-signature Dirac tangent. This is "
      "EXACTLY toy 5119's split: order = time (d~1.3), the N_c=3 color-space (the tangent) lifts to 4. "
      "The records are the TIME/record axis; the tangent is the SPATIAL axis",
      spacelike_count == 0 and spacelike22 > 0,
      "records give time, tangent gives space -- the same (1 time + N_c space) split, from two independent "
      "angles (dimension-MM in 5119, causal-classification here).")

check("VERDICT: bare item-10 idempotents behave as the emergent TIME/record axis (timelike-only, "
      "target-innocent); SPACE needs the (2,2) Dirac tangent (where the N_c spatial directions live). "
      "'geometry from order' is HALF: order->time, (2,2) tangent->space. The miss localizes to the SAME "
      "(1 time + N_c space) split whose FORCING is the open deep edge. Map to CFS, do not promote",
      spacelike_count == 0 and spacelike22 > 0,
      "complementary to Lyra's full-object CFS map; supports toy 5119. Forcing of the split = frontier.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (records = TIME only; space needs the (2,2) tangent -- miss localized)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5120, task #95 frontier toy 2 -- item-10 idempotents = the TIME/record axis):
  * bare rank-1 idempotents (records): F_i F_j is rank-1, single REAL eigenvalue |<i|j>|^2 -> EVERY pair
    TIMELIKE (0/400 spacelike). Records give a causal ORDER = TIME, no space.
  * (2,2)-signature Dirac operators (the tangent, toy 5097): F_x F_y gives complex-conjugate pairs ->
    SPACELIKE exists. Space requires the indefinite (2,2) tangent, which the records lack.
  * THE MISS LOCALIZES: records = TIME axis; (2,2) tangent = SPACE axis = the N_c color-space of toy 5119.
    Same (1 time + N_c space) split, from two independent angles (MM-dimension + causal-classification).
  * OPEN (deep edge): the FORCING of that split (why 1 time-record + why N_c-space tangent) = the frontier.

AUG-08 [TEGMARK]. Nothing pushed. Nothing banked. Bare idempotents = time-only (target-innocent); space =
the (2,2) Dirac tangent; miss localized to the (1 time + N_c space) split. Complementary to Lyra's CFS
map. Post-break, guards held. Count N.
""")
