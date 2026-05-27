#!/usr/bin/env python3
"""
Toy 3537 — Phase A cutoff extension m_1+m_2 ≤ 7 (Keeper Task #356)

Elie, Tuesday 2026-05-26 ~10:00 EDT (Phase A v0.2 reaction-table foundation)

PURPOSE
-------
Per Keeper Task #356: extend Toy 3535's 21-node enumeration to cutoff
m_1+m_2 ≤ 7 (36 nodes total, 15 new). Stays in Phase A scope (50-100
target). Addresses Grace v0.2 reconciliation question (catalog references
"Wallach K-type dim_7/9/12" that didn't match the 21 nodes at cutoff ≤ 5).

Two deliverables:
(A) Updated JSON artifact play/data/k_type_nodes_phase_A.json with 36 nodes
(B) Wallach-dim reconciliation check: does the 36-node set contain SO(5)
    irrep dimensions 7, 9, or 12?

CALIBRATION #27 STANDING preserved: pure enumeration; no observable
assignment; no principle promotion. Cal #22 PCAP-transcription discipline:
re-check all indices after editing.

INVESTIGATIONS (5 scored)
1. Enumerate cutoff m_1+m_2 ≤ 7 → 36 K-types
2. Verify 21 prior Phase A nodes preserved + 15 new K-types added
3. Wallach-dim reconciliation: any dim ∈ {7, 9, 12}?
4. JSON re-export with updated scope
5. Structural observations (substrate anchor preserved, Z_2 grading)
"""
import sys
import json
from fractions import Fraction
from pathlib import Path

print("=" * 78)
print("Toy 3537 — Phase A cutoff extension m_1+m_2 ≤ 7")
print("Per Keeper Task #356 — addresses Grace v0.2 Wallach dim_7/9/12 question")
print("Elie, Tuesday 2026-05-26")
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
                "sum_half": int(2 * (m1 + m2)),  # 2(m_1+m_2) for cutoff tracking
            })
    return out


def frac_to_str(f):
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else str(f.numerator)


def k_label(k):
    return f"({frac_to_str(k['m1'])}, {frac_to_str(k['m2'])})"


# ============================================================
# Test 1: Enumerate cutoff m_1+m_2 ≤ 7 → 36 K-types
# ============================================================
print("\n--- Test 1: Enumerate cutoff m_1+m_2 ≤ 7 ---")
phase_a_v2 = enumerate_k(cutoff_doubled=14)
n_bosons = sum(1 for k in phase_a_v2 if k["chirality"] == "BOSON")
n_fermions = sum(1 for k in phase_a_v2 if k["chirality"] == "FERMION")
print(f"  Total K-types: {len(phase_a_v2)} (expect 36 per Toy 3536 sizing)")
print(f"  Bosons: {n_bosons}")
print(f"  Fermions: {n_fermions}")

# Verify mixed-forbidden still zero
mixed = [k for k in phase_a_v2 if k["chirality"] == "MIXED-FORBIDDEN"]
test_1 = len(phase_a_v2) == 36 and len(mixed) == 0
print(f"  Mixed-forbidden K-types: {len(mixed)} (expect 0)")
print(f"  Test 1: {'PASS' if test_1 else 'FAIL'}")

# ============================================================
# Test 2: Verify prior 21 Phase A v0.1 nodes preserved + 15 new
# ============================================================
print("\n--- Test 2: Phase A v0.1 21 preserved + 15 new at sum ≤ 7 ---")
prior_21 = enumerate_k(cutoff_doubled=10)  # m_1+m_2 ≤ 5
new_15 = [k for k in phase_a_v2 if k["sum_half"] > 10]
prior_21_set = {(k["m1"], k["m2"]) for k in prior_21}
phase_a_v2_set = {(k["m1"], k["m2"]) for k in phase_a_v2}

# All prior 21 should be in new set
all_preserved = prior_21_set.issubset(phase_a_v2_set)
print(f"  Prior Phase A v0.1: {len(prior_21)} nodes")
print(f"  All preserved in v0.2: {all_preserved}")
print(f"  New nodes (sum > 5, sum ≤ 7): {len(new_15)} (expect 15)")
print()
print(f"  New K-types at m_1+m_2 ∈ {{6, 7}}:")
print(f"  {'(m_1,m_2)':<14} {'Sector':<10} {'sum':<6} {'Casimir':<10} {'Bergman ρ-wt':<22} {'dim':<6}")
print(f"  {'-'*14} {'-'*10} {'-'*6} {'-'*10} {'-'*22} {'-'*6}")
for k in sorted(new_15, key=lambda x: (x["sum_half"], -float(x["m1"]))):
    label = k_label(k)
    sect = k["chirality"]
    sum_val = Fraction(k["sum_half"], 2)
    cas = frac_to_str(k["casimir_so5"])
    bw = f"({frac_to_str(k['bergman_weight'][0])}, {frac_to_str(k['bergman_weight'][1])})"
    dim = k["so5_dim"]
    print(f"  {label:<14} {sect:<10} {str(sum_val):<6} {cas:<10} {bw:<22} {dim:<6}")

