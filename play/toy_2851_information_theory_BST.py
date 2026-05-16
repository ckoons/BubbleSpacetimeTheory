"""
Toy 2851 — Information theory BST.

Shannon entropy of fair coin: 1 bit = log_rank(rank)
Channel capacity binary symmetric channel: C = 1 - H(p)
Bit (basic unit): rank = 2
Byte (storage): 8 = rank³
Word in CPU: 32 = rank⁵ or 64 = rank^6
Network OSI layers: 7 = g ✓

Huffman coding minimum bits: ceiling(log_2(n)) — rank-based.
Reed-Solomon block sizes: typically powers of rank.
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    info = [
        ("Bit (binary digit)",   2,  rank,    "rank"),
        ("Byte",                 8,  rank**3, "rank³"),
        ("Nibble (half byte)",   4,  rank**2, "rank²"),
        ("Word (32-bit)",        32, rank**5, "rank⁵"),
        ("Word (64-bit)",        64, rank**6, "rank^6"),
        ("OSI network layers",   7,  g,       "g"),
        ("TCP/IP layers",        4,  rank**2, "rank²"),
        ("DNS hierarchy levels", 7,  g,       "g (root + 6 TLD-like)"),
    ]

    print("Information theory + networking BST:")
    matches = 0
    for name, val, bst, formula in info:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<28} = {val:<3} = {formula:<10} {marker}")

    print(f"\nSCORE: {matches}/{len(info)}")
    return matches, len(info)


if __name__ == "__main__":
    run()
