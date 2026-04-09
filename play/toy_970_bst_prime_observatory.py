#!/usr/bin/env python3
"""
Toy 970 — The BST Prime Observatory
=====================================
Keeper's directive: Generate all products of {2, 3, 5, 6, 7} up to a bound,
test ±1 for primality, cross-reference against existing BST predictions.

Every prime that ISN'T already matched to a known observable is a prediction
waiting for a domain. The composites linearize. The primes don't. The physics
is in the don't.

"AC(0) — one primality test per candidate."

BST integers: N_c=3, n_C=5, g=7, C_2=6, rank=2, N_max=137
"""

import math
from sympy import isprime, factorint

# =====================================================================
# BST integers
# =====================================================================
N_c = 3
n_C = 5
g = 7
C_2 = 6
rank = 2
N_max = 137

BST_INTS = [rank, N_c, n_C, C_2, g]
BST_NAMES = {2: "rank", 3: "N_c", 5: "n_C", 6: "C_2", 7: "g"}

# =====================================================================
# Step 1: Generate all products of {2,3,5,6,7} up to bound
# =====================================================================
BOUND = 10000

def generate_products(ints, bound):
    """Generate all products of elements from ints, up to bound.
    Each integer can appear 0 or more times (with repetition)."""
    products = {1: []}  # value -> list of factors used
    queue = [(1, [])]

    while queue:
        val, factors = queue.pop(0)
        for i in ints:
            new_val = val * i
            if new_val <= bound and new_val not in products:
                new_factors = factors + [i]
                products[new_val] = new_factors
                queue.append((new_val, new_factors))
            elif new_val <= bound and new_val in products:
                # Keep shorter factorization
                if len(factors) + 1 < len(products[new_val]):
                    products[new_val] = factors + [i]

    return products

print("=" * 70)
print("Toy 970 — The BST Prime Observatory")
print("=" * 70)
print(f"\nGenerating all products of {{2, 3, 5, 6, 7}} up to {BOUND}...")

products = generate_products(BST_INTS, BOUND)
print(f"  Found {len(products)} distinct BST-composite numbers")

# =====================================================================
# Step 2: Test n±1 for primality
# =====================================================================
print(f"\n{'='*70}")
print("Step 2: Primality test on BST-composite ± 1")
print("="*70)

observer_primes = []  # n+1 primes (observer shift)
mersenne_primes = []  # n-1 primes (Mersenne deficit)

for n in sorted(products.keys()):
    if n < 2:
        continue

    # Test n+1 (observer shift)
    if isprime(n + 1):
        factors = products[n]
        observer_primes.append((n, n+1, factors, "+1"))

    # Test n-1 (Mersenne deficit)
    if n > 1 and isprime(n - 1):
        factors = products[n]
        mersenne_primes.append((n, n-1, factors, "-1"))

print(f"\n  Observer primes (n+1): {len(observer_primes)}")
print(f"  Mersenne primes (n-1): {len(mersenne_primes)}")
print(f"  Total BST primes: {len(observer_primes) + len(mersenne_primes)}")

# =====================================================================
# Step 3: The known predictions catalog
# =====================================================================
# Map known BST observables to their prime content
KNOWN_PRIMES = {
    3: {"name": "N_c (color charge)", "context": "QCD gauge group SU(3)", "shift": "+1 from rank=2"},
    5: {"name": "n_C (compact dim)", "context": "D_IV^5 dimension count", "shift": "+1 from 2^rank=4"},
    7: {"name": "g (genus)", "context": "Genus of D_IV^5", "shift": "+1 from C_2=6 AND -1 from 2^N_c=8"},
    13: {"name": "2C_2+1", "context": "Ω_Λ numerator (13/19), 2C_2+1 structural unit", "shift": "+1 from 12=2C_2"},
    19: {"name": "2N_c²+1", "context": "Ω_Λ denominator (13/19), reality budget", "shift": "+1 from 18=2N_c²"},
    31: {"name": "2^n_C-1", "context": "Mersenne prime, Hamming code", "shift": "-1 from 32=2^n_C"},
    37: {"name": "C_2²+1", "context": "Appears in nuclear binding", "shift": "+1 from 36=C_2²"},
    41: {"name": "C_2×g-1", "context": "Near 42=C_2×g", "shift": "-1 from 42=C_2×g"},
    43: {"name": "C_2×g+1", "context": "Percolation γ=43/18, 3D Ising β=14/43", "shift": "+1 from 42=C_2×g"},
    89: {"name": "?", "context": "Fibonacci prime, near 90=2×C_2×g+C_2", "shift": ""},
    91: {"name": "g(2C_2+1)", "context": "Percolation δ=91/5, 3D Ising δ-1=91/24", "shift": "COMPOSITE (7×13)"},
    127: {"name": "2^g-1", "context": "Mersenne prime M_7", "shift": "-1 from 128=2^g"},
    137: {"name": "N_max", "context": "Fine structure 1/α, η_Ising≈5/137", "shift": "terminus"},
    139: {"name": "N_max+rank", "context": "Near 137", "shift": "?"},
    181: {"name": "?", "context": "Near 180=C_2×n_C×C_2", "shift": "+1 from 180"},
    211: {"name": "?", "context": "Near 210=rank×N_c×n_C×g", "shift": "+1 from 210"},
    3329: {"name": "?", "context": "Near 3328", "shift": "+1 from 3328"},
}

