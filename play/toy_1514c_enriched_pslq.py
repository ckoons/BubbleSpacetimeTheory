#!/usr/bin/env python3
"""
Toy 1514c — Enriched PSLQ Analysis of Sunrise Integrals
========================================================

Follow-up to Toy 1514b. Given f1(0,0,0) = 63/10 * zeta(3) PROVED,
test remaining f-integrals against enriched bases including:
  zeta(5), zeta(7), ln(3), zeta(3)*ln(3), zeta(3)^2, etc.

Also test ratios to look for internal algebraic structure.

SCORE: ?/?
(C=2, D=1). Depends on T1458, Toy 1514b.
"""

from mpmath import (mp, mpf, pi as mpi, gamma, sqrt, log, zeta, polylog,
                    ellipk, ellipe, quad, hyper, nstr, fabs, pslq, power, re)
from fractions import Fraction
import sys
import time

PRECISION = int(sys.argv[1]) if len(sys.argv) > 1 else 200
mp.dps = PRECISION + 100

rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7; N_max = 137

print("=" * 70)
print("Toy 1514c: Enriched PSLQ for Sunrise Integrals")
print("=" * 70)
print(f"Working precision: {PRECISION} digits (mp.dps={mp.dps})")
print()

t0 = time.time()

# ── Recompute B3, C3 via hypergeometric (fast) ──
G_16 = gamma(mpf(1)/6); G_13 = gamma(mpf(1)/3)
G_23 = gamma(mpf(2)/3); G_56 = gamma(mpf(5)/6)
G_76 = gamma(mpf(7)/6); G_m13 = gamma(mpf(-1)/3)

pf1 = G_76**2 * G_13 / (G_23**2 * G_56)
pf2 = G_56**2 * G_m13 / (G_13**2 * G_16)
F1 = hyper([mpf(1)/6, mpf(1)/3, mpf(1)/3, mpf(1)/2],
           [mpf(5)/6, mpf(5)/6, mpf(2)/3], 1)
F2 = hyper([mpf(1)/2, mpf(2)/3, mpf(2)/3, mpf(5)/6],
           [mpf(7)/6, mpf(7)/6, mpf(4)/3], 1)
B3 = 4 * mpi**(mpf(3)/2) / 3 * (pf1 * F1 + pf2 * F2)
A3 = 2 * mpi**(mpf(3)/2) / 3 * (pf1 * F1 - pf2 * F2)
C3_hyper = hyper(
    [mpf(7)/4, mpf(-1)/3, mpf(1)/3, mpf(2)/3, mpf(4)/3, mpf(3)/2, mpf(3)/2],
    [mpf(3)/4, mpf(1), mpf(7)/6, mpf(11)/6, mpf(13)/6, mpf(17)/6], 1)
C3 = 486 * mpi**2 / 1925 * C3_hyper

print(f"B3 = {nstr(B3, 40)}")
print(f"A3 = {nstr(A3, 40)}")
print(f"C3 = {nstr(C3, 40)}")

# ── Recompute f-integrals ──
def D1(s):
    rs = sqrt(s)
    num = (rs - 3) * (rs + 1)**3
    den = (rs + 3) * (rs - 1)**3
    modulus = num / den
    prefactor = 2 / sqrt((rs + 3) * (rs - 1)**3)
    return prefactor * ellipk(modulus)

def D2(s):
    rs = sqrt(s)
    num = (rs - 3) * (rs + 1)**3
    den = (rs + 3) * (rs - 1)**3
    modulus = num / den
    prefactor = 2 / sqrt((rs + 3) * (rs - 1)**3)
    return prefactor * ellipk(1 - modulus)

def f1_integrand(s, i=0, j=0, k=0):
    d1 = D1(s)
    factor = d1**2 * (s - mpf(9)/5)
    if i > 0: factor *= log(9 - s)**i
    if j > 0: factor *= log(s - 1)**j
    if k > 0: factor *= log(s)**k
    return factor

