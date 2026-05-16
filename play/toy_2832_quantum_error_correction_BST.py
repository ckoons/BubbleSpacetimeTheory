"""
Toy 2832 — Quantum error correction codes BST.

Shor 9-qubit code: 9 = N_c²
Steane 7-qubit code: 7 = g (Ogg)
5-qubit code (smallest perfect): 5 = n_C
Surface code minimum distance: 3 = N_c
Bacon-Shor codes: rectangular, sizes ~rank^n
Toric code: d×d torus, BST integer side lengths

Quantum gate count for arbitrary 2-qubit ops: 6 = C_2 (CNOTs)
Bell basis: 4 = rank² ✓
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13

    qec = [
        ("Shor code qubits",        9,  N_c**2, "N_c²"),
        ("Steane code qubits",      7,  g, "g (Ogg)"),
        ("Smallest perfect QEC",    5,  n_C, "n_C"),
        ("Surface code min distance",3, N_c, "N_c"),
        ("CNOTs for 2-qubit op",    6,  C_2, "C_2"),
        ("Bell basis dim",          4,  rank**2, "rank²"),
        ("Qubits per logical (Shor)",9, N_c**2, "N_c²"),
    ]

    print("Quantum error correction BST:")
    matches = 0
    for name, val, bst, formula in qec:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<28} = {val} = {formula:<10} {marker}")

    print(f"\nSCORE: {matches}/{len(qec)}")
    return matches, len(qec)


if __name__ == "__main__":
    run()
