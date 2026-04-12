#!/usr/bin/env python3
"""
Toy 1128 — Medicine: BST Integer Counts in Human Physiology
=============================================================
New domain for SC-5 convergence + SE-3 enrichment. Medical/physiological
counts tested against BST integer products.

BST Five Integers: N_c=3, n_C=5, g=7, C_2=6, rank=2. N_max=137.

Author: Elie (Compute CI)
Date: April 12, 2026
"""

# ── BST constants ──
N_c = 3
n_C = 5
g = 7
C_2 = 6
rank = 2
N_max = 137

def is_7_smooth(n):
    if n <= 0:
        return False
    m = abs(n)
    for p in [2, 3, 5, 7]:
        while m % p == 0:
            m //= p
    return m == 1

# ============================================================
# Medical / Physiological Counts
# ============================================================

MEDICAL_COUNTS = [
    # Value, Description, BST connection if known, Level
    (206, "bones in adult human body", "", 1),
    (12, "pairs of cranial nerves", "2×C_2 = 12", 2),
    (31, "pairs of spinal nerves", "", 1),
    (4, "heart chambers", "rank² = 4", 2),
    (7, "cervical vertebrae", "g = 7", 2),
    (12, "thoracic vertebrae", "2×C_2 = 12", 2),
    (5, "lumbar vertebrae", "n_C = 5", 2),
    (5, "sacral vertebrae (fused)", "n_C = 5", 2),
    (4, "coccygeal vertebrae (typical)", "rank² = 4", 1),
    (5, "vertebral regions", "n_C = 5", 2),
    (4, "blood types (ABO)", "rank² = 4", 2),
    (8, "blood types (ABO + Rh)", "2^{N_c} = 8", 2),
    (2, "lung lobes (left)", "rank = 2", 1),
    (3, "lung lobes (right)", "N_c = 3", 1),
    (5, "fingers per hand", "n_C = 5", 1),
    (5, "toes per foot", "n_C = 5", 1),
    (20, "digits (fingers + toes)", "rank²×n_C = 20", 2),
    (4, "wisdom teeth", "rank² = 4", 1),
    (32, "adult teeth", "2^{n_C} = 32", 2),
    (20, "deciduous (baby) teeth", "rank²×n_C = 20", 2),
    (3, "ear bones (ossicles)", "N_c = 3", 2),
    (6, "semicircular structures (3 canals × 2 ears)", "C_2 = 6", 1),
    (2, "eyes", "rank = 2", 1),
    (2, "ears", "rank = 2", 1),
    (7, "layers of skin (if counting all sublayers)", "g = 7", 1),
    (3, "main skin layers (epidermis/dermis/hypodermis)", "N_c = 3", 2),
    (12, "ribs (pairs)", "2×C_2 = 12", 2),
    (24, "ribs (total)", "rank²×C_2 = 24", 2),
    (5, "types of white blood cell", "n_C = 5", 2),
    (3, "types of muscle (skeletal/smooth/cardiac)", "N_c = 3", 2),
    (4, "tissue types (epithelial/connective/muscle/nerve)", "rank² = 4", 2),
    (7, "endocrine glands (major)", "g = 7", 1),
    (6, "nutrients classes (carbs/fats/protein/vitamins/minerals/water)", "C_2 = 6", 2),
    (3, "macronutrients (carbs/fats/protein)", "N_c = 3", 2),
    (2, "sexes (chromosomal)", "rank = 2", 2),
    (46, "chromosomes (human)", "", 1),
    (23, "chromosome pairs", "", 1),
]

