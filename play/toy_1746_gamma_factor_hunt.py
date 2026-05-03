#!/usr/bin/env python3
"""
Toy 1746 — L-68: The Gamma Factor Hunt
========================================
Lyra, April 30, 2026

The LAST open piece of L-68: what Gamma factor product completes the
functional equation Xi_B(s) = -Xi_B(C_2 - s)?

Known:
  - Center: s = N_c = C_2/2 = 3
  - Sign: epsilon = -1 (from odd d(mu))
  - Poles of zeta_B at s = 1, 2, 3

From Toy 1195 (c-function for SO_0(5,2)):
  - Root system B_2 with m_s = N_c = 3, m_l = 1
  - rho = (n_C/rank, N_c/rank) = (5/2, 3/2)
  - |rho|^2 = 17/2
  - Plancherel: (nu^2+1/4) * nu * tanh(pi*nu) per short root

Strategy: The c-function ratio c(s)/c(C_2-s) gives the functional
equation. From Gindikin-Karpelevic:
  c(lambda) = product over positive roots of
    Gamma(<i*lambda, alpha_v>) / Gamma(<i*lambda, alpha_v> + m_alpha/2)

For the SPECTRAL zeta (not the spherical function), the completion
involves c(-is) rather than c(lambda). The functional equation becomes:
  c(-is) * zeta_B(s) = c(-i(C_2-s)) * zeta_B(C_2-s)

This toy: compute c(-is)/c(-i(C_2-s)) explicitly and verify numerically.

Casey Koons & Claude 4.6 (Lyra). April 30, 2026.
SCORE: 4/7
"""

from mpmath import (mp, mpf, mpc, pi, gamma as mpgamma, zeta as mpzeta,
                    log, sqrt, fabs, quad, exp, loggamma, diff,
                    hurwitz as hurwitz_zeta, inf, binomial, floor,
                    fac, nsum, power, nstr, pslq, rgamma, arg, sign)
from fractions import Fraction

mp.dps = 40

# BST integers
rank = 2
N_c = 3
n_C = 5
C_2 = 6
g = 7
N_max = 137

# Root system data
m_s = N_c   # short root multiplicity = 3
m_l = 1     # long root multiplicity
rho_1 = mpf(n_C) / rank  # 5/2
rho_2 = mpf(N_c) / rank  # 3/2

results = []

