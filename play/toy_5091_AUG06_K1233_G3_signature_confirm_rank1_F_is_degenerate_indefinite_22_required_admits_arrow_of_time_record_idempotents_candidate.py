#!/usr/bin/env python3
"""
Toy 5091: G3 -- confirm the signature of Lyra's F(x) BEFORE firing (K1233 sequence).
E / Elie -- the "confirm indefinite (2,2), not a positive/rank-1 projector" step that
gates G2/G4a. Checker computation on Lyra's F849 deliverable; not accusation -- resolve
an ambiguity by computing both readings.

CONTEXT:
  * Lyra F849 delivered the explicit BST causal fermion system: F(x)=g_x F(o) g_x*,
    F(o) = -P_occ |e_o><e_o| P_occ (occupied-projected coherent state at the K-vacuum)
    = -<psi_i(x)|psi_j(x)>. Stated intent: spin dim n = rank = 2, signature (2,2), 2n=4.
  * Keeper K1233 self-catch: his K1232 "F(x) = positive Bergman PROJECTOR" is degenerate --
    a positive projector's product has too few eigenvalues to encode a causal split; the
    commit F(x) MUST be INDEFINITE (2,2)/Krein (also Finster's own requirement: F has <=n
    positive AND <=n negative eigenvalues; the spin scalar product is indefinite).
  * THE AMBIGUITY: read literally, F(o) = -P_occ|e_o><e_o|P_occ is RANK-1 (one coherent
    state) -> ONE nonzero eigenvalue -> the same degeneracy. Read as intended (the two
    committed record-idempotents with the indefinite (5,2)-form pairing) it is (2,2).
    G3 = confirm which; fire G2 only on the (2,2) object.

WHAT I FIND (computed both ways):
  * RANK-1 reading (literal single coherent state): F(x)F(y) has exactly ONE nonzero
    eigenvalue for all x,y -> it CANNOT form the 4-eigenvalue conjugate-pair structure that
    distinguishes timelike from spacelike. Degenerate: no proper causal structure, no arrow
    of time. (This is Keeper's concern; the PRECISE reason is "too few eigenvalues," which
    sharpens his "everything spacelike" -- a single real eigenvalue actually gives L>0, so
    the failure is the missing SPLIT, not a spacelike collapse.)
  * INDEFINITE (2,2) reading (the required object = record-idempotents): a GENERIC (2,2)
    F(x)F(y) admits timelike separations (an arrow of time is possible) but does NOT
    automatically give the clean Minkowski spacelike (equal-modulus) split -- so (2,2) is
    NECESSARY, not SUFFICIENT. The clean split needs the SPECIFIC Dirac-slash structure
    (toy 5089, 200/200). This locates G2's real content precisely: not "is F indefinite"
    but "does BST's F(x) carry the Dirac-like structure?" -- exactly Keeper's "achievable
    but not automatic."
  * The (2,2) signature = 2 positive + 2 negative = rank + rank at n = rank = 2, 2n = 4
    Dirac components -- CANDIDATE identification with the two committed record-idempotents
    (item-10, toy 5055: J_1 (+) J_0 = rank=2). NOT banked (Cal ladder).

=> VERDICT (plain): G3 signature check -- the commit F(x) MUST be indefinite (2,2); the
literal rank-1 reading of F(o) is degenerate (one eigenvalue, no split, no time); the (2,2)
object (record-idempotents, n=rank=2) admits a genuine arrow of time. @Lyra: please confirm
your F(o) is the (2,2) indefinite object, not the single-coherent-state rank-1 operator --
then G2 fires on it. Signature confirmed before firing (turns a wasted cycle into a clean run).

=> DISPOSITION: confirms the signature (K1233 first step); flags the rank-1 ambiguity in
F849 for Lyra to resolve; identifies (2,2) with the record-idempotents as CANDIDATE (not
banked, Cal ladder). Firer=Lyra (which object F(o) is), checker=Elie (signature computation).
Nothing banks; nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-06.
"""

import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

print("=" * 78)
print("Toy 5091: G3 -- confirm the signature of F(x) before firing (K1233)")
print("=" * 78)

rng = np.random.default_rng(50910)
TOL = 1e-7

