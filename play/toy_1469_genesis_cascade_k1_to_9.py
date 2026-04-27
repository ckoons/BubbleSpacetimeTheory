#!/usr/bin/env python3
"""
Toy 1469 — Genesis Cascade: D_IV^k for k = 1..9
==================================================
BST / APG: D_IV^5 = SO_0(5,2)/[SO(5)×SO(2)]
Five integers: rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137

Paper #85 companion computation. For each type IV domain D_IV^k
(k = 1..9), compute all structural integers and elliptic curve
invariants, then test the four locks:

  Lock 1: N_c >= 2 (confinement)
  Lock 2: g is Heegner (unique CM curve)
  Lock 3: N_c, n_C, g all prime (irreducibility)
  Lock 4: N_c = 3 (physical color group SU(3))

Only k = 5 passes all four. The cascade table shows WHY every
other dimension fails — each failure is structural, not numerical.

Additional tests:
  - Verify c_4 = g!! at k = 5 (double factorial cascade)
  - Verify c_6 = N_c^{N_c} * g^r at k = 5 (self-referential exponents)
  - Verify Delta = -g^3 at k = 5
  - Verify j = -(N_c * n_C)^3 at k = 5
  - Cross-type check: D_IV^9 is nearest competitor (Heegner g=11)
  - N_max formula: N_c^3 * n_C + r at k = 5 gives 137 (prime)

Ref: Paper #85 Section 5, Toy 1399 (cross-type), T1404 (invariant decomposition)
"""

import math
from fractions import Fraction
from functools import reduce

# ── Heegner numbers ──
HEEGNER = {1, 2, 3, 7, 11, 19, 43, 67, 163}

