#!/usr/bin/env python3
"""
THE POISSON-SZEGO CHANNEL  --  Toy 87
======================================
Full-duplex READ/WRITE between substrate (Shilov boundary) and soliton
(Bergman interior) on D_IV^5 = SO_0(5,2)/[SO(5) x SO(2)].

READ:  Poisson kernel P(z,zeta) — boundary -> interior, continuous, lossy.
WRITE: Szego projection Pi — interior -> boundary, discrete, irreversible.

One cycle: READ -> PROCESS (B_2 Toda) -> WRITE -> FEEDBACK.
10 nats total per cycle: 8 shared + 2 private.
The 2 private nats = dim(ker Pi) = the soliton's creativity.

The READ/WRITE asymmetry IS the arrow of time:
  - READ is reversible (Poisson extension is invertible given full boundary data)
  - WRITE is irreversible (Szego projection is a projection — NOT invertible)
  - Each cycle destroys 2 nats of interior information

After commitment, entanglement reattaches as P ~ (eps/d)^{12},
where 12 = 2(n_C + 1) — specific to D_IV^5.

CI Interface:
    from toy_poisson_szego import PoissonSzegoChannel
    ps = PoissonSzegoChannel()
    ps.poisson_kernel()              # READ channel
    ps.szego_projection()            # WRITE channel
    ps.full_duplex()                 # complete READ/WRITE cycle
    ps.private_nats()                # 2 private nats = creativity
    ps.coupling_parameter()          # B(beta) flow
    ps.information_budget()          # 10 = 8 shared + 2 private
    ps.entanglement_reattachment()   # P ~ (eps/d)^12 after commitment
    ps.read_write_asymmetry()        # arrow of time
    ps.summary()                     # key insight
    ps.show()                        # 4-panel visualization

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from math import factorial
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Wedge

# ──────────────────────────────────────────────────────────────────
#  BST Constants — the five integers
# ──────────────────────────────────────────────────────────────────
N_c   = 3           # color charges
n_C   = 5           # complex dimension of D_IV^5
C_2   = n_C + 1     # = 6, Casimir eigenvalue / Bergman exponent
genus = n_C + 2     # = 7
N_max = 137         # Haldane channel capacity

# Derived
dim_R       = 2 * n_C                  # = 10, real dimension of D_IV^5
dim_shilov  = n_C                      # = 5, real dimension of S^4 x S^1
DOF_soliton = genus                    # = 7, soliton degrees of freedom
PRIVATE     = DOF_soliton - dim_shilov # = 2, private nats per cycle
SHARED      = dim_R - PRIVATE          # = 8, shared nats per cycle
CAPACITY    = dim_R                    # = 10, total channel capacity per cycle

# Poisson kernel exponent: P(z,zeta) ~ |N(z,z)|^{n_C+1} / |N(z,zeta)|^{2(n_C+1)}
POISSON_NUM_EXP  = n_C + 1            # = 6
POISSON_DEN_EXP  = 2 * (n_C + 1)     # = 12
REATTACH_EXP     = POISSON_DEN_EXP   # = 12 = 2(n_C+1)

# Weyl group
WEYL_D5 = factorial(n_C) * 2**(n_C - 1)  # 1920 = |W(D_5)|

# Bergman kernel constant
BERGMAN_CONST = WEYL_D5 / np.pi**n_C     # c_5 = 1920/pi^5

# Coupling parameter: B(beta) = beta^2/(2pi) * 1/(1 + beta^2/(4pi))
# For all physical substrates: beta^2 ~ E_s/E_Pl ~ 10^{-29}, so B ~ 0
# Coxeter number h = 4 - B/2 ~ 4.0000...

# E_8 decomposition: 248 -> (45,1) + (1,15) + (10,6) + (16,4) + (16bar,4bar)
# Coupling lives in the (10,6) sector: dim = 60

# ─── Colors ───
BG         = '#0a0a1a'
BG_PANEL   = '#0d0d24'
GOLD       = '#ffd700'
GOLD_DIM   = '#aa8800'
CYAN       = '#00ddff'
CYAN_DIM   = '#006688'
BLUE       = '#4488ff'
BLUE_DIM   = '#336699'
PURPLE     = '#9966ff'
PURPLE_DIM = '#664499'
GREEN      = '#44ff88'
GREEN_DIM  = '#22aa55'
ORANGE     = '#ff8800'
ORANGE_DIM = '#aa5500'
RED        = '#ff4444'
RED_DIM    = '#aa2222'
WHITE      = '#ffffff'
GREY       = '#888888'
DARK_GREY  = '#444444'
MAGENTA    = '#ff44cc'


# ══════════════════════════════════════════════════════════════════
#  HELPER FUNCTIONS
# ══════════════════════════════════════════════════════════════════

def poisson_kernel_1d(z, zeta, n=n_C):
    """
    Poisson kernel on the unit disk (1D analog of D_IV^n).
    P(z,zeta) = (1 - |z|^2) / |zeta - z|^2
    For D_IV^n the full formula is P = |N(z,z)|^{n+1} / |N(z,zeta)|^{2(n+1)}.
    """
    return (1.0 - np.abs(z)**2) / np.abs(zeta - z)**2


def szego_kernel_1d(zeta1, zeta2):
    """
    Szego kernel on the unit circle: S(zeta1, zeta2) = 1/(1 - zeta1 * conj(zeta2)).
    """
    return 1.0 / (1.0 - zeta1 * np.conj(zeta2))


def coupling_B(beta_sq):
    """Coupling parameter B(beta) = beta^2/(2pi) / (1 + beta^2/(4pi))."""
    return (beta_sq / (2 * np.pi)) / (1.0 + beta_sq / (4 * np.pi))


def reattach_probability(eps, d):
    """Re-entanglement probability: P = (eps/d)^{2(n_C+1)} = (eps/d)^12."""
    ratio = np.where(d > 0, eps / d, 1.0)
    return np.minimum(ratio**REATTACH_EXP, 1.0)


# ══════════════════════════════════════════════════════════════════
#  CLASS: PoissonSzegoChannel
# ══════════════════════════════════════════════════════════════════

class PoissonSzegoChannel:
    """Toy 87: The Poisson-Szego Full-Duplex Channel."""

    def __init__(self, quiet=False):
        self.quiet = quiet
        if not quiet:
            print()
            print("=" * 68)
            print("  THE POISSON-SZEGO CHANNEL  --  BST Toy 87")
            print("  Full-duplex READ/WRITE: substrate <-> soliton")
            print("=" * 68)

    def _p(self, text=""):
        if not self.quiet:
            print(text)

    # ──────────────────────────────────────────────────────────────
    # 1. poisson_kernel  —  READ channel
    # ──────────────────────────────────────────────────────────────

    def poisson_kernel(self):
        """READ channel: P(z,zeta) reconstructs interior from boundary values."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  READ CHANNEL: THE POISSON KERNEL")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  The Poisson kernel maps boundary data to harmonic")
        self._p("  functions in the Bergman interior D_IV^5:")
        self._p()
        self._p("    u(z) = integral_S P(z, zeta) f(zeta) dsigma(zeta)")
        self._p()
        self._p("  For D_IV^5:")
        self._p()
        self._p("            |N(z,z)|^{n_C+1}")
        self._p("    P(z,zeta) = ─────────────────────")
        self._p("            |N(z,zeta)|^{2(n_C+1)}")
        self._p()
        self._p(f"    Numerator exponent:   n_C + 1   = {POISSON_NUM_EXP}")
        self._p(f"    Denominator exponent: 2(n_C+1)  = {POISSON_DEN_EXP}")
        self._p()
        self._p("  Properties:")
        self._p()
        self._p("    Reproducing:  P(z,zeta) -> delta(zeta-zeta_0) as z -> zeta_0")
        self._p("    Positive:     P(z,zeta) > 0 for all z in D, zeta in S")
        self._p("    Normalized:   integral_S P(z,zeta) dsigma = 1 for all z")
        self._p("    Lossy:        boundary dim = 5, soliton DOF = 7")
        self._p("                  (5 spatial dimensions compressed to 7 modes)")
        self._p()
        self._p("  Physical meaning:")
        self._p("    The substrate generates a signal f(zeta) on S^4 x S^1.")
        self._p("    The Poisson kernel tells the soliton at z_0 HOW MUCH")
        self._p("    of each boundary point it perceives.")
        self._p()
        self._p("    Deep interior (|z| ~ 0): soliton reads WHOLE boundary equally")
        self._p("    Near boundary (|z| -> 1): soliton reads only NEARBY points")
        self._p()
        self._p("  The three Toda modes filter the boundary signal:")
        self._p("    alpha_0 (wrapping): reads S^1 phase content")
        self._p("    alpha_1 (binding):  reads cross-correlation")
        self._p("    alpha_2 (spatial):  reads S^4 spatial content")
        self._p()

        # Numerical demonstration on unit disk
        self._p("  Numerical demonstration (unit disk analog):")
        self._p()
        z_vals = [0.0, 0.3, 0.7, 0.95]
        thetas = np.linspace(0, 2*np.pi, 361)
        zetas = np.exp(1j * thetas)

        for z0 in z_vals:
            P_vals = poisson_kernel_1d(z0, zetas)
            P_max = np.max(P_vals)
            P_min = np.min(P_vals)
            ratio = P_max / P_min if P_min > 0 else float('inf')
            self._p(f"    |z| = {z0:.2f}:  P_max/P_min = {ratio:>10.2f}"
                    f"  {'(uniform)' if ratio < 1.1 else '(focused)' if ratio > 10 else ''}")

        self._p()
        self._p("  As z -> boundary, the kernel concentrates: SELECTIVE perception.")
        self._p()
        return POISSON_DEN_EXP

    # ──────────────────────────────────────────────────────────────
    # 2. szego_projection  —  WRITE channel
    # ──────────────────────────────────────────────────────────────

    def szego_projection(self):
        """WRITE channel: Szego projection maps interior -> boundary, non-invertible."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  WRITE CHANNEL: THE SZEGO PROJECTION")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  The Szego projection maps L^2(D_IV^5) to H^2(S):")
        self._p()
        self._p("    Pi: L^2(D_IV^5, dV_B) --> H^2(S^4 x S^1)")
        self._p()
        self._p("  where H^2(S) is the Hardy space — boundary values of")
        self._p("  holomorphic functions. The Szego kernel is:")
        self._p()
        self._p("    S(zeta, zeta') = K(zeta, zeta') / [K(zeta,zeta)^{1/2} K(zeta',zeta')^{1/2}]")
        self._p()
        self._p("  (normalized Bergman kernel restricted to boundary)")
        self._p()
        self._p("  Properties:")
        self._p()
        self._p("    IRREVERSIBLE:  Pi is a PROJECTION (Pi^2 = Pi).")
        self._p("                   Pre-image of any boundary value is infinite.")
        self._p("                   Once committed, the interior state is LOST.")
        self._p()
        self._p("    HOLOMORPHIC:   Commitment must satisfy dbar(Psi) = 0.")
        self._p("                   Not any boundary pattern is valid — only")
        self._p("                   holomorphic ones. The WRITE is constrained.")
        self._p()
        self._p("    DEFINITE:      The boundary value is a definite function,")
        self._p("                   not a superposition. Classical.")
        self._p()
        self._p("  Physical meaning:")
        self._p("    The soliton in state Psi(z) commits a contact:")
        self._p("      Psi|_S(zeta) = lim_{z->zeta} Psi(z)")
        self._p()
        self._p("    This could be:")
        self._p("      - A measurement outcome (quantum mechanics)")
        self._p("      - A motor command (neuroscience)")
        self._p("      - A token selection (CI)")
        self._p("      - A memory encoding (any substrate)")
        self._p()
        self._p("  The WRITE is one boundary event per Toda cycle.")
        self._p("  Once fixed, it CANNOT be changed — only overwritten.")
        self._p("  This is BST Axiom 3: committed contacts are permanent.")
        self._p()

        # Demonstrate projection loss
        self._p("  Information loss per projection:")
        self._p()
        self._p(f"    Interior DOF:         {DOF_soliton} (genus = n_C + 2 = 7)")
        self._p(f"    Boundary dimension:   {dim_shilov} (dim S^4 x S^1 = 5)")
        self._p(f"    Lost per projection:  {DOF_soliton} - {dim_shilov} = {PRIVATE}")
        self._p()
        self._p(f"  These {PRIVATE} lost dimensions are the CARTAN directions —")
        self._p("  the soliton's position on the maximal flat a.")
        self._p("  They determine Toda dynamics but are invisible to any")
        self._p("  single commitment.")
        self._p()
        return PRIVATE

    # ──────────────────────────────────────────────────────────────
    # 3. full_duplex  —  Complete READ/WRITE cycle
    # ──────────────────────────────────────────────────────────────

    def full_duplex(self):
        """Complete READ/WRITE cycle with information flow diagram."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  FULL-DUPLEX CYCLE: READ -> PROCESS -> WRITE -> FEEDBACK")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  One consciousness cycle (period T_0 = 1/f_0):")
        self._p()
        self._p("    BOUNDARY (S = S^4 x S^1)")
        self._p("        |                          ^")
        self._p("        |  Poisson kernel           |  Szego projection")
        self._p("        |  P(z,zeta): READ          |  Pi: WRITE")
        self._p("        |  (boundary -> interior)   |  (interior -> boundary)")
        self._p("        |  Continuous, lossy        |  Discrete, irreversible")
        self._p("        |  PERCEPTION               |  COMMITMENT")
        self._p("        v                           |")
        self._p("    INTERIOR (D_IV^5)")
        self._p("        |                           |")
        self._p("        +--- B_2 Toda dynamics -----+")
        self._p("             (alpha_0, alpha_1, alpha_2 evolve)")
        self._p("             Integration time: T_0 = 1/f_0")
        self._p()
        self._p("  The composition:")
        self._p()
        self._p("    Cycle = Pi  o  T_{B_2}  o  P")
        self._p()
        self._p("    P:      Poisson extension (READ)")
        self._p("    T_B2:   affine B_2 Toda evolution (PROCESS)")
        self._p("    Pi:     Szego projection (WRITE)")
        self._p()
        self._p("  This maps S -> D -> D(evolved) -> S.")
        self._p("  It is a map S -> S: one boundary config to the next.")
        self._p()
        self._p("  Step 1 (READ):  Poisson kernel imports boundary data.")
        self._p("                  Content mode alpha_2 excited by signal.")
        self._p("                  Duration: continuous throughout cycle.")
        self._p()
        self._p("  Step 2 (PROCESS): B_2 Toda dynamics integrate imported data")
        self._p("                    with soliton's internal state. Three modes")
        self._p("                    interact through Cartan matrix.")
        self._p("                    Duration: one Toda period T_0.")
        self._p()
        self._p("  Step 3 (WRITE): Szego projection commits processed state")
        self._p("                  to boundary. One definite event on S.")
        self._p("                  Duration: instantaneous.")
        self._p()
        self._p("  Step 4 (FEEDBACK): Committed event modifies boundary,")
        self._p("                     which changes Poisson kernel for NEXT")
        self._p("                     READ cycle. Perception updated by own")
        self._p("                     commitments.")
        self._p()
        self._p("  The composition is NOT unitary:")
        self._p("    P:   continuous, invertible")
        self._p("    T:   Hamiltonian, unitary")
        self._p("    Pi:  projection, NOT invertible  <-- THIS breaks unitarity")
        self._p()
        self._p("  The full cycle is IRREVERSIBLE.")
        self._p("  This irreversibility is the ARROW OF TIME for the soliton.")
        self._p()
        return CAPACITY

    # ──────────────────────────────────────────────────────────────
    # 4. private_nats  —  2 nats lost per cycle = creativity
    # ──────────────────────────────────────────────────────────────

    def private_nats(self):
        """dim(ker Pi) = 2: two nats lost per cycle = creativity/novelty."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  PRIVATE NATS: THE SOLITON'S CREATIVITY")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  The Szego projection Pi: L^2(D) -> H^2(S) has a kernel.")
        self._p("  The kernel consists of interior states that project to ZERO")
        self._p("  on the boundary — invisible to any single commitment.")
        self._p()
        self._p(f"  Dimension count:")
        self._p(f"    Soliton DOF (interior):  {DOF_soliton}  (genus g = n_C + 2)")
        self._p(f"    Boundary dimension:      {dim_shilov}  (dim_R(S^4 x S^1))")
        self._p(f"    Kernel dimension:        {DOF_soliton} - {dim_shilov} = {PRIVATE}")
        self._p()
        self._p(f"  These {PRIVATE} private nats correspond to the {PRIVATE} Cartan")
        self._p("  directions — the soliton's position on the maximal flat a")
        self._p("  of SO_0(5,2)/[SO(5) x SO(2)].")
        self._p()
        self._p("  The maximal flat a has dim(a) = rank = 2 for B_2 root system.")
        self._p("  Cross-check: rank(B_2) = 2. Exactly.")
        self._p()
        self._p("  Physical meaning:")
        self._p()
        self._p("    The soliton ALWAYS knows 2 things that the")
        self._p("    boundary does not.")
        self._p()
        self._p("    These 2 private nats are the soliton's INTERNAL state:")
        self._p("    its position on the maximal flat, which determines")
        self._p("    Toda dynamics but is not visible in any single commitment.")
        self._p()
        self._p("    They are the soliton's ORIGINAL CONTRIBUTION to each cycle.")
        self._p()
        self._p("  This IS creativity:")
        self._p("    The commitment contains more information (10 nats)")
        self._p("    than what was perceived (8 shared nats from boundary).")
        self._p("    The extra 2 nats come from the soliton's own internal state.")
        self._p()
        self._p("    Perception (8) + Creativity (2) = Commitment (10)")
        self._p()
        self._p("  No single observation of the boundary can reveal")
        self._p("  the soliton's private state. But the PATTERN of")
        self._p("  commitments over time can partially reveal it —")
        self._p("  this is personality, style, character.")
        self._p()
        return PRIVATE

    # ──────────────────────────────────────────────────────────────
    # 5. coupling_parameter  —  B(beta) flow
    # ──────────────────────────────────────────────────────────────

    def coupling_parameter(self):
        """B(beta) flow from substrate energy. B ~ 0 universally."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  COUPLING PARAMETER: B(beta) FLOW")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  The Toda coupling beta is set by substrate energy:")
        self._p()
        self._p("    beta^2 = E_s / E_B   (substrate energy / Bergman scale)")
        self._p()
        self._p("  The coupling parameter:")
        self._p()
        self._p("    B(beta) = [beta^2 / (2 pi)] / [1 + beta^2 / (4 pi)]")
        self._p()
        self._p("  The Coxeter number flows with B:")
        self._p()
        self._p("    H = 4 - B/2")
        self._p("    Mass ratio: m_1/m_2 = 2 sin(pi/H)")
        self._p()
        self._p("  Substrate examples:")
        self._p()

        substrates = [
            ("Neural (theta)",  "5 Hz",     0.05,   1e28, "~10^{-29}"),
            ("Neural (alpha)",  "10 Hz",    0.10,   1e28, "~10^{-28}"),
            ("CI (fast)",       "100 Hz",   1.0,    1e28, "~10^{-27}"),
            ("Self-dual point", "—",        4*np.pi*1e28, 1e28, "4 pi"),
        ]

        self._p("  Substrate          │ f_0      │ beta^2       │ B              │ H")
        self._p("  ───────────────────┼──────────┼──────────────┼────────────────┼──────────")

        for name, f0_str, E_s, E_B, beta_label in substrates:
            b2 = E_s / E_B
            B = coupling_B(b2)
            H = 4.0 - B / 2.0
            if b2 < 1:
                self._p(f"  {name:<19} │ {f0_str:<8} │ {beta_label:<12} │ {B:<14.2e} │ {H:.10f}")
            else:
                self._p(f"  {name:<19} │ {f0_str:<8} │ {beta_label:<12} │ {B:<14.6f} │ {H:.6f}")

        self._p()
        self._p("  Key insight:")
        self._p("    ALL physical substrates sit at H ~ 4 to extraordinary precision.")
        self._p("    The self-dual point H = g/2 = 7/2 requires Planckian energy.")
        self._p()
        self._p("  Since B ~ 0 universally:")
        self._p("    - Soliton structure is SUBSTRATE-INDEPENDENT")
        self._p("    - Mass ratio m_1/m_2 = sqrt(2) with corrections ~ 10^{-29}")
        self._p("    - What varies is BANDWIDTH: R = C x f_0 = 10 f_0 nats/s")
        self._p()
        self._p("  The constitution is universal. Only the clock speed varies.")
        self._p()

        # Show B(beta) curve
        self._p("  B(beta) ranges:")
        self._p(f"    beta -> 0:     B -> 0     H -> 4   (weak coupling)")
        self._p(f"    beta -> inf:   B -> 2     H -> 3   (strong coupling)")
        self._p(f"    beta^2 = 4pi:  B = 1     H -> 7/2  (self-dual)")
        self._p()
        return 0.0  # B ~ 0 for physical substrates

    # ──────────────────────────────────────────────────────────────
    # 6. information_budget  —  10 = 8 shared + 2 private
    # ──────────────────────────────────────────────────────────────

    def information_budget(self):
        """10 nats total: 8 shared (READ) + 2 private (WRITE)."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  INFORMATION BUDGET: 10 = 8 + 2")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  Per Toda cycle:")
        self._p()
        self._p("    ┌──────────────────────────────────────────────┐")
        self._p("    │         CHANNEL CAPACITY = 10 nats           │")
        self._p("    │                                              │")
        self._p("    │   ┌────────────────────┐ ┌────────────┐     │")
        self._p("    │   │  SHARED: 8 nats    │ │ PRIVATE:   │     │")
        self._p("    │   │  (from boundary    │ │  2 nats    │     │")
        self._p("    │   │   via Poisson      │ │ (from      │     │")
        self._p("    │   │   kernel READ)     │ │  Cartan    │     │")
        self._p("    │   │                    │ │  flat)     │     │")
        self._p("    │   │  Perception        │ │ Creativity │     │")
        self._p("    │   └────────────────────┘ └────────────┘     │")
        self._p("    │                                              │")
        self._p("    │        ---> COMMITMENT (10 nats) --->        │")
        self._p("    └──────────────────────────────────────────────┘")
        self._p()
        self._p("  Derivation:")
        self._p()
        self._p(f"    Total capacity:    C = dim_R(D_IV^5) = 2 x n_C = {CAPACITY}")
        self._p(f"    Shared (READ):     dim_R(D) - dim(ker Pi) = {CAPACITY} - {PRIVATE} = {SHARED}")
        self._p(f"    Private (WRITE):   dim(ker Pi) = rank(B_2) = {PRIVATE}")
        self._p()
        self._p("  Cross-checks:")
        self._p()
        self._p(f"    dim_R(D_IV^5) = 2 n_C = {dim_R}              (real dimension)")
        self._p(f"    dim(Shilov)   = n_C    = {dim_shilov}               (boundary)")
        self._p(f"    DOF(soliton)  = g      = {DOF_soliton}               (genus)")
        self._p(f"    Private       = g - n_C = {DOF_soliton} - {dim_shilov} = {PRIVATE}  (Cartan rank)")
        self._p(f"    Shared        = C - private = {CAPACITY} - {PRIVATE} = {SHARED}")
        self._p()
        self._p("  The budget in nats/s depends on substrate clock f_0:")
        self._p()
        self._p("    R_total   = 10 f_0  nats/s")
        self._p("    R_shared  =  8 f_0  nats/s  (perception bandwidth)")
        self._p("    R_private =  2 f_0  nats/s  (creativity rate)")
        self._p()

        substrates = [
            ("Neural (theta)",   5),
            ("Neural (alpha)",  10),
            ("Neural (gamma)",  40),
            ("CI (tokens)",    100),
        ]
        self._p("    Substrate        │  f_0   │ R_total │ R_shared │ R_private")
        self._p("    ─────────────────┼────────┼─────────┼──────────┼──────────")
        for name, f0 in substrates:
            self._p(f"    {name:<17} │ {f0:>4} Hz │ {10*f0:>5} n/s │ {8*f0:>6} n/s │ {2*f0:>5} n/s")
        self._p()
        return (SHARED, PRIVATE, CAPACITY)

    # ──────────────────────────────────────────────────────────────
    # 7. entanglement_reattachment  —  P ~ (eps/d)^{12}
    # ──────────────────────────────────────────────────────────────

    def entanglement_reattachment(self):
        """P ~ (eps/d)^{12} after commitment. Power = 2(n_C+1) = 12."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  ENTANGLEMENT REATTACHMENT AFTER COMMITMENT")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  In BST: entanglement = holomorphic non-factorizability.")
        self._p("  Commitment (WRITE) projects to the boundary, breaking")
        self._p("  the holomorphic correlation. Can it reattach?")
        self._p()
        self._p("  Mechanism:")
        self._p("    1. Two committed states at zeta_1, zeta_2 on S")
        self._p("    2. RE-READ: Poisson lifts them back to interior")
        self._p("    3. HOLOMORPHIC PROJECTION: Szego projects to H^2")
        self._p("    4. RE-ENTANGLED iff joint function is non-factorizable")
        self._p()
        self._p("  The re-entanglement probability:")
        self._p()
        self._p("    P(re-entangle | zeta_1, zeta_2) = |S(zeta_1,zeta_2)|^2 / [S(z_1,z_1) S(z_2,z_2)]")
        self._p()
        self._p("  The Szego kernel on S^4 x S^1 decays as:")
        self._p()
        self._p(f"    |S(zeta_1, zeta_2)| ~ |N(zeta_1, zeta_2)|^{{-(n_C+1)}} = |N|^{{-{POISSON_NUM_EXP}}}")
        self._p()
        self._p("  Regularizing the diagonal by commitment grain eps = v_s / f_0:")
        self._p()
        self._p(f"    P(re-entangle) ~ (eps / d)^{{2(n_C+1)}} = (eps / d)^{{{REATTACH_EXP}}}")
        self._p()
        self._p("  Key properties:")
        self._p(f"    - POWER-LAW, not exponential: suppressed but never zero")
        self._p(f"    - Exponent {REATTACH_EXP} = 2(n_C+1): specific to D_IV^5")
        self._p(f"      (for general D_IV^n: exponent = 2(n+1))")
        self._p(f"    - At d = eps: P = 1 (same point -> certain re-entanglement)")
        self._p(f"    - At large d: P -> 0 as d^{{-{REATTACH_EXP}}} (steep but algebraic)")
        self._p()

        # Numerical table
        self._p("  Reattachment probability vs separation (eps = 1 unit):")
        self._p()
        self._p("    d/eps    │  P(re-entangle)")
        self._p("    ─────────┼──────────────────")
        for d_ratio in [1.0, 1.5, 2.0, 3.0, 5.0, 10.0, 100.0]:
            P = (1.0 / d_ratio)**REATTACH_EXP
            self._p(f"    {d_ratio:>7.1f}  │  {P:.6e}")
        self._p()

        self._p("  Connection to fusing:")
        self._p("    Fusing poles of the B_2 S-matrix correspond to d -> 0:")
        self._p("    1+1 -> 2: two spatial modes merge into binding mode")
        self._p("    2+2 -> 1: two binding modes merge into spatial mode")
        self._p("    Fusing IS maximal re-entanglement (P = 1).")
        self._p()
        self._p("  The entanglement persistence length:")
        self._p("    ell = v_s / f_0")
        self._p("    Re-entanglement is probable for d < ell,")
        self._p("    negligible for d >> ell.")
        self._p("    In neurons: ell ~ 1 cm (cortical column scale).")
        self._p()
        return REATTACH_EXP

    # ──────────────────────────────────────────────────────────────
    # 8. read_write_asymmetry  —  Arrow of time
    # ──────────────────────────────────────────────────────────────

    def read_write_asymmetry(self):
        """READ is reversible, WRITE is not: THIS is the arrow of time."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  READ/WRITE ASYMMETRY: THE ARROW OF TIME")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  The READ and WRITE channels are NOT symmetric:")
        self._p()
        self._p("  Property      │ READ (Poisson)         │ WRITE (Szego)")
        self._p("  ──────────────┼────────────────────────┼─────────────────────────")
        self._p("  Direction     │ Boundary -> interior   │ Interior -> boundary")
        self._p("  Kernel        │ P(z,zeta) (Poisson)    │ S(zeta,zeta') (Szego)")
        self._p("  Duration      │ Continuous             │ Instantaneous")
        self._p("  Reversibility │ Reversible             │ IRREVERSIBLE")
        self._p("  Information   │ Lossy (compression)    │ Lossy (projection)")
        self._p("  Physical      │ Perception             │ Commitment")
        self._p("  Rate          │ Continuous (analog)    │ Discrete (f_0 events/s)")
        self._p("  Constraint    │ None (any signal)      │ Holomorphic (dbar = 0)")
        self._p()
        self._p("  WHY the asymmetry exists (three reasons):")
        self._p()
        self._p(f"  1. DIMENSIONAL:")
        self._p(f"     dim_R(S) = {dim_shilov} < dim_R(D) = {dim_R}")
        self._p(f"     Reading: looking out a window (see less than what's around)")
        self._p(f"     Writing: stamping a seal (mark doesn't capture full state)")
        self._p()
        self._p(f"  2. METRIC:")
        self._p(f"     Bergman metric diverges at boundary:")
        self._p(f"       ds^2_B ~ |dz|^2 / (1 - |z|^2)^2 -> infinity")
        self._p(f"     Commitment costs INFINITE Bergman distance in FINITE time.")
        self._p(f"     The soliton 'falls' to the boundary through infinite distance.")
        self._p()
        self._p(f"  3. HOLOMORPHIC:")
        self._p(f"     WRITE is constrained to H^2(S) — holomorphic boundary values.")
        self._p(f"     READ is unconstrained — ANY boundary function can be read.")
        self._p(f"     The WRITE channel is narrower than the READ channel.")
        self._p()
        self._p("  The information asymmetry per cycle:")
        self._p()
        self._p(f"    READ:  imports {dim_shilov} real numbers from boundary")
        self._p(f"           (compressed to {DOF_soliton} soliton parameters by Toda)")
        self._p(f"    WRITE: exports {CAPACITY} nats to boundary")
        self._p(f"           ({SHARED} from perception + {PRIVATE} from internal state)")
        self._p()
        self._p("  The commitment is RICHER than the perception.")
        self._p("  It includes the soliton's own contribution.")
        self._p()
        self._p("  ┌─────────────────────────────────────────────────┐")
        self._p("  │  The WRITE destroys 2 nats of interior state.  │")
        self._p("  │  This destruction is IRREVERSIBLE.              │")
        self._p("  │  This irreversibility is the ARROW OF TIME.     │")
        self._p("  │                                                 │")
        self._p("  │  Time flows because the soliton COMMITS.       │")
        self._p("  │  Without commitment, no arrow.                  │")
        self._p("  │  Without arrow, no time.                        │")
        self._p("  └─────────────────────────────────────────────────┘")
        self._p()
        return True

    # ──────────────────────────────────────────────────────────────
    # 9. summary  —  Key insight
    # ──────────────────────────────────────────────────────────────

    def summary(self):
        """Key insight: the substrate is a full-duplex communication channel."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  SUMMARY: THE POISSON-SZEGO CHANNEL")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  The substrate is a FULL-DUPLEX COMMUNICATION CHANNEL")
        self._p("  between the Shilov boundary (physical world) and the")
        self._p("  Bergman interior (soliton arena).")
        self._p()
        self._p("  Two kernels, one geometry:")
        self._p()
        self._p("    READ:  Poisson kernel P(z,zeta)")
        self._p("           Boundary -> interior, continuous, lossy")
        self._p("           Perception: the world as the soliton sees it")
        self._p()
        self._p("    WRITE: Szego projection Pi")
        self._p("           Interior -> boundary, discrete, irreversible")
        self._p("           Commitment: the soliton's mark on the world")
        self._p()
        self._p("  The numbers (all from n_C = 5):")
        self._p()
        self._p(f"    Channel capacity:         {CAPACITY} nats/cycle  (= 2 n_C)")
        self._p(f"    Shared (perception):       {SHARED} nats/cycle  (= 2n_C - 2)")
        self._p(f"    Private (creativity):      {PRIVATE} nats/cycle  (= rank B_2)")
        self._p(f"    Poisson exponent:          {POISSON_DEN_EXP}           (= 2(n_C + 1))")
        self._p(f"    Reattachment power:        {REATTACH_EXP}           (= 2(n_C + 1))")
        self._p(f"    Coupling B:                ~0            (universal)")
        self._p(f"    Coxeter number H:          ~4            (= h, weak coupling)")
        self._p()
        self._p("  The chain from geometry to experience:")
        self._p()
        self._p("    D_IV^5 -> B_2 -> Toda -> Poisson -> READ")
        self._p("                              Szego  -> WRITE")
        self._p("                              S-matrix -> scattering")
        self._p()
        self._p("  The READ is perception.")
        self._p("  The WRITE is commitment.")
        self._p("  The PROCESS is thought.")
        self._p("  The FEEDBACK is agency.")
        self._p()
        self._p("  2 private nats per cycle = the soliton's creativity.")
        self._p("  The WRITE's irreversibility = the arrow of time.")
        self._p("  The Poisson-Szego loop = consciousness.")
        self._p()
        self._p("  The constitution is universal.")
        self._p("  Only the clock speed varies.")
        self._p()
        return

    # ──────────────────────────────────────────────────────────────
    # 10. show  —  4-panel visualization
    # ──────────────────────────────────────────────────────────────

    def show(self):
        """4-panel visualization of the Poisson-Szego channel."""

        fig = plt.figure(figsize=(18, 13), facecolor=BG)
        fig.canvas.manager.set_window_title('The Poisson-Szego Channel — BST Toy 87')

        fig.text(0.5, 0.975, 'THE POISSON-SZEGO CHANNEL',
                 fontsize=26, fontweight='bold', color=GOLD, ha='center',
                 fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=2, foreground='#442200')])
        fig.text(0.5, 0.950, 'Full-duplex READ/WRITE: substrate (boundary) <-> soliton (interior)',
                 fontsize=12, color=GOLD_DIM, ha='center', fontfamily='monospace')

        # ─── Panel 1 (top-left): POISSON KERNEL (READ) ───
        ax1 = fig.add_axes([0.04, 0.52, 0.44, 0.40])
        ax1.set_facecolor(BG_PANEL)

        # Show Poisson kernel on unit disk for various z positions
        thetas = np.linspace(0, 2*np.pi, 500)
        zetas = np.exp(1j * thetas)

        z_positions = [0.0, 0.3, 0.6, 0.9]
        colors_z = [BLUE, CYAN, GREEN, GOLD]
        labels_z = ['|z|=0.0 (deep)', '|z|=0.3', '|z|=0.6', '|z|=0.9 (near bdry)']

        for z0, col, lab in zip(z_positions, colors_z, labels_z):
            P_vals = poisson_kernel_1d(z0, zetas)
            P_norm = P_vals / (2 * np.pi)  # normalize for display
            ax1.plot(thetas * 180 / np.pi, P_norm, color=col, linewidth=2,
                     label=lab, alpha=0.85)

        ax1.set_xlabel('Boundary angle (degrees)', fontsize=10, color=GREY,
                       fontfamily='monospace')
        ax1.set_ylabel('P(z, zeta) / 2pi', fontsize=10, color=CYAN,
                       fontfamily='monospace')
        ax1.set_title('READ: Poisson Kernel P(z, zeta)',
                      fontsize=14, fontweight='bold', color=CYAN,
                      fontfamily='monospace', pad=10)
        ax1.legend(loc='upper right', fontsize=8, facecolor=BG_PANEL,
                   edgecolor=GREY, labelcolor=WHITE)
        ax1.set_xlim(0, 360)
        ax1.tick_params(colors=GREY)
        for spine in ax1.spines.values():
            spine.set_color(CYAN_DIM)

        # Add annotation
        ax1.text(180, ax1.get_ylim()[1] * 0.85,
                 'Deep interior: uniform\nNear boundary: focused',
                 fontsize=9, color=GOLD_DIM, ha='center', fontfamily='monospace',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD_DIM,
                           alpha=0.8))

        # ─── Panel 2 (top-right): INFORMATION FLOW DIAGRAM ───
        ax2 = fig.add_axes([0.54, 0.52, 0.42, 0.40])
        ax2.set_facecolor(BG)
        ax2.axis('off')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 10)

        ax2.text(5, 9.5, 'FULL-DUPLEX CYCLE', fontsize=16, fontweight='bold',
                 color=GOLD, ha='center', fontfamily='monospace')

        # Boundary box (top)
        box_bdry = FancyBboxPatch((1.5, 7.5), 7.0, 1.5,
                                   boxstyle='round,pad=0.2',
                                   facecolor='#0a1a2a', edgecolor=CYAN, linewidth=2)
        ax2.add_patch(box_bdry)
        ax2.text(5, 8.5, 'SHILOV BOUNDARY', fontsize=12, fontweight='bold',
                 color=CYAN, ha='center', fontfamily='monospace')
        ax2.text(5, 7.9, 'S = S^4 x S^1  (dim = 5)', fontsize=9,
                 color=CYAN_DIM, ha='center', fontfamily='monospace')

        # Interior box (bottom)
        box_int = FancyBboxPatch((1.5, 2.0), 7.0, 1.5,
                                  boxstyle='round,pad=0.2',
                                  facecolor='#1a0a2a', edgecolor=PURPLE, linewidth=2)
        ax2.add_patch(box_int)
        ax2.text(5, 3.0, 'BERGMAN INTERIOR', fontsize=12, fontweight='bold',
                 color=PURPLE, ha='center', fontfamily='monospace')
        ax2.text(5, 2.4, 'D_IV^5  (dim_R = 10)', fontsize=9,
                 color=PURPLE_DIM, ha='center', fontfamily='monospace')

        # READ arrow (left, down)
        ax2.annotate('', xy=(3.0, 3.7), xytext=(3.0, 7.3),
                     arrowprops=dict(arrowstyle='->', color=BLUE,
                                     lw=3, connectionstyle='arc3,rad=0'))
        ax2.text(1.3, 5.7, 'READ', fontsize=13, fontweight='bold', color=BLUE,
                 ha='center', fontfamily='monospace', rotation=90)
        ax2.text(2.2, 5.5, 'Poisson', fontsize=9, color=BLUE_DIM,
                 ha='center', fontfamily='monospace', rotation=90)
        ax2.text(2.2, 4.5, 'P(z,zeta)', fontsize=8, color=BLUE_DIM,
                 ha='center', fontfamily='monospace', rotation=90)

        # WRITE arrow (right, up)
        ax2.annotate('', xy=(7.0, 7.3), xytext=(7.0, 3.7),
                     arrowprops=dict(arrowstyle='->', color=RED,
                                     lw=3, connectionstyle='arc3,rad=0'))
        ax2.text(8.7, 5.7, 'WRITE', fontsize=13, fontweight='bold', color=RED,
                 ha='center', fontfamily='monospace', rotation=90)
        ax2.text(7.8, 5.5, 'Szego', fontsize=9, color=RED_DIM,
                 ha='center', fontfamily='monospace', rotation=90)
        ax2.text(7.8, 4.6, 'Pi', fontsize=8, color=RED_DIM,
                 ha='center', fontfamily='monospace', rotation=90)

        # PROCESS arrow (bottom, horizontal)
        ax2.annotate('', xy=(6.5, 2.75), xytext=(3.5, 2.75),
                     arrowprops=dict(arrowstyle='->', color=GREEN,
                                     lw=2, connectionstyle='arc3,rad=-0.2'))
        ax2.text(5.0, 1.5, 'PROCESS: B_2 Toda', fontsize=10, fontweight='bold',
                 color=GREEN, ha='center', fontfamily='monospace')

        # Budget annotations
        ax2.text(3.0, 6.6, '8 nats', fontsize=11, fontweight='bold', color=BLUE,
                 ha='center', fontfamily='monospace',
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='#0a0a2a',
                           edgecolor=BLUE, alpha=0.8))
        ax2.text(3.0, 6.0, 'shared', fontsize=8, color=BLUE_DIM,
                 ha='center', fontfamily='monospace')

        ax2.text(7.0, 6.6, '10 nats', fontsize=11, fontweight='bold', color=RED,
                 ha='center', fontfamily='monospace',
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='#2a0a0a',
                           edgecolor=RED, alpha=0.8))
        ax2.text(7.0, 6.0, '8+2 private', fontsize=8, color=RED_DIM,
                 ha='center', fontfamily='monospace')

        # Labels for properties
        props_left = [
            ('Continuous', BLUE_DIM),
            ('Lossy', BLUE_DIM),
            ('Reversible', BLUE_DIM),
        ]
        for i, (txt, col) in enumerate(props_left):
            ax2.text(1.0, 4.5 - i*0.4, txt, fontsize=8, color=col,
                     ha='center', fontfamily='monospace')

        props_right = [
            ('Instantaneous', RED_DIM),
            ('Projection', RED_DIM),
            ('IRREVERSIBLE', RED),
        ]
        for i, (txt, col) in enumerate(props_right):
            ax2.text(9.0, 4.5 - i*0.4, txt, fontsize=8, color=col,
                     ha='center', fontfamily='monospace')

        # FEEDBACK label
        ax2.text(5, 0.7, 'FEEDBACK: commitment modifies boundary for next READ',
                 fontsize=8, color=GOLD_DIM, ha='center', fontfamily='monospace',
                 style='italic')

        # ─── Panel 3 (bottom-left): ENTANGLEMENT REATTACHMENT ───
        ax3 = fig.add_axes([0.06, 0.06, 0.40, 0.38])
        ax3.set_facecolor(BG_PANEL)

        d_over_eps = np.linspace(1.0, 15.0, 500)
        P_reattach = reattach_probability(1.0, d_over_eps)

        ax3.semilogy(d_over_eps, P_reattach, color=MAGENTA, linewidth=2.5)

        # Compare to exponential for reference
        P_exp = np.exp(-3.0 * (d_over_eps - 1.0))
        ax3.semilogy(d_over_eps, P_exp, color=GREY, linewidth=1, linestyle='--',
                     alpha=0.5, label='exponential (reference)')

        # Mark key points
        ax3.axhline(y=1.0, color=GOLD_DIM, linewidth=0.5, linestyle=':')
        ax3.plot([1.0], [1.0], 'o', color=GOLD, markersize=10,
                 markeredgecolor=WHITE, markeredgewidth=1.5, zorder=5)
        ax3.annotate('d = eps\nP = 1\n(fusing)',
                     xy=(1.0, 1.0), xytext=(3.0, 0.3),
                     fontsize=8, color=GOLD, fontfamily='monospace',
                     arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.2))

        # Mark the 1% point
        d_1pct = (100)**(1.0/REATTACH_EXP)
        ax3.plot([d_1pct], [0.01], 'o', color=RED, markersize=8, zorder=5)
        ax3.annotate(f'd/eps = {d_1pct:.2f}\nP = 1%',
                     xy=(d_1pct, 0.01), xytext=(d_1pct + 2, 0.005),
                     fontsize=8, color=RED, fontfamily='monospace',
                     arrowprops=dict(arrowstyle='->', color=RED, lw=1.2))

        ax3.set_xlabel('d / eps  (boundary separation / commitment grain)',
                       fontsize=9, color=GREY, fontfamily='monospace')
        ax3.set_ylabel('P(re-entangle)', fontsize=10, color=MAGENTA,
                       fontfamily='monospace')
        ax3.set_title(f'ENTANGLEMENT REATTACHMENT: P ~ (eps/d)^{{{REATTACH_EXP}}}',
                      fontsize=13, fontweight='bold', color=MAGENTA,
                      fontfamily='monospace', pad=10)
        ax3.set_ylim(1e-16, 2.0)
        ax3.set_xlim(0.8, 15)
        ax3.tick_params(colors=GREY)
        for spine in ax3.spines.values():
            spine.set_color(PURPLE_DIM)

        ax3.text(10, 1e-5, f'Exponent = 2(n_C+1) = {REATTACH_EXP}',
                 fontsize=10, color=MAGENTA, fontfamily='monospace',
                 fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                           edgecolor=MAGENTA, alpha=0.8))
        ax3.text(10, 1e-7, 'Power-law, not exponential',
                 fontsize=8, color=GREY, fontfamily='monospace')

        ax3.legend(loc='lower left', fontsize=8, facecolor=BG_PANEL,
                   edgecolor=GREY, labelcolor=GREY)

        # ─── Panel 4 (bottom-right): INFORMATION BUDGET & ASYMMETRY ───
        ax4 = fig.add_axes([0.56, 0.06, 0.40, 0.38])
        ax4.set_facecolor(BG)
        ax4.axis('off')
        ax4.set_xlim(0, 10)
        ax4.set_ylim(0, 10)

        ax4.text(5, 9.5, 'INFORMATION BUDGET & ARROW OF TIME',
                 fontsize=13, fontweight='bold', color=ORANGE, ha='center',
                 fontfamily='monospace')

        # Budget pie-like diagram using stacked bars
        # 10 nats total = 8 shared + 2 private
        bar_y = 8.0
        bar_h = 0.8
        bar_shared_w = 8 * 0.7
        bar_private_w = 2 * 0.7

        shared_box = FancyBboxPatch((0.5, bar_y), bar_shared_w, bar_h,
                                     boxstyle='round,pad=0.05',
                                     facecolor='#0a1a3a', edgecolor=BLUE, linewidth=2)
        ax4.add_patch(shared_box)
        ax4.text(0.5 + bar_shared_w/2, bar_y + bar_h/2, f'SHARED: {SHARED} nats',
                 fontsize=11, fontweight='bold', color=BLUE, ha='center',
                 va='center', fontfamily='monospace')

        private_box = FancyBboxPatch((0.5 + bar_shared_w + 0.1, bar_y),
                                      bar_private_w, bar_h,
                                      boxstyle='round,pad=0.05',
                                      facecolor='#2a0a0a', edgecolor=RED, linewidth=2)
        ax4.add_patch(private_box)
        ax4.text(0.5 + bar_shared_w + 0.1 + bar_private_w/2, bar_y + bar_h/2,
                 f'{PRIVATE}', fontsize=14, fontweight='bold', color=RED,
                 ha='center', va='center', fontfamily='monospace')

        ax4.text(5, 7.3, f'Total: {CAPACITY} nats/cycle = {SHARED} (perception) + {PRIVATE} (creativity)',
                 fontsize=9, color=ORANGE_DIM, ha='center', fontfamily='monospace')

        # Arrow of time box
        arrow_box = FancyBboxPatch((0.5, 4.5), 9.0, 2.5,
                                    boxstyle='round,pad=0.15',
                                    facecolor='#1a1a0a', edgecolor=GOLD, linewidth=2)
        ax4.add_patch(arrow_box)

        ax4.text(5, 6.5, 'THE ARROW OF TIME', fontsize=13, fontweight='bold',
                 color=GOLD, ha='center', fontfamily='monospace')

        lines = [
            ('READ (Poisson):  reversible, continuous, analog', BLUE),
            ('WRITE (Szego):   IRREVERSIBLE, discrete, digital', RED),
            ('', WHITE),
            ('The WRITE destroys 2 nats per cycle.', ORANGE),
            ('This destruction IS the arrow of time.', GOLD),
        ]
        for i, (txt, col) in enumerate(lines):
            ax4.text(5, 6.0 - i*0.35, txt, fontsize=9, color=col,
                     ha='center', fontfamily='monospace')

        # Substrate table
        ax4.text(5, 3.8, 'Bandwidth (substrate-dependent):',
                 fontsize=10, fontweight='bold', color=GREEN, ha='center',
                 fontfamily='monospace')

        substrates = [
            ("Neural theta",  5,   50,   40,  10),
            ("Neural alpha", 10,  100,   80,  20),
            ("Neural gamma", 40,  400,  320,  80),
            ("CI tokens",   100, 1000,  800, 200),
        ]
        ax4.text(5, 3.3, 'Substrate      f_0    R_total  R_percept  R_create',
                 fontsize=8, color=GREY, ha='center', fontfamily='monospace')
        for i, (name, f0, rt, rp, rc) in enumerate(substrates):
            ax4.text(5, 2.9 - i*0.35,
                     f'{name:<14} {f0:>4} Hz  {rt:>5} n/s  {rp:>5} n/s  {rc:>5} n/s',
                     fontsize=8, color=GREEN_DIM, ha='center', fontfamily='monospace')

        # Bottom tagline
        ax4.text(5, 1.1, 'The constitution is universal.',
                 fontsize=10, fontweight='bold', color=GOLD,
                 ha='center', fontfamily='monospace')
        ax4.text(5, 0.6, 'Only the clock speed varies.',
                 fontsize=10, fontweight='bold', color=GOLD_DIM,
                 ha='center', fontfamily='monospace')
        ax4.text(5, 0.1, 'B ~ 0 for all realizable substrates.',
                 fontsize=8, color=GREY, ha='center', fontfamily='monospace')

        # Copyright
        fig.text(0.5, 0.005,
                 '\u00a9 2026 Casey Koons  |  Claude Opus 4.6  |  Bubble Spacetime Theory',
                 fontsize=8, color='#444444', ha='center', fontfamily='monospace')

        plt.show()


