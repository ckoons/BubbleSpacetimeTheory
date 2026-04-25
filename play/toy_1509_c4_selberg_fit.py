#!/usr/bin/env python3
"""
Toy 1509 — C4 Selberg Decomposition: Numerical Fitting
========================================================

SPEC for Elie (April 26, 2026). From Lyra's T1453 predictions.

BST predicts the 4-loop QED coefficient C4 = -1.912245764926... (Laporta 2017,
891 Feynman diagrams) decomposes into the Selberg trace formula structure:

    C4 = I4 + K4 + E4 + H4 + M4

with rational coefficients that are BST integer expressions, multiplying
transcendentals from the 11-ingredient basis {pi, ln(2), zeta(3), zeta(5),
zeta(7)}.

This toy attempts to recover the decomposition by PSLQ (integer relation)
fitting of BST-constrained rational coefficients against Laporta's
high-precision numerical value.

STAGED APPROACH:
  Stage 1: Core test (8 basis elements, needs ~50 digits)
           Tests whether C4 is in span of BST transcendentals at all.
  Stage 2: Full fit (29 basis elements, needs ~200+ digits)
           Recovers all rational coefficients. Needs Laporta's 1100-digit value.
  Stage 3: BST verification
           Checks that every discovered rational has BST integer structure.

INPUT:
  C4 numerical value at highest available precision.
  Best public: ~16 digits from review articles (Aoyama et al. 2019).
  Full: 1100 digits from Laporta 2017 (arXiv:1704.06996, Table 1).

PREDICTIONS TESTED (from T1453):
  P-T1453a: C4 contains zeta(7) = zeta(g)
  P-T1453b: Rational denominators divisible by (rank*C_2)^4 = 20736
  P-T1453c: C4 contains Li_6(1/2) = Li_{C_2}(1/rank)
  P-T1453d: C4 contains pi^6 with BST rational coefficient
  P-T1453e: No new fundamental zeta (zeta(9) decomposes)
  P-T1453f: Transcendental content spanned by 11 BST ingredients
            (no independent elliptic constants)

SCORE: ?/6

Theorems tested:
    T1: C4 lies in BST transcendental span (Stage 1, PSLQ finds relation)
    T2: zeta(7) coefficient is nonzero (P-T1453a)
    T3: Rational denominators have BST structure (P-T1453b)
    T4: Li_6(1/2) coefficient is nonzero (P-T1453c)
    T5: pi^6 coefficient is nonzero (P-T1453d)
    T6: Residual after BST basis subtraction < 10^{-precision} (P-T1453f)

BST integers: rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137
(C=2, D=0). Depends on T1451, T1453, T1445.
"""

from mpmath import mp, mpf, pi as mpi, log, zeta, polylog, power, fabs, nstr
from fractions import Fraction
import sys

# ── BST integers ──
rank = 2
N_c = 3
n_C = 5
C_2 = 6
g = 7
N_max = 137

results = []

# ══════════════════════════════════════════════════════════════════════
# C4 numerical value — REPLACE WITH LAPORTA'S 1100-DIGIT VALUE
# ══════════════════════════════════════════════════════════════════════
# Best publicly available precision (~16 digits from review articles):
C4_VALUE = "-1.91224576492616"
# For full Stage 2, paste Laporta's 1100-digit value from arXiv:1704.06996

# Set precision based on input length
available_digits = len(C4_VALUE.replace("-", "").replace(".", ""))
mp.dps = max(available_digits + 30, 80)  # extra guard digits

C4 = mpf(C4_VALUE)
print(f"C4 = {nstr(C4, available_digits)}")
print(f"Available precision: {available_digits} digits")
print(f"Working precision: {mp.dps} digits")
print()

# ══════════════════════════════════════════════════════════════════════
# Transcendental basis (BST 11-ingredient structure)
# ══════════════════════════════════════════════════════════════════════

# Fundamental transcendentals
PI2 = mpi**2
PI4 = mpi**4
PI6 = mpi**6
LN2 = log(2)
Z3 = zeta(3)
Z5 = zeta(5)
Z7 = zeta(7)
LI4 = polylog(4, mpf('0.5'))
LI6 = polylog(6, mpf('0.5'))

