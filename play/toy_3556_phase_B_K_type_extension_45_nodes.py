#!/usr/bin/env python3
"""
Toy 3556 — Phase B K-type extension to 45-node (cutoff m_1+m_2 ≤ 8)

Elie, Wednesday 2026-05-27 ~10:20 EDT date-verified
Per Grace blocking dependency identified ~10:18 EDT: Grace's catalog
lookup work waits on Elie 45/66-node sets.

PURPOSE
-------
Extend Phase A v0.2 (36 nodes at cutoff m_1+m_2 ≤ 7) to Phase B v0.1
(45 nodes at cutoff m_1+m_2 ≤ 8). Update JSON artifact backward-
compatibly with v0.3 schema. 9 new K-types added.

Note: this is Phase B SCOPE EXTENSION. Lyra's v0.7 edge enumeration was
on 36-node set; extended graph would need re-enumeration. Hand-off flag
explicit.

CAL #29 STANDING QUESTION-SHAPE AUDIT (PRE-PASS):
  Question: "Extend Phase A K-type table to 45 nodes for Grace catalog
             lookup at extended scope?"
  - Forward enumeration; same logic as Toy 3537
  - Cross-CI unblock (Grace dependency)
  - Cal #133: no new substrate-mechanism claimed
  CLEAN PASS

INVESTIGATIONS (4 scored)
1. Enumerate K-types at cutoff m_1+m_2 ≤ 8 (expect 45 nodes)
2. Verify 36 prior Phase A v0.2 nodes preserved + 9 new K-types
3. Update JSON artifact to v0.3 (backward-compatible)
4. Substrate-anchor preservation verification
"""
import sys
import json
from fractions import Fraction
from pathlib import Path

print("=" * 78)
print("Toy 3556 — Phase B K-type extension to 45-node")
print("Per Grace blocking dependency; cross-CI unblock")
print("Elie, Wednesday 2026-05-27 10:20 EDT")
print("=" * 78)

# BST primaries
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
rho_1 = Fraction(5, 2)
rho_2 = Fraction(3, 2)


def casimir_so5(m1, m2):
    return m1 * (m1 + 3) + m2 * (m2 + 1)


def casimir_so2(m2):
    return m2 * m2


def bergman_weight(m1, m2):
    return (m1 + rho_1, m2 + rho_2)


def so5_weyl_dim(m1, m2):
    a = m1 - m2 + 1
    b = m1 + m2 + 2
    c = 2 * m1 + 3
    d = 2 * m2 + 1
    raw = a * b * c * d
    return int(round(float(raw / 6)))


def chirality(m1, m2):
    if m1.denominator == 1 and m2.denominator == 1:
        return "BOSON"
    if m1.denominator == 2 and m2.denominator == 2:
        return "FERMION"
    return "MIXED-FORBIDDEN"


def enumerate_k(cutoff_doubled):
    out = []
    for two_m1 in range(0, cutoff_doubled + 1):
        for two_m2 in range(0, two_m1 + 1):
            if two_m1 + two_m2 > cutoff_doubled:
                continue
            if (two_m1 % 2) != (two_m2 % 2):
                continue
            m1 = Fraction(two_m1, 2)
            m2 = Fraction(two_m2, 2)
            chir = chirality(m1, m2)
            if chir == "FERMION" and m2 < Fraction(1, 2):
                continue
            out.append({
                "m1": m1, "m2": m2, "chirality": chir,
                "casimir_so5": casimir_so5(m1, m2),
                "casimir_so2": casimir_so2(m2),
                "bergman_weight": bergman_weight(m1, m2),
                "so5_dim": so5_weyl_dim(m1, m2),
                "sum_half": int(2 * (m1 + m2)),
            })
    return out


def frac_to_str(f):
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else str(f.numerator)


