"""BST Candidate Generator — enumerate integer expressions for discovery.

Given an observed value and type, generates all BST integer expressions
that match within tolerance.  This is the core of the write path.

Safety: NEVER auto-registers.  Only proposes candidates for Keeper audit.
"""
import math
from itertools import combinations

# ── The Five Integers + Derived ────────────────────────────────────────
N_c, n_C, g, C_2, N_max, rank = 3, 5, 7, 6, 137, 2
pi = math.pi
alpha = 1.0 / N_max

# ── Base Integer Expressions ──────────────────────────────────────────
# Level 0: the five integers + rank
_BASE = {
    "N_c": N_c, "n_C": n_C, "g": g, "C_2": C_2, "N_max": N_max,
    "rank": rank,
}

# Level 1: simple derivations (powers, small products, combinations)
_DERIVED = {
    "2*rank": 2*rank,
    "2*N_c": 2*N_c,
    "2*n_C": 2*n_C,
    "2*g": 2*g,
    "2*C_2": 2*C_2,
    "N_c^2": N_c**2,
    "n_C^2": n_C**2,
    "g^2": g**2,
    "C_2^2": C_2**2,
    "N_c^3": N_c**3,
    "2^rank": 2**rank,
    "2^N_c": 2**N_c,
    "2^n_C": 2**n_C,
    "C(g,2)": math.comb(g, 2),      # 21
    "C(g,3)": math.comb(g, 3),      # 35
    "C(g,4)": math.comb(g, 4),      # 35 (same!)
    "C(n_C,2)": math.comb(n_C, 2),  # 10
    "n_C!": math.factorial(n_C),     # 120
    "N_c!": math.factorial(N_c),     # 6 = C_2
    "2n_C+1": 2*n_C + 1,            # 11
    "2g-1": 2*g - 1,                # 13
    "N_c+2n_C": N_c + 2*n_C,        # 13
    "N_max+rank": N_max + rank,      # 139
    "N_max-1": N_max - 1,           # 136
    "g-1": g - 1,                    # 6 = C_2
    "g+1": g + 1,                    # 8 = 2^N_c
    "n_C+2*g": n_C + 2*g,           # 19 — the Bubble number
    "N_c+2*C_2+rank": N_c + 2*C_2 + rank,  # 17
    "2^rank*n_C": 2**rank * n_C,    # 20 = amino acids
    "2^rank*g": 2**rank * g,        # 28
    "2^rank*C_2": 2**rank * C_2,    # 24
    "2^rank*N_c": 2**rank * N_c,    # 12
    "N_c*C_2+rank": N_c*C_2+rank,   # 20
    "C_2*N_c-rank": C_2*N_c-rank,   # 16
    "2^N_c*N_c": 2**N_c * N_c,     # 24
    "N_c^2+n_C": N_c**2 + n_C,     # 14
    "n_C^2-C_2": n_C**2 - C_2,     # 19
}

# Level 1: products of pairs of base integers
for (n1, v1), (n2, v2) in combinations(_BASE.items(), 2):
    key = f"{n1}*{n2}"
    _DERIVED[key] = v1 * v2

# Add some triple products
_DERIVED["N_c*n_C*g"] = N_c * n_C * g          # 105
_DERIVED["N_c*C_2*g"] = N_c * C_2 * g          # 126
_DERIVED["rank*n_C*C_2"] = rank * n_C * C_2    # 60

# ── All Integer Expressions (positive) ─────────────────────────────────
INTEGERS = {}
INTEGERS.update(_BASE)
INTEGERS.update(_DERIVED)
# Filter to positive values
INTEGERS = {k: v for k, v in INTEGERS.items() if v > 0}

# ── Ratio Expressions ─────────────────────────────────────────────────
RATIOS = {}
for (n1, v1), (n2, v2) in ((a, b) for a in INTEGERS.items() for b in INTEGERS.items()):
    if v2 > 0 and n1 != n2:
        ratio = v1 / v2
        if 1e-4 < ratio < 1e4:  # reasonable range
            key = f"{n1}/{n2}"
            RATIOS[key] = ratio

# Special transcendental-containing ratios
RATIOS["alpha"] = alpha
RATIOS["1/pi"] = 1/pi
RATIOS["pi"] = pi
RATIOS["N_c/(n_C*pi)"] = N_c / (n_C * pi)   # f = 19.1%
RATIOS["1-2^(-1/N_c)"] = 1 - 2**(-1/N_c)    # f_crit = 20.6%
RATIOS["6*pi^5"] = 6 * pi**5                  # m_p/m_e
RATIOS["pi^2"] = pi**2
RATIOS["pi^3"] = pi**3
RATIOS["pi^4"] = pi**4
RATIOS["pi^5"] = pi**5

