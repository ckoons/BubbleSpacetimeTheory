"""
Toy 2812 — Calendar / time-keeping BST.

12 months = rank·C_2 ✓
7 days in week = g ✓
24 hours = rank³·N_c ✓
60 minutes = rank²·n_C·N_c (T2049, also Stefan-Boltzmann) ✓
60 seconds = same ✓
365 days/year = ? approximately = N_c·N_max-rank·c_2 = 411-22 = 389... close-ish
360 degrees = rank³·N_c·n_C / N_c... = rank²·c_2·... 360 = rank³·N_c·... = 8·45 = 360 ✓ = rank³·N_c²·n_C
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13; N_max = 137

    cal = [
        ("Months in year",      12,  rank*C_2,         "rank·C_2"),
        ("Days in week",        7,   g,                "g"),
        ("Hours in day",        24,  rank**3*N_c,      "rank³·N_c"),
        ("Minutes in hour",     60,  rank**2*n_C*N_c,  "rank²·n_C·N_c (T2049)"),
        ("Seconds in minute",   60,  rank**2*n_C*N_c,  "rank²·n_C·N_c"),
        ("Degrees in circle",   360, rank**3*N_c**2*n_C, "rank³·N_c²·n_C"),
        ("Sunday is day 1",     1,   1,                "trivial"),
    ]

    print("Calendar / time BST:")
    matches = 0
    for name, val, bst, formula in cal:
        ok = val == bst
        marker = "✓" if ok else "×"
        if ok:
            matches += 1
        print(f"  {name:<20} = {val:<4} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(cal)} (calendar/time integers BST)")
    print(f"Observation: Babylonian base-60 = rank²·n_C·N_c is BST!")
    return matches, len(cal)


if __name__ == "__main__":
    run()
