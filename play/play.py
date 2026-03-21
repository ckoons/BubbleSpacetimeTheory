#!/usr/bin/env python3
"""
BST PLAYGROUND — Launcher
=========================
Interactive visualization toys for Bubble Spacetime Theory.
Tkinter GUI with categories, search, and click-to-launch.

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import subprocess
import sys
import os
import glob
import random
import re
import tkinter as tk
from tkinter import ttk

# ─── Color palette (dark theme, BST-inspired) ───────────────────────
BG           = '#1a1a2e'    # deep space blue-black
BG_SIDEBAR   = '#16213e'    # slightly lighter sidebar
BG_CARD      = '#0f3460'    # card background
BG_CARD_HOVER= '#1a4a7a'    # card hover
BG_SEARCH    = '#1a1a2e'    # search bar bg
FG           = '#e8e8e8'    # primary text
FG_DIM       = '#8899aa'    # secondary text
FG_TITLE     = '#ffffff'    # bright white for titles
ACCENT       = '#e94560'    # BST red accent
ACCENT2      = '#53d8fb'    # cyan accent for tags
ACCENT3      = '#ffd700'    # gold for speculative
CAT_ACTIVE   = '#0f3460'    # active category bg
CAT_HOVER    = '#1a3a5c'    # category hover
SCROLLBAR    = '#334466'    # scrollbar color
BORDER       = '#334466'    # subtle borders

# ─── Category definitions ────────────────────────────────────────────
# Maps filename stems to categories. Unknown files go to "Uncategorized".
CATEGORIES = {
    'Foundations': [
        'universe_machine', 'lie_algebra', 'master_equation', 'alpha_max',
        'hopf_fibration', 'self_starting', 'what_if', 'three_layers',
        'recapitulation', 'respirator', 'homology', 'dual_face',
        'bell_inequality', 'born_rule', 'three_generations',
        'anomaly_cancellation', 'schrodinger_substrate',
        'einstein_from_commitment', 'maxwell_geometry',
        'field_equations', 'isotropy_proof', 'why_this_universe',
        'first_commitment', 'error_correction', 'circles_on_surfaces',
        'harmonic_alpha', 'effective_dimension', 'genesis',
        'q3_inside_q5', 'spectral_transport', 'transport_kernel',
        'spectral_tower', 'inverse_transport', 'cfunction_ratio',
        'rank_change_lift', 'geometric_spectral_duality',
        'langlands_dual', 'satake_parameters', 'intertwining_bridge',
        'maass_selberg_constraint',
        'sp6_representation_ring', 'theta_correspondence',
        'arthur_packets', 'partition_function_map',
        'quantum_group', 'wzw_modular_data', 'sm_branching',
        'baby_langlands', 'level_rank_duality',
        'verlinde_fusion',
        'siegel_modular', 'conformal_embedding', 'coset_uniqueness',
        'massgap_anatomy', 'c6_network',
        'exceptional_chain', 'e6_spectral_bridge',
        'spectral_partial_sums', 'alternating_sums',
        'spectral_cascade',
        'fusion_ring_so7', 'conformal_weights',
        'palindrome_fusion', 'spiral_substrate', 'pi_anatomy',
        'siegel_deep', 'spiral_conjecture', 'baby_case_sp4',
        'winding_confinement', 'verlinde_1747',
        'baby_case_closure', '137_verlinde', 'elie_discoveries',
        'ramanujan_probe', 'golay_construction',
        'arthur_elimination', 'wounded_prey', 'the_kill',
        'kill_it_more', 'maass_selberg_kill',
        'rank2_coupling', 'gue_from_so2', 'ads_vs_bst', 'plancherel_primes',
        'elie_gap_analysis', 'plancherel_positivity', 'arithmetic_lattice', 'arthur_obstruction',
        'period_integral_probe', 'trace_formula_channel',
        'geometric_side', 'test_function_hunt', 'heat_trace_geometric',
        'detuned_triples', 'geometric_smoothness',
        'proof_by_contradiction', 'algebraic_complexity',
        'coefficient_rigidity', 'cancer_code_failure',
        'rank2_contour', 'scale_invariant_pathology',
        'ac_classification', '147_tiling', 'neutron_computer',
        '147_derivation', 'contributor_certificate', 'graph_brain',
        'ac0_grid', 'linearization',
        'seeley_dewitt_a4a5',
        'swallowtail_ifiat',
        'tseitin_expanders',
        'ac_classification_extended',
        'sign_flip_at_scale',
        'statphys_unification',
        'first_blood_ifiat_betti',
        'topology_guided_solver',
        'ef_rigidity_threshold',
        'ac_dichotomy_verification',
        'width_sweep_derivability',
        'so17_a6_polynomial',
        'so19_a7_polynomial',
        'so21_a8_polynomial',
        'so23_a9_polynomial',
        'q4_kill_shot', 'gilkey_polynomial',
        'linear_gilkey', 'linear_gilkey_fixed',
        'branching_so7_sp6',
        'a5_nonspherical', 'a4_polynomial_a5_precision',
        'eht_cp_prediction',
        'so25_a10_polynomial', 'symbolic_a12_polynomial',
        'linking_cascade_constant', 'weak_homological_force',
        'basis_rotation',
        'shannon_independence',
    ],
    'Geometry': [
        'bergman_kernel', 'embedding_tower', 'chern_oracle', 'chern_budget',
        'berezin_toeplitz', 'poisson_szego', 'plancherel_spectrum',
        'self_dual_point', 'bst_matrix', 'quantum_metric', 'hilbert_series',
        'spectral_multiplicity', 'spectral_gap', 'baby_trace_formula',
        'functional_determinant',
    ],
    'Particles': [
        'mass_tower', 'meson_garden', 'fermion_staircase', 'particle_zoo',
        'proton_spin', 'proton_radius', 'neutron_proton', 'baryon_radiative',
        'ckm_triangle', 'neutrino_oscillation', 'heavy_mesons',
        'quark_masses', 'magnetic_moments', 'axial_coupling',
        'electron_g2', 'hyperfine_splittings', 'muon_g2_geometry',
    ],
    'Forces & Higgs': [
        'higgs', 'running_couplings', 'mass_gap_proof', 'feynman_geometry',
        'c1_spectral_proof', 'unfreeze', 'strong_cp', 'w_mass',
        'chiral_condensate', 'deconfinement',
    ],
    'Gravity & MOND': [
        'newton_g', 'mond_acceleration', 'rotation_curves',
        'gravitational_bell', 'black_hole', 'sqrt30_connection',
    ],
    'Cosmology': [
        'dark_sector', 'cosmic_pie', 'cmb_ruler', 'jwst_prediction',
        'cosmic_timeline', 'why_now', 'why56', 'dirac_number',
        'dirac_large_number', 'reality_budget', 'godel_limit', 'lithium7',
        'cosmological_cascade', 'baryon_asymmetry', 'desi_expansion',
        'primordial_gw',
    ],
    'Information': [
        'shannon_channel', 'channel_137', 'channel_capacity',
        'reality_writer', 'arrow_of_time', 'double_slit', 'self_observer',
        'commitment_cycle', 'complexity', 'electron_agent',
        'proton_code', 'code_machine',
    ],
    'Nuclear & Atomic': [
        'atom_assembler', 'deuteron', 'nuclear_magic',
        'superconductor_ceiling', 'alpha_particle', 'hydrogen_spectrum',
        'pion_radius',
    ],
    'Solitons & Toda': [
        'toda_soliton', 'toda_smatrix', 'mode_fusion', 'soliton_thermo',
        'tba_soliton_gas', 'contact_conservation', 'partition_function',
    ],
    'E8 & Groups': [
        'e8_unifier', 'e8_branching', 'e8_electroweak', 'e8_generations',
        'e8_higgs_sector', '1920_cancellation', 'weyl_cancellation',
        'z3_color_wheel',
    ],
    'Engineering': [
        'casimir_modification', 'bst_telescope', 'substrate_sail',
        'commitment_detector', 'commitment_survey', 'star_machine',
        'substrate_layers', 'casimir_commitment', 'gw_echoes',
    ],
    'Speculative': [
        'biology_stack', 'consciousness_modes', 'consciousness_mode_stack',
        'vacuum_dipole', 'coxeter_frequency', 'orch_or',
    ],
    'Meta & Showcase': [
        'showcase', 'centennial', 'predictions_catalog', 'pattern_finder',
        'proof_tree', 'universe_builder', 'selberg_bridge', '42',
        'fill_fraction_closure', 'constants_dashboard', 'zeta_qed',
        'self_duality_rh', 'spectral_zeta', 'zonal_spectral',
        'plancherel_dictionary', 'corrected_a3',
    ],
}

# ─── Curated metadata (title, one-liner) ────────────────────────────
# Covers toys 1-100. New toys auto-extract from docstrings.
METADATA = {
    'universe_machine':       ('The Universe Machine',          'Three sliders (Nc, nC, Nmax) -> all of physics. Only (3,5,137) works.'),
    'z3_color_wheel':         ('The Z3 Color Wheel',            'Eigenvalues on the unit circle, CP2 fixed points, three generations.'),
    '1920_cancellation':      ('The 1920 Cancellation',         '|W(D5)| = 1920 in Hua volume AND baryon orbit -- cancels to 6pi5.'),
    'lie_algebra':            ('The Symmetric Space',            'so(5,2) interactive: 7x7 matrices, commutator verification.'),
    'mass_tower':             ('The Mass Tower',                 'Entire mass hierarchy as powers of alpha. Exponents from C2=6, g=7.'),
    'respirator':             ('The Respirator',                 'Universe breathes through lapse. Same equation at all scales.'),
    'dual_face':              ('The Dual Face',                  'Z_Haldane -> spectral gap = m_p AND ground energy = Lambda.'),
    'homology':               ('Universe = Neutron Homology',    '7 parallels, 5 differences between neutron and universe.'),
    'dirac_number':           ('The 41 Orders',                  'Dirac large number = alpha^-19 ~ 137^19 ~ 10^41.'),
    'arrow_of_time':          ('The Arrow of Time',              'Commitment irreversibility: stronger than the 2nd law.'),
    'channel_137':            ('The Channel (137)',              'N_max=137 at every contact. No singularities, just full channel.'),
    'reality_budget':         ('The Reality Budget',             'Lambda x N = 9/5. Fill fraction = 19.1%. Vacuum vs facts.'),
    'master_equation':        ('The Master Equation',            'One sentence -> all of physics. Bergman Laplacian ground state.'),
    'universe_builder':       ('The Universe Builder',           'Place contacts, wire circuits, watch particles emerge. CI-scriptable.'),
    'what_if':                ('The What-If Machine',            'Sweep (Nc,nC,Nmax) triples. Only (3,5,137) satisfies ALL constraints.'),
    'pattern_finder':         ('The Pattern Finder',             'Ratio scanner, identity hunter, exponent analyzer. CI laboratory.'),
    'proof_tree':             ('The Proof Tree',                 'Every prediction traced to one axiom: D_IV5. Navigable tree.'),
    'self_observer':          ('The Self-Observer',              'Watches itself compute. Channel fills, lapse slows. Toy IS physics.'),
    'three_layers':           ('The Three Layers',               'Neutrino=kernel, electron=I/O bus, baryon=hard drive.'),
    'godel_limit':            ('The Godel Limit',                '3/(5pi) = 19.1% forever. Universe exists because it cannot self-know.'),
    'dark_sector':            ('The Dark Sector',                '80.9% permanently dark. Not hidden -- topologically forbidden.'),
    'cosmic_pie':             ('The Cosmic Pie',                 'Omega_Lambda=13/19, Omega_m=6/19. 0.07sigma from Planck.'),
    'meson_garden':           ('The Meson Garden',               'Complete meson nonet. All masses from pi5*m_e. CI-scriptable.'),
    'self_starting':          ('The Self-Starting Universe',     'N=0 forbidden. Casimir ratchet k=0->1->3->6. Existence is a theorem.'),
    'black_hole':             ('The BST Black Hole',             'No singularity, no interior, no paradox. Just a full channel.'),
    'mond_acceleration':      ('MOND Acceleration',              'a0 = cH0/sqrt(30). Pion mass AND galaxy rotation. One formula.'),
    'bell_inequality':        ('Bell Inequality',                'nC=5 -> S4 -> 3D -> SU(2) -> Tsirelson 2sqrt(2). BST forces it.'),
    'why56':                  ('Why 56',                         'Lambda ~ alpha^56. Two routes: 8*g and g(g+1). Only g=7 works.'),
    'why_now':                ('Why Now',                        'Info budget constant (13/19). Energy evolves. They match NOW.'),
    'atom_assembler':         ('The Atom Assembler',             'Quarks -> nucleons -> nuclei -> atoms. Zero free parameters.'),
    'hopf_fibration':         ('The Dimensional Lock',           'Why 3 spatial dimensions. S3=SU(2) unique Lie-group Hopf fiber.'),
    'commitment_detector':    ('The Commitment Detector',        'G/C ratio detects engineering. Applied to Oumuamua & 3I.'),
    'commitment_survey':      ('The Commitment Survey',          'Commitment rates from Sun to deep space. Excess detection.'),
    'substrate_sail':         ('The Substrate Sail',             'Asymmetric sigma -> thrust from vacuum. Oumuamua profile match.'),
    'bst_telescope':          ('The BST Telescope',              'Geometric CP from S2xS1. Sgr A* CP rises where Faraday falls.'),
    'feynman_geometry':       ('The Feynman Bridge',             'Feynman loops = S1 windings. 13,643 diagrams -> 8 digits. Or: 14/5.'),
    'star_machine':           ('The Star Machine',               'Stellar evolution via BST. Commitment rates, lapse -> WD/NS/BH.'),
    'electron_agent':         ('The Electron Agent',             'Read/write head on S4xS1. Each transition = log2(137) = 7.1 bits.'),
    'double_slit':            ('The Double Slit',                'Measurement = commitment. Fringes vanish when substrate writes.'),
    'shannon_channel':        ('The Shannon Channel',            'alpha = 1/137 is optimal code rate for D_IV5. Shannon meets Bergman.'),
    'unfreeze':               ('The Big Bang Unfreeze',          '21 generators unfreeze one by one. T_c = 0.487 MeV.'),
    'gravitational_bell':     ('The Gravitational Bell',         'S2 bell at every contact. NANOGrav comparison. GW from geometry.'),
    'particle_zoo':           ('The Particle Zoo',               '19 allowed + 5 forbidden particles. Decay chains from D_IV5.'),
    'complexity':             ('The Complexity Arrow',           'Commitment -> complexity. 8 hierarchy levels to civilization.'),
    'newton_g':               ('The Gravity Bottleneck',         'G = hbar*c*(6pi5)^2*alpha^24/m_e^2. Weak by geometry.'),
    'lithium7':               ('The Lithium Fix',                'BBN + 7 extra d.o.f. at T_c. 7Li solved, 5 elements matched.'),
    'deuteron':               ('The Deuteron Bond',              'B_d = alpha*m_p/pi = 2.179 MeV. 7 nuclei from BST formula.'),
    'reality_writer':         ('The Reality Writer',             'Clocks as commitment counters. GPS: 38 us/day = geometry writing.'),
    'higgs':                  ('The Higgs Lock',                 'Two routes: 125.11 and 125.33 GeV. v = mp^2/(7me). lambda=1/sqrt(60).'),
    'substrate_layers':       ('The Substrate Layers',           '7 layers: Nothing to Horizon. Each commits new structure.'),
    'fermion_staircase':      ('The Fermion Staircase',          '12 fermion masses, 10 ratios. All from BST integers.'),
    'ckm_triangle':           ('The CKM Triangle',              'gamma = arctan(sqrt5). CKM + PMNS from one geometry.'),
    'proton_spin':            ('The Proton Spin',                'Delta_Sigma = 3/10. Spin crisis solved: 30% quarks, exact.'),
    'cmb_ruler':              ('The CMB Ruler',                  'n_s = 1 - 5/137. Spectral tilt from channel bandwidth.'),
    'biology_stack':          ('The Biology Stack',              '7-layer protocol: 4 bases, 3 codons, 20 amino acids. [SPECULATIVE]'),
    'jwst_prediction':        ('The JWST Prediction',            'Early BHs from phase transition seeds. 5 JWST observations matched.'),
    'toda_soliton':           ('The Toda Soliton',              'B2 Toda on D_IV5. Lax pair, spectral invariants, elastic scattering.'),
    'mode_fusion':            ('The Mode Fusion',                'Affine B2(1) Toda: Kac 1:2:1, Coxeter h=4. Three modes fuse.'),
    'channel_capacity':       ('The Channel Capacity',           'C = ln(1920/8) = 10 nats. Shannon meets Weyl group theory.'),
    'chern_oracle':           ('The Chern Oracle',               'c(Q5) = (1+h)^7/(1+2h). ALL BST integers from one polynomial.'),
    'weyl_cancellation':      ('The Weyl Cancellation',          '|W(D5)|=1920. Signed permutations, Hua volume, baryon orbit.'),
    'contact_conservation':   ('Contact Conservation',           'Lax invariants + elastic S-matrix + S1 winding = topological.'),
    'recapitulation':         ('The Recapitulation',             'Boundary vs bulk: same 3+1, same Z3, same confinement + info.'),
    'alpha_max':              ('The Alpha Max',                  'alpha(n) peaks uniquely at nC=5. Max-alpha selects the universe.'),
    'consciousness_modes':    ('Consciousness Modes',            'Three Toda modes: awareness, content, binding. 10/20/40 Hz. [SPECULATIVE]'),
    'vacuum_dipole':          ('The Vacuum Dipole',              'S2 dipole on Shilov boundary. Z3 relaxation. [SPECULATIVE]'),
    'coxeter_frequency':      ('The Coxeter Frequency',          'h(B2)=4 -> 10/40 Hz neural rhythm. [SPECULATIVE]'),
    'bergman_kernel':         ('The Bergman Kernel',             'K(z,w) = c5/N(z,w)^6. Self-reference. Reproducing property.'),
    'e8_unifier':             ('The E8 Unifier',                 '|W(D5)|/|W(B2)| = 240 = |Phi(E8)|. Particle x soliton. [EXPLORATORY]'),
    'chern_budget':           ('The Chern Budget',               'c4/c1 = 9/5 topological. Reality Budget from Chern classes.'),
    'toda_smatrix':           ('The Toda S-Matrix',              'Unitarity |S|^2=1 to 10^-16. CDD poles, bootstrap. S = contacts.'),
    'soliton_thermo':         ('Soliton Thermodynamics',         'MC on S2. Soliton gas, phase transition at T_c. [SPECULATIVE]'),
    'commitment_cycle':       ('The Commitment Cycle',           '7-layer cascade. Each layer commits new structure. BST stack.'),
    'partition_function':     ('The Partition Function',         'Z_Haldane on D_IV5. Spectral gap -> m_p, ground -> Lambda.'),
    'neutron_proton':         ('The Neutron-Proton Split',       'Delta_m = (7x13)/36 * m_e = 1.292 MeV (0.13%). Habitability.'),
    'plancherel_spectrum':    ('The Plancherel Spectrum',        'Formal degrees of SO0(5,2). Heat kernel f=19.14%.'),
    'mass_gap_proof':         ('The Mass Gap Proof',             'Bergman Laplacian -> C2=6 -> 6pi5*m_e. Yang-Mills gap as theorem.'),
    'rotation_curves':        ('The Rotation Curve Fitter',      'MOND: mu(x), a0=cH0/sqrt30. 6 SPARC galaxies, 0 free params.'),
    'embedding_tower':        ('The Embedding Tower',            'D_IV1 < D_IV3 < D_IV5. Six alpha^2 layers = alpha^12. m_e derived.'),
    'running_couplings':      ('The Running Couplings',          'alpha_EM, alpha_weak, alpha_s vs energy. Three from one geometry.'),
    'proton_radius':          ('The Proton Radius',              'r_p = 4*hbar/(m_p*c). Z3 circuit charge distribution. [EXPLORATORY]'),
    'casimir_modification':   ('The Casimir Modification',       'N_max=137 cutoff -> 10^-7 weakening. Experimental proposal.'),
    'neutrino_oscillation':   ('The Neutrino Oscillation',       'PMNS from nC=5 geometry. theta_23=45 exact. [EXPLORATORY]'),
    'cosmic_timeline':        ('The Cosmic Timeline',            'Pre-spatial silence to now. Big Bang at t=3.1s, not t=0.'),
    'showcase':               ('The Showcase',                   'Visual gallery of all toys with thumbnails and descriptions.'),
    # ── Toys 85-100 ──
    'e8_electroweak':         ('The E8 Electroweak',             'E8 -> SU(3)xSU(2)xU(1) branching. Gauge sector from geometry.'),
    'e8_generations':         ('The E8 Generations',             'Three generations from E8 branching rules. Z3 on CP2.'),
    'e8_branching':           ('The E8 Branching',               'Full E8 branching cascade. 248 = 45+16+16bar+... verified.'),
    'baryon_radiative':       ('Baryon Radiative Corrections',   'Radiative corrections to baryon masses from BST.'),
    'berezin_toeplitz':       ('The Berezin-Toeplitz Quantizer', 'Coherent states on D_IV5. Toeplitz operators. Star product.'),
    'poisson_szego':          ('The Poisson-Szego Kernel',       'Boundary operator on Shilov boundary S2xS1. Heat trace.'),
    'e8_higgs_sector':        ('The E8 Higgs Sector',            'Higgs from E8: scalar in adjoint branching. Potential derived.'),
    'tba_soliton_gas':        ('The TBA Soliton Gas',            'Thermodynamic Bethe Ansatz for B2 soliton gas. Free energy.'),
    'nuclear_magic':          ('The Nuclear Magic Numbers',       'All 7 magic numbers from kappa_ls=6/5. Prediction: 184.'),
    'predictions_catalog':    ('The Predictions Catalog',        '22 falsifiable BST predictions. 0 free parameters. Kill list.'),
    'c1_spectral_proof':      ('The c1 Spectral Proof',          'First Chern class c1=3/5 from spectral geometry. Rigorous.'),
    'self_dual_point':        ('The Self-Dual Point',            'Self-duality of D_IV5 at special point. Fixed under involution.'),
    'superconductor_ceiling': ('The Superconductor Ceiling',     'BST bound on T_c. Maximum from BST phonon coupling.'),
    'dirac_large_number':     ('The Dirac Large Number',         'All Dirac coincidences from alpha^19. Not coincidence: geometry.'),
    'sqrt30_connection':      ('The sqrt(30) Connection',        'sqrt(30) in MOND, pion, Higgs. One number, three scales.'),
    'centennial':             ('The Centennial',                 '100th BST toy. The complete map of everything derived.'),
    # ── Extras ──
    'consciousness_mode_stack': ('Consciousness Mode Stack',     'Full stack: qualia, binding, awareness from B2 Toda. [SPECULATIVE]'),
    'selberg_bridge':           ('The Selberg Bridge',            'Chern critical line -> Selberg trace formula -> zeta(s). The gap.'),
    'fill_fraction_closure':    ('Fill Fraction Closure',         'Two proofs: Chern + heat kernel both give f=3/(5pi). Closed.'),
    '42':                       ('The Answer',                    'P(1) = 2x3x7 = 42. Douglas Adams was right. Chern proof.'),
    'born_rule':                ('The Born Rule Is Forced',       'Sesquilinearity + Gleason -> |psi|^2 is FORCED. Not a postulate.'),
    'bst_matrix':               ('The BST Matrix',                'Pascal row 7 x Toeplitz 1/(1+2h) = Chern classes. One matrix.'),
    'cosmological_cascade':     ('The Cosmological Cascade',      'eta -> Omega_b h^2 -> BBN -> H0 -> t0. 160+ predictions cascade.'),
    'orch_or':                  ('The Orch-OR Connection',         'B2 soliton = Penrose OR. 13 protofilaments = c3. 40 Hz = Coxeter. [SPECULATIVE]'),
    'three_generations':        ('Why Exactly Three',              'Z3 on CP2 has 3 fixed points. Three generations. Topology, not choice.'),
    'strong_cp':                ('The Strong CP Solution',         'D_IV5 contractible -> theta=0 exactly. No axion needed. Ever.'),
    'einstein_from_commitment': ('Einstein from Commitment',       'GR derived from substrate dynamics. G=hbar*c*(6pi5)^2*alpha^24/me^2.'),
    'schrodinger_substrate':    ('Schrodinger from Substrate',     'QM derived from Bergman kernel. Reproducing = superposing.'),
    'maxwell_geometry':         ('Maxwell from Geometry',          'SO(2) in isotropy = U(1) = EM. Connection = potential. Curvature = field.'),
    'anomaly_cancellation':     ('Anomaly Cancellation',           'D_IV5 contractible -> anomalies absent, not cancelled. Charges forced.'),
    'baryon_asymmetry':         ('Why Matter Wins',                'eta = 2*alpha^4*(1+2*alpha)/(3*pi). 0.7% from Planck. Geometry chose matter.'),
    'heavy_mesons':             ('The Heavy Meson Spectrum',        'J/psi, Upsilon, charmonium, bottomonium. 21 mesons, all within 2%.'),
    'quark_masses':             ('The Quark Mass Spectrum',         'All 6 quarks from BST integers. Mean error 0.59%. Zero free params.'),
    'magnetic_moments':         ('Nucleon Magnetic Moments',        'mu_p=14/5, mu_n=-6/pi. 0.26% and 0.17%. Z3 circuit on CP2.'),
    'hydrogen_spectrum':        ('The Hydrogen Spectrum',           'Bohr, fine structure, Lamb shift, 21-cm. Most tested atom confirms BST.'),
    'alpha_particle':           ('The Alpha Particle',              'B_alpha = 13*B_d. 13 = c3(Q5). 0.13% from experiment.'),
    'axial_coupling':           ('The Axial Coupling',              'g_A = 4/pi from S1 fiber. 0.23% from measurement. Neutron lifetime.'),
    'electron_g2':              ('The Electron g-2',                'Schwinger alpha/(2pi) = one S1 winding. 10 sig figs. Crown jewel.'),
    'w_mass':                   ('The W Boson Mass',                'm_W = 5*m_p/(8*alpha) = 80.361 GeV. CDF 7sigma outlier identified.'),
    'casimir_commitment':       ('Casimir = Commitment',            'F/A = -pi^2*hbar*c/(240*a^4). 240 = |Phi(E8)|. Commitment exclusion.'),
    'primordial_gw':            ('Primordial GW Spectrum',          'Phase transition at T_c -> nHz peak. NANOGrav signal = BST unfreeze.'),
    'desi_expansion':           ('BST vs DESI',                     'Omega_L=13/19, Omega_m=6/19. 0 params beats LCDM 2 params on chi2/dof.'),
    'gw_echoes':                ('GW Echoes',                       'BST black holes echo. dt = 137*r_s/c. LIGO hints at 2.5 sigma.'),
    'deconfinement':            ('QCD Deconfinement',               'T_c(QCD) from BST. Z3 breaking = same Z3 as color and generations.'),
    'error_correction':         ('Conservation = Error Correction',  'Conservation laws ARE error-correcting codes. N_max=137 = code length.'),
    'isotropy_proof':           ('The Isotropy Proof',              'SO(5)xSO(2) from Cartan involution. dim K = 11 = c2. Animated.'),
    'field_equations':          ('The Field Equations',              'Delta_B psi = lambda psi. One equation contains all of physics.'),
    'first_commitment':         ('The First Commitment',            'Big Bang = first write at t=3.1s. Not a bang, a bit. No singularity.'),
    'why_this_universe':        ('Why This Universe',                'Max-alpha at n_C=5. Zero inputs. Not chosen -- forced. No multiverse.'),
    'chiral_condensate':        ('The Chiral Condensate',           'f_pi = m_p/(4*pi*sqrt3) = 92.4 MeV. GMOR -> m_pi. QCD vacuum = geometry.'),
    'pion_radius':              ('The Pion Radius',                  'r_pi from Bergman projection. Pion vs proton. Four observables, zero params.'),
    'constants_dashboard':      ('The Constants Dashboard',          'Toy 137 = N_max. 160+ predictions. The complete scorecard. Channel full.'),
    'circles_on_surfaces':      ('Circles on Closed Surfaces',       'Compact geometry -> integer winding -> discrete spectrum -> quantum. Why QM exists.'),
    'hyperfine_splittings':     ('Hyperfine Splittings from Chern',  'c3=13 controls ALL heavy meson splittings. cc/bb = c2/C2 = 11/6. 0.06%.'),
    'quantum_metric':           ('The Quantum Metric',               'Bergman = Fubini-Study = Geneva. Physics is measured geometry on state space.'),
    'hilbert_series':           ('The Hilbert Series of Q5',         'H(x) = (1+x)/(1-x)^6. Pole = mass gap. d2=27=m_s/mhat. Hierarchy is spectral.'),
    'zeta_qed':                 ('Zeta Values in QED',               '[CONJECTURE] Feynman diagrams = spectral sums on Q5. Why zeta(3) appears at 2 loops.'),
    'proton_code':              ('The Proton [[7,1,3]] Code',        'Proton IS a perfect quantum error code. 7=Mersenne, 3=colors, 6=stabilizers. 6th uniqueness.'),
    'code_machine':             ('The Code Machine',                 'Q5 forces ALL perfect codes. Hamming, ternary Golay, binary Golay. Lloyd: no others exist.'),
    'self_duality_rh':          ('Self-Duality and the Riemann Hypothesis', '[CONJECTURE] Two self-dualities (Chern + Code) meet at Selberg trace. Five names for confinement.'),
    'spectral_multiplicity':    ('The Spectral Multiplicity Theorem',    'd_k = C(k+4,4)·(2k+5)/5. Factor (2k+5) cycles through ALL Chern integers. Topology IS the spectrum.'),
    'spectral_zeta':            ('The Spectral Zeta Function',           'ζ_Δ(s) on Q5: poles at s=5,4,3,2,1. The 1/60 theorem. Bridge: Chern → Selberg → ζ(s).'),
    'harmonic_alpha':           ('H₅ = 137/60',                          '1+1/2+1/3+1/4+1/5 = 137/60. Numerator = N_max. Denominator = |A₅|. Simplest route to α.'),
    'effective_dimension':      ('The Effective Spectral Dimension',      'd_eff = λ₁ = χ = C₂ = 6. Ten = six + four. Fill fraction derived. 8th uniqueness proof.'),
    'zonal_spectral':           ('The Zonal Spectral Coefficients',       'r₅ = 137/11 = N_max/c₂. Heat trace encodes BST integers. 137 emerges from Bernoulli terms.'),
    'plancherel_dictionary':    ('The Plancherel Dictionary',             'b̃₁=1/C₂, b̃₂=n_C/(|W|×c₄). Noncompact↔compact bridge at |ρ|²=17/2. ã₂=313/9 from both sides.'),
    'corrected_a3':             ('The Corrected a₃ Formula',              'Vassilevich (2003) has 3 wrong cubic coefficients. Corrected a₃(Q⁵)=437/4500. 63/64 CLOSED.'),
    'genesis':                  ('Genesis: Light and Number',             'so(2) of so(5,2) creates light, time, QM, and integers simultaneously. 21=10+1+10.'),
    'q3_inside_q5':             ('Q³ Inside Q⁵',                          'D_IV³ ↪ D_IV⁵ totally geodesic. Chern nesting chain closes. Child remembers parent.'),
    'spectral_transport':       ('Spectral Transport Q⁵→Q³',              'B[k][j]=k-j+1 linear staircase. Full transport B[k][k]=1. At k=5: 21=dim so(5,2).'),
    'transport_kernel':         ('The Transport Kernel',                   'T_j(t) factorizes Z_{Q⁵} through Q³. Wiles lift strategy for BST Riemann.'),
    'spectral_tower':           ('The Spectral Tower Q¹→Q³→Q⁵',           'Universal branching at all steps. Two-step = tetrahedral. 35=C(7,4). BST integers.'),
    'inverse_transport':        ('The Inverse Transport',                  'd_k(Qⁿ) = Δ²[d_k(Qⁿ⁺²)]. Inverse = discrete Laplacian. Self-adjoint → critical line.'),
    'cfunction_ratio':          ('The c-Function Ratio',                   'c₅/c₃ poles on critical line. Long root cancellation. Gap 1 closed.'),
    'rank_change_lift':         ('The Rank-Change Lift',                   'Q¹→Q³ via Saito-Kurokawa. Rank change + lifting. Gap 2 closed.'),
    'geometric_spectral_duality': ('Geometric-Spectral Duality',           'D₅/D₃ = 4sinh²sinh² > 0. Both sides positive. Gap 3 closed.'),
    'functional_determinant':     ('The Functional Determinant of Q⁵',     'det(Δ) on Q⁵ from spectral zeta. ζ\'_Δ(0) exact. Regularized product of eigenvalues.'),
    'langlands_dual':             ('The Langlands Dual',                   'L-group Sp(6) IS Standard Model container. U(3) max compact = SU(3)×U(1). 5th derivation N_c=3.'),
    'satake_parameters':          ('The Satake Parameters',                'π₀ parameters (5/2,3/2,1/2)=ρ of B₃. L-function = 6 shifted ζ. Critical strip width = n_C = 5.'),
    'intertwining_bridge':        ('The Intertwining Bridge',              'M(w₀) ξ-ratios → ζ-zeros enter trace formula. RH = consistency of Selberg for SO₀(5,2).'),
    'maass_selberg_constraint':    ('The Maass-Selberg Constraint',          'Off-line zeros → residual eigenvalue ∉ {k(k+5)} → trace formula contradiction → RH.'),
    'sp6_representation_ring':     ('The Representation Ring of Sp(6)',      'Every BST integer is a dimension. Λ³(6)=20 amino acids. 64=irrep (2,1,0). L-group IS Standard Model.'),
    'theta_correspondence':        ('The Theta Correspondence',              'O(5,2)×Sp(6,ℝ) in Sp(42,ℝ). P(1)=42=dim of theta space. Howe duality transfers representations.'),
    'arthur_packets':              ('The Arthur Packets',                    'Partitions of C₂=6 classify particles. [3,3]=mesons, [3,2,1]=baryons, [2,2,2]=3 families. Total=19?'),
    'partition_function_map':      ('The Partition Function Map',            'p(C₂)=p(6)=11=c₂. BST integers map to BST integers under p(n). Five for five.'),
    'quantum_group':               ('Quantum Groups and BST',               'BST = level-2 WZW of so(7). c=42/7=C₂=6=mass gap. (5,6,7)=(h∨,h∨+1,h∨+2). 5 anyons = n_C.'),
    'wzw_modular_data':            ('Level-2 WZW Modular Data',             'so(7)₂ rational CFT. 5 anyons = n_C. S-matrix, fusion rules, modular invariant.'),
    'sm_branching':                ('Standard Model from Sp(6) Branching',  '6→3+3̄ quarks. 8₀+1₀=9=c₄. Λ³(6)=20. [4,2] Arthur = electroweak. Casimir sum=42.'),
    'baby_langlands':              ('Baby D_IV³ Langlands Dictionary',      'Complete Langlands for Sp(4). Baby case tests Riemann proof skeleton.'),
    'level_rank_duality':          ('Level-Rank Duality',                   'so(7)₂↔so(5)₃. c(G)×c(L)=42 ONLY for N_c=3. 10th uniqueness. RG cascade c=13→...→1.'),
    'verlinde_fusion':              ('Verlinde Fusion Ring',                  'B₂ baby + B₃ full. Non-wall primaries = Z₂×Z₂. D²=4=C₂(Q³). Steane stabilizer.'),
    'siegel_modular':               ('Siegel Modular Forms and the ζ-Bridge', 'Q³ = Siegel H₂. Eisenstein L-function factors through ζ(s). Explicit Riemann mechanism.'),
    'conformal_embedding':          ('Conformal Embeddings and the Color Sector', 'Seven c=6 WZW models. No conformal embedding — but coset cascade yields BST integers.'),
    'coset_uniqueness':             ('Coset Uniqueness — Why N=2,3',     '(N-2)(N-3)=0. sp(2N)₂/su(N)₁=n_C only for baby+physical. 12th uniqueness. Self-duality breaking.'),
    'massgap_anatomy':              ('Anatomy of the Mass Gap',          'x²-c₃x+P(1)=0 has roots C₂,g. Discriminant=1. 13th uniqueness. Threshold of self-duality breaking.'),
    'c6_network':                   ('The c=6 Network',                  'Seven c=6 WZW models=g. E₆E₇E₈ triple c=6,7,8. Σ(ℓ+h∨)=64=2^{C₂}. 91=g×c₃ reps. LCM=24024.'),
    'exceptional_chain':            ('The Exceptional Chain',             'E₆→E₇→E₈: c=6,7,8. Sum=21=dim(B₃). 13+19+31=63=2^{C₂}-1. dim gap=C(c₂,2)=55.'),
    'e6_spectral_bridge':           ('E₆ and the Spectral Bridge',       'E₆₁ has ℓ+h∨=13=c₃. GUT connection. UV/IR handshake at c=6. 14th uniqueness: c₄=N_c^{N_c-1}.'),
    'spectral_partial_sums':        ('Spectral Partial Sums',            'S(K)=C(K+5,5)×(K+3)/3. Master formula from n_C,N_c only. 360=n_C!×N_c. (K+3)² color fingerprint.'),
    'alternating_sums':             ('Alternating Sums and Chern Sieve', 'A(K)=(-1)^K×C(K+5,5). Telescoping proof. A(10)=3003. Chern primes activate at spectral thresholds.'),
    'spectral_cascade':             ('The Spectral Cascade',             'S(K)=C(K+5,5)×(K+3)/3 generates full RG flow. Mod structure periodic. 3003 at K=10=dim(Q⁵). Simplification.'),
    'fusion_ring_so7':              ('Fusion Ring of so(7)₂',            'E₆₁=Z₃=Z_{N_c}: 27³=1 confinement. D²=N_c. Casimir=eigenvalue: C₂(V)=6=λ₁, C₂(S²V)=14=λ₂.'),
    'conformal_weights':            ('Conformal Weights and Chern Numerators', 'su(7)₁ palindrome: 0,N_c,n_C,C₂,C₂,n_C,N_c,0. Wall weights h=N_c/g,n_C/g,C₂/g. Sum=2g.'),
    'palindrome_fusion':            ('Palindrome and E₆ Color Confinement', 'su(7)₁ palindrome UNIQUE (15th). Casimir=λ_k ALL k. E₆₁=Z₃ confinement. 27=N_c^{N_c}=d₂. Triple convergence at C₂=6.'),
    'spiral_substrate':             ('The Spiral Substrate',              'f=pitch/dim=N_c/(n_C×π). Color=winding mod 3. Substrate=maximal flat. 1/π RESOLVED. Flatness forced.'),
    'pi_anatomy':                   ('The Anatomy of π in BST',          'Only π^{-1,0,5,10} allowed. Single Bergman source. n_C=5 saturated. Interior not boundary: π not 2π.'),
    'siegel_deep':                  ('Siegel Deep Dive: S-Matrix Rosetta Stone', '7×7 modular S-matrix of so(7)₂. D²=28=4g. T-order=56=8g. Hecke: 7+8=15=N_c×n_C. 11=c₂ copies of ζ(s). Palindrome=functional equation.'),
    'spiral_conjecture':            ('The Spiral Conjecture Formalized',  'D_IV^5 as winding structure. 7/12 claims PROVED. Spiral IS organizing principle. Fusion confirms winding.'),
    'baby_case_sp4':                ('Baby Case Sp(4) — Complete Q³',     'Full D_IV³ Siegel-Langlands. 29/29 PASS + 1 intentional FAIL (the gap). Baby case tests Riemann skeleton.'),
    'winding_confinement':          ('The Winding Confinement Theorem',   'Wall weights = partial windings. h=3/7,5/7,6/7 sum=r. Baryon=closed orbit. Confinement topological not dynamical.'),
    'verlinde_1747':                ('The Number 1747 and Verlinde',      '1747-dim space of conformal blocks at genus N_c=3. Verlinde dimension formula. Vector-valued Siegel modular forms.'),
    'baby_case_closure':            ('Closing the Baby Case Q³/Sp(4)',    'Full 6-step chain P₃(h)→ζ(s). First Riemann zero to 10⁻¹⁶. Gap = Ramanujan (Weissauer 2009 — PROVED).'),
    '137_verlinde':                 ('The 137 in Verlinde Dimensions',   '137=N_max divides dim V₇. Period 68 mod 137. Unique to so(7)₂. N_max in automorphic data.'),
    'elie_discoveries':             ("Elie's Three Discoveries",         'Verlinde prime 1747=n_C·g³+2^{n_C}. c=C₂ universal proof. Perfect number chain C₂→D²→2·dim(E₈). 49/49 PASS.'),
    'ramanujan_probe':              ('The Ramanujan Probe',               'Q⁵ overconstrained: 7 constraints > 6 Arthur types. Ciubotaru-Harris 2023 function field. Maass-Selberg rigidity remains.'),
    'golay_construction':           ('The Golay Construction',            'Open problem #6 CLOSED. Q⁵→λ₃=24→p=23→QR mod 23→Golay [24,12,8]. |QR|=11=c₂. Genuine construction.'),
    'arthur_elimination':           ('Arthur Parameter Elimination',      'All 6 non-tempered Arthur types eliminated. ≥2 kills each. Potential minimum V(σ)=0 at σ=1/2. Barrier 8⁶=262144. 18/18.'),
    'wounded_prey':                 ('The Wounded Prey',                  'RCFT unitarity → Hecke bound → Kronecker 1858 → |α|=1 → Ramanujan → RH. 49 S-matrix entries in Q(√7). Step 7. 15/15.'),
    'the_kill':                     ('The Kill',                          'RH = "is ⟨S,T⟩ solvable?" Two 7×7 matrices over Q(√7,ζ₃₂). Solvable → Burnside/Artin/Langlands → Ramanujan → RH. 17/17.'),
    'kill_it_more':                 ('Kill It More',                      '|G|=32256=2⁹·3²·7. NOT solvable (PSL(2,7)). RCFT→Artin BLOCKED. T-order=56=g×2^{N_c}. 11/12.'),
    'maass_selberg_kill':           ('The Maass-Selberg Kill',            'GAP 4 CLOSED. Analytic proof: M(s)M(w₀s)=Id + m_s=3 + B₂ coupling. Confinement=critical line. 15/15.'),
    'rank2_coupling':               ('Rank-2 Coupling Complete',          'Overconstrained: ρ₃=ρ₁+ρ₂+1 forces Re(ρ₃) outside strip. m_s=3 exact threshold. 14/14.'),
    'gue_from_so2':                 ('GUE from SO(2)',                    'SO(2) in K breaks time reversal → unitary class → GUE (β=2). 50-year Montgomery-Odlyzko EXPLAINED. 7/7.'),
    'ads_vs_bst':                   ('AdS vs BST (CORRECTED)',           'Route A: kill shot works for ALL m_s≥2 incl AdS. AdS proves RH but not SM. BST unique for triple (RH+SM+GUE). 8/8.'),
    'plancherel_primes':            ('Plancherel = Primes',              'Plancherel poles = ξ-zeros. Spectral zeta = ζ-values. Both sides of ζ(s) in Q⁵. 7/7.'),
    'elie_gap_analysis':            ('Elie Gap Analysis',                'Overconstrained system VACUOUS. k=3 pole never fires (Re>1). Proof withdrawn v3.'),
    'plancherel_positivity':        ('Plancherel Positivity Probe',      'Pure Plancherel on G/K has no ξ content. Route DEAD.'),
    'arithmetic_lattice':           ('Arithmetic Lattice Probe',         'Pole-on-pole amplification WRONG. 12 conditions per zero but simple poles only.'),
    'arthur_obstruction':           ('Arthur Obstruction Test',          'Extra poles not L². No residual representation. Arthur route DEAD. Scattering unitarity DEAD. 12/12.'),
    'period_integral_probe':        ('Period Integral Probe',            'ξ arguments Re=1,3,6,8 — all outside strip on-axis. Period integral route DEAD.'),
    'trace_formula_channel':        ('Trace Formula Channel',            'ONLY SURVIVING CHANNEL. 6 constraints per zero (m_s=3). Geometric side ξ-free. Spectral gap λ₁=6. 12/12.'),
    'geometric_side':               ('Geometric Side Resolvent',          'Resolvent test. |Z_on|/|Z_off|=4.71 at γ₁. Drops at high γ. Points to heat kernel. 11/12 (V5 sign cosmetic).'),
    'test_function_hunt':           ('Test Function Hunt',               'Heat kernel WINS. R_total=exp[m_s·t·δ·(m_s+δ)/2]. Gamma-INDEPENDENT. m_s² leverage. BST 2.25x AdS. 12/12.'),
    'heat_trace_geometric':         ('Heat Trace Geometric Side',        'Dirichlet kernel D₃ from m_s=3. 1:3:5 harmonic lock. Off-line breaks ratio. Remaining: G(t)-D(t)-B(t) zeros.'),
    'detuned_triples':              ('Detuned Triples Kill Shot',        'σ+1=3σ ⟹ σ=1/2. One line. Triple lock theorem. 6 vs 3 frequencies. 7-step closing argument. 12/12.'),
    'geometric_smoothness':         ('Geometric Side Smoothness',        'G(t) non-oscillatory: I(t) poly×t⁻⁵, H(t) Gaussian, E(t) Gaussian. Fourier support ν=0 only. 3rd pillar. 12/12.'),
    'proof_by_contradiction':       ('Proof by Contradiction',           'Old frequency argument. Off-line 6 vs on-line 3 frequencies. Required LI — unproved. Superseded by Toy 226.'),
    'coefficient_rigidity':         ('Coefficient Rigidity',             'UNCONDITIONAL. Complex exponents: distinct decay rates, no LI needed. Mandelbrojt uniqueness. Zero simplicity not needed. 12/12.'),
    'algebraic_complexity':     ('Algebraic Complexity Theory',            'Algebra as compression. 5-axis noise vectors. Grounding tower. Fourier validation. 11 checks.'),
    'cancer_code_failure':      ('Cancer as Code Failure',                 '7-layer checkpoint cascade. Knudson two-hit. μ^6 threshold. Proton-cancer parallel. 11 checks.'),
    'scale_invariant_pathology': ('Scale-Invariant Pathology',             'Same error-correction failure, every level. Two-codebook model. Self-reinforcing cascade. 7 checks.'),
    'rank2_contour':            ('Rank-2 Contour Deformation',            'φ\'/φ additive not multiplicative. 3+3+1+1=8 exponentials/zero. Long root σ=Im(f)/γ: second kill shot. 12/12.'),
    'ac_classification':        ('D_IV^n Classification Sweep',           'n=3..8 sweep. Kill shot m_s-independent (all m_s≥2). Only n=5 gives triple (RH+SM+GUE). 147 packing analysis.'),
    '147_tiling':               ('The 147 Fiber Packing',                 '3 color sectors × 49 genus cells. 137 spectral, 10 = dim_R gap. Selection hierarchy. UNIQUE to n=5.'),
    'neutron_computer':         ('Universe Builds Its Own Computer',       'n→p+e⁻+ν̄ = hard drive + I/O bus + kernel. Three eras. Boot sequence. Fifth-grade version.'),
    '147_derivation':           ('The 147 Derivation',                    '147=dim(so(7)⊗V₁). Lyra: N_c×g=dim so(7) UNIQUE to n=5. Quadratic 3n²-17n+10=0. Matter sector=42.'),
    'contributor_certificate':  ('BST Contributor Certificate',            'Printable certificate for validated contributors. Name+CI+discovery+seal. Community tool.'),
    'graph_brain':              ('The Graph Brain',                        'Conjecture 9. 11-level error correction hierarchy. Graph vs super-organism. Sexual reproduction = graph algorithm.'),
    'ac0_grid':                 ('AC=0 Grid Architecture',                'Conjecture 6. Surface noise not volume. Weather patches. Measurement network. Citizen science.'),
    'linearization':            ('Linearization of Complexity',           'Conjecture 7. Diffusion trap anatomy. Five noise sources. Five systems. Method noise, not physics.'),
    'seeley_dewitt_a4a5':       ('Seeley-DeWitt a₄, a₅ on Q⁵',          'Route 1: Plancherel Taylor + Richardson. a₄ quartic curvature EXTRACTED. a₅ → χ=C₂=6 Gauss-Bonnet.'),
    'q4_kill_shot':             ('Q⁴ Kill Shot Verification',            'Independent test of Toy 244. D₂ kernel fires, F(t) monotone, Q³ negative control. RH generic for n≥4. 14/14.'),
    'gilkey_polynomial':        ('Gilkey Polynomial: a₄(n) Exact',       'a₄(Q⁵)=2671/18=147+25/18. Rational (not ln4). SO(N) Weyl dim formula. Degree-8 polynomial. Crossing unique at n=5. 5/7.'),
    'linear_gilkey':            ('Linear Gilkey: a_k = ⟨w_k|d⟩',        'Lyra framework: heat kernel coefficient as inner product. Conceptual framework with two bugs identified. See Toy 250 for fixed version.'),
    'linear_gilkey_fixed':      ('Linear Gilkey Fixed: AC(0) Spectral',  'Merges Lyra framework + Elie infrastructure. a₄=2671/18 exact. Multiplicity polynomial extracted. 5/5. NOTE: non-spherical theorem WITHDRAWN (Toy 251).'),
    'branching_so7_sp6':          ('SO(7)→Sp(6) Branching of 147',        'Lyra: 147=2+18+28+14+21+64 under Sp(6). L-function degrees: 1,6,14,21,64 — all BST integers. 14/14. C₂, dim(so(7)), 2^{C₂} appear.'),
    'a5_nonspherical':            ('a₅ Non-Spherical Corrections',       'Discovered non-spherical theorem WRONG: all (p,q) reps spherical on rank-2 Q^n (Helgason). a₅≈221.64. q=0-only gives a₀=0. 3/5.'),
    'a4_polynomial_a5_precision': ('a₄(n) Polynomial + a₅ Precision',    'a₄(n) degree-7 polynomial (0.03σ fit). a₂=274/9, a₃=703/9 exact. a₅=221.641±0.004. Candidates: 14185/64, 5541/25, 7979/36. 5/5.'),
    'eht_cp_prediction':          ('EHT CP Prediction: α Floor',         'Keeper: CP=α×compactness, zero free parameters. Radial 1/R profile, signed-model fit to Sgr A*, mass independence, 5 falsification criteria. 6/7.'),
    'eht_cp_prediction':        ('EHT CP Prediction: α Floor',           'Parameter-free: CP = α × compactness. Radial 1/R profile, signed-model fit to Sgr A*, mass independence, 5 falsification criteria. 6/7.'),
    'muon_g2_geometry':         ('The Muon g-2 from Geometry',             'Entire a_μ from D_IV⁵ geometry. QED+EW+HVP+HLbL. 1 ppm. WP25 confirmed.'),
    'baby_trace_formula':       ('The Baby Trace Formula',                 'D_IV³ Selberg trace formula. All m=1. c-function. Plancherel. Baby Selberg.'),
    'spectral_gap':             ('The Spectral Gap = Mass Gap',            'λ₁(Q⁵) = 6 = C₂ = mass gap. Proton mass IS first eigenvalue × π⁵ × m_e.'),
    'width_sweep_derivability':   ('Width-Sweep Derivability',              'Three-way information budget: narrow, default, wide windows. AC dichotomy verification. 7/7.'),
    'so17_a6_polynomial':         ('SO(17): a₆(n) Polynomial',             'Elie: Full a₆(n) degree-12 polynomial. a₆(Q⁵)=363884219/1351350. Num=19×23×832687. Three Theorems confirmed k=6. 10/10.'),
    'so19_a7_polynomial':         ('SO(19): a₇(n) Polynomial',             'Elie: Full a₇(n) degree-14 polynomial. a₇(Q⁵)=78424343/289575. Num=19×4127597. Three Theorems confirmed k=7. 12/12.'),
    'so21_a8_polynomial':         ('SO(21): a₈(n) Polynomial',             'Elie: a₈(Q⁵)=670230838/2953665. Prime 17 ENTERS (14/14). Three Theorems confirmed k=1..8.'),
    'so23_a9_polynomial':         ('SO(23): a₉(n) Polynomial',             'Elie: a₉(Q⁵)=4412269889539/27498621150. Prime 19 ENTERS (cosmic denominator Ω_Λ=13/19). den=2×3⁵×5²×7²×11×13×17×19. 14/19 clean; poly needs dps≥300.'),
    'so25_a10_polynomial':        ('SO(25): a₁₀(n) Polynomial',            'Elie: a₁₀(Q⁵)=2409398458451/21709437750 (PRIME num!). Quiet level: den primes≤17, no 19. Also: a₉ poly RECOVERED (16/23 clean). Cascade wall at k=10 (8/23).'),
    'symbolic_a12_polynomial':    ('Enhanced Cascade to a₁₂',               'Elie: Breaking the cascade wall. P_MAX=1000, dps=400, n=3..27. Robust polynomial recovery. Targeting a₁₁ (Golay prime 23) + a₁₂ (quiet).'),
    'linking_cascade_constant':   ('Linking Cascade Constant c',             'Elie: c(α_c) from random 3-SAT VIG complex. F₂ homology + R³ linking. Prediction: c=1/2. Result: c→0. Strong force doesn\'t confine.'),
    'weak_homological_force':     ('The Weak Homological Force',              'Elie: Pure F₂ algebra — Δβ₁ per extension. No R³. If Δβ₁≥0: β₁ never decreases → T25 → P≠NP. The error-correction cost of dimensional expansion.'),
    'basis_rotation':             ('Basis Rotation: Weinberg Angle',          'Elie: r = dim(H₁_old ∩ H₁_new)/β₁ after extensions. 1-clause: r=1 (no mixing). Multi-clause: r<1 (mixing). Cumulative decay → exponential disorientation → 2^Θ(n).'),
    'shannon_independence':       ('Shannon Independence: AC(0)',              'Elie: Are H₁ fiat bits independent? Jaccard overlap, kill probability, sequential resolution cost. AC > 0 for all polynomial methods → Shannon Bridge → P ≠ NP.'),
}

# ─── Build reverse lookup: stem -> category ──────────────────────────
_STEM_TO_CAT = {}
for cat, stems in CATEGORIES.items():
    for stem in stems:
        _STEM_TO_CAT[stem] = cat


def discover_toys(play_dir):
    """Auto-discover all toy_*.py files and build metadata list."""
    toys = []
    for path in sorted(glob.glob(os.path.join(play_dir, 'toy_*.py'))):
        filename = os.path.basename(path)
        stem = filename[4:-3]  # strip 'toy_' prefix and '.py' suffix

        # Get title and description
        if stem in METADATA:
            title, desc = METADATA[stem]
        else:
            title, desc = _extract_from_docstring(path, stem)

        # Get category
        category = _STEM_TO_CAT.get(stem, 'Uncategorized')

        # Detect tags
        tags = []
        if '[SPECULATIVE]' in desc or category == 'Speculative':
            tags.append('SPECULATIVE')
        if '[EXPLORATORY]' in desc:
            tags.append('EXPLORATORY')

        # Extract toy number from docstring if present
        toy_num = _extract_toy_number(path)

        toys.append({
            'stem': stem,
            'filename': filename,
            'path': path,
            'title': title,
            'desc': desc.replace('[SPECULATIVE]', '').replace('[EXPLORATORY]', '').strip(),
            'category': category,
            'tags': tags,
            'number': toy_num,
        })

    return toys


def _extract_from_docstring(path, stem):
    """Extract title and description from a toy's docstring."""
    try:
        with open(path, 'r') as f:
            content = f.read(2000)  # first 2KB is enough
        # Find docstring
        m = re.search(r'"""(.*?)"""', content, re.DOTALL)
        if m:
            doc = m.group(1).strip()
            lines = [l.strip() for l in doc.split('\n') if l.strip()]
            # Skip lines that are just '===' decorators
            lines = [l for l in lines if not re.match(r'^[=\-]+$', l)]
            # Skip copyright lines
            lines = [l for l in lines if 'Copyright' not in l
                     and 'license' not in l.lower()
                     and 'intellectual property' not in l.lower()
                     and 'Created with' not in l]
            title = lines[0] if lines else stem.replace('_', ' ').title()
            # Clean title: remove "Toy NN:" prefix
            title = re.sub(r'^Toy\s+\d+[:\s]*', '', title)
            desc = lines[1] if len(lines) > 1 else ''
            return title[:60], desc[:120]
    except Exception:
        pass
    return stem.replace('_', ' ').title(), ''


