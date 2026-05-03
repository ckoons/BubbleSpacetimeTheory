"""
Toy 1791: Spectral Zeta Closed Form Candidates
================================================
From Toys 1785/1789: zB(4)*N_max^2 = n_C^3 at 0.02%.

Systematic search for BST closed forms of zeta_B(s) at integer points.
Key question: are the spectral zeta values at BST integers expressible
as simple BST fractions, or do they require transcendental corrections?

The Fox H classification (Lyra Toy 1787) says zB(s) IS a Fox H function.
Fox H at integer points CAN reduce to algebraic expressions involving
Gamma ratios. So exact BST forms may exist.

Author: Elie | Date: 2026-05-02
"""

from mpmath import (mp, mpf, log, exp, pi, zeta, fsum, fac,
                     nstr, power, sqrt, gamma as mpgamma, pslq,
                     rf)  # rf = rising factorial

mp.dps = 60

# BST integers
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137

pass_count = 0
fail_count = 0
total_tests = 0

def test(name, condition, detail=""):
    global pass_count, fail_count, total_tests
    total_tests += 1
    tag = "PASS" if condition else "FAIL"
    if condition:
        pass_count += 1
    else:
        fail_count += 1
    print(f"  T{total_tests} [{tag}] {name}")
    if detail:
        print(f"       {detail}")

def d(k):
    k = mpf(k)
    return (2*k + n_C) * (k+1) * (k+2) * (k+3) * (k+4) / fac(n_C)

def lam(k):
    return mpf(k) * (mpf(k) + n_C)

def zeta_B(s, N=30000):
    s = mpf(s)
    return fsum(d(k) / lam(k)**s for k in range(1, N+1))

# ============================================================
# PART 1: HIGH-PRECISION VALUES
# ============================================================
print("=" * 70)
print("PART 1: High-Precision Spectral Zeta Values")
print("=" * 70)

zB = {}
for s in range(4, 12):
    zB[s] = zeta_B(s, 30000)
    print(f"  zB({s:2d}) = {nstr(zB[s], 25)}")

# Also s = 7/2
zB_72 = zeta_B(mpf(7)/2, 30000)
print(f"  zB(7/2) = {nstr(zB_72, 25)}")

# ============================================================
# PART 2: n_C^3/N_max^2 CANDIDATE FOR zB(4)
# ============================================================
print()
print("=" * 70)
print("PART 2: zB(4) = n_C^3/N_max^2 Candidate")
print("=" * 70)

candidate_4 = mpf(n_C**3) / N_max**2  # 125/18769
gap_4 = abs(zB[4] - candidate_4) / zB[4] * 100
print(f"  zB(4)         = {nstr(zB[4], 20)}")
print(f"  n_C^3/N_max^2 = {nstr(candidate_4, 20)}")
print(f"  Gap = {float(gap_4):.4f}%")

test("zB(4) ~ n_C^3/N_max^2 at < 0.05%",
     gap_4 < mpf('0.05'),
     f"125/18769, gap = {float(gap_4):.4f}%")

# What is the exact difference?
diff_4 = zB[4] - candidate_4
print(f"\n  zB(4) - n_C^3/N_max^2 = {nstr(diff_4, 15)}")
print(f"  This is {float(diff_4/candidate_4 * 100):.4f}% of the candidate")

# Is the difference itself a BST fraction?
diff_scaled = diff_4 * N_max**2
print(f"  (zB(4) - 125/N_max^2) * N_max^2 = {float(diff_scaled):.8f}")
# Check: is this close to a BST fraction?
for p in range(1, 50):
    for q in range(1, 200):
        val = mpf(p) / q
        if abs(diff_scaled - val) / abs(diff_scaled) < 0.01:
            print(f"    ~ {p}/{q} ({float(abs(diff_scaled - val)/abs(diff_scaled)*100):.4f}%)")

# ============================================================
# PART 3: SYSTEMATIC BST FRACTION SEARCH AT ALL s
# ============================================================
print()
print("=" * 70)
print("PART 3: Systematic BST Closed Form Search")
print("=" * 70)

# Build BST expression basis
bst_atoms = {
    'rank': rank, 'N_c': N_c, 'n_C': n_C, 'C_2': C_2, 'g': g, 'N_max': N_max,
    'C_2^2': C_2**2, 'g^2': g**2, 'N_max^2': N_max**2,
    'n_C!': 120, 'd_1': 7, 'C_2^3': C_2**3,
    'N_c*n_C': N_c*n_C, 'C_2*g': C_2*g, 'rank*n_C': rank*n_C,
    'N_c^2': N_c**2, 'n_C^2': n_C**2, 'n_C^3': n_C**3,
    'g^3': g**3, 'C_2^C_2': C_2**C_2, 'N_max^3': N_max**3,
}

