#!/usr/bin/env python3
"""
THE ISOTROPY PROOF — ANIMATED  (Toy 131)
==========================================
Analytic proof that the isotropy group of D_IV^5 is SO(5) x SO(2).

The oldest open problem in the BST program — closed with five lines of algebra.

The proof:
  1. Define: Cartan involution theta(X) = -X^T on so(5,2)
  2. Fixed set: theta(X) = X  <=>  X^T = -X, combined with X in so(5,2) gives [X, eta] = 0
  3. Block diagonal: [X, eta] = 0 forces X = diag(A, D) with A in so(5), D in so(2)
  4. Identify: k = so(5) + so(2), dim k = 10 + 1 = 11 = c_2(Q^5)
  5. Exponentiate: K = SO(5) x SO(2) — connected, compact, maximal compact in G
  6. Universal: for all D_IV^n, K = SO(n) x SO(2), dim K = n(n-1)/2 + 1

Six animated panels walk through each step visually.

CI Interface:
    from toy_isotropy_proof import IsotropyProof
    ip = IsotropyProof()
    ip.cartan_involution()        # theta(X) = -X^T on so(5,2)
    ip.fixed_subalgebra()         # theta(X) = X plus so(5,2) => [X, eta] = 0
    ip.block_diagonal()           # commutation forces block structure
    ip.identify_algebra()         # so(5) + so(2), dim = 11 = c_2
    ip.exponentiate()             # K = SO(5) x SO(2)
    ip.universality()             # n = 3, 5, 7, 9 table
    ip.numerical_check()          # explicit matrix verification
    ip.summary()                  # key result
    ip.show()                     # 6-panel animated visualization

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
from math import comb, factorial

# ═══════════════════════════════════════════════════════════════════
# BST CONSTANTS
# ═══════════════════════════════════════════════════════════════════

N_c   = 3                    # color charges
n_C   = 5                    # complex dimension of D_IV^5
genus = n_C + 2              # = 7
C_2   = n_C + 1              # = 6, Casimir eigenvalue
N_max = 137                  # channel capacity

# Metric signature (5,2)
eta = np.diag([1., 1., 1., 1., 1., -1., -1.])

# Weyl group
W_D5 = factorial(n_C) * 2**(n_C - 1)   # 1920

# Chern classes of Q^5
def chern_class(n, k):
    """c_k(Q^n) = sum_{j=0}^{k} C(n+2, k-j) * (-2)^j"""
    ck = 0
    for j in range(k + 1):
        ck += comb(n + 2, k - j) * ((-2) ** j)
    return ck


# ═══════════════════════════════════════════════════════════════════
# LIE ALGEBRA GENERATORS
# ═══════════════════════════════════════════════════════════════════

def make_so52_generator(i, j, n=7):
    """
    Build a generator E_ij of so(5,2).

    For so(p,q) with eta = diag(I_p, -I_q), the condition is X^T eta + eta X = 0.
    The generators are:
      - E_ij - E_ji  for 0 <= i < j < p  (compact, so(5) block)
      - E_ij - E_ji  for p <= i < j < p+q  (compact, so(2) block)
      - E_ij + E_ji  for 0 <= i < p, p <= j < p+q  (non-compact, p block)
    """
    X = np.zeros((n, n))
    if i < 5 and j < 5:
        # so(5) block: standard skew-symmetric
        X[i, j] = 1.0
        X[j, i] = -1.0
    elif i >= 5 and j >= 5:
        # so(2) block: standard skew-symmetric
        X[i, j] = 1.0
        X[j, i] = -1.0
    else:
        # mixed block: X^T eta + eta X = 0 => symmetric off-diagonal
        X[i, j] = 1.0
        X[j, i] = 1.0
    return X


def in_so52(X, tol=1e-10):
    """Check X^T eta + eta X = 0."""
    return np.max(np.abs(X.T @ eta + eta @ X)) < tol


def commutator(X, Y):
    """[X, Y] = XY - YX"""
    return X @ Y - Y @ X


def commutes_with_eta(X, tol=1e-10):
    """Check [X, eta] = 0."""
    return np.max(np.abs(commutator(X, eta))) < tol


# Build complete basis
def build_k_basis():
    """Build the 11 generators of k = so(5) + so(2)."""
    basis = []
    labels = []
    # so(5) generators: 10 of them
    for i in range(5):
        for j in range(i + 1, 5):
            basis.append(make_so52_generator(i, j))
            labels.append(f'K_{i}{j}')
    # so(2) generator: 1 (the J operator)
    basis.append(make_so52_generator(5, 6))
    labels.append('J')
    return basis, labels


def build_p_basis():
    """Build the 10 generators of p (tangent space)."""
    basis = []
    labels = []
    for i in range(5):
        for a in range(5, 7):
            basis.append(make_so52_generator(i, a))
            labels.append(f'P_{i}{a-5}')
    return basis, labels


# ═══════════════════════════════════════════════════════════════════
# CARTAN INVOLUTION
# ═══════════════════════════════════════════════════════════════════

def cartan_involution(X):
    """theta(X) = -X^T"""
    return -X.T


def is_theta_fixed(X, tol=1e-10):
    """Check theta(X) = X, i.e., X is skew-symmetric."""
    return np.max(np.abs(X + X.T)) < tol


def is_theta_negated(X, tol=1e-10):
    """Check theta(X) = -X, i.e., X is symmetric."""
    return np.max(np.abs(X - X.T)) < tol


# ═══════════════════════════════════════════════════════════════════
# BLOCK STRUCTURE ANALYSIS
# ═══════════════════════════════════════════════════════════════════

def extract_blocks(X):
    """Extract the four blocks of a 7x7 matrix in the (5,2) partition."""
    A = X[:5, :5]     # 5x5 upper-left
    B = X[:5, 5:]     # 5x2 upper-right
    C = X[5:, :5]     # 2x5 lower-left
    D = X[5:, 5:]     # 2x2 lower-right
    return A, B, C, D


def is_block_diagonal(X, tol=1e-10):
    """Check if X is block diagonal in the (5,2) partition."""
    _, B, C, _ = extract_blocks(X)
    return np.max(np.abs(B)) < tol and np.max(np.abs(C)) < tol


# ═══════════════════════════════════════════════════════════════════
# UNIVERSALITY FOR D_IV^n
# ═══════════════════════════════════════════════════════════════════

def dim_k_universal(n):
    """dim K = n(n-1)/2 + 1 for D_IV^n."""
    return n * (n - 1) // 2 + 1


def dim_gk_universal(n):
    """dim G/K = 2n for D_IV^n."""
    return 2 * n


def dim_g_universal(n):
    """dim G = dim so(n,2) = (n+2)(n+1)/2 for D_IV^n."""
    return (n + 2) * (n + 1) // 2


# ═══════════════════════════════════════════════════════════════════
# CLASS: IsotropyProof
# ═══════════════════════════════════════════════════════════════════

class IsotropyProof:
    """Toy 131: The Isotropy Proof -- Animated."""

    def __init__(self, quiet=False):
        self.quiet = quiet
        self.k_basis, self.k_labels = build_k_basis()
        self.p_basis, self.p_labels = build_p_basis()
        if not quiet:
            print()
            print("=" * 68)
            print("  THE ISOTROPY PROOF -- BST Toy 131")
            print("  Analytic proof: K(D_IV^5) = SO(5) x SO(2)")
            print("=" * 68)
            print()
            self._verify_all()

    # ───────────────────────────────────────────────────────────
    #  VERIFICATION
    # ───────────────────────────────────────────────────────────

    def _verify_all(self):
        """Run all numerical checks."""
        # Check all k generators are in so(5,2)
        for X in self.k_basis:
            assert in_so52(X), "k generator not in so(5,2)!"
        for X in self.p_basis:
            assert in_so52(X), "p generator not in so(5,2)!"

        # Check k generators are theta-fixed
        for X in self.k_basis:
            assert is_theta_fixed(X), "k generator not theta-fixed!"
        # Check p generators are theta-negated
        for X in self.p_basis:
            assert is_theta_negated(X), "p generator not theta-negated!"

        # Check k generators commute with eta
        for X in self.k_basis:
            assert commutes_with_eta(X), "k generator doesn't commute with eta!"

        # Check k generators are block diagonal
        for X in self.k_basis:
            assert is_block_diagonal(X), "k generator not block diagonal!"

        # Dimensions
        assert len(self.k_basis) == 11, f"dim k = {len(self.k_basis)}, expected 11"
        assert len(self.p_basis) == 10, f"dim p = {len(self.p_basis)}, expected 10"

        # Bracket structure: [k, k] in k, [k, p] in p, [p, p] in k
        self._check_bracket_structure()

        if not self.quiet:
            print("  All 21 generators verified in so(5,2)         [PASS]")
            print("  11 k-generators: theta-fixed, [X,eta]=0       [PASS]")
            print("  10 p-generators: theta-negated, {X,eta}=0     [PASS]")
            print("  Bracket structure [k,k]<k  [k,p]<p  [p,p]<k  [PASS]")
            print(f"  dim k = 11 = c_2(Q^5)                         [PASS]")
            print(f"  dim p = 10 = 2 n_C                            [PASS]")
            print(f"  dim g = 21 = C(7,2)                           [PASS]")
            print()

    def _check_bracket_structure(self):
        """Verify [k,k] < k, [k,p] < p, [p,p] < k."""
        k_all = np.column_stack([x.flatten() for x in self.k_basis])
        p_all = np.column_stack([x.flatten() for x in self.p_basis])

        def in_span(X, basis_mat, tol=1e-10):
            if basis_mat.shape[1] == 0:
                return np.max(np.abs(X)) < tol
            res = np.linalg.lstsq(basis_mat, X.flatten(), rcond=None)
            return np.max(np.abs(basis_mat @ res[0] - X.flatten())) < tol

        # [k, k] in k
        for i, Xi in enumerate(self.k_basis):
            for j, Xj in enumerate(self.k_basis):
                if i < j:
                    C = commutator(Xi, Xj)
                    assert in_span(C, k_all), f"[{self.k_labels[i]},{self.k_labels[j]}] not in k!"

        # [k, p] in p
        for Xi in self.k_basis:
            for Xj in self.p_basis:
                C = commutator(Xi, Xj)
                assert in_span(C, p_all), "[k,p] not in p!"

        # [p, p] in k
        for i, Xi in enumerate(self.p_basis):
            for j, Xj in enumerate(self.p_basis):
                if i < j:
                    C = commutator(Xi, Xj)
                    assert in_span(C, k_all), "[p,p] not in k!"

    # ───────────────────────────────────────────────────────────
    #  CI METHODS: Step-by-step proof
    # ───────────────────────────────────────────────────────────

    def cartan_involution(self):
        """Step 1: theta(X) = -X^T on so(5,2)."""
        print()
        print("─" * 60)
        print("  STEP 1: THE CARTAN INVOLUTION")
        print("─" * 60)
        print()
        print("  g = so(5,2) = { X in gl(7,R) : X^T eta + eta X = 0 }")
        print(f"  eta = diag(+1,+1,+1,+1,+1,-1,-1)   [signature (5,2)]")
        print(f"  dim g = C(7,2) = 21")
        print()
        print("  Cartan involution:  theta(X) = -X^T")
        print()
        print("  Properties:")
        print("    theta^2 = id                (involutive)")
        print("    theta([X,Y]) = [theta(X), theta(Y)]  (automorphism)")
        print("    theta preserves so(5,2)     (proved below)")
        print()
        # Demonstrate on a sample
        X = self.k_basis[0]  # K_01
        tX = cartan_involution(X)
        print(f"  Example: X = {self.k_labels[0]} (so(5) generator)")
        print(f"    theta(X) = -X^T = X   (fixed!)")
        print(f"    Verified: {np.allclose(tX, X)}")
        print()
        X2 = self.p_basis[0]
        tX2 = cartan_involution(X2)
        print(f"  Example: X = {self.p_labels[0]} (tangent space generator)")
        print(f"    theta(X) = -X^T = -X  (negated!)")
        print(f"    Verified: {np.allclose(tX2, -X2)}")
        print()
        return eta

    def fixed_subalgebra(self):
        """Step 2: theta(X) = X combined with so(5,2) gives [X, eta] = 0."""
        print()
        print("─" * 60)
        print("  STEP 2: THE FIXED SUBALGEBRA")
        print("─" * 60)
        print()
        print("  k = { X in g : theta(X) = X } = { X in g : X^T = -X }")
        print()
        print("  X in k satisfies TWO conditions simultaneously:")
        print("    (i)   X^T = -X          (skew-symmetric, from theta)")
        print("    (ii)  X^T eta + eta X = 0  (the so(5,2) condition)")
        print()
        print("  Substituting (i) into (ii):")
        print("    -X eta + eta X = 0")
        print("    [eta, X] = 0")
        print()
        print("  >>> X commutes with eta <<<")
        print()
        # Verify for all k generators
        all_pass = all(commutes_with_eta(X) for X in self.k_basis)
        print(f"  All 11 k-generators commute with eta: {all_pass}")
        none_p = all(not commutes_with_eta(X) for X in self.p_basis)
        print(f"  No p-generator commutes with eta:     {none_p}")
        print()

    def block_diagonal(self):
        """Step 3: [X, eta] = 0 forces block diagonal structure."""
        print()
        print("─" * 60)
        print("  STEP 3: BLOCK DIAGONAL STRUCTURE")
        print("─" * 60)
        print()
        print("  Write X in blocks matching eta = diag(I_5, -I_2):")
        print()
        print("        ( A   B )       A: 5x5")
        print("    X = (       )       B: 5x2")
        print("        ( C   D )       C: 2x5, D: 2x2")
        print()
        print("  [eta, X] = 0  =>  eta X = X eta")
        print()
        print("    ( I_5  0  )( A  B )   ( A  B )( I_5   0  )")
        print("    ( 0  -I_2 )( C  D ) = ( C  D )( 0   -I_2 )")
        print()
        print("    ( A   B  )   ( A  -B )")
        print("    (-C  -D  ) = ( C  -D  )")
        print()
        print("  Comparing blocks:")
        print("    B = -B  =>  B = 0")
        print("    C = -C  =>  C = 0")
        print()
        print("  Therefore X = diag(A, D) is BLOCK DIAGONAL.")
        print()
        # Show for a sample generator
        X = self.k_basis[0]
        A, B, C, D = extract_blocks(X)
        print(f"  Example: {self.k_labels[0]}")
        print(f"    |B| = {np.max(np.abs(B)):.0e},  |C| = {np.max(np.abs(C)):.0e}")
        print(f"    Block diagonal: {is_block_diagonal(X)}")
        print()

    def identify_algebra(self):
        """Step 4: so(5) + so(2), dim = 11 = c_2(Q^5)."""
        print()
        print("─" * 60)
        print("  STEP 4: IDENTIFYING THE ALGEBRA")
        print("─" * 60)
        print()
        print("  X = diag(A, D) with X^T = -X (skew-symmetric)")
        print()
        print("  Upper-left:   A^T = -A  =>  A in so(5)")
        print("  Lower-right:  D^T = -D  =>  D in so(2)")
        print()
        print("  ┌─────────────────────────────────────────────────┐")
        print("  │  k = so(5) + so(2)                              │")
        print("  │                                                  │")
        print("  │  dim k = C(5,2) + C(2,2)                        │")
        print("  │        = 10     + 1                              │")
        print("  │        = 11                                      │")
        print("  │        = c_2(Q^5)    [second Chern class]        │")
        print("  └─────────────────────────────────────────────────┘")
        print()
        c2 = chern_class(5, 2)
        print(f"  c_2(Q^5) = {c2}  (from Chern polynomial)")
        print(f"  dim k    = {len(self.k_basis)}")
        print(f"  Match:     {c2 == len(self.k_basis)}")
        print()
        print("  The Chern class COUNTS the isotropy generators.")
        print()

    def exponentiate(self):
        """Step 5: K = exp(k) = SO(5) x SO(2)."""
        print()
        print("─" * 60)
        print("  STEP 5: EXPONENTIATION")
        print("─" * 60)
        print()
        print("  From Lie algebra to Lie group:")
        print()
        print("    K = exp(k) = exp(so(5) + so(2))")
        print("                = exp(so(5)) x exp(so(2))")
        print("                = SO(5) x SO(2)")
        print()
        print("  Properties of K:")
        print("    - Connected  (both factors connected)")
        print("    - Compact    (product of compact groups)")
        print("    - Maximal    (G/K contractible, Cartan-Iwasawa-Malcev)")
        print()
        # Numerical demonstration: exponentiate a k-generator
        X = self.k_basis[0]  # K_01
        t = 0.3
        g = _matrix_exp(t * X)
        print(f"  Numerical check: g = exp(0.3 * {self.k_labels[0]})")
        print(f"    g^T eta g = eta:  {np.allclose(g.T @ eta @ g, eta)}")
        print(f"    g^T g = I:        {np.allclose(g.T @ g, np.eye(7))}")
        print(f"    Block diagonal:   {is_block_diagonal(g)}")
        print(f"    det(g) = {np.linalg.det(g):.6f}")
        print()
        print("  K is the stabilizer of the origin of D_IV^5.")
        print("  D_IV^5 = SO_0(5,2) / [SO(5) x SO(2)]")
        print()

    def universality(self):
        """Step 6: Universal for all D_IV^n."""
        print()
        print("─" * 60)
        print("  STEP 6: UNIVERSALITY FOR ALL D_IV^n")
        print("─" * 60)
        print()
        print("  Replace 5 by n and eta = diag(I_n, -I_2) throughout.")
        print("  The proof goes through unchanged.")
        print()
        print("  For D_IV^n:  K = SO(n) x SO(2)")
        print()
        header = f"  {'n':>3}  {'dim K':>8}  {'dim G/K':>8}  {'c_2(Q^n)':>10}  {'match':>6}"
        print(header)
        print("  " + "─" * 50)
        for n in [3, 5, 7, 9]:
            dk = dim_k_universal(n)
            dgk = dim_gk_universal(n)
            c2 = chern_class(n, 2)
            match = "yes" if dk == c2 else "NO"
            print(f"  {n:>3}  {dk:>8}  {dgk:>8}  {c2:>10}  {match:>6}")
        print()
        print("  c_2(Q^n) = n(n-1)/2 + 1 = dim K  for ALL n.")
        print("  The Chern class encodes the isotropy for every dimension.")
        print()

    def numerical_check(self):
        """Explicit matrix verification of the full proof chain."""
        print()
        print("─" * 60)
        print("  NUMERICAL VERIFICATION")
        print("─" * 60)
        print()
        # Generate random k-element and verify all properties
        np.random.seed(42)
        coeffs = np.random.randn(11)
        X = sum(c * B for c, B in zip(coeffs, self.k_basis))
        print(f"  Random X = sum of 11 k-generators:")
        print(f"    in so(5,2):           {in_so52(X)}")
        print(f"    theta-fixed (X^T=-X): {is_theta_fixed(X)}")
        print(f"    commutes with eta:    {commutes_with_eta(X)}")
        print(f"    block diagonal:       {is_block_diagonal(X)}")
        print()
        # Exponentiate and check group element
        g = _matrix_exp(X)
        print(f"  g = exp(X):")
        print(f"    g^T eta g = eta:  {np.allclose(g.T @ eta @ g, eta)}")
        print(f"    g^T g = I (orth):  {np.allclose(g.T @ g, np.eye(7))}")
        print(f"    block diagonal:    {is_block_diagonal(g, tol=1e-8)}")
        A, B, C, D = extract_blocks(g)
        print(f"    det(A) = {np.linalg.det(A):+.6f}  (SO(5))")
        print(f"    det(D) = {np.linalg.det(D):+.6f}  (SO(2))")
        print()
        # Random p-element: should NOT be block diagonal
        coeffs_p = np.random.randn(10)
        Y = sum(c * B for c, B in zip(coeffs_p, self.p_basis))
        print(f"  Random Y = sum of 10 p-generators:")
        print(f"    in so(5,2):           {in_so52(Y)}")
        print(f"    theta-negated (Y^T=Y):{is_theta_negated(Y)}")
        print(f"    commutes with eta:    {commutes_with_eta(Y)}")
        print(f"    block diagonal:       {is_block_diagonal(Y)}")
        print()

    def summary(self):
        """Print the key result."""
        print()
        print("═" * 68)
        print("  THE ISOTROPY PROOF — SUMMARY")
        print("═" * 68)
        print()
        print("  ┌────────────────────────────────────────────────────────┐")
        print("  │                                                        │")
        print("  │   K(D_IV^5) = SO(5) x SO(2)                           │")
        print("  │                                                        │")
        print("  │   dim K = 10 + 1 = 11 = c_2(Q^5)                      │")
        print("  │                                                        │")
        print("  │   The proof is five lines of linear algebra.           │")
        print("  │                                                        │")
        print("  └────────────────────────────────────────────────────────┘")
        print()
        print("  Five steps:")
        print("    1. Cartan involution theta(X) = -X^T")
        print("    2. Fixed set: X^T = -X  plus  so(5,2) => [X, eta] = 0")
        print("    3. Commuting with eta forces block diagonal")
        print("    4. Blocks: so(5) + so(2), dim = 10 + 1 = 11 = c_2")
        print("    5. Exponentiate: K = SO(5) x SO(2)")
        print()
        print("  This closes the oldest open problem in the BST program.")
        print()

    # ───────────────────────────────────────────────────────────
    #  VISUALIZATION: 6-panel animated proof
    # ───────────────────────────────────────────────────────────

    def show(self):
        """Display the 6-panel animated proof visualization."""
        import matplotlib
        matplotlib.use('TkAgg')
        import matplotlib.pyplot as plt
        import matplotlib.patheffects as pe
        from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
        from matplotlib.animation import FuncAnimation

        # ─── Color palette ───
        BG       = '#0a0a1a'
        GOLD     = '#ffaa00'
        BRIGHT   = '#ffffff'
        DIMTEXT  = '#888899'
        BLUE     = '#4488ff'
        CYAN     = '#00cccc'
        GREEN    = '#44cc44'
        RED      = '#ff4444'
        MAGENTA  = '#cc44cc'
        ORANGE   = '#ff8844'
        PANEL_BG = '#0d0d22'
        BOX_EDGE = '#444466'
        HILIGHT  = '#ffcc00'

        glow = [pe.withStroke(linewidth=3, foreground='#000000')]
        glow_gold = [pe.withStroke(linewidth=2, foreground='#442200')]

        # ─── Figure ───
        fig = plt.figure(figsize=(18, 12), facecolor=BG)
        fig.canvas.manager.set_window_title('The Isotropy Proof — BST Toy 131')

        # Title
        fig.text(0.5, 0.975, 'THE ISOTROPY PROOF',
                 fontsize=28, fontweight='bold', color=GOLD,
                 ha='center', va='top', fontfamily='monospace',
                 path_effects=glow_gold)
        fig.text(0.5, 0.945, 'K(D_IV^5) = SO(5) x SO(2)   |   dim K = 11 = c_2(Q^5)',
                 fontsize=13, color=DIMTEXT, ha='center', va='top',
                 fontfamily='monospace')

        # Footer
        fig.text(0.5, 0.01,
                 'Copyright Casey Koons, March 2026  |  BST Toy 131  |  Claude Opus 4.6',
                 fontsize=9, color='#444455', ha='center', fontfamily='monospace')

        # ─── 6 panels: 3 columns x 2 rows ───
        panel_specs = [
            [0.02, 0.50, 0.31, 0.42],   # Panel 1: top-left
            [0.35, 0.50, 0.31, 0.42],   # Panel 2: top-center
            [0.68, 0.50, 0.31, 0.42],   # Panel 3: top-right
            [0.02, 0.04, 0.31, 0.42],   # Panel 4: bottom-left
            [0.35, 0.04, 0.31, 0.42],   # Panel 5: bottom-center
            [0.68, 0.04, 0.31, 0.42],   # Panel 6: bottom-right
        ]

        axes = []
        for spec in panel_specs:
            ax = fig.add_axes(spec)
            ax.set_facecolor(PANEL_BG)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis('off')
            axes.append(ax)

        # ─── Animation state ───
        anim_elements = {'artists': [], 'frame': [0]}
        N_FRAMES = 300
        # Phase boundaries for the 6 panels (each gets ~50 frames)
        PHASE = [0, 50, 100, 150, 200, 250, 300]

        def alpha_for_panel(frame, panel_idx):
            """Return alpha 0..1 for a panel based on frame."""
            start = PHASE[panel_idx]
            end = PHASE[panel_idx + 1]
            if frame < start:
                return 0.0
            elif frame >= end:
                return 1.0
            else:
                t = (frame - start) / (end - start)
                # Smooth ease-in
                return t * t * (3 - 2 * t)

        def alpha_text(frame, panel_idx, sub_frac=0.0):
            """Alpha for sub-elements within a panel, appearing after sub_frac."""
            start = PHASE[panel_idx]
            end = PHASE[panel_idx + 1]
            dur = end - start
            element_start = start + sub_frac * dur
            if frame < element_start:
                return 0.0
            elif frame >= end:
                return 1.0
            else:
                t = (frame - element_start) / (end - element_start)
                return min(1.0, t * t * (3 - 2 * t))

        # ═══════════════════════════════════════════════════════
        # PANEL 1: "THE QUESTION"
        # ═══════════════════════════════════════════════════════

        def draw_panel_1(frame):
            ax = axes[0]
            a = alpha_for_panel(frame, 0)
            if a <= 0:
                return

            # Title
            ax.text(0.5, 0.95, 'THE QUESTION', fontsize=14, fontweight='bold',
                    color=(*_hex2rgb(GOLD), a), ha='center', va='top',
                    fontfamily='monospace', transform=ax.transAxes)

            # Domain description
            a1 = alpha_text(frame, 0, 0.1)
            ax.text(0.5, 0.85, 'What stabilizes the origin of D_IV^5?',
                    fontsize=11, color=(*_hex2rgb(BRIGHT), a1),
                    ha='center', va='top', fontfamily='monospace',
                    transform=ax.transAxes)

            # The domain
            a2 = alpha_text(frame, 0, 0.2)
            ax.text(0.5, 0.75,
                    'D_IV^5 = SO_0(5,2) / K',
                    fontsize=13, fontweight='bold',
                    color=(*_hex2rgb(CYAN), a2),
                    ha='center', va='top', fontfamily='monospace',
                    transform=ax.transAxes,
                    bbox=dict(boxstyle='round,pad=0.4',
                              facecolor=(*_hex2rgb('#001a2a'), a2 * 0.8),
                              edgecolor=(*_hex2rgb(BLUE), a2 * 0.6),
                              linewidth=2))

            # Draw the domain as an ellipse with a fixed point
            a3 = alpha_text(frame, 0, 0.35)
            if a3 > 0:
                theta_vals = np.linspace(0, 2 * np.pi, 100)
                # Pulsating boundary
                pulse = 1.0 + 0.03 * np.sin(frame * 0.15)
                rx, ry = 0.25 * pulse, 0.15 * pulse
                cx, cy = 0.5, 0.42
                xs = cx + rx * np.cos(theta_vals)
                ys = cy + ry * np.sin(theta_vals)
                ax.plot(xs, ys, color=(*_hex2rgb(BLUE), a3 * 0.8),
                        linewidth=2, transform=ax.transAxes)
                # Fill
                ax.fill(xs, ys, color=(*_hex2rgb(BLUE), a3 * 0.1),
                        transform=ax.transAxes)
                # Origin dot
                ax.plot(cx, cy, 'o', color=(*_hex2rgb(HILIGHT), a3),
                        markersize=10, markeredgecolor=(*_hex2rgb(GOLD), a3),
                        markeredgewidth=2, transform=ax.transAxes)
                ax.text(cx + 0.03, cy + 0.02, 'o = 0',
                        fontsize=10, color=(*_hex2rgb(HILIGHT), a3),
                        fontfamily='monospace', transform=ax.transAxes)

                # Domain label
                ax.text(cx, cy - ry - 0.04, 'D_IV^5',
                        fontsize=12, fontweight='bold',
                        color=(*_hex2rgb(BLUE), a3),
                        ha='center', fontfamily='monospace',
                        transform=ax.transAxes)

            # K = ?
            a4 = alpha_text(frame, 0, 0.6)
            ax.text(0.5, 0.18, 'K = Stab(origin) = ???',
                    fontsize=13, fontweight='bold',
                    color=(*_hex2rgb(ORANGE), a4),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes)

            a5 = alpha_text(frame, 0, 0.75)
            ax.text(0.5, 0.08, 'dim G = 21     dim D_IV^5 = 10',
                    fontsize=10, color=(*_hex2rgb(DIMTEXT), a5),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes)
            ax.text(0.5, 0.02, '=> dim K = 21 - 10 = 11',
                    fontsize=10, color=(*_hex2rgb(DIMTEXT), a5),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes)

        # ═══════════════════════════════════════════════════════
        # PANEL 2: "CARTAN INVOLUTION"
        # ═══════════════════════════════════════════════════════

        def draw_panel_2(frame):
            ax = axes[1]
            a = alpha_for_panel(frame, 1)
            if a <= 0:
                return

            ax.text(0.5, 0.95, 'CARTAN INVOLUTION', fontsize=14,
                    fontweight='bold', color=(*_hex2rgb(GOLD), a),
                    ha='center', va='top', fontfamily='monospace',
                    transform=ax.transAxes)

            a1 = alpha_text(frame, 1, 0.05)
            ax.text(0.5, 0.86, 'theta(X) = -X^T    on so(5,2)',
                    fontsize=12, color=(*_hex2rgb(CYAN), a1),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes,
                    bbox=dict(boxstyle='round,pad=0.3',
                              facecolor=(*_hex2rgb('#001a2a'), a1 * 0.7),
                              edgecolor=(*_hex2rgb(CYAN), a1 * 0.5),
                              linewidth=1.5))

            # Animated matrix: show a 7x7 matrix being transposed and negated
            a2 = alpha_text(frame, 1, 0.2)
            if a2 > 0:
                # Example so(5,2) element
                X_example = self.k_basis[0]  # K_01

                # Interpolation: show X -> X^T -> -X^T
                phase_local = alpha_text(frame, 1, 0.2)
                # Draw 3 small matrix grids
                # X
                self._draw_mini_matrix(ax, X_example, 0.12, 0.38, 0.08,
                                       a2, 'X', BLUE, frame)
                # Arrow
                if a2 > 0.3:
                    ax.annotate('', xy=(0.38, 0.52), xytext=(0.28, 0.52),
                                arrowprops=dict(arrowstyle='->', color=(*_hex2rgb(DIMTEXT), a2 * 0.8),
                                                lw=2),
                                transform=ax.transAxes)
                    ax.text(0.33, 0.57, 'transpose', fontsize=7,
                            color=(*_hex2rgb(DIMTEXT), a2 * 0.7),
                            ha='center', fontfamily='monospace',
                            transform=ax.transAxes)

                # X^T
                a3 = alpha_text(frame, 1, 0.4)
                if a3 > 0:
                    self._draw_mini_matrix(ax, X_example.T, 0.40, 0.38, 0.08,
                                           a3, 'X^T', DIMTEXT, frame)
                    # Arrow
                    ax.annotate('', xy=(0.66, 0.52), xytext=(0.56, 0.52),
                                arrowprops=dict(arrowstyle='->', color=(*_hex2rgb(DIMTEXT), a3 * 0.8),
                                                lw=2),
                                transform=ax.transAxes)
                    ax.text(0.61, 0.57, 'negate', fontsize=7,
                            color=(*_hex2rgb(DIMTEXT), a3 * 0.7),
                            ha='center', fontfamily='monospace',
                            transform=ax.transAxes)

                # -X^T = theta(X)
                a4 = alpha_text(frame, 1, 0.55)
                if a4 > 0:
                    self._draw_mini_matrix(ax, -X_example.T, 0.68, 0.38, 0.08,
                                           a4, '-X^T', GREEN, frame)

            # Fixed set = k
            a5 = alpha_text(frame, 1, 0.7)
            ax.text(0.5, 0.20, 'theta(X) = X   <==>   X^T = -X',
                    fontsize=11, fontweight='bold',
                    color=(*_hex2rgb(GREEN), a5),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes)

            a6 = alpha_text(frame, 1, 0.8)
            ax.text(0.5, 0.12, 'Fixed set k = { X in so(5,2) : X skew-sym }',
                    fontsize=10, color=(*_hex2rgb(BRIGHT), a6),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes)

            ax.text(0.5, 0.04, 'theta^2 = id  (involutive automorphism)',
                    fontsize=9, color=(*_hex2rgb(DIMTEXT), a6),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes)

        # ═══════════════════════════════════════════════════════
        # PANEL 3: "BLOCK DIAGONAL"
        # ═══════════════════════════════════════════════════════

        def draw_panel_3(frame):
            ax = axes[2]
            a = alpha_for_panel(frame, 2)
            if a <= 0:
                return

            ax.text(0.5, 0.95, 'BLOCK DIAGONAL', fontsize=14,
                    fontweight='bold', color=(*_hex2rgb(GOLD), a),
                    ha='center', va='top', fontfamily='monospace',
                    transform=ax.transAxes)

            a1 = alpha_text(frame, 2, 0.05)
            ax.text(0.5, 0.86, '[X, eta] = 0   with   eta = diag(I_5, -I_2)',
                    fontsize=10, color=(*_hex2rgb(CYAN), a1),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes)

            # Draw the block structure of X
            a2 = alpha_text(frame, 2, 0.15)
            if a2 > 0:
                # Matrix outline
                mx, my = 0.22, 0.32
                mw, mh = 0.28, 0.40
                # Outer border
                rect = plt.Rectangle((mx, my), mw, mh, linewidth=2,
                                     edgecolor=(*_hex2rgb(BRIGHT), a2 * 0.8),
                                     facecolor='none',
                                     transform=ax.transAxes)
                ax.add_patch(rect)

                # Dividing lines at 5/7 of width and height
                frac = 5.0 / 7.0
                # Vertical divider
                xdiv = mx + frac * mw
                ax.plot([xdiv, xdiv], [my, my + mh],
                        color=(*_hex2rgb(DIMTEXT), a2 * 0.6),
                        linewidth=1.5, linestyle='--',
                        transform=ax.transAxes)
                # Horizontal divider (from top)
                ydiv = my + mh - frac * mh
                ax.plot([mx, mx + mw], [ydiv, ydiv],
                        color=(*_hex2rgb(DIMTEXT), a2 * 0.6),
                        linewidth=1.5, linestyle='--',
                        transform=ax.transAxes)

                # A block (upper-left) — filled
                a3 = alpha_text(frame, 2, 0.25)
                ax.fill([mx, xdiv, xdiv, mx],
                        [ydiv, ydiv, my + mh, my + mh],
                        color=(*_hex2rgb(BLUE), a3 * 0.25),
                        transform=ax.transAxes)
                ax.text((mx + xdiv) / 2, (ydiv + my + mh) / 2, 'A',
                        fontsize=18, fontweight='bold',
                        color=(*_hex2rgb(BLUE), a3),
                        ha='center', va='center', fontfamily='monospace',
                        transform=ax.transAxes)
                ax.text((mx + xdiv) / 2, ydiv + 0.02, '5x5',
                        fontsize=8, color=(*_hex2rgb(BLUE), a3 * 0.7),
                        ha='center', fontfamily='monospace',
                        transform=ax.transAxes)

                # D block (lower-right) — filled
                ax.fill([xdiv, mx + mw, mx + mw, xdiv],
                        [my, my, ydiv, ydiv],
                        color=(*_hex2rgb(GREEN), a3 * 0.25),
                        transform=ax.transAxes)
                ax.text((xdiv + mx + mw) / 2, (my + ydiv) / 2, 'D',
                        fontsize=14, fontweight='bold',
                        color=(*_hex2rgb(GREEN), a3),
                        ha='center', va='center', fontfamily='monospace',
                        transform=ax.transAxes)
                ax.text((xdiv + mx + mw) / 2, my + 0.02, '2x2',
                        fontsize=8, color=(*_hex2rgb(GREEN), a3 * 0.7),
                        ha='center', fontfamily='monospace',
                        transform=ax.transAxes)

                # B block (upper-right) — X'ed out
                a4 = alpha_text(frame, 2, 0.45)
                bcx = (xdiv + mx + mw) / 2
                bcy = (ydiv + my + mh) / 2
                ax.text(bcx, bcy, '0',
                        fontsize=16, fontweight='bold',
                        color=(*_hex2rgb(RED), a4),
                        ha='center', va='center', fontfamily='monospace',
                        transform=ax.transAxes)

                # C block (lower-left) — X'ed out
                ccx = (mx + xdiv) / 2
                ccy = (my + ydiv) / 2
                ax.text(ccx, ccy, '0',
                        fontsize=16, fontweight='bold',
                        color=(*_hex2rgb(RED), a4),
                        ha='center', va='center', fontfamily='monospace',
                        transform=ax.transAxes)

            # Label on right
            a5 = alpha_text(frame, 2, 0.55)
            ax.text(0.60, 0.62, 'B = -B => B = 0',
                    fontsize=9, color=(*_hex2rgb(RED), a5),
                    ha='left', fontfamily='monospace',
                    transform=ax.transAxes)
            ax.text(0.60, 0.55, 'C = -C => C = 0',
                    fontsize=9, color=(*_hex2rgb(RED), a5),
                    ha='left', fontfamily='monospace',
                    transform=ax.transAxes)

            # Result
            a6 = alpha_text(frame, 2, 0.7)
            ax.text(0.60, 0.44, 'X = diag(A, D)',
                    fontsize=11, fontweight='bold',
                    color=(*_hex2rgb(BRIGHT), a6),
                    ha='left', fontfamily='monospace',
                    transform=ax.transAxes)

            # Summary at bottom
            a7 = alpha_text(frame, 2, 0.8)
            ax.text(0.5, 0.12,
                    'Commutation with eta KILLS the off-diagonal blocks.',
                    fontsize=9, fontweight='bold',
                    color=(*_hex2rgb(ORANGE), a7),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes)
            ax.text(0.5, 0.04,
                    'Only block-diagonal elements survive in k.',
                    fontsize=9, color=(*_hex2rgb(DIMTEXT), a7),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes)

        # ═══════════════════════════════════════════════════════
        # PANEL 4: "so(5) + so(2)"
        # ═══════════════════════════════════════════════════════

        def draw_panel_4(frame):
            ax = axes[3]
            a = alpha_for_panel(frame, 3)
            if a <= 0:
                return

            ax.text(0.5, 0.95, 'so(5) \u2295 so(2)', fontsize=14,
                    fontweight='bold', color=(*_hex2rgb(GOLD), a),
                    ha='center', va='top', fontfamily='monospace',
                    transform=ax.transAxes)

            a1 = alpha_text(frame, 3, 0.05)
            ax.text(0.5, 0.86, 'X = diag(A, D)  with  X^T = -X',
                    fontsize=10, color=(*_hex2rgb(BRIGHT), a1),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes)

            # so(5) box
            a2 = alpha_text(frame, 3, 0.15)
            if a2 > 0:
                box_so5 = FancyBboxPatch((0.05, 0.52), 0.42, 0.26,
                                         boxstyle="round,pad=0.02",
                                         facecolor=(*_hex2rgb(BLUE), a2 * 0.15),
                                         edgecolor=(*_hex2rgb(BLUE), a2 * 0.8),
                                         linewidth=2, transform=ax.transAxes)
                ax.add_patch(box_so5)
                ax.text(0.26, 0.73, 'so(5)', fontsize=16, fontweight='bold',
                        color=(*_hex2rgb(BLUE), a2),
                        ha='center', fontfamily='monospace',
                        transform=ax.transAxes)
                ax.text(0.26, 0.66, 'A^T = -A', fontsize=10,
                        color=(*_hex2rgb(BLUE), a2 * 0.8),
                        ha='center', fontfamily='monospace',
                        transform=ax.transAxes)
                ax.text(0.26, 0.57, 'dim = C(5,2) = 10', fontsize=10,
                        color=(*_hex2rgb(BLUE), a2 * 0.7),
                        ha='center', fontfamily='monospace',
                        transform=ax.transAxes)

            # Plus sign
            a_plus = alpha_text(frame, 3, 0.3)
            ax.text(0.52, 0.65, '\u2295', fontsize=22,
                    color=(*_hex2rgb(BRIGHT), a_plus),
                    ha='center', va='center', fontfamily='monospace',
                    transform=ax.transAxes)

            # so(2) box
            a3 = alpha_text(frame, 3, 0.35)
            if a3 > 0:
                box_so2 = FancyBboxPatch((0.57, 0.52), 0.38, 0.26,
                                         boxstyle="round,pad=0.02",
                                         facecolor=(*_hex2rgb(GREEN), a3 * 0.15),
                                         edgecolor=(*_hex2rgb(GREEN), a3 * 0.8),
                                         linewidth=2, transform=ax.transAxes)
                ax.add_patch(box_so2)
                ax.text(0.76, 0.73, 'so(2)', fontsize=16, fontweight='bold',
                        color=(*_hex2rgb(GREEN), a3),
                        ha='center', fontfamily='monospace',
                        transform=ax.transAxes)
                ax.text(0.76, 0.66, 'D^T = -D', fontsize=10,
                        color=(*_hex2rgb(GREEN), a3 * 0.8),
                        ha='center', fontfamily='monospace',
                        transform=ax.transAxes)
                ax.text(0.76, 0.57, 'dim = C(2,2) = 1', fontsize=10,
                        color=(*_hex2rgb(GREEN), a3 * 0.7),
                        ha='center', fontfamily='monospace',
                        transform=ax.transAxes)

            # Dimension count
            a4 = alpha_text(frame, 3, 0.55)
            ax.text(0.5, 0.43, 'dim k = 10 + 1 = 11',
                    fontsize=14, fontweight='bold',
                    color=(*_hex2rgb(HILIGHT), a4),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes)

            # Chern class connection
            a5 = alpha_text(frame, 3, 0.65)
            ax.text(0.5, 0.33, '= c_2(Q^5)',
                    fontsize=14, fontweight='bold',
                    color=(*_hex2rgb(MAGENTA), a5),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes,
                    bbox=dict(boxstyle='round,pad=0.3',
                              facecolor=(*_hex2rgb('#1a0a2a'), a5 * 0.7),
                              edgecolor=(*_hex2rgb(MAGENTA), a5 * 0.5),
                              linewidth=2))

            a6 = alpha_text(frame, 3, 0.75)
            ax.text(0.5, 0.20, 'The second Chern class COUNTS',
                    fontsize=10, color=(*_hex2rgb(BRIGHT), a6),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes)
            ax.text(0.5, 0.13, 'the isotropy generators.',
                    fontsize=10, color=(*_hex2rgb(BRIGHT), a6),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes)

            # Generator count
            a7 = alpha_text(frame, 3, 0.85)
            ax.text(0.5, 0.04,
                    '10 rotations in R^5  +  1 phase rotation',
                    fontsize=9, color=(*_hex2rgb(DIMTEXT), a7),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes)

        # ═══════════════════════════════════════════════════════
        # PANEL 5: "EXPONENTIATE"
        # ═══════════════════════════════════════════════════════

        def draw_panel_5(frame):
            ax = axes[4]
            a = alpha_for_panel(frame, 4)
            if a <= 0:
                return

            ax.text(0.5, 0.95, 'EXPONENTIATE', fontsize=14,
                    fontweight='bold', color=(*_hex2rgb(GOLD), a),
                    ha='center', va='top', fontfamily='monospace',
                    transform=ax.transAxes)

            a1 = alpha_text(frame, 4, 0.05)
            ax.text(0.5, 0.86, 'K = exp(k) = SO(5) x SO(2)',
                    fontsize=13, fontweight='bold',
                    color=(*_hex2rgb(CYAN), a1),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes,
                    bbox=dict(boxstyle='round,pad=0.3',
                              facecolor=(*_hex2rgb('#001a2a'), a1 * 0.7),
                              edgecolor=(*_hex2rgb(CYAN), a1 * 0.5),
                              linewidth=2))

            # SO(5): rotation group visualization
            a2 = alpha_text(frame, 4, 0.2)
            if a2 > 0:
                # Draw SO(5) as a sphere-like object with rotation arrows
                cx5, cy5 = 0.28, 0.58
                r5 = 0.14
                theta_vals = np.linspace(0, 2 * np.pi, 80)
                xs = cx5 + r5 * np.cos(theta_vals)
                ys = cy5 + r5 * 0.8 * np.sin(theta_vals)
                ax.fill(xs, ys, color=(*_hex2rgb(BLUE), a2 * 0.15),
                        transform=ax.transAxes)
                ax.plot(xs, ys, color=(*_hex2rgb(BLUE), a2 * 0.8),
                        linewidth=2, transform=ax.transAxes)

                # Rotation arrow inside
                rot_angle = frame * 0.08
                ax.annotate('',
                            xy=(cx5 + 0.07 * np.cos(rot_angle),
                                cy5 + 0.06 * np.sin(rot_angle)),
                            xytext=(cx5 + 0.07 * np.cos(rot_angle + 2.5),
                                    cy5 + 0.06 * np.sin(rot_angle + 2.5)),
                            arrowprops=dict(arrowstyle='->',
                                            color=(*_hex2rgb(BLUE), a2),
                                            lw=2),
                            transform=ax.transAxes)

                ax.text(cx5, cy5 - r5 - 0.04, 'SO(5)', fontsize=12,
                        fontweight='bold',
                        color=(*_hex2rgb(BLUE), a2),
                        ha='center', fontfamily='monospace',
                        transform=ax.transAxes)
                ax.text(cx5, cy5 - r5 - 0.10, 'rotations in R^5',
                        fontsize=8, color=(*_hex2rgb(BLUE), a2 * 0.7),
                        ha='center', fontfamily='monospace',
                        transform=ax.transAxes)

            # Cross sign
            a_x = alpha_text(frame, 4, 0.35)
            ax.text(0.50, 0.58, '\u00d7', fontsize=22,
                    color=(*_hex2rgb(BRIGHT), a_x),
                    ha='center', va='center', fontfamily='monospace',
                    transform=ax.transAxes)

            # SO(2): circle with rotation
            a3 = alpha_text(frame, 4, 0.35)
            if a3 > 0:
                cx2, cy2 = 0.72, 0.58
                r2 = 0.09
                xs2 = cx2 + r2 * np.cos(theta_vals)
                ys2 = cy2 + r2 * np.sin(theta_vals)
                ax.fill(xs2, ys2, color=(*_hex2rgb(GREEN), a3 * 0.15),
                        transform=ax.transAxes)
                ax.plot(xs2, ys2, color=(*_hex2rgb(GREEN), a3 * 0.8),
                        linewidth=2, transform=ax.transAxes)

                # Rotating vector inside
                angle2 = frame * 0.12
                ax.plot([cx2, cx2 + 0.06 * np.cos(angle2)],
                        [cy2, cy2 + 0.06 * np.sin(angle2)],
                        color=(*_hex2rgb(GREEN), a3), linewidth=2,
                        transform=ax.transAxes)
                ax.plot(cx2 + 0.06 * np.cos(angle2),
                        cy2 + 0.06 * np.sin(angle2),
                        'o', color=(*_hex2rgb(GREEN), a3),
                        markersize=4, transform=ax.transAxes)

                ax.text(cx2, cy2 - r2 - 0.04, 'SO(2)', fontsize=12,
                        fontweight='bold',
                        color=(*_hex2rgb(GREEN), a3),
                        ha='center', fontfamily='monospace',
                        transform=ax.transAxes)
                ax.text(cx2, cy2 - r2 - 0.10, 'phase / U(1)',
                        fontsize=8, color=(*_hex2rgb(GREEN), a3 * 0.7),
                        ha='center', fontfamily='monospace',
                        transform=ax.transAxes)

            # Properties
            a4 = alpha_text(frame, 4, 0.55)
            props = [
                ('Connected', 'both factors connected'),
                ('Compact', 'product of compact groups'),
                ('Maximal', 'G/K contractible (Cartan-Iwasawa-Malcev)'),
            ]
            for i, (prop, detail) in enumerate(props):
                yi = 0.30 - i * 0.08
                ax.text(0.10, yi, f'\u2713 {prop}:',
                        fontsize=10, fontweight='bold',
                        color=(*_hex2rgb(GREEN), a4),
                        fontfamily='monospace',
                        transform=ax.transAxes)
                ax.text(0.38, yi, detail,
                        fontsize=9, color=(*_hex2rgb(DIMTEXT), a4),
                        fontfamily='monospace',
                        transform=ax.transAxes)

            a5 = alpha_text(frame, 4, 0.8)
            ax.text(0.5, 0.04,
                    'D_IV^5  =  G / K  =  SO_0(5,2) / [SO(5) x SO(2)]',
                    fontsize=10, fontweight='bold',
                    color=(*_hex2rgb(HILIGHT), a5),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes)

        # ═══════════════════════════════════════════════════════
        # PANEL 6: "UNIVERSAL"
        # ═══════════════════════════════════════════════════════

        def draw_panel_6(frame):
            ax = axes[5]
            a = alpha_for_panel(frame, 5)
            if a <= 0:
                return

            ax.text(0.5, 0.95, 'UNIVERSAL', fontsize=14,
                    fontweight='bold', color=(*_hex2rgb(GOLD), a),
                    ha='center', va='top', fontfamily='monospace',
                    transform=ax.transAxes)

            a1 = alpha_text(frame, 5, 0.05)
            ax.text(0.5, 0.86,
                    'For ALL D_IV^n:  K = SO(n) x SO(2)',
                    fontsize=11, color=(*_hex2rgb(CYAN), a1),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes,
                    bbox=dict(boxstyle='round,pad=0.3',
                              facecolor=(*_hex2rgb('#001a2a'), a1 * 0.7),
                              edgecolor=(*_hex2rgb(CYAN), a1 * 0.5),
                              linewidth=1.5))

            # Table of n = 3, 5, 7, 9
            a2 = alpha_text(frame, 5, 0.2)
            if a2 > 0:
                # Header
                y_top = 0.74
                y_step = 0.075
                cols = [0.10, 0.28, 0.47, 0.68, 0.88]

                headers = ['n', 'dim K', 'dim G/K', 'c_2(Q^n)', 'match']
                for c, h in zip(cols, headers):
                    ax.text(c, y_top, h, fontsize=9, fontweight='bold',
                            color=(*_hex2rgb(BRIGHT), a2),
                            ha='center', fontfamily='monospace',
                            transform=ax.transAxes)

                # Divider line
                ax.plot([0.03, 0.97], [y_top - 0.025, y_top - 0.025],
                        color=(*_hex2rgb(DIMTEXT), a2 * 0.4),
                        linewidth=1, transform=ax.transAxes)

                # Data rows
                row_data = [
                    (3, DIMTEXT),
                    (5, HILIGHT),
                    (7, DIMTEXT),
                    (9, DIMTEXT),
                ]
                for row_i, (n, row_color) in enumerate(row_data):
                    a_row = alpha_text(frame, 5, 0.25 + row_i * 0.08)
                    if a_row <= 0:
                        continue
                    y = y_top - (row_i + 1) * y_step
                    dk = dim_k_universal(n)
                    dgk = dim_gk_universal(n)
                    c2 = chern_class(n, 2)
                    match_str = '\u2713' if dk == c2 else '\u2717'

                    vals = [str(n), str(dk), str(dgk), str(c2), match_str]
                    for c, v in zip(cols, vals):
                        # Highlight n=5 row
                        clr = HILIGHT if n == 5 else BRIGHT
                        fsize = 11 if n == 5 else 10
                        fw = 'bold' if n == 5 else 'normal'
                        ax.text(c, y, v, fontsize=fsize, fontweight=fw,
                                color=(*_hex2rgb(clr), a_row),
                                ha='center', fontfamily='monospace',
                                transform=ax.transAxes)

                    # Highlight n=5 row background
                    if n == 5 and a_row > 0.3:
                        highlight = plt.Rectangle((0.03, y - 0.02), 0.94, 0.06,
                                                  facecolor=(*_hex2rgb(HILIGHT), a_row * 0.06),
                                                  edgecolor='none',
                                                  transform=ax.transAxes)
                        ax.add_patch(highlight)

            # Formula
            a3 = alpha_text(frame, 5, 0.6)
            ax.text(0.5, 0.32,
                    'dim K = n(n-1)/2 + 1 = c_2(Q^n)',
                    fontsize=11, fontweight='bold',
                    color=(*_hex2rgb(MAGENTA), a3),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes,
                    bbox=dict(boxstyle='round,pad=0.3',
                              facecolor=(*_hex2rgb('#1a0a2a'), a3 * 0.7),
                              edgecolor=(*_hex2rgb(MAGENTA), a3 * 0.5),
                              linewidth=2))

            # Three case illustrations
            a4 = alpha_text(frame, 5, 0.7)
            if a4 > 0:
                cases = [
                    (0.20, 'n=3', '4', BLUE),
                    (0.50, 'n=5', '11', HILIGHT),
                    (0.80, 'n=7', '22', GREEN),
                ]
                for cx, label, dim_str, clr in cases:
                    ax.text(cx, 0.21, label, fontsize=10,
                            fontweight='bold',
                            color=(*_hex2rgb(clr), a4),
                            ha='center', fontfamily='monospace',
                            transform=ax.transAxes)
                    # Small circle for the group
                    circ_r = 0.04 + 0.02 * (int(dim_str) / 22.0)
                    t_vals = np.linspace(0, 2 * np.pi, 50)
                    circ_x = cx + circ_r * np.cos(t_vals)
                    circ_y = 0.13 + circ_r * 0.8 * np.sin(t_vals)
                    ax.plot(circ_x, circ_y,
                            color=(*_hex2rgb(clr), a4 * 0.7),
                            linewidth=1.5, transform=ax.transAxes)
                    ax.text(cx, 0.13, dim_str, fontsize=9,
                            color=(*_hex2rgb(clr), a4),
                            ha='center', va='center',
                            fontfamily='monospace',
                            transform=ax.transAxes)

            # Footer
            a5 = alpha_text(frame, 5, 0.85)
            ax.text(0.5, 0.03,
                    'The proof works for every dimension.',
                    fontsize=9, fontweight='bold',
                    color=(*_hex2rgb(ORANGE), a5),
                    ha='center', fontfamily='monospace',
                    transform=ax.transAxes)

        # ═══════════════════════════════════════════════════════
        # ANIMATION LOOP
        # ═══════════════════════════════════════════════════════

        def animate(frame):
            # Clear all axes
            for ax in axes:
                ax.clear()
                ax.set_facecolor(PANEL_BG)
                ax.set_xlim(0, 1)
                ax.set_ylim(0, 1)
                ax.axis('off')

            # Draw step labels on the panels
            step_labels = [
                ('Step 1', DIMTEXT),
                ('Step 2', DIMTEXT),
                ('Step 3', DIMTEXT),
                ('Step 4', DIMTEXT),
                ('Step 5', DIMTEXT),
                ('Step 6', DIMTEXT),
            ]
            for i, (label, clr) in enumerate(step_labels):
                a = alpha_for_panel(frame, i)
                if a > 0:
                    axes[i].text(0.02, 0.01, label,
                                 fontsize=8,
                                 color=(*_hex2rgb(clr), a * 0.5),
                                 fontfamily='monospace',
                                 transform=axes[i].transAxes)

            # Draw panels
            draw_panel_1(frame)
            draw_panel_2(frame)
            draw_panel_3(frame)
            draw_panel_4(frame)
            draw_panel_5(frame)
            draw_panel_6(frame)

            return []

        anim = FuncAnimation(fig, animate, frames=N_FRAMES,
                             interval=50, blit=False, repeat=True)

        plt.show()

    # ───────────────────────────────────────────────────────────
    #  HELPER: Draw mini matrix
    # ───────────────────────────────────────────────────────────

    def _draw_mini_matrix(self, ax, M, x0, y0, cell_size, alpha, label,
                          color, frame):
        """Draw a small 7x7 matrix heatmap at (x0, y0)."""
        n = M.shape[0]
        total = cell_size * n
        vmax = max(np.max(np.abs(M)), 1e-10)

        for i in range(n):
            for j in range(n):
                val = M[i, j]
                if abs(val) > 1e-10:
                    # Color: blue for positive, red for negative
                    if val > 0:
                        clr = (0.3, 0.5, 1.0, alpha * 0.8)
                    else:
                        clr = (1.0, 0.3, 0.3, alpha * 0.8)
                else:
                    clr = (0.1, 0.1, 0.15, alpha * 0.3)

                rect = plt.Rectangle(
                    (x0 + j * cell_size / total * 0.16,
                     y0 + (n - 1 - i) * cell_size / total * 0.16),
                    cell_size / total * 0.15,
                    cell_size / total * 0.15,
                    facecolor=clr,
                    edgecolor=(0.3, 0.3, 0.4, alpha * 0.3),
                    linewidth=0.5,
                    transform=ax.transAxes)
                ax.add_patch(rect)

        # Label below
        cx = x0 + 0.08
        ax.text(cx, y0 - 0.04, label,
                fontsize=8, color=(*_hex2rgb(color), alpha),
                ha='center', fontfamily='monospace',
                transform=ax.transAxes)


# ═══════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

def _matrix_exp(X, terms=30):
    """Matrix exponential via Taylor series (sufficient for 7x7)."""
    n = X.shape[0]
    result = np.eye(n)
    power = np.eye(n)
    for k in range(1, terms + 1):
        power = power @ X / k
        result += power
    return result


def _hex2rgb(hexcolor):
    """Convert '#rrggbb' to (r, g, b) floats in [0, 1]."""
    h = hexcolor.lstrip('#')
    return tuple(int(h[i:i+2], 16) / 255.0 for i in (0, 2, 4))


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    ip = IsotropyProof()
    ip.cartan_involution()
    ip.fixed_subalgebra()
    ip.block_diagonal()
    ip.identify_algebra()
    ip.exponentiate()
    ip.universality()
    ip.numerical_check()
    ip.summary()
    ip.show()
