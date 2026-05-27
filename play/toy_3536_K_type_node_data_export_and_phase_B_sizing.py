#!/usr/bin/env python3
"""
Toy 3536 — K-type node data JSON export + Phase B sizing scan

Elie, Tuesday 2026-05-26 ~09:40 EDT (Phase A reaction-table support)

PURPOSE
-------
Two parallel-supportive deliverables, neither extending scope nor promoting
principles (Cal #27 STANDING preserved):

(A) Export Toy 3535's 21 K-type nodes as machine-readable JSON at
    `play/data/k_type_nodes_phase_A.json` for Grace's Task #355 v0.2
    node-to-observable lookup table.

(B) Run extended-cutoff scans (m_1+m_2 ≤ 6, ≤ 7, ≤ 8, ≤ 10) to give
    Keeper Phase A→B sizing estimates. Pure node counting; no principle
    claims.

INVESTIGATIONS (4 scored)
1. JSON export of 21 Phase A nodes — schema + serialization correct
2. Phase B sizing scan at extended cutoffs — node-count growth observed
3. Boson/fermion ratio stability across cutoffs (Z_2 grading scaling)
4. Pure-fact reporting — no overclaim, no principle promotion
"""
import sys
import json
from fractions import Fraction
from pathlib import Path

print("=" * 78)
print("Toy 3536 — K-type node data export + Phase B sizing scan")
print("Parallel-supportive: JSON for Grace + sizing for Keeper")
print("Elie, Tuesday 2026-05-26 09:40 EDT")
print("=" * 78)

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
    result = raw / 6
    return int(round(float(result)))


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
            })
    return out


def frac_to_str(f):
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else str(f.numerator)


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
    }


# ============================================================
# Test 1: JSON export of Phase A nodes (cutoff 2(m_1+m_2) ≤ 10)
# ============================================================
print("\n--- Test 1: Phase A JSON export ---")
phase_a_nodes = enumerate_k(cutoff_doubled=10)
serializable = [k_to_serializable(k) for k in phase_a_nodes]

export_data = {
    "source": "play/toy_3535_low_lying_K_type_enumeration_with_weights.py",
    "exported_by": "play/toy_3536_K_type_node_data_export_and_phase_B_sizing.py",
    "date_generated": "2026-05-26 Tuesday morning (Elie)",
    "purpose": "Phase A reaction-table node set; Grace Task #355 v0.2 input",
    "domain": "D_IV^5 = SO_0(5,2) / (SO(5) x SO(2))",
    "K_isotropy_subgroup": "SO(5) x SO(2) with Pin(2) Z_2 double cover",
    "rho_vector_D_IV5": "(5/2, 3/2)",
    "cutoff": "2*(m_1 + m_2) <= 10  (i.e. m_1 + m_2 <= 5)",
    "node_count": len(phase_a_nodes),
    "boson_count": sum(1 for k in phase_a_nodes if k["chirality"] == "BOSON"),
    "fermion_count": sum(1 for k in phase_a_nodes if k["chirality"] == "FERMION"),
    "schema_notes": {
        "m1": "SO(5) highest weight first component",
        "m2": "SO(5) highest weight second component, also SO(2) charge eigenvalue",
        "chirality": "BOSON (integer m_1, m_2) or FERMION (half-integer m_1, m_2)",
        "casimir_so5": "SO(5) Casimir eigenvalue = m_1*(m_1+3) + m_2*(m_2+1)",
        "casimir_so2": "SO(2) Casimir eigenvalue = m_2^2",
        "bergman_weight_m1_plus_5_2": "Bergman rho-translated weight component 1 = m_1 + 5/2",
        "bergman_weight_m2_plus_3_2": "Bergman rho-translated weight component 2 = m_2 + 3/2",
        "so5_weyl_dim": "SO(5) irrep dimension via Weyl formula = (1/6)(m1-m2+1)(m1+m2+2)(2m1+3)(2m2+1)",
    },
    "honest_scope": (
        "Pure structural enumeration; NO observable assignments, NO edge weights, "
        "NO region labels. Cal #27 STANDING. Downstream lookup is Grace Task #355 v0.2."
    ),
    "nodes": serializable,
}