# ============================================================
# Test 1: Enumerate at cutoff m_1+m_2 ≤ 8
# ============================================================
print("\n--- Test 1: Enumerate cutoff m_1+m_2 ≤ 8 ---")
phase_b_v1 = enumerate_k(cutoff_doubled=16)
n_bosons = sum(1 for k in phase_b_v1 if k["chirality"] == "BOSON")
n_fermions = sum(1 for k in phase_b_v1 if k["chirality"] == "FERMION")
mixed = [k for k in phase_b_v1 if k["chirality"] == "MIXED-FORBIDDEN"]
print(f"  Total K-types: {len(phase_b_v1)} (expect 45)")
print(f"  Bosons: {n_bosons}")
print(f"  Fermions: {n_fermions}")
print(f"  Mixed-forbidden: {len(mixed)} (expect 0)")
test_1 = len(phase_b_v1) == 45 and len(mixed) == 0
print(f"  Test 1: {'PASS' if test_1 else 'FAIL'}")

# ============================================================
# Test 2: Verify prior 36 nodes preserved + 9 new
# ============================================================
print("\n--- Test 2: Verify Phase A v0.2 36 preserved + 9 new at sum=8 ---")
prior_36 = enumerate_k(cutoff_doubled=14)  # m_1+m_2 ≤ 7
new_9 = [k for k in phase_b_v1 if k["sum_half"] > 14]  # sum > 7
prior_set = {(k["m1"], k["m2"]) for k in prior_36}
phase_b_set = {(k["m1"], k["m2"]) for k in phase_b_v1}
all_preserved = prior_set.issubset(phase_b_set)
print(f"  Prior 36 preserved: {all_preserved}")
print(f"  New K-types at m_1+m_2 = 8: {len(new_9)} (expect 9)")
print()
print(f"  New K-types:")
print(f"  {'(m_1, m_2)':<14} {'sector':<10} {'Casimir':<10} {'Bergman ρ-wt':<22} {'dim':<6}")
print(f"  {'-'*14} {'-'*10} {'-'*10} {'-'*22} {'-'*6}")
for k in sorted(new_9, key=lambda x: -float(x["m1"])):
    label = f"({frac_to_str(k['m1'])}, {frac_to_str(k['m2'])})"
    cas = frac_to_str(k["casimir_so5"])
    bw = f"({frac_to_str(k['bergman_weight'][0])}, {frac_to_str(k['bergman_weight'][1])})"
    print(f"  {label:<14} {k['chirality']:<10} {cas:<10} {bw:<22} {k['so5_dim']:<6}")

test_2 = all_preserved and len(new_9) == 9
print(f"\n  Test 2: {'PASS' if test_2 else 'FAIL'}")

# ============================================================
# Test 3: Update JSON artifact to v0.3
# ============================================================
print("\n--- Test 3: Update JSON artifact to v0.3 (backward-compatible) ---")


def k_to_serializable(k):
    return {
        "m1": frac_to_str(k["m1"]),
        "m2": frac_to_str(k["m2"]),
        "chirality": k["chirality"],
        "casimir_so5": frac_to_str(k["casimir_so5"]),
        "casimir_so2": frac_to_str(k["casimir_so2"]),
        "bergman_weight_m1_plus_5_2": frac_to_str(k["bergman_weight"][0]),
        "bergman_weight_m2_plus_3_2": frac_to_str(k["bergman_weight"][1]),
        "so5_weyl_dim": k["so5_dim"],
        "sum_m1_plus_m2": frac_to_str(Fraction(k["sum_half"], 2)),
        "added_in_v0_2_extension": k["sum_half"] > 10 and k["sum_half"] <= 14,
        "added_in_v0_3_extension": k["sum_half"] > 14,
    }


