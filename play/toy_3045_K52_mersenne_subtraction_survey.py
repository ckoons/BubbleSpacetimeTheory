"""
Toy 3045 — K52 candidate prep: Mersenne-subtraction pattern survey.

Owner: Elie (per Keeper K52 audit candidate flag 2026-05-18)
Date: 2026-05-18

CONTEXT
=======
Toy 3043 found that the Lamb shift sub-leading correction denominator 127 has
DUAL BST identification:
  127 = N_max - rank·n_C  (BST primary subtraction)
  127 = 2^g - 1 = M_g     (7th Mersenne prime)

Keeper K52 candidate question: "Does this Mersenne-subtraction pattern recur in
other BST integer relations, or is Lamb the unique appearance?"

GOAL: survey BST integer combinations of form N_max - (BST product) and check
which are Mersenne primes.

MERSENNE PRIMES in BST-relevant range:
  M_2 = 3      = N_c (BST primary directly, no subtraction)
  M_3 = 7      = g (BST primary directly)
  M_5 = 31
  M_7 = 127
  M_13 = 8191  (way beyond typical BST observable range)
  M_17 = 131071 (similar)

For each Mersenne prime, check BST primary subtraction identifications.
"""

rank, N_c, n_C, C_2, g_b, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137
g = g_b

tests = []
def check(label, ok):
    tests.append((bool(ok), label))


print("="*70)
print("Toy 3045 — Mersenne-subtraction pattern K52 prep survey")
print("="*70)
print()

# === GENERATE BST primary subtractions of N_max ===
print("BST primary subtractions of N_max = 137:")
print()

# Generate small BST products to subtract
bst_primaries = [rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, chi]
bst_products = set()

# Single primaries
for p in bst_primaries:
    bst_products.add(p)

# Two-factor products
for i, a in enumerate(bst_primaries):
    for b in bst_primaries:
        bst_products.add(a * b)

# rank^k powers
for k in [2, 3, 4, 5, 6]:
    bst_products.add(rank**k)

bst_products = sorted(bst_products)

# Find which subtractions of N_max from BST products are Mersenne primes
mersenne_primes = {3: 2, 7: 3, 31: 5, 127: 7}  # M_p = 2^p - 1, value: p

print(f"  {'Subtraction':<22} {'= N_max - X':<14} {'Result':>8} {'Mersenne?':>12} {'Note'}")
print(f"  " + "-"*72)

mersenne_hits = []
for x in bst_products:
    if x < N_max:
        result = N_max - x
        # Check if result is Mersenne prime
        is_mers = result in mersenne_primes
        # Express x in BST primary form (best-effort)
        if x == rank * n_C: bst_form = "rank·n_C"
        elif x == rank * c_2: bst_form = "rank·c_2"
        elif x == N_c * c_2: bst_form = "N_c·c_2"
        elif x == c_2 * g: bst_form = "c_2·g"
        elif x == rank**3 * N_c: bst_form = "rank³·N_c (chi)"
        elif x == rank**3 * c_2: bst_form = "rank³·c_2"
        elif x == rank**4: bst_form = "rank⁴"
        elif x == rank**3: bst_form = "rank³"
        elif x == rank**2 * c_2: bst_form = "rank²·c_2"
        elif x == C_2 * c_2: bst_form = "C_2·c_2"
        elif x == C_2 * g: bst_form = "C_2·g"
        elif x == rank * c_3: bst_form = "rank·c_3 (=26)"
        elif x == g * c_2: bst_form = "g·c_2"
        elif x == c_2**2: bst_form = "c_2²"
        elif x == g**2: bst_form = "g²"
        elif x in bst_primaries:
            bst_form = f"BST primary {x}"
        else:
            bst_form = f"x={x}"

        mers_mark = f"✓ M_{mersenne_primes[result]}" if is_mers else ""
        if is_mers:
            mersenne_hits.append((x, bst_form, result, mersenne_primes[result]))
            note = "MERSENNE HIT"
        else:
            note = ""
        # Only print interesting rows
        if is_mers or result in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
            print(f"  {bst_form:<22} = N_max - {x:<6}   {result:>5}   {mers_mark:>12}  {note}")

print()
print(f"  MERSENNE HITS: {len(mersenne_hits)}")
print()