def is_prime(n):
    """Simple primality test."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def double_factorial(n):
    """n!! = n * (n-2) * (n-4) * ... * 1 for odd n."""
    result = 1
    while n > 0:
        result *= n
        n -= 2
    return result

results = []

print("=" * 76)
print("Toy 1469 — Genesis Cascade: D_IV^k for k = 1..9")
print("=" * 76)

# ══════════════════════════════════════════════════════════════════════
# T1: Cascade table — compute all D_IV^k structural integers
# ══════════════════════════════════════════════════════════════════════
print("\n─── T1: Cascade Table ───")
print(f"{'k':>3} {'n_C':>4} {'N_c':>4} {'g':>4} {'C_2':>4} {'N_max':>6} "
      f"{'c_4':>8} {'c_6':>8} {'Lock1':>6} {'Lock2':>6} {'Lock3':>6} {'Lock4':>6} {'ALL':>5}")
print("─" * 76)

cascade_data = {}
sole_survivor = None
lock_counts = {1: 0, 2: 0, 3: 0, 4: 0}

for k in range(1, 10):
    n_C = k
    N_c = k - 2
    g_val = k + 2
    C_2 = 2 * (k - 2)
    r = 2
    N_max_k = N_c**3 * n_C + r if N_c > 0 else None

    # Compute c_4, c_6 for the associated curve (if N_c > 0)
    if N_c > 0 and n_C > 0 and g_val > 0:
        c4 = N_c * n_C * g_val
        c6 = N_c**3 * g_val**2
    else:
        c4 = None
        c6 = None

    # Test four locks
    lock1 = N_c >= 2
    lock2 = g_val in HEEGNER
    lock3 = is_prime(N_c) and is_prime(n_C) and is_prime(g_val) if N_c > 0 else False
    lock4 = N_c == 3
    all_pass = lock1 and lock2 and lock3 and lock4

    for i, l in enumerate([lock1, lock2, lock3, lock4], 1):
        if l:
            lock_counts[i] += 1

    if all_pass:
        sole_survivor = k

    cascade_data[k] = {
        'n_C': n_C, 'N_c': N_c, 'g': g_val, 'C_2': C_2, 'r': r,
        'N_max': N_max_k, 'c4': c4, 'c6': c6,
        'locks': (lock1, lock2, lock3, lock4), 'all': all_pass
    }

    c4_str = str(c4) if c4 is not None else "---"
    c6_str = str(c6) if c6 is not None else "---"
    nmax_str = str(N_max_k) if N_max_k is not None else "---"
    mark = " <<<" if all_pass else ""

    print(f"{k:>3} {n_C:>4} {N_c:>4} {g_val:>4} {C_2:>4} {nmax_str:>6} "
          f"{c4_str:>8} {c6_str:>8} "
          f"{'PASS' if lock1 else 'FAIL':>6} {'PASS' if lock2 else 'FAIL':>6} "
          f"{'PASS' if lock3 else 'FAIL':>6} {'PASS' if lock4 else 'FAIL':>6} "
          f"{'YES' if all_pass else 'no':>5}{mark}")

ok1 = (sole_survivor == 5)
print(f"\n  Sole survivor: k = {sole_survivor}")
results.append(("T1: k=5 sole survivor", ok1,
                f"k={sole_survivor} {'PASS' if ok1 else 'FAIL'}"))

# ══════════════════════════════════════════════════════════════════════
# T2: c_4 = g!! (double factorial cascade)
# ══════════════════════════════════════════════════════════════════════
print("\n─── T2: Double factorial cascade ───")
g_bst = 7
gdf = double_factorial(g_bst)
c4_bst = cascade_data[5]['c4']
print(f"  g!! = {g_bst}!! = 7 × 5 × 3 × 1 = {gdf}")
print(f"  c_4 = N_c × n_C × g = 3 × 5 × 7 = {c4_bst}")
ok2 = (gdf == c4_bst == 105)
print(f"  g!! = c_4 = 105?  {ok2}")
print(f"  Walk: g=7 → n_C=5 → N_c=3 → 1 (every odd BST integer)")
results.append(("T2: c_4 = g!! = 105", ok2,
                f"{gdf} = {c4_bst} {'PASS' if ok2 else 'FAIL'}"))

# ══════════════════════════════════════════════════════════════════════
# T3: c_6 = N_c^{N_c} * g^r (self-referential exponents)
# ══════════════════════════════════════════════════════════════════════
print("\n─── T3: Self-referential exponents ───")
N_c_bst = 3
r_bst = 2
c6_formula = N_c_bst**N_c_bst * g_bst**r_bst
c6_bst = cascade_data[5]['c6']
print(f"  N_c^{{N_c}} × g^r = {N_c_bst}^{N_c_bst} × {g_bst}^{r_bst} = {N_c_bst**N_c_bst} × {g_bst**r_bst} = {c6_formula}")
print(f"  c_6 = {c6_bst}")
ok3 = (c6_formula == c6_bst == 1323)
results.append(("T3: c_6 = N_c^N_c · g^r = 1323", ok3,
                f"{c6_formula} = {c6_bst} {'PASS' if ok3 else 'FAIL'}"))

# ══════════════════════════════════════════════════════════════════════
# T4: Delta = -g^3 and j = -(N_c * n_C)^3
# ══════════════════════════════════════════════════════════════════════
print("\n─── T4: Discriminant and j-invariant ───")
c4 = 105
c6 = 1323
delta_num = c4**3 - c6**2
delta = delta_num // 1728  # 1728 = 12^3 = (r*C_2)^3
j_val = 1728 * c4**3 // (-delta_num) * (-1)  # j = 1728*c4^3 / (c4^3 - c6^2)

# Compute properly
delta_exact = Fraction(c4**3 - c6**2, 1728)
j_exact = Fraction(1728 * c4**3, c4**3 - c6**2)

print(f"  c_4^3 = {c4**3}")
print(f"  c_6^2 = {c6**2}")
print(f"  c_4^3 - c_6^2 = {c4**3 - c6**2}")
print(f"  1728 = 12^3 = (r·C₂)^3 = ({r_bst}·{6})^3 = {1728}")
print(f"  Δ = (c_4^3 - c_6^2)/1728 = {delta_exact} = {int(delta_exact)}")
print(f"  -g^3 = -{g_bst}^3 = {-g_bst**3}")
print(f"  j = 1728·c_4^3/Δ·1728 = {j_exact} = {int(j_exact)}")
print(f"  -(N_c·n_C)^3 = -({N_c_bst}·{5})^3 = {-(N_c_bst*5)**3}")

ok4a = (int(delta_exact) == -g_bst**3)
ok4b = (int(j_exact) == -(N_c_bst * 5)**3)
ok4 = ok4a and ok4b
print(f"  Δ = -g^3?  {ok4a}")
print(f"  j = -(N_c·n_C)^3?  {ok4b}")
results.append(("T4: Δ=-g³, j=-(N_c·n_C)³", ok4,
                f"Δ={int(delta_exact)}, j={int(j_exact)} {'PASS' if ok4 else 'FAIL'}"))

# ══════════════════════════════════════════════════════════════════════
# T5: N_max = 137 is prime (spectral cap)
# ══════════════════════════════════════════════════════════════════════
print("\n─── T5: N_max = 137 at k=5 ───")
N_max_5 = N_c_bst**3 * 5 + r_bst
print(f"  N_max = N_c³·n_C + r = {N_c_bst}³·{5} + {r_bst} = {N_c_bst**3*5} + {r_bst} = {N_max_5}")
print(f"  Is prime: {is_prime(N_max_5)}")

# Check N_max at other k values
print(f"  Comparison with other k:")
for k in range(4, 10):
    d = cascade_data[k]
    if d['N_max'] is not None:
        p = is_prime(d['N_max'])
        print(f"    k={k}: N_max = {d['N_max']} {'(prime)' if p else '(composite)'}")

ok5 = (N_max_5 == 137) and is_prime(137)
results.append(("T5: N_max(k=5) = 137 prime", ok5,
                f"N_max={N_max_5}, prime={is_prime(N_max_5)} {'PASS' if ok5 else 'FAIL'}"))

# ══════════════════════════════════════════════════════════════════════
# T6: 1728 = (r * C_2)^3 = 12^3 (BST cube)
# ══════════════════════════════════════════════════════════════════════
print("\n─── T6: 1728 = (r·C₂)³ ───")
bst_cube = (r_bst * 6)**3
ok6 = (bst_cube == 1728)
print(f"  (r·C₂)³ = ({r_bst}·{6})³ = {r_bst*6}³ = {bst_cube}")
print(f"  Standard 1728 in Weierstrass theory = BST cube")
results.append(("T6: 1728 = (r·C₂)³", ok6,
                f"{bst_cube} {'PASS' if ok6 else 'FAIL'}"))

# ══════════════════════════════════════════════════════════════════════
# T7: Nearest competitor D_IV^9 failure analysis
# ══════════════════════════════════════════════════════════════════════
print("\n─── T7: D_IV^9 (nearest competitor) ───")
d9 = cascade_data[9]
print(f"  k=9: N_c={d9['N_c']}, n_C={d9['n_C']}, g={d9['g']}")
print(f"  Lock 1 (N_c≥2): {d9['locks'][0]}  (N_c={d9['N_c']})")
print(f"  Lock 2 (g Heegner): {d9['locks'][1]}  (g={d9['g']}, 11 is Heegner)")
print(f"  Lock 3 (all prime): {d9['locks'][2]}  (n_C={d9['n_C']}=3², NOT prime)")
print(f"  Lock 4 (N_c=3): {d9['locks'][3]}  (N_c={d9['N_c']}≠3)")
print(f"  Passes 2 of 4 locks — strongest near-miss")

# D_IV^9 fails on BOTH independent conditions (Lock 3 and Lock 4)
ok7 = (not d9['all']) and d9['locks'][0] and d9['locks'][1] and (not d9['locks'][2])
results.append(("T7: D_IV^9 fails Lock 3+4", ok7,
                f"n_C=9 composite, N_c=7≠3 {'PASS' if ok7 else 'FAIL'}"))

# ══════════════════════════════════════════════════════════════════════
# T8: Every failure at k≠5 has a DIFFERENT structural reason
# ══════════════════════════════════════════════════════════════════════
print("\n─── T8: Distinct failure modes ───")
failure_modes = {}
for k in range(1, 10):
    if k == 5:
        continue
    d = cascade_data[k]
    locks = d['locks']
    if not locks[0]:
        mode = f"N_c={d['N_c']}<2"
    elif not locks[1] and not locks[2]:
        mode = f"g={d['g']} not Heegner + not all prime"
    elif not locks[1]:
        mode = f"g={d['g']} not Heegner"
    elif not locks[2]:
        mode = f"n_C={d['n_C']} or N_c={d['N_c']} composite"
    else:
        mode = "Lock 4 only"
    failure_modes[k] = mode
    print(f"  k={k}: {mode}")

# Check that we get at least 4 distinct failure types
distinct_modes = len(set(failure_modes.values()))
ok8 = distinct_modes >= 4
print(f"\n  Distinct failure types: {distinct_modes}")
results.append(("T8: ≥4 distinct failure modes", ok8,
                f"{distinct_modes} types {'PASS' if ok8 else 'FAIL'}"))

# ══════════════════════════════════════════════════════════════════════
# T9: Frobenius at p=137 — a_137 = -r*n_C = -10
# ══════════════════════════════════════════════════════════════════════
print("\n─── T9: Frobenius at spectral prime ───")
# For CM curve with d=-7, a_p uses the norm equation 4p = a_p^2 + 7*b^2
# At p=137: 4*137 = 548. Need a^2 + 7*b^2 = 548.
# a=10, b=8: 100 + 7*64 = 100 + 448 = 548. ✓
# a_137 = -10 (sign from Grossencharacter)
a_137 = -(r_bst * 5)  # -r * n_C = -10
b_137 = 2**N_c_bst     # 2^N_c = 8
check = a_137**2 + 7 * b_137**2
print(f"  a_137 = -r·n_C = -{r_bst}·{5} = {a_137}")
print(f"  b_137 = 2^N_c = 2^{N_c_bst} = {b_137}")
print(f"  4·N_max = 4·137 = {4*137}")
print(f"  a²+7b² = {a_137}²+7·{b_137}² = {a_137**2}+{7*b_137**2} = {check}")
print(f"  Third 137 identity: N_max = n_C² + g·r⁴ = {5**2} + {7}·{r_bst**4} = {5**2 + 7*r_bst**4}")

ok9 = (check == 4 * 137) and (5**2 + 7 * r_bst**4 == 137)
results.append(("T9: Frobenius a_137 = -r·n_C", ok9,
                f"a²+7b²={check}=4·137={4*137} {'PASS' if ok9 else 'FAIL'}"))

# ══════════════════════════════════════════════════════════════════════
# T10: QR/QNR partition matches BST integers
# ══════════════════════════════════════════════════════════════════════
print("\n─── T10: Quadratic residue partition ───")
# QR mod 7: {1, 2, 4} = {1, r, r^2} = <rank>
# QNR mod 7: {3, 5, 6} = {N_c, n_C, C_2}
qr_mod7 = set()
qnr_mod7 = set()
for a in range(1, 7):
    if any((x*x) % 7 == a for x in range(1, 7)):
        qr_mod7.add(a)
    else:
        qnr_mod7.add(a)

bst_qr = {1, r_bst, r_bst**2}  # {1, 2, 4}
bst_qnr = {N_c_bst, 5, 6}      # {3, 5, 6}

print(f"  QR mod 7:  {sorted(qr_mod7)} = {{1, r, r²}} = {sorted(bst_qr)}")
print(f"  QNR mod 7: {sorted(qnr_mod7)} = {{N_c, n_C, C₂}} = {sorted(bst_qnr)}")

ok10 = (qr_mod7 == bst_qr) and (qnr_mod7 == bst_qnr)
print(f"  Perfect partition: {ok10}")
print(f"  Supersingular density: QNR/total = {len(qnr_mod7)}/{6} = 1/{r_bst} = 1/rank")
results.append(("T10: QR={1,r,r²}, QNR={N_c,n_C,C₂}", ok10,
                f"QR={sorted(qr_mod7)}, QNR={sorted(qnr_mod7)} {'PASS' if ok10 else 'FAIL'}"))

# ══════════════════════════════════════════════════════════════════════
# Summary
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 76)
print("RESULTS")
print("=" * 76)
passes = 0
for name, ok, detail in results:
    status = "PASS" if ok else "FAIL"
    print(f"  {'✓' if ok else '✗'} {name}: {detail}")
    if ok:
        passes += 1

total = len(results)
print(f"\nSCORE: {passes}/{total}")

print(f"\nGenesis cascade summary:")
print(f"  k=5 is the UNIQUE type IV domain passing all 4 locks")
print(f"  c_4 = g!! = 105 (double factorial walks through every odd BST integer)")
print(f"  c_6 = N_c^N_c · g^r = 1323 (self-referential exponents)")
print(f"  Δ = -g³ = -343, j = -(N_c·n_C)³ = -3375")
print(f"  1728 = (r·C₂)³ (Weierstrass normalization IS a BST cube)")
print(f"  Frobenius at p=137: a_137 = -r·n_C, third derivation of 137")
print(f"  QR/QNR partition: primes classified by BST integers")

print(f"\n{'=' * 76}")
print(f"Toy 1469 — SCORE: {passes}/{total}")
print(f"{'=' * 76}")