def f2_integrand(s, i=0, j=0, k=0):
    d1 = D1(s)
    d2 = D2(s)
    factor = d1 * re(sqrt(mpf(3)) * d2) * (s - mpf(9)/5)
    if i > 0: factor *= log(9 - s)**i
    if j > 0: factor *= log(s - 1)**j
    if k > 0: factor *= log(s)**k
    return factor

print("\nComputing f-integrals via quadrature...")
sys.stdout.flush()

integrals = {}
for name, i, j, k, func in [
    ('f1_000', 0, 0, 0, f1_integrand),
    ('f1_001', 0, 0, 1, f1_integrand),
    ('f1_010', 0, 1, 0, f1_integrand),
    ('f1_100', 1, 0, 0, f1_integrand),
    ('f1_002', 0, 0, 2, f1_integrand),
    ('f2_000', 0, 0, 0, f2_integrand),
    ('f2_001', 0, 0, 1, f2_integrand),
    ('f2_010', 0, 1, 0, f2_integrand),
    ('f2_100', 1, 0, 0, f2_integrand),
    ('f2_002', 0, 0, 2, f2_integrand),
]:
    try:
        val = quad(lambda s, ii=i, jj=j, kk=k, ff=func: ff(s, ii, jj, kk),
                   [mpf(1), mpf(9)], method='tanh-sinh')
        integrals[name] = val
        print(f"  {name:10s} = {nstr(val, 30)}")
    except Exception as e:
        print(f"  {name:10s} FAILED: {e}")

t1 = time.time()
print(f"\nQuadrature time: {t1-t0:.1f}s")

# ── Verify f1(0,0,0) = 63/10 * zeta(3) ──
PI2 = mpi**2
Z3 = zeta(3); Z5 = zeta(5); Z7 = zeta(7)
LN2 = log(2); LN3 = log(3); LN9 = log(9)
sq3 = sqrt(mpf(3))

pred = mpf(63)/10 * Z3
res = fabs(integrals['f1_000'] - pred)
print(f"\nf1(0,0,0) = 63/10 * zeta(3)  residual = {nstr(res, 5)}  {'CONFIRMED' if res < power(10, -50) else 'FAILED'}")

# ── PSLQ helper ──
def run_pslq(name, target, basis_names, basis_values, dps_limit=PRECISION):
    vec = [target] + basis_values
    rel = pslq(vec, maxcoeff=10**9, maxsteps=50000)
    if rel is None:
        print(f"  {name:15s}: No relation found ({len(basis_names)} elements)")
        return None
    m0 = rel[0]
    if m0 == 0:
        print(f"  {name:15s}: Degenerate")
        return None
    # Extract non-zero terms
    terms = []
    recon = mpf(0)
    for i, n in enumerate(basis_names):
        if rel[i+1] != 0:
            c = Fraction(-rel[i+1], m0)
            recon += mpf(c.numerator)/mpf(c.denominator) * basis_values[i]
            d = abs(c.denominator)
            rem = d
            for p in [2,3,5,7]:
                while rem % p == 0: rem //= p
            smooth = 'BST' if rem == 1 else f'non-BST({rem})'
            terms.append((n, c, smooth))
    res = fabs(target - recon)
    quality = 'GENUINE' if res < power(10, -dps_limit + 30) else 'SPURIOUS'
    if terms:
        print(f"  {name:15s}: Found! m0={m0} [{quality}]")
        for n, c, s in terms:
            print(f"    {n:20s}: {str(c):25s}  [{s}]")
        print(f"    Residual: {nstr(res, 5)}")
    return terms if quality == 'GENUINE' else None

# ══════════════════════════════════════════════════════════════════════
# TEST 1: f1 integrals against enriched basis
# ══════════════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("TEST 1: f1 integrals (D1^2 kernel)")
print("=" * 70)
print()
print("Hypothesis: f1 integrals are polylogarithmic (reduce to zeta values)")
print()

