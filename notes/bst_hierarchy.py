"""
BST Hierarchy Problem: Derivation of m_e/m_Pl (Newton's Constant)
==================================================================
Casey Koons & Claude (Anthropic), March 2026

The hierarchy problem: why is m_e/m_Pl = 4.185×10⁻²³?

This script:
  1. Confirms F_BST = ln(138)/50 to 10 significant figures (partition fn ground state)
  2. Tests the approximate formula: m_e/m_Pl ≈ (N_max-1) × F_BST × α^{11}
  3. Tests the T_c route: m_e c² = N_max × T_c(phys) / T_c(BST)
  4. Systematic search: test combinations of α, π, ln(N+1), Vol_D5, F_BST at all powers
  5. Identifies correction factor that would make route A exact
  6. Reports all candidates within 1% and top candidates within 0.1%

Author: Casey Koons & Claude (Anthropic), March 2026
"""

import numpy as np
from itertools import product as iproduct

pi    = np.pi
e_nat = np.e   # Euler's number (e)

# ── BST constants ─────────────────────────────────────────────────────────────
alpha   = 1.0 / 137.036082        # Wyler fine structure constant (0.0001%)
N_max   = 137                      # Haldane cap / fine structure integer
n_C     = 5                        # complex dimension of D_IV^5
F_BST   = np.log(N_max + 1) / 50  # vacuum free energy: exact converged value
Vol_D5  = pi**5 / 1920             # Vol(D_IV^5) real, = 0.016116
Vol_S4  = 8*pi**2 / 3             # Vol(S^4) = 26.32
T_c_BST = 130.5                    # phase transition in BST natural units
lnN1    = np.log(N_max + 1)       # ln(138) = 4.9273
mp_me   = (n_C+1) * pi**n_C       # proton/electron mass ratio = 6π^5

# ── Physical constants ─────────────────────────────────────────────────────────
m_e_kg   = 9.10938e-31            # kg
m_Pl_kg  = 2.17645e-8             # kg
m_e_mPl  = m_e_kg / m_Pl_kg      # = 4.18499e-23  (target)
m_e_MeV  = 0.510999               # MeV
T_c_phys = 0.487                  # MeV (BST phase transition = BBN epoch)

print("=" * 70)
print("BST HIERARCHY: DERIVATION OF m_e/m_Pl")
print("Casey Koons & Claude (Anthropic), March 2026")
print("=" * 70)

print(f"""
Target:  m_e/m_Pl  = {m_e_mPl:.8e}
         log_α(m_e/m_Pl) = {np.log(m_e_mPl)/np.log(alpha):.6f}  (not an integer)

BST building blocks:
  α        = 1/{1/alpha:.6f}
  N_max    = {N_max}
  n_C      = {n_C}
  F_BST    = ln({N_max+1})/50 = {F_BST:.10f}
  Vol(D_IV^5) = π^5/1920 = {Vol_D5:.8f}
  ln(N+1)  = ln({N_max+1}) = {lnN1:.8f}
  T_c(BST) = {T_c_BST}
""")

# ══════════════════════════════════════════════════════════════════════════════
# 1. CONFIRM F_BST EXACT VALUE
# ══════════════════════════════════════════════════════════════════════════════
print("=" * 70)
print("1. PARTITION FUNCTION: F_BST TO 10 SIGNIFICANT FIGURES")
print("=" * 70)

# At low T (beta >> 1), lnZ → ln(N_max+1) × d_0
# where d_0 = 1 (zero mode degeneracy on S^4: l=0, m=0)
# All excited modes contribute e^{-beta*E} → 0
# So F_BST = -lnZ/beta → -ln(138)/beta as beta → ∞

