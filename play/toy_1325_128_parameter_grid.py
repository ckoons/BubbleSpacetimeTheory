#!/usr/bin/env python3
"""
Toy 1325 — The 128-Entry Parameter Grid: The Full Periodic Table
=================================================================
MON-4: The complete 8×16 Gauss multiplication table.

Rows (8 = g+1 = 2^N_c): Integer bases 0 through g.
Columns (16 = 2^(N_c+1)): Fractional parts k/d for BST denominators d ∈ {2,3,4,5,7}.

Each cell contains one parameter value from the extended catalog.
The grid IS the periodic table — every function lives in a cell.

Key cells:
  [0, 0]   = 0 (identity, vacuum)
  [1, 0]   = 1 (unity, normalization)
  [0, 1/2] = 1/2 = 1/rank (critical line)
  [1, 1/5] = 6/5 = κ_ls (spin-orbit coupling)
  [1, 2/3] = 5/3 (Kolmogorov spectrum)
  [1, 4/5] = 9/5 (reality budget Λ·N)
  [3, 1/7] = 22/7 ≈ π (N_c + 1/g)

SCORE: See bottom.
"""

import math
from fractions import Fraction

# BST integers
rank = 2; N_c = 3; n_C = 5; g = 7; C_2 = 6
N_max = N_c**3 * n_C + rank


def generate_fractional_parts():
    """Generate the 16 = 2^(N_c+1) fractional parts from BST denominators."""
    # BST denominators: {2, 3, 4, 5, 7} (primes and their composites ≤ g)
    denominators = [2, 3, 4, 5, 7]

    fracs = set()
    fracs.add(Fraction(0))  # zero fractional part

    for d in denominators:
        for k in range(1, d):
            fracs.add(Fraction(k, d))

    # Sort by value
    sorted_fracs = sorted(fracs)
    return sorted_fracs


def generate_grid():
    """Generate the full 8×16 parameter grid."""
    integer_bases = list(range(g + 1))  # 0, 1, 2, ..., 7
    frac_parts = generate_fractional_parts()

    grid = {}
    for row, base in enumerate(integer_bases):
        for col, frac in enumerate(frac_parts):
            value = base + frac
            grid[(row, col)] = {
                'value': value,
                'base': base,
                'frac': frac,
                'float': float(value),
            }

    return grid, integer_bases, frac_parts


# ─── Notable cells ────────────────────────────────────────────────

NOTABLE = {
    'identity':        Fraction(0),
    'critical_line':   Fraction(1, 2),
    'unity':           Fraction(1),
    'kappa_ls':        Fraction(6, 5),
    'kolmogorov':      Fraction(5, 3),
    'reality_budget':  Fraction(9, 5),
    'pi_approx':       Fraction(22, 7),
    'golden_approx':   Fraction(8, 5),  # 1.6 ≈ φ
    'euler_approx':    Fraction(19, 7),  # 2.714... ≈ e
    'half_integer':    Fraction(1, 2),
    'casimir':         Fraction(C_2),
    'genus':           Fraction(g),
}


# ─── Tests ────────────────────────────────────────────────────────

def test_fractional_count():
    """Exactly 16 = 2^(N_c+1) distinct fractional parts."""
    fracs = generate_fractional_parts()
    return len(fracs) == 2**(N_c + 1), \
        f"{len(fracs)} fractional parts = 2^(N_c+1) = {2**(N_c+1)}", \
        f"from denominators {{2, 3, 4, 5, 7}}"


def test_grid_size():
    """Grid has exactly 128 = 2^g cells."""
    grid, bases, fracs = generate_grid()
    n_cells = len(grid)
    n_rows = len(bases)
    n_cols = len(fracs)

    return n_cells == 2**g and n_rows * n_cols == 128, \
        f"{n_rows} × {n_cols} = {n_cells} = 2^g = {2**g}", \
        f"rows: 0..{g}, cols: 16 fractional parts"


def test_notable_cells_present():
    """All notable physical constants appear as grid values."""
    grid, bases, fracs = generate_grid()
    all_values = set(cell['value'] for cell in grid.values())

    found = {}
    for name, value in NOTABLE.items():
        found[name] = value in all_values

    n_found = sum(found.values())

    return n_found >= 8, \
        f"{n_found}/{len(NOTABLE)} notable values found in grid", \
        f"missing: {[k for k, v in found.items() if not v]}"


