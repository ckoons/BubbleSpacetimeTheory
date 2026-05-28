#!/usr/bin/env python3
"""
Toy 3557 — Phase B v0.2 K-type extension to 66 nodes (cutoff m_1+m_2 ≤ 10)

Elie, Wednesday 2026-05-27 ~10:22 EDT date-verified
Extends Toy 3556 Phase B v0.1 (45 nodes) per Grace's full 66-node lookup
dependency.

CAL #29 STANDING (PRE-PASS): forward enumeration extension. No new
substrate-mechanism claims; pure data hand-off.

INVESTIGATIONS (4 scored)
1. Enumerate K-types at cutoff m_1+m_2 ≤ 10 (66 nodes expected)
2. Verify 45 Phase B v0.1 + 21 new at m_1+m_2 ∈ {9, 10}
3. Update JSON to v0.2 schema (66 nodes; backward-compatible)
4. Substrate-anchor preservation verification
"""
import sys
import json
from fractions import Fraction
from pathlib import Path

print("=" * 78)
print("Toy 3557 — Phase B v0.2 K-type extension to 66 nodes")
print("Per Grace 66-node lookup dependency")
print("Elie, Wednesday 2026-05-27 10:22 EDT")
print("=" * 78)

rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
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
    return int(round(float((a * b * c * d) / 6)))


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


def fs(f):
    return f"{f.numerator}/{f.denominator}" if f.denominator > 1 else str(f.numerator)


# Test 1
print("\n--- Test 1: Enumerate at cutoff m_1+m_2 ≤ 10 ---")
phase_b_v2 = enumerate_k(cutoff_doubled=20)
n_b = sum(1 for k in phase_b_v2 if k["chirality"] == "BOSON")
n_f = sum(1 for k in phase_b_v2 if k["chirality"] == "FERMION")
print(f"  Total: {len(phase_b_v2)} ({n_b} bosons + {n_f} fermions; expect 66)")
mixed = sum(1 for k in phase_b_v2 if k["chirality"] == "MIXED-FORBIDDEN")
print(f"  Mixed-forbidden: {mixed} (expect 0)")
test_1 = len(phase_b_v2) == 66 and mixed == 0
print(f"  Test 1: {'PASS' if test_1 else 'FAIL'}")

# Test 2
print("\n--- Test 2: Phase B v0.1 (45) preserved + 21 new ---")
prior_45 = enumerate_k(cutoff_doubled=16)
prior_set = {(k["m1"], k["m2"]) for k in prior_45}
phase_b_v2_set = {(k["m1"], k["m2"]) for k in phase_b_v2}
all_pres = prior_set.issubset(phase_b_v2_set)
new_21 = [k for k in phase_b_v2 if k["sum_half"] > 16]
print(f"  45 prior preserved: {all_pres}")
print(f"  New (m_1+m_2 ∈ {{9, 10}}): {len(new_21)} (expect 21)")
test_2 = all_pres and len(new_21) == 21
print(f"  Test 2: {'PASS' if test_2 else 'FAIL'}")

# Test 3
print("\n--- Test 3: Write Phase B v0.2 JSON ---")


def k_to_json(k):
    return {
        "m1": fs(k["m1"]),
        "m2": fs(k["m2"]),
        "chirality": k["chirality"],
        "casimir_so5": fs(k["casimir_so5"]),
        "casimir_so2": fs(k["casimir_so2"]),
        "bergman_weight_m1_plus_5_2": fs(k["bergman_weight"][0]),
        "bergman_weight_m2_plus_3_2": fs(k["bergman_weight"][1]),
        "so5_weyl_dim": k["so5_dim"],
        "sum_m1_plus_m2": fs(Fraction(k["sum_half"], 2)),
        "added_in_v0_2_extension": 10 < k["sum_half"] <= 14,
        "added_in_v0_3_extension": 14 < k["sum_half"] <= 16,
        "added_in_v0_4_extension": k["sum_half"] > 16,
    }


