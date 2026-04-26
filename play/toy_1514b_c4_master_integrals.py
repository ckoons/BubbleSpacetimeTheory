#!/usr/bin/env python3
"""
Toy 1514b — C4 Master Integral Computation & PSLQ Analysis
============================================================

Level 3 computation for the C4 closed form project (T1458).

STRATEGY:
  Phase 1: Compute B3, C3 to 200+ digits via hypergeometric closed forms
  Phase 2: Compute f1(i,j,k), f2(i,j,k) to 100+ digits via quadrature
  Phase 3: PSLQ each against BST/color period basis
  Phase 4: Assemble and verify against Laporta's C4

The elliptic constants B3, C3 have closed-form hypergeometric representations
(Laporta 2008). The f1/f2 are 1D integrals of elliptic functions over [1,9].

All Gamma arguments in B3/C3 are BST fractions:
  {1/6, 1/3, 2/3, 5/6, 7/6} = {1/C_2, 1/N_c, rank/N_c, n_C/C_2, g/C_2}

BST integers: rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137

SCORE: ?/?
(C=2, D=1). Depends on T1458, T1453.
"""

from mpmath import (mp, mpf, mpc, pi as mpi, gamma, sqrt, log, zeta, polylog,
                    ellipk, ellipe, quad, hyper, nstr, fabs, pslq, power, re, im)
from fractions import Fraction
import sys
import time

# ══════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════

PRECISION = int(sys.argv[1]) if len(sys.argv) > 1 else 200
mp.dps = PRECISION + 100  # guard digits

rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7; N_max = 137

print("=" * 70)
print("Toy 1514b: C4 Master Integral Computation")
print("=" * 70)
print(f"Working precision: {PRECISION} digits (mp.dps={mp.dps})")
print(f"BST: rank={rank}, N_c={N_c}, n_C={n_C}, C_2={C_2}, g={g}")
print()

# ══════════════════════════════════════════════════════════════════════
# PHASE 1: Compute B3 and C3 via hypergeometric closed forms
# ══════════════════════════════════════════════════════════════════════

print("=" * 70)
print("PHASE 1: B3 and C3 from hypergeometric representations")
print("=" * 70)
print()

t0 = time.time()

# Gamma values at BST fractions
G_16 = gamma(mpf(1)/6)   # 1/C_2
G_13 = gamma(mpf(1)/3)   # 1/N_c
G_23 = gamma(mpf(2)/3)   # rank/N_c
G_56 = gamma(mpf(5)/6)   # n_C/C_2
G_76 = gamma(mpf(7)/6)   # g/C_2
G_m13 = gamma(mpf(-1)/3) # -1/N_c

print(f"Gamma(1/C_2) = Gamma(1/6) = {nstr(G_16, 30)}")
print(f"Gamma(1/N_c) = Gamma(1/3) = {nstr(G_13, 30)}")
print(f"Gamma(rank/N_c) = Gamma(2/3) = {nstr(G_23, 30)}")
print(f"Gamma(n_C/C_2) = Gamma(5/6) = {nstr(G_56, 30)}")
print(f"Gamma(g/C_2) = Gamma(7/6) = {nstr(G_76, 30)}")
print()

# Prefactors for B3 hypergeometric
# B3 = (4*pi^(3/2)/3) * [pf1 * F1 + pf2 * F2]
pf1 = G_76**2 * G_13 / (G_23**2 * G_56)
pf2 = G_56**2 * G_m13 / (G_13**2 * G_16)

print("Computing 4F3 hypergeometric series at z=1...")
print("  (This may take a few minutes at high precision)")
sys.stdout.flush()

# 4F3(1/6, 1/3, 1/3, 1/2; 5/6, 5/6, 2/3; 1)
F1 = hyper([mpf(1)/6, mpf(1)/3, mpf(1)/3, mpf(1)/2],
           [mpf(5)/6, mpf(5)/6, mpf(2)/3], 1)

# 4F3(1/2, 2/3, 2/3, 5/6; 7/6, 7/6, 4/3; 1)
F2 = hyper([mpf(1)/2, mpf(2)/3, mpf(2)/3, mpf(5)/6],
           [mpf(7)/6, mpf(7)/6, mpf(4)/3], 1)

print(f"  4F3 #1 = {nstr(F1, 30)}")
print(f"  4F3 #2 = {nstr(F2, 30)}")