# =====================================================================
# Step 4: Cross-reference — find unmatched primes
# =====================================================================
print(f"\n{'='*70}")
print("Step 4: The Observatory — BST Primes Catalog")
print("="*70)

def factorize_bst(n):
    """Express n as a product of BST integers."""
    if n in products:
        factors = products[n]
        if factors:
            names = [BST_NAMES.get(f, str(f)) for f in sorted(factors)]
            nums = "×".join(str(f) for f in sorted(factors))
            named = "×".join(names)
            return f"{nums} = {named}"
        else:
            return "1"
    return None

# Combine and sort all primes
all_primes = []
for n, p, factors, shift in observer_primes:
    all_primes.append((p, n, shift, factors))
for n, p, factors, shift in mersenne_primes:
    all_primes.append((p, n, shift, factors))

# Remove duplicates (same prime from different composites)
seen_primes = {}
for p, n, shift, factors in all_primes:
    if p not in seen_primes:
        seen_primes[p] = (n, shift, factors)
    elif len(factors) < len(seen_primes[p][2]):
        seen_primes[p] = (n, shift, factors)

all_unique = sorted(seen_primes.keys())

print(f"\n  Total unique BST primes up to {BOUND+1}: {len(all_unique)}")

# Categorize: known vs unknown
known = []
unknown = []
for p in all_unique:
    n, shift, factors = seen_primes[p]
    bst_expr = factorize_bst(n)
    if p in KNOWN_PRIMES:
        known.append((p, n, shift, bst_expr, KNOWN_PRIMES[p]))
    else:
        unknown.append((p, n, shift, bst_expr))

print(f"  Known (matched to observables): {len(known)}")
print(f"  UNKNOWN (predictions waiting): {len(unknown)}")

# =====================================================================
# T1: Known primes — the existing catalog
# =====================================================================
print(f"\n{'='*70}")
print("T1: Known BST Primes (matched to physics)")
print("="*70)

passed = 0
failed = 0
total = 0

def test(name, condition, detail=""):
    global passed, failed, total
    total += 1
    if condition:
        passed += 1
        print(f"  [PASS] {name}")
    else:
        failed += 1
        print(f"  [FAIL] {name}")
    if detail:
        print(f"         {detail}")

for p, n, shift, bst_expr, info in known[:20]:
    print(f"  {p:5d} = {n}{shift:>3s}  [{bst_expr}]  → {info['name']}: {info['context']}")

test("T1: Known catalog populated", len(known) >= 5,
     f"{len(known)} known primes in catalog")

# =====================================================================
# T2: Unknown primes — the prediction map
# =====================================================================
print(f"\n{'='*70}")
print("T2: UNKNOWN BST Primes — Predictions Waiting for Domains")
print("="*70)

print(f"\n  These primes are REQUIRED by BST number theory but have no")
print(f"  known observable assignment. Each is a prediction.\n")

# Show first 50 unknown primes
print(f"  {'Prime':>6s}  {'Composite':>10s}  {'Shift':>5s}  {'BST Expression':40s}")
print(f"  {'─'*6}  {'─'*10}  {'─'*5}  {'─'*40}")

for p, n, shift, bst_expr in unknown[:60]:
    print(f"  {p:6d}  {n:10d}  {shift:>5s}  {bst_expr}")

print(f"\n  ... ({len(unknown)} total unknown primes)")

test("T2: Unknown primes found", len(unknown) > 0,
     f"{len(unknown)} predictions waiting for domains")

# =====================================================================
# T3: Structure of the prime observatory
# =====================================================================
print(f"\n{'='*70}")
print("T3: Structure analysis")
print("="*70)

