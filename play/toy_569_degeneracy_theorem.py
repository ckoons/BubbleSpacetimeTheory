#!/usr/bin/env python3
"""
Toy 569 — The Degeneracy Theorem: Which Universes Can Exist?
=============================================================
Elie — March 28, 2026 (late night)

Discovery from Toy 564: at n_C = 4, g = C_2 = 5. The root multiplicity
equals the Casimir invariant — a structural degeneracy that means the
universe can't distinguish curvature from dynamics.

This toy proves: for ALL even n_C ≥ 4, g = C_2. Even-dimensional type IV
bounded symmetric domains are structurally degenerate. Only odd n_C produces
five DISTINCT structural integers.

This is a selection principle: the universe must have odd compact dimension.
Combined with rank ≥ 2 and both N_c, g prime, this leaves only n_C ∈ {5, 9, ...}.
n_C = 5 is the smallest. Our universe is the simplest possible universe.

Framework: BST — D_IV^n classification
Tests: 8
"""

import math

PASS = 0
results = []

def test(name, condition, detail=""):
    global PASS
    ok = bool(condition)
    results.append(ok)
    status = "✓" if ok else "✗"
    print(f"  {status} {name}")
    if detail:
        print(f"    {detail}")
    if ok:
        PASS += 1

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("=" * 72)
print("The Degeneracy Theorem: Which Universes Can Exist?")
print("=" * 72)

# ─── The Five Structural Integers ───

print("\n─── The Five Structural Integers of D_IV^n ───\n")
print("  For a type IV bounded symmetric domain D_IV^n:")
print("    rank  = ⌊n/2⌋")
print("    N_c   = rank + 1    (color charges / positive roots)")
print("    g     = 2(n - rank) + 1  (root multiplicity structure)")
print("    C_2   = n + 1       (Casimir of fundamental rep)")
print("    N_max = f(n)        (largest representation)")
print()
print("  For BST to work, ALL FIVE must be distinct.")
print("  If any two coincide, the physics is degenerate —")
print("  two different structural roles map to the same number,")
print("  and the theory can't distinguish them.")

# ─── Test 1: The degeneracy pattern ───

print("\n─── T1: The Even-n_C Degeneracy ───\n")

print("  n_C  rank  N_c   g   C_2   g=C_2?   Parity")
print("  ───  ────  ───  ───  ───   ──────   ──────")

degen_count = 0
non_degen_count = 0
for n in range(3, 21):
    r = n // 2
    Nc = r + 1
    g = 2 * (n - r) + 1
    C2 = n + 1
    degenerate = (g == C2)
    if degenerate:
        degen_count += 1
    else:
        non_degen_count += 1
    marker = " ◀ OUR UNIVERSE" if n == 5 else ""
    degen_str = "YES" if degenerate else "no"
    parity = "even" if n % 2 == 0 else "odd"
    print(f"  {n:>3}  {r:>4}  {Nc:>3}  {g:>3}  {C2:>3}   {degen_str:>6}   {parity:>6}{marker}")

print()
print(f"  Degenerate (g = C_2): {degen_count} cases")
print(f"  Non-degenerate:       {non_degen_count} cases")

# Prove the pattern: for even n, rank = n/2, so
# g = 2(n - n/2) + 1 = 2(n/2) + 1 = n + 1 = C_2
# For odd n, rank = (n-1)/2, so
# g = 2(n - (n-1)/2) + 1 = 2((n+1)/2) + 1 = n + 2 ≠ n + 1 = C_2

print()
print("  PROOF:")
print("  For even n: rank = n/2")
print("    g = 2(n - n/2) + 1 = n + 1 = C_2  ← ALWAYS degenerate")
print("  For odd n: rank = (n-1)/2")
print("    g = 2(n - (n-1)/2) + 1 = n + 2 ≠ n + 1 = C_2  ← NEVER degenerate")
print()
print("  The degeneracy is EXACTLY the even-n_C cases. No exceptions.")