export = {
    "version": "Phase B v0.2 (cutoff m_1+m_2 ≤ 10, 66 nodes)",
    "source": "play/toy_3557_phase_B_v02_K_type_66_nodes.py",
    "supersedes": "Phase B v0.1 (toy_3556, 45 nodes)",
    "date_generated": "2026-05-27 Wednesday (Elie; per Grace 66-node dependency)",
    "purpose": "Phase B reaction-table extended scope v0.2; Grace catalog lookup at 66-node scope",
    "domain": "D_IV^5 = SO_0(5,2) / (SO(5) x SO(2))",
    "rho_vector_D_IV5": "(5/2, 3/2)",
    "cutoff_v0_1": "m_1 + m_2 ≤ 5 (21 nodes)",
    "cutoff_v0_2": "m_1 + m_2 ≤ 7 (36 nodes)",
    "cutoff_v0_3": "m_1 + m_2 ≤ 8 (45 nodes; Phase B v0.1)",
    "cutoff_v0_4": "m_1 + m_2 ≤ 10 (66 nodes; Phase B v0.2)",
    "node_count": 66,
    "boson_count": n_b,
    "fermion_count": n_f,
    "new_in_v0_4": 21,
    "operator_interpretation_note": (
        "'chirality' field encodes σ_BF (Pin(2) Z_2 grading) per Lyra v0.7 disambiguation."
    ),
    "phase_B_hand_off_flag": (
        "PHASE B v0.2 EXTENSION TO 66 NODES. Lyra v0.7 edge enumeration on 36-node "
        "Phase A v0.2; subsequent extensions (v0.3 45-node, v0.4 66-node) require "
        "edge re-enumeration. Hand-off coordination needed for Lyra Multi-phase "
        "quiver v0.4+ work."
    ),
    "schema_notes": {
        "m1": "SO(5) highest weight first component",
        "m2": "SO(5) highest weight second component (= SO(2) charge)",
        "chirality": "σ_BF Pin(2) Z_2 grading (NOT γ⁵)",
        "casimir_so5": "SO(5) Casimir = m_1(m_1+3) + m_2(m_2+1)",
        "casimir_so2": "SO(2) Casimir = m_2²",
        "bergman_weight_m1_plus_5_2": "Bergman ρ-translated m_1 + 5/2",
        "bergman_weight_m2_plus_3_2": "Bergman ρ-translated m_2 + 3/2",
        "so5_weyl_dim": "SO(5) irrep dimension via Weyl formula",
        "sum_m1_plus_m2": "m_1 + m_2 for cutoff tracking",
        "added_in_v0_2_extension": "added at v0.2 (m_1+m_2 ∈ {6, 7})",
        "added_in_v0_3_extension": "added at v0.3 (m_1+m_2 = 8)",
        "added_in_v0_4_extension": "added at v0.4 (m_1+m_2 ∈ {9, 10})",
    },
    "nodes": [k_to_json(k) for k in phase_b_v2],
}

out_path = Path("/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/data/k_type_nodes_phase_B.json")
with open(out_path, "w") as f:
    json.dump(export, f, indent=2)
print(f"  Wrote {out_path} ({out_path.stat().st_size} bytes; supersedes v0.1)")
with open(out_path) as f:
    reloaded = json.load(f)
test_3 = reloaded["node_count"] == 66
print(f"  Test 3: {'PASS' if test_3 else 'FAIL'}")

# Test 4
print("\n--- Test 4: Substrate-anchor preservation in v0.4 (66 nodes) ---")
adj = next(k for k in phase_b_v2 if k["m1"] == 1 and k["m2"] == 1)
print(f"  T2435 (1,1) C_2 = {adj['casimir_so5']} ✓")
ferms = [k for k in phase_b_v2 if k["chirality"] == "FERMION"]
all_int = all(k["bergman_weight"][0].denominator == 1 and k["bergman_weight"][1].denominator == 1 for k in ferms)
print(f"  All {len(ferms)} fermion Bergman ρ-weights integer: {all_int} ✓")
test_4 = adj["casimir_so5"] == 6 and all_int
print(f"  Test 4: {'PASS' if test_4 else 'FAIL'}")

# Summary
results = [test_1, test_2, test_3, test_4]
score = sum(results)
total = len(results)

print("\n" + "=" * 78)
print("PHASE B v0.2 (66 NODES) — RESULT")
print("=" * 78)
print(f"""
PHASE B v0.2 DELIVERED:
  66 K-types at cutoff m_1+m_2 ≤ 10 ({n_b} bosons + {n_f} fermions)
  21 new K-types beyond Phase B v0.1 (m_1+m_2 ∈ {{9, 10}})
  ZERO mixed-forbidden K-types
  All {len(ferms)} fermions have INTEGER Bergman ρ-weights (Pin(2) integerization preserved)

ARTIFACT:
  play/data/k_type_nodes_phase_B.json — 66 nodes v0.4 schema (supersedes v0.1 45-node)

CROSS-CI HAND-OFF COMPLETE for Grace:
  - 21 / 36 / 45 / 66 node tables all available
  - JSON backward-compatible across all versions via 'added_in_v0_x' flags
  - Grace catalog lookup unblocked at full 66-node scope

LYRA EDGE RE-ENUMERATION FLAG:
  Lyra v0.7 edges (~1242 on 36-node) need extension to:
  - 45-node graph (Phase B v0.1)
  - 66-node graph (Phase B v0.2)
  Coordination required for Lyra Multi-phase quiver v0.4+.

HONEST SCOPE: pure data extension; no new substrate-mechanism claims.
""")

print(f"SCORE: {score}/{total}")
print(f"Toy 3557 Phase B v0.2: {'PASS' if score == total else 'PARTIAL'}")
print()
print(f"NET: 66-node Phase B v0.2 delivered; Grace fully unblocked at maximum scope.")
print()
print("— Elie, Toy 3557 Phase B v0.2 2026-05-27 Wednesday 10:22 EDT")
sys.exit(0 if score == total else 1)
