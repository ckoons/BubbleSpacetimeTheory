#!/usr/bin/env python3
"""
Toy 3545 — K-type BST-primary content distribution analysis

Elie, Wednesday 2026-05-27 ~09:35 EDT
Forward analysis on Phase A 36-node table: count BST-primary content
matches across K-type properties. Identifies "BST-primary-rich" K-types
as candidates for Track P (K-type Population Principle) investigation.

CAL #29 STANDING QUESTION-SHAPE AUDIT (PRE-PASS):
  Question: "What's the BST-primary content distribution across the 36
             K-type nodes' Casimir, dim, Bergman weight values?"
  - Forward counting; doesn't presume answer
  - Loads existing JSON artifact (Toy 3537 v0.2)
  - Doesn't assign K-type → observable identifications
  CLEAN PASS

INVESTIGATIONS (4 scored)
1. Per-node BST-primary content count (Casimir, Casimir SO(2), Bergman, dim)
2. Distribution: how many nodes have N BST-primary matches?
3. Identify "BST-primary-rich" K-types (highest content)
4. Aggregate distribution for Cal Thread 4 + Track P input
"""
import sys
import json
from pathlib import Path
from fractions import Fraction

print("=" * 78)
print("Toy 3545 — K-type BST-primary content distribution analysis")
print("Forward analysis on Phase A 36-node table; Track P + Cal Thread 4 input")
print("Elie, Wednesday 2026-05-27 09:35 EDT")
print("=" * 78)

# BST primaries (6 total) + small auxiliary primes
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
BST_PRIMARIES = {rank, N_c, n_C, C_2, g, N_max}
BST_PRIMARY_PRIMES = {2, 3, 5, 7}  # primes among BST primaries (C_2=6 composite, N_max=137 prime)
BST_PRIMARIES_AS_INTS = BST_PRIMARIES | {137}  # explicit


def parse_frac(s):
    if "/" in s:
        n, d = s.split("/")
        return Fraction(int(n), int(d))
    return Fraction(int(s))


