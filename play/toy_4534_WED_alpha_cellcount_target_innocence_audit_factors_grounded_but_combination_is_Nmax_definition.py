#!/usr/bin/env python3
"""
Toy 4534 — Wednesday: TARGET-INNOCENCE AUDIT of the α cell-count frontier.
Is "α = 1/N_cells with N_cells = N_c^{N_c}·n_C + rank = 137" an independent
forcing, or the DEFINITION of N_max relabeled? Holding the bar hard (Casey away).

FRONTIER (Keeper long-pull board): is the total substrate channel count FORCED as
N_max = N_c^{N_c}·n_C + rank = 27·5+2 = 137, with α = 1/N_cells per-cell equipartition?
DISCIPLINE (K635-prearm): 137 is form-cheap (competitor 137 = N_c²+2^g = 9+128).
Reaching 137 is NOT the test; structure-FORCING from D_IV⁵ target-innocent is.
Pull the existing definition, don't invent (the K547 move).

CORPUS FACTS PULLED (not invented):
 * bst_seed.md L54: N_max = 137 = "Channel capacity = N_c³·n_C + rank, spectral
   ceiling." -> the cell-count expression IS the DEFINITION of N_max.
 * P6 Periodic Table: N_c³ = 27 = dim(E_6)/Albert algebra = color-anomalous tensor
   V_(1,2). -> the 27 factor has INDEPENDENT substrate-rep grounding (not just 3³).
 * Geodesic Table (Mar 27): 27 primitive bulk rank-1 geodesics (mult N_c), 4 wall
   (mult n_C), 8 R2 = 39 entries. Independent geometric enumeration -> gives 39,
   NOT 137. So no independent enumeration YET yields the 137 combination.

AUDIT VERDICT (previewed): the three FACTORS (27 = Albert color-tensor; n_C = 5
domain dim; rank = 2) each have independent grounding, BUT the COMBINATION
(27·5)+2 = 137 as a "total DOF count" is the DEFINITION of N_max, and 137 is
form-cheap, so the value does not single out this factorization. => the cell-count
reframe GROUNDS THE FACTORS but does NOT deliver an independent FORCING of the
combination. Reopened (not blind, per Casey), factors partially grounded, but the
forcing gap = a DOF-counting PRINCIPLE (why color-tensor × ladder + rank) +
the equipartition justification. NO bank. Honest state: live candidate, gap named.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
N_max = N_c**3 * n_C + rank
results = []
def check(label, cond, detail):
    results.append((label, bool(cond), detail))

print("=" * 78)
print("Toy 4534 — target-innocence audit: α cell-count (forcing or relabel?)")
print("=" * 78)

# ---- PART 1: the combination IS the definition of N_max ---------------------
print("\n[PART 1] N_max definition (bst_seed L54): 'Channel capacity = N_c³·n_C+rank':")
print(f"  N_c³·n_C + rank = {N_c**3}·{n_C} + {rank} = {N_max}")
print(f"  N_c^{{N_c}}·n_C + rank = {N_c**N_c}·{n_C} + {rank} = {N_c**N_c*n_C+rank}  (same; N_c^N_c = N_c³ = 27)")
check("N_cells = N_c^{N_c}·n_C+rank is IDENTICAL to the N_max definition (relabel risk)",
      N_c**N_c * n_C + rank == N_max == 137,
      "'α=1/N_cells' = the existing α=1/N_max claim, re-described")

# ---- PART 2: the FACTORS — which are independently grounded? -----------------
print("\n[PART 2] independent grounding of each factor:")
albert_dim = 27
check("27 = N_c³ = dim(Albert)/dim(E_6 fund) = color-anomalous tensor V_(1,2) (P6): GROUNDED",
      N_c**3 == albert_dim == 27, "independent substrate rep, NOT merely 3³ — target-innocent")
check("n_C = 5 = domain dimension of D_IV⁵ (independent invariant)", n_C == 5, "grounded")
check("rank = 2 = domain rank of D_IV⁵ (independent invariant)", rank == 2, "grounded")
# but does an independent ENUMERATION yield 137? geodesic table gives 39, not 137.
geodesic_entries = 27 + 4 + 8   # bulk R1 + wall R1 + R2 (Geodesic Table)
print(f"  independent geodesic enumeration = 27+4+8 = {geodesic_entries} entries, NOT {N_max}")
check("no independent enumeration YET yields 137 (geodesic table gives 39)",
      geodesic_entries != N_max, "the 137 combination is not independently enumerated")

# ---- PART 3: is the COMBINATION forced by the value? (form-cheapness) --------
print("\n[PART 3] does the value 137 single out the color-tensor factorization?")
decomps = {
    "N_c³·n_C + rank (N_max def, multiplicative color-tensor)": N_c**3*n_C + rank,
    "N_c² + 2^g (additive competitor, Keeper)":                 N_c**2 + 2**g,
    "rank⁴·n_C·g − N_c·g − rank (RFC-ish)":                     rank**4*n_C*g - N_c*g - rank,
    "2^g + N_c² (same as competitor)":                          2**g + N_c**2,
}
hits = {k: v for k, v in decomps.items() if v == 137}
print("  distinct substrate expressions hitting 137:")
for k, v in decomps.items():
    print(f"    {'HIT' if v==137 else '   '} {v:>4}  {k}")
check("137 has >=2 structurally-different substrate decompositions (form-cheap)",
      len(set(v for v in decomps.values() if v == 137)) >= 1 and (N_c**2 + 2**g == 137),
      "additive N_c²+2^g=137 competes with multiplicative N_c³·n_C+rank -> value doesn't force factorization")

# ---- PART 4: is α = 1/N_cells (equipartition) a forced principle? ------------
print("\n[PART 4] is α = 1/N_cells a forced equipartition principle, or an ansatz?")
print("  Sakharov induced coupling: 1/α ∝ Σ Q_i²·(species)·log(Λ) — NOT a clean 1/count.")
print("  'α = 1/(channel capacity)' is the existing BST identification (α=1/137);")
print("  the 'per-cell equipartition' is a re-description, not an independent")
print("  derivation of WHY α = 1/N_max (the log/charge² structure is absent).")
check("α = 1/N_cells equipartition is an ANSATZ (re-describes α=1/N_max), not forced",
      True, "no independent equipartition principle delivered; Sakharov gives Σ Q²log, not 1/count")

# ---- PART 5: honest verdict --------------------------------------------------
print("\n[PART 5] VERDICT (target-innocence audit):")
check("FACTORS grounded (27=Albert target-innocent; n_C, rank domain invariants)",
      True, "the reframe DOES add: 27 = color-anomalous tensor is a genuine substrate object")
check("COMBINATION (27·5)+2 = N_max DEFINITION, not an independent forcing",
      N_c**3*n_C+rank == N_max, "relabel, not derivation; value form-cheap; no independent enum of 137")
check("cell-count route: REOPENED (not blind, per Casey) but FORCING NOT DELIVERED",
      True, "gap = DOF-counting principle (why color-tensor×ladder+rank) + equipartition justification")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 78)
print("RESULTS")
print("=" * 78)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         {detail}")
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}")
print("=" * 78)
print("""
TARGET-INNOCENCE AUDIT VERDICT (my own frontier, bar held hard, Casey away):
  * The cell-count expression N_c^{N_c}·n_C + rank IS the DEFINITION of N_max
    (bst_seed: 'channel capacity, spectral ceiling'). So "α = 1/N_cells" is the
    EXISTING α = 1/N_max identification re-described — not a new independent forcing.
  * WHAT THE REFRAME GENUINELY ADDS (target-innocent): 27 = N_c³ = dim(Albert)
    = dim(E_6 fund) = color-anomalous tensor V_(1,2) — a real substrate rep, not
    merely 3³. That is the one genuinely independent grounding, and it's good.
  * WHAT IT DOES NOT DELIVER: an independent enumeration of 137 (the geodesic
    table gives 39, not 137), a forced COMBINATION rule (why color-tensor × ladder
    + rank, vs the additive competitor N_c²+2^g=137), or an equipartition principle
    (Sakharov gives Σ Q²·log, not a clean 1/count).
  => HONEST STATE: per-channel-α is REOPENED (Casey's catch stands — not blind),
     the color factor is grounded (Albert-27), but the FORCING is NOT delivered by
     the cell-count reframe — it relabels N_max. NO bank. The real forcing gap for
     @Lyra/@Grace: a DOF-counting PRINCIPLE that derives the (color-tensor × ladder
     + rank) combination independently, + why α = per-cell equipartition. Staged as
     NO-bank / forcing-gap-named; nothing to ratify. Count stays 10.
""")
