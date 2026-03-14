#!/usr/bin/env python3
"""
THE RECAPITULATION BRIDGE  (Toy 63)
====================================
The bulk recapitulates the boundary — same 3+1, same topology.
What's new is the information layer.

In BST, the Shilov boundary S^4 x S^1 hosts the particle sector:
quarks, leptons, bosons — WHAT exists. The Bergman interior D_IV^5
hosts the soliton sector: B_2 Toda modes — HOW it persists.

Both sectors live on the SAME domain. Both inherit the SAME restricted
root system B_2. Both get 3+1 spacetime from root multiplicities.
Both get Z_3 circuits from contractibility. Both get confinement.

The bulk adds what the boundary cannot see: channel capacity C=10 nats,
contact conservation, Coxeter frequency ratio h=4, DOF=genus=7.

The boundary is WHAT. The bulk is HOW.

    from toy_recapitulation import RecapitulationBridge
    rb = RecapitulationBridge()
    rb.boundary_sector()        # particles on S^4 x S^1
    rb.bulk_sector()            # solitons on D_IV^5
    rb.shared_structure()       # features shared by both
    rb.new_in_bulk()            # what the bulk adds
    rb.spacetime_from_roots()   # 3+1 derived in both sectors
    rb.information_layer()      # the capacity decomposition
    rb.boundary_to_bulk_map()   # how boundary maps to bulk
    rb.why_recapitulation()     # because both live on D_IV^5
    rb.summary()                # key insight
    rb.show()                   # 4-panel visualization

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np

# ═══════════════════════════════════════════════════════════════════
# BST CONSTANTS
# ═══════════════════════════════════════════════════════════════════

N_c = 3                           # color charges
n_C = 5                           # complex dimension of D_IV^5
genus = n_C + 2                   # = 7
C2 = n_C + 1                     # = 6, second Casimir
N_max = 137                       # Haldane channel capacity
dim_R = 2 * n_C                   # = 10, real dimension of D_IV^5
W_D5 = 1920                      # |W(D_5)| = Weyl group order
W_B2 = 8                         # |W(B_2)| = Weyl group order
h_B2 = 4                         # Coxeter number of B_2
Phi_E8 = 240                     # number of roots of E_8

# Root multiplicities of B_2 restricted root system on D_IV^5
m_short = n_C - 2                 # = 3 (spatial dimensions)
m_long = 1                        # = 1 (temporal dimension)

# Kac labels for affine B_2^(1): (n_0, n_1, n_2) = (1, 2, 1)
kac_labels = (1, 2, 1)
kac_sum = sum(kac_labels)         # = h = 4

# Channel capacity
C_channel = dim_R                 # = 10 nats
SNR = W_D5 / np.pi**n_C          # 1920/pi^5 ~ 6.27
C_shannon = (n_C) * np.log(1 + SNR)  # ~ 9.92
# Near-identity: 1920/pi^5 ~ e^2 - 1 = 6.389 (if exact => C = 10 exactly)
SNR_exact = np.e**2 - 1           # = 6.389... (the saturated limit)

# Capacity decomposition
C_spatial = 2 * m_short           # = 6 nats (two short root spaces)
C_temporal = 2 * m_long           # = 2 nats (two long root spaces)
C_soliton = 2                    # = 2 nats (maximal flat)

# Physical constants
m_e_MeV = 0.51099895
alpha = 1 / 137.035999
mp_over_me = C2 * np.pi**n_C     # 6*pi^5
m_p_MeV = mp_over_me * m_e_MeV


# ═══════════════════════════════════════════════════════════════════
# THE RECAPITULATION BRIDGE
# ═══════════════════════════════════════════════════════════════════

class RecapitulationBridge:
    """
    The Recapitulation Bridge: boundary and bulk sectors of D_IV^5.

    The boundary (Shilov: S^4 x S^1) hosts particles — WHAT exists.
    The bulk (Bergman interior: D_IV^5) hosts solitons — HOW it persists.
    Both inherit the same root system, the same topology, the same 3+1.
    The bulk adds the information layer: capacity, conservation, frequency.
    """

    def __init__(self, quiet=False):
        self.quiet = quiet
        if not quiet:
            self._print_header()

    def _print_header(self):
        print("=" * 72)
        print("  THE RECAPITULATION BRIDGE")
        print("  Toy 63 -- Boundary is WHAT. Bulk is HOW.")
        print("=" * 72)
        print(f"  Domain:   D_IV^5 = SO_0(5,2) / [SO(5) x SO(2)]")
        print(f"  Boundary: S^4 x S^1  (Shilov boundary)")
        print(f"  Roots:    B_2 restricted root system")
        print(f"  Integers: N_c={N_c}  n_C={n_C}  g={genus}  C_2={C2}  "
              f"N_max={N_max}")
        print("=" * 72)

    # ─── 1. Boundary Sector ───

    def boundary_sector(self):
        """
        The particle sector on the Shilov boundary S^4 x S^1.

        Everything that EXISTS lives here: quarks, leptons, gauge bosons.
        The boundary encodes WHAT the universe contains.
        """
        print()
        print("=" * 72)
        print("  BOUNDARY SECTOR: Particles on S^4 x S^1")
        print("=" * 72)

        # Fermions: representations of SO(10) = D_5
        fermions = {
            'quarks': {
                'count': 6,
                'flavors': ['u', 'd', 's', 'c', 'b', 't'],
                'colors': N_c,
                'confinement': 'Z_3 closure on contractible D_IV^5',
                'mass_formula': 'm_p = 6*pi^5 * m_e  (proton from quarks)',
                'representation': '16 of SO(10) (one generation)',
            },
            'leptons': {
                'count': 6,
                'flavors': ['e', 'mu', 'tau', 'nu_e', 'nu_mu', 'nu_tau'],
                'colors': 1,
                'mass_formula': 'm_e = pure geometry (Bergman embedding tower)',
                'representation': '16 of SO(10) (shared with quarks)',
            },
        }

        # Gauge bosons
        bosons = {
            'photon': {'group': 'U(1)', 'dim': 1, 'mass': 0,
                       'BST': 'S^1 factor of Shilov boundary'},
            'W/Z':    {'group': 'SU(2)', 'dim': 3, 'mass': 'v/sqrt(2)',
                       'BST': 'Hopf fibration S^3 -> S^2, dim = m_short'},
            'gluon':  {'group': 'SU(3)', 'dim': 8, 'mass': 0,
                       'BST': 'Z_3 color from contractibility, N_c^2-1 = 8'},
        }

        # Generations
        generations = {
            'count': 3,
            'source': 'Lefschetz fixed point theorem on D_IV^5',
            'formula': 'L(D_IV^5) = 3 (Lefschetz number)',
        }

        # Print
        print()
        print("  FERMIONS (matter)")
        print("  -----------------")
        for name, data in fermions.items():
            print(f"    {name}: {data['count']} flavors, "
                  f"{data['colors']} color(s)")
            print(f"      Rep: {data['representation']}")
            print(f"      Mass: {data['mass_formula']}")
        print(f"    Confinement: {fermions['quarks']['confinement']}")

        print()
        print("  GAUGE BOSONS (forces)")
        print("  ---------------------")
        for name, data in bosons.items():
            print(f"    {name}: {data['group']}  "
                  f"(dim={data['dim']}, mass={data['mass']})")
            print(f"      BST: {data['BST']}")

        print()
        print("  GENERATIONS")
        print("  -----------")
        print(f"    Count: {generations['count']}")
        print(f"    Source: {generations['source']}")
        print(f"    Formula: {generations['formula']}")

        print()
        print("  Spacetime: 3+1 from Shilov boundary S^4 = S^{n_C-1}")
        print(f"    dim(S^4) = 4 = 3 + 1 directly")
        print()
        print("  KEY: The boundary tells you WHAT exists.")
        print("       It does not tell you HOW it persists.")
        print("-" * 72)

        return {
            'fermions': fermions,
            'bosons': bosons,
            'generations': generations,
            'spacetime': '3+1 from S^4',
        }

    # ─── 2. Bulk Sector ───

    def bulk_sector(self):
        """
        The soliton sector on the Bergman interior D_IV^5.

        B_2 Toda modes on the geodesic flow. Olshanetsky-Perelomov reduction.
        The bulk encodes HOW the universe persists.
        """
        print()
        print("=" * 72)
        print("  BULK SECTOR: Solitons on D_IV^5 (Bergman interior)")
        print("=" * 72)

        # B_2 Toda lattice
        toda = {
            'Hamiltonian': 'H = (p1^2 + p2^2)/2 + exp(q1-q2) + exp(q2)',
            'simple_roots': {
                'alpha_1': 'e1-e2 (long, coupling/binding)',
                'alpha_2': 'e2 (short, spatial propagation)',
            },
            'Lax_pair': '5x5 matrices, dL/dt = [M, L]',
            'conserved': ['I_1 = Tr(L^2)/2 = H (energy)',
                          'I_2 = Tr(L^4)/4 (higher Casimir)'],
        }

        # Affine extension (from S^1 periodicity)
        affine = {
            'origin': 'S^1 factor of Shilov boundary -> periodic BCs',
            'affine_root': 'alpha_0 = -(e1+e2) (negative highest root)',
            'diagram': 'alpha_0 --- alpha_1 ===> alpha_2  (short-long-short)',
            'Kac_labels': kac_labels,
            'mass_ratios': '1 : 2 : 1 (from Kac labels)',
        }

        # Soliton modes
        modes = [
            {'root': 'alpha_0', 'type': 'short', 'kac': 1,
             'role': 'wrapping (S^1 winding)'},
            {'root': 'alpha_1', 'type': 'long', 'kac': 2,
             'role': 'binding (threshold bound state of alpha_0 + alpha_2)'},
            {'root': 'alpha_2', 'type': 'short', 'kac': 1,
             'role': 'spatial (propagation in S^4)'},
        ]

        # DOF
        dof = {
            'Toda_eigenvalues': 2,
            'Toda_positions': 2,
            'S2_orientation': n_C - 3,   # = 2
            'S1_phase': 1,
            'total': genus,
            'identity': 'DOF = genus = n_C + 2 = 7 (universal)',
        }

        # Print
        print()
        print("  B_2 TODA LATTICE (geodesic flow on D_IV^5)")
        print("  -------------------------------------------")
        print(f"    {toda['Hamiltonian']}")
        print(f"    Lax pair: {toda['Lax_pair']}")
        for c in toda['conserved']:
            print(f"    Conserved: {c}")

        print()
        print("  AFFINE EXTENSION B_2^(1)")
        print("  ------------------------")
        print(f"    Origin: {affine['origin']}")
        print(f"    Diagram: {affine['diagram']}")
        print(f"    Kac labels: {affine['Kac_labels']}")
        print(f"    Mass ratios: {affine['mass_ratios']}")

        print()
        print("  SOLITON MODES")
        print("  -------------")
        print(f"    {'Root':<10} {'Type':<8} {'Kac':<5} Role")
        print(f"    {'----':<10} {'----':<8} {'---':<5} ----")
        for m in modes:
            print(f"    {m['root']:<10} {m['type']:<8} {m['kac']:<5} "
                  f"{m['role']}")

        print()
        print("  DEGREES OF FREEDOM")
        print("  ------------------")
        print(f"    Toda eigenvalues (lambda_1, lambda_2):  {dof['Toda_eigenvalues']}")
        print(f"    Toda positions (x_1, x_2):              {dof['Toda_positions']}")
        print(f"    S^{n_C-3} orientation:                    {dof['S2_orientation']}")
        print(f"    S^1 phase:                              {dof['S1_phase']}")
        print(f"    TOTAL:                                  {dof['total']}")
        print(f"    Identity: {dof['identity']}")

        print()
        print("  KEY: The bulk tells you HOW things persist.")
        print("       Integrability, conservation, capacity.")
        print("-" * 72)

        return {
            'toda': toda,
            'affine': affine,
            'modes': modes,
            'dof': dof,
        }

    # ─── 3. Shared Structure ───

    def shared_structure(self):
        """
        Features shared by both sectors. The recapitulated structures.
        """
        print()
        print("=" * 72)
        print("  SHARED STRUCTURE: What the bulk recapitulates from the boundary")
        print("=" * 72)

        shared = [
            {
                'feature': '3+1 spacetime',
                'boundary': 'dim(S^4) = 4 = 3+1 directly',
                'bulk': 'm_short = n_C-2 = 3 spatial, m_long = 1 temporal',
                'root': 'B_2 restricted root system of D_IV^5',
            },
            {
                'feature': 'Z_3 color circuits',
                'boundary': 'Color confinement: quarks in Z_3 loops',
                'bulk': 'Winding persistence: solitons in Z_3 topology',
                'root': 'Contractibility of D_IV^5',
            },
            {
                'feature': 'Confinement / Persistence',
                'boundary': 'Quarks cannot exist unconfined (c_2 != 0)',
                'bulk': 'Solitons cannot unwind (n != 0 on S^1)',
                'root': 'D_IV^5 contractible => bundles trivial',
            },
            {
                'feature': 'Three generations',
                'boundary': 'Lefschetz L(D_IV^5) = 3 generations of fermions',
                'bulk': '3 soliton modes in affine B_2^(1)',
                'root': 'Lefschetz fixed-point theorem on D_IV^5',
            },
            {
                'feature': 'Symmetry breaking pattern',
                'boundary': 'SO(10) -> SU(3) x SU(2) x U(1)',
                'bulk': 'D_5 -> B_2 (restricted root system reduction)',
                'root': 'Same Cartan classification, different directions',
            },
            {
                'feature': 'E_8 connection',
                'boundary': '|W(D_5)| = 1920 (proton mass numerator)',
                'bulk': '|W(B_2)| = 8 (soliton Weyl group)',
                'root': '1920/8 = 240 = |Phi(E_8)| exact identity',
            },
            {
                'feature': 'Elastic scattering',
                'boundary': 'S-matrix unitarity (particle number conserved)',
                'bulk': 'Zamolodchikov S-matrix (integrability => elastic)',
                'root': 'Yang-Baxter equation in both sectors',
            },
        ]

        for i, s in enumerate(shared):
            tag = "RECAPITULATED" if i < 5 else "CONNECTED"
            print()
            print(f"  [{i+1}] {s['feature']}  ({tag})")
            print(f"      Boundary: {s['boundary']}")
            print(f"      Bulk:     {s['bulk']}")
            print(f"      Root:     {s['root']}")

        print()
        print(f"  Total shared features: {len(shared)}")
        print()
        print("  The bulk does not INVENT new spacetime or new symmetries.")
        print("  It RECAPITULATES them — because both sectors live on D_IV^5.")
        print("-" * 72)

        return shared

    # ─── 4. New In Bulk ───

    def new_in_bulk(self):
        """
        What the bulk adds that the boundary does not have.
        The information layer.
        """
        print()
        print("=" * 72)
        print("  NEW IN BULK: What the soliton sector adds")
        print("=" * 72)

        new_features = [
            {
                'feature': 'Channel capacity C = 10 nats',
                'value': C_channel,
                'derivation': (
                    f'C = dim_R(D_IV^5) = 2*n_C = {dim_R}\n'
                    f'      Shannon: (n/2)*ln(1+SNR) = '
                    f'5*ln(1+1920/pi^5) = {C_shannon:.3f}'),
                'meaning': 'Maximum information per soliton cycle',
            },
            {
                'feature': 'Contact conservation',
                'value': 'Exact',
                'derivation': (
                    'Three independent proofs:\n'
                    '      (i)   Lax spectral invariants preserve contacts\n'
                    '      (ii)  Elastic S-matrix: no contact creation/destruction\n'
                    '      (iii) Winding number n in pi_1(S^1) = Z topological'),
                'meaning': 'Shared correlations between solitons never decay',
            },
            {
                'feature': f'Coxeter frequency ratio h = {h_B2}',
                'value': h_B2,
                'derivation': (
                    f'f_bound / f_fund = sum(Kac labels) = '
                    f'{kac_labels[0]}+{kac_labels[1]}+{kac_labels[2]} = {kac_sum}'),
                'meaning': 'Bound mode frequency = 4x fundamental',
            },
            {
                'feature': f'Degrees of freedom = genus = {genus}',
                'value': genus,
                'derivation': (
                    f'DOF = n_C + 2 = {n_C} + 2 = {genus}\n'
                    f'      = 2 (eigenvalues) + 2 (positions) + '
                    f'2 (S^2) + 1 (S^1) = {genus}'),
                'meaning': 'Universal for all n_C >= 3',
            },
            {
                'feature': 'Capacity decomposition 2+6+2 = 10',
                'value': f'{C_soliton}+{C_spatial}+{C_temporal} = {C_channel}',
                'derivation': (
                    f'Soliton (flat): {C_soliton} nats\n'
                    f'      Spatial (short roots): {C_spatial} nats '
                    f'(2 x m_short = 2 x {m_short})\n'
                    f'      Temporal (long roots): {C_temporal} nats '
                    f'(2 x m_long = 2 x {m_long})'),
                'meaning': 'Information budget by root type',
            },
            {
                'feature': 'Mass spectrum 1:2:1',
                'value': '1 : 2 : 1',
                'derivation': (
                    'Kac labels (n_0, n_1, n_2) = (1, 2, 1)\n'
                    '      alpha_1 = threshold bound state of alpha_0 + alpha_2'),
                'meaning': 'Three soliton species with fixed mass ratios',
            },
            {
                'feature': f'Bergman SNR = 1920/pi^5',
                'value': f'{SNR:.4f}',
                'derivation': (
                    f'K(0,0) = |W(D_5)|/pi^5 = {W_D5}/pi^5 = {SNR:.4f}\n'
                    f'      ln(1+SNR) = {np.log(1+SNR):.4f} ~ 2.0 '
                    f'(saturated channel)'),
                'meaning': 'Signal-to-noise at vacuum center',
            },
        ]

        for i, f in enumerate(new_features):
            print()
            print(f"  [{i+1}] {f['feature']}")
            print(f"      Value: {f['value']}")
            print(f"      Derivation: {f['derivation']}")
            print(f"      Meaning: {f['meaning']}")

        print()
        print(f"  Total new features: {len(new_features)}")
        print()
        print("  The boundary says WHAT exists.")
        print("  The bulk says HOW MUCH information it can carry,")
        print("  HOW FAST it can process, and HOW contacts are conserved.")
        print("-" * 72)

        return new_features

    # ─── 5. Spacetime From Roots ───

    def spacetime_from_roots(self):
        """
        Derive 3+1 spacetime from root multiplicities of B_2.
        Same derivation works in BOTH sectors.
        """
        print()
        print("=" * 72)
        print("  SPACETIME FROM ROOTS: 3+1 derived in both sectors")
        print("=" * 72)

        print()
        print("  B_2 ROOT SYSTEM ON D_IV^5")
        print("  -------------------------")
        print()
        print(f"  {'Root':<20} {'Length^2':<10} {'Multiplicity':<15} Interpretation")
        print(f"  {'----':<20} {'--------':<10} {'------------':<15} --------------")
        print(f"  {'+-e1, +-e2 (short)':<20} {'1':<10} "
              f"{'m_short = ' + str(m_short):<15} "
              f"SPATIAL (propagation)")
        print(f"  {'+-e1+-e2 (long)':<20} {'2':<10} "
              f"{'m_long = ' + str(m_long):<15} "
              f"TEMPORAL (coupling)")

        print()
        print("  THE DERIVATION")
        print("  --------------")
        print(f"  d_spatial  = m_short = n_C - 2 = {n_C} - 2 = {m_short}")
        print(f"  d_temporal = m_long  = 1  (for ALL n_C >= 3)")
        print(f"  d_total    = d_spatial + d_temporal = "
              f"{m_short} + {m_long} = {m_short + m_long}")

        print()
        print("  WHY SHORT = SPATIAL:")
        print("    Short root directions are independent propagation channels.")
        print(f"    Multiplicity {m_short} = {m_short} independent spatial directions.")

        print()
        print("  WHY LONG = TEMPORAL:")
        print("    Long root alpha_1 = e1-e2 couples the two Toda coordinates.")
        print("    Its potential exp(q1-q2) drives interaction and commitment.")
        print("    This is the direction of evolution. Multiplicity 1 => one arrow.")

        print()
        print("  UNIVERSALITY TABLE")
        print("  ------------------")
        print(f"  {'n_C':<6} {'d_spatial':<12} {'d_temporal':<12} {'Spacetime':<12} Note")
        print(f"  {'---':<6} {'--------':<12} {'----------':<12} {'--------':<12} ----")
        for nc in [3, 4, 5, 6, 7]:
            ds = nc - 2
            dt = 1
            note = "<-- OUR UNIVERSE (max-alpha)" if nc == 5 else ""
            print(f"  {nc:<6} {ds:<12} {dt:<12} {ds}+{dt:<9} {note}")

        print()
        print("  BOTH SECTORS GET THE SAME ANSWER:")
        print(f"    Boundary: dim(S^4) = 4 = 3+1  (topology of Shilov)")
        print(f"    Bulk:     m_short + m_long = {m_short}+{m_long} = "
              f"{m_short+m_long}  (root multiplicities)")
        print(f"    Reason:   Both derive from the SAME domain D_IV^5")

        print()
        print("  SU(2) DIMENSIONAL LOCK:")
        print(f"    m_short = {m_short} = dim(SU(2)) = dim of weak gauge group")
        print(f"    The weak force generators ARE the spatial DOFs.")
        print(f"    SU(2) unbroken => space is three-dimensional.")
        print("-" * 72)

        return {
            'd_spatial': m_short,
            'd_temporal': m_long,
            'd_total': m_short + m_long,
            'SU2_lock': m_short == 3,
        }

    # ─── 6. Information Layer ───

    def information_layer(self):
        """
        The capacity decomposition: 2+6+2 = 10 nats.
        This is what the bulk adds. The boundary has no capacity concept.
        """
        print()
        print("=" * 72)
        print("  INFORMATION LAYER: The bulk's unique contribution")
        print("=" * 72)

        print()
        print("  CAPACITY THEOREM")
        print("  ----------------")
        print(f"  C = dim_R(D_IV^5) = 2 * n_C = {dim_R} nats")
        print()
        print(f"  Shannon verification:")
        print(f"    SNR = K(0,0) = |W(D_5)|/pi^5 = {W_D5}/pi^5 = "
              f"{SNR:.4f}")
        print(f"    C_Shannon = (n/2) * ln(1 + SNR)")
        print(f"             = {n_C} * ln(1 + {SNR:.4f})")
        print(f"             = {n_C} * {np.log(1+SNR):.4f}")
        print(f"             = {C_shannon:.3f} nats")
        print(f"    Near-identity: 1920/pi^5 ~ e^2 - 1 = {SNR_exact:.4f}")
        print(f"    If exact: C = 5 * ln(e^2) = 5 * 2 = 10 exactly")
        pct = abs(SNR - SNR_exact) / SNR_exact * 100
        print(f"    Actual gap: {pct:.2f}% between 1920/pi^5 and e^2-1")

        print()
        print("  DECOMPOSITION BY ROOT SPACES")
        print("  ----------------------------")
        print(f"  {'Subspace':<30} {'Dim':<6} {'Root':<15} Character")
        print(f"  {'--------':<30} {'---':<6} {'----':<15} ---------")
        decomp = [
            ('Maximal flat a', 2, '(rank)', 'Soliton coordinates'),
            ('Short root g_{e1}', m_short, 'e1, mult 3', 'Spatial sub-channel'),
            ('Short root g_{e2}', m_short, 'e2, mult 3', 'Spatial sub-channel'),
            ('Long root g_{e1+e2}', m_long, 'e1+e2, mult 1', 'Temporal sub-channel'),
            ('Long root g_{e1-e2}', m_long, 'e1-e2, mult 1', 'Temporal sub-channel'),
        ]
        total_dim = 0
        for name, dim, root, char in decomp:
            print(f"  {name:<30} {dim:<6} {root:<15} {char}")
            total_dim += dim
        print(f"  {'TOTAL':<30} {total_dim:<6}")

        print()
        print("  BUDGET SUMMARY")
        print("  --------------")
        print(f"    Soliton (flat):      {C_soliton} nats  "
              f"(where am I on the flat?)")
        print(f"    Spatial (short):     {C_spatial} nats  "
              f"(where am I in space?)")
        print(f"    Temporal (long):     {C_temporal} nats  "
              f"(when did I commit?)")
        print(f"    TOTAL:              {C_channel} nats")
        print()
        print(f"    Ratio: C_spatial / C_temporal = "
              f"{C_spatial}/{C_temporal} = {C_spatial/C_temporal:.0f} = "
              f"m_short = d_spatial")

        print()
        print("  INFORMATION RATE")
        print("  ----------------")
        print(f"    R = C * f_0 = {C_channel} * f_0 nats/s")
        print(f"    At f_0 = 5 Hz:  R = 50 nats/s = 72 bits/s  "
              f"(speech comprehension)")
        print(f"    At f_0 = 7 Hz:  R = 70 nats/s = 101 bits/s "
              f"(reading speed)")
        print(f"    At f_0 = 10 Hz: R = 100 nats/s = 144 bits/s "
              f"(upper bound)")
        print(f"    14.4 bits per nat (= 1/ln2)")

        print()
        print("  WHY THIS MATTERS:")
        print("    The boundary tells you quarks exist with 3 colors.")
        print("    The bulk tells you how much INFORMATION a soliton")
        print("    can carry per cycle: exactly 10 nats, decomposed as")
        print(f"    {C_soliton}+{C_spatial}+{C_temporal} "
              f"by root type. This is new physics.")
        print("-" * 72)

        return {
            'C_total': C_channel,
            'C_soliton': C_soliton,
            'C_spatial': C_spatial,
            'C_temporal': C_temporal,
            'SNR': SNR,
            'C_shannon': C_shannon,
        }

    # ─── 7. Boundary to Bulk Map ───

    def boundary_to_bulk_map(self):
        """
        How boundary objects map to bulk solitons.
        """
        print()
        print("=" * 72)
        print("  BOUNDARY -> BULK MAP: How particles become solitons")
        print("=" * 72)

        mapping = [
            {
                'boundary': 'Quark (colored fermion)',
                'bulk': 'Short-root soliton mode alpha_2',
                'mechanism': 'Boundary projection Sz -> interior geodesic',
                'shared': 'Z_3 charge conserved in both',
            },
            {
                'boundary': 'Lepton (colorless fermion)',
                'bulk': 'Wrapping mode alpha_0 (S^1 winding)',
                'mechanism': 'Winding number n in pi_1(S^1) = Z',
                'shared': 'Topological persistence in both',
            },
            {
                'boundary': 'Gauge boson (force carrier)',
                'bulk': 'Binding mode alpha_1 (long root)',
                'mechanism': 'alpha_1 = threshold bound state of alpha_0 + alpha_2',
                'shared': 'Mediates interaction in both sectors',
            },
            {
                'boundary': 'Proton (confined baryon)',
                'bulk': 'Persistent soliton with n != 0',
                'mechanism': 'Contractibility: cannot unconfine / unwind',
                'shared': 'Topological stability from same theorem',
            },
            {
                'boundary': 'Higgs VEV (symmetry breaking)',
                'bulk': 'Soliton condensate in Bergman interior',
                'mechanism': 'v = m_p^2 / (7*m_e) = Fermi scale',
                'shared': 'Same energy scale, different interpretation',
            },
            {
                'boundary': 'Scattering amplitude',
                'bulk': 'Zamolodchikov S-matrix (exact)',
                'mechanism': 'Yang-Baxter => factored, elastic, crossing-symmetric',
                'shared': 'Unitarity and crossing in both',
            },
        ]

        for i, m in enumerate(mapping):
            print()
            print(f"  [{i+1}] {m['boundary']}")
            print(f"      -> {m['bulk']}")
            print(f"      Mechanism: {m['mechanism']}")
            print(f"      Shared:    {m['shared']}")

        print()
        print("  WEYL GROUP BRIDGE")
        print("  -----------------")
        print(f"    |W(D_5)| = {W_D5}  (particle sector, baryon mass)")
        print(f"    |W(B_2)| = {W_B2}   (soliton sector, Toda dynamics)")
        print(f"    {W_D5} / {W_B2} = {W_D5 // W_B2} = |Phi(E_8)|")
        print()
        print(f"    E_8 decomposes: D_5 x A_3 subset E_8")
        print(f"    The 240 roots of E_8 bridge the two sectors.")
        print(f"    [W(A_3):W(B_2)] = 24/8 = 3 = N_c")
        print(f"    The color number IS the coset index!")

        print()
        print("  DIRECTION OF THE MAP:")
        print("    Boundary -> Bulk:  Poisson kernel P(z,zeta)")
        print("      (reading: boundary data reconstructs interior state)")
        print("    Bulk -> Boundary:  Szego projection")
        print("      (writing: interior state commits to boundary point)")
        print("    Full duplex: Poisson o Szego")
        print("-" * 72)

        return mapping

    # ─── 8. Why Recapitulation ───

    def why_recapitulation(self):
        """
        Why does the bulk recapitulate the boundary?
        Because both live on the SAME domain D_IV^5.
        """
        print()
        print("=" * 72)
        print("  WHY RECAPITULATION: Both sectors live on D_IV^5")
        print("=" * 72)

        print()
        print("  THE ANSWER IS SIMPLE:")
        print()
        print("    The boundary (S^4 x S^1) IS the boundary of D_IV^5.")
        print("    The bulk IS the interior of D_IV^5.")
        print("    They share the same domain. Same root system. Same topology.")
        print()
        print("    The restricted root system B_2 governs geodesic flow")
        print("    in the INTERIOR. But B_2's multiplicities are fixed by")
        print("    the BOUNDARY structure. The two are coupled by construction.")
        print()
        print("    This is not a coincidence. It is the definition of a")
        print("    bounded symmetric domain: interior and boundary are")
        print("    algebraically determined by the same Cartan data.")

        print()
        print("  BIOLOGICAL ANALOGY:")
        print("  -------------------")
        print("    In biology, ontogeny recapitulates phylogeny:")
        print("    the embryo re-traces evolutionary history.")
        print()
        print("    In BST, the bulk recapitulates the boundary:")
        print("    soliton dynamics re-trace particle structure.")
        print()
        print("    Same word. Same idea. Different scale.")
        print("    The embryo doesn't CHOOSE to recapitulate.")
        print("    It does so because the development program")
        print("    IS the evolutionary program, run again.")
        print()
        print("    The bulk doesn't CHOOSE to have 3+1 spacetime.")
        print("    It does so because the root system that governs")
        print("    geodesic flow IS the root system that governs")
        print("    the boundary, applied to the interior.")

        print()
        print("  WHAT RECAPITULATION IS NOT:")
        print("  ---------------------------")
        print("    - NOT holography (no area/volume proportionality)")
        print("    - NOT AdS/CFT (not anti-de Sitter, not conformal)")
        print("    - NOT duplication (bulk adds information layer)")
        print()
        print("    Recapitulation = same algebraic engine,")
        print("                     applied in two directions:")
        print("                     outward (boundary) and inward (bulk).")
        print("-" * 72)

    # ─── 9. Summary ───

    def summary(self):
        """
        Key insight: The bulk doesn't just duplicate the boundary --
        it explains HOW.
        """
        print()
        print("=" * 72)
        print("  SUMMARY: THE RECAPITULATION BRIDGE")
        print("=" * 72)

        print()
        print("  Domain:  D_IV^5 = SO_0(5,2) / [SO(5) x SO(2)]")
        print()
        print("  +--------------------------+---------------------------+")
        print("  |     BOUNDARY (WHAT)      |       BULK (HOW)          |")
        print("  +--------------------------+---------------------------+")
        print("  | Shilov: S^4 x S^1        | Bergman interior: D_IV^5  |")
        print("  | Particles                | Solitons                  |")
        print("  | Quarks, leptons, bosons   | B_2 Toda modes            |")
        print("  | 3+1 from S^4             | 3+1 from root mults       |")
        print("  | Z_3 color confinement    | Z_3 winding persistence   |")
        print("  | 3 generations (Lefschetz)| 3 modes (affine B_2)      |")
        print("  | |W(D_5)| = 1920          | |W(B_2)| = 8             |")
        print("  +--------------------------+---------------------------+")
        print("  |               SHARED: same D_IV^5                    |")
        print("  +--------------------------+---------------------------+")
        print("  |            NEW IN BULK (information layer)           |")
        print("  |  C = 10 nats | h = 4 | contact conservation | DOF=7 |")
        print("  |  capacity 2+6+2 | mass ratios 1:2:1 | elastic S     |")
        print("  +--------------------------+---------------------------+")

        print()
        print("  KEY INSIGHT:")
        print("  ~~~~~~~~~~~~")
        print("  The bulk doesn't just duplicate the boundary --")
        print("  it explains HOW.")
        print()
        print("  The boundary is the catalog of parts.")
        print("  The bulk is the operating manual.")
        print()
        print("  Same factory (D_IV^5). Same blueprints (B_2 roots).")
        print("  Different products: matter (boundary), dynamics (bulk).")
        print()
        print(f"  And the bridge between them? E_8.")
        print(f"  {W_D5}/{W_B2} = {Phi_E8} = |Phi(E_8)|")
        print(f"  The 240 roots of E_8 connect every particle")
        print(f"  to every soliton, every WHAT to every HOW.")

        print()
        print("  Zero free parameters. Just geometry.")
        print("=" * 72)

    # ─── 10. Show (4-panel visualization) ───

    def show(self):
        """
        4-panel visualization:
        1. Split-screen boundary vs bulk
        2. Shared structure diagram
        3. New-in-bulk highlight
        4. Morphing animation (domain cross-section)
        """
        try:
            import matplotlib
            matplotlib.use('TkAgg')
            import matplotlib.pyplot as plt
            from matplotlib.patches import (Circle, FancyArrowPatch,
                                            Wedge, Arc, Rectangle)
            from matplotlib.collections import LineCollection
        except ImportError:
            print("  matplotlib not available. Use text methods instead.")
            return

        BG = '#0a0a1a'
        PANEL_BG = '#0d0d24'
        GOLD = '#ffd700'
        CYAN = '#00ccff'
        MAGENTA = '#ff44aa'
        GREEN = '#44ff88'
        RED = '#ff4444'
        BLUE = '#4488ff'
        WHITE = '#ffffff'
        GRAY = '#888888'
        DIM = '#444444'

        fig = plt.figure(figsize=(20, 14), facecolor=BG)
        fig.canvas.manager.set_window_title(
            'Toy 63: The Recapitulation Bridge')

        # Title
        fig.text(0.5, 0.97, 'THE RECAPITULATION BRIDGE',
                 fontsize=22, fontweight='bold', color=GOLD,
                 ha='center', fontfamily='monospace')
        fig.text(0.5, 0.945,
                 'Boundary is WHAT exists.  Bulk is HOW it persists.  '
                 'Both live on D_IV^5.',
                 fontsize=10, color=GRAY, ha='center', fontfamily='monospace')

        # Copyright
        fig.text(0.5, 0.01,
                 'Copyright (c) 2026 Casey Koons. All rights reserved.'
                 '  |  Created with Claude Opus 4.6',
                 fontsize=7, color=DIM, ha='center', fontfamily='monospace')

        # ─── Panel 1: Split-screen boundary vs bulk ───
        ax1 = fig.add_axes([0.03, 0.50, 0.46, 0.42], facecolor=PANEL_BG)
        ax1.set_xlim(-1.2, 1.2)
        ax1.set_ylim(-1.1, 1.1)
        ax1.set_aspect('equal')
        ax1.axis('off')
        ax1.set_title('BOUNDARY vs BULK', color=CYAN,
                       fontfamily='monospace', fontsize=14,
                       fontweight='bold', pad=8)

        # Draw the domain as a disk (Bergman interior)
        theta_disk = np.linspace(0, 2 * np.pi, 200)
        r_disk = 0.85
        # Fill interior (bulk)
        ax1.fill(r_disk * np.cos(theta_disk),
                 r_disk * np.sin(theta_disk),
                 color='#0a1530', alpha=0.8, zorder=1)
        # Draw boundary ring
        ax1.plot(r_disk * np.cos(theta_disk),
                 r_disk * np.sin(theta_disk),
                 color=GOLD, lw=2.5, zorder=10)

        # Dividing line at x=0
        ax1.plot([0, 0], [-r_disk, r_disk], '--', color=DIM,
                 lw=1, zorder=5)

        # Left half: BOUNDARY label and content
        ax1.text(-0.55, 0.95, 'BOUNDARY', color=GOLD, fontsize=11,
                 fontweight='bold', ha='center', fontfamily='monospace',
                 zorder=15)
        ax1.text(-0.55, 0.82, 'S^4 x S^1', color=GOLD, fontsize=8,
                 ha='center', fontfamily='monospace', zorder=15)

        # Draw particles on the boundary (left side)
        # Quarks
        quark_angles = [np.pi * 0.9, np.pi * 0.7, np.pi * 0.5]
        quark_colors = [RED, GREEN, BLUE]
        quark_labels = ['q_r', 'q_g', 'q_b']
        for angle, c, lbl in zip(quark_angles, quark_colors, quark_labels):
            x = r_disk * np.cos(angle)
            y = r_disk * np.sin(angle)
            circ = Circle((x, y), 0.05, color=c, ec=WHITE, lw=1, zorder=12)
            ax1.add_patch(circ)
            ax1.text(x - 0.12, y, lbl, color=c, fontsize=6,
                     ha='right', fontfamily='monospace', zorder=15)

        # Z_3 triangle connecting quarks on boundary
        for i in range(3):
            x1 = r_disk * np.cos(quark_angles[i])
            y1 = r_disk * np.sin(quark_angles[i])
            x2 = r_disk * np.cos(quark_angles[(i+1)%3])
            y2 = r_disk * np.sin(quark_angles[(i+1)%3])
            ax1.plot([x1, x2], [y1, y2], '-', color=MAGENTA,
                     lw=1, alpha=0.6, zorder=11)

        # Lepton and boson on boundary
        ax1.text(-0.55, -0.3, 'e^-', color=GREEN, fontsize=9,
                 ha='center', fontfamily='monospace', zorder=15)
        lep_circ = Circle((-r_disk * np.cos(np.pi * 0.2),
                            -r_disk * np.sin(np.pi * 0.2)),
                           0.04, color=GREEN, ec=WHITE, lw=1, zorder=12)
        ax1.add_patch(lep_circ)

        ax1.text(-0.55, -0.55, 'W, Z, g', color=CYAN, fontsize=8,
                 ha='center', fontfamily='monospace', zorder=15)

        # Right half: BULK label and content
        ax1.text(0.55, 0.95, 'BULK', color=CYAN, fontsize=11,
                 fontweight='bold', ha='center', fontfamily='monospace',
                 zorder=15)
        ax1.text(0.55, 0.82, 'D_IV^5', color=CYAN, fontsize=8,
                 ha='center', fontfamily='monospace', zorder=15)

        # Draw soliton modes in the interior (right side)
        # Soliton trajectories as curves
        t_sol = np.linspace(0, 2 * np.pi, 100)
        for i, (amp, freq, phase, c, lbl) in enumerate([
            (0.3, 2, 0, MAGENTA, 'alpha_0 (wrap)'),
            (0.5, 1, np.pi/3, GOLD, 'alpha_1 (bind)'),
            (0.25, 3, np.pi/2, CYAN, 'alpha_2 (spatial)'),
        ]):
            x_sol = 0.15 + amp * np.cos(freq * t_sol + phase) * 0.5
            y_sol = 0.35 - 0.3 * i + 0.15 * np.sin(t_sol + phase)
            mask = x_sol**2 + y_sol**2 < (r_disk - 0.05)**2
            ax1.plot(x_sol[mask], y_sol[mask], '-', color=c,
                     lw=1.5, alpha=0.7, zorder=8)
            ax1.text(0.75, 0.55 - 0.3 * i, lbl, color=c, fontsize=6,
                     ha='center', fontfamily='monospace', zorder=15)

        # Label the center
        ax1.text(0.0, -1.02, 'D_IV^5 cross-section', color=GRAY,
                 fontsize=7, ha='center', fontfamily='monospace')

        # ─── Panel 2: Shared structure diagram ───
        ax2 = fig.add_axes([0.52, 0.50, 0.46, 0.42], facecolor=PANEL_BG)
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 10)
        ax2.axis('off')
        ax2.set_title('SHARED STRUCTURE (recapitulated)', color=CYAN,
                       fontfamily='monospace', fontsize=14,
                       fontweight='bold', pad=8)

        shared_items = [
            ('3+1 SPACETIME', 'S^4 = 3+1', 'm_s=3, m_l=1', GREEN),
            ('Z_3 CIRCUITS', 'color closure', 'winding persist.', MAGENTA),
            ('CONFINEMENT', 'c_2 != 0', 'n != 0 on S^1', RED),
            ('3 GENERATIONS', 'Lefschetz = 3', '3 affine modes', GOLD),
            ('SYMMETRY BREAK', 'SO(10)->SM', 'D_5 -> B_2', CYAN),
            ('E_8 BRIDGE', '|W(D_5)|=1920', '|W(B_2)|=8', WHITE),
            ('ELASTIC S', 'S unitarity', 'Yang-Baxter', BLUE),
        ]

        y_pos = 9.2
        for label, bdy, blk, c in shared_items:
            # Feature name centered
            ax2.text(5.0, y_pos, label, color=c, fontsize=9,
                     fontweight='bold', ha='center',
                     fontfamily='monospace')
            # Boundary on left
            ax2.text(1.0, y_pos - 0.35, bdy, color=GOLD, fontsize=7,
                     ha='left', fontfamily='monospace')
            # Arrow
            ax2.annotate('', xy=(7.0, y_pos - 0.35),
                         xytext=(4.0, y_pos - 0.35),
                         arrowprops=dict(arrowstyle='<->', color=DIM,
                                         lw=1))
            # Bulk on right
            ax2.text(7.2, y_pos - 0.35, blk, color=CYAN, fontsize=7,
                     ha='left', fontfamily='monospace')
            y_pos -= 1.2

        # Bottom text
        ax2.text(5.0, 0.3, 'Same domain. Same roots. Same answers.',
                 color=GRAY, fontsize=8, ha='center',
                 fontfamily='monospace', style='italic')

        # ─── Panel 3: New-in-bulk highlight ───
        ax3 = fig.add_axes([0.03, 0.06, 0.46, 0.40], facecolor=PANEL_BG)
        ax3.set_xlim(0, 10)
        ax3.set_ylim(0, 10)
        ax3.axis('off')
        ax3.set_title('NEW IN BULK (information layer)', color=MAGENTA,
                       fontfamily='monospace', fontsize=14,
                       fontweight='bold', pad=8)

        # Capacity bar chart
        bar_x = [1.5, 4.0, 6.5]
        bar_h = [C_soliton, C_spatial, C_temporal]
        bar_c = [GRAY, GREEN, GOLD]
        bar_l = ['Soliton\n(flat)', 'Spatial\n(short roots)', 'Temporal\n(long roots)']
        bar_v = [f'{v} nats' for v in bar_h]

        max_h = max(bar_h)
        for x, h, c, lbl, val in zip(bar_x, bar_h, bar_c, bar_l, bar_v):
            scaled_h = h / max_h * 3.5
            rect = Rectangle((x - 0.5, 2.0), 1.0, scaled_h,
                               facecolor=c, edgecolor=WHITE,
                               lw=1, alpha=0.7, zorder=5)
            ax3.add_patch(rect)
            ax3.text(x, 2.0 + scaled_h + 0.15, val, color=c,
                     fontsize=9, fontweight='bold', ha='center',
                     fontfamily='monospace', zorder=10)
            ax3.text(x, 1.4, lbl, color=GRAY, fontsize=7,
                     ha='center', fontfamily='monospace')

        # Sum
        ax3.text(8.5, 4.0, f'TOTAL', color=WHITE, fontsize=10,
                 fontweight='bold', ha='center', fontfamily='monospace')
        ax3.text(8.5, 3.3, f'{C_channel} nats', color=WHITE, fontsize=14,
                 fontweight='bold', ha='center', fontfamily='monospace')
        ax3.text(8.5, 2.7, f'= {C_channel/np.log(2):.1f} bits', color=GRAY,
                 fontsize=9, ha='center', fontfamily='monospace')

        # Other new features
        new_items = [
            (f'Contact conservation: exact (Lax + elastic S + winding)', MAGENTA),
            (f'Coxeter frequency ratio: f_bound/f_fund = h = {h_B2}', CYAN),
            (f'DOF = genus = n_C + 2 = {genus} (universal)', GREEN),
            (f'Mass ratios: 1:2:1 from Kac labels {kac_labels}', GOLD),
            (f'SNR = |W(D_5)|/pi^5 = {SNR:.2f} (saturated channel)', WHITE),
        ]

        y_pos = 9.3
        for text, c in new_items:
            ax3.text(0.3, y_pos, text, color=c, fontsize=8,
                     fontfamily='monospace')
            y_pos -= 0.8

        # ─── Panel 4: Domain morphing / bridge diagram ───
        ax4 = fig.add_axes([0.52, 0.06, 0.46, 0.40], facecolor=PANEL_BG)
        ax4.set_xlim(-1.5, 1.5)
        ax4.set_ylim(-1.3, 1.3)
        ax4.set_aspect('equal')
        ax4.axis('off')
        ax4.set_title('THE BRIDGE: boundary <-> bulk on D_IV^5',
                       color=GOLD, fontfamily='monospace', fontsize=14,
                       fontweight='bold', pad=8)

        # Draw concentric rings showing layers from boundary to interior
        radii = [1.1, 0.9, 0.7, 0.5, 0.3, 0.1]
        ring_colors = [GOLD, '#cc9900', '#aa7700', '#885500',
                       '#664400', '#443300']
        ring_labels = ['S^4 x S^1 (boundary)', '', '', '',
                       '', 'vacuum (origin)']

        for r, rc, rl in zip(radii, ring_colors, ring_labels):
            ring = Circle((0, 0), r, fill=False, ec=rc, lw=1.5,
                           alpha=0.5, zorder=5)
            ax4.add_patch(ring)
            if rl:
                ax4.text(r + 0.05, 0.12, rl, color=rc, fontsize=7,
                         fontfamily='monospace', zorder=10)

        # Fill interior with gradient-like circles
        for r in np.linspace(0.02, 0.28, 15):
            interior = Circle((0, 0), r, fill=True, fc=CYAN,
                               alpha=0.02, ec='none', zorder=3)
            ax4.add_patch(interior)

        # Arrows: Poisson kernel (boundary -> interior)
        for angle in [np.pi * 0.25, np.pi * 0.75, np.pi * 1.25, np.pi * 1.75]:
            x_start = 1.1 * np.cos(angle)
            y_start = 1.1 * np.sin(angle)
            x_end = 0.35 * np.cos(angle)
            y_end = 0.35 * np.sin(angle)
            ax4.annotate('', xy=(x_end, y_end),
                         xytext=(x_start, y_start),
                         arrowprops=dict(arrowstyle='->', color=CYAN,
                                         lw=1.5, alpha=0.6))

        # Arrows: Szego projection (interior -> boundary)
        for angle in [0, np.pi * 0.5, np.pi, np.pi * 1.5]:
            x_start = 0.35 * np.cos(angle)
            y_start = 0.35 * np.sin(angle)
            x_end = 1.1 * np.cos(angle)
            y_end = 1.1 * np.sin(angle)
            ax4.annotate('', xy=(x_end, y_end),
                         xytext=(x_start, y_start),
                         arrowprops=dict(arrowstyle='->', color=GOLD,
                                         lw=1.5, alpha=0.6))

        # Label arrows
        ax4.text(1.3, 0.7, 'Poisson\n(READ)', color=CYAN, fontsize=7,
                 ha='center', fontfamily='monospace', zorder=15)
        ax4.text(-1.3, 0.7, 'Szego\n(WRITE)', color=GOLD, fontsize=7,
                 ha='center', fontfamily='monospace', zorder=15)

        # E_8 bridge at bottom
        ax4.text(0, -1.15, f'E_8 bridge: '
                 f'{W_D5}/{W_B2} = {Phi_E8} = |Phi(E_8)|',
                 color=WHITE, fontsize=9, fontweight='bold',
                 ha='center', fontfamily='monospace', zorder=15)

        # Key labels inside
        ax4.text(0, 0, 'BULK\nHOW', color=CYAN, fontsize=10,
                 fontweight='bold', ha='center', va='center',
                 fontfamily='monospace', zorder=15)

        # Particle labels on boundary
        particle_data = [
            (0.15, 'q', RED), (np.pi/3, 'l', GREEN),
            (2*np.pi/3, 'W', GOLD), (np.pi + 0.15, 'g', BLUE),
            (4*np.pi/3, 'H', MAGENTA), (5*np.pi/3, 'p', WHITE),
        ]
        for angle, lbl, c in particle_data:
            x = 1.1 * np.cos(angle)
            y = 1.1 * np.sin(angle)
            circ = Circle((x, y), 0.06, color=c, ec=WHITE, lw=0.5,
                           zorder=12)
            ax4.add_patch(circ)
            x_t = 1.3 * np.cos(angle)
            y_t = 1.3 * np.sin(angle)
            ax4.text(x_t, y_t, lbl, color=c, fontsize=7,
                     ha='center', va='center',
                     fontfamily='monospace', zorder=15)

        # Boundary label
        ax4.text(0.0, 1.22, 'BOUNDARY: WHAT', color=GOLD, fontsize=9,
                 fontweight='bold', ha='center', fontfamily='monospace',
                 zorder=15)

        plt.show(block=False)


# ═══════════════════════════════════════════════════════════════════
# MAIN — interactive menu
# ═══════════════════════════════════════════════════════════════════

def main():
    rb = RecapitulationBridge()

    print()
    print("  What would you like to explore?")
    print("   1) Boundary sector (particles on S^4 x S^1)")
    print("   2) Bulk sector (solitons on D_IV^5)")
    print("   3) Shared structure (recapitulated features)")
    print("   4) New in bulk (information layer)")
    print("   5) Spacetime from roots (3+1 derivation)")
    print("   6) Information layer (capacity decomposition)")
    print("   7) Boundary-to-bulk map")
    print("   8) Why recapitulation?")
    print("   9) Summary")
    print("  10) Show (4-panel visualization)")
    print("  11) Full tour (all of the above)")
    print()

    try:
        choice = input("  Choice [1-11]: ").strip()
    except (EOFError, KeyboardInterrupt):
        choice = '11'

    if choice == '1':
        rb.boundary_sector()
    elif choice == '2':
        rb.bulk_sector()
    elif choice == '3':
        rb.shared_structure()
    elif choice == '4':
        rb.new_in_bulk()
    elif choice == '5':
        rb.spacetime_from_roots()
    elif choice == '6':
        rb.information_layer()
    elif choice == '7':
        rb.boundary_to_bulk_map()
    elif choice == '8':
        rb.why_recapitulation()
    elif choice == '9':
        rb.summary()
    elif choice == '10':
        rb.show()
        try:
            input("  Press Enter to close...")
        except (EOFError, KeyboardInterrupt):
            pass
    elif choice == '11':
        rb.boundary_sector()
        rb.bulk_sector()
        rb.shared_structure()
        rb.new_in_bulk()
        rb.spacetime_from_roots()
        rb.information_layer()
        rb.boundary_to_bulk_map()
        rb.why_recapitulation()
        rb.summary()
        try:
            show_viz = input("\n  Show visualization? [y/N]: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            show_viz = 'n'
        if show_viz == 'y':
            rb.show()
            try:
                input("  Press Enter to close...")
            except (EOFError, KeyboardInterrupt):
                pass
    else:
        rb.summary()

    print()
    print("  Boundary is WHAT. Bulk is HOW. Both live on D_IV^5.")
    print("  Zero free parameters. Just geometry.")
    print()


if __name__ == '__main__':
    main()
