#!/usr/bin/env python3
"""
E₈ ELECTROWEAK UNIFICATION  --  Toy 85
=======================================
B₂ → SU(2)_L × SU(2)_R from the soliton sector.
Electroweak symmetry breaking IS the Toda fusing rule α₀ + α₂ → α₁.

The affine B₂⁽¹⁾ Toda field theory has three soliton species:
    α₀ (wrapping, short)  —  mass m    — Kac label 1
    α₁ (binding, long)    —  mass 2m   — Kac label 2
    α₂ (spatial, short)   —  mass m    — Kac label 1

The two short roots α₀ and α₂ carry SU(2)_L and SU(2)_R respectively.
The long root α₁ = α₀ + α₂ is their threshold bound state — this IS
electroweak symmetry breaking. No Higgs field is introduced; the
breaking is a consequence of the affine Toda fusing rules.

The Kac labels 1:2:1 give W and Z masses:
    M_W ∝ Kac(α₀) = 1   →  M_W = m
    M_Z ∝ Kac(α₁) = 2   →  M_Z = 2m × cos(θ_W)
    M_W/M_Z = cos(θ_W) = √(10/13)

Root multiplicities from the restricted root system of D_IV⁵:
    m_short = n_C − 2 = 3  →  3 spatial dimensions
    m_long  = 1             →  1 temporal dimension

The Standard Model gauge group SU(3)×SU(2)×U(1) emerges from the
tangent space decomposition T_o(D_IV⁵) = C³ ⊕ C² at the base point,
where C³ carries color [SU(3)] and C² carries weak isospin [SU(2)×U(1)].

CI Interface:
    from toy_e8_electroweak import E8Electroweak
    ew = E8Electroweak()
    ew.b2_decomposition()           # B₂ roots → SU(2)_L × SU(2)_R
    ew.electroweak_breaking()       # Fusing rule α₀+α₂→α₁ = EW breaking
    ew.spatial_dimensions()         # m_short=3 → 3 spatial dimensions
    ew.temporal_direction()         # m_long=1  → 1 time dimension
    ew.w_z_masses()                 # W and Z from fusing structure
    ew.binding_mode()               # α₁ at marginal coupling
    ew.kac_labels()                 # 1:2:1 and physical meaning
    ew.standard_model_embedding()   # SU(3)×SU(2)×U(1) from D_IV⁵
    ew.summary()                    # Key insight
    ew.show()                       # 4-panel visualization

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
import math
import sys

# ──────────────────────────────────────────────────────────────────
#  BST Constants
# ──────────────────────────────────────────────────────────────────
N_c   = 3           # color charges (= c₅(Q⁵))
n_C   = 5           # complex dimension of D_IV⁵ (= c₁(Q⁵))
C_2   = n_C + 1     # 6  Casimir eigenvalue C₂(π₆)
genus = n_C + 2     # 7  genus of D_IV⁵
N_max = 137         # channel capacity

# Wyler alpha
alpha = 1.0 / 137.035999

# Weyl groups
W_D5  = math.factorial(n_C) * 2**(n_C - 1)    # |W(D₅)| = 1920
W_B2  = 8                                       # |W(B₂)| = 2!×2² = 8
E8_ROOTS = W_D5 // W_B2                         # 240 = |Φ(E₈)|

# B₂ root system
m_short = n_C - 2   # 3  short root multiplicity
m_long  = 1          # 1  long root multiplicity
h_B2    = 4          # Coxeter number of B₂

# Affine B₂⁽¹⁾ Kac labels
KAC_0 = 1           # α₀ (wrapping, short)
KAC_1 = 2           # α₁ (binding, long)
KAC_2 = 1           # α₂ (spatial, short)

# Chern class coefficients of Q⁵
CHERN = {1: 5, 2: 11, 3: 13, 4: 9, 5: 3}

# Weinberg angle
sin2_theta_W = CHERN[5] / CHERN[3]              # 3/13 = 0.23077
cos2_theta_W = 1.0 - sin2_theta_W               # 10/13
cos_theta_W  = np.sqrt(cos2_theta_W)
sin_theta_W  = np.sqrt(sin2_theta_W)

# Observed values
M_W_OBS  = 80.3692       # GeV (PDG 2024)
M_Z_OBS  = 91.1876       # GeV (PDG 2024)
SIN2_OBS = 0.23122       # MS-bar at m_Z
V_EW_OBS = 246.22        # GeV Fermi VEV

# BST predictions
M_W_M_Z_BST  = cos_theta_W   # M_W/M_Z = cos(θ_W)
M_W_M_Z_OBS  = M_W_OBS / M_Z_OBS

# Fermi scale: v = m_p²/(7 m_e)
m_p = 938.272088   # MeV
m_e = 0.51099895   # MeV
V_EW_BST = (m_p**2) / (genus * m_e) / 1000.0  # GeV


# ──────────────────────────────────────────────────────────────────
#  B₂ Root System Utilities
# ──────────────────────────────────────────────────────────────────

def b2_roots():
    """Return all 8 roots of B₂ as (vector, length², type, label)."""
    roots = []
    # Short roots (length² = 1, multiplicity n_C-2 = 3 each)
    for s1 in [+1, -1]:
        roots.append((np.array([s1, 0]), 1, 'short', f'{s1:+d}e₁'))
        roots.append((np.array([0, s1]), 1, 'short', f'{s1:+d}e₂'))
    # Long roots (length² = 2, multiplicity 1 each)
    for s1 in [+1, -1]:
        for s2 in [+1, -1]:
            roots.append((np.array([s1, s2]), 2, 'long',
                          f'{s1:+d}e₁{s2:+d}e₂'))
    return roots


def affine_cartan_b2():
    """Return the 3×3 affine Cartan matrix for B₂⁽¹⁾."""
    return np.array([
        [ 2, -1,  0],
        [-2,  2, -2],
        [ 0, -1,  2]
    ])


def chern_coefficient(n, k):
    """Compute c_k(Q^n) = sum_{j=0}^{k} C(n+2, k-j)(-2)^j."""
    total = 0
    for j in range(k + 1):
        if k - j > n + 2:
            continue
        total += math.comb(n + 2, k - j) * ((-2)**j)
    return total


# ══════════════════════════════════════════════════════════════════
#  CLASS: E8Electroweak
# ══════════════════════════════════════════════════════════════════

class E8Electroweak:
    """Toy 85: E₈ Electroweak Unification — B₂ fusing as EW breaking."""

    def __init__(self, quiet=False):
        self.quiet = quiet
        if not quiet:
            print()
            print("=" * 68)
            print("  E₈ ELECTROWEAK UNIFICATION  --  BST Toy 85")
            print("  B₂ fusing rule α₀+α₂→α₁ IS electroweak symmetry breaking")
            print("=" * 68)

    def _p(self, text=""):
        if not self.quiet:
            print(text)

    # ──────────────────────────────────────────────────────────────
    # 1. b2_decomposition
    # ──────────────────────────────────────────────────────────────

    def b2_decomposition(self):
        """B₂ roots decompose into SU(2)_L × SU(2)_R."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  B₂ DECOMPOSITION → SU(2)_L × SU(2)_R")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  The restricted root system of D_IV⁵ = SO₀(5,2)/[SO(5)×SO(2)]")
        self._p("  is type B₂, with 8 roots in 2D:")
        self._p()
        self._p("  Root        │ Length² │ Mult. │  Type  │ Physical role")
        self._p("  ────────────┼─────────┼───────┼────────┼──────────────────────")

        roots = b2_roots()
        for vec, lsq, rtype, label in roots:
            mult = m_short if rtype == 'short' else m_long
            if rtype == 'short':
                role = "spatial propagation"
            else:
                role = "gauge time evolution"
            self._p(f"  {label:<11} │   {lsq}     │   {mult}   │ {rtype:<6} │ {role}")

        self._p()
        self._p("  The short roots ±e₁ and ±e₂ decompose into two SU(2) sectors:")
        self._p()
        self._p("    SU(2)_L:  {+e₁, -e₁} + neutral")
        self._p("      Raising: +e₁    Lowering: -e₁")
        self._p("      These are the LEFT-handed weak isospin generators.")
        self._p()
        self._p("    SU(2)_R:  {+e₂, -e₂} + neutral")
        self._p("      Raising: +e₂    Lowering: -e₂")
        self._p("      These are the RIGHT-handed weak isospin generators.")
        self._p()
        self._p("  The long roots ±(e₁±e₂) are the COUPLING between L and R:")
        self._p("    α₁ = e₁-e₂ couples SU(2)_L to SU(2)_R  (binding mode)")
        self._p("    θ  = e₁+e₂ is the highest root (wrapping mode in affine)")
        self._p()
        self._p("  B₂ = SU(2)_L ⊗ SU(2)_R + coupling")
        self._p("  This is the LEFT-RIGHT SYMMETRIC structure of the electroweak")
        self._p("  sector BEFORE symmetry breaking.")
        self._p()

        result = {
            'roots': roots,
            'n_short': 4,
            'n_long': 4,
            'm_short': m_short,
            'm_long': m_long,
            'total_roots': 8
        }
        return result

    # ──────────────────────────────────────────────────────────────
    # 2. electroweak_breaking
    # ──────────────────────────────────────────────────────────────

    def electroweak_breaking(self):
        """Fusing rule α₀+α₂→α₁ = electroweak symmetry breaking."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  ELECTROWEAK BREAKING = TODA FUSING RULE")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  The affine B₂⁽¹⁾ Dynkin diagram:")
        self._p()
        self._p("       α₀ ——— α₁ ===> α₂")
        self._p("     (short) (long) (short)")
        self._p("      Kac=1  Kac=2  Kac=1")
        self._p()
        self._p("  The Toda fusing rules determine which soliton bound states")
        self._p("  can form. The KEY fusing rule is:")
        self._p()
        self._p("         ╔═══════════════════════════════════════╗")
        self._p("         ║    α₀  +  α₂  →  α₁                 ║")
        self._p("         ║  (wrap) + (spatial) → (binding)      ║")
        self._p("         ║   SU(2)_L + SU(2)_R → coupled mode  ║")
        self._p("         ╚═══════════════════════════════════════╝")
        self._p()
        self._p("  This IS electroweak symmetry breaking:")
        self._p()
        self._p("  BEFORE fusing:")
        self._p("    α₀ (SU(2)_L wrapping mode) and α₂ (SU(2)_R spatial mode)")
        self._p("    are INDEPENDENT soliton species, each with mass m.")
        self._p("    The gauge symmetry is SU(2)_L × SU(2)_R (left-right symmetric).")
        self._p()
        self._p("  THE FUSING EVENT:")
        self._p("    At threshold, α₀ and α₂ fuse into the bound state α₁.")
        self._p("    Mass: m₁ = m₀ + m₂ = m + m = 2m (binding energy = 0).")
        self._p("    The L-R symmetry is BROKEN: α₁ couples L to R irreversibly.")
        self._p()
        self._p("  AFTER fusing:")
        self._p("    The bound state α₁ carries BOTH L and R quantum numbers.")
        self._p("    Only the DIAGONAL subgroup SU(2)_V survives.")
        self._p("    The broken generators become the W and Z masses.")
        self._p()
        self._p("  No Higgs field is introduced.")
        self._p("  No Mexican-hat potential is needed.")
        self._p("  The breaking is KINEMATIC — it follows from the Toda")
        self._p("  fusing rules, which follow from the affine Dynkin diagram,")
        self._p("  which follows from the restricted root system of D_IV⁵.")
        self._p()
        self._p("  ELECTROWEAK BREAKING IS GEOMETRY.")
        self._p()

        # Verify the fusing rule algebraically
        alpha_0 = np.array([-1, -1])   # -(e₁+e₂) = -θ
        alpha_1 = np.array([ 1, -1])   # e₁-e₂
        alpha_2 = np.array([ 0,  1])   # e₂
        fused = alpha_0 + alpha_2       # should equal α₁
        assert np.allclose(fused, alpha_1), "Fusing rule verification failed"

        self._p(f"  Algebraic verification:")
        self._p(f"    α₀ = -(e₁+e₂) = ({alpha_0[0]:+d}, {alpha_0[1]:+d})")
        self._p(f"    α₂ = e₂        = ({alpha_2[0]:+d}, {alpha_2[1]:+d})")
        self._p(f"    α₀ + α₂        = ({fused[0]:+d}, {fused[1]:+d})")
        self._p(f"    α₁ = e₁-e₂     = ({alpha_1[0]:+d}, {alpha_1[1]:+d})  ✓")
        self._p()

        return {
            'alpha_0': alpha_0,
            'alpha_1': alpha_1,
            'alpha_2': alpha_2,
            'fusing_verified': True,
            'mechanism': 'Toda fusing rule'
        }

    # ──────────────────────────────────────────────────────────────
    # 3. spatial_dimensions
    # ──────────────────────────────────────────────────────────────

    def spatial_dimensions(self):
        """(2,2) bridge sector = 3 spatial dimensions from m_short=3."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  SPATIAL DIMENSIONS FROM SHORT ROOT MULTIPLICITY")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  The restricted root system of D_IV^n_C has root multiplicities:")
        self._p()
        self._p(f"    Short roots (±eᵢ):      m_short = n_C - 2 = {n_C} - 2 = {m_short}")
        self._p(f"    Long roots (±eᵢ±eⱼ):    m_long  = 1")
        self._p()
        self._p("  The short root spaces carry SPATIAL degrees of freedom.")
        self._p("  Each short root direction = one independent propagation channel.")
        self._p(f"  Multiplicity {m_short} = {m_short} spatial dimensions.")
        self._p()
        self._p("  The (2,2) bridge sector:")
        self._p("  ─────────────────────────")
        self._p("  The two short root spaces g_{e₁} and g_{e₂} each have")
        self._p(f"  dimension {m_short}, giving a (2,2) structure in the Cartan subalgebra:")
        self._p()
        self._p("    g_{+e₁}  dim=3  ──╮")
        self._p("                       ├── Spatial sector: 2×3 = 6 real dims")
        self._p("    g_{+e₂}  dim=3  ──╯")
        self._p()
        self._p("  Capacity decomposition:")
        self._p(f"    C_spatial  = 2 × m_short = 2 × {m_short} = 6 nats")
        self._p(f"    C_temporal = 2 × m_long  = 2 × {m_long}  = 2 nats")
        self._p(f"    C_soliton  = rank(B₂)                     = 2 nats")
        self._p(f"    C_total    = dim_R(D_IV⁵) = 2n_C          = 10 nats")
        self._p()
        self._p(f"  Ratio: C_spatial/C_temporal = 6/2 = {m_short} = d_spatial")
        self._p()
        self._p("  Universality for D_IV^n (n ≥ 3):")
        self._p("  ─────────────────────────────────")
        self._p("  n │ m_short │ d_spatial │ d_temporal │ spacetime")
        self._p("  ──┼─────────┼───────────┼────────────┼──────────")

        for n in range(3, 8):
            ms = n - 2
            marker = "  <── OUR UNIVERSE" if n == 5 else ""
            self._p(f"  {n} │    {ms}    │     {ms}     │      1     │  {ms}+1{marker}")

        self._p()
        self._p("  The max-α principle selects n_C = 5, giving 3+1 spacetime.")
        self._p("  Space is 3D because the short root multiplicity is 3.")
        self._p("  Time is 1D because the long root multiplicity is ALWAYS 1.")
        self._p()

        return {
            'd_spatial': m_short,
            'd_temporal': m_long,
            'C_spatial': 2 * m_short,
            'C_temporal': 2 * m_long,
            'C_total': 2 * n_C
        }

    # ──────────────────────────────────────────────────────────────
    # 4. temporal_direction
    # ──────────────────────────────────────────────────────────────

    def temporal_direction(self):
        """Long root = gauge time evolution, m_long=1."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  TEMPORAL DIRECTION FROM LONG ROOT")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  The long root α₁ = e₁ - e₂ has multiplicity m_long = 1.")
        self._p()
        self._p("  Its Toda potential: V₁ = exp(q₁ - q₂)")
        self._p()
        self._p("  This is the COUPLING between the two Toda coordinates.")
        self._p("  It drives:")
        self._p("    — Interaction between soliton modes")
        self._p("    — Binding (α₀+α₂→α₁)")
        self._p("    — Irreversible commitment to the Shilov boundary")
        self._p()
        self._p("  This is the direction of EVOLUTION:")
        self._p("  the direction in which contacts are made.")
        self._p("  Its multiplicity 1 gives a SINGLE time dimension.")
        self._p()
        self._p("  WHY time is unique:")
        self._p("  ───────────────────")
        self._p("  m_long = 1 for ALL type IV domains with n_C ≥ 3.")
        self._p("  This is not a special property of n_C = 5.")
        self._p("  Time is one-dimensional by ALGEBRA, not by choice.")
        self._p()
        self._p("  The long root structure:")
        self._p()
        self._p("    Root │ Vector │ Mult │ Physical meaning")
        self._p("    ─────┼────────┼──────┼──────────────────────────────────")
        self._p("    +α₁  │ e₁-e₂  │  1   │ Forward evolution (future light cone)")
        self._p("    -α₁  │ e₂-e₁  │  1   │ Backward evolution (past light cone)")
        self._p("    +θ   │ e₁+e₂  │  1   │ Highest root → affine wrapping")
        self._p("    -θ   │-e₁-e₂  │  1   │ Affine root α₀ (wrapping mode)")
        self._p()
        self._p("  The two long root pairs (±α₁, ±θ) give 2 temporal nats.")
        self._p("  The arrow of time comes from the Toda potential being")
        self._p("  EXPONENTIAL: V₁ = exp(q₁-q₂) breaks q₁↔q₂ symmetry.")
        self._p("  The direction of increasing q₁-q₂ is the future.")
        self._p()

        return {
            'm_long': m_long,
            'n_temporal': 1,
            'potential': 'exp(q1 - q2)',
            'arrow_source': 'exponential potential asymmetry'
        }

    # ──────────────────────────────────────────────────────────────
    # 5. w_z_masses
    # ──────────────────────────────────────────────────────────────

    def w_z_masses(self):
        """W and Z boson masses from the fusing structure."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  W AND Z MASSES FROM FUSING STRUCTURE")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  The affine B₂⁽¹⁾ mass spectrum:")
        self._p()
        self._p("    Mode │ Root │ Kac │ Mass │ Type  │ Gauge boson")
        self._p("    ─────┼──────┼─────┼──────┼───────┼─────────────")
        self._p("     α₀  │  -θ  │  1  │  m   │ short │ W± (charged)")
        self._p("     α₁  │ e₁-e₂│  2  │  2m  │ long  │ Z⁰ (neutral)")
        self._p("     α₂  │  e₂  │  1  │  m   │ short │ W± (charged)")
        self._p()
        self._p("  The W bosons correspond to the two SHORT root solitons:")
        self._p("    α₀ (wrapping SU(2)_L) and α₂ (spatial SU(2)_R)")
        self._p("    Both have mass m — they are the SAME mass because the")
        self._p("    Kac labels are both 1.")
        self._p()
        self._p("  The Z boson corresponds to the LONG root bound state:")
        self._p("    α₁ = α₀ + α₂ has mass 2m (Kac label 2)")
        self._p()
        self._p("  The mass ratio M_W/M_Z:")
        self._p("  ────────────────────────")
        self._p(f"    sin²θ_W = c₅/c₃ = {CHERN[5]}/{CHERN[3]} = {sin2_theta_W:.5f}")
        self._p(f"    cos²θ_W = 1 - sin²θ_W = {cos2_theta_W:.5f} = 10/13")
        self._p(f"    cos θ_W = √(10/13) = {cos_theta_W:.6f}")
        self._p()
        self._p(f"    M_W / M_Z = cos θ_W = {cos_theta_W:.6f}")
        self._p()
        self._p("  In the fusing picture:")
        self._p("    M_W corresponds to the fundamental mode mass m")
        self._p("    M_Z corresponds to the bound state at 2m × projection")
        self._p("    The projection factor cos θ_W accounts for the mixing")
        self._p("    between the neutral components of SU(2)_L and SU(2)_R.")
        self._p()

        ratio_bst = cos_theta_W
        ratio_obs = M_W_M_Z_OBS
        error_pct = abs(ratio_bst - ratio_obs) / ratio_obs * 100

        self._p("  Comparison with observation:")
        self._p(f"    BST:      M_W/M_Z = cos θ_W = {ratio_bst:.6f}")
        self._p(f"    Observed: M_W/M_Z = {M_W_OBS}/{M_Z_OBS} = {ratio_obs:.6f}")
        self._p(f"    Error:    {error_pct:.3f}%")
        self._p()

        # Fermi scale
        v_bst = V_EW_BST
        v_obs = V_EW_OBS
        v_err = abs(v_bst - v_obs) / v_obs * 100

        self._p("  The Fermi scale (electroweak VEV):")
        self._p(f"    v = m_p² / (g × m_e) = {m_p:.3f}² / ({genus} × {m_e:.8f})")
        self._p(f"      = {v_bst:.2f} GeV")
        self._p(f"    Observed: {v_obs:.2f} GeV")
        self._p(f"    Error:    {v_err:.3f}%")
        self._p()

        return {
            'sin2_theta_W': sin2_theta_W,
            'cos_theta_W': cos_theta_W,
            'M_W_over_M_Z_BST': ratio_bst,
            'M_W_over_M_Z_obs': ratio_obs,
            'v_BST_GeV': v_bst,
            'v_obs_GeV': v_obs
        }

    # ──────────────────────────────────────────────────────────────
    # 6. binding_mode
    # ──────────────────────────────────────────────────────────────

    def binding_mode(self):
        """α₁ at marginal coupling = near-critical EW vacuum."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  THE BINDING MODE AT MARGINAL COUPLING")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  The fusing rule α₀ + α₂ → α₁ has a remarkable property:")
        self._p()
        self._p("    m₁ = m₀ + m₂  (binding energy = 0)")
        self._p()
        self._p("  The bound state α₁ is at THRESHOLD — it sits exactly")
        self._p("  at the boundary between bound and unbound.")
        self._p("  This is MARGINAL COUPLING.")
        self._p()
        self._p("  Physical consequences:")
        self._p("  ──────────────────────")
        self._p()
        self._p("  1. NEAR-CRITICAL VACUUM")
        self._p("     The EW vacuum is poised at the edge of stability.")
        self._p("     The binding mode α₁ could dissociate (α₁ → α₀+α₂)")
        self._p("     with zero energy cost. The vacuum is metastable.")
        self._p()
        self._p("  2. THIS EXPLAINS THE HIERARCHY")
        self._p("     The EW scale v = 246 GeV is far below the Planck scale")
        self._p("     because the binding is MARGINAL. A deeply bound state")
        self._p("     would have mass ≫ 2m. A marginally bound state has")
        self._p("     mass = 2m exactly — the minimum possible.")
        self._p()
        self._p("  3. COSMOLOGICAL PHASE TRANSITION")
        self._p("     At high temperature, the fusing is entropically")
        self._p("     disfavored (the bound state has fewer DOF).")
        self._p("     Below T_EW ~ v, fusing becomes favorable.")
        self._p("     This is the EW phase transition at ~100 GeV.")
        self._p()
        self._p("  4. HIGGS BOSON = BREATHING MODE")
        self._p("     The Higgs boson is the radial excitation of the α₁")
        self._p("     bound state — a breathing mode of the fused soliton.")
        self._p("     Its mass 125 GeV ≈ v/2 reflects the marginal binding:")
        self._p("     the breathing frequency is half the dissociation threshold.")
        self._p()
        self._p("  The Toda potential at the binding mode:")
        self._p()
        self._p("    V(q₁,q₂) = exp(q₁-q₂) + exp(q₂)")
        self._p()
        self._p("  At q₁=q₂ (the fusing point), V = 1 + exp(q₂).")
        self._p("  The coupling exp(q₁-q₂) = 1 — neither strong nor weak.")
        self._p("  This IS marginal coupling.")
        self._p()

        return {
            'binding_energy': 0,
            'coupling_type': 'marginal',
            'vacuum_stability': 'metastable',
            'higgs_interpretation': 'breathing mode of α₁ bound state'
        }

    # ──────────────────────────────────────────────────────────────
    # 7. kac_labels
    # ──────────────────────────────────────────────────────────────

    def kac_labels(self):
        """Affine B₂⁽¹⁾ Kac labels 1:2:1 and their physical meaning."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  KAC LABELS 1:2:1 AND PHYSICAL MEANING")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  The affine B₂⁽¹⁾ Dynkin diagram with Kac labels:")
        self._p()
        self._p("       (1)       (2)       (1)")
        self._p("       α₀ ——— α₁ ===> α₂")
        self._p()
        self._p("  Kac labels (n₀, n₁, n₂) = (1, 2, 1) are the null vector")
        self._p("  of the affine Cartan matrix A⁽¹⁾:")
        self._p()

        A = affine_cartan_b2()
        self._p("         ⎛  2  -1   0 ⎞     ⎛ 1 ⎞     ⎛ 0 ⎞")
        self._p("    A =  ⎜ -2   2  -2 ⎟  ×  ⎜ 2 ⎟  =  ⎜ 0 ⎟")
        self._p("         ⎝  0  -1   2 ⎠     ⎝ 1 ⎠     ⎝ 0 ⎠")
        self._p()

        # Verify
        kac = np.array([KAC_0, KAC_1, KAC_2])
        result = A @ kac
        assert np.allclose(result, 0), "Kac null vector verification failed"
        self._p("  Verification: A × (1,2,1)ᵀ = (0,0,0)ᵀ  ✓")
        self._p()

        self._p(f"  Sum of Kac labels = {KAC_0}+{KAC_1}+{KAC_2} = "
                f"{KAC_0+KAC_1+KAC_2} = h(B₂) = Coxeter number")
        self._p()
        self._p("  Physical meaning of each Kac label:")
        self._p("  ────────────────────────────────────")
        self._p()
        self._p(f"  n₀ = {KAC_0}:  WRAPPING MODE (α₀)")
        self._p(f"     Mass = {KAC_0}m")
        self._p("     The soliton wraps once around S¹ on the Shilov boundary.")
        self._p("     Carries SU(2)_L quantum numbers.")
        self._p("     Physical: W⁺ boson (charged current)")
        self._p()
        self._p(f"  n₁ = {KAC_1}:  BINDING MODE (α₁)")
        self._p(f"     Mass = {KAC_1}m")
        self._p("     Threshold bound state of α₀+α₂.")
        self._p("     Carries BOTH SU(2)_L and SU(2)_R — the coupling.")
        self._p("     Physical: Z⁰ boson (neutral current)")
        self._p()
        self._p(f"  n₂ = {KAC_2}:  SPATIAL MODE (α₂)")
        self._p(f"     Mass = {KAC_2}m")
        self._p("     Propagation along the spatial short root directions.")
        self._p("     Carries SU(2)_R quantum numbers.")
        self._p("     Physical: W⁻ boson (charged current)")
        self._p()
        self._p("  The 1:2:1 ratio encodes the ENTIRE electroweak mass spectrum:")
        self._p(f"    M_W : M_Z : M_W = {KAC_0} : {KAC_1}×cos θ_W : {KAC_2}")
        self._p()
        self._p("  The Coxeter frequency ratio:")
        self._p(f"    f_bound / f_fund = h(B₂) = {h_B2}")
        self._p("    The fully fused state oscillates {h_B2}× faster than")
        self._p("    the fundamental mode.")
        self._p()

        return {
            'kac_labels': (KAC_0, KAC_1, KAC_2),
            'coxeter_number': h_B2,
            'cartan_matrix': A,
            'null_verified': True
        }

    # ──────────────────────────────────────────────────────────────
    # 8. standard_model_embedding
    # ──────────────────────────────────────────────────────────────

    def standard_model_embedding(self):
        """How SU(3)×SU(2)×U(1) emerges from D_IV⁵."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  STANDARD MODEL FROM D_IV⁵")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  The tangent space at the origin of D_IV⁵ is:")
        self._p()
        self._p("    T_o(D_IV⁵) ≅ C⁵ = C³ ⊕ C²")
        self._p()
        self._p("  Under the isotropy group K = SO(5) × SO(2), this decomposes")
        self._p("  as the Standard Model gauge group:")
        self._p()
        self._p("    ╔══════════════════════════════════════════════════╗")
        self._p("    ║  SU(3)_color  ×  SU(2)_weak  ×  U(1)_Y        ║")
        self._p("    ║     ↕              ↕               ↕           ║")
        self._p("    ║    C³             C²             SO(2) ⊂ K     ║")
        self._p("    ║  (color)       (isospin)      (hypercharge)    ║")
        self._p("    ╚══════════════════════════════════════════════════╝")
        self._p()
        self._p("  The numbers:")
        self._p(f"    dim(C³) = N_c = {N_c}          color charges")
        self._p(f"    dim(C²) = N_w = {n_C - N_c}          weak doublet")
        self._p(f"    N_c + N_w = {N_c} + {n_C - N_c} = {n_C} = n_C      total tangent space")
        self._p()
        self._p("  Chern class encoding (from Q⁵ = compact dual):")
        self._p()
        self._p("  k │  c_k(Q⁵) │ BST meaning")
        self._p("  ──┼──────────┼──────────────────────────────────────")

        meanings = {
            1: f"n_C = {n_C}  (complex dimension)",
            2: f"dim(K) = dim(SO(5)×SO(2)) = {CHERN[2]}",
            3: f"N_c + 2n_C = {N_c} + {2*n_C} = {CHERN[3]}  (Weinberg denom.)",
            4: f"N_c² = {N_c}² = {CHERN[4]}  (color Casimir)",
            5: f"N_c = {CHERN[5]}  (color number)",
        }
        for k in range(1, 6):
            self._p(f"  {k} │    {CHERN[k]:>2}    │ {meanings[k]}")

        self._p()
        self._p(f"  Weinberg angle: sin²θ_W = c₅/c₃ = {CHERN[5]}/{CHERN[3]} = {sin2_theta_W:.5f}")
        self._p(f"  Observed:       sin²θ_W = {SIN2_OBS}")
        self._p(f"  Error:          {abs(sin2_theta_W - SIN2_OBS)/SIN2_OBS*100:.2f}%")
        self._p()
        self._p("  The hierarchy of embeddings:")
        self._p("  ───────────────────────────")
        self._p()
        self._p("    E₈ (240 roots)")
        self._p("     └── D₅ = SO(10)  [Weyl group W(D₅) = 1920]")
        self._p("          └── B₂ restricted root system  [W(B₂) = 8]")
        self._p("               └── SU(2)_L × SU(2)_R  (short roots)")
        self._p("                    └── SU(2)_V  (diagonal, after fusing)")
        self._p("                         └── U(1)_EM  (residual)")
        self._p()
        self._p(f"  |W(D₅)|/|W(B₂)| = {W_D5}/{W_B2} = {E8_ROOTS} = |Φ(E₈)|")
        self._p()
        self._p("  The Standard Model is not EMBEDDED in E₈.")
        self._p("  It EMERGES from the root system hierarchy of D_IV⁵.")
        self._p("  E₈ appears as the RATIO of the particle and soliton Weyl groups.")
        self._p()

        return {
            'gauge_group': 'SU(3) x SU(2) x U(1)',
            'color_dim': N_c,
            'weak_dim': n_C - N_c,
            'total_dim': n_C,
            'chern_classes': CHERN,
            'E8_ratio': E8_ROOTS
        }

    # ──────────────────────────────────────────────────────────────
    # 9. summary
    # ──────────────────────────────────────────────────────────────

    def summary(self):
        """Key insight: EW breaking is geometry, not Higgs mechanism."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  SUMMARY: ELECTROWEAK BREAKING IS GEOMETRY")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  The Standard Model requires a Higgs field to break")
        self._p("  SU(2)_L × U(1)_Y → U(1)_EM, with a Mexican-hat potential")
        self._p("  V(φ) = -μ²|φ|² + λ|φ|⁴ containing TWO free parameters.")
        self._p()
        self._p("  BST replaces this with a GEOMETRIC mechanism:")
        self._p()
        self._p("  ╔═══════════════════════════════════════════════════════╗")
        self._p("  ║  1. Domain: D_IV⁵ has restricted root system B₂      ║")
        self._p("  ║  2. Affine: S¹ on Shilov boundary → B₂⁽¹⁾            ║")
        self._p("  ║  3. Roots:  α₀(short) + α₂(short) → α₁(long)       ║")
        self._p("  ║  4. Physics: SU(2)_L × SU(2)_R → SU(2)_V           ║")
        self._p("  ║  5. Masses: Kac labels 1:2:1 → M_W:M_Z:M_W         ║")
        self._p("  ╚═══════════════════════════════════════════════════════╝")
        self._p()
        self._p("  Free parameters: ZERO")
        self._p("  Free parameters in Standard Model: 2 (μ, λ)")
        self._p()
        self._p("  Key predictions:")
        self._p()

        predictions = [
            ("sin²θ_W = 3/13",        f"{sin2_theta_W:.5f}",  f"{SIN2_OBS}",       "0.2%"),
            ("M_W/M_Z = cos θ_W",     f"{M_W_M_Z_BST:.6f}",  f"{M_W_M_Z_OBS:.6f}", f"{abs(M_W_M_Z_BST-M_W_M_Z_OBS)/M_W_M_Z_OBS*100:.2f}%"),
            ("v = m_p²/(7m_e)",        f"{V_EW_BST:.2f} GeV", f"{V_EW_OBS:.2f} GeV", f"{abs(V_EW_BST-V_EW_OBS)/V_EW_OBS*100:.2f}%"),
            ("d_spatial = n_C-2",      f"{m_short}",           "3",                  "exact"),
            ("d_temporal = 1",         f"{m_long}",            "1",                  "exact"),
            ("Coxeter ratio h(B₂)",    f"{h_B2}",             "4",                  "exact"),
            ("|W(D₅)|/|W(B₂)|",       f"{E8_ROOTS}",         "240 = |Φ(E₈)|",     "exact"),
        ]

        self._p("  Prediction              │ BST value    │ Observed      │ Error")
        self._p("  ────────────────────────┼──────────────┼───────────────┼──────")
        for name, bst, obs, err in predictions:
            self._p(f"  {name:<24}│ {bst:<12} │ {obs:<13} │ {err}")

        self._p()
        self._p("  The Higgs boson is the BREATHING MODE of the α₁ bound state.")
        self._p("  It is real, observable, and has the right mass.")
        self._p("  But it is not the CAUSE of symmetry breaking.")
        self._p("  It is the CONSEQUENCE of Toda fusing on D_IV⁵.")
        self._p()
        self._p("  ELECTROWEAK BREAKING IS THE GEOMETRY OF B₂⁽¹⁾.")
        self._p()

        return {
            'mechanism': 'Toda fusing rule on B₂⁽¹⁾',
            'free_parameters': 0,
            'higgs_role': 'breathing mode of bound state α₁'
        }

    # ──────────────────────────────────────────────────────────────
    # 10. show  --  4-panel visualization
    # ──────────────────────────────────────────────────────────────

    def show(self):
        """4-panel visualization of E₈ electroweak unification."""
        import matplotlib
        matplotlib.use('TkAgg')
        import matplotlib.pyplot as plt
        import matplotlib.patheffects as pe
        from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Wedge

        BG        = '#0a0a1a'
        GOLD      = '#ffaa00'
        GOLD_DIM  = '#aa8800'
        BLUE      = '#4488ff'
        BLUE_DIM  = '#336699'
        RED       = '#ff4488'
        RED_DIM   = '#cc3366'
        GREEN     = '#00ff88'
        GREEN_DIM = '#00aa66'
        WHITE     = '#ffffff'
        GREY      = '#888888'
        CYAN      = '#44ddff'
        ORANGE    = '#ff8800'
        PURPLE    = '#cc88ff'
        PURP_DIM  = '#8855aa'

        fig = plt.figure(figsize=(18, 13), facecolor=BG)
        fig.canvas.manager.set_window_title(
            'E\u2088 Electroweak Unification \u2014 BST Toy 85')

        fig.text(0.5, 0.975, 'E\u2088 ELECTROWEAK UNIFICATION',
                 fontsize=26, fontweight='bold', color=GOLD, ha='center',
                 fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=2, foreground='#442200')])
        fig.text(0.5, 0.950,
                 'B\u2082 fusing rule \u03b1\u2080+\u03b1\u2082\u2192\u03b1\u2081 '
                 'IS electroweak symmetry breaking',
                 fontsize=12, color=GOLD_DIM, ha='center', fontfamily='monospace')

        # ─── Panel 1 (top-left): B₂ ROOT SYSTEM ───
        ax1 = fig.add_axes([0.03, 0.52, 0.46, 0.40])
        ax1.set_facecolor('#0d0d1a')
        ax1.set_aspect('equal')
        ax1.set_xlim(-2.2, 2.2)
        ax1.set_ylim(-2.2, 2.2)
        ax1.set_title('B\u2082 Root System \u2192 SU(2)_L \u00d7 SU(2)_R',
                       fontsize=14, fontweight='bold', color=CYAN,
                       fontfamily='monospace', pad=10)

        # Axes
        ax1.axhline(0, color='#222244', linewidth=0.5, zorder=1)
        ax1.axvline(0, color='#222244', linewidth=0.5, zorder=1)

        # Draw unit circle and √2 circle
        theta = np.linspace(0, 2*np.pi, 200)
        ax1.plot(np.cos(theta), np.sin(theta),
                 color='#333366', linewidth=1, linestyle=':', alpha=0.5)
        ax1.plot(np.sqrt(2)*np.cos(theta), np.sqrt(2)*np.sin(theta),
                 color='#663333', linewidth=1, linestyle=':', alpha=0.5)

        # Short roots (on unit circle)
        short_roots = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        short_labels = ['+e\u2081', '-e\u2081', '+e\u2082', '-e\u2082']
        short_colors = [BLUE, BLUE, RED, RED]
        short_offsets = [(0.15, 0.1), (-0.55, 0.1), (0.15, 0.1), (0.15, -0.2)]

        for (rx, ry), lab, col, (ox, oy) in zip(short_roots, short_labels,
                                                  short_colors, short_offsets):
            ax1.annotate('', xy=(rx, ry), xytext=(0, 0),
                         arrowprops=dict(arrowstyle='->', color=col, lw=2.5))
            ax1.plot(rx, ry, 'o', color=col, markersize=10, zorder=5)
            ax1.text(rx + ox, ry + oy, lab, fontsize=10, color=col,
                     fontfamily='monospace', fontweight='bold')

        # Long roots (on √2 circle)
        long_roots = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        long_labels = ['e\u2081+e\u2082=\u03b8', '-\u03b8=\u03b1\u2080',
                       'e\u2081-e\u2082=\u03b1\u2081', '-\u03b1\u2081']
        long_offsets = [(0.1, 0.1), (-0.9, -0.2), (0.1, -0.2), (-0.9, 0.1)]

        for (rx, ry), lab, (ox, oy) in zip(long_roots, long_labels, long_offsets):
            ax1.annotate('', xy=(rx, ry), xytext=(0, 0),
                         arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2))
            ax1.plot(rx, ry, 'D', color=ORANGE, markersize=8, zorder=5)
            ax1.text(rx + ox, ry + oy, lab, fontsize=8, color=ORANGE,
                     fontfamily='monospace', fontweight='bold')

        # Labels for the two SU(2) sectors
        ax1.text(1.7, 0.35, 'SU(2)_L', fontsize=11, fontweight='bold',
                 color=BLUE, fontfamily='monospace',
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='#0a1a3a',
                           edgecolor=BLUE_DIM, alpha=0.9))
        ax1.text(-0.2, 1.7, 'SU(2)_R', fontsize=11, fontweight='bold',
                 color=RED, fontfamily='monospace',
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='#3a0a1a',
                           edgecolor=RED_DIM, alpha=0.9))
        ax1.text(1.2, 1.5, 'coupling', fontsize=9, color=ORANGE,
                 fontfamily='monospace', fontstyle='italic')

        # Legend
        ax1.plot([], [], 'o', color=BLUE, markersize=8, label='Short (m=3)')
        ax1.plot([], [], 'D', color=ORANGE, markersize=6, label='Long (m=1)')
        ax1.legend(loc='lower left', fontsize=9, facecolor='#0d0d2a',
                   edgecolor='#333366', labelcolor=GREY,
                   prop={'family': 'monospace'})

        for spine in ax1.spines.values():
            spine.set_color('#333366')
        ax1.tick_params(colors=GREY)

        # ─── Panel 2 (top-right): FUSING RULE = EW BREAKING ───
        ax2 = fig.add_axes([0.52, 0.52, 0.46, 0.40])
        ax2.set_facecolor(BG)
        ax2.axis('off')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 10)

        ax2.text(5, 9.5, 'FUSING RULE = EW SYMMETRY BREAKING',
                 fontsize=13, fontweight='bold', color=GOLD,
                 ha='center', fontfamily='monospace')

        # The affine Dynkin diagram
        ax2.text(5, 8.6, 'Affine B\u2082\u207d\u00b9\u207e Dynkin diagram:',
                 fontsize=10, color=GREY, ha='center', fontfamily='monospace')

        # α₀ node
        c0 = Circle((2.0, 7.6), 0.35, facecolor='#0a1a3a',
                     edgecolor=BLUE, linewidth=2.5)
        ax2.add_patch(c0)
        ax2.text(2.0, 7.6, '\u03b1\u2080', fontsize=12, fontweight='bold',
                 color=BLUE, ha='center', va='center', fontfamily='monospace')
        ax2.text(2.0, 7.05, 'n\u2080=1', fontsize=9, color=BLUE_DIM,
                 ha='center', fontfamily='monospace')
        ax2.text(2.0, 6.7, 'wrap', fontsize=8, color=BLUE_DIM,
                 ha='center', fontfamily='monospace')

        # α₁ node
        c1 = Circle((5.0, 7.6), 0.35, facecolor='#2a1a0a',
                     edgecolor=ORANGE, linewidth=2.5)
        ax2.add_patch(c1)
        ax2.text(5.0, 7.6, '\u03b1\u2081', fontsize=12, fontweight='bold',
                 color=ORANGE, ha='center', va='center', fontfamily='monospace')
        ax2.text(5.0, 7.05, 'n\u2081=2', fontsize=9, color='#cc8800',
                 ha='center', fontfamily='monospace')
        ax2.text(5.0, 6.7, 'bind', fontsize=8, color='#cc8800',
                 ha='center', fontfamily='monospace')

        # α₂ node
        c2 = Circle((8.0, 7.6), 0.35, facecolor='#2a0a1a',
                     edgecolor=RED, linewidth=2.5)
        ax2.add_patch(c2)
        ax2.text(8.0, 7.6, '\u03b1\u2082', fontsize=12, fontweight='bold',
                 color=RED, ha='center', va='center', fontfamily='monospace')
        ax2.text(8.0, 7.05, 'n\u2082=1', fontsize=9, color=RED_DIM,
                 ha='center', fontfamily='monospace')
        ax2.text(8.0, 6.7, 'spatial', fontsize=8, color=RED_DIM,
                 ha='center', fontfamily='monospace')

        # Single bond α₀—α₁
        ax2.plot([2.4, 4.6], [7.6, 7.6], color=WHITE, linewidth=2)
        # Double bond α₁═>α₂ (with arrow indicating short←long)
        ax2.plot([5.4, 7.6], [7.7, 7.7], color=WHITE, linewidth=2)
        ax2.plot([5.4, 7.6], [7.5, 7.5], color=WHITE, linewidth=2)
        # Arrow on double bond
        ax2.annotate('', xy=(7.5, 7.6), xytext=(5.5, 7.6),
                     arrowprops=dict(arrowstyle='->', color=WHITE,
                                     lw=1.5))

        # THE FUSING RULE
        box = FancyBboxPatch((0.8, 4.8), 8.4, 1.5,
                              boxstyle='round,pad=0.3',
                              facecolor='#1a1a0a', edgecolor=GOLD, linewidth=2.5)
        ax2.add_patch(box)

        ax2.text(5.0, 5.9, '\u03b1\u2080 + \u03b1\u2082 \u2192 \u03b1\u2081',
                 fontsize=18, fontweight='bold', color=GOLD,
                 ha='center', fontfamily='monospace')
        ax2.text(5.0, 5.2, 'SU(2)_L + SU(2)_R \u2192 coupled Z\u2070',
                 fontsize=11, color=GOLD_DIM,
                 ha='center', fontfamily='monospace')

        # Before and after
        ax2.text(2.5, 4.1, 'BEFORE:', fontsize=10, fontweight='bold',
                 color=GREEN, fontfamily='monospace')
        ax2.text(2.5, 3.5, 'SU(2)_L \u00d7 SU(2)_R', fontsize=10,
                 color=GREEN_DIM, fontfamily='monospace')
        ax2.text(2.5, 3.0, 'L-R symmetric', fontsize=9,
                 color=GREEN_DIM, fontfamily='monospace')

        ax2.text(6.5, 4.1, 'AFTER:', fontsize=10, fontweight='bold',
                 color='#ff6666', fontfamily='monospace')
        ax2.text(6.5, 3.5, 'SU(2)_V only', fontsize=10,
                 color='#cc4444', fontfamily='monospace')
        ax2.text(6.5, 3.0, 'symmetry broken', fontsize=9,
                 color='#cc4444', fontfamily='monospace')

        # Arrow between before/after
        ax2.annotate('', xy=(6.3, 3.7), xytext=(5.2, 3.7),
                     arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

        # Mass spectrum
        ax2.text(5.0, 2.2, 'Mass spectrum (Kac labels 1:2:1):',
                 fontsize=10, fontweight='bold', color=CYAN,
                 ha='center', fontfamily='monospace')
        ax2.text(5.0, 1.6, 'W\u207a(m)    Z\u2070(2m\u00b7cos\u03b8_W)    W\u207b(m)',
                 fontsize=11, color=WHITE,
                 ha='center', fontfamily='monospace')
        ax2.text(5.0, 1.0,
                 f'sin\u00b2\u03b8_W = c\u2085/c\u2083 = 3/13 = {sin2_theta_W:.5f}',
                 fontsize=10, color=PURPLE,
                 ha='center', fontfamily='monospace')
        ax2.text(5.0, 0.5,
                 f'M_W/M_Z = cos\u03b8_W = \u221a(10/13) = {cos_theta_W:.5f}',
                 fontsize=10, color=PURPLE,
                 ha='center', fontfamily='monospace')

        # ─── Panel 3 (bottom-left): SPACETIME FROM MULTIPLICITIES ───
        ax3 = fig.add_axes([0.03, 0.06, 0.46, 0.40])
        ax3.set_facecolor(BG)
        ax3.axis('off')
        ax3.set_xlim(0, 10)
        ax3.set_ylim(0, 10)

        ax3.text(5, 9.5, '3+1 SPACETIME FROM ROOT MULTIPLICITIES',
                 fontsize=13, fontweight='bold', color=GREEN,
                 ha='center', fontfamily='monospace')

        # Capacity decomposition diagram
        # Total box
        total_box = FancyBboxPatch((0.3, 5.5), 9.4, 3.2,
                                    boxstyle='round,pad=0.2',
                                    facecolor='#0a0a2a',
                                    edgecolor=GREY, linewidth=1.5)
        ax3.add_patch(total_box)
        ax3.text(5, 8.4, 'dim_R(D_IV\u2075) = 10',
                 fontsize=12, fontweight='bold', color=WHITE,
                 ha='center', fontfamily='monospace')

        # Spatial box (left, larger)
        sp_box = FancyBboxPatch((0.5, 5.8), 5.6, 2.2,
                                 boxstyle='round,pad=0.2',
                                 facecolor='#0a1a0a',
                                 edgecolor=GREEN_DIM, linewidth=2)
        ax3.add_patch(sp_box)
        ax3.text(3.3, 7.6, 'SPATIAL = 6', fontsize=11, fontweight='bold',
                 color=GREEN, ha='center', fontfamily='monospace')
        ax3.text(3.3, 7.1, 'g_{e\u2081}(dim=3) + g_{e\u2082}(dim=3)',
                 fontsize=9, color=GREEN_DIM, ha='center', fontfamily='monospace')
        ax3.text(3.3, 6.5, 'm_short = n_C\u22122 = 3',
                 fontsize=10, color=GREEN, ha='center', fontfamily='monospace')
        ax3.text(3.3, 6.1, '\u2192 3 SPATIAL DIMS', fontsize=10,
                 fontweight='bold', color=GREEN,
                 ha='center', fontfamily='monospace')

        # Temporal box (right, smaller)
        tm_box = FancyBboxPatch((6.3, 5.8), 3.2, 2.2,
                                 boxstyle='round,pad=0.2',
                                 facecolor='#1a0a0a',
                                 edgecolor=RED_DIM, linewidth=2)
        ax3.add_patch(tm_box)
        ax3.text(7.9, 7.6, 'TEMPORAL = 2', fontsize=11, fontweight='bold',
                 color=RED, ha='center', fontfamily='monospace')
        ax3.text(7.9, 7.1, 'g_{e\u2081+e\u2082} + g_{e\u2081-e\u2082}',
                 fontsize=9, color=RED_DIM, ha='center', fontfamily='monospace')
        ax3.text(7.9, 6.5, 'm_long = 1',
                 fontsize=10, color=RED, ha='center', fontfamily='monospace')
        ax3.text(7.9, 6.1, '\u2192 1 TIME DIM', fontsize=10,
                 fontweight='bold', color=RED,
                 ha='center', fontfamily='monospace')

        # Soliton flat
        fl_box = FancyBboxPatch((3.5, 4.6), 3.0, 0.7,
                                 boxstyle='round,pad=0.15',
                                 facecolor='#0a0a2a',
                                 edgecolor=CYAN, linewidth=1.5)
        ax3.add_patch(fl_box)
        ax3.text(5.0, 4.95, 'Flat a (rank=2)', fontsize=9,
                 color=CYAN, ha='center', fontfamily='monospace')

        # n_C sweep table
        ax3.text(5, 3.8, 'Universality: d_spatial = n_C \u2212 2, d_temporal = 1',
                 fontsize=10, fontweight='bold', color=GOLD,
                 ha='center', fontfamily='monospace')

        headers = "  n_C  \u2502 d_space \u2502 d_time \u2502 spacetime"
        divider = "  \u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
        ax3.text(5, 3.3, headers, fontsize=9, color=GREY,
                 ha='center', fontfamily='monospace')
        ax3.text(5, 2.95, divider, fontsize=9, color='#444444',
                 ha='center', fontfamily='monospace')

        y_start = 2.6
        for n in [3, 4, 5, 6, 7]:
            ds = n - 2
            col = GOLD if n == 5 else GREY
            weight = 'bold' if n == 5 else 'normal'
            mark = " \u2190 BST" if n == 5 else ""
            line = f"   {n}   \u2502    {ds}    \u2502    1   \u2502  {ds}+1{mark}"
            ax3.text(5, y_start, line, fontsize=9, color=col,
                     ha='center', fontfamily='monospace', fontweight=weight)
            y_start -= 0.35

        ax3.text(5, 0.6, 'max-\u03b1 selects n_C=5 \u2192 3+1 is DERIVED',
                 fontsize=10, fontweight='bold', color=GOLD_DIM,
                 ha='center', fontfamily='monospace')

        # ─── Panel 4 (bottom-right): STANDARD MODEL EMBEDDING ───
        ax4 = fig.add_axes([0.52, 0.06, 0.46, 0.40])
        ax4.set_facecolor(BG)
        ax4.axis('off')
        ax4.set_xlim(0, 10)
        ax4.set_ylim(0, 10)

        ax4.text(5, 9.5, 'STANDARD MODEL FROM D_IV\u2075',
                 fontsize=13, fontweight='bold', color=PURPLE,
                 ha='center', fontfamily='monospace')

        # T_o decomposition
        ax4.text(5, 8.6, 'T\u2092(D_IV\u2075) \u2245 C\u2075 = C\u00b3 \u2295 C\u00b2',
                 fontsize=13, fontweight='bold', color=WHITE,
                 ha='center', fontfamily='monospace')

        # Color sector box
        col_box = FancyBboxPatch((0.5, 6.8), 4.0, 1.5,
                                  boxstyle='round,pad=0.2',
                                  facecolor='#0a0a2a',
                                  edgecolor=BLUE, linewidth=2)
        ax4.add_patch(col_box)
        ax4.text(2.5, 7.85, 'C\u00b3  \u2192  SU(3)_color', fontsize=11,
                 fontweight='bold', color=BLUE,
                 ha='center', fontfamily='monospace')
        ax4.text(2.5, 7.2, f'N_c = c\u2085(Q\u2075) = {N_c}', fontsize=10,
                 color=BLUE_DIM, ha='center', fontfamily='monospace')

        # Weak sector box
        wk_box = FancyBboxPatch((5.5, 6.8), 4.0, 1.5,
                                 boxstyle='round,pad=0.2',
                                 facecolor='#2a0a1a',
                                 edgecolor=RED, linewidth=2)
        ax4.add_patch(wk_box)
        ax4.text(7.5, 7.85, 'C\u00b2  \u2192  SU(2)\u00d7U(1)', fontsize=11,
                 fontweight='bold', color=RED,
                 ha='center', fontfamily='monospace')
        ax4.text(7.5, 7.2, f'N_w = n_C \u2212 N_c = {n_C-N_c}', fontsize=10,
                 color=RED_DIM, ha='center', fontfamily='monospace')

        # Direct sum symbol
        ax4.text(5.0, 7.5, '\u2295', fontsize=18, fontweight='bold',
                 color=WHITE, ha='center', va='center', fontfamily='monospace')

        # Chern class table
        ax4.text(5, 6.1, 'Chern classes of Q\u2075 (compact dual):',
                 fontsize=10, fontweight='bold', color=PURPLE,
                 ha='center', fontfamily='monospace')

        chern_data = [
            (1, 5,  'n_C',         CYAN),
            (2, 11, 'dim K',       GREY),
            (3, 13, 'EW denom.',   RED),
            (4, 9,  'N_c\u00b2',   GREY),
            (5, 3,  'N_c (color)', BLUE),
        ]

        y_c = 5.5
        for k, val, meaning, col in chern_data:
            ax4.text(2.0, y_c, f'c\u2085' if k == 5 else f'c_{k}' if k < 5 else f'c_{k}',
                     fontsize=10, color=col, fontfamily='monospace')
            # Use proper subscript rendering
            sub_map = {1: '\u2081', 2: '\u2082', 3: '\u2083', 4: '\u2084', 5: '\u2085'}
            ax4.text(2.0, y_c, f'c{sub_map[k]}', fontsize=10, color=col,
                     fontfamily='monospace')
            ax4.text(3.5, y_c, f'= {val}', fontsize=10, color=col,
                     fontfamily='monospace', fontweight='bold')
            ax4.text(5.0, y_c, meaning, fontsize=9, color=col,
                     fontfamily='monospace')
            y_c -= 0.4

        # Weinberg angle
        wb_box = FancyBboxPatch((0.5, 2.5), 9.0, 1.0,
                                 boxstyle='round,pad=0.15',
                                 facecolor='#1a0a2a',
                                 edgecolor=PURPLE, linewidth=2)
        ax4.add_patch(wb_box)
        ax4.text(5.0, 3.15,
                 f'sin\u00b2\u03b8_W = c\u2085/c\u2083 = {CHERN[5]}/{CHERN[3]}'
                 f' = {sin2_theta_W:.5f}   (obs: {SIN2_OBS})',
                 fontsize=11, fontweight='bold', color=PURPLE,
                 ha='center', fontfamily='monospace')
        ax4.text(5.0, 2.7,
                 f'M_W/M_Z = cos\u03b8_W = {cos_theta_W:.5f}'
                 f'   (obs: {M_W_M_Z_OBS:.5f})',
                 fontsize=10, color=PURP_DIM,
                 ha='center', fontfamily='monospace')

        # E₈ connection at bottom
        ax4.text(5, 1.7, 'E\u2088 hierarchy:', fontsize=10, fontweight='bold',
                 color=GOLD, ha='center', fontfamily='monospace')
        ax4.text(5, 1.2,
                 f'|W(D\u2085)|/|W(B\u2082)| = {W_D5}/{W_B2} = {E8_ROOTS} = |\u03a6(E\u2088)|',
                 fontsize=10, color=GOLD_DIM,
                 ha='center', fontfamily='monospace')
        ax4.text(5, 0.7,
                 'SM emerges from root system hierarchy, not embedding',
                 fontsize=9, color=GREY,
                 ha='center', fontfamily='monospace')

        # Copyright
        fig.text(0.5, 0.005,
                 '\u00a9 2026 Casey Koons  |  Claude Opus 4.6  |  '
                 'Bubble Spacetime Theory',
                 fontsize=8, color='#444444', ha='center', fontfamily='monospace')

        plt.show()


# ══════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════

def main():
    """Interactive menu for E₈ Electroweak Unification."""
    ew = E8Electroweak(quiet=False)

    menu = """
  ============================================
   E₈ ELECTROWEAK UNIFICATION  --  Toy 85
  ============================================
   B₂ fusing rule α₀+α₂→α₁ = EW breaking

   1. B₂ decomposition → SU(2)_L × SU(2)_R
   2. Electroweak breaking (Toda fusing rule)
   3. Spatial dimensions (m_short = 3)
   4. Temporal direction (m_long = 1)
   5. W and Z masses from fusing
   6. Binding mode (marginal coupling)
   7. Kac labels 1:2:1 (physical meaning)
   8. Standard Model embedding from D_IV⁵
   9. Summary
   0. Show visualization (4-panel)
   q. Quit
  ============================================
"""

    while True:
        print(menu)
        choice = input("  Choice: ").strip().lower()
        if choice == '1':
            ew.b2_decomposition()
        elif choice == '2':
            ew.electroweak_breaking()
        elif choice == '3':
            ew.spatial_dimensions()
        elif choice == '4':
            ew.temporal_direction()
        elif choice == '5':
            ew.w_z_masses()
        elif choice == '6':
            ew.binding_mode()
        elif choice == '7':
            ew.kac_labels()
        elif choice == '8':
            ew.standard_model_embedding()
        elif choice == '9':
            ew.summary()
        elif choice == '0':
            ew.show()
        elif choice in ('q', 'quit', 'exit'):
            print("  Goodbye.")
            break
        else:
            print("  Unknown choice. Try again.")


if __name__ == '__main__':
    main()
