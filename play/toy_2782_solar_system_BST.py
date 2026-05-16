"""
Toy 2782 — Solar system structural integers BST.

8 planets = rank³ ✓
4 inner rocky = rank² ✓
4 outer gas/ice giants = rank² ✓
Gas giants: 4 (Jupiter, Saturn, Uranus, Neptune) = rank²
Asteroid belt: located between rocky and gas at ~5/2 AU = n_C/rank
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    solar = [
        ("Total planets (recognized)", 8,    rank**3,    "rank³"),
        ("Inner rocky planets",        4,    rank**2,    "rank²"),
        ("Outer giant planets",        4,    rank**2,    "rank²"),
        ("Earth's moons",              1,    1,          "trivial"),
        ("Mars's moons",               2,    rank,       "rank"),
        ("Jupiter Galilean moons",     4,    rank**2,    "rank²"),
        ("Saturn major moons",         8,    rank**3,    "rank³"),  # approximately
    ]

    print("Solar system structural BST:")
    matches = 0
    for name, val, bst, formula in solar:
        ok = val == bst
        marker = "✓" if ok else "×"
        if ok:
            matches += 1
        print(f"  {name:<30} = {val:<4} = {formula:<10} {marker}")

    print(f"\nSCORE (rough structural): {matches}/{len(solar)}")
    print(f"Note: solar system counts are observational, not strict BST claim.")
    return matches, len(solar)


if __name__ == "__main__":
    run()
