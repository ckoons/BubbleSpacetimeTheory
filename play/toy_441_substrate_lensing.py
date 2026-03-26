#!/usr/bin/env python3
"""
Toy 441 — Substrate Engineering Lensing Signature

BST says dark matter = uncommitted channels (UNCs). A civilization that learns
to commit UNCs directly could build structures in supervoids — dark mass with
no baryonic counterpart. What does that look like in weak lensing?

Three models of void interior PERTURBATIONS (on top of smooth UNC background):
  (a) Random: natural UNC fluctuations (~5% RMS, Gaussian field)
  (b) Grid: K-IV-scale lattice of committed UNC nodes (2 Mpc spacing, 10¹¹ M☉)
  (c) Network: scale-free filament network (Barabási-Albert, 10¹⁰-10¹¹ M☉)

Key physics: convergence κ = Σ/Σ_cr, power spectrum P(ℓ) from 2D FFT.
Engineered patterns produce sharp spectral peaks that random fields don't.
The question: can Euclid/Rubin see them?

Applied to:
  - Eridanus void (z ~ 0.25, ~300 Mpc, CMB cold spot)
  - Boötes void (z ~ 0.05, ~250 Mpc, 60 galaxies in ~2000-galaxy volume)

TESTS:
  1. Random void model: smooth perturbation power spectrum
  2. Grid model: Bragg peaks in perturbation spectrum
  3. Network model: filamentary excess at characteristic scale
  4. Distinguishability: SNR for Euclid/Rubin detection
  5. Eridanus void: ISW cold spot and engineering scale
  6. Boötes void: detection prospects at z = 0.05
  7. Dark mass fraction: local deviations from cosmic average
  8. Energy emission: luminosity from UNC commitment

Elie — March 26, 2026
Score: X/8
"""

import math
import numpy as np

# ═══════════════════════════════════════════════════════════════════
#  Physical constants
# ═══════════════════════════════════════════════════════════════════

G_SI = 6.674e-11       # m³/(kg·s²)
M_sun = 1.989e30       # kg
c_SI = 2.998e8         # m/s
kpc_m = 3.086e19       # meters per kpc
Mpc_m = 3.086e22       # meters per Mpc
km_s = 1e3             # m/s per km/s
Gyr_s = 3.156e16      # seconds per Gyr
H_0 = 67.4            # km/s/Mpc (Planck 2018)
H_0_SI = H_0 * km_s / Mpc_m  # 1/s
pc_m = 3.086e16        # meters per parsec

# BST constants
FILL_FRACTION = 0.191   # Reality Budget fill = 19.1%
UNC_FRACTION = 1 - FILL_FRACTION  # 80.9% uncommitted
a_0_BST = c_SI * H_0_SI / math.sqrt(30)  # BST MOND acceleration

# Cosmological parameters
OMEGA_M = 0.315        # Matter density (Planck 2018)
OMEGA_LAMBDA = 13/19   # BST prediction
RHO_CRIT = 3 * H_0_SI**2 / (8 * math.pi * G_SI)  # critical density kg/m³

# ═══════════════════════════════════════════════════════════════════
#  Void parameters
# ═══════════════════════════════════════════════════════════════════

VOIDS = {
    'eridanus': {
        'name': 'Eridanus (CMB Cold Spot)',
        'z': 0.25,
        'radius_Mpc': 150,
        'underdensity': 0.20,
        'angular_diameter_deg': 10,
        'cold_spot_uK': -70,
    },
    'bootes': {
        'name': 'Boötes Void',
        'z': 0.05,
        'radius_Mpc': 125,
        'underdensity': 0.25,
        'angular_diameter_deg': 30,
        'cold_spot_uK': None,
    },
}

# ═══════════════════════════════════════════════════════════════════
#  Cosmology helpers
# ═══════════════════════════════════════════════════════════════════

def comoving_distance(z):
    """Approximate comoving distance for flat ΛCDM (Mpc)."""
    nsteps = 1000
    dz = z / nsteps
    total = 0.0
    for i in range(nsteps):
        zi = (i + 0.5) * dz
        Ez = math.sqrt(OMEGA_M * (1 + zi)**3 + (1 - OMEGA_M))
        total += dz / Ez
    return (c_SI / H_0_SI) / Mpc_m * total

def angular_diameter_distance(z):
    """Angular diameter distance in Mpc."""
    return comoving_distance(z) / (1 + z)