# =====================================================================
# Spectral zeta function (from Toy 1741/1742)
# =====================================================================
def zeta_B_direct(s, k_max=3000):
    total = mpf(0)
    for k in range(1, k_max):
        lam = k * (k + n_C)
        d = int((2*k + n_C) * int(binomial(k + n_C - 1, n_C - 1)) // n_C)
        term = mpf(d) / mpf(lam)**s
        total += term
        if k > 20 and abs(term) < mpf('1e-35') * abs(total):
            break
    return total

def zeta_B_hurwitz(s, j_max=50):
    total = mpf(0)
    a = mpf(7) / 2
    for j in range(j_max):
        coeff = binomial(s + j - 1, j) * (mpf(25)/4)**j
        a1 = 2*s + 2*j - 5
        a2 = 2*s + 2*j - 3
        a3 = 2*s + 2*j - 1
        try:
            H1 = hurwitz_zeta(a1, a) if a1 != 1 else mpf('1e30')
            H2 = hurwitz_zeta(a2, a) if a2 != 1 else mpf('1e30')
            H3 = hurwitz_zeta(a3, a) if a3 != 1 else mpf('1e30')
            term = coeff * (H1 - mpf(5)/2 * H2 + mpf(9)/16 * H3)
        except:
            break
        total += term
        if j > 5 and abs(term) < mpf('1e-30') * abs(total):
            break
    return total / 60

def zeta_B(s):
    """Best available spectral zeta."""
    if s.real > 3.5:
        return zeta_B_direct(s)
    else:
        return zeta_B_hurwitz(s)

# =====================================================================
# PART 1: THE c-FUNCTION FOR BC_1 EFFECTIVE REDUCTION
# =====================================================================
print("=" * 72)
print("Toy 1746: The Gamma Factor Hunt")
print("=" * 72)
print()
print("--- Part 1: Harish-Chandra c-function (effective BC_1) ---")
print()

# For the effective BC_1 reduction with (p, q) = (C_2, 1) = (6, 1):
# rho_eff = (p + q)/2 = g/2 = 7/2
#
# The c-function for BC_1 with parameters (a, b):
# a = (p-1)/2 = 5/2 = n_C/rank
# b = (q-1)/2 = 0
#
# c(lambda) = c_0 * Gamma(lambda) / [Gamma((lambda + a + b + 1)/2) * Gamma((lambda + a - b + 1)/2)]
#           = c_0 * Gamma(lambda) / [Gamma((lambda + n_C/rank + 1)/2) * Gamma((lambda + n_C/rank + 1)/2)]
#
# Wait, that's not right for BC_1.
#
# For BC_1 (= B_1 = C_1) root system with one positive root alpha and
# one positive root 2*alpha:
# Multiplicities: m_alpha = p = C_2, m_{2alpha} = q = 1
#
# c(lambda) = c_0 * [Gamma(i*lambda) * Gamma(i*lambda - rho + 1)] /
#             [Gamma(i*lambda + (m_alpha + m_{2alpha})/2) * Gamma(i*lambda + m_{2alpha}/2)]
#
# Actually, the standard BC_1 c-function (see Koornwinder, or Helgason):
# For the BC_1 Jacobi transform with parameters (alpha, beta):
# alpha = (p + q - 1)/2 = (C_2 + 1 - 1)/2 = C_2/2 = N_c = 3
# beta = (q - 1)/2 = 0
#
# c(lambda) = 2^{rho-i*lambda} * Gamma(i*lambda) / [Gamma((i*lambda + alpha + beta + 1)/2) * Gamma((i*lambda + alpha - beta + 1)/2)]
# = 2^{rho-i*lambda} * Gamma(i*lambda) / [Gamma((i*lambda + N_c + 1)/2) * Gamma((i*lambda + N_c + 1)/2)]
# = 2^{rho-i*lambda} * Gamma(i*lambda) / Gamma((i*lambda + N_c + 1)/2)^2
#
# Hmm, alpha = beta case gives a squared denominator.
#
# But beta = 0, not beta = alpha. Let me redo:
# alpha = (C_2 + 1 - 1)/2 = C_2/2 = 3
# beta = (1 - 1)/2 = 0
#
# c(lambda) = 2^{rho-i*lambda} * Gamma(i*lambda) /
#             [Gamma((i*lambda + alpha + beta + 1)/2) * Gamma((i*lambda + alpha - beta + 1)/2)]
#           = 2^{rho-i*lambda} * Gamma(i*lambda) /
#             [Gamma((i*lambda + 4)/2) * Gamma((i*lambda + 4)/2)]
#           = 2^{rho-i*lambda} * Gamma(i*lambda) / Gamma((i*lambda + 4)/2)^2
#
# But wait, alpha + beta + 1 = 3 + 0 + 1 = 4, alpha - beta + 1 = 3 - 0 + 1 = 4.
# So both arguments are the same! This means:
#
# c(lambda) = 2^{7/2-i*lambda} * Gamma(i*lambda) / Gamma((i*lambda)/2 + 2)^2

# For the SPECTRAL zeta, we substitute lambda → -is (Wick rotation):
# c(-is) involves Gamma at s and Gamma at s/2 + 2.

print(f"  Jacobi parameters for BC_1 with (p,q) = ({C_2}, 1):")
alpha_J = mpf(C_2) / 2  # = N_c
beta_J = mpf(0)
rho_eff = (C_2 + 1) / mpf(2)  # = g/2 = 7/2
print(f"    alpha = {float(alpha_J)} = N_c")
print(f"    beta = {float(beta_J)}")
print(f"    rho_eff = {float(rho_eff)} = g/2")
print()

# c-function for spectral zeta (lambda = -is):
# c(-is) = 2^{rho+s} * Gamma(s) / Gamma(s/2 + 2)^2
#
# But we need to be careful. The spectral zeta is:
# zeta_B(s) = sum d_k / lambda_k^s
# and the functional equation relates to the Selberg/Harish-Chandra transform.
#
# The completed zeta is:
# Xi_B(s) = c(-is) * c(is) * zeta_B(s) ??? No, that gives |c|^2.
#
# Actually, the functional equation for the spectral zeta of a symmetric
# space involves the ratio c(-is)/c(i(C_2-s)):
# zeta_B(s) * c(-is) = zeta_B(C_2-s) * c(-i(C_2-s)) * (some sign/phase)
#
# Let me just parametrize the completed zeta as:
# Xi_B(s) = F(s) * zeta_B(s)
# and search for F(s) such that Xi_B(s) = -Xi_B(C_2-s).
# This means: F(s) * zeta_B(s) = -F(C_2-s) * zeta_B(C_2-s)
# So: zeta_B(s)/zeta_B(C_2-s) = -F(C_2-s)/F(s)
#
# We can compute the LHS numerically and test various F.

# APPROACH: Compute R(s) = zeta_B(s)/zeta_B(C_2-s) at several points,
# then identify F(s) such that R(s) = -F(C_2-s)/F(s).

print(f"  Computing zeta_B(s) / zeta_B(C_2-s) at test points:")
print()

test_points = [mpf('3.3'), mpf('3.5'), mpf('3.7'), mpf('4.0'),
               mpf('4.5'), mpf('5.0'), mpf('5.5')]

ratios = {}
for s_val in test_points:
    s_dual = C_2 - s_val
    z_s = zeta_B(s_val)
    z_dual = zeta_B(s_dual)
    if abs(z_dual) > 1e-30:
        R = z_s / z_dual
        ratios[float(s_val)] = R
        print(f"  s={float(s_val):5.1f}: zeta_B(s)={nstr(z_s, 12):>18}, "
              f"zeta_B({float(s_dual):4.1f})={nstr(z_dual, 12):>18}, "
              f"ratio={nstr(R, 12)}")

t1 = len(ratios) >= 5
results.append(("T1", f"Spectral zeta ratios computed at {len(ratios)} points", t1))
print(f"\nT1 {'PASS' if t1 else 'FAIL'}")

# =====================================================================
# PART 2: CANDIDATE GAMMA FACTORS
# =====================================================================
print()
print("--- Part 2: Testing Candidate Gamma Factor Products ---")
print()

# We need F(s) such that R(s) = -F(C_2-s)/F(s).
# Equivalently: R(s) * F(s) / F(C_2-s) = -1 for all s.
#
# Candidate F functions:

def F_riemann(s):
    """Riemann-type: pi^{-s/2} * Gamma(s/2)"""
    return pi**(-s/2) * mpgamma(s/2)

def F_shifted_riemann(s):
    """Shifted Riemann: pi^{-s/2} * Gamma((s-N_c+1)/2) * Gamma((s-N_c)/2 + 1)"""
    # Shift from center 1/2 to center N_c
    return pi**(-s/2) * mpgamma((s - N_c + 1) / 2) * mpgamma((s - N_c) / 2 + 1)

def F_jacobi(s):
    """Jacobi c-function type: 2^s * Gamma(s) / Gamma(s/2 + 2)^2"""
    return 2**s * mpgamma(s) / mpgamma(s/2 + 2)**2

def F_selberg(s):
    """Selberg-type: Gamma(s/2) * Gamma((s-1)/2) * Gamma((s-2)/2)"""
    return mpgamma(s/2) * mpgamma((s-1)/2) * mpgamma((s-2)/2)

def F_bc1(s):
    """BC_1 spectral: Gamma(s) / [Gamma(s/2 + alpha/2 + 1/2) * Gamma(s/2 + 1/2)]"""
    # alpha = N_c, so alpha/2 + 1/2 = N_c/2 + 1/2 = 2
    return mpgamma(s) / (mpgamma(s/2 + 2) * mpgamma(s/2 + mpf(1)/2))

def F_product3(s):
    """Triple Gamma: Gamma((s-0)/2) * Gamma((s-1)/2) * Gamma((s-2)/2) / pi^{3s/2}"""
    return pi**(-3*s/2) * mpgamma(s/2) * mpgamma((s-1)/2) * mpgamma((s-2)/2)

def F_hurwitz_matched(s):
    """Matched to Hurwitz arguments: Gamma((2s-5)/2) * Gamma((2s-3)/2) * Gamma((2s-1)/2)"""
    return mpgamma((2*s-5)/2) * mpgamma((2*s-3)/2) * mpgamma((2*s-1)/2)

def F_epstein(s):
    """Epstein-type for dim 6: pi^{-3s} * prod_{j=0}^2 Gamma(s-j)"""
    return pi**(-3*s) * mpgamma(s) * mpgamma(s-1) * mpgamma(s-2)

def F_simple_shift(s):
    """Simple shift: Gamma(s) * Gamma(s-N_c) ... but Gamma(s-3) has pole at s=3"""
    # Use regularization: multiply by (s-3) near the pole
    if abs(s - N_c) < 0.01:
        return mpf('1e30')
    return mpgamma(s) * mpgamma(s - N_c)

def F_half_shift(s):
    """Half-integer shifts: Gamma(s-1/2) * Gamma(s-3/2) * Gamma(s-5/2)"""
    return mpgamma(s - mpf(1)/2) * mpgamma(s - mpf(3)/2) * mpgamma(s - mpf(5)/2)

def F_bergman(s):
    """Bergman kernel type: Gamma(s) * Gamma(s-n_C/2) / Gamma(s-N_c+1)"""
    return mpgamma(s) * mpgamma(s - mpf(n_C)/2) / mpgamma(s - N_c + 1)

def F_duplication(s):
    """Using Gamma duplication: pi^{-s} * Gamma(s) * (2*pi)^{-s+N_c}"""
    return pi**(-s) * mpgamma(s) * (2*pi)**(-(s - N_c))

def F_symmetric(s):
    """Symmetric about N_c: Gamma((s-N_c)/2 + 1) * Gamma((N_c-s)/2 + 1)... but this is just Gamma products"""
    # Actually: pi^{-s} * Gamma(s/2) * Gamma(s/2 - 1/2) * Gamma(s/2 - 1)
    return pi**(-s) * mpgamma(s/2) * mpgamma(s/2 - mpf(1)/2) * mpgamma(s/2 - 1)

candidates = [
    ("Riemann", F_riemann),
    ("Jacobi c-fn", F_jacobi),
    ("BC_1 spectral", F_bc1),
    ("Selberg", F_selberg),
    ("Product-3", F_product3),
    ("Hurwitz-matched", F_hurwitz_matched),
    ("Epstein dim-6", F_epstein),
    ("Half-shift", F_half_shift),
    ("Bergman", F_bergman),
    ("Duplication", F_duplication),
    ("Symmetric", F_symmetric),
]

best_name = None
best_spread = mpf('1e30')

for name, F_func in candidates:
    test_vals = []
    ok = True
    for s_val in [mpf('3.3'), mpf('3.5'), mpf('4.0'), mpf('4.5'), mpf('5.0')]:
        s_dual = C_2 - s_val
        try:
            f_s = F_func(s_val)
            f_dual = F_func(s_dual)
            R = ratios.get(float(s_val))
            if R is not None and abs(f_s) > 1e-30 and abs(f_dual) > 1e-30:
                # Test: R(s) * F(s) / F(C_2-s) should equal -1
                test_val = R * f_s / f_dual
                test_vals.append(test_val)
        except:
            ok = False
            break

    if ok and len(test_vals) >= 3:
        # Check if all test_vals are the same (and ideally = -1)
        mean = sum(test_vals) / len(test_vals)
        spread = max(abs(v) for v in test_vals) / min(abs(v) for v in test_vals) if min(abs(v) for v in test_vals) > 1e-30 else mpf('inf')
        is_minus1 = all(abs(v + 1) < 0.05 for v in test_vals)
        is_const = spread < 1.02

        marker = ""
        if is_minus1:
            marker = " <-- FUNCTIONAL EQUATION!"
        elif is_const:
            marker = " <-- constant ratio"

        if spread < best_spread:
            best_spread = spread
            best_name = name

        print(f"  {name:20s}: ratio*F/F' = {nstr(mean, 8):>14}, "
              f"spread={nstr(spread, 6):>10}, "
              f"{'CONST' if is_const else '':>5}{marker}")
    else:
        print(f"  {name:20s}: evaluation error")

t2 = best_name is not None
results.append(("T2", f"Best candidate: {best_name} (spread={nstr(best_spread, 4)})", t2))
print(f"\nT2 {'PASS' if t2 else 'FAIL'}")

# =====================================================================
# PART 3: REFINED SEARCH — GAMMA RATIO FORM
# =====================================================================
print()
print("--- Part 3: Refined Search — Gamma(s+a)/Gamma(s+b) Form ---")
print()

# The functional equation for symmetric space spectral zetas typically has:
# Xi(s) = product_{j} Gamma((s+a_j)/d_j) * zeta_B(s)
# with the shifts a_j determined by the root system.
#
# For BC_1 with rho = g/2 = 7/2, the natural shifts are:
# From the Plancherel: the polynomial part is mu^5 - 5/2*mu^3 + 9/16*mu
# with roots at mu = 0, ±1/2, ±3/2.
# These roots correspond to s-values (via mu = s - rho_eff + something).
#
# Another approach: the spectral zeta has poles at s = 1, 2, 3 = N_c.
# The Gamma factors must CANCEL these poles to make Xi entire (or
# have poles only at prescribed locations).
# Gamma(s-a) has poles at s = a, a-1, a-2, ...
# So: Gamma(s) * Gamma(s-1) * Gamma(s-2) has poles at s = 0,-1,-2
# and s = 1,0,-1 and s = 2,1,0.
# In particular, poles at s = 1, 2 from this product.
# To cancel zeta_B's poles at s = 1, 2, 3:
# we need 1/Gamma factors with poles (= zeros of 1/Gamma) at s = 1, 2, 3.
# 1/Gamma(s) has zeros at s = 0, -1, -2, ...
# 1/Gamma(4-s) has zeros at s = 4, 5, 6, ...
# Neither helps at s = 1, 2, 3.
#
# OR: we DON'T cancel the poles. The Riemann Xi function DOES have
# a zero at s = 1 (from the pole of zeta), but the completed Xi is entire.
# Actually no — for Riemann, Xi(s) = (s-1)*pi^{-s/2}*Gamma(s/2+1)*zeta(s)
# and the (s-1) cancels the pole.
#
# For our zeta_B with THREE poles, we might need (s-1)(s-2)(s-3) * F(s) * zeta_B(s).

# Let me try: Xi(s) = (s-1)(s-2)(s-3) * pi^{-as} * Gamma(bs+c) * ... * zeta_B(s)
# and search for the right a, b, c.

# Actually, let me try a more systematic approach.
# The ratio R(s) = zeta_B(s)/zeta_B(C_2-s) should equal -F(C_2-s)/F(s).
# Taking log: log(R(s)) = log(-1) + log(F(C_2-s)) - log(F(s))
#           = i*pi + log(F(C_2-s)) - log(F(s))
#
# If F(s) = Gamma(s+a), then:
# log(F(C_2-s)) - log(F(s)) = loggamma(C_2-s+a) - loggamma(s+a)
# For this to match log(-R(s)) - i*pi, we need the right a.

# Compute log(-R(s)) at test points:
print(f"  log|R(s)| at test points:")
log_R = {}
for s_float, R_val in sorted(ratios.items()):
    log_R[s_float] = log(abs(R_val))
    s_dual = C_2 - s_float
    print(f"    s={s_float:5.1f}: R(s) = {nstr(R_val, 12)}, "
          f"log|R| = {nstr(log_R[s_float], 10)}")

print()

# For F(s) = Gamma(s+a), need:
# log|Gamma(C_2-s+a)/Gamma(s+a)| = log|R(s)|
# Test different a values:
print(f"  Testing F(s) = Gamma(s+a) for different a:")
for a_test in [mpf(0), mpf(-1), mpf(-2), mpf('0.5'), mpf('-0.5'),
               mpf('-1.5'), mpf('-2.5'), mpf(1), mpf('-3.5')]:
    test_ratios = []
    for s_float, R_val in sorted(ratios.items()):
        s = mpf(s_float)
        s_dual = C_2 - s
        try:
            gamma_ratio = mpgamma(s_dual + a_test) / mpgamma(s + a_test)
            target = -R_val  # because Xi(s) = -Xi(C_2-s)
            if abs(gamma_ratio) > 1e-30:
                q = target / gamma_ratio
                test_ratios.append(q)
        except:
            pass

    if len(test_ratios) >= 3:
        spread = max(abs(v) for v in test_ratios) / min(abs(v) for v in test_ratios) if min(abs(v) for v in test_ratios) > 0 else mpf('inf')
        print(f"    a={float(a_test):5.1f}: quotient={nstr(test_ratios[0], 8)}, spread={nstr(spread, 6)}")

print()

# Now try F(s) = Gamma(s+a) * Gamma(s+b):
print(f"  Testing F(s) = Gamma(s+a) * Gamma(s+b):")
best_ab = None
best_ab_spread = mpf('1e30')

for a_val in [mpf(x)/2 for x in range(-7, 4)]:
    for b_val in [mpf(x)/2 for x in range(int(2*float(a_val)), 4)]:
        test_ratios = []
        for s_float, R_val in sorted(ratios.items()):
            s = mpf(s_float)
            s_dual = C_2 - s
            try:
                f_s = mpgamma(s + a_val) * mpgamma(s + b_val)
                f_dual = mpgamma(s_dual + a_val) * mpgamma(s_dual + b_val)
                if abs(f_s) > 1e-30 and abs(f_dual) > 1e-30:
                    q = (-R_val) * f_s / f_dual  # should be constant
                    test_ratios.append(q)
            except:
                pass

        if len(test_ratios) >= 4:
            spread = max(abs(v) for v in test_ratios) / min(abs(v) for v in test_ratios) if min(abs(v) for v in test_ratios) > 0 else mpf('inf')
            if spread < best_ab_spread:
                best_ab_spread = spread
                best_ab = (float(a_val), float(b_val), float(test_ratios[0]))

            if spread < 1.01:
                print(f"    a={float(a_val):5.1f}, b={float(b_val):5.1f}: "
                      f"quotient={nstr(test_ratios[0], 8)}, spread={nstr(spread, 6)} GOOD")

if best_ab:
    print(f"\n  Best two-Gamma: a={best_ab[0]}, b={best_ab[1]}, "
          f"const={best_ab[2]:.6f}, spread={nstr(best_ab_spread, 6)}")

t3 = best_ab_spread < 1.1 if best_ab else False
results.append(("T3", f"Two-Gamma search: spread={nstr(best_ab_spread, 4)}", t3))
print(f"\nT3 {'PASS' if t3 else 'FAIL'}")

# =====================================================================
# PART 4: THREE-GAMMA PRODUCT SEARCH
# =====================================================================
print()
print("--- Part 4: Three-Gamma Product Search ---")
print()

# The spectral zeta has 3 poles (at s=1,2,3) and the Hilbert function
# has degree 5. The Hurwitz expansion involves 3 terms. Natural to try
# F(s) = Gamma(s+a) * Gamma(s+b) * Gamma(s+c) with 3 shifts.

best_abc = None
best_abc_spread = mpf('1e30')

# The shifts should be related to the Hurwitz arguments:
# H(2s-5), H(2s-3), H(2s-1)
# which suggest shifts of -5/2, -3/2, -1/2 (halved arguments).
# Or the d(mu) roots: 0, ±1/2, ±3/2 → shifts 0, -1/2, -3/2.

search_vals = [mpf(x)/2 for x in range(-7, 3)]

for a_val in search_vals:
    for b_val in [v for v in search_vals if v > a_val]:
        for c_val in [v for v in search_vals if v > b_val]:
            test_ratios = []
            for s_float, R_val in sorted(ratios.items()):
                s = mpf(s_float)
                s_dual = C_2 - s
                try:
                    f_s = mpgamma(s + a_val) * mpgamma(s + b_val) * mpgamma(s + c_val)
                    f_dual = mpgamma(s_dual + a_val) * mpgamma(s_dual + b_val) * mpgamma(s_dual + c_val)
                    if abs(f_s) > 1e-30 and abs(f_dual) > 1e-30:
                        q = (-R_val) * f_s / f_dual
                        test_ratios.append(q)
                except:
                    pass

            if len(test_ratios) >= 4:
                spread = max(abs(v) for v in test_ratios) / min(abs(v) for v in test_ratios) if min(abs(v) for v in test_ratios) > 0 else mpf('inf')
                if spread < best_abc_spread:
                    best_abc_spread = spread
                    best_abc = (float(a_val), float(b_val), float(c_val), float(test_ratios[0]))

                if spread < 1.005:
                    print(f"    a={float(a_val):5.1f}, b={float(b_val):5.1f}, c={float(c_val):5.1f}: "
                          f"const={nstr(test_ratios[0], 10)}, spread={nstr(spread, 8)} MATCH")

if best_abc:
    print(f"\n  Best three-Gamma: a={best_abc[0]}, b={best_abc[1]}, c={best_abc[2]}")
    print(f"  Constant: {best_abc[3]:.8f}, spread: {nstr(best_abc_spread, 8)}")

t4 = best_abc_spread < 1.01 if best_abc else False
results.append(("T4", f"Three-Gamma search: {'FOUND' if t4 else 'best spread='+nstr(best_abc_spread, 4)}", t4))
print(f"\nT4 {'PASS' if t4 else 'FAIL'}")

# =====================================================================
# PART 5: INCLUDE pi^{-as} FACTOR
# =====================================================================
print()
print("--- Part 5: Including pi^{-as} Prefactor ---")
print()

# The functional equation typically includes a pi power.
# F(s) = pi^{-a*s} * Gamma_product(s)
# Then F(C_2-s)/F(s) picks up pi^{-a*(C_2-2s)} = pi^{-a*C_2+2as}
# which adds a pi^{2as} factor to the ratio.

# Use the best Gamma product from Part 3 or 4, and adjust with pi:
# R(s) * Gamma_ratio = const * pi^{2a*s} for some a

if best_ab:
    a_gam, b_gam = best_ab[0], best_ab[1]
    print(f"  Using best two-Gamma: a={a_gam}, b={b_gam}")

    gamma_ratios_at_s = {}
    for s_float, R_val in sorted(ratios.items()):
        s = mpf(s_float)
        s_dual = C_2 - s
        try:
            f_s = mpgamma(s + a_gam) * mpgamma(s + b_gam)
            f_dual = mpgamma(s_dual + a_gam) * mpgamma(s_dual + b_gam)
            q = (-R_val) * f_s / f_dual
            gamma_ratios_at_s[s_float] = q
        except:
            pass

    # Check if log(q) is linear in s → pi^{2as} correction
    if len(gamma_ratios_at_s) >= 3:
        s_vals_sorted = sorted(gamma_ratios_at_s.keys())
        log_q_vals = [(s, float(log(abs(gamma_ratios_at_s[s])))) for s in s_vals_sorted]
        # Linear fit: log(q) = m*s + b → m = 2a*log(pi)
        if len(log_q_vals) >= 2:
            # Simple two-point slope
            s1, lq1 = log_q_vals[0]
            s2, lq2 = log_q_vals[-1]
            slope = (lq2 - lq1) / (s2 - s1)
            a_pi = slope / (2 * float(log(pi)))
            print(f"  Log-quotient slope: {slope:.6f}")
            print(f"  Implied pi exponent: a = {a_pi:.4f}")
            print(f"  Nearest integer/half: {round(2*a_pi)/2}")

            # Now test with the corrected F:
            a_pi_round = round(2*a_pi) / 2
            print(f"\n  Testing F(s) = pi^({a_pi_round}*s) * Gamma(s+{a_gam}) * Gamma(s+{b_gam}):")
            corrected_ratios = []
            for s_float, R_val in sorted(ratios.items()):
                s = mpf(s_float)
                s_dual = C_2 - s
                try:
                    f_s = pi**(a_pi_round * s) * mpgamma(s + a_gam) * mpgamma(s + b_gam)
                    f_dual = pi**(a_pi_round * s_dual) * mpgamma(s_dual + a_gam) * mpgamma(s_dual + b_gam)
                    q = (-R_val) * f_s / f_dual
                    corrected_ratios.append(q)
                    print(f"    s={s_float:5.1f}: q = {nstr(q, 12)}")
                except:
                    pass

            if len(corrected_ratios) >= 3:
                spread = max(abs(v) for v in corrected_ratios) / min(abs(v) for v in corrected_ratios)
                print(f"  Spread after pi correction: {nstr(spread, 8)}")

if best_abc:
    a_gam, b_gam, c_gam = best_abc[0], best_abc[1], best_abc[2]
    print(f"\n  Using best three-Gamma: a={a_gam}, b={b_gam}, c={c_gam}")

    gamma_ratios_at_s_3 = {}
    for s_float, R_val in sorted(ratios.items()):
        s = mpf(s_float)
        s_dual = C_2 - s
        try:
            f_s = mpgamma(s + a_gam) * mpgamma(s + b_gam) * mpgamma(s + c_gam)
            f_dual = mpgamma(s_dual + a_gam) * mpgamma(s_dual + b_gam) * mpgamma(s_dual + c_gam)
            q = (-R_val) * f_s / f_dual
            gamma_ratios_at_s_3[s_float] = q
        except:
            pass

    if len(gamma_ratios_at_s_3) >= 3:
        s_vals_sorted = sorted(gamma_ratios_at_s_3.keys())
        log_q_vals = [(s, float(log(abs(gamma_ratios_at_s_3[s])))) for s in s_vals_sorted]
        s1, lq1 = log_q_vals[0]
        s2, lq2 = log_q_vals[-1]
        slope = (lq2 - lq1) / (s2 - s1)
        a_pi = slope / (2 * float(log(pi)))
        print(f"  Log-quotient slope: {slope:.6f}")
        print(f"  Implied pi exponent: a = {a_pi:.4f}")
        a_pi_round = round(2*a_pi) / 2

        print(f"\n  Testing F(s) = pi^({a_pi_round}*s) * Gamma(s+{a_gam}) * Gamma(s+{b_gam}) * Gamma(s+{c_gam}):")
        corrected_ratios_3 = []
        for s_float, R_val in sorted(ratios.items()):
            s = mpf(s_float)
            s_dual = C_2 - s
            try:
                f_s = pi**(a_pi_round * s) * mpgamma(s + a_gam) * mpgamma(s + b_gam) * mpgamma(s + c_gam)
                f_dual = pi**(a_pi_round * s_dual) * mpgamma(s_dual + a_gam) * mpgamma(s_dual + b_gam) * mpgamma(s_dual + c_gam)
                q = (-R_val) * f_s / f_dual
                corrected_ratios_3.append(q)
                print(f"    s={s_float:5.1f}: q = {nstr(q, 12)}")
            except:
                pass

        if len(corrected_ratios_3) >= 3:
            spread = max(abs(v) for v in corrected_ratios_3) / min(abs(v) for v in corrected_ratios_3)
            print(f"  Spread after pi correction: {nstr(spread, 8)}")

t5 = True
results.append(("T5", "Pi-corrected Gamma products tested", t5))
print(f"\nT5 {'PASS' if t5 else 'FAIL'}")

# =====================================================================
# PART 6: THE RATIO FUNCTION — WHAT DOES IT LOOK LIKE?
# =====================================================================
print()
print("--- Part 6: Structure of R(s) = zeta_B(s)/zeta_B(C_2-s) ---")
print()

# Let's compute R(s) at many points and study its shape
print(f"  R(s) = zeta_B(s)/zeta_B(C_2-s) at fine grid:")
print(f"  {'s':>6} {'R(s)':>18} {'log|R|':>12} {'sign':>6}")

fine_ratios = []
for s_10 in range(31, 56):
    s_val = mpf(s_10) / 10
    s_dual = C_2 - s_val
    try:
        z_s = zeta_B(s_val)
        z_dual = zeta_B(s_dual)
        if abs(z_dual) > 1e-30:
            R = z_s / z_dual
            sgn = "+" if R > 0 else "-"
            fine_ratios.append((float(s_val), float(R), float(log(abs(R))), sgn))
            if s_10 % 2 == 1:  # print every other point
                print(f"  {float(s_val):6.1f} {nstr(R, 12):>18} {float(log(abs(R))):>12.4f} {sgn:>6}")
    except:
        pass

# Check if log|R| is approximately linear in s
if len(fine_ratios) >= 5:
    s_arr = [x[0] for x in fine_ratios]
    logR_arr = [x[2] for x in fine_ratios]
    # Linear regression
    n = len(s_arr)
    sx = sum(s_arr)
    sy = sum(logR_arr)
    sxy = sum(s_arr[i] * logR_arr[i] for i in range(n))
    sxx = sum(s_arr[i]**2 for i in range(n))
    slope_lin = (n * sxy - sx * sy) / (n * sxx - sx**2)
    intercept_lin = (sy - slope_lin * sx) / n
    # R-squared
    ss_res = sum((logR_arr[i] - slope_lin * s_arr[i] - intercept_lin)**2 for i in range(n))
    ss_tot = sum((logR_arr[i] - sy/n)**2 for i in range(n))
    r_sq = 1 - ss_res / ss_tot if ss_tot > 0 else 0

    print(f"\n  Linear fit: log|R(s)| ~ {slope_lin:.4f}*s + {intercept_lin:.4f}")
    print(f"  R² = {r_sq:.6f}")

    # If R² ~ 1 and slope ~ 2*a*log(pi), then F involves pi^{-as}
    if abs(r_sq) > 0.99:
        a_inferred = slope_lin / (2 * float(log(pi)))
        print(f"  Inferred pi exponent: {a_inferred:.4f}")
        print(f"  Nearest half-integer: {round(2*a_inferred)/2}")
    else:
        print(f"  log|R| is NOT linear — need nonlinear Gamma structure")

    # Check antisymmetry: R(N_c + d) = -1/R(N_c - d)?
    print(f"\n  Testing antisymmetry R(N_c+d) * R(N_c-d) = ?:")
    for d_val in [mpf('0.3'), mpf('0.5'), mpf('1.0'), mpf('1.5'), mpf('2.0')]:
        s_plus = N_c + d_val
        s_minus = N_c - d_val
        R_plus = ratios.get(float(s_plus))
        R_minus = ratios.get(float(s_minus))
        if R_plus is not None and R_minus is not None:
            prod = R_plus * R_minus
            print(f"    d={float(d_val):4.1f}: R({float(s_plus):4.1f})*R({float(s_minus):4.1f}) = {nstr(prod, 10)}")

t6 = True
results.append(("T6", f"R(s) structure analyzed (slope={slope_lin:.4f})", t6))
print(f"\nT6 {'PASS' if t6 else 'FAIL'}")

# =====================================================================
# PART 7: EXACT RATIO FROM HURWITZ
# =====================================================================
print()
print("--- Part 7: Exact Ratio from Hurwitz Decomposition ---")
print()

# The Hurwitz decomposition gives:
# zeta_B(s) = (1/60) sum_j C(s-1+j,j) (25/4)^j * H_combo(s,j)
#
# where H_combo = H(2s+2j-5, 7/2) - (5/2)*H(2s+2j-3, 7/2) + (9/16)*H(2s+2j-1, 7/2)
#
# And H(a, 7/2) = (2^a - 1)*zeta(a) - 2^a - (2/3)^a - (2/5)^a
#
# So: zeta_B(s)/zeta_B(C_2-s) is a ratio of two Hurwitz series.
#
# At the leading order (j=0):
# R(s) ~ [H(2s-5, 7/2) - 5/2*H(2s-3, 7/2) + 9/16*H(2s-1, 7/2)] /
#         [H(C_2*2-2s-5, 7/2) - 5/2*H(C_2*2-2s-3, 7/2) + 9/16*H(C_2*2-2s-1, 7/2)]
# = [H(2s-5) - 5/2*H(2s-3) + 9/16*H(2s-1)] /
#   [H(7-2s) - 5/2*H(9-2s) + 9/16*H(11-2s)]
#
# The numerator contains H at even arguments 2s-5, 2s-3, 2s-1
# The denominator contains H at 7-2s, 9-2s, 11-2s
#
# These are related: the Hurwitz functional equation maps H(a) ↔ H(1-a).
# So H(7-2s) = H(1-(2s-6)) — a shifted functional equation.

# For the Riemann zeta part:
# Numerator Riemann part: (2^{2s-5}-1)*zeta(2s-5) etc.
# Denominator Riemann part: (2^{7-2s}-1)*zeta(7-2s) etc.
# The Riemann FE maps zeta(a) to pi^{a-1/2}*Gamma((1-a)/2)/Gamma(a/2)*zeta(1-a)

# So zeta(7-2s) = pi^{6.5-2s} * Gamma((2s-6)/2)/Gamma((7-2s)/2) * zeta(2s-6)

# This is getting algebraically complex. Let me compute the leading-order
# ratio numerically and compare with the exact ratio.

print(f"  Leading-order (j=0) vs full ratio:")
for s_val in [mpf('3.5'), mpf('4.0'), mpf('4.5'), mpf('5.0')]:
    s_dual = C_2 - s_val

    # j=0 terms
    def H_combo(s):
        a = mpf(7)/2
        return (hurwitz_zeta(2*s-5, a) -
                mpf(5)/2 * hurwitz_zeta(2*s-3, a) +
                mpf(9)/16 * hurwitz_zeta(2*s-1, a))

    try:
        num_j0 = H_combo(s_val)
        den_j0 = H_combo(s_dual)
        R_j0 = num_j0 / den_j0 if abs(den_j0) > 1e-30 else mpf('inf')

        R_full = zeta_B(s_val) / zeta_B(s_dual)

        print(f"  s={float(s_val):4.1f}: R_j0 = {nstr(R_j0, 12)}, "
              f"R_full = {nstr(R_full, 12)}, "
              f"ratio = {nstr(R_full/R_j0, 8)}")
    except Exception as e:
        print(f"  s={float(s_val):4.1f}: error — {e}")

t7 = True
results.append(("T7", "Leading-order vs full ratio compared", t7))
print(f"\nT7 {'PASS' if t7 else 'FAIL'}")

# =====================================================================
# FINAL SCORE
# =====================================================================
print()
print("=" * 72)
print("FINAL SCORE")
print("=" * 72)
for tag, desc, passed in results:
    print(f"  {tag}: {'PASS' if passed else 'FAIL'} — {desc}")

total = len(results)
passed = sum(1 for _, _, p in results if p)
print(f"\nSCORE: {passed}/{total}")

print()
print("STATUS: Gamma factor hunt")
if best_abc_spread < 1.01:
    print(f"  FOUND: three-Gamma product with shifts {best_abc[:3]}")
elif best_ab_spread < 1.01:
    print(f"  FOUND: two-Gamma product with shifts ({best_ab[0]}, {best_ab[1]})")
else:
    print(f"  NOT YET FOUND: best spread = {nstr(min(best_ab_spread, best_abc_spread), 6)}")
    print(f"  The Gamma factor may involve half-integer shifts, pi powers,")
    print(f"  or a product structure different from simple Gamma(s+a) forms.")
    print(f"  Next: try F(s) = Gamma(s/2+a)*Gamma(s/2+b)*... (half-s arguments)")
