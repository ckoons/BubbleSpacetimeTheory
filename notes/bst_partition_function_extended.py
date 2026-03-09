#!/usr/bin/env python3
"""
BST Partition Function: Extended Computation
Casey Koons & Claude (Anthropic), March 2026

Extends the Shilov boundary partition function on S^4 x S^1 (first computed in
the Opus session) to higher mode truncations, full thermodynamic profiles,
N_max dependence, bulk D_IV^5 correction, and refined Lambda estimate.

Tasks:
  1. Convergence study: F vs l_max at several temperatures
  2. Thermodynamic profile: lnZ, E, S, F, Cv across all phases
  3. N_max dependence: how Haldane(137) sits relative to fermionic/bosonic
  4. Refined cosmological constant estimate
  5. Bulk D_IV^5 Bergman measure correction

Outputs: CSV files and summary statistics.
"""

import numpy as np
import csv
import os
import sys
from time import time

# Output directory: same folder as this script
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


# ============================================================================
# Core computation functions
# ============================================================================

def s4_degeneracy(l):
    """Degeneracy of l-th S^4 spherical harmonic: d_l = (2l+3)(l+1)(l+2) // 6"""
    return (2 * l + 3) * (l + 1) * (l + 2) // 6


def ln_Z_mode_array(x, N_max=137):
    """
    Compute ln(Z_mode) for an array of x = beta * E.

    Z_mode = sum_{n=0}^{N_max} exp(-n*x) = (1 - exp(-(N_max+1)*x)) / (1 - exp(-x))

    Special cases:
      x = 0: Z_mode = N_max + 1  =>  ln Z_mode = ln(N_max + 1)
      x >> 1: Z_mode -> 1         =>  ln Z_mode -> 0
    """
    x = np.asarray(x, dtype=float)
    result = np.zeros_like(x)

    zero_mask = (x == 0.0)
    result[zero_mask] = np.log(N_max + 1)

    # For x > 50, the mode is effectively unoccupied: ln Z_mode ~ 0
    normal_mask = ~zero_mask & (x < 50.0)
    xn = x[normal_mask]
    # log(1 - exp(-y)) = log(-expm1(-y)) for numerical stability
    log_numer = np.log(-np.expm1(-(N_max + 1) * xn))
    log_denom = np.log(-np.expm1(-xn))
    result[normal_mask] = log_numer - log_denom

    return result


def build_energy_grid(l_max, m_max, R_b=1.0, R_s=1.0):
    """
    Return (d_l, E) where:
      d_l: shape (l_max+1,)  -- S^4 degeneracies
      E:   shape (l_max+1, 2*m_max+1) -- energies E_{l,m}
    """
    l_vals = np.arange(l_max + 1)
    m_vals = np.arange(-m_max, m_max + 1)

    d_l = np.array([s4_degeneracy(l) for l in l_vals])

    l_grid, m_grid = np.meshgrid(l_vals, m_vals, indexing='ij')
    E = np.sqrt(l_grid * (l_grid + 3) / R_b**2 + m_grid**2 / R_s**2)
    return d_l, E


def ln_Z_total(beta, l_max, m_max, N_max=137, R_b=1.0, R_s=1.0):
    """Compute total ln Z on Shilov boundary S^4 x S^1."""
    d_l, E = build_energy_grid(l_max, m_max, R_b, R_s)
    x = beta * E
    lnZ_mode = ln_Z_mode_array(x, N_max)
    return float(np.sum(d_l[:, np.newaxis] * lnZ_mode))


def ln_Z_qft(l_max, m_max, R_b=1.0, R_s=1.0):
    """QFT zero-point energy: sum of d_l * E/2 (no cap, diverges with modes)."""
    d_l, E = build_energy_grid(l_max, m_max, R_b, R_s)
    return float(np.sum(d_l[:, np.newaxis] * E / 2.0))


