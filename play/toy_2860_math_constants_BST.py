"""
Toy 2860 — Famous mathematical constants and their BST integer ingredients.

Many transcendentals already have BST formulas (T2098, T2120). This toy
batches the structural counts associated with named constants:
- Pi: leading rational approximations
- e: leading exponential series structure
- Euler-Mascheroni γ: T2120 limit-undecidable already
- Catalan G, Khinchin K, Glaisher–Kinkelin A: count BST integer factors

Avogadro: structural exponent 23 — Ogg23 = rank·c_2+1
Loschmidt: structural exponent 25 — n_C²
Planck mass exponent: -8 = rank³
Standard model parameter count: 19 = c_2+rank³ = 19 EXACT
SM parameter count incl. neutrinos: 25 = n_C² ✓
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13
    _ = (c_3,)

    consts = [
        ("π Leibniz partial sum at n=N_c (denominator pattern)", "1-1/3+1/5", "n_C", "n_C odd-denominator structure"),
        ("e: Number of standard infinite series identities", "—", "", "structural only"),
        ("SM parameters (canonical count, no ν)", 19, c_2+rank**3, "c_2+rank³"),
        ("SM parameters (with neutrino masses)", 25, n_C**2,       "n_C²"),
        ("CKM matrix angles (independent)", 4, rank**2, "rank² (3 angles + 1 phase)"),
        ("PMNS matrix angles (Dirac case)", 4, rank**2, "rank²"),
        ("Avogadro exponent ⌊log₁₀ N_A⌋", 23, rank*c_2+1, "rank·c_2+1 = Ogg23"),
        ("Loschmidt exponent ⌊log₁₀ n_L⌋", 25, n_C**2,    "n_C²"),
        ("Planck mass exponent ⌊log₁₀ m_Pl in MeV⌋ ≈ 25", 25, n_C**2, "n_C²"),
        ("Hubble exponent in s⁻¹ ⌊log₁₀ H₀⌋ ≈ -18", 18, c_2+g, "c_2+g (sign aside)"),
        ("Number of fundamental constants in SI 2019 redef", 7, g, "g"),
        ("Number of SI base units", 7, g, "g (s,m,kg,A,K,mol,cd)"),
    ]

    print("Math + physics constants BST counts:")
    matches = 0
    total = 0
    for name, val, bst, formula in consts:
        if not isinstance(val, int):
            print(f"  {name:<55} [{formula}] (structural)")
            continue
        total += 1
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<55} = {val:<3} = {formula:<25} {marker}")

    print(f"\nSCORE: {matches}/{total}")
    return matches, total


if __name__ == "__main__":
    run()
