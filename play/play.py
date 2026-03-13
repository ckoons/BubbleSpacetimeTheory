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

    choice = input('  Choose a toy (1-23, s=showcase, a=all, q=quit): ').strip().lower()

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
