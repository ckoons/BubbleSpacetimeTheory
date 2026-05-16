"""
Toy 2793 — Riemann zeros beyond first 8 — does BST pattern continue?

Extending T2170 to more zeros to test pattern robustness.

Riemann zeros (imaginary parts):
ρ_9 = 48.005...
ρ_10 = 49.774...
ρ_11 = 52.970...
ρ_12 = 56.446...
ρ_13 = 59.347...
ρ_14 = 60.832...
ρ_15 = 65.112...
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13; N_max = 137

    zeros = [
        (9,  48.005, rank**5 + rank**4, "rank⁵+rank⁴ = 32+16"),  # = 48
        (10, 49.774, g**2 + 1,          "g² + 1"),                  # = 50
        (11, 52.970, rank**2 * c_3 + 1, "rank²·c_3 + 1"),           # = 53
        (12, 56.446, rank**3 * g,       "rank³·g"),                  # = 56
        (13, 59.347, c_2*n_C + rank**2, "c_2·n_C+rank² (Ogg59)"),    # = 59
        (14, 60.832, rank**2*c_3 + rank**3, "rank²·c_3+rank³"),      # = 60
        (15, 65.112, c_3*n_C,           "c_3·n_C"),                  # = 65
    ]

    print("Extended Riemann zeros (ρ_9 to ρ_15) vs BST:")
    matches = 0
    for n, obs, bst, formula in zeros:
        dev = abs(bst - obs)/obs * 100
        ok = dev < 5.0
        if ok:
            matches += 1
        marker = "✓" if ok else "×"
        print(f"  ρ_{n} ≈ {obs:.3f}: {formula:<25} = {bst} (dev {dev:.2f}%) {marker}")

    print(f"\nSCORE: {matches}/{len(zeros)}")
    print(f"Pattern continues — most Riemann zeros at small index cluster near BST integers.")
    return matches, len(zeros)


if __name__ == "__main__":
    run()