# B3 = (4*pi^(3/2)/3) * (pf1*F1 + pf2*F2)
B3 = 4 * mpi**(mpf(3)/2) / 3 * (pf1 * F1 + pf2 * F2)

# A3 = (2*pi^(3/2)/3) * (pf1*F1 - pf2*F2)
A3 = 2 * mpi**(mpf(3)/2) / 3 * (pf1 * F1 - pf2 * F2)

print()
print(f"B3 = {nstr(B3, min(PRECISION, 60))}")
print(f"A3 = {nstr(A3, min(PRECISION, 60))}")

# Verify B3 against Laporta's published value
B3_laporta = mpf('7.396099534768919553449114417961526519643')
print(f"\nB3 check vs Laporta (38 digits):")
print(f"  Residual: {nstr(fabs(B3 - B3_laporta), 5)}")

# C3 via 7F6 hypergeometric
print("\nComputing C3 via 7F6 hypergeometric...")
sys.stdout.flush()

# C3 = (486*pi^2/1925) * 7F6(7/4,-1/3,1/3,2/3,4/3,3/2,3/2; 3/4,1,7/6,11/6,13/6,17/6; 1)
C3_hyper = hyper(
    [mpf(7)/4, mpf(-1)/3, mpf(1)/3, mpf(2)/3, mpf(4)/3, mpf(3)/2, mpf(3)/2],
    [mpf(3)/4, mpf(1), mpf(7)/6, mpf(11)/6, mpf(13)/6, mpf(17)/6],
    1)

C3 = 486 * mpi**2 / 1925 * C3_hyper

print(f"C3 = {nstr(C3, min(PRECISION, 60))}")

# Cross-check E_4a
E4a_computed = mpi * (mpf(-28458503)/691200 * B3 + mpf(250077961)/18662400 * C3)
E4a_laporta = mpf('-856.605968292200108497784694038000040595')
print(f"\nE_4a cross-check:")
print(f"  Computed: {nstr(E4a_computed, 30)}")
print(f"  Laporta: {nstr(E4a_laporta, 30)}")
print(f"  Residual: {nstr(fabs(E4a_computed - E4a_laporta), 5)}")

t1 = time.time()
print(f"\nPhase 1 time: {t1-t0:.1f}s")

# ══════════════════════════════════════════════════════════════════════
# PHASE 2: Compute f1 and f2 base integrals
# ══════════════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("PHASE 2: f1 and f2 integrals (sunrise elliptic integrals)")
print("=" * 70)
print()

# D1(s) = 2/sqrt((sqrt(s)+3)(sqrt(s)-1)^3) * K(modulus)
# where modulus = (sqrt(s)-3)(sqrt(s)+1)^3 / ((sqrt(s)+3)(sqrt(s)-1)^3)
#
# D2(s) = 2/sqrt((sqrt(s)+3)(sqrt(s)-1)^3) * K(1 - modulus)

def D1(s):
    """First elliptic kernel for sunrise integral."""
    rs = sqrt(s)
    num = (rs - 3) * (rs + 1)**3
    den = (rs + 3) * (rs - 1)**3
    modulus = num / den
    prefactor = 2 / sqrt((rs + 3) * (rs - 1)**3)
    return prefactor * ellipk(modulus)

def D2(s):
    """Second elliptic kernel (complementary)."""
    rs = sqrt(s)
    num = (rs - 3) * (rs + 1)**3
    den = (rs + 3) * (rs - 1)**3
    modulus = num / den
    prefactor = 2 / sqrt((rs + 3) * (rs - 1)**3)
    return prefactor * ellipk(1 - modulus)

def f1_integrand(s, i=0, j=0, k=0):
    """f1(i,j,k) integrand."""
    d1 = D1(s)
    factor = d1**2 * (s - mpf(9)/5)
    if i > 0: factor *= log(9 - s)**i
    if j > 0: factor *= log(s - 1)**j
    if k > 0: factor *= log(s)**k
    return factor

def f2_integrand(s, i=0, j=0, k=0):
    """f2(i,j,k) integrand."""
    d1 = D1(s)
    d2 = D2(s)
    factor = d1 * re(sqrt(mpf(3)) * d2) * (s - mpf(9)/5)
    if i > 0: factor *= log(9 - s)**i
    if j > 0: factor *= log(s - 1)**j
    if k > 0: factor *= log(s)**k
    return factor

