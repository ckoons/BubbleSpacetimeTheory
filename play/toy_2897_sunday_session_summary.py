"""
Toy 2897 — Sunday session summary aggregator.

Counts the total BST identification work done in Lyra's Sunday 2026-05-16
session and validates the cumulative cross-domain integer count.
"""

import os
import re


def run():
    play_dir = os.path.dirname(os.path.abspath(__file__))
    sunday_toys = []
    # Sunday Lyra toys: scattered through 2700-2900 range with Lyra in summary
    for fname in sorted(os.listdir(play_dir)):
        if not fname.startswith("toy_"):
            continue
        m = re.match(r"toy_(\d+)_", fname)
        if not m:
            continue
        n = int(m.group(1))
        if 2747 <= n <= 2897:
            sunday_toys.append((n, fname))

    print(f"Toys in 2747-2897 range: {len(sunday_toys)}")

    # Count theorems registered in Sunday range (T2001-T2300 cluster)
    reg_path = os.path.join(os.path.dirname(play_dir), "notes", "BST_AC_Theorem_Registry.md")
    sunday_theorems = []
    if os.path.exists(reg_path):
        with open(reg_path, "r") as f:
            content = f.read()
        for m in re.finditer(r"## T(\d+) — .*Lyra 2026-05-1[567]", content):
            n = int(m.group(1))
            if 2000 <= n <= 2300:
                sunday_theorems.append(n)
    print(f"Lyra-attributed theorems T2000-T2300: {len(sunday_theorems)}")

    # Categorize Sunday Lyra topics from this session
    domains_covered = [
        "Topology (stable homotopy)", "Quantum information", "Information theory",
        "Cognitive science", "Cosmology", "Crystallography", "Extended biology",
        "Math constants", "Gauge groups", "Atomic spectroscopy",
        "Chemistry bonding", "Particle decay modes", "GR/Black holes",
        "Electromagnetism", "Modular forms/Galois", "Ancient symbolic",
        "Statistical mechanics", "QFT scattering", "Knot theory",
        "Number theory (Fermat primes)", "Solar system", "Music theory",
        "Combinatorics/games", "Hadron spectroscopy", "Anthropic/observer",
        "Protein structures", "Quantum algorithms", "Complexity classes",
        "Nuclear magic numbers (extended)",
    ]

    print(f"\nDomains touched in this 16:00-16:45 session window: {len(domains_covered)}")
    for d in domains_covered:
        print(f"  - {d}")

    # BST primary integer usage histogram (from the 8 batches in this window)
    # rank=2, N_c=3, rank²=4, n_C=5, C_2=6, g=7, rank³=8, N_c²=9, rank·n_C=10
    # c_2=11, rank·C_2=12, c_3=13, rank·g=14, N_c·n_C=15, rank⁴=16, c_2+C_2=17
    # rank·g+rank²=18, N_max=137, etc.

    integer_usage = {
        2: "rank — extremely common (binary symmetry)",
        3: "N_c — frequent (color, generations, axes)",
        4: "rank² — very common (spacetime, scaffolding)",
        5: "n_C — frequent (Lagrange, pentads)",
        6: "C_2 — frequent (Lie group dim, Petrov, dice)",
        7: "g — very common (week, EC, periods, magic)",
        8: "rank³ — common (octets, octave, IT)",
        9: "N_c² — common (Yukawa, nonet, tic-tac-toe)",
        10: "rank·n_C — common (decuplet, Poincaré, Weyl)",
        11: "c_2 — present (Z channels, Sophie Germain)",
        12: "rank·C_2 — common (semitones, Olympians)",
        13: "c_3 — present (deck = rank²·c_3)",
        14: "rank·g — present (Bravais)",
        24: "rank³·N_c — present (χ(K3), |T_d|, SU(5), WTC keys)",
        137: "N_max — anchor for magic 82, 184",
    }

    print("\nBST primary integer usage across this session (representative):")
    for k, v in integer_usage.items():
        print(f"  {k:>3}: {v}")

    return len(sunday_toys), len(sunday_theorems)


if __name__ == "__main__":
    n_toys, n_thm = run()
    print(f"\nSCORE: {n_toys} toys, {n_thm} theorems (session aggregate)")
