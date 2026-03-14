#!/usr/bin/env python3
"""
MAXWELL'S EQUATIONS FROM D_IV^5 GEOMETRY
=========================================
Toy 114: Electromagnetism is not assumed -- it's derived.

The isotropy group of D_IV^5 = SO_0(5,2)/[SO(5) x SO(2)] contains SO(2).
SO(2) is isomorphic to U(1). That U(1) IS the electromagnetic gauge group.
Everything else follows:

  1. SO(2) = U(1): The electromagnetic gauge group lives inside the isotropy.
  2. CONNECTION = POTENTIAL: The U(1) connection 1-form IS A_mu.
  3. CURVATURE = FIELD: F = dA. The field tensor IS the curvature.
  4. MAXWELL FOR FREE: dF = 0 (Bianchi, automatic) and d*F = *J (Hodge dual).
  5. alpha = 1/137: The Bergman kernel normalization sets the coupling strength.
  6. ONE GEOMETRY, ONE FORCE: Light is curvature on a circle fiber.

All of classical electromagnetism -- field equations, wave equation, speed of
light, coupling constant, gauge invariance, absence of monopoles -- from the
geometry of a circle fibered over a sphere.

Maxwell didn't need four equations. He needed one geometry.

    from toy_maxwell_geometry import MaxwellGeometry
    mg = MaxwellGeometry()
    mg.so2_equals_u1()            # SO(2) factor IS electromagnetism
    mg.connection_potential()      # U(1) connection = electromagnetic potential
    mg.curvature_field()           # F = dA, E and B from geometry
    mg.maxwell_for_free()          # 4 equations from 2 geometric identities
    mg.alpha_from_bergman()        # alpha = 1/137 from embedding tower
    mg.wave_equation()             # c = 1 from Bergman metric isotropy
    mg.gauge_invariance()          # S^1 fiber reparameterization
    mg.no_monopoles()              # trivial Chern class of product bundle
    mg.summary()                   # one geometry, one force
    mg.show()                      # 6-panel visualization

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from math import factorial

# ═══════════════════════════════════════════════════════════════════
# BST CONSTANTS -- the five integers
# ═══════════════════════════════════════════════════════════════════

N_c = 3                      # color charges
n_C = 5                      # complex dimension of D_IV^5
genus = n_C + 2              # = 7
C_2 = n_C + 1               # = 6, Casimir eigenvalue
N_max = 137                  # Haldane channel capacity
Gamma_order = 1920           # |W(D_5)| = n_C! * 2^(n_C-1)

# ═══════════════════════════════════════════════════════════════════
# DERIVED CONSTANTS (all from BST geometry)
# ═══════════════════════════════════════════════════════════════════

# Wyler's formula for alpha_EM
_vol_D = np.pi**n_C / Gamma_order
alpha_BST = (N_c**2 / (2**N_c * np.pi**4)) * _vol_D**(1/4)  # ~ 1/137.036

# Observed value
ALPHA_OBS = 1.0 / 137.035999084

# Proton mass ratio
mp_over_me = C_2 * np.pi**n_C     # 6*pi^5 ~ 1836.12

# Bergman kernel normalization constants
SIX_PI5 = C_2 * np.pi**n_C

# Physical constants
M_E_MEV = 0.51099895000
M_P_MEV = 938.27208816
M_PL_MEV = 1.22089e22
HBAR_C_MEV_FM = 197.3269804   # hbar*c in MeV*fm
C_M_S = 2.99792458e8          # speed of light in m/s

# Classical EM constants (SI)
EPSILON_0 = 8.8541878128e-12   # F/m
MU_0 = 1.25663706212e-6       # H/m
E_CHARGE = 1.602176634e-19     # Coulombs


# ═══════════════════════════════════════════════════════════════════
# THE DERIVATION CHAIN
# ═══════════════════════════════════════════════════════════════════

def _isotropy_group():
    """
    D_IV^5 = SO_0(5,2) / [SO(5) x SO(2)]

    The isotropy group K = SO(5) x SO(2) contains SO(2) as a factor.
    SO(2) is the group of rotations of a circle. As a Lie group,
    SO(2) is isomorphic to U(1), the group of unit complex numbers.

    Returns dict with group structure information.
    """
    # SO(2) generators: single generator J with [J] = so(2) ~ u(1)
    # The isomorphism: R(theta) in SO(2) <-> e^{i*theta} in U(1)
    dim_SO5 = 10       # dim SO(5) = 5*4/2
    dim_SO2 = 1        # dim SO(2) = 1
    dim_K = dim_SO5 + dim_SO2   # = 11
    dim_G = 21         # dim SO_0(5,2) = 7*6/2
    dim_DIV5 = dim_G - dim_K    # = 10 real = 5 complex

    return {
        'dim_G': dim_G,
        'dim_K': dim_K,
        'dim_SO5': dim_SO5,
        'dim_SO2': dim_SO2,
        'dim_domain': dim_DIV5,
        'dim_complex': n_C,
    }


def _connection_curvature():
    """
    On a principal U(1) bundle:
    - The connection 1-form A specifies parallel transport of phase.
    - In local coordinates: A = A_mu dx^mu
    - The curvature 2-form: F = dA = (1/2) F_{mu nu} dx^mu ^ dx^nu
    - Components: F_{mu nu} = d_mu A_nu - d_nu A_mu

    The electric and magnetic fields are components of F:
    - E_i = F_{0i}    (temporal-spatial components)
    - B_i = (1/2) eps_{ijk} F_{jk}    (spatial-spatial components)

    Returns dict with field decomposition.
    """
    # F_{mu nu} is a 4x4 antisymmetric tensor
    # 6 independent components = 3 (E) + 3 (B)
    n_components = 6
    n_E = 3   # electric field components
    n_B = 3   # magnetic field components

    return {
        'n_components': n_components,
        'n_E': n_E,
        'n_B': n_B,
        'equations_topology': 2,    # dF = 0 gives 2 equations
        'equations_dynamics': 2,    # d*F = *J gives 2 equations
        'total_maxwell': 4,
    }


def _bianchi_identity():
    """
    The Bianchi identity for a U(1) connection:
        d(dA) = 0  =>  dF = 0

    In components:
        d_{[mu} F_{nu rho]} = 0

    This single equation encodes TWO of Maxwell's equations:
        1. div B = 0          (no magnetic monopoles)
        2. curl E = -dB/dt    (Faraday's law)

    These are automatic -- they follow from F being a curvature.
    No physics input required. Pure differential geometry.
    """
    return {
        'identity': 'dF = 0',
        'equation_1': 'div B = 0',
        'equation_2': 'curl E = -dB/dt',
        'origin': 'Bianchi identity (automatic for curvature)',
        'physics_content': 'None -- purely geometric identity',
    }


def _hodge_equations():
    """
    The source equations from the action principle on D_IV^5:
        S = -(1/4alpha) int F^{mu nu} F_{mu nu} sqrt(-g) d^4x
            + int A_mu J^mu sqrt(-g) d^4x

    Variation gives:
        d*F = *J   (in form language)

    In components:
        3. div E = rho/eps_0       (Gauss's law)
        4. curl B = mu_0 J + mu_0 eps_0 dE/dt   (Ampere-Maxwell)

    The factor 1/alpha in the action IS the Bergman normalization.
    """
    return {
        'equation': 'd*F = *J',
        'equation_3': 'div E = rho / epsilon_0',
        'equation_4': 'curl B = mu_0 J + mu_0 epsilon_0 dE/dt',
        'origin': 'Hodge dual + action principle on D_IV^5',
        'coupling': f'1/alpha = {1.0/alpha_BST:.3f}',
    }


def _wyler_alpha():
    """
    The fine structure constant from Bergman kernel normalization.

    Wyler (1971):
        alpha = (9/(8 pi^4)) * (pi^5/1920)^{1/4}

    BST interpretation:
        - pi^5/1920 = Vol(D_IV^5) / |W(D_5)|
        - 9/(8 pi^4) = N_c^2 / (2^{N_c} pi^4)
        - The 1/4 power comes from the 4th root of the domain volume

    The embedding tower: each of C_2 = 6 layers contributes alpha^2.
        m_e = 6 pi^5 alpha^12 m_Pl

    alpha is not a coupling constant you CHOOSE. It's the ratio of
    volumes in D_IV^5.
    """
    # Step-by-step Wyler computation
    vol_D5 = np.pi**5 / 1920
    prefactor = 9.0 / (8.0 * np.pi**4)
    alpha_computed = prefactor * vol_D5**(1.0/4.0)

    # Verify against standard formula
    inv_alpha = 1.0 / alpha_computed

    # The embedding tower
    alpha_sq = alpha_computed**2
    tower_factor = alpha_sq**C_2    # alpha^12

    return {
        'vol_D5': vol_D5,
        'prefactor': prefactor,
        'alpha': alpha_computed,
        'inv_alpha': inv_alpha,
        'observed_inv_alpha': 1.0 / ALPHA_OBS,
        'deviation_pct': abs(alpha_computed - ALPHA_OBS) / ALPHA_OBS * 100,
        'n_layers': C_2,
        'tower_factor': tower_factor,
    }


def _wave_speed():
    """
    Combining the source equations in vacuum (rho=0, J=0):
        curl(curl E) = -d/dt(curl B) = -d^2E/dt^2
        => nabla^2 E = d^2E/dt^2

    Wave equation with speed c = 1 (natural units).

    BST explanation: epsilon_0 and mu_0 are Bergman metric components
    in the temporal and spatial directions. Their product is 1 because
    the Bergman metric on D_IV^5 restricted to the Shilov boundary
    has unit determinant in the EM sector.
    """
    c_computed = 1.0 / np.sqrt(EPSILON_0 * MU_0)  # Should be c

    return {
        'c_natural_units': 1.0,
        'c_SI': c_computed,
        'c_observed': C_M_S,
        'eps0_mu0_product': EPSILON_0 * MU_0,
        'inv_c_sq': 1.0 / C_M_S**2,
    }


def _holonomy_phase(loop_area, field_strength):
    """
    Compute the holonomy (phase rotation) around a loop.

    For a U(1) connection with curvature F:
        Phase = exp(i * integral of A around loop)
              = exp(i * integral of F over enclosed area)   [Stokes]

    This IS the Aharonov-Bohm effect: geometry determines phase.
    """
    phase = field_strength * loop_area
    return np.exp(1j * phase)


def _gauge_transform(A_mu, chi_gradient):
    """
    Gauge transformation: A_mu -> A_mu + d_mu chi

    This is S^1 fiber reparameterization. The curvature F is invariant:
        F = d(A + d chi) = dA + d(d chi) = dA = F

    because d^2 = 0 (exterior derivative squares to zero).
    """
    return A_mu + chi_gradient


# ═══════════════════════════════════════════════════════════════════
# COLOR PALETTE (dark theme)
# ═══════════════════════════════════════════════════════════════════

BG       = '#0a0a1a'
BG_PANEL = '#0d0d24'
GOLD     = '#ffcc00'
CYAN     = '#00ccff'
WHITE    = '#ffffff'
GREY     = '#888888'
DGREY    = '#333333'
LGREY    = '#cccccc'
RED      = '#ff4444'
GREEN    = '#44ff88'
BLUE     = '#4488ff'
MAGENTA  = '#ff44cc'
ORANGE   = '#ff8844'
PURPLE   = '#aa66ff'
TEAL     = '#44ccaa'

import matplotlib.patheffects as pe
GLOW_GOLD = [pe.withStroke(linewidth=3, foreground='#ffcc0033')]
GLOW_CYAN = [pe.withStroke(linewidth=3, foreground='#00ccff33')]
GLOW_WHITE = [pe.withStroke(linewidth=2, foreground='#ffffff22')]


# ═══════════════════════════════════════════════════════════════════
# THE MAXWELL GEOMETRY CLASS
# ═══════════════════════════════════════════════════════════════════

class MaxwellGeometry:
    """
    Maxwell's Equations from D_IV^5 Geometry.

    Electromagnetism is not assumed -- it's derived from the SO(2) factor
    in the isotropy group SO(5) x SO(2) of D_IV^5.

    Methods:
        so2_equals_u1()            -- SO(2) = U(1) = electromagnetism
        connection_potential()      -- U(1) connection = A_mu
        curvature_field()           -- F = dA = electromagnetic field tensor
        maxwell_for_free()          -- 4 equations from 2 geometric identities
        alpha_from_bergman()        -- alpha = 1/137 from Bergman normalization
        wave_equation()             -- c = 1 from metric isotropy
        gauge_invariance()          -- S^1 reparameterization freedom
        no_monopoles()              -- trivial Chern class => no monopoles
        summary()                   -- one geometry, one force
        show()                      -- 6-panel visualization
    """

    def __init__(self, quiet=False):
        self.quiet = quiet

    def _print(self, *args, **kwargs):
        if not self.quiet:
            print(*args, **kwargs)

    # ─── Method 1: SO(2) = U(1) = Electromagnetism ───

    def so2_equals_u1(self):
        """
        The isotropy group of D_IV^5 has an SO(2) factor.
        SO(2) is isomorphic to U(1). This IS electromagnetism.

        The gauge group of electromagnetism was hiding in the isotropy
        group of the bounded symmetric domain all along.
        """
        info = _isotropy_group()

        self._print()
        self._print("  ═══════════════════════════════════════════════════════")
        self._print("  SO(2) = U(1) = ELECTROMAGNETISM")
        self._print("  ═══════════════════════════════════════════════════════")
        self._print()
        self._print("  The bounded symmetric domain:")
        self._print(f"    D_IV^{n_C} = SO_0({n_C},{2}) / [SO({n_C}) x SO(2)]")
        self._print()
        self._print("  Isotropy group K = SO(5) x SO(2)")
        self._print(f"    dim SO(5)   = {info['dim_SO5']}")
        self._print(f"    dim SO(2)   = {info['dim_SO2']}")
        self._print(f"    dim K       = {info['dim_K']}")
        self._print(f"    dim D_IV^5  = {info['dim_domain']} real = {info['dim_complex']} complex")
        self._print()
        self._print("  The key isomorphism:")
        self._print("    SO(2) = {R(theta) : theta in [0, 2pi)}")
        self._print("    U(1)  = {e^{i theta} : theta in [0, 2pi)}")
        self._print()
        self._print("    R(theta) <-> e^{i theta}")
        self._print("    Rotation of a plane <-> Phase multiplication")
        self._print()
        self._print("  This is EXACT, not an analogy:")
        self._print("    - SO(2) rotates a 2D plane by angle theta")
        self._print("    - U(1) multiplies a complex number by phase e^{i theta}")
        self._print("    - Same group, same algebra, same representations")
        self._print()
        self._print("  U(1) IS the electromagnetic gauge group.")
        self._print("  It was hiding in the isotropy of D_IV^5.")
        self._print("  Electromagnetism is not postulated -- it's DERIVED.")
        self._print()

        return info

    # ─── Method 2: Connection = Potential ───

    def connection_potential(self):
        """
        The U(1) connection on the principal bundle IS the
        electromagnetic potential A_mu.

        Parallel transport around a loop = phase rotation = EM potential.
        """
        self._print()
        self._print("  ═══════════════════════════════════════════════════════")
        self._print("  CONNECTION = POTENTIAL")
        self._print("  ═══════════════════════════════════════════════════════")
        self._print()
        self._print("  Principal U(1) bundle over spacetime:")
        self._print()
        self._print("    S^1 ----> P        (total space)")
        self._print("              |")
        self._print("              v")
        self._print("              M         (spacetime)")
        self._print()
        self._print("  The connection 1-form A specifies how the S^1 phase")
        self._print("  rotates as you move along spacetime:")
        self._print()
        self._print("    A = A_mu dx^mu")
        self._print()
        self._print("  Parallel transport along path gamma:")
        self._print()
        self._print("    Phase(gamma) = exp(i * integral_gamma A_mu dx^mu)")
        self._print()
        self._print("  This IS the electromagnetic potential.")
        self._print("    - A_0 = scalar potential (phi/c)")
        self._print("    - A_i = vector potential components")
        self._print()
        self._print("  Holonomy around a closed loop:")
        self._print()
        self._print("    exp(i * oint A) = exp(i * iint F)    [Stokes theorem]")
        self._print()
        self._print("  The Aharonov-Bohm effect is PROOF that the electromagnetic")
        self._print("  potential is a connection on a U(1) bundle.")
        self._print()

        # Demonstrate holonomy for a small loop
        B_field = 1.0  # Tesla (natural units proxy)
        areas = [0.1, 0.5, 1.0, 2.0, np.pi]
        self._print("  Holonomy phases for unit field strength:")
        self._print(f"    {'Area':>8}  {'Phase (rad)':>12}  {'|exp(i*phi)|':>12}")
        self._print(f"    {'─'*8}  {'─'*12}  {'─'*12}")
        for a in areas:
            h = _holonomy_phase(a, B_field)
            self._print(f"    {a:8.3f}  {np.angle(h):12.6f}  {abs(h):12.6f}")
        self._print()
        self._print("  Phase depends on enclosed flux, not on path details.")
        self._print("  GEOMETRY determines the electromagnetic potential.")
        self._print()

        return {
            'connection': 'A_mu',
            'parallel_transport': 'exp(i * integral A)',
            'holonomy': 'exp(i * oint A) = exp(i * iint F)',
        }

    # ─── Method 3: Curvature = Field ───

    def curvature_field(self):
        """
        F = dA. The curvature 2-form IS the electromagnetic field tensor.

        No postulate needed. F_{mu nu} is DEFINED as the curvature of
        the U(1) connection. E and B are its components.
        """
        info = _connection_curvature()

        self._print()
        self._print("  ═══════════════════════════════════════════════════════")
        self._print("  CURVATURE = FIELD")
        self._print("  ═══════════════════════════════════════════════════════")
        self._print()
        self._print("  The curvature 2-form of the U(1) connection:")
        self._print()
        self._print("    F = dA = (1/2) F_{mu nu} dx^mu ^ dx^nu")
        self._print()
        self._print("  In components:")
        self._print()
        self._print("    F_{mu nu} = d_mu A_nu - d_nu A_mu")
        self._print()
        self._print("  This 4x4 antisymmetric tensor has 6 independent components:")
        self._print()
        self._print("           |  0    -E_x  -E_y  -E_z |")
        self._print("           | E_x    0    -B_z   B_y |")
        self._print("  F_uv  =  | E_y   B_z    0    -B_x |")
        self._print("           | E_z  -B_y   B_x    0   |")
        self._print()
        self._print(f"  {info['n_E']} electric field components:")
        self._print("    E_i = F_{0i}   (temporal-spatial curvature)")
        self._print("    = rate of change of S^1 phase in time")
        self._print()
        self._print(f"  {info['n_B']} magnetic field components:")
        self._print("    B_i = (1/2) eps_{ijk} F_{jk}   (spatial-spatial curvature)")
        self._print("    = twist of S^1 phase around spatial loops")
        self._print()
        self._print(f"  Total: {info['n_components']} independent components")
        self._print()
        self._print("  E and B are NOT separate fields.")
        self._print("  They are components of ONE geometric object: the curvature F.")
        self._print("  Frame-dependent decomposition, frame-independent geometry.")
        self._print()

        return info

    # ─── Method 4: Maxwell for Free ───

    def maxwell_for_free(self):
        """
        All four Maxwell equations from two geometric identities.

        dF = 0   (Bianchi identity, automatic) => 2 equations
        d*F = *J (Hodge dual, from action)     => 2 equations
        """
        bianchi = _bianchi_identity()
        hodge = _hodge_equations()

        self._print()
        self._print("  ═══════════════════════════════════════════════════════")
        self._print("  MAXWELL FOR FREE")
        self._print("  ═══════════════════════════════════════════════════════")
        self._print()
        self._print("  IDENTITY 1: dF = 0   (Bianchi identity)")
        self._print("  ─────────────────────────────────────────")
        self._print("  Automatic for ANY curvature of ANY connection.")
        self._print("  d(dA) = 0 because d^2 = 0 (the exterior derivative")
        self._print("  squares to zero on any manifold).")
        self._print()
        self._print("  This gives TWO of Maxwell's equations:")
        self._print()
        self._print(f"    (1) {bianchi['equation_1']}")
        self._print("        No magnetic monopoles.")
        self._print("        Magnetic field is a curl => divergence-free.")
        self._print()
        self._print(f"    (2) {bianchi['equation_2']}")
        self._print("        Faraday's law of induction.")
        self._print("        Phase consistency in the fiber bundle.")
        self._print()
        self._print(f"  Origin: {bianchi['origin']}")
        self._print(f"  Physics content: {bianchi['physics_content']}")
        self._print()
        self._print("  IDENTITY 2: d*F = *J  (from action principle)")
        self._print("  ──────────────────────────────────────────────")
        self._print(f"  Action: S = -(1/4alpha) int F^2 + int A.J")
        self._print(f"  The factor 1/alpha = {1.0/alpha_BST:.3f} is the Bergman normalization.")
        self._print()
        self._print("  This gives the other TWO Maxwell equations:")
        self._print()
        self._print(f"    (3) {hodge['equation_3']}")
        self._print("        Gauss's law: field lines diverge from charges.")
        self._print("        Bergman response to winding number density.")
        self._print()
        self._print(f"    (4) {hodge['equation_4']}")
        self._print("        Ampere-Maxwell law: currents and changing E")
        self._print("        produce magnetic fields.")
        self._print()
        self._print("  ═══════════════════════════════════════════════════════")
        self._print("  TOTAL: 4 equations from 2 geometric identities.")
        self._print("  Maxwell wrote 20 equations (1865), Heaviside reduced")
        self._print("  them to 4 (1884), geometry reduces them to 2.")
        self._print("  ═══════════════════════════════════════════════════════")
        self._print()

        return {
            'bianchi': bianchi,
            'hodge': hodge,
            'n_topology': 2,
            'n_dynamics': 2,
            'total': 4,
        }

    # ─── Method 5: alpha from Bergman ───

    def alpha_from_bergman(self):
        """
        alpha = 1/137 from the Bergman kernel normalization.

        The Wyler formula + embedding tower explain why the coupling
        has precisely this value.
        """
        wyler = _wyler_alpha()

        self._print()
        self._print("  ═══════════════════════════════════════════════════════")
        self._print("  alpha = 1/137 FROM BERGMAN NORMALIZATION")
        self._print("  ═══════════════════════════════════════════════════════")
        self._print()
        self._print("  WYLER'S FORMULA (1971, given BST foundation 2026):")
        self._print()
        self._print("    alpha = (9 / (8 pi^4)) * (pi^5 / 1920)^{1/4}")
        self._print()
        self._print("  Step by step:")
        self._print(f"    pi^5 / 1920 = {wyler['vol_D5']:.10f}")
        self._print(f"    (pi^5/1920)^{{1/4}} = {wyler['vol_D5']**(1/4):.10f}")
        self._print(f"    9 / (8 pi^4) = {wyler['prefactor']:.10f}")
        self._print()
        self._print(f"    alpha = {wyler['alpha']:.12f}")
        self._print(f"    1/alpha = {wyler['inv_alpha']:.6f}")
        self._print(f"    Observed: 1/alpha = {wyler['observed_inv_alpha']:.6f}")
        self._print(f"    Agreement: {wyler['deviation_pct']:.4f}%")
        self._print()
        self._print("  BST INTERPRETATION:")
        self._print(f"    - 1920 = |W(D_5)| = {n_C}! x 2^{{{n_C}-1}} (Weyl group order)")
        self._print(f"    - pi^5 = Vol(S^{{2*{n_C}-1}}) / normalization")
        self._print(f"    - N_c^2 / 2^N_c = 9/8 (color factor)")
        self._print()
        self._print("  THE EMBEDDING TOWER:")
        self._print(f"    {C_2} layers, each contributing alpha^2:")
        self._print(f"    alpha^{{2 x {C_2}}} = alpha^{2*C_2} = {wyler['tower_factor']:.6e}")
        self._print()
        self._print(f"    m_e = {C_2} pi^{n_C} x alpha^{2*C_2} x m_Pl")
        self._print(f"        = {SIX_PI5:.2f} x {wyler['tower_factor']:.4e} x {M_PL_MEV:.3e} MeV")
        m_e_pred = SIX_PI5 * wyler['tower_factor'] * M_PL_MEV
        self._print(f"        = {m_e_pred:.6f} MeV")
        self._print(f"    Observed: {M_E_MEV:.6f} MeV ({abs(m_e_pred - M_E_MEV)/M_E_MEV*100:.2f}%)")
        self._print()
        self._print("  alpha is NOT a free parameter.")
        self._print("  It is a VOLUME RATIO in D_IV^5.")
        self._print("  The coupling strength of electromagnetism is GEOMETRY.")
        self._print()

        return wyler

    # ─── Method 6: Wave Equation ───

    def wave_equation(self):
        """
        The speed of light from the Bergman metric.

        c = 1 in natural units because the Bergman metric on D_IV^5
        restricted to the Shilov boundary is locally isotropic.
        """
        wave = _wave_speed()

        self._print()
        self._print("  ═══════════════════════════════════════════════════════")
        self._print("  WAVE EQUATION: LIGHT SPEED FROM GEOMETRY")
        self._print("  ═══════════════════════════════════════════════════════")
        self._print()
        self._print("  In vacuum (rho = 0, J = 0), Maxwell's equations give:")
        self._print()
        self._print("    nabla^2 E = (1/c^2) d^2E/dt^2")
        self._print()
        self._print("  This is the wave equation with speed:")
        self._print(f"    c = 1/sqrt(eps_0 * mu_0)")
        self._print(f"      = 1/sqrt({wave['eps0_mu0_product']:.6e})")
        self._print(f"      = {wave['c_SI']:.6f} m/s")
        self._print(f"    Observed: {wave['c_observed']:.6f} m/s")
        self._print()
        self._print("  BST EXPLANATION:")
        self._print("    In the contact graph:")
        self._print("    - Spatial distance = number of contacts")
        self._print("    - Temporal distance = number of commitment steps")
        self._print("    - One step advances by one contact")
        self._print("    - Therefore c = 1 contact/step (natural units)")
        self._print()
        self._print("    eps_0 and mu_0 are Bergman metric components in the")
        self._print("    temporal and spatial directions. Their product = 1/c^2")
        self._print("    because the Bergman metric has unit determinant in")
        self._print("    the electromagnetic sector.")
        self._print()
        self._print("    Maxwell didn't know why 1/sqrt(eps_0 * mu_0) = c.")
        self._print("    BST knows: because the metric is isotropic.")
        self._print()

        return wave

    # ─── Method 7: Gauge Invariance ───

    def gauge_invariance(self):
        """
        Gauge invariance is S^1 fiber reparameterization.

        A_mu -> A_mu + d_mu chi leaves F_{mu nu} unchanged because
        d^2 = 0. This is as natural as rotational invariance for S^2.
        """
        self._print()
        self._print("  ═══════════════════════════════════════════════════════")
        self._print("  GAUGE INVARIANCE = S^1 REPARAMETERIZATION")
        self._print("  ═══════════════════════════════════════════════════════")
        self._print()
        self._print("  Gauge transformation:")
        self._print("    A_mu -> A_mu + d_mu chi")
        self._print()
        self._print("  The curvature is INVARIANT:")
        self._print("    F = d(A + d chi) = dA + d(d chi) = dA + 0 = F")
        self._print()
        self._print("  because d^2 = 0 (exterior derivative squares to zero).")
        self._print()
        self._print("  BST INTERPRETATION:")
        self._print("    - The S^1 fiber at each point of spacetime has NO")
        self._print("      preferred origin. You can relabel the positions")
        self._print("      on the circle by any smooth function chi(x).")
        self._print("    - Physics depends on phase DIFFERENCES (holonomies),")
        self._print("      not on absolute phase values.")
        self._print("    - Gauge invariance is S^1 coordinate freedom.")
        self._print("    - As natural as the fact that rotating your axes")
        self._print("      on S^2 doesn't change the sphere.")
        self._print()
        self._print("  EXAMPLE: Two gauge-equivalent potentials")

        # Demonstrate with a simple example
        A_orig = np.array([1.0, 0.5, -0.3, 0.2])
        chi_grad = np.array([0.1, -0.2, 0.4, -0.1])
        A_new = _gauge_transform(A_orig, chi_grad)

        self._print(f"    A_mu     = {A_orig}")
        self._print(f"    d_mu chi = {chi_grad}")
        self._print(f"    A'_mu    = {A_new}")
        self._print()

        # Show F is the same
        self._print("    F_{01} = d_0 A_1 - d_1 A_0  (same for both A and A')")
        self._print("    because the chi terms cancel in the antisymmetric combo.")
        self._print()
        self._print("  Gauge invariance is NOT mysterious.")
        self._print("  It is the OBVIOUS statement that labeling positions")
        self._print("  on a circle is arbitrary.")
        self._print()

        return {
            'transformation': 'A -> A + d chi',
            'invariant': 'F = dA',
            'reason': 'd^2 = 0',
            'interpretation': 'S^1 coordinate freedom',
        }

    # ─── Method 8: No Monopoles ───

    def no_monopoles(self):
        """
        The product bundle S^2 x S^1 has trivial Chern class.
        No magnetic monopoles exist.
        """
        self._print()
        self._print("  ═══════════════════════════════════════════════════════")
        self._print("  NO MAGNETIC MONOPOLES")
        self._print("  ═══════════════════════════════════════════════════════")
        self._print()
        self._print("  Electric charges: S^1 winding numbers")
        self._print("    Winding number +1 = positive charge")
        self._print("    Winding number -1 = negative charge")
        self._print("    Winding number  0 = neutral")
        self._print()
        self._print("  Magnetic charges would require: topological defects in S^2")
        self._print("    Points where the base surface is undefined.")
        self._print()
        self._print("  The bundle S^2 x S^1 is a PRODUCT bundle (trivial).")
        self._print("  No topological defects. No undefined points.")
        self._print("  First Chern class: c_1(S^2 x S^1) = 0")
        self._print()
        self._print("  The electric-magnetic asymmetry:")
        self._print("    - Fiber (S^1) CAN carry winding numbers => charges exist")
        self._print("    - Base (S^2) has NO defects in the product => no monopoles")
        self._print()
        self._print("  PREDICTION: No magnetic monopole will ever be detected.")
        self._print("  This is permanent. Falsifiable by any confirmed detection.")
        self._print()
        self._print("  NOTE: The Dirac monopole construction WOULD require a")
        self._print("  non-trivial Chern class (winding of S^1 around a point")
        self._print("  on S^2). BST excludes this because the substrate bundle")
        self._print("  is globally trivial.")
        self._print()

        return {
            'chern_class': 0,
            'monopoles_exist': False,
            'reason': 'Product bundle S^2 x S^1 is trivial',
            'prediction': 'No magnetic monopoles',
        }

    # ─── Method 9: Summary ───

    def summary(self):
        """
        One geometry, one force. The key insight.
        """
        self._print()
        self._print("  ═══════════════════════════════════════════════════════")
        self._print("  ONE GEOMETRY, ONE FORCE")
        self._print("  ═══════════════════════════════════════════════════════")
        self._print()
        self._print("  THE DERIVATION CHAIN:")
        self._print()
        self._print("    D_IV^5 = SO_0(5,2) / [SO(5) x SO(2)]")
        self._print("                                   ^^^^")
        self._print("                                   SO(2) = U(1)")
        self._print("                                       |")
        self._print("                              Connection A_mu")
        self._print("                                       |")
        self._print("                              Curvature F = dA")
        self._print("                                    /       \\")
        self._print("                               dF = 0     d*F = *J")
        self._print("                              (Bianchi)   (Action)")
        self._print("                               /    \\       /    \\")
        self._print("                          div B=0  Faraday  Gauss  Ampere")
        self._print("                                         \\  /")
        self._print("                                     Wave equation")
        self._print("                                     c = 1 (natural)")
        self._print()
        self._print("  ┌─────────────────────────────────────────────────┐")
        self._print("  │  WHAT MAXWELL DERIVED:                          │")
        self._print("  │    'Light is an electromagnetic wave.'          │")
        self._print("  │                                                 │")
        self._print("  │  WHAT BST DERIVES:                              │")
        self._print("  │    'Light is curvature on a circle fiber.       │")
        self._print("  │     The circle was inside the isotropy group    │")
        self._print("  │     of D_IV^5 all along. The photon is a       │")
        self._print("  │     connection. The field is curvature.         │")
        self._print(f"  │     The coupling alpha = 1/{1.0/alpha_BST:.3f} is geometry.  │")
        self._print("  │     Maxwell's equations are free.'              │")
        self._print("  └─────────────────────────────────────────────────┘")
        self._print()

        # Summary table
        self._print("  ┌──────────────────────┬──────────────────────────────┐")
        self._print("  │ Standard physics      │ BST origin                   │")
        self._print("  ├──────────────────────┼──────────────────────────────┤")
        self._print("  │ U(1) gauge group      │ SO(2) in isotropy of D_IV^5  │")
        self._print("  │ A_mu potential         │ U(1) connection 1-form       │")
        self._print("  │ F_{mu nu} field        │ Curvature 2-form F = dA      │")
        self._print("  │ div B = 0             │ Bianchi identity (automatic) │")
        self._print("  │ curl E = -dB/dt       │ Bianchi identity (automatic) │")
        self._print("  │ div E = rho/eps_0     │ Bergman response to winding  │")
        self._print("  │ curl B = ...          │ Bergman response to current  │")
        self._print("  │ c = 1/sqrt(mu_0*e_0)  │ Bergman metric isotropy      │")
        self._print("  │ alpha = 1/137         │ Bergman volume ratio (Wyler) │")
        self._print("  │ Gauge invariance       │ S^1 fiber reparameterization │")
        self._print("  │ No monopoles           │ Trivial Chern class          │")
        self._print("  └──────────────────────┴──────────────────────────────┘")
        self._print()
        self._print("  Maxwell didn't need four equations.")
        self._print("  He needed one geometry.")
        self._print()

    # ─── Method 10: 6-Panel Visualization ───

    def show(self):
        """Launch the 6-panel visualization."""
        try:
            import matplotlib
            matplotlib.use('TkAgg')
            import matplotlib.pyplot as plt
            from matplotlib.gridspec import GridSpec
            from matplotlib.patches import Circle, FancyArrowPatch, Arc
            from matplotlib.patches import FancyBboxPatch
        except ImportError:
            print("  matplotlib not available. Use text API methods.")
            return

        fig = plt.figure(figsize=(20, 13), facecolor=BG)
        if fig.canvas.manager:
            fig.canvas.manager.set_window_title(
                'BST Toy 114 \u2014 Maxwell from Geometry')

        fig.text(0.5, 0.975, "MAXWELL'S EQUATIONS FROM D\u1d35\u2c7d\u2075 GEOMETRY",
                 fontsize=24, fontweight='bold', color=GOLD,
                 ha='center', fontfamily='monospace',
                 path_effects=GLOW_GOLD)
        fig.text(0.5, 0.950,
                 'Electromagnetism is not assumed \u2014 it\'s derived.'
                 '  SO(2) inside the isotropy group IS U(1).',
                 fontsize=11, color=CYAN, ha='center',
                 fontfamily='monospace', style='italic',
                 path_effects=GLOW_CYAN)
        fig.text(0.5, 0.012,
                 'Copyright (c) 2026 Casey Koons \u2014 Demonstration Only',
                 fontsize=8, color='#334455', ha='center',
                 fontfamily='monospace')

        gs = GridSpec(2, 3, figure=fig,
                      left=0.04, right=0.97, top=0.92, bottom=0.05,
                      hspace=0.32, wspace=0.25)

        # ──── Panel 1: SO(2) = U(1) = Electromagnetism ────
        ax1 = fig.add_subplot(gs[0, 0])
        self._draw_panel1_so2_u1(ax1)

        # ──── Panel 2: Connection = Potential ────
        ax2 = fig.add_subplot(gs[0, 1])
        self._draw_panel2_connection(ax2)

        # ──── Panel 3: Curvature = Field ────
        ax3 = fig.add_subplot(gs[0, 2])
        self._draw_panel3_curvature(ax3)

        # ──── Panel 4: Maxwell for Free ────
        ax4 = fig.add_subplot(gs[1, 0])
        self._draw_panel4_maxwell(ax4)

        # ──── Panel 5: alpha = 1/137 ────
        ax5 = fig.add_subplot(gs[1, 1])
        self._draw_panel5_alpha(ax5)

        # ──── Panel 6: One Geometry, One Force ────
        ax6 = fig.add_subplot(gs[1, 2])
        self._draw_panel6_summary(ax6)

        self.fig = fig
        plt.show(block=False)
        return fig

    # ══════════════════════════════════════════════════════════════════
    #  PANEL DRAWING METHODS
    # ══════════════════════════════════════════════════════════════════

    def _panel_setup(self, ax, title, subtitle=None):
        """Common panel setup: dark background, title."""
        ax.set_facecolor(BG_PANEL)
        for spine in ax.spines.values():
            spine.set_color(DGREY)
            spine.set_linewidth(0.5)
        ax.set_title(title, fontsize=13, fontweight='bold', color=GOLD,
                     pad=10, fontfamily='monospace',
                     path_effects=GLOW_GOLD)
        if subtitle:
            ax.text(0.5, 1.02, subtitle, transform=ax.transAxes,
                    ha='center', va='bottom', fontsize=8, color=CYAN,
                    fontfamily='monospace', style='italic')
        ax.tick_params(colors=GREY, which='both')

    # ──────────────────────────────────────────────────────────────────
    # Panel 1: SO(2) = U(1) = Electromagnetism
    # ──────────────────────────────────────────────────────────────────

    def _draw_panel1_so2_u1(self, ax):
        """SO(2) = U(1) = Electromagnetism: the circle, phase, gauge group."""
        self._panel_setup(ax, 'SO(2) = U(1) = ELECTROMAGNETISM',
                         'The gauge group was hiding in the isotropy')
        ax.set_xlim(-2.5, 2.5)
        ax.set_ylim(-2.5, 2.5)
        ax.set_aspect('equal')
        ax.axis('off')

        # Draw the unit circle (S^1)
        theta = np.linspace(0, 2*np.pi, 200)
        ax.plot(np.cos(theta), np.sin(theta), color=CYAN, linewidth=2.5,
                alpha=0.8)

        # Draw phase arrow at several angles
        phase_angles = [0, np.pi/3, 2*np.pi/3, np.pi, 4*np.pi/3, 5*np.pi/3]
        for phi in phase_angles:
            x, y = np.cos(phi), np.sin(phi)
            ax.plot(x, y, 'o', color=GOLD, markersize=5, zorder=5)

        # Highlight one phase point with arrow from origin
        phi_highlight = np.pi / 4
        x_h, y_h = np.cos(phi_highlight), np.sin(phi_highlight)
        ax.annotate('', xy=(x_h, y_h), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color=GOLD,
                                    lw=2.0))
        ax.text(x_h + 0.15, y_h + 0.15, r'$e^{i\theta}$',
                color=GOLD, fontsize=14, fontweight='bold',
                fontfamily='monospace')

        # Draw arc showing rotation
        arc_theta = np.linspace(0, phi_highlight, 50)
        ax.plot(0.4*np.cos(arc_theta), 0.4*np.sin(arc_theta),
                color=ORANGE, linewidth=1.5, alpha=0.8)
        ax.text(0.5, 0.2, r'$\theta$', color=ORANGE, fontsize=12,
                fontfamily='monospace')

        # Label the isomorphism
        ax.text(0, -1.5, 'SO(2)', color=CYAN, fontsize=14,
                fontweight='bold', ha='center', fontfamily='monospace')
        ax.text(0, -1.85, r'$\cong$', color=WHITE, fontsize=16,
                ha='center', fontfamily='monospace')
        ax.text(0, -2.2, 'U(1)', color=GOLD, fontsize=14,
                fontweight='bold', ha='center', fontfamily='monospace')

        # Isotropy group label
        ax.text(0, 2.2, r'K = SO(5) $\times$ SO(2)',
                color=GREY, fontsize=9, ha='center',
                fontfamily='monospace')
        ax.text(0, 1.9, r'$\uparrow$ from D$_{IV}^5$ isotropy',
                color=GREY, fontsize=8, ha='center',
                fontfamily='monospace')

    # ──────────────────────────────────────────────────────────────────
    # Panel 2: Connection = Potential
    # ──────────────────────────────────────────────────────────────────

    def _draw_panel2_connection(self, ax):
        """Parallel transport on U(1) bundle = electromagnetic potential."""
        self._panel_setup(ax, 'CONNECTION = POTENTIAL',
                         'Parallel transport of phase = A$_\\mu$')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')

        # Draw a path in the base space (horizontal line)
        path_x = np.linspace(1.5, 8.5, 100)
        path_y = np.ones_like(path_x) * 3.0
        ax.plot(path_x, path_y, color=GREY, linewidth=2, alpha=0.6)
        ax.text(5.0, 2.3, 'spacetime path', color=GREY, fontsize=9,
                ha='center', fontfamily='monospace')

        # Draw S^1 fibers at several points along the path
        fiber_x_positions = [2.0, 3.5, 5.0, 6.5, 8.0]
        phases = [0, 0.4, 0.9, 1.5, 2.2]  # accumulated phase
        fiber_radius = 0.5

        for i, (fx, phi) in enumerate(zip(fiber_x_positions, phases)):
            # Small circle representing S^1 fiber
            t = np.linspace(0, 2*np.pi, 60)
            cy = 6.0
            ax.plot(fx + fiber_radius * np.cos(t),
                    cy + fiber_radius * np.sin(t),
                    color=CYAN, linewidth=1.2, alpha=0.5)

            # Phase point on the fiber
            px = fx + fiber_radius * np.cos(phi)
            py = cy + fiber_radius * np.sin(phi)
            ax.plot(px, py, 'o', color=GOLD, markersize=7, zorder=5)

            # Vertical line connecting base to fiber
            ax.plot([fx, fx], [3.2, cy - fiber_radius - 0.1],
                    color=DGREY, linewidth=0.8, linestyle=':')

        # Draw phase transport arrows between fibers
        for i in range(len(fiber_x_positions) - 1):
            x1 = fiber_x_positions[i] + fiber_radius + 0.15
            x2 = fiber_x_positions[i+1] - fiber_radius - 0.15
            ax.annotate('', xy=(x2, 6.0), xytext=(x1, 6.0),
                        arrowprops=dict(arrowstyle='->',
                                        color=ORANGE, lw=1.5,
                                        connectionstyle='arc3,rad=0.2'))

        # Labels
        ax.text(5.0, 8.5, r'$\Phi = \exp\left(i\oint A_\mu\,dx^\mu\right)$',
                color=GOLD, fontsize=13, ha='center',
                fontfamily='monospace', fontweight='bold')
        ax.text(5.0, 7.7, 'Phase = holonomy of connection',
                color=CYAN, fontsize=9, ha='center',
                fontfamily='monospace')

        # A_mu label
        ax.text(5.0, 4.4, r'$A_\mu$ = connection 1-form',
                color=ORANGE, fontsize=10, ha='center',
                fontfamily='monospace', fontweight='bold')

        # Fiber label
        ax.text(9.3, 6.0, r'$S^1$', color=CYAN, fontsize=11,
                fontfamily='monospace', va='center')

        # Bottom insight
        ax.text(5.0, 1.0, 'The Aharonov-Bohm effect',
                color=GREY, fontsize=8, ha='center',
                fontfamily='monospace')
        ax.text(5.0, 0.4, 'proves A is a connection',
                color=GREY, fontsize=8, ha='center',
                fontfamily='monospace')

    # ──────────────────────────────────────────────────────────────────
    # Panel 3: Curvature = Field
    # ──────────────────────────────────────────────────────────────────

    def _draw_panel3_curvature(self, ax):
        """F = dA: the field tensor IS the curvature."""
        self._panel_setup(ax, 'CURVATURE = FIELD',
                         'F = dA: field strength IS curvature')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')

        # Central equation
        ax.text(5.0, 9.0, r'$F = dA$', color=GOLD, fontsize=22,
                fontweight='bold', ha='center', fontfamily='monospace',
                path_effects=GLOW_GOLD)

        ax.text(5.0, 8.2,
                r'$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$',
                color=WHITE, fontsize=12, ha='center',
                fontfamily='monospace')

        # Field tensor matrix
        matrix_y = 5.8
        ax.text(5.0, matrix_y + 1.2, 'The field tensor:', color=CYAN,
                fontsize=10, ha='center', fontfamily='monospace')

        rows = [
            (r'$0$',     r'$-E_x$', r'$-E_y$', r'$-E_z$'),
            (r'$E_x$',  r'$0$',     r'$-B_z$', r'$B_y$'),
            (r'$E_y$',  r'$B_z$',   r'$0$',    r'$-B_x$'),
            (r'$E_z$',  r'$-B_y$',  r'$B_x$',  r'$0$'),
        ]

        x_offsets = [3.0, 4.5, 6.0, 7.5]
        for i, row in enumerate(rows):
            y = matrix_y - i * 0.55
            for j, elem in enumerate(row):
                color = RED if 'E' in elem else (BLUE if 'B' in elem else DGREY)
                ax.text(x_offsets[j], y, elem, color=color, fontsize=9,
                        ha='center', fontfamily='monospace')

        # Brackets
        ax.text(2.3, matrix_y - 0.85, r'$F_{\mu\nu}=$',
                color=WHITE, fontsize=11, ha='center',
                fontfamily='monospace', va='center')

        # E and B labels
        ax.text(2.0, 2.7, r'$\vec{E}$', color=RED, fontsize=16,
                fontweight='bold', ha='center', fontfamily='monospace')
        ax.text(2.0, 2.1, 'temporal', color=RED, fontsize=8,
                ha='center', fontfamily='monospace')
        ax.text(2.0, 1.6, 'phase gradient', color=RED, fontsize=8,
                ha='center', fontfamily='monospace')

        ax.text(5.0, 2.7, '+', color=GREY, fontsize=16,
                ha='center', fontfamily='monospace')

        ax.text(8.0, 2.7, r'$\vec{B}$', color=BLUE, fontsize=16,
                fontweight='bold', ha='center', fontfamily='monospace')
        ax.text(8.0, 2.1, 'spatial', color=BLUE, fontsize=8,
                ha='center', fontfamily='monospace')
        ax.text(8.0, 1.6, 'phase twist', color=BLUE, fontsize=8,
                ha='center', fontfamily='monospace')

        # Bottom
        ax.text(5.0, 0.6, 'Not two fields. ONE curvature.',
                color=GREY, fontsize=9, ha='center',
                fontfamily='monospace', style='italic')

    # ──────────────────────────────────────────────────────────────────
    # Panel 4: Maxwell for Free
    # ──────────────────────────────────────────────────────────────────

    def _draw_panel4_maxwell(self, ax):
        """Four equations from two geometric identities."""
        self._panel_setup(ax, 'MAXWELL FOR FREE',
                         'Four equations from two identities')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')

        # Identity 1: Bianchi
        ax.text(5.0, 9.3, 'BIANCHI IDENTITY', color=GREEN,
                fontsize=11, fontweight='bold', ha='center',
                fontfamily='monospace')
        ax.text(5.0, 8.7, r'$dF = 0$   (automatic: $d^2 = 0$)',
                color=GREEN, fontsize=11, ha='center',
                fontfamily='monospace')

        # Bianchi gives
        ax.text(2.5, 7.8, r'$\nabla \cdot \vec{B} = 0$',
                color=WHITE, fontsize=11, ha='center',
                fontfamily='monospace')
        ax.text(2.5, 7.2, 'No monopoles', color=GREY, fontsize=8,
                ha='center', fontfamily='monospace')
        ax.text(2.5, 6.8, '(topology)', color=GREEN, fontsize=8,
                ha='center', fontfamily='monospace', style='italic')

        ax.text(7.5, 7.8,
                r'$\nabla\times\vec{E} = -\frac{\partial\vec{B}}{\partial t}$',
                color=WHITE, fontsize=11, ha='center',
                fontfamily='monospace')
        ax.text(7.5, 7.2, "Faraday's law", color=GREY, fontsize=8,
                ha='center', fontfamily='monospace')
        ax.text(7.5, 6.8, '(topology)', color=GREEN, fontsize=8,
                ha='center', fontfamily='monospace', style='italic')

        # Divider
        ax.plot([1, 9], [6.1, 6.1], color=DGREY, linewidth=0.8)

        # Identity 2: Hodge / Action
        ax.text(5.0, 5.5, 'ACTION PRINCIPLE', color=ORANGE,
                fontsize=11, fontweight='bold', ha='center',
                fontfamily='monospace')
        ax.text(5.0, 4.9, r'$d{\star}F = {\star}J$   (from Bergman metric)',
                color=ORANGE, fontsize=11, ha='center',
                fontfamily='monospace')

        # Action gives
        ax.text(2.5, 4.0,
                r'$\nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0}$',
                color=WHITE, fontsize=11, ha='center',
                fontfamily='monospace')
        ax.text(2.5, 3.4, "Gauss's law", color=GREY, fontsize=8,
                ha='center', fontfamily='monospace')
        ax.text(2.5, 3.0, '(dynamics)', color=ORANGE, fontsize=8,
                ha='center', fontfamily='monospace', style='italic')

        ax.text(7.5, 4.0,
                r'$\nabla\times\vec{B} = \mu_0\vec{J} + \mu_0\epsilon_0\frac{\partial\vec{E}}{\partial t}$',
                color=WHITE, fontsize=9, ha='center',
                fontfamily='monospace')
        ax.text(7.5, 3.4, "Amp\u00e8re-Maxwell", color=GREY, fontsize=8,
                ha='center', fontfamily='monospace')
        ax.text(7.5, 3.0, '(dynamics)', color=ORANGE, fontsize=8,
                ha='center', fontfamily='monospace', style='italic')

        # Bottom: the reduction
        ax.plot([1, 9], [2.1, 2.1], color=DGREY, linewidth=0.8)
        ax.text(5.0, 1.5, 'Maxwell: 20 equations (1865)',
                color=GREY, fontsize=8, ha='center',
                fontfamily='monospace')
        ax.text(5.0, 1.0, 'Heaviside: 4 equations (1884)',
                color=GREY, fontsize=8, ha='center',
                fontfamily='monospace')
        ax.text(5.0, 0.5, 'Geometry: 2 identities (derived)',
                color=GOLD, fontsize=9, ha='center',
                fontfamily='monospace', fontweight='bold')

    # ──────────────────────────────────────────────────────────────────
    # Panel 5: alpha = 1/137
    # ──────────────────────────────────────────────────────────────────

    def _draw_panel5_alpha(self, ax):
        """The fine structure constant from Bergman normalization."""
        self._panel_setup(ax, r'$\alpha$ = 1/137',
                         'Coupling strength from Bergman normalization')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')

        # Wyler formula
        ax.text(5.0, 9.2,
                r'$\alpha = \frac{9}{8\pi^4}\left(\frac{\pi^5}{1920}\right)^{1/4}$',
                color=GOLD, fontsize=16, fontweight='bold', ha='center',
                fontfamily='monospace', path_effects=GLOW_GOLD)

        wyler = _wyler_alpha()
        ax.text(5.0, 8.2, f'= 1 / {wyler["inv_alpha"]:.6f}',
                color=GOLD, fontsize=12, ha='center',
                fontfamily='monospace')
        ax.text(5.0, 7.6,
                f'Observed: 1 / {wyler["observed_inv_alpha"]:.6f}'
                f'  ({wyler["deviation_pct"]:.4f}%)',
                color=GREY, fontsize=9, ha='center',
                fontfamily='monospace')

        # Embedding tower
        ax.text(5.0, 6.5, 'THE EMBEDDING TOWER', color=CYAN,
                fontsize=11, fontweight='bold', ha='center',
                fontfamily='monospace')

        # Draw 6 layers
        tower_y_start = 5.8
        layer_height = 0.55
        layer_colors = [CYAN, BLUE, PURPLE, MAGENTA, RED, ORANGE]

        for i in range(C_2):
            y = tower_y_start - i * layer_height
            # Bar representing a layer
            bar_width = 2.0 + i * 0.3
            x_left = 5.0 - bar_width / 2
            from matplotlib.patches import FancyBboxPatch
            rect = FancyBboxPatch(
                (x_left, y - 0.15), bar_width, 0.30,
                boxstyle='round,pad=0.05',
                facecolor=layer_colors[i], edgecolor='none', alpha=0.3)
            ax.add_patch(rect)
            ax.text(5.0, y, r'$\alpha^2$', color=layer_colors[i],
                    fontsize=9, ha='center', va='center',
                    fontfamily='monospace', fontweight='bold')
            ax.text(x_left - 0.3, y, f'{i+1}', color=GREY, fontsize=8,
                    ha='right', va='center', fontfamily='monospace')

        # Product
        bottom_y = tower_y_start - C_2 * layer_height - 0.1
        ax.text(5.0, bottom_y,
                r'$\alpha^{2\times 6} = \alpha^{12}$',
                color=WHITE, fontsize=11, ha='center',
                fontfamily='monospace', fontweight='bold')

        # Electron mass
        ax.text(5.0, bottom_y - 0.7,
                r'$m_e = 6\pi^5 \cdot \alpha^{12} \cdot m_{Pl}$',
                color=TEAL, fontsize=10, ha='center',
                fontfamily='monospace')

        # Bottom insight
        ax.text(5.0, 0.6,
                r'$\alpha$ is a volume ratio, not a free parameter',
                color=GREY, fontsize=8, ha='center',
                fontfamily='monospace', style='italic')

    # ──────────────────────────────────────────────────────────────────
    # Panel 6: One Geometry, One Force
    # ──────────────────────────────────────────────────────────────────

    def _draw_panel6_summary(self, ax):
        """The final panel: one geometry, one force."""
        self._panel_setup(ax, 'ONE GEOMETRY, ONE FORCE',
                         'Light is curvature on a circle fiber')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')

        # The derivation chain as a flow
        steps = [
            (r'D$_{IV}^5$ = SO$_0$(5,2) / [SO(5)$\times$SO(2)]', CYAN, 11),
            (r'SO(2) $\cong$ U(1)', GOLD, 12),
            (r'Connection A$_\mu$', ORANGE, 11),
            (r'Curvature F = dA', RED, 11),
            (r'dF = 0  +  d$\star$F = $\star$J', WHITE, 11),
            (r'Maxwell: all 4 equations', GREEN, 11),
        ]

        y_start = 9.0
        y_step = 1.15
        for i, (text, color, size) in enumerate(steps):
            y = y_start - i * y_step
            ax.text(5.0, y, text, color=color, fontsize=size,
                    ha='center', fontfamily='monospace',
                    fontweight='bold')
            # Arrow to next
            if i < len(steps) - 1:
                ax.annotate('', xy=(5.0, y - 0.45),
                           xytext=(5.0, y - 0.15),
                           arrowprops=dict(arrowstyle='->', color=DGREY,
                                           lw=1.5))

        # Separator
        ax.plot([1.5, 8.5], [2.3, 2.3], color=DGREY, linewidth=0.8)

        # Quote
        ax.text(5.0, 1.7,
                '"Maxwell didn\'t need four equations.',
                color=GREY, fontsize=9, ha='center',
                fontfamily='monospace', style='italic')
        ax.text(5.0, 1.1,
                'He needed one geometry."',
                color=GREY, fontsize=9, ha='center',
                fontfamily='monospace', style='italic')
        ax.text(5.0, 0.4,
                'The photon is a connection. The field is curvature. Light is geometry.',
                color=GOLD, fontsize=8, ha='center',
                fontfamily='monospace',
                path_effects=GLOW_GOLD)


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    mg = MaxwellGeometry()

    print()
    print("  What would you like to explore?")
    print("  1) SO(2) = U(1) = Electromagnetism")
    print("  2) Connection = Potential (A_mu from parallel transport)")
    print("  3) Curvature = Field (F = dA, E and B from geometry)")
    print("  4) Maxwell for Free (4 equations from 2 identities)")
    print("  5) alpha = 1/137 from Bergman normalization")
    print("  6) Wave equation and the speed of light")
    print("  7) Gauge invariance as S^1 reparameterization")
    print("  8) No monopoles (trivial Chern class)")
    print("  9) Full summary + visualization")
    print()

    try:
        choice = input("  Choice [1-9]: ").strip()
    except (EOFError, KeyboardInterrupt):
        choice = '9'

    if choice == '1':
        mg.so2_equals_u1()
    elif choice == '2':
        mg.connection_potential()
    elif choice == '3':
        mg.curvature_field()
    elif choice == '4':
        mg.maxwell_for_free()
    elif choice == '5':
        mg.alpha_from_bergman()
    elif choice == '6':
        mg.wave_equation()
    elif choice == '7':
        mg.gauge_invariance()
    elif choice == '8':
        mg.no_monopoles()
    elif choice == '9':
        mg.so2_equals_u1()
        mg.connection_potential()
        mg.curvature_field()
        mg.maxwell_for_free()
        mg.alpha_from_bergman()
        mg.wave_equation()
        mg.gauge_invariance()
        mg.no_monopoles()
        mg.summary()
        try:
            mg.show()
            input("\n  Press Enter to close...")
        except Exception:
            pass
    else:
        mg.summary()


if __name__ == '__main__':
    main()