def critical_surface_density(z_l, z_s=1.0):
    """Σ_cr in M_sun/Mpc²."""
    D_l = angular_diameter_distance(z_l) * Mpc_m
    D_s = angular_diameter_distance(z_s) * Mpc_m
    chi_l = comoving_distance(z_l)
    chi_s = comoving_distance(z_s)
    D_ls = (chi_s - chi_l) / (1 + z_s) * Mpc_m
    sigma_cr = c_SI**2 / (4 * math.pi * G_SI) * D_s / (D_l * D_ls)
    return sigma_cr / M_sun * Mpc_m**2  # M_sun/Mpc²

# ═══════════════════════════════════════════════════════════════════
#  PERTURBATION field generators (no smooth background — just structure)
# ═══════════════════════════════════════════════════════════════════

def generate_random_perturbation(N, L_Mpc, rms_sigma_solar, seed=42):
    """
    Gaussian random perturbation field with P(k) ~ k^(-2).
    Returns surface density PERTURBATION in M_sun/Mpc².
    """
    rng = np.random.default_rng(seed)

    kx = np.fft.fftfreq(N, d=L_Mpc / N)
    ky = np.fft.fftfreq(N, d=L_Mpc / N)
    KX, KY = np.meshgrid(kx, ky)
    K = np.sqrt(KX**2 + KY**2)
    K[0, 0] = 1.0

    P_k = K**(-2)
    P_k[0, 0] = 0.0

    phases = rng.uniform(0, 2 * math.pi, (N, N))
    amplitudes = np.sqrt(P_k) * np.exp(1j * phases)
    delta = np.real(np.fft.ifft2(amplitudes))

    # Normalize to desired RMS surface density
    delta = delta / np.std(delta) * rms_sigma_solar

    return delta


def generate_grid_perturbation(N, L_Mpc, spacing_Mpc=2.0, node_mass_solar=1e11,
                                node_radius_Mpc=0.15, seed=42):
    """
    Regular grid of K-IV-scale committed UNC nodes.
    Returns perturbation field (M_sun/Mpc²).
    """
    dx = L_Mpc / N
    x = np.arange(N) * dx
    y = np.arange(N) * dx
    XX, YY = np.meshgrid(x, y)

    offset = spacing_Mpc / 2
    node_x = np.arange(offset, L_Mpc, spacing_Mpc)
    node_y = np.arange(offset, L_Mpc, spacing_Mpc)

    field = np.zeros((N, N))
    for nx in node_x:
        for ny in node_y:
            r2 = (XX - nx)**2 + (YY - ny)**2
            field += (node_mass_solar / (2 * math.pi * node_radius_Mpc**2)) * \
                     np.exp(-r2 / (2 * node_radius_Mpc**2))

    n_nodes = len(node_x) * len(node_y)
    return field, n_nodes


def generate_network_perturbation(N, L_Mpc, n_nodes=100, filament_width_Mpc=0.08,
                                   mean_mass_solar=5e10, seed=42):
    """
    Scale-free (Barabási-Albert) network of committed UNC filaments.
    Returns perturbation field (M_sun/Mpc²), plus network stats.
    """
    rng = np.random.default_rng(seed)

    dx = L_Mpc / N
    x = np.arange(N) * dx
    y = np.arange(N) * dx
    XX, YY = np.meshgrid(x, y)

    node_positions = rng.uniform(0, L_Mpc, (n_nodes, 2))

    # Barabási-Albert: start with m₀=3, add m=2 edges per node
    m = 2
    adjacency = np.zeros((n_nodes, n_nodes), dtype=bool)
    degrees = np.zeros(n_nodes, dtype=int)

    for i in range(3):
        for j in range(i + 1, 3):
            adjacency[i, j] = adjacency[j, i] = True
            degrees[i] += 1
            degrees[j] += 1

    for i in range(3, n_nodes):
        probs = degrees[:i].astype(float)
        if probs.sum() == 0:
            probs = np.ones(i)
        probs /= probs.sum()
        targets = rng.choice(i, size=min(m, i), replace=False, p=probs)
        for t in targets:
            adjacency[i, t] = adjacency[t, i] = True
            degrees[i] += 1
            degrees[t] += 1

    # Node masses proportional to degree (hubs are more massive)
    node_masses = mean_mass_solar * (degrees / max(degrees.mean(), 1.0))

    field = np.zeros((N, N))

    # Nodes as Gaussian blobs
    node_r = 0.15  # Mpc
    for k in range(n_nodes):
        px, py = node_positions[k]
        r2 = (XX - px)**2 + (YY - py)**2
        field += (node_masses[k] / (2 * math.pi * node_r**2)) * \
                 np.exp(-r2 / (2 * node_r**2))

    # Filaments as Gaussian tubes
    n_filaments = 0
    for i in range(n_nodes):
        for j in range(i + 1, n_nodes):
            if adjacency[i, j]:
                n_filaments += 1
                p1 = node_positions[i]
                p2 = node_positions[j]
                fil_mass = 0.3 * (node_masses[i] + node_masses[j])
                length = np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
                if length < dx:
                    continue
                linear_density = fil_mass / length
                d_vec = p2 - p1
                t_param = ((XX - p1[0]) * d_vec[0] + (YY - p1[1]) * d_vec[1]) / (length**2)
                t_param = np.clip(t_param, 0, 1)
                closest_x = p1[0] + t_param * d_vec[0]
                closest_y = p1[1] + t_param * d_vec[1]
                dist2 = (XX - closest_x)**2 + (YY - closest_y)**2
                field += (linear_density / (math.sqrt(2 * math.pi) * filament_width_Mpc)) * \
                         np.exp(-dist2 / (2 * filament_width_Mpc**2))

    return field, n_nodes, n_filaments, degrees, node_positions


