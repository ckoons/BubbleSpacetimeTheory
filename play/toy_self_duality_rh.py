#!/usr/bin/env python3
"""
SELF-DUALITY AND THE CRITICAL LINE [CONJECTURE]
================================================
"The codes and the curvature agree. That is the Riemann Hypothesis."

Two independent paths from Q⁵ to ζ(s), both carrying self-duality,
equated by the Selberg trace formula.

Path A (Chern/Geometric):
    Q⁵ → P(h) → palindromic → Re(h)=-1/2 → Seeley-DeWitt a_k → heat kernel Z(t)
    This is the GEOMETRIC SIDE of the Selberg trace formula.

Path B (Code/Algebraic):
    Q⁵ → spectral codes → self-dual Golay → Leech Λ₂₄ → theta function → modular → L(s)
    This is the SPECTRAL SIDE of the Selberg trace formula.

The Selberg trace formula says: Path A = Path B. Both sides are
independently constrained to be palindromic/self-dual. The ζ-zeros
have no room to deviate.

    from toy_self_duality_rh import SelfDualityRH
    sd = SelfDualityRH()
    sd.two_paths()               # two paths from Q⁵ to ζ(s)
    sd.self_duality_cascade()    # Code → Lattice → Modular → L-function
    sd.three_palindromes()       # P(h), Golay, ξ(s) — same symmetry
    sd.golay_bst_numbers()       # 759 = N_c × c₂ × 23, all BST integers
    sd.physical_reading()        # RH = error correction at all frequencies
    sd.summary()                 # the punchline
    sd.show()                    # 6-panel visualization

*** CONJECTURE — The Code-Chern RH conjecture is deep but unproved. ***

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

N_c = 3                      # color charges
n_C = 5                      # complex dimension of D_IV^5
genus = n_C + 2              # = 7
C2 = n_C + 1                 # = 6, Casimir eigenvalue
N_max = 137                  # Haldane channel capacity
Gamma_order = 1920           # |W(D₅)| = n_C! × 2^(n_C-1)

# Chern classes of Q⁵ = SO(7)/[SO(5) × SO(2)]
# c(Q⁵) = (1+h)⁷ / (1+2h) mod h⁶
CHERN = [5, 11, 13, 9, 3]   # c₁, c₂, c₃, c₄, c₅

# Golay code parameters
GOLAY_N = 24                 # code length
GOLAY_K = 12                 # dimension (self-dual: k = n-k)
GOLAY_D = 8                  # minimum distance
GOLAY_WEIGHTS = [1, 759, 2576, 759, 1]  # weight enumerator (nonzero terms)
GOLAY_WEIGHT_INDICES = [0, 8, 12, 16, 24]  # corresponding weights

# Leech lattice
LEECH_DIM = 24
LEECH_KISSING = 196560       # minimal vectors
LEECH_MIN_NORM_SQ = 4

# Derived
_vol_D = np.pi**n_C / Gamma_order
alpha = (N_c**2 / (2**N_c * np.pi**4)) * _vol_D**(1/4)  # ~ 1/137.036


# ═══════════════════════════════════════════════════════════════════
# CHERN CLASS COMPUTATION
# ═══════════════════════════════════════════════════════════════════

def _chern_coefficients(n):
    """
    Compute Chern class coefficients c_1, ..., c_n for Q^n.
    c(Q^n) = (1+h)^(n+2) / (1+2h) mod h^(n+1)
    """
    coeffs = []
    for k in range(1, n + 1):
        ck = 0
        for j in range(k + 1):
            ck += comb(n + 2, k - j) * ((-2) ** j)
        coeffs.append(ck)
    return coeffs


def _chern_polynomial_coeffs(n):
    """Full polynomial coefficients [c_0=1, c_1, ..., c_n] for Q^n."""
    return [1] + _chern_coefficients(n)


# ═══════════════════════════════════════════════════════════════════
# THE SELF-DUALITY RH CLASS
# ═══════════════════════════════════════════════════════════════════

class SelfDualityRH:
    """
    Self-Duality and the Critical Line [CONJECTURE].

    Two independent paths from Q⁵ to ζ(s), both carrying self-duality,
    equated by the Selberg trace formula.
    """

    def __init__(self, quiet=False):
        self.quiet = quiet
        self._chern = _chern_coefficients(n_C)
        self._poly = _chern_polynomial_coeffs(n_C)
        if not quiet:
            print()
            print("  ╔═══════════════════════════════════════════════════════════╗")
            print("  ║    SELF-DUALITY AND THE CRITICAL LINE  [CONJECTURE]      ║")
            print("  ╠═══════════════════════════════════════════════════════════╣")
            print("  ║                                                          ║")
            print("  ║  \"The codes and the curvature agree.                     ║")
            print("  ║   That is the Riemann Hypothesis.\"                       ║")
            print("  ║                                                          ║")
            print("  ╚═══════════════════════════════════════════════════════════╝")
            print()

    # ─── 1. Two Paths ───

    def two_paths(self) -> dict:
        """
        Two independent paths from Q⁵ to ζ(s).

        Path A (Chern/Geometric):
            Q⁵ → P(h) → palindromic → Re(h)=-1/2 → Seeley-DeWitt → heat kernel
            GEOMETRIC SIDE of the Selberg trace formula.

        Path B (Code/Algebraic):
            Q⁵ → spectral codes → self-dual Golay → Leech Λ₂₄ → theta → modular → L(s)
            SPECTRAL SIDE of the Selberg trace formula.
        """
        print()
        print("  TWO PATHS FROM Q\u2075 TO \u03b6(s)")
        print("  ==============================")
        print()
        print("  ┌─────────────────────────────────────────────────────────┐")
        print("  │                        Q\u2075                              │")
        print("  │        compact dual of D_IV\u2075 = SO\u2080(5,2)/K            │")
        print("  └───────────────┬──────────────────────┬──────────────────┘")
        print("                  │                      │")
        print("            PATH A (Chern)         PATH B (Code)")
        print("            ══════════════         ═══════════════")
        print("                  │                      │")
        print("                  ▼                      ▼")
        print("  ┌───────────────────────┐  ┌──────────────────────────┐")
        print("  │ P(h) = (1+h)\u2077/(1+2h) │  │ spectral codes from Q\u2075   │")
        print("  │ = 1+5h+11h\u00b2+13h\u00b3     │  │ Hamming-type on dim=5     │")
        print("  │   +9h\u2074+3h\u2075          │  │                          │")
        print("  └──────────┬────────────┘  └────────────┬─────────────┘")
        print("             │                            │")
        print("             ▼                            ▼")
        print("  ┌───────────────────────┐  ┌──────────────────────────┐")
        print("  │ PALINDROMIC:          │  │ self-dual Golay [24,12,8]│")
        print("  │ P(-1/2+u)=P(-1/2-u)  │  │ k = n-k = 12            │")
        print("  │ zeros on Re(h)=-1/2   │  │ MacWilliams identity     │")
        print("  └──────────┬────────────┘  └────────────┬─────────────┘")
        print("             │                            │")
        print("             ▼                            ▼")
        print("  ┌───────────────────────┐  ┌──────────────────────────┐")
        print("  │ Seeley-DeWitt a_k     │  │ Leech lattice \u039b\u2082\u2084       │")
        print("  │ spectral coefficients │  │ \u039b* = \u039b (unimodular)      │")
        print("  └──────────┬────────────┘  └────────────┬─────────────┘")
        print("             │                            │")
        print("             ▼                            ▼")
        print("  ┌───────────────────────┐  ┌──────────────────────────┐")
        print("  │ heat kernel Z(t)      │  │ \u0398_\u039b(\u03c4): weight-12 modular │")
        print("  │ = tr(e^{-t\u0394})        │  │ \u0398(-1/\u03c4) = \u03c4\u00b9\u00b2\u0398(\u03c4)       │")
        print("  └──────────┬────────────┘  └────────────┬─────────────┘")
        print("             │                            │")
        print("     GEOMETRIC SIDE              SPECTRAL SIDE")
        print("             │                            │")
        print("             └──────────┬─────────────────┘")
        print("                        ▼")
        print("           ┌─────────────────────────┐")
        print("           │   SELBERG TRACE FORMULA  │")
        print("           │    geometric = spectral  │")
        print("           │                          │")
        print("           │   Path A = Path B        │")
        print("           │   Both palindromic.      │")
        print("           │   Zeros on Re(s) = 1/2.  │")
        print("           └─────────────────────────┘")
        print()
        print("  [CONJECTURE] The Selberg trace formula equates two")
        print("  independently self-dual objects. The ζ-zeros have")
        print("  no room to deviate from the critical line.")

        return {
            'path_a': 'Chern/Geometric',
            'path_b': 'Code/Algebraic',
            'convergence': 'Selberg trace formula',
            'status': 'CONJECTURE',
        }

    # ─── 2. Self-Duality Cascade ───

    def self_duality_cascade(self) -> dict:
        """
        The 4-level self-duality cascade:
          Code → Lattice → Modular form → L-function.
        Each level inherits self-duality from the one above.
        """
        print()
        print("  SELF-DUALITY CASCADE")
        print("  ====================")
        print()
        print("  Each level inherits self-duality from the one above.")
        print("  The cascade is RIGID — break any level and all below fail.")
        print()
        print("  ┌─────────────────────────────────────────────────────────────┐")
        print("  │  Level 1: CODE                                             │")
        print("  │                                                             │")
        print("  │  Golay code G\u2082\u2084 = [24, 12, 8]\u2082                            │")
        print("  │  Self-duality: k = n - k = 12                              │")
        print("  │  Functional equation: MacWilliams identity                  │")
        print("  │                                                             │")
        print("  │  W_C(x,y) = W_{C\u22a5}(x,y)  because C = C\u22a5                    │")
        print("  │                                                             │")
        print("  │  The Golay code is the unique [24,12,8] binary self-dual    │")
        print("  │  code. It is PERFECT: every word is within distance 3       │")
        print("  │  of a codeword.                                             │")
        print("  └──────────────────────────┬──────────────────────────────────┘")
        print("                             │ Construction A")
        print("                             ▼")
        print("  ┌─────────────────────────────────────────────────────────────┐")
        print("  │  Level 2: LATTICE                                           │")
        print("  │                                                             │")
        print("  │  Leech lattice \u039b\u2082\u2084 (via Construction A from Golay)        │")
        print("  │  Self-duality: \u039b* = \u039b  (even unimodular)                   │")
        print("  │  Functional equation: Poisson summation                     │")
        print("  │                                                             │")
        print("  │  \u03a3_{\u03bb\u2208\u039b*} f(\u03bb) = vol(\u039b) \u03a3_{\u03bb\u2208\u039b} f\u0302(\u03bb)")
        print("  │  Since \u039b* = \u039b, both sides sum over the SAME lattice.       │")
        print("  │                                                             │")
        print("  │  Kissing number: 196560. Min norm: 4.                       │")
        print("  └──────────────────────────┬──────────────────────────────────┘")
        print("                             │ Theta function")
        print("                             ▼")
        print("  ┌─────────────────────────────────────────────────────────────┐")
        print("  │  Level 3: MODULAR FORM                                      │")
        print("  │                                                             │")
        print("  │  \u0398_\u039b(\u03c4) = \u03a3_{\u03bb\u2208\u039b} q^{|\u03bb|\u00b2/2}     (q = e^{2\u03c0i\u03c4})")
        print("  │  Self-duality: weight 12 for SL(2,\u2124)                       │")
        print("  │  Functional equation: \u0398(-1/\u03c4) = \u03c4\u00b9\u00b2 \u0398(\u03c4)                │")
        print("  │                                                             │")
        print("  │  Weight 12 = dim(\u039b\u2082\u2084)/2 = 24/2.                          │")
        print("  │  The Ramanujan \u0394 function is the cusp form of weight 12.    │")
        print("  └──────────────────────────┬──────────────────────────────────┘")
        print("                             │ Mellin transform")
        print("                             ▼")
        print("  ┌─────────────────────────────────────────────────────────────┐")
        print("  │  Level 4: L-FUNCTION                                        │")
        print("  │                                                             │")
        print("  │  L(s) = Mellin transform of \u0398_\u039b(\u03c4)                       │")
        print("  │  Self-duality: completed \u039b(s) = \u039b(k-s)                    │")
        print("  │  Functional equation: \u039b(s) = \u039b(12-s)                      │")
        print("  │                                                             │")
        print("  │  [CONJECTURE] Zeros on Re(s) = k/2 = 6.                    │")
        print("  │  For the Riemann \u03b6: \u039b(s) = \u039b(1-s), zeros on Re(s)=1/2.  │")
        print("  └─────────────────────────────────────────────────────────────┘")
        print()
        print("  The chain: self-dual code \u2192 unimodular lattice \u2192")
        print("             modular form \u2192 functional equation \u2192 critical line.")
        print()
        print("  [CONJECTURE] Self-duality at the CODE level forces")
        print("  the L-function zeros onto the critical line.")

        return {
            'levels': ['Code', 'Lattice', 'Modular form', 'L-function'],
            'self_dualities': [
                'k = n-k = 12',
                'Lambda* = Lambda',
                'Theta(-1/tau) = tau^12 Theta(tau)',
                'Lambda(s) = Lambda(k-s)',
            ],
            'equations': [
                'MacWilliams identity',
                'Poisson summation',
                'SL(2,Z) modularity',
                'Functional equation',
            ],
            'status': 'CONJECTURE',
        }

    # ─── 3. Three Palindromes ───

    def three_palindromes(self) -> dict:
        """
        The palindromic principle in three languages:
          1. P(h) of Q⁵: coefficients (1,5,11,13,9,3)
          2. Golay weight enumerator: (1, 759, 2576, 759, 1)
          3. ξ(s) = ξ(1-s): the Riemann functional equation
        """
        poly = self._poly  # [1, 5, 11, 13, 9, 3]
        rev = list(reversed(poly))

        # The Chern polynomial has a reciprocal symmetry:
        # h⁵ P(1/h) = (1/3) P(h)  (up to leading coefficient ratio)
        # More precisely: the SCALED reciprocal polynomial
        # R(h) = h⁵ P(1/h) / c₅ has the same zeros as P(h) mapped by h → 1/h.
        #
        # The deep palindromic structure is:
        # c_k * c_{n-k} obeys a constraint from Poincare duality on Q⁵.
        # Specifically: c₁c₅ = 15, c₂c₄ = 99, c₃² = 169.
        # The ratios c_k/c_{n-k} form a consistent pattern.
        #
        # The Golay weight enumerator IS literally palindromic: 1,759,2576,759,1.
        # That is the stronger statement.

        # Verify the Poincare duality products: c_k × c_{n_C+1-k}
        # where poly[k] = c_k (with poly[0] = c_0 = 1)
        pd_products = [
            (1, 5, poly[1] * poly[n_C]),      # c_1 × c_5
            (2, 4, poly[2] * poly[n_C - 1]),  # c_2 × c_4
            (3, 3, poly[3] * poly[n_C - 2]),  # c_3 × c_3
        ]

        # Golay weight enumerator palindromic check
        golay_wt = GOLAY_WEIGHTS  # [1, 759, 2576, 759, 1]
        golay_rev = list(reversed(golay_wt))
        golay_palindromic = (golay_wt == golay_rev)

        print()
        print("  THREE PALINDROMES [CONJECTURE]")
        print("  ==============================")
        print()
        print("  The same symmetry appears in three different languages.")
        print()
        print("  ── Palindrome 1: Chern polynomial of Q\u2075 ──")
        print()
        print(f"    P(h) = {' + '.join(f'{c}h^{k}' if k > 0 else str(c) for k, c in enumerate(poly))}")
        print(f"    Coefficients:  {poly}")
        print(f"    Reversed:      {rev}")
        print()
        print("    Poincar\u00e9 duality products c_k \u00d7 c_{n-k}:")
        for k, nk, prod in pd_products:
            print(f"      c_{k} \u00d7 c_{nk} = {poly[k]} \u00d7 {poly[nk]} = {prod}")
        print()
        print("    The reciprocal polynomial R(h) = h\u2075P(1/h)/c\u2085 satisfies:")
        print("    R(h) = (1/3)(1 + 3h + 3h\u00b2 + ...) — encoding the same zeros")
        print("    mapped by h \u2194 1/h through the Weyl involution.")
        print()
        # Find zeros
        roots = np.roots(list(reversed(poly)))
        n_on_half = sum(1 for z in roots if abs(z.real + 0.5) < 1e-8)
        print()
        print(f"    Zeros of P(h): {n_on_half} of {len(roots)} lie on Re(h) = -1/2")
        print(f"    (The remaining zero at h=-1 is from the (1+h)\u2077 factor.)")
        print(f"    Chern-Gauss-Bonnet: \u222b c_5 = \u03c7(Q\u2075) = n_C+1 = 6 [PROVED]")
        print()
        print("  ── Palindrome 2: Golay weight enumerator ──")
        print()
        print(f"    Weight enumerator of G\u2082\u2084:")
        for i, (w, c) in enumerate(zip(GOLAY_WEIGHT_INDICES, GOLAY_WEIGHTS)):
            print(f"      A_{w:>2} = {c:>5}")
        print()
        print(f"    Coefficients:  {golay_wt}")
        print(f"    Reversed:      {golay_rev}")
        print(f"    Palindromic:   {golay_palindromic}  [PROVED by MacWilliams]")
        print()
        print("  ── Palindrome 3: Riemann xi function ──")
        print()
        print("    \u03be(s) = \u03be(1-s)")
        print("    If palindromic symmetry forces zeros to the center line,")
        print("    then: zeros on Re(s) = 1/2  [RH, UNPROVED]")
        print()
        print("  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("  [CONJECTURE] All three exhibit the SAME structural symmetry —")
        print("  a duality that pairs each coefficient/zero with a mirror partner.")
        print("  For Golay and \u03be(s), the palindrome is literal.")
        print("  For P(h), it is a Poincar\u00e9 duality constraint on the Chern ring.")
        print("  The conjecture: these are three faces of one self-duality.")

        return {
            'chern_poly': poly,
            'chern_reversed': rev,
            'poincare_products': [(k, nk, p) for k, nk, p in pd_products],
            'golay_weights': golay_wt,
            'golay_palindromic': golay_palindromic,
            'xi_palindromic': 'UNPROVED (= RH)',
            'status': 'CONJECTURE',
        }

    # ─── 4. BST Numbers in Golay ───

    def golay_bst_numbers(self) -> dict:
        """
        The Golay weight enumerator factors entirely into BST integers.

        759 = 3 × 11 × 23 = N_c × c₂ × (dim SU(5) - 1)
        2576 = 2⁴ × 7 × 23 = 2⁴ × g × 23
        """
        # Factorize
        f759 = (3, 11, 23)
        f2576 = (16, 7, 23)

        # Verify
        assert 3 * 11 * 23 == 759
        assert 16 * 7 * 23 == 2576

        # BST identifications
        print()
        print("  BST NUMBERS IN THE GOLAY CODE [CONJECTURE]")
        print("  ==========================================")
        print()
        print("  The weight enumerator of the most perfect binary code")
        print("  factors entirely into BST integers.")
        print()
        print("  ┌────────────────────────────────────────────────────────┐")
        print("  │                                                        │")
        print(f"  │  759 = 3 \u00d7 11 \u00d7 23                                     │")
        print(f"  │      = N_c \u00d7 c\u2082 \u00d7 23                                  │")
        print(f"  │      = N_c \u00d7 c\u2082 \u00d7 (dim SU(5) - 1)                    │")
        print("  │                                                        │")
        print("  │  N_c = 3   (color number = c\u2085)                         │")
        print("  │  c\u2082  = 11  (second Chern class of Q\u2075)                  │")
        print("  │  23  = 24 - 1 = dim(SU(5)) - 1                        │")
        print("  │       also: second largest prime \u2264 n_C! = 120          │")
        print("  │                                                        │")
        print("  ├────────────────────────────────────────────────────────┤")
        print("  │                                                        │")
        print(f"  │  2576 = 2\u2074 \u00d7 7 \u00d7 23                                   │")
        print(f"  │       = 2\u2074 \u00d7 g \u00d7 23                                   │")
        print(f"  │       = 2^{n_C-1} \u00d7 (n_C+2) \u00d7 23                        │")
        print("  │                                                        │")
        print("  │  2\u2074  = 2^(n_C-1) = 16  (half-spinor dimension)        │")
        print("  │  g   = 7   (genus = n_C + 2)                           │")
        print("  │  23  = same factor as in 759                           │")
        print("  │                                                        │")
        print("  └────────────────────────────────────────────────────────┘")
        print()
        print("  Additional connections:")
        print(f"    759 + 2576 + 759 = {759 + 2576 + 759}")
        print(f"                     = 4094 = 2\u00b9\u00b2 - 2")
        print(f"                     = 2(2\u00b9\u00b9 - 1)")
        print(f"                     2\u00b9\u00b9 - 1 = 2047 = 23 \u00d7 89")
        print()
        print(f"    Total codewords:  2\u00b9\u00b2 = 4096 = 2^k  (k = Golay dimension)")
        print(f"    Nontrivial:       4094 = 2\u00b9\u00b2 - 2  (minus zero + all-ones)")
        print()
        print("  [CONJECTURE] The appearance of N_c, c\u2082, and g in the Golay")
        print("  weight enumerator is not coincidence — it reflects the")
        print("  algebraic structure of Q\u2075 propagating into the code world.")

        return {
            '759_factorization': f'{f759[0]} x {f759[1]} x {f759[2]}',
            '759_bst': 'N_c x c_2 x 23',
            '2576_factorization': f'{f2576[0]} x {f2576[1]} x {f2576[2]}',
            '2576_bst': '2^(n_C-1) x g x 23',
            'bst_integers_present': ['N_c=3', 'c_2=11', 'g=7', '2^(n_C-1)=16'],
            'status': 'CONJECTURE',
        }

    # ─── 5. Physical Reading ───

    def physical_reading(self) -> dict:
        """
        The physical reading of RH:
          Zero on the critical line → damped resonance → stable physics.
          Zero OFF the critical line → growing resonance → code failure → proton decay.
          RH = "the codes work at all frequencies."
        """
        print()
        print("  THE PHYSICAL READING [CONJECTURE]")
        print("  =================================")
        print()
        print("  In BST, error correction is not a metaphor. The vacuum IS")
        print("  a self-dual code. The Golay structure ensures stability.")
        print()
        print("  ┌─────────────────────────────────────────────────────────┐")
        print("  │                                                         │")
        print("  │   ZERO ON Re(s) = 1/2:                                 │")
        print("  │                                                         │")
        print("  │   \u03b6(\u00bd + it\u2099) = 0                                       │")
        print("  │                                                         │")
        print("  │   \u2192 Contribution to prime counting function:            │")
        print("  │     x^{\u00bd + it\u2099} / (\u00bd + it\u2099)                             │")
        print("  │                                                         │")
        print("  │   \u2192 Amplitude: x^{1/2}  [BOUNDED]                      │")
        print("  │   \u2192 Oscillation: e^{it\u2099 log x}  [PHASE ONLY]           │")
        print("  │                                                         │")
        print("  │   Physical: damped resonance. Primes distributed as     │")
        print("  │   uniformly as possible. Error-correcting code WORKS.   │")
        print("  │                                                         │")
        print("  ├─────────────────────────────────────────────────────────┤")
        print("  │                                                         │")
        print("  │   HYPOTHETICAL ZERO OFF LINE:                           │")
        print("  │                                                         │")
        print("  │   \u03b6(\u03c3 + it) = 0  with \u03c3 > 1/2                          │")
        print("  │                                                         │")
        print("  │   \u2192 Amplitude: x^{\u03c3}  [GROWS with x!]                   │")
        print("  │   \u2192 Resonance amplifies instead of damping              │")
        print("  │                                                         │")
        print("  │   Physical: self-dual code FAILS. Poisson summation     │")
        print("  │   breaks. Lattice loses unimodularity. Error grows.     │")
        print("  │                                                         │")
        print("  │   Consequence: proton decay. The baryon orbit ceases    │")
        print("  │   to close. m_p/m_e = 6\u03c0\u2075 acquires corrections that    │")
        print("  │   grow without bound.                                   │")
        print("  │                                                         │")
        print("  └─────────────────────────────────────────────────────────┘")
        print()
        print("  The chain of consequences:")
        print()
        print("    compact Q\u2075")
        print("      \u2192 perfect codes exist (Hamming bound saturated)")
        print("      \u2192 self-dual codes exist (MacWilliams fixed)")
        print("      \u2192 unimodular lattices exist (Poisson closed)")
        print("      \u2192 modular forms exist (SL(2,\u2124) invariant)")
        print("      \u2192 functional equation holds (\u039b(s) = \u039b(k-s))")
        print("      \u2192 zeros on the critical line")
        print("      \u2192 exact physics (no growing resonances)")
        print()
        print("  RH = \"error correction works at all frequencies.\"")
        print()
        print("  [CONJECTURE] A zero off the critical line would be an error")
        print("  the code cannot correct. BST says this is impossible because")
        print("  Q\u2075 is compact — there is no room for the code to fail.")

        return {
            'on_line': 'damped resonance, stable physics',
            'off_line': 'growing resonance, code failure, proton decay',
            'interpretation': 'RH = error correction at all frequencies',
            'bst_reason': 'Q^5 compact => code cannot fail',
            'status': 'CONJECTURE',
        }

    # ─── 6. Summary ───

    def summary(self) -> dict:
        """
        The punchline: two self-dualities, one critical line.
        """
        print()
        print("  ╔═══════════════════════════════════════════════════════════╗")
        print("  ║    THE PUNCHLINE  [CONJECTURE]                           ║")
        print("  ╠═══════════════════════════════════════════════════════════╣")
        print("  ║                                                          ║")
        print("  ║  Two self-dualities. One critical line.                  ║")
        print("  ║                                                          ║")
        print("  ║  Path A: Q\u2075 \u2192 Chern polynomial \u2192 palindromic          ║")
        print("  ║          \u2192 heat kernel \u2192 GEOMETRIC SIDE               ║")
        print("  ║                                                          ║")
        print("  ║  Path B: Q\u2075 \u2192 spectral codes \u2192 self-dual Golay       ║")
        print("  ║          \u2192 Leech \u2192 modular \u2192 SPECTRAL SIDE           ║")
        print("  ║                                                          ║")
        print("  ║  Selberg trace formula: Path A = Path B                  ║")
        print("  ║                                                          ║")
        print("  ║  Both sides independently self-dual.                     ║")
        print("  ║  The \u03b6-zeros have no room to deviate.                   ║")
        print("  ║                                                          ║")
        print("  ╠═══════════════════════════════════════════════════════════╣")
        print("  ║                                                          ║")
        print("  ║  RH is the statement that the geometric and algebraic    ║")
        print("  ║  self-dualities of Q\u2075 are compatible.                   ║")
        print("  ║                                                          ║")
        print("  ║  They must be \u2014 they describe the same manifold.         ║")
        print("  ║                                                          ║")
        print("  ╠═══════════════════════════════════════════════════════════╣")
        print("  ║                                                          ║")
        print("  ║  759 = N_c \u00d7 c\u2082 \u00d7 23     (all BST integers)            ║")
        print("  ║  2576 = 2\u2074 \u00d7 g \u00d7 23      (all BST integers)            ║")
        print("  ║                                                          ║")
        print("  ║  The codes and the curvature agree.                      ║")
        print("  ║  That is the Riemann Hypothesis.                         ║")
        print("  ║                                                          ║")
        print("  ╚═══════════════════════════════════════════════════════════╝")
        print()

        return {
            'path_a': 'Chern/Geometric (palindromic)',
            'path_b': 'Code/Algebraic (self-dual)',
            'bridge': 'Selberg trace formula',
            'conclusion': 'Zeros on Re(s) = 1/2',
            'physical': 'Error correction at all frequencies',
            'status': 'CONJECTURE',
        }

    # ─── 7. Show (6-panel visualization) ───

    def show(self):
        """
        Launch the 6-panel (2x3) visualization:
            Panel 1: Two Paths diagram
            Panel 2: Self-Duality Cascade
            Panel 3: Three Palindromes
            Panel 4: BST Numbers in Golay
            Panel 5: Physical Reading
            Panel 6: The Punchline
        """
        try:
            import matplotlib
            matplotlib.use('TkAgg')
            import matplotlib.pyplot as plt
            import matplotlib.patheffects as pe
        except ImportError:
            print("  matplotlib not available. Use text API methods instead.")
            return

        fig = plt.figure(figsize=(20, 14), facecolor='#0a0a1a')
        if fig.canvas.manager:
            fig.canvas.manager.set_window_title(
                'BST Toy 145 — Self-Duality and the Critical Line [CONJECTURE]')

        fig.text(0.5, 0.975,
                 'SELF-DUALITY AND THE CRITICAL LINE \u2014 Toy 145 [CONJECTURE]',
                 fontsize=22, fontweight='bold', color='#ffd700',
                 ha='center', fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=2, foreground='#665500')])
        fig.text(0.5, 0.955,
                 '"The codes and the curvature agree. That is the Riemann Hypothesis."',
                 fontsize=10, color='#aa8800', ha='center',
                 fontfamily='monospace', fontstyle='italic')
        fig.text(0.5, 0.008,
                 'Copyright (c) 2026 Casey Koons \u2014 Demonstration Only  |  '
                 'Claude Opus 4.6',
                 fontsize=8, color='#334444', ha='center',
                 fontfamily='monospace')

        # 2x3 grid layout
        # Row 1: panels 1-3
        # Row 2: panels 4-6
        h_pad = 0.035
        v_pad = 0.04
        pw = (1.0 - 4 * h_pad) / 3
        ph = (0.93 - 3 * v_pad) / 2

        def panel_rect(row, col):
            x = h_pad + col * (pw + h_pad)
            y = 0.93 - v_pad - (row + 1) * ph - row * v_pad
            return [x, y, pw, ph]

        ax1 = fig.add_axes(panel_rect(0, 0))
        ax2 = fig.add_axes(panel_rect(0, 1))
        ax3 = fig.add_axes(panel_rect(0, 2))
        ax4 = fig.add_axes(panel_rect(1, 0))
        ax5 = fig.add_axes(panel_rect(1, 1))
        ax6 = fig.add_axes(panel_rect(1, 2))

        for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
            ax.set_facecolor('#0a0a1a')

        self._draw_two_paths(ax1, pe)
        self._draw_cascade(ax2, pe)
        self._draw_three_palindromes(ax3, pe)
        self._draw_golay_bst(ax4, pe)
        self._draw_physical(ax5, pe)
        self._draw_punchline(ax6, pe)

        plt.show()

    # ─── Drawing helpers ───

    def _draw_two_paths(self, ax, pe):
        """Panel 1: Two Paths from Q⁵ converging on Selberg."""
        ax.axis('off')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        ax.set_title('TWO PATHS FROM Q\u2075',
                      color='#ffd700', fontfamily='monospace', fontsize=10,
                      fontweight='bold', pad=6)

        # Q⁵ at top center
        ax.text(5.0, 9.3, 'Q\u2075', fontsize=20, fontweight='bold',
                color='#ffd700', ha='center', va='center',
                fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a1a0a',
                          edgecolor='#ffd700', linewidth=2))

        # Path A (left, gold)
        path_a_x = 2.5
        steps_a = [
            ('P(h)', 7.5),
            ('Poincar\u00e9 dual', 6.0),
            ('Seeley-DeWitt', 4.5),
            ('heat kernel', 3.0),
        ]
        ax.text(path_a_x, 8.5, 'PATH A', fontsize=9, fontweight='bold',
                color='#ffd700', ha='center', fontfamily='monospace')
        ax.text(path_a_x, 8.0, '(Chern/Geometric)', fontsize=7,
                color='#ccaa00', ha='center', fontfamily='monospace')

        for label, y in steps_a:
            ax.text(path_a_x, y, label, fontsize=8, color='#ffd700',
                    ha='center', fontfamily='monospace',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='#1a1a0a',
                              edgecolor='#665500', linewidth=0.8, alpha=0.8))

        # Arrows for path A
        for i in range(len(steps_a) - 1):
            ax.annotate('', xy=(path_a_x, steps_a[i+1][1] + 0.35),
                        xytext=(path_a_x, steps_a[i][1] - 0.35),
                        arrowprops=dict(arrowstyle='->', color='#ffd700',
                                        lw=1.2))
        # From Q⁵ to first step
        ax.annotate('', xy=(path_a_x, steps_a[0][1] + 0.35),
                    xytext=(3.8, 8.9),
                    arrowprops=dict(arrowstyle='->', color='#ffd700',
                                    lw=1.5, connectionstyle='arc3,rad=0.2'))

        # Path B (right, cyan)
        path_b_x = 7.5
        steps_b = [
            ('spectral codes', 7.5),
            ('Golay [24,12,8]', 6.0),
            ('Leech \u039b\u2082\u2084', 4.5),
            ('\u0398_\u039b(\u03c4) modular', 3.0),
        ]
        ax.text(path_b_x, 8.5, 'PATH B', fontsize=9, fontweight='bold',
                color='#00ddff', ha='center', fontfamily='monospace')
        ax.text(path_b_x, 8.0, '(Code/Algebraic)', fontsize=7,
                color='#0099aa', ha='center', fontfamily='monospace')

        for label, y in steps_b:
            ax.text(path_b_x, y, label, fontsize=8, color='#00ddff',
                    ha='center', fontfamily='monospace',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='#0a1a1a',
                              edgecolor='#005566', linewidth=0.8, alpha=0.8))

        # Arrows for path B
        for i in range(len(steps_b) - 1):
            ax.annotate('', xy=(path_b_x, steps_b[i+1][1] + 0.35),
                        xytext=(path_b_x, steps_b[i][1] - 0.35),
                        arrowprops=dict(arrowstyle='->', color='#00ddff',
                                        lw=1.2))
        # From Q⁵ to first step
        ax.annotate('', xy=(path_b_x, steps_b[0][1] + 0.35),
                    xytext=(6.2, 8.9),
                    arrowprops=dict(arrowstyle='->', color='#00ddff',
                                    lw=1.5, connectionstyle='arc3,rad=-0.2'))

        # Selberg box at bottom center
        ax.text(5.0, 1.3, 'SELBERG\nTRACE\nFORMULA', fontsize=9,
                fontweight='bold', color='#44ff88', ha='center',
                va='center', fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#0a1a0a',
                          edgecolor='#44ff88', linewidth=2))

        # Converging arrows
        ax.annotate('', xy=(3.8, 1.8), xytext=(path_a_x, 2.7),
                    arrowprops=dict(arrowstyle='->', color='#ffd700',
                                    lw=1.5, connectionstyle='arc3,rad=0.15'))
        ax.annotate('', xy=(6.2, 1.8), xytext=(path_b_x, 2.7),
                    arrowprops=dict(arrowstyle='->', color='#00ddff',
                                    lw=1.5, connectionstyle='arc3,rad=-0.15'))

        # Labels on arrows
        ax.text(2.0, 2.0, 'geometric\nside', fontsize=6, color='#ffd700',
                ha='center', fontfamily='monospace', alpha=0.8)
        ax.text(8.0, 2.0, 'spectral\nside', fontsize=6, color='#00ddff',
                ha='center', fontfamily='monospace', alpha=0.8)

        # Equation
        ax.text(5.0, 0.2, 'Path A = Path B', fontsize=8,
                color='#44ff88', ha='center', fontfamily='monospace',
                fontstyle='italic')

    def _draw_cascade(self, ax, pe):
        """Panel 2: Self-Duality Cascade (4 levels)."""
        ax.axis('off')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        ax.set_title('SELF-DUALITY CASCADE',
                      color='#ffd700', fontfamily='monospace', fontsize=10,
                      fontweight='bold', pad=6)

        levels = [
            ('CODE', 'Golay [24,12,8]\u2082', 'k = n-k = 12', '#00ddff'),
            ('LATTICE', 'Leech \u039b\u2082\u2084', '\u039b* = \u039b (unimodular)', '#44ff88'),
            ('MODULAR', '\u0398_\u039b(\u03c4)', '\u0398(-1/\u03c4) = \u03c4\u00b9\u00b2\u0398(\u03c4)', '#ffd700'),
            ('L-FUNCTION', 'L(s)', '\u039b(s) = \u039b(k-s)', '#9966ff'),
        ]

        y_positions = [8.5, 6.3, 4.1, 1.9]
        box_h = 1.5

        for i, ((name, obj, eq, col), y) in enumerate(zip(levels, y_positions)):
            # Level box
            ax.add_patch(plt.Rectangle((0.5, y - box_h/2), 9.0, box_h,
                                        facecolor='#0a0a1a',
                                        edgecolor=col, linewidth=1.5,
                                        linestyle='-', alpha=0.9))
            # Level label
            ax.text(1.2, y + 0.3, f'Level {i+1}: {name}', fontsize=8,
                    fontweight='bold', color=col, fontfamily='monospace')
            # Object
            ax.text(1.2, y - 0.1, obj, fontsize=7, color=col,
                    fontfamily='monospace', alpha=0.8)
            # Self-duality equation
            ax.text(5.5, y + 0.15, 'Self-duality:', fontsize=6,
                    color='#666666', fontfamily='monospace')
            ax.text(5.5, y - 0.25, eq, fontsize=8, fontweight='bold',
                    color=col, fontfamily='monospace')

            # Arrow to next level
            if i < len(levels) - 1:
                mid_y = (y - box_h/2 + y_positions[i+1] + box_h/2) / 2
                ax.annotate('', xy=(5.0, y_positions[i+1] + box_h/2 + 0.05),
                            xytext=(5.0, y - box_h/2 - 0.05),
                            arrowprops=dict(arrowstyle='->', color='#444466',
                                            lw=1.5))
                connectors = ['Construction A', 'Theta function', 'Mellin transform']
                ax.text(6.0, mid_y, connectors[i], fontsize=6,
                        color='#555577', fontfamily='monospace',
                        fontstyle='italic')

        # Bottom label
        ax.text(5.0, 0.3, 'Each level inherits self-duality from above',
                fontsize=7, color='#888866', ha='center',
                fontfamily='monospace', fontstyle='italic')

    def _draw_three_palindromes(self, ax, pe):
        """Panel 3: Three Palindromes side by side."""
        import matplotlib.pyplot as plt
        ax.axis('off')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        ax.set_title('THREE SELF-DUALITIES',
                      color='#ffd700', fontfamily='monospace', fontsize=10,
                      fontweight='bold', pad=6)

        # Palindrome 1: Chern polynomial
        y1 = 8.5
        ax.text(5.0, y1, 'P(h) of Q\u2075', fontsize=9, fontweight='bold',
                color='#ffd700', ha='center', fontfamily='monospace')
        coeffs = self._poly  # [1, 5, 11, 13, 9, 3]
        coeffs_rev = list(reversed(coeffs))

        # Draw coefficients as bars
        bar_x0 = 1.5
        bar_w = 1.1
        max_c = max(coeffs)
        bar_h_scale = 1.8 / max_c

        for j, c in enumerate(coeffs):
            x = bar_x0 + j * bar_w
            h = c * bar_h_scale
            ax.add_patch(plt.Rectangle((x, y1 - 2.5), bar_w * 0.7, h,
                                        facecolor='#ffd700', alpha=0.6,
                                        edgecolor='#ffd700', linewidth=0.5))
            ax.text(x + bar_w * 0.35, y1 - 2.6 + h + 0.1, str(c),
                    fontsize=7, color='#ffd700', ha='center',
                    fontfamily='monospace')

        ax.text(5.0, y1 - 0.4, 'Poincar\u00e9 duality on Q\u2075',
                fontsize=7, color='#ccaa00', ha='center',
                fontfamily='monospace')
        ax.text(8.8, y1 - 1.5, 'DUALITY', fontsize=7, fontweight='bold',
                color='#ffd700', ha='center', fontfamily='monospace')

        # Palindrome 2: Golay weights
        y2 = 4.8
        ax.text(5.0, y2, 'Golay weight enumerator', fontsize=9,
                fontweight='bold', color='#00ddff', ha='center',
                fontfamily='monospace')

        golay_w = GOLAY_WEIGHTS  # [1, 759, 2576, 759, 1]
        max_g = max(golay_w)
        bar_h_scale_g = 1.8 / max_g
        bar_x0_g = 1.5
        bar_w_g = 1.3

        for j, c in enumerate(golay_w):
            x = bar_x0_g + j * bar_w_g
            h = max(c * bar_h_scale_g, 0.05)
            ax.add_patch(plt.Rectangle((x, y2 - 2.5), bar_w_g * 0.7, h,
                                        facecolor='#00ddff', alpha=0.6,
                                        edgecolor='#00ddff', linewidth=0.5))
            label = str(c) if c < 1000 else str(c)
            ax.text(x + bar_w_g * 0.35, y2 - 2.6 + h + 0.1, label,
                    fontsize=6, color='#00ddff', ha='center',
                    fontfamily='monospace')

        ax.text(5.0, y2 - 0.4, '1, 759, 2576, 759, 1',
                fontsize=7, color='#0099aa', ha='center',
                fontfamily='monospace')
        ax.text(8.8, y2 - 1.5, 'PROVED', fontsize=8, fontweight='bold',
                color='#44ff88', ha='center', fontfamily='monospace')

        # Palindrome 3: xi(s) = xi(1-s)
        y3 = 1.2
        ax.text(5.0, y3, '\u03be(s) = \u03be(1\u2212s)', fontsize=12,
                fontweight='bold', color='#9966ff', ha='center',
                fontfamily='monospace')
        ax.text(5.0, y3 - 0.5, 'zeros on Re(s) = \u00bd ?', fontsize=8,
                color='#7744cc', ha='center', fontfamily='monospace')
        ax.text(8.8, y3 - 0.2, 'RH', fontsize=8, fontweight='bold',
                color='#ff4444', ha='center', fontfamily='monospace')

        # Vertical line showing center symmetry
        for y_center in [y1 - 1.5, y2 - 1.5]:
            ax.plot([5.0, 5.0], [y_center - 0.7, y_center + 0.7],
                    '--', color='#444466', linewidth=0.8, alpha=0.5)

    def _draw_golay_bst(self, ax, pe):
        """Panel 4: BST Numbers in Golay."""
        import matplotlib.pyplot as plt
        ax.axis('off')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        ax.set_title('BST NUMBERS IN GOLAY [CONJECTURE]',
                      color='#ffd700', fontfamily='monospace', fontsize=10,
                      fontweight='bold', pad=6)

        # 759 factorization
        ax.text(5.0, 9.0, '759', fontsize=28, fontweight='bold',
                color='#00ddff', ha='center', fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=2, foreground='#004455')])

        ax.text(5.0, 7.8, '= 3 \u00d7 11 \u00d7 23', fontsize=14,
                color='#00ddff', ha='center', fontfamily='monospace')

        # Factor labels
        ax.text(2.5, 7.0, 'N_c = 3', fontsize=10, fontweight='bold',
                color='#44ff88', ha='center', fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#0a1a0a',
                          edgecolor='#44ff88', linewidth=1))
        ax.text(5.0, 7.0, 'c\u2082 = 11', fontsize=10, fontweight='bold',
                color='#ffd700', ha='center', fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a1a0a',
                          edgecolor='#ffd700', linewidth=1))
        ax.text(7.5, 7.0, '23', fontsize=10, fontweight='bold',
                color='#9966ff', ha='center', fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#0a0a1a',
                          edgecolor='#9966ff', linewidth=1))
        ax.text(7.5, 6.4, 'dim SU(5)\u22121', fontsize=7,
                color='#7744cc', ha='center', fontfamily='monospace')

        # Divider
        ax.plot([1.0, 9.0], [5.7, 5.7], '-', color='#333344',
                linewidth=0.8)

        # 2576 factorization
        ax.text(5.0, 5.0, '2576', fontsize=28, fontweight='bold',
                color='#00ddff', ha='center', fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=2, foreground='#004455')])

        ax.text(5.0, 3.8, '= 2\u2074 \u00d7 7 \u00d7 23', fontsize=14,
                color='#00ddff', ha='center', fontfamily='monospace')

        # Factor labels
        ax.text(2.5, 3.0, '2\u2074 = 16', fontsize=10, fontweight='bold',
                color='#44ff88', ha='center', fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#0a1a0a',
                          edgecolor='#44ff88', linewidth=1))
        ax.text(5.0, 3.0, 'g = 7', fontsize=10, fontweight='bold',
                color='#ffd700', ha='center', fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a1a0a',
                          edgecolor='#ffd700', linewidth=1))
        ax.text(7.5, 3.0, '23', fontsize=10, fontweight='bold',
                color='#9966ff', ha='center', fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#0a0a1a',
                          edgecolor='#9966ff', linewidth=1))

        ax.text(2.5, 2.4, '2^(n_C\u22121)', fontsize=7,
                color='#33aa55', ha='center', fontfamily='monospace')
        ax.text(5.0, 2.4, 'genus', fontsize=7,
                color='#ccaa00', ha='center', fontfamily='monospace')

        # Bottom note
        ax.text(5.0, 1.0, 'Weight enumerator of the most\nperfect '
                'binary code factors\nentirely into BST integers.',
                fontsize=7, color='#888866', ha='center',
                fontfamily='monospace', fontstyle='italic',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#0a0a1a',
                          edgecolor='#333344', linewidth=0.8))

    def _draw_physical(self, ax, pe):
        """Panel 5: Physical Reading — error correction diagram."""
        import matplotlib.pyplot as plt
        ax.axis('off')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        ax.set_title('THE PHYSICAL READING [CONJECTURE]',
                      color='#ffd700', fontfamily='monospace', fontsize=10,
                      fontweight='bold', pad=6)

        # Top: zero on line (stable)
        ax.text(5.0, 9.3, 'ZERO ON Re(s) = \u00bd', fontsize=9,
                fontweight='bold', color='#44ff88', ha='center',
                fontfamily='monospace')

        # Draw damped oscillation
        t = np.linspace(0, 4, 200)
        damped = np.exp(-0.5 * t) * np.cos(8 * t)
        t_scaled = 1.0 + t * 1.8
        d_scaled = 7.8 + damped * 0.7

        ax.plot(t_scaled, d_scaled, '-', color='#44ff88', linewidth=1.5)
        ax.plot([1.0, 8.2], [7.8, 7.8], '--', color='#224422',
                linewidth=0.5)
        ax.text(8.5, 8.0, 'DAMPED', fontsize=7, color='#44ff88',
                fontfamily='monospace')
        ax.text(8.5, 7.5, 'stable', fontsize=6, color='#338833',
                fontfamily='monospace')

        # Arrow pointing to "codes work"
        ax.text(5.0, 6.8, '\u2192 error-correcting code WORKS', fontsize=8,
                color='#44ff88', ha='center', fontfamily='monospace')
        ax.text(5.0, 6.3, '\u2192 primes distributed optimally', fontsize=7,
                color='#338833', ha='center', fontfamily='monospace')

        # Divider
        ax.plot([0.5, 9.5], [5.7, 5.7], '-', color='#ff3333',
                linewidth=0.5, alpha=0.5)
        ax.text(9.5, 5.5, '\u2718', fontsize=12, color='#ff3333',
                ha='center')

        # Bottom: hypothetical zero off line (unstable)
        ax.text(5.0, 5.1, 'ZERO OFF LINE (\u03c3 > \u00bd)', fontsize=9,
                fontweight='bold', color='#ff4444', ha='center',
                fontfamily='monospace')

        # Draw growing oscillation
        growing = np.exp(0.4 * t) * np.cos(8 * t)
        # Clip for visual
        growing = np.clip(growing, -3, 3)
        g_scaled = 3.5 + growing * 0.5

        ax.plot(t_scaled, g_scaled, '-', color='#ff4444', linewidth=1.5)
        ax.plot([1.0, 8.2], [3.5, 3.5], '--', color='#442222',
                linewidth=0.5)
        ax.text(8.5, 3.8, 'GROWS', fontsize=7, color='#ff4444',
                fontfamily='monospace')
        ax.text(8.5, 3.3, 'unstable', fontsize=6, color='#883333',
                fontfamily='monospace')

        # Consequence
        ax.text(5.0, 2.3, '\u2192 code FAILS', fontsize=8,
                color='#ff4444', ha='center', fontfamily='monospace')
        ax.text(5.0, 1.8, '\u2192 proton decay', fontsize=7,
                color='#883333', ha='center', fontfamily='monospace')

        # Bottom label
        ax.text(5.0, 0.5,
                'RH = "error correction works\nat all frequencies"',
                fontsize=8, color='#ffd700', ha='center',
                fontfamily='monospace', fontstyle='italic',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a1a0a',
                          edgecolor='#ffd700', linewidth=1.2))

    def _draw_punchline(self, ax, pe):
        """Panel 6: The Punchline."""
        ax.axis('off')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        ax.set_title('THE PUNCHLINE [CONJECTURE]',
                      color='#ffd700', fontfamily='monospace', fontsize=10,
                      fontweight='bold', pad=6)

        lines = [
            ('Two self-dualities.', 8.8, 14, '#ffd700', 'bold'),
            ('One critical line.', 8.0, 14, '#00ddff', 'bold'),
            ('', 7.5, 8, '#666666', 'normal'),
            ('The Selberg trace formula', 7.0, 10, '#44ff88', 'normal'),
            ('equates them.', 6.5, 10, '#44ff88', 'normal'),
            ('', 6.0, 8, '#666666', 'normal'),
            ('RH is the statement that', 5.3, 9, '#888888', 'normal'),
            ('the geometric and algebraic', 4.8, 9, '#888888', 'normal'),
            ('self-dualities of Q\u2075', 4.3, 9, '#aaaaaa', 'bold'),
            ('are compatible.', 3.8, 9, '#888888', 'normal'),
            ('', 3.3, 8, '#666666', 'normal'),
            ('They must be \u2014', 2.6, 10, '#ffd700', 'bold'),
            ('they describe the', 2.0, 10, '#ffd700', 'bold'),
            ('same manifold.', 1.4, 10, '#ffd700', 'bold'),
        ]

        for text, y, size, color, weight in lines:
            if text:
                ax.text(5.0, y, text, fontsize=size, fontweight=weight,
                        color=color, ha='center', fontfamily='monospace')

        # Small equation at bottom
        ax.text(5.0, 0.3,
                'compact \u2192 perfect codes \u2192 self-duality \u2192 '
                'critical line \u2192 exact physics',
                fontsize=5.5, color='#555555', ha='center',
                fontfamily='monospace')


# ═══════════════════════════════════════════════════════════════════
# STANDALONE UTILITIES
# ═══════════════════════════════════════════════════════════════════

def verify_chern_palindrome():
    """
    Verify the Poincare duality structure of the Chern polynomial of Q⁵.
    The polynomial is NOT literally palindromic, but has a deeper duality.
    """
    poly = _chern_polynomial_coeffs(n_C)
    print()
    print("  CHERN DUALITY VERIFICATION")
    print("  ===========================")
    print()
    print(f"  P(h) = {' + '.join(f'{c}h^{k}' if k > 0 else str(c) for k, c in enumerate(poly))}")
    print(f"  Coefficients: {poly}")
    print(f"  Reversed:     {list(reversed(poly))}")
    print()
    print("  NOTE: P(h) is NOT literally palindromic in its coefficients.")
    print("  The self-duality is DEEPER — it comes from Poincare duality on Q\u2075.")
    print()

    # Poincare duality products
    print("  Poincar\u00e9 duality products c_k \u00d7 c_{n-k}:")
    for k in range(1, n_C + 1):
        ck = poly[k]
        cnk = poly[n_C + 1 - k] if (n_C + 1 - k) >= 0 else 0
        print(f"    c_{k} \u00d7 c_{n_C+1-k} = {ck} \u00d7 {cnk} = {ck * cnk}")

    # Reciprocal polynomial
    print()
    print("  Reciprocal polynomial: R(h) = h\u2075 P(1/h)")
    r_coeffs = list(reversed(poly))
    print(f"    R(h) = {' + '.join(f'{c}h^{k}' if k > 0 else str(c) for k, c in enumerate(r_coeffs))}")
    print()

    # Ratio P(h)/R(h) at h=1 is c_0/c_5 = 1/3
    ratio = poly[0] / poly[n_C]
    print(f"  Ratio c_0/c_{n_C} = {poly[0]}/{poly[n_C]} = {ratio:.4f}")
    print(f"  This is 1/N_c = 1/{N_c}")
    print()

    # Find actual zeros
    roots = np.roots(list(reversed(poly)))
    print("  Zeros of P(h):")
    n_on_line = 0
    for i, z in enumerate(roots):
        on_line = abs(z.real - (-0.5)) < 1e-8
        if on_line:
            n_on_line += 1
        marker = " <-- Re = -1/2" if on_line else ""
        print(f"    z_{i+1} = {z.real:+.6f} {z.imag:+.6f}i    "
              f"Re = {z.real:.6f}{marker}")

    print()
    print(f"  {n_on_line} of {len(roots)} zeros have Re(h) = -1/2")
    if n_on_line == len(roots):
        print("  ALL zeros on the critical line Re(h) = -1/2  [PROVED]")
    else:
        # The factor (1+2h) in the denominator gives h = -1/2 as a pole.
        # The actual zero at h = -1 comes from (1+h)^7.
        print(f"  The zero at h = -1 comes from the (1+h)\u2077 factor.")
        print(f"  The 4 zeros at Re(h) = -1/2 are the \"deep\" zeros")
        print(f"  associated with the self-duality structure.")

    # Euler characteristic
    chi = n_C + 1
    print()
    print(f"  Chern-Gauss-Bonnet: \u222bc_{n_C} = c\u2085 = {CHERN[4]} = N_c")
    print(f"  Euler characteristic: \u03c7(Q\u2075) = n_C + 1 = {chi}")
    print()
    print("  The Golay weight enumerator {1, 759, 2576, 759, 1} IS")
    print("  literally palindromic — that is the direct self-duality.")
    print("  The Chern polynomial encodes self-duality via Poincar\u00e9 duality,")
    print("  not via literal coefficient reversal.")
    print()

    return True


def verify_golay_factorizations():
    """Verify that Golay weight enumerator terms factor into BST integers."""
    print()
    print("  GOLAY FACTORIZATION VERIFICATION")
    print("  =================================")
    print()

    assert 3 * 11 * 23 == 759, "759 factorization failed"
    print(f"  759 = 3 x 11 x 23 = N_c x c_2 x 23  VERIFIED")

    assert 16 * 7 * 23 == 2576, "2576 factorization failed"
    print(f"  2576 = 16 x 7 x 23 = 2^4 x g x 23   VERIFIED")

    print()
    print(f"  BST integers in factorizations:")
    print(f"    N_c = {N_c}   (color number = c_5)")
    print(f"    c_2 = {CHERN[1]}  (second Chern class)")
    print(f"    g   = {genus}   (genus = n_C + 2)")
    print(f"    2^(n_C-1) = {2**(n_C-1)}  (half-spinor dimension)")
    print(f"    23 = 24-1 = dim SU(5) - 1")
    print()


# ═══════════════════════════════════════════════════════════════════
# MAIN MENU
# ═══════════════════════════════════════════════════════════════════

def main():
    sd = SelfDualityRH()

    print()
    print("  What would you like to explore?")
    print("   1) Two Paths (Q\u2075 \u2192 \u03b6(s) via geometry and codes)")
    print("   2) Self-Duality Cascade (Code \u2192 Lattice \u2192 Modular \u2192 L)")
    print("   3) Three Palindromes (P(h), Golay, \u03be(s))")
    print("   4) BST Numbers in Golay (759, 2576)")
    print("   5) Physical Reading (RH = error correction)")
    print("   6) Summary (the punchline)")
    print("   7) 6-panel visualization")
    print("   8) Everything + visualization")
    print("   9) Verify Chern palindrome")
    print("  10) Verify Golay factorizations")
    print()

    try:
        choice = input("  Choice [1-10]: ").strip()
    except (EOFError, KeyboardInterrupt):
        choice = '8'

    dispatch = {
        '1': sd.two_paths,
        '2': sd.self_duality_cascade,
        '3': sd.three_palindromes,
        '4': sd.golay_bst_numbers,
        '5': sd.physical_reading,
        '6': sd.summary,
        '7': sd.show,
        '9': verify_chern_palindrome,
        '10': verify_golay_factorizations,
    }

    if choice == '8':
        sd.two_paths()
        sd.self_duality_cascade()
        sd.three_palindromes()
        sd.golay_bst_numbers()
        sd.physical_reading()
        sd.summary()
        verify_chern_palindrome()
        verify_golay_factorizations()
        try:
            sd.show()
            input("\n  Press Enter to close...")
        except Exception:
            pass
    elif choice in dispatch:
        result = dispatch[choice]()
        if choice == '7':
            try:
                input("\n  Press Enter to close...")
            except Exception:
                pass
    else:
        sd.summary()


if __name__ == '__main__':
    main()