def thermodynamics(beta, l_max, m_max, N_max=137):
    """
    Compute thermodynamic quantities at given beta using central differences.
    Returns dict: lnZ, E_avg, S, F, Cv
    """
    h = max(beta * 0.005, 1e-5)
    lnZ   = ln_Z_total(beta,     l_max, m_max, N_max)
    lnZ_p = ln_Z_total(beta + h, l_max, m_max, N_max)
    lnZ_m = ln_Z_total(beta - h, l_max, m_max, N_max)

    E_avg = -(lnZ_p - lnZ_m) / (2 * h)
    Cv    =  beta**2 * (lnZ_p - 2 * lnZ + lnZ_m) / h**2
    S     =  beta * E_avg + lnZ
    F     = -lnZ / beta
    return dict(lnZ=lnZ, E_avg=E_avg, S=S, F=F, Cv=Cv)


# ============================================================================
# Task 1: Convergence Study
# ============================================================================

def task1_convergence():
    print("\n" + "=" * 65)
    print("TASK 1: CONVERGENCE STUDY")
    print("=" * 65)

    # Run at three temperatures: high T, intermediate, low T
    beta_cases = [
        (0.1,  "high-T  (T=10)"),
        (1.0,  "mid-T   (T=1) "),
        (50.0, "low-T   (T=0.02)"),
    ]

    # Increasing mode truncations
    runs = [
        (5,  3),
        (10, 5),
        (15, 8),
        (20, 8),   # Reproduces Opus result
        (25, 10),
        (30, 12),
        (40, 15),
        (50, 20),
    ]

    all_rows = []

    for beta, label in beta_cases:
        print(f"\n  {label}  beta={beta}")
        print(f"  {'l_max':>6} {'m_max':>6} {'mode_slots':>12} "
              f"{'ln Z':>12} {'F':>12} {'delta_F':>12}")

        prev_F = None
        for l_max, m_max in runs:
            mode_slots = sum(s4_degeneracy(l) for l in range(l_max + 1)) * (2 * m_max + 1)
            t0 = time()
            lnZ = ln_Z_total(beta, l_max, m_max)
            F = -lnZ / beta
            dF = (F - prev_F) if prev_F is not None else float('nan')
            elapsed = time() - t0

            print(f"  {l_max:>6} {m_max:>6} {mode_slots:>12,} "
                  f"{lnZ:>12.4f} {F:>12.6f} {dF:>12.6f}  ({elapsed:.2f}s)")

            all_rows.append(dict(
                beta=beta, T=1/beta, label=label,
                l_max=l_max, m_max=m_max, mode_slots=mode_slots,
                lnZ=lnZ, F=F, delta_F=dF
            ))
            prev_F = F

            if elapsed > 90:
                print(f"  (stopping at l_max={l_max} — time limit)")
                break

    # Also print QFT vacuum energy comparison
    print("\n  QFT zero-point energy (no Haldane cap):")
    for l_max, m_max in [(10,5), (20,8), (30,12)]:
        E_qft = ln_Z_qft(l_max, m_max)
        lnZ_bst = ln_Z_total(50.0, l_max, m_max)
        F_bst = -lnZ_bst / 50.0
        print(f"    l_max={l_max}: QFT E_vac = {E_qft:.2e},  BST |F| = {abs(F_bst):.4f},  ratio = {E_qft/abs(F_bst):.2e}")

    # Write CSV
    csv_path = os.path.join(OUT_DIR, 'BST_PartitionFunction_Convergence.csv')
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['beta','T','label','l_max','m_max',
                                          'mode_slots','lnZ','F','delta_F'])
        w.writeheader(); w.writerows(all_rows)
    print(f"\n  -> {csv_path}")
    return all_rows


# ============================================================================
# Task 2: Full Thermodynamic Profile
# ============================================================================

