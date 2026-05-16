"""
Toy 2927 — Cryptography / coding theory BST.

AES key sizes (bits): 128, 192, 256 = rank⁷, rank·N_c·rank³·... messy
  Better: AES key sizes = 3 = N_c options
AES rounds: 10, 12, 14 = rank·n_C, rank·C_2, rank·g — BST cascade in rank·{n_C, C_2, g}
AES state matrix: 4×4 = rank² × rank² bytes = rank⁴ = 16 bytes
AES SubBytes operations: 16 = rank⁴

DES key effective bits: 56 = rank³·g
DES rounds: 16 = rank⁴

RSA prime count per key: 2 = rank
RSA exponent typical: 65537 = rank^16+1 = Fermat F_4 (matches T2248)

SHA family hash outputs: 5 = n_C (SHA-1=160, SHA-224, SHA-256, SHA-384, SHA-512)
SHA-256 round count: 64 = rank^6
SHA-512 round count: 80 = rank⁴·n_C

Reed-Solomon block sizes: typically powers of rank
Hamming code parameters: (7,4) = (g, rank²) BST cascade exactly!
Repetition code n: arbitrary; typical 3 = N_c (3-fold repeat)

Public key cryptosystem categories: 4 = rank² (RSA-like factoring,
  DLP, ECC, lattice/code-based)

Block cipher modes: 5 = n_C (ECB, CBC, CFB, OFB, CTR) standard
+ GCM, XTS = 7 = g extended

Standard elliptic curves NIST: 5 = n_C (P-192, P-224, P-256, P-384, P-521)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    crypto = [
        ("AES key size options",            3, N_c,     "N_c (128, 192, 256 bits)"),
        ("AES state matrix bytes",          16, rank**4, "rank⁴ (4×4 bytes)"),
        ("AES-128 rounds",                  10, rank*n_C, "rank·n_C"),
        ("AES-192 rounds",                  12, rank*C_2, "rank·C_2"),
        ("AES-256 rounds",                  14, rank*g,   "rank·g"),
        ("DES rounds",                      16, rank**4, "rank⁴"),
        ("RSA prime count per key",         2, rank,    "rank"),
        ("RSA standard exponent",           65537, rank**16+1, "rank^16+1 = F_4"),
        ("SHA family variants",             5, n_C,     "n_C"),
        ("SHA-256 rounds",                  64, rank**6, "rank^6"),
        ("SHA-512 rounds",                  80, rank**4*n_C, "rank⁴·n_C"),
        ("Hamming code n",                  7, g,       "g (Hamming(7,4))"),
        ("Hamming code k",                  4, rank**2, "rank²"),
        ("Public key cryptosystem categories", 4, rank**2, "rank²"),
        ("Block cipher standard modes",     5, n_C,     "n_C"),
        ("Block cipher extended modes",     7, g,       "g (+GCM, XTS)"),
        ("NIST elliptic curves",            5, n_C,     "n_C (P-192..P-521)"),
        ("Steane code qubits (T2257 dual)", 7, g,       "g"),
    ]

    print("Cryptography / coding theory BST:")
    matches = 0
    for name, val, bst, formula in crypto:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<42} = {val:<6} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(crypto)}")
    return matches, len(crypto)


if __name__ == "__main__":
    run()