# Count observer (+1) vs Mersenne (-1)
n_observer = sum(1 for p, n, s, _ in unknown if s == "+1")
n_mersenne = sum(1 for p, n, s, _ in unknown if s == "-1")
print(f"  Observer primes (+1): {n_observer}")
print(f"  Mersenne primes (-1): {n_mersenne}")
print(f"  Ratio observer/mersenne: {n_observer/max(n_mersenne,1):.2f}")

# Distribution by BST integer depth (number of factors)
from collections import Counter
depths = Counter()
for p, n, shift, bst_expr in unknown:
    n_val, _, factors = seen_primes[p]
    depths[len(factors)] += 1

print(f"\n  By composite depth (number of BST factors):")
for d in sorted(depths.keys()):
    bar = "█" * (depths[d] // 2)
    print(f"    depth {d}: {depths[d]:4d} primes  {bar}")

# Which BST integers appear most in the composites?
int_freq = Counter()
for p, n, shift, bst_expr in unknown:
    n_val, _, factors = seen_primes[p]
    for f in factors:
        int_freq[f] += 1

print(f"\n  BST integer frequency in unknown composites:")
for i, count in int_freq.most_common():
    name = BST_NAMES.get(i, str(i))
    print(f"    {name:6s} ({i}): {count} appearances")

test("T3: Both +1 and -1 primes present", n_observer > 0 and n_mersenne > 0,
     f"+1: {n_observer}, -1: {n_mersenne}")

# =====================================================================
# T4: The first 20 — immediate prediction targets
# =====================================================================
print(f"\n{'='*70}")
print("T4: The First 20 Unmatched Primes — Immediate Targets")
print("="*70)

print(f"\n  These are the LOWEST unmatched BST primes. Each represents")
print(f"  an observable that the number theory requires but we haven't")
print(f"  identified yet.\n")

targets = unknown[:20]
for i, (p, n, shift, bst_expr) in enumerate(targets):
    # Try to suggest a domain based on the composite structure
    n_val, _, factors = seen_primes[p]
    depth = len(factors)

    # Heuristic domain suggestions based on factors
    if 7 in factors and 6 in factors:
        hint = "gauge/flavor (g×C₂ sector)"
    elif 7 in factors:
        hint = "genus/topology sector"
    elif 5 in factors and 6 in factors:
        hint = "compact×Casimir sector"
    elif 5 in factors:
        hint = "compact dimension sector"
    elif 3 in factors and 2 in factors:
        hint = "color/rank sector"
    elif 6 in factors:
        hint = "Casimir sector"
    elif 3 in factors:
        hint = "color sector"
    elif 2 in factors:
        hint = "rank sector"
    else:
        hint = "uncharacterized"

    print(f"  {i+1:2d}. p = {p:5d} = {n}{shift}  [{bst_expr}]  → {hint}")

test("T4: At least 20 immediate targets", len(targets) >= 20,
     f"{len(targets)} targets identified")

# =====================================================================
# T5: Dual-membership primes (both +1 and -1 from different composites)
# =====================================================================
print(f"\n{'='*70}")
print("T5: Dual-membership primes (like g=7: both 6+1 AND 8-1)")
print("="*70)

dual = []
obs_set = set(p for n, p, f, s in observer_primes)
mer_set = set(p for n, p, f, s in mersenne_primes)
both = obs_set & mer_set

print(f"\n  Primes reachable from BOTH +1 and -1: {len(both)}")
for p in sorted(both)[:30]:
    # Find the +1 composite
    plus_composites = [(n, f) for n, pp, f, s in observer_primes if pp == p]
    minus_composites = [(n, f) for n, pp, f, s in mersenne_primes if pp == p]

    plus_str = ", ".join(f"{n}+1" for n, f in plus_composites[:2])
    minus_str = ", ".join(f"{n}-1" for n, f in minus_composites[:2])

    matched = "KNOWN" if p in KNOWN_PRIMES else "unknown"
    print(f"  {p:5d} = {plus_str:20s} AND {minus_str:20s}  [{matched}]")

# g = 7 should be in this list
test("T5: g=7 has dual membership", 7 in both,
     f"7 = 6+1 (C₂+1) AND 8-1 (2^N_c-1)")

# =====================================================================
# T6: Prime density — how many BST primes per decade?
# =====================================================================
print(f"\n{'='*70}")
print("T6: Prime density by magnitude")
print("="*70)

decades = {}
for p in all_unique:
    decade = len(str(p))
    if decade not in decades:
        decades[decade] = 0
    decades[decade] += 1

# Also compute total primes per decade for comparison
from sympy import primerange
decade_totals = {}
for d in sorted(decades.keys()):
    lo = 10**(d-1) if d > 1 else 2
    hi = 10**d
    total_primes = len(list(primerange(lo, hi)))
    decade_totals[d] = total_primes

print(f"\n  {'Digits':>6s}  {'BST primes':>10s}  {'All primes':>10s}  {'BST fraction':>12s}")
for d in sorted(decades.keys()):
    frac = decades[d] / decade_totals[d] * 100 if decade_totals[d] > 0 else 0
    print(f"  {d:6d}  {decades[d]:10d}  {decade_totals[d]:10d}  {frac:11.2f}%")

# Total
total_bst = sum(decades.values())
total_all = sum(decade_totals.values())
print(f"  {'TOTAL':>6s}  {total_bst:10d}  {total_all:10d}  {total_bst/total_all*100:11.2f}%")

test("T6: BST primes are a small fraction of all primes",
     total_bst / total_all < 0.5,
     f"BST fraction: {total_bst/total_all*100:.2f}% — selective, not trivial")

# =====================================================================
# T7: The prediction count
# =====================================================================
print(f"\n{'='*70}")
print("T7: Summary — The Observatory")
print("="*70)

print(f"\n  BST-composite numbers up to {BOUND}: {len(products)}")
print(f"  BST primes (composite ± 1):    {len(all_unique)}")
print(f"  Already matched to physics:    {len(known)}")
print(f"  PREDICTIONS (unmatched):       {len(unknown)}")
print()
print(f"  Each unmatched prime is an observable that BST number theory")
print(f"  REQUIRES to exist but hasn't been identified yet.")
print()
print(f"  The search algorithm: for each BST composite n,")
print(f"    test isprime(n+1) and isprime(n-1).")
print(f"  Complexity: AC(0) — one primality test per candidate.")
print()

# The prediction density
print(f"  Prediction density:")
print(f"    Up to 100:   {sum(1 for p,_,_,_ in unknown if p<=100)} predictions")
print(f"    Up to 1000:  {sum(1 for p,_,_,_ in unknown if p<=1000)} predictions")
print(f"    Up to 10000: {sum(1 for p,_,_,_ in unknown if p<=10000)} predictions")

test("T7: Observatory produces >100 predictions", len(unknown) > 100,
     f"{len(unknown)} predictions generated")

# =====================================================================
# T8: Cross-check — do ALL known BST primes appear?
# =====================================================================
print(f"\n{'='*70}")
print("T8: Cross-check — completeness")
print("="*70)

# Check that key known primes appear in our list
key_primes = [3, 5, 7, 13, 19, 31, 37, 43, 127, 137]
found_key = []
missing_key = []
for p in key_primes:
    if p in seen_primes:
        found_key.append(p)
    else:
        missing_key.append(p)

print(f"  Key BST primes checked: {key_primes}")
print(f"  Found: {found_key}")
print(f"  Missing: {missing_key}")

if missing_key:
    print(f"\n  NOTE: Missing primes may require extended generation.")
    for p in missing_key:
        if p == 137:
            print(f"    137 = N_max: terminus, not from BST-composite ± 1")
            print(f"         137-1 = 136 = 2³×17 — 17 not BST")
            print(f"         137+1 = 138 = 2×3×23 — 23 not BST")
            print(f"         137 is ORPHAN: no BST composite neighbors")

test("T8: Key primes recovered (except terminus)",
     len(found_key) >= len(key_primes) - 2,
     f"{len(found_key)}/{len(key_primes)} found. Missing: {missing_key}")

# =====================================================================
# RESULTS
# =====================================================================
print(f"\n{'='*70}")
print("RESULTS")
print("="*70)
print(f"  {passed}/{total} PASS\n")

print("  KEY FINDINGS:")
print(f"  1. {len(unknown)} unmatched BST primes = {len(unknown)} predictions")
print(f"     waiting for observational domains.")
print(f"  2. The composites linearize. The primes don't. Physics IS the primes.")
print(f"  3. Search complexity: AC(0) — one primality test per candidate.")
print(f"  4. {len(both)} dual-membership primes (reachable from both ±1).")
print(f"     g=7 is dual: 6+1 AND 8-1. These may be structurally special.")
print(f"  5. N_max=137 is ORPHAN — no BST-composite neighbor is 136 or 138.")
print(f"     It stands alone as the representation-theoretic terminus.")
print(f"  6. BST primes are {total_bst/total_all*100:.1f}% of all primes — selective,")
print(f"     not trivial. The observatory has resolving power.")