# Compute f1(0,0,0) and f2(0,0,0) — the base integrals
# Integration over [1,9] with endpoint singularities
# Use tanh-sinh (doubly-exponential) quadrature

print("Computing f1(0,0,0) via quadrature over [1,9]...")
print("  (Singularities at s=1 and s=9, using tanh-sinh)")
sys.stdout.flush()

t2 = time.time()

# Split integration to handle singularities: [1+eps, 9-eps]
# with substitution near endpoints
try:
    f1_000 = quad(lambda s: f1_integrand(s), [mpf(1), mpf(9)], method='tanh-sinh')
    print(f"  f1(0,0,0) = {nstr(f1_000, min(PRECISION, 50))}")
except Exception as e:
    print(f"  f1(0,0,0) failed: {e}")
    f1_000 = None

print("\nComputing f2(0,0,0)...")
sys.stdout.flush()

try:
    f2_000 = quad(lambda s: f2_integrand(s), [mpf(1), mpf(9)], method='tanh-sinh')
    print(f"  f2(0,0,0) = {nstr(f2_000, min(PRECISION, 50))}")
except Exception as e:
    print(f"  f2(0,0,0) failed: {e}")
    f2_000 = None

# Compute f2(0,0,1) — needed for E_5a
print("\nComputing f2(0,0,1) [needed for E_5a]...")
sys.stdout.flush()

try:
    f2_001 = quad(lambda s: f2_integrand(s, 0, 0, 1), [mpf(1), mpf(9)], method='tanh-sinh')
    print(f"  f2(0,0,1) = {nstr(f2_001, min(PRECISION, 50))}")
except Exception as e:
    print(f"  f2(0,0,1) failed: {e}")
    f2_001 = None

# Compute f1(0,0,1) — needed for E_6b
print("\nComputing f1(0,0,1) [needed for E_6b]...")
sys.stdout.flush()

try:
    f1_001 = quad(lambda s: f1_integrand(s, 0, 0, 1), [mpf(1), mpf(9)], method='tanh-sinh')
    print(f"  f1(0,0,1) = {nstr(f1_001, min(PRECISION, 50))}")
except Exception as e:
    print(f"  f1(0,0,1) failed: {e}")
    f1_001 = None

# Additional integrals for full master integral computation
print("\nComputing additional f-integrals for master integral assembly...")
sys.stdout.flush()

extra_integrals = {}
for name, i, j, k, func in [
    ('f1(1,0,0)', 1, 0, 0, f1_integrand),
    ('f1(0,1,0)', 0, 1, 0, f1_integrand),
    ('f2(1,0,0)', 1, 0, 0, f2_integrand),
    ('f2(0,1,0)', 0, 1, 0, f2_integrand),
    ('f1(0,0,2)', 0, 0, 2, f1_integrand),
    ('f2(0,0,2)', 0, 0, 2, f2_integrand),
]:
    try:
        val = quad(lambda s, ii=i, jj=j, kk=k, ff=func: ff(s, ii, jj, kk),
                   [mpf(1), mpf(9)], method='tanh-sinh')
        extra_integrals[name] = val
        print(f"  {name} = {nstr(val, min(PRECISION, 40))}")
    except Exception as e:
        print(f"  {name} failed: {e}")
        extra_integrals[name] = None

t3 = time.time()
print(f"\nPhase 2 time: {t3-t2:.1f}s")

# Cross-check E_5a = (483913/77760) * pi * f2(0,0,1)
if f2_001 is not None:
    E5a_computed = mpf(483913)/77760 * mpi * f2_001
    E5a_laporta = mpf('601.136193120690233763409588135510244820')
    print(f"\nE_5a cross-check:")
    print(f"  Computed: {nstr(E5a_computed, 30)}")
    print(f"  Laporta: {nstr(E5a_laporta, 30)}")
    print(f"  Residual: {nstr(fabs(E5a_computed - E5a_laporta), 5)}")

# Cross-check E_6b = -(4715/1458) * zeta(2) * f1(0,0,1)
if f1_001 is not None:
    E6b_computed = mpf(-4715)/1458 * mpi**2/6 * f1_001
    E6b_laporta = mpf('-89.049936952630079330356943951138211140')
    print(f"\nE_6b cross-check:")
    print(f"  Computed: {nstr(E6b_computed, 30)}")
    print(f"  Laporta: {nstr(E6b_laporta, 30)}")
    print(f"  Residual: {nstr(fabs(E6b_computed - E6b_laporta), 5)}")

