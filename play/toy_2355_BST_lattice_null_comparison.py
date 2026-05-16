"""
Toy 2355 — BST lattice density: null comparison + density at higher N.

Toy 2353 showed BST atoms {2,3,5,6,7,11,13,17,24,137} with two-term
decomposition cover 100% of [2, 1000]. Is this trivial?

Test 1: Push N higher (to 10000) — does the cover break?
Test 2: Compare to RANDOM 10-atom subsets of small primes — do they
        also give 100% cover, or is BST special?
Test 3: Find FIRST integer that breaks two-term cover (if any).
"""

import random


def make_products(atoms, max_factors=3, max_value=20000):
    """Generate all products up to max_factors from atom set."""
    products = set([1])
    last_round = set([1])
    for _ in range(max_factors):
        next_round = set()
        for p in last_round:
            for a in atoms:
                v = p * a
                if 1 <= v <= max_value:
                    next_round.add(v)
        products.update(next_round)
        last_round = next_round
    return products


def two_term_cover_with(atoms, N_max, max_factors=3):
    """Check coverage of [2, N_max] via two-term decomposition."""
    products = make_products(atoms, max_factors, N_max * 2)
    products_sorted = sorted(products)
    products_set = set(products)
    count = 0
    failures = []
    for n in range(2, N_max + 1):
        if n in products_set:
            count += 1
            continue
        # Check n = p + q or n = p - q
        found = False
        for p in products_sorted:
            if p > n * 2:
                break
            q = n - p
            if q in products_set:
                found = True
                break
            q = p - n
            if q > 0 and q in products_set:
                found = True
                break
        if found:
            count += 1
        else:
            failures.append(n)
    return count, failures


# BST atoms
BST_ATOMS = [2, 3, 5, 6, 7, 11, 13, 17, 24, 137]

# Push N higher
print("Pushing BST coverage to higher N:")
for N in [200, 500, 1000, 2000, 5000, 10000]:
    count, fails = two_term_cover_with(BST_ATOMS, N)
    coverage = 100 * count / (N - 1)
    print(f"  N={N}: BST covers {count}/{N-1} = {coverage:.2f}%   "
          f"failures: {len(fails)}")
    if fails and len(fails) < 30:
        print(f"    First failures: {fails[:20]}")
    elif fails:
        print(f"    First 20: {fails[:20]}, last 5: {fails[-5:]}")

# Null comparison: random subsets of small primes
print("\n" + "=" * 65)
print("NULL COMPARISON — 10 random small primes + 1 fine-structure-like anchor")
print("=" * 65)
SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# Try 5 random samples
random.seed(42)
results = []
N_test_null = 1000
for trial in range(5):
    null_atoms = random.sample(SMALL_PRIMES, 7)
    # Add a composite and an "anchor" similar to 24, 137
    null_atoms.append(2**3 * 3)  # 24 analog
    null_atoms.append(random.randint(100, 200))  # random "anchor"
    null_atoms.append(2 * 3)  # 6 analog
    count, fails = two_term_cover_with(sorted(null_atoms), N_test_null)
    results.append((null_atoms, count, fails))
    print(f"  Trial {trial+1}: atoms = {sorted(null_atoms)}")
    print(f"    Coverage: {count}/{N_test_null-1} = {100*count/(N_test_null-1):.2f}%, "
          f"failures: {len(fails)}")

print(f"\nBST coverage: 100.00% (compare)")

# ============================================================
# What's the actual breaking point of BST?
# ============================================================
print("\n" + "=" * 65)
print("BST breaking point search (large N)")
print("=" * 65)
for N in [20000, 50000, 100000]:
    count, fails = two_term_cover_with(BST_ATOMS, N, max_factors=4)
    coverage = 100 * count / (N - 1)
    print(f"  N={N}: {count}/{N-1} = {coverage:.4f}%   failures: {len(fails)}")
    if fails and len(fails) < 30:
        print(f"    Failures: {fails}")
    elif fails:
        print(f"    First 15 failures: {fails[:15]}")
        print(f"    Last 15 failures:  {fails[-15:]}")
