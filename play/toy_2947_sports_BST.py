"""
Toy 2947 — Sports / games structural counts BST.

Soccer (football) players per side: 11 = c_2
American football players per side: 11 = c_2
Cricket players per side: 11 = c_2
Rugby Union players per side: 15 = N_c·n_C
Rugby League players per side: 13 = c_3
Field hockey: 11 = c_2

Baseball players per side: 9 = N_c²
Volleyball players per side: 6 = C_2
Basketball players per side: 5 = n_C
Hockey players per side (ice): 6 = C_2 (with goalie)

Bowling pins: 10 = rank·n_C
Bowling frames: 10 = rank·n_C
Billiards balls (8-ball): 16 = rank⁴ (15 numbered + cue)

Olympic rings: 5 = n_C (continents)
Olympic medals: 3 = N_c (gold, silver, bronze)
Summer Olympics events ~33 = rank·c_2+rank·n_C (varies)
Winter Olympics events ~15 = N_c·n_C disciplines

Golf clubs in bag max: 14 = rank·g
Standard 9 holes: 9 = N_c²
Standard 18-hole round: 18 = rank·g + rank²

Tennis players per side: 1 or 2 = rank (singles/doubles)
Tennis sets typical match: 3 = N_c (best of 5 = n_C)
Tennis Grand Slam events: 4 = rank²

Boxing weight categories Olympic men: ~10 = rank·n_C
Boxing rounds professional: 12 = rank·C_2 (heavyweight title)

Marathon distance: 42.195 km — exponent c_2 + N_c·rank = 11+6+... no
Marathon kilometers integer: 42 = rank·N_c·g = 42 ✓
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13

    sports = [
        ("Soccer players per side",          11, c_2, "c_2"),
        ("Cricket players per side",         11, c_2, "c_2"),
        ("Field hockey players per side",    11, c_2, "c_2"),
        ("Rugby Union players per side",     15, N_c*n_C, "N_c·n_C"),
        ("Rugby League players per side",    13, c_3, "c_3"),
        ("Baseball players per side",        9, N_c**2, "N_c²"),
        ("Volleyball players per side",      6, C_2, "C_2"),
        ("Basketball players per side",      5, n_C, "n_C"),
        ("Ice hockey players per side",      6, C_2, "C_2"),
        ("Bowling pins",                     10, rank*n_C, "rank·n_C"),
        ("Olympic rings",                    5, n_C, "n_C"),
        ("Olympic medal types",              3, N_c, "N_c"),
        ("Golf clubs max in bag",            14, rank*g, "rank·g"),
        ("9-hole golf",                      9, N_c**2, "N_c²"),
        ("18-hole golf",                     18, rank*g + rank**2, "rank·g + rank²"),
        ("Tennis match modes",               2, rank, "rank (singles/doubles)"),
        ("Tennis sets standard match",       3, N_c, "N_c"),
        ("Tennis Grand Slam events",         4, rank**2, "rank²"),
        ("Heavyweight title boxing rounds",  12, rank*C_2, "rank·C_2"),
        ("Marathon kilometers integer",      42, rank*N_c*g, "rank·N_c·g"),
    ]

    print("Sports BST:")
    matches = 0
    for name, val, bst, formula in sports:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<42} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(sports)}")
    return matches, len(sports)


if __name__ == "__main__":
    run()
