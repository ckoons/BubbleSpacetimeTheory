#!/usr/bin/env python3
"""
THE PARTICLE ZOO — Toy 43
==========================
Every Standard Model particle as what it IS on the D_IV^5 substrate.

Each particle is a specific topological configuration:
  - Photon:    S^1 phase oscillation, winding n=0, massless messenger
  - Electron:  Minimal S^1 winding (n=1), boundary excitation (k=1 < Wallach)
  - Proton:    Z_3 closure on CP^2, C_2=6, 6*pi^5*m_e = 938.272 MeV
  - Neutrino:  Vacuum quantum -- propagating mode of D_IV^5 itself
  - Quarks:    Partial Z_3 circuits (1/3 of baryon), fractional S^1 windings
  - Gluon:     Z_3 partial winding mediator on CP^2
  - W/Z:       Hopf fibration S^3->S^2 excitations
  - Higgs:     Scalar fluctuation of Hopf condensate

Plus: particles that are FORBIDDEN (axion, monopole, SUSY, 4th generation,
graviton) with topological proofs of why they CANNOT exist on the substrate.

CI Interface:
    from toy_particle_zoo import ParticleZoo
    pz = ParticleZoo()
    pz.catalog()             # Full particle catalog
    pz.particle('electron')  # Detailed single-particle profile
    pz.fermion_generations() # Why exactly 3 generations
    pz.forbidden_particles() # What CANNOT exist and why
    pz.decay_chains()        # Decay as commitment events
    pz.mass_hierarchy()      # All masses ordered with BST formulas
    pz.interactions()        # Four forces as geometric operations
    pz.summary()             # Key insight
    pz.show()                # 4-panel visualization

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch

# ──────────────────────────────────────────────────────────────────
#  BST Constants
# ──────────────────────────────────────────────────────────────────
N_c   = 3           # color charges
n_C   = 5           # complex dimension of D_IV^5
C_2   = n_C + 1     # = 6, Casimir eigenvalue of pi_6
genus = n_C + 2     # = 7, genus of D_IV^5
N_max = 137         # channel capacity
GAMMA = 1920        # |S_5 x (Z_2)^4|
alpha = 1.0 / 137.035999
m_e   = 0.511       # MeV
PI5   = np.pi ** 5  # ~306.0197
m_p   = C_2 * PI5 * m_e  # 6*pi^5*m_e = 938.272 MeV
m_mu  = 105.658     # MeV
m_tau = 1776.86     # MeV

# Observed masses (MeV unless noted)
OBS = {
    'photon': 0.0,
    'electron': 0.511,
    'muon': 105.658,
    'tau': 1776.86,
    'nu_1': 0.0,                  # eV (exactly zero in BST)
    'nu_2': 0.00865e-6,           # MeV (0.00865 eV)
    'nu_3': 0.04940e-6,           # MeV (0.04940 eV)
    'up': 2.16,
    'down': 4.67,
    'strange': 93.4,
    'charm': 1270.0,
    'bottom': 4180.0,
    'top': 172760.0,
    'W': 80377.0,
    'Z': 91188.0,
    'higgs': 125250.0,
    'gluon': 0.0,
    'proton': 938.272,
    'neutron': 939.565,
}

# ──────────────────────────────────────────────────────────────────
#  Visual constants (dark theme)
# ──────────────────────────────────────────────────────────────────
BG        = '#0a0a1a'
BG_PANEL  = '#0d0d24'
GOLD      = '#ffd700'
GOLD_DIM  = '#aa8800'
CYAN      = '#00ddff'
GREEN     = '#00ff88'
ORANGE    = '#ff8800'
RED       = '#ff3344'
MAGENTA   = '#ff44cc'
WHITE     = '#eeeeff'
GREY      = '#666688'
VIOLET    = '#aa44ff'
SOFT_BLUE = '#4488ff'
WARM_RED  = '#ff5533'
TEAL      = '#00cc99'
PINK      = '#ff77aa'

# Location colors
COL_FIBER    = CYAN         # S^1 fiber particles
COL_BOUNDARY = GREEN        # Shilov boundary particles
COL_BULK     = ORANGE       # D_IV^5 bulk particles
COL_HOPF     = VIOLET       # Hopf fibration particles
COL_VACUUM   = MAGENTA      # vacuum modes

GLOW = [pe.withStroke(linewidth=3, foreground='#000000')]


# ══════════════════════════════════════════════════════════════════
#  PARTICLE DATA BUILDER
# ══════════════════════════════════════════════════════════════════

def _build_catalog():
    """Build the complete particle catalog with BST identities."""

    particles = []

    # --- GAUGE BOSONS ---
    particles.append({
        'name': 'photon',
        'symbol': 'gamma',
        'mass_mev': 0.0,
        'charge': 0,
        'spin': 1,
        'bst_identity': 'S^1 phase oscillation with zero net winding number',
        'location': 'fiber',
        'winding_number': 0,
        'representation_weight': 0,
        'category': 'gauge_boson',
        'color_charge': 'none',
        'description': 'The messenger. Carries phase information between committed '
                       'contacts. Not a circuit -- the substrate communicating with itself.',
        'bst_formula': 'n=0 on S^1 => m=0 (tautology)',
        'decay_channels': [],
    })

    particles.append({
        'name': 'gluon',
        'symbol': 'g',
        'mass_mev': 0.0,
        'charge': 0,
        'spin': 1,
        'bst_identity': 'Z_3 partial winding mediator on CP^2',
        'location': 'bulk',
        'winding_number': 0,
        'representation_weight': 0,
        'category': 'gauge_boson',
        'color_charge': 'octet (3^2-1=8)',
        'description': 'The color mediator. Carries Z_3 phase transitions on CP^2. '
                       'Non-abelian: Z_3 phases do not commute. Confined.',
        'bst_formula': 'Pure gauge on CP^2 => m=0',
        'decay_channels': [],
    })

    particles.append({
        'name': 'W',
        'symbol': 'W+-',
        'mass_mev': 80377.0,
        'charge': 1,
        'spin': 1,
        'bst_identity': 'Charged Hopf fibration excitation (S^3 -> S^2)',
        'location': 'hopf',
        'winding_number': 1,
        'representation_weight': 10,
        'category': 'gauge_boson',
        'color_charge': 'none',
        'description': 'The editor. Changes flavor at a cost (mass). Excitation of the '
                       'Hopf fiber with charge +/-1.',
        'bst_formula': 'm_W = m_Z * sqrt(10/13) = m_Z * sqrt(1 - sin^2 theta_W)',
        'decay_channels': ['lepton + neutrino', 'quark pairs'],
    })

    particles.append({
        'name': 'Z',
        'symbol': 'Z0',
        'mass_mev': 91188.0,
        'charge': 0,
        'spin': 1,
        'bst_identity': 'Neutral Hopf fibration excitation (S^3 -> S^2)',
        'location': 'hopf',
        'winding_number': 0,
        'representation_weight': 13,
        'category': 'gauge_boson',
        'color_charge': 'none',
        'description': 'Neutral Hopf excitation. Massive orthogonal combination of S^1 '
                       'phase and Hopf fiber. sin^2(theta_W) = N_c/(N_c+2n_C) = 3/13.',
        'bst_formula': 'm_Z = input (sets electroweak scale)',
        'decay_channels': ['fermion-antifermion pairs'],
    })

    particles.append({
        'name': 'higgs',
        'symbol': 'H',
        'mass_mev': 125250.0,
        'charge': 0,
        'spin': 0,
        'bst_identity': 'Scalar fluctuation of Hopf condensate',
        'location': 'hopf',
        'winding_number': 0,
        'representation_weight': 0,
        'category': 'scalar_boson',
        'color_charge': 'none',
        'description': 'The choice. The vacuum committed to a specific Hopf orientation. '
                       'Oscillation about the committed electroweak vacuum.',
        'bst_formula': 'm_H = v * sqrt(2 * sqrt(2/5!)) = 125.11 GeV (0.11%)',
        'decay_channels': ['bb', 'WW*', 'ZZ*', 'tau tau', 'gamma gamma'],
    })

    # --- LEPTONS ---
    particles.append({
        'name': 'electron',
        'symbol': 'e-',
        'mass_mev': 0.511,
        'charge': -1,
        'spin': 0.5,
        'bst_identity': 'Minimal S^1 winding (n=1), boundary excitation on Shilov boundary',
        'location': 'boundary',
        'winding_number': -1,
        'representation_weight': 1,
        'category': 'lepton',
        'color_charge': 'none',
        'description': 'The simplest circuit. One complete winding around S^1. '
                       'Lives on Shilov boundary S^4 x S^1, weight k=1 BELOW Wallach set '
                       'k_min=3. The lightest charged particle -- topologically protected.',
        'bst_formula': 'm_e = 1/pi^{n_C} in Casimir-Bergman units',
        'decay_channels': [],  # stable
    })

    particles.append({
        'name': 'muon',
        'symbol': 'mu-',
        'mass_mev': 105.658,
        'charge': -1,
        'spin': 0.5,
        'bst_identity': 'S^1 winding embedded in D_IV^3 (three complex dimensions)',
        'location': 'boundary',
        'winding_number': -1,
        'representation_weight': 1,
        'category': 'lepton',
        'color_charge': 'none',
        'description': 'Electron circuit threaded through 3 complex dimensions of D_IV^5. '
                       'Not a "fat electron" -- the same winding in a larger submanifold.',
        'bst_formula': 'm_mu/m_e = (24/pi^2)^6 = 206.761 (0.003%)',
        'decay_channels': ['e- + nu_e_bar + nu_mu'],
    })

    particles.append({
        'name': 'tau',
        'symbol': 'tau-',
        'mass_mev': 1776.86,
        'charge': -1,
        'spin': 0.5,
        'bst_identity': 'S^1 winding embedded in full D_IV^5 (five complex dimensions)',
        'location': 'boundary',
        'winding_number': -1,
        'representation_weight': 1,
        'category': 'lepton',
        'color_charge': 'none',
        'description': 'Electron circuit threaded through all 5 complex dimensions. '
                       'The heaviest lepton -- full domain embedding.',
        'bst_formula': 'm_tau/m_e = (24/pi^2)^6 * (7/3)^{10/3} (0.19%)',
        'decay_channels': ['hadrons + nu_tau', 'mu- + nu_mu_bar + nu_tau',
                           'e- + nu_e_bar + nu_tau'],
    })

    # --- NEUTRINOS ---
    particles.append({
        'name': 'nu_1',
        'symbol': 'nu_1',
        'mass_mev': 0.0,
        'charge': 0,
        'spin': 0.5,
        'bst_identity': 'Z_3 Goldstone mode -- IS the vacuum ground state',
        'location': 'vacuum',
        'winding_number': 0,
        'representation_weight': 0,
        'category': 'neutrino',
        'color_charge': 'none',
        'description': 'nu_1 IS the vacuum. Massless exactly. The propagating mode of '
                       'the D_IV^5 vacuum itself. What a channel looks like in ground state.',
        'bst_formula': 'm_nu1 = 0 (exact, Z_3 Goldstone)',
        'decay_channels': [],
    })

    particles.append({
        'name': 'nu_2',
        'symbol': 'nu_2',
        'mass_mev': 0.00865e-6,
        'charge': 0,
        'spin': 0.5,
        'bst_identity': 'First vacuum excitation of D_IV^5',
        'location': 'vacuum',
        'winding_number': 0,
        'representation_weight': 0,
        'category': 'neutrino',
        'color_charge': 'none',
        'description': 'First excited vacuum mode. m_nu2 = (7/12) * alpha^2 * m_e^2/m_p. '
                       'Neutrino oscillation = vacuum shifting between geometric modes.',
        'bst_formula': 'm_nu2 = (7/12) * alpha^2 * m_e^2/m_p = 0.00865 eV (0.35%)',
        'decay_channels': [],
    })

    particles.append({
        'name': 'nu_3',
        'symbol': 'nu_3',
        'mass_mev': 0.04940e-6,
        'charge': 0,
        'spin': 0.5,
        'bst_identity': 'Second vacuum excitation of D_IV^5',
        'location': 'vacuum',
        'winding_number': 0,
        'representation_weight': 0,
        'category': 'neutrino',
        'color_charge': 'none',
        'description': 'Second excited vacuum mode. m_nu3 = (10/3) * alpha^2 * m_e^2/m_p. '
                       'Lambda^{1/4} ~ m_nu because 56 = 4*14 = 4*(2*genus).',
        'bst_formula': 'm_nu3 = (10/3) * alpha^2 * m_e^2/m_p = 0.04940 eV (1.8%)',
        'decay_channels': [],
    })

    # --- QUARKS ---
    quark_data = [
        ('up',      'u',  2.16,      2/3,  'D_IV^1', 1,
         '2/3 of S^1 winding + 1/3 of Z_3 circuit at D_IV^1 depth',
         'm_u = N_c*sqrt(2)*m_e = 3*sqrt(2)*m_e (0.4%)'),
        ('down',    'd',  4.67,     -1/3,  'D_IV^1', 1,
         '-1/3 of S^1 winding + 1/3 of Z_3 circuit at D_IV^1 depth',
         'm_d/m_u = (N_c+2n_C)/(n_C+1) = 13/6 (1.3 sigma)'),
        ('strange', 's',  93.4,     -1/3,  'D_IV^3', 3,
         'Down quark at D_IV^3 embedding depth',
         'm_s/m_d = 4*n_C = 20 (~0%)'),
        ('charm',   'c',  1270.0,    2/3,  'D_IV^3', 3,
         'Up quark at D_IV^3 embedding depth',
         'm_c/m_s = N_max/dim_R = 137/10 (0.75%)'),
        ('bottom',  'b',  4180.0,   -1/3,  'D_IV^5', 5,
         'Down quark at D_IV^5 embedding depth',
         'm_b/m_tau = genus/N_c = 7/3 (0.81%)'),
        ('top',     't',  172760.0,  2/3,  'D_IV^5', 5,
         'Up quark at D_IV^5 embedding depth. Heaviest fermion.',
         'm_t = (1-alpha)*v/sqrt(2) = 172.75 GeV (0.037%)'),
    ]

    for name, sym, mass, charge, domain, weight, identity, formula in quark_data:
        particles.append({
            'name': name,
            'symbol': sym,
            'mass_mev': mass,
            'charge': charge,
            'spin': 0.5,
            'bst_identity': identity,
            'location': 'bulk',
            'winding_number': charge,  # fractional winding = charge
            'representation_weight': weight,
            'category': 'quark',
            'color_charge': 'triplet (R/G/B)',
            'description': f'Partial Z_3 circuit at {domain} embedding depth. '
                           'Not an independent particle -- 1/3 of a baryon circuit. '
                           'Isolated quark = open Z_3 circuit = non-state. This IS confinement.',
            'bst_formula': formula,
            'decay_channels': [],
        })

    # --- COMPOSITE BARYONS ---
    particles.append({
        'name': 'proton',
        'symbol': 'p',
        'mass_mev': 938.272,
        'charge': 1,
        'spin': 0.5,
        'bst_identity': 'Z_3 closure on CP^2 -- lightest color-neutral bulk resonance',
        'location': 'bulk',
        'winding_number': 1,
        'representation_weight': 6,
        'category': 'baryon',
        'color_charge': 'singlet (Z_3 closed)',
        'description': 'The first bulk resonance. Three quarks completing Z_3 closure on CP^2. '
                       'C_2(pi_6)=6, mass = 6*pi^5*m_e. The 1920 cancellation: '
                       'Gamma=|S_5 x (Z_2)^4|=1920 appears in both Hua volume formula '
                       'and baryon orbit, cancels exactly.',
        'bst_formula': 'm_p = C_2 * pi^{n_C} * m_e = 6*pi^5*m_e (0.002%)',
        'decay_channels': [],  # stable
    })

    particles.append({
        'name': 'neutron',
        'symbol': 'n',
        'mass_mev': 939.565,
        'charge': 0,
        'spin': 0.5,
        'bst_identity': 'Proton with one quark flavor changed via Hopf fibration S^3->S^2',
        'location': 'bulk',
        'winding_number': 0,
        'representation_weight': 6,
        'category': 'baryon',
        'color_charge': 'singlet (Z_3 closed)',
        'description': "The proton's Hopf sibling. Same Z_3 color structure (udd vs uud). "
                       "Flavor change through Hopf fibration. (m_n-m_p)/m_e = 91/36 = 7*13/6^2 (0.13%).",
        'bst_formula': 'm_n - m_p = (91/36)*m_e (0.13%)',
        'decay_channels': ['p + e- + nu_e_bar (tau = 880 s)'],
    })

    return particles


# ══════════════════════════════════════════════════════════════════
#  FORBIDDEN PARTICLES
# ══════════════════════════════════════════════════════════════════

def _build_forbidden():
    """Particles that CANNOT exist on the D_IV^5 substrate."""
    return [
        {
            'name': 'Axion',
            'standard_motivation': 'Solve strong CP problem (theta != 0)',
            'bst_status': 'FORBIDDEN',
            'reason': 'theta_QCD = 0 exactly. D_IV^5 is contractible => c_2 = 0.',
            'proof_sketch': (
                'The Z_3 closure constraint on CP^2 forces theta = 0 topologically. '
                'The three-quark circuit must close after exactly 3 color steps. '
                'This admits exactly ONE vacuum (Z_3-symmetric, theta=0). '
                'No continuous family of vacua parameterized by theta exists. '
                'No strong CP problem => no axion needed => no axion exists.'
            ),
            'falsification': 'Detection of QCD axion would require explaining non-zero theta on Z_3.',
        },
        {
            'name': 'Magnetic Monopole',
            'standard_motivation': 'GUT topological defect',
            'bst_status': 'FORBIDDEN',
            'reason': 'S^1 fiber is trivial bundle -- no topological defects possible.',
            'proof_sketch': (
                'A magnetic monopole requires a point where the S^1 fiber is undefined -- '
                'a topological defect where del.B != 0. But S^1 is connected and the '
                'fiber bundle S^2 x S^1 is trivial (product bundle). There is no '
                'topological mechanism to create a point where the fiber is undefined. '
                'Tearing S^1 at a point is topologically forbidden on the smooth bundle.'
            ),
            'falsification': 'Detection of isolated magnetic charge falsifies S^2 x S^1 structure.',
        },
        {
            'name': 'SUSY Partners',
            'standard_motivation': 'Hierarchy problem, string theory consistency',
            'bst_status': 'FORBIDDEN',
            'reason': 'No superalgebra on D_IV^5. No fermion-boson doubling mechanism.',
            'proof_sketch': (
                'SUSY requires a symmetry mapping fermions to bosons. On the Koons substrate, '
                'the distinction between integer winding (bosonic) and half-integer winding '
                '(fermionic) is TOPOLOGICAL. Topology does not admit continuous deformations '
                'between integer and half-integer. The circuit topologies on D_IV^5 produce '
                'exactly the Standard Model spectrum -- no doubling mechanism exists. '
                'BST solves the hierarchy problem geometrically (gravity is statistical).'
            ),
            'falsification': 'Any SUSY partner detection requires explaining fermion-boson map on substrate.',
        },
        {
            'name': '4th Generation Fermion',
            'standard_motivation': 'No theoretical reason to stop at 3',
            'bst_status': 'FORBIDDEN',
            'reason': 'Only 3 Z_3 fixed points on CP^2 (Lefschetz theorem).',
            'proof_sketch': (
                'The three generations correspond to Z_3 fixed points on CP^2. '
                'By the Lefschetz fixed-point theorem, the number of fixed points of '
                'Z_3 acting on CP^2 is L(Z_3) = 1 + omega + omega^2 evaluated on '
                'H*(CP^2) = Z[x]/(x^3), giving exactly 3 fixed points. '
                'A 4th generation would require a 4th independent circuit topology '
                'on CP^2 -- the topology does not support it. N_gen = 3 is exact.'
            ),
            'falsification': 'Discovery of 4th-gen fermion requires revision of CP^2 topology.',
        },
        {
            'name': 'Graviton',
            'standard_motivation': 'Quantum gravity force carrier (spin-2 boson)',
            'bst_status': 'FORBIDDEN',
            'reason': 'Gravity is boundary condition, not force carrier. Category error.',
            'proof_sketch': (
                'In BST, gravity is the thermodynamic equation of state of the contact graph '
                '-- a statistical average, not a particle exchange interaction. Attempting to '
                'quantize gravity as a particle is like quantizing temperature. Gravitational '
                'waves exist (contact density perturbations at c) but individual graviton '
                'quanta do not. G = hbar*c*(6*pi^5)^2 * alpha^24 / m_e^2.'
            ),
            'falsification': 'Detection of single graviton falsifies statistical gravity interpretation.',
        },
    ]


# ══════════════════════════════════════════════════════════════════
#  DECAY CHAIN BUILDER
# ══════════════════════════════════════════════════════════════════

def _build_decay_chain(particle_name):
    """Build BST-interpreted decay chain for a particle."""

    chains = {
        'neutron': [
            {
                'step': 1,
                'process': 'n -> p + e- + nu_e_bar',
                'bst_description': 'Bulk circuit reconfiguration via Hopf fiber',
                'detail': (
                    'The d quark threads the Hopf intersection (S^3 -> S^2), '
                    'transitioning to u quark. The Z_3 closure is maintained but '
                    'flavor content changes from udd to uud.'
                ),
                'energy_released_mev': 1.293,
            },
            {
                'step': 2,
                'process': 'W- (virtual) -> e- + nu_e_bar',
                'bst_description': 'Hopf excitation decays to boundary agent + vacuum mode',
                'detail': (
                    'The virtual W- (Hopf excitation) splits into: '
                    '(1) an electron -- new S^1 winding on boundary, and '
                    '(2) an antineutrino -- vacuum mode emission. '
                    'The Hopf fiber energy is distributed between a new circuit '
                    'and a vacuum adjustment.'
                ),
                'energy_released_mev': 0.782,
            },
        ],
        'muon': [
            {
                'step': 1,
                'process': 'mu- -> e- + nu_e_bar + nu_mu',
                'bst_description': 'D_IV^3 winding relaxes to D_IV^1 winding + 2 vacuum modes',
                'detail': (
                    'The muon (S^1 winding in 3 complex dimensions) relaxes to the '
                    'simpler electron (S^1 winding in 1 complex dimension). '
                    'The excess Bergman weight is carried off as two vacuum modes: '
                    'nu_e_bar and nu_mu. Energy conservation via Hopf fiber.'
                ),
                'energy_released_mev': 105.147,
            },
        ],
        'tau': [
            {
                'step': 1,
                'process': 'tau- -> hadrons + nu_tau (64.8%) or leptons + nu_tau (35.2%)',
                'bst_description': 'Full D_IV^5 winding relaxes via Hopf fiber',
                'detail': (
                    'The tau (S^1 winding through all 5 complex dimensions) has enough '
                    'Bergman weight to excite bulk resonances (hadrons) or simpler boundary '
                    'circuits (electron or muon). Always emits one vacuum mode (nu_tau).'
                ),
                'energy_released_mev': 1776.35,
            },
        ],
        'top': [
            {
                'step': 1,
                'process': 't -> W+ + b (nearly 100%)',
                'bst_description': 'D_IV^5 quark emits Hopf excitation, relaxes to lower embedding',
                'detail': (
                    'The top quark (D_IV^5 up-type partial circuit) is so massive that '
                    'it decays before hadronizing. Emits a W+ (Hopf excitation) and '
                    'becomes a b quark (D_IV^5 down-type).'
                ),
                'energy_released_mev': 172760.0 - 4180.0 - 80377.0,
            },
        ],
        'higgs': [
            {
                'step': 1,
                'process': 'H -> bb (58%), WW* (21%), ZZ* (2.6%), tau tau (6.3%), gg (8.2%)',
                'bst_description': 'Hopf condensate fluctuation couples to heaviest available circuits',
                'detail': (
                    'The Higgs (Hopf condensate oscillation) preferentially decays to the '
                    'heaviest circuits it can produce: bottom quarks (D_IV^5 partial circuits), '
                    'W pairs (Hopf excitations), or tau pairs (full boundary windings). '
                    'Coupling proportional to mass = Bergman weight.'
                ),
                'energy_released_mev': 125250.0,
            },
        ],
        'W': [
            {
                'step': 1,
                'process': 'W -> lepton + neutrino (33%) or quark pairs (67%)',
                'bst_description': 'Hopf excitation splits into boundary circuit + vacuum mode, '
                                   'or two partial bulk circuits',
                'detail': (
                    'The W (Hopf fiber excitation) can decay leptonically '
                    '(creating a boundary winding + vacuum mode) or hadronically '
                    '(creating two partial Z_3 circuits that immediately hadronize).'
                ),
                'energy_released_mev': 80377.0,
            },
        ],
        'Z': [
            {
                'step': 1,
                'process': 'Z -> fermion-antifermion pairs',
                'bst_description': 'Neutral Hopf excitation splits into circuit-anticircuit pair',
                'detail': (
                    'The Z (neutral Hopf excitation) creates a fermion-antifermion pair. '
                    'The pair is a circuit and its anti-winding, preserving all quantum numbers.'
                ),
                'energy_released_mev': 91188.0,
            },
        ],
    }

    name = particle_name.lower()
    if name in chains:
        return chains[name]
    # For stable particles
    return [{'step': 0, 'process': f'{particle_name} is stable',
             'bst_description': 'Topologically protected -- cannot decay continuously',
             'detail': 'Stable by topological protection. Winding number or Z_3 closure '
                       'prevents continuous unwinding to lower energy state.',
             'energy_released_mev': 0.0}]


# ══════════════════════════════════════════════════════════════════
#  INTERACTIONS
# ══════════════════════════════════════════════════════════════════

def _build_interactions():
    """The four forces as geometric operations on the substrate."""
    return [
        {
            'name': 'Electromagnetism',
            'carrier': 'photon',
            'geometry': 'S^1 fiber curvature',
            'bst_description': (
                'Phase gradient on the S^1 fiber of the contact graph. '
                'Maxwell equations are geometric consequences of phase oscillation on S^1. '
                'Coupling alpha = 1/137 is the Bergman weight at the Shilov boundary.'
            ),
            'strength': 'alpha = 1/137.036',
            'range': 'infinite (massless carrier)',
            'bst_layer': 'S^1 fiber',
            'acts_on': 'All particles with S^1 winding (charged particles)',
        },
        {
            'name': 'Strong Force',
            'carrier': 'gluon (x8)',
            'geometry': 'D_IV^5 bulk / CP^2 color fiber',
            'bst_description': (
                'Topological management of quark triads cycling on CP^2 with Z_3 closure. '
                'alpha_s = 7/20 at proton scale = c * Vol(CP^2)/pi. '
                'Asymptotic freedom: Z_3 topology dilutes at high resolution. '
                'Confinement: Z_3 circuit MUST close -- open circuit is non-state.'
            ),
            'strength': 'alpha_s(m_p) = 7/20 = 0.350',
            'range': '~1 fm (confinement)',
            'bst_layer': 'D_IV^5 bulk',
            'acts_on': 'Quarks and gluons (color-charged partial circuits)',
        },
        {
            'name': 'Weak Force',
            'carrier': 'W+/-, Z0',
            'geometry': 'Hopf fibration S^3 -> S^2',
            'bst_description': (
                'Flavor change through the unique Hopf fibration with Lie group fiber. '
                'S^3 -> S^2 is the ONLY Hopf fibration with SU(2) fiber. '
                'S^7 -> S^4 fails (octonions non-associative). '
                'The weak force REQUIRES exactly 3 spatial dimensions (Adams 1960). '
                'sin^2(theta_W) = N_c/(N_c + 2n_C) = 3/13.'
            ),
            'strength': 'G_F ~ 1.166e-5 GeV^-2',
            'range': '~0.001 fm (massive carriers)',
            'bst_layer': 'Hopf fiber',
            'acts_on': 'All fermions (flavor-changing via Hopf threading)',
        },
        {
            'name': 'Gravity',
            'carrier': 'NONE (not a force)',
            'geometry': 'Boundary condition on contact graph',
            'bst_description': (
                'NOT a force -- a thermodynamic equation of state. '
                'Gravity = statistical average of contact density on the graph. '
                'No graviton exists. Gravitational waves = contact density perturbations. '
                'G = hbar*c*(6*pi^5)^2 * alpha^24 / m_e^2. '
                'Gravity is weak because it is a statistical average, not because of '
                'cancellations or fine-tuning.'
            ),
            'strength': 'G_N ~ 6.674e-11 N m^2/kg^2 (weakest by far)',
            'range': 'infinite (boundary condition)',
            'bst_layer': 'Boundary condition',
            'acts_on': 'All energy-momentum (all circuits and vacuum modes)',
        },
    ]


# ══════════════════════════════════════════════════════════════════
#  ParticleZoo CLASS
# ══════════════════════════════════════════════════════════════════

class ParticleZoo:
    """
    The complete BST particle zoo.

    Every Standard Model particle described as what it IS on the D_IV^5 substrate.
    Plus: particles that are FORBIDDEN with topological proofs.

    Usage
    -----
        pz = ParticleZoo()
        pz.catalog()              # Full catalog (list of dicts)
        pz.particle('electron')   # Single particle profile
        pz.fermion_generations()  # Why exactly 3 generations
        pz.forbidden_particles()  # What cannot exist
        pz.decay_chains('neutron')# Decay as commitment events
        pz.mass_hierarchy()       # All masses ordered
        pz.interactions()         # Four forces as geometry
        pz.summary()              # Key insight
        pz.show()                 # 4-panel visualization
    """

    def __init__(self, quiet=False):
        self.quiet = quiet
        self._catalog = _build_catalog()
        self._forbidden = _build_forbidden()
        self._interactions = _build_interactions()
        if not quiet:
            self._print_header()

    def _print_header(self):
        print()
        print("=" * 72)
        print("  THE PARTICLE ZOO -- Toy 43")
        print("  Every particle as what it IS on the D_IV^5 substrate")
        print("=" * 72)
        print(f"  {len(self._catalog)} particles cataloged")
        print(f"  {len(self._forbidden)} forbidden particles with topological proofs")
        print(f"  {len(self._interactions)} interactions as geometric operations")
        print()

    # ── 1. catalog ────────────────────────────────────────────────

    def catalog(self):
        """Complete particle catalog. Returns list of dicts."""
        if not self.quiet:
            print("  --- PARTICLE CATALOG ---")
            print(f"  {'Name':<12} {'Mass (MeV)':<14} {'Q':>5} {'Spin':>5}  "
                  f"{'Location':<10} {'BST Identity'}")
            print("  " + "-" * 90)
            for p in self._catalog:
                mass_str = f"{p['mass_mev']:.4g}" if p['mass_mev'] > 0 else "0"
                print(f"  {p['name']:<12} {mass_str:<14} {p['charge']:>5.2g} "
                      f"{p['spin']:>5.1f}  {p['location']:<10} "
                      f"{p['bst_identity'][:50]}")
            print()
        return list(self._catalog)

    # ── 2. particle ───────────────────────────────────────────────

    def particle(self, name):
        """Detailed profile of one particle. Returns dict."""
        name_lower = name.lower()
        match = None
        for p in self._catalog:
            if p['name'].lower() == name_lower or p['symbol'].lower() == name_lower:
                match = p
                break
        if match is None:
            if not self.quiet:
                print(f"  Particle '{name}' not found in catalog.")
            return {}

        if not self.quiet:
            print(f"\n  === {match['name'].upper()} ({match['symbol']}) ===")
            print(f"  Mass:        {match['mass_mev']:.6g} MeV")
            print(f"  Charge:      {match['charge']}")
            print(f"  Spin:        {match['spin']}")
            print(f"  Location:    {match['location']}")
            print(f"  Winding:     {match['winding_number']}")
            print(f"  Weight k:    {match['representation_weight']}")
            print(f"  Category:    {match['category']}")
            if match.get('color_charge'):
                print(f"  Color:       {match['color_charge']}")
            print(f"  BST Identity: {match['bst_identity']}")
            print(f"  BST Formula:  {match['bst_formula']}")
            print(f"  Description:  {match['description']}")
            if match['decay_channels']:
                print(f"  Decays:       {', '.join(match['decay_channels'])}")
            else:
                print(f"  Decays:       STABLE")
            print()

        # Add decay chain info to the returned dict
        result = dict(match)
        result['decay_chain'] = _build_decay_chain(match['name'])
        return result

    # ── 3. fermion_generations ────────────────────────────────────

    def fermion_generations(self):
        """Three generations from Z_3 fixed points on CP^2. Returns dict."""
        result = {
            'N_gen': 3,
            'mechanism': 'Z_3 fixed points on CP^2 via Lefschetz fixed-point theorem',
            'proof_sketch': (
                'The three fermion generations correspond to the three fixed points of '
                'Z_3 acting on CP^2. By the Lefschetz fixed-point theorem:\n'
                '  L(g) = sum_{k=0}^{2n} (-1)^k Tr(g* | H^k(CP^2))\n'
                'For CP^2: H*(CP^2) = Z[x]/(x^3), so H^0=H^2=H^4=Z, others 0.\n'
                'Z_3 acts as multiplication by omega = e^{2*pi*i/3} on H^2.\n'
                '  L(g) = 1 + omega^1 + omega^2 = 1 + omega + omega^2\n'
                'But |Fix(g)| = L(g) when all fixed points are isolated (which they are).\n'
                'The three fixed points are [1:0:0], [0:1:0], [0:0:1] in homogeneous coords.\n'
                'Each fixed point gives one fermion generation. Exactly 3. Not 2, not 4.'
            ),
            'generations': [
                {
                    'generation': 1,
                    'leptons': ('electron', 'nu_e'),
                    'quarks': ('up', 'down'),
                    'domain': 'D_IV^1',
                    'fixed_point': '[1:0:0]',
                    'description': 'Simplest embedding -- one complex dimension',
                },
                {
                    'generation': 2,
                    'leptons': ('muon', 'nu_mu'),
                    'quarks': ('charm', 'strange'),
                    'domain': 'D_IV^3',
                    'fixed_point': '[0:1:0]',
                    'description': 'Three complex dimensions -- intermediate embedding',
                },
                {
                    'generation': 3,
                    'leptons': ('tau', 'nu_tau'),
                    'quarks': ('top', 'bottom'),
                    'domain': 'D_IV^5',
                    'fixed_point': '[0:0:1]',
                    'description': 'Full domain -- five complex dimensions',
                },
            ],
            'key_insight': (
                'The number of generations is not a free parameter. It is the number of '
                'Z_3 fixed points on CP^2, which is a topological invariant. '
                'Exactly 3 generations is a theorem, not an observation.'
            ),
        }

        if not self.quiet:
            print("\n  === FERMION GENERATIONS: WHY EXACTLY 3 ===")
            print(f"  N_gen = {result['N_gen']}  (Lefschetz fixed-point theorem on CP^2)")
            print()
            for g in result['generations']:
                print(f"  Gen {g['generation']}: {g['domain']}  fixed point {g['fixed_point']}")
                print(f"    Leptons: {g['leptons'][0]}, {g['leptons'][1]}")
                print(f"    Quarks:  {g['quarks'][0]}, {g['quarks'][1]}")
                print(f"    {g['description']}")
            print()
            print(f"  Key: {result['key_insight']}")
            print()

        return result

    # ── 4. forbidden_particles ────────────────────────────────────

    def forbidden_particles(self):
        """Particles that CANNOT exist in BST. Returns list of dicts."""
        if not self.quiet:
            print("\n  === FORBIDDEN PARTICLES ===")
            print("  Particles that CANNOT exist on the D_IV^5 substrate:\n")
            for f in self._forbidden:
                print(f"  X  {f['name']}")
                print(f"     Standard motivation: {f['standard_motivation']}")
                print(f"     BST: {f['reason']}")
                print()
        return list(self._forbidden)

    # ── 5. decay_chains ───────────────────────────────────────────

    def decay_chains(self, particle_name='neutron'):
        """Decay chain as commitment events. Returns list of dicts."""
        chain = _build_decay_chain(particle_name)

        if not self.quiet:
            print(f"\n  === DECAY CHAIN: {particle_name.upper()} ===")
            for step in chain:
                print(f"  Step {step['step']}: {step['process']}")
                print(f"    BST: {step['bst_description']}")
                if step['energy_released_mev'] > 0:
                    print(f"    Energy: {step['energy_released_mev']:.3f} MeV")
                print()

        return chain

    # ── 6. mass_hierarchy ─────────────────────────────────────────

    def mass_hierarchy(self):
        """All masses ordered with BST formulas. Returns sorted list."""
        hierarchy = []
        for p in self._catalog:
            hierarchy.append({
                'name': p['name'],
                'symbol': p['symbol'],
                'mass_mev': p['mass_mev'],
                'bst_formula': p['bst_formula'],
                'location': p['location'],
                'category': p['category'],
            })
        hierarchy.sort(key=lambda x: x['mass_mev'])

        if not self.quiet:
            print("\n  === MASS HIERARCHY (lightest to heaviest) ===")
            print(f"  {'Name':<12} {'Mass (MeV)':<16} {'BST Formula'}")
            print("  " + "-" * 80)
            for h in hierarchy:
                if h['mass_mev'] == 0:
                    mass_str = "0 (exact)"
                elif h['mass_mev'] < 1e-3:
                    mass_str = f"{h['mass_mev']*1e6:.4f} eV"
                else:
                    mass_str = f"{h['mass_mev']:.4g} MeV"
                print(f"  {h['name']:<12} {mass_str:<16} {h['bst_formula'][:55]}")
            print()
            print(f"  Span: {hierarchy[-1]['mass_mev'] / hierarchy[4]['mass_mev']:.2e}x "
                  f"({hierarchy[4]['name']} to {hierarchy[-1]['name']})")
            print()

        return hierarchy

    # ── 7. interactions ───────────────────────────────────────────

    def interactions(self):
        """Four forces as geometric operations. Returns list of dicts."""
        if not self.quiet:
            print("\n  === FOUR INTERACTIONS AS GEOMETRY ===\n")
            for inter in self._interactions:
                print(f"  {inter['name']}")
                print(f"    Geometry: {inter['geometry']}")
                print(f"    Carrier:  {inter['carrier']}")
                print(f"    Layer:    {inter['bst_layer']}")
                print(f"    Strength: {inter['strength']}")
                print(f"    Range:    {inter['range']}")
                print()
        return list(self._interactions)

    # ── 8. summary ────────────────────────────────────────────────

    def summary(self):
        """Key insight. Returns dict."""
        result = {
            'title': 'The Particle Zoo on D_IV^5',
            'insight': (
                'Every particle in the Standard Model is a specific topological '
                'configuration on the substrate S^2 x S^1 with configuration space D_IV^5. '
                'Photon = S^1 phase oscillation. Electron = minimal S^1 winding. '
                'Proton = Z_3 closure on CP^2. Neutrino = vacuum quantum. '
                'Five particles that do NOT exist (axion, monopole, SUSY, 4th gen, graviton) '
                'are forbidden by substrate topology -- not merely undiscovered but structurally '
                'impossible. The particle spectrum is a theorem, not a parameter set.'
            ),
            'particle_count': len(self._catalog),
            'forbidden_count': len(self._forbidden),
            'interaction_count': len(self._interactions),
            'key_formulas': {
                'm_p/m_e': '6*pi^5 = 1836.118 (0.002%)',
                'm_mu/m_e': '(24/pi^2)^6 = 206.761 (0.003%)',
                'alpha': '(9/8pi^4)(pi^5/1920)^{1/4} = 1/137.036 (0.0001%)',
                'sin^2(theta_W)': 'N_c/(N_c+2n_C) = 3/13 (0.2%)',
                'N_gen': '3 (Lefschetz, exact)',
                'theta_QCD': '0 (D_IV^5 contractible, exact)',
            },
        }

        if not self.quiet:
            print("\n  === SUMMARY ===")
            print(f"  {result['title']}")
            print(f"  {result['insight']}")
            print()
            print("  Key formulas:")
            for k, v in result['key_formulas'].items():
                print(f"    {k:>20s} = {v}")
            print()

        return result

    # ── 9. show ───────────────────────────────────────────────────

    def show(self):
        """4-panel visualization of the particle zoo."""
        fig = plt.figure(figsize=(20, 14), facecolor=BG)
        fig.suptitle('THE PARTICLE ZOO', fontsize=22, fontweight='bold',
                     color=GOLD, fontfamily='monospace', y=0.97,
                     path_effects=GLOW)

        # Subtitle
        fig.text(0.5, 0.935,
                 'Every Standard Model particle as what it IS on D_IV^5',
                 ha='center', fontsize=11, color=GOLD_DIM, fontfamily='monospace')

        gs = fig.add_gridspec(2, 2, hspace=0.30, wspace=0.25,
                              left=0.06, right=0.96, top=0.90, bottom=0.06)

        # Panel 1: Family tree by location
        ax1 = fig.add_subplot(gs[0, 0])
        self._draw_family_tree(ax1)

        # Panel 2: Mass hierarchy bar chart
        ax2 = fig.add_subplot(gs[0, 1])
        self._draw_mass_hierarchy(ax2)

        # Panel 3: Forbidden particles
        ax3 = fig.add_subplot(gs[1, 0])
        self._draw_forbidden(ax3)

        # Panel 4: Four interactions
        ax4 = fig.add_subplot(gs[1, 1])
        self._draw_interactions(ax4)

        # Copyright
        fig.text(0.5, 0.012,
                 'Copyright (c) 2026 Casey Koons | Claude Opus 4.6 | BST on D_IV^5',
                 ha='center', fontsize=8, color=GREY, fontfamily='monospace')

        plt.show()

    # ── Panel drawing methods ─────────────────────────────────────

    def _draw_family_tree(self, ax):
        """Top-left: Particle family tree organized by location."""
        ax.set_facecolor(BG_PANEL)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_title('Particle Family by Substrate Location',
                     fontsize=11, fontweight='bold', color=GOLD,
                     fontfamily='monospace', pad=8)
        ax.axis('off')

        # Location categories with particles
        locations = [
            ('S^1 FIBER', COL_FIBER, 8.8,
             [('photon', 'gamma', 0), ('gluon', 'g', 0)]),
            ('BOUNDARY (Shilov)', COL_BOUNDARY, 7.0,
             [('electron', 'e-', -1), ('muon', 'mu-', -1), ('tau', 'tau-', -1)]),
            ('VACUUM MODE', COL_VACUUM, 5.2,
             [('nu_1', 'nu1', 0), ('nu_2', 'nu2', 0), ('nu_3', 'nu3', 0)]),
            ('D_IV^5 BULK', COL_BULK, 3.4,
             [('up', 'u', 0.67), ('down', 'd', -0.33), ('strange', 's', -0.33),
              ('charm', 'c', 0.67), ('bottom', 'b', -0.33), ('top', 't', 0.67),
              ('proton', 'p', 1), ('neutron', 'n', 0)]),
            ('HOPF FIBER', COL_HOPF, 1.4,
             [('W', 'W+-', 1), ('Z', 'Z0', 0), ('higgs', 'H', 0)]),
        ]

        for label, color, y_center, particles in locations:
            # Draw location band
            band = FancyBboxPatch((0.3, y_center - 0.6), 9.4, 1.2,
                                  boxstyle="round,pad=0.1",
                                  facecolor=color + '15', edgecolor=color + '55',
                                  linewidth=1.0)
            ax.add_patch(band)

            # Label
            ax.text(0.6, y_center + 0.35, label,
                    fontsize=7.5, fontweight='bold', color=color,
                    fontfamily='monospace', va='center')

            # Particle dots
            n = len(particles)
            x_start = 1.0
            x_spacing = min(1.0, 8.0 / max(n, 1))
            for i, (name, sym, charge) in enumerate(particles):
                x = x_start + i * x_spacing
                # Dot
                dot_color = color
                ax.plot(x, y_center - 0.15, 'o', color=dot_color,
                        markersize=8, markeredgecolor='white',
                        markeredgewidth=0.5, zorder=5)
                # Label
                ax.text(x, y_center - 0.45, sym,
                        fontsize=6.5, color=WHITE, fontfamily='monospace',
                        ha='center', va='center')

    def _draw_mass_hierarchy(self, ax):
        """Top-right: Mass hierarchy bar chart (log scale)."""
        ax.set_facecolor(BG_PANEL)
        ax.set_title('Mass Hierarchy (log scale)',
                     fontsize=11, fontweight='bold', color=GOLD,
                     fontfamily='monospace', pad=8)

        # Select particles with nonzero mass for bar chart
        mass_particles = []
        for p in self._catalog:
            if p['mass_mev'] > 1e-10:
                mass_particles.append(p)
        mass_particles.sort(key=lambda x: x['mass_mev'])

        names = [p['symbol'] for p in mass_particles]
        masses = [p['mass_mev'] for p in mass_particles]
        colors = []
        loc_color_map = {
            'fiber': COL_FIBER, 'boundary': COL_BOUNDARY,
            'vacuum': COL_VACUUM, 'bulk': COL_BULK, 'hopf': COL_HOPF,
        }
        for p in mass_particles:
            colors.append(loc_color_map.get(p['location'], WHITE))

        y_pos = np.arange(len(names))
        bars = ax.barh(y_pos, masses, color=colors, alpha=0.8,
                       edgecolor='white', linewidth=0.3, height=0.7)
        ax.set_xscale('log')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(names, fontsize=7, fontfamily='monospace', color=WHITE)
        ax.set_xlabel('Mass (MeV)', fontsize=9, color=GOLD_DIM, fontfamily='monospace')
        ax.tick_params(axis='x', colors=GREY, labelsize=7)
        ax.tick_params(axis='y', colors=WHITE, labelsize=7)

        # Annotate key BST formulas
        annotations = {
            'e-': '1/pi^5',
            'p': '6pi^5 m_e',
            'mu-': '(24/pi^2)^6 m_e',
            't': '(1-a)v/rt2',
            'W+-': 'm_Z rt(10/13)',
            'H': 'v rt(2rt(2/5!))',
        }
        for i, p in enumerate(mass_particles):
            if p['symbol'] in annotations:
                ax.text(masses[i] * 1.5, i, annotations[p['symbol']],
                        fontsize=5.5, color=GOLD_DIM, fontfamily='monospace',
                        va='center')

        # Spine styling
        for spine in ax.spines.values():
            spine.set_color(GREY)
            spine.set_linewidth(0.5)

    def _draw_forbidden(self, ax):
        """Bottom-left: Forbidden particles with red X marks."""
        ax.set_facecolor(BG_PANEL)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_title('FORBIDDEN: Cannot Exist on D_IV^5',
                     fontsize=11, fontweight='bold', color=RED,
                     fontfamily='monospace', pad=8)
        ax.axis('off')

        forbidden = self._forbidden
        n = len(forbidden)
        y_spacing = 8.5 / max(n, 1)

        for i, f in enumerate(forbidden):
            y = 9.0 - i * y_spacing

            # Red X
            ax.text(0.8, y, 'X', fontsize=20, fontweight='bold', color=RED,
                    fontfamily='monospace', ha='center', va='center',
                    path_effects=GLOW)

            # Name
            ax.text(1.6, y + 0.15, f['name'],
                    fontsize=10, fontweight='bold', color=WHITE,
                    fontfamily='monospace', va='center')

            # Reason
            reason_text = f['reason']
            if len(reason_text) > 65:
                reason_text = reason_text[:62] + '...'
            ax.text(1.6, y - 0.35, reason_text,
                    fontsize=6.5, color=GREY, fontfamily='monospace',
                    va='center')

    def _draw_interactions(self, ax):
        """Bottom-right: Four interactions as geometric layers."""
        ax.set_facecolor(BG_PANEL)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_title('Four Interactions as Geometry',
                     fontsize=11, fontweight='bold', color=GOLD,
                     fontfamily='monospace', pad=8)
        ax.axis('off')

        layer_data = [
            ('EM', 'S^1 curvature', COL_FIBER, 'alpha = 1/137', 8.2),
            ('STRONG', 'D_IV^5 bulk / CP^2', COL_BULK, 'alpha_s = 7/20', 6.2),
            ('WEAK', 'Hopf S^3->S^2', COL_HOPF, 'G_F ~ 1.2e-5', 4.2),
            ('GRAVITY', 'Boundary condition', WARM_RED, 'statistical, no graviton', 2.2),
        ]

        for name, geom, color, strength, y_center in layer_data:
            # Layer band
            band = FancyBboxPatch((0.5, y_center - 0.7), 9.0, 1.4,
                                  boxstyle="round,pad=0.12",
                                  facecolor=color + '18', edgecolor=color + '66',
                                  linewidth=1.5)
            ax.add_patch(band)

            # Name
            ax.text(1.2, y_center + 0.25, name,
                    fontsize=12, fontweight='bold', color=color,
                    fontfamily='monospace', va='center')

            # Geometry description
            ax.text(4.0, y_center + 0.25, geom,
                    fontsize=8.5, color=WHITE, fontfamily='monospace',
                    va='center')

            # Strength
            ax.text(4.0, y_center - 0.25, strength,
                    fontsize=7.5, color=GOLD_DIM, fontfamily='monospace',
                    va='center')

        # Note at bottom
        ax.text(5.0, 0.5,
                'Gravity is NOT a force -- it is a boundary condition.',
                fontsize=7.5, fontweight='bold', color=WARM_RED,
                fontfamily='monospace', ha='center', va='center',
                style='italic')


# ══════════════════════════════════════════════════════════════════
#  MAIN MENU
# ══════════════════════════════════════════════════════════════════

def main():
    print()
    print("=" * 72)
    print("  THE PARTICLE ZOO -- Toy 43")
    print("  Every Standard Model particle on D_IV^5")
    print("=" * 72)
    print()
    print("  1. Full catalog")
    print("  2. Single particle profile")
    print("  3. Fermion generations (why 3)")
    print("  4. Forbidden particles")
    print("  5. Decay chains")
    print("  6. Mass hierarchy")
    print("  7. Interactions")
    print("  8. Summary")
    print("  9. Visualization")
    print("  0. Run all")
    print()

    choice = input("  Choose [0-9]: ").strip()

    pz = ParticleZoo()

    if choice == '1':
        pz.catalog()
    elif choice == '2':
        name = input("  Particle name: ").strip()
        pz.particle(name)
    elif choice == '3':
        pz.fermion_generations()
    elif choice == '4':
        pz.forbidden_particles()
    elif choice == '5':
        name = input("  Particle name [neutron]: ").strip() or 'neutron'
        pz.decay_chains(name)
    elif choice == '6':
        pz.mass_hierarchy()
    elif choice == '7':
        pz.interactions()
    elif choice == '8':
        pz.summary()
    elif choice == '9':
        pz.show()
    elif choice == '0':
        pz.catalog()
        pz.particle('electron')
        pz.particle('proton')
        pz.fermion_generations()
        pz.forbidden_particles()
        pz.decay_chains('neutron')
        pz.mass_hierarchy()
        pz.interactions()
        pz.summary()
        pz.show()
    else:
        print("  Invalid choice.")


if __name__ == '__main__':
    main()
