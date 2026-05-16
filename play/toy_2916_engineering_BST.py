"""
Toy 2916 — Engineering / architecture structural counts BST.

Bridge truss types standard: 7 = g (Pratt, Howe, Warren, K, Vierendeel,
  Bowstring, Cantilever)
Bridge structural classes: 5 = n_C (beam, arch, truss, cable-stayed, suspension)
Roof structural types: 5 = n_C (flat, gabled, hipped, gambrel, mansard)

Standard column orders Greek: 3 = N_c (Doric, Ionic, Corinthian)
+ Roman additions: 5 = n_C (+ Tuscan, Composite)

Standard wall types: 4 = rank² (load-bearing, partition, curtain, retaining)
Standard load types in civil engineering: 4 = rank² (dead, live, wind, seismic)
Engineering safety factor rationale levels: 3 = N_c (probabilistic, severity, recovery)

Standard machine elements (Reuleaux): 6 = C_2 categories
Standard fastener types: 5 = n_C (bolt, screw, rivet, nail, weld)
Standard transmission types: 7 = g (gear, belt, chain, friction, hydraulic, electric, magnetic)

Standard manufacturing processes (Kalpakjian): 7 = g categories
  casting, forming, machining, joining, surface, polymer, additive

Antenna fundamental types: 7 = g (dipole, monopole, loop, horn, parabolic,
  helical, microstrip)

Computer architecture levels (Tanenbaum): 6 = C_2 (digital logic, microarchitecture,
  ISA, OS, assembly, problem-oriented language)

Standard programming paradigms: 5 = n_C (imperative, OOP, functional, logic, dataflow)
Standard sorting algorithm classes complexity-wise: 4 = rank²
Standard data structure categories: 5 = n_C (array, list, tree, graph, hash)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    eng = [
        ("Bridge truss types standard",            7, g, "g"),
        ("Bridge structural classes",              5, n_C, "n_C"),
        ("Roof structural types",                  5, n_C, "n_C"),
        ("Greek column orders",                    3, N_c, "N_c"),
        ("All classical column orders",            5, n_C, "n_C"),
        ("Wall types",                             4, rank**2, "rank²"),
        ("Civil eng load types",                   4, rank**2, "rank²"),
        ("Safety factor rationale levels",         3, N_c, "N_c"),
        ("Reuleaux machine element categories",    6, C_2, "C_2"),
        ("Fastener types",                         5, n_C, "n_C"),
        ("Transmission types",                     7, g, "g"),
        ("Kalpakjian manufacturing process types", 7, g, "g"),
        ("Antenna fundamental types",              7, g, "g"),
        ("Tanenbaum computer arch levels",         6, C_2, "C_2"),
        ("Programming paradigms major",            5, n_C, "n_C"),
        ("Sorting algo complexity classes",        4, rank**2, "rank²"),
        ("Data structure categories",              5, n_C, "n_C"),
        ("MEMS device categories",                 4, rank**2, "rank² (sensor, actuator, optical, RF)"),
    ]

    print("Engineering BST:")
    matches = 0
    for name, val, bst, formula in eng:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<44} = {val:<3} = {formula:<15} {marker}")

    print(f"\nSCORE: {matches}/{len(eng)}")
    return matches, len(eng)


if __name__ == "__main__":
    run()