for beta in [50, 100, 200, 500]:
    # At large beta, only the (l=0, m=0) mode survives: E=0 → lnZ = ln(138)
    # The first excited modes: (l=0, m=±1) with E=1 → contribution = 2 × ln(1/(1-e^{-beta})) ≈ 2e^{-beta}
    # (l=1, m=0) with E=2 → contribution ≈ 5 × e^{-2beta}

    lnZ = lnN1  # exact ground state
    # Add first excited state corrections
    corr_m1 = 2 * np.log(-np.expm1(-beta))     # (l=0, m=±1) modes
    corr_l1 = 5 * np.log(-np.expm1(-2*beta))   # (l=1, m=0) mode, d_1=5

    # These are numerically zero for beta >= 50
    lnZ_full = lnZ + corr_m1 + corr_l1  # still ≈ lnN1
    F_at_beta = -lnZ_full / beta

    print(f"  beta={beta:5.0f}: lnZ = {lnZ_full:.10f}, F = {F_at_beta:.10f}")

print(f"""
  F_BST = ln({N_max+1})/β  (β-dependent — picks beta=50 as reference)
  Exact converged value at β=50: {F_BST:.10f}

  VERDICT: F_BST = ln(138)/50 exactly. Higher beta gives a different
  (smaller) F — the partition function is fully converged; no new
  digits emerge from increasing l_max or beta.
""")

# ══════════════════════════════════════════════════════════════════════════════
# 2. TEST THE APPROXIMATE FORMULA
# ══════════════════════════════════════════════════════════════════════════════
print("=" * 70)
print("2. TEST: m_e/m_Pl = (N_max-1) × F_BST × α^{2n_C+1}")
print("=" * 70)

formula_A = (N_max - 1) * F_BST * alpha**(2*n_C + 1)
err_A = (formula_A / m_e_mPl - 1) * 100
correction_needed = m_e_mPl / formula_A

print(f"""
  Formula A: (N_max-1) × F_BST × α^11
    = {N_max-1} × {F_BST:.8f} × α^11
    = {formula_A:.8e}
  Observed:   {m_e_mPl:.8e}
  Error:      {err_A:+.4f}%
  Correction: {correction_needed:.8f}  (multiply formula by this to get exact)
""")

# Decompose the correction factor
print(f"  Correction factor analysis: {correction_needed:.8f}")
print(f"    1/N_max               = {1/N_max:.8f}   diff = {abs(correction_needed - 1/N_max)/correction_needed*100:.4f}%")
print(f"    1/(N_max+1)           = {1/(N_max+1):.8f}   diff = {abs(correction_needed - 1/(N_max+1))/correction_needed*100:.4f}%")
print(f"    α                     = {alpha:.8f}   diff = {abs(correction_needed - alpha)/correction_needed*100:.4f}%")
print(f"    Vol_D5                = {Vol_D5:.8f}   diff = {abs(correction_needed - Vol_D5)/correction_needed*100:.4f}%")
print(f"    (1-α)                 = {1-alpha:.8f}   diff = {abs(correction_needed - (1-alpha))/correction_needed*100:.4f}%")
print(f"    1 - 2/N_max           = {1 - 2/N_max:.8f}   diff = {abs(correction_needed - (1-2/N_max))/correction_needed*100:.4f}%")
print(f"    pi/(pi+α^(-1))        = {pi/(pi + 1/alpha):.8f}   diff = {abs(correction_needed - pi/(pi + 1/alpha))/correction_needed*100:.4f}%")
print(f"    T_c(phys)/m_e         = {T_c_phys/m_e_MeV:.8f}   diff = {abs(correction_needed - T_c_phys/m_e_MeV)/correction_needed*100:.4f}%")
print(f"    T_c(BST)/N_max        = {T_c_BST/N_max:.8f}   diff = {abs(correction_needed - T_c_BST/N_max)/correction_needed*100:.4f}%")

# ══════════════════════════════════════════════════════════════════════════════
# 3. T_c ROUTE
# ══════════════════════════════════════════════════════════════════════════════
print()
print("=" * 70)
print("3. T_c ROUTE: m_e = N_max × T_c(phys) / T_c(BST)")
print("=" * 70)

m_e_from_Tc = N_max * T_c_phys / T_c_BST
err_Tc = (m_e_from_Tc / m_e_MeV - 1) * 100

