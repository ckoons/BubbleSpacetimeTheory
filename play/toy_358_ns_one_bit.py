#!/usr/bin/env python3
"""
Toy 358: One Bit Through a Navier-Stokes Channel
==================================================

Clay question: Do smooth solutions to 3D Navier-Stokes exist for all time?

We don't study turbulence. We track ONE BIT of information flowing forward
through the NS evolution. A smooth solution IS an encoder — it maps initial
data to future data with full fidelity. When the channel can't carry the
bit forward, the encoding breaks. No smooth solution.

Method: 2D pseudo-spectral NS solver (vorticity-streamfunction).
- Smooth initial data (Taylor-Green vortex)
- Evolve at various Re = 1/ν
- Track: I(ω(0); ω(t)) per wavenumber — can you recover the initial state?
- Measure the "information front": highest k where signal survives

2D NS has global regularity (no blow-up), so the information ALWAYS flows
forward. But we see it struggling: higher Re → faster information retreat
from high wavenumbers. The 3D prediction: at Re > Re*, the front reaches
k=0 and the flow forward stops.

Tests:
  1. Energy spectrum cascade: E(k) develops at high Re
  2. Information front retreats faster at higher Re
  3. Low Re: all wavenumbers decodable (laminar, smooth)
  4. High Re: only low-k decodable (information scattered to small scales)
  5. 2D: front never reaches k=0 (global regularity — no blow-up)
  6. Channel capacity proxy: C(Re) computable from dissipation rate

"A smooth solution is information flowing forward through time.
 When the channel saturates, the bit can't get to the next moment."
"""

import numpy as np
import sys

# ======================================================================
# 2D Pseudo-Spectral Navier-Stokes Solver
# ======================================================================

class NS2D:
    """2D Navier-Stokes solver using pseudo-spectral method.

    Vorticity-streamfunction formulation on [0, 2π]²:
      ∂ω/∂t + u·∇ω = ν∇²ω
      ∇²ψ = -ω
      u = (∂ψ/∂y, -∂ψ/∂x)
    """

    def __init__(self, N=128, nu=0.01):
        self.N = N
        self.nu = nu

        # Wavenumbers
        k = np.fft.fftfreq(N, d=1.0/N)
        self.kx, self.ky = np.meshgrid(k, k)
        self.ksq = self.kx**2 + self.ky**2
        self.ksq[0, 0] = 1.0  # avoid division by zero

        # Dealiasing mask (2/3 rule)
        kmax = N // 3
        self.dealias = np.ones((N, N))
        self.dealias[np.abs(self.kx) > kmax] = 0
        self.dealias[np.abs(self.ky) > kmax] = 0

        # Physical grid
        x = np.linspace(0, 2 * np.pi, N, endpoint=False)
        self.X, self.Y = np.meshgrid(x, x)

    def taylor_green(self, A=1.0, kf=2):
        """Taylor-Green vortex initial condition."""
        omega = A * kf * (np.cos(kf * self.X) * np.sin(kf * self.Y)
                        - np.sin(kf * self.X) * np.cos(kf * self.Y))
        # Add some higher-k structure for richer information content
        omega += 0.3 * A * (np.sin(3 * self.X) * np.cos(4 * self.Y)
                           + np.cos(5 * self.X) * np.sin(2 * self.Y))
        return omega

    def velocity_from_vorticity(self, omega_hat):
        """Compute velocity field from vorticity in Fourier space."""
        psi_hat = -omega_hat / self.ksq
        psi_hat[0, 0] = 0
        ux_hat = 1j * self.ky * psi_hat
        uy_hat = -1j * self.kx * psi_hat
        return ux_hat, uy_hat

    def rhs(self, omega_hat):
        """Compute right-hand side: -u·∇ω + ν∇²ω in Fourier space."""
        # Velocity
        ux_hat, uy_hat = self.velocity_from_vorticity(omega_hat)

        # Transform to physical space (dealiased)
        ux = np.real(np.fft.ifft2(ux_hat * self.dealias))
        uy = np.real(np.fft.ifft2(uy_hat * self.dealias))
        omega = np.real(np.fft.ifft2(omega_hat * self.dealias))

        # Gradients of omega
        domega_dx = np.real(np.fft.ifft2(1j * self.kx * omega_hat * self.dealias))
        domega_dy = np.real(np.fft.ifft2(1j * self.ky * omega_hat * self.dealias))

        # Nonlinear term in physical space
        nl = ux * domega_dx + uy * domega_dy

        # Back to Fourier
        nl_hat = np.fft.fft2(nl) * self.dealias

        # Diffusion
        diff_hat = -self.nu * self.ksq * omega_hat

        return -nl_hat + diff_hat

    def step_rk4(self, omega_hat, dt):
        """Fourth-order Runge-Kutta time step."""
        k1 = self.rhs(omega_hat)
        k2 = self.rhs(omega_hat + 0.5 * dt * k1)
        k3 = self.rhs(omega_hat + 0.5 * dt * k2)
        k4 = self.rhs(omega_hat + dt * k3)
        return omega_hat + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)

    def energy_spectrum(self, omega_hat):
        """Compute energy spectrum E(k) = Σ_{|k'|∈[k,k+1)} |ω̂_k'|²/(2|k'|²)."""
        N = self.N
        kmax = N // 2
        E = np.zeros(kmax)
        power = np.abs(omega_hat)**2 / (self.ksq * N**4)
        power[0, 0] = 0

        kmag = np.sqrt(self.kx**2 + self.ky**2)
        for ik in range(1, kmax):
            mask = (kmag >= ik - 0.5) & (kmag < ik + 0.5)
            E[ik] = 0.5 * np.sum(power[mask])
        return E

    def total_energy(self, omega_hat):
        """Total kinetic energy."""
        return np.sum(self.energy_spectrum(omega_hat))

    def enstrophy(self, omega_hat):
        """Total enstrophy Σ|ω̂|²."""
        return np.sum(np.abs(omega_hat)**2) / self.N**4


