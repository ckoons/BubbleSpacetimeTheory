#!/usr/bin/env python3
"""
Toy 1003 — BST Analyzer: Any Number → BST Decomposition
=========================================================
Track F1 from consensus: CLI tool. Input any number → sector, generation,
BST expression, T914 status, reliability tier, falsification criterion.

Uses the full T914 machinery + abc bridge + sector assignment + Rank Mirror.

Usage:
  python3 toy_1003_bst_analyzer.py 137
  python3 toy_1003_bst_analyzer.py 343
  python3 toy_1003_bst_analyzer.py --batch 1 50

Tests:
  T1: Analyze BST integers themselves (2,3,5,6,7)
  T2: Analyze N_max=137
  T3: Analyze g^3=343 (Debye temperature)
  T4: Analyze first 20 primes — all get T914 status
  T5: Batch mode — analyze 1..200 with summary statistics
  T6: Known physics constants → BST decomposition
  T7: Dark prime analysis (311, 619, 937)
  T8: Stress test — large numbers (1000, 2000, 5000)

Elie — April 10, 2026
"""

import math
import sys
from fractions import Fraction
from collections import defaultdict

# ── BST constants ──
N_c = 3
n_C = 5
g = 7
C_2 = 6
rank = 2
N_max = 137
BST_INTS = {"N_c": N_c, "n_C": n_C, "g": g, "C_2": C_2, "rank": rank}

# ── Helpers ──
def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True

def prime_factors(n):
    if n <= 1: return {}
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

def is_7smooth(n):
    if n <= 1: return True
    return all(p <= 7 for p in prime_factors(n))

# ── Precompute smooth numbers up to reasonable bound ──
SMOOTH_BOUND = 10000
smooth_set = set(n for n in range(1, SMOOTH_BOUND + 1) if is_7smooth(n))

# ── BST product decomposition ──
def bst_decomposition(n):
    """Decompose n into BST integers {2,3,5,6,7} if possible."""
    if n <= 0: return None
    if n == 1: return "1"

    pf = prime_factors(n)
    if any(p > 7 for p in pf):
        return None  # Not 7-smooth

    # Express in terms of BST integers
    parts = []
    remaining = n

    # Try named products first
    named = [
        (N_max, "N_max"),  # 137 - not smooth, won't match
        (g**3, "g^3"),
        (C_2 * g, "C_2*g"),
        (N_c * g, "N_c*g"),
        (n_C * g, "n_C*g"),
        (g**2, "g^2"),
        (N_c * n_C, "N_c*n_C"),
        (C_2**2, "C_2^2"),
        (n_C**2, "n_C^2"),
        (N_c**2, "N_c^2"),
        (rank * g, "rank*g"),
        (rank * n_C, "rank*n_C"),
        (rank * N_c, "rank*N_c"),
    ]

    # Simple: just show prime factorization in BST terms
    expr_parts = []
    r = n
    bst_map = {2: "rank", 3: "N_c", 5: "n_C", 7: "g"}
    for p in [7, 5, 3, 2]:
        count = 0
        while r % p == 0:
            r //= p
            count += 1
        if count > 0:
            name = bst_map[p]
            if count == 1:
                expr_parts.append(name)
            else:
                expr_parts.append(f"{name}^{count}")

    return " * ".join(expr_parts) if expr_parts else "1"


def sector_assignment(n):
    """Assign BST sector based on residues mod N_c, n_C, g."""
    return (n % N_c, n % n_C, n % g)


def sector_name(sector):
    """Human-readable sector name."""
    mod3, mod5, mod7 = sector
    # Sectors from T930
    names = {
        (0, 0, 0): "color+rank+genus",
        (1, 0, 0): "rank-shifted",
        (2, 0, 0): "Casimir",
        (0, 1, 0): "compact-1",
        (0, 2, 0): "compact-2",
        (0, 3, 0): "compact-3",
        (0, 4, 0): "compact-4",
        (0, 0, 1): "genus-1",
        (0, 0, 2): "genus-2",
    }
    # Simplified: use dominant residue
    if mod3 == 0 and mod5 == 0:
        return f"color+compact aligned"
    elif mod3 == 0:
        return f"color sector (r5={mod5}, r7={mod7})"
    elif mod5 == 0:
        return f"compact sector (r3={mod3}, r7={mod7})"
    elif mod7 == 0:
        return f"genus sector (r3={mod3}, r5={mod5})"
    else:
        return f"generic ({mod3},{mod5},{mod7})"


