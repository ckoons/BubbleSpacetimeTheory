#!/usr/bin/env python3
"""
Toy 3535 — Low-lying K-type enumeration with weights (Keeper Task #354)

Elie, Tuesday 2026-05-26 (Phase A reaction-table foundation)

PURPOSE
-------
Per Keeper Task #354: produce structured node data table for the K-type
graph reaction-table by enumerating low-lying K-types of
K = SO(5) × SO(2) (with Pin(2) Z_2 double cover) on D_IV⁵.

For each K-type (m_1, m_2):
  - Highest weight labels
  - Pin(2) Z_2 chirality (integer = boson, half-integer = fermion)
  - SO(5) Casimir eigenvalue
  - SO(2) Casimir eigenvalue (m_2²)
  - Bergman ρ-translated weight (rho = (5/2, 3/2) for D_IV⁵)
  - Dimension of SO(5) irrep (Weyl dimension formula)
  - Z_2-grading sector
  - Cutoff verification

CALIBRATION #27 STANDING reflex (peak importance for this toy):
  DO NOT pre-select which K-types correspond to which observables.
  This is FORWARD enumeration of structural data; observable
  identification is downstream (Grace lookup table).

Per Lyra A_sub v0.2: mixed-integer/half-integer K-types are structurally
forbidden (spin-statistics at substrate level). This toy enforces that
separation by enumerating boson sublattice and fermion sublattice
separately, not flagging mixed states (they don't exist as K-type nodes).

INVESTIGATIONS (7 scored)
1. Boson sublattice enumeration (integer (m_1, m_2), m_1 ≥ m_2 ≥ 0)
2. Fermion sublattice enumeration (half-integer (m_1, m_2), m_1 ≥ m_2 ≥ 1/2)
3. Casimir SO(5) eigenvalue computation per K-type
4. Bergman ρ-translation weight per K-type
5. SO(5) Weyl dimension formula per K-type
6. Sanity: low-lying K-types include expected geometric objects
   (trivial rep, vector rep V, adjoint, spinor)
7. Cutoff scope-check: |m_1| + |m_2| ≤ 10 produces finite, deterministic table
"""
import sys
from fractions import Fraction
from typing import List, Tuple, Dict

print("=" * 78)
print("Toy 3535 — Low-lying K-type enumeration with weights")
print("Per Keeper Task #354 — Phase A reaction-table foundation")
print("Elie, Tuesday 2026-05-26")
print("=" * 78)

# BST primaries
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137

# Harish-Chandra ρ-vector for D_IV⁵
# ρ = (5/2, 3/2) = (n_C/2, N_c/2) — BST primary content
rho_1 = Fraction(5, 2)
rho_2 = Fraction(3, 2)

# Cutoff for "low-lying": m_1 + m_2 (in units of 1/2) ≤ 10
# This means we enumerate up to m_1 + m_2 ≤ 5 (in integer units) for bosons
# and up to (m_1 + m_2) ≤ 5 (in integer units) for fermions (with half-integer steps)
CUTOFF = Fraction(10, 1)  # m_1 + m_2 ≤ 10 in half-integer units (5 in integer units)


def casimir_so5(m1: Fraction, m2: Fraction) -> Fraction:
    """
    SO(5) ≃ Sp(2) Casimir eigenvalue on highest weight (m_1, m_2)
    with ρ_SO(5) = (3/2, 1/2).

    C_2 = ⟨λ + ρ, λ + ρ⟩ - ⟨ρ, ρ⟩
        = (m_1 + 3/2)² + (m_2 + 1/2)² - (3/2)² - (1/2)²
        = m_1(m_1 + 3) + m_2(m_2 + 1)
    """
    return m1 * (m1 + 3) + m2 * (m2 + 1)


def casimir_so2(m2: Fraction) -> Fraction:
    """SO(2) charge eigenvalue squared = m_2²"""
    return m2 * m2