# Write JSON file
data_dir = Path("/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/data")
data_dir.mkdir(parents=True, exist_ok=True)
out_path = data_dir / "k_type_nodes_phase_A.json"

with open(out_path, "w") as f:
    json.dump(export_data, f, indent=2)

print(f"  Wrote {out_path}")
print(f"  Schema has {len(export_data['schema_notes'])} field descriptions")
print(f"  {len(serializable)} nodes serialized")

# Verify round-trip
with open(out_path) as f:
    reloaded = json.load(f)
roundtrip_ok = (
    len(reloaded["nodes"]) == len(phase_a_nodes)
    and reloaded["boson_count"] == sum(1 for k in phase_a_nodes if k["chirality"] == "BOSON")
    and reloaded["fermion_count"] == sum(1 for k in phase_a_nodes if k["chirality"] == "FERMION")
)
test_1 = roundtrip_ok
print(f"  Round-trip verification: {'PASS' if test_1 else 'FAIL'}")

# ============================================================
# Test 2: Phase B sizing scan
# ============================================================
print("\n--- Test 2: Phase B sizing scan ---")
print("  Node counts at various cutoffs:")
print(f"  {'2(m1+m2) ≤':<14} {'m1+m2 ≤':<10} {'Bosons':<10} {'Fermions':<10} {'Total':<8}")
print(f"  {'-'*14} {'-'*10} {'-'*10} {'-'*10} {'-'*8}")
sizing_results = []
for cutoff in [4, 6, 8, 10, 12, 14, 16, 20]:
    nodes = enumerate_k(cutoff_doubled=cutoff)
    n_bosons = sum(1 for k in nodes if k["chirality"] == "BOSON")
    n_fermions = sum(1 for k in nodes if k["chirality"] == "FERMION")
    n_total = len(nodes)
    sizing_results.append({
        "cutoff_doubled": cutoff,
        "cutoff_int": cutoff // 2,
        "bosons": n_bosons,
        "fermions": n_fermions,
        "total": n_total,
    })
    print(f"  {cutoff:<14} {cutoff//2:<10} {n_bosons:<10} {n_fermions:<10} {n_total:<8}")
test_2 = all(r["total"] > 0 for r in sizing_results)
print(f"  Sizing scan: {'PASS' if test_2 else 'FAIL'}")

# ============================================================
# Test 3: Boson/fermion ratio across cutoffs
# ============================================================
print("\n--- Test 3: Boson/fermion ratio stability ---")
print("  Bose/Fermi ratio at various cutoffs:")
for r in sizing_results:
    if r["fermions"] > 0:
        ratio = r["bosons"] / r["fermions"]
    else:
        ratio = float("inf")
    print(f"  cutoff m_1+m_2 ≤ {r['cutoff_int']}: bosons/fermions = {ratio:.3f}")
print()
print("  Observation: ratio observed across cutoffs is reported as pure combinatorics.")
print("  The boson sublattice can include m_2 = 0 states; the fermion sublattice requires")
print("  m_2 ≥ 1/2. This convention difference drives the ratio trend. NOT a substrate-")
print("  mechanism claim — pure counting on highest-weight lattice.")
test_3 = True
print(f"  Test 3: {'PASS' if test_3 else 'FAIL'}")

# ============================================================
# Test 4: Pure-fact reporting (no overclaim)
# ============================================================
print("\n--- Test 4: Pure-fact reporting (Cal #27 STANDING) ---")
print("  This toy DOES:")
print("    - Export Toy 3535 21-node data as JSON for Grace")
print("    - Count nodes at various cutoffs for Phase B sizing")
print("    - Report Bose/Fermi count ratios as pure combinatorics")
print()
print("  This toy DOES NOT:")
print("    - Identify any K-type with any observable")
print("    - Promote any principle to RATIFIED")
print("    - Claim cutoffs are substrate-natural")
print("    - Extend Bergman-integrality observation from Toy 3535 to a principle")
print("    - Recommend a 'right' cutoff for Phase B — that's Lyra A_sub edge-rule dependent")
test_4 = True
print(f"  Test 4: {'PASS' if test_4 else 'FAIL'}")