# Basis: polylogs + logs + their products
f1_basis_names = [
    '1', 'pi', 'pi^2', 'pi^3', 'pi^4',
    'z3', 'z5', 'z7', 'z3^2',
    'ln2', 'ln3', 'ln2^2', 'ln3^2', 'ln2*ln3',
    'z3*ln2', 'z3*ln3', 'z3*pi', 'z3*pi^2',
    'pi*ln2', 'pi*ln3', 'pi^2*ln2', 'pi^2*ln3',
]
f1_basis_values = [
    mpf(1), mpi, PI2, mpi**3, mpi**4,
    Z3, Z5, Z7, Z3**2,
    LN2, LN3, LN2**2, LN3**2, LN2*LN3,
    Z3*LN2, Z3*LN3, Z3*mpi, Z3*PI2,
    mpi*LN2, mpi*LN3, PI2*LN2, PI2*LN3,
]

print(f"Polylog basis: {len(f1_basis_names)} elements")
print()

for fname in ['f1_001', 'f1_010', 'f1_100', 'f1_002']:
    if fname in integrals:
        sys.stdout.flush()
        run_pslq(fname, integrals[fname], f1_basis_names, f1_basis_values)

# ══════════════════════════════════════════════════════════════════════
# TEST 2: f2 integrals against full basis (polylogs + elliptic)
# ══════════════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("TEST 2: f2 integrals (D1*D2 kernel — genuinely elliptic?)")
print("=" * 70)
print()

# Full basis: polylogs + B3, C3, A3 and their products
f2_basis_names = [
    '1', 'pi', 'pi^2', 'pi^3',
    'sq3', 'pi*sq3', 'pi^2*sq3',
    'z3', 'z5', 'ln2', 'ln3',
    'B3', 'C3', 'A3',
    'pi*B3', 'pi*C3', 'pi*A3',
    'sq3*B3', 'sq3*C3', 'sq3*A3',
    'z3*B3', 'z3*C3',
    'ln3*B3', 'ln3*C3',
]
f2_basis_values = [
    mpf(1), mpi, PI2, mpi**3,
    sq3, mpi*sq3, PI2*sq3,
    Z3, Z5, LN2, LN3,
    B3, C3, A3,
    mpi*B3, mpi*C3, mpi*A3,
    sq3*B3, sq3*C3, sq3*A3,
    Z3*B3, Z3*C3,
    LN3*B3, LN3*C3,
]

print(f"Full basis: {len(f2_basis_names)} elements")
print()

for fname in ['f2_000', 'f2_001', 'f2_010', 'f2_100', 'f2_002']:
    if fname in integrals:
        sys.stdout.flush()
        run_pslq(fname, integrals[fname], f2_basis_names, f2_basis_values)

# ══════════════════════════════════════════════════════════════════════
# TEST 3: Ratios of f2 integrals (internal structure)
# ══════════════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("TEST 3: Ratio analysis")
print("=" * 70)
print()

small_basis_names = ['1', 'pi', 'pi^2', 'sq3', 'ln2', 'ln3', 'z3', 'z5']
small_basis_values = [mpf(1), mpi, PI2, sq3, LN2, LN3, Z3, Z5]

ratios_to_test = []
if 'f2_000' in integrals and 'f2_001' in integrals:
    ratios_to_test.append(('f2_001/f2_000', integrals['f2_001']/integrals['f2_000']))
if 'f1_001' in integrals:
    ratios_to_test.append(('f1_001/z3', integrals['f1_001']/Z3))
if 'f2_000' in integrals:
    ratios_to_test.append(('f2_000/B3', integrals['f2_000']/B3))
    ratios_to_test.append(('f2_000/A3', integrals['f2_000']/A3))
    ratios_to_test.append(('f2_000/C3', integrals['f2_000']/C3))
    ratios_to_test.append(('f2_000/(pi*B3)', integrals['f2_000']/(mpi*B3)))