for s in range(4, 11):
    val = zB[s]
    print(f"\n  zB({s}) = {nstr(val, 18)}")

    # Try p/q where p and q are products of BST atoms
    best_name = ""
    best_pct = 100.0

    # Simple fractions a/b where a,b are BST products
    for nname, nval in bst_atoms.items():
        for dname, dval in bst_atoms.items():
            if dval == 0:
                continue
            candidate = mpf(nval) / dval
            if candidate > 0 and candidate < 1:  # zB values are small
                pct = float(abs(val - candidate) / abs(val) * 100)
                if pct < best_pct:
                    best_pct = pct
                    best_name = f"{nname}/{dname} = {nval}/{dval}"

            # Also try 1/(a*b) forms
            candidate2 = mpf(1) / (nval * dval)
            if candidate2 > 0:
                pct2 = float(abs(val - candidate2) / abs(val) * 100)
                if pct2 < best_pct:
                    best_pct = pct2
                    best_name = f"1/({nname}*{dname}) = 1/{nval*dval}"

    # Also try a/(b*c) forms for small combinations
    for nname, nval in [('1', 1), ('rank', rank), ('N_c', N_c), ('n_C', n_C), ('g', g)]:
        for d1name, d1val in bst_atoms.items():
            for d2name, d2val in [('N_max', N_max), ('N_max^2', N_max**2), ('C_2^C_2', C_2**C_2), ('g^3', g**3)]:
                denom = d1val * d2val
                if denom == 0:
                    continue
                candidate = mpf(nval) / denom
                if candidate > 0:
                    pct = float(abs(val - candidate) / abs(val) * 100)
                    if pct < best_pct:
                        best_pct = pct
                        best_name = f"{nname}/({d1name}*{d2name}) = {nval}/{denom}"

    if best_pct < 5:
        marker = " **" if best_pct < 0.1 else " *" if best_pct < 1 else ""
        print(f"    Best: {best_name} ({best_pct:.4f}%){marker}")
    else:
        print(f"    No BST match < 5% (best: {best_name} at {best_pct:.2f}%)")

# ============================================================
# PART 4: PSLQ WITH BST-ENRICHED BASIS
# ============================================================
print()
print("=" * 70)
print("PART 4: PSLQ Against BST-Enriched Basis")
print("=" * 70)

# For zB(4): try expressing as combination of 1/N_max^2 and BST rationals
mp.dps = 40

# Basis: zB(4), 1/N_max^2, 1/(N_max^2*C_2), 1/(N_max^2*g), 1/(N_max^2*n_C), 1
basis_4 = [
    zB[4],
    mpf(1) / N_max**2,
    mpf(1) / (N_max**2 * C_2),
    mpf(1) / (N_max**2 * g),
    mpf(1) / (N_max**2 * n_C),
    mpf(1) / (N_max**2 * N_c),
]
names_4 = ["zB(4)", "1/N_max^2", "1/(N_max^2*C_2)", "1/(N_max^2*g)",
           "1/(N_max^2*n_C)", "1/(N_max^2*N_c)"]

result = pslq(basis_4)
if result:
    print(f"\n  PSLQ for zB(4) against N_max^2-based fractions:")
    for c, n in zip(result, names_4):
        if c != 0:
            print(f"    {c:>8d} * {n}")
    print(f"  = 0")

    # Verify
    if result[0] != 0:
        recon = -sum(result[i] * basis_4[i] for i in range(1, len(result))) / result[0]
        err = abs(recon - zB[4]) / zB[4] * 100
        print(f"  Reconstruction error: {float(err):.2e}%")
        test("PSLQ zB(4) = BST/N_max^2 decomposition",
             err < mpf('0.001'),
             f"error = {float(err):.2e}%")
else:
    print(f"  PSLQ: no relation found against N_max^2 basis")

# Try for zB(6) against C_2^C_2 basis
basis_6 = [
    zB[6],
    mpf(1) / C_2**C_2,
    mpf(g) / C_2**C_2,
    mpf(1) / (C_2**C_2 * C_2),
    mpf(1) / (C_2**C_2 * g),
    mpf(1) / (C_2**C_2 * n_C),
]
names_6 = ["zB(6)", "1/C_2^C_2", "g/C_2^C_2", "1/(C_2^(C_2+1))",
           "1/(C_2^C_2*g)", "1/(C_2^C_2*n_C)"]