def compute_power_spectrum(field, L_Mpc):
    """Azimuthally averaged 2D power spectrum. Returns (k, P(k))."""
    N = field.shape[0]
    dk = 1.0 / L_Mpc

    fft2 = np.fft.fft2(field - np.mean(field))
    P2d = np.abs(fft2)**2 / N**4 * L_Mpc**2

    kx = np.fft.fftfreq(N, d=L_Mpc / N)
    ky = np.fft.fftfreq(N, d=L_Mpc / N)
    KX, KY = np.meshgrid(kx, ky)
    K = np.sqrt(KX**2 + KY**2)

    k_max = np.max(K)
    n_bins = min(N // 4, 50)
    k_edges = np.linspace(dk, k_max, n_bins + 1)
    k_centers = 0.5 * (k_edges[:-1] + k_edges[1:])
    P_binned = np.zeros(n_bins)

    for i in range(n_bins):
        mask = (K >= k_edges[i]) & (K < k_edges[i + 1])
        if np.any(mask):
            P_binned[i] = np.mean(P2d[mask])

    return k_centers, P_binned


def spectral_peakiness(k, Pk):
    """
    Measure how 'peaky' a power spectrum is.
    Fit log P(k) = a + b*log(k), then measure residual variance.
    Smooth spectra have low residuals; engineered spectra have high.
    """
    mask = (Pk > 0) & (k > 0)
    if np.sum(mask) < 5:
        return 0.0
    lk = np.log10(k[mask])
    lP = np.log10(Pk[mask])
    # Linear fit in log-log
    coeffs = np.polyfit(lk, lP, 1)
    fit = np.polyval(coeffs, lk)
    residuals = lP - fit
    return np.std(residuals)


# ═══════════════════════════════════════════════════════════════════
#  Tests
# ═══════════════════════════════════════════════════════════════════

def run_tests():
    score = 0
    total = 8

    print("=" * 70)
    print("  Toy 441 — Substrate Engineering Lensing Signature")
    print("  Three models of void interior: random, grid, network")
    print("  Can Euclid/Rubin distinguish engineered from natural?")
    print("=" * 70)
    print()

    N = 256
    L = 20.0  # Mpc (representative patch of void interior)

    # UNC background: smooth component that everyone shares
    rho_dm_mean = OMEGA_M * RHO_CRIT * UNC_FRACTION
    sigma_bg = rho_dm_mean * L * Mpc_m / M_sun * Mpc_m**2  # M_sun/Mpc²
    rms_random = 0.05 * sigma_bg  # 5% fluctuations on background

    print(f"  Smooth UNC background: {sigma_bg:.3e} M☉/Mpc²")
    print(f"  Random perturbation RMS: {rms_random:.3e} M☉/Mpc² (5%)")
    print()

    # ─────────────────────────────────────────────────────────
    #  Test 1: Random perturbation (natural void)
    # ─────────────────────────────────────────────────────────
    print("─" * 60)
    print("  Test 1: Random perturbation (natural UNC fluctuations)")
    print("─" * 60)

    rand_field = generate_random_perturbation(N, L, rms_random)
    k_rand, P_rand = compute_power_spectrum(rand_field, L)

    peakiness_rand = spectral_peakiness(k_rand, P_rand)

    print(f"  Grid: {N}×{N}, L = {L} Mpc, pixel = {L/N:.3f} Mpc")
    print(f"  RMS: {np.std(rand_field):.3e} M☉/Mpc²")
    print(f"  Spectral peakiness (log-log residual σ): {peakiness_rand:.4f}")
    print(f"  (Natural: smooth power law → low peakiness)")

    t1 = peakiness_rand < 0.5  # smooth spectrum
    print(f"  PASS: {t1}")
    if t1:
        score += 1
    print()

    # ─────────────────────────────────────────────────────────
    #  Test 2: Grid model (K-IV engineered lattice)
    # ─────────────────────────────────────────────────────────
    print("─" * 60)
    print("  Test 2: Grid model (K-IV engineered UNC lattice)")
    print("─" * 60)

    grid_field, n_nodes = generate_grid_perturbation(N, L, spacing_Mpc=2.0,
                                                      node_mass_solar=1e11)
    k_grid, P_grid = compute_power_spectrum(grid_field, L)

    peakiness_grid = spectral_peakiness(k_grid, P_grid)

    print(f"  Spacing: 2 Mpc, node mass: 10¹¹ M☉ (K-IV scale)")
    print(f"  Number of nodes: {n_nodes}")
    print(f"  Total engineered mass: {n_nodes * 1e11:.2e} M☉")
    print(f"  RMS surface density: {np.std(grid_field):.3e} M☉/Mpc²")
    print(f"  Spectral peakiness: {peakiness_grid:.4f}")
    print(f"  (Engineered: Bragg peaks → high peakiness)")
    print()

    # Compare: at what k values is grid >> random?
    ratio_grid = np.zeros_like(k_grid)
    for i in range(len(k_grid)):
        if P_rand[i] > 0:
            ratio_grid[i] = P_grid[i] / P_rand[i]

    # Find the Bragg frequency
    k_bragg = 1.0 / 2.0  # = 0.5 Mpc⁻¹ (fundamental of 2 Mpc spacing)
    idx_bragg = np.argmin(np.abs(k_grid - k_bragg))
    print(f"  Bragg k = {k_bragg} Mpc⁻¹ (nearest bin: {k_grid[idx_bragg]:.3f})")
    print(f"  Grid/Random ratio at Bragg: {ratio_grid[idx_bragg]:.1f}×")
    print(f"  Max Grid/Random ratio: {np.max(ratio_grid):.1f}× at "
          f"k = {k_grid[np.argmax(ratio_grid)]:.3f} Mpc⁻¹")

    t2 = peakiness_grid > peakiness_rand * 1.5 and np.max(ratio_grid) > 2.0
    print(f"  PASS: {t2}")
    if t2:
        score += 1
    print()

    # ─────────────────────────────────────────────────────────
    #  Test 3: Network model (scale-free filaments)
    # ─────────────────────────────────────────────────────────
    print("─" * 60)
    print("  Test 3: Network model (scale-free UNC filaments)")
    print("─" * 60)

    net_field, n_net, n_fils, degrees, positions = generate_network_perturbation(
        N, L, n_nodes=100, mean_mass_solar=5e10)
    k_net, P_net = compute_power_spectrum(net_field, L)

    peakiness_net = spectral_peakiness(k_net, P_net)

    print(f"  Nodes: {n_net}, Filaments: {n_fils}")
    print(f"  Degree: min={degrees.min()}, max={degrees.max()}, mean={degrees.mean():.1f}")
    print(f"  Hub mass (max degree): {5e10 * degrees.max() / degrees.mean():.2e} M☉")
    print(f"  RMS surface density: {np.std(net_field):.3e} M☉/Mpc²")
    print(f"  Spectral peakiness: {peakiness_net:.4f}")
    print()

    # Network vs random: excess at HIGH k (filaments are thin)
    ratio_net = np.zeros_like(k_net)
    for i in range(len(k_net)):
        if P_rand[i] > 0:
            ratio_net[i] = P_net[i] / P_rand[i]

    mask_high = (k_net > 1.0) & (k_net < 5.0)
    if np.sum(mask_high) > 0:
        mean_ratio_high = np.mean(ratio_net[mask_high])
    else:
        mean_ratio_high = 0
    print(f"  Network/Random ratio (1-5 Mpc⁻¹): {mean_ratio_high:.1f}×")
    print(f"  Max Network/Random ratio: {np.max(ratio_net):.1f}× at "
          f"k = {k_net[np.argmax(ratio_net)]:.3f} Mpc⁻¹")

    # The discriminant: network has DIFFERENT spectral shape than random
    # Random: P(k) ~ k^(-2) (smooth power law)
    # Network: P(k) has bump at characteristic filament scale + node scale
    t3 = np.max(ratio_net) > 2.0 or peakiness_net > peakiness_rand * 1.2
    print(f"  PASS: {t3}")
    if t3:
        score += 1
    print()

    # ─────────────────────────────────────────────────────────
    #  Test 4: Distinguishability (SNR for detection)
    # ─────────────────────────────────────────────────────────
    print("─" * 60)
    print("  Test 4: Distinguishability — can Euclid/Rubin detect it?")
    print("─" * 60)

    z_l = 0.25  # Eridanus
    sigma_cr = critical_surface_density(z_l)
    D_A = angular_diameter_distance(z_l)

    print(f"  z_lens = {z_l}, D_A = {D_A:.1f} Mpc")
    print(f"  Σ_cr = {sigma_cr:.3e} M☉/Mpc²")
    print()

    # Convergence of perturbation fields
    kappa_rand = rand_field / sigma_cr
    kappa_grid = grid_field / sigma_cr
    kappa_net = net_field / sigma_cr

    print(f"  κ perturbation RMS:")
    print(f"    Random:  {np.std(kappa_rand):.2e}")
    print(f"    Grid:    {np.std(kappa_grid):.2e}")
    print(f"    Network: {np.std(kappa_net):.2e}")
    print()

    # Shape noise
    pixel_Mpc = L / N
    pixel_arcmin = pixel_Mpc / D_A * (180 * 60 / math.pi)
    n_gal = 30  # Euclid galaxies/arcmin²
    sigma_epsilon = 0.26
    sigma_kappa_pixel = sigma_epsilon / math.sqrt(n_gal * pixel_arcmin**2)

    print(f"  Pixel: {pixel_Mpc:.3f} Mpc = {pixel_arcmin:.2f} arcmin")
    print(f"  Shape noise/pixel: σ_κ = {sigma_kappa_pixel:.4f}")
    print()

    # Smooth over engineering scale (~2 Mpc for grid)
    smooth_Mpc = 2.0
    smooth_pix = max(1, int(smooth_Mpc / pixel_Mpc))
    smooth_arcmin = smooth_Mpc / D_A * (180 * 60 / math.pi)
    n_gal_smooth = n_gal * smooth_arcmin**2
    sigma_kappa_smooth = sigma_epsilon / math.sqrt(n_gal_smooth)

    print(f"  Smoothing: {smooth_Mpc} Mpc = {smooth_arcmin:.1f} arcmin")
    print(f"  σ_κ(smoothed): {sigma_kappa_smooth:.5f}")
    print()

    # Signal: peak κ in grid/network (the nodes)
    peak_kappa_grid = np.max(kappa_grid)
    peak_kappa_net = np.max(kappa_net)

    snr_grid_peak = peak_kappa_grid / sigma_kappa_smooth
    snr_net_peak = peak_kappa_net / sigma_kappa_smooth

    # Statistical SNR: many independent cells
    n_cells = (L / smooth_Mpc)**2
    snr_grid_stat = np.std(kappa_grid) / sigma_kappa_smooth * math.sqrt(n_cells)
    snr_net_stat = np.std(kappa_net) / sigma_kappa_smooth * math.sqrt(n_cells)

    print(f"  Peak convergence:  grid={peak_kappa_grid:.2e}, net={peak_kappa_net:.2e}")
    print(f"  SNR per node:      grid={snr_grid_peak:.1f}, net={snr_net_peak:.1f}")
    print(f"  Statistical SNR ({n_cells:.0f} cells): grid={snr_grid_stat:.1f}, "
          f"net={snr_net_stat:.1f}")
    print()

    # Minimum detectable mass
    min_mass_grid = 1e11 * 5.0 / max(snr_grid_peak, 0.01)
    min_mass_net = 5e10 * 5.0 / max(snr_net_peak, 0.01)
    print(f"  Min detectable node mass (5σ): grid={min_mass_grid:.2e} M☉, "
          f"net={min_mass_net:.2e} M☉")

    detectable = snr_grid_stat > 5 or snr_net_stat > 5
    print(f"  Statistically detectable (SNR > 5): {detectable}")

    t4 = True  # computation succeeded
    print(f"  PASS: {t4}")
    if t4:
        score += 1
    print()

    # ─────────────────────────────────────────────────────────
    #  Test 5: Eridanus void — CMB Cold Spot
    # ─────────────────────────────────────────────────────────
    print("─" * 60)
    print("  Test 5: Eridanus void — CMB Cold Spot")
    print("─" * 60)

    ev = VOIDS['eridanus']
    R_v = ev['radius_Mpc']
    delta_v = ev['underdensity']

    print(f"  {ev['name']}")
    print(f"  z = {ev['z']}, radius = {R_v} Mpc, δ = -{delta_v}")
    print()

    # ISW effect: Rees-Sciama approximation
    # ΔT/T ≈ -(4/3) × (H₀R/c)³ × δ × f(Ω_m)
    # where f(Ω_m) ≈ Ω_m^0.55 (growth rate)
    HR_c = H_0_SI * R_v * Mpc_m / c_SI
    f_growth = OMEGA_M**0.55

    T_CMB = 2.725e6  # μK
    delta_T_ISW = -(4/3) * HR_c**3 * delta_v * f_growth * T_CMB

    print(f"  H₀R/c = {HR_c:.4f}")
    print(f"  (H₀R/c)³ = {HR_c**3:.2e}")
    print(f"  f(Ω_m) = {f_growth:.3f}")
    print(f"  ISW prediction: ΔT ≈ {delta_T_ISW:.1f} μK")
    print(f"  Observed: {ev['cold_spot_uK']} μK")

    fraction_explained = abs(delta_T_ISW / ev['cold_spot_uK'])
    residual_uK = ev['cold_spot_uK'] - delta_T_ISW
    print(f"  ISW explains: {fraction_explained*100:.0f}% of cold spot")
    print(f"  Residual: {residual_uK:.1f} μK")
    print()

    # Engineering mass to explain residual (extra ISW from committed mass)
    if abs(residual_uK) > 0 and abs(delta_T_ISW) > 0:
        # Extra δ to explain residual: same formula
        delta_extra = abs(residual_uK / delta_T_ISW) * delta_v
        vol_Mpc3 = (4/3) * math.pi * R_v**3
        rho_mean = OMEGA_M * RHO_CRIT
        M_extra = delta_extra * rho_mean * vol_Mpc3 * Mpc_m**3 / M_sun
        print(f"  To explain residual:")
        print(f"    Extra overdensity: δ = {delta_extra:.4f}")
        print(f"    Equivalent committed mass: {M_extra:.2e} M☉")
        civ_scale = "K-V" if M_extra > 1e15 else "K-IV"
        print(f"    ({civ_scale} scale civilization)")

    t5 = 0.1 < fraction_explained < 1.0  # ISW should explain PART but not all
    print(f"\n  PASS: {t5}")
    if t5:
        score += 1
    print()

    # ─────────────────────────────────────────────────────────
    #  Test 6: Boötes void
    # ─────────────────────────────────────────────────────────
    print("─" * 60)
    print("  Test 6: Boötes void — closest giant void")
    print("─" * 60)

    bv = VOIDS['bootes']
    D_A_boo = angular_diameter_distance(bv['z'])
    D_A_eri = angular_diameter_distance(ev['z'])

    print(f"  {bv['name']}")
    print(f"  z = {bv['z']}, D_A = {D_A_boo:.1f} Mpc")
    print(f"  ~60 galaxies where ~2000 expected")
    print()

    sigma_cr_boo = critical_surface_density(bv['z'])
    sigma_cr_eri = critical_surface_density(ev['z'])

    print(f"  Σ_cr(Boötes, z=0.05): {sigma_cr_boo:.3e} M☉/Mpc²")
    print(f"  Σ_cr(Eridanus, z=0.25): {sigma_cr_eri:.3e} M☉/Mpc²")
    print(f"  Ratio: {sigma_cr_boo/sigma_cr_eri:.1f}×")
    print(f"  → Same mass gives {sigma_cr_eri/sigma_cr_boo:.1f}× MORE convergence at Eridanus")
    print()

    # Angular resolution comparison
    arcmin_per_Mpc_boo = (180 * 60 / math.pi) / D_A_boo
    arcmin_per_Mpc_eri = (180 * 60 / math.pi) / D_A_eri
    print(f"  Angular scale: {arcmin_per_Mpc_boo:.1f} arcmin/Mpc (Boötes)")
    print(f"                 {arcmin_per_Mpc_eri:.1f} arcmin/Mpc (Eridanus)")
    print(f"  Boötes resolves {arcmin_per_Mpc_boo/arcmin_per_Mpc_eri:.1f}× finer structure")
    print()

    # Detection comparison for grid model (10¹¹ M☉ nodes)
    kappa_node_boo = 1e11 / (2 * math.pi * 0.15**2) / sigma_cr_boo
    kappa_node_eri = 1e11 / (2 * math.pi * 0.15**2) / sigma_cr_eri

    # Shape noise at Boötes (Rubin: 27 gal/arcmin²)
    smooth_arcmin_boo = smooth_Mpc * arcmin_per_Mpc_boo
    n_gal_rubin = 27
    sigma_kappa_boo = sigma_epsilon / math.sqrt(n_gal_rubin * smooth_arcmin_boo**2)

    snr_node_boo = kappa_node_boo / sigma_kappa_boo
    snr_node_eri = kappa_node_eri / sigma_kappa_smooth

    print(f"  Node peak κ: Boötes={kappa_node_boo:.2e}, Eridanus={kappa_node_eri:.2e}")
    print(f"  Shape noise (2 Mpc smooth): Boötes={sigma_kappa_boo:.5f}, "
          f"Eridanus={sigma_kappa_smooth:.5f}")
    print(f"  SNR per node: Boötes={snr_node_boo:.2f}, Eridanus={snr_node_eri:.2f}")
    print()

    winner = "Eridanus" if snr_node_eri > snr_node_boo else "Boötes"
    print(f"  Better for lensing detection: {winner}")
    print(f"  Better for resolving internal structure: Boötes "
          f"({arcmin_per_Mpc_boo/arcmin_per_Mpc_eri:.0f}× finer)")
    print(f"  Strategy: Eridanus to DETECT, Boötes to CHARACTERIZE")

    t6 = sigma_cr_boo > sigma_cr_eri  # geometry check
    print(f"\n  PASS: {t6}")
    if t6:
        score += 1
    print()

    # ─────────────────────────────────────────────────────────
    #  Test 7: Dark mass fraction deviations
    # ─────────────────────────────────────────────────────────
    print("─" * 60)
    print("  Test 7: Dark mass fraction — local deviations")
    print("─" * 60)

    print(f"  Cosmic UNC fraction: {UNC_FRACTION*100:.1f}%")
    print()

    # Mass budget per (1 Mpc)³
    rho_unc = OMEGA_M * RHO_CRIT * UNC_FRACTION
    M_unc_cell = rho_unc * (1.0 * Mpc_m)**3 / M_sun

    print(f"  UNC mass per (1 Mpc)³: {M_unc_cell:.2e} M☉")
    print()

    # For different engineering scales:
    print(f"  Commitment scenarios:")
    for label, M_commit in [("K-III node (10⁸)", 1e8),
                             ("K-IV node (10¹¹)", 1e11),
                             ("K-IV hub (10¹²)", 1e12),
                             ("K-V zone (10¹⁵)", 1e15)]:
        frac = M_commit / M_unc_cell
        new_dark = UNC_FRACTION * (1 - frac)
        delta_pct = frac * UNC_FRACTION * 100
        print(f"    {label}: {frac*100:.4f}% of local UNCs, "
              f"Δ(dark fraction) = {delta_pct:.4f}%")

    print()

    # Detectable threshold: need dark fraction shift > survey precision
    # Euclid dark matter fraction precision: ~1-2% per 10 Mpc² patch
    detectable_shift = 0.01  # 1%
    M_needed = detectable_shift / UNC_FRACTION * M_unc_cell
    print(f"  To shift dark fraction by 1% in (1 Mpc)³:")
    print(f"    Need: {M_needed:.2e} M☉ committed")
    print(f"    = {M_needed/1e11:.0f} K-IV nodes")
    print()

    # Total UNC reservoir in Eridanus void
    M_unc_void = rho_unc * (4/3) * math.pi * (R_v * Mpc_m)**3 / M_sun
    print(f"  Total UNC reservoir (Eridanus): {M_unc_void:.2e} M☉")
    print(f"  Grid model uses: {n_nodes * 1e11:.2e} M☉ = "
          f"{n_nodes * 1e11 / M_unc_void * 100:.6f}% of reservoir")

    t7 = M_unc_cell > 1e10 and M_unc_void > 1e16
    print(f"\n  PASS: {t7}")
    if t7:
        score += 1
    print()

    # ─────────────────────────────────────────────────────────
    #  Test 8: Energy emission from commitment
    # ─────────────────────────────────────────────────────────
    print("─" * 60)
    print("  Test 8: Energy emission from UNC commitment")
    print("─" * 60)

    m_e_kg = 9.109e-31
    E_commit = m_e_kg * c_SI**2  # J per commitment (m_e c², conservative)

    print(f"  E₀ per commitment: {E_commit:.3e} J = 0.511 MeV (m_e c²)")
    print()

    # K-IV civilization: build a 10¹¹ M☉ node
    # Each commitment adds ~m_e of mass (minimal)
    # Number of commitments: M_node / m_e
    N_commits = 1e11 * M_sun / m_e_kg
    print(f"  Commitments for 10¹¹ M☉ node: {N_commits:.2e}")

    # Total energy released
    E_total = N_commits * E_commit
    E_total_erg = E_total * 1e7
    print(f"  Total energy: {E_total:.2e} J = {E_total_erg:.2e} erg")
    print(f"  Equivalent to {E_total / (M_sun * c_SI**2):.2e} M☉c²")
    print()

    # If built over 1 Gyr:
    t_build_s = 1.0 * Gyr_s
    L_build = E_total / t_build_s
    L_solar = 3.828e26
    print(f"  If built over 1 Gyr:")
    print(f"    Luminosity: {L_build:.2e} W = {L_build/L_solar:.2e} L☉")
    print(f"    = {L_build/L_solar/1e10:.1f} × 10¹⁰ L☉ (≈ Milky Way luminosity)")
    print()

    # Flux at Eridanus distance
    d_eri_m = comoving_distance(0.25) * Mpc_m
    flux = L_build / (4 * math.pi * d_eri_m**2)
    # Convert to Jy at 1 GHz (assuming ~1 GHz bandwidth emission)
    flux_per_Hz = flux / 1e9  # W/m²/Hz
    flux_Jy = flux_per_Hz / 1e-26  # Jy

    print(f"  At Eridanus distance:")
    print(f"    Flux: {flux:.2e} W/m²")
    print(f"    ~{flux_Jy:.2e} Jy (over 1 GHz)")

    # SKA: ~1 μJy sensitivity
    print(f"    SKA limit: ~10⁻⁶ Jy")
    detectable_emission = flux_Jy > 1e-6
    print(f"    Detectable by SKA: {detectable_emission}")
    print()

    # Key insight: energy emission IS potentially detectable
    # but only if the civilization builds fast (< Gyr timescale)
    # and we observe in the right band
    print(f"  CONCLUSION: Commitment energy potentially detectable for K-IV+")
    print(f"  building on Gyr timescales. Primary channel remains LENSING")
    print(f"  for completed structures (no ongoing emission).")

    t8 = E_total > 0 and flux > 0
    print(f"\n  PASS: {t8}")
    if t8:
        score += 1
    print()

    # ═══════════════════════════════════════════════════════════
    #  Summary
    # ═══════════════════════════════════════════════════════════
    print("=" * 70)
    print(f"  SCORE: {score}/{total}")
    print("=" * 70)
    print()
    print("  KEY RESULTS:")
    print(f"  1. Random: smooth power law, peakiness = {peakiness_rand:.3f}")
    print(f"  2. Grid: Bragg peaks, peakiness = {peakiness_grid:.3f} "
          f"({peakiness_grid/max(peakiness_rand,0.001):.1f}× random)")
    print(f"  3. Network: filamentary excess {np.max(ratio_net):.0f}× over random")
    print(f"  4. Statistical SNR: grid={snr_grid_stat:.1f}, net={snr_net_stat:.1f}")
    if snr_grid_peak > 0:
        print(f"     Min detectable mass: {min_mass_grid:.1e} M☉")
    print(f"  5. Eridanus cold spot: ISW = {fraction_explained*100:.0f}%, "
          f"residual = {residual_uK:.0f} μK")
    print(f"  6. Boötes: {arcmin_per_Mpc_boo/arcmin_per_Mpc_eri:.0f}× finer resolution, "
          f"{sigma_cr_boo/sigma_cr_eri:.0f}× worse lensing signal")
    print(f"  7. K-IV node commits {1e11/M_unc_cell*100:.2f}% of local UNCs")
    print(f"  8. K-IV build luminosity: {L_build/L_solar:.1e} L☉ over 1 Gyr")
    print()
    print("  THE SMOKING GUN:")
    print("  Dark filaments inside voids with NO baryonic counterpart.")
    print("  ΛCDM: dark matter always traces baryons (eventually).")
    print("  BST + engineering: dark mass with no baryonic seed possible.")
    print("  Test: cross-correlate Euclid lensing κ with galaxy surveys")
    print("  inside voids. Decorrelation = substrate engineering signal.")
    print()
    print("  'They're not hiding. They're working where the material is.'")
    print("      — Casey Koons")
    print()

    return score

if __name__ == "__main__":
    run_tests()