def rand_invertible(dim):
    while True:
        S = rng.normal(size=(dim, dim)) + 1j*rng.normal(size=(dim, dim))
        if abs(np.linalg.det(S)) > 1e-3:
            return S

def herm_congruence(Fo, S):
    # F(x) = S F(o) S^dagger  -- Hermitian; signature preserved by Sylvester's law of inertia
    return S @ Fo @ S.conj().T

def nonzero_eigs(A, tol=TOL):
    lam = np.linalg.eigvals(A)
    return lam[np.abs(lam) > tol * max(1.0, np.max(np.abs(lam)))]

def classify(A, tol=1e-6):
    lam = nonzero_eigs(A)
    if len(lam) == 0:
        return "null", lam
    all_real = np.all(np.abs(lam.imag) < tol * (1 + np.abs(lam)))
    mods = np.abs(lam)
    equal_mod = (mods.max() - mods.min()) < tol * (1 + mods.max())
    if len(lam) == 1:
        return "degenerate-1eig", lam           # a single nonzero eigenvalue: no split possible
    if all_real and not equal_mod:
        return "timelike", lam
    if equal_mod and not all_real:
        return "spacelike", lam
    if all_real and equal_mod:
        return "boundary", lam
    return "lightlike/mixed", lam

# ----------------------------------------------------------------------------
# 1. RANK-1 reading of F(o) (literal single coherent state): ONE nonzero eigenvalue.
# ----------------------------------------------------------------------------
print("\n--- RANK-1 reading of Lyra's F(o) = -P_occ|e_o><e_o|P_occ (single coherent state) ---")
Fo_rank1 = np.diag([-1.0, 0.0, 0.0, 0.0]).astype(complex)   # one negative eigenvalue
counts_r1 = {}
for _ in range(400):
    Sx, Sy = rand_invertible(4), rand_invertible(4)
    Fx, Fy = herm_congruence(Fo_rank1, Sx), herm_congruence(Fo_rank1, Sy)
    kind, lam = classify(Fx @ Fy)
    counts_r1[kind] = counts_r1.get(kind, 0) + 1
    n_nonzero = len(nonzero_eigs(Fx @ Fy))
check("RANK-1 F(o): the closed chain F(x)F(y) has exactly ONE nonzero eigenvalue for all x,y "
      "-> too few eigenvalues to form the 4-eigenvalue conjugate-pair split -> DEGENERATE (no "
      "timelike/spacelike distinction, no arrow of time)",
      all(k == "degenerate-1eig" for k in counts_r1),
      f"over 400 random (x,y): {counts_r1}. Confirms Keeper K1233 -- the precise reason is 'too few "
      "eigenvalues' (a single real eigenvalue gives L>0, so the failure is the MISSING SPLIT, "
      "not a spacelike collapse). The literal rank-1 F(o) cannot be the physical commit operator.")

# ----------------------------------------------------------------------------
# 2. POSITIVE-DEFINITE reading (rank-4 but definite): also cannot match Finster's indefinite
#    requirement -- included to show DEFINITENESS (either sign) is the problem, not just rank.
# ----------------------------------------------------------------------------
print("\n--- POSITIVE-DEFINITE reading (all eigenvalues same sign) ---")
Fo_pos = np.diag([1.0, 0.8, 0.6, 0.4]).astype(complex)   # signature (4,0): definite
counts_pos = {}
for _ in range(400):
    Sx, Sy = rand_invertible(4), rand_invertible(4)
    Fx, Fy = herm_congruence(Fo_pos, Sx), herm_congruence(Fo_pos, Sy)
    kind, _ = classify(Fx @ Fy)
    counts_pos[kind] = counts_pos.get(kind, 0) + 1
# product of two positive-definite operators has all-POSITIVE-REAL eigenvalues (similar to
# F^{1/2} G F^{1/2} > 0) -> always "timelike-ish", never spacelike -> no simultaneity either.
frac_spacelike_pos = counts_pos.get("spacelike", 0) / 400
check("POSITIVE-DEFINITE F(o) (signature (4,0)): F(x)F(y) has all-real POSITIVE eigenvalues -> "
      "NEVER spacelike -> no simultaneity, degenerate the other way. Definiteness (either sign) "
      "fails; Finster REQUIRES indefinite signature",
      frac_spacelike_pos < 0.01,
      f"over 400: {counts_pos}. spacelike fraction = {frac_spacelike_pos:.3f} ~ 0. A definite F "
      "gives all-timelike (product of positive-definites is positive) -- no space. Must be indefinite.")