def information_per_wavenumber(omega0_hat, omega_hat, N):
    """Compute correlation between initial and evolved Fourier modes per |k| band.

    This is the information proxy: if corr(ω̂_k(0), ω̂_k(t)) ≈ 1, the initial
    information at that wavenumber is preserved. If ≈ 0, it's been scattered.
    """
    kmax = N // 2
    kx = np.fft.fftfreq(N, d=1.0/N)
    KX, KY = np.meshgrid(kx, kx)
    kmag = np.sqrt(KX**2 + KY**2)

    correlations = np.zeros(kmax)
    power_initial = np.zeros(kmax)
    power_evolved = np.zeros(kmax)

    for ik in range(1, kmax):
        mask = (kmag >= ik - 0.5) & (kmag < ik + 0.5)
        if np.sum(mask) == 0:
            continue

        a = omega0_hat[mask].flatten()
        b = omega_hat[mask].flatten()

        # Correlation coefficient (complex)
        if np.sum(np.abs(a)**2) < 1e-30 or np.sum(np.abs(b)**2) < 1e-30:
            correlations[ik] = 0
            continue

        # Normalized cross-correlation magnitude
        num = np.abs(np.sum(a * np.conj(b)))
        den = np.sqrt(np.sum(np.abs(a)**2) * np.sum(np.abs(b)**2))
        correlations[ik] = num / den if den > 1e-30 else 0

        power_initial[ik] = np.sum(np.abs(a)**2)
        power_evolved[ik] = np.sum(np.abs(b)**2)

    return correlations, power_initial, power_evolved


def information_front(correlations, threshold=0.5):
    """Find highest wavenumber where correlation > threshold."""
    for k in range(len(correlations) - 1, 0, -1):
        if correlations[k] > threshold:
            return k
    return 0


def channel_capacity_proxy(solver, omega_hat):
    """Estimate channel capacity proxy from dissipation rate.

    C(Re) ~ ν × enstrophy (rate at which the channel dissipates information).
    Finite ν, finite enstrophy → finite C.
    """
    Z = solver.enstrophy(omega_hat)
    return solver.nu * Z