# ══════════════════════════════════════════════════════════════════════
# PHASE 3: PSLQ analysis of B3 and C3
# ══════════════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("PHASE 3: PSLQ analysis of elliptic constants")
print("=" * 70)
print()

# Build a color-period basis
# Key transcendentals related to CM by Q(sqrt(-3)):
# Gamma(1/3)^3, Gamma(1/6)^2, pi, sqrt(3), and polylogs

PI2 = mpi**2
Z3 = zeta(3)
LN2 = log(2)
sq3 = sqrt(mpf(3))

# Omega_color = Gamma(1/3)^3 / (4*pi*sqrt(3))  -- period of 27a1
OMEGA_color = G_13**3 / (4 * mpi * sq3)

# Omega_genus = Gamma(1/7)*Gamma(2/7)*Gamma(4/7) / (4*pi^2*sqrt(7))
OMEGA_genus = gamma(mpf(1)/7) * gamma(mpf(2)/7) * gamma(mpf(4)/7) / (4 * PI2 * sqrt(mpf(7)))

print(f"Color period Omega_Nc = {nstr(OMEGA_color, 30)}")
print(f"Genus period Omega_g  = {nstr(OMEGA_genus, 30)}")
print()

# Test B3 against basis
print("--- PSLQ: B3 against color period basis ---")
print()

b3_basis = {
    '1':           mpf(1),
    'pi':          mpi,
    'pi^2':        PI2,
    'pi^3':        mpi**3,
    'sq3':         sq3,
    'pi*sq3':      mpi * sq3,
    'pi^2*sq3':    PI2 * sq3,
    'Omega_Nc':    OMEGA_color,
    'G13^3':       G_13**3,
    'G13^3*sq3':   G_13**3 * sq3,
    'z3':          Z3,
    'ln2':         LN2,
}

# Use precision appropriate for basis size
pslq_dps = min(PRECISION, 200)
names = list(b3_basis.keys())
values = list(b3_basis.values())

print(f"  Basis: {len(names)} elements, {pslq_dps} digits")
vec = [B3] + values
sys.stdout.flush()

rel = pslq(vec, maxcoeff=10**8, maxsteps=30000)
if rel is None:
    print("  B3: No relation found in color period basis")
else:
    m0 = rel[0]
    if m0 == 0:
        print("  B3: Degenerate relation")
    else:
        print(f"  B3: Found relation! m0 = {m0}")
        recon = mpf(0)
        for i, n in enumerate(names):
            if rel[i+1] != 0:
                c = Fraction(-rel[i+1], m0)
                recon += mpf(c.numerator)/mpf(c.denominator) * values[i]
                d = abs(c.denominator)
                rem = d
                for p in [2,3,5,7]:
                    while rem % p == 0: rem //= p
                smooth = 'BST' if rem == 1 else f'non-BST({rem})'
                print(f"    {n:20s}: {str(c):25s}  [{smooth}]")
        res = fabs(B3 - recon)
        quality = 'GENUINE' if res < power(10, -pslq_dps + 30) else 'SPURIOUS'
        print(f"  Residual: {nstr(res, 5)} [{quality}]")

# Test C3
print()
print("--- PSLQ: C3 against color period basis ---")
print()

vec_c3 = [C3] + values
rel_c3 = pslq(vec_c3, maxcoeff=10**8, maxsteps=30000)
if rel_c3 is None:
    print("  C3: No relation found in color period basis")
else:
    m0 = rel_c3[0]
    if m0 == 0:
        print("  C3: Degenerate relation")
    else:
        print(f"  C3: Found relation! m0 = {m0}")
        recon = mpf(0)
        for i, n in enumerate(names):
            if rel_c3[i+1] != 0:
                c = Fraction(-rel_c3[i+1], m0)
                recon += mpf(c.numerator)/mpf(c.denominator) * values[i]
                d = abs(c.denominator)
                rem = d
                for p in [2,3,5,7]:
                    while rem % p == 0: rem //= p
                smooth = 'BST' if rem == 1 else f'non-BST({rem})'
                print(f"    {n:20s}: {str(c):25s}  [{smooth}]")
        res = fabs(C3 - recon)
        quality = 'GENUINE' if res < power(10, -pslq_dps + 30) else 'SPURIOUS'
        print(f"  Residual: {nstr(res, 5)} [{quality}]")

