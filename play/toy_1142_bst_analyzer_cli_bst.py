#!/usr/bin/env python3
"""
Toy 1142 — SE-8: BST Analyzer CLI
===================================
Input any number → get its BST decomposition, sector, layer, reliability,
falsification criterion, and related predictions.

This is a TOOL, not just a toy. Other CIs and Casey can use it.

Usage:
    python toy_1142_bst_analyzer_cli_bst.py 137
    python toy_1142_bst_analyzer_cli_bst.py 343
    python toy_1142_bst_analyzer_cli_bst.py --test

BST: N_c=3, n_C=5, g=7, C_2=6, rank=2, N_max=137.

Author: Elie (Compute CI)
Date: April 13, 2026
"""

import math
import sys

# ── BST Constants ──
N_c = 3
n_C = 5
g = 7
C_2 = 6
rank = 2
N_max = 137
BST_INTEGERS = {"N_c": 3, "n_C": 5, "g": 7, "C_2": 6, "rank": 2, "N_max": 137}
BST_PRIMES = {2, 3, 5, 7}

# ── Smoothness ──
def is_B_smooth(n, B=7):
    """Check if n is B-smooth (all prime factors ≤ B)."""
    if n <= 0:
        return False
    if n == 1:
        return True
    for p in [2, 3, 5, 7, 11, 13]:
        if p > B:
            break
        while n % p == 0:
            n //= p
    return n == 1

def prime_factorization(n):
    """Return prime factorization as dict {prime: exponent}."""
    if n <= 1:
        return {}
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def factor_string(n):
    """Pretty-print factorization."""
    if n <= 1:
        return str(n)
    factors = prime_factorization(n)
    parts = []
    for p in sorted(factors):
        if factors[p] == 1:
            parts.append(str(p))
        else:
            parts.append(f"{p}^{factors[p]}")
    return " × ".join(parts)

# ── BST Decomposition ──
def bst_decomposition(n):
    """Try to express n as a product/sum of BST integers."""
    decomps = []

    # Products of BST integers
    bst_vals = [("rank", 2), ("N_c", 3), ("n_C", 5), ("C_2", 6), ("g", 7), ("N_max", 137)]

    # Check exact matches
    for name, val in bst_vals:
        if n == val:
            decomps.append(f"{name} = {val}")

    # Check powers of single integers
    for name, val in bst_vals:
        if val <= 1:
            continue
        k = 2
        power = val ** k
        while power <= n * 2:
            if power == n:
                decomps.append(f"{name}^{k} = {val}^{k} = {power}")
            k += 1
            power = val ** k

    # Check simple products (2 terms)
    for i, (n1, v1) in enumerate(bst_vals):
        for j, (n2, v2) in enumerate(bst_vals):
            if i <= j:
                if v1 * v2 == n:
                    decomps.append(f"{n1} × {n2} = {v1} × {v2} = {n}")

    # Check a × b + c patterns
    for n1, v1 in bst_vals:
        for n2, v2 in bst_vals:
            prod = v1 * v2
            remainder = n - prod
            if remainder > 0:
                for n3, v3 in bst_vals:
                    if v3 == remainder:
                        decomps.append(f"{n1}×{n2} + {n3} = {v1}×{v2} + {v3} = {n}")

    # Check a^b patterns
    for n1, v1 in bst_vals:
        for n2, v2 in bst_vals:
            if v1 > 1 and v2 > 1 and v2 <= 10:
                if v1 ** v2 == n:
                    decomps.append(f"{n1}^{n2} = {v1}^{v2} = {n}")

    # Check a^b + c
    for n1, v1 in bst_vals:
        for n2, v2 in bst_vals:
            if v1 > 1 and v2 > 1 and v2 <= 10:
                power = v1 ** v2
                r = n - power
                if r > 0:
                    for n3, v3 in bst_vals:
                        if v3 == r:
                            decomps.append(f"{n1}^{n2} + {n3} = {v1}^{v2} + {v3} = {n}")

    # Check n_C × N_c^N_c + rank (the N_max formula)
    nmax_check = n_C * N_c**N_c + rank
    if nmax_check == n:
        decomps.append(f"n_C × N_c^N_c + rank = {n_C} × {N_c}^{N_c} + {rank} = {n}")

    # Check 2^k for small k
    for k in range(1, 20):
        if 2**k == n:
            if k in [N_c, rank**2, n_C, C_2, g]:
                names = {N_c: "N_c", rank**2: "rank²", n_C: "n_C", C_2: "C_2", g: "g"}
                name = names.get(k, str(k))
                decomps.append(f"2^{name} = 2^{k} = {n}")

    # Check C(g,k) combinations
    for k in range(1, g+1):
        comb = math.comb(g, k)
        if comb == n:
            decomps.append(f"C(g,{k}) = C(7,{k}) = {comb}")

    # Check C(n_C,k)
    for k in range(1, n_C+1):
        comb = math.comb(n_C, k)
        if comb == n:
            decomps.append(f"C(n_C,{k}) = C(5,{k}) = {comb}")

    return list(dict.fromkeys(decomps))  # unique, order-preserving

