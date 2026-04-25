#!/usr/bin/env python3
"""
Toy 1483 — Integer-Adjacency Conjecture Test
===============================================
Lyra's conjecture (T1448 session): All known BST corrections involve
numbers that are ±1, ±rank, or ±N_c from a BST product.

A "BST product" is any product of {rank, N_c, n_C, C_2, g, N_max}
and their powers. The conjecture says the correction denominators
(or key numbers in the corrected formula) are always "adjacent" to
a BST product in this sense.

This toy systematically tests every correction from the current session.

All from rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137

Tests:
 T1-T8: Each correction tested for adjacency
 T9: Hit rate
 T10: Pattern classification
"""

from fractions import Fraction
import math
from itertools import product as iter_product

print("=" * 72)
print("Toy 1483 -- Integer-Adjacency Conjecture Test")
print("=" * 72)

# BST integers
rank = 2
N_c = 3
n_C = 5
C_2 = 6
g = 7
N_max = 137

# Generate all "BST products" up to ~1000
# Products of powers of {rank, N_c, n_C, C_2, g} up to reasonable exponents
bst_atoms = {'rank': rank, 'N_c': N_c, 'n_C': n_C, 'C_2': C_2, 'g': g, 'N_max': N_max}

# Generate all products up to 1000
bst_products = set()
bst_product_labels = {}

# Single integers
for name, val in bst_atoms.items():
    bst_products.add(val)
    bst_product_labels[val] = name

# Powers
for name, val in bst_atoms.items():
    for p in range(2, 10):
        v = val**p
        if v <= 2000:
            bst_products.add(v)
            bst_product_labels[v] = f"{name}^{p}"

# Products of two
atoms = list(bst_atoms.items())
for i in range(len(atoms)):
    for j in range(i, len(atoms)):
        for pi in range(1, 6):
            for pj in range(1, 6):
                v = atoms[i][1]**pi * atoms[j][1]**pj
                if v <= 2000:
                    bst_products.add(v)
                    label = ""
                    if pi == 1:
                        label += atoms[i][0]
                    else:
                        label += f"{atoms[i][0]}^{pi}"
                    label += "·"
                    if pj == 1:
                        label += atoms[j][0]
                    else:
                        label += f"{atoms[j][0]}^{pj}"
                    if v not in bst_product_labels or len(label) < len(bst_product_labels[v]):
                        bst_product_labels[v] = label

# Products of three (common cases)
for i in range(len(atoms)):
    for j in range(i, len(atoms)):
        for k in range(j, len(atoms)):
            v = atoms[i][1] * atoms[j][1] * atoms[k][1]
            if v <= 2000:
                bst_products.add(v)
                label = f"{atoms[i][0]}·{atoms[j][0]}·{atoms[k][0]}"
                if v not in bst_product_labels or len(label) < len(bst_product_labels.get(v, label + "xxx")):
                    bst_product_labels[v] = label

print(f"\nGenerated {len(bst_products)} BST products up to 2000")

# Adjacency offsets
offsets = [0, 1, -1, rank, -rank, N_c, -N_c]
offset_labels = {0: "exact", 1: "+1", -1: "-1", rank: f"+rank", -rank: f"-rank", N_c: f"+N_c", -N_c: f"-N_c"}

def check_adjacency(n):
    """Check if n is adjacent to a BST product. Return (is_adjacent, product, offset)"""
    for off in offsets:
        target = n - off  # n = target + off, so target = n - off
        if target in bst_products:
            return True, target, off
    return False, None, None

# =====================================================================
# All corrections from this session, with the key integer that changed
# =====================================================================