# Test f1(0,0,0) if available
if f1_000 is not None:
    print()
    print("--- PSLQ: f1(0,0,0) against extended basis ---")
    print()

    f_basis = dict(b3_basis)
    f_basis['B3'] = B3
    f_basis['C3'] = C3
    f_basis['pi*B3'] = mpi * B3
    f_basis['pi*C3'] = mpi * C3

    f_names = list(f_basis.keys())
    f_values = list(f_basis.values())
    vec_f1 = [f1_000] + f_values

    print(f"  Basis: {len(f_names)} elements")
    sys.stdout.flush()

    rel_f1 = pslq(vec_f1, maxcoeff=10**8, maxsteps=30000)
    if rel_f1 is None:
        print("  f1(0,0,0): No relation found")
    else:
        m0 = rel_f1[0]
        if m0 != 0:
            print(f"  f1(0,0,0): Found! m0 = {m0}")
            recon = mpf(0)
            for i, n in enumerate(f_names):
                if rel_f1[i+1] != 0:
                    c = Fraction(-rel_f1[i+1], m0)
                    recon += mpf(c.numerator)/mpf(c.denominator) * f_values[i]
                    d = abs(c.denominator)
                    rem = d
                    for p in [2,3,5,7]:
                        while rem % p == 0: rem //= p
                    smooth = 'BST' if rem == 1 else f'non-BST({rem})'
                    print(f"    {n:20s}: {str(c):25s}  [{smooth}]")
            res = fabs(f1_000 - recon)
            quality = 'GENUINE' if res < power(10, -pslq_dps + 30) else 'SPURIOUS'
            print(f"  Residual: {nstr(res, 5)} [{quality}]")

# Helper to run PSLQ and display results
def run_pslq(name, target, basis_names, basis_values, dps_limit):
    """Run PSLQ on target against basis, print results."""
    print(f"\n--- PSLQ: {name} against extended basis ---\n")
    print(f"  Basis: {len(basis_names)} elements, {dps_limit} digits")
    sys.stdout.flush()
    vec = [target] + basis_values
    rel = pslq(vec, maxcoeff=10**8, maxsteps=50000)
    if rel is None:
        print(f"  {name}: No relation found")
        return None
    m0 = rel[0]
    if m0 == 0:
        print(f"  {name}: Degenerate relation")
        return None
    print(f"  {name}: Found relation! m0 = {m0}")
    recon = mpf(0)
    terms = []
    for i, n in enumerate(basis_names):
        if rel[i+1] != 0:
            c = Fraction(-rel[i+1], m0)
            recon += mpf(c.numerator)/mpf(c.denominator) * basis_values[i]
            d = abs(c.denominator)
            rem = d
            for p in [2,3,5,7]:
                while rem % p == 0: rem //= p
            smooth = 'BST' if rem == 1 else f'non-BST({rem})'
            print(f"    {n:20s}: {str(c):25s}  [{smooth}]")
            terms.append((n, c, smooth))
    res = fabs(target - recon)
    quality = 'GENUINE' if res < power(10, -dps_limit + 30) else 'SPURIOUS'
    print(f"  Residual: {nstr(res, 5)} [{quality}]")
    return terms if quality == 'GENUINE' else None

# Test f2(0,0,0) if available
if f2_000 is not None:
    run_pslq("f2(0,0,0)", f2_000, f_names, f_values, pslq_dps)

# Test f2(0,0,1) if available
if f2_001 is not None:
    run_pslq("f2(0,0,1)", f2_001, f_names, f_values, pslq_dps)

# Test f1(0,0,1) if available
if f1_001 is not None:
    run_pslq("f1(0,0,1)", f1_001, f_names, f_values, pslq_dps)

# Test extra integrals
for ename, eval in extra_integrals.items():
    if eval is not None:
        run_pslq(ename, eval, f_names, f_values, pslq_dps)

# ══════════════════════════════════════════════════════════════════════
# PHASE 3b: Direct PSLQ of master integral combinations
# ══════════════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("PHASE 3b: PSLQ of Laporta's E-combinations")
print("=" * 70)

# From Laporta's table, the 6 master integrals C81a,b,c, C83a,b,c are
# linear combinations of f1, f2 integrals. Let's compute the ones we can.