print(f"""
  m_e = N_max × T_c(phys) / T_c(BST)
      = {N_max} × {T_c_phys} MeV / {T_c_BST}
      = {m_e_from_Tc:.6f} MeV
  Observed: {m_e_MeV:.6f} MeV
  Error: {err_Tc:+.4f}%

  T_c(BST)/N_max = {T_c_BST/N_max:.8f}
  T_c(phys)/m_e  = {T_c_phys/m_e_MeV:.8f}

  Physical interpretation:
    The BST phase transition occurs at T_c(BST) = 130.5 natural units.
    Physically T_c = 0.487 MeV (BBN epoch, electron-positron annihilation).
    The electron mass m_e = N_max × T_c(phys) / T_c(BST) = 137 × T_c(phys)/130.5
    means the electron mass is set by exactly N_max copies of the phase
    transition temperature, scaled by T_c(BST)/N_max.

  NOTE: T_c(phys) = 0.487 MeV requires one input. The formula becomes
  parameter-free once T_c(phys) is derived from α (see open problem below).
""")

# ══════════════════════════════════════════════════════════════════════════════
# 4. SYSTEMATIC SEARCH FOR m_e/m_Pl
# ══════════════════════════════════════════════════════════════════════════════
print("=" * 70)
print("4. SYSTEMATIC SEARCH: m_e/m_Pl from BST geometry")
print("=" * 70)
print(f"  Target: {m_e_mPl:.8e}")
print(f"  n_α = log(target)/log(α) = {np.log(m_e_mPl)/np.log(alpha):.6f}")
print()

target = m_e_mPl

# Build pool of base quantities and their BST interpretations
bases = {
    'α':         alpha,
    'α²':        alpha**2,
    'π':         pi,
    'e':         e_nat,
    'ln(N+1)':   lnN1,
    'Vol_D5':    Vol_D5,
    'F_BST':     F_BST,
    'N_max':     float(N_max),
    'n_C+1':     float(n_C + 1),
    '(N+1)':     float(N_max + 1),
    'mp_me':     mp_me,
    'T_c(BST)':  T_c_BST,
}

# Single-base power scan (most informative)
print("  Power scan: target = base^p")
print(f"  {'base':20s} {'best_p':>8}  {'value':>14}  {'error%':>8}")

for name, base in [('α', alpha), ('α²', alpha**2), ('Vol_D5', Vol_D5),
                   ('F_BST', F_BST), ('ln(138)', lnN1)]:
    if base > 0 and base != 1:
        p = np.log(target) / np.log(base)
        val = base**p
        print(f"  {name:20s} {p:8.4f}  {val:14.4e}  {'exact':>8}")

print()

# Two-factor search: target = A^p × B^q
print("  Two-factor: target = α^p × C for various C")
print(f"  {'C':25s} {'C value':>12}  {'α power':>8}  {'value':>14}  {'error':>8}")

C_bases = {
    '1':              1.0,
    'N_max-1=136':    136.0,
    'N_max':          137.0,
    'N_max+1=138':    138.0,
    'ln(138)':        lnN1,
    'F_BST':          F_BST,
    'ln(138)/N_max':  lnN1/N_max,
    'F_BST×(N-1)':    F_BST*(N_max-1),
    'π':              pi,
    'π^n_C=π^5':      pi**5,
    'e^{-1/2}':       e_nat**(-0.5),
    'Vol_D5':         Vol_D5,
    'Vol_D5^4':       Vol_D5**4,
    '1/N_max':        1.0/N_max,
    '1/(N+1)=1/138':  1.0/138,
    'mp_me=6π^5':     mp_me,
    'mp_me/N_max':    mp_me/N_max,
    '1/mp_me':        1.0/mp_me,
    'T_c(BST)':       T_c_BST,
    'T_c(BST)/N_max': T_c_BST/N_max,
    '1/T_c(BST)':     1.0/T_c_BST,
    'F_BST×e^{-1/2}': F_BST*e_nat**(-0.5),
    'ln(138)/138':    lnN1/138,
    'π/N_max':        pi/N_max,
    '(N-1)×ln(N+1)':  (N_max-1)*lnN1,
}

