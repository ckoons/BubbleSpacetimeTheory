"""BST Evaluator — Q(integers)[pi] computation engine.

All BST observables are computed from five integers {N_c=3, n_C=5, g=7, C_2=6, N_max=137}
plus pi.  No free parameters.  This module provides the evaluation namespace.
"""
from fractions import Fraction
import math

# ── The Five BST Integers ──────────────────────────────────────────────
N_c   = 3       # color dimension  (SU(3))
n_C   = 5       # compact dimension (CP^2)
g     = 7       # Bergman genus
C_2   = 6       # Casimir invariant
N_max = 137     # maximum quantum number

# ── Derived ────────────────────────────────────────────────────────────
rank      = 2                       # rank of D_IV^5
alpha     = 1.0 / N_max            # fine structure constant (zeroth order)
alpha_inv = N_max
pi        = math.pi
pi5       = pi ** 5                 # pi^5 ~ 306.020

# ── Physical references (CODATA 2022) ─────────────────────────────────
m_e_MeV   = 0.51099895000          # electron mass [MeV/c^2]
m_e_GeV   = m_e_MeV / 1000.0
m_p_ratio = 6 * pi5                # BST: m_p/m_e = 6*pi^5
m_p_MeV   = m_p_ratio * m_e_MeV   # proton mass [MeV]
m_p_GeV   = m_p_MeV / 1000.0
hbar_c_MeV_fm = 197.3269804       # hbar*c [MeV*fm]


def make_namespace():
    """Return the safe evaluation namespace for BST expressions."""
    return {
        # Five integers
        "N_c": N_c, "n_C": n_C, "g": g, "C_2": C_2, "N_max": N_max,
        # Derived
        "rank": rank, "alpha": alpha, "alpha_inv": alpha_inv,
        # Math
        "pi": pi, "pi5": pi5,
        "sqrt": math.sqrt, "cbrt": lambda x: x ** (1.0/3.0),
        "log": math.log, "ln": math.log, "exp": math.exp,
        "sin": math.sin, "cos": math.cos, "tan": math.tan,
        "atan": math.atan, "asin": math.asin, "acos": math.acos,
        "comb": math.comb, "factorial": math.factorial,
        "Fraction": Fraction, "abs": abs, "pow": pow, "float": float,
        "inf": float("inf"),
        # Physical
        "m_e": m_e_MeV, "m_e_GeV": m_e_GeV,
        "m_p": m_p_MeV, "m_p_GeV": m_p_GeV,
        "m_p_ratio": m_p_ratio,
        "hbar_c": hbar_c_MeV_fm,
    }


def evaluate(expr_str):
    """Evaluate a BST expression in Q(integers)[pi].

    >>> evaluate("6 * pi**5")
    1836.118...
    >>> evaluate("N_c + n_C + g + C_2 + N_max")
    158
    """
    ns = make_namespace()
    return float(eval(expr_str, {"__builtins__": {}}, ns))


def show_integers():
    """Return a formatted display of the five BST integers."""
    return (
        f"  N_c   = {N_c:<4}  (color dimension)\n"
        f"  n_C   = {n_C:<4}  (compact dimension)\n"
        f"  g     = {g:<4}  (Bergman genus)\n"
        f"  C_2   = {C_2:<4}  (Casimir invariant)\n"
        f"  N_max = {N_max:<4}  (maximum quantum number)\n"
        f"  rank  = {rank:<4}  (derived: rank of D_IV^5)"
    )