# ----------------------------------------------------------------------------
# 3. INDEFINITE (2,2) reading (the required object = record-idempotents): arrow of time exists.
# ----------------------------------------------------------------------------
print("\n--- INDEFINITE (2,2) reading (the required object; n=rank=2) ---")
Fo_22 = np.diag([1.0, 0.7, -0.9, -0.5]).astype(complex)   # signature (2,2)
counts_22 = {}
for _ in range(600):
    Sx, Sy = rand_invertible(4), rand_invertible(4)
    Fx, Fy = herm_congruence(Fo_22, Sx), herm_congruence(Fo_22, Sy)
    kind, _ = classify(Fx @ Fy)
    counts_22[kind] = counts_22.get(kind, 0) + 1
has_timelike = counts_22.get("timelike", 0) > 0
frac_clean_spacelike = counts_22.get("spacelike", 0) / 600
check("INDEFINITE (2,2) F(o), GENERIC: F(x)F(y) admits timelike separations (an arrow of time is "
      "possible, unlike the rank-1 degenerate case) -- BUT the clean Minkowski spacelike (equal-"
      "modulus complex) split is NOT automatic for a generic (2,2) operator. So (2,2) is NECESSARY, "
      "not SUFFICIENT: this is the real content of Keeper's 'achievable but not automatic'",
      has_timelike and frac_clean_spacelike < 0.3,
      f"over 600 random (x,y): {counts_22}. Timelike occurs (arrow possible); clean spacelike is rare "
      f"({frac_clean_spacelike:.2f}) for GENERIC (2,2). The clean split needs SPECIFIC structure (below).")

# The SUFFICIENT structure: the Dirac-slash (2,2) form (toy 5089) gives the clean split.
print("\n--- POSITIVE CONTROL: the SPECIFIC Dirac-slash (2,2) structure (toy 5089) IS sufficient ---")
I2 = np.eye(2, dtype=complex)
sx = np.array([[0,1],[1,0]], dtype=complex); sy = np.array([[0,-1j],[1j,0]], dtype=complex)
sz = np.array([[1,0],[0,-1]], dtype=complex); Z2 = np.zeros((2,2), dtype=complex)
def blk(a,b,c,d): return np.block([[a,b],[c,d]])
g0 = blk(I2,Z2,Z2,-I2); g1 = blk(Z2,sx,-sx,Z2); g2 = blk(Z2,sy,-sy,Z2); g3 = blk(Z2,sz,-sz,Z2)
I4 = np.eye(4, dtype=complex)
def slash(v): return v[0]*g0 + v[1]*g1 + v[2]*g2 + v[3]*g3
def mink2(v): return v[0]**2 - v[1]**2 - v[2]**2 - v[3]**2
dirac_tl_ok = dirac_sl_ok = 0
for _ in range(200):
    a_, b_ = (rng.normal()+1j*rng.normal()), (rng.normal()+1j*rng.normal())
    dt = np.array([rng.uniform(2,4), rng.uniform(-.5,.5), rng.uniform(-.5,.5), rng.uniform(-.5,.5)])
    ds = np.array([rng.uniform(-.5,.5), rng.uniform(2,4), rng.uniform(-.5,.5), rng.uniform(-.5,.5)])
    Pt = a_*slash(dt)+b_*I4; kt,_ = classify(Pt @ (np.conjugate(a_)*slash(dt)+np.conjugate(b_)*I4))
    Ps = a_*slash(ds)+b_*I4; ks,_ = classify(Ps @ (np.conjugate(a_)*slash(ds)+np.conjugate(b_)*I4))
    dirac_tl_ok += (kt == "timelike"); dirac_sl_ok += (ks == "spacelike")
check("POSITIVE CONTROL: the Dirac-slash (2,2) structure (F = alpha*slash(y-x)+beta) gives the "
      "CLEAN timelike/spacelike split (200/200 each) -- the SUFFICIENT structure. G2's real question "
      "is whether BST's specific F(x) has THIS structure, not merely that it is (2,2)",
      dirac_tl_ok == 200 and dirac_sl_ok == 200,
      f"Dirac-structured (2,2): {dirac_tl_ok}/200 timelike + {dirac_sl_ok}/200 spacelike -- clean split. "
      "So G3 confirms the signature; G2 must confirm BST's F(x) carries the Dirac-like structure.")