# Detailed report
print("="*70)
print("MERSENNE SUBTRACTION PATTERN — DETAILED")
print("="*70)
print()
for x, bst_form, result, p in mersenne_hits:
    print(f"  N_max - {bst_form} = {N_max} - {x} = {result} = M_{p} (2^{p} - 1)")
    if p in [2, 3, 5, 7]:
        print(f"    Mersenne exponent p = {p}")
        if p in bst_primaries:
            print(f"    Note: exponent {p} IS a BST primary (rank/N_c/n_C/g)")
        else:
            print(f"    Note: exponent {p} not a BST primary directly")
    print()

# === STRUCTURAL READING ===
print("="*70)
print("STRUCTURAL READING")
print("="*70)
print()

if mersenne_hits:
    # The 127 hit
    found_127 = any(r == 127 for _, _, r, _ in mersenne_hits)
    if found_127:
        print(f"  ✓ 127 = N_max - rank·n_C = M_7 (Lamb correction, Toy 3043)")
        print(f"    Exponent 7 = g (BST primary)")
        print()

    # The 31 hit (if found)
    found_31 = any(r == 31 for _, _, r, _ in mersenne_hits)
    if found_31:
        print(f"  ✓ 31 = M_5 found via BST subtraction")
        for x, bst_form, r, p in mersenne_hits:
            if r == 31:
                print(f"    N_max - {bst_form} = 31 = M_5")
        print(f"    Exponent 5 = n_C (BST primary)")
        print()

    found_7 = any(r == 7 for _, _, r, _ in mersenne_hits)
    if found_7:
        print(f"  ✓ 7 = M_3 found via BST subtraction (trivial, 7 = g BST primary)")
        print()

    found_3 = any(r == 3 for _, _, r, _ in mersenne_hits)
    if found_3:
        print(f"  ✓ 3 = M_2 found via BST subtraction (trivial, 3 = N_c BST primary)")
        print()

print(f"  PATTERN STATUS:")
if len(mersenne_hits) >= 2:
    print(f"  ✓ Mersenne-subtraction pattern RECURS — Lamb 127 is NOT unique")
    print(f"  Multiple BST primary subtractions of N_max produce Mersenne primes.")
    print(f"  K52 audit candidate has supporting evidence beyond single Lamb instance.")
else:
    print(f"  ~ Pattern may be Lamb-specific; insufficient sample for K52 promotion")

check("Mersenne-subtraction survey complete with ≥1 Mersenne hits", len(mersenne_hits) >= 1)
check("Toy 3043 127 result reproduced", any(r == 127 for _, _, r, _ in mersenne_hits))

# Also check inverse: M_p + (BST primary) = N_max?
print()
print("="*70)
print("INVERSE CHECK: M_p + BST product = N_max?")
print("="*70)
print()
for p, m_val in [(2, 3), (3, 7), (5, 31), (7, 127)]:
    diff = N_max - m_val
    # Try to express diff in BST primaries
    if diff in bst_products:
        for x in bst_products:
            if x == diff:
                if x == rank * n_C: bst_form = "rank·n_C"
                elif x == C_2 * g: bst_form = "C_2·g (42)"
                elif x == chi - rank: bst_form = "chi-rank"
                else: bst_form = f"BST product {x}"
                print(f"  N_max - M_{p} = {N_max} - {m_val} = {diff} = {bst_form}")
                break
    else:
        print(f"  N_max - M_{p} = {diff} (not a clean small BST product)")

# Score
passed = sum(1 for ok,*_ in tests if ok)
total = len(tests)
print()
print("="*70)
print(f"Toy 3045 SCORE: {passed}/{total}")
print("="*70)
print()
print("Detail:")
for ok, label in tests:
    mark = "PASS" if ok else "FAIL"
    print(f"  [{mark}] {label}")

print(f"""
K52 CANDIDATE PREP — MERSENNE SUBTRACTION PATTERN SURVEY

Lamb shift correction Toy 3043 found:
  127 = N_max - rank·n_C = M_g = M_7

Keeper question: does this pattern recur?

SURVEY RESULTS:
  Found {len(mersenne_hits)} Mersenne hits via BST primary subtraction of N_max

  Key recurrences (if any):
  - 127 = N_max - rank·n_C = M_7 (Lamb, Toy 3043) ✓ confirmed
  - Others identified in detailed table above

INTERPRETATION:
  If pattern recurs: K52 audit candidate has multi-instance support; promote
  If Lamb-specific: K52 candidate is weaker; single-instance observation

DATA FILED for Keeper K52 audit deliberation when picked up.
""")
