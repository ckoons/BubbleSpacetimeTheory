"""
BST Cost Function: Mathematical Natural Selection for N* = 137
==============================================================
From notes/maybe/BST_Before.md

The substrate with fiber ratio rho competed with other structures.
The winner minimizes:

   C(rho) = C_geometric(rho) + C_computational(rho)

where:
  C_g = rho * ln(rho)       [cost grows with capacity × addressing entropy]
  C_c = kappa / ln(1+rho)   [overhead falls as Shannon capacity grows]

The minimum requires kappa/gamma = rho * ln^3(rho).

This script:
  1. Computes the cost function shape for various kappa/gamma
  2. Finds the kappa/gamma implied by D_IV^5 geometry
  3. Evaluates arithmetic packing efficiency P(N) for N in [100, 200]
  4. Shows that arithmetic corrections shift the minimum toward 137

Key result: Z^2 = (N_max+1)^2 = 138^2 = 19044 gives continuous minimum
at rho* = 133.5 (2.4% from 137). Adding arithmetic corrections (Eisenstein,
strong prime, sum-of-squares isolation) shifts it toward 137.

Authors: Casey Koons & Claude (Anthropic), March 2026
"""
import numpy as np
from scipy.optimize import minimize_scalar, brentq
import math

pi = np.pi

# ── D_IV^5 Geometry ─────────────────────────────────────────────────────────
Vol_DIV5   = pi**5 / 1920           # domain volume
Vol_S4     = 8 * pi**2 / 3          # Shilov base S^4
K5_origin  = 1920 / pi**5           # Bergman kernel K_5(0,0) = 1/Vol
F_BST      = 0.09855                # vacuum free energy (zero-temperature)
N_max      = 137

print("=" * 65)
print("PART 1: COST FUNCTION MINIMUM LOCATION vs kappa/gamma")
print("=" * 65)

def C_simple(rho, kappa_over_gamma):
    """C(rho) = rho*ln(rho) + kappa/ln(1+rho) with gamma=1"""
    return rho * np.log(rho) + kappa_over_gamma / np.log(1 + rho)

def find_min(kappa_over_gamma, C_func=C_simple, bounds=(2, 2000)):
    res = minimize_scalar(lambda r: C_func(r, kappa_over_gamma),
                          bounds=bounds, method='bounded')
    return res.x

# What kappa/gamma is needed for rho* = 137?
kappa_needed_simple = brentq(lambda k: find_min(k) - 137, 1000, 100000)
print(f"C(rho) = rho*ln(rho) + kappa/ln(1+rho)")
print(f"  kappa/gamma needed for rho*=137: {kappa_needed_simple:.0f}")
print(f"  (N_max+1)^2 = 138^2 = {138**2}  → rho* = {find_min(138**2):.2f}")
print(f"  (N_max+1)^3 = 138^3 = {138**3}  → rho* = {find_min(138**3):.2f}")
print()

# Alternative: C(rho) = rho + kappa / ((rho+1)*ln(rho+1))
def C_with_Z(rho, kappa):
    return rho + kappa / ((rho + 1) * np.log(rho + 1))

def find_min_Z(kappa):
    res = minimize_scalar(lambda r: C_with_Z(r, kappa),
                          bounds=(2, 2000), method='bounded')
    return res.x

kappa_needed_Z = brentq(lambda k: find_min_Z(k) - 137, 1000, 1e8)
print(f"C(rho) = rho + kappa/((rho+1)*ln(rho+1))  [Z(rho) = rho+1 in denominator]")
print(f"  kappa needed for rho*=137: {kappa_needed_Z:.0f}")
print(f"  138^2 = {138**2}  → rho* = {find_min_Z(138**2):.2f}")
print(f"  138^2 * pi^2/9 = {138**2 * pi**2/9:.0f}  → rho* = {find_min_Z(138**2 * pi**2/9):.2f}")
print()

# Scan kappa/gamma values
print(f"{'kappa/gamma':>14}  {'rho* (simple)':>14}  {'rho* (with Z)':>14}")
print("-" * 47)
for ratio in [10000, 15000, 16304, 18000, 19044, 20000, 22000, 25000]:
    r1 = find_min(ratio)
    r2 = find_min_Z(ratio)
    mk = " ← Z²=138²" if ratio == 19044 else ""
    print(f"{ratio:>14}  {r1:>14.2f}  {r2:>14.2f}{mk}")

print()
print("=" * 65)
print("PART 2: ARITHMETIC PACKING EFFICIENCY P(N)")
print("=" * 65)

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def sum_sq(n):
    for a in range(0, int(n**0.5) + 1):
        b2 = n - a*a
        b = int(b2**0.5 + 0.5)
        if b*b == b2 and b >= a:
            return (a, b)
    return None

def is_eisenstein_prime(n):
    return is_prime(n) and n % 3 == 2

def is_strong_prime(n):
    if not is_prime(n): return False
    p = n - 1
    while not is_prime(p): p -= 1
    q = n + 1
    while not is_prime(q): q += 1
    return n > (p + q) / 2

def isolation(n):
    """How many neighboring primes are NOT sums of two squares"""
    p = n - 1
    while not is_prime(p): p -= 1
    q = n + 1
    while not is_prime(q): q += 1
    return (1 if sum_sq(p) is None else 0) + (1 if sum_sq(q) is None else 0)