def task2_thermodynamics(l_max=25, m_max=10, N_max=137):
    print("\n" + "=" * 65)
    print(f"TASK 2: THERMODYNAMIC PROFILE  l_max={l_max}, m_max={m_max}, N_max={N_max}")
    print("=" * 65)

    beta_vals = np.logspace(-2, np.log10(200), 120)

    rows = []
    Cv_max = -np.inf
    Tc = None

    for i, beta in enumerate(beta_vals):
        T = 1.0 / beta
        th = thermodynamics(beta, l_max, m_max, N_max)
        if th['Cv'] > Cv_max:
            Cv_max = th['Cv']
            Tc = T
        rows.append(dict(beta=beta, T=T, **th))

        if (i + 1) % 24 == 0:
            print(f"  beta={beta:7.3f}  T={T:7.3f}  lnZ={th['lnZ']:10.3f}  "
                  f"Cv={th['Cv']:10.3f}  F={th['F']:10.5f}")

    # Key results
    low_T = rows[-1]
    hi_T  = rows[0]
    print(f"\n  Phase transition:  T_c = {Tc:.4f},  Cv_max = {Cv_max:.4f}")
    print(f"  Low-T  (beta=200): lnZ = {low_T['lnZ']:.4f}  "
          f"(expect ln(138) = {np.log(138):.4f}),  F = {low_T['F']:.6f}")
    print(f"  High-T (beta=0.01): lnZ = {hi_T['lnZ']:.2f}")

    csv_path = os.path.join(OUT_DIR, 'BST_PartitionFunction_Thermodynamics.csv')
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['beta','T','lnZ','E_avg','S','F','Cv'])
        w.writeheader(); w.writerows(rows)
    print(f"  -> {csv_path}")

    return rows, Tc, Cv_max


# ============================================================================
# Task 3: N_max Dependence
# ============================================================================

def task3_nmax(l_max=20, m_max=8):
    print("\n" + "=" * 65)
    print(f"TASK 3: N_MAX DEPENDENCE  l_max={l_max}, m_max={m_max}")
    print("=" * 65)

    N_max_vals = [1, 2, 5, 10, 20, 50, 100, 137, 200, 500, 1000, 10000]
    beta_low = 100.0   # Deep spatial phase

    # Scan beta for T_c
    beta_scan = np.logspace(-2, 2, 60)

    print(f"  {'N_max':>8} {'lnZ(T→0)':>12} {'ln(N+1)':>10} "
          f"{'F(T→0)':>10} {'T_c':>8} {'Cv_max':>10}")

    rows = []
    for N_max in N_max_vals:
        lnZ_low = ln_Z_total(beta_low, l_max, m_max, N_max)
        F_low   = -lnZ_low / beta_low
        exp_lnZ = np.log(N_max + 1)

        Cv_list = [thermodynamics(b, l_max, m_max, N_max)['Cv'] for b in beta_scan]
        Cv_max_val = max(Cv_list)
        Tc_val = 1.0 / beta_scan[np.argmax(Cv_list)]

        print(f"  {N_max:>8} {lnZ_low:>12.4f} {exp_lnZ:>10.4f} "
              f"{F_low:>10.5f} {Tc_val:>8.4f} {Cv_max_val:>10.4f}")

        rows.append(dict(N_max=N_max, lnZ_low_T=lnZ_low, expected_lnZ=exp_lnZ,
                         F_low_T=F_low, T_c=Tc_val, Cv_max=Cv_max_val))

    # Is N_max=137 special? Compare to neighbors
    r137 = next(r for r in rows if r['N_max'] == 137)
    r136 = dict(N_max=136, T_c=None)  # just for reference
    print(f"\n  N_max=137 T_c = {r137['T_c']:.4f}  (BST value)")
    print(f"  Monotonic T_c vs N_max: {all(rows[i]['T_c'] <= rows[i+1]['T_c'] for i in range(len(rows)-1))}")

    csv_path = os.path.join(OUT_DIR, 'BST_PartitionFunction_NmaxDependence.csv')
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['N_max','lnZ_low_T','expected_lnZ',
                                          'F_low_T','T_c','Cv_max'])
        w.writeheader(); w.writerows(rows)
    print(f"  -> {csv_path}")
    return rows


# ============================================================================
# Task 4: Cosmological Constant
# ============================================================================