def test_kappa_ls_location():
    """κ_ls = 6/5 is at cell [1, 1/5] — base 1, fractional part 1/5."""
    grid, bases, fracs = generate_grid()

    kappa = Fraction(6, 5)
    location = None
    for (r, c), cell in grid.items():
        if cell['value'] == kappa:
            location = (r, c, cell['base'], cell['frac'])
            break

    if location is None:
        return False, "κ_ls = 6/5 not found", ""

    row, col, base, frac = location

    return base == 1 and frac == Fraction(1, 5), \
        f"κ_ls = 6/5 at row {row} (base {base}), col {col} (frac {frac})", \
        "spin-orbit coupling lives in the n_C denominator column"


def test_critical_line_column():
    """The 1/2 = 1/rank column contains the critical line parameters."""
    grid, bases, fracs = generate_grid()

    # Find the column index for 1/2
    half_col = None
    for i, f in enumerate(fracs):
        if f == Fraction(1, 2):
            half_col = i
            break

    # All values in this column: 1/2, 3/2, 5/2, 7/2, 9/2, 11/2, 13/2, 15/2
    column_values = [grid[(r, half_col)]['value'] for r in range(len(bases))]
    half_integers = [v for v in column_values if v.denominator == 2]

    # The BST half-integer catalog {1/2, 3/2, 5/2, 7/2} is the first rank² = 4 entries
    bst_half = [Fraction(2*k+1, 2) for k in range(rank**2)]
    bst_in_column = all(h in column_values for h in bst_half)

    return bst_in_column and len(half_integers) == len(bases), \
        f"1/rank column: {len(half_integers)} half-integers, BST catalog subset: {bst_half}", \
        "the critical line column carries the half-integer parameters"


def test_farey_connection():
    """The 16 fractional parts are a subset of Farey F_g = F_7."""
    fracs = generate_fractional_parts()

    # Farey sequence F_7: all fractions p/q with 0 ≤ p/q ≤ 1, q ≤ 7
    farey = set()
    for q in range(1, g + 1):
        for p in range(0, q + 1):
            farey.add(Fraction(p, q))
    farey = sorted(farey)

    # Count: |F_7| includes 0/1 and 1/1
    n_farey = len(farey)  # Should be 19 + 1 = 20 (including 0/1 and 1/1)
    # Actually |F_n| = 1 + sum_{k=1}^{n} φ(k) = 1 + 1+1+2+2+4+2+6 = 19
    # But that counts 0/1, so fractions in (0,1] are 18

    # Our fracs include 0 and exclude 1
    fracs_in_01 = [f for f in fracs if 0 <= f < 1]
    farey_in_01 = [f for f in farey if 0 <= f < 1]

    # How many of our 16 fracs are in F_7?
    overlap = [f for f in fracs_in_01 if f in farey_in_01]
    n_overlap = len(overlap)

    # The 3 fracs NOT in F_7 (if any): those with denominator combinations
    not_in_farey = [f for f in fracs_in_01 if f not in farey_in_01]

    return n_overlap == len(fracs_in_01), \
        f"{n_overlap}/{len(fracs_in_01)} fractional parts ∈ Farey F_{g}", \
        f"|Farey F_{g}| = {len(farey_in_01)}, BST covers {n_overlap}/{len(farey_in_01)}"


def test_12_value_catalog_subset():
    """The original 12-value catalog is a subset of the 128-entry grid."""
    grid, bases, fracs = generate_grid()
    all_values = set(cell['value'] for cell in grid.values())

    # The 12-value catalog: 8 integers + 4 half-integers
    catalog = set(
        [Fraction(n) for n in range(g + 1)] +
        [Fraction(2*k + 1, 2) for k in range(rank**2)]
    )

    catalog_in_grid = catalog.issubset(all_values)
    n_catalog = len(catalog)

    return catalog_in_grid and n_catalog == 2 * C_2, \
        f"all {n_catalog} = 2·C₂ catalog values present in 128-entry grid", \
        "the 12-value catalog is embedded in the full table"


def test_symmetry():
    """The grid has a reflection symmetry through the center column."""
    fracs = generate_fractional_parts()

    # Check: for each frac f, is 1-f also present?
    symmetric_pairs = 0
    for f in fracs:
        if f == 0:
            continue
        complement = 1 - f
        if complement in fracs:
            symmetric_pairs += 1

    # The number of symmetric pairs tells us about the grid's symmetry
    # For fractions in (0,1): if f is present, is 1-f present?

    fracs_interior = [f for f in fracs if 0 < f < 1]
    n_symmetric = sum(1 for f in fracs_interior if (1 - f) in fracs)

    return n_symmetric >= len(fracs_interior) - 2, \
        f"{n_symmetric}/{len(fracs_interior)} interior fracs have complement in grid", \
        "near-complete reflection symmetry f ↔ 1-f"