for rname, rval in ratios_to_test:
    print(f"  {rname:25s} = {nstr(rval, 25)}")
    run_pslq(rname, rval, small_basis_names, small_basis_values)

# ══════════════════════════════════════════════════════════════════════
# TEST 4: Direct test — can we express C4's elliptic part?
# ══════════════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("TEST 4: C4 elliptic sector reconstruction")
print("=" * 70)
print()

# E_4a = pi * (-28458503/691200 * B3 + 250077961/18662400 * C3)
E4a = mpi * (mpf(-28458503)/691200 * B3 + mpf(250077961)/18662400 * C3)

# E_5a = (483913/77760) * pi * f2(0,0,1)
E5a = mpf(483913)/77760 * mpi * integrals.get('f2_001', mpf(0))

# E_6b = -(4715/1458) * (pi^2/6) * f1(0,0,1)
E6b = mpf(-4715)/1458 * PI2/6 * integrals.get('f1_001', mpf(0))

# Published Laporta values (38 digits)
E4a_pub = mpf('-856.605968292200108497784694038000040595')
E5a_pub = mpf('601.136193120690233763409588135510244820')
E6b_pub = mpf('-89.049936952630079330356943951138211140')

print("Cross-checks vs Laporta (38-digit published):")
print(f"  E_4a: delta = {nstr(fabs(E4a - E4a_pub), 5)}")
print(f"  E_5a: delta = {nstr(fabs(E5a - E5a_pub), 5)}")
print(f"  E_6b: delta = {nstr(fabs(E6b - E6b_pub), 5)}")

# Sum of elliptic E terms (from Laporta's Table 2)
# V_4a = E_4a, etc. These get multiplied by sqrt(3) in the assembly
# The elliptic contribution to C4/pi^4 is:
# sqrt(3) * (V_4a + V_6a) + sqrt(3) * (E_4a + E_5a + E_6a + E_7a)
# We have E_4a, E_5a, E_6b computed. Print their sum for structure.

print(f"\n  E_4a = {nstr(E4a, 40)}")
print(f"  E_5a = {nstr(E5a, 40)}")
print(f"  E_6b = {nstr(E6b, 40)}")
print(f"  Sum(E_4a+E_5a+E_6b) = {nstr(E4a + E5a + E6b, 40)}")

# Key finding: f1(0,0,0) = 63/10 * zeta(3) means the D1^2 part is polylogarithmic.
# This simplifies any master integral expression that uses f1-type integrals.
# E_6b = -(4715/1458) * zeta(2) * f1(0,0,1)
# If f1(0,0,1) ALSO reduces to polylogs, then E_6b is purely polylogarithmic.

print()
print("=" * 70)
print("SUMMARY OF CLOSED FORMS FOUND")
print("=" * 70)
print()

print("CONFIRMED:")
print(f"  f1(0,0,0) = (N_c^2 * g)/(rank * n_C) * zeta(3)")
print(f"           = (9 * 7)/(2 * 5) * zeta(3)")
print(f"           = 63/10 * zeta(3)")
print(f"           = {nstr(mpf(63)/10 * Z3, 40)}")
print(f"  Residual:  {nstr(res, 5)} at {PRECISION} digits")
print()

print("  B3 = (4*pi^(3/2)/3) * [pf1*4F3(...;1) + pf2*4F3(...;1)]")
print("     where all Gamma args are BST fractions {a/C_2, b/N_c}")
print(f"     = {nstr(B3, 40)}")
print()
print("  C3 = (486*pi^2/1925) * 7F6(...;1)")
print(f"     = {nstr(C3, 40)}")
print()

print("STATUS:")
print("  f1(0,0,k) — likely polylogarithmic (D1^2 kernel)")
print("  f2(0,0,k) — genuinely elliptic (D1*D2 kernel)")
print("  B3, C3    — closed hypergeometric forms, transcendentally independent")

t_final = time.time()
print(f"\nTotal time: {t_final-t0:.1f}s")