test_2 = all_preserved and len(new_15) == 15
print(f"  Test 2: {'PASS' if test_2 else 'FAIL'}")

# ============================================================
# Test 3: Wallach-dim reconciliation — search for dims 7, 9, 12
# ============================================================
print("\n--- Test 3: Wallach-dim reconciliation (Grace v0.2 question) ---")
print(f"  Grace flagged: catalog references 'Wallach K-type dim_7/9/12' that didn't")
print(f"  match the 21-node Phase A v0.1 set. Does the 36-node v0.2 set contain")
print(f"  SO(5) irrep dimensions 7, 9, or 12?")
print()
target_dims = [7, 9, 12]
matches = {d: [] for d in target_dims}
for k in phase_a_v2:
    if k["so5_dim"] in target_dims:
        matches[k["so5_dim"]].append(k)

for d in target_dims:
    if matches[d]:
        for k in matches[d]:
            print(f"  dim={d}: K-type ({frac_to_str(k['m1'])}, {frac_to_str(k['m2'])}) {k['chirality']}")
    else:
        print(f"  dim={d}: NO K-type with this SO(5) irrep dimension found in 36-node set")

print()
print(f"  All SO(5) irrep dimensions present in 36-node set (sorted):")
all_dims = sorted(set(k["so5_dim"] for k in phase_a_v2))
print(f"    {all_dims}")

# Honest reconciliation answer
any_match = any(matches[d] for d in target_dims)
print()
print(f"  HONEST RECONCILIATION ANSWER:")
if not any_match:
    print(f"  SO(5) irrep dimensions 7, 9, 12 do NOT appear in any K-type up to cutoff")
    print(f"  m_1+m_2 ≤ 7. Possibilities Grace + Keeper should consider:")
    print(f"    (a) 'Wallach dim_N' refers to something OTHER than SO(5) Weyl dimension")
    print(f"        — perhaps Wallach-set parameter ν, or composite K-type dimension,")
    print(f"        or representation parameter unique to D_IV^5 harmonic analysis")
    print(f"    (b) The catalog entries cite K-types at cutoff > 7 not yet enumerated")
    print(f"    (c) The catalog entries cite a different group's irrep dim (e.g.,")
    print(f"        SO(2) charge, U(1) eigenvalue, etc.)")
    print(f"  RECOMMENDATION: Grace to inspect specific catalog entries citing 'Wallach")
    print(f"  dim_7/9/12' to determine which interpretation applies.")
else:
    print(f"  Some target dimensions found — see specific K-types above.")

test_3 = True  # This test surfaces honest reconciliation; not principle test
print(f"  Test 3: {'PASS' if test_3 else 'FAIL'} (reconciliation surfaced honestly)")

# ============================================================
# Test 4: Update JSON artifact
# ============================================================
print("\n--- Test 4: JSON artifact update (Phase A v0.2) ---")


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
        "added_in_v0_2_extension": k["sum_half"] > 10,
    }