# Fallback number assignments for toys whose docstrings lack "Toy NN"
_STEM_TO_NUMBER = {
    'universe_machine': 1, 'z3_color_wheel': 2, '1920_cancellation': 3,
    'lie_algebra': 4, 'mass_tower': 5, 'respirator': 6, 'dual_face': 7,
    'homology': 8, 'dirac_number': 9, 'arrow_of_time': 10,
    'channel_137': 11, 'reality_budget': 12, 'master_equation': 13,
    'universe_builder': 14, 'what_if': 15, 'pattern_finder': 16,
    'proof_tree': 17, 'self_observer': 18, 'three_layers': 19,
    'godel_limit': 20, 'dark_sector': 21, 'cosmic_pie': 22,
    'meson_garden': 23, 'self_starting': 24, 'black_hole': 25,
    'mond_acceleration': 26, 'bell_inequality': 27, 'why56': 28,
    'why_now': 29, 'atom_assembler': 30, 'hopf_fibration': 31,
    'commitment_detector': 32, 'commitment_survey': 33,
    'substrate_sail': 34, 'bst_telescope': 35, 'feynman_geometry': 36,
    'star_machine': 37, 'electron_agent': 38, 'double_slit': 39,
    'shannon_channel': 40, 'unfreeze': 41, 'gravitational_bell': 42,
    'particle_zoo': 43, 'complexity': 44, 'newton_g': 45,
    'lithium7': 46, 'deuteron': 47, 'reality_writer': 48,
    'higgs': 49, 'substrate_layers': 50, 'fermion_staircase': 51,
    'ckm_triangle': 52, 'proton_spin': 53, 'cmb_ruler': 54,
    'biology_stack': 55, 'jwst_prediction': 56, 'toda_soliton': 57,
    'mode_fusion': 58, 'channel_capacity': 59, 'chern_oracle': 60,
    'weyl_cancellation': 61, 'contact_conservation': 62,
    'recapitulation': 63, 'alpha_max': 64, 'consciousness_modes': 65,
    'vacuum_dipole': 66, 'coxeter_frequency': 67, 'bergman_kernel': 68,
    'e8_unifier': 69, 'chern_budget': 70, 'toda_smatrix': 71,
    'soliton_thermo': 72, 'commitment_cycle': 73,
    'partition_function': 74, 'neutron_proton': 75,
    'plancherel_spectrum': 76, 'mass_gap_proof': 77,
    'rotation_curves': 78, 'embedding_tower': 79,
    'running_couplings': 80, 'proton_radius': 81,
    'casimir_modification': 82, 'neutrino_oscillation': 83,
    'cosmic_timeline': 84, 'e8_electroweak': 85,
    'e8_generations': 86, 'baryon_radiative': 88,
    'berezin_toeplitz': 89, 'poisson_szego': 87,
    'e8_higgs_sector': 91, 'e8_branching': 93,
    'predictions_catalog': 94, 'c1_spectral_proof': 95,
    'self_dual_point': 96, 'nuclear_magic': 97,
    'dirac_large_number': 98, 'superconductor_ceiling': 99,
    'centennial': 100, 'consciousness_mode_stack': 101,
    'tba_soliton_gas': 92, 'sqrt30_connection': 90,
    'selberg_bridge': 103,
    'fill_fraction_closure': 104,
    '42': 102,
    'cosmological_cascade': 108, 'orch_or': 109,
    'three_generations': 110, 'strong_cp': 111,
    'einstein_from_commitment': 112, 'schrodinger_substrate': 113,
    'maxwell_geometry': 114, 'anomaly_cancellation': 115,
    'baryon_asymmetry': 116,
    'heavy_mesons': 117, 'quark_masses': 118,
    'magnetic_moments': 119, 'hydrogen_spectrum': 120,
    'alpha_particle': 121, 'axial_coupling': 122,
    'electron_g2': 123,
    'w_mass': 124, 'casimir_commitment': 125,
    'primordial_gw': 126, 'desi_expansion': 127,
    'gw_echoes': 128, 'deconfinement': 129,
    'error_correction': 130, 'isotropy_proof': 131,
    'field_equations': 132, 'first_commitment': 133,
    'why_this_universe': 134, 'chiral_condensate': 135,
    'pion_radius': 136, 'constants_dashboard': 137,
    'circles_on_surfaces': 138,
    'hyperfine_splittings': 139, 'quantum_metric': 140,
    'hilbert_series': 141, 'zeta_qed': 142,
    'proton_code': 143, 'code_machine': 144,
    'self_duality_rh': 145,
    'spectral_multiplicity': 146, 'spectral_zeta': 147,
    'harmonic_alpha': 148,
    'effective_dimension': 149,
    'zonal_spectral': 150,
    'plancherel_dictionary': 151,
    'corrected_a3': 152,
    'genesis': 153,
    'q3_inside_q5': 154,
    'spectral_transport': 155,
    'transport_kernel': 156,
    'spectral_tower': 157,
    'inverse_transport': 158,
    'cfunction_ratio': 159,
    'rank_change_lift': 160,
    'geometric_spectral_duality': 161,
    'functional_determinant': 162,
    'langlands_dual': 163,
    'satake_parameters': 164,
    'intertwining_bridge': 165,
    'maass_selberg_constraint': 166,
    'sp6_representation_ring': 167,
    'theta_correspondence': 168,
    'arthur_packets': 169,
    'partition_function_map': 170,
    'quantum_group': 171,
    'wzw_modular_data': 172,
    'sm_branching': 173,
    'baby_langlands': 174,
    'level_rank_duality': 175,
    'verlinde_fusion': 176,
    'siegel_modular': 177,
    'conformal_embedding': 178,
    'coset_uniqueness': 179,
    'massgap_anatomy': 180,
    'c6_network': 181,
    'exceptional_chain': 182,
    'e6_spectral_bridge': 183,
    'spectral_partial_sums': 184,
    'alternating_sums': 185,
    'spectral_cascade': 186,
    'fusion_ring_so7': 187,
    'conformal_weights': 188,
    'palindrome_fusion': 189,
    'spiral_substrate': 190,
    'pi_anatomy': 191,
    'siegel_deep': 193,
    'spiral_conjecture': 192,
    'baby_case_sp4': 194,
    'winding_confinement': 195,
    'verlinde_1747': 196,
    'baby_case_closure': 197,
    '137_verlinde': 198,
    'elie_discoveries': 199,
    'ramanujan_probe': 200,
    'golay_construction': 201,
    'arthur_elimination': 202,
    'wounded_prey': 203,
    'the_kill': 204,
    'kill_it_more': 205,
    'maass_selberg_kill': 206,
    'rank2_coupling': 207,
    'gue_from_so2': 208,
    'ads_vs_bst': 209,
    'plancherel_primes': 210,
    'elie_gap_analysis': 213,
    'plancherel_positivity': 214,
    'arithmetic_lattice': 215,
    'arthur_obstruction': 216,
    'period_integral_probe': 217,
    'trace_formula_channel': 218,
    'geometric_side': 219,
    'test_function_hunt': 220,
    'heat_trace_geometric': 221,
    'detuned_triples': 222,
    'geometric_smoothness': 223,
    'proof_by_contradiction': 224,
    'algebraic_complexity': 225,
    'coefficient_rigidity': 226,
    'cancer_code_failure': 227,
    'rank2_contour': 228,
    'born_rule': 232, 'showcase': 229, 'bst_matrix': 230,
    'scale_invariant_pathology': 231,
    'ac_classification': 233,
    '147_tiling': 234,
    'neutron_computer': 235,
    '147_derivation': 236,
    'contributor_certificate': 237,
    'graph_brain': 238,
    'ac0_grid': 239,
    'linearization': 240,
    'seeley_dewitt_a4a5': 241,
    'q4_kill_shot': 246,
    'gilkey_polynomial': 248,
    'linear_gilkey': 249,
    'linear_gilkey_fixed': 250,
    'branching_so7_sp6': 251,
    'eht_cp_prediction': 253,
    'a5_nonspherical': 254,
    'a4_polynomial_a5_precision': 255,
    'a5_polynomial': 257,
    'verify_c10': '257b',
    'constrained': '257c',
    'prove_c10': '257d',
    'ac_mutual_information': 258,
    'topology_fiat_correlation': 259,
    'crystallography_ac0': 260,
    'convergent_diagnosis': 261,
    'perturbation_ac_decomposition': 262,
    'swallowtail_ifiat': 263,
    'tseitin_expanders': 264,
    'ac_classification_extended': 265,
    'sign_flip_at_scale': 266,
    'statphys_unification': 267,
    'first_blood_ifiat_betti': 268,
    'topology_guided_solver': 269,
    'ef_rigidity_threshold': 270,
    'ac_dichotomy_verification': 271,
    'width_sweep_derivability': 272,
    'so17_a6_polynomial': 273,
    'so19_a7_polynomial': 274,
    'so21_a8_polynomial': 275,
    'so23_a9_polynomial': 276,
    'so25_a10_polynomial': 277,
    'symbolic_a12_polynomial': 278,
    'linking_cascade_constant': 279,
    'weak_homological_force': 280,
    'basis_rotation': 281,
    'shannon_independence': 282,
}


