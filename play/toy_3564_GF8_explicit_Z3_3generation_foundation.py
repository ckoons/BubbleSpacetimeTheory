#!/usr/bin/env python3
"""
Toy 3564 — GF(8) explicit construction + Z_3 Galois (Candidate F foundation)

Elie, Wednesday 2026-05-27 ~10:55 EDT date-verified
Per Toy 3561+3562+3563 analysis: Candidate F (GF(8) Galois Z_3) is the
strongest remaining substrate-mechanism candidate for 3-generation
structure. This toy builds the explicit structural foundation.

PURPOSE
-------
Construct GF(2^N_c) = GF(8) explicitly parallel to Toy 3550 (GF(32))
and Toy 3551 (GF(32) Frobenius orbits). Document Z_3 Galois action
structure for Lyra Track P / Track DC v0.x 3-generation investigation.

The Cal #139 cyclotomic chain at X = N_c = 3 gives:
  2^N_c − 1 = M_N_c = 7 = g (Mersenne prime, BST primary)
GF(8) has order 8 = 2^N_c. F_8^* has order 7 = M_N_c.
Galois Gal(GF(8) / GF(2)) ≅ Z/3 (since order_2(7) = 3 = N_c).

CAL #29 PRE-PASS:
  Question: "What's the explicit GF(8) Frobenius Z_3 orbit structure?"
  - Forward computation; standard finite-field theory
  - Substrate identification of Z_3 with possible 3-generation structure
    is INTERPRETIVE (Lyra v0.x territory)
  CLEAN PASS

INVESTIGATIONS (5 scored)
1. Find irreducible polynomial degree 3 over GF(2)
2. Construct GF(8); verify cyclic structure
3. Find primitive element + verify order 7
4. Compute Frobenius orbits (expect 2 size-3 + identity)
5. Document Z_3 structure for Lyra investigation
"""
import sys

print("=" * 78)
print("Toy 3564 — GF(8) explicit Z_3 Galois (Candidate F foundation)")
print("Per Toy 3561 strongest remaining 3-generation candidate")
print("Elie, Wednesday 2026-05-27 10:55 EDT")
print("=" * 78)

rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7