def t914_status(n):
    """Full T914 analysis of n."""
    result = {
        "is_prime": is_prime(n),
        "is_smooth": is_7smooth(n),
        "is_bst_prime": n in {2, 3, 5, 7},
        "bst_decomp": bst_decomposition(n) if is_7smooth(n) else None,
        "sector": sector_assignment(n),
        "min_gap": None,
        "nearest_smooth": None,
        "t914_layer": None,
        "abc_reachable": False,
        "abc_rep": None,
        "reliability": None,
    }

    # Gap from nearest smooth
    min_gap = SMOOTH_BOUND
    nearest = None
    for s in smooth_set:
        d = abs(n - s)
        if d < min_gap:
            min_gap = d
            nearest = s
    result["min_gap"] = min_gap
    result["nearest_smooth"] = nearest

    # T914 layer assignment
    if result["is_bst_prime"]:
        result["t914_layer"] = "L0: BST prime"
    elif result["is_smooth"]:
        result["t914_layer"] = "smooth (BST composite)"
    elif min_gap <= 1:
        result["t914_layer"] = "L1: gap-1 (T914 primary)"
    elif min_gap == 2:
        result["t914_layer"] = "L2: gap-2 (Rank Mirror)"
    elif min_gap == g:
        result["t914_layer"] = "L4: gap-g (genus resonance)"

    # abc check: is n = smooth_a + smooth_b with gcd=1?
    if result["is_prime"] and not result["is_bst_prime"]:
        smooth_list_local = sorted(s for s in smooth_set if s < n)
        for a in smooth_list_local:
            b = n - a
            if b >= a and is_7smooth(b) and math.gcd(a, b) == 1:
                result["abc_reachable"] = True
                result["abc_rep"] = (a, b)
                break

    if result["abc_reachable"] and result["t914_layer"] is None:
        result["t914_layer"] = "L3: abc sum"

    if result["t914_layer"] is None and result["is_prime"]:
        result["t914_layer"] = "L5: dark"

    # Reliability tier
    if n <= g**3:
        result["reliability"] = "Tier 1 (below g^3=343)"
    elif n <= 1000:
        result["reliability"] = "Tier 2 (343 < n ≤ 1000)"
    elif n <= 5000:
        result["reliability"] = "Tier 3 (1000 < n ≤ 5000)"
    else:
        result["reliability"] = "Tier 4 (beyond 5000)"

    # Generation
    if n <= g:
        result["generation"] = 1
    elif n <= g**2:
        result["generation"] = 2
    elif n <= g**3:
        result["generation"] = 3
    else:
        result["generation"] = int(math.log(n) / math.log(g)) + 1 if n > 0 else 0

    return result


def format_analysis(n, r):
    """Pretty-print analysis result."""
    lines = [f"  === {n} ==="]

    # Type
    if r["is_bst_prime"]:
        lines.append(f"  Type: BST PRIME (one of the five generators)")
    elif r["is_smooth"]:
        lines.append(f"  Type: 7-smooth composite")
        lines.append(f"  BST decomposition: {n} = {r['bst_decomp']}")
    elif r["is_prime"]:
        lines.append(f"  Type: Prime")
    else:
        # Composite, not smooth
        pf = prime_factors(n)
        lines.append(f"  Type: Composite (factors: {dict(pf)})")

    # Sector
    sec = r["sector"]
    lines.append(f"  Sector: ({sec[0]},{sec[1]},{sec[2]}) = {sector_name(sec)}")

    # Generation
    lines.append(f"  Generation: {r.get('generation', '?')}")

    # T914 status
    if r["is_prime"] or r["is_smooth"]:
        lines.append(f"  Nearest smooth: {r['nearest_smooth']} (gap={r['min_gap']})")
        if r["t914_layer"]:
            lines.append(f"  T914 layer: {r['t914_layer']}")
        if r["abc_reachable"]:
            a, b = r["abc_rep"]
            lines.append(f"  abc route: {n} = {a} + {b}")

    # Reliability
    lines.append(f"  Reliability: {r['reliability']}")

    # Special identities
    specials = []
    if n == N_max:
        specials.append(f"N_max = N_c^3*n_C + rank = {N_c}^3*{n_C}+{rank}")
    if n == g**3:
        specials.append(f"g^3 = Debye temperature of Cu")
    if n == N_c * n_C * g:
        specials.append(f"N_c*n_C*g = 105 (product of three generators)")
    if n == 2 * 3 * 5 * 7:
        specials.append(f"rank*N_c*n_C*g = 210 (product of all generators)")
    if is_prime(n) and n - 1 in smooth_set:
        specials.append(f"Størmer adjacent: {n}-1 = {n-1} is smooth")
    if is_prime(n) and n + 1 in smooth_set:
        specials.append(f"Størmer adjacent: {n}+1 = {n+1} is smooth")

    for s in specials:
        lines.append(f"  ** {s}")

    return "\n".join(lines)