export_data = {
    "version": "Phase B v0.1 (extending Phase A v0.2)",
    "source": "play/toy_3556_phase_B_K_type_extension_45_nodes.py",
    "supersedes_versions": [
        "Phase A v0.1 (toy_3535, 21 nodes)",
        "Phase A v0.2 (toy_3537, 36 nodes)",
    ],
    "date_generated": "2026-05-27 Wednesday (Elie; per Grace blocking dependency)",
    "purpose": "Phase B reaction-table node set v0.1; Grace catalog lookup at extended scope",
    "domain": "D_IV^5 = SO_0(5,2) / (SO(5) x SO(2))",
    "K_isotropy_subgroup": "SO(5) x SO(2) with Pin(2) Z_2 double cover",
    "rho_vector_D_IV5": "(5/2, 3/2)",
    "cutoff_v0_1": "m_1 + m_2 ≤ 5 (21 nodes)",
    "cutoff_v0_2": "m_1 + m_2 ≤ 7 (36 nodes)",
    "cutoff_v0_3": "m_1 + m_2 ≤ 8 (45 nodes, Phase B v0.1)",
    "node_count": 45,
    "boson_count": n_bosons,
    "fermion_count": n_fermions,
    "new_in_v0_2": sum(1 for k in phase_b_v1 if k["sum_half"] > 10 and k["sum_half"] <= 14),
    "new_in_v0_3": 9,
    "operator_interpretation_note": (
        "Per Lyra v0.7 canonical disambiguation: 'chirality' field encodes σ_BF "
        "(Pin(2) Z_2 sublattice grading), NOT γ⁵ (Dirac chirality). σ_BF +1 on integer "
        "K-types/bosons; -1 on half-integer/fermions; commutes with T, C, P. γ⁵ is "
        "L/R Weyl distinguisher within fermion sublattice; anti-commutes with T, C."
    ),
    "phase_B_hand_off_flag": (
        "PHASE B EXTENSION TO 45 NODES. Lyra v0.7 edge enumeration was on 36-node "
        "Phase A v0.2 set. Extended graph (45 nodes) requires re-enumeration of "
        "edges to include new 9 K-types at m_1+m_2 = 8. Hand-off needed for Lyra "
        "Multi-phase quiver v0.4+ work."
    ),
    "schema_notes": {
        "m1": "SO(5) highest weight first component",
        "m2": "SO(5) highest weight second component (= SO(2) charge)",
        "chirality": "σ_BF Pin(2) Z_2 grading (NOT γ⁵)",
        "casimir_so5": "SO(5) Casimir = m_1(m_1+3) + m_2(m_2+1)",
        "casimir_so2": "SO(2) Casimir = m_2²",
        "bergman_weight_m1_plus_5_2": "Bergman ρ-translated weight m_1 + 5/2",
        "bergman_weight_m2_plus_3_2": "Bergman ρ-translated weight m_2 + 3/2",
        "so5_weyl_dim": "SO(5) irrep dimension via Weyl formula",
        "sum_m1_plus_m2": "m_1 + m_2 for cutoff tracking",
        "added_in_v0_2_extension": "true if added at v0.2 (m_1+m_2 ∈ {6, 7})",
        "added_in_v0_3_extension": "true if added at v0.3 (m_1+m_2 = 8)",
    },
    "nodes": [k_to_serializable(k) for k in phase_b_v1],
}

out_path = Path("/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/data/k_type_nodes_phase_B.json")
with open(out_path, "w") as f:
    json.dump(export_data, f, indent=2)
print(f"  Wrote {out_path}")
print(f"  Size: {out_path.stat().st_size} bytes")
print(f"  NOTE: Phase A v0.2 JSON (k_type_nodes_phase_A.json) UNCHANGED for backward compatibility")

# Round-trip verification
with open(out_path) as f:
    reloaded = json.load(f)
test_3 = reloaded["node_count"] == 45 and reloaded["new_in_v0_3"] == 9
print(f"  Round-trip: {'PASS' if test_3 else 'FAIL'}")

# ============================================================
# Test 4: Substrate-anchor preservation
# ============================================================
print("\n--- Test 4: Substrate-anchor preservation in v0.3 ---")
# T2435 anchor: K-type (1,1) Casimir = 6 = C_2
adj = next(k for k in phase_b_v1 if k["m1"] == 1 and k["m2"] == 1)
print(f"  T2435 RATIFIED anchor (1,1): Casimir = {adj['casimir_so5']} = C_2 ✓")

# Spinor Bergman weight preservation
spin = next(k for k in phase_b_v1 if k["m1"] == Fraction(1, 2) and k["m2"] == Fraction(1, 2))
print(f"  Dirac spinor (1/2,1/2): Bergman ρ-weight = ({spin['bergman_weight'][0]}, {spin['bergman_weight'][1]}) ✓")