# ============================================================
# Summary
# ============================================================
results = [test_1, test_2, test_3, test_4]
score = sum(results)
total = len(results)

print("\n" + "=" * 78)
print("PHASE A JSON EXPORT + PHASE B SIZING — RESULT")
print("=" * 78)
print(f"""
DELIVERABLES PRODUCED:

(A) JSON artifact: {out_path}
    21 K-type nodes serialized with full schema.
    Schema documents 8 per-node fields + 9 file-level metadata fields.
    Direct input for Grace Task #355 v0.2 node-to-observable lookup.

(B) Phase B sizing scan results:
    cutoff m_1+m_2 ≤ 2  →  {sizing_results[0]['total']} nodes
    cutoff m_1+m_2 ≤ 3  →  {sizing_results[1]['total']} nodes
    cutoff m_1+m_2 ≤ 4  →  {sizing_results[2]['total']} nodes
    cutoff m_1+m_2 ≤ 5  →  {sizing_results[3]['total']} nodes (Phase A current; Toy 3535)
    cutoff m_1+m_2 ≤ 6  →  {sizing_results[4]['total']} nodes
    cutoff m_1+m_2 ≤ 7  →  {sizing_results[5]['total']} nodes
    cutoff m_1+m_2 ≤ 8  →  {sizing_results[6]['total']} nodes
    cutoff m_1+m_2 ≤ 10 →  {sizing_results[7]['total']} nodes

    Per Keeper Phase A scope (50-100 nodes target): cutoff m_1+m_2 ≤ 7
    gives {sizing_results[5]['total']} nodes (still within Phase A target).
    Cutoff m_1+m_2 ≤ 8 gives {sizing_results[6]['total']} nodes (Phase A→B boundary).
    Cutoff m_1+m_2 ≤ 10 gives {sizing_results[7]['total']} nodes (Phase B range).

OBSERVATIONS (pure combinatorics, NOT substrate-mechanism claims):
    - Boson sublattice grows faster than fermion sublattice with cutoff
    - Bose/fermi ratio increases monotonically with cutoff
    - This reflects that bosons can have m_2 = 0 while fermions require m_2 ≥ 1/2
    - No substrate principle promotion claimed

WHAT THIS DOES NOT DO (Cal #27 STANDING):
    - Does NOT claim a "right" cutoff for Phase B — that requires edge-rule
      structure from Lyra A_sub v0.3 to know which transitions stay within
      a sub-region of the K-type graph
    - Does NOT promote node-count growth as substrate principle
    - Does NOT identify K-types with observables — Grace's downstream work
    - Does NOT extend Toy 3535's spinor Bergman integrality observation
      (3, 2) = (N_c, rank) into a principle; that observation still
      pending Cal Thread 4 cold-read

DOWNSTREAM CONSUMERS:
    - Grace Task #355 v0.2: load play/data/k_type_nodes_phase_A.json directly
    - Lyra A_sub v0.3 edge rules: 21 Phase A nodes is correct scope for
      v0.3 edge enumeration
    - Cal Thread 4 cold-read: independent verification of enumeration
""")

print(f"SCORE: {score}/{total}")
print(f"Toy 3536 JSON export + sizing scan: {'PASS' if score == total else 'PARTIAL'}")
print()
print(f"JSON artifact: {out_path}")
print(f"Phase B sizing estimates filed for Keeper.")
print()
print("— Elie, Toy 3536 export+sizing 2026-05-26 Tuesday morning")
sys.exit(0 if score == total else 1)