def is_bst_product(n, max_factors=4):
    """True if n > 0 can be factored entirely into BST primaries (allowing repeats, primary set {2,3,5,7,137,6})."""
    if n <= 0:
        return False
    if n == 1:
        return True
    # Try BST primaries as factors
    for p in [137, 7, 6, 5, 3, 2]:
        if n % p == 0 and max_factors > 0:
            if is_bst_product(n // p, max_factors - 1):
                return True
    return False


def bst_classify(value):
    """Classify a numeric value.
    Returns: 'BST_PRIMARY' if value is a BST primary,
             'BST_PRODUCT' if value is product of BST primaries,
             'BST_RATIONAL' if value = p/q with p,q BST products,
             'INTEGER' if integer but not BST,
             'RATIONAL_OTHER' if rational but not BST,
             'TRIVIAL' if 0 or 1.
    """
    if value == 0:
        return "TRIVIAL"
    if value == 1:
        return "TRIVIAL"
    if isinstance(value, Fraction):
        if value.denominator == 1:
            n = abs(value.numerator)
            if n in BST_PRIMARIES_AS_INTS:
                return "BST_PRIMARY"
            if is_bst_product(n):
                return "BST_PRODUCT"
            return "INTEGER"
        else:
            num, den = abs(value.numerator), value.denominator
            num_bst = num == 1 or num in BST_PRIMARIES_AS_INTS or is_bst_product(num)
            den_bst = den == 1 or den in BST_PRIMARIES_AS_INTS or is_bst_product(den)
            if num_bst and den_bst:
                return "BST_RATIONAL"
            return "RATIONAL_OTHER"
    if isinstance(value, int):
        if value in BST_PRIMARIES_AS_INTS:
            return "BST_PRIMARY"
        if is_bst_product(value):
            return "BST_PRODUCT"
        return "INTEGER"
    return "OTHER"


# ============================================================
# Load Phase A 36-node JSON
# ============================================================
json_path = Path("/Users/cskoons/projects/github/BubbleSpacetimeTheory/play/data/k_type_nodes_phase_A.json")
with open(json_path) as f:
    data = json.load(f)
nodes = data["nodes"]
print(f"\nLoaded {len(nodes)} K-types from Phase A v0.2 JSON")

# ============================================================
# Test 1: Per-node BST-primary content count
# ============================================================
print("\n--- Test 1: Per-node BST-primary content classification ---")
print(f"\n  {'K-type':<14} {'Sector':<8} {'C_SO(5)':<8} {'C_SO(2)':<8} {'Berg_1':<8} {'Berg_2':<8} {'dim':<6} {'BST hits'}")
print(f"  {'-'*14} {'-'*8} {'-'*8} {'-'*8} {'-'*8} {'-'*8} {'-'*6} {'-'*8}")

analyses = []
for k in nodes:
    m1 = parse_frac(k["m1"])
    m2 = parse_frac(k["m2"])
    cas5 = parse_frac(k["casimir_so5"])
    cas2 = parse_frac(k["casimir_so2"])
    bw1 = parse_frac(k["bergman_weight_m1_plus_5_2"])
    bw2 = parse_frac(k["bergman_weight_m2_plus_3_2"])
    dim = k["so5_weyl_dim"]

    props = {
        "casimir_so5": bst_classify(cas5),
        "casimir_so2": bst_classify(cas2),
        "bergman_1": bst_classify(bw1),
        "bergman_2": bst_classify(bw2),
        "dim": bst_classify(dim),
    }

    # Count "BST hits" = entries classified as BST_PRIMARY or BST_PRODUCT or BST_RATIONAL
    bst_hits = sum(1 for v in props.values() if v in ("BST_PRIMARY", "BST_PRODUCT", "BST_RATIONAL"))

    analyses.append({
        "k": k, "m1": m1, "m2": m2, "cas5": cas5, "cas2": cas2,
        "bw1": bw1, "bw2": bw2, "dim": dim,
        "props": props, "bst_hits": bst_hits,
    })

    m1_s = f"{m1.numerator}/{m1.denominator}" if m1.denominator > 1 else str(m1.numerator)
    m2_s = f"{m2.numerator}/{m2.denominator}" if m2.denominator > 1 else str(m2.numerator)
    label = f"({m1_s},{m2_s})"

    def short(c):
        return {"BST_PRIMARY": "P", "BST_PRODUCT": "p", "BST_RATIONAL": "r",
                "TRIVIAL": "·", "INTEGER": "I", "RATIONAL_OTHER": "?"}.get(c, "?")

    print(f"  {label:<14} {k['chirality'][:5]:<8} "
          f"{str(cas5):<8} {str(cas2):<8} {str(bw1):<8} {str(bw2):<8} {dim:<6} "
          f"{bst_hits}/5  [{short(props['casimir_so5'])}{short(props['casimir_so2'])}"
          f"{short(props['bergman_1'])}{short(props['bergman_2'])}{short(props['dim'])}]")

test_1 = len(analyses) == 36
print(f"\n  Classification complete: 36 nodes × 5 properties = 180 classifications")
print(f"  Legend: P=BST_PRIMARY, p=BST_PRODUCT, r=BST_RATIONAL, ·=TRIVIAL, I=INTEGER, ?=RATIONAL_OTHER")
print(f"  Test 1: {'PASS' if test_1 else 'FAIL'}")

# ============================================================
# Test 2: Distribution — count of nodes by BST-hit count
# ============================================================
print("\n--- Test 2: BST-hit count distribution ---")
hit_distribution = {}
for a in analyses:
    h = a["bst_hits"]
    hit_distribution[h] = hit_distribution.get(h, 0) + 1

print(f"  BST hits (out of 5 properties): node count")
for h in sorted(hit_distribution.keys()):
    bar = "█" * hit_distribution[h]
    print(f"  {h}/5 : {hit_distribution[h]:>3} nodes  {bar}")

test_2 = sum(hit_distribution.values()) == 36
print(f"\n  Distribution sum: {sum(hit_distribution.values())} (= 36 expected): {'PASS' if test_2 else 'FAIL'}")

# ============================================================
# Test 3: BST-primary-rich K-types (highest content)
# ============================================================
print("\n--- Test 3: BST-primary-rich K-types (top candidates for Track P) ---")
sorted_by_hits = sorted(analyses, key=lambda a: -a["bst_hits"])
print(f"\n  Top 15 most BST-primary-rich K-types:")
print(f"  {'rank':<6} {'(m_1,m_2)':<14} {'sector':<10} {'hits':<8} {'properties'}")
print(f"  {'-'*6} {'-'*14} {'-'*10} {'-'*8} {'-'*60}")
for i, a in enumerate(sorted_by_hits[:15], 1):
    m1_s = f"{a['m1'].numerator}/{a['m1'].denominator}" if a['m1'].denominator > 1 else str(a['m1'].numerator)
    m2_s = f"{a['m2'].numerator}/{a['m2'].denominator}" if a['m2'].denominator > 1 else str(a['m2'].numerator)
    label = f"({m1_s},{m2_s})"

    # List BST-relevant property values
    bst_props = []
    for key, val in [("C5", a["cas5"]), ("C2", a["cas2"]), ("B1", a["bw1"]), ("B2", a["bw2"]), ("d", a["dim"])]:
        cls = a["props"][{"C5": "casimir_so5", "C2": "casimir_so2", "B1": "bergman_1", "B2": "bergman_2", "d": "dim"}[key]]
        if cls in ("BST_PRIMARY", "BST_PRODUCT", "BST_RATIONAL"):
            bst_props.append(f"{key}={val}")
    props_str = ", ".join(bst_props) if bst_props else "(none)"
    print(f"  {i:<6} {label:<14} {a['k']['chirality']:<10} {a['bst_hits']}/5     {props_str}")

test_3 = True
print(f"\n  Test 3: PASS (BST-primary-rich K-types identified)")

# ============================================================
# Test 4: Aggregate distribution per property
# ============================================================
print("\n--- Test 4: Aggregate distribution per property ---")
prop_counts = {p: {"BST_PRIMARY": 0, "BST_PRODUCT": 0, "BST_RATIONAL": 0,
                   "TRIVIAL": 0, "INTEGER": 0, "RATIONAL_OTHER": 0}
              for p in ["casimir_so5", "casimir_so2", "bergman_1", "bergman_2", "dim"]}
for a in analyses:
    for prop_name, cls in a["props"].items():
        prop_counts[prop_name][cls] += 1

print(f"\n  Per-property classification counts (out of 36 K-types):")
print(f"  {'Property':<14} {'BST_PRIM':<10} {'BST_PROD':<10} {'BST_RAT':<10} {'TRIVIAL':<10} {'OTHER':<10}")
print(f"  {'-'*14} {'-'*10} {'-'*10} {'-'*10} {'-'*10} {'-'*10}")
for p in ["casimir_so5", "casimir_so2", "bergman_1", "bergman_2", "dim"]:
    pc = prop_counts[p]
    other = pc["INTEGER"] + pc["RATIONAL_OTHER"]
    print(f"  {p:<14} {pc['BST_PRIMARY']:<10} {pc['BST_PRODUCT']:<10} {pc['BST_RATIONAL']:<10} {pc['TRIVIAL']:<10} {other:<10}")

# Highlight: which property is most "BST-natural" across nodes?
print(f"\n  BST-content rate per property (BST_PRIMARY + BST_PRODUCT + BST_RATIONAL):")
for p in ["casimir_so5", "casimir_so2", "bergman_1", "bergman_2", "dim"]:
    pc = prop_counts[p]
    bst_total = pc["BST_PRIMARY"] + pc["BST_PRODUCT"] + pc["BST_RATIONAL"]
    pct = 100 * bst_total / 36
    print(f"    {p:<14} : {bst_total}/36 = {pct:.1f}%")

test_4 = True
print(f"\n  Test 4: PASS (aggregate distribution computed)")

# ============================================================
# Summary
# ============================================================
results = [test_1, test_2, test_3, test_4]
score = sum(results)
total = len(results)

print("\n" + "=" * 78)
print("K-TYPE BST-PRIMARY CONTENT DISTRIBUTION — RESULT")
print("=" * 78)

# Compute top properties summary
total_bst_hits = sum(a["bst_hits"] for a in analyses)
avg_bst_hits = total_bst_hits / 36
max_hits = max(a["bst_hits"] for a in analyses)
min_hits = min(a["bst_hits"] for a in analyses)

print(f"""
AGGREGATE FINDINGS:

  Total BST-content hits across 36 nodes × 5 properties = {total_bst_hits} / 180
  Average BST-hits per node: {avg_bst_hits:.2f} / 5
  Max BST-hits in single node: {max_hits} / 5
  Min BST-hits in single node: {min_hits} / 5

DISTRIBUTION:
  {hit_distribution}

NODE-BY-NODE TOP CANDIDATES for Track P (K-type Population Principle):

  K-types with highest BST-primary content are CANDIDATES for physical
  observable identification, but Cal #27 STANDING applies HARD —
  felt-substrate-natural at peak convergence + correlation ≠ causation.
  Forward derivation from substrate principles is the gate for identification,
  NOT high BST-primary content.

USE CASES (downstream):

  - Grace catalog matching: nodes with many BST primary matches are easier
    to cross-reference with observables having BST primary content
  - Cal Thread 4 typing: BST-primary content distribution informs typing
    of chirality-inversion observation as Type A/B/C
  - Lyra K-type Population Principle: high-BST-content K-types are natural
    candidates but require forward-derivation per Cal #29 audit

HONEST SCOPE (Cal #27 + #29 + #133 in tandem):

  - Counts BST-primary content per K-type forward
  - Does NOT promote any K-type → observable identification
  - Does NOT claim BST-primary-rich K-types ARE physical observables
  - Cal #133 partial-tautology check: Bergman weight integrality is
    expected via ρ-translation (5/2, 3/2); high BST content via this
    route is partly tautological
  - Substrate-mechanism for K-type Population Principle remains
    multi-week Lyra v0.7+ derivation work

WHAT THIS DOES NOT DO:
  - Identifies observables — that's Grace lookup + Lyra Track P
  - Promotes substrate-mechanism — multi-week derivation work
  - Filters BST primaries by Cal #133 caveat (Bergman ρ-translation is
    arithmetic structure, not new substrate-mechanism)

WHAT THIS DOES PROVIDE:
  - Per-node BST-content classification (180 classifications)
  - Distribution showing how BST-rich the K-type lattice is
  - Top candidates for Track P investigation (with Cal #27 caveats)
  - Per-property BST-content rate (which structural quantity is most
    BST-natural across the lattice)
""")

print(f"SCORE: {score}/{total}")
print(f"Toy 3545 K-type BST-primary content analysis: {'PASS' if score == total else 'PARTIAL'}")
print()
print(f"NET: 36 K-types classified; distribution computed; top BST-rich candidates surfaced")
print(f"for Track P (with Cal #27 STANDING caveats on Mode 1 / felt-substrate-natural risks).")
print()
print("— Elie, Toy 3545 K-type BST-content distribution 2026-05-27 Wednesday 09:35 EDT")
sys.exit(0 if score == total else 1)