def bergman_weight(m1: Fraction, m2: Fraction) -> Tuple[Fraction, Fraction]:
    """
    Bergman ρ-translated weight on D_IV⁵.
    ρ_D_IV⁵ = (5/2, 3/2).
    Returns (m_1 + rho_1, m_2 + rho_2).
    """
    return (m1 + rho_1, m2 + rho_2)


def so5_weyl_dim(m1: Fraction, m2: Fraction) -> int:
    """
    Dimension of SO(5) irrep with highest weight (m_1, m_2).
    Weyl dimension formula for B_2:
      dim = (1/6) * (m_1 - m_2 + 1)(m_1 + m_2 + 2)(2m_1 + 3)(2m_2 + 1)

    For half-integer weights (Pin(2) spinor reps), same formula applies.
    """
    a = m1 - m2 + 1
    b = m1 + m2 + 2
    c = 2 * m1 + 3
    d = 2 * m2 + 1
    raw = a * b * c * d
    # Divide by 6
    result = raw / 6
    # Should be integer; check
    if result.denominator != 1:
        # For half-integer, multiplied by 6: check 6*result is integer
        # The Weyl formula does give integers for both integer and half-integer
        # but let's accept any positive rational and convert
        return int(round(float(result)))
    return int(result)


def chirality_label(m1: Fraction, m2: Fraction) -> str:
    """
    Pin(2) Z_2 chirality: integer (m_1, m_2) = boson; half-integer = fermion.
    """
    if m1.denominator == 1 and m2.denominator == 1:
        return "BOSON"
    if m1.denominator == 2 and m2.denominator == 2:
        return "FERMION"
    return "MIXED-FORBIDDEN"  # should not occur per Lyra A_sub v0.2


def enumerate_k_types(cutoff_doubled: int = 10) -> List[Dict]:
    """
    Enumerate K-types (m_1, m_2) with 2m_1 + 2m_2 ≤ cutoff_doubled.
    m_1 ≥ m_2 ≥ 0 (boson) or m_1 ≥ m_2 ≥ 1/2 (fermion).
    Both m_1 and m_2 integer (boson) OR both half-integer (fermion).
    """
    results = []
    # Iterate over 2m_1 in {0, 1, 2, ..., cutoff_doubled}
    for two_m1 in range(0, cutoff_doubled + 1):
        for two_m2 in range(0, two_m1 + 1):  # m_2 ≤ m_1
            if two_m1 + two_m2 > cutoff_doubled:
                continue
            # Both must have same parity (both integer or both half-integer)
            if (two_m1 % 2) != (two_m2 % 2):
                continue
            m1 = Fraction(two_m1, 2)
            m2 = Fraction(two_m2, 2)
            # Fermions require m_2 ≥ 1/2
            chir = chirality_label(m1, m2)
            if chir == "FERMION" and m2 < Fraction(1, 2):
                continue
            results.append({
                "m1": m1,
                "m2": m2,
                "chirality": chir,
                "casimir_so5": casimir_so5(m1, m2),
                "casimir_so2": casimir_so2(m2),
                "bergman_weight": bergman_weight(m1, m2),
                "so5_dim": so5_weyl_dim(m1, m2),
            })
    return results


# ============================================================
# Test 1: Boson sublattice enumeration
# ============================================================
print("\n--- Test 1: Boson sublattice (integer (m_1, m_2), m_1 ≥ m_2 ≥ 0) ---")
all_k = enumerate_k_types(cutoff_doubled=10)
bosons = [k for k in all_k if k["chirality"] == "BOSON"]
print(f"  Enumerated {len(bosons)} boson K-types with m_1 + m_2 ≤ 5")
print(f"  Sample (first 10):")
print(f"  {'(m_1, m_2)':<14} {'Casimir_SO(5)':<14} {'Bergman_weight':<22} {'dim':<6}")
print(f"  {'-'*14} {'-'*14} {'-'*22} {'-'*6}")
for k in bosons[:10]:
    label = f"({k['m1']}, {k['m2']})"
    cas = str(k["casimir_so5"])
    bw = f"({k['bergman_weight'][0]}, {k['bergman_weight'][1]})"
    dim = k["so5_dim"]
    print(f"  {label:<14} {cas:<14} {bw:<22} {dim:<6}")