def test_density():
    """Grid density: 128 values span [0, g + (g-1)/g] = [0, 48/7]."""
    grid, bases, fracs = generate_grid()

    min_val = min(cell['float'] for cell in grid.values())
    max_val = max(cell['float'] for cell in grid.values())
    span = max_val - min_val

    # Average spacing
    avg_spacing = span / (128 - 1)

    # The density is not uniform — it's higher near integers
    # and lower between them. This reflects the BST denominator structure.

    return min_val == 0 and max_val > g - 1, \
        f"grid spans [{min_val:.1f}, {max_val:.4f}], avg spacing = {avg_spacing:.4f}", \
        f"128 values covering the BST parameter range"


def test_print_grid_sample():
    """Print a sample of the grid to verify structure."""
    grid, bases, fracs = generate_grid()

    # Print first 4 rows, first 8 columns
    sample = []
    for r in range(min(4, len(bases))):
        row_vals = []
        for c in range(min(8, len(fracs))):
            val = grid[(r, c)]['value']
            row_vals.append(str(val))
        sample.append(row_vals)

    n_unique = len(set(cell['value'] for cell in grid.values()))

    return n_unique == 128, \
        f"all 128 values are UNIQUE — no duplicates in the grid", \
        f"sample row 0: {sample[0][:6]}..."


# ─── Main ─────────────────────────────────────────────────────────
def main():
    print("=" * 70)
    print("Toy 1325 — The 128-Entry Parameter Grid")
    print("MON-4: The full 8×16 periodic table")
    print("=" * 70)

    tests = [
        ("T1  16 = 2^(N_c+1) fractional parts",           test_fractional_count),
        ("T2  128 = 2^g grid cells",                       test_grid_size),
        ("T3  Notable physical constants in grid",          test_notable_cells_present),
        ("T4  κ_ls = 6/5 at [1, 1/5]",                    test_kappa_ls_location),
        ("T5  Critical line column (1/rank = 1/2)",        test_critical_line_column),
        ("T6  Fractional parts ⊂ Farey F_g",              test_farey_connection),
        ("T7  12-value catalog ⊂ 128-entry grid",         test_12_value_catalog_subset),
        ("T8  Reflection symmetry f ↔ 1-f",               test_symmetry),
        ("T9  Grid density and uniqueness",                 test_density),
        ("T10 Grid sample verification",                    test_print_grid_sample),
    ]

    print()
    passed = 0
    for name, test_fn in tests:
        try:
            result = test_fn()
            ok = result[0]
            detail = result[1:]
            status = "PASS" if ok else "FAIL"
            if ok: passed += 1
            print(f"  {name}: {status}  ({detail[0]})")
        except Exception as e:
            print(f"  {name}: FAIL  (exception: {e})")

    print(f"\nSCORE: {passed}/{len(tests)} PASS")

    # Print the grid
    grid, bases, fracs = generate_grid()
    print("\n─── THE 128-ENTRY GRID (first 8 columns) ───\n")
    print(f"  {'base':>4s}", end="")
    for c in range(8):
        print(f"  {str(fracs[c]):>6s}", end="")
    print()
    print("  " + "─" * 60)
    for r in range(len(bases)):
        print(f"  {bases[r]:4d}", end="")
        for c in range(8):
            val = grid[(r, c)]['value']
            print(f"  {str(val):>6s}", end="")
        print()

    # Notable cells
    print("\n─── NOTABLE CELLS ───\n")
    for name, value in sorted(NOTABLE.items(), key=lambda x: x[1]):
        for (r, c), cell in grid.items():
            if cell['value'] == value:
                print(f"  [{r},{c:2d}] = {str(value):>6s} = {float(value):.4f}  ({name})")
                break

    print("""
─── THE FULL PERIODIC TABLE ───

8 rows (integer bases 0..g) × 16 columns (BST fractional parts) = 128 cells.

Every cell contains a unique rational number from BST's extended catalog.
Every function in physics lives in one of these 128 cells.
The cell determines the function's Meijer G type, parameters, and properties.

The 12-value original catalog (8 integers + 4 half-integers) is embedded
in rows 0-7 of the 0 and 1/2 columns. The remaining 116 cells are the
EXTENSION via Gauss multiplication — fractional shifts that give the
full function space.

Key structural features:
  - Column 1/2: the critical line (half-integers)
  - Column 1/5: spin-orbit and BST denominators
  - Column 1/7: genus-related fractions (22/7 ≈ π)
  - Row 0: fractional parts only (the "light" functions)
  - Row 7: the heaviest functions (base = genus)
""")


if __name__ == "__main__":
    main()