def task4_lambda(conv_rows, thermo_rows):
    print("\n" + "=" * 65)
    print("TASK 4: COSMOLOGICAL CONSTANT ESTIMATE")
    print("=" * 65)

    # Scale: d0/l_Planck from observed channel utilization
    # rho_universe / rho_137 ~ 10^{-123}
    # d0/l_Planck ~ (rho/rho_137)^{1/4} ~ 10^{-30.75}
    log10_ratio = -30.75
    scale4 = 10**(4 * log10_ratio)   # (d0/l_Planck)^4 ~ 10^{-123}

    lambda_obs = 2.9e-122

    # Collect F_BST candidates
    cases = []

    # From convergence study at beta=50
    beta50 = [r for r in conv_rows if abs(r['beta'] - 50.0) < 0.01]
    if beta50:
        for r in beta50[-3:]:
            cases.append((f"Convergence l={r['l_max']},m={r['m_max']},β=50",
                          abs(r['F'])))

    # From thermodynamics at lowest T
    low_T_F = abs(thermo_rows[-1]['F'])
    cases.append((f"Thermodynamics (highest β), F = {low_T_F:.5f}", low_T_F))

    # Original Opus result
    cases.append(("Opus session result (l=20,m=8,β=50)", 0.099))

    print(f"\n  Scale: (d0/l_Pl)^4 = 10^{4*log10_ratio:.2f} = {scale4:.3e}")
    print(f"  Observed Lambda = {lambda_obs:.2e}  (log10 = {np.log10(lambda_obs):.2f})")
    print()
    print(f"  {'Source':>44} {'|F_BST|':>10} {'Lambda':>13} {'orders off':>11}")

    rows = []
    for label, F_bst in cases:
        Lambda = F_bst * scale4
        log_L  = np.log10(Lambda) if Lambda > 0 else -999
        off    = log_L - np.log10(lambda_obs)
        print(f"  {label:>44} {F_bst:>10.5f} {Lambda:>13.3e}  {off:>+10.2f}")
        rows.append(dict(source=label, F_BST=F_bst, Lambda=Lambda,
                         log10_Lambda=log_L, orders_from_obs=off))

    # Alternative scale: d0 = alpha^n * l_Planck — which n gives Lambda_obs?
    alpha = 1.0 / 137
    F_ref = 0.099
    print(f"\n  Alternative: d0 = (1/137)^n * l_Planck  (F_BST = {F_ref})")
    print(f"  {'n':>4} {'d0/l_Pl':>14} {'Lambda':>14} {'orders off':>12}")
    for n in range(1, 12):
        d0_ratio = alpha**n
        L = F_ref * d0_ratio**4
        off = np.log10(L) - np.log10(lambda_obs) if L > 0 else -999
        mark = "  <-- exact match!" if abs(off) < 0.5 else ""
        print(f"  {n:>4} {d0_ratio:>14.4e} {L:>14.3e} {off:>12.2f}{mark}")

    # Note: if n = 30.75/log10(137) ≈ 30.75/2.137 ≈ 14.4, we'd get Lambda_obs
    n_exact = 30.75 / np.log10(137)
    L_nexact = F_ref * (alpha**n_exact)**4
    print(f"\n  For exact match: n = {n_exact:.3f}  (not a simple integer)")

    return rows


# ============================================================================
# Task 5: Bulk D_IV^5 Correction
# ============================================================================