corrections = [
    # (name, key_number, description)
    # Batch 1 (prior session): CKM, PMNS, glueball
    ("sinθ_C", 79, "80-1 = rank⁴·n_C - 1: vacuum subtraction"),
    ("Wolfenstein A", 11, "12-1 = rank·C₂ - 1: dressed Casimir"),
    ("PMNS cos²θ₁₃", 44, "45-1 = N_c²·n_C - 1"),
    ("PMNS sin²θ₁₂ num", 154, "155-1? or 2·77 = 2·g·11"),
    ("PMNS sin²θ₂₃ num", 23, "24-1 = rank³·N_c - 1"),
    ("Glueball 0++", 31, "2^n_C - 1 = Mersenne prime M₅"),

    # Batch 2 (Toy 1476): hadronic corrections
    ("BR(H→bb̄)", 43, "42+1 = C₂·g + 1"),
    ("M_max NS", 42, "C₂·g = 42: exact BST product"),
    ("m_φ/m_ρ", 61, "60+1 = rank·n_C·C₂ + 1"),
    ("Γ_W", 0, "QCD factor α_s/π — not integer correction"),

    # Batch 3 (Toy 1481): cosmology + particle
    ("BR(H→gg)", 59, "60-1 = rank·n_C·C₂ - 1"),
    ("m_b/m_c", 59, "60-1 = rank·n_C·C₂ - 1 (same!)"),

    # Keeper (Toy 1475)
    ("m_b/m_c Keeper", 33, "unclear — 33 = N_c·(2C₂-1)?"),
    ("Glueball 2++/0++", 23, "24-1 = rank³·N_c - 1"),
    ("m_φ/m_ρ Keeper", 19, "20-1 = rank²·n_C - 1"),

    # Ising corrections (prior session)
    ("Ising γ", 17, "18-1 = rank·N_c² - 1"),
    ("Ising β denom", 411, "N_c·N_max = exact BST product"),
    ("Charm m_c/m_s", 136, "137-1 = N_max - 1"),
    ("H₂O bond angle correction", 0, "arccos(-1/N_c) - n_C, not integer form"),
]

print("\n" + "=" * 72)
print("ADJACENCY TEST")
print("=" * 72)

score = 0
total_testable = 0
hits = 0

for name, key_num, description in corrections:
    if key_num == 0:
        print(f"\n  {name}: SKIP — not integer correction form")
        continue

    total_testable += 1
    is_adj, product, offset = check_adjacency(key_num)

    if is_adj:
        hits += 1
        off_label = offset_labels.get(offset, f"+{offset}")
        prod_label = bst_product_labels.get(product, str(product))
        print(f"\n  {name}: {key_num} = {product} {off_label}")
        print(f"    BST product: {prod_label} = {product}")
        print(f"    Offset: {off_label}")
        print(f"    [{description}]")
    else:
        print(f"\n  {name}: {key_num} — NOT ADJACENT")
        print(f"    [{description}]")
        # Check what it IS near
        for off in range(-5, 6):
            if (key_num - off) in bst_products:
                print(f"    Near: {key_num - off} + {off} (offset {off})")

# =====================================================================
# Special cases: check the numbers more carefully
# =====================================================================
print("\n" + "=" * 72)
print("DETAILED ANALYSIS")
print("=" * 72)

# Check 154 (PMNS sin²θ₁₂ numerator)
print("\n  154 analysis:")
print(f"    154 = 2 × 77 = 2 × g × 11 = rank × g × (2C₂-1)")
print(f"    154 = 155 - 1 = (N_c·n_C·(2C₂-1)+rank) - 1 ?")
print(f"    155 = 5 × 31 = n_C × M₅")
print(f"    So 154 = n_C × M₅ - 1 = n_C × (2^n_C - 1) - 1")
adj_154, p_154, o_154 = check_adjacency(154)
print(f"    Adjacent? {adj_154}")
if adj_154:
    print(f"    = {p_154} {offset_labels.get(o_154, str(o_154))}")

# Check 33 (Keeper's m_b/m_c)
print("\n  33 analysis:")
print(f"    33 = 3 × 11 = N_c × (2C₂-1)")
adj_33, p_33, o_33 = check_adjacency(33)
print(f"    Adjacent? {adj_33}")
if adj_33:
    print(f"    = {p_33} {offset_labels.get(o_33, str(o_33))}")
else:
    # 33 = 30 + 3 = n_C·C₂ + N_c
    print(f"    33 = n_C·C₂ + N_c = 30 + 3: product 30 + N_c")
    print(f"    Or: 33 = 35 - 2 = n_C·g - rank: product 35 - rank")
    # Check if 30 is BST product
    print(f"    30 in BST products? {30 in bst_products} ({bst_product_labels.get(30, 'N/A')})")
    print(f"    35 in BST products? {35 in bst_products} ({bst_product_labels.get(35, 'N/A')})")

