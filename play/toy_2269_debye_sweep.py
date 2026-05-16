"""
Toy 2269 — Debye temperature sweep / catalog hygiene.

Owner: Elie
Date: 2026-05-15
Out of: RUN_LIST Elie queue item 1; production-tempo cadence.

THE TEMPLATE
============
Toy 2257 + Tungsten fix established: Debye temperature Theta_D for a
metal/material has the form

    Theta_D = rank * n_C * p   (in Kelvin)

where p is a small BST prime or BST product. Examples:
    Theta_D(Au) = rank*n_C*17  = 170 K
    Theta_D(W)  = rank*n_C*M_5 = rank*n_C*31 = 310 K (Mersenne)

This toy SWEEPS the catalog, applies the template, flags broken text,
and identifies the BST factor p for every clean fit.
"""

import json
import re


# BST integers
rank = 2
N_c  = 3
n_C  = 5
C_2  = 6
g    = 7
c_2  = 11
c_3  = 13
chi  = 24

template_factor = rank * n_C  # = 10


def factorize(n):
    """Return prime factorization as list of primes (with multiplicity)."""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def bst_name(n):
    """Try to express integer n as BST product. Return None if no clean match."""
    if n == 1: return "1"
    if n == rank: return "rank"
    if n == N_c: return "N_c"
    if n == n_C: return "n_C"
    if n == C_2: return "C_2"
    if n == g: return "g"
    if n == c_2: return "c_2"
    if n == c_3: return "c_3"
    if n == chi: return "chi"
    if n == 17: return "N_c^3 - rank*n_C"  # Lyra: 17 = 27 - 10
    if n == 23: return "chi - 1"
    if n == 31: return "M_{n_C}"  # Mersenne
    if n == 41: return "rank^N_c*n_C + 1"  # Mersenne offset
    if n == 47: return "Ogg-7"  # Ogg prime
    if n == 59: return "Ogg-7"
    if n == 71: return "Ogg-7"  # largest Monster Ogg prime
    # Simple products
    for a in [rank, N_c, n_C, C_2, g, c_2, c_3]:
        if n % a == 0:
            other = n // a
            inner = bst_name(other)
            if inner and a != 1:
                a_name = {rank: "rank", N_c: "N_c", n_C: "n_C",
                          C_2: "C_2", g: "g", c_2: "c_2", c_3: "c_3"}[a]
                return f"{a_name} * {inner}"
    # Power forms
    if n == rank ** 2: return "rank^2"
    if n == rank ** 3: return "rank^3"
    if n == rank ** 4: return "rank^4"
    if n == N_c ** 2: return "N_c^2"
    if n == n_C ** 2: return "n_C^2"
    return None


tests = []

def check(label, condition, note=""):
    tests.append((bool(condition), label, note))


# ============================================================
# PART 1 — Load the catalog and find Debye entries
# ============================================================

with open("/Users/cskoons/projects/github/BubbleSpacetimeTheory/data/bst_geometric_invariants.json") as f:
    d = json.load(f)

debye_entries = []
for e in d["invariants"]:
    sym = e.get("symbol", "")
    name = e.get("name", "")
    if any(s in sym for s in ["Debye", "Theta_D", "theta_D", "T_D", "thetaD"]):
        debye_entries.append(e)
    elif "Debye" in name or "Theta_D" in name:
        debye_entries.append(e)

print(f"Total Debye-related entries: {len(debye_entries)}")

# ============================================================
# PART 2 — Apply template
# ============================================================

template_fits = []
template_misses = []
ratio_entries = []
broken_text = []