def task5_bulk(l_max=15, m_max=8, N_max=137, N_r=25):
    """
    Estimate bulk correction using Bergman measure on D_IV^5.

    Model: interior points at radial parameter r in [0, 1-eps] have
    effective scale R_eff = R0 * sqrt(1 - r^2), giving higher mode energies
    than the Shilov boundary (r=0 in this parameterization). The Bergman
    measure weight is w(r) = (1-r^2)^{-7} * r^9.

    This parameterization places the Shilov boundary at r -> 0 (minimum
    energy, dominant at low T) and the center of the domain at r = 0
    (trivially — we let r run from 0 at boundary toward 1 at center).

    Concretely: R_eff(r) = R0 / sqrt(1 - r^2) means energies GROW away
    from the Shilov boundary, confirming that the boundary dominates at
    low T.
    """
    print("\n" + "=" * 65)
    print(f"TASK 5: BULK D_IV^5 CORRECTION  l_max={l_max}, m_max={m_max}, N_r={N_r}")
    print("=" * 65)

    beta = 50.0  # low T (spatial phase)
    eps  = 0.05  # stay away from r=1 where Bergman measure diverges

    # Shilov boundary (r=0): modes have natural energies
    lnZ_boundary = ln_Z_total(beta, l_max, m_max, N_max, R_b=1.0, R_s=1.0)
    F_boundary = -lnZ_boundary / beta
    print(f"  Shilov boundary: lnZ = {lnZ_boundary:.6f},  F = {F_boundary:.8f}")

    # Radial shells r in (0, 1-eps)
    r_vals = np.linspace(0.02, 1 - eps, N_r)

    def bergman_weight(r):
        # Bergman measure: (1-r^2)^{-7} * r^9 (Type IV domain, n=5, dim=10)
        return (1 - r**2)**(-7) * r**9

    rows = []
    lnZ_r_list = []
    w_list     = []

    print(f"\n  {'r':>6} {'R_eff':>8} {'Bergman_w':>14} {'lnZ(r)':>12} {'F(r)':>12}")
    for i, r in enumerate(r_vals):
        # Energy scales as 1/sqrt(1-r^2) relative to boundary
        # Equivalently, effective radius shrinks: R_eff = 1/sqrt(1-r^2)... wait.
        # If E = sqrt(l(l+3)/R_b^2 + m^2/R_s^2), smaller R_b => larger E.
        # At r in the interior, R_eff = R0 * sqrt(1-r^2) < R0,
        # so E_interior > E_boundary. Interior modes are more suppressed at low T.
        R_eff = np.sqrt(1 - r**2)
        w     = bergman_weight(r)

        lnZ_r = ln_Z_total(beta, l_max, m_max, N_max, R_b=R_eff, R_s=R_eff)
        F_r   = -lnZ_r / beta

        lnZ_r_list.append(lnZ_r)
        w_list.append(w)

        if i % 5 == 0:
            print(f"  {r:6.3f} {R_eff:8.4f} {w:14.4e} {lnZ_r:12.6f} {F_r:12.8f}")

        rows.append(dict(r=r, R_eff=R_eff, bergman_weight=w, lnZ=lnZ_r, F=F_r))

    lnZ_arr = np.array(lnZ_r_list)
    w_arr   = np.array(w_list)

    # Weighted average lnZ over the interior
    denom   = np.trapz(w_arr, r_vals)
    numer   = np.trapz(w_arr * lnZ_arr, r_vals)
    lnZ_bulk_avg = numer / denom if denom > 0 else 0
    F_bulk_avg   = -lnZ_bulk_avg / beta

    # Bulk/boundary ratio (how much does interior add?)
    bulk_fraction = lnZ_bulk_avg / lnZ_boundary

    print(f"\n  Shilov boundary lnZ:        {lnZ_boundary:.6f}")
    print(f"  Bergman-weighted bulk lnZ:  {lnZ_bulk_avg:.6f}")
    print(f"  Bulk / boundary ratio:      {bulk_fraction:.6f}")
    print(f"  Interpretation: interior modes contribute {bulk_fraction*100:.4f}% of boundary value")
    print(f"  => Boundary approximation is {'EXCELLENT' if bulk_fraction < 0.01 else 'GOOD' if bulk_fraction < 0.1 else 'APPROXIMATE'}")

    # Refined F including bulk
    # Total F = F_boundary + integral of w(r)*F(r)*dr / integral of w(r)*dr
    # (schematic — the exact combination depends on the normalization)
    F_refined = F_boundary + (F_bulk_avg - F_boundary) * 0.1  # rough estimate
    print(f"\n  F_boundary:     {F_boundary:.8f}")
    print(f"  F_bulk_avg:     {F_bulk_avg:.8f}")
    print(f"  F_refined est.: {F_refined:.8f}  (boundary + 10% bulk correction)")

    csv_path = os.path.join(OUT_DIR, 'BST_PartitionFunction_BulkCorrection.csv')
    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['r','R_eff','bergman_weight','lnZ','F'])
        writer.writeheader(); writer.writerows(rows)
    print(f"  -> {csv_path}")

    return rows, lnZ_boundary, F_boundary, lnZ_bulk_avg, F_bulk_avg