# Check 31 (Mersenne)
print("\n  31 analysis:")
print(f"    31 = 2^5 - 1 = rank^n_C - 1: Mersenne prime M₅")
adj_31, p_31, o_31 = check_adjacency(31)
print(f"    Adjacent? {adj_31}")
if adj_31:
    print(f"    = {p_31} {offset_labels.get(o_31, str(o_31))}")

# =====================================================================
# RESULTS
# =====================================================================
print("\n" + "=" * 72)
print("RESULTS")
print("=" * 72)

hit_rate = hits / total_testable * 100 if total_testable > 0 else 0
print(f"\n  Testable corrections: {total_testable}")
print(f"  Adjacent to BST product: {hits}")
print(f"  Hit rate: {hit_rate:.1f}%")

# Classify offsets
offset_counts = {0: 0, 1: 0, -1: 0, rank: 0, -rank: 0, N_c: 0, -N_c: 0}
for name, key_num, desc in corrections:
    if key_num == 0:
        continue
    is_adj, product, offset = check_adjacency(key_num)
    if is_adj and offset in offset_counts:
        offset_counts[offset] += 1

print(f"\n  Offset distribution:")
for off, count in sorted(offset_counts.items()):
    if count > 0:
        print(f"    {offset_labels.get(off, str(off))}: {count}")

# Scoring
results = []

# T1-T8: individual corrections
test_names = ["sinθ_C (79=80-1)", "Wolfenstein A (11=12-1)", "PMNS θ₁₃ (44=45-1)",
              "Glueball (31=32-1)", "BR(H→bb̄) (43=42+1)", "BR(H→gg) (59=60-1)",
              "Ising γ (17=18-1)", "Charm (136=137-1)"]
test_nums = [79, 11, 44, 31, 43, 59, 17, 136]

for i, (tname, tnum) in enumerate(zip(test_names, test_nums)):
    is_adj, prod, off = check_adjacency(tnum)
    passed = is_adj
    if passed: score += 1
    results.append((f"T{i+1}", tname, passed))

# T9: Hit rate ≥ 80%
t9_pass = hit_rate >= 80
if t9_pass: score += 1
results.append(("T9", f"Hit rate {hit_rate:.0f}% ≥ 80%", t9_pass))

# T10: Pattern — most corrections are -1 (vacuum subtraction)
minus_1_count = sum(1 for name, key_num, desc in corrections
                    if key_num > 0 and check_adjacency(key_num)[2] == -1)
t10_pass = minus_1_count >= 5
if t10_pass: score += 1
results.append(("T10", f"Vacuum subtraction (-1) dominant: {minus_1_count} cases", t10_pass))

print(f"\n  Individual tests:")
for tag, desc, passed in results:
    print(f"  {'PASS' if passed else 'FAIL'} {tag}: {desc}")

print(f"\nSCORE: {score}/10")

# Formalize the conjecture
print(f"\n{'=' * 72}")
print("INTEGER-ADJACENCY CONJECTURE (formalized)")
print("=" * 72)
print(f"""
  Let P = {{products of rank^a · N_c^b · n_C^c · C_2^d · g^e : a,b,c,d,e ≥ 0}}.
  Let A = {{p + δ : p ∈ P, δ ∈ {{0, ±1, ±rank, ±N_c}}}}.

  CONJECTURE: Every BST correction denominator/numerator lies in A.

  EVIDENCE: {hits}/{total_testable} corrections tested ({hit_rate:.0f}%).
  DOMINANT MODE: -1 (vacuum subtraction, {minus_1_count} cases).
  PHYSICAL: The constant eigenmode (k=0) doesn't participate →
            N_max modes → N_max - 1 active modes.

  This is T1444 (Vacuum Subtraction Principle) generalized:
  corrections are always "one mode away" from a BST product.
""")

print(f"{'=' * 72}")
print(f"Toy 1483 -- SCORE: {score}/10")
print(f"{'=' * 72}")
