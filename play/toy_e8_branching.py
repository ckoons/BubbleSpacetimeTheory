#!/usr/bin/env python3
"""
THE E8 BRANCHING COMPARE  --  Toy 93
=====================================
Two valid routes through E8 to three generations of fermions.

Route A: E8 -> D5 x A3 = SO(10) x SU(4)
  BST standard. Contains the soliton sector B2 inside A3.
  248 = (45,1) + (1,15) + (10,6) + (16,4) + (16b,4b)
  Three generations from [W(A3):W(B2)] = 24/8 = 3.

Route B: E8 -> E6 x SU(3)
  Cleaner generations but hides B2.
  248 = (78,1) + (1,8) + (27,3) + (27b,3b)
  Three generations from dim(fund SU(3)) = 3.

Both converge at SO(10) x SU(3)_family x U(1).

CI Interface:
    from toy_e8_branching import E8Branching
    eb = E8Branching()
    eb.route_a()                # E8 -> D5 x A3 decomposition
    eb.route_b()                # E8 -> E6 x SU(3) decomposition
    eb.convergence()            # Both routes -> SO(10) x SU(3)_fam x U(1)
    eb.generation_comparison()  # How each route gives 3 generations
    eb.soliton_visibility()     # Route A shows B2; Route B hides it
    eb.peccei_quinn()           # Barr's PQ uniquely selects SU(3)_fam
    eb.heterotic_connection()   # Route A = non-standard, Route B = standard
    eb.advantages_table()       # Side-by-side comparison
    eb.summary()                # Twin decompositions of one algebra
    eb.show()                   # 4-panel visualization

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
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
from matplotlib.gridspec import GridSpec

# ──────────────────────────────────────────────────────────────────
#  BST Constants
# ──────────────────────────────────────────────────────────────────
N_c   = 3           # color charges
n_C   = 5           # complex dimension of D_IV^5
C_2   = n_C + 1     # 6  Casimir eigenvalue C_2(pi_6)
genus = n_C + 2     # 7  genus of D_IV^5
N_max = 137         # channel capacity
alpha = 1.0 / 137.035999

# Weyl groups
W_D5 = math.factorial(5) * 2**4          # |W(D_5)| = 1920
W_A3 = math.factorial(4)                 # |W(A_3)| = 24
W_B2 = math.factorial(2) * 2**2          # |W(B_2)| = 8
N_gen = W_A3 // W_B2                     # 24/8 = 3
E8_ROOTS = W_D5 // W_B2                  # 1920/8 = 240

# ──────────────────────────────────────────────────────────────────
#  Route A: E8 -> D5 x A3 = SO(10) x SU(4)
# ──────────────────────────────────────────────────────────────────
ROUTE_A_REPS = [
    ('(45,1)',   'D_5 adjoint',   45, 'SO(10) gauge bosons'),
    ('(1,15)',   'A_3 adjoint',   15, 'SU(4) gauge / hidden sector'),
    ('(10,6)',   'vector-vector',  60, 'Higgs/scalar sector'),
    ('(16,4)',   'spinor-fund',    64, '3 generations + 1 sterile'),
    ('(16b,4b)', 'conj spinor',   64, '3 anti-generations + 1 sterile'),
]

# ──────────────────────────────────────────────────────────────────
#  Route B: E8 -> E6 x SU(3)
# ──────────────────────────────────────────────────────────────────
ROUTE_B_REPS = [
    ('(78,1)',   'E_6 adjoint',   78, 'E_6 gauge bosons'),
    ('(1,8)',    'SU(3) adjoint',   8, 'Family gluons'),
    ('(27,3)',   'fund-fund',      81, '3 generations (27 = 16+10+1)'),
    ('(27b,3b)', 'conj fund',     81, '3 mirror generations'),
]

# ──────────────────────────────────────────────────────────────────
#  Colors
# ──────────────────────────────────────────────────────────────────
BG       = '#0a0a1a'
GOLD     = '#ffaa00'
GOLD_DIM = '#aa8800'
BLUE     = '#4488ff'
BLUE_DIM = '#336699'
RED      = '#ff4488'
RED_DIM  = '#cc3366'
GREEN    = '#00ff88'
GREEN_DIM = '#00aa66'
WHITE    = '#ffffff'
GREY     = '#888888'
CYAN     = '#44ddff'
ORANGE   = '#ff8800'
PURPLE   = '#bb77ff'
PURPLE_DIM = '#8855cc'


# ══════════════════════════════════════════════════════════════════
#  CLASS: E8Branching
# ══════════════════════════════════════════════════════════════════

class E8Branching:
    """Toy 93: The E8 Branching Compare."""

    def __init__(self, quiet=False):
        self.quiet = quiet
        if not quiet:
            print()
            print("=" * 68)
            print("  THE E8 BRANCHING COMPARE  --  BST Toy 93")
            print("  Two routes through E8, both yield 3 generations")
            print("=" * 68)

    def _p(self, text=""):
        if not self.quiet:
            print(text)

    # ──────────────────────────────────────────────────────────────
    # 1. route_a  --  E8 -> D5 x A3
    # ──────────────────────────────────────────────────────────────

    def route_a(self):
        """E8 -> D5 x A3 = SO(10) x SU(4): BST standard decomposition."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  ROUTE A:  E8 -> D5 x A3  =  SO(10) x SU(4)")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  Maximal rank regular subalgebra (Dynkin 1952):")
        self._p("    rank(D5) + rank(A3) = 5 + 3 = 8 = rank(E8)")
        self._p()
        self._p("  Branching rule for the adjoint 248:")
        self._p()
        self._p("    248 -> (45,1) + (1,15) + (10,6) + (16,4) + (16b,4b)")
        self._p()
        self._p("  Dimension check:")
        self._p()
        self._p("  Rep          Type               Dim   Role")
        self._p("  ───────────  ─────────────────  ────  ─────────────────────────────")

        total = 0
        for rep, typ, dim, role in ROUTE_A_REPS:
            self._p(f"  {rep:<11}  {typ:<17}  {dim:>4}  {role}")
            total += dim

        self._p(f"  {'':11}  {'':17}  ────")
        self._p(f"  {'':11}  {'TOTAL':17}  {total:>4}")
        self._p()

        assert total == 248, f"Dimension mismatch: {total} != 248"
        self._p("  Dimension check: 45 + 15 + 60 + 64 + 64 = 248  OK")
        self._p()

        # The clean split
        self._p("  The 60:60:128 budget:")
        self._p("    Gauge   (45+15)       =  60   symmetry generators")
        self._p("    Higgs   (10 x 6)      =  60   commitment field")
        self._p("    Fermion (16x4+16bx4b) = 128   matter content")
        self._p()
        self._p("  Gauge and Higgs sectors have EQUAL dimension.")
        self._p("  Fermion sector = 2^7 = 2^g (genus = 7).")
        self._p()

        # Root decomposition
        self._p("  Root decomposition (240 = dim(E8) - rank(E8)):")
        self._p()
        roots = [
            ('(45,1)',  40, 'D5 roots (40 non-zero weights)'),
            ('(1,15)',  12, 'A3 roots (12 non-zero weights)'),
            ('(10,6)',  60, 'mixed sector (5 x 2 x 3 x 2)'),
            ('(16,4)',  64, 'half-spinor x fundamental'),
            ('(16b,4b)',64, 'conj half-spinor x conj fund'),
        ]
        rtotal = 0
        for rep, nroots, note in roots:
            self._p(f"    {rep:<11}  {nroots:>3} roots   {note}")
            rtotal += nroots
        self._p(f"    {'TOTAL':<11}  {rtotal:>3} roots   + 8 Cartan = 248")
        self._p()
        assert rtotal == 240

        return {
            'group': 'SO(10) x SU(4)',
            'reps': ROUTE_A_REPS,
            'total_dim': 248,
            'total_roots': 240,
        }

    # ──────────────────────────────────────────────────────────────
    # 2. route_b  --  E8 -> E6 x SU(3)
    # ──────────────────────────────────────────────────────────────

    def route_b(self):
        """E8 -> E6 x SU(3): 248 = (78,1)+(1,8)+(27,3)+(27b,3b)."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  ROUTE B:  E8 -> E6 x SU(3)")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  Maximal rank regular subalgebra:")
        self._p("    rank(E6) + rank(SU(3)) = 6 + 2 = 8 = rank(E8)")
        self._p("    Center quotient: E6 x SU(3) / (Z/3Z)")
        self._p()
        self._p("  Branching rule for the adjoint 248:")
        self._p()
        self._p("    248 -> (78,1) + (1,8) + (27,3) + (27b,3b)")
        self._p()
        self._p("  Dimension check:")
        self._p()
        self._p("  Rep          Type               Dim   Role")
        self._p("  ───────────  ─────────────────  ────  ─────────────────────────────")

        total = 0
        for rep, typ, dim, role in ROUTE_B_REPS:
            self._p(f"  {rep:<11}  {typ:<17}  {dim:>4}  {role}")
            total += dim

        self._p(f"  {'':11}  {'':17}  ────")
        self._p(f"  {'':11}  {'TOTAL':17}  {total:>4}")
        self._p()

        assert total == 248, f"Dimension mismatch: {total} != 248"
        self._p("  Dimension check: 78 + 8 + 81 + 81 = 248  OK")
        self._p()

        # The 27 decomposition
        self._p("  The 27 of E6 under E6 -> SO(10) x U(1)_chi:")
        self._p()
        self._p("    27 -> 16_1 + 10_{-2} + 1_4")
        self._p()
        self._p("    Component   SO(10) rep   Content")
        self._p("    ─────────   ──────────   ───────────────────────────────")
        self._p("    16_1        Spinor       One complete SM generation")
        self._p("    10_{-2}     Vector       Vector-like exotics (5+5b)")
        self._p("    1_4         Singlet      Right-handed neutrino candidate")
        self._p()
        self._p("  The (27,3) = 3 copies of 27 = THREE GENERATIONS.")
        self._p("  Each slot in the SU(3) triplet carries a full 27.")
        self._p()
        self._p("  The (27b,3b) provides 3 mirror (anti-)generations")
        self._p("  that must be made heavy (Barr's PQ mechanism).")
        self._p()

        return {
            'group': 'E6 x SU(3)',
            'reps': ROUTE_B_REPS,
            'total_dim': 248,
            '27_decomposition': '16_1 + 10_{-2} + 1_4',
        }

    # ──────────────────────────────────────────────────────────────
    # 3. convergence  --  Both routes meet at SO(10) x SU(3)_fam x U(1)
    # ──────────────────────────────────────────────────────────────

    def convergence(self):
        """Both routes converge at SO(10) x SU(3)_family x U(1)."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  CONVERGENCE: THE COMMUTING DIAGRAM")
        self._p("  " + "=" * 60)
        self._p()
        self._p("                          E8")
        self._p("                         /   \\")
        self._p("          SO(10) x SU(4)     E6 x SU(3)")
        self._p("            (Route A)         (Route B)")
        self._p("                         \\   /")
        self._p("                SO(10) x SU(3)_fam x U(1)")
        self._p()
        self._p("  Route A path:")
        self._p("    E8 -> SO(10) x SU(4)")
        self._p("    SU(4) -> SU(3)_fam x U(1)")
        self._p("    4 -> 3 + 1     (family triplet + sterile singlet)")
        self._p()
        self._p("  Route B path:")
        self._p("    E8 -> E6 x SU(3)_fam")
        self._p("    E6 -> SO(10) x U(1)_chi")
        self._p("    27 -> 16_1 + 10_{-2} + 1_4")
        self._p()
        self._p("  The U(1) factors differ:")
        self._p("    Route A: U(1) in SU(4)   (family hypercharge)")
        self._p("    Route B: U(1)_chi in E6   (E6 GUT charge)")
        self._p()
        self._p("  But at the intersection, both yield:")
        self._p("    - SO(10) gauge group")
        self._p("    - SU(3) family symmetry acting on 3 generations")
        self._p("    - U(1) distinguishing the extra content")
        self._p()

        # Full decomposition table under converged group
        self._p("  Under SO(10) x SU(3)_fam x U(1):")
        self._p()
        self._p("  From Route A (16,4) -> (16,3)_1 + (16,1)_{-3}:")
        self._p("    3 chiral generations + 1 sterile")
        self._p()
        self._p("  From Route B (27,3) -> (16_1,3) + (10_{-2},3) + (1_4,3):")
        self._p("    3 chiral generations + exotics")
        self._p()
        self._p("  In BOTH cases: the 16 of SO(10) appears in a triplet")
        self._p("  of SU(3)_family.  Three generations.  Same answer.")
        self._p()

        return {
            'convergent_group': 'SO(10) x SU(3)_fam x U(1)',
            'route_a_extra': '4th generation singlet (16,1)',
            'route_b_extra': 'exotics (10,3) + singlets (1,3)',
        }

    # ──────────────────────────────────────────────────────────────
    # 4. generation_comparison
    # ──────────────────────────────────────────────────────────────

    def generation_comparison(self):
        """Route A: [W(A3):W(B2)]=3.  Route B: 27 = 16+10+1."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  GENERATION COUNTING: TWO MECHANISMS")
        self._p("  " + "=" * 60)
        self._p()

        # Route A mechanism
        self._p("  ROUTE A: Weyl group coset index")
        self._p("  ─────────────────────────────────")
        self._p()
        self._p(f"    |W(A_3)| = |S_4| = 4! = {W_A3}")
        self._p(f"    |W(B_2)| = |S_2 x (Z_2)^2| = 2! x 2^2 = {W_B2}")
        self._p()
        self._p(f"    [W(A_3) : W(B_2)] = {W_A3} / {W_B2} = {N_gen}")
        self._p()
        self._p("    The 3 cosets of W(B_2) = D_4 inside W(A_3) = S_4")
        self._p("    correspond to 3 ways to partition {{1,2,3,4}} into")
        self._p("    two unordered pairs:")
        self._p("      {{1,2}} {{3,4}}   --  generation 1  (e, u, d)")
        self._p("      {{1,3}} {{2,4}}   --  generation 2  (mu, c, s)")
        self._p("      {{1,4}} {{2,3}}   --  generation 3  (tau, t, b)")
        self._p()
        self._p("    The B_2 core (soliton sector) is the 4th slot:")
        self._p("      identity coset of W(B_2) = inaccessible 4th generation")
        self._p()
        self._p(f"    Under SU(4) -> SU(3)_fam x U(1):")
        self._p(f"      4 -> 3 + 1   (3 accessible + 1 sterile)")
        self._p()

        # Route B mechanism
        self._p("  ROUTE B: Fundamental representation of SU(3)")
        self._p("  ────────────────────────────────────────────────")
        self._p()
        self._p("    (27, 3) of E6 x SU(3):")
        self._p("    Each 27 of E6 = one complete generation:")
        self._p("      27 -> 16_1 + 10_{-2} + 1_4   under SO(10) x U(1)")
        self._p()
        self._p("    The 3 of SU(3) is the family triplet DIRECTLY:")
        self._p("      slot 1: 27 = generation 1  (e, u, d)")
        self._p("      slot 2: 27 = generation 2  (mu, c, s)")
        self._p("      slot 3: 27 = generation 3  (tau, t, b)")
        self._p()
        self._p("    No 4th generation.  But carries exotics:")
        self._p("      10_{-2} per generation  (vector-like pairs)")
        self._p("      1_4 per generation      (singlets / nu_R)")
        self._p()

        # Comparison
        self._p("  KEY DIFFERENCE:")
        self._p("  ──────────────")
        self._p("    Route A: N_gen = [W(A_3):W(B_2)] = 24/8 = 3")
        self._p("              (Weyl group combinatorics, contains B_2)")
        self._p("    Route B: N_gen = dim(fund SU(3)) = 3")
        self._p("              (representation dimension, cleaner)")
        self._p()
        self._p("    Route A: 4th generation exists but inaccessible")
        self._p("    Route B: no 4th generation at all")
        self._p()

        return {
            'route_a_mechanism': 'Weyl coset [W(A3):W(B2)] = 3',
            'route_b_mechanism': 'dim(fund SU(3)) = 3',
            'route_a_extra_gen': True,
            'route_b_extra_gen': False,
        }

    # ──────────────────────────────────────────────────────────────
    # 5. soliton_visibility
    # ──────────────────────────────────────────────────────────────

    def soliton_visibility(self):
        """Route A shows B2 explicitly; Route B hides it."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  SOLITON VISIBILITY: WHERE IS B2?")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  The B_2 restricted root system of SO_0(5,2) controls")
        self._p("  the Toda soliton dynamics in BST.  Its visibility")
        self._p("  differs dramatically between the two routes.")
        self._p()

        self._p("  ROUTE A:  B_2 is EXPLICIT")
        self._p("  ──────────────────────────")
        self._p("    The chain of inclusions:")
        self._p()
        self._p("      D_5 x B_2  -->  D_5 x A_3  -->  E_8")
        self._p()
        self._p("    B_2 embeds in A_3 because:")
        self._p("      A_3 = SU(4) = SO(6)   (local isomorphism)")
        self._p("      B_2 = SO(5) in SO(6)   (standard inclusion)")
        self._p()
        self._p(f"    The Weyl group indices factorize:")
        self._p(f"      |W(D_5)|/|W(B_2)| = 1920/8 = 240 = |Phi(E_8)|")
        self._p(f"      |W(D_5)|/|W(A_3)| = 1920/24 = 80")
        self._p(f"      |W(A_3)|/|W(B_2)| = 24/8 = 3 = N_gen")
        self._p()
        self._p("    The soliton sector, the particle sector, and the")
        self._p("    generation number are all visible in ONE formula:")
        self._p(f"      240 = 80 x 3")
        self._p()

        self._p("  ROUTE B:  B_2 is HIDDEN")
        self._p("  ──────────────────────────")
        self._p("    E_8 -> E_6 x SU(3)")
        self._p("    The SU(3)_fam acts as the family group.")
        self._p("    There is NO explicit B_2 embedding visible.")
        self._p()
        self._p("    To find B_2, you must:")
        self._p("      1. Go from E_6 -> SO(10) x U(1)")
        self._p("      2. Recognize SO(10) has root system D_5")
        self._p("      3. Pass to the real form so(5,2)")
        self._p("      4. Compute the restricted root system -> B_2")
        self._p()
        self._p("    The Toda soliton structure is not manifest.")
        self._p("    Route B is algebraically cleaner for generations,")
        self._p("    but the BST dynamics require Route A.")
        self._p()

        self._p("  CONSEQUENCE FOR BST:")
        self._p("  ────────────────────")
        self._p("    Route A is the NATURAL BST route because it contains")
        self._p("    D_5 x B_2 explicitly.  The soliton sector (B_2 Toda"),
        self._p("    lattice, contact dynamics, substrate coupling) lives")
        self._p("    inside A_3 and is visible at every step.")
        self._p()
        self._p("    Route B hides all of this and must reconstruct it.")
        self._p()

        return {
            'route_a_b2': 'explicit (B2 in A3 in E8)',
            'route_b_b2': 'hidden (must reconstruct from E6 -> SO(10))',
            'bst_preferred': 'Route A',
        }

    # ──────────────────────────────────────────────────────────────
    # 6. peccei_quinn
    # ──────────────────────────────────────────────────────────────

    def peccei_quinn(self):
        """Barr's result: PQ protection uniquely selects SU(3)_family."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  PECCEI-QUINN AND THE FAMILY GROUP")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  The mirror problem:")
        self._p("    The 248 of E8 is REAL (self-conjugate).")
        self._p("    For every (27,3) there is a (27b,3b).")
        self._p("    Equal families and anti-families.")
        self._p("    This must be resolved to get chiral fermions.")
        self._p()

        self._p("  Barr's theorem (Phys. Rev. D 37, 204, 1988):")
        self._p("  ─────────────────────────────────────────────")
        self._p("    A Peccei-Quinn symmetry UNIQUELY selects")
        self._p("    SU(3)_family among all family subgroups of E8,")
        self._p("    subject to three requirements:")
        self._p()
        self._p("    1. PQ symmetry solves the strong CP problem")
        self._p("    2. Light fermion protection is maintained")
        self._p("    3. Perturbative unification is not destroyed")
        self._p()
        self._p("    Result: PQ charges distinguish families from")
        self._p("    anti-families.  Mirrors get superheavy masses.")
        self._p("    The 3 chiral families remain light.")
        self._p()

        self._p("  BST connection:")
        self._p("  ───────────────")
        self._p("    BST resolves strong CP differently:")
        self._p("      theta_QCD = 0 from contractibility of D_IV^5")
        self._p("      (c_2 = 0 for contractible manifolds)")
        self._p()
        self._p("    But Barr's algebraic result is consistent:")
        self._p("      PQ uniquely selects SU(3)_fam in Route B.")
        self._p("      BST's contractibility selects B_2 in Route A.")
        self._p("      Both mechanisms point to the SAME family group.")
        self._p()

        self._p("  Route A vs Route B on strong CP:")
        self._p("    Route A: theta = 0 from topology (separate mechanism)")
        self._p("    Route B: theta = 0 from PQ (built into E6 structure)")
        self._p()

        return {
            'barr_result': 'PQ uniquely selects SU(3)_fam in E8',
            'bst_mechanism': 'theta=0 from contractibility of D_IV^5',
            'consistency': 'both select the same family group',
        }

    # ──────────────────────────────────────────────────────────────
    # 7. heterotic_connection
    # ──────────────────────────────────────────────────────────────

    def heterotic_connection(self):
        """Route A = non-standard embedding, Route B = standard E8xE8."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  HETEROTIC STRING CONNECTION")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  In the E8 x E8 heterotic string on Calabi-Yau CY3:")
        self._p()

        self._p("  STANDARD EMBEDDING  (Route B)")
        self._p("  ──────────────────────────────")
        self._p("    - CY3 has holonomy SU(3)")
        self._p("    - Spin connection = gauge connection in one E8")
        self._p("    - SU(3)_holonomy in E8 breaks E8 -> E6 x SU(3)")
        self._p("    - 4D gauge group: E6 x E8_hidden")
        self._p()
        self._p("    Number of generations from topology:")
        self._p("      N_gen = |chi(CY3)| / 2 = |h^{2,1} - h^{1,1}|")
        self._p("      Three generations requires |chi| = 6")
        self._p("      First example: Tian-Yau manifold (1986)")
        self._p()
        self._p("    SU(3)_family = SU(3)_holonomy of compactification")
        self._p()

        self._p("  NON-STANDARD EMBEDDING  (Route A)")
        self._p("  ──────────────────────────────────")
        self._p("    - Vector bundle V with structure group H in E8")
        self._p("    - H = SU(4):  unbroken SO(10) x SU(4)")
        self._p("    - Further breaking SU(4) -> SU(3) x U(1)")
        self._p("    - Anderson, Gray, Lukas, Palti (2012):")
        self._p("      systematic construction of heterotic SO(10) models")
        self._p()
        self._p("    Structure group hierarchy:")
        self._p("      H = SU(3): unbroken E6        (standard)")
        self._p("      H = SU(4): unbroken SO(10)    (Route A)")
        self._p("      H = SU(5): unbroken SU(5)     (Georgi-Glashow)")
        self._p()

        self._p("  BST PERSPECTIVE:")
        self._p("  ────────────────")
        self._p("    In BST, E8 is LATENT, not gauged.")
        self._p("    D_IV^5 lives inside the structure of E8.")
        self._p("    The 240 = 1920/8 identity is the shadow of")
        self._p("    this containment, not an active gauge symmetry.")
        self._p()
        self._p("    Distler-Garibaldi no-go (2010):")
        self._p("      E8 cannot embed chiral gens as a 4D gauge theory.")
        self._p("      Evaded because:")
        self._p("        - In string theory: chirality from CY topology")
        self._p("        - In BST: E8 is latent, not gauged")
        self._p()

        self._p("  The topological origin of SU(3)_family:")
        self._p("    Heterotic: SU(3)_fam = SU(3)_holonomy of CY3")
        self._p("    BST:       SU(3)_fam = Weyl group coset of B2 in A3")
        self._p("    Same group, different topological origin.")
        self._p()

        return {
            'route_a_string': 'non-standard embedding (H=SU(4))',
            'route_b_string': 'standard embedding (H=SU(3))',
            'bst_role': 'E8 is latent, not gauged',
        }

    # ──────────────────────────────────────────────────────────────
    # 8. advantages_table
    # ──────────────────────────────────────────────────────────────

    def advantages_table(self):
        """Side-by-side comparison of both routes."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  ADVANTAGES TABLE: ROUTE A vs ROUTE B")
        self._p("  " + "=" * 60)
        self._p()

        rows = [
            ('Subgroup',          'D5 x A3 = SO(10)xSU(4)', 'E6 x SU(3)'),
            ('Family group',      'SU(4) -> SU(3)+U(1)',     'SU(3) directly'),
            ('4th generation',    'YES: (16,1) singlet',     'NO'),
            ('Generation count',  '[W(A3):W(B2)] = 3',       'dim(fund) = 3'),
            ('B2 soliton sector', 'EXPLICIT in A3',          'Hidden'),
            ('Higgs sector',      '(10,6) = 60-dim, L=1/v60','(10,3)+(10,3b)'),
            ('Mirror fermions',   '(16b,4b) = 4 anti-gen',   '(27b,3b) = 3 anti-gen'),
            ('Strong CP',         'theta=0 from topology',   'PQ built in (Barr)'),
            ('Heterotic string',  'Non-standard embedding',  'Standard embedding'),
            ('BST natural?',      'YES: contains D5 x B2',   'Less direct'),
            ('Exotic content',    '(10,6) = 60-dim Higgs',   '(10,3)+(1,3) lighter'),
        ]

        # Compute column widths
        w0 = max(len(r[0]) for r in rows) + 2
        w1 = max(len(r[1]) for r in rows) + 2
        w2 = max(len(r[2]) for r in rows) + 2

        header = f"  {'Feature':<{w0}} {'Route A (D5xA3)':<{w1}} {'Route B (E6xSU3)':<{w2}}"
        sep = f"  {'─'*w0} {'─'*w1} {'─'*w2}"

        self._p(header)
        self._p(sep)

        for feat, a, b in rows:
            self._p(f"  {feat:<{w0}} {a:<{w1}} {b:<{w2}}")

        self._p()
        self._p("  Both routes are valid decompositions of E8.")
        self._p("  Route A is PREFERRED in BST because it contains the")
        self._p("  soliton sector B2 and the full D5 x B2 chain.")
        self._p("  Route B has string-theory pedigree and cleaner")
        self._p("  generation counting.")
        self._p()

        return rows

    # ──────────────────────────────────────────────────────────────
    # 9. summary
    # ──────────────────────────────────────────────────────────────

    def summary(self):
        """Twin decompositions of one algebra."""
        self._p()
        self._p("  " + "=" * 60)
        self._p("  SUMMARY: TWIN DECOMPOSITIONS OF E8")
        self._p("  " + "=" * 60)
        self._p()
        self._p("  E8 (dim 248, rank 8) admits two maximal rank regular")
        self._p("  subalgebra decompositions that produce three generations")
        self._p("  of Standard Model fermions:")
        self._p()
        self._p("  Route A:  E8 -> SO(10) x SU(4)")
        self._p("    248 = (45,1) + (1,15) + (10,6) + (16,4) + (16b,4b)")
        self._p("    N_gen = [W(A3):W(B2)] = 24/8 = 3")
        self._p("    Contains B2 soliton sector explicitly")
        self._p("    BST STANDARD ROUTE")
        self._p()
        self._p("  Route B:  E8 -> E6 x SU(3)")
        self._p("    248 = (78,1) + (1,8) + (27,3) + (27b,3b)")
        self._p("    N_gen = dim(fund SU(3)) = 3")
        self._p("    PQ protection selects SU(3)_fam (Barr 1988)")
        self._p("    HETEROTIC STANDARD ROUTE")
        self._p()
        self._p("  Convergence:")
        self._p()
        self._p("                        E8")
        self._p("                       /   \\")
        self._p("        SO(10) x SU(4)     E6 x SU(3)")
        self._p("                       \\   /")
        self._p("              SO(10) x SU(3)_fam x U(1)")
        self._p()
        self._p("  Both routes agree on:")
        self._p("    - SO(10) as the GUT gauge group")
        self._p("    - SU(3) as the family symmetry")
        self._p("    - 3 generations from the 16 of SO(10)")
        self._p()
        self._p("  They differ on:")
        self._p("    - 4th generation: Route A has one, Route B does not")
        self._p("    - Soliton sector: Route A shows B2, Route B hides it")
        self._p("    - Strong CP: Route A uses topology, Route B uses PQ")
        self._p("    - Exotic content: different Higgs and singlet sectors")
        self._p()
        self._p("  The existence of two valid routes is a CONSISTENCY CHECK.")
        self._p("  The algebra E8 contains BST's D_IV^5 structure in")
        self._p("  multiple complementary ways.")
        self._p()
        self._p("  The deepest fact:")
        self._p(f"    |W(D5)|/|W(B2)| = {W_D5}/{W_B2} = {E8_ROOTS} = |Phi(E8)|")
        self._p("    One ratio, bridging particles, solitons, and E8.")
        self._p()

        return {
            'route_a': 'SO(10) x SU(4), BST standard, contains B2',
            'route_b': 'E6 x SU(3), heterotic standard, cleaner generations',
            'convergence': 'SO(10) x SU(3)_fam x U(1)',
            'N_gen': 3,
        }

    # ──────────────────────────────────────────────────────────────
    # 10. show  --  4-panel visualization
    # ──────────────────────────────────────────────────────────────

    def show(self):
        """4-panel visualization: both decomposition trees, shared SO(10)."""

        fig = plt.figure(figsize=(18, 13), facecolor=BG)
        fig.canvas.manager.set_window_title(
            'The E8 Branching Compare -- BST Toy 93')

        # ── Title ──
        fig.text(0.5, 0.975, 'THE E\u2088 BRANCHING COMPARE',
                 fontsize=26, fontweight='bold', color=GOLD, ha='center',
                 fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=2, foreground='#442200')])
        fig.text(0.5, 0.950,
                 'Two routes through E\u2088 to three generations of matter',
                 fontsize=12, color=GOLD_DIM, ha='center',
                 fontfamily='monospace')

        # ═══════════════════════════════════════════════════════════
        #  Panel 1 (top-left): Route A decomposition tree
        # ═══════════════════════════════════════════════════════════
        ax1 = fig.add_axes([0.02, 0.50, 0.47, 0.43])
        ax1.set_facecolor(BG)
        ax1.axis('off')
        ax1.set_xlim(0, 10)
        ax1.set_ylim(0, 10)

        ax1.text(5, 9.5, 'ROUTE A:  E\u2088 \u2192 SO(10) \u00d7 SU(4)',
                 fontsize=14, fontweight='bold', color=BLUE,
                 ha='center', fontfamily='monospace')
        ax1.text(5, 9.0, 'BST Standard  |  Contains B\u2082 soliton sector',
                 fontsize=9, color=BLUE_DIM, ha='center',
                 fontfamily='monospace')

        # E8 at top
        self._draw_box(ax1, 5, 8.3, 'E\u2088', GOLD, '#1a1a0a', w=1.4, h=0.5)
        ax1.text(5, 7.85, '248', fontsize=8, color=GREY,
                 ha='center', fontfamily='monospace')

        # Branches
        ax1.plot([5, 2.5], [7.7, 7.0], color=BLUE, linewidth=2, alpha=0.6)
        ax1.plot([5, 7.5], [7.7, 7.0], color=RED, linewidth=2, alpha=0.6)

        # SO(10)
        self._draw_box(ax1, 2.5, 6.7, 'SO(10)', BLUE, '#0a1a2a', w=1.6, h=0.4)
        ax1.text(2.5, 6.15, 'D\u2085  rank 5', fontsize=8, color=BLUE_DIM,
                 ha='center', fontfamily='monospace')

        # SU(4)
        self._draw_box(ax1, 7.5, 6.7, 'SU(4)', RED, '#2a0a1a', w=1.4, h=0.4)
        ax1.text(7.5, 6.15, 'A\u2083  rank 3', fontsize=8, color=RED_DIM,
                 ha='center', fontfamily='monospace')

        # B2 inside SU(4)
        ax1.plot([7.5, 7.5], [5.9, 5.3], color=PURPLE, linewidth=1.5, alpha=0.8)
        self._draw_box(ax1, 7.5, 5.0, 'B\u2082 = SO(5)', PURPLE, '#1a0a2a',
                       w=2.0, h=0.4)
        ax1.text(7.5, 4.45, 'soliton sector', fontsize=8, color=PURPLE_DIM,
                 ha='center', fontfamily='monospace')

        # Representation boxes
        reps_a = [
            (0.6, 3.3, '(45,1)', '45', BLUE_DIM, 'gauge'),
            (2.3, 3.3, '(1,15)', '15', RED_DIM, 'hidden'),
            (4.0, 3.3, '(10,6)', '60', ORANGE, 'Higgs'),
            (5.9, 3.3, '(16,4)', '64', GREEN, '3 gen'),
            (8.0, 3.3, '(16\u0305,4\u0305)', '64', GREEN_DIM, '3 anti'),
        ]
        for x, y, label, dim, color, note in reps_a:
            box = FancyBboxPatch((x - 0.7, y - 0.3), 1.4, 0.6,
                                  boxstyle='round,pad=0.1',
                                  facecolor='#0d0d24', edgecolor=color,
                                  linewidth=1.5)
            ax1.add_patch(box)
            ax1.text(x, y + 0.05, label, fontsize=9, fontweight='bold',
                     color=color, ha='center', va='center',
                     fontfamily='monospace')
            ax1.text(x, y - 0.5, dim, fontsize=8, color=GREY,
                     ha='center', fontfamily='monospace')
            ax1.text(x, y - 0.8, note, fontsize=7, color=color,
                     ha='center', fontfamily='monospace', alpha=0.7)

        # Sum
        ax1.text(5, 2.1, '45 + 15 + 60 + 64 + 64 = 248',
                 fontsize=10, fontweight='bold', color=WHITE,
                 ha='center', fontfamily='monospace')

        # Generation formula
        box_gen = FancyBboxPatch((1.5, 0.5), 7, 1.0,
                                  boxstyle='round,pad=0.2',
                                  facecolor='#0a2a1a', edgecolor=GREEN,
                                  linewidth=2)
        ax1.add_patch(box_gen)
        ax1.text(5, 1.15, 'N_gen = [W(A\u2083):W(B\u2082)] = 24/8 = 3',
                 fontsize=12, fontweight='bold', color=GREEN,
                 ha='center', fontfamily='monospace')
        ax1.text(5, 0.7, 'Weyl group coset  |  3 pair-partitions of {{1,2,3,4}}',
                 fontsize=8, color=GREEN_DIM,
                 ha='center', fontfamily='monospace')

        # ═══════════════════════════════════════════════════════════
        #  Panel 2 (top-right): Route B decomposition tree
        # ═══════════════════════════════════════════════════════════
        ax2 = fig.add_axes([0.51, 0.50, 0.47, 0.43])
        ax2.set_facecolor(BG)
        ax2.axis('off')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 10)

        ax2.text(5, 9.5, 'ROUTE B:  E\u2088 \u2192 E\u2086 \u00d7 SU(3)',
                 fontsize=14, fontweight='bold', color=CYAN,
                 ha='center', fontfamily='monospace')
        ax2.text(5, 9.0, 'Heterotic Standard  |  Cleaner generations',
                 fontsize=9, color='#336666', ha='center',
                 fontfamily='monospace')

        # E8 at top
        self._draw_box(ax2, 5, 8.3, 'E\u2088', GOLD, '#1a1a0a', w=1.4, h=0.5)
        ax2.text(5, 7.85, '248', fontsize=8, color=GREY,
                 ha='center', fontfamily='monospace')

        # Branches
        ax2.plot([5, 2.5], [7.7, 7.0], color=CYAN, linewidth=2, alpha=0.6)
        ax2.plot([5, 7.5], [7.7, 7.0], color=ORANGE, linewidth=2, alpha=0.6)

        # E6
        self._draw_box(ax2, 2.5, 6.7, 'E\u2086', CYAN, '#0a1a2a', w=1.4, h=0.4)
        ax2.text(2.5, 6.15, 'rank 6  dim 78', fontsize=8, color='#336666',
                 ha='center', fontfamily='monospace')

        # SU(3)
        self._draw_box(ax2, 7.5, 6.7, 'SU(3)_fam', ORANGE, '#2a1a0a',
                       w=2.0, h=0.4)
        ax2.text(7.5, 6.15, 'A\u2082  rank 2', fontsize=8, color='#996633',
                 ha='center', fontfamily='monospace')

        # E6 -> SO(10) x U(1)
        ax2.plot([2.5, 2.5], [5.9, 5.3], color=CYAN, linewidth=1.5, alpha=0.5)
        self._draw_box(ax2, 2.5, 5.0, 'SO(10)\u00d7U(1)\u1d6a',
                       BLUE, '#0a1a2a', w=2.6, h=0.4)
        ax2.text(2.5, 4.45, '27 = 16\u2081 + 10\u208b\u2082 + 1\u2084',
                 fontsize=8, color=BLUE_DIM,
                 ha='center', fontfamily='monospace')

        # B2 NOT visible indicator
        ax2.text(7.5, 5.3, 'B\u2082 ?', fontsize=12, color='#553333',
                 ha='center', fontfamily='monospace', fontweight='bold',
                 alpha=0.5)
        ax2.text(7.5, 4.8, '(hidden)', fontsize=8, color='#553333',
                 ha='center', fontfamily='monospace', alpha=0.5)

        # Representation boxes
        reps_b = [
            (1.3, 3.3, '(78,1)', '78', CYAN, 'gauge'),
            (3.3, 3.3, '(1,8)', '8', ORANGE, 'fam gluon'),
            (5.5, 3.3, '(27,3)', '81', GREEN, '3 gen'),
            (7.9, 3.3, '(27\u0305,3\u0305)', '81', GREEN_DIM, '3 mirror'),
        ]
        for x, y, label, dim, color, note in reps_b:
            box = FancyBboxPatch((x - 0.8, y - 0.3), 1.6, 0.6,
                                  boxstyle='round,pad=0.1',
                                  facecolor='#0d0d24', edgecolor=color,
                                  linewidth=1.5)
            ax2.add_patch(box)
            ax2.text(x, y + 0.05, label, fontsize=9, fontweight='bold',
                     color=color, ha='center', va='center',
                     fontfamily='monospace')
            ax2.text(x, y - 0.5, dim, fontsize=8, color=GREY,
                     ha='center', fontfamily='monospace')
            ax2.text(x, y - 0.8, note, fontsize=7, color=color,
                     ha='center', fontfamily='monospace', alpha=0.7)

        # Sum
        ax2.text(5, 2.1, '78 + 8 + 81 + 81 = 248',
                 fontsize=10, fontweight='bold', color=WHITE,
                 ha='center', fontfamily='monospace')

        # Generation formula
        box_gen2 = FancyBboxPatch((1.5, 0.5), 7, 1.0,
                                   boxstyle='round,pad=0.2',
                                   facecolor='#0a2a1a', edgecolor=GREEN,
                                   linewidth=2)
        ax2.add_patch(box_gen2)
        ax2.text(5, 1.15, 'N_gen = dim(fund SU(3)) = 3',
                 fontsize=12, fontweight='bold', color=GREEN,
                 ha='center', fontfamily='monospace')
        ax2.text(5, 0.7, 'Representation dimension  |  PQ selects SU(3) (Barr 1988)',
                 fontsize=8, color=GREEN_DIM,
                 ha='center', fontfamily='monospace')

        # ═══════════════════════════════════════════════════════════
        #  Panel 3 (bottom-left): Convergence diagram
        # ═══════════════════════════════════════════════════════════
        ax3 = fig.add_axes([0.02, 0.04, 0.47, 0.42])
        ax3.set_facecolor(BG)
        ax3.axis('off')
        ax3.set_xlim(0, 10)
        ax3.set_ylim(0, 10)

        ax3.text(5, 9.5, 'CONVERGENCE DIAGRAM', fontsize=14,
                 fontweight='bold', color=GOLD, ha='center',
                 fontfamily='monospace')

        # E8 at top
        self._draw_box(ax3, 5, 8.3, 'E\u2088 (248)', WHITE, '#1a1a1a',
                       w=2.2, h=0.5)

        # Two branches
        ax3.plot([5, 2.2], [7.7, 6.5], color=BLUE, linewidth=2.5, alpha=0.8)
        ax3.plot([5, 7.8], [7.7, 6.5], color=CYAN, linewidth=2.5, alpha=0.8)

        # Route A box
        self._draw_box(ax3, 2.2, 6.2, 'SO(10)\u00d7SU(4)', BLUE, '#0a1a2a',
                       w=2.8, h=0.5)
        ax3.text(2.2, 5.5, 'Route A', fontsize=10, fontweight='bold',
                 color=BLUE, ha='center', fontfamily='monospace')
        ax3.text(2.2, 5.1, 'BST standard', fontsize=8, color=BLUE_DIM,
                 ha='center', fontfamily='monospace')
        ax3.text(2.2, 4.7, 'B\u2082 explicit', fontsize=8, color=PURPLE,
                 ha='center', fontfamily='monospace')

        # Route B box
        self._draw_box(ax3, 7.8, 6.2, 'E\u2086\u00d7SU(3)', CYAN, '#0a1a2a',
                       w=2.4, h=0.5)
        ax3.text(7.8, 5.5, 'Route B', fontsize=10, fontweight='bold',
                 color=CYAN, ha='center', fontfamily='monospace')
        ax3.text(7.8, 5.1, 'Heterotic standard', fontsize=8, color='#336666',
                 ha='center', fontfamily='monospace')
        ax3.text(7.8, 4.7, 'PQ protection', fontsize=8, color=ORANGE,
                 ha='center', fontfamily='monospace')

        # Converging arrows
        ax3.plot([2.2, 5], [4.3, 3.3], color=BLUE, linewidth=2.5, alpha=0.8)
        ax3.plot([7.8, 5], [4.3, 3.3], color=CYAN, linewidth=2.5, alpha=0.8)

        # Convergent group
        conv_box = FancyBboxPatch((1.8, 2.3), 6.4, 1.3,
                                   boxstyle='round,pad=0.2',
                                   facecolor='#1a1a0a', edgecolor=GOLD,
                                   linewidth=2.5)
        ax3.add_patch(conv_box)
        ax3.text(5, 3.15, 'SO(10) \u00d7 SU(3)_fam \u00d7 U(1)',
                 fontsize=14, fontweight='bold', color=GOLD,
                 ha='center', fontfamily='monospace')
        ax3.text(5, 2.6, '3 generations of 16-plet fermions',
                 fontsize=10, color=GOLD_DIM,
                 ha='center', fontfamily='monospace')

        # Differences at bottom
        ax3.text(2.2, 1.6, 'Route A has:', fontsize=9, fontweight='bold',
                 color=BLUE, ha='center', fontfamily='monospace')
        ax3.text(2.2, 1.1, '4th gen singlet (16,1)', fontsize=8,
                 color=BLUE_DIM, ha='center', fontfamily='monospace')
        ax3.text(2.2, 0.7, '60-dim Higgs (10,6)', fontsize=8,
                 color=BLUE_DIM, ha='center', fontfamily='monospace')

        ax3.text(7.8, 1.6, 'Route B has:', fontsize=9, fontweight='bold',
                 color=CYAN, ha='center', fontfamily='monospace')
        ax3.text(7.8, 1.1, 'no 4th generation', fontsize=8,
                 color='#336666', ha='center', fontfamily='monospace')
        ax3.text(7.8, 0.7, 'exotics (10,3)+(1,3)', fontsize=8,
                 color='#336666', ha='center', fontfamily='monospace')

        ax3.text(5, 0.2, 'Both routes agree: 3 gens \u00d7 16 of SO(10)',
                 fontsize=9, fontweight='bold', color=GREEN,
                 ha='center', fontfamily='monospace')

        # ═══════════════════════════════════════════════════════════
        #  Panel 4 (bottom-right): Comparison table + key numbers
        # ═══════════════════════════════════════════════════════════
        ax4 = fig.add_axes([0.51, 0.04, 0.47, 0.42])
        ax4.set_facecolor(BG)
        ax4.axis('off')
        ax4.set_xlim(0, 10)
        ax4.set_ylim(0, 10)

        ax4.text(5, 9.5, 'KEY NUMBERS', fontsize=14, fontweight='bold',
                 color=PURPLE, ha='center', fontfamily='monospace')

        # Weyl group identities
        y = 8.5
        identities = [
            ('|W(D\u2085)| = 5!\u00d72\u2074',      f'= {W_D5}',    BLUE),
            ('|W(A\u2083)| = 4!',                    f'= {W_A3}',    RED),
            ('|W(B\u2082)| = 2!\u00d72\u00b2',       f'= {W_B2}',    PURPLE),
            ('', '', ''),
            ('[W(A\u2083):W(B\u2082)]',              f'= {N_gen}  = N_gen', GREEN),
            ('|W(D\u2085)|/|W(B\u2082)|',            f'= {E8_ROOTS}  = |\u03a6(E\u2088)|', GOLD),
            ('|W(D\u2085)|/|W(A\u2083)|',            f'= {W_D5//W_A3}', GREY),
        ]
        for label, val, color in identities:
            if label:
                ax4.text(0.5, y, label, fontsize=10, color=color,
                         fontfamily='monospace')
                ax4.text(6.0, y, val, fontsize=10, fontweight='bold',
                         color=color, fontfamily='monospace')
            y -= 0.55

        # The 240 factorization
        y -= 0.3
        ax4.text(5, y, '240 = 80 \u00d7 3', fontsize=13, fontweight='bold',
                 color=GOLD, ha='center', fontfamily='monospace',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#2a2a0a',
                           edgecolor=GOLD_DIM, linewidth=1.5))
        y -= 0.6
        ax4.text(5, y,
                 'particle index \u00d7 generation number = E\u2088 roots',
                 fontsize=8, color=GOLD_DIM, ha='center',
                 fontfamily='monospace')

        # Generation comparison box
        y -= 1.0
        gen_box = FancyBboxPatch((0.5, y - 0.8), 9, 1.8,
                                  boxstyle='round,pad=0.15',
                                  facecolor='#0d0d24', edgecolor=GREEN,
                                  linewidth=1.5)
        ax4.add_patch(gen_box)

        ax4.text(5, y + 0.6, 'WHY THREE GENERATIONS?', fontsize=11,
                 fontweight='bold', color=GREEN, ha='center',
                 fontfamily='monospace')
        ax4.text(2.5, y, 'Route A:', fontsize=9, fontweight='bold',
                 color=BLUE, ha='center', fontfamily='monospace')
        ax4.text(2.5, y - 0.4,
                 'coset [W(A\u2083):W(B\u2082)]', fontsize=8,
                 color=BLUE_DIM, ha='center', fontfamily='monospace')
        ax4.text(7.5, y, 'Route B:', fontsize=9, fontweight='bold',
                 color=CYAN, ha='center', fontfamily='monospace')
        ax4.text(7.5, y - 0.4, 'dim(fund SU(3))', fontsize=8,
                 color='#336666', ha='center', fontfamily='monospace')

        # Bottom note
        ax4.text(5, 0.7,
                 'N_colors = N_gen = 3', fontsize=13,
                 fontweight='bold', color=WHITE, ha='center',
                 fontfamily='monospace')
        ax4.text(5, 0.2,
                 'same number, different algebraic origin',
                 fontsize=9, color=GREY, ha='center',
                 fontfamily='monospace')

        # ── Copyright ──
        fig.text(0.5, 0.005,
                 '\u00a9 2026 Casey Koons  |  Claude Opus 4.6  '
                 '|  Bubble Spacetime Theory',
                 fontsize=8, color='#444444', ha='center',
                 fontfamily='monospace')

        plt.show()

    # ──────────────────────────────────────────────────────────────
    #  Helper: draw a labeled box
    # ──────────────────────────────────────────────────────────────

    def _draw_box(self, ax, cx, cy, label, color, fill, w=2.0, h=0.5):
        """Draw a rounded box with centered label."""
        box = FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                              boxstyle='round,pad=0.15',
                              facecolor=fill, edgecolor=color,
                              linewidth=2)
        ax.add_patch(box)
        ax.text(cx, cy, label, fontsize=11, fontweight='bold',
                color=color, ha='center', va='center',
                fontfamily='monospace')


# ══════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════

def main():
    """Interactive menu for the E8 Branching Compare."""
    eb = E8Branching(quiet=False)

    menu = """
  ============================================
   THE E8 BRANCHING COMPARE  --  Toy 93
  ============================================
   Two routes through E8, both -> 3 generations

   1. Route A: E8 -> SO(10) x SU(4)
   2. Route B: E8 -> E6 x SU(3)
   3. Convergence diagram
   4. Generation comparison
   5. Soliton visibility (B2)
   6. Peccei-Quinn & family group
   7. Heterotic string connection
   8. Advantages table
   9. Summary
   0. Show visualization (4-panel)
   q. Quit
  ============================================
"""

    while True:
        print(menu)
        choice = input("  Choice: ").strip().lower()
        if choice == '1':
            eb.route_a()
        elif choice == '2':
            eb.route_b()
        elif choice == '3':
            eb.convergence()
        elif choice == '4':
            eb.generation_comparison()
        elif choice == '5':
            eb.soliton_visibility()
        elif choice == '6':
            eb.peccei_quinn()
        elif choice == '7':
            eb.heterotic_connection()
        elif choice == '8':
            eb.advantages_table()
        elif choice == '9':
            eb.summary()
        elif choice == '0':
            eb.show()
        elif choice in ('q', 'quit', 'exit'):
            print("  Goodbye.")
            break
        else:
            print("  Unknown choice. Try again.")


if __name__ == '__main__':
    main()