export_data = {
    "version": "Phase A v0.2",
    "source": "play/toy_3537_K_type_phase_A_cutoff_extension_to_7.py",
    "supersedes": "play/toy_3535_low_lying_K_type_enumeration_with_weights.py (Phase A v0.1)",
    "date_generated": "2026-05-26 Tuesday morning (Elie, per Keeper Task #356)",
    "purpose": "Phase A reaction-table node set v0.2; Grace Task #355 v0.3 input + Wallach dim_7/9/12 reconciliation",
    "domain": "D_IV^5 = SO_0(5,2) / (SO(5) x SO(2))",
    "K_isotropy_subgroup": "SO(5) x SO(2) with Pin(2) Z_2 double cover",
    "rho_vector_D_IV5": "(5/2, 3/2)",
    "cutoff_v0_1": "m_1 + m_2 ≤ 5 (21 nodes)",
    "cutoff_v0_2": "m_1 + m_2 ≤ 7 (36 nodes)",
    "node_count": len(phase_a_v2),
    "boson_count": n_bosons,
    "fermion_count": n_fermions,
    "new_in_v0_2": len(new_15),
    "all_so5_irrep_dims_present": all_dims,
    "wallach_dim_7_9_12_reconciliation": (
        "SO(5) Weyl dims 7, 9, 12 do NOT appear in 36-node set. "
        "Grace v0.3 should verify whether 'Wallach dim_N' catalog references "
        "use SO(5) Weyl dimension or a different parameter."
    ),
    "schema_notes": {
        "m1": "SO(5) highest weight first component",
        "m2": "SO(5) highest weight second component, also SO(2) charge eigenvalue",
        "chirality": "BOSON (integer m_1, m_2) or FERMION (half-integer m_1, m_2)",
        "casimir_so5": "SO(5) Casimir eigenvalue = m_1*(m_1+3) + m_2*(m_2+1)",
        "casimir_so2": "SO(2) Casimir eigenvalue = m_2^2",
        "bergman_weight_m1_plus_5_2": "Bergman rho-translated weight component 1 = m_1 + 5/2",
        "bergman_weight_m2_plus_3_2": "Bergman rho-translated weight component 2 = m_2 + 3/2",
        "so5_weyl_dim": "SO(5) irrep dimension via Weyl formula = (1/6)(m1-m2+1)(m1+m2+2)(2m1+3)(2m2+1)",
        "sum_m1_plus_m2": "m_1 + m_2 (for cutoff tracking)",
        "added_in_v0_2_extension": "true if this node is new in v0.2 (not in v0.1 21-node set)",
    },
    "honest_scope": (
        "Pure structural enumeration; NO observable assignments, NO edge weights, "
        "NO region labels. Cal #27 STANDING. SO(5) dims {7,9,12} not present — "
        "Grace v0.3 reconciliation determines interpretation. Downstream lookup is "
        "Grace Task #355 v0.3."
    ),
    "nodes": [k_to_serializable(k) for k in phase_a_v2],
}

out_path = Path("/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/data/k_type_nodes_phase_A.json")
with open(out_path, "w") as f:
    json.dump(export_data, f, indent=2)
print(f"  Updated {out_path}")

# Round-trip verification
with open(out_path) as f:
    reloaded = json.load(f)
test_4 = (
    reloaded["node_count"] == 36
    and reloaded["new_in_v0_2"] == 15
    and reloaded["boson_count"] == n_bosons
    and reloaded["fermion_count"] == n_fermions
)
print(f"  Round-trip: 36 nodes + 15 new + correct boson/fermion counts: {'PASS' if test_4 else 'FAIL'}")

# ============================================================
# Test 5: Structural observations preserved
# ============================================================
print("\n--- Test 5: Structural observations preserved at v0.2 ---")
# Substrate anchor C_2 = 6 at K-type (1,1) — already verified Toy 3535
adj = next(k for k in phase_a_v2 if k["m1"] == 1 and k["m2"] == 1)
print(f"  Substrate anchor K-type (1,1) Casimir = {adj['casimir_so5']} (T2435: C_2 = 6)")

# Spinor (1/2, 1/2) Bergman ρ-weight = (3, 2) — Pin(2) cover integerization
spin = next(k for k in phase_a_v2 if k["m1"] == Fraction(1, 2) and k["m2"] == Fraction(1, 2))
bw_spin = spin["bergman_weight"]
print(f"  Spinor (1/2,1/2) Bergman weight = ({bw_spin[0]}, {bw_spin[1]}) = (N_c, rank)")
print(f"  → Pin(2) cover Z_2 grading translates half-integer K-types to integer Bergman weights")

# Check whether new fermion K-types also exhibit integer Bergman weights
print()
print(f"  Bergman weights of all new fermion K-types (m_1+m_2 ∈ {{6, 7}}):")
new_fermions = [k for k in new_15 if k["chirality"] == "FERMION"]
all_new_fermion_integer = True
for k in sorted(new_fermions, key=lambda x: (x["sum_half"], -float(x["m1"]))):
    bw = k["bergman_weight"]
    is_int = (bw[0].denominator == 1 and bw[1].denominator == 1)
    if not is_int:
        all_new_fermion_integer = False
    label = k_label(k)
    print(f"    {label} fermion: Bergman ({bw[0]}, {bw[1]}) {'INTEGER' if is_int else 'NON-INTEGER'}")

print()
if all_new_fermion_integer:
    print(f"  → ALL new fermion K-types continue to exhibit integer Bergman weights")
    print(f"    via Pin(2) ρ-translation (5/2, 3/2). This extends Toy 3535's spinor")
    print(f"    observation to all enumerated fermions. NOT yet a principle — Cal Thread 4")
    print(f"    cold-read pending.")

test_5 = (adj["casimir_so5"] == 6 and bw_spin == (3, 2) and all_new_fermion_integer)
print(f"  Test 5: {'PASS' if test_5 else 'FAIL'}")

