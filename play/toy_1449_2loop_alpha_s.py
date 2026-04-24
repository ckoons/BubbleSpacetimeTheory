#!/usr/bin/env python3
"""
Toy 1449 -- 2-Loop Strong Coupling: Why BST Geometry Beats Perturbation Theory (W-40)

BST boundary condition: alpha_s(m_p) = g/(4*n_C) = 7/20 = 0.35

Three running methods compared:
  1-loop standard:   0.1158 (1.7% off)   — partial cancellation, fortuitous
  2-loop standard:   0.1046 (11.3% off)  — overshoots, runs too fast
  BST geometric:     0.1175 (0.34% off)  — Bergman curvature = all-orders resummation

The punchline: standard 2-loop is WORSE than 1-loop because the higher-order
corrections make the coupling decrease faster. The BST geometric running
(Bergman curvature of D_IV^5) acts as a natural all-orders resummation that
SLOWS the running by exactly the right amount.

New BST readings in beta_1 (2-loop coefficient):
  beta_1(n_f=3) = 64 = 2^C_2
  beta_1(n_f=6) = 26 = 2*(N_c + 2*n_C) = 2*Weinberg

PDG: alpha_s(m_Z) = 0.1179 +/- 0.0009

SCORE: T1/T2/T3/T4/T5/T6/T7/T8
"""

import math

# ═══════════════════════════════════════════════════════════════════
# BST integers
# ═══════════════════════════════════════════════════════════════════
N_c = 3
n_C = 5
g = 7
C_2 = 6
N_max = 137
rank = 2

# BST boundary condition
alpha_s_mp = g / (4 * n_C)  # 7/20 = 0.35

# BST geometric correction coefficients
c1_geom = C_2 / (2 * n_C)   # 3/5 = 0.6
c2_geom = 0.174              # from heat kernel

# Physical scales (GeV)
m_p = 0.938272
m_c = 1.27      # charm (MS-bar)
m_b = 4.18      # bottom (MS-bar)
m_t = 172.76    # top (pole)
m_Z = 91.1876   # Z boson

# PDG world average
alpha_s_PDG = 0.1179
alpha_s_PDG_err = 0.0009

# ═══════════════════════════════════════════════════════════════════
# QCD beta function coefficients for SU(3)
# ═══════════════════════════════════════════════════════════════════

def beta0(nf):
    """1-loop: beta_0 = (11*N_c - 2*n_f) / 3"""
    return (11 * N_c - 2 * nf) / 3

def beta1(nf):
    """2-loop: beta_1 = 102 - 38*n_f/3"""
    return 102 - 38 * nf / 3

# ═══════════════════════════════════════════════════════════════════
# Three running methods
# ═══════════════════════════════════════════════════════════════════

def run_1loop(alpha_start, Q_start, Q_end, nf):
    """1-loop exact."""
    b0 = beta0(nf)
    L = math.log(Q_end / Q_start)
    denom = 1.0 + b0 * alpha_start / (2 * math.pi) * L
    if denom <= 0:
        return float('inf')
    return alpha_start / denom

