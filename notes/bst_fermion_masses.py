#!/usr/bin/env python3
"""
BST Fermion Mass Spectrum from D_IV^5 Submanifold Geometry
===========================================================
BST principle: mass ∝ circuit length ∝ number of contacts.
Each fermion generation lives on a totally geodesic submanifold D_IV^k ⊂ D_IV^5.
Mass ratios come from ratios of geometric quantities on these submanifolds.

Authors: Casey Koons & Claude (Anthropic), March 2026
"""

import numpy as np
from scipy.special import gamma
from itertools import product as iterproduct

# ─── Physical constants ────────────────────────────────────────────────────
# Lepton masses in MeV (PDG 2022)
M_E   = 0.51099895    # electron
M_MU  = 105.6583755   # muon
M_TAU = 1776.86       # tau

R_MU_E  = M_MU / M_E    # 206.768
R_TAU_MU = M_TAU / M_MU  # 16.817
R_TAU_E  = M_TAU / M_E   # 3477.15

# Quark masses (MS-bar at 2 GeV, MeV) — for later
M_U = 2.16;   M_D = 4.67;  M_S = 93.4
M_C = 1270.0; M_B = 4180.0; M_T = 172760.0

# BST constants
N_MAX = 137
ALPHA_WYLER = 0.00729735   # 1/137.036082

print("=" * 65)
print("BST FERMION MASS SPECTRUM — GEOMETRIC EXPLORATION")
print("=" * 65)
print(f"\nTarget ratios:")
print(f"  m_μ/m_e  = {R_MU_E:.6f}")
print(f"  m_τ/m_μ  = {R_TAU_MU:.6f}")
print(f"  m_τ/m_e  = {R_TAU_E:.6f}")

# ─── Section 1: D_IV^k Bergman volumes ──────────────────────────────────────
print("\n" + "─" * 65)
print("SECTION 1: D_IV^k Bergman Volumes")
print("  Formula: Vol(D_IV^n) = π^n / (2^(n-1) × n!)")
print("─" * 65)

def vol_DIV(n):
    """Bergman volume of D_IV^n."""
    return np.pi**n / (2**(n-1) * gamma(n+1))

vols = {n: vol_DIV(n) for n in range(1, 8)}
for n, v in vols.items():
    print(f"  Vol(D_IV^{n}) = π^{n}/(2^{n-1}×{n}!) = {v:.8f}")

# Verify D_IV^5
print(f"\n  D_IV^5 check: π^5/1920 = {np.pi**5/1920:.8f}  (must match vol_DIV(5) = {vols[5]:.8f})")

# ─── Section 2: Shilov boundary volumes ─────────────────────────────────────
print("\n" + "─" * 65)
print("SECTION 2: Shilov Boundary Volumes  S^(n-1) × S^1")
print("─" * 65)

def vol_sphere(n):
    """Volume of S^n."""
    return 2 * np.pi**((n+1)/2) / gamma((n+1)/2)

def vol_shilov(n):
    """Vol of Shilov boundary of D_IV^n = Vol(S^(n-1)) × Vol(S^1)."""
    if n == 1:
        return vol_sphere(1)   # just S^1
    return vol_sphere(n-1) * vol_sphere(1)

for n in range(1, 8):
    sb = vol_shilov(n)
    if n == 1:
        print(f"  Shilov(D_IV^1) = S^1,       Vol = {sb:.6f}")
    else:
        print(f"  Shilov(D_IV^{n}) = S^{n-1}×S^1, Vol = {sb:.6f}")

# ─── Section 3: Natural volume ratios ──────────────────────────────────────
print("\n" + "─" * 65)
print("SECTION 3: Key Volume Ratios (Domain and Shilov Boundary)")
print("─" * 65)

ratios = {}
for n1 in range(1, 6):
    for n2 in range(1, 6):
        if n2 != n1:
            ratios[f'D{n1}/D{n2}'] = vols[n1] / vols[n2]
            ratios[f'S{n1}/S{n2}'] = vol_shilov(n1) / vol_shilov(n2)

