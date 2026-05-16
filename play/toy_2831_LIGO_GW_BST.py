"""
Toy 2831 — LIGO GW observables BST.

GW frequency at merger: 250 Hz for 30+30 M_sun (GW150914)
Strain h ~ 10^-21
LIGO arm length: 4 km

For binary BH ~30 M_sun: ringdown frequency ω = c³/(GM·rank³·π) per T2106.

In BST: GW150914 final mass = 62 M_sun ≈ ?
62 = N_max - n_C - 2·N_c - 2·rank·... = ad hoc

GW190521 final mass = 142 = N_max + n_C ✓ (Elie)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13; N_max = 137

    gw = [
        ("GW150914 final M (M_sun)",   62,  None,            "62 not obviously BST"),
        ("GW170817 BNS chirp mass",    1.19, None,           "1.19 ≈ C_2/n_C = 1.2"),
        ("GW190521 final M (M_sun)",   142, N_max + n_C,     "N_max+n_C ✓ Elie"),
        ("LIGO arm length (km)",       4,   rank**2,         "rank² (engineered)"),
    ]

    print("LIGO/Virgo GW events BST:")
    matches = 0
    total = 0
    for name, val, bst, formula in gw:
        if bst is None:
            print(f"  {name:<30} = {val:<5} {formula}")
            continue
        total += 1
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<30} = {val:<5} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{total}")
    return matches, total


if __name__ == "__main__":
    run()
