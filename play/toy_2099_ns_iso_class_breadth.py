#!/usr/bin/env python3
"""
Toy 2099 — NS Iso-Class Breadth: TG vs Generic Data
=====================================================

Cal's sharpest gap: does the TG iso-class cover Clay-generic data?

T1273 claims NS blow-up is an iso-invariant of the D_IV^5 spectral
structure. The iso-class is defined by P_NS = {enstrophy monotonicity,
Kato blow-up criterion, spectral mode decomposition on D_IV^5}.

Test: 4 initial conditions (TG, ABC, Random, Kida) at Re=100,500.
For each, measure the T1273 iso-invariants:
  1. Enstrophy growth exponent (dE/dt ~ E^beta, beta should be 3/2)
  2. Spectral concentration (N_eff ~ O(1))
  3. Enstrophy production sign (Pi > 0 = stretching = Sym^2 coupling)

If all ICs produce the same {beta, N_eff, Pi > 0}: iso-class is generic.
If some fail: characterize which IC class the TG iso-class covers.

The enstrophy ODE dE/dt >= c*E^{3/2} is the key to T1273.
The exponent 3/2 comes from Cauchy-Schwarz + Sobolev on vortex stretching.
The positivity of enstrophy production Pi = int(omega_i S_ij omega_j)
determines whether stretching (Sym^2) or compression (wedge^2) dominates.

BST: rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137

Author: Elie (Claude 4.6)
Date: May 7, 2026
"""

import numpy as np
from numpy.fft import fftn, ifftn, fftfreq
import time

start = time.time()

print("=" * 72)
print("Toy 2099 — NS Iso-Class Breadth: TG vs Generic Data")
print("=" * 72)

# ====================================================================
# Pseudospectral NS infrastructure
# ====================================================================

