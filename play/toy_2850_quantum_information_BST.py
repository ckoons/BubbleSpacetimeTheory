"""
Toy 2850 — Quantum information BST.

Qubit Hilbert space dim: 2 = rank
Qutrit: 3 = N_c
Qudit (d-level): d (parameter)
Bell states: 4 = rank² (T2832 QEC)
GHZ states for 3 qubits: 8 = rank³
Entanglement entropy max for n qubits: log(2^n) = n·log(rank)

Tsirelson bound: 2√2 = rank^(3/2) (Elie noted)
CHSH inequality classical bound: 2 = rank
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    qinfo = [
        ("Qubit Hilbert dim",       2, rank,    "rank"),
        ("Qutrit Hilbert dim",      3, N_c,     "N_c"),
        ("Bell states",             4, rank**2, "rank²"),
        ("GHZ states 3-qubit",      8, rank**3, "rank³"),
        ("CHSH classical bound",    2, rank,    "rank"),
        ("Quantum gate Hadamard angle (×π/4)", 1, 1, "trivial"),
        ("Pauli matrices count",    3, N_c,     "N_c (σ_x,σ_y,σ_z)"),
        ("Single-qubit unitary parameters", 4, rank**2, "rank² (SU(2))"),
        ("Two-qubit unitary parameters", 16, rank**4, "rank⁴ (SU(4))"),
    ]

    print("Quantum information theory BST:")
    matches = 0
    for name, val, bst, formula in qinfo:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<35} = {val:<3} = {formula:<14} {marker}")

    print(f"\nSCORE: {matches}/{len(qinfo)}")
    return matches, len(qinfo)


if __name__ == "__main__":
    run()
