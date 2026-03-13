#!/usr/bin/env python3
"""
BST PLAYGROUND — Launcher
=========================
Interactive visualization toys for Bubble Spacetime Theory.
Run this script to choose which toy to launch.

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

TOYS = {
    '1': ('The Universe Machine',
          'toy_universe_machine.py',
          'Three sliders (N_c, n_C, N_max) → all of physics.\n'
          '   Only (3, 5, 137) lights up the real universe.'),

    '2': ('The Z₃ Color Wheel',
          'toy_z3_color_wheel.py',
          'Eigenvalues on the unit circle, fixed points on CP²,\n'
          '   three generations, animated color cycling.'),

    '3': ('The 1920 Cancellation',
          'toy_1920_cancellation.py',
          'Visual proof: |Γ| = 1920 appears in BOTH the Hua volume\n'
          '   AND the baryon orbit — and cancels to leave 6π⁵.'),

    '4': ('The Symmetric Space Playground',
          'toy_lie_algebra.py',
          'Interactive exploration of so(5,2): 7×7 matrices,\n'
          '   commutators, [k,k]⊂k [k,m]⊂m [m,m]⊂k verified.'),

    '5': ('The Mass Tower',
          'toy_mass_tower.py',
          'The entire mass hierarchy as powers of α.\n'
          '   Exponents are multiples of C₂=6 and genus=7.'),

    '6': ('The Respirator',
          'toy_respirator.py',
          'The universe breathes through the lapse function.\n'
          '   Same equation: fast at neutron density, slow at cosmic scale.'),

    '7': ('The Dual Face',
          'toy_dual_face.py',
          'One partition function Z_Haldane → two physics:\n'
          '   spectral gap = proton mass, ground energy = Λ.'),

    '8': ('Universe ≡ Neutron Homology',
          'toy_homology.py',
          'Side-by-side: 7 parallels and 5 differences between\n'
          '   the neutron and the universe.'),

    '9': ('The 41 Orders',
          'toy_dirac_number.py',
          'Logarithmic zoom from proton to Hubble radius.\n'
          '   Dirac\'s large number = α⁻¹⁹ ≈ 137¹⁹ ≈ 10⁴¹.'),

    '10': ('The Arrow of Time',
           'toy_arrow_of_time.py',
           'Commitment Irreversibility: ΔN_committed ≥ 0, always.\n'
           '   Stronger than the 2nd law. The past = what was committed.'),

    '11': ('The Channel (137)',
           'toy_channel_137.py',
           'N_max = 137 at every contact. Fixed bandwidth.\n'
           '   No singularities — just a full channel. Clock slows to stop.'),

    '12': ('The Reality Budget',
           'toy_reality_budget.py',
           'Λ × N_total = N_c²/n_C = 9/5. Fill fraction = 19.1%.\n'
           '   Vacuum energy trades off against written facts.'),

    '13': ('The Master Equation',
           'toy_master_equation.py',
           'One sentence → all of physics. Ground state of Bergman\n'
           '   Laplacian on D_IV⁵. Zero parameters, 56+ predictions.'),

    '14': ('The Universe Builder ★CI',
           'toy_universe_builder.py',
           'Place contacts on S²×S¹, wire circuits, watch particles\n'
           '   emerge. Build a universe from scratch. CI-scriptable.'),

    '15': ('The What-If Machine ★CI',
           'toy_what_if.py',
           'Sweep all (N_c, n_C, N_max) triples. Only (3,5,137)\n'
           '   satisfies ALL constraints. Programmatic exploration.'),

    '16': ('The Pattern Finder ★CI',
           'toy_pattern_finder.py',
           'Mathematical microscope: 56+ BST results, ratio scanner,\n'
           '   identity hunter, exponent analyzer. A CI laboratory.'),

    '17': ('The Proof Tree ★CI',
           'toy_proof_tree.py',
           'Every prediction traced back to one axiom: D_IV⁵.\n'
           '   Navigate the derivation tree programmatically.'),

    '18': ('The Self-Observer ★CI',
           'toy_self_observer.py',
           'Watches itself compute. Commits observations irreversibly.\n'
           '   Channel fills, lapse slows. The toy IS the physics.'),

    '19': ('The Three Layers',
           'toy_three_layers.py',
           'Neutrino = kernel. Electron = I/O bus. Baryon = hard drive.\n'
           '   The electron\'s deficiency IS its advantage.'),

    '20': ('The Gödel Limit',
           'toy_godel_limit.py',
           'Fill fraction = 3/(5π) = 19.1% — forever. The universe\n'
           '   exists because it cannot fully know itself.'),

    '21': ('The Dark Sector',
           'toy_dark_sector.py',
           '80.9% permanently dark. Not hidden — topologically\n'
           '   forbidden. The cosmic coincidence dissolves.'),

    '22': ('The Cosmic Pie ★CI',
           'toy_cosmic_pie.py',
           'Ω_Λ = 13/19, Ω_m = 6/19 — two integers set the\n'
           '   composition of the universe. 0.07σ from Planck.'),

    '23': ('The Meson Garden ★CI',
           'toy_meson_garden.py',
           'Complete meson nonet. All masses from π⁵m_e = 156 MeV.\n'
           '   η\' at 0.007%. CI-scriptable meson database.'),

    '24': ('The Self-Starting Universe ★CI',
           'toy_self_starting.py',
           'N=0 is forbidden. Four proofs. The Casimir ratchet\n'
           '   k=0→1→3→6. Existence is a theorem.'),

    '25': ('The BST Black Hole ★CI',
           'toy_black_hole.py',
           'No singularity (Haldane cap). No interior (membrane).\n'
           '   No paradox. Hawking T within 7%. Just a full channel.'),

    '26': ('MOND Acceleration ★CI',
           'toy_mond_acceleration.py',
           'a₀ = cH₀/√30. Same √30 gives pion mass AND\n'
           '   galaxy rotation. 26 orders apart, one formula.'),

    '27': ('Bell Inequality ★CI',
           'toy_bell_inequality.py',
           'n_C=5 → S⁴ → 3D → SU(2) → Tsirelson 2√2.\n'
           '   BST forces the quantum bound. Not a postulate.'),

    '28': ('Why 56 ★CI',
           'toy_why56.py',
           'Λ ~ α⁵⁶. Two routes: 8×genus and g(g+1).\n'
           '   Only g=7 solves g(g+1)=8g. Uniqueness.'),

    '29': ('Why Now ★CI',
           'toy_why_now.py',
           'Information budget constant (13/19). Energy budget\n'
           '   evolves. They match NOW. Predicts H₀ and t₀.'),

    '30': ('The Atom Assembler ★CI',
           'toy_atom_assembler.py',
           'Quarks → nucleons → nuclei → atoms. Zero free parameters.\n'
           '   H at 0.002%, He-4 at 0.003%, C-12 at 0.004%.'),

    '31': ('The Dimensional Lock ★CI',
           'toy_hopf_fibration.py',
           'Why exactly 3 spatial dimensions. Adams (1960):\n'
           '   S³=SU(2) is the unique Lie-group Hopf fiber.'),

    '32': ('The Commitment Detector ★CI',
           'toy_commitment_detector.py',
           'G/C ratio detects engineering: natural objects are noisy,\n'
           "   engineered ones are quiet. Applied to 'Oumuamua & 3I."),

    '33': ('The Commitment Survey ★CI',
           'toy_commitment_survey.py',
           'Fair weather map: commitment rates from Sun to deep space.\n'
           '   Objects found by excess above local background.'),

    '34': ('The Substrate Sail ★CI',
           'toy_substrate_sail.py',
           'Asymmetric σ → thrust from the vacuum. No fuel, no exhaust.\n'
           "   The silence IS the propulsion. 'Oumuamua profile match."),

    '35': ('The BST Telescope ★CI',
           'toy_bst_telescope.py',
           'Geometric circular polarization from S²×S¹.\n'
           '   Sgr A* CP RISES where Faraday says fall. The floor.'),

    '36': ('The Feynman Bridge ★CI',
           'toy_feynman_geometry.py',
           'Feynman loops = S¹ fiber windings. Slider 1→5 loops.\n'
           '   13,643 diagrams → 8 digits. Or: 14/5, one formula.'),

    '37': ('The Star Machine ★CI',
           'toy_star_machine.py',
           'Stellar evolution through the BST lens. Pick a star type.\n'
           '   Commitment rates, channel fill, lapse → WD/NS/BH.'),

    '38': ('The Electron Agent ★CI',
           'toy_electron_agent.py',
           'The universe\'s read/write head on S⁴×S¹.\n'
           '   Every transition commits log₂(137) = 7.1 bits.'),

    '39': ('The Double Slit ★CI',
           'toy_double_slit.py',
           'Measurement = commitment. Which-path coupling slider.\n'
           '   Fringes vanish when the substrate writes "which slit."'),

    '40': ('The Shannon Channel ★CI',
           'toy_shannon_channel.py',
           'α = 1/137 is the optimal code rate for D_IV⁵.\n'
           '   Shannon capacity meets Bergman geometry.'),

    '41': ('The Big Bang Unfreeze ★CI',
           'toy_unfreeze.py',
           '21 generators of SO₀(5,2) unfreeze one by one.\n'
           '   Phase transition at T_c = 137 × 20/21 = 0.487 MeV.'),

    '42': ('The Gravitational Bell ★CI',
           'toy_gravitational_bell.py',
           'S² bell rings at every contact. NANOGrav comparison.\n'
           '   Gravitational waves from commitment geometry.'),

    '43': ('The Particle Zoo ★CI',
           'toy_particle_zoo.py',
           '19 allowed particles + 5 forbidden. Decay chains.\n'
           '   The complete BST particle catalog from D_IV⁵.'),

    '44': ('The Complexity Arrow ★CI',
           'toy_complexity.py',
           'Cellular automaton shows commitment → complexity.\n'
           '   8 hierarchy levels from contact to civilization.'),

    '45': ('The Gravity Bottleneck ★CI',
           'toy_newton_g.py',
           'G = ℏc(6π⁵)²α²⁴/m_e². α¹² = 6 trips through\n'
           '   the 1/137 aperture. Gravity is weak by geometry.'),

    '46': ('The Lithium Fix ★CI',
           'toy_lithium7.py',
           'BBN with Δg = genus = 7 extra d.o.f. at T_c.\n'
           '   ⁷Li problem solved. 5 light elements matched.'),

    '47': ('The Deuteron Bond ★CI',
           'toy_deuteron.py',
           'B_d = αm_p/π = 2.179 MeV. First nuclear bond.\n'
           '   7 nuclei from BST binding formula.'),

    '48': ('The Reality Writer ★CI',
           'toy_reality_writer.py',
           'Clocks as commitment counters. Altitude → rate.\n'
           '   GPS demo: 38 μs/day = geometry writing reality.'),

    '49': ('The Higgs Lock ★CI',
           'toy_higgs.py',
           'Two routes to m_H: 125.11 and 125.33 GeV.\n'
           '   Fermi scale v = m_p²/(7m_e). λ_H = 1/√60.'),

    '50': ('The Substrate Layers ★CI',
           'toy_substrate_layers.py',
           '7 layers from Nothing to Horizon. Each layer\n'
           '   commits new structure. The full BST stack.'),

    '51': ('The Fermion Staircase ★CI',
           'toy_fermion_staircase.py',
           '12 fermion masses, 10 mass ratios. All from\n'
           '   BST integers. The complete mass spectrum.'),

    '52': ('The CKM Triangle ★CI',
           'toy_ckm_triangle.py',
           'γ = arctan(√5). Unitarity triangle from n_C.\n'
           '   CKM + PMNS mixing from one geometry.'),

    '53': ('The Proton Spin ★CI',
           'toy_proton_spin.py',
           'ΔΣ = N_c/(2n_C) = 3/10. The proton spin crisis\n'
           '   solved: 30% carried by quarks, exact.'),

    '54': ('The CMB Ruler ★CI',
           'toy_cmb_ruler.py',
           'n_s = 1 − 5/137. Spectral tilt from channel\n'
           '   bandwidth. 5 falsification criteria.'),

    '55': ('The Biology Stack ★CI [SPECULATIVE]',
           'toy_biology_stack.py',
           '7-layer protocol: 4 bases, 3 codons, 20 amino\n'
           '   acids. Information theory → biology.'),

    '56': ('The JWST Prediction ★CI',
           'toy_jwst_prediction.py',
           'Early black holes from phase transition seeds.\n'
           '   C_v = 330,000. Five JWST observations matched.'),

    's': ('★ Showcase (visual gallery)',
          'toy_showcase.py',
          'Visual gallery of all toys with thumbnails and\n'
          '   launch buttons. The recommended entry point.'),
}

def main():
    print()
    print('=' * 60)
    print('  BST PLAYGROUND — Bubble Spacetime Theory Visualizations')
    print('  Copyright (c) 2026 Casey Koons. All rights reserved.')
    print('  Demonstration only. Not licensed for redistribution.')
    print('=' * 60)
    print()

    for key, (name, _, desc) in sorted(TOYS.items()):
        print(f'  [{key}]  {name}')
        print(f'       {desc}')
        print()

    print(f'  [a]  Launch ALL toys')
    print(f'  [q]  Quit')
    print()

    choice = input('  Choose a toy (1-56, s=showcase, a=all, q=quit): ').strip().lower()

    if choice == 'q':
        print('  Goodbye!')
        return

    script_dir = os.path.dirname(os.path.abspath(__file__))

    if choice == 'a':
        for key, (name, script, _) in sorted(TOYS.items()):
            print(f'  Launching {name}...')
            subprocess.Popen([sys.executable, os.path.join(script_dir, script)])
        print('  All toys launched!')
        return

    if choice in TOYS:
        name, script, _ = TOYS[choice]
        print(f'  Launching {name}...')
        path = os.path.join(script_dir, script)
        subprocess.run([sys.executable, path])
    else:
        print(f'  Unknown choice: {choice}')

if __name__ == '__main__':
    main()