key_ratios = {
    'Vol(D1)/Vol(D3)': vols[1]/vols[3],
    'Vol(D3)/Vol(D5)': vols[3]/vols[5],
    'Vol(D1)/Vol(D5)': vols[1]/vols[5],
    'Vol(D5)/Vol(D1)': vols[5]/vols[1],
    'Vol(D3)/Vol(D1)': vols[3]/vols[1],
    'Vol(D5)/Vol(D3)': vols[5]/vols[3],
    'Shilov(D5)/Shilov(D3)': vol_shilov(5)/vol_shilov(3),
    'Shilov(D3)/Shilov(D1)': vol_shilov(3)/vol_shilov(1),
    'Shilov(D5)/Shilov(D1)': vol_shilov(5)/vol_shilov(1),
}

for name, val in key_ratios.items():
    print(f"  {name:35s} = {val:.8f}")

# ─── Section 4: Power-law search for m_μ/m_e ────────────────────────────────
print("\n" + "─" * 65)
print("SECTION 4: Power-law Search  r^p = 206.768")
print("─" * 65)

candidates = {
    '24/π²  = Vol(D1)/Vol(D3)':   vols[1]/vols[3],
    '1920/π⁴ = Vol(D1)/Vol(D5)':  vols[1]/vols[5],
    '80/π²  = Vol(D3)/Vol(D5)':   vols[3]/vols[5],  # actually D3/D5 not D1/D5... let me recheck
    'π²/24  = Vol(D3)/Vol(D1)':   vols[3]/vols[1],
    'π^4/1920 = Vol(D5)/Vol(D1)': vols[5]/vols[1],
    'π^2/80 = Vol(D5)/Vol(D3)':   vols[5]/vols[3],
    'Vol(S4)/Vol(S2)':             vol_sphere(4)/vol_sphere(2),
    'Vol(S4)/Vol(S1)':             vol_sphere(4)/vol_sphere(1),
    'Vol(S2)/Vol(S1)':             vol_sphere(2)/vol_sphere(1),
}

print(f"  Target: m_μ/m_e = {R_MU_E:.4f}")
for name, base in candidates.items():
    if base > 1:
        p = np.log(R_MU_E) / np.log(base)
        pred = base**round(p)
        err = abs(pred - R_MU_E)/R_MU_E * 100
        print(f"  ({name:38s})^{p:.3f}  [nearest int p={round(p)}: pred={pred:.2f}, err={err:.2f}%]")

# ─── Section 5: The key finding — (24/π²)^6 ────────────────────────────────
print("\n" + "─" * 65)
print("SECTION 5: The (24/π²)^6 Formula")
print("─" * 65)

x = 24 / np.pi**2
print(f"  x = 24/π² = Vol(D_IV^1)/Vol(D_IV^3) = {x:.8f}")
print(f"  x^6 = {x**6:.6f}  (target m_μ/m_e = {R_MU_E:.6f}, err = {abs(x**6-R_MU_E)/R_MU_E*100:.3f}%)")
print(f"  x^9 = {x**9:.2f}   (target m_τ/m_e = {R_TAU_E:.2f})")
print()
# Now check if there's a consistent exponent pattern
# If m_k ∝ x^{a_k}, then m_e:m_μ:m_τ ∝ x^0 : x^6 : x^{?}
p_tau_e = np.log(R_TAU_E) / np.log(x)
p_tau_mu = np.log(R_TAU_MU) / np.log(x)
print(f"  For m_τ/m_e = {R_TAU_E:.2f}:  need x^p with p = {p_tau_e:.4f}")
print(f"  For m_τ/m_μ = {R_TAU_MU:.4f}: need x^p with p = {p_tau_mu:.4f}")

# ─── Section 6: BST-natural formulas ────────────────────────────────────────
print("\n" + "─" * 65)
print("SECTION 6: BST-Natural Formulas Involving N_max")
print("─" * 65)