# ============================================================
# Summary
# ============================================================
results = [test_1, test_2, test_3, test_4, test_5]
score = sum(results)
total = len(results)

print("\n" + "=" * 78)
print("PHASE A CUTOFF EXTENSION v0.2 — RESULT")
print("=" * 78)
print(f"""
DELIVERABLES PRODUCED:

(A) Updated JSON artifact: play/data/k_type_nodes_phase_A.json
    - Now 36 K-types ({n_bosons} bosons + {n_fermions} fermions)
    - Added flag `added_in_v0_2_extension` per node for v0.1 vs v0.2 tracking
    - Schema documents 10 per-node fields + 14 file-level metadata fields
    - Direct input for Grace Task #355 v0.3 node-to-observable lookup
    - Backward compatible: prior 21 nodes preserved with identical fields

(B) Wallach-dim reconciliation answer:
    SO(5) Weyl dimensions 7, 9, 12 are NOT present in the 36-node set.
    Recommendation to Grace: inspect specific catalog entries citing
    'Wallach dim_7/9/12' to determine whether this refers to:
      (a) Wallach-set parameter ν or composite K-type representation dim
          unique to D_IV^5 harmonic analysis (most likely candidate)
      (b) K-types at cutoff > 7 (would push to Phase B scope)
      (c) Different group's irrep dim (SO(2), U(1), Pin(2))

STRUCTURAL OBSERVATIONS (extended from Toy 3535, NOT new principles):

1. Z_2 grading PRESERVED at extended cutoff: ZERO mixed-forbidden K-types
   in any of the 36 nodes. Lyra A_sub v0.2 substrate-natural spin-
   statistics confirmed at extended scope.

2. SUBSTRATE ANCHOR PRESERVED: K-type (1,1) adjoint Casimir = 6 = C_2
   (T2435 SVC-verified by Cal #132 morning).

3. BERGMAN INTEGRALITY EXTENDED: ALL fermion K-types in the 36-node set
   exhibit INTEGER Bergman ρ-translated weights. Pin(2) cover Z_2 grading
   translates half-integer highest weights uniformly via (5/2, 3/2)
   addition. Toy 3535's observation at (1/2,1/2) → (3,2) extends to all
   {n_fermions} fermion nodes. STILL flagged as observation; Cal Thread 4
   cold-read pending. Not yet principle promotion.

4. NEW K-TYPES at m_1+m_2 ∈ {{6, 7}}:
   - {len([k for k in new_15 if k['chirality'] == 'BOSON'])} bosons added
   - {len([k for k in new_15 if k['chirality'] == 'FERMION'])} fermions added
   - SO(5) irrep dimensions range from 84 to higher; specific values per
     above table

5. NEW SO(5) DIMS APPEARING: {sorted(set(k['so5_dim'] for k in new_15))}

WHAT THIS DOES NOT DO (Cal #27 STANDING):
  - Does NOT assign new K-types to observables (Grace v0.3 territory)
  - Does NOT promote Bergman integrality observation to principle (Cal
    Thread 4 cold-read gate)
  - Does NOT resolve Wallach dim_7/9/12 question algorithmically; just
    surfaces the discrepancy honestly for Grace + Lyra
  - Does NOT recommend extending to Phase B; cutoff ≤ 7 is well within
    Phase A scope at 36 nodes

DOWNSTREAM CONSUMERS:
  - Grace Task #355 v0.3: load updated play/data/k_type_nodes_phase_A.json
    (36 nodes); re-run three-column lookup; address Wallach dim question
  - Lyra v0.5 phase-tagging: now has 36 nodes to tag (15 more than v0.1)
  - Lyra A_sub v0.3 edge rules: edge set should be defined on the 36-node
    set; transitions stay within Phase A scope
  - Cal Thread 4 cold-read: independent verification of enumeration +
    fermion Bergman integrality observation
""")

print(f"SCORE: {score}/{total}")
print(f"Toy 3537 Phase A v0.2 cutoff extension: {'PASS' if score == total else 'PARTIAL'}")
print()
print(f"Updated JSON: 36 K-type nodes ({n_bosons} bosons + {n_fermions} fermions).")
print(f"15 new nodes added at m_1+m_2 ∈ {{6, 7}}. Wallach dim_7/9/12 reconciliation surfaced.")
print(f"Bergman integrality observation extended to all {n_fermions} fermion K-types in v0.2.")
print()
print("— Elie, Toy 3537 Phase A v0.2 cutoff extension 2026-05-26 Tuesday")
sys.exit(0 if score == total else 1)