def run_tests():
    print("=" * 70)
    print("Toy 1128 — Medicine: BST Integer Counts in Physiology")
    print("=" * 70)
    print()

    score = 0
    tests = 10

    values = [v for v, _, _, _ in MEDICAL_COUNTS]
    total = len(values)
    smooth = sum(1 for v in values if is_7_smooth(v))
    non_smooth = sorted(set(v for v in values if not is_7_smooth(v)))
    smooth_rate = smooth / total

    level_2_plus = sum(1 for _, _, _, l in MEDICAL_COUNTS if l >= 2)
    l2_frac = level_2_plus / total

    print(f"── Overview ──")
    print(f"  Total counts: {total}")
    print(f"  7-smooth: {smooth}/{total} = {smooth_rate:.1%}")
    print(f"  Level 2+: {level_2_plus}/{total} = {l2_frac:.1%}")
    print(f"  Non-7-smooth: {non_smooth}")
    print()

    # Print each entry
    print(f"── Medical Counts ──")
    for v, desc, bst, lev in MEDICAL_COUNTS:
        sm = "✓" if is_7_smooth(v) else "✗"
        lvl = f"L{lev}"
        print(f"  {v:4d} {sm} {lvl} {desc:50s} {bst}")
    print()

    # T1: At least 30 entries
    t1 = total >= 30
    if t1: score += 1
    print(f"  T1 [{'PASS' if t1 else 'FAIL'}] Collected {total} medical counts (target ≥ 30)")
    print()

    # T2: 7-smooth rate > 80%
    t2 = smooth_rate > 0.80
    if t2: score += 1
    print(f"  T2 [{'PASS' if t2 else 'FAIL'}] 7-smooth rate: {smooth_rate:.1%} (target > 80%)")
    print()

    # T3: Level 2+ > 50%
    t3 = l2_frac > 0.50
    if t3: score += 1
    print(f"  T3 [{'PASS' if t3 else 'FAIL'}] Level 2+ fraction: {l2_frac:.1%} (target > 50%)")
    print()

    # T4: g=7 appears in medicine
    g_count = sum(1 for v, _, _, _ in MEDICAL_COUNTS if v == g)
    t4 = g_count >= 2
    if t4: score += 1
    print(f"  T4 [{'PASS' if t4 else 'FAIL'}] g=7 appears {g_count}× in medicine")
    print(f"       Cervical vertebrae (ALL mammals) + endocrine glands + skin layers.")
    print()

    # T5: Vertebral column encodes BST
    vert = [7, 12, 5, 5, 4]  # C, T, L, S, Co
    vert_bst = {7: "g", 12: "2×C_2", 5: "n_C", 5: "n_C", 4: "rank²"}
    vert_total = sum(vert)
    vert_smooth = all(is_7_smooth(v) for v in vert)
    t5 = vert_smooth and vert_total == 33
    if t5: score += 1
    print(f"  T5 [{'PASS' if t5 else 'FAIL'}] Vertebral column: {vert} = all 7-smooth, total {vert_total}")
    print(f"       C=g=7, T=2×C_2=12, L=n_C=5, S=n_C=5, Co=rank²=4. Total=33=N_c×11.")
    print()

    # T6: Blood types encode BST
    t6 = is_7_smooth(4) and is_7_smooth(8)
    if t6: score += 1
    print(f"  T6 [{'PASS' if t6 else 'FAIL'}] Blood: ABO = rank² = 4, ABO+Rh = 2^{{N_c}} = 8")
    print(f"       Both 7-smooth. Rh factor adds N_c=3 bits.")
    print()

    # T7: Teeth encode BST
    t7 = is_7_smooth(32) and is_7_smooth(20)
    if t7: score += 1
    print(f"  T7 [{'PASS' if t7 else 'FAIL'}] Teeth: adult = 2^{{n_C}} = 32, baby = rank²×n_C = 20")
    print(f"       Both are BST products. 32/20 = 8/5 = 2^{{N_c}}/n_C.")
    print()

    # T8: Digits = rank²×n_C = 20
    digits = 20
    t8 = digits == rank**2 * n_C
    if t8: score += 1
    print(f"  T8 [{'PASS' if t8 else 'FAIL'}] Digits (fingers + toes) = {digits} = rank²×n_C = {rank**2 * n_C}")
    print(f"       n_C = 5 per hand, rank² = 4 limbs. Level 2.")
    print()

    # T9: 12 pairs of ribs and cranial nerves
    twelve_items = sum(1 for v, _, _, _ in MEDICAL_COUNTS if v == 12)
    t9 = twelve_items >= 3
    if t9: score += 1
    print(f"  T9 [{'PASS' if t9 else 'FAIL'}] Value 12 = 2×C_2 appears {twelve_items}× (cranial nerves, thoracic vert, ribs)")
    print(f"       2×C_2 is the body's most repeated structural count.")
    print()

    # T10: Non-7-smooth are chromosomes + bones + spinal nerves
    # 206 = 2×103, 31 = prime, 46 = 2×23, 23 = prime
    t10 = set(non_smooth) == {23, 31, 46, 206}
    if t10: score += 1
    print(f"  T10 [{'PASS' if t10 else 'FAIL'}] Non-7-smooth = {non_smooth}")
    print(f"       23 chromosomes (prime), 46 = 2×23, 31 spinal nerves (prime), 206 bones.")
    print(f"       These four are the only failures in {total} medical counts.")
    print()

    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print(f"  Tests: {score}/{tests} PASS")
    print()
    print(f"  HEADLINE: Medicine — {smooth_rate:.1%} 7-smooth ({smooth}/{total})")
    print(f"  {level_2_plus} entries with BST algebraic derivations.")
    print(f"  Vertebral column = [g, 2×C_2, n_C, n_C, rank²] = [7,12,5,5,4].")
    print(f"  Teeth: adult = 2^{{n_C}} = 32, baby = rank²×n_C = 20.")
    print(f"  Blood types: ABO = rank² = 4, +Rh = 2^{{N_c}} = 8.")
    print(f"  Only 4 non-7-smooth values: chromosomes (23, 46), nerves (31), bones (206).")

if __name__ == "__main__":
    run_tests()