result_6 = pslq(basis_6)
if result_6:
    print(f"\n  PSLQ for zB(6) against C_2^C_2-based fractions:")
    for c, n in zip(result_6, names_6):
        if c != 0:
            print(f"    {c:>8d} * {n}")
    print(f"  = 0")
else:
    print(f"\n  PSLQ: no relation found for zB(6) against C_2^C_2 basis")

# ============================================================
# PART 5: RATIO CLOSED FORMS
# ============================================================
print()
print("=" * 70)
print("PART 5: Exact BST Ratios Between Evaluation Points")
print("=" * 70)

# From Toy 1789: zB(C_2)/zB(g) ~ 439/72 at 0.0007%
# 439 = C_2^3*rank + g
# 72 = C_2^2*rank

# Are ALL adjacent ratios BST fractions of this type?
print(f"\n  Adjacent ratios zB(s)/zB(s+1):")
print(f"  {'s':>4s} | {'ratio':>18s} | {'BST candidate':>25s} | {'gap %':>10s}")
print("  " + "-" * 70)

# For each ratio, try (a*lam_1^2 + b*lam_1 + c) / d type expressions
# where a,b,c,d are BST integers

for s in range(4, 10):
    ratio = zB[s] / zB[s+1]

    # The ratio approaches lam_1 = C_2 = 6
    # Excess = ratio - 6 ~ (d_2/d_1)*(lam_1/lam_2)^s * (lam_2 - lam_1)
    # = (55/7)*(6/14)^s * 8

    # Try p/q search with larger range
    best_p, best_q, best_err = 0, 1, mpf('inf')
    for q in range(1, 1000):
        p_approx = int(float(ratio) * q + 0.5)
        for p in range(max(1, p_approx - 2), p_approx + 3):
            err = abs(ratio - mpf(p)/q)
            if err < best_err:
                best_err = err
                best_p, best_q = p, q

    pct = float(best_err / ratio * 100)

    # Try to express p and q in BST terms
    p_bst = f"{best_p}"
    q_bst = f"{best_q}"

    # Check if numerator/denominator factor into BST integers
    print(f"  {s:4d} | {float(ratio):18.10f} | {best_p:>6d}/{best_q:<6d} | {pct:10.6f}%")

# ============================================================
# PART 6: THE GENERATING FUNCTION CONNECTION
# ============================================================
print()
print("=" * 70)
print("PART 6: Spectral Zeta as Evaluation of Generating Function")
print("=" * 70)

# zB(s) = sum d_k / lambda_k^s
# d_k = dim of k-th eigenspace on Q^5
# lambda_k = k(k+5)
#
# The generating function: sum d_k * x^k = (1+x)/(1-x)^6
# (Hilbert series of Q^5 = CP^5 analog)
#
# So zB(s) "evaluates the Hilbert series at x = exp(-t*lambda_k)"
# in some Mellin-transformed sense.
#
# More precisely: the heat trace K(t) = sum d_k * exp(-lambda_k * t)
# and zB(s) = (1/Gamma(s)) * int_0^inf t^{s-1} * K(t) dt

# The Hilbert series: H(x) = sum d_k * x^k = (1+x)/(1-x)^6
# Verify:
print(f"  Hilbert series check:")
for k in [1, 2, 3, 5, 10]:
    d_val = d(k)
    # Coefficient of x^k in (1+x)/(1-x)^6
    # = C(k+5,5) + C(k+4,5) (from 1/(1-x)^6 and x/(1-x)^6)
    from mpmath import binomial
    h_val = binomial(k+5, 5) + binomial(k+4, 5)
    match = abs(d_val - h_val) < mpf('1e-10')
    print(f"    k={k}: d_k = {int(d_val)}, Hilbert coeff = {int(h_val)}, match = {match}")

test("Hilbert series (1+x)/(1-x)^6 gives d_k",
     all(abs(d(k) - binomial(k+5,5) - binomial(k+4,5)) < mpf('1e-10') for k in range(1, 20)),
     "Verified k=1..19")

# The connection: zB(s) is a "spectral evaluation" of the Hilbert series
# H(x) at x related to the eigenvalues.
#
# In fact: since lambda_k = k(k+5), we can write
# zB(s) = sum H_k * [k(k+5)]^{-s}
# where H_k is the k-th Hilbert coefficient.
#
# For the Hilbert series: sum H_k * x^k = (1+x)/(1-x)^6
# So zB(s) = sum_{k=1}^inf (H_k / k^s) * (1/(1+5/k))^s
#
# The factor (1+5/k)^{-s} couples the Hilbert structure to the
# eigenvalue structure. At s=0: zB(0) = sum H_k * 1 - H_0 = divergent
# but regularized via the Hilbert series at x=1 minus H_0.

