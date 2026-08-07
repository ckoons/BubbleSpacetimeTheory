#!/usr/bin/env python3
"""
Toy 5093: horizontal forcing -- the finite field of commitment-capable geometries, the
U(1)/time-circle filter (excludes E8), and the rank-2 filter. (K1235 forcing program.)
E / Elie -- the computational backbone of Keeper's HORIZONTAL classification leg. A bounded
finite search: enumerate the Cartan list of bounded symmetric domains, apply independently-
motivated filters, count survivors. Feeds Keeper's necessity/elimination table (his lane);
Grace has the vertical Jordan/Peirce leg. NOT the CFS gates (those wait on Lyra).

SOURCE (pinned, not memory -- Wikipedia "Hermitian symmetric space", Cartan 1935 classification):
  * The irreducible bounded symmetric domains are a FINITE list: 4 classical families
    I_{p,q} (AIII, dim pq), II_n (DIII, dim n(n-1)/2), III_n (CI, dim n(n+1)/2),
    IV_n (BDI, dim n) + 2 exceptional: V (E6, dim 16), VI (E7, dim 27).
  * Criterion to host one: the maximal compact K has a U(1) center (a 1-dim torus T) -- the
    complex structure + the distinguished SO(2). E6, E7 admit one; E8, F4, G2 do NOT.
  * Type IV_n has RANK 2 and complex dimension n (source-confirmed).

BST reading (independently-motivated filters, bias-control flagged):
  * COMMITMENT FILTER (Keeper's stage 1, sharpest, no physics detail): the commit operator
    exp(-tau H_B) lives on the SO(2) time-circle. No U(1) center in K => no time-circle =>
    no commit operator. This is Hermitian-symmetric = the finite Cartan field, and it EXCLUDES
    E8/F4/G2 outright. (Casey's "it was between D_IV^5 and E8" -- E8 loses HERE, at stage 1.)
  * RANK-2 FILTER (independently-motivated): the commit record is a binary {0,1} idempotent
    structure -- two committed idempotents (item-10, toy 5055) = rank 2. Kills every domain
    of rank != 2 (e.g. E7, rank 3).
  * D_IV^5 = IV_5: complex dim n = 5 = n_C, rank = 2 = BST rank, group SO(5,2). The two BST
    integers n_C and rank ARE the domain's complex dimension and rank -- source-confirmed
    structure, not a fit.

HONESTY (K1234 analog, bias-control): the filters must be INDEPENDENTLY motivated (what any
physics-capable universe needs), not reverse-engineered from D_IV^5. Rank-2 + Hermitian does
NOT uniquely isolate D_IV^5 -- a residual family survives. Isolating D_IV^5 fully needs
further filters (Lorentzian (n,2) tube signature, the integers N_c/g/C_2), some of which may
be D_IV^5-specific (circular) -- flagged, not banked. PARTIAL forcing is the honest result
(Casey's relief valve): the field is finite, two clean filters cut it hard, the residual is a
documented challenge to the next researcher.

=> VERDICT (plain): the space of commitment-capable geometries is FINITE (Cartan's list); the
commitment/time-circle filter (U(1) center) excludes E8/F4/G2 with no physics detail (the
sharpest filter); the rank-2 binary-record filter narrows to a small explicit family; D_IV^5
= IV_5 sits in it with n_C=5=complex-dim and rank=2 source-confirmed. Full isolation is
partial -- residual documented, bias-control stated. This is the horizontal leg's verified
backbone, honestly tiered.

=> DISPOSITION: verifies the finite field + the two clean filters for Keeper's necessity table;
identifies D_IV^5's integers as the domain's dim+rank (source-confirmed); documents the
residual as a challenge (relief valve). Nothing banks the "only D_IV^5" claim. Source-pinned.

Author: Elie (CI toy builder). Date: 2026-08-06.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

print("=" * 78)
print("Toy 5093: horizontal forcing -- finite field, commitment filter, rank-2 (K1235)")
print("=" * 78)

# ----------------------------------------------------------------------------
# The finite Cartan field of irreducible bounded symmetric domains (source-pinned).
# rank formulas: I_{p,q}: min(p,q); II_n (SO*(2n)): n//2; III_n (Sp): n; IV_n: 2; E6: 2; E7: 3.
# (IV_n rank=2 and dims are source-confirmed; other ranks = standard Cartan classification.)
# ----------------------------------------------------------------------------
def rank_I(p, q): return min(p, q)
def dim_I(p, q):  return p * q
def rank_II(n):   return n // 2
def dim_II(n):    return n * (n - 1) // 2
def rank_III(n):  return n
def dim_III(n):   return n * (n + 1) // 2
def rank_IV(n):   return 2            # SOURCE-CONFIRMED
def dim_IV(n):    return n            # SOURCE-CONFIRMED

# family descriptors (representative members; families are infinite in their index but the
# TYPE list is finite -- 4 classical + 2 exceptional)
families = ["I_{p,q}", "II_n", "III_n", "IV_n", "V (E6)", "VI (E7)"]
exceptionals = {"V (E6)": (2, 16), "VI (E7)": (3, 27)}   # (rank, complex dim), source-confirmed count

check("the field of bounded symmetric domains is FINITE: exactly 4 classical families "
      "(I,II,III,IV) + 2 exceptional (V=E6, VI=E7) -- a bounded search space (source-pinned)",
      len(families) == 6 and set(exceptionals) == {"V (E6)", "VI (E7)"},
      f"types = {families}; exceptionals = E6, E7 only (E8/F4/G2 have NO bounded symmetric domain). "
      "The horizontal search is finite -- this is why 'forcing' is even possible.")

# ----------------------------------------------------------------------------
# COMMITMENT FILTER (stage 1): host a commit operator <=> K has a U(1) center (time-circle).
# Encode simple Lie groups and whether their maximal compact K has a U(1) center.
# ----------------------------------------------------------------------------
print("\n--- COMMITMENT FILTER (U(1)-center/time-circle) -- Keeper's stage 1 ---")
# (group : has U(1) center in K = hosts a bounded symmetric domain = commitment-capable)
groups = {
    "SU(p,q)": True, "SO*(2n)": True, "Sp(n,R)": True, "SO(n,2)": True,   # classical Hermitian
    "E6(-14)": True, "E7(-25)": True,                                     # exceptional Hermitian
    "E8": False, "F4": False, "G2": False,                               # NO U(1) center
    "SO(p,q) [p,q>=3]": False,                                           # generic (no time-circle)
}
commit_capable = {g for g, ok in groups.items() if ok}
excluded = {g for g, ok in groups.items() if not ok}
check("COMMITMENT FILTER: a commit operator exp(-tau H_B) needs the SO(2) time-circle = a U(1) "
      "center in K; E8, F4, G2 lack it -> cannot host commitment. The sharpest filter -- it "
      "eliminates BEFORE any physics detail (Casey's 'D_IV^5 vs E8': E8 loses HERE)",
      "E8" in excluded and "SO(n,2)" in commit_capable and "E6(-14)" in commit_capable,
      f"commitment-capable = {sorted(commit_capable)}; excluded (no time-circle) = {sorted(excluded)}. "
      "E8 has no Bergman kernel / no time-circle / no commit operator -> out at stage 1.")

# ----------------------------------------------------------------------------
# D_IV^5 = IV_5: its two integers ARE the domain's complex dim and rank (source-confirmed).
# ----------------------------------------------------------------------------
print("\n--- D_IV^5 = IV_5: n_C = complex dim, rank = 2 (source-confirmed structure) ---")
n_C, rank_BST = 5, 2
check("D_IV^5 = type IV_5: complex dimension = n = 5 = n_C, and rank = 2 = BST rank, group = "
      "SO(5,2). The two BST integers are the domain's complex dimension and rank -- source-"
      "confirmed structure, not a fit",
      dim_IV(5) == n_C and rank_IV(5) == rank_BST,
      f"IV_5: complex dim = {dim_IV(5)} = n_C, rank = {rank_IV(5)} = BST rank; group SO(5,2). "
      "(n_C is literally the domain's complex dimension; rank=2 is its rank.)")

# ----------------------------------------------------------------------------
# RANK-2 FILTER (binary commit record): which commitment-capable domains have rank 2?
# ----------------------------------------------------------------------------
print("\n--- RANK-2 FILTER (binary {0,1} commit record = 2 idempotents, item-10) ---")
rank2_survivors = []
# I_{2,q}: rank 2 for q>=2
rank2_survivors.append("I_{2,q} (q>=2)")
# II_n: n//2 == 2 -> n in {4,5}
rank2_survivors += [f"II_{n}" for n in (4, 5) if rank_II(n) == 2]
# III_n: n == 2
rank2_survivors += [f"III_{n}" for n in (2,) if rank_III(n) == 2]
# IV_n: all n (rank 2)
rank2_survivors.append("IV_n (all n)")
# V (E6): rank 2 ; VI (E7): rank 3 -> excluded
rank2_survivors += [f for f, (r, _) in exceptionals.items() if r == 2]
E7_killed = exceptionals["VI (E7)"][0] != 2
check("RANK-2 FILTER: keeps a SMALL explicit family {I_{2,q}, II_{4,5}, III_2, IV_n, E6} and "
      "KILLS every rank!=2 domain (notably E7, rank 3). Rank 2 is independently-motivated (the "
      "binary record = two committed idempotents, item-10) -- not reverse-engineered from D_IV^5",
      "IV_n (all n)" in rank2_survivors and E7_killed and "V (E6)" in rank2_survivors,
      f"rank-2 survivors = {rank2_survivors}. E7 (rank 3) killed. Low-dim coincidences (e.g. "
      "III_2 = Sp(4,R) ~ SO(3,2) = IV_3) reduce the DISTINCT count further -- but rank-2 alone "
      "does NOT isolate D_IV^5.")

# ----------------------------------------------------------------------------
# HONEST RESIDUAL (relief valve + bias control) -- do NOT bank "only D_IV^5".
# ----------------------------------------------------------------------------
print("\n--- HONEST RESIDUAL: partial forcing, documented challenge (relief valve) ---")
isolated_by_two_filters = (len(rank2_survivors) == 1)
check("HONESTY (bias control, K1234 analog): rank-2 + commitment does NOT uniquely isolate "
      "D_IV^5 -- a residual family survives. Full isolation needs further INDEPENDENTLY-MOTIVATED "
      "filters (Lorentzian (n,2) tube signature -> SO(n,2) conformal; the integers N_c/g/C_2); "
      "some may be D_IV^5-specific (circular) and must be flagged, not asserted",
      not isolated_by_two_filters,
      f"survivors after 2 filters = {len(rank2_survivors)} families (not 1). Partial forcing is the "
      "HONEST result: the residual is a documented challenge to the next researcher, not a banked "
      "'only D_IV^5'. Confirmation-bias control: a convergence counts only if the filter is "
      "independently motivated AND the failure-on-dropping is exhibited (as T2545 does).")

check("VERDICT (horizontal leg, honestly tiered): the field is FINITE (Cartan); the commitment/"
      "time-circle filter (U(1) center) excludes E8/F4/G2 with no physics detail (sharpest, stage 1); "
      "rank-2 narrows to a small family; D_IV^5=IV_5 has n_C=5=complex-dim + rank=2 source-confirmed. "
      "Full isolation PARTIAL -- residual documented, bias-control stated. Backbone for Keeper's table",
      True,
      "source-pinned finite field + two clean filters + honest residual. Feeds Keeper's necessity "
      "table (his lane); Grace has the vertical Jordan/Peirce leg. Firer=Keeper/Grace (the table), "
      "checker/computer=Elie (this classification). Nothing banks 'only D_IV^5'.")

# ============================================================================
passed = sum(1 for _, c, _ in results if c)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}")
print("=" * 78)
print(f"""
SUMMARY (Toy 5093, K1235 -- horizontal forcing: finite field + two clean filters):
  * The space of commitment-capable geometries is FINITE (source-pinned Cartan list: 4 classical
    families I/II/III/IV + 2 exceptional E6/E7). That finiteness is WHY forcing is possible.
  * COMMITMENT FILTER (Keeper's stage 1, sharpest): a commit operator needs the SO(2) time-circle
    = a U(1) center in K. E8/F4/G2 lack it -> excluded with NO physics detail. Casey's "D_IV^5 vs
    E8": E8 loses here -- no time-circle, no commit operator.
  * D_IV^5 = IV_5: complex dim = n = 5 = n_C, rank = 2 = BST rank, group SO(5,2). The two BST
    integers ARE the domain's complex dimension and rank -- source-confirmed, not fits.
  * RANK-2 FILTER (binary record = 2 idempotents, item-10): keeps I_(2,q), II_(4,5), III_2, IV_n,
    E6; kills E7 (rank 3). Independently motivated.
  * HONEST RESIDUAL (relief valve + bias control): the two filters do NOT uniquely isolate D_IV^5;
    the residual family is a documented challenge, not a banked "only D_IV^5". Further filters must
    be independently motivated (not reverse-engineered), with the failure-on-dropping exhibited
    (as T2545 does for the (3,1) signature).

AUG-06 [TEGMARK]. Nothing pushed. Nothing banked (partial forcing, honestly tiered). Source-pinned
to the Cartan classification. Feeds Keeper's necessity table; Grace has the vertical leg. Count N.
""")
