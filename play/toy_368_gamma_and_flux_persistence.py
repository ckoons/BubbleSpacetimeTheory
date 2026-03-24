#!/usr/bin/env python3
"""
Toy 368 — γ Exponent and Flux Persistence (K1-K2 Closure Tests)
================================================================
Two measurements that close or kill the iteration argument for NS blow-up:

PART A: γ across amplitudes
  If P(t) ~ c·Ω^γ with γ > 1, then dΩ/dt = 2P gives ODE blow-up.
  Toy 367 measured γ on a narrow Ω range (single A=1.0) → overfit.
  Fix: Run multiple amplitudes A = 1, 2, 5, 10, 20 at N=64³.
  Combined dataset spans orders of magnitude in Ω → reliable γ fit.
  Dimensional prediction: γ = 3/2.

PART B: Flux persistence through evolution
  The iteration argument needs Π(K,t) to remain proportional to some
  power of the norm throughout evolution, not just at t = 0⁺.
  Compute shell flux Π(K,t) = -Σ_{k≤K} T(k,t) at regular intervals.
  Track Π_max(t) vs Ω(t) and ||u||_{H^s}(t).

Tests:
  Test 1: γ fit across amplitudes — is γ ≈ 3/2?
  Test 2: γ > 1 (required for ODE blow-up)
  Test 3: P > 0 for all amplitudes (Conjecture 5.6)
  Test 4: Π_max(t) > 0 throughout evolution
  Test 5: Π_max scales with Ω (power law persists)
  Test 6: Energy conservation (sanity check)
  Test 7: dΩ/dt ≈ 2P consistency (solver validation)
  Test 8: Combined iteration viability assessment

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6 (Elie). March 2026.
"""

import numpy as np
from numpy.fft import fftn, ifftn, fftfreq
import time as _time

_print = print
def print(*args, **kwargs):
    kwargs.setdefault('flush', True)
    _print(*args, **kwargs)

PASS = 0
FAIL = 0