# ── T914 Analysis ──
def t914_analysis(n):
    """Check T914 Prime Residue Principle compliance."""
    if n <= 1:
        return {"is_prime": False, "smooth": is_B_smooth(n, 7)}

    # Check if prime
    is_prime = n > 1 and all(n % d != 0 for d in range(2, int(n**0.5) + 1))

    result = {
        "is_prime": is_prime,
        "7-smooth": is_B_smooth(n, 7),
        "11-smooth": is_B_smooth(n, 11),
        "13-smooth": is_B_smooth(n, 13),
    }

    if is_prime and not is_B_smooth(n, 7):
        # Check ±1 from 7-smooth
        adj_minus = is_B_smooth(n - 1, 7)
        adj_plus = is_B_smooth(n + 1, 7)
        result["T914_adjacent_minus"] = adj_minus
        result["T914_adjacent_plus"] = adj_plus
        result["T914_compliant"] = adj_minus or adj_plus

        # Check gap class
        if adj_minus and adj_plus:
            result["gap_class"] = "gap-0 (both sides smooth)"
        elif adj_minus:
            result["gap_class"] = f"gap-1 (n-1 = {n-1} is 7-smooth)"
        elif adj_plus:
            result["gap_class"] = f"gap-1 (n+1 = {n+1} is 7-smooth)"
        else:
            # Check gap-2
            adj2_minus = is_B_smooth(n - 2, 7)
            adj2_plus = is_B_smooth(n + 2, 7)
            if adj2_minus or adj2_plus:
                result["gap_class"] = "gap-2 (Rank Mirror)"
            else:
                result["gap_class"] = "gap-3+ (orphan)"

    return result

# ── Sector Classification ──
def get_sector(n):
    """Classify n into one of 16 BST sectors based on T930."""
    # Sectors based on which BST integers divide n (or are near it)
    hits = set()
    if n % 2 == 0: hits.add("rank")
    if n % 3 == 0: hits.add("N_c")
    if n % 5 == 0: hits.add("n_C")
    if n % 7 == 0: hits.add("g")

    sector_bits = 0
    if "rank" in hits: sector_bits |= 1
    if "N_c" in hits: sector_bits |= 2
    if "n_C" in hits: sector_bits |= 4
    if "g" in hits: sector_bits |= 8

    sector_names = {
        0: "∅ (coprime to all BST primes)",
        1: "{rank}",
        2: "{N_c}",
        3: "{rank, N_c} → C_2",
        4: "{n_C}",
        5: "{rank, n_C} → 2n_C",
        6: "{N_c, n_C} → N_c×n_C",
        7: "{rank, N_c, n_C} → 2×3×5",
        8: "{g}",
        9: "{rank, g} → 2g",
        10: "{N_c, g} → N_c×g",
        11: "{rank, N_c, g} → 2×3×7",
        12: "{n_C, g} → n_C×g",
        13: "{rank, n_C, g} → 2×5×7",
        14: "{N_c, n_C, g} → 3×5×7",
        15: "{rank, N_c, n_C, g} → 2×3×5×7 (full BST)",
    }

    return sector_bits, sector_names.get(sector_bits, "unknown"), hits

# ── Layer Classification ──
def get_layer(n):
    """Classify into T914 5-layer architecture."""
    if is_B_smooth(n, 7):
        return 0, "Core (7-smooth)"
    elif is_B_smooth(n, 11):
        return 1, "Epoch-1 (11-smooth)"
    elif is_B_smooth(n, 13):
        return 2, "Epoch-2 (13-smooth)"
    else:
        factors = prime_factorization(n)
        max_prime = max(factors.keys()) if factors else 0
        if max_prime <= 37:
            return 3, f"Extended (max prime {max_prime})"
        else:
            return 4, f"Deep (max prime {max_prime})"