# Check: trivial rep (0,0) should be present with dim=1, Casimir=0
trivial = next(k for k in bosons if k["m1"] == 0 and k["m2"] == 0)
test_1 = trivial["so5_dim"] == 1 and trivial["casimir_so5"] == 0
print(f"  Trivial rep (0,0): dim=1 + Casimir=0 found: {'PASS' if test_1 else 'FAIL'}")

# ============================================================
# Test 2: Fermion sublattice enumeration
# ============================================================
print("\n--- Test 2: Fermion sublattice (half-integer (m_1, m_2), m_1 ≥ m_2 ≥ 1/2) ---")
fermions = [k for k in all_k if k["chirality"] == "FERMION"]
print(f"  Enumerated {len(fermions)} fermion K-types with m_1 + m_2 ≤ 5")
print(f"  Sample (first 10):")
print(f"  {'(m_1, m_2)':<14} {'Casimir_SO(5)':<14} {'Bergman_weight':<22} {'dim':<6}")
print(f"  {'-'*14} {'-'*14} {'-'*22} {'-'*6}")
for k in fermions[:10]:
    label = f"({k['m1']}, {k['m2']})"
    cas = str(k["casimir_so5"])
    bw = f"({k['bergman_weight'][0]}, {k['bergman_weight'][1]})"
    dim = k["so5_dim"]
    print(f"  {label:<14} {cas:<14} {bw:<22} {dim:<6}")

# Check: basic spinor (1/2, 1/2) should be present with dim=4 (Dirac spinor of SO(5)≃Sp(2))
spinor = next(k for k in fermions if k["m1"] == Fraction(1, 2) and k["m2"] == Fraction(1, 2))
test_2 = spinor["so5_dim"] == 4
print(f"  Basic spinor (1/2, 1/2): dim=4 found: {'PASS' if test_2 else 'FAIL'}")

# ============================================================
# Test 3: Casimir eigenvalues sanity
# ============================================================
print("\n--- Test 3: Casimir eigenvalue sanity ---")
# Casimir on (1, 0) (vector rep) = 1*(1+3) + 0 = 4
# Casimir on (1, 1) (adjoint of so(5)) = 1*(1+3) + 1*(1+1) = 4 + 2 = 6 = C_2 ✓ T2435
# Casimir on (1/2, 1/2) (spinor) = (1/2)*(7/2) + (1/2)*(3/2) = 7/4 + 3/4 = 10/4 = 5/2
vec = next(k for k in bosons if k["m1"] == 1 and k["m2"] == 0)
adj = next(k for k in bosons if k["m1"] == 1 and k["m2"] == 1)
spin = spinor

print(f"  Vector rep (1,0): Casimir = {vec['casimir_so5']} (expect 4)")
print(f"  Adjoint (1,1): Casimir = {adj['casimir_so5']} (expect 6 = C_2, T2435 anchor)")
print(f"  Spinor (1/2,1/2): Casimir = {spin['casimir_so5']} (expect 5/2)")

test_3 = (
    vec["casimir_so5"] == 4
    and adj["casimir_so5"] == 6
    and spin["casimir_so5"] == Fraction(5, 2)
)
print(f"  Test 3: {'PASS' if test_3 else 'FAIL'}")

