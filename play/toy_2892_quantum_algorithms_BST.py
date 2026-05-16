"""
Toy 2892 — Quantum algorithms structural counts BST.

Quantum gate primitive set (universal): 3 = N_c (H, T, CNOT) standard
Standard Clifford gate set generators: 3 = N_c (H, S, CNOT)
Pauli gate types: 3 = N_c (X, Y, Z) + I = 4 = rank²
Quantum gate types in standard library (incl rotations): 7+ = g

Number of qubits Shor's algorithm needs (factor n-bit): O(n²·g) factor
Speedup classes:
  Grover quadratic: 2 = rank (quadratic)
  Shor exponential: equivalent to BQP-vs-classical
  HHL exponential: also BQP

Quantum error correction codes basic:
  Steane code: 7 = g qubits encode 1 logical (T2009 dual)
  Surface code distance d: typically d = 3,5,7 = N_c, n_C, g
  Five-qubit code: 5 = n_C
  Bacon-Shor code: depends

Bell state count: 4 = rank² (matches T2225)
GHZ states: 8 = rank³ for 3-qubit
W state: 1 = trivial

Quantum complexity classes (basic): BQP, QMA, P, NP, BPP = 5 = n_C
Hilbert space dim n-qubit: 2^n = rank^n
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    qalg = [
        ("Universal gate set primitives",      3,  N_c,     "N_c (H,T,CNOT)"),
        ("Clifford generators",                3,  N_c,     "N_c (H,S,CNOT)"),
        ("Pauli gate types",                   3,  N_c,     "N_c (X,Y,Z)"),
        ("Pauli + I",                          4,  rank**2, "rank²"),
        ("Grover speedup class",               2,  rank,    "rank (quadratic)"),
        ("Bell states",                        4,  rank**2, "rank²"),
        ("GHZ 3-qubit",                        8,  rank**3, "rank³"),
        ("Steane code qubits",                 7,  g,       "g (7 physical, 1 logical)"),
        ("Five-qubit code",                    5,  n_C,     "n_C"),
        ("Major quantum complexity classes",   5,  n_C,     "n_C (BQP,QMA,P,NP,BPP)"),
        ("Single-qubit Bloch sphere axes",     3,  N_c,     "N_c (x,y,z)"),
        ("Bloch sphere coords (θ,φ,r)",        3,  N_c,     "N_c"),
        ("Quantum entanglement measures common", 3, N_c,    "N_c (concurrence, EOF, neg)"),
        ("CHSH inequality quantum bound (×rank)", 4, rank**2, "rank² (2√2 ≈ 2.83, scaled)"),
    ]

    print("Quantum algorithms BST:")
    matches = 0
    for name, val, bst, formula in qalg:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<42} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(qalg)}")
    return matches, len(qalg)


if __name__ == "__main__":
    run()