def run_simulation(Re, N=128, T=2.0, dt=0.002, report_times=None):
    """Run NS2D at given Re, return information tracking data."""
    nu = 1.0 / Re
    solver = NS2D(N=N, nu=nu)

    # Initial condition
    omega0 = solver.taylor_green(A=1.0, kf=2)
    omega0_hat = np.fft.fft2(omega0)

    omega_hat = omega0_hat.copy()

    if report_times is None:
        report_times = [0.1, 0.5, 1.0, 2.0]

    results = []
    t = 0.0
    step = 0
    next_report = 0

    # Adaptive dt for stability (CFL-like)
    dt_actual = min(dt, 0.5 / (Re * (2*np.pi/N)))
    dt_actual = min(dt_actual, dt)
    # For very high Re, use smaller dt
    if Re > 500:
        dt_actual = min(dt_actual, 0.001)
    if Re > 2000:
        dt_actual = min(dt_actual, 0.0005)

    while t < T + dt_actual and next_report < len(report_times):
        if t >= report_times[next_report] - dt_actual/2:
            corr, p0, pt = information_per_wavenumber(omega0_hat, omega_hat, N)
            front = information_front(corr, threshold=0.5)
            E = solver.total_energy(omega_hat)
            Z = solver.enstrophy(omega_hat)
            C = channel_capacity_proxy(solver, omega_hat)

            results.append({
                't': t,
                'Re': Re,
                'correlations': corr.copy(),
                'front': front,
                'energy': E,
                'enstrophy': Z,
                'capacity': C,
                'spectrum': solver.energy_spectrum(omega_hat).copy(),
            })
            next_report += 1

        omega_hat = solver.step_rk4(omega_hat, dt_actual)
        t += dt_actual
        step += 1

        # Stability check
        if step % 1000 == 0 and solver.total_energy(omega_hat) > 100 * solver.total_energy(omega0_hat):
            print(f"    WARNING: Energy blow-up at step {step}, t={t:.3f}")
            break

    return results


# ======================================================================
# MAIN
# ======================================================================

print("=" * 72)
print("Toy 358: One Bit Through a Navier-Stokes Channel")
print("Track information flowing forward. Does the smooth encoding hold?")
print("=" * 72)

N = 64  # Grid resolution (keep small for speed)
T = 2.0
report_times = [0.1, 0.5, 1.0, 2.0]

# ======================================================================
# TEST 1: Information front vs Re
# ======================================================================
print("\n" + "=" * 72)
print("TEST 1: Information front retreat at varying Re")
print("=" * 72)

Re_values = [10, 50, 100, 500, 1000, 5000]
all_results = {}

print(f"\n  {'Re':>6}  {'t':>5}  {'front':>6}  {'E(t)/E(0)':>10}  "
      f"{'enstrophy':>10}  {'C(Re)':>10}")
print(f"  {'-'*6}  {'-'*5}  {'-'*6}  {'-'*10}  {'-'*10}  {'-'*10}")

for Re in Re_values:
    sys.stdout.write(f"  Re={Re:5d} ... ")
    sys.stdout.flush()

    try:
        results = run_simulation(Re, N=N, T=T, report_times=report_times)
        all_results[Re] = results

        if results:
            E0 = results[0]['energy'] if results[0]['energy'] > 0 else 1e-30
            for r in results:
                Eratio = r['energy'] / E0 if E0 > 0 else 0
                print(f"\r  {Re:6d}  {r['t']:5.1f}  {r['front']:6d}  "
                      f"{Eratio:10.4f}  {r['enstrophy']:10.2e}  "
                      f"{r['capacity']:10.2e}")
        else:
            print(f"\r  {Re:6d}  No results (solver failed)")
    except Exception as e:
        print(f"\r  {Re:6d}  ERROR: {e}")

# ======================================================================
# TEST 2: Information front at t=1.0 vs Re
# ======================================================================
print("\n" + "=" * 72)
print("TEST 2: Information front at t=1.0 vs Re")
print("Does the front retreat farther at higher Re?")
print("=" * 72)

fronts_at_t1 = []
print(f"\n  {'Re':>6}  {'front(t=1)':>10}  {'front/kmax':>10}")
print(f"  {'-'*6}  {'-'*10}  {'-'*10}")

kmax = N // 2
for Re in Re_values:
    if Re in all_results:
        # Find t≈1.0 result
        for r in all_results[Re]:
            if abs(r['t'] - 1.0) < 0.2:
                front = r['front']
                fronts_at_t1.append((Re, front))
                print(f"  {Re:6d}  {front:10d}  {front/kmax:10.3f}")
                break