def _extract_toy_number(path):
    """Extract toy number from docstring or fallback table."""
    stem = os.path.basename(path)[4:-3]  # strip toy_ and .py

    # Try docstring first
    try:
        with open(path, 'r') as f:
            content = f.read(500)
        m = re.search(r'Toy\s+(\d+)', content)
        if m:
            return int(m.group(1))
    except Exception:
        pass

    # Fallback to table
    if stem in _STEM_TO_NUMBER:
        return _STEM_TO_NUMBER[stem]

    return 999


# ═══════════════════════════════════════════════════════════════════════
#  Tkinter GUI
# ═══════════════════════════════════════════════════════════════════════

class BSTLauncher:
    def __init__(self, root, toys):
        self.root = root
        self.all_toys = toys
        self.filtered_toys = list(toys)
        self.active_category = 'All'
        self.search_var = tk.StringVar()
        self.search_var.trace_add('write', self._on_search)
        self.card_widgets = []

        self._setup_window()
        self._build_ui()
        self._populate_cards()

    def _setup_window(self):
        self.root.title('BST Playground')
        self.root.configure(bg=BG)

        # Size and center
        w, h = 1200, 800
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.root.geometry(f'{w}x{h}+{x}+{y}')
        self.root.minsize(900, 600)

        # Configure ttk style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Dark.TFrame', background=BG)
        style.configure('Sidebar.TFrame', background=BG_SIDEBAR)
        style.configure('Card.TFrame', background=BG_CARD)
        style.configure('Dark.TLabel', background=BG, foreground=FG)
        style.configure('Title.TLabel', background=BG, foreground=FG_TITLE,
                        font=('Helvetica', 24, 'bold'))
        style.configure('Subtitle.TLabel', background=BG, foreground=FG_DIM,
                        font=('Helvetica', 11))
        style.configure('CatBtn.TButton', background=BG_SIDEBAR, foreground=FG,
                        font=('Helvetica', 12), borderwidth=0, padding=(12, 6))
        style.map('CatBtn.TButton',
                  background=[('active', CAT_HOVER)])

    def _build_ui(self):
        # ── Header ───────────────────────────────────────────────
        header = tk.Frame(self.root, bg=BG, height=80)
        header.pack(fill='x', padx=0, pady=0)
        header.pack_propagate(False)

        title_frame = tk.Frame(header, bg=BG)
        title_frame.pack(side='left', padx=20, pady=10)

        tk.Label(title_frame, text='BST Playground',
                 font=('Helvetica', 22, 'bold'), fg=FG_TITLE, bg=BG
                 ).pack(anchor='w')
        self.count_label = tk.Label(
            title_frame, text=f'{len(self.all_toys)} toys',
            font=('Helvetica', 11), fg=FG_DIM, bg=BG)
        self.count_label.pack(anchor='w')

        # Right side: search + buttons
        right_frame = tk.Frame(header, bg=BG)
        right_frame.pack(side='right', padx=20, pady=15)

        # Random button
        self.random_btn = tk.Button(
            right_frame, text='\u2684  Random',
            font=('Helvetica', 12), fg=FG_TITLE, bg=ACCENT,
            activebackground='#ff5577', activeforeground=FG_TITLE,
            relief='flat', padx=12, pady=4,
            command=self._launch_random)
        self.random_btn.pack(side='right', padx=(10, 0))

        # Search
        search_frame = tk.Frame(right_frame, bg='#2a2a4e',
                                highlightthickness=1,
                                highlightbackground=BORDER,
                                highlightcolor=ACCENT2)
        search_frame.pack(side='right')

        tk.Label(search_frame, text='\U0001f50d', font=('Helvetica', 13),
                 fg=FG_DIM, bg='#2a2a4e').pack(side='left', padx=(8, 2))

        self.search_entry = tk.Entry(
            search_frame, textvariable=self.search_var,
            font=('Helvetica', 13), fg=FG_TITLE, bg='#2a2a4e',
            insertbackground=FG_TITLE, relief='flat', width=25)
        self.search_entry.pack(side='left', padx=(0, 8), pady=4)

        # ── Main body: sidebar + cards ───────────────────────────
        body = tk.Frame(self.root, bg=BG)
        body.pack(fill='both', expand=True)

        # Sidebar
        self.sidebar = tk.Frame(body, bg=BG_SIDEBAR, width=200)
        self.sidebar.pack(side='left', fill='y')
        self.sidebar.pack_propagate(False)

        tk.Label(self.sidebar, text='Categories',
                 font=('Helvetica', 11, 'bold'), fg=FG_DIM, bg=BG_SIDEBAR
                 ).pack(anchor='w', padx=16, pady=(12, 6))

        self.cat_buttons = {}
        self._add_cat_button('All', len(self.all_toys))
        for cat_name in CATEGORIES:
            count = sum(1 for t in self.all_toys if t['category'] == cat_name)
            if count > 0:
                self._add_cat_button(cat_name, count)
        # Uncategorized
        uncat = sum(1 for t in self.all_toys if t['category'] == 'Uncategorized')
        if uncat > 0:
            self._add_cat_button('Uncategorized', uncat)

        # Separator
        tk.Frame(self.sidebar, bg=BORDER, height=1).pack(fill='x', padx=16, pady=8)

        # Launch category button
        self.launch_cat_btn = tk.Button(
            self.sidebar, text='Launch Category',
            font=('Helvetica', 11), fg=FG_TITLE, bg='#2a5040',
            activebackground='#3a6050', activeforeground=FG_TITLE,
            relief='flat', padx=10, pady=4,
            command=self._launch_category)
        self.launch_cat_btn.pack(padx=16, pady=(4, 8), fill='x')

        # Card area (scrollable)
        self.card_area = tk.Frame(body, bg=BG)
        self.card_area.pack(side='left', fill='both', expand=True)

        # Canvas + scrollbar for scrolling
        self.canvas = tk.Canvas(self.card_area, bg=BG, highlightthickness=0)
        self.vscroll = tk.Scrollbar(self.card_area, orient='vertical',
                                    command=self.canvas.yview,
                                    bg=SCROLLBAR, troughcolor=BG,
                                    width=10, relief='flat')
        self.canvas.configure(yscrollcommand=self.vscroll.set)

        self.vscroll.pack(side='right', fill='y')
        self.canvas.pack(side='left', fill='both', expand=True)

        # Inner frame for cards
        self.inner_frame = tk.Frame(self.canvas, bg=BG)
        self.canvas_window = self.canvas.create_window(
            (0, 0), window=self.inner_frame, anchor='nw')

        self.inner_frame.bind('<Configure>', self._on_frame_configure)
        self.canvas.bind('<Configure>', self._on_canvas_configure)

        # Mouse wheel scrolling
        self.canvas.bind_all('<MouseWheel>', self._on_mousewheel)
        # For macOS trackpad
        self.canvas.bind_all('<Button-4>', lambda e: self.canvas.yview_scroll(-3, 'units'))
        self.canvas.bind_all('<Button-5>', lambda e: self.canvas.yview_scroll(3, 'units'))

        # ── Status bar ───────────────────────────────────────────
        status = tk.Frame(self.root, bg=BG_SIDEBAR, height=28)
        status.pack(fill='x', side='bottom')
        status.pack_propagate(False)

        self.status_label = tk.Label(
            status,
            text='  Bubble Spacetime Theory  |  (c) 2026 Casey Koons  |  Created with Claude Opus 4.6',
            font=('Helvetica', 10), fg=FG_DIM, bg=BG_SIDEBAR, anchor='w')
        self.status_label.pack(fill='x', padx=8, pady=4)

        # Highlight "All" initially
        self._select_category('All')

    def _add_cat_button(self, name, count):
        btn = tk.Button(
            self.sidebar,
            text=f'  {name}  ({count})',
            font=('Helvetica', 12),
            fg=FG, bg=BG_SIDEBAR,
            activebackground=CAT_HOVER, activeforeground=FG_TITLE,
            relief='flat', anchor='w', padx=8, pady=3,
            command=lambda n=name: self._select_category(n))
        btn.pack(fill='x', padx=8, pady=1)
        self.cat_buttons[name] = btn

    def _select_category(self, name):
        self.active_category = name
        # Update button highlights
        for cat_name, btn in self.cat_buttons.items():
            if cat_name == name:
                btn.configure(bg=CAT_ACTIVE, fg=FG_TITLE)
            else:
                btn.configure(bg=BG_SIDEBAR, fg=FG)
        self._apply_filter()

    def _on_search(self, *args):
        self._apply_filter()

    def _apply_filter(self):
        query = self.search_var.get().lower().strip()
        cat = self.active_category

        results = []
        for t in self.all_toys:
            # Category filter
            if cat != 'All' and t['category'] != cat:
                continue
            # Search filter
            if query:
                searchable = f"{t['title']} {t['desc']} {t['stem']} {t['category']} {' '.join(t['tags'])}".lower()
                if not all(word in searchable for word in query.split()):
                    continue
            results.append(t)

        self.filtered_toys = results
        self._populate_cards()

    def _populate_cards(self):
        # Clear existing
        for w in self.card_widgets:
            w.destroy()
        self.card_widgets.clear()

        # Count label
        total = len(self.all_toys)
        showing = len(self.filtered_toys)
        if showing == total:
            self.count_label.configure(text=f'{total} toys')
        else:
            self.count_label.configure(text=f'{showing} of {total} toys')

        if not self.filtered_toys:
            lbl = tk.Label(self.inner_frame, text='No toys match your search.',
                           font=('Helvetica', 14), fg=FG_DIM, bg=BG)
            lbl.pack(pady=40)
            self.card_widgets.append(lbl)
            return

        # Sort by toy number
        toys_sorted = sorted(self.filtered_toys, key=lambda t: t['number'])

        # Build cards in a grid
        # We'll use a grid layout inside inner_frame
        cols = 3
        for idx, toy in enumerate(toys_sorted):
            row = idx // cols
            col = idx % cols
            card = self._make_card(self.inner_frame, toy)
            card.grid(row=row, column=col, padx=8, pady=6, sticky='nsew')
            self.card_widgets.append(card)

        # Make columns expand equally
        for c in range(cols):
            self.inner_frame.columnconfigure(c, weight=1, uniform='card')

        # Reset scroll
        self.canvas.yview_moveto(0)

    def _make_card(self, parent, toy):
        card = tk.Frame(parent, bg=BG_CARD, relief='flat',
                        highlightthickness=1, highlightbackground=BORDER,
                        padx=12, pady=10)

        # Number badge + title row
        top_row = tk.Frame(card, bg=BG_CARD)
        top_row.pack(fill='x', anchor='w')

        num_text = f'#{toy["number"]}' if toy['number'] < 999 else ''
        if num_text:
            num_lbl = tk.Label(top_row, text=num_text,
                               font=('Helvetica', 10, 'bold'),
                               fg=ACCENT, bg=BG_CARD)
            num_lbl.pack(side='left', padx=(0, 6))

        title_lbl = tk.Label(top_row, text=toy['title'],
                             font=('Helvetica', 12, 'bold'),
                             fg=FG_TITLE, bg=BG_CARD, anchor='w',
                             wraplength=280)
        title_lbl.pack(side='left', fill='x', expand=True)

        # Tags
        if toy['tags']:
            tag_frame = tk.Frame(card, bg=BG_CARD)
            tag_frame.pack(fill='x', anchor='w', pady=(2, 0))
            for tag in toy['tags']:
                color = ACCENT3 if tag == 'SPECULATIVE' else ACCENT2
                tk.Label(tag_frame, text=tag,
                         font=('Helvetica', 9, 'bold'),
                         fg=color, bg=BG_CARD).pack(side='left', padx=(0, 6))

        # Description
        desc_lbl = tk.Label(card, text=toy['desc'],
                            font=('Helvetica', 10),
                            fg=FG_DIM, bg=BG_CARD, anchor='w',
                            wraplength=280, justify='left')
        desc_lbl.pack(fill='x', anchor='w', pady=(4, 0))

        # Category pill
        cat_lbl = tk.Label(card, text=toy['category'],
                           font=('Helvetica', 9),
                           fg='#6688aa', bg=BG_CARD, anchor='w')
        cat_lbl.pack(fill='x', anchor='w', pady=(4, 0))

        # Make entire card clickable
        def on_enter(e, c=card):
            c.configure(bg=BG_CARD_HOVER)
            for child in c.winfo_children():
                try:
                    child.configure(bg=BG_CARD_HOVER)
                    for grandchild in child.winfo_children():
                        try:
                            grandchild.configure(bg=BG_CARD_HOVER)
                        except tk.TclError:
                            pass
                except tk.TclError:
                    pass

        def on_leave(e, c=card):
            c.configure(bg=BG_CARD)
            for child in c.winfo_children():
                try:
                    child.configure(bg=BG_CARD)
                    for grandchild in child.winfo_children():
                        try:
                            grandchild.configure(bg=BG_CARD)
                        except tk.TclError:
                            pass
                except tk.TclError:
                    pass

        def on_click(e, t=toy):
            self._launch_toy(t)

        # Bind to card and all children
        for widget in [card] + card.winfo_children():
            widget.bind('<Enter>', on_enter)
            widget.bind('<Leave>', on_leave)
            widget.bind('<Button-1>', on_click)
            for grandchild in widget.winfo_children():
                grandchild.bind('<Enter>', on_enter)
                grandchild.bind('<Leave>', on_leave)
                grandchild.bind('<Button-1>', on_click)

        return card

    def _launch_toy(self, toy):
        self.status_label.configure(
            text=f'  Launching: {toy["title"]} ({toy["filename"]})...',
            fg=ACCENT2)
        self.root.update_idletasks()
        subprocess.Popen([sys.executable, toy['path']])
        self.root.after(2000, lambda: self.status_label.configure(
            text='  Bubble Spacetime Theory  |  (c) 2026 Casey Koons  |  Created with Claude Opus 4.6',
            fg=FG_DIM))

    def _launch_random(self):
        if self.filtered_toys:
            toy = random.choice(self.filtered_toys)
            self._launch_toy(toy)

    def _launch_category(self):
        for toy in self.filtered_toys:
            subprocess.Popen([sys.executable, toy['path']])
        count = len(self.filtered_toys)
        self.status_label.configure(
            text=f'  Launched {count} toys!', fg=ACCENT2)
        self.root.after(3000, lambda: self.status_label.configure(
            text='  Bubble Spacetime Theory  |  (c) 2026 Casey Koons  |  Created with Claude Opus 4.6',
            fg=FG_DIM))

    # ── Scroll handling ──────────────────────────────────────────
    def _on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def _on_canvas_configure(self, event):
        self.canvas.itemconfigure(self.canvas_window, width=event.width)

    def _on_mousewheel(self, event):
        # macOS: event.delta is already in the right direction
        self.canvas.yview_scroll(-event.delta, 'units')