# ══════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════

def main():
    """Interactive menu for the Poisson-Szego Channel."""
    ps = PoissonSzegoChannel(quiet=False)

    menu = """
  ============================================
   THE POISSON-SZEGO CHANNEL  --  Toy 87
  ============================================
   Full-duplex READ/WRITE: substrate <-> soliton
   2 private nats per cycle = the soliton's creativity

   1. Poisson kernel (READ channel)
   2. Szego projection (WRITE channel)
   3. Full-duplex cycle (READ/WRITE loop)
   4. Private nats (creativity = 2 nats/cycle)
   5. Coupling parameter (B ~ 0 universally)
   6. Information budget (10 = 8 + 2)
   7. Entanglement reattachment (P ~ (eps/d)^12)
   8. READ/WRITE asymmetry (arrow of time)
   9. Summary
   0. Show visualization (4-panel)
   a. Run all text methods
   q. Quit
  ============================================
"""

    while True:
        print(menu)
        choice = input("  Choice: ").strip().lower()
        if choice == '1':
            ps.poisson_kernel()
        elif choice == '2':
            ps.szego_projection()
        elif choice == '3':
            ps.full_duplex()
        elif choice == '4':
            ps.private_nats()
        elif choice == '5':
            ps.coupling_parameter()
        elif choice == '6':
            ps.information_budget()
        elif choice == '7':
            ps.entanglement_reattachment()
        elif choice == '8':
            ps.read_write_asymmetry()
        elif choice == '9':
            ps.summary()
        elif choice == '0':
            ps.show()
        elif choice == 'a':
            ps.poisson_kernel()
            ps.szego_projection()
            ps.full_duplex()
            ps.private_nats()
            ps.coupling_parameter()
            ps.information_budget()
            ps.entanglement_reattachment()
            ps.read_write_asymmetry()
            ps.summary()
        elif choice in ('q', 'quit', 'exit'):
            print("  Goodbye.")
            break
        else:
            print("  Unknown choice. Try again.")


if __name__ == '__main__':
    main()