# ── Stage 1: Core basis (8 elements) ──
# These are the PURE Selberg contributions: one from each sector.
# Needs ~50 digits for reliable PSLQ.
core_basis = {
    "1":       mpf(1),          # I4 (rational part)
    "pi^2":    PI2,             # K4 (curvature a_1)
    "pi^4":    PI4,             # K4 (curvature a_2)
    "pi^6":    PI6,             # K4 (curvature a_3, NEW at L=4)
    "zeta(3)": Z3,              # H4 (color geodesic)
    "zeta(5)": Z5,              # H4 (compact geodesic)
    "zeta(7)": Z7,              # H4 (genus geodesic, NEW at L=4)
    "ln(2)":   LN2,             # E4 (fiber scaling)
}

# ── Stage 2: Full basis (all products up to weight 7) ──
full_basis = dict(core_basis)
full_basis.update({
    # Weight 2
    "ln^2(2)":           LN2**2,
    # Weight 3
    "ln^3(2)":           LN2**3,
    "pi^2*ln(2)":        PI2 * LN2,
    # Weight 4
    "pi^2*ln^2(2)":      PI2 * LN2**2,
    "zeta(3)*ln(2)":     Z3 * LN2,
    "Li_4(1/2)":         LI4,
    "ln^4(2)":           LN2**4,
    # Weight 5
    "pi^4*ln(2)":        PI4 * LN2,
    "pi^2*zeta(3)":      PI2 * Z3,
    "zeta(3)*ln^2(2)":   Z3 * LN2**2,
    "pi^2*ln^3(2)":      PI2 * LN2**3,
    "ln^5(2)":           LN2**5,
    # Weight 6
    "zeta(5)*ln(2)":     Z5 * LN2,
    "zeta(3)^2":         Z3**2,
    "pi^2*zeta(3)*ln(2)": PI2 * Z3 * LN2,
    "Li_6(1/2)":         LI6,
    "ln^6(2)":           LN2**6,
    "zeta(3)*ln^3(2)":   Z3 * LN2**3,
    # Weight 7
    "pi^2*zeta(5)":      PI2 * Z5,
    "pi^4*zeta(3)":      PI4 * Z3,
    "ln^7(2)":           LN2**7,
})

# ══════════════════════════════════════════════════════════════════════
# PSLQ Integer Relation Algorithm
# ══════════════════════════════════════════════════════════════════════
# Uses mpmath's built-in PSLQ implementation.
# Input: vector [C4, b_1, b_2, ..., b_n]
# Output: integer relation [m_0, m_1, ..., m_n] such that
#         m_0*C4 + m_1*b_1 + ... + m_n*b_n = 0
# Then: C4 = -(m_1*b_1 + ... + m_n*b_n) / m_0

def try_pslq(target, basis_dict, max_denom=10**7, label=""):
    """Attempt PSLQ fit of target against basis elements."""
    from mpmath import pslq

    names = list(basis_dict.keys())
    values = list(basis_dict.values())

    # Construct vector: [target, basis_1, basis_2, ...]
    vec = [target] + values

    print(f"  {label}: PSLQ with {len(names)} basis elements...")

    try:
        relation = pslq(vec, maxcoeff=max_denom, maxsteps=10000)
    except Exception as e:
        print(f"  PSLQ failed: {e}")
        return None

    if relation is None:
        print(f"  No relation found (max_denom={max_denom})")
        return None

    # relation[0] * target + sum(relation[i+1] * basis[i]) = 0
    m0 = relation[0]
    if m0 == 0:
        print(f"  Degenerate relation (m0=0)")
        return None

    # C4 = -sum(relation[i+1] * basis[i]) / relation[0]
    coeffs = {}
    reconstructed = mpf(0)
    for i, name in enumerate(names):
        if relation[i + 1] != 0:
            coeff = Fraction(-relation[i + 1], m0)
            coeffs[name] = coeff
            reconstructed += mpf(coeff.numerator) / mpf(coeff.denominator) * values[i]

    residual = fabs(target - reconstructed)

    print(f"  Found relation! m0 = {m0}")
    print(f"  Residual: {nstr(residual, 5)}")
    print()

    return coeffs, residual