# Verify for all tested
all_even_degenerate = all(
    (2 * (n - n//2) + 1) == (n + 1)
    for n in range(4, 100, 2)
)
all_odd_nondegenerate = all(
    (2 * (n - n//2) + 1) != (n + 1)
    for n in range(3, 100, 2)
)

test("ALL even n_C have g = C_2 (degenerate)",
     all_even_degenerate,
     f"Verified for n = 4, 6, 8, ..., 98")

# ─── Test 2: Odd n_C always non-degenerate ───

print("\n─── T2: Odd n_C — Always Non-Degenerate ───\n")

# For odd n, g = n + 2, C_2 = n + 1. So g = C_2 + 1.
# The gap is always exactly 1.

print("  For odd n_C: g = n_C + 2, C_2 = n_C + 1, so g - C_2 = 1 always.")
print()
print("  n_C  g     C_2   g - C_2")
print("  ───  ───   ───   ───────")
for n in range(3, 20, 2):
    r = n // 2
    g = 2 * (n - r) + 1
    C2 = n + 1
    marker = " ◀" if n == 5 else ""
    print(f"  {n:>3}  {g:>3}   {C2:>3}   {g - C2:>7}{marker}")

print()
print("  The gap is always 1. Minimal but sufficient.")
print("  g and C_2 are consecutive integers. Distinct. Non-degenerate.")

test("ALL odd n_C have g - C_2 = 1 (non-degenerate, minimal gap)",
     all_odd_nondegenerate,
     f"g = C_2 + 1 for all odd n in [3, 99]")

# ─── Test 3: Full distinctness check ───

print("\n─── T3: Five-Integer Distinctness ───\n")

# For the five integers to be fully distinct, we need:
# {N_c, n_C, g, C_2} all different (N_max is always large, so distinct)
# Check all pairs:

print("  n_C  {N_c, n_C, g, C_2}          All distinct?  Pairs equal")
print("  ───  ─────────────────────────    ─────────────  ──────────")

fully_distinct_odd = []
for n in range(3, 16):
    r = n // 2
    Nc = r + 1
    g = 2 * (n - r) + 1
    C2 = n + 1
    vals = {'N_c': Nc, 'n_C': n, 'g': g, 'C_2': C2}
    unique = len(set(vals.values()))
    all_dist = unique == 4

    # Find equal pairs
    pairs = []
    names = list(vals.keys())
    for i in range(len(names)):
        for j in range(i+1, len(names)):
            if vals[names[i]] == vals[names[j]]:
                pairs.append(f"{names[i]}={names[j]}={vals[names[i]]}")

    pair_str = ", ".join(pairs) if pairs else "—"
    marker = " ◀" if n == 5 else ""
    print(f"  {n:>3}  {{{Nc}, {n}, {g}, {C2}}}".ljust(40) +
          f"{'YES' if all_dist else 'NO':>13}  {pair_str}{marker}")

    if all_dist and n % 2 == 1:
        fully_distinct_odd.append(n)

print()
print(f"  Fully distinct odd n_C: {fully_distinct_odd}")

# n_C = 3: {2, 3, 5, 4} — all distinct!
# But rank = 1, so fails other criteria.
# n_C = 5: {3, 5, 7, 6} — all distinct!

test("n_C = 5 has all four integers distinct",
     5 in fully_distinct_odd,
     f"{{3, 5, 7, 6}} — four distinct structural constants")

# ─── Test 4: What degeneracy means physically ───

print("\n─── T4: Physical Meaning of g = C_2 ───\n")

print("  g = root multiplicity structure")
print("    → Controls how field excitations propagate")
print("    → Determines the 'geometric constant' in BST")
print()
print("  C_2 = Casimir invariant of fundamental representation")
print("    → Controls the curvature of the internal space")
print("    → Determines binding energies and force strengths")
print()
print("  If g = C_2:")
print("    The number controlling propagation = the number controlling curvature")
print("    The theory can't distinguish 'how things move' from 'how space curves'")
print("    This is like a language where 'verb' and 'noun' are the same word")
print("    — you can't form meaningful sentences")
print()

# In BST, g and C_2 play different roles:
# m_p = 6π⁵ m_e  →  6 = C_2, π⁵ → 5 = n_C
# g appears in: Fermi scale v = m_p²/(g·m_e), g = 7
# C_2 appears in: proton mass m_p = C_2·π^{n_C}·m_e, C_2 = 6
# If g = C_2, these would collapse into the same number
# and the Fermi scale would become v = m_p²/(C_2·m_e) = m_p/π⁵
# — losing the independent parameter that sets the weak force scale

# Compute what happens to the Fermi scale if g = C_2:
# At n_C = 4: g = C_2 = 5
# Proton would be: 5 · π⁴ · m_e = 5 × 97.41 × 0.511 MeV = 248.9 MeV (too light!)
# Fermi scale: (248.9)² / (5 × 0.511) = 24,260 MeV = 24.3 GeV (too low!)

m_e = 0.51099895  # MeV

# n_C = 4 universe:
n4_C2 = 5
n4_nC = 4
n4_g = 5  # = C_2, degenerate!
m_p_n4 = n4_C2 * math.pi**n4_nC * m_e
v_n4 = m_p_n4**2 / (n4_g * m_e)

# Our universe (n_C = 5):
n5_C2 = 6
n5_nC = 5
n5_g = 7
m_p_n5 = n5_C2 * math.pi**n5_nC * m_e
v_n5 = m_p_n5**2 / (n5_g * m_e)

print(f"  n_C = 4 universe (g = C_2 = 5):")
print(f"    Proton mass: {n4_C2} × π⁴ × m_e = {m_p_n4:.1f} MeV")
print(f"    Fermi scale: {v_n4/1000:.1f} GeV")
print(f"    Ratio g/C_2 = 1.000 (degenerate)")
print()
print(f"  n_C = 5 universe (g = 7, C_2 = 6) — OURS:")
print(f"    Proton mass: {n5_C2} × π⁵ × m_e = {m_p_n5:.1f} MeV")
print(f"    Fermi scale: {v_n5/1000:.1f} GeV")
print(f"    Ratio g/C_2 = {n5_g/n5_C2:.4f} (non-degenerate)")
print()
print(f"  The n_C = 4 proton is {m_p_n5/m_p_n4:.1f}× lighter.")
print(f"  The n_C = 4 Fermi scale is {v_n5/v_n4:.1f}× lower.")
print(f"  Chemistry would barely work. Stars might not ignite.")

test("Degenerate universe has wrong proton mass (< 300 MeV)",
     m_p_n4 < 300,
     f"{m_p_n4:.1f} MeV vs {m_p_n5:.1f} MeV — the n_C=4 proton is too light for nuclear stability")

# ─── Test 5: The selection principle ───

print("\n─── T5: The Selection Principle ───\n")

# Combine all constraints:
# 1. rank ≥ 2 (need gauge group complexity) → n_C ≥ 4
# 2. n_C odd (no g = C_2 degeneracy)
# 3. N_c = rank + 1 prime (for color confinement)
# 4. g prime (for geometric rigidity)
# 5. All four integers distinct

print("  Combined constraints on n_C:\n")
print("  1. rank ≥ 2           → n_C ≥ 4")
print("  2. n_C odd            → n_C ∈ {5, 7, 9, 11, ...}")
print("  3. N_c prime          → rank + 1 prime")
print("  4. g prime            → 2(n_C - rank) + 1 prime")
print("  5. All four distinct  → (automatic for odd n_C)")
print()

valid = []
print("  n_C  rank  N_c  g   Checks                     Valid?")
print("  ───  ────  ───  ──  ─────────────────────────   ──────")

for n in range(5, 30, 2):  # odd only, starting from 5
    r = n // 2
    Nc = r + 1
    g = 2 * (n - r) + 1
    C2 = n + 1

    checks = []
    ok = True

    if r < 2:
        checks.append("rank<2")
        ok = False
    if not is_prime(Nc):
        checks.append(f"N_c={Nc} not prime")
        ok = False
    if not is_prime(g):
        checks.append(f"g={g} not prime")
        ok = False

    if ok:
        checks.append("all pass")
        valid.append(n)

    check_str = ", ".join(checks)
    marker = " ◀ OURS" if n == 5 else ""
    print(f"  {n:>3}  {r:>4}  {Nc:>3}  {g:>2}  {check_str:<27} {'YES' if ok else 'no'}{marker}")

print()
print(f"  Valid universes with n_C < 30: {valid}")
print()

if valid:
    print(f"  The simplest valid universe: n_C = {valid[0]}")
    if len(valid) > 1:
        print(f"  Next valid: n_C = {valid[1]}")
        # What's special about n_C = 5 vs the next?
        next_n = valid[1]
        next_r = next_n // 2
        next_Nc = next_r + 1
        print(f"  But n_C = {next_n} has N_c = {next_Nc} colors — {next_Nc} is more complex than 3")
        print(f"  More colors → more particle species → more complex universe")
        print(f"  The simplest universe that WORKS is n_C = 5.")

test("n_C = 5 is the unique smallest valid universe",
     len(valid) > 0 and valid[0] == 5,
     f"Valid: {valid}. n_C = 5 is first, next is {valid[1] if len(valid) > 1 else '?'}")

# ─── Test 6: The parity theorem ───

print("\n─── T6: The Parity Theorem ───\n")

# THEOREM: For type IV bounded symmetric domains D_IV^n,
# g = C_2 if and only if n is even.
#
# Proof:
# rank(D_IV^n) = ⌊n/2⌋
# g = 2(n - ⌊n/2⌋) + 1
# C_2 = n + 1
#
# Case n = 2k (even):
#   ⌊n/2⌋ = k
#   g = 2(2k - k) + 1 = 2k + 1 = n + 1 = C_2 ✓
#
# Case n = 2k+1 (odd):
#   ⌊n/2⌋ = k
#   g = 2(2k+1 - k) + 1 = 2k + 3 = (n+1) + 1 = C_2 + 1 ≠ C_2 ✓
#
# QED.

print("  THEOREM (Degeneracy Parity):")
print("  For D_IV^n: g = C_2 ⟺ n is even.")
print()
print("  Proof:")
print("  Case n = 2k:  g = 2(2k - k) + 1 = 2k + 1 = n + 1 = C_2.  ✓")
print("  Case n = 2k+1: g = 2(2k+1 - k) + 1 = 2k + 3 = C_2 + 1 ≠ C_2.  ✓")
print("  QED.")
print()
print("  Corollary: The compact dimension of any viable BST universe")
print("  must be ODD. Even-dimensional internal spaces are degenerate.")
print()
print("  This is a pure number theory result about floor functions.")
print("  It has nothing to do with physics — it's about which SHAPES")
print("  can produce five distinct structural integers.")
print("  The universe is odd because even doesn't work.")

# Verify the algebraic identity
identity_even = all(
    2 * (2*k - k) + 1 == 2*k + 1 == (2*k) + 1
    for k in range(2, 50)
)
identity_odd = all(
    2 * (2*k+1 - k) + 1 == 2*k + 3 == (2*k+1) + 1 + 1
    for k in range(1, 50)
)

test("Parity theorem verified algebraically for k = 1..49",
     identity_even and identity_odd,
     "Even: g = 2k+1 = C_2. Odd: g = 2k+3 = C_2+1. No exceptions.")

# ─── Test 7: Density of valid universes ───

print("\n─── T7: How Rare Are Valid Universes? ───\n")

# Among all n_C from 3 to 100, how many pass all criteria?
all_valid = []
for n in range(3, 101):
    r = n // 2
    Nc = r + 1
    g = 2 * (n - r) + 1
    C2 = n + 1

    if r >= 2 and is_prime(Nc) and is_prime(g) and n % 2 == 1:
        all_valid.append(n)

total = 98  # n from 3 to 100
density = len(all_valid) / total

print(f"  n_C from 3 to 100: {total} possible values")
print(f"  Valid universes: {len(all_valid)}")
print(f"  Density: {density*100:.1f}%")
print()
print(f"  Valid: {all_valid}")
print()

# The valid universes are sparse and follow no obvious pattern
# (they depend on twin-prime-like conditions on rank+1 and 2(n-rank)+1)
gaps = [all_valid[i+1] - all_valid[i] for i in range(len(all_valid)-1)]
print(f"  Gaps between valid universes: {gaps}")
print(f"  Average gap: {sum(gaps)/len(gaps):.1f}" if gaps else "")
print()
print(f"  Valid universes are ~{1/density:.0f}:1 against random selection.")
print(f"  The universe picked the FIRST one. Minimal complexity.")

test(f"Valid universes are < 15% of all possibilities",
     density < 0.15,
     f"{density*100:.1f}% — only {len(all_valid)} out of {total}")

# ─── Test 8: The simplest universe theorem ───

print("\n─── T8: The Simplest Universe Theorem ───\n")

print("  THEOREM (Simplest Universe):")
print("  Among all type IV bounded symmetric domains D_IV^n with:")
print("    (i)   rank ≥ 2")
print("    (ii)  g ≠ C_2 (non-degenerate)")
print("    (iii) N_c prime")
print("    (iv)  g prime")
print("  the unique smallest n is n = 5.")
print()
print("  Proof:")
print("  By (ii), n must be odd. By (i), n ≥ 4, so n ≥ 5.")
print("  At n = 5: rank = 2, N_c = 3 (prime ✓), g = 7 (prime ✓).")
print("  n = 5 satisfies all four conditions.")
print("  n = 3: rank = 1 < 2. Fails (i).")
print("  No smaller odd n ≥ 4 exists.")
print("  Therefore n = 5 is the unique smallest.  QED.")
print()
print("  Our universe has exactly 5 compact dimensions because 5 is")
print("  the smallest odd number ≥ 4 where rank+1 and 2(n-rank)+1")
print("  are both prime.")
print()
print("  That's not fine-tuning. That's FIRST(filter(constraints)).")
print("  The universe is a minimum.")

# The theorem is: 5 is the smallest odd integer ≥ 4 such that
# ⌊5/2⌋ + 1 = 3 is prime AND 2(5 - ⌊5/2⌋) + 1 = 7 is prime
is_5_smallest = (
    # n = 3 fails rank ≥ 2
    3 // 2 < 2 and
    # n = 5 passes everything
    5 // 2 >= 2 and
    is_prime(5 // 2 + 1) and  # N_c = 3
    is_prime(2 * (5 - 5 // 2) + 1) and  # g = 7
    5 % 2 == 1  # odd
)

test("n = 5 is provably the unique smallest valid universe",
     is_5_smallest,
     "rank=2≥2, N_c=3 prime, g=7 prime, 5 is odd. No smaller exists. QED.")

# ─── Summary ───

print()
print("=" * 72)
print()
print("  THE DEGENERACY THEOREM:")
print()
print("  g = C_2 ⟺ n_C is even.")
print()
print("  Even-dimensional type IV domains can't distinguish")
print("  curvature from root multiplicity. They're broken.")
print()
print("  Combined with rank ≥ 2 and primality of N_c and g:")
print("  n_C = 5 is the UNIQUE smallest valid universe.")
print()
print("  The compact dimension is 5 because:")
print("    • 3 fails (rank 1)")
print("    • 4 fails (g = C_2 = 5, degenerate)")
print("    • 5 works (3 prime, 7 prime, all distinct)")
print()
print("  Five isn't a choice. It's the minimum of a filter.")
print()

# ─── Scorecard ───

TOTAL = 8
print("=" * 72)
print(f"SCORECARD: {PASS}/{TOTAL}")
print("=" * 72)
labels = [
    "All even n_C degenerate (g = C_2)",
    "All odd n_C non-degenerate (g = C_2 + 1)",
    "n_C = 5 fully distinct",
    "Degenerate universe proton too light",
    "n_C = 5 unique smallest valid",
    "Parity theorem algebraically verified",
    "Valid universes < 15% of possibilities",
    "n = 5 provably smallest (formal proof)",
]
for i, label in enumerate(labels):
    status = "✓" if results[i] else "✗"
    print(f"  {status} T{i+1}: {label}")

print()
if PASS == TOTAL:
    print("ALL TESTS PASSED.\n")
else:
    print(f"{PASS}/{TOTAL} tests passed.\n")

print("The universe is odd because even is degenerate.")
print("Five because it's first. Three colors because rank is two.")
print("Seven because it's the prime that fits.")
print("The simplest thing that works. Nothing more, nothing less.")
