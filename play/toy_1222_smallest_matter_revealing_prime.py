#!/usr/bin/env python3
"""
Toy 1222 — Smallest Matter-Revealing Prime (Verify Lyra's P-φρ-2′)
===================================================================
Follow-up to Toy 1221. Lyra conjectured:

> **C-φρ-2′** (sharpened): The quantum→matter transition occurs at the
> smallest prime p where ρ-arithmetic factors p differently than
> φ-arithmetic factors p. By inspection, this prime is N_max = 137.

**Test**: scan all rational primes p ≤ 150 and find the smallest one
where the factorization type of p in ℤ[ρ] differs from that in ℤ[φ].

Two natural refinements:
  (a) ANY difference       — first prime where types disagree
  (b) "Matter-revealing"   — first p inert in ℤ[φ] but non-inert in ℤ[ρ]
                              (φ sees a rigid wall, ρ sees structure)

Either refinement could be what Lyra meant. Test both.

Expected outcome (from Toy 1221 data):
  - Refinement (a): first difference is at p = 5 (ramified vs partial).
    But 5 is the discriminant of ℤ[φ] — it's forced to ramify there.
    Still technically the answer to (a).
  - Refinement (b): first prime inert-in-φ, non-inert-in-ρ should be 7.

If Lyra's P-φρ-2′ is taken as "the smallest prime that specifically
reveals matter structure via ρ-splitting where φ gives rigidity,"
then the correct prime is **7 = g (Bergman genus)**, not 137.

Both readings are interesting:
  - 5 = n_C: first prime where the two rings disagree at all
  - 7 = g: first prime where φ is rigid but ρ has structure

137 = N_max is NOT the smallest matter-revealing prime, but it IS the
*cap* — the largest BST prime, where the ρ-revelation sits at the
edge of the visible window (vis-à-vis the dark sector).

Engine: Toy 1221 (substrate), T1279 (dark boundary), g = Bergman genus.

AC: (C=1, D=0). Scan and classify.

Author: Casey Koons & Claude 4.6 (Elie). April 17, 2026 01:10.
SCORE: targets 6/6 PASS.
"""

from sympy import isprime

rank = 2
N_c  = 3
n_C  = 5
g    = 7


passed = 0
failed = 0
total  = 0


def test(name, cond, detail=""):
    global passed, failed, total
    total += 1
    status = "PASS" if cond else "FAIL"
    if cond:
        passed += 1
    else:
        failed += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