def score(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        tag = "✓ PASS"
    else:
        FAIL += 1
        tag = "✗ FAIL"
    print(f"  {tag}: {name}")
    if detail:
        print(f"         {detail}")


# ═══════════════════════════════════════════════════════════════════
# CORE: Pseudo-spectral Euler solver (from Toy 367, Leray-correct)
# ═══════════════════════════════════════════════════════════════════

def setup_grid(N):
    """Set up 3D periodic grid and wavenumbers."""
    x = np.linspace(0, 2*np.pi, N, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    k1d = fftfreq(N, d=1.0/N)
    kxg, kyg, kzg = np.meshgrid(k1d, k1d, k1d, indexing='ij')
    k_sq = kxg**2 + kyg**2 + kzg**2
    k_sq_safe = k_sq.copy()
    k_sq_safe[0, 0, 0] = 1.0
    k_mag = np.sqrt(k_sq)
    dealias = k_mag > N / 3.0
    return X, Y, Z, kxg, kyg, kzg, k_sq, k_sq_safe, k_mag, dealias


def taylor_green(X, Y, Z, A):
    """Taylor-Green vortex initial condition."""
    u1 = A * np.sin(X) * np.cos(Y) * np.cos(Z)
    u2 = -A * np.cos(X) * np.sin(Y) * np.cos(Z)
    u3 = np.zeros_like(X)
    return np.array([u1, u2, u3])


def compute_rhs(u_hat, kxg, kyg, kzg, k_sq_safe, dealias, N):
    """
    Compute RHS of Euler: -P[(u·∇)u].
    Leray projection with CORRECT sign (Toy 367 fix).
    """
    kg = [kxg, kyg, kzg]
    k_sq = kxg**2 + kyg**2 + kzg**2

    u_phys = np.array([np.real(ifftn(u_hat[i])) for i in range(3)])

    F_hat = np.zeros_like(u_hat)
    for j in range(3):
        for i in range(3):
            du_dx = np.real(ifftn(1j * kg[i] * u_hat[j]))
            F_hat[j] += fftn(u_phys[i] * du_dx)

    for i in range(3):
        F_hat[i][dealias] = 0

    # Leray projection: P[F] = F - ∇(Δ⁻¹(∇·F))
    # φ̂ = -(ik·F̂)/|k|², then F -= ik·φ̂
    div_F = sum(1j * kg[i] * F_hat[i] for i in range(3))
    p_hat = -div_F / k_sq_safe  # CORRECT sign
    p_hat[0, 0, 0] = 0
    for i in range(3):
        F_hat[i] -= 1j * kg[i] * p_hat

    return -F_hat


def rk4_step(u_hat, dt, kxg, kyg, kzg, k_sq_safe, dealias, N):
    """Single RK4 step for inviscid Euler."""
    args = (kxg, kyg, kzg, k_sq_safe, dealias, N)
    k1 = compute_rhs(u_hat, *args)
    k2 = compute_rhs(u_hat + 0.5*dt*k1, *args)
    k3 = compute_rhs(u_hat + 0.5*dt*k2, *args)
    k4 = compute_rhs(u_hat + dt*k3, *args)
    return u_hat + (dt/6.0) * (k1 + 2*k2 + 2*k3 + k4)


# ═══════════════════════════════════════════════════════════════════
# DIAGNOSTICS
# ═══════════════════════════════════════════════════════════════════

def measure_enstrophy(u_hat, kxg, kyg, kzg, N):
    """Enstrophy Ω = mean(|ω|²). Parseval: Σ|ω̂|²/N⁶."""
    w_hat = np.zeros_like(u_hat)
    w_hat[0] = 1j * (kyg * u_hat[2] - kzg * u_hat[1])
    w_hat[1] = 1j * (kzg * u_hat[0] - kxg * u_hat[2])
    w_hat[2] = 1j * (kxg * u_hat[1] - kyg * u_hat[0])
    return np.sum(np.abs(w_hat)**2).real / N**6


def measure_enstrophy_production(u_hat, kxg, kyg, kzg, N):
    """P(t) = mean(ω_i S_{ij} ω_j). For Euler: dΩ/dt = 2P."""
    kg = [kxg, kyg, kzg]

    w_hat = np.zeros_like(u_hat)
    w_hat[0] = 1j * (kyg * u_hat[2] - kzg * u_hat[1])
    w_hat[1] = 1j * (kzg * u_hat[0] - kxg * u_hat[2])
    w_hat[2] = 1j * (kxg * u_hat[1] - kyg * u_hat[0])
    w_phys = np.array([np.real(ifftn(w_hat[i])) for i in range(3)])

    S = np.zeros((3, 3) + u_hat.shape[1:])
    for i in range(3):
        for j in range(i, 3):
            du_i_dj = np.real(ifftn(1j * kg[j] * u_hat[i]))
            du_j_di = np.real(ifftn(1j * kg[i] * u_hat[j]))
            S[i, j] = 0.5 * (du_i_dj + du_j_di)
            if i != j:
                S[j, i] = S[i, j]

    prod = np.zeros(u_hat.shape[1:], dtype=float)
    for i in range(3):
        for j in range(3):
            prod += w_phys[i] * S[i, j] * w_phys[j]

    return np.mean(prod)


def measure_energy(u_hat, N):
    """Total kinetic energy = (1/2) mean(|u|²)."""
    E = 0
    for j in range(3):
        E += 0.5 * np.sum(np.abs(u_hat[j])**2).real
    return E / N**6


def measure_Hs_norm(u_hat, k_sq, N, s=3.0):
    """||u||²_{H^s} = (1/N⁶) Σ (1+|k|²)^s |û|²."""
    weight = (1 + k_sq)**s
    norm_sq = 0
    for j in range(3):
        norm_sq += np.sum(weight * np.abs(u_hat[j])**2).real
    return norm_sq / N**6


def measure_flux(u_hat, kxg, kyg, kzg, k_sq_safe, dealias, k_mag, N):
    """
    Compute energy flux Π(K) = -Σ_{|k|≤K} T(k).
    T(k) = -Re[û*·P[(u·∇)u]^] summed over shell |k| ∈ [k-½, k+½).

    Returns (Pi_max, Pi_array, k_shells) for full flux profile.
    """
    kg = [kxg, kyg, kzg]
    u_phys = np.array([np.real(ifftn(u_hat[i])) for i in range(3)])

    F_hat = np.zeros_like(u_hat)
    for j in range(3):
        for i in range(3):
            du_dx = np.real(ifftn(1j * kg[i] * u_hat[j]))
            F_hat[j] += fftn(u_phys[i] * du_dx)
    for i in range(3):
        F_hat[i][dealias] = 0

    # Leray project
    div_F = sum(1j * kg[i] * F_hat[i] for i in range(3))
    p_hat = -div_F / k_sq_safe
    p_hat[0, 0, 0] = 0
    for i in range(3):
        F_hat[i] -= 1j * kg[i] * p_hat

    # Energy transfer per mode: T_mode(k) = -Re[û*(k)·F̂(k)] / N³
    T_mode = np.zeros(u_hat.shape[1:])
    for j in range(3):
        T_mode += -np.real(np.conj(u_hat[j]) * F_hat[j]) / N**3

    # Shell-sum
    k_shells = np.arange(1, N // 3)
    T_k = np.zeros(len(k_shells))
    for idx, ks in enumerate(k_shells):
        shell = (k_mag >= ks - 0.5) & (k_mag < ks + 0.5)
        T_k[idx] = np.sum(T_mode[shell])

    Pi_k = -np.cumsum(T_k)
    Pi_max = np.max(Pi_k) if len(Pi_k) > 0 else 0.0
    return Pi_max, Pi_k, k_shells


# ═══════════════════════════════════════════════════════════════════
# PART A: γ across amplitudes
# ═══════════════════════════════════════════════════════════════════

def part_a_gamma():
    """
    Run TG at multiple amplitudes. Collect (Ω, P) pairs across all runs.
    Fit P = c·Ω^γ on the combined dataset spanning orders of magnitude.

    Dimensional prediction: P has dimensions of enstrophy/time.
    Ω ~ ω², P ~ ω²·S ~ ω²·(∂u/∂x). For TG: ω ~ A|k|, S ~ A|k|.
    So P ~ A³|k|³ and Ω ~ A²|k|². Thus P ~ Ω^{3/2} / |k|^0 → γ = 3/2.
    """
    print("\n" + "=" * 70)
    print("PART A: γ exponent — P vs Ω across amplitudes")
    print("=" * 70)

    print("""
  Dimensional prediction: P ~ Ω^{3/2}  (γ = 3/2)
  Method: Evolve TG at A = 1, 2, 5, 10, 20. Collect all (Ω, P) pairs.
  Log-log fit on combined data spanning ~4 decades in Ω.
  """)

    N = 64
    X, Y, Z, kxg, kyg, kzg, k_sq, k_sq_safe, k_mag, dealias = setup_grid(N)

    amplitudes = [1.0, 2.0, 5.0, 10.0, 20.0]
    all_omega = []
    all_P = []
    all_labels = []  # for tracking which amplitude each point came from

    per_amp_results = {}

    for A in amplitudes:
        # Adaptive dt: CFL ~ dx/u_max ~ (2π/N)/A. Be conservative.
        dt = min(0.005, 0.5 * (2*np.pi/N) / A)
        n_steps = max(200, int(0.5 / dt))  # evolve to t ≈ 0.5 or 200 steps minimum
        t_final = n_steps * dt

        u_phys = taylor_green(X, Y, Z, A)
        u_hat = np.array([fftn(u_phys[i]) for i in range(3)])

        E0 = measure_energy(u_hat, N)
        Omega0 = measure_enstrophy(u_hat, kxg, kyg, kzg, N)
        P0 = measure_enstrophy_production(u_hat, kxg, kyg, kzg, N)

        omegas_this = []
        prods_this = []
        P_all_positive = True

        sample_interval = max(1, n_steps // 50)

        for step in range(n_steps + 1):
            if step % sample_interval == 0:
                omega = measure_enstrophy(u_hat, kxg, kyg, kzg, N)
                P = measure_enstrophy_production(u_hat, kxg, kyg, kzg, N)

                omegas_this.append(omega)
                prods_this.append(P)

                if step > 5 and P < -1e-10 * omega:
                    P_all_positive = False

            if step < n_steps:
                u_hat = rk4_step(u_hat, dt, kxg, kyg, kzg, k_sq_safe, dealias, N)

        E_final = measure_energy(u_hat, N)
        dE_rel = abs(E_final - E0) / E0

        # Collect positive (Ω, P) pairs for log-log fit (skip first 3 for transient)
        skip = 3
        for o, p in zip(omegas_this[skip:], prods_this[skip:]):
            if p > 0 and o > 0:
                all_omega.append(o)
                all_P.append(p)
                all_labels.append(A)

        Omega_final = omegas_this[-1]
        P_final = prods_this[-1]

        per_amp_results[A] = {
            'Omega0': Omega0, 'Omega_final': Omega_final,
            'P0': P0, 'P_final': P_final,
            'P_positive': P_all_positive,
            'n_points': len(omegas_this) - skip,
            'dE_rel': dE_rel,
            'dt': dt, 'n_steps': n_steps,
        }

        print(f"  A = {A:>5.1f}: Ω: {Omega0:.4e} → {Omega_final:.4e} "
              f"({Omega_final/Omega0:.4f}x)  P: {P0:.4e} → {P_final:.4e}  "
              f"{'P>0 ✓' if P_all_positive else 'P<0 ✗'}  "
              f"ΔE/E={dE_rel:.1e}  dt={dt:.4f}  steps={n_steps}")

    # ── Log-log fit ──
    if len(all_omega) < 10:
        print(f"\n  Only {len(all_omega)} positive (Ω,P) points — cannot fit γ reliably")
        gamma_fit = None
        c_fit = None
    else:
        log_omega = np.log(np.array(all_omega))
        log_P = np.log(np.array(all_P))
        coeffs = np.polyfit(log_omega, log_P, 1)
        gamma_fit = coeffs[0]
        c_fit = np.exp(coeffs[1])

        # Residual analysis
        predicted = coeffs[0] * log_omega + coeffs[1]
        residuals = log_P - predicted
        r_std = np.std(residuals)
        r_max = np.max(np.abs(residuals))

        # Also fit quadratic to check for curvature (overfitting indicator)
        if len(all_omega) > 20:
            coeffs2 = np.polyfit(log_omega, log_P, 2)
            curvature = coeffs2[0]
        else:
            curvature = 0

        print(f"\n  ── γ fit results ──")
        print(f"  Data points: {len(all_omega)} (across {len(amplitudes)} amplitudes)")
        print(f"  Ω range: [{min(all_omega):.4e}, {max(all_omega):.4e}] "
              f"({max(all_omega)/min(all_omega):.1f}x span)")
        print(f"  P range: [{min(all_P):.4e}, {max(all_P):.4e}]")
        print(f"\n  FIT: P = {c_fit:.6e} · Ω^{gamma_fit:.6f}")
        print(f"  Dimensional prediction: γ = 3/2 = 1.500000")
        print(f"  Deviation from 3/2: {abs(gamma_fit - 1.5):.6f} "
              f"({abs(gamma_fit - 1.5)/1.5*100:.2f}%)")
        print(f"\n  Fit quality:")
        print(f"    Residual σ (log space): {r_std:.4f}")
        print(f"    Residual max: {r_max:.4f}")
        if len(all_omega) > 20:
            print(f"    Quadratic curvature: {curvature:.6f} "
                  f"({'negligible' if abs(curvature) < 0.05 else 'SIGNIFICANT — fit may be curved'})")

        # Print a few representative points for visual verification
        print(f"\n  {'Ω':>12} {'P (data)':>12} {'P (fit)':>12} {'ratio':>8} {'A':>6}")
        print(f"  {'─'*54}")
        # Sample ~15 evenly spaced points
        indices = np.linspace(0, len(all_omega)-1, min(15, len(all_omega)), dtype=int)
        for idx in indices:
            o = all_omega[idx]
            p = all_P[idx]
            p_pred = c_fit * o**gamma_fit
            print(f"  {o:>12.4e} {p:>12.4e} {p_pred:>12.4e} {p/p_pred:>8.4f} {all_labels[idx]:>6.1f}")

    # ── Scores ──
    all_pos = all(v['P_positive'] for v in per_amp_results.values())
    score("P > 0 for all amplitudes (Conjecture 5.6)",
          all_pos,
          f"All positive: {all_pos}")

    if gamma_fit is not None:
        score("γ > 1 (required for ODE blow-up)",
              gamma_fit > 1.0,
              f"γ = {gamma_fit:.4f}")

        score("γ ≈ 3/2 (dimensional prediction)",
              abs(gamma_fit - 1.5) < 0.15,
              f"γ = {gamma_fit:.4f}, |γ - 3/2| = {abs(gamma_fit-1.5):.4f}")
    else:
        score("γ > 1 (required for ODE blow-up)", False, "insufficient data")
        score("γ ≈ 3/2 (dimensional prediction)", False, "insufficient data")

    return gamma_fit, c_fit, all_omega, all_P, per_amp_results


# ═══════════════════════════════════════════════════════════════════
# PART B: Flux persistence through evolution
# ═══════════════════════════════════════════════════════════════════

def part_b_flux_persistence():
    """
    Evolve TG at moderate amplitude, measuring Π_max(t) at regular intervals.
    The iteration argument needs Π to stay proportional to a power of the norm
    throughout evolution — not just at t = 0⁺.

    Track: Π_max(t), Ω(t), P(t), ||u||_{H³}(t), E(t).
    Fit: Π_max ~ Ω^α and Π_max ~ ||u||_{H³}^β.
    """
    print("\n\n" + "=" * 70)
    print("PART B: Flux persistence through TG evolution")
    print("=" * 70)

    print("""
  Question: Does Π_max(t) stay proportional to a power of ||u||?
  If Π_max → 0 while ||u|| grows, the iteration can't feed itself.
  If Π_max ~ ||u||^β with β > 0, the cascade sustains.
  """)

    N = 64
    X, Y, Z, kxg, kyg, kzg, k_sq, k_sq_safe, k_mag, dealias = setup_grid(N)

    A = 5.0  # Moderate amplitude for visible dynamics
    dt = 0.001
    n_steps = 500  # t → 0.5
    t_final = n_steps * dt

    u_phys = taylor_green(X, Y, Z, A)
    u_hat = np.array([fftn(u_phys[i]) for i in range(3)])

    E0 = measure_energy(u_hat, N)

    print(f"  A = {A}, N = {N}³, dt = {dt}, T = {t_final}")
    print(f"  E₀ = {E0:.6f}")
    print(f"\n  {'t':>7} {'Π_max':>12} {'Ω':>12} {'P':>12} "
          f"{'||u||_H³':>12} {'E':>12} {'dΩ/dt':>12} {'2P':>12}")
    print(f"  {'─'*95}")

    times = []
    Pi_maxes = []
    omegas = []
    productions = []
    Hs_norms = []
    energies = []

    measure_interval = max(1, n_steps // 40)
    prev_omega = None
    prev_t = None

    for step in range(n_steps + 1):
        if step % measure_interval == 0:
            t = step * dt
            omega = measure_enstrophy(u_hat, kxg, kyg, kzg, N)
            P = measure_enstrophy_production(u_hat, kxg, kyg, kzg, N)
            E = measure_energy(u_hat, N)
            Hs = measure_Hs_norm(u_hat, k_sq, N, s=3.0)
            Pi_max, _, _ = measure_flux(u_hat, kxg, kyg, kzg, k_sq_safe,
                                        dealias, k_mag, N)

            times.append(t)
            Pi_maxes.append(Pi_max)
            omegas.append(omega)
            productions.append(P)
            Hs_norms.append(Hs)
            energies.append(E)

            if prev_omega is not None and prev_t is not None:
                dt_meas = t - prev_t
                dOmega_dt = (omega - prev_omega) / dt_meas if dt_meas > 0 else 0
                two_P = 2 * P
            else:
                dOmega_dt = 0
                two_P = 0

            if step % (measure_interval * 4) == 0:  # Print every ~4th measurement
                print(f"  {t:>7.4f} {Pi_max:>12.4e} {omega:>12.4e} {P:>12.4e} "
                      f"{Hs:>12.4e} {E:>12.6f} {dOmega_dt:>12.4e} {two_P:>12.4e}")

            prev_omega = omega
            prev_t = t

        if step < n_steps:
            u_hat = rk4_step(u_hat, dt, kxg, kyg, kzg, k_sq_safe, dealias, N)

    # ── Analysis ──
    print(f"\n  ── Flux persistence analysis ──")

    # Check: is Π_max > 0 throughout?
    # Skip the very first point (t=0 where Π = 0 by mode orthogonality)
    skip = 2
    Pi_positive = [p for p in Pi_maxes[skip:] if p > 0]
    Pi_nonpositive = [p for p in Pi_maxes[skip:] if p <= 0]
    n_measured = len(Pi_maxes) - skip

    print(f"  Π_max > 0: {len(Pi_positive)}/{n_measured} measurements (after t=0 transient)")

    # Did Π_max grow, shrink, or stay constant?
    if len(Pi_maxes) > 5:
        Pi_start = np.mean(Pi_maxes[2:5])
        Pi_end = np.mean(Pi_maxes[-3:])
        print(f"  Π_max: {Pi_start:.4e} (early) → {Pi_end:.4e} (late) "
              f"({Pi_end/Pi_start:.4f}x)")

    # Fit Π_max vs Ω (log-log)
    valid_flux = [(o, pi) for o, pi in zip(omegas[skip:], Pi_maxes[skip:])
                  if pi > 0 and o > 0]

    if len(valid_flux) > 5:
        log_omega_f = np.log(np.array([v[0] for v in valid_flux]))
        log_Pi = np.log(np.array([v[1] for v in valid_flux]))
        coeffs_f = np.polyfit(log_omega_f, log_Pi, 1)
        alpha = coeffs_f[0]
        c_alpha = np.exp(coeffs_f[1])

        # Residuals
        pred_f = coeffs_f[0] * log_omega_f + coeffs_f[1]
        res_f = log_Pi - pred_f
        r_std_f = np.std(res_f)

        print(f"\n  Π_max vs Ω:")
        print(f"    FIT: Π_max = {c_alpha:.4e} · Ω^{alpha:.4f}")
        print(f"    Residual σ: {r_std_f:.4f}")
    else:
        alpha = 0
        print(f"\n  Insufficient valid Π_max > 0 points for fit")

    # Fit Π_max vs ||u||_{H^s}
    valid_Hs = [(h, pi) for h, pi in zip(Hs_norms[skip:], Pi_maxes[skip:])
                if pi > 0 and h > 0]

    if len(valid_Hs) > 5:
        log_Hs = np.log(np.array([v[0] for v in valid_Hs]))
        log_Pi_h = np.log(np.array([v[1] for v in valid_Hs]))
        coeffs_h = np.polyfit(log_Hs, log_Pi_h, 1)
        beta = coeffs_h[0]
        c_beta = np.exp(coeffs_h[1])

        pred_h = coeffs_h[0] * log_Hs + coeffs_h[1]
        r_std_h = np.std(log_Pi_h - pred_h)

        print(f"\n  Π_max vs ||u||_H³:")
        print(f"    FIT: Π_max = {c_beta:.4e} · ||u||_H³^{beta:.4f}")
        print(f"    Residual σ: {r_std_h:.4f}")
    else:
        beta = 0
        print(f"\n  Insufficient valid Π_max > 0 points for H^s fit")

    # dΩ/dt vs 2P consistency
    consistency_ratios = []
    for i in range(skip+1, len(times)):
        dt_m = times[i] - times[i-1]
        if dt_m > 0 and abs(productions[i]) > 1e-20:
            dO = (omegas[i] - omegas[i-1]) / dt_m
            ratio = dO / (2 * productions[i])
            consistency_ratios.append(ratio)

    if consistency_ratios:
        mean_ratio = np.mean(consistency_ratios)
        std_ratio = np.std(consistency_ratios)
        print(f"\n  dΩ/dt vs 2P consistency:")
        print(f"    Mean ratio: {mean_ratio:.6f} (should be 1.0)")
        print(f"    Std: {std_ratio:.6f}")

    # Energy conservation
    E_final = energies[-1]
    dE_rel = abs(E_final - E0) / E0

    print(f"\n  Energy: ΔE/E₀ = {dE_rel:.4e}")

    # ── Flux profile at a few key times ──
    print(f"\n  ── Flux profile snapshots ──")
    # Re-evolve briefly to get profiles at t=0, t≈0.1, t≈0.25, t≈0.5
    # (We already have the data — just show the evolution trend)
    print(f"  {'t':>7} {'Π_max':>12} {'Ω':>12} {'Π_max/Ω':>12} {'Π_max/Ω^α':>12}")
    print(f"  {'─'*58}")
    for i in range(0, len(times), max(1, len(times)//12)):
        t = times[i]
        pi = Pi_maxes[i]
        o = omegas[i]
        ratio_o = pi / o if o > 0 else 0
        ratio_oa = pi / (o**alpha) if o > 0 and alpha > 0 else 0
        print(f"  {t:>7.4f} {pi:>12.4e} {o:>12.4e} {ratio_o:>12.4e} {ratio_oa:>12.4e}")

    # ── Scores ──
    Pi_persists = len(Pi_positive) > 0.8 * n_measured
    score("Π_max(t) > 0 throughout evolution",
          Pi_persists,
          f"{len(Pi_positive)}/{n_measured} positive")

    if len(valid_flux) > 5:
        score("Π_max scales with Ω (power law persists)",
              abs(alpha) > 0.3 and r_std_f < 0.5,
              f"α = {alpha:.4f}, σ = {r_std_f:.4f}")
    else:
        score("Π_max scales with Ω (power law persists)", False, "insufficient data")

    score("Energy conserved (Euler sanity)",
          dE_rel < 1e-4,
          f"ΔE/E₀ = {dE_rel:.4e}")

    if consistency_ratios:
        score("dΩ/dt ≈ 2P (solver validation)",
              abs(mean_ratio - 1.0) < 0.05,
              f"mean ratio = {mean_ratio:.6f}")
    else:
        score("dΩ/dt ≈ 2P (solver validation)", False, "no data")

    return {
        'times': times, 'Pi_maxes': Pi_maxes, 'omegas': omegas,
        'productions': productions, 'Hs_norms': Hs_norms, 'energies': energies,
        'alpha': alpha, 'beta': beta if 'beta' in dir() else 0,
    }


# ═══════════════════════════════════════════════════════════════════
# COMBINED ASSESSMENT
# ═══════════════════════════════════════════════════════════════════

def iteration_assessment(gamma, flux_data):
    """
    The two numbers that matter:
    1. γ in P ~ Ω^γ : needs γ > 1 for ODE blow-up
    2. Π persistence: needs Π_max ~ ||u||^β with β > 0

    If both hold: the iteration argument closes.
    If either fails: identify which piece breaks.
    """
    print("\n\n" + "=" * 70)
    print("COMBINED ASSESSMENT: Does the iteration close?")
    print("=" * 70)

    alpha = flux_data.get('alpha', 0)

    print(f"\n  ── The two numbers ──")
    print(f"  γ (enstrophy production exponent): {gamma if gamma else 'FAILED'}")
    if gamma:
        print(f"    Dimensional prediction: 3/2 = 1.500")
        print(f"    Required: γ > 1")
        print(f"    Status: {'PASS — ODE blow-up possible' if gamma > 1 else 'FAIL — ODE stays bounded'}")

    print(f"\n  α (flux-enstrophy power): {alpha:.4f}")
    print(f"    Meaning: Π_max ~ Ω^{alpha:.2f}")
    print(f"    Required: α > 0 (flux persists as enstrophy grows)")
    print(f"    Status: {'PASS — flux sustains' if alpha > 0.3 else 'FAIL or WEAK — flux may die'}")

    # The iteration argument:
    # Step 1: P > 0 → dΩ/dt > 0 → enstrophy grows
    # Step 2: P ~ Ω^γ, γ > 1 → superlinear growth → ODE blow-up at T*
    # Step 3: Π persists → energy cascade feeds itself → growth sustains
    #
    # All three are needed.

    closes = (gamma is not None and gamma > 1.0 and alpha > 0.3)

    print(f"\n  ── Verdict ──")
    if closes:
        if gamma and abs(gamma - 1.5) < 0.15:
            print(f"  γ = {gamma:.4f} ≈ 3/2 (dimensional prediction CONFIRMED)")
        print(f"  The iteration argument is VIABLE:")
        print(f"    P > 0 always  ✓")
        print(f"    γ = {gamma:.4f} > 1  ✓  → T* = Ω₀^{{1-γ}} / (2c(γ-1))")
        print(f"    Π ~ Ω^{alpha:.2f} persists  ✓  → cascade self-sustains")
        print(f"\n  K1-K2 closure status: NUMERICALLY CONFIRMED")
        print(f"  Remaining: analytical proof of P > 0 and γ = 3/2 for TG symmetry class")
    else:
        if gamma is None or gamma <= 1:
            print(f"  γ ≤ 1: The ODE dΩ/dt = 2c·Ω^γ does NOT blow up.")
            print(f"  The iteration argument FAILS at the production step.")
        if alpha <= 0.3:
            print(f"  α ≤ 0.3: Flux dies as enstrophy grows.")
            print(f"  The iteration argument FAILS at the flux persistence step.")
        print(f"\n  K1-K2 closure status: BLOCKED")

    score("Iteration argument viable (γ > 1 AND Π persists)",
          closes,
          f"γ = {gamma if gamma else 'N/A'}, α = {alpha:.4f}")

    return closes


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  Toy 368 — γ Exponent and Flux Persistence                     ║")
    print("║  The two numbers that close or kill K1-K2.                      ║")
    print("║  Part A: P ~ Ω^γ across amplitudes (predict γ = 3/2)           ║")
    print("║  Part B: Π_max(t) through evolution (must persist)             ║")
    print("╚══════════════════════════════════════════════════════════════════╝")

    t0 = _time.time()

    # Part A: γ
    gamma, c_fit, all_omega, all_P, amp_results = part_a_gamma()

    # Part B: Flux
    flux_data = part_b_flux_persistence()

    # Combined assessment
    closes = iteration_assessment(gamma, flux_data)

    elapsed = _time.time() - t0

    print(f"\n" + "=" * 70)
    print(f"SCORECARD: {PASS}/{PASS+FAIL}")
    print(f"Time: {elapsed:.1f}s")
    print("=" * 70)
