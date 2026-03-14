#!/usr/bin/env python3
"""
THE E₈ ROOT UNIFIER
====================
The ratio of particle world to soliton world IS E₈.

    |W(D₅)| / |W(B₂)| = 1920 / 8 = 240 = |Φ(E₈)|

E₈ is the largest exceptional Lie algebra. Its 240 roots in 8 dimensions
organize the relationship between the particle sector (D₅ = SO(10), the
baryon orbit) and the soliton sector (B₂, the restricted root system of
the symmetric space D_IV^5 = SO₀(5,2)/[SO(5)×SO(2)]).

This is NOT a coincidence. It is a consequence of the chain of inclusions:

    D₅ × B₂  ⊂  D₅ × A₃  ⊂  E₈

where E₈ → D₅ × A₃ is a maximal rank regular subalgebra decomposition
(Dynkin 1952), and B₂ ⊂ A₃ with Weyl group index [W(A₃):W(B₂)] = 3 = N_c.

The 240 E₈ roots decompose under D₅ × A₃ ≅ SO(10) × SU(4) as:
    (45,1): 40 roots — D₅ adjoint (particle sector)
    (1,15): 12 roots — A₃ adjoint (hidden sector containing B₂)
    (10,6): 60 roots — vector-vector (mixed states)
    (16,4): 64 roots — spinor (one generation of fermions × 4)
   (16̄,4̄): 64 roots — conjugate spinor

BST does NOT postulate E₈ as a gauge symmetry. E₈ is the algebraic
structure that naturally contains both the particle and soliton sectors.
The 240 = 1920/8 identity is the shadow of this containment.

*** EXPLORATORY — The E₈ unification is structural, not yet derived ***
*** from a unique physical principle. Handle with appropriate caution. ***

    from toy_e8_unifier import E8Unifier
    u = E8Unifier()
    u.weyl_orders()           # |W(D₅)|=1920, |W(B₂)|=8, ratio=240
    u.e8_roots()              # construct the 240 roots
    u.root_count()            # verify |Φ(E₈)| = 240
    u.d5_sector()             # particle sector: 1920 elements
    u.b2_sector()             # soliton sector: 8 elements
    u.unification_ratio()     # 1920/8 = 240 with interpretation
    u.e8_properties()         # rank, dim, Coxeter number, exponents
    u.dynkin_diagram()        # E₈ Dynkin diagram with subdiagrams
    u.summary()               # the punchline
    u.show()                  # 4-panel visualization

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
# BST CONSTANTS
# ═══════════════════════════════════════════════════════════════════

n_C = 5                              # complex dimension of D_IV^5
N_c = 3                              # color number
C2 = n_C + 1                        # = 6
genus = n_C + 2                      # = 7

# Weyl group orders
WEYL_D5 = 2**(n_C - 1) * factorial(n_C)   # 2⁴ × 5! = 1920
WEYL_B2 = 2**2 * factorial(2)              # 2² × 2! = 8
WEYL_A3 = factorial(4)                     # 4! = 24
RATIO = WEYL_D5 // WEYL_B2                          # 240

# E₈ properties
E8_RANK = 8
E8_DIM = 248
E8_ROOTS = 240
E8_COXETER = 30
E8_EXPONENTS = [1, 7, 11, 13, 17, 19, 23, 29]
E8_DUAL_COXETER = 30

# Root multiplicities of B₂ at n_C=5
M_SHORT = n_C - 2                    # = 3 (spatial dimensions)
M_LONG = 1                           # = 1 (temporal dimension)


# ═══════════════════════════════════════════════════════════════════
# E₈ ROOT SYSTEM CONSTRUCTION
# ═══════════════════════════════════════════════════════════════════

def build_e8_roots():
    """
    Construct all 240 roots of E₈ in 8 dimensions.

    E₈ roots come in two forms (using the even coordinate system):

    Type I  (integer form): all permutations of (±1, ±1, 0, 0, 0, 0, 0, 0)
            — vectors with exactly two nonzero entries ±1.
            Count: C(8,2) × 2² = 28 × 4 = 112

    Type II (half-integer form): (±½, ±½, ±½, ±½, ±½, ±½, ±½, ±½)
            with an EVEN number of minus signs.
            Count: 2⁸ / 2 = 128

    Total: 112 + 128 = 240. ✓

    These are the minimal vectors of the E₈ lattice — the unique even
    unimodular lattice in 8 dimensions (Viazovska 2016, Fields Medal 2022).
    """
    roots = []

    # Type I: integer roots — ±eᵢ ± eⱼ for i < j
    for i in range(8):
        for j in range(i + 1, 8):
            for si in [+1, -1]:
                for sj in [+1, -1]:
                    v = np.zeros(8)
                    v[i] = si
                    v[j] = sj
                    roots.append(v)

    # Type II: half-integer roots — (±½)⁸ with even number of minus signs
    for bits in range(256):
        signs = np.array([(bits >> k) & 1 for k in range(8)])
        n_minus = np.sum(signs)
        if n_minus % 2 == 0:     # even number of minus signs
            v = np.where(signs, -0.5, +0.5)
            roots.append(v)

    return np.array(roots)


def decompose_under_d5_a3(roots):
    """
    Decompose E₈ roots under D₅ × A₃ ≅ SO(10) × SU(4).

    D₅ lives in coordinates 1-5, A₃ in coordinates 6-8.

    The branching:
        248 → (45,1) + (1,15) + (10,6) + (16,4) + (16̄,4̄)

    For roots (non-zero weights of adjoint):
        240 → 40 + 12 + 60 + 64 + 64
    """
    d5_adj = []    # (45,1): roots purely in D₅ coordinates (1-5)
    a3_adj = []    # (1,15): roots purely in A₃ coordinates (6-8)
    mixed = []     # (10,6): roots in both sectors
    spinor_p = []  # (16,4): half-integer with specific chirality
    spinor_m = []  # (16̄,4̄): half-integer with conjugate chirality

    for r in roots:
        d5_part = r[:5]
        a3_part = r[5:]

        is_integer = np.allclose(r, np.round(r))

        if is_integer:
            d5_nonzero = np.any(np.abs(d5_part) > 0.01)
            a3_nonzero = np.any(np.abs(a3_part) > 0.01)

            if d5_nonzero and not a3_nonzero:
                d5_adj.append(r)
            elif a3_nonzero and not d5_nonzero:
                a3_adj.append(r)
            elif d5_nonzero and a3_nonzero:
                mixed.append(r)
        else:
            # Half-integer roots: classify by D₅ chirality
            # Product of signs of D₅ part determines spinor vs conjugate
            d5_signs = np.sign(d5_part)
            chirality = np.prod(d5_signs)
            if chirality > 0:
                spinor_p.append(r)
            else:
                spinor_m.append(r)

    return {
        'D5_adjoint': np.array(d5_adj),
        'A3_adjoint': np.array(a3_adj),
        'mixed': np.array(mixed),
        'spinor_plus': np.array(spinor_p),
        'spinor_minus': np.array(spinor_m),
    }


# ═══════════════════════════════════════════════════════════════════
# WEYL GROUP CONSTRUCTIONS
# ═══════════════════════════════════════════════════════════════════

def build_weyl_b2():
    """
    Build the 8 elements of W(B₂) = S₂ ⋉ (Z₂)².
    Acts on R² by permutations and sign changes of 2 coordinates.
    """
    elements = []
    labels = []
    for perm in [(0, 1), (1, 0)]:
        for s0 in [+1, -1]:
            for s1 in [+1, -1]:
                M = np.zeros((2, 2))
                M[0, perm[0]] = s0
                M[1, perm[1]] = s1
                elements.append(M)
                p_str = "id" if perm == (0, 1) else "swap"
                s_str = f"({'+' if s0 > 0 else '-'}{'+' if s1 > 0 else '-'})"
                labels.append(f"{p_str}{s_str}")
    return elements, labels


def build_weyl_d5_order():
    """
    Compute |W(D₅)| = 2^(n-1) × n! for n=5.
    W(Dₙ) = Sₙ ⋉ (Z₂)^(n-1) — permutations plus EVEN sign changes.
    """
    n = 5
    order = 2**(n - 1) * factorial(n)
    return order


# ═══════════════════════════════════════════════════════════════════
# THE E₈ UNIFIER CLASS
# ═══════════════════════════════════════════════════════════════════

class E8Unifier:
    """
    The E₈ Root Unifier — connecting particle and soliton sectors.

    *** EXPLORATORY ***
    The E₈ connection is a structural observation, not yet derived
    from a unique physical principle. The identity 1920/8 = 240 is
    exact, the algebraic chain D₅ × B₂ ⊂ D₅ × A₃ ⊂ E₈ is standard
    Lie theory, but the physical interpretation remains open.

    The argument:
        1. D₅ (particle sector): |W(D₅)| = 1920 (baryon orbit)
        2. B₂ (soliton sector): |W(B₂)| = 8 (Toda lattice symmetry)
        3. Ratio: 1920/8 = 240 = |Φ(E₈)| (roots of E₈)
        4. Chain: D₅ × B₂ ⊂ D₅ × A₃ ⊂ E₈ (Dynkin)
        5. Index: [W(A₃):W(B₂)] = 3 = N_c (the color number)
    """

    def __init__(self, quiet=False):
        self._roots = None
        self._decomposition = None
        if not quiet:
            self._print_header()

    def _print_header(self):
        print("=" * 68)
        print("  THE E8 ROOT UNIFIER")
        print("  The ratio of particle world to soliton world IS E8")
        print("  |W(D5)| / |W(B2)| = 1920 / 8 = 240 = |Phi(E8)|")
        print()
        print("  *** EXPLORATORY — structural observation, not derived ***")
        print("=" * 68)

    def _ensure_roots(self):
        """Lazily build and cache the E₈ root system."""
        if self._roots is None:
            self._roots = build_e8_roots()
        return self._roots

    def _ensure_decomposition(self):
        """Lazily compute and cache the D₅ × A₃ decomposition."""
        if self._decomposition is None:
            roots = self._ensure_roots()
            self._decomposition = decompose_under_d5_a3(roots)
        return self._decomposition

    # ─── 1. Weyl group orders ───

    def weyl_orders(self) -> dict:
        """
        The two Weyl groups and their ratio.

        |W(D₅)| = 2⁴ × 5! = 16 × 120 = 1920  (particle sector)
        |W(B₂)| = 2² × 2! =  4 ×   2 =    8  (soliton sector)
        Ratio = 1920 / 8 = 240 = |Φ(E₈)|
        """
        print()
        print("  WEYL GROUP ORDERS")
        print("  =================")
        print()
        print("  Two Weyl groups govern BST:")
        print()
        print(f"  {'Sector':<12} {'Root sys':<10} {'Weyl group':<24} {'Order':<8} {'Role'}")
        print(f"  {'─'*12} {'─'*10} {'─'*24} {'─'*8} {'─'*30}")
        print(f"  {'Particle':<12} {'D5':<10} {'S5 x (Z2)^4':<24} "
              f"{WEYL_D5:<8} {'Bergman kernel, baryon orbit'}")
        print(f"  {'Soliton':<12} {'B2':<10} {'S2 x (Z2)^2':<24} "
              f"{WEYL_B2:<8} {'Toda lattice symmetry'}")
        print()
        print(f"  D5: |W(D5)| = 2^(n-1) x n! = 2^4 x 5! = 16 x 120 = {WEYL_D5}")
        print(f"  B2: |W(B2)| = 2^n x n!     = 2^2 x 2! =  4 x   2 = {WEYL_B2}")
        print()
        print(f"  Ratio: {WEYL_D5} / {WEYL_B2} = {RATIO}")
        print(f"         = |Phi(E8)| = number of roots of E8")
        print()
        print(f"  Intermediate: |W(A3)| = 4! = {WEYL_A3}")
        print(f"    [W(D5):W(A3)] = {WEYL_D5}/{WEYL_A3} = {WEYL_D5 // WEYL_A3}")
        print(f"    [W(A3):W(B2)] = {WEYL_A3}/{WEYL_B2} = {WEYL_A3 // WEYL_B2} = N_c")
        print()
        print(f"  The color number N_c = {N_c} is the coset index connecting")
        print(f"  the soliton symmetry B2 to the full complex symmetry A3.")

        return {
            'W_D5': WEYL_D5,
            'W_B2': WEYL_B2,
            'W_A3': WEYL_A3,
            'ratio': RATIO,
            'intermediate': WEYL_D5 // WEYL_A3,
            'color_index': WEYL_A3 // WEYL_B2,
        }

    # ─── 2. E₈ root system ───

    def e8_roots(self) -> np.ndarray:
        """
        Construct all 240 roots of E₈ in 8 dimensions.

        Two types:
          Type I  (integer): +/-e_i +/- e_j  → 112 roots
          Type II (half-int): (+/-1/2)^8 with even # of minus signs → 128 roots

        These are the minimal vectors of the E₈ lattice — the densest
        lattice packing in 8D (Viazovska 2016).
        """
        roots = self._ensure_roots()

        # Classify
        integer_mask = np.array([np.allclose(r, np.round(r)) for r in roots])
        n_int = np.sum(integer_mask)
        n_half = len(roots) - n_int

        print()
        print("  E8 ROOT SYSTEM")
        print("  ==============")
        print()
        print(f"  Dimension: {roots.shape[1]}")
        print(f"  Total roots: {len(roots)}")
        print()
        print(f"  Type I  (integer):      {n_int:>4}  "
              f"(+/-e_i +/- e_j, i<j)")
        print(f"  Type II (half-integer): {n_half:>4}  "
              f"((+/-1/2)^8, even # of minus signs)")
        print(f"  Total:                  {n_int + n_half:>4}")
        print()

        # Verify all roots have the same squared length
        norms_sq = np.sum(roots**2, axis=1)
        print(f"  All roots have |r|^2 = {norms_sq[0]:.1f}  "
              f"(variance: {np.var(norms_sq):.2e})")
        print()

        # Show a few examples
        print("  Sample integer roots:")
        for r in roots[integer_mask][:3]:
            print(f"    {r}")
        print("  Sample half-integer roots:")
        for r in roots[~integer_mask][:3]:
            print(f"    {r}")

        return roots

    # ─── 3. Root count verification ───

    def root_count(self) -> dict:
        """
        Verify |Φ(E₈)| = 240 and the decomposition under D₅ × A₃.

        248 → (45,1) + (1,15) + (10,6) + (16,4) + (16̄,4̄)
        240 →   40   +   12   +   60   +   64   +   64
        """
        roots = self._ensure_roots()
        decomp = self._ensure_decomposition()

        counts = {
            'D5_adjoint': len(decomp['D5_adjoint']),
            'A3_adjoint': len(decomp['A3_adjoint']),
            'mixed': len(decomp['mixed']),
            'spinor_plus': len(decomp['spinor_plus']),
            'spinor_minus': len(decomp['spinor_minus']),
        }
        total = sum(counts.values())

        print()
        print("  ROOT COUNT VERIFICATION")
        print("  =======================")
        print()
        print(f"  |Phi(E8)| = {len(roots)}   {'VERIFIED' if len(roots) == 240 else 'ERROR!'}")
        print()
        print("  Decomposition under D5 x A3 = SO(10) x SU(4):")
        print()
        print(f"    {'Sector':<20} {'Rep':<12} {'Roots':<8} {'Expected':<10} {'Status'}")
        print(f"    {'─'*20} {'─'*12} {'─'*8} {'─'*10} {'─'*8}")

        expected = {
            'D5_adjoint': ('(45,1)', 40),
            'A3_adjoint': ('(1,15)', 12),
            'mixed': ('(10,6)', 60),
            'spinor_plus': ('(16,4)', 64),
            'spinor_minus': ('(16b,4b)', 64),
        }

        all_ok = True
        for key in ['D5_adjoint', 'A3_adjoint', 'mixed', 'spinor_plus', 'spinor_minus']:
            rep, exp = expected[key]
            got = counts[key]
            ok = got == exp
            if not ok:
                all_ok = False
            status = "OK" if ok else f"MISMATCH (got {got})"
            print(f"    {key:<20} {rep:<12} {got:<8} {exp:<10} {status}")

        print(f"    {'─'*20} {'─'*12} {'─'*8} {'─'*10}")
        print(f"    {'TOTAL':<20} {'248':<12} {total:<8} {240:<10} "
              f"{'VERIFIED' if total == 240 and all_ok else 'CHECK'}")
        print()
        print(f"  Plus {E8_RANK} Cartan generators: 5 from D5 + 3 from A3 = {E8_RANK}")
        print(f"  Total dimension: {total} + {E8_RANK} = {total + E8_RANK} = dim(E8)")
        print()
        print("  The 16 of SO(10) = one generation of Standard Model fermions.")
        print("  The 4 of SU(4) connects each fermion to 4 soliton states.")

        return {
            'total_roots': len(roots),
            'decomposition': counts,
            'all_verified': total == 240 and all_ok,
        }

    # ─── 4. D₅ particle sector ───

    def d5_sector(self) -> dict:
        """
        The particle sector: D₅ = SO(10).

        |W(D₅)| = 2⁴ × 5! = 1920 elements.
        This is the Weyl group of the Bergman kernel numerator —
        the baryon orbit that appears in m_p/m_e = 6π⁵.
        """
        print()
        print("  D5 PARTICLE SECTOR")
        print("  ==================")
        print()
        print(f"  Root system: D5 = so(10)")
        print(f"  Rank: 5")
        print(f"  Dimension of Lie algebra: 45 = 10×9/2")
        print(f"  Number of roots: 40 = 2 × C(5,2) × 2 = 40")
        print(f"  Weyl group: W(D5) = S5 x (Z2)^4")
        print(f"  |W(D5)| = 5! x 2^4 = 120 x 16 = {WEYL_D5}")
        print()
        print("  BST roles of D5:")
        print(f"    -- Bergman kernel: K(0,0) = |W(D5)| / pi^5 = {WEYL_D5}/pi^5")
        print(f"    -- Baryon orbit: the Z3 circuit visits {WEYL_D5} configurations")
        print(f"    -- Proton mass: m_p/m_e = C2 x |W(D5)| x (pi^5/|W(D5)|) = 6pi^5")
        print(f"    -- The {WEYL_D5} appears AND cancels, leaving 6pi^5 = {C2*np.pi**5:.5f}")
        print()
        print(f"  Observed m_p/m_e = 1836.15267")
        print(f"  BST:     m_p/m_e = 6pi^5     = {C2*np.pi**5:.5f}")
        print(f"  Error: {abs(C2*np.pi**5 - 1836.15267)/1836.15267*100:.3f}%")
        print()
        print("  The 16 of SO(10) contains one complete generation:")
        print("    3 × (u_L, d_L) + 3 × (u_R, d_R) + (e_L, nu_L) + e_R + nu_R = 16")

        return {
            'root_system': 'D5',
            'lie_algebra': 'so(10)',
            'rank': 5,
            'dim': 45,
            'roots': 40,
            'weyl_order': WEYL_D5,
            'proton_ratio': C2 * np.pi**5,
        }

    # ─── 5. B₂ soliton sector ───

    def b2_sector(self) -> dict:
        """
        The soliton sector: B₂ (restricted root system of D_IV^5).

        |W(B₂)| = 8 elements.
        This is the symmetry group of the B₂ Toda lattice —
        the integrable system governing soliton dynamics in the bulk.
        """
        elements, labels = build_weyl_b2()

        print()
        print("  B2 SOLITON SECTOR")
        print("  =================")
        print()
        print(f"  Root system: B2 (restricted root system of D_IV^5)")
        print(f"  Rank: 2")
        print(f"  Root multiplicities at n_C = {n_C}:")
        print(f"    Short roots: m_short = n_C - 2 = {M_SHORT} = spatial dimensions")
        print(f"    Long roots:  m_long  = {M_LONG}             = temporal dimension")
        print(f"  Weyl group: W(B2) = S2 x (Z2)^2")
        print(f"  |W(B2)| = {WEYL_B2}")
        print(f"  Coxeter number: h(B2) = 4")
        print()
        print(f"  The {WEYL_B2} elements of W(B2):")
        print()

        for i, (M, lab) in enumerate(zip(elements, labels)):
            det = np.linalg.det(M)
            print(f"    {i+1:>2}. {lab:<12}  det = {det:+.0f}  "
                  f"[{M[0,0]:+.0f} {M[0,1]:+.0f}]")
            print(f"        {'':12}            "
                  f"[{M[1,0]:+.0f} {M[1,1]:+.0f}]")

        print()
        print("  BST roles of B2:")
        print("    -- Restricted root system of D_IV^5 = SO_0(5,2)/[SO(5)×SO(2)]")
        print("    -- Toda lattice symmetry group")
        print("    -- 3+1 spacetime from root multiplicities: (m_short, m_long) = (3,1)")
        print("    -- Channel capacity: C = dim_R = 10 nats")
        print()
        print(f"  Remarkable: rank(E8) = |W(B2)| = {WEYL_B2}")
        print(f"  The Cartan dimension of E8 equals the soliton Weyl group order.")

        return {
            'root_system': 'B2',
            'rank': 2,
            'weyl_order': WEYL_B2,
            'coxeter': 4,
            'elements': elements,
            'labels': labels,
            'm_short': M_SHORT,
            'm_long': M_LONG,
        }

    # ─── 6. Unification ratio ───

    def unification_ratio(self) -> dict:
        """
        The central identity: 1920/8 = 240 = |Φ(E₈)|.

        This factorizes through A₃:
            1920/8 = (1920/24) × (24/8) = 80 × 3

        The factor of 3 = N_c is the color number.
        The factor of 80 is [W(D₅):W(A₃)].
        """
        print()
        print("  THE UNIFICATION RATIO")
        print("  =====================")
        print()
        print(f"  |W(D5)| / |W(B2)| = {WEYL_D5} / {WEYL_B2} = {RATIO}")
        print(f"                     = |Phi(E8)| = 240")
        print()
        print("  This factorizes through A3 = su(4):")
        print()
        print(f"    {WEYL_D5}/{WEYL_B2} = ({WEYL_D5}/{WEYL_A3}) "
              f"x ({WEYL_A3}/{WEYL_B2})")
        print(f"        = {WEYL_D5 // WEYL_A3} x {WEYL_A3 // WEYL_B2}")
        print(f"        = 80 x N_c")
        print()
        print("  The chain of inclusions:")
        print()
        print("    D5 x B2  ⊂  D5 x A3  ⊂  E8")
        print()
        print(f"    B2 ⊂ A3:  A3 = D3 = so(6), B2 = so(5) ⊂ so(6)")
        print(f"              Weyl index = {WEYL_A3}/{WEYL_B2} = {N_c} = N_c")
        print()
        print(f"    D5 x A3 ⊂ E8:  Maximal rank regular subalgebra (Dynkin 1952)")
        print(f"                    rank(D5) + rank(A3) = 5 + 3 = 8 = rank(E8)")
        print()
        print("  Interpretation:")
        print(f"    240 = number of distinct particle-sector configurations")
        print(f"    visible from a single soliton-sector viewpoint.")
        print(f"    Each E8 root is a direction in the 8D Cartan subalgebra")
        print(f"    that combines particle (D5) and soliton (A3 ⊃ B2) quantum numbers.")
        print()
        print("  E8 is NOT a gauge symmetry in BST. It is the algebraic")
        print("  structure that naturally contains both sectors. The 240 = 1920/8")
        print("  identity is the shadow of this containment.")

        return {
            'ratio': RATIO,
            'factorization': (WEYL_D5 // WEYL_A3, N_c),
            'chain': 'D5 x B2 ⊂ D5 x A3 ⊂ E8',
            'color_factor': N_c,
        }

    # ─── 7. E₈ properties ───

    def e8_properties(self) -> dict:
        """
        Properties of E₈ — the largest exceptional simple Lie algebra.
        """
        print()
        print("  E8 PROPERTIES")
        print("  =============")
        print()
        print(f"  Rank:              {E8_RANK}")
        print(f"  Dimension:         {E8_DIM} = {E8_ROOTS} roots + {E8_RANK} Cartan")
        print(f"  Roots:             {E8_ROOTS}")
        print(f"  Coxeter number:    {E8_COXETER}")
        print(f"  Dual Coxeter:      {E8_DUAL_COXETER}")
        print(f"  Exponents:         {E8_EXPONENTS}")
        print()
        print("  Integer coincidences with BST:")
        print()
        print(f"    rank(E8) = {E8_RANK} = |W(B2)| = {WEYL_B2}")
        print(f"    dim(E8)  = {E8_DIM} = |Phi(E8)| + rank(E8) = {E8_ROOTS} + {E8_RANK}")
        print(f"    |Phi(E8)|= {E8_ROOTS} = |W(D5)|/|W(B2)| = {WEYL_D5}/{WEYL_B2}")
        print(f"    h(E8)    = {E8_COXETER} = 6 x 5 = C2 x n_C")
        print()
        print("  The E8 lattice:")
        print("    -- Unique even unimodular lattice in 8 dimensions")
        print("    -- 240 minimal vectors = roots of E8")
        print("    -- Densest lattice packing in 8D (Viazovska 2016, Fields 2022)")
        print("    -- Kissing number: 240 (each sphere touches 240 others)")
        print()
        print("  E8 x E8 is the gauge group of the heterotic string.")
        print("  In BST, E8 is latent, not active — the universe lives")
        print("  inside E8, but does not gauge it.")

        return {
            'rank': E8_RANK,
            'dim': E8_DIM,
            'roots': E8_ROOTS,
            'coxeter': E8_COXETER,
            'exponents': E8_EXPONENTS,
            'coincidences': {
                'rank_eq_W_B2': E8_RANK == WEYL_B2,
                'roots_eq_ratio': E8_ROOTS == RATIO,
                'coxeter_eq_C2_nC': E8_COXETER == C2 * n_C,
            }
        }

    # ─── 8. Dynkin diagram ───

    def dynkin_diagram(self) -> dict:
        """
        The E₈ Dynkin diagram with D₅ and A₃ subdiagrams highlighted.

        E₈ Dynkin diagram (Bourbaki labeling):

            1 — 3 — 4 — 5 — 6 — 7 — 8
                    |
                    2

        Removing node 5 gives D₅ (nodes 1,2,3,4,5*→A branch) × A₃ (nodes 6,7,8).
        Actually the standard maximal subalgebra decomposition removes a node
        from the EXTENDED (affine) E₈ diagram to get D₅ × A₃.
        """
        print()
        print("  E8 DYNKIN DIAGRAM")
        print("  =================")
        print()
        print("  Standard E8 (Bourbaki numbering):")
        print()
        print("        1 --- 3 --- 4 --- 5 --- 6 --- 7 --- 8")
        print("                    |")
        print("                    2")
        print()
        print("  Extended (affine) E8^(1) — add node 0:")
        print()
        print("    0 --- 1 --- 3 --- 4 --- 5 --- 6 --- 7 --- 8")
        print("                      |")
        print("                      2")
        print()
        print("  Remove node 5 from the extended diagram:")
        print()
        print("    [D5 sector]              [A3 sector]")
        print("    0 --- 1 --- 3 --- 4      6 --- 7 --- 8")
        print("                |")
        print("                2")
        print()
        print("    D5 = nodes {0,1,2,3,4}    A3 = nodes {6,7,8}")
        print("    rank 5                     rank 3")
        print("    dim 45                     dim 15")
        print()
        print("  This is Dynkin's maximal rank regular subalgebra theorem.")
        print("  E8 -> D5 x A3 = SO(10) x SU(4).")
        print()
        print("  B2 sits inside A3:")
        print("    A3 = D3 = so(6) ⊃ B2 = so(5)")
        print("    [W(A3):W(B2)] = 24/8 = 3 = N_c")

        return {
            'nodes_D5': [0, 1, 2, 3, 4],
            'nodes_A3': [6, 7, 8],
            'removed': 5,
            'subalgebra': 'D5 x A3',
        }

    # ─── 9. Summary ───

    def summary(self) -> dict:
        """
        The key insight: the ratio of particle world to soliton world IS E₈.
        """
        roots = self._ensure_roots()

        print()
        print("  ╔════════════════════════════════════════════════════════╗")
        print("  ║          THE E8 UNIFICATION — SUMMARY                ║")
        print("  ║          *** EXPLORATORY ***                         ║")
        print("  ╠════════════════════════════════════════════════════════╣")
        print("  ║                                                      ║")
        print("  ║  D5 (particle sector): |W(D5)| = 1920               ║")
        print("  ║  B2 (soliton sector):  |W(B2)| =    8               ║")
        print("  ║                                                      ║")
        print("  ║  Ratio: 1920 / 8 = 240 = |Phi(E8)|                 ║")
        print("  ║                                                      ║")
        print("  ║  The ratio of particle world to soliton world       ║")
        print("  ║  IS E8 — the largest exceptional Lie group.         ║")
        print("  ║                                                      ║")
        print("  ╠════════════════════════════════════════════════════════╣")
        print("  ║                                                      ║")
        print("  ║  Chain: D5 x B2 ⊂ D5 x A3 ⊂ E8                    ║")
        print("  ║                                                      ║")
        print("  ║  [W(A3):W(B2)] = 3 = N_c  (the color number)       ║")
        print("  ║                                                      ║")
        print("  ║  rank(E8) = 8 = |W(B2)|                            ║")
        print("  ║  h(E8) = 30 = C2 x n_C = 6 x 5                    ║")
        print("  ║                                                      ║")
        print("  ║  240 roots verified: 40 + 12 + 60 + 64 + 64        ║")
        print("  ║  = D5 adj + A3 adj + mixed + spinor + conj spinor  ║")
        print("  ║                                                      ║")
        print("  ║  The 16 of SO(10) = one generation of fermions      ║")
        print("  ║  tensored with 4 of SU(4) in E8 decomposition      ║")
        print("  ║                                                      ║")
        print("  ╚════════════════════════════════════════════════════════╝")
        print()
        print("  E8 is not a gauge symmetry in BST.")
        print("  It is the structure the universe lives inside.")
        print("  The 240 = 1920/8 identity is the shadow of containment.")

        return {
            'identity': f'{WEYL_D5}/{WEYL_B2} = {RATIO} = |Phi(E8)|',
            'chain': 'D5 x B2 ⊂ D5 x A3 ⊂ E8',
            'roots_verified': len(roots) == 240,
            'color_index': N_c,
            'status': 'EXPLORATORY',
        }

    # ─── 10. Show (4-panel visualization) ───

    def show(self):
        """
        Launch the 4-panel visualization:
            Panel 1: E₈ root projection (Petrie polygon / 2D projection)
            Panel 2: Weyl group comparison (D₅ vs B₂)
            Panel 3: Dynkin diagram with subdiagrams
            Panel 4: Unification schematic
        """
        try:
            import matplotlib
            matplotlib.use('TkAgg')
            import matplotlib.pyplot as plt
            import matplotlib.patheffects as pe
        except ImportError:
            print("  matplotlib not available. Use text API methods instead.")
            return

        roots = self._ensure_roots()
        decomp = self._ensure_decomposition()

        fig = plt.figure(figsize=(18, 12), facecolor='#0a0a1a')
        if fig.canvas.manager:
            fig.canvas.manager.set_window_title(
                'BST Toy 69 — The E8 Root Unifier [EXPLORATORY]')

        fig.text(0.5, 0.975, 'THE E\u2088 ROOT UNIFIER',
                 fontsize=24, fontweight='bold', color='#ff8800',
                 ha='center', fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=2, foreground='#442200')])
        fig.text(0.5, 0.95,
                 '|W(D\u2085)| / |W(B\u2082)| = 1920 / 8 = 240 = '
                 '|\u03a6(E\u2088)|'
                 '     [EXPLORATORY]',
                 fontsize=11, color='#aa6600', ha='center',
                 fontfamily='monospace')
        fig.text(0.5, 0.012,
                 'Copyright (c) 2026 Casey Koons \u2014 Demonstration Only  |  '
                 'Claude Opus 4.6',
                 fontsize=8, color='#334444', ha='center',
                 fontfamily='monospace')

        # ─── Panel 1: E₈ root projection (Petrie polygon) ───
        ax1 = fig.add_axes([0.04, 0.52, 0.44, 0.40])
        ax1.set_facecolor('#0a0a1a')
        ax1.set_aspect('equal')
        self._draw_root_projection(ax1, roots, decomp)

        # ─── Panel 2: Weyl group comparison ───
        ax2 = fig.add_axes([0.54, 0.52, 0.44, 0.40])
        ax2.set_facecolor('#0a0a1a')
        self._draw_weyl_comparison(ax2)

        # ─── Panel 3: Dynkin diagram ───
        ax3 = fig.add_axes([0.04, 0.05, 0.44, 0.40])
        ax3.set_facecolor('#0a0a1a')
        self._draw_dynkin(ax3)

        # ─── Panel 4: Unification schematic ───
        ax4 = fig.add_axes([0.54, 0.05, 0.44, 0.40])
        ax4.set_facecolor('#0a0a1a')
        self._draw_unification_schematic(ax4)

        plt.show()

    def _draw_root_projection(self, ax, roots, decomp):
        """
        Project E₈ roots to 2D using Petrie polygon projection.

        The Petrie projection uses specific plane angles to display
        the full 30-fold symmetry (Coxeter number h = 30).
        """
        # Petrie projection: use angles 2*pi*k/30 for the 8 coordinates
        # This reveals the h=30 symmetry of E₈
        angles = np.array([2 * np.pi * k / 30 for k in range(8)])
        proj_x = np.cos(angles)
        proj_y = np.sin(angles)

        x = roots @ proj_x
        y = roots @ proj_y

        # Color by decomposition sector
        sector_colors = {
            'D5_adjoint': '#4488ff',
            'A3_adjoint': '#44ff88',
            'mixed': '#ffaa44',
            'spinor_plus': '#ff4488',
            'spinor_minus': '#ff88cc',
        }
        sector_labels = {
            'D5_adjoint': f'D\u2085 adj ({len(decomp["D5_adjoint"])})',
            'A3_adjoint': f'A\u2083 adj ({len(decomp["A3_adjoint"])})',
            'mixed': f'Mixed ({len(decomp["mixed"])})',
            'spinor_plus': f'Spinor+ ({len(decomp["spinor_plus"])})',
            'spinor_minus': f'Spinor\u2212 ({len(decomp["spinor_minus"])})',
        }

        # Build a color array for all roots
        # We need to identify which sector each root belongs to
        root_colors = []
        for r in roots:
            found = False
            for key in ['D5_adjoint', 'A3_adjoint', 'mixed',
                        'spinor_plus', 'spinor_minus']:
                if len(decomp[key]) > 0:
                    diffs = np.sum(np.abs(decomp[key] - r), axis=1)
                    if np.any(diffs < 1e-10):
                        root_colors.append(sector_colors[key])
                        found = True
                        break
            if not found:
                root_colors.append('#666666')

        # Plot each sector
        for key in ['D5_adjoint', 'A3_adjoint', 'mixed',
                    'spinor_plus', 'spinor_minus']:
            if len(decomp[key]) > 0:
                sx = decomp[key] @ proj_x
                sy = decomp[key] @ proj_y
                ax.scatter(sx, sy, c=sector_colors[key], s=12, alpha=0.7,
                           label=sector_labels[key], zorder=3, edgecolors='none')

        # Draw connecting lines between nearby roots (nearest neighbors)
        # For visual effect, connect roots that differ by a root
        max_r = np.max(np.abs(x)) * 1.15
        ax.set_xlim(-max_r, max_r)
        ax.set_ylim(-max_r, max_r)

        ax.set_title('E\u2088 ROOTS \u2014 PETRIE PROJECTION (h=30 symmetry)',
                      color='#ff8800', fontfamily='monospace', fontsize=11,
                      fontweight='bold', pad=8)

        ax.legend(loc='lower right', fontsize=7, facecolor='#0a0a1a',
                  edgecolor='#333344', labelcolor='#cccccc',
                  framealpha=0.9)

        # Draw a faint 30-gon to show the Coxeter symmetry
        theta_30 = np.linspace(0, 2 * np.pi, 31)
        r_30 = max_r * 0.92
        ax.plot(r_30 * np.cos(theta_30), r_30 * np.sin(theta_30),
                color='#222244', linewidth=0.5, linestyle='--', alpha=0.4)

        ax.text(0, 0, '240', fontsize=20, color='#ff8800', alpha=0.3,
                ha='center', va='center', fontfamily='monospace',
                fontweight='bold')

        for spine in ax.spines.values():
            spine.set_color('#222244')
        ax.tick_params(colors='#444466', labelsize=7)

    def _draw_weyl_comparison(self, ax):
        """Draw bar comparison of Weyl group orders."""
        import matplotlib.pyplot as plt
        ax.axis('off')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        ax.set_title('WEYL GROUP ORDERS',
                      color='#ff8800', fontfamily='monospace', fontsize=11,
                      fontweight='bold', pad=8)

        # D₅ bar
        bar_width = 3.0
        d5_height = 7.5   # scaled
        b2_height = d5_height * (WEYL_B2 / WEYL_D5)  # tiny

        # D₅ bar
        ax.add_patch(plt.Rectangle((1.5, 1.0), bar_width, d5_height,
                                    facecolor='#4488ff', alpha=0.7,
                                    edgecolor='#6699ff', linewidth=1.5))
        ax.text(3.0, 1.0 + d5_height + 0.3, f'|W(D\u2085)|\n= {WEYL_D5}',
                fontsize=12, color='#4488ff', ha='center',
                fontfamily='monospace', fontweight='bold')
        ax.text(3.0, 0.5, 'PARTICLE', fontsize=9, color='#4488ff',
                ha='center', fontfamily='monospace')

        # B₂ bar (very small relative to D₅)
        b2_display_height = max(b2_height, 0.15)
        ax.add_patch(plt.Rectangle((5.5, 1.0), bar_width, b2_display_height,
                                    facecolor='#ff4488', alpha=0.7,
                                    edgecolor='#ff6699', linewidth=1.5))
        ax.text(7.0, 1.0 + b2_display_height + 0.3, f'|W(B\u2082)|\n= {WEYL_B2}',
                fontsize=12, color='#ff4488', ha='center',
                fontfamily='monospace', fontweight='bold')
        ax.text(7.0, 0.5, 'SOLITON', fontsize=9, color='#ff4488',
                ha='center', fontfamily='monospace')

        # Ratio arrow and label
        ax.annotate('', xy=(7.0, 4.5), xytext=(3.0, 4.5),
                    arrowprops=dict(arrowstyle='<->', color='#ffaa00',
                                    lw=2.0))
        ax.text(5.0, 5.0, f'RATIO = {RATIO}',
                fontsize=14, fontweight='bold', color='#ffaa00',
                ha='center', fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#2a1a0a',
                          edgecolor='#ffaa00', linewidth=1.5))
        ax.text(5.0, 4.0, f'= |\u03a6(E\u2088)|',
                fontsize=12, color='#ffaa00', ha='center',
                fontfamily='monospace')

        # Factorization
        ax.text(5.0, 2.5, f'{WEYL_D5}/{WEYL_B2} = '
                f'({WEYL_D5}/{WEYL_A3}) \u00d7 ({WEYL_A3}/{WEYL_B2}) '
                f'= 80 \u00d7 3',
                fontsize=9, color='#888866', ha='center',
                fontfamily='monospace')
        ax.text(5.0, 2.0, f'N_c = 3 is the color factor',
                fontsize=9, color='#888866', ha='center',
                fontfamily='monospace')

    def _draw_dynkin(self, ax):
        """Draw E₈ Dynkin diagram with D₅ and A₃ subdiagrams highlighted."""
        ax.axis('off')
        ax.set_xlim(-0.5, 10.5)
        ax.set_ylim(-1.5, 4.5)

        ax.set_title('E\u2088 DYNKIN DIAGRAM \u2014 D\u2085 \u00d7 A\u2083 '
                      'DECOMPOSITION',
                      color='#ff8800', fontfamily='monospace', fontsize=11,
                      fontweight='bold', pad=8)

        # Extended E₈ nodes: 0--1--3--4--5--6--7--8, with 2 branching from 4
        # But for the standard E₈ (not extended), nodes are 1-8:
        #   1--3--4--5--6--7--8 with 2 branching from 4

        # For the decomposition, we show the extended diagram
        # and highlight which nodes go to D₅ and A₃

        # Node positions (extended E₈^(1))
        node_pos = {
            0: (0.5, 2.5),
            1: (2.0, 2.5),
            3: (3.5, 2.5),
            4: (5.0, 2.5),
            5: (6.5, 2.5),   # THIS ONE GETS REMOVED
            6: (8.0, 2.5),
            7: (9.5, 2.5),
            8: (10.0, 2.5),  # adjust spacing
            2: (3.5, 1.0),   # branch below node 3 (Bourbaki: branch from 4)
        }
        # Re-layout for clarity
        node_pos = {
            0: (0.5, 2.5),
            1: (1.8, 2.5),
            3: (3.1, 2.5),
            2: (3.1, 1.0),    # branch below 3
            4: (4.4, 2.5),
            5: (5.7, 2.5),    # REMOVED
            6: (7.0, 2.5),
            7: (8.3, 2.5),
            8: (9.6, 2.5),
        }

        # Edges in extended E₈
        edges = [(0, 1), (1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8),
                 (3, 2)]

        # D₅ nodes and A₃ nodes
        d5_nodes = {0, 1, 2, 3, 4}
        a3_nodes = {6, 7, 8}
        removed = {5}

        # Draw edges first
        for n1, n2 in edges:
            x1, y1 = node_pos[n1]
            x2, y2 = node_pos[n2]
            if n1 in removed or n2 in removed:
                # Dashed line for removed connection
                ax.plot([x1, x2], [y1, y2], '--', color='#333344',
                        linewidth=1.5, alpha=0.5)
            elif n1 in d5_nodes and n2 in d5_nodes:
                ax.plot([x1, x2], [y1, y2], '-', color='#4488ff',
                        linewidth=2.5)
            elif n1 in a3_nodes and n2 in a3_nodes:
                ax.plot([x1, x2], [y1, y2], '-', color='#44ff88',
                        linewidth=2.5)
            else:
                ax.plot([x1, x2], [y1, y2], '-', color='#666666',
                        linewidth=1.5)

        # Draw nodes
        for node_id, (x, y) in node_pos.items():
            if node_id in removed:
                # Removed node — show as X
                ax.plot(x, y, 'x', color='#ff3333', markersize=18,
                        markeredgewidth=3, zorder=5)
                ax.text(x, y + 0.4, str(node_id), fontsize=9,
                        color='#ff3333', ha='center', fontfamily='monospace')
                ax.text(x, y - 0.5, 'CUT', fontsize=8,
                        color='#ff3333', ha='center', fontfamily='monospace',
                        fontweight='bold')
            elif node_id in d5_nodes:
                ax.plot(x, y, 'o', color='#4488ff', markersize=20, zorder=5,
                        markeredgecolor='#6699ff', markeredgewidth=2)
                ax.text(x, y, str(node_id), fontsize=10,
                        color='white', ha='center', va='center',
                        fontfamily='monospace', fontweight='bold', zorder=6)
            elif node_id in a3_nodes:
                ax.plot(x, y, 'o', color='#44ff88', markersize=20, zorder=5,
                        markeredgecolor='#66ffaa', markeredgewidth=2)
                ax.text(x, y, str(node_id), fontsize=10,
                        color='white', ha='center', va='center',
                        fontfamily='monospace', fontweight='bold', zorder=6)

        # Labels
        ax.text(2.2, 3.5, 'D\u2085 = SO(10)', fontsize=12, color='#4488ff',
                ha='center', fontfamily='monospace', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#0a1a3a',
                          edgecolor='#4488ff', alpha=0.8))
        ax.text(8.3, 3.5, 'A\u2083 = SU(4)', fontsize=12, color='#44ff88',
                ha='center', fontfamily='monospace', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#0a2a1a',
                          edgecolor='#44ff88', alpha=0.8))

        # B₂ inside A₃
        ax.text(8.3, 0.5, 'B\u2082 = SO(5) \u2282 A\u2083 = SO(6)\n'
                '[W(A\u2083):W(B\u2082)] = 24/8 = 3 = N_c',
                fontsize=8, color='#ff4488', ha='center',
                fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a0a1a',
                          edgecolor='#ff4488', alpha=0.7))

        # Rank annotation
        ax.text(2.2, -0.5, 'rank 5', fontsize=9, color='#4488ff',
                ha='center', fontfamily='monospace')
        ax.text(8.3, -0.5, 'rank 3', fontsize=9, color='#44ff88',
                ha='center', fontfamily='monospace')
        ax.text(5.7, -0.5, '5 + 3 = 8 = rank(E\u2088)', fontsize=9,
                color='#ffaa00', ha='center', fontfamily='monospace')

    def _draw_unification_schematic(self, ax):
        """Draw the unification schematic connecting all sectors."""
        ax.axis('off')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        ax.set_title('THE UNIFICATION',
                      color='#ff8800', fontfamily='monospace', fontsize=11,
                      fontweight='bold', pad=8)

        # Central E₈ label
        ax.text(5.0, 8.5, 'E\u2088', fontsize=36, fontweight='bold',
                color='#ffaa00', ha='center', va='center',
                fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=3, foreground='#553300')])
        ax.text(5.0, 7.5, 'dim 248  |  rank 8  |  240 roots',
                fontsize=9, color='#aa8844', ha='center',
                fontfamily='monospace')

        # D₅ box (left)
        ax.text(2.0, 5.5, 'D\u2085 = SO(10)', fontsize=13,
                fontweight='bold', color='#4488ff', ha='center',
                fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#0a1a3a',
                          edgecolor='#4488ff', linewidth=2))
        ax.text(2.0, 4.5, '|W(D\u2085)| = 1920', fontsize=11,
                color='#6699ff', ha='center', fontfamily='monospace')
        ax.text(2.0, 3.8, 'PARTICLE SECTOR', fontsize=9,
                color='#4488ff', ha='center', fontfamily='monospace')
        ax.text(2.0, 3.1, 'm_p/m_e = 6\u03c0\u2075', fontsize=10,
                color='#88aaff', ha='center', fontfamily='monospace')
        ax.text(2.0, 2.4, 'baryon orbit', fontsize=9,
                color='#6688aa', ha='center', fontfamily='monospace')

        # A₃ box (right)
        ax.text(8.0, 5.5, 'A\u2083 = SU(4)', fontsize=13,
                fontweight='bold', color='#44ff88', ha='center',
                fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#0a2a1a',
                          edgecolor='#44ff88', linewidth=2))
        ax.text(8.0, 4.5, '|W(A\u2083)| = 24', fontsize=11,
                color='#66ffaa', ha='center', fontfamily='monospace')
        ax.text(8.0, 3.8, 'HIDDEN SECTOR', fontsize=9,
                color='#44ff88', ha='center', fontfamily='monospace')
        ax.text(8.0, 3.1, 'contains B\u2082', fontsize=10,
                color='#88ffaa', ha='center', fontfamily='monospace')
        ax.text(8.0, 2.4, 'soliton symmetry', fontsize=9,
                color='#669988', ha='center', fontfamily='monospace')

        # B₂ box (below A₃)
        ax.text(8.0, 1.2, 'B\u2082\n|W| = 8', fontsize=10,
                color='#ff4488', ha='center', fontfamily='monospace',
                fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a0a1a',
                          edgecolor='#ff4488', linewidth=1.5))

        # Arrows
        # E₈ → D₅
        ax.annotate('', xy=(2.0, 6.3), xytext=(3.5, 7.2),
                    arrowprops=dict(arrowstyle='->', color='#4488ff',
                                    lw=2.0, connectionstyle='arc3,rad=0.1'))
        # E₈ → A₃
        ax.annotate('', xy=(8.0, 6.3), xytext=(6.5, 7.2),
                    arrowprops=dict(arrowstyle='->', color='#44ff88',
                                    lw=2.0, connectionstyle='arc3,rad=-0.1'))
        # A₃ → B₂
        ax.annotate('', xy=(8.0, 1.8), xytext=(8.0, 2.2),
                    arrowprops=dict(arrowstyle='->', color='#ff4488',
                                    lw=1.5))
        ax.text(9.2, 2.0, 'index 3\n= N_c', fontsize=8,
                color='#ff4488', fontfamily='monospace')

        # The ratio connection
        ax.annotate('', xy=(6.5, 4.5), xytext=(3.5, 4.5),
                    arrowprops=dict(arrowstyle='<->', color='#ffaa00',
                                    lw=2.5))
        ax.text(5.0, 5.0, f'1920 / 8 = 240', fontsize=11,
                fontweight='bold', color='#ffaa00', ha='center',
                fontfamily='monospace')
        ax.text(5.0, 4.3, '= |\u03a6(E\u2088)|', fontsize=10,
                color='#ffaa00', ha='center', fontfamily='monospace')

        # Bottom insight
        ax.text(5.0, 0.3, '"The ratio of particle world to '
                'soliton world IS E\u2088"',
                fontsize=10, color='#ffcc44', ha='center',
                fontfamily='monospace', fontstyle='italic',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a1a0a',
                          edgecolor='#ffcc44', linewidth=1.5, alpha=0.8))


# ═══════════════════════════════════════════════════════════════════
# MAIN MENU
# ═══════════════════════════════════════════════════════════════════

def main():
    u = E8Unifier()

    print()
    print("  What would you like to explore?")
    print("   1) Weyl group orders (D5, B2, ratio)")
    print("   2) E8 root system (construct 240 roots)")
    print("   3) Root count verification (D5 x A3 decomposition)")
    print("   4) D5 particle sector")
    print("   5) B2 soliton sector")
    print("   6) Unification ratio (1920/8 = 240)")
    print("   7) E8 properties")
    print("   8) Dynkin diagram")
    print("   9) Summary")
    print("  10) 4-panel visualization")
    print("  11) Everything + visualization")
    print()

    try:
        choice = input("  Choice [1-11]: ").strip()
    except (EOFError, KeyboardInterrupt):
        choice = '11'

    dispatch = {
        '1': u.weyl_orders,
        '2': u.e8_roots,
        '3': u.root_count,
        '4': u.d5_sector,
        '5': u.b2_sector,
        '6': u.unification_ratio,
        '7': u.e8_properties,
        '8': u.dynkin_diagram,
        '9': u.summary,
        '10': u.show,
    }

    if choice == '11':
        u.weyl_orders()
        u.e8_roots()
        u.root_count()
        u.d5_sector()
        u.b2_sector()
        u.unification_ratio()
        u.e8_properties()
        u.dynkin_diagram()
        u.summary()
        try:
            u.show()
            input("\n  Press Enter to close...")
        except Exception:
            pass
    elif choice in dispatch:
        result = dispatch[choice]()
        if choice == '10':
            try:
                input("\n  Press Enter to close...")
            except Exception:
                pass
    else:
        u.summary()


if __name__ == '__main__':
    main()