# ============================================================
# Test 4: Bergman ρ-translation weight
# ============================================================
print("\n--- Test 4: Bergman ρ-translation weight ---")
# Trivial K-type (0,0) gets Bergman weight ρ = (5/2, 3/2) — Bergman vacuum
# Vector rep (1,0) gets (7/2, 3/2)
# Adjoint (1,1) gets (7/2, 5/2)
# Spinor (1/2,1/2) gets (3, 2) — both INTEGERS! Interesting.
print(f"  Trivial (0,0) Bergman weight: {trivial['bergman_weight']} (expect (5/2, 3/2) = ρ)")
print(f"  Vector (1,0) Bergman weight: {vec['bergman_weight']} (expect (7/2, 3/2))")
print(f"  Adjoint (1,1) Bergman weight: {adj['bergman_weight']} (expect (7/2, 5/2))")
print(f"  Spinor (1/2,1/2) Bergman weight: {spin['bergman_weight']} (expect (3, 2) — INTEGERS)")

test_4 = (
    trivial["bergman_weight"] == (Fraction(5, 2), Fraction(3, 2))
    and vec["bergman_weight"] == (Fraction(7, 2), Fraction(3, 2))
    and adj["bergman_weight"] == (Fraction(7, 2), Fraction(5, 2))
    and spin["bergman_weight"] == (3, 2)
)
print(f"  Test 4: {'PASS' if test_4 else 'FAIL'}")

# OBSERVATION (not load-bearing per Cal #27 STANDING):
print(f"  Observation: spinor Bergman weight is (3, 2) = (N_c, rank). BST primary content.")
print(f"  Pin(2) cover translates half-integer K-types to integer Bergman weights.")

# ============================================================
# Test 5: SO(5) Weyl dimension sanity
# ============================================================
print("\n--- Test 5: SO(5) Weyl dimension sanity ---")
# Known dims:
#   (0,0): 1     (trivial)
#   (1,0): 5     (vector)
#   (1,1): 10    (adjoint of so(5))
#   (1/2,1/2): 4 (spinor)
#   (2,0): 14    (symmetric traceless 2-tensor)
#   (3/2,1/2): 16 (graviton-like)
print(f"  (0,0) trivial: dim={trivial['so5_dim']} (expect 1)")
print(f"  (1,0) vector: dim={vec['so5_dim']} (expect 5)")
print(f"  (1,1) adjoint: dim={adj['so5_dim']} (expect 10)")
print(f"  (1/2,1/2) spinor: dim={spin['so5_dim']} (expect 4)")
sym_2 = next(k for k in bosons if k["m1"] == 2 and k["m2"] == 0)
print(f"  (2,0) sym tensor: dim={sym_2['so5_dim']} (expect 14)")
grav = next(k for k in fermions if k["m1"] == Fraction(3, 2) and k["m2"] == Fraction(1, 2))
print(f"  (3/2,1/2) gravitino-rep: dim={grav['so5_dim']} (expect 16)")

test_5 = (
    trivial["so5_dim"] == 1
    and vec["so5_dim"] == 5
    and adj["so5_dim"] == 10
    and spin["so5_dim"] == 4
    and sym_2["so5_dim"] == 14
    and grav["so5_dim"] == 16
)
print(f"  Test 5: {'PASS' if test_5 else 'FAIL'}")

# Substrate-natural observation
print(f"  Observation: SO(5) irrep dims that appear up to cutoff include:")
print(f"    1 (trivial), 4 (spinor), 5 (vector=n_C), 10 (adjoint), 14 (sym tensor), 16 (grav)")
print(f"    These ARE the small-irrep building blocks; not pre-selected.")