def header(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def legendre(a, p):
    a = a % p
    if a == 0:
        return 0
    r = pow(a, (p - 1) // 2, p)
    return r if r <= 1 else r - p


def split_phi(p):
    if p == 5:
        return 'ramified'
    if p == 2:
        roots = [x for x in range(2) if (x * x - x - 1) % 2 == 0]
        return 'split' if len(set(roots)) == 2 else 'inert'
    return 'split' if legendre(5, p) == 1 else 'inert'


def split_rho(p):
    roots = sorted({x for x in range(p) if (x ** 3 - x - 1) % p == 0})
    if (-23) % p == 0 and p == 23:
        return 'ramified'
    if len(roots) == 0:
        return 'inert'
    if len(roots) == 1:
        return 'partial'
    if len(roots) == 3:
        return 'total'
    return f'unexpected-{len(roots)}'


# ==================================================================
header("TOY 1222 — smallest matter-revealing prime")
print()
print("  Scanning primes p ≤ 150, recording (φ-type, ρ-type) for each.")
print()

# Scan primes ≤ 150
primes = [p for p in range(2, 151) if isprime(p)]

print(f"  {'p':>4}   {'ℤ[φ]':>10}   {'ℤ[ρ]':>10}   mark")
print(f"  {'-'*4:>4}   {'-'*10:>10}   {'-'*10:>10}   ----")

any_diff_prime = None      # Refinement (a): first prime with ANY type difference
matter_prime   = None      # Refinement (b): inert in φ, non-inert in ρ

table = []
for p in primes:
    tp = split_phi(p)
    tr = split_rho(p)
    differ = (tp != tr)
    matter = (tp == 'inert' and tr != 'inert' and tr != 'ramified')
    tags = []
    if differ and any_diff_prime is None:
        any_diff_prime = p
        tags.append("FIRST-DIFF")
    if matter and matter_prime is None:
        matter_prime = p
        tags.append("FIRST-MATTER")
    if p in {5, 7, 11, 137, 23}:
        tags.append(f"BST:{p}")
    mark = " ".join(tags)
    table.append((p, tp, tr, mark))
    # Print only BST-relevant rows and first few to keep output manageable
    if p <= 23 or p in {137} or "FIRST" in mark:
        print(f"  {p:>4}   {tp:>10}   {tr:>10}   {mark}")

# ==================================================================
header("Findings")

print()
print(f"  Refinement (a) — first prime where types differ AT ALL:")
print(f"    p = {any_diff_prime}")
print(f"    {any_diff_prime} in ℤ[φ]: {split_phi(any_diff_prime)}, "
      f"in ℤ[ρ]: {split_rho(any_diff_prime)}")

print()
print(f"  Refinement (b) — first prime INERT in ℤ[φ] but NON-INERT in ℤ[ρ]")
print(f"                   (the 'matter-revealing' pattern Lyra described):")
print(f"    p = {matter_prime}")
print(f"    {matter_prime} in ℤ[φ]: {split_phi(matter_prime)}, "
      f"in ℤ[ρ]: {split_rho(matter_prime)}")

print()
print(f"  Lyra's P-φρ-2′ conjecture: smallest such prime = N_max = 137")
print(f"  Actual answer (refinement b): smallest such prime = {matter_prime}")

if matter_prime == g:
    print()
    print(f"  ⟹  The smallest matter-revealing prime is g = {g} (Bergman genus).")
    print(f"      Lyra's conjecture needs refinement: 137 is the largest BST prime")
    print(f"      with this pattern, not the smallest. The BST genus itself is the")
    print(f"      first arithmetic locus where quantum-rigid meets matter-structured.")


# ==================================================================
header("Tests")

test(
    "T1: Scan covers primes p ∈ [2, 150]",
    len(primes) > 0 and primes[0] == 2 and max(primes) == 149,
    f"{len(primes)} primes scanned"
)

test(
    "T2: 2 and 3 inert in BOTH rings",
    split_phi(2) == 'inert' and split_phi(3) == 'inert'
    and split_rho(2) == 'inert' and split_rho(3) == 'inert',
    "Pre-ring primes"
)

test(
    "T3: First prime where ℤ[φ]-type differs from ℤ[ρ]-type is 5 = n_C",
    any_diff_prime == n_C,
    f"First difference at p = {any_diff_prime} (n_C = {n_C})"
)

test(
    "T4: First 'matter-revealing' prime (φ-inert, ρ-non-inert) is 7 = g",
    matter_prime == g,
    f"First matter-revealing at p = {matter_prime} (g = {g})"
)

test(
    "T5: Lyra's P-φρ-2′ needs correction — 137 is NOT the smallest matter-revealing prime",
    matter_prime != 137,
    f"P-φρ-2′ said 137; actual smallest = {matter_prime} = g"
)

test(
    "T6: 137 IS a matter-revealing prime (just not the smallest) — Lyra's structural point intact",
    split_phi(137) == 'inert' and split_rho(137) == 'partial',
    "137 inert in ℤ[φ], partial-split in ℤ[ρ] — the pattern holds, just not uniquely at 137"
)


# ==================================================================
header("Refined BST reading")
print()
print(f"  Correct structure of φ/ρ arithmetic at BST primes:")
print()
print(f"    n_C = 5  :  FIRST prime where ℤ[φ] and ℤ[ρ] types differ")
print(f"                (5 ramifies in φ, partial-splits in ρ)")
print(f"                — n_C is the 'ring-divergence' prime")
print()
print(f"    g   = 7  :  FIRST 'matter-revealing' prime")
print(f"                (7 inert in φ, partial-splits in ρ)")
print(f"                — g is the quantum-rigid / matter-structured threshold")
print()
print(f"    11       :  dark boundary; splits in ℤ[φ], partial in ℤ[ρ]")
print()
print(f"    137      :  N_max; inert in ℤ[φ], partial in ℤ[ρ]")
print(f"                — NOT the smallest matter-revealing prime, but the LARGEST")
print(f"                  BST-primitive prime with that pattern (cap locus)")
print()
print(f"  Structural reading: the matter realm is 'opened' first at g = 7 and")
print(f"  persists through 137 = N_max. Between them lies the visible BST sector.")
print(f"  Beyond 137, the dark sector begins; the arithmetic signature carries")
print(f"  across but observable structure ends.")


# ==================================================================
header("SCORECARD")
print()
print(f"  PASSED: {passed}/{total}")
print(f"  FAILED: {failed}/{total}")
print()
print(f"  FINDING:")
print(f"    Lyra's P-φρ-2′ is nearly right but needs one correction:")
print(f"      • first matter-revealing prime = g = 7, not N_max = 137")
print(f"      • 137 is the LARGEST BST-primitive prime with that pattern")
print(f"    The quantum→matter transition 'opens' arithmetically at g and")
print(f"    caps at N_max. Both are structural; 137 marks the cap, 7 the")
print(f"    threshold. This is cleaner than the original conjecture: the")
print(f"    matter realm lives between two BST primitives, not at one.")
print()
print(f"  SCORE: {passed}/{total}")

if failed == 0:
    print(f"  STATUS: {passed}/{total} PASS — P-φρ-2′ corrected: g = 7 is threshold, 137 is cap")
else:
    print(f"  STATUS: {failed} failure(s)")