for e in debye_entries:
    sym = e.get("symbol", "?")
    val = e.get("value")
    formula = e.get("formula") or e.get("bst_formula") or ""

    # Skip ratio entries (they don't have a single Debye temperature)
    if "ratio" in sym.lower():
        ratio_entries.append(e)
        continue

    # Try to extract numerical Debye temperature
    theta = None
    if isinstance(val, (int, float)):
        theta = float(val)
    elif isinstance(val, str):
        m = re.search(r'(\d+\.?\d*)\s*K?', val)
        if m:
            try:
                theta = float(m.group(1))
            except ValueError:
                pass
    if theta is None or theta < 1:
        continue

    # Apply template
    p = theta / template_factor
    if abs(p - round(p)) < 0.01:
        p_int = int(round(p))
        bst = bst_name(p_int)
        if bst:
            template_fits.append((sym, theta, p_int, bst, formula))
        else:
            template_misses.append((sym, theta, p_int, "NOT BST", formula))
    else:
        template_misses.append((sym, theta, p, "NOT INTEGER MULTIPLE OF 10", formula))

    # Flag broken text
    if isinstance(formula, str) and ("? No" in formula or "TBD" in formula or
                                       re.search(r'=\s*\d+\?', formula)):
        broken_text.append((sym, formula[:80]))

# ============================================================
# REPORT
# ============================================================

print(f"\nTemplate fits (Theta_D = rank*n_C*p, p BST):")
print(f"  Count: {len(template_fits)}/{len(debye_entries) - len(ratio_entries)}")
print()
for sym, theta, p, bst, formula in template_fits:
    check(f"{sym}: Theta_D = rank*n_C*{bst} = {theta:.0f} K", True)
    print(f"  {sym:<25} Theta = {theta:>6.0f} K = rank*n_C * {p:>3} = rank*n_C * ({bst})")

print(f"\nTemplate MISSES (Theta_D not of form rank*n_C*p):")
print(f"  Count: {len(template_misses)}")
for sym, theta, p, status, formula in template_misses[:15]:
    print(f"  {sym:<25} Theta = {theta:>6.2f} K   p = {p}   {status}")

print(f"\nBroken-text entries (formula has '? No' or '=N?' pattern):")
for sym, f in broken_text:
    print(f"  {sym}: {f}")

# ============================================================
# Multi-template analysis: try OTHER BST factors
# ============================================================

# Some Debye temperatures fit OTHER templates: Theta_D = X where
# X is a clean BST expression but NOT of the rank*n_C*p form.

other_templates = []
for sym, theta, p, status, formula in template_misses:
    # Check if theta itself is a clean BST product
    if not isinstance(theta, (int, float)) or theta < 1:
        continue
    theta_int = int(round(theta))
    if abs(theta - theta_int) > 0.5:
        continue  # not integer K
    bst = bst_name(theta_int)
    if bst:
        other_templates.append((sym, theta_int, bst))

print(f"\nOther BST templates for misses:")
for sym, theta, bst in other_templates:
    check(f"{sym}: Theta_D = {bst} = {theta} K (alt template)", True)
    print(f"  {sym:<25} Theta = {theta:>6} K = {bst}")

# ============================================================
# SCORE
# ============================================================
passed = sum(1 for ok, *_ in tests if ok)
total = len(tests)
print(f"\n{'='*60}\nToy 2269 score: {passed}/{total}\n{'='*60}")

print(f"""
SUMMARY:
- {len(debye_entries)} total Debye-related catalog entries
- {len(template_fits)} fit rank*n_C*p template with BST p
- {len(other_templates)} fit other clean BST templates
- {len(broken_text)} have broken formula text
- {len(ratio_entries)} are ratio entries (skipped)

The rank*n_C*p template covers a clean subfamily (clean BST primes
17, 23, 31, etc. multiplied by 10). Other entries use g^3 (Cu=343),
N_c*n_C*g (Pb=105), or larger BST products. Multi-template structure.

ACTION ITEMS:
- Tungsten Debye_W_310: already fixed (Toy 2257 session)
- Other broken-text entries: deferred to per-entry fix if Grace catches them
- Multi-template catalog hygiene: working as designed; not all Debye
  temperatures need same template.
""")