# Nambu-type
nambu = 3 * (N_MAX + 1) / 2
print(f"  (3/2)(N_max+1) = (3/2)(138)  = {nambu:.4f}  [target {R_MU_E:.4f}, err={abs(nambu-R_MU_E)/R_MU_E*100:.3f}%]")

nambu_exact = 3 * N_MAX / 2
print(f"  (3/2)(N_max)   = (3/2)(137)  = {nambu_exact:.4f}  [target {R_MU_E:.4f}, err={abs(nambu_exact-R_MU_E)/R_MU_E*100:.3f}%]")

# (3/2)/α
half_alpha = 1.5 / ALPHA_WYLER
print(f"  3/(2α_Wyler)              = {half_alpha:.4f}  [target {R_MU_E:.4f}, err={abs(half_alpha-R_MU_E)/R_MU_E*100:.3f}%]")

# Tau formulas
print(f"\n  For m_τ/m_e = {R_TAU_E:.2f}:")
f1 = 8 * np.pi * (N_MAX + 1)
print(f"  8π(N_max+1)  = 8π×138      = {f1:.2f}  [err={abs(f1-R_TAU_E)/R_TAU_E*100:.2f}%]")
f2 = (3/2)**2 * (N_MAX+1) * np.pi * np.sqrt(N_MAX+1)
f3 = 3 * np.pi * (N_MAX+1) * np.pi   # just trying
f4 = np.pi**2 * (N_MAX + 1) * 3 / (np.pi/2)
print(f"  3(N_max+1)²/... trying various...")

# Check if m_τ/m_e has a clean form
# 3477 ≈ 3 × 137 × π² / 3.53...
for a in [1, 2, 3, 4]:
    for b in [-2, -1, 0, 1, 2]:
        for nfact in [N_MAX, N_MAX+1, 2*N_MAX, 2*(N_MAX+1)]:
            val = a * nfact * np.pi**b if b != 0 else a * nfact
            err = abs(val - R_TAU_E) / R_TAU_E * 100
            if err < 1.0:
                print(f"    {a}×{nfact}×π^{b} = {val:.3f}  (err={err:.3f}%)")

# ─── Section 7: Systematic search over Vol ratio powers ─────────────────────
print("\n" + "─" * 65)
print("SECTION 7: Systematic Search — Vol(D_IV^a)^p / Vol(D_IV^b)^q")
print("─" * 65)

print(f"  Searching for (Vol(D_IV^a)/Vol(D_IV^b))^p = m_μ/m_e = {R_MU_E:.4f}")
print(f"  and separately for m_τ/m_μ = {R_TAU_MU:.4f}")
print()

best_mue = []
best_taumu = []

for a in range(1, 7):
    for b in range(1, 7):
        if a == b:
            continue
        ratio = vols[a] / vols[b] if b <= 5 else vol_DIV(b)
        if ratio <= 0:
            continue
        # For m_μ/m_e
        p = np.log(R_MU_E) / np.log(ratio) if ratio != 1 else np.inf
        for p_test in [p - 0.5, p, p + 0.5]:
            if 0.1 < p_test < 20:
                pred = ratio**p_test
                err = abs(pred - R_MU_E) / R_MU_E * 100
                if err < 2.0 and abs(p_test - round(p_test)) < 0.05:
                    best_mue.append((err, f"(Vol(D{a})/Vol(D{b}))^{round(p_test)}", pred, round(p_test), ratio))
        # For m_τ/m_μ
        p2 = np.log(R_TAU_MU) / np.log(ratio) if ratio != 1 else np.inf
        for p_test in [p2 - 0.5, p2, p2 + 0.5]:
            if 0.1 < p_test < 20:
                pred = ratio**p_test
                err = abs(pred - R_TAU_MU) / R_TAU_MU * 100
                if err < 5.0 and abs(p_test - round(p_test)) < 0.1:
                    best_taumu.append((err, f"(Vol(D{a})/Vol(D{b}))^{round(p_test)}", pred, round(p_test), ratio))

best_mue.sort()
best_taumu.sort()