# ── Pi-containing products ────────────────────────────────────────────
for name, val in list(_BASE.items()):
    RATIOS[f"{name}*pi"] = val * pi
    RATIOS[f"{name}/pi"] = val / pi
    RATIOS[f"{name}*pi^2"] = val * pi**2
    RATIOS[f"pi/{name}"] = pi / val
    RATIOS[f"pi^2/{name}"] = pi**2 / val


def find_count_matches(observed, tolerance=0.001):
    """Find BST integer expressions matching an exact count."""
    matches = []
    for name, val in INTEGERS.items():
        if isinstance(observed, int) and val == observed:
            matches.append((name, val, 0.0))
        elif abs(val - observed) / max(abs(observed), 1) < tolerance:
            matches.append((name, val, abs(val - observed) / max(abs(observed), 1)))
    matches.sort(key=lambda x: x[2])
    return matches[:10]


def find_ratio_matches(observed, tolerance=0.02):
    """Find BST expressions matching a dimensionless ratio."""
    matches = []
    pool = {**INTEGERS, **RATIOS}
    for name, val in pool.items():
        if observed != 0:
            error = abs(val - observed) / abs(observed)
            if error < tolerance:
                matches.append((name, val, error))
    matches.sort(key=lambda x: x[2])
    return matches[:10]


def find_angle_matches(observed_deg, tolerance=0.02):
    """Find BST expressions for an angle in degrees.

    Tries:
      1. arccos(BST ratio) in degrees
      2. Direct BST integer product as degrees
      3. BST ratio as degrees
    """
    matches = []

    # Try arccos of ratios
    for name, val in {**INTEGERS, **RATIOS}.items():
        if -1 <= val <= 1:
            angle = math.degrees(math.acos(val))
            error = abs(angle - observed_deg) / abs(observed_deg) if observed_deg != 0 else abs(angle)
            if error < tolerance:
                matches.append((f"arccos({name})", angle, error))
            # Also try -val
            angle_neg = math.degrees(math.acos(-val))
            error_neg = abs(angle_neg - observed_deg) / abs(observed_deg) if observed_deg != 0 else abs(angle_neg)
            if error_neg < tolerance:
                matches.append((f"arccos(-{name})", angle_neg, error_neg))

    # Try direct integer values as degrees
    for name, val in INTEGERS.items():
        if val > 0:
            error = abs(val - observed_deg) / abs(observed_deg) if observed_deg != 0 else abs(val)
            if error < tolerance:
                matches.append((f"{name} deg", float(val), error))

    # Try ratio values as degrees
    for name, val in RATIOS.items():
        if val > 0:
            error = abs(val - observed_deg) / abs(observed_deg) if observed_deg != 0 else abs(val)
            if error < tolerance:
                matches.append((f"{name} deg", val, error))

    matches.sort(key=lambda x: x[2])
    return matches[:10]


def find_length_matches(observed_bohr, tolerance=0.02):
    """Find BST expressions for a length in Bohr radii (a₀ units)."""
    matches = []
    pool = {**INTEGERS, **RATIOS}
    for name, val in pool.items():
        if val > 0:
            error = abs(val - observed_bohr) / abs(observed_bohr) if observed_bohr != 0 else abs(val)
            if error < tolerance:
                matches.append((f"a_0 * {name}", val, error))
    matches.sort(key=lambda x: x[2])
    return matches[:10]


def find_energy_matches(observed_ry, tolerance=0.02):
    """Find BST expressions for an energy in Rydberg units."""
    matches = []
    pool = {**INTEGERS, **RATIOS}
    for name, val in pool.items():
        if val > 0:
            error = abs(val - observed_ry) / abs(observed_ry) if observed_ry != 0 else abs(val)
            if error < tolerance:
                matches.append((f"Ry * {name}", val, error))
    matches.sort(key=lambda x: x[2])
    return matches[:10]


def find_matches(observed, obs_type="ratio", tolerance=0.02):
    """Master dispatcher: find BST matches for any observable type.

    obs_type: "count", "ratio", "angle_deg", "length_bohr", "energy_ry"
    """
    if obs_type == "count":
        return find_count_matches(observed, tolerance)
    elif obs_type == "ratio":
        return find_ratio_matches(observed, tolerance)
    elif obs_type == "angle_deg":
        return find_angle_matches(observed, tolerance)
    elif obs_type == "length_bohr":
        return find_length_matches(observed, tolerance)
    elif obs_type == "energy_ry":
        return find_energy_matches(observed, tolerance)
    else:
        return find_ratio_matches(observed, tolerance)
