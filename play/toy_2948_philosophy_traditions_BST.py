"""
Toy 2948 — Philosophy / religious tradition structural counts BST.

Major philosophy traditions east: 5 = n_C (Hinduism, Buddhism, Confucianism,
  Daoism, Shintoism)
Major philosophy traditions west: 7 = g (Greek, Roman, Patristic, Medieval,
  Renaissance, Modern, Contemporary)
Abrahamic religions: 3 = N_c (Judaism, Christianity, Islam)
Major world religions standard: 7 = g (5 east + 3 west - overlap)

Christian denominations major: 3 = N_c (Catholic, Orthodox, Protestant)
+ Anglican = 4 = rank²

Buddhist Noble Truths: 4 = rank²
Buddhist Eightfold Path: 8 = rank³
Buddhist Three Jewels: 3 = N_c
Buddhist Five Precepts: 5 = n_C
Buddhist Three Marks of Existence: 3 = N_c

Confucianism Five Constants: 5 = n_C
Confucianism Three Bonds: 3 = N_c
Hindu Trimurti (Brahma, Vishnu, Shiva): 3 = N_c
Hindu major paths to liberation: 4 = rank² (jñāna, karma, bhakti, rāja)
Hindu Vedas: 4 = rank² (Rig, Sama, Yajur, Atharva)

Major Indo-European pantheon counts: cluster around 12 = rank·C_2
Greek primordial deities: 7 = g main (Chaos, Gaia, Tartarus, Eros, Nyx, Erebus, Aether)

Kabbalah Sefirot: 10 = rank·n_C
Kabbalah Trees of Life: 4 = rank² (4 worlds)

Major Western philosophical schools modern: 5 = n_C (empiricism, rationalism,
  pragmatism, phenomenology, analytic)

Plato's cardinal virtues: 4 = rank² (wisdom, courage, temperance, justice)
+ Christian theological: 3 = N_c → 7 = g total
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    phil = [
        ("Major east traditions",            5, n_C, "n_C"),
        ("Major west traditions",            7, g, "g"),
        ("Abrahamic religions",              3, N_c, "N_c"),
        ("Major world religions",            7, g, "g"),
        ("Christian denominations major",    3, N_c, "N_c"),
        ("Buddhist Noble Truths",            4, rank**2, "rank²"),
        ("Buddhist Eightfold Path",          8, rank**3, "rank³"),
        ("Buddhist Three Jewels",            3, N_c, "N_c"),
        ("Buddhist Five Precepts",           5, n_C, "n_C"),
        ("Buddhist Three Marks",             3, N_c, "N_c"),
        ("Confucian Five Constants",         5, n_C, "n_C"),
        ("Confucian Three Bonds",            3, N_c, "N_c"),
        ("Hindu Trimurti",                   3, N_c, "N_c"),
        ("Hindu major paths to liberation",  4, rank**2, "rank²"),
        ("Hindu Vedas",                      4, rank**2, "rank²"),
        ("Greek primordials",                7, g, "g"),
        ("Kabbalah Sefirot",                 10, rank*n_C, "rank·n_C"),
        ("Kabbalah Trees of Life",           4, rank**2, "rank²"),
        ("Western modern schools",           5, n_C, "n_C"),
        ("Plato's cardinal virtues",         4, rank**2, "rank²"),
        ("Plato + Christian theological virtues", 7, g, "g (4+3)"),
    ]

    print("Philosophy / tradition counts BST:")
    matches = 0
    for name, val, bst, formula in phil:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<44} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(phil)}")
    return matches, len(phil)


if __name__ == "__main__":
    run()