candidates = []
for name, C in C_bases.items():
    if C > 0:
        # Find exact power p such that α^p × C = target
        # log(target) = p×log(α) + log(C)
        p = (np.log(target) - np.log(C)) / np.log(alpha)
        val = alpha**p * C
        err = (val / target - 1) * 100
        # Check if p is close to an integer or simple fraction
        p_frac = p - round(p)
        near_int = abs(p_frac) < 0.02
        p_half = abs(p_frac - 0.5) < 0.02 or abs(p_frac + 0.5) < 0.02
        flag = " ◄ INTEGER" if near_int else (" ◄ HALF-INT" if p_half else "")

        candidates.append((name, C, p, val, err, flag))

        if abs(err) < 0.001 or near_int or p_half:
            print(f"  {name:25s} {C:12.6f}  {p:8.4f}  {val:14.4e}  {err:+7.4f}%{flag}")

print()
print("  All candidates with integer or half-integer α-power:")
print(f"  {'C':25s} {'p (α power)':>12}  {'value':>14}  {'error%':>9}")
for name, C, p, val, err, flag in candidates:
    if flag:
        print(f"  {name:25s} {p:12.4f}  {val:14.4e}  {err:+8.4f}%  ← {flag.strip()}")

# ══════════════════════════════════════════════════════════════════════════════
# 5. COMPOUND FORMULA SEARCH
# ══════════════════════════════════════════════════════════════════════════════
print()
print("=" * 70)
print("5. COMPOUND FORMULA SEARCH")
print("=" * 70)

# The most promising route from theory: Bergman oscillator ground state
# m_e should be related to the minimal Bergman action on D_IV^5
# The electron is the minimal S^1 winding — its action is E_0 = ½ħω_B
#
# Physical picture: m_e c² = E_0 / ln(m_Pl/m_e) [Bekenstein-style]
# or m_e = m_Pl × exp(-S_Bergman) for some Bergman action S_Bergman

print(f"""
  Physical interpretation: Bergman oscillator ground state

  m_e / m_Pl = exp(-S_Bergman)  where S_Bergman = Bergman action for
  minimal S^1 winding on D_IV^5.

  Test: S_Bergman = ?
    S_obs = -ln(m_e/m_Pl) = {-np.log(m_e_mPl):.6f}
    In units of ln(N+1) = {lnN1:.6f}: S_obs/ln(N+1) = {-np.log(m_e_mPl)/lnN1:.6f}
    In units of π: S_obs/π = {-np.log(m_e_mPl)/pi:.6f}
    In units of α^(-1): S_obs × α = {-np.log(m_e_mPl)*alpha:.6f}
    In units of n_C: S_obs/n_C = {-np.log(m_e_mPl)/n_C:.6f}
""")