# ============================================================================
# Main
# ============================================================================

if __name__ == '__main__':
    t_start = time()
    print("=" * 65)
    print("BST PARTITION FUNCTION: EXTENDED COMPUTATION")
    print("Casey Koons & Claude (Anthropic), March 2026")
    print("=" * 65)

    # Sanity check: reproduce Opus result
    lnZ_check = ln_Z_total(50.0, 20, 8, N_max=137)
    print(f"\nSanity check: Opus result at (l=20,m=8,beta=50):")
    print(f"  lnZ = {lnZ_check:.4f}  (expect ~4.93 = ln(138))")
    print(f"  F   = {-lnZ_check/50:.6f}  (expect ~-0.099)")

    lnZ_qft_check = ln_Z_qft(20, 8)
    print(f"  QFT E_vac = {lnZ_qft_check:.2f}  (expect ~3e6)")

    # Run tasks
    conv_rows = task1_convergence()

    thermo_rows, Tc, Cv_max = task2_thermodynamics(l_max=25, m_max=10, N_max=137)

    nmax_rows = task3_nmax(l_max=20, m_max=8)

    lambda_rows = task4_lambda(conv_rows, thermo_rows)

    bulk_rows, lnZ_bnd, F_bnd, lnZ_blk, F_blk = task5_bulk(
        l_max=15, m_max=8, N_max=137, N_r=25)

    # ----------------------------------------------------------------
    # Summary
    # ----------------------------------------------------------------
    elapsed = time() - t_start
    print("\n" + "=" * 65)
    print("SUMMARY OF KEY RESULTS")
    print("=" * 65)

    low_T = thermo_rows[-1]
    print(f"\n  Vacuum free energy F(T->0):     {low_T['F']:.6f}  BST natural units")
    print(f"  Ground state lnZ(T->0):         {low_T['lnZ']:.6f}  (expect ln(138) = {np.log(138):.6f})")
    print(f"  Phase transition T_c:           {Tc:.4f}  BST natural units")
    print(f"  C_v at transition:              {Cv_max:.4f}")
    print(f"  Bulk/boundary lnZ ratio:        {lnZ_blk/lnZ_bnd:.6f}  (1 = same as boundary)")

    # N_max=137 T_c
    r137 = next((r for r in nmax_rows if r['N_max'] == 137), None)
    if r137:
        print(f"  T_c for N_max=137:              {r137['T_c']:.4f}")
        print(f"  T_c monotonic with N_max:       {all(nmax_rows[i]['T_c'] <= nmax_rows[i+1]['T_c'] for i in range(len(nmax_rows)-1))}")

    scale4 = 10**(4 * -30.75)
    F_final = abs(low_T['F'])
    Lambda_refined = F_final * scale4
    print(f"\n  Lambda estimate (using converged F = {F_final:.5f}):")
    print(f"    Lambda ~ {Lambda_refined:.3e} Planck units")
    print(f"    log10(Lambda) = {np.log10(Lambda_refined):.2f}")
    print(f"    Observed: 2.9e-122  (log10 = -121.54)")
    print(f"    Gap: {np.log10(Lambda_refined) - np.log10(2.9e-122):.2f} orders of magnitude")

    print(f"\n  Total runtime: {elapsed:.1f}s")
    print(f"  Output files in: {OUT_DIR}")