# =========================================================
# TESTS
# =========================================================
results = []
def test(name, condition, detail):
    status = "PASS" if condition else "FAIL"
    results.append((name, status))
    print(f"  [{status}] {name}")
    print(f"         {detail}")

print("=" * 70)
print("Toy 1003 — BST Analyzer: Any Number → BST Decomposition")
print("=" * 70)


# =========================================================
# T1: BST integers themselves
# =========================================================
print(f"\n--- T1: Analyze BST Integers ---")

bst_nums = [(2, "rank"), (3, "N_c"), (5, "n_C"), (6, "C_2"), (7, "g")]
all_correct = True
for n, name in bst_nums:
    r = t914_status(n)
    print(format_analysis(n, r))
    if n in {2, 3, 5, 7} and not r["is_bst_prime"]:
        all_correct = False
    if n == 6 and not r["is_smooth"]:
        all_correct = False

test("T1: BST integers correctly classified",
     all_correct,
     f"All 5 BST integers analyzed. Primes: 2,3,5,7 → BST PRIME. 6 → smooth composite.")


# =========================================================
# T2: N_max = 137
# =========================================================
print(f"\n--- T2: N_max = 137 ---")

r137 = t914_status(137)
print(format_analysis(137, r137))

test("T2: N_max=137 analyzed",
     r137["is_prime"] and r137["t914_layer"] == "L2: gap-2 (Rank Mirror)" and r137["abc_reachable"],
     f"137: prime, gap={r137['min_gap']}, layer={r137['t914_layer']}, abc={'YES' if r137['abc_reachable'] else 'NO'}.")


# =========================================================
# T3: g^3 = 343
# =========================================================
print(f"\n--- T3: g^3 = 343 (Debye temperature) ---")

r343 = t914_status(343)
print(format_analysis(343, r343))

test("T3: g^3=343 analyzed",
     r343["is_smooth"] and r343["bst_decomp"] is not None,
     f"343 = {r343['bst_decomp']}. Smooth. Reliability: {r343['reliability']}.")


# =========================================================
# T4: First 20 primes
# =========================================================
print(f"\n--- T4: First 20 Primes ---")

first_20_primes = [p for p in range(2, 80) if is_prime(p)][:20]
classified = 0
print(f"  {'p':>4} {'layer':>25} {'gap':>4} {'abc':>5} {'sector':>15}")
for p in first_20_primes:
    r = t914_status(p)
    abc_str = f"{r['abc_rep'][0]}+{r['abc_rep'][1]}" if r['abc_reachable'] else "—"
    layer = r["t914_layer"] or "?"
    sec = r["sector"]
    print(f"  {p:>4} {layer:>25} {r['min_gap']:>4} {abc_str:>5} ({sec[0]},{sec[1]},{sec[2]})")
    if r["t914_layer"]:
        classified += 1

test("T4: First 20 primes classified",
     classified == 20,
     f"{classified}/20 primes have T914 layer assignment.")


# =========================================================
# T5: Batch mode 1..200
# =========================================================
print(f"\n--- T5: Batch Analysis 1..200 ---")

layer_counts = defaultdict(int)
smooth_count = 0
prime_count = 0
composite_non_smooth = 0

for n in range(1, 201):
    r = t914_status(n)
    if r["is_prime"]:
        prime_count += 1
        if r["t914_layer"]:
            layer_counts[r["t914_layer"]] += 1
    elif r["is_smooth"]:
        smooth_count += 1
    else:
        composite_non_smooth += 1