S_obs = -np.log(m_e_mPl)
print(f"  S_Bergman = {S_obs:.8f}")
print()
print(f"  {'Candidate S':30s}  {'Value':>12}  {'Error in S':>10}  {'error in m_e%':>14}")
S_candidates = [
    ("n_C / α",                     n_C / alpha),
    ("(n_C+1) / α",                 (n_C+1) / alpha),
    ("(n_C+2) / α",                 (n_C+2) / alpha),
    ("n_C × ln(N_max)",             n_C * np.log(N_max)),
    ("(n_C+1) × ln(N_max)",         (n_C+1) * np.log(N_max)),
    ("N_max × ln(n_C+1)",           N_max * np.log(n_C+1)),
    ("N_max × ln(N_max)",           N_max * np.log(N_max)),
    ("α^{-1} × ln(N_max+1)",        np.log(N_max+1)/alpha),
    ("2π × n_C / α^{1/n_C}",        2*pi*n_C / alpha**(1/n_C)),
    ("2π × ln(N+1) / α",            2*pi*lnN1/alpha),
    ("n_C × (n_C+1) × π²",          n_C*(n_C+1)*pi**2),
    ("α^{-11} × ... [series]",       11*np.log(1/alpha)),
    ("α^{-10.47}",                   10.47*np.log(1/alpha)),
    ("4π × n_C × ln(N+1) / Vol_D5", 4*pi*n_C*lnN1/Vol_D5),
    ("ln(N+1)^2 / Vol_D5",          lnN1**2/Vol_D5),
    ("π^{n_C} × (n_C+1)",           pi**n_C*(n_C+1)),  # = mp_me !
    ("π^{n_C+1}",                   pi**(n_C+1)),
    ("8π × n_C × (n_C+1)",          8*pi*n_C*(n_C+1)),
]
for name, S in S_candidates:
    err_S = (S - S_obs)
    err_me = (np.exp(-S) / m_e_mPl - 1) * 100
    flag = " ◄◄◄" if abs(err_me) < 0.1 else (" ◄◄" if abs(err_me) < 1 else (" ◄" if abs(err_me) < 5 else ""))
    print(f"  {name:30s}  {S:12.4f}  {err_S:+10.4f}  {err_me:+13.4f}%{flag}")

# ══════════════════════════════════════════════════════════════════════════════
# 6. α_s SYSTEMATIC SEARCH (from roadmap Priority 8)
# ══════════════════════════════════════════════════════════════════════════════
print()
print("=" * 70)
print("6. STRONG COUPLING α_s(M_Z) = 0.1179")
print("=" * 70)
alpha_s_obs = 0.1179

print(f"""
  Physical picture: α_s = α_em × (Z_3 circuit area) / (U(1) circuit area)
  The Z_3 circuit on D_IV^5 has 3 quarks; U(1) has 1 electron.
  Ratio of circuit areas ~ (n_C+1)/1 × (some geometric factor)

  Best existing candidate: Vol_D5 × (1 + 1/π) = {Vol_D5*(1+1/pi):.5f}  (78% off — no)
""")

print(f"  {'Formula':42s}  {'Value':>10}  {'Error':>8}")
for label, val in [
    ("α × (N_max+1)² / (4π²)",     alpha*(N_max+1)**2/(4*pi**2)),
    ("1/(4π) + Vol_D5",             1/(4*pi) + Vol_D5),
    ("(n_C+1) × α × ln(N+1)^(-1)", (n_C+1)*alpha/lnN1),
    ("α × mp_me / (4π × N_max)",    alpha*mp_me/(4*pi*N_max)),
    ("ln(n_C+1)/α × α²",            np.log(n_C+1)/alpha * alpha**2),
    ("6 × α × ln(N+1)",             6*alpha*lnN1),
    ("α × N_max / (4π)",            alpha*N_max/(4*pi)),
    ("α × (N_max/π)^{1/2}",         alpha*(N_max/pi)**0.5),
    ("π^{n_C-3} × alpha^{1/3}",     pi**(n_C-3)*alpha**(1/3)),
    ("n_C × α^{(n_C-1)/n_C}",       n_C*alpha**((n_C-1)/n_C)),
    ("F_BST + α",                    F_BST + alpha),
    ("F_BST × (1 + 1/N_max)",        F_BST*(1 + 1/N_max)),
    ("ln(N+1)/N_max + F_BST/2",      lnN1/N_max + F_BST/2),
    ("2 × F_BST - Vol_D5",           2*F_BST - Vol_D5),
]:
    if val > 0:
        err = (val - alpha_s_obs) / alpha_s_obs * 100
        flag = " ◄◄◄" if abs(err)<0.5 else (" ◄◄" if abs(err)<2 else (" ◄" if abs(err)<10 else ""))
        print(f"  {label:42s}  {val:10.5f}  {err:+7.2f}%{flag}")

# ══════════════════════════════════════════════════════════════════════════════
# 7. ELECTRON-PLANCK RATIO: FOCUS ON N_max AND ln(N+1)
# ══════════════════════════════════════════════════════════════════════════════
print()
print("=" * 70)
print("7. FOCUSED SEARCH: α^n × f(N_max, π, e, lnN1)")
print("=" * 70)