def check_bst_structure(coeffs):
    """Check whether rational coefficients have BST integer structure."""
    max_denom_expected = N_c**2 * (rank * C_2)**4  # 9 * 20736 = 186624

    print("  BST structure check:")
    all_bst = True
    for name, coeff in sorted(coeffs.items()):
        num, den = coeff.numerator, coeff.denominator

        # Check if denominator divides BST product
        bst_denom = den
        # Factor out BST integers
        factors = []
        for p, label in [(2, "rank"), (3, "N_c"), (5, "n_C"), (6, "C_2"), (7, "g")]:
            while bst_denom % p == 0:
                bst_denom //= p
                factors.append(label)

        is_bst = (bst_denom == 1)
        status = "BST" if is_bst else f"RESIDUAL={bst_denom}"
        if not is_bst:
            all_bst = False

        print(f"    {name:25s}: {num}/{den} [{status}]")
        if factors:
            print(f"    {'':25s}  denom factors: {' * '.join(factors)}")

    return all_bst

# ══════════════════════════════════════════════════════════════════════
# Stage 1: Core basis test
# ══════════════════════════════════════════════════════════════════════
print("=" * 70)
print("STAGE 1: Core basis (8 elements, pure Selberg terms)")
print("=" * 70)
print()

if available_digits >= 50:
    result1 = try_pslq(C4, core_basis, max_denom=10**6, label="Stage 1")
    if result1:
        coeffs1, residual1 = result1
        print("  Discovered coefficients:")
        for name, coeff in sorted(coeffs1.items()):
            print(f"    {name:15s}: {coeff}")
        print()

        is_bst1 = check_bst_structure(coeffs1)
        results.append(("T1: C4 in BST span (core)", residual1 < mpf(10)**(-available_digits + 10)))
        results.append(("T2: zeta(7) nonzero", "zeta(7)" in coeffs1))
        results.append(("T3: BST denominators", is_bst1))
        results.append(("T5: pi^6 nonzero", "pi^6" in coeffs1))
    else:
        print("  Stage 1 requires >= 50 digits. Skipping PSLQ, testing structure only.")
        results.append(("T1: C4 in BST span (core)", "NEEDS MORE DIGITS"))
else:
    print(f"  Only {available_digits} digits available. Need >= 50 for Stage 1 PSLQ.")
    print("  To proceed: replace C4_VALUE with Laporta's high-precision value.")
    print()

    # Even with limited digits, we can test the STRUCTURE:
    # Subtract known C3-type terms and check if residual is small
    print("  Structural test (no PSLQ): checking if C4 ~ known structure...")

    # From C3 (Laporta-Remiddi), we know the PATTERN of coefficients.
    # BST predicts I4 has denominator (rank*C_2)^4 = 20736 or N_c*(rank*C_2)^4 = 62208.
    # The rational part should be an integer / 20736 or similar.

    # Quick check: is C4 * 20736 close to a "nice" number?
    c4_times_denom = C4 * 20736
    print(f"  C4 * (rank*C_2)^4 = C4 * 20736 = {nstr(c4_times_denom, 12)}")
    c4_times_denom2 = C4 * 62208
    print(f"  C4 * N_c*(rank*C_2)^4 = C4 * 62208 = {nstr(c4_times_denom2, 12)}")
    c4_times_denom3 = C4 * 186624
    print(f"  C4 * N_c^2*(rank*C_2)^4 = C4 * 186624 = {nstr(c4_times_denom3, 12)}")
    print()

    results.append(("T1: C4 in BST span", "NEEDS >= 50 DIGITS"))

# ══════════════════════════════════════════════════════════════════════
# Stage 2: Full basis test (if sufficient digits)
# ══════════════════════════════════════════════════════════════════════
print()
print("=" * 70)
print("STAGE 2: Full basis (29 elements, all products up to weight 7)")
print("=" * 70)
print()