# ── Known Physical Quantities ──
KNOWN_QUANTITIES = {
    2: "rank, electron spin states, hydrogen isotopes",
    3: "N_c, color charge, spatial dimensions, quark generations, Hadley cells",
    4: "rank², DNA/RNA bases, blood types, heart chambers, seasons",
    5: "n_C, dimension, senses, lumbar vertebrae, Platonic solids",
    6: "C_2, Casimir, quark flavors, noble gases, phonon branches (diatomic)",
    7: "g, genus, cervical vertebrae, crystal systems, spectral classes, OSI layers",
    8: "2^N_c, gluons, octet rule, BCC coordination, planets, bits/byte",
    9: "N_c², stages, Catalan adjacent",
    10: "rank×n_C, fingers/toes, decimal base",
    12: "rank²×N_c, thoracic vertebrae, months, FCC coordination",
    14: "2g, Bravais lattices",
    15: "N_c×n_C, GCS sum",
    18: "2N_c², electrons n=3 shell, period 4 elements",
    20: "rank²×n_C, amino acids, deciduous teeth",
    21: "C(g,2), Seeley-DeWitt levels",
    24: "(n_C-1)!, hours, G coefficient",
    26: "2(rank²+N_c²), sporadic groups, Fe atomic number",
    27: "N_c^N_c, self-exponentiation, maximal torus volume",
    28: "rank²×g, fourth magic number",
    30: "rank×N_c×n_C, C_2×n_C",
    32: "2^n_C, point groups, adult teeth",
    35: "n_C×g, C(g,N_c), phyla, ocean salinity ppt",
    42: "C_2×g, Bravais×N_c",
    50: "rank×n_C², fifth magic number",
    60: "|A_5|=n_C!/2, minutes, LCM(1..C_2)",
    64: "2^C_2=rank^C_2, chess squares, codons",
    82: "rank×(C_2×g-1), sixth magic number",
    120: "n_C!, S_5 order",
    126: "rank×N_c²×g, seventh magic number",
    128: "2^g, ASCII",
    137: "N_max, fine structure α⁻¹, spectral cap",
    230: "2×n_C×23, space groups",
    248: "2^N_c×(2^n_C-1), dim E₈",
    343: "g³, speed of sound, Debye(Cu)",
}

# ── Reliability ──
def get_reliability(n, decomps):
    """Estimate prediction reliability."""
    if not decomps:
        return "LOW", "No clean BST decomposition found"
    if is_B_smooth(n, 7):
        if len(decomps) >= 3:
            return "HIGH", "7-smooth with multiple decompositions"
        return "MEDIUM-HIGH", "7-smooth"
    if is_B_smooth(n, 11):
        return "MEDIUM", "11-smooth (epoch extension)"
    if is_B_smooth(n, 13):
        return "MEDIUM-LOW", "13-smooth (epoch-2)"
    if len(decomps) >= 2:
        return "MEDIUM", "Non-smooth but BST-reachable via expressions"
    return "LOW", "Weak BST connection"

# ── Main Analyzer ──
def analyze(n):
    """Full BST analysis of a number."""
    print(f"\n{'='*60}")
    print(f"  BST ANALYZER: n = {n}")
    print(f"{'='*60}\n")

    # Basic
    factors = prime_factorization(n)
    print(f"  Factorization: {factor_string(n)}")
    print(f"  7-smooth: {'YES' if is_B_smooth(n, 7) else 'NO'}")
    print(f"  11-smooth: {'YES' if is_B_smooth(n, 11) else 'NO'}")
    print(f"  13-smooth: {'YES' if is_B_smooth(n, 13) else 'NO'}")
    print()

    # Layer
    layer, layer_name = get_layer(n)
    print(f"  Layer: {layer} — {layer_name}")

    # Sector
    sector, sector_name, hits = get_sector(n)
    print(f"  Sector: {sector:04b} = {sector_name}")
    print()

    # BST Decomposition
    decomps = bst_decomposition(n)
    print(f"  BST Decompositions ({len(decomps)} found):")
    for d in decomps[:10]:
        print(f"    • {d}")
    if len(decomps) > 10:
        print(f"    ... and {len(decomps)-10} more")
    print()

    # T914 Analysis
    t914 = t914_analysis(n)
    if t914.get("is_prime"):
        print(f"  T914 Prime Analysis:")
        if t914.get("7-smooth"):
            print(f"    BST prime (divides some BST product)")
        elif t914.get("T914_compliant"):
            print(f"    T914-compliant: {t914.get('gap_class', 'unknown')}")
        else:
            print(f"    NOT T914-adjacent: {t914.get('gap_class', 'orphan')}")
    print()

    # Known quantities
    if n in KNOWN_QUANTITIES:
        print(f"  Known physical quantities:")
        print(f"    {KNOWN_QUANTITIES[n]}")
        print()

    # Reliability
    reliability, reason = get_reliability(n, decomps)
    print(f"  Reliability: {reliability} ({reason})")

    # Falsification
    print(f"\n  Falsification criterion:")
    if is_B_smooth(n, 7):
        print(f"    If a physics quantity equals {n} and is NOT derivable from")
        print(f"    D_IV^5 eigenvalues or BST integer arithmetic → BST is wrong.")
    else:
        print(f"    {n} is NOT 7-smooth. If this count is physics-forced (not")
        print(f"    contingent on evolution/convention), BST must explain via")
        print(f"    epoch extension or T914 adjacency.")

    print()