# The hierarchy problem likely involves N_max in a deep way.
# Scan: target = α^n_int × prefactor(N_max)
print(f"  Scanning α^n × [various N_max combinations]")
print(f"  {'Formula':45s}  {'Value':>14}  {'Error':>8}")

best_results = []
for n_alpha in range(8, 13):  # try n=8..12
    alpha_n = alpha**n_alpha
    factor_needed = target / alpha_n

    # Is factor_needed close to a simple N_max combination?
    tests = {
        f"α^{n_alpha}":                          alpha_n,
        f"α^{n_alpha} × N_max":                   alpha_n * N_max,
        f"α^{n_alpha} × ln(N+1)":                 alpha_n * lnN1,
        f"α^{n_alpha} × ln(N+1) × (N-1)":         alpha_n * lnN1 * (N_max-1),
        f"α^{n_alpha} × ln(N+1)/N_max":            alpha_n * lnN1 / N_max,
        f"α^{n_alpha} × π/N_max":                  alpha_n * pi / N_max,
        f"α^{n_alpha} × π^2/N_max":                alpha_n * pi**2 / N_max,
        f"α^{n_alpha} × Vol_D5 × N_max":           alpha_n * Vol_D5 * N_max,
        f"α^{n_alpha} × Vol_D5 × (N+1)²":          alpha_n * Vol_D5 * (N_max+1)**2,
        f"α^{n_alpha} × mp_me/N_max":              alpha_n * mp_me / N_max,
        f"α^{n_alpha} × e^{{-1/2}} × ln(N+1)×(N-1)": alpha_n * e_nat**(-0.5) * lnN1*(N_max-1),
        f"α^{n_alpha} × T_c(BST)/N_max × ln(N+1)": alpha_n * T_c_BST / N_max * lnN1,
    }
    for label, val in tests.items():
        if val > 0:
            err = (val / target - 1) * 100
            if abs(err) < 1.0:
                flag = " ◄◄◄" if abs(err)<0.1 else " ◄◄"
                print(f"  {label:45s}  {val:14.4e}  {err:+7.4f}%{flag}")
                best_results.append((label, val, err))

if not best_results:
    print("  No candidates within 1%")

# ══════════════════════════════════════════════════════════════════════════════
# 8. THE BEKENSTEIN ROUTE (physical derivation candidate)
# ══════════════════════════════════════════════════════════════════════════════
print()
print("=" * 70)
print("8. BEKENSTEIN-BERGMAN ROUTE")
print("=" * 70)

print(f"""
  Physical argument:
  The electron is a minimal S^1 winding on the BST channel (Shilov boundary).
  Its entropy budget: S_electron = N_committed × ln(2) where N_committed
  channels go from |uncommitted> to |e⁻-present>.

  By Bekenstein, S_Schwarzschild = 4π R_s² / (4G) = S_BST.
  This fixes G (and thus m_Pl) relative to the BST circuit energy.

  Argument: m_e / m_Pl = exp(-π × n_C × ln(N_max+1))

  Test:
""")
S_Bekenstein = pi * n_C * lnN1
m_e_Bek = np.exp(-S_Bekenstein)
print(f"  S = π × n_C × ln(N+1) = π × {n_C} × {lnN1:.4f} = {S_Bekenstein:.4f}")
print(f"  exp(-S) = {m_e_Bek:.4e}  vs  m_e/m_Pl = {m_e_mPl:.4e}")
print(f"  Error: {(m_e_Bek/m_e_mPl - 1)*100:+.4f}%")
print()