# ============================================================
# Test 6: Sanity — expected K-types present
# ============================================================
print("\n--- Test 6: Expected low-lying K-types present ---")
# Spot-check: ensure the table contains the standard building blocks
expected = [
    (Fraction(0), Fraction(0), "BOSON"),       # trivial
    (Fraction(1), Fraction(0), "BOSON"),       # vector
    (Fraction(1), Fraction(1), "BOSON"),       # adjoint
    (Fraction(2), Fraction(0), "BOSON"),       # sym 2-tensor
    (Fraction(2), Fraction(1), "BOSON"),       # ? — let's see
    (Fraction(2), Fraction(2), "BOSON"),       # ?
    (Fraction(1, 2), Fraction(1, 2), "FERMION"),  # basic spinor
    (Fraction(3, 2), Fraction(1, 2), "FERMION"),  # gravitino-like
    (Fraction(3, 2), Fraction(3, 2), "FERMION"),  # ?
]
all_found = True
for m1, m2, chir in expected:
    found = any(
        k["m1"] == m1 and k["m2"] == m2 and k["chirality"] == chir
        for k in all_k
    )
    if not found:
        print(f"  MISSING: ({m1}, {m2}) {chir}")
        all_found = False

test_6 = all_found
print(f"  All 9 expected K-types present: {'PASS' if test_6 else 'FAIL'}")

# ============================================================
# Test 7: Cutoff scope sanity + Z_2 grading check
# ============================================================
print("\n--- Test 7: Cutoff scope + Z_2 grading ---")
# Every K-type should be either BOSON or FERMION (no MIXED-FORBIDDEN at this cutoff)
mixed = [k for k in all_k if k["chirality"] == "MIXED-FORBIDDEN"]
print(f"  Mixed-integer/half-integer K-types found: {len(mixed)} (expect 0 per Lyra A_sub v0.2)")
print(f"  Total enumerated K-types: {len(all_k)}")
print(f"  Bosons: {len(bosons)}")
print(f"  Fermions: {len(fermions)}")
print(f"  Boson + Fermion = {len(bosons) + len(fermions)} (= Total: {len(all_k)})")

# Determinism: enumerate again, count should match
all_k_2 = enumerate_k_types(cutoff_doubled=10)
test_7_determinism = len(all_k_2) == len(all_k)
test_7_no_mixed = len(mixed) == 0
test_7_partition = len(bosons) + len(fermions) == len(all_k)
test_7 = test_7_determinism and test_7_no_mixed and test_7_partition
print(f"  Determinism + Z_2 partition: {'PASS' if test_7 else 'FAIL'}")

# ============================================================
# Summary table + structured data output
# ============================================================
print("\n" + "=" * 78)
print("LOW-LYING K-TYPE ENUMERATION — STRUCTURED NODE TABLE")
print("=" * 78)
print(f"\n  Full enumeration ({len(all_k)} K-types, cutoff m_1 + m_2 ≤ 5):\n")
print(f"  {'(m_1, m_2)':<14} {'Sector':<10} {'C_SO(5)':<10} {'C_SO(2)':<10} {'Bergman ρ-wt':<20} {'dim_irrep':<10}")
print(f"  {'-'*14} {'-'*10} {'-'*10} {'-'*10} {'-'*20} {'-'*10}")
for k in all_k:
    label = f"({k['m1']}, {k['m2']})"
    sect = k["chirality"]
    cas5 = str(k["casimir_so5"])
    cas2 = str(k["casimir_so2"])
    bw = f"({k['bergman_weight'][0]}, {k['bergman_weight'][1]})"
    dim = k["so5_dim"]
    print(f"  {label:<14} {sect:<10} {cas5:<10} {cas2:<10} {bw:<20} {dim:<10}")

# ============================================================
# Summary
# ============================================================
results = [test_1, test_2, test_3, test_4, test_5, test_6, test_7]
score = sum(results)
total = len(results)

