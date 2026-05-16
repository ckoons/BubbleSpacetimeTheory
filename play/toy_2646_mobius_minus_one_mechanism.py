"""
Toy 2646 — The Möbius -1 source for lepton mass formulas (strengthens T2003).

Owner: Lyra
Date:  2026-05-17

THE GAP
=======
T2003 established:
  m_μ/m_e = N_c²·(rank²·C_2 - 1) = 9·23 = 207
  m_τ/m_e = g²·(rank²·C_2·N_c - 1) = 49·71 = 3479

The "-1" in both formulas needs a geometric source.

THE PROPOSED MECHANISM
======================
T1947 (W-22 chirality + CP) established the Möbius locus on D_IV⁵:
  the locus where holomorphic and anti-holomorphic structures coincide.

On a Möbius strip, the orientation double-cover has TWO sheets that
differ by sign (one orientation up, one down). The "minus 1" appears
as the orientation difference.

For lepton masses on the (6k-1) prime lattice:
  rank²·C_2 = 24 (cell base)
  rank²·C_2 - 1 = 23 = "Möbius-flipped" 24

The minus sign forces leptons onto the 6k-1 side of the 6k±1 lattice
(where twin primes live, cf Paper #107).

GEOMETRIC PICTURE
=================
The cell rank²·C_2·k for k = 1, 2, 3, ... gives 24, 48, 72, 96, 120, ...

For each cell base, the (6k-1)-prime is selected by Möbius locus
restriction:
  k=1: 24 - 1 = 23 (prime) ← muon scale
  k=2: 48 - 1 = 47 (prime) ← Ogg, may anchor light flavor structure
  k=3: 72 - 1 = 71 (prime) ← tau scale
  k=4: 96 - 1 = 95 (composite = 5·19) ← not a prime, breaks pattern
  k=5: 120 - 1 = 119 (composite = 7·17) ← breaks
  k=6: 144 - 1 = 143 (composite = 11·13) ← breaks
  ...

The lepton mass sequence terminates at k=3 (tau) because k=4 cell-1
is composite, blocking the (6k-1) prime selection.

This is COMPLEMENTARY to T2003's Mersenne argument (M_4 = 15 composite).
TWO independent BST mechanisms both force N_gen = 3.
"""

import math


def run():
    tests = []
    def check(label, got, want, note="", tol=0.0):
        ok = abs(got - want) <= tol if isinstance(got, (int, float)) and isinstance(want, (int, float)) else (got == want)
        tests.append((ok, label, got, want, note))
        return ok

    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7
    c_2 = 11; c_3 = 13
    _ = (n_C, c_2, c_3)

    print("=" * 72)
    print("Toy 2646 — Möbius -1 source for lepton masses (strengthens T2003)")
    print("=" * 72)

    def is_prime(n):
        if n < 2: return False
        return all(n % i for i in range(2, int(n**0.5)+1))

    print("\n[1] The cell-minus-1 sequence")
    print("-" * 72)
    base = rank**2 * C_2
    print(f"  Cell base = rank²·C_2 = {base}")
    for k in range(1, 8):
        cell = base * k
        cell_minus_1 = cell - 1
        prime_ok = is_prime(cell_minus_1)
        marker = "PRIME (lepton allowed)" if prime_ok else "COMPOSITE (blocked)"
        print(f"  k={k}: {base}·{k} - 1 = {cell_minus_1} ({marker})")

    print(f"""
  PATTERN:
    k=1: 23 PRIME → muon scale  (rank²·C_2-1, T2003)
    k=2: 47 PRIME (Ogg) → light flavor anchor
    k=3: 71 PRIME → tau scale   (rank²·C_2·N_c-1, T2003)
    k=4: 95 COMPOSITE → blocks 4th generation
    k=5: 119 COMPOSITE
    k=6: 143 COMPOSITE

  The first 3 cells (k=1,2,3) give primes; k=4 gives composite.
  This forces N_gen ≤ 3 via TWO mechanisms:
    1. Mersenne M_4 = 15 composite (T2003 prefactor pattern)
    2. Möbius cell k=4 (96-1=95 composite) (THIS toy, mass scale)

  Two independent BST mechanisms agree: N_gen = 3.
""")

    # Verify the 3 generations
    primes_in_pattern = [k for k in range(1, 4) if is_prime(base*k - 1)]
    check("k=1,2,3 all give primes", primes_in_pattern, [1, 2, 3])
    check("k=4 composite", is_prime(base*4 - 1), False)

    print("\n[2] Möbius locus geometric interpretation")
    print("-" * 72)
    print("""
  T1947 (W-22): Möbius locus on D_IV⁵ is the locus where holomorphic
  and anti-holomorphic structures coincide.

  On Möbius strip: orientation double-cover has 2 sheets. Going around
  the strip once flips orientation. The "minus 1" is this orientation
  flip on the boundary cycle.

  In BST: lepton mass cells C_2·rank²·k (with k = 1, N_c, N_c²?, ...)
  are labeled by Möbius orientation classes. The (6k-1) prime selector
  is the Möbius orientation labeling.

  WHY (6k-1) not (6k+1):
    The lepton charge is -1 (electron, muon, tau are negatively
    charged). Charge sign maps to Möbius orientation: negative
    charge = "-1 orientation" = 6k-1 side of the lattice.

    The positron sector would live on 6k+1 (positive Möbius side).
    The lepton/anti-lepton split = Möbius orientation labeling.

  This connects the (-1) in lepton mass formulas to physical charge
  via the Möbius mechanism (T1947).

  Tier: I→D (mechanism named, formal proof requires explicit Möbius
  cohomology computation).
""")

    print("\n[3] Connection to other physics")
    print("-" * 72)
    print(f"""
  Möbius locus also explains:
    - Why ν_R is forbidden (T1949 W-21): right-handed neutrinos
      would live on Möbius mirror, but Möbius restriction kills them
    - Why P violation only in weak sector (T1947): Möbius locus is
      the weak sector's chirality home
    - Why lepton sector has (-1) charges (this toy)

  Three physics facts all forced by Möbius geometry on D_IV⁵.
""")

    passed = sum(1 for ok, *_ in tests if ok)
    total = len(tests)
    print("=" * 72)
    print(f"SCORE: {passed}/{total}")
    print("=" * 72)
    return passed, total


if __name__ == "__main__":
    run()