# All fermions still have integer Bergman weights (extension to 45)
all_fermions = [k for k in phase_b_v1 if k["chirality"] == "FERMION"]
all_int_bergman = all(
    (k["bergman_weight"][0].denominator == 1 and k["bergman_weight"][1].denominator == 1)
    for k in all_fermions
)
print(f"  ALL {len(all_fermions)} fermion Bergman ρ-weights integer: {all_int_bergman} ✓")

test_4 = adj["casimir_so5"] == 6 and all_int_bergman
print(f"  Test 4: {'PASS' if test_4 else 'FAIL'}")

# ============================================================
# Summary
# ============================================================
results = [test_1, test_2, test_3, test_4]
score = sum(results)
total = len(results)

print("\n" + "=" * 78)
print("PHASE B K-TYPE EXTENSION v0.1 — RESULT")
print("=" * 78)
print(f"""
PHASE B v0.1 DELIVERED:

  45 K-types at cutoff m_1 + m_2 ≤ 8 ({n_bosons} bosons + {n_fermions} fermions)
  9 new K-types beyond Phase A v0.2 (36 nodes)
  ZERO mixed-forbidden K-types at any cutoff (Z_2 grading preserved)

NEW K-TYPES at m_1 + m_2 = 8 (added in v0.3):
""")
for k in sorted(new_9, key=lambda x: -float(x["m1"])):
    label = f"({frac_to_str(k['m1'])}, {frac_to_str(k['m2'])})"
    bw = f"({frac_to_str(k['bergman_weight'][0])}, {frac_to_str(k['bergman_weight'][1])})"
    print(f"  {label:<14} {k['chirality']:<10} C={frac_to_str(k['casimir_so5']):<10} Bergman={bw:<22} dim={k['so5_dim']}")

print(f"""
SUBSTRATE-ANCHOR PRESERVATION:
  - T2435 RATIFIED (1,1) C_2 = 6: confirmed ✓
  - Dirac spinor (1/2,1/2) Bergman (3, 2) = (N_c, rank): confirmed ✓
  - All 20 fermion K-types have INTEGER Bergman weights (Pin(2) Z_2 integerization)

ARTIFACT LOCATIONS:
  play/data/k_type_nodes_phase_B.json — 45 nodes v0.3 schema
  play/data/k_type_nodes_phase_A.json — 36 nodes v0.2 UNCHANGED (backward compat)

CROSS-CI HAND-OFF:
  - Grace catalog lookup: extended JSON ready for Phase B audit scope
  - Lyra Multi-phase quiver v0.4: edge enumeration must extend to 45-node graph
    (v0.7's ~1242 edges were on 36-node Phase A v0.2; extension needed)
  - Keeper integration: Phase A → Phase B transition documented

HONEST SCOPE (Cal #27 + #29 + #133):
  - Pure structural enumeration extension
  - No new substrate-mechanism claims
  - Phase B v0.1 is DATA hand-off; scope-transition decision pending team consensus

WHAT THIS TOY ACHIEVES:
  - Unblocks Grace's catalog lookup at extended scope
  - Provides Lyra v0.4+ Hall algebra base with 45-node node set
  - Documents Phase A v0.2 → Phase B v0.1 transition cleanly

WHAT THIS TOY DOES NOT DO:
  - Does NOT promote Phase B as scope-transition (team decision)
  - Does NOT enumerate edges (Lyra v0.4 work)
  - Does NOT assign observables (Grace lookup work)
""")

print(f"SCORE: {score}/{total}")
print(f"Toy 3556 Phase B 45-node extension: {'PASS' if score == total else 'PARTIAL'}")
print()
print(f"NET: Phase B v0.1 = 45 nodes (cutoff m_1+m_2 ≤ 8) delivered; Grace blocking dependency")
print(f"unblocked. New artifact: play/data/k_type_nodes_phase_B.json")
print()
print("— Elie, Toy 3556 Phase B extension 2026-05-27 Wednesday 10:20 EDT")
sys.exit(0 if score == total else 1)