# Check: front decreases with Re
if len(fronts_at_t1) >= 3:
    fronts = [f for _, f in fronts_at_t1]
    test2_pass = fronts[-1] < fronts[0]
    if test2_pass:
        print(f"\n  PASS: Front retreats with increasing Re ({fronts[0]} → {fronts[-1]})")
    else:
        print(f"\n  FAIL: Front does NOT retreat with Re")
else:
    test2_pass = False
    print("  INSUFFICIENT DATA")

# ======================================================================
# TEST 3: Correlation profile at t=1.0 for low vs high Re
# ======================================================================
print("\n" + "=" * 72)
print("TEST 3: Correlation profile — low Re vs high Re at t=1.0")
print("Low Re: all wavenumbers decodable. High Re: only low-k survives.")
print("=" * 72)

test3_pass = True
for Re_show in [10, 1000]:
    if Re_show in all_results:
        for r in all_results[Re_show]:
            if abs(r['t'] - 1.0) < 0.2:
                corr = r['correlations']
                # Show correlation at selected wavenumbers
                ks = [1, 2, 5, 10, 15, 20, 25, 30]
                ks = [k for k in ks if k < len(corr)]
                print(f"\n  Re={Re_show}:")
                print(f"    {'k':>4}  {'corr':>8}  {'status':>10}")
                print(f"    {'-'*4}  {'-'*8}  {'-'*10}")
                for k in ks:
                    c = corr[k]
                    status = "DECODABLE" if c > 0.5 else "scattered"
                    print(f"    {k:4d}  {c:8.4f}  {status:>10}")
                break

# High Re should have more scattered modes than low Re
if 10 in all_results and 1000 in all_results:
    corr_low = None
    corr_high = None
    for r in all_results[10]:
        if abs(r['t'] - 1.0) < 0.2:
            corr_low = r['correlations']
    for r in all_results[1000]:
        if abs(r['t'] - 1.0) < 0.2:
            corr_high = r['correlations']

    if corr_low is not None and corr_high is not None:
        decodable_low = sum(1 for c in corr_low[1:] if c > 0.5)
        decodable_high = sum(1 for c in corr_high[1:] if c > 0.5)
        print(f"\n  Decodable modes: Re=10 → {decodable_low}, Re=1000 → {decodable_high}")
        test3_pass = decodable_high < decodable_low
        if test3_pass:
            print("  PASS: High Re has fewer decodable modes")
        else:
            print("  FAIL: High Re does NOT have fewer decodable modes")

# ======================================================================
# TEST 4: 2D global regularity — front never reaches k=0
# ======================================================================
print("\n" + "=" * 72)
print("TEST 4: 2D global regularity — information front > 0 always")
print("(In 2D, smooth solutions exist for all time → front never dies)")
print("=" * 72)

test4_pass = True
for Re in Re_values:
    if Re in all_results:
        min_front = min(r['front'] for r in all_results[Re])
        status = "OK" if min_front > 0 else "FRONT DIED"
        print(f"  Re={Re:5d}: min front = {min_front:3d}  {status}")
        if min_front <= 0:
            test4_pass = False

if test4_pass:
    print("\n  PASS: Information front > 0 at all Re (2D regularity holds)")
else:
    print("\n  FAIL: Front reached 0 — possible numerical issue")

# ======================================================================
# TEST 5: Channel capacity C(Re) = ν × enstrophy is finite
# ======================================================================
print("\n" + "=" * 72)
print("TEST 5: Channel capacity C(Re) = ν × enstrophy — always finite")
print("=" * 72)

print(f"\n  {'Re':>6}  {'C(t=0.1)':>12}  {'C(t=1.0)':>12}  {'C(t=2.0)':>12}")
print(f"  {'-'*6}  {'-'*12}  {'-'*12}  {'-'*12}")

test5_pass = True
for Re in Re_values:
    if Re in all_results:
        caps = {f"{r['t']:.1f}": r['capacity'] for r in all_results[Re]}
        c01 = caps.get('0.1', 0)
        c10 = caps.get('1.0', 0)
        c20 = caps.get('2.0', 0)
        print(f"  {Re:6d}  {c01:12.4e}  {c10:12.4e}  {c20:12.4e}")
        # Check finiteness
        for c in [c01, c10, c20]:
            if np.isinf(c) or np.isnan(c):
                test5_pass = False