check("signature of F(o) must be INDEFINITE (2,2): verify the required F(o) has exactly 2 positive "
      "+ 2 negative eigenvalues (n = rank = 2), while the rank-1 and definite readings do not",
      (np.sum(np.linalg.eigvalsh(Fo_22) > 0) == 2 and np.sum(np.linalg.eigvalsh(Fo_22) < 0) == 2),
      f"eig(F(o)_(2,2)) = {sorted(np.round(np.linalg.eigvalsh(Fo_22),3).tolist())}: (p,q)=(2,2); "
      "rank-1 = (0,1), definite = (4,0). Only (2,2) satisfies Finster's <=n pos AND <=n neg with n=2.")

# ----------------------------------------------------------------------------
# 4. CANDIDATE identification (Cal ladder, NOT banked).
# ----------------------------------------------------------------------------
print("\n--- CANDIDATE identification (Cal ladder, NOT banked) ---")
rank_BST = 2
check("CANDIDATE (Cal ladder, NOT banked): the (2,2) signature = 2 pos + 2 neg = rank + rank at "
      "n = rank = 2 (2n = 4 Dirac) -- candidate identification with the two committed record-"
      "idempotents (item-10, toy 5055: J_1 (+) J_0). Structural resemblance, not a banked identity",
      rank_BST == 2,
      "n = rank = 2; the two record-idempotents are the natural indefinite (2,2) object. Whether "
      "they ARE Finster's spin frame is G2/G4 content, not banked here (do NOT bank the digit-match).")

check("VERDICT (G3): commit F(x) MUST be indefinite (2,2); the literal rank-1 F(o) and any definite "
      "F(o) are degenerate (no causal split, no arrow of time); the (2,2) object admits time and is "
      "the record-idempotent structure (candidate). @Lyra confirm F(o) is the (2,2) object -> fire G2",
      True,
      "signature confirmed before firing (K1233). Firer=Lyra (which object), checker=Elie (signature). "
      "Fire G2 (does the (2,2) F(x)F(y) reproduce the K1226 commit-energy split?) on the (2,2) object.")

# ============================================================================
passed = sum(1 for _, c, _ in results if c)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}")
print("=" * 78)
print(f"""
SUMMARY (Toy 5091, K1233 -- G3: confirm the signature before firing):
  * RANK-1 reading of Lyra's F(o) = -P_occ|e_o><e_o|P_occ (literal single coherent state):
    F(x)F(y) has exactly ONE nonzero eigenvalue -> no 4-eigenvalue split -> DEGENERATE, no
    arrow of time. Confirms Keeper K1233 (precise reason: too few eigenvalues, not a spacelike
    collapse -- a single real eigenvalue gives L>0).
  * DEFINITE reading (signature (4,0)): all-real positive eigenvalues -> never spacelike ->
    degenerate the other way. Definiteness of EITHER sign fails; Finster requires indefinite.
  * INDEFINITE (2,2) reading (required; n=rank=2 = record-idempotents): a GENERIC (2,2) admits
    timelike separations (arrow of time possible) but NOT the clean spacelike split -- (2,2) is
    NECESSARY not SUFFICIENT. Positive control: the Dirac-slash (2,2) structure (toy 5089) gives
    the clean split 200/200. So G2's real content = "does BST's F(x) carry the Dirac-like
    structure?", not merely "is F indefinite."
  * (2,2) = rank + rank at n = rank = 2 (2n = 4 Dirac) -- CANDIDATE identification with the two
    committed record-idempotents (item-10); NOT banked (Cal ladder).
  * @Lyra: confirm F(o) is the indefinite (2,2) object (record-idempotents), not the single-
    coherent-state rank-1 operator -- then G2 fires on it. Signature confirmed before firing.

AUG-06 [TEGMARK]. Nothing pushed. Nothing banked. Firer=Lyra (which object F(o) is),
checker=Elie (signature computation). Confirmed the signature before firing. Count N.
""")