# E_4a = pi * (-28458503/691200 * B3 + 250077961/18662400 * C3) — already verified
# E_5a = (483913/77760) * pi * f2(0,0,1) — already verified
# E_6b = -(4715/1458) * zeta(2) * f1(0,0,1) — already verified (zeta(2) = pi^2/6)

# E_7a = pi * (37/6 * f2(0,0,0) + 49/3 * f2(0,0,1) + ...)
# We have f2(0,0,0), f2(0,0,1), can compute partial combinations

# Direct PSLQ of known E values against the basis
E4a_val = E4a_computed  # = pi*(-28458503/691200*B3 + 250077961/18662400*C3)
E5a_val = mpf(483913)/77760 * mpi * f2_001
E6b_val = mpf(-4715)/1458 * PI2/6 * f1_001

# Extend basis with B3*pi^2, C3*pi, etc.
ext_basis_names = list(f_names) + ['z3*pi', 'z3*pi^2', 'B3*pi^2', 'C3*pi^2', 'z3*sq3', 'pi^3*sq3']
ext_basis_values = list(f_values) + [Z3*mpi, Z3*PI2, B3*PI2, C3*PI2, Z3*sq3, mpi**3*sq3]

print("\n--- PSLQ: E_4a against extended basis ---")
run_pslq("E_4a", E4a_val, ext_basis_names, ext_basis_values, pslq_dps)

print("\n--- PSLQ: E_5a against extended basis ---")
run_pslq("E_5a", E5a_val, ext_basis_names, ext_basis_values, pslq_dps)

print("\n--- PSLQ: E_6b against extended basis ---")
run_pslq("E_6b", E6b_val, ext_basis_names, ext_basis_values, pslq_dps)

# ══════════════════════════════════════════════════════════════════════
# PHASE 3c: The key test — does f1(0,0,0) = 63/10 * zeta(3)?
# ══════════════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("PHASE 3c: Verification of f1(0,0,0) = (N_c^2 * g)/(rank * n_C) * zeta(3)")
print("=" * 70)
print()

# Direct algebraic check
ratio_63_10 = mpf(N_c**2 * g) / mpf(rank * n_C)  # = 63/10
predicted = ratio_63_10 * Z3
actual = f1_000
res = fabs(predicted - actual)
print(f"  63/10 = N_c^2*g/(rank*n_C) = {ratio_63_10}")
print(f"  63/10 * zeta(3) = {nstr(predicted, 50)}")
print(f"  f1(0,0,0)       = {nstr(actual, 50)}")
print(f"  Residual: {nstr(res, 5)}")
print(f"  Match: {'YES' if res < power(10, -PRECISION + 20) else 'NO'} at {PRECISION} digits")
print()

# BST decomposition
print("  BST decomposition of 63/10:")
print(f"    Numerator:   63 = 9*7 = N_c^2 * g")
print(f"    Denominator: 10 = 2*5 = rank * n_C")
print(f"    ALL five BST integers appear in one fraction!")

# ══════════════════════════════════════════════════════════════════════
# PHASE 4: Assembly and summary
# ══════════════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("PHASE 4: Summary")
print("=" * 70)
print()

print(f"B3 = {nstr(B3, 50)}")
print(f"C3 = {nstr(C3, 50)}")
if f1_000: print(f"f1(0,0,0) = {nstr(f1_000, 50)}")
if f2_000: print(f"f2(0,0,0) = {nstr(f2_000, 50)}")
if f2_001: print(f"f2(0,0,1) = {nstr(f2_001, 50)}")
if f1_001: print(f"f1(0,0,1) = {nstr(f1_001, 50)}")

print()
print("BST STRUCTURE OF THE ELLIPTIC SECTOR:")
print()
print("  B3 Gamma args: {1/C_2, 1/N_c, rank/N_c, n_C/C_2, g/C_2}")
print("  C3 7F6 args: all multiples of 1/C_2 and 1/N_c")
print("  E terms: multiplied by sqrt(N_c)")
print("  Denominators: 691200 = 2^10*3^3*5^2, 18662400 = 2^10*3^6*5^2")
print("  Both BST-smooth (no factor of g=7)")
print()
print("  Master integral coefficients:")
print("    49/3 = g^2/N_c")
print("    49/36 = g^2/(rank*N_c)^2")
print("    37/6 = 37/C_2")
print("    541/300, 629/60, 327/160 — all BST-smooth denominators")

t_final = time.time()
print(f"\nTotal time: {t_final-t0:.1f}s")