print("  Best fits for m_μ/m_e (integer exponents, err < 2%):")
for err, name, pred, p, base in best_mue[:8]:
    print(f"    {name:40s} = {pred:.4f}  (err={err:.3f}%,  base={base:.4f})")

print("\n  Best fits for m_τ/m_μ (integer exponents, err < 5%):")
for err, name, pred, p, base in best_taumu[:8]:
    print(f"    {name:40s} = {pred:.4f}  (err={err:.3f}%,  base={base:.4f})")

# ─── Section 8: Shilov boundary systematic search ───────────────────────────
print("\n" + "─" * 65)
print("SECTION 8: Shilov Boundary Ratio Search")
print("─" * 65)

print(f"  Sphere volumes:")
for n in range(0, 6):
    print(f"    Vol(S^{n}) = {vol_sphere(n):.6f}")
print()

# S^4, S^2, S^1 ratios
s4s1 = vol_sphere(4) / vol_sphere(1)
s2s1 = vol_sphere(2) / vol_sphere(1)
s4s2 = vol_sphere(4) / vol_sphere(2)
print(f"  Vol(S^4)/Vol(S^1) = {s4s1:.6f}")
print(f"  Vol(S^2)/Vol(S^1) = {s2s1:.6f}")
print(f"  Vol(S^4)/Vol(S^2) = {s4s2:.6f}")

# Check powers
for base_name, base_val in [("S4/S1", s4s1), ("S2/S1", s2s1), ("S4/S2", s4s2)]:
    p = np.log(R_MU_E) / np.log(base_val)
    print(f"\n  ({base_name})^p = 206.77: p = {p:.4f}")
    for pi in range(1, 10):
        pred = base_val**pi
        err = abs(pred - R_MU_E) / R_MU_E * 100
        if err < 20:
            print(f"    p={pi}: {pred:.4f}  (err={err:.1f}%)")

# ─── Section 9: Combined formula search ─────────────────────────────────────
print("\n" + "─" * 65)
print("SECTION 9: Combined Formula — α, N_max, volumes")
print("─" * 65)

alpha = 1/137.036082
Nmax = 137

# Is there a formula m_μ/m_e = f(α, π, N_max) that's exact?
# We know x^6 ≈ 207 where x = 24/π², and (3/2)(N_max+1) ≈ 207
# Let's look at these simultaneously

print(f"  x = 24/π² = {24/np.pi**2:.8f}")
print(f"  x^6 = {(24/np.pi**2)**6:.8f}   vs m_μ/m_e = {R_MU_E:.8f}")
print(f"  (3/2)(N_max+1) = {1.5*(N_MAX+1):.8f}  vs m_μ/m_e = {R_MU_E:.8f}")
print()
print(f"  Are these the same?  x^6 / [(3/2)(N_max+1)] = {(24/np.pi**2)**6 / (1.5*138):.8f}")
print()

# Search for combinations α^a × π^b × N^c matching the tau/muon ratio
print(f"  Searching for α^a × π^b × (N_max+1)^c = m_τ/m_μ = {R_TAU_MU:.4f}:")
hits = []
for a in np.arange(-2, 3, 0.5):
    for b in np.arange(-4, 5, 0.5):
        for c in np.arange(-1, 3, 0.5):
            val = (alpha**a if a != 0 else 1) * (np.pi**b if b != 0 else 1) * ((N_MAX+1)**c if c != 0 else 1)
            err = abs(val - R_TAU_MU) / R_TAU_MU * 100
            if err < 0.5:
                hits.append((err, a, b, c, val))

hits.sort()
for err, a, b, c, val in hits[:10]:
    print(f"    α^{a:.1f} × π^{b:.1f} × (N+1)^{c:.1f} = {val:.6f}  (err={err:.4f}%)")

# ─── Section 10: The Wyler-style mass formula ───────────────────────────────
print("\n" + "─" * 65)
print("SECTION 10: Wyler-Style Mass Formula from D_IV^k")
print("─" * 65)

