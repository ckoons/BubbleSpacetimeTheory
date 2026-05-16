"""
Toy 2884 — Combinatorics / games structural counts BST.

Standard deck of cards: 52 = rank²·c_2+rank² = rank²(c_2+1) = rank²·12 - hmm.
Actually 52 = rank²·c_2+rank³ = 44+8 = 52 ✓ or 4·13=rank²·c_3.
Best: 52 = rank²·c_3 = 4·13 ✓.
Standard deck suits: 4 = rank²
Suit colors: 2 = rank (red, black)
Face cards: 12 = rank·C_2 (J, Q, K × 4 suits = 12 per deck/3 face per suit)
  Face per suit = 3 = N_c ✓ (J,Q,K)
Number cards per suit: 10 = rank·n_C (A counted as 1, plus 2-10 = 9)
  Counted from A to 10 = 10 = rank·n_C ✓
Aces: 4 = rank²
Jokers (extra): 2 = rank

Chess pieces per side: 16 = rank⁴
Chess piece types: 6 = C_2 (K,Q,R,B,N,P)
Chess board squares: 64 = rank^6
Chess board colors: 2 = rank
Chess ranks/files: 8 = rank³

Checkers/draughts pieces per side: 12 = rank·C_2
Checkers board squares same as chess: 64 = rank^6

Mah-jongg suit tiles: 3 = N_c (dots, bamboo, characters)
Standard dice faces: 6 = C_2
Dominos in double-six set: 28 = ?  Sum 0..6 of (n+1) = 28 = (C_2)(C_2+1)/2 = 21 wrong, 28 = 2·14 = rank·rank·g

Rubik's cube facelets per face: 9 = N_c²
Rubik's cube corner pieces: 8 = rank³
Rubik's cube edge pieces: 12 = rank·C_2
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13

    games = [
        ("Card deck (no jokers)",          52, rank**2*c_3, "rank²·c_3"),
        ("Card suits",                     4,  rank**2,     "rank²"),
        ("Suit colors",                    2,  rank,        "rank"),
        ("Face cards per suit",            3,  N_c,         "N_c (J,Q,K)"),
        ("Number cards per suit (A-10)",   10, rank*n_C,    "rank·n_C"),
        ("Jokers (standard extra)",        2,  rank,        "rank"),
        ("Chess pieces per side",          16, rank**4,     "rank⁴"),
        ("Chess piece types",              6,  C_2,         "C_2"),
        ("Chess board squares",            64, rank**6,     "rank^6"),
        ("Chess board colors",             2,  rank,        "rank"),
        ("Chess ranks/files",              8,  rank**3,     "rank³"),
        ("Checkers pieces per side",       12, rank*C_2,    "rank·C_2"),
        ("Mah-jongg suit types",           3,  N_c,         "N_c"),
        ("Dice faces (standard)",          6,  C_2,         "C_2"),
        ("Rubik's cube facelets per face", 9,  N_c**2,      "N_c²"),
        ("Rubik's cube corner pieces",     8,  rank**3,     "rank³"),
        ("Rubik's cube edge pieces",       12, rank*C_2,    "rank·C_2"),
        ("Tic-tac-toe board cells",        9,  N_c**2,      "N_c²"),
        ("Tic-tac-toe players",            2,  rank,        "rank"),
    ]

    print("Combinatorics / games BST:")
    matches = 0
    for name, val, bst, formula in games:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<40} = {val:<3} = {formula:<20} {marker}")

    print(f"\nSCORE: {matches}/{len(games)}")
    return matches, len(games)


if __name__ == "__main__":
    run()