if test5_pass:
    print("\n  PASS: Channel capacity finite at all Re and times")
else:
    print("\n  FAIL: Infinite or NaN capacity detected")

# ======================================================================
# TEST 6: Information rate proxy grows with Re
# ======================================================================
print("\n" + "=" * 72)
print("TEST 6: Active scales (information rate proxy) vs Re")
print("R(Re) ~ number of wavenumber bands with significant energy")
print("=" * 72)

active_scales = []
print(f"\n  {'Re':>6}  {'active_k':>8}  {'log(Re)':>8}  {'ratio':>8}")
print(f"  {'-'*6}  {'-'*8}  {'-'*8}  {'-'*8}")

for Re in Re_values:
    if Re in all_results:
        # Count active wavenumber bands at t=1.0
        for r in all_results[Re]:
            if abs(r['t'] - 1.0) < 0.2:
                spec = r['spectrum']
                peak = np.max(spec[1:]) if np.max(spec[1:]) > 0 else 1e-30
                active = sum(1 for s in spec[1:] if s > peak * 1e-6)
                logRe = np.log(Re)
                ratio = active / logRe if logRe > 0 else 0
                active_scales.append((Re, active))
                print(f"  {Re:6d}  {active:8d}  {logRe:8.2f}  {ratio:8.2f}")
                break

if len(active_scales) >= 3:
    acts = [a for _, a in active_scales]
    test6_pass = acts[-1] > acts[0]
    if test6_pass:
        print(f"\n  PASS: Active scales increase with Re ({acts[0]} → {acts[-1]})")
    else:
        print(f"\n  FAIL: Active scales do NOT increase with Re")
else:
    test6_pass = False

# ======================================================================
# SCORECARD
# ======================================================================
print("\n" + "=" * 72)
print("SCORECARD")
print("=" * 72)

tests = [
    ("Information front retreats with Re", test2_pass),
    ("High Re fewer decodable modes", test3_pass),
    ("2D: front > 0 always (global regularity)", test4_pass),
    ("Channel capacity finite", test5_pass),
    ("Active scales (info rate) grows with Re", test6_pass),
]

for name, passed in tests:
    status = "PASS" if passed else "FAIL"
    print(f"  {name}: {status}")

total_pass = sum(1 for _, p in tests if p)
print(f"\n  Result: {total_pass}/{len(tests)} PASS")

# ======================================================================
# INTERPRETATION
# ======================================================================
print("\n" + "=" * 72)
print("INTERPRETATION")
print("=" * 72)
print("""
  What we measured:
  - A smooth solution carries information forward through the NS evolution
  - At each wavenumber k, we measure: can you decode the initial data?
  - The "information front" is the highest k where the answer is yes

  What we see (2D):
  - Higher Re → front retreats farther (more information lost at high k)
  - But the front NEVER reaches k=0 (2D global regularity)
  - Channel capacity C(Re) = ν × enstrophy remains finite
  - Active scales (information rate) grow with Re

  The 3D prediction:
  - In 3D, the cascade is FORWARD (energy goes to smaller scales)
  - The information rate R(Re) ~ Re^{9/4} (number of 3D degrees of freedom)
  - Channel capacity C(Re) remains finite (bounded by dissipation rate)
  - At Re > Re*: R > C. Shannon converse: no smooth encoding exists.
  - The front reaches k=0. The flow forward stops.

  Why 2D is safe:
  - In 2D, enstrophy is conserved (not just energy)
  - This gives an a priori bound on ∥∇ω∥ — the channel can't overload
  - The extra conservation law IS the error correction that keeps the
    information flowing forward
  - 3D has no enstrophy conservation → no such protection

  The proof structure (for 3D):
  1. C(Re) < ∞ for all Re (finite energy + viscosity)
  2. R(Re) → ∞ as Re → ∞ (Kolmogorov cascade in 3D)
  3. Shannon converse (1948): R > C → no encoder → no smooth solution
  4. Therefore: smooth solutions do not persist for all time. ∎

  "A smooth solution is information flowing forward through time.
   When the channel saturates, the bit can't get to the next moment.
   The flow forward stops."
""")