# Wyler formula: α = (9/8π^4)(Vol D_IV^5)^{1/4}
# Generalize: α_k = C_k × (Vol D_IV^k)^{1/(2(k-1))}  for k ≥ 2
# (the 1/4 for k=5 comes from dim(S^4) = 4 = 2(5-1)/... hmm, 4 = k-1 for k=5)
# More natural: α_k = C_k × (Vol D_IV^k)^{1/(k-1)}

# For the Wyler formula, the exponent is 1/4 = 1/(k-1) with k=5
print("  Wyler-type formula: α_k ∝ Vol(D_IV^k)^{1/(k-1)}")
for k in range(2, 7):
    v = vol_DIV(k)
    alpha_k = v**(1/(k-1))
    print(f"    k={k}: Vol^{{1/{k-1}}} = {alpha_k:.8f}")

print()
# What if mass ∝ 1/Vol(D_IV^k)^{1/(k-1)} ?
print("  mass_k ∝ 1/Vol(D_IV^k)^{1/(k-1)} :")
masses_wyler = {}
for k in [1, 3, 5]:
    if k == 1:
        m_k = 1.0 / vol_DIV(1)   # 1/π
    else:
        m_k = 1.0 / vol_DIV(k)**(1/(k-1))
    masses_wyler[k] = m_k
    print(f"    k={k}: 1/Vol^{{1/{max(1,k-1)}}} = {m_k:.6f}")

if 3 in masses_wyler and 1 in masses_wyler:
    print(f"\n  m_μ/m_e = masses[3]/masses[1] = {masses_wyler[3]/masses_wyler[1]:.4f}  (target {R_MU_E:.4f})")
if 5 in masses_wyler and 3 in masses_wyler:
    print(f"  m_τ/m_μ = masses[5]/masses[3] = {masses_wyler[5]/masses_wyler[3]:.4f}  (target {R_TAU_MU:.4f})")

# ─── Section 11: Summary ────────────────────────────────────────────────────
print("\n" + "=" * 65)
print("SECTION 11: SUMMARY OF FINDINGS")
print("=" * 65)

print(f"""
Key findings:

1. VOLUME FORMULA: Vol(D_IV^k) = π^k / (2^(k-1) × k!)
   k=1: {vols[1]:.6f}  (= π)
   k=3: {vols[3]:.6f}  (= π³/24)
   k=5: {vols[5]:.6f}  (= π^5/1920)

2. STRIKING NUMERICAL RESULT:
   x = Vol(D_IV^1)/Vol(D_IV^3) = 24/π² = {24/np.pi**2:.6f}
   x^6 = {(24/np.pi**2)**6:.4f}  vs  m_μ/m_e = {R_MU_E:.4f}  (err = {abs((24/np.pi**2)**6 - R_MU_E)/R_MU_E*100:.3f}%)
   
   This suggests m_μ/m_e = (Vol D_IV^1 / Vol D_IV^3)^6
   Exponent 6 = real dimension of D_IV^3 = 2 × complex dim of D_IV^3

3. BST-NATURAL FORMULA:
   (3/2)(N_max+1) = {1.5*(N_MAX+1):.4f}  vs  m_μ/m_e = {R_MU_E:.4f}  (err = {abs(1.5*(N_MAX+1) - R_MU_E)/R_MU_E*100:.3f}%)
   
   NOTE: x^6 and (3/2)(N_max+1) are DIFFERENT numbers — they coincide to 0.15%,
   not from the same formula.

4. TAU MASS:
   m_τ/m_μ = {R_TAU_MU:.4f} does NOT have a clean Vol(D_IV^k)^{{integer}} form.
   Best Vol-based fit: requires non-integer or large exponents.
   
   Possible BST formula: m_τ/m_e = 8π(N_max+1) = {8*np.pi*(N_MAX+1):.2f}  (err={abs(8*np.pi*(N_MAX+1)-R_TAU_E)/R_TAU_E*100:.2f}%)

5. OPEN QUESTION: 
   Is the exponent 6 = 2×(complex dim of D_IV^3) a coincidence or
   derived from the Bergman metric embedding structure?
   Need: induced metric ratio for D_IV^3 ⊂ D_IV^5.
""")