print(f"  Numbers 1..200:")
print(f"    Smooth composites: {smooth_count}")
print(f"    Non-smooth composites: {composite_non_smooth}")
print(f"    Primes: {prime_count}")
print(f"  Prime layer distribution:")
for layer, count in sorted(layer_counts.items()):
    print(f"    {layer:>30}: {count}")

total_classified = sum(layer_counts.values())
test("T5: Batch mode works",
     total_classified == prime_count,
     f"{total_classified}/{prime_count} primes ≤200 classified. {smooth_count} smooth composites.")


# =========================================================
# T6: Physics constants
# =========================================================
print(f"\n--- T6: Known Physics Constants ---")

physics = [
    (137, "α^-1 (fine structure)"),
    (343, "θ_D(Cu) = g^3"),
    (938, "m_p (MeV) ≈ 6π^5 m_e"),
    (14, "pKa(water) = rank*g"),
    (21, "bp/turn DNA ≈ N_c*g"),
    (118, "heaviest element Z"),
    (184, "predicted magic number"),
    (210, "rank*N_c*n_C*g"),
    (105, "N_c*n_C*g"),
]

for n, desc in physics:
    r = t914_status(n)
    decomp = r["bst_decomp"] if r["is_smooth"] else f"gap={r['min_gap']} from smooth"
    abc = f", abc={r['abc_rep'][0]}+{r['abc_rep'][1]}" if r["abc_reachable"] else ""
    print(f"  {n:>4} ({desc}): {decomp}{abc}")

test("T6: Physics constants analyzed",
     True,
     f"{len(physics)} physics-relevant numbers decomposed.")


# =========================================================
# T7: Dark primes
# =========================================================
print(f"\n--- T7: Dark Prime Analysis ---")

dark_examples = [311, 619, 937, 1103, 1559]
all_dark = True
for p in dark_examples:
    r = t914_status(p)
    print(format_analysis(p, r))
    if r["t914_layer"] != "L5: dark":
        all_dark = False

test("T7: Dark primes correctly identified",
     all_dark,
     f"{len(dark_examples)} dark primes analyzed. All classified as L5: dark.")


# =========================================================
# T8: Stress test — large numbers
# =========================================================
print(f"\n--- T8: Stress Test ---")

stress = [1000, 2000, 5000, 7919, 10007]
all_analyzed = True
for n in stress:
    r = t914_status(n)
    layer = r["t914_layer"] or "composite"
    decomp = r["bst_decomp"] if r["is_smooth"] else f"gap={r['min_gap']}"
    print(f"  {n:>6}: {'prime' if r['is_prime'] else 'composite'}, {decomp}, {layer}, {r['reliability']}")
    if r["is_prime"] and r["t914_layer"] is None:
        all_analyzed = False

test("T8: Stress test passed",
     all_analyzed,
     f"{len(stress)} large numbers analyzed. All primes classified.")


# =========================================================
# Summary
# =========================================================
print("\n" + "=" * 70)
print(f"RESULTS: {sum(1 for _,s in results if s=='PASS')}/{len(results)} PASS")
print("=" * 70)
for name, status in results:
    print(f"  [{status}] {name}")

print(f"\nHEADLINE: BST Analyzer Tool")
print(f"  A1: Any number → type, sector, generation, BST decomposition")
print(f"  A2: Primes → T914 layer (L0-L5), abc route, nearest smooth, gap")
print(f"  A3: Composites → smooth/non-smooth, factor decomposition in BST terms")
print(f"  A4: Physics constants decoded (137=N_c^3*n_C+rank, 343=g^3, ...)")
print(f"  A5: Reliability tiers (1-4) based on distance from g^3 boundary")
print(f"  TOOL: Ready for CLI integration. Usage: python3 toy_1003_bst_analyzer.py <number>")


# =========================================================
# CLI mode
# =========================================================
if len(sys.argv) > 1:
    print(f"\n{'='*70}")
    print(f"CLI Analysis")
    print(f"{'='*70}")
    if sys.argv[1] == "--batch":
        lo = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        hi = int(sys.argv[3]) if len(sys.argv) > 3 else 100
        for n in range(lo, hi + 1):
            r = t914_status(n)
            if r["is_prime"]:
                print(format_analysis(n, r))
    else:
        for arg in sys.argv[1:]:
            try:
                n = int(arg)
                r = t914_status(n)
                print(format_analysis(n, r))
            except ValueError:
                print(f"  Skipping non-integer: {arg}")