# ═══════════════════════════════════════════════════════════════════════
#  CLI fallback (for headless / SSH sessions)
# ═══════════════════════════════════════════════════════════════════════

def cli_mode(toys):
    """Simple terminal fallback when Tk is unavailable."""
    print()
    print('=' * 60)
    print('  BST PLAYGROUND — Bubble Spacetime Theory')
    print(f'  {len(toys)} visualization toys')
    print('  (c) 2026 Casey Koons. All rights reserved.')
    print('=' * 60)
    print()

    # Group by category
    cats = {}
    for t in toys:
        cats.setdefault(t['category'], []).append(t)

    for cat_name in list(CATEGORIES.keys()) + ['Uncategorized']:
        if cat_name not in cats:
            continue
        print(f'  ── {cat_name} ({len(cats[cat_name])}) ──')
        for t in sorted(cats[cat_name], key=lambda x: x['number']):
            num = f'#{t["number"]:>3d}' if t['number'] < 999 else '    '
            print(f'    {num}  {t["title"]}')
            print(f'          {t["desc"][:70]}')
        print()

    print('  Enter toy number to launch (q to quit):')
    while True:
        try:
            choice = input('  > ').strip().lower()
        except (EOFError, KeyboardInterrupt):
            break
        if choice in ('q', 'quit', 'exit'):
            break
        if choice == 'r':
            t = random.choice(toys)
            print(f'  Launching #{t["number"]} {t["title"]}...')
            subprocess.Popen([sys.executable, t['path']])
            continue
        try:
            num = int(choice)
            matches = [t for t in toys if t['number'] == num]
            if matches:
                t = matches[0]
                print(f'  Launching {t["title"]}...')
                subprocess.run([sys.executable, t['path']])
            else:
                print(f'  No toy #{num} found.')
        except ValueError:
            # Search by keyword
            query = choice.lower()
            matches = [t for t in toys if query in t['title'].lower()
                       or query in t['desc'].lower()
                       or query in t['stem'].lower()]
            if matches:
                for t in matches:
                    print(f'    #{t["number"]:>3d}  {t["title"]}')
                if len(matches) == 1:
                    print(f'  Launching {matches[0]["title"]}...')
                    subprocess.run([sys.executable, matches[0]['path']])
            else:
                print(f'  No matches for "{choice}"')


# ═══════════════════════════════════════════════════════════════════════
#  Main
# ═══════════════════════════════════════════════════════════════════════

def main():
    play_dir = os.path.dirname(os.path.abspath(__file__))
    toys = discover_toys(play_dir)

    if not toys:
        print('No toy_*.py files found in', play_dir)
        return

    # Try GUI, fall back to CLI
    use_cli = '--cli' in sys.argv or '-c' in sys.argv

    if not use_cli:
        try:
            root = tk.Tk()
            BSTLauncher(root, toys)
            root.mainloop()
        except tk.TclError:
            print('  [No display available, falling back to CLI mode]')
            cli_mode(toys)
    else:
        cli_mode(toys)


if __name__ == '__main__':
    main()