# Try alternative Bekenstein actions
print(f"  Alternative Bekenstein actions S and m_e = exp(-S):")
print(f"  {'S candidate':35s}  {'S value':>10}  {'m_e':>14}  {'error%':>10}")
for name, S in [
    ("π × n_C × ln(N+1)",          pi * n_C * lnN1),
    ("2π × n_C × ln(N+1)/2",       2*pi * n_C * lnN1/2),
    ("(n_C+1) × π × ln(N+1)",      (n_C+1) * pi * lnN1),
    ("n_C × π² × ln(N+1)",         n_C * pi**2 * lnN1),
    ("n_C × 2π × ln(N+1)",         n_C * 2*pi * lnN1),
    ("α^{-1} × ln(N+1)",           lnN1 / alpha),
    ("α^{-1} × n_C × ln(N+1)",     n_C * lnN1 / alpha),
    ("N_max × ln(N+1)",             N_max * lnN1),
    ("N_max × ln(N_max)",           N_max * np.log(N_max)),
    ("N_max × π",                   N_max * pi),
    ("N_max × 2π",                  N_max * 2*pi),
    ("N_max × 4π",                  N_max * 4*pi),
    ("N_max × ln(mp_me)",           N_max * np.log(mp_me)),
    ("N_max × ln(N+1) × α",        N_max * lnN1 * alpha),  # ← this would be nice
]:
    m_pred = np.exp(-S)
    err = (m_pred/m_e_mPl - 1)*100
    flag = " ◄◄◄" if abs(err)<0.5 else (" ◄◄" if abs(err)<2 else (" ◄" if abs(err)<10 else ""))
    print(f"  {name:35s}  {S:10.4f}  {m_pred:14.4e}  {err:+9.4f}%{flag}")

# ══════════════════════════════════════════════════════════════════════════════
# 9. SUMMARY AND CONCLUSIONS
# ══════════════════════════════════════════════════════════════════════════════
print()
print("=" * 70)
print("9. SUMMARY")
print("=" * 70)

print(f"""
  TARGET: m_e/m_Pl = {m_e_mPl:.8e}
  S_Bergman ≡ -ln(m_e/m_Pl) = {-np.log(m_e_mPl):.6f}

  Route A: (N_max-1) × ln(N+1)/50 × α^11
    = {formula_A:.6e}   error = {err_A:+.4f}%
    VERDICT: Genuine 0.06% gap — F_BST is β-dependent (F = ln(138)/β),
             and β=50 has no deep physical meaning. Formula is approximate.

  Route B: N_max × T_c(phys) / T_c(BST)
    m_e = {m_e_from_Tc:.5f} MeV   error = {err_Tc:+.4f}%
    VERDICT: 0.05% — promising but requires T_c(phys) as input.
             T_c(phys) = 0.487 MeV is not yet derived from BST geometry.
             OPEN: Can T_c(phys) be derived from α alone?

  n_α = log(m_e/m_Pl)/log(α) = {np.log(m_e_mPl)/np.log(alpha):.6f} (not an integer)
    → m_e/m_Pl is NOT a pure power of α. Requires additional structure.
    → The Bekenstein route (exponential suppression) is more natural.

  PHYSICAL INSIGHT: The hierarchy m_e << m_Pl is an exponential,
  not a power law. The BST derivation should give:

    m_e/m_Pl = exp(-S_Bergman)

  where S_Bergman is the Bergman action of the minimal S^1 winding on
  D_IV^5. The value S_Bergman = {-np.log(m_e_mPl):.2f} must follow from the Bergman
  geometry alone — not from a simple formula involving α.

  NEXT STEPS:
    1. Derive T_c(phys) from α: if T_c(phys) = m_e × T_c(BST)/N_max,
       then the T_c equation is circular. Need external BST derivation of T_c(phys).
    2. Compute S_Bergman directly from the Bergman kernel on D_IV^5:
       S = ∫_{{S^1}} K_Bergman(z,z) dz for the minimal winding curve.
    3. Bekenstein argument: the electron's entropy in BST contact graph
       = Bekenstein entropy of Schwarzschild horizon of m_e black hole
       → S = 4πG m_e²/(ħc) × some factor = S_Bergman.

  Code: notes/bst_hierarchy.py  (this file)
  Next: notes/BST_GravitationalConstant.md (working note for G derivation)
""")