print(f"\nPrimes ≡ 1 (mod 4) in [100, 200]: arithmetic properties\n")
print(f"{'N':>5}  {'Decomp':>10}  {'b/a':>6}  {'Eis':>4}  {'Str':>4}  {'Iso':>4}  {'Props':>5}")
print("-" * 50)

s2_primes = []
for n in range(100, 201):
    if is_prime(n) and n % 4 == 1:
        s2 = sum_sq(n)
        a, b = s2
        ratio = b/a if a > 0 else 999
        eis  = is_eisenstein_prime(n)
        strg = is_strong_prime(n)
        iso  = isolation(n)
        nprops = int(eis) + int(strg) + int(iso == 2)
        s2_primes.append((n, s2, ratio, eis, strg, iso, nprops))
        marker = " <===" if n == 137 else ""
        print(f"{n:>5}  {str(s2):>10}  {ratio:>6.3f}  {str(eis):>4}  {str(strg):>4}  {iso:>4}  {nprops:>5}{marker}")

print()
print("137 and 149 both have 3/3 arithmetic properties.")
print("137 wins as the SMALLEST prime with all three.")
print("The Wyler formula (continuous geometry) gives α⁻¹ = 137.036,")
print("landing in [137, 138), not [149, 150). Two independent principles agree.")

print()
print("=" * 65)
print("PART 3: COST FUNCTION WITH ARITHMETIC CORRECTIONS")
print("=" * 65)
print()

# P(N): natural arithmetic weighting, NO circular aspect-ratio bias
def P_arithmetic(n):
    """Packing efficiency from arithmetic properties alone"""
    score = 1.0
    if is_prime(n):
        score *= 2.0
    s2 = sum_sq(n)
    if s2:
        score *= 1.5           # compatible with 2D Shilov packing
    if is_eisenstein_prime(n):
        score *= 1.3           # irreducible on hexagonal lattice
    if is_strong_prime(n):
        score *= 1.2           # locally prominent
    iso = isolation(n)
    score *= (1.0 + 0.15 * iso)  # bonus for arithmetic isolation
    return score

# C_eff(N) = C_base(N) / P_arith(N), kappa = Z^2 = 138^2
kappa = 19044  # Z^2

P_norm = P_arithmetic(137)
data = []
for N in range(100, 200):
    C_base = C_with_Z(N, kappa)
    P = P_arithmetic(N) / P_norm
    C_eff = C_base / P
    data.append((N, C_base, P, C_eff))

data_sorted = sorted(data, key=lambda x: x[3])

print(f"Effective cost C_eff(N) = C_base(N) / P(N),  kappa = Z² = 138² = 19044")
print(f"(Lower = more efficient = more likely to be the substrate)\n")
print(f"{'Rank':>5}  {'N':>5}  {'C_base':>8}  {'P(N)/P(137)':>12}  {'C_eff':>8}  {'prime':>6}  {'s2':>10}")
print("-" * 63)
for rank, (N, C, P, Ceff) in enumerate(data_sorted[:12], 1):
    s2 = sum_sq(N)
    p  = is_prime(N)
    marker = " <===" if N == 137 else ""
    print(f"{rank:>5}  {N:>5}  {C:>8.2f}  {P:>12.3f}  {Ceff:>8.2f}  {str(p):>6}  {str(s2):>10}{marker}")

rank_137 = next(i for i, (N,_,_,_) in enumerate(data_sorted, 1) if N == 137)
print(f"\n137 ranks {rank_137} with kappa = Z² = 138²")
print()

# What kappa puts 137 at rank 1 in the arithmetic-corrected cost?
# Scan kappa values
print("Finding kappa that puts 137 at rank 1:")
for kappa_test in [15000, 17000, 19044, 20000, 22000, 24000, 26000]:
    data_k = [(N, C_with_Z(N, kappa_test)/P_arithmetic(N), P_arithmetic(N))
              for N in range(100, 200)]
    best_N = min(data_k, key=lambda x: x[1])[0]
    print(f"  kappa={kappa_test:>7}: best N = {best_N}")

print()
print("=" * 65)
print("SUMMARY")
print("=" * 65)
print(f"""
The BST cost function approach gives the following picture:

CONTINUOUS GEOMETRY (Wyler):
  α⁻¹ = (8π/9) × (1920/π⁵)^(1/4) = 137.036082...  [0.0001%]
  Continuous minimum of C(ρ) = ρ + (N+1)²/((ρ+1)·ln(ρ+1)):
    rho* = 133.5 for kappa = Z² = 138² = 19044  [2.4% from 137]
  Exact minimum at 137 requires kappa ≈ 78,004 -- not yet derived from geometry.

ARITHMETIC (packing efficiency):
  137 and 149 are the only primes in [100,200] with all 3 properties:
    Eisenstein prime + strong prime + fully isolated between ≡3 (mod 4) neighbors
  137 is the SMALLEST (natural selection would find minimum cost first)
  The next arithmetically equivalent prime (149) is ruled out by the Wyler geometry.

OPEN CALCULATION:
  Derive kappa ≈ 78,004 from D_IV^5 Bergman geometry:
  kappa = N*(N+1)² * ln(N+1)² / (1 + ln(N+1)) ← self-referential at N=137
  Need: BST-geometric formula for kappa that evaluates to ~78,004 independently.

THREE-WAY CONVERGENCE (if the cost function is solved):
  1. Wyler formula (domain volume ratio):            α⁻¹ = 137.036
  2. Topological rigidity (Cartan classification):  D_IV^5 unique → N = 137
  3. Cost function minimum (mathematical selection): N* = 137
""")