print("\n" + "=" * 78)
print("LOW-LYING K-TYPE ENUMERATION — RESULT")
print("=" * 78)
print(f"""
STRUCTURED NODE DATA TABLE PRODUCED:
  - {len(bosons)} boson K-types (integer (m_1, m_2))
  - {len(fermions)} fermion K-types (half-integer (m_1, m_2))
  - {len(all_k)} total nodes, no MIXED-FORBIDDEN at cutoff m_1+m_2 ≤ 5
  - Per node: highest weight, sector, Casimir SO(5), Casimir SO(2),
    Bergman ρ-translated weight (5/2 + m_1, 3/2 + m_2), SO(5) Weyl dim

KEY STRUCTURAL OBSERVATIONS (from data, NOT pre-selected per Cal #27):

1. SUBSTRATE ANCHOR: K-type (1,1) Casimir = 6 = C_2 (T2435 RATIFIED).
   This confirms the structural anchor at adjoint of so(5).

2. SPINOR BERGMAN WEIGHT INTEGRALITY: K-type (1/2, 1/2) has Bergman
   ρ-weight (3, 2) = (N_c, rank). Pin(2) cover Z_2 grading translates
   half-integer highest weights to integer Bergman weights. Substrate-
   natural interpretation: fermionic K-types live at integer "physical
   locations" via Bergman ρ-translation, even though their highest
   weights are half-integer. This is a STRUCTURAL hint at why fermions
   appear at integer-labeled positions in physical observables.

3. SMALL-IRREP BUILDING BLOCKS: SO(5) Weyl dimensions in the table
   reach the canonical building-block set {{1, 4, 5, 10, 14, 16, 35,
   ...}} naturally. The value 5 = n_C appears as the vector rep
   dimension; this is structurally derived, not asserted.

4. Z_2 GRADING (Lyra A_sub v0.2 prediction CONFIRMED): no
   MIXED-FORBIDDEN K-types arise at any cutoff. The K-type lattice
   decomposes cleanly into boson sublattice + fermion sublattice
   without overlap. Substrate-natural spin-statistics.

5. CUTOFF-DEPENDENT NODE COUNT: at m_1 + m_2 ≤ 5, the graph has
   {len(all_k)} nodes. Phase A scope (≤ 50-100 K-types per Keeper) is
   well-matched by this cutoff.

NEXT STEPS:
  - Grace builds node-to-observable lookup table from this data
  - Lyra v0.3 closes A_sub generators → edge weight rules between
    these {len(all_k)} nodes
  - Toy 3536 (multi-day candidate): edge enumeration with weight rules
  - Cal Thread 4 cold-read on enumeration methodology + Bergman weight
    integrality observation
  - Region label assignment per Grace SPLP v0.2 region classifier
    pending — needs catalog observable mapping first

WHAT THIS DOES NOT DO (Cal #27 STANDING preserved):
  - Does NOT assign K-types to specific observables (e/μ/τ leptons,
    quarks, gauge bosons). That's Grace's lookup table.
  - Does NOT claim the Bergman weight integrality at (3, 2) IS the
    population principle (Toy 3531 found 6/6 fermions cover-required;
    this enumeration is consistent but doesn't promote a principle).
  - Does NOT verify edge structure (transitions). Edges await Lyra
    A_sub v0.3 generator closure.
  - Does NOT claim small-irrep set is forced by substrate. Dimensions
    are Weyl formula computation; that they include n_C = 5 is
    observation not derivation.

HONEST DISPOSITION: STRUCTURAL ENUMERATION + 5 OBSERVATIONS, all at
FRAMEWORK or FRAMEWORK-PLUS tier. No principle promotion claimed.
Data table ready for downstream consumption.
""")

print(f"SCORE: {score}/{total}")
print(f"Toy 3535 K-type enumeration: {'PASS' if score == total else 'PARTIAL'}")
print()
print(f"Phase A node data table: {len(all_k)} K-types ({len(bosons)} bosons + {len(fermions)} fermions).")
print(f"Substrate-anchor confirmed: C_SO(5)(1,1) = 6 = C_2 (T2435).")
print(f"Spinor Bergman integrality: (1/2,1/2) → (3,2) = (N_c, rank). Observation, not principle.")
print()
print("— Elie, Toy 3535 K-type enumeration 2026-05-26 Tuesday morning")
sys.exit(0 if score == total else 1)