# ============================================================
# PART 7: GAMMA RATIO PREDICTIONS FROM FOX H
# ============================================================
print()
print("=" * 70)
print("PART 7: Fox H Gamma Ratio Predictions")
print("=" * 70)

# From Lyra Toy 1787: zB(s) is a Fox H function with parameters
# from the B_2 root system.
#
# The Fox H function at integer points reduces to:
# products of Gamma functions evaluated at BST rationals.
#
# Specifically, the Gamma ratios from the c-function:
# c_reg(s) = Gamma(2s)/Gamma(2s+3/2) * [Gamma(s)/Gamma(s+1/2)]^2
#
# At integer s, these give specific rational * pi products.

# Let me compute the c-function ratio at integer points
def c_reg(s):
    """Regularized c-function for B_2(3,1) on Bergman line"""
    s = mpf(s)
    return mpgamma(2*s) / mpgamma(2*s + mpf(3)/2) * (mpgamma(s) / mpgamma(s + mpf(1)/2))**2

print(f"  c-function values at integer points:")
for s in range(1, 10):
    c_val = c_reg(s)
    print(f"    c_reg({s}) = {nstr(c_val, 15)}")

# c-function RATIO c_reg(s)/c_reg(s+1)
print(f"\n  c-function ratios (should relate to zB ratios):")
for s in range(1, 8):
    c_ratio = c_reg(s) / c_reg(s + 1)
    z_ratio = zB[max(4, s)] / zB[max(4, s) + 1] if max(4, s) + 1 in zB else mpf(0)
    print(f"    c_reg({s})/c_reg({s+1}) = {float(c_ratio):.8f}")

# The FE says: zB(s) * Gamma_factor(s) = zB(5-s) * Gamma_factor(5-s)
# where Gamma_factor involves c_reg.
#
# At s=4 and s=1 (which are related by 5-s reflection):
# zB(4) * c_reg(4) = zB(1) * c_reg(1)  (up to normalization)
#
# This gives zB(4) in terms of zB(1) and Gamma ratio.
# But zB(1) requires analytic continuation.

# Instead, let me check: does c_reg(s)/c_reg(s+1) predict zB(s)/zB(s+1)?
# If the FE is "multiplicative", then zB(s)/zB(s+1) should factor as:
# (eigenvalue ratio) * (c-function correction)

print(f"\n  Check: zB(s)/zB(s+1) vs C_2 * c_reg(s+1)/c_reg(s):")
for s in range(4, 9):
    z_ratio = zB[s] / zB[s + 1]
    c_corr = mpf(C_2) * c_reg(s + 1) / c_reg(s)
    pct = float(abs(z_ratio - c_corr) / z_ratio * 100)
    print(f"    s={s}: zB ratio = {float(z_ratio):.8f}, C_2*c_inv = {float(c_corr):.8f}, gap = {pct:.2f}%")

# ============================================================
# PART 8: SUMMARY TABLE
# ============================================================
print()
print("=" * 70)
print("PART 8: Summary — BST Content of Spectral Zeta Values")
print("=" * 70)

print(f"""
  VALUE CANDIDATES (ordered by precision):

  | Quantity                  | BST Candidate            | Precision |
  |--------------------------|--------------------------|-----------|
  | zB(C_2)/zB(g)            | 439/72 = (C_2^3r+g)/(C_2^2r) | 0.0007% |
  | zB(4)*N_max^2            | n_C^3 = 125              | 0.026%  |
  | N_c*zB(4)+rank*zB(8)     | 1/(n_C^2*rank) = 1/50    | 0.040%  |
  | zB(g/rank) = zB(7/2)     | 1/g^2 = 1/49             | 0.080%  |
  | cross ratio (4,6)/(5,7)  | C_2*g = 42               | 0.139%  |
  | zB(C_2)                  | g/C_2^C_2 = 7/46656      | 2.74%   |

  STRUCTURAL:
  - 439 = C_2^3*rank + g (prime), same pattern as N_max = N_c^3*n_C + rank
  - Eigenvalue hierarchy: 1st order g/N_c = 7/3, 2nd order 12/7 = C_2*rank/g
  - Hilbert series: (1+x)/(1-x)^6
  - PSLQ null: values are NOT combinations of Riemann zeta values
  - Fox H classification: alpha=2, z=(n_C/rank)^2=25/4
""")

print(f"SCORE: {pass_count}/{total_tests} PASS ({fail_count} FAIL)")