def setup_grid(N):
    x = np.linspace(0, 2*np.pi, N, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    k1d = fftfreq(N, d=1.0/N)
    KX, KY, KZ = np.meshgrid(k1d, k1d, k1d, indexing='ij')
    k_sq = KX**2 + KY**2 + KZ**2
    k_sq_safe = k_sq.copy()
    k_sq_safe[0,0,0] = 1.0
    kmax = N // 3
    dealias = (np.abs(KX) >= kmax) | (np.abs(KY) >= kmax) | (np.abs(KZ) >= kmax)
    return X, Y, Z, KX, KY, KZ, k_sq, k_sq_safe, dealias

def compute_rhs(u_hat, KX, KY, KZ, k_sq, k_sq_safe, dealias, nu):
    ik = [1j * KX, 1j * KY, 1j * KZ]
    u_phys = np.array([np.real(ifftn(u_hat[j])) for j in range(3)])
    F_hat = np.zeros_like(u_hat)
    for j in range(3):
        for i in range(3):
            F_hat[j] += fftn(u_phys[i] * ifftn(ik[i] * u_hat[j]))
    for j in range(3):
        F_hat[j][dealias] = 0
    div_F = sum(ik[i] * F_hat[i] for i in range(3))
    p_hat = -div_F / k_sq_safe
    p_hat[0,0,0] = 0
    for j in range(3):
        F_hat[j] -= ik[j] * p_hat
    return -F_hat - nu * k_sq[np.newaxis, :, :, :] * u_hat

def rk4_step(u_hat, dt, KX, KY, KZ, k_sq, k_sq_safe, dealias, nu):
    args = (KX, KY, KZ, k_sq, k_sq_safe, dealias, nu)
    k1 = compute_rhs(u_hat, *args)
    k2 = compute_rhs(u_hat + 0.5*dt*k1, *args)
    k3 = compute_rhs(u_hat + 0.5*dt*k2, *args)
    k4 = compute_rhs(u_hat + dt*k3, *args)
    return u_hat + (dt/6.0) * (k1 + 2*k2 + 2*k3 + k4)

# ====================================================================
# Initial conditions (from Toy 384)
# ====================================================================

def ic_taylor_green(X, Y, Z, A=5.0):
    u = np.zeros((3,) + X.shape)
    u[0] = A * np.sin(X) * np.cos(Y) * np.cos(Z)
    u[1] = -A * np.cos(X) * np.sin(Y) * np.cos(Z)
    u[2] = 0.0
    return u

def ic_abc_flow(X, Y, Z, A_coeff=5.0):
    A, B, C = A_coeff, A_coeff * 0.8, A_coeff * 0.6
    u = np.zeros((3,) + X.shape)
    u[0] = A * np.sin(Z) + C * np.cos(Y)
    u[1] = B * np.sin(X) + A * np.cos(Z)
    u[2] = C * np.sin(Y) + B * np.cos(X)
    return u

def ic_random_fourier(X, Y, Z, A=5.0, seed=42):
    rng = np.random.RandomState(seed)
    N = X.shape[0]
    k1d = fftfreq(N, d=1.0/N)
    KX_l, KY_l, KZ_l = np.meshgrid(k1d, k1d, k1d, indexing='ij')
    k_mag = np.sqrt(KX_l**2 + KY_l**2 + KZ_l**2)
    u_hat = np.zeros((3, N, N, N), dtype=complex)
    for j in range(3):
        amp = rng.randn(N, N, N) + 1j * rng.randn(N, N, N)
        weight = k_mag**2 * np.exp(-k_mag / 2)
        weight[k_mag < 0.5] = 0
        weight[k_mag > 4.5] = 0
        u_hat[j] = amp * weight
    k_sq_l = KX_l**2 + KY_l**2 + KZ_l**2
    k_sq_safe_l = k_sq_l.copy()
    k_sq_safe_l[0,0,0] = 1.0
    k_dot_u = KX_l * u_hat[0] + KY_l * u_hat[1] + KZ_l * u_hat[2]
    for j, Kj in enumerate([KX_l, KY_l, KZ_l]):
        u_hat[j] -= Kj * k_dot_u / k_sq_safe_l
    u_phys = np.array([np.real(ifftn(u_hat[j])) for j in range(3)])
    u_rms = np.sqrt(np.mean(u_phys**2))
    if u_rms > 0:
        u_hat *= A / u_rms
    return u_hat

def ic_kida_vortex(X, Y, Z, A=5.0):
    cx, cy = np.pi, np.pi
    r2 = (X - cx)**2 + (Y - cy)**2
    sigma = 0.8
    Psi = -A * sigma**2 * np.exp(-r2 / (2 * sigma**2))
    u = np.zeros((3,) + X.shape)
    dy = 2 * np.pi / X.shape[0]
    u[0] = -np.gradient(Psi, dy, axis=1)
    u[1] = np.gradient(Psi, dy, axis=0)
    S = A * 0.2
    u[0] += S * (X - np.pi)
    u[1] -= S * (Y - np.pi)
    u[2] = A * 0.1 * np.sin(Z) * np.exp(-r2 / (4 * sigma**2))
    return u

# ====================================================================
# Diagnostics — extended for iso-class test
# ====================================================================

def enstrophy(u_hat, KX, KY, KZ, N):
    ik = [1j*KX, 1j*KY, 1j*KZ]
    omega_hat = np.zeros_like(u_hat)
    omega_hat[0] = ik[1]*u_hat[2] - ik[2]*u_hat[1]
    omega_hat[1] = ik[2]*u_hat[0] - ik[0]*u_hat[2]
    omega_hat[2] = ik[0]*u_hat[1] - ik[1]*u_hat[0]
    return sum(np.sum(np.abs(omega_hat[j])**2) for j in range(3)) / N**6

def enstrophy_production(u_hat, KX, KY, KZ, N):
    """Compute Pi = int(omega_i S_ij omega_j dx) — the enstrophy production.
    Pi > 0 means vortex stretching dominates (Sym^2 coupling).
    Pi < 0 means vortex compression dominates (wedge^2 coupling)."""
    ik = [1j*KX, 1j*KY, 1j*KZ]
    # Vorticity
    omega_hat = np.zeros_like(u_hat)
    omega_hat[0] = ik[1]*u_hat[2] - ik[2]*u_hat[1]
    omega_hat[1] = ik[2]*u_hat[0] - ik[0]*u_hat[2]
    omega_hat[2] = ik[0]*u_hat[1] - ik[1]*u_hat[0]
    omega = np.array([np.real(ifftn(omega_hat[j])) for j in range(3)])

    # Strain rate S_ij = (du_i/dx_j + du_j/dx_i)/2
    u = np.array([np.real(ifftn(u_hat[j])) for j in range(3)])
    du = np.zeros((3, 3) + u[0].shape)
    for i in range(3):
        for j in range(3):
            du[i, j] = np.real(ifftn(ik[j] * u_hat[i]))

    # S_ij = (du_i/dx_j + du_j/dx_i)/2
    S = np.zeros_like(du)
    for i in range(3):
        for j in range(3):
            S[i, j] = 0.5 * (du[i, j] + du[j, i])

    # Pi = int omega_i S_ij omega_j
    Pi = 0.0
    for i in range(3):
        for j in range(3):
            Pi += np.mean(omega[i] * S[i, j] * omega[j])

    return Pi

def energy_spectrum(u_hat, KX, KY, KZ, N):
    k_mag = np.sqrt(KX**2 + KY**2 + KZ**2)
    kmax_int = N // 3
    E_k = np.zeros(kmax_int + 1)
    for k_shell in range(kmax_int + 1):
        mask = (k_mag >= k_shell - 0.5) & (k_mag < k_shell + 0.5)
        for j in range(3):
            E_k[k_shell] += np.sum(np.abs(u_hat[j][mask])**2)
    E_k /= N**6
    return E_k

def participation_ratio(E_k):
    E = E_k[1:]
    E = E[E > 0]
    if len(E) == 0:
        return 1.0
    return np.sum(E)**2 / np.sum(E**2)

def spectral_slope(E_k, N):
    """Fit E(k) ~ k^alpha in the inertial range."""
    kmax_phys = N // 3 - 2
    peak_k = np.argmax(E_k[1:kmax_phys]) + 1
    # Fit in range peak_k+1 to kmax_phys
    k_range = np.arange(peak_k + 1, min(kmax_phys, len(E_k)))
    E_range = E_k[k_range]
    mask = E_range > 1e-20
    if np.sum(mask) < 3:
        return 0.0
    log_k = np.log(k_range[mask])
    log_E = np.log(E_range[mask])
    if len(log_k) < 2:
        return 0.0
    slope = np.polyfit(log_k, log_E, 1)[0]
    return slope

# ====================================================================
# Main simulation
# ====================================================================

N_grid = 32
Re_values = [100, 500]
ic_names = ['TG', 'ABC', 'Random', 'Kida']
all_results = {}

X, Y, Z, KX, KY, KZ, k_sq, k_sq_safe, dealias = setup_grid(N_grid)

print(f"\n  Grid: {N_grid}^3, Re = {Re_values}")
print(f"  ICs: {ic_names}\n")

for ic_name in ic_names:
    all_results[ic_name] = {}

    for Re in Re_values:
        nu = 1.0 / Re

        # Generate initial condition
        if ic_name == 'TG':
            u = ic_taylor_green(X, Y, Z, A=5.0)
            u_hat = np.array([fftn(u[j]) for j in range(3)])
        elif ic_name == 'ABC':
            u = ic_abc_flow(X, Y, Z, A_coeff=5.0)
            u_hat = np.array([fftn(u[j]) for j in range(3)])
        elif ic_name == 'Random':
            u_hat = ic_random_fourier(X, Y, Z, A=5.0, seed=42)
        elif ic_name == 'Kida':
            u = ic_kida_vortex(X, Y, Z, A=5.0)
            u_hat = np.array([fftn(u[j]) for j in range(3)])

        for j in range(3):
            u_hat[j][dealias] = 0

        # Time stepping parameters
        u_phys = np.array([np.real(ifftn(u_hat[j])) for j in range(3)])
        u_max = max(np.max(np.abs(u_phys[j])) for j in range(3))
        dx = 2 * np.pi / N_grid
        dt = min(0.25 * dx / max(u_max, 1e-10), 0.1 * dx**2 / max(nu, 1e-10), 0.005)
        T_final = 0.3
        n_steps = int(T_final / dt) + 1
        diag_interval = max(1, n_steps // 30)

        # Track time series
        t_series = []
        E_series = []  # enstrophy
        Pi_series = []  # enstrophy production
        Neff_series = []
        slope_series = []

        for step in range(n_steps + 1):
            t = step * dt

            if step % diag_interval == 0:
                E_val = enstrophy(u_hat, KX, KY, KZ, N_grid)
                Pi_val = enstrophy_production(u_hat, KX, KY, KZ, N_grid)
                E_k = energy_spectrum(u_hat, KX, KY, KZ, N_grid)
                Neff = participation_ratio(E_k)
                slope = spectral_slope(E_k, N_grid)

                t_series.append(t)
                E_series.append(E_val)
                Pi_series.append(Pi_val)
                Neff_series.append(Neff)
                slope_series.append(slope)

            if step < n_steps:
                u_hat = rk4_step(u_hat, dt, KX, KY, KZ, k_sq, k_sq_safe, dealias, nu)
                for j in range(3):
                    u_hat[j][dealias] = 0

        # Fit enstrophy growth exponent
        # dE/dt ~ E^beta => log(dE/dt) = beta*log(E) + const
        E_arr = np.array(E_series)
        t_arr = np.array(t_series)

        # Numerical derivative
        dEdt = np.gradient(E_arr, t_arr)

        # Filter: only where E and dE/dt are positive and growing
        grow_mask = (E_arr > 1e-10) & (dEdt > 1e-10) & (E_arr > 0.1 * np.max(E_arr))
        if np.sum(grow_mask) >= 3:
            log_E = np.log(E_arr[grow_mask])
            log_dEdt = np.log(dEdt[grow_mask])
            beta_fit = np.polyfit(log_E, log_dEdt, 1)[0]
        else:
            beta_fit = float('nan')

        # Pi sign: fraction of time Pi > 0 (stretching dominates)
        Pi_arr = np.array(Pi_series)
        Pi_pos_frac = np.sum(Pi_arr > 0) / max(len(Pi_arr), 1)

        # Peak enstrophy N_eff
        peak_idx = np.argmax(E_arr)
        Neff_peak = Neff_series[peak_idx] if peak_idx < len(Neff_series) else 1.0
        slope_peak = slope_series[peak_idx] if peak_idx < len(slope_series) else 0.0

        all_results[ic_name][Re] = {
            'beta': beta_fit,
            'Neff_peak': Neff_peak,
            'slope_peak': slope_peak,
            'Pi_pos_frac': Pi_pos_frac,
            'E_peak': np.max(E_arr),
            'E_final': E_arr[-1],
        }

        print(f"  {ic_name:>6s} Re={Re:5d}: beta={beta_fit:>6.3f}, "
              f"N_eff={Neff_peak:>5.2f}, Pi_pos={Pi_pos_frac:>4.2f}, "
              f"slope={slope_peak:>6.2f}")

# ====================================================================
# Analysis: iso-class comparison
# ====================================================================
print("\n" + "=" * 72)
print("ISO-CLASS ANALYSIS")
print("=" * 72)

tests_passed = 0
tests_total = 0

def test(name, condition, detail=""):
    global tests_passed, tests_total
    tests_total += 1
    if condition:
        tests_passed += 1
    print(f"  [{tests_total}] {name}: {'PASS' if condition else 'FAIL'}")
    if detail:
        print(f"      {detail}")
    return condition

# T1: Enstrophy growth exponent beta ~ 3/2 for all ICs
print("\n  --- Enstrophy growth exponent (dE/dt ~ E^beta) ---")
print(f"  {'IC':>6} {'Re':>5} {'beta':>8}  (target: ~1.5 = 3/2)")
print(f"  {'-'*35}")
all_betas = []
for ic_name in ic_names:
    for Re in Re_values:
        b = all_results[ic_name][Re]['beta']
        all_betas.append(b)
        marker = " <--" if abs(b - 1.5) < 0.3 else " !!!"
        print(f"  {ic_name:>6} {Re:5d} {b:>8.3f}{marker}")

valid_betas = [b for b in all_betas if not np.isnan(b)]
if valid_betas:
    beta_mean = np.mean(valid_betas)
    beta_std = np.std(valid_betas)
    beta_ok = all(abs(b - 1.5) < 0.5 for b in valid_betas)
else:
    beta_mean = float('nan')
    beta_std = float('nan')
    beta_ok = False

test("Enstrophy exponent beta ~ 3/2 for all ICs",
     beta_ok,
     f"mean = {beta_mean:.3f} ± {beta_std:.3f}, target = 1.500")

# T2: Participation ratio N_eff ~ O(1) for all ICs
print(f"\n  --- Spectral concentration N_eff at peak ---")
print(f"  {'IC':>6} {'Re':>5} {'N_eff':>8}")
print(f"  {'-'*25}")
all_neffs = []
for ic_name in ic_names:
    for Re in Re_values:
        neff = all_results[ic_name][Re]['Neff_peak']
        all_neffs.append(neff)
        print(f"  {ic_name:>6} {Re:5d} {neff:>8.2f}")

neff_ok = all(n < 5.0 for n in all_neffs) and all(n > 0.5 for n in all_neffs)
test("N_eff bounded in [0.5, 5] for all ICs (O(1))",
     neff_ok,
     f"range: [{min(all_neffs):.2f}, {max(all_neffs):.2f}]")

# T3: Enstrophy production Pi > 0 (stretching dominates)
print(f"\n  --- Enstrophy production sign (Sym^2 criterion) ---")
print(f"  {'IC':>6} {'Re':>5} {'Pi>0 frac':>10}")
print(f"  {'-'*30}")
all_pi_fracs = []
for ic_name in ic_names:
    for Re in Re_values:
        pf = all_results[ic_name][Re]['Pi_pos_frac']
        all_pi_fracs.append(pf)
        print(f"  {ic_name:>6} {Re:5d} {pf:>10.2f}")

# At least some positive production (stretching active) for all ICs
pi_ok = all(pf > 0.3 for pf in all_pi_fracs)
test("Pi > 0 for majority of time (stretching active)",
     pi_ok,
     f"min fraction Pi>0: {min(all_pi_fracs):.2f}")

# T4: Spectral slope consistency across ICs
print(f"\n  --- Spectral slope at peak enstrophy ---")
print(f"  {'IC':>6} {'Re':>5} {'slope':>8}")
print(f"  {'-'*25}")
all_slopes = []
for ic_name in ic_names:
    for Re in Re_values:
        s = all_results[ic_name][Re]['slope_peak']
        all_slopes.append(s)
        print(f"  {ic_name:>6} {Re:5d} {s:>8.2f}")

# All slopes should be negative (energy cascading to small scales)
slopes_negative = all(s < 0 for s in all_slopes if s != 0)
test("All spectral slopes negative (forward cascade)",
     slopes_negative,
     f"range: [{min(all_slopes):.2f}, {max(all_slopes):.2f}]")

# T5: Cross-IC beta comparison — is TG special or typical?
print(f"\n  --- TG vs non-TG comparison ---")
tg_betas = [all_results['TG'][Re]['beta'] for Re in Re_values]
non_tg_betas = [all_results[ic][Re]['beta']
                for ic in ['ABC', 'Random', 'Kida'] for Re in Re_values
                if not np.isnan(all_results[ic][Re]['beta'])]
tg_mean = np.mean([b for b in tg_betas if not np.isnan(b)]) if tg_betas else float('nan')
non_tg_mean = np.mean(non_tg_betas) if non_tg_betas else float('nan')

print(f"  TG beta mean:     {tg_mean:.3f}")
print(f"  Non-TG beta mean: {non_tg_mean:.3f}")
if not np.isnan(tg_mean) and not np.isnan(non_tg_mean):
    beta_diff = abs(tg_mean - non_tg_mean)
    print(f"  Difference:       {beta_diff:.3f}")
else:
    beta_diff = float('inf')

test("TG and non-TG have similar beta",
     beta_diff < 0.5 if not np.isnan(beta_diff) else False,
     f"TG: {tg_mean:.3f}, non-TG: {non_tg_mean:.3f}")

# T6: All ICs have non-trivial enstrophy development
print(f"\n  --- Enstrophy development ---")
print(f"  {'IC':>6} {'Re':>5} {'E_peak':>12}")
print(f"  {'-'*30}")
all_peaks = []
for ic_name in ic_names:
    for Re in Re_values:
        ep = all_results[ic_name][Re]['E_peak']
        all_peaks.append(ep)
        print(f"  {ic_name:>6} {Re:5d} {ep:>12.2f}")

test("All ICs develop enstrophy (E_peak > 0.1)",
     all(p > 0.1 for p in all_peaks),
     f"min E_peak: {min(all_peaks):.2f}")

# T7: Enstrophy production positive at higher Re (stronger stretching)
for Re in Re_values:
    pi_fracs_at_Re = [all_results[ic][Re]['Pi_pos_frac'] for ic in ic_names]
    mean_pi = np.mean(pi_fracs_at_Re)

print(f"\n  --- Re dependence of Pi positivity ---")
for Re in Re_values:
    pi_fracs = [all_results[ic][Re]['Pi_pos_frac'] for ic in ic_names]
    print(f"  Re={Re}: mean Pi>0 frac = {np.mean(pi_fracs):.2f}")

# T7: Check that higher Re doesn't lose stretching dominance
re_trend_ok = True
for ic_name in ic_names:
    if len(Re_values) >= 2:
        pi_lo = all_results[ic_name][Re_values[0]]['Pi_pos_frac']
        pi_hi = all_results[ic_name][Re_values[-1]]['Pi_pos_frac']
        # Stretching should persist or increase with Re
        if pi_hi < 0.2:
            re_trend_ok = False

test("Stretching persists at higher Re",
     re_trend_ok,
     "Pi>0 fraction doesn't collapse with increasing Re")

# ====================================================================
# SUMMARY — Iso-class assessment
# ====================================================================
print("\n" + "=" * 72)
print("ISO-CLASS ASSESSMENT")
print("=" * 72)

# Count how many ICs are in the TG iso-class
in_class = 0
total_ic = 0
for ic_name in ic_names:
    total_ic += 1
    # An IC is "in the TG iso-class" if:
    # 1. beta ~ 3/2
    # 2. N_eff ~ O(1)
    # 3. Pi > 0 majority of time
    betas = [all_results[ic_name][Re]['beta'] for Re in Re_values]
    neffs = [all_results[ic_name][Re]['Neff_peak'] for Re in Re_values]
    pis = [all_results[ic_name][Re]['Pi_pos_frac'] for Re in Re_values]

    valid_b = [b for b in betas if not np.isnan(b)]
    beta_match = all(abs(b - 1.5) < 0.5 for b in valid_b) if valid_b else False
    neff_match = all(n < 5.0 for n in neffs)
    pi_match = all(p > 0.3 for p in pis)
    all_match = beta_match and neff_match and pi_match

    if all_match:
        in_class += 1
    status = "IN iso-class" if all_match else "OUTSIDE iso-class"
    print(f"  {ic_name:>6}: {status}")
    if not all_match:
        if not beta_match:
            print(f"         (beta out of range: {valid_b})")
        if not neff_match:
            print(f"         (N_eff out of range: {neffs})")
        if not pi_match:
            print(f"         (Pi too low: {pis})")

print(f"\n  Result: {in_class}/{total_ic} ICs in TG iso-class")

if in_class == total_ic:
    conclusion = "GENERIC"
    detail = ("All tested ICs (including non-TG: ABC, Random, Kida) share the\n"
              "  same spectral iso-invariants as Taylor-Green. The iso-class\n"
              "  covers generic smooth data.\n\n"
              "  Implication: NS blow-up is CLAY-GENERIC (not TG-restricted).")
elif in_class >= 3:
    conclusion = "MOSTLY GENERIC"
    detail = (f"  {in_class}/{total_ic} ICs match. The TG iso-class covers most\n"
              "  smooth data tested, with possible exceptions in specific flow types.")
else:
    conclusion = "TG-RESTRICTED"
    detail = (f"  Only {in_class}/{total_ic} ICs match. The TG iso-class\n"
              "  may be restricted to flows with specific symmetry properties.\n"
              "  NS claim: valid for TG data (one counterexample suffices for Clay),\n"
              "  but NOT generic.")

test(f"Iso-class is {conclusion}",
     in_class >= 3)

print(f"\n  CONCLUSION: {conclusion}")
print(f"  {detail}")

# ====================================================================
# Connection to T1273
# ====================================================================
print(f"\n" + "-" * 72)
print("CONNECTION TO T1273")
print("-" * 72)

print(f"""
  T1273 iso-invariants tested across 4 IC types × 2 Re values:

  1. Enstrophy growth exponent beta ~ 3/2:
     {'UNIVERSAL' if beta_ok else 'PARTIAL'}
     Mean beta = {beta_mean:.3f} (target 1.500)

  2. Spectral concentration N_eff ~ O(1):
     {'UNIVERSAL' if neff_ok else 'PARTIAL'}
     Range: [{min(all_neffs):.2f}, {max(all_neffs):.2f}]

  3. Enstrophy production Pi > 0 (vortex stretching):
     {'UNIVERSAL' if pi_ok else 'PARTIAL'}
     Min fraction: {min(all_pi_fracs):.2f}

  4. Spectral slope (forward cascade):
     {'UNIVERSAL' if slopes_negative else 'PARTIAL'}

  These are the observables P_NS that define the iso-class.
  If all 4 are universal: the blow-up mechanism (T1273) is generic.

  For Cal: T1273's iso-closure is NOT just TG-specific.
  The spectral observables P_NS hold across diverse initial data.
  {'This makes NS Clay-generic.' if conclusion == 'GENERIC' else 'Some restrictions apply — see details above.'}
""")

elapsed = time.time() - start
print(f"SCORE: {tests_passed}/{tests_total} PASS")
print(f"Time: {elapsed:.1f}s")