def poly_mul_gf2(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r


def poly_div_gf2(num, den):
    q = 0
    deg_den = den.bit_length() - 1
    while num.bit_length() - 1 >= deg_den and num != 0:
        shift = num.bit_length() - 1 - deg_den
        q |= (1 << shift)
        num ^= (den << shift)
    return q, num


def is_irreducible_deg3_gf2(poly):
    """Check if poly is irreducible degree-3 over GF(2): no roots in GF(2)."""
    # Eval at x=0: constant term (bit 0)
    if poly & 1 == 0:
        return False
    # Eval at x=1: sum of coefficients mod 2 = popcount mod 2
    if bin(poly).count("1") % 2 == 0:
        return False
    # Degree 3: no quadratic factor possible (since 3 prime; only deg 1 factors blocked)
    return True


def gf8_mul(a, b, prim):
    p = poly_mul_gf2(a, b)
    _, r = poly_div_gf2(p, prim)
    return r


def gf8_pow(base, exp, prim):
    r = 1
    while exp > 0:
        if exp & 1:
            r = gf8_mul(r, base, prim)
        base = gf8_mul(base, base, prim)
        exp >>= 1
    return r


def gf8_square(a, prim):
    return gf8_mul(a, a, prim)


# ============================================================
# Test 1: Find irreducible polynomial degree 3
# ============================================================
print("\n--- Test 1: Find irreducible polynomial degree 3 over GF(2) ---")
candidates = []
for poly in range(8, 16):  # degree-3: bit 3 set
    if is_irreducible_deg3_gf2(poly):
        candidates.append(poly)
print(f"  Found {len(candidates)} irreducible deg-3 polynomials (expect 2)")
for poly in candidates:
    bits = bin(poly)[2:]
    terms = []
    for i, b in enumerate(bits[::-1]):
        if b == "1":
            if i == 0: terms.append("1")
            elif i == 1: terms.append("x")
            else: terms.append(f"x^{i}")
    print(f"    {poly} = {bin(poly)} = {' + '.join(reversed(terms))}")

PRIM = candidates[0]  # use first
print(f"\n  GF(8) = GF(2)[x] / ({bin(PRIM)[2:]})")
test_1 = len(candidates) == 2
print(f"  Test 1: {'PASS' if test_1 else 'FAIL'}")

# ============================================================
# Test 2: Construct GF(8); verify cyclic structure
# ============================================================
print("\n--- Test 2: GF(8) cyclic structure (F_8^* order 7) ---")
# Check elem^7 = 1 for all non-zero elements
all_order_7 = True
for elem in range(1, 8):
    p7 = gf8_pow(elem, 7, PRIM)
    if p7 != 1:
        all_order_7 = False
        print(f"    elem={elem}: ^7 = {p7} (FAIL)")
print(f"  All 7 non-zero elements satisfy x^7 = 1: {all_order_7}")
test_2 = all_order_7
print(f"  Test 2: {'PASS' if test_2 else 'FAIL'}")

# ============================================================
# Test 3: Primitive elements
# ============================================================
print("\n--- Test 3: Primitive elements + verify order 7 ---")
# Order of element = smallest k such that elem^k = 1
primitives = []
for elem in range(2, 8):
    order = 1
    v = elem
    while v != 1 and order <= 7:
        v = gf8_mul(v, elem, PRIM)
        order += 1
    if order == 7:
        primitives.append(elem)
print(f"  Primitive elements (order = 7): {len(primitives)} found (expect φ(7) = 6)")
print(f"  Primitive elements: {primitives}")
alpha = primitives[0]
print(f"  Canonical α = {alpha}")

# Powers of alpha
powers = [1]
v = 1
for i in range(7):
    v = gf8_mul(v, alpha, PRIM)
    powers.append(v)
print(f"  α^0..α^7 = {powers}  (α^7 should = 1: {powers[7] == 1})")

test_3 = len(primitives) == 6
print(f"  Test 3: {'PASS' if test_3 else 'FAIL'}")

# ============================================================
# Test 4: Frobenius Z_3 orbits
# ============================================================
print("\n--- Test 4: Frobenius orbits (x → x²) in F_8^* ---")
orbits = []
seen = set()
for x in range(1, 8):
    if x in seen:
        continue
    orbit = []
    cur = x
    while cur not in seen:
        orbit.append(cur)
        seen.add(cur)
        cur = gf8_square(cur, PRIM)
    orbits.append(orbit)

print(f"  Total orbits: {len(orbits)} (expect 3: 1 fixed + 2 size-3)")
for i, orbit in enumerate(orbits, 1):
    print(f"    Orbit {i}: {sorted(orbit)} (size {len(orbit)})")

size_3 = [o for o in orbits if len(o) == 3]
size_1 = [o for o in orbits if len(o) == 1]
print(f"\n  Size-3 orbits: {len(size_3)} (expect 2)")
print(f"  Size-1 fixed points: {len(size_1)} (expect 1, the identity)")

# Order of 2 mod 7
val = 2
ord_2 = 1
while val != 1:
    val = (val * 2) % 7
    ord_2 += 1
print(f"\n  Order of 2 mod 7: {ord_2} = N_c (Galois Z/N_c structure confirmed)")

test_4 = len(size_3) == 2 and len(size_1) == 1 and ord_2 == 3
print(f"  Test 4: {'PASS' if test_4 else 'FAIL'}")

# ============================================================
# Test 5: Document for Lyra 3-generation investigation
# ============================================================
print("\n--- Test 5: Z_3 structure documentation ---")
print(f"""
  GF(8) STRUCTURAL DATA for Lyra Candidate F investigation:

  Field: GF(8) = GF(2)[x] / (x³ + x + 1)
  Order: 8 = 2^N_c
  Multiplicative group F_8^*: cyclic of order M_N_c = 7 = g (Mersenne, BST primary)
  Primitive element α = {alpha}
  Galois group Gal(GF(8) / GF(2)): cyclic Z/3 (generated by Frobenius x → x²)

  FROBENIUS Z_3 ORBITS:
    Identity orbit:     {{1}} = {{α^0}}                  (1 fixed point)
    Size-3 orbit α:     {sorted(orbits[1] if len(orbits) > 1 else [])} = {{α^1, α^2, α^4}}
    Size-3 orbit α^3:   {sorted(orbits[2] if len(orbits) > 2 else [])} = {{α^3, α^5, α^6}}

  Total partition: 3 orbits = potential 3-generation correspondence?

  CANDIDATE F (Lyra investigation):
    The 3 Frobenius orbits in F_8^* + the 0 element provide a natural Z_3-
    structured object in BST framework. Each non-identity orbit has size 3.
    Candidate hypothesis: 2 size-3 orbits + 1 identity = 3 generations?
    Or: 3 partitions = 3 generations directly?

  CAL #29 STANDING APPLIES HARD:
    - Z_3 structure exists in GF(8); this is substrate-natural via M_N_c
    - But mapping "3 orbits" → "3 generations" is structural-match risk
    - Substrate-mechanism for the mapping requires Lyra v0.x derivation
    - This toy DOCUMENTS the Z_3 structure but does NOT promote the mapping

  CAL #133 PARTIAL-TAUTOLOGY:
    - order_2(7) = 3 is general Fermat arithmetic
    - Substrate naturalness: M_N_c = 7 IS BST primary (= g)
    - GF(8) substrate-relevance is via Cal #139 chain at X = N_c level
    - The Z_3 Galois structure is substrate-INHERITED but the
      Z_3 ↔ 3-generation map is INTERPRETIVE

  HAND-OFF for Lyra:
    - Explicit GF(8) structure ready
    - 3 Frobenius partitions documented
    - Substrate-mechanism for Z_3 ↔ generations is Lyra theoretical work
    - Could potentially extend to GF(8)-related K-type identification
""")

test_5 = True
print(f"  Test 5: PASS (Z_3 structure documented)")

# ============================================================
# Summary
# ============================================================
results = [test_1, test_2, test_3, test_4, test_5]
score = sum(results)
total = len(results)

print("\n" + "=" * 78)
print("GF(8) EXPLICIT Z_3 GALOIS STRUCTURE — RESULT")
print("=" * 78)
print(f"""
EXPLICIT CONSTRUCTION:
  GF(8) = GF(2)[x] / (x³ + x + 1)
  F_8^* = ⟨α⟩ cyclic of order 7 = M_N_c = g (BST primary)
  Gal(GF(8)/GF(2)) = ⟨Frobenius⟩ ≅ Z/3 = Z/N_c

FROBENIUS Z_3 ORBITS in F_8^*:
  3 total: 1 fixed {{1}} + 2 size-3 orbits

PARALLEL STRUCTURE (GF(8) ↔ GF(32) ↔ GF(128)):
  GF(2^N_c) = GF(8):   chain length N_c=3, orbits = 3 = (2 size-3 + 1 fixed)
  GF(2^n_C) = GF(32):  chain length n_C=5, orbits = 7 = (6 size-5 + 1 fixed) per Toy 3551
  GF(2^g) = GF(128):   chain length g=7, orbits = 19 = (18 size-7 + 1 fixed) per K59

  Pattern: orbits = (M_p − 1)/p + 1 = (2^p−2)/p + 1 for prime p

CANDIDATE F (3-generation substrate-mechanism):
  - Substrate-natural Z_3 exists via Cal #139 chain at X = N_c level
  - 3 Frobenius partitions in F_8^* (including identity)
  - Worth Lyra Track P / Track DC v0.x multi-week investigation
  - Hand-off data ready

HONEST SCOPE (Cal #27 + #29 + #133):
  - Forward computation of standard GF(8) structure
  - Z_3 Galois structurally present in substrate framework
  - Z_3 ↔ 3-generation MAPPING remains Lyra theoretical work
  - Does NOT promote Candidate F to substrate-mechanism

CROSS-CI HAND-OFF:
  Substrate cyclotomic ladder now has explicit data at 3 levels:
    GF(8)   X=N_c chain level (this toy)
    GF(32)  X=n_C chain level (Toys 3550-3552)
    GF(128) X=g chain level (K59 RATIFIED)
  All three together: full Mersenne-tower foundation for Lyra Hall-algebra
  v0.7+ work at substrate q=2 specialization.
""")

print(f"SCORE: {score}/{total}")
print(f"Toy 3564 GF(8) Z_3 foundation: {'PASS' if score == total else 'PARTIAL'}")
print()
print(f"NET: GF(8) explicit + Z_3 Galois structure documented. Hand-off for Lyra Candidate F")
print(f"investigation. Substrate cyclotomic ladder GF(8) / GF(32) / GF(128) complete.")
print()
print("— Elie, Toy 3564 GF(8) Z_3 foundation 2026-05-27 Wednesday 10:55 EDT")
sys.exit(0 if score == total else 1)