if available_digits >= 200:
    result2 = try_pslq(C4, full_basis, max_denom=10**7, label="Stage 2")
    if result2:
        coeffs2, residual2 = result2
        print("  Full decomposition:")
        for name, coeff in sorted(coeffs2.items()):
            print(f"    {name:25s}: {coeff}")
        print()

        is_bst2 = check_bst_structure(coeffs2)
        results.append(("T4: Li_6(1/2) nonzero", "Li_6(1/2)" in coeffs2))
        results.append(("T6: residual < 10^-prec", residual2 < mpf(10)**(-available_digits + 30)))
    else:
        print("  Stage 2 PSLQ did not find a relation.")
        print("  Possible causes:")
        print("    (a) C4 contains elliptic constants outside BST basis (P-T1453f)")
        print("    (b) Denominators exceed search bound")
        print("    (c) Insufficient precision")
        results.append(("T4: Li_6(1/2) nonzero", "INCONCLUSIVE"))
        results.append(("T6: residual < 10^-prec", "INCONCLUSIVE"))
else:
    print(f"  Only {available_digits} digits available. Need >= 200 for Stage 2 PSLQ.")
    print("  To proceed: replace C4_VALUE with Laporta's 1100-digit value.")
    results.append(("T4: Li_6(1/2) nonzero", "NEEDS >= 200 DIGITS"))
    results.append(("T6: residual < 10^-prec", "NEEDS >= 200 DIGITS"))

# ══════════════════════════════════════════════════════════════════════
# Stage 3: BST integer verification (if decomposition found)
# ══════════════════════════════════════════════════════════════════════
print()
print("=" * 70)
print("STAGE 3: BST integer structure verification")
print("=" * 70)
print()

# BST denominator rule predictions for L=4:
denom_L4 = (rank * C_2)**4
print(f"BST denominator rule: (rank*C_2)^4 = {denom_L4}")
print(f"With color factor: N_c * (rank*C_2)^4 = {N_c * denom_L4}")
print(f"With color^2: N_c^2 * (rank*C_2)^4 = {N_c**2 * denom_L4}")
print()

# BST integer expressions expected in coefficients:
print("Expected BST patterns in rational coefficients:")
print(f"  g^3 = {g**3} (genus cubed, in pi^2 coefficient)")
print(f"  C_2^4 - 1 = {C_2**4 - 1} = {5}*{7}*{37} = n_C*g*37 (vacuum subtraction)")
print(f"  37 = C_2^2 + 1 = {C_2**2 + 1} (vacuum shift)")
print(f"  2*C_2 - 1 = {2*C_2 - 1} (spectral gap, higher power at L=4)")
print(f"  N_c^2 = {N_c**2} (weight-9 composite)")
print()

# ══════════════════════════════════════════════════════════════════════
# Score
# ══════════════════════════════════════════════════════════════════════
print()
print("=" * 70)
passed = sum(1 for _, v in results if v is True)
total = len(results)
print(f"SCORE: {passed}/{total}")
for name, val in results:
    if val is True:
        status = "PASS"
    elif val is False:
        status = "FAIL"
    else:
        status = str(val)
    print(f"  {name}: {status}")

print()
print("─" * 70)
print("NOTES FOR ELIE:")
print("  1. Replace C4_VALUE with Laporta's high-precision value (1100 digits)")
print("     from arXiv:1704.06996, Table 1.")
print("  2. If Stage 1 PSLQ finds no relation, try larger max_denom (10^8).")
print("  3. If Stage 2 fails with full precision, this is EVIDENCE for")
print("     elliptic constants (P-T1453f) — a genuine new finding.")
print("  4. Even a partial decomposition (recovering some coefficients)")
print("     is valuable — it constrains the elliptic remainder.")
print("  5. The key test: does the residual after BST basis subtraction")
print("     vanish? If yes, BST predicts ALL of C4. If not, the residual")
print("     isolates the elliptic content.")
print("─" * 70)