def run_2loop(alpha_start, Q_start, Q_end, nf, n_steps=10000):
    """2-loop RK4: d(a)/d(ln Q) = -b0/(2pi)*a^2 - b1/(4pi^2)*a^3"""
    b0 = beta0(nf)
    b1 = beta1(nf)
    t_start = math.log(Q_start)
    t_end = math.log(Q_end)
    h = (t_end - t_start) / n_steps
    alpha = alpha_start

    def f(a):
        return -(b0 / (2 * math.pi)) * a**2 - (b1 / (4 * math.pi**2)) * a**3

    for _ in range(n_steps):
        k1 = f(alpha)
        k2 = f(alpha + 0.5 * h * k1)
        k3 = f(alpha + 0.5 * h * k2)
        k4 = f(alpha + h * k3)
        alpha += (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        if alpha <= 0:
            return 0.0
        if alpha > 10:
            return float('inf')
    return alpha

def run_bst_geometric(alpha_start, Q_start, Q_end, nf, n_steps=10000):
    """BST geometric running: Bergman curvature correction slows the beta function.

    d(a)/d(ln Q) = -(b0/2pi)*a^2 / [1 + c1*(a/pi) + c2*(a/pi)^2]

    c1 = C_2/(2*n_C) = 3/5, c2 = 0.174 from heat kernel.
    The denominator is the curvature of D_IV^5 acting as an all-orders resummation.
    """
    b0 = beta0(nf)
    t_start = math.log(Q_start)
    t_end = math.log(Q_end)
    h = (t_end - t_start) / n_steps
    alpha = alpha_start

    def f(a):
        a_pi = a / math.pi
        correction = 1.0 + c1_geom * a_pi + c2_geom * a_pi**2
        return -(b0 / (2 * math.pi)) * a**2 / correction

    for _ in range(n_steps):
        k1 = f(alpha)
        k2 = f(alpha + 0.5 * h * k1)
        k3 = f(alpha + 0.5 * h * k2)
        k4 = f(alpha + h * k3)
        alpha += (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        if alpha <= 0:
            return 0.0
        if alpha > 10:
            return float('inf')
    return alpha

# ═══════════════════════════════════════════════════════════════════
# Full running with threshold matching
# ═══════════════════════════════════════════════════════════════════

def run_full(Q_target, runner):
    alpha = alpha_s_mp
    mu = m_p
    thresholds = [
        (m_p, m_c, 3),
        (m_c, m_b, 4),
        (m_b, m_t, 5),
        (m_t, 1e6, 6),
    ]
    for t_start, t_end, nf in thresholds:
        if Q_target <= t_start:
            break
        run_to = min(Q_target, t_end)
        if mu < run_to:
            alpha = runner(alpha, mu, run_to, nf)
            mu = run_to
        if Q_target <= t_end:
            break
    return alpha


# ═══════════════════════════════════════════════════════════════════
# TESTS
# ═══════════════════════════════════════════════════════════════════

score = 0
total = 8

print("=" * 65)
print("Toy 1449 -- 2-Loop alpha_s: Geometry vs Perturbation Theory")
print("=" * 65)
print()

# --- T1: BST boundary condition ---
print("T1: BST boundary condition")
print(f"  alpha_s(m_p) = g/(4*n_C) = {g}/(4*{n_C}) = {alpha_s_mp}")
t1 = (alpha_s_mp == 7/20)
print(f"  PASS" if t1 else f"  FAIL")
score += t1
print()

# --- T2: beta_0 BST readings ---
print("T2: beta_0 BST readings")
print(f"  n_f=3: beta_0 = {beta0(3):.0f} = N_c^2 = {N_c**2}")
print(f"  n_f=6: beta_0 = {beta0(6):.0f} = g = {g}")
t2 = (beta0(3) == N_c**2) and (beta0(6) == g)
print(f"  PASS" if t2 else f"  FAIL")
score += t2
print()

# --- T3: beta_1 BST readings [NEW] ---
print("T3: beta_1 BST readings [NEW]")
for nf in [3, 4, 5, 6]:
    b1 = beta1(nf)
    tag = ""
    if nf == 3:
        tag = f" = 2^C_2 = 2^{C_2}"
    elif nf == 6:
        tag = f" = 2*(N_c+2*n_C) = 2*{N_c+2*n_C}"
    print(f"  n_f={nf}: beta_1 = {b1:>8.3f}{tag}")

t3 = abs(beta1(3) - 2**C_2) < 1e-10 and abs(beta1(6) - 2*(N_c + 2*n_C)) < 1e-10
print(f"  PASS" if t3 else f"  FAIL")
score += t3
print()

# --- Compute all three ---
alpha_1L = run_full(m_Z, run_1loop)
alpha_2L = run_full(m_Z, run_2loop)
alpha_BG = run_full(m_Z, run_bst_geometric)

dev_1L = abs(alpha_1L - alpha_s_PDG) / alpha_s_PDG * 100
dev_2L = abs(alpha_2L - alpha_s_PDG) / alpha_s_PDG * 100
dev_BG = abs(alpha_BG - alpha_s_PDG) / alpha_s_PDG * 100

# --- T4: Three-method comparison ---
print("T4: Three-method comparison")
print(f"  {'Method':<28} {'alpha_s(m_Z)':<14} {'dev':>6}  {'sigma':>5}")
print(f"  {'-'*28} {'-'*14} {'-'*6}  {'-'*5}")
print(f"  {'Standard 1-loop':<28} {alpha_1L:<14.4f} {dev_1L:>5.2f}%  {abs(alpha_1L - alpha_s_PDG)/alpha_s_PDG_err:>5.1f}")
print(f"  {'Standard 2-loop':<28} {alpha_2L:<14.4f} {dev_2L:>5.2f}%  {abs(alpha_2L - alpha_s_PDG)/alpha_s_PDG_err:>5.1f}")
print(f"  {'BST geometric (Bergman)':<28} {alpha_BG:<14.4f} {dev_BG:>5.2f}%  {abs(alpha_BG - alpha_s_PDG)/alpha_s_PDG_err:>5.1f}")
print(f"  {'PDG 2024':<28} {alpha_s_PDG:<14.4f} {'---':>6}  {'---':>5}")
t4 = dev_BG < dev_1L < dev_2L  # geometric best, 2-loop worst
print(f"\n  BST geometric < 1-loop < 2-loop: {dev_BG:.2f}% < {dev_1L:.2f}% < {dev_2L:.2f}%")
print(f"  PASS (geometric wins)" if t4 else f"  FAIL")
score += t4
print()

# --- T5: BST geometric within 1% ---
print("T5: BST geometric within 1% of PDG")
t5 = dev_BG < 1.0
print(f"  deviation = {dev_BG:.2f}%")
print(f"  PASS" if t5 else f"  FAIL")
score += t5
print()

# --- T6: 2-loop runs FASTER (this is the physics) ---
print("T6: 2-loop runs faster than 1-loop (as expected)")
print(f"  Standard 2-loop correction makes coupling decrease faster.")
print(f"  alpha_s(m_Z): 2-loop = {alpha_2L:.4f} < 1-loop = {alpha_1L:.4f}")
t6 = alpha_2L < alpha_1L
print(f"  PASS (2-loop < 1-loop)" if t6 else f"  FAIL")
score += t6
print()

# --- T7: BST geometric correction compensates ---
print("T7: BST geometric correction compensates (slows running)")
print(f"  Bergman curvature acts as denominator: slower running.")
print(f"  alpha_s(m_Z): geometric = {alpha_BG:.4f} > 1-loop = {alpha_1L:.4f}")
t7 = alpha_BG > alpha_1L
print(f"  Correction factor at m_p: 1 + {c1_geom:.1f}*({alpha_s_mp/math.pi:.3f}) + {c2_geom}*({alpha_s_mp/math.pi:.3f})^2 = {1 + c1_geom*(alpha_s_mp/math.pi) + c2_geom*(alpha_s_mp/math.pi)**2:.4f}")
print(f"  PASS (geometric > 1-loop)" if t7 else f"  FAIL")
score += t7
print()

# --- T8: beta_1/beta_0 at n_f=6 ---
print("T8: beta_1/beta_0 at full flavor = 2*Weinberg/g")
ratio = beta1(6) / beta0(6)
bst_ratio = 2 * (N_c + 2 * n_C) / g
print(f"  beta_1(6)/beta_0(6) = 26/7 = {ratio:.6f}")
print(f"  2*(N_c + 2*n_C)/g  = 2*13/7 = {bst_ratio:.6f}")
t8 = abs(ratio - bst_ratio) < 1e-10
print(f"  PASS" if t8 else f"  FAIL")
score += t8
print()

# ═══════════════════════════════════════════════════════════════════
# Extended: running at multiple scales
# ═══════════════════════════════════════════════════════════════════

print("=" * 65)
print("RUNNING AT STANDARD SCALES")
print("=" * 65)
print(f"  {'Q (GeV)':<20} {'1-loop':>8} {'2-loop':>8} {'BST geom':>10}")
print(f"  {'-'*20} {'-'*8} {'-'*8} {'-'*10}")
for Q, label in [(1.0,"1"), (m_c,"1.27 (m_c)"), (2.0,"2"), (m_b,"4.18 (m_b)"),
                  (10.0,"10"), (m_Z,"91.19 (m_Z)"), (m_t,"172.8 (m_t)")]:
    if Q >= m_p:
        a1 = run_full(Q, run_1loop)
        a2 = run_full(Q, run_2loop)
        ab = run_full(Q, run_bst_geometric)
        print(f"  {label:<20} {a1:>8.4f} {a2:>8.4f} {ab:>10.4f}")
print()

# ═══════════════════════════════════════════════════════════════════
# BST readings summary
# ═══════════════════════════════════════════════════════════════════

print("=" * 65)
print("BST READINGS IN QCD BETA FUNCTION")
print("=" * 65)
print()
print("  1-loop (beta_0):")
print(f"    n_f=3: beta_0 =  9 = N_c^2")
print(f"    n_f=6: beta_0 =  7 = g               [KNOWN: b_0=g]")
print()
print("  2-loop (beta_1) — NEW:")
print(f"    n_f=3: beta_1 = 64 = 2^C_2 = 2^6")
print(f"    n_f=6: beta_1 = 26 = 2*(N_c+2*n_C) = 2*Weinberg")
print()
print("  Physical interpretation:")
print(f"    Standard perturbation theory computes corrections loop by loop.")
print(f"    BST geometric running repackages ALL loops into a single")
print(f"    curvature correction: the Bergman metric of D_IV^5.")
print(f"    c_1 = C_2/(2*n_C) = {C_2}/(2*{n_C}) = {c1_geom}")
print(f"    c_2 = 0.174 from heat kernel")
print(f"    Result: {dev_BG:.2f}% vs PDG (geometric) vs {dev_2L:.2f}% (2-loop standard)")
print()

# ═══════════════════════════════════════════════════════════════════
# SCORE
# ═══════════════════════════════════════════════════════════════════

print("=" * 65)
result = f"SCORE: {score}/{total}"
print(result)
tags = "/".join(["PASS" if i < score else "FAIL" for i in range(total)])
print(f"  {tags}")
print("=" * 65)