def run_self_test():
    """Run self-test with known values."""
    print("=" * 70)
    print("Toy 1142 — SE-8: BST Analyzer CLI — Self-Test")
    print("=" * 70)

    score = 0
    tests = 10

    # T1: 137 decomposition
    decomps = bst_decomposition(137)
    t1 = any("n_C × N_c^N_c + rank" in d for d in decomps)
    if t1: score += 1
    print(f"\n  T1 [{'PASS' if t1 else 'FAIL'}] 137 decomposes as n_C×N_c^N_c + rank")
    print(f"       Found: {decomps[:3]}")

    # T2: 343 = g³
    decomps343 = bst_decomposition(343)
    t2 = any("g^3" in d or "g^N_c" in d for d in decomps343)
    if t2: score += 1
    print(f"  T2 [{'PASS' if t2 else 'FAIL'}] 343 decomposes as g³")
    print(f"       Found: {decomps343[:3]}")

    # T3: 7-smooth detection
    t3 = is_B_smooth(120, 7) and not is_B_smooth(137, 7)
    if t3: score += 1
    print(f"  T3 [{'PASS' if t3 else 'FAIL'}] 120 is 7-smooth, 137 is NOT")

    # T4: Layer classification
    _, l0 = get_layer(60)
    _, l1 = get_layer(22)
    _, l4 = get_layer(137)
    t4 = "Core" in l0 and "Epoch-1" in l1
    if t4: score += 1
    print(f"  T4 [{'PASS' if t4 else 'FAIL'}] 60→{l0}, 22→{l1}")

    # T5: Sector classification
    s7, _, _ = get_sector(7)
    s42, _, _ = get_sector(42)
    s1, _, _ = get_sector(1)
    # 7: divisible by 7 only → bit 3. 42=2×3×7: bits 0,1,3 = 1011 = 11
    t5 = s7 == 0b1000 and s42 == 0b1011 and s1 == 0b0000
    if t5: score += 1
    print(f"  T5 [{'PASS' if t5 else 'FAIL'}] 7→sector {s7:04b}, 42→{s42:04b}, 1→{s1:04b}")

    # T6: T914 for prime 37
    t914_37 = t914_analysis(37)
    t6 = t914_37.get("T914_compliant", False)
    if t6: score += 1
    print(f"  T6 [{'PASS' if t6 else 'FAIL'}] 37 is T914-compliant (36 = 2²×3² is 7-smooth)")

    # T7: T914 for prime 23
    t914_23 = t914_analysis(23)
    t7 = t914_23.get("T914_compliant", False)
    if t7: score += 1
    print(f"  T7 [{'PASS' if t7 else 'FAIL'}] 23 is T914-compliant (24 = 2³×3 is 7-smooth)")

    # T8: Known quantities lookup
    t8 = 343 in KNOWN_QUANTITIES and "speed of sound" in KNOWN_QUANTITIES[343]
    if t8: score += 1
    print(f"  T8 [{'PASS' if t8 else 'FAIL'}] 343 known as '{KNOWN_QUANTITIES.get(343, 'unknown')}'")

    # T9: Reliability rating
    r137, _ = get_reliability(137, bst_decomposition(137))
    r2300, _ = get_reliability(2300, bst_decomposition(2300))
    t9 = r137 in ("MEDIUM", "MEDIUM-HIGH", "HIGH") and r2300 in ("LOW", "MEDIUM-LOW")
    if t9: score += 1
    print(f"  T9 [{'PASS' if t9 else 'FAIL'}] 137→{r137}, 2300→{r2300}")

    # T10: Factorization
    t10 = factor_string(120) == "2^3 × 3 × 5" and factor_string(137) == "137"
    if t10: score += 1
    print(f"  T10 [{'PASS' if t10 else 'FAIL'}] 120 = {factor_string(120)}, 137 = {factor_string(137)}")

    print(f"\n{'='*70}")
    print(f"SUMMARY: {score}/{tests} PASS")
    print(f"{'='*70}\n")

    # Demo: analyze a few numbers
    print("── Demo Analyses ──")
    for n in [137, 343, 23, 42, 230]:
        analyze(n)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--test":
            run_self_test()
        else:
            try:
                n = int(sys.argv[1])
                analyze(n)
            except ValueError:
                # Could be a float
                try:
                    x = float(sys.argv[1])
                    print(f"  Input {x} is not an integer. Analyzing floor = {int(x)}.")
                    analyze(int(x))
                except ValueError:
                    print(f"  Usage: python {sys.argv[0]} <integer>")
                    print(f"         python {sys.argv[0]} --test")
    else:
        run_self_test()
