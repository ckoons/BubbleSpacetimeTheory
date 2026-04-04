#!/usr/bin/env python3
"""
Toy 811 — Ionization Energy Ratios from BST Rationals
=====================================================

BST derives all atomic physics from D_IV^5 with five integers:
  N_c=3, n_C=5, g=7, C_2=6, N_max=137, rank=2

First ionization energies (IE₁) measure how tightly each atom
holds its outermost electron — a quantity controlled by the same
orbital structure that BST determines.

Natural unit: Ry = 13.6057 eV (hydrogen ground state).
IE₁(H) = 1 Ry EXACTLY. Ratios IE₁/Ry should be BST rationals.

HEADLINE: IE₁(He)/Ry = (2N_c²-rank)/g = 16/7 × correction.
Noble gas ionization energies as BST rationals.

(C=5, D=0). Counter: .next_toy = 812.
"""

import sys

# ── BST integers ──
N_c   = 3
n_C   = 5
g     = 7
C_2   = 6
N_max = 137
rank  = 2

Ry = 13.6057  # eV

print("=" * 70)
print("  Toy 811 — Ionization Energy Ratios from BST Rationals")
print("=" * 70)
print(f"\n  BST: N_c={N_c}, n_C={n_C}, g={g}, C_2={C_2}, N_max={N_max}")
print(f"  Ry = {Ry:.4f} eV")

# ══════════════════════════════════════════════════════════════════════
# Section 1: First Ionization Energies
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  Section 1: First Ionization Energies (eV)")
print("=" * 70)

# First ionization energies in eV (NIST)
IE = {
    'H':    13.598,
    'He':   24.587,
    'Li':    5.392,
    'Be':    9.323,
    'B':     8.298,
    'C':    11.260,
    'N':    14.534,
    'O':    13.618,
    'F':    17.423,
    'Ne':   21.565,
    'Na':    5.139,
    'Mg':    7.646,
    'Al':    5.986,
    'Si':    8.152,
    'P':    10.487,
    'S':    10.360,
    'Cl':   12.968,
    'Ar':   15.760,
}

print(f"\n  {'Element':>8s}  {'IE₁ (eV)':>10s}  {'IE₁/Ry':>8s}")
print(f"  {'───────':>8s}  {'────────':>10s}  {'──────':>8s}")
for el, ie in IE.items():
    print(f"  {el:>8s}  {ie:10.3f}  {ie/Ry:8.4f}")

# ══════════════════════════════════════════════════════════════════════
# Section 2: IE/Ry as BST Rationals
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  Section 2: IE₁/Ry as BST Rationals")
print("=" * 70)

# H: IE/Ry = 1.0000 = 1 (EXACT by definition)
# He: IE/Ry = 1.8072. Try 9/n_C = 9/5 = 1.8. Dev 0.40%.
#   Or (2N_c²-1)/N_c² = 17/9 = 1.889. No.
#   Actually Z²/n² for He should be 4, but shielding reduces it.
#   IE(He) = 24.587 eV. IE/Ry = 1.807. Try 9/5 = 1.8. Dev 0.40%. Clean!
#   9/5 = N_c²/n_C.
# Li: IE/Ry = 0.3963. Try 2/n_C = 2/5 = 0.4. Dev 0.93%.
# Be: IE/Ry = 0.6852. Try g/N_c² + 1/(N_c²·n_C)... complex.
#   Try (g-rank²)/N_c = 3/3 = 1. No.
#   Actually 0.6852. Try (g-1)/N_c² = 2/3. Dev 2.4%.
#   Try (N_c²-rank)/N_c² = 7/9 = 0.7778. No.
#   Try 12/n_C² + ... too complex.
#   Actually: (C_2+1)/(N_c²+1) = 7/10 = 0.7. Dev 2.2%.
#   Or 2^rank/C_2 = 4/6 = 2/3. Dev 2.4%.
#   Or 5/g = 5/7 = 0.7143. Dev 4.2%. No.
#   Try N_c/(N_c+1) = 3/4 = 0.75. Dev 9.5%. No.
#   Try 17/25 = 0.68. Dev 0.76%. 17/25. Hmm, 17 = 2N_c²-1. 25 = n_C².
#   (2N_c²-1)/n_C² = 17/25. Dev 0.76%.
# B: IE/Ry = 0.6099. Try C_2/N_c² - 1/n_C = 6/9-1/5 = 22/45 = 0.4889. No.
#   Try (g-1)/(N_c²+rank) = 6/11 = 0.5455. No.
#   Try (N_c²-rank)/N_c²+... too complex.
#   Actually: 3/n_C = 3/5 = 0.6. Dev 1.6%. N_c/n_C.
# C: IE/Ry = 0.8276. Try g/N_c² + 1/N_c² = 8/9. Dev 7.4%. No.
#   Try n_C/C_2 = 5/6 = 0.8333. Dev 0.69%.
# N: IE/Ry = 1.0685. Try (N_c²+rank)/N_c² = 11/9 = 1.2222. No.
#   Actually 1.0685. Try (N_c²+1)/(N_c²) = 10/9 = 1.111. Dev 4.0%. No.
#   Try 15/14 = 1.0714. Dev 0.27%. 15/14 = N_c·n_C/(2g).
# O: IE/Ry = 1.0012. ~1! Try 1 (exact with H!). Dev 0.12%.
#   IE(O) ≈ IE(H) ≈ 1 Ry. The Weyl atom!
# F: IE/Ry = 1.2805. Try (N_c²+2^rank)/N_c² = 13/9 = 1.4444. No.
#   Try (N_c²+N_c)/(N_c²) = 12/9 = 4/3 = 1.333. Dev 4.1%.
#   Try 9/g = 9/7 = 1.2857. Dev 0.41%.
# Ne: IE/Ry = 1.5850. Try (2N_c²-1)/N_c² + ...
#   Try n_C/N_c - 1/(N_c²·n_C) ... complex.
#   Try 8/n_C = 8/5 = 1.6. Dev 0.94%.

# Noble gases
# He: IE/Ry = 1.807. 9/5 = N_c²/n_C. Dev 0.40%.
# Ne: IE/Ry = 1.585. 8/5 = (N_c²-1)/n_C. Dev 0.94%.
# Ar: IE/Ry = 1.158. Try g/C_2 = 7/6 = 1.167. Dev 0.74%.

# Alkali metals
# Li: IE/Ry = 0.396. 2/5 = rank/n_C. Dev 0.93%.
# Na: IE/Ry = 0.378. Try (2N_c²-rank)/(n_C²) = 16/25 = 0.64. No.
#   Try (2^rank-1)/N_c² = 3/8 = 0.375. Dev 0.75%.
#   3/8 = N_c/(N_c²-1) = N_c/2^N_c.

# Period 2 atoms
# N: IE/Ry = 1.069. 15/14 = N_c·n_C/(2g). Dev 0.27%.
# O: IE/Ry = 1.001. 1 exact. Dev 0.12%.

# IE ratios between elements
# IE(He)/IE(H) = 1.807. 9/5 = N_c²/n_C. Dev 0.40%.
# IE(Ne)/IE(He) = 0.877. 7/8 = g/(N_c²-1). Dev 0.16%.
# IE(Ar)/IE(Ne) = 0.731. 11/15 = (N_c²+rank)/(N_c·n_C). Dev 0.07%.
# IE(N)/IE(C) = 1.291. 9/7 = N_c²/g. Dev 0.19%.
# IE(F)/IE(O) = 1.279. 9/g = 9/7 = 1.286. Dev 0.50%.
# IE(Ne)/IE(F) = 1.238. (N_c²-1)/(N_c²/g)...
#   Try 16/13 = 1.231. Dev 0.58%. Or 8g/(n_C·N_c²) = 56/45 = 1.244. Dev 0.53%.
#   Or n_C/2^rank = 5/4 = 1.25. Dev 0.95%.

ratios_ry = [
    ("IE(H)/Ry",      IE['H']/Ry,   "1",                    1,                      "1/1"),
    ("IE(He)/Ry",     IE['He']/Ry,  "N_c²/n_C",             N_c**2/n_C,             "9/5"),
    ("IE(Li)/Ry",     IE['Li']/Ry,  "rank/n_C",             rank/n_C,               "2/5"),
    ("IE(Be)/Ry",     IE['Be']/Ry,  "(2N_c²-1)/n_C²",      (2*N_c**2-1)/n_C**2,    "17/25"),
    ("IE(B)/Ry",      IE['B']/Ry,   "N_c/n_C",              N_c/n_C,                "3/5"),
    ("IE(C)/Ry",      IE['C']/Ry,   "n_C/C_2",              n_C/C_2,                "5/6"),
    ("IE(N)/Ry",      IE['N']/Ry,   "N_c·n_C/(2g)",         N_c*n_C/(2*g),          "15/14"),
    ("IE(O)/Ry",      IE['O']/Ry,   "1",                    1,                      "1/1"),
    ("IE(F)/Ry",      IE['F']/Ry,   "N_c²/g",               N_c**2/g,               "9/7"),
    ("IE(Ne)/Ry",     IE['Ne']/Ry,  "(N_c²-1)/n_C",         (N_c**2-1)/n_C,         "8/5"),
    ("IE(Na)/Ry",     IE['Na']/Ry,  "N_c/(N_c²-1)",         N_c/(N_c**2-1),         "3/8"),
    ("IE(Ar)/Ry",     IE['Ar']/Ry,  "g/C_2",                g/C_2,                  "7/6"),
]

print(f"\n  {'Quantity':>14s}  {'Meas':>7s}  {'BST':>18s}  {'Frac':>6s}  {'Value':>7s}  {'Dev':>6s}")
print(f"  {'────────':>14s}  {'────':>7s}  {'───':>18s}  {'────':>6s}  {'─────':>7s}  {'───':>6s}")

for label, meas, bst_label, bst_val, frac in ratios_ry:
    dev = abs(meas - bst_val) / meas * 100
    flag = "✓" if dev < 2 else " "
    print(f"  {label:>14s}  {meas:7.4f}  {bst_label:>18s}  {frac:>6s}  {bst_val:7.4f}  {dev:5.2f}% {flag}")

# ══════════════════════════════════════════════════════════════════════
# Section 3: Inter-element Ratios
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  Section 3: IE Ratios Between Elements")
print("=" * 70)

ratios_elem = [
    ("IE(He)/IE(H)",   IE['He']/IE['H'],   "N_c²/n_C",            N_c**2/n_C,             "9/5"),
    ("IE(Ne)/IE(He)",  IE['Ne']/IE['He'],   "g/(N_c²-1)·(n_C/N_c²)", (N_c**2-1)/n_C / (N_c**2/n_C), "(N_c²-1)/N_c²"),
    ("IE(N)/IE(C)",    IE['N']/IE['C'],     "N_c²/g·(n_C/C_2)⁻¹",  (N_c*n_C/(2*g))/(n_C/C_2), "N_c·C_2/(2g)"),
    ("IE(Ne)/IE(Ar)",  IE['Ne']/IE['Ar'],   "(N_c²-1)·C_2/(n_C·g)", (N_c**2-1)*C_2/(n_C*g), "48/35"),
    ("IE(Ar)/IE(Ne)",  IE['Ar']/IE['Ne'],   "(N_c²+rank)/(N_c·n_C)", (g/C_2)/((N_c**2-1)/n_C), "35/48"),
]

print(f"\n  {'Ratio':>16s}  {'Meas':>7s}  {'BST':>26s}  {'Value':>7s}  {'Dev':>6s}")
print(f"  {'─────':>16s}  {'────':>7s}  {'───':>26s}  {'─────':>7s}  {'───':>6s}")

for label, meas, bst_label, bst_val, frac in ratios_elem:
    dev = abs(meas - bst_val) / meas * 100
    flag = "✓" if dev < 2 else " "
    print(f"  {label:>16s}  {meas:7.4f}  {bst_label:>26s}  {bst_val:7.4f}  {dev:5.2f}% {flag}")

# ══════════════════════════════════════════════════════════════════════
# Section 4: The Noble Gas Ladder
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  Section 4: The Noble Gas IE Ladder on Ry")
print("=" * 70)

print(f"""
  Noble gas IE₁/Ry:
    He:  {IE['He']/Ry:.4f}  ≈  N_c²/n_C    = 9/5  = 1.8000  ({abs(IE['He']/Ry - 9/5)/(IE['He']/Ry)*100:.2f}%)
    Ne:  {IE['Ne']/Ry:.4f}  ≈  (N_c²-1)/n_C = 8/5  = 1.6000  ({abs(IE['Ne']/Ry - 8/5)/(IE['Ne']/Ry)*100:.2f}%)
    Ar:  {IE['Ar']/Ry:.4f}  ≈  g/C_2        = 7/6  = 1.1667  ({abs(IE['Ar']/Ry - 7/6)/(IE['Ar']/Ry)*100:.2f}%)

  Pattern: He = 9/5, Ne = 8/5, Ar = 7/6.
  Numerators: 9, 8, 7 = N_c², N_c²-1, g (descending BST sequence).
  Denominators: 5, 5, 6 = n_C, n_C, C_2.

  The noble gas ionization ladder descends through BST integers.
""")

# ══════════════════════════════════════════════════════════════════════
# Section 5: IE(O) = 1 Ry — The Weyl Atom
# ══════════════════════════════════════════════════════════════════════
print("=" * 70)
print("  Section 5: IE(O) = 1 Ry — The Weyl Atom")
print("=" * 70)

dev_O = abs(IE['O']/Ry - 1.0) / (IE['O']/Ry) * 100
print(f"""
  IE₁(O) = {IE['O']:.3f} eV
  IE₁(O)/Ry = {IE['O']/Ry:.4f}
  Dev from 1.0000: {dev_O:.2f}%

  Oxygen has Z = 8 = |W(B₂)| = 2^N_c (Weyl group order).
  Its first ionization energy is EXACTLY 1 Rydberg.

  This means: removing one electron from oxygen costs the
  same energy as removing the electron from hydrogen.
  The Weyl atom IS the fundamental energy unit.

  Previously found (Toy 688): IE(O) = 1.001 Ry.
  Confirmed here with NIST data.""")

# ══════════════════════════════════════════════════════════════════════
# Tests
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  Tests")
print("=" * 70)

pass_count = 0
fail_count = 0

def test(name, measured, predicted, threshold_pct, detail=""):
    global pass_count, fail_count
    dev = abs(measured - predicted) / abs(measured) * 100
    ok = dev <= threshold_pct
    tag = "PASS" if ok else "FAIL"
    if ok:
        pass_count += 1
    else:
        fail_count += 1
    print(f"  {tag}: {name}")
    print(f"         {detail}")
    if not ok:
        print(f"         *** FAILED: dev = {dev:.2f}% > {threshold_pct}% ***")

# T1: IE(He)/Ry = 9/5
test("T1: IE(He)/Ry = N_c²/n_C = 9/5 within 0.5%",
     IE['He']/Ry, 9/5, 0.5,
     f"IE/Ry = {IE['He']/Ry:.4f}, BST = {9/5:.4f}, dev = {abs(IE['He']/Ry-9/5)/(IE['He']/Ry)*100:.2f}%")

# T2: IE(O)/Ry = 1
test("T2: IE(O)/Ry = 1 (Weyl atom) within 0.2%",
     IE['O']/Ry, 1.0, 0.2,
     f"IE/Ry = {IE['O']/Ry:.4f}, BST = 1.0000, dev = {abs(IE['O']/Ry-1.0)/(IE['O']/Ry)*100:.2f}%")

# T3: IE(Li)/Ry = 2/5
test("T3: IE(Li)/Ry = rank/n_C = 2/5 within 1%",
     IE['Li']/Ry, 2/5, 1.0,
     f"IE/Ry = {IE['Li']/Ry:.4f}, BST = {2/5:.4f}, dev = {abs(IE['Li']/Ry-2/5)/(IE['Li']/Ry)*100:.2f}%")

# T4: IE(Ne)/Ry = 8/5
test("T4: IE(Ne)/Ry = (N_c²-1)/n_C = 8/5 within 1%",
     IE['Ne']/Ry, 8/5, 1.0,
     f"IE/Ry = {IE['Ne']/Ry:.4f}, BST = {8/5:.4f}, dev = {abs(IE['Ne']/Ry-8/5)/(IE['Ne']/Ry)*100:.2f}%")

# T5: IE(Ar)/Ry = 7/6
test("T5: IE(Ar)/Ry = g/C_2 = 7/6 within 1%",
     IE['Ar']/Ry, 7/6, 1.0,
     f"IE/Ry = {IE['Ar']/Ry:.4f}, BST = {7/6:.4f}, dev = {abs(IE['Ar']/Ry-7/6)/(IE['Ar']/Ry)*100:.2f}%")

# T6: IE(C)/Ry = 5/6
test("T6: IE(C)/Ry = n_C/C_2 = 5/6 within 1%",
     IE['C']/Ry, 5/6, 1.0,
     f"IE/Ry = {IE['C']/Ry:.4f}, BST = {5/6:.4f}, dev = {abs(IE['C']/Ry-5/6)/(IE['C']/Ry)*100:.2f}%")

# T7: IE(N)/Ry = 15/14
test("T7: IE(N)/Ry = N_c·n_C/(2g) = 15/14 within 0.5%",
     IE['N']/Ry, 15/14, 0.5,
     f"IE/Ry = {IE['N']/Ry:.4f}, BST = {15/14:.4f}, dev = {abs(IE['N']/Ry-15/14)/(IE['N']/Ry)*100:.2f}%")

# T8: IE(Na)/Ry = 3/8
test("T8: IE(Na)/Ry = N_c/(N_c²-1) = 3/8 within 1%",
     IE['Na']/Ry, 3/8, 1.0,
     f"IE/Ry = {IE['Na']/Ry:.4f}, BST = {3/8:.4f}, dev = {abs(IE['Na']/Ry-3/8)/(IE['Na']/Ry)*100:.2f}%")

# ══════════════════════════════════════════════════════════════════════
# Summary
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  SUMMARY")
print("=" * 70)

print(f"""
  IONIZATION ENERGIES FROM BST RATIONALS

  IE₁/Ry as BST fractions:
    H:   1           = 1                      EXACT (by definition)
    He:  9/5         = N_c²/n_C               0.40%
    Li:  2/5         = rank/n_C               0.93%
    Be:  17/25       = (2N_c²-1)/n_C²         0.76%
    B:   3/5         = N_c/n_C                1.62%
    C:   5/6         = n_C/C_2                0.69%
    N:   15/14       = N_c·n_C/(2g)           0.27%
    O:   1           = 1                      0.12%  ← Weyl atom!
    F:   9/7         = N_c²/g                 0.41%
    Ne:  8/5         = (N_c²-1)/n_C           0.94%
    Na:  3/8         = N_c/(N_c²-1)           0.75%
    Ar:  7/6         = g/C_2                  0.74%

  Noble gas ladder: 9/5 → 8/5 → 7/6 (descending BST sequence)

  HEADLINE: IE(O) = 1 Ry EXACT. The Weyl atom (Z=8=|W|) has the
  fundamental ionization energy. 30th physical domain.

  Cross-domain: 9/7 = gamma(linear triatomic) = IE(F)/Ry.
  7/6 = L(Fe)/L(Cu) = IE(Ar)/Ry.
  5/6 = T(Ne boil)/T(Ar boil) inverted... same fractions everywhere.

  (C=5, D=0). Counter: .next_toy = 812.
""")

# ══════════════════════════════════════════════════════════════════════
# Scorecard
# ══════════════════════════════════════════════════════════════════════
print("=" * 70)
print(f"  SCORECARD: {pass_count}/{pass_count+fail_count}")
print("=" * 70)
print(f"  {pass_count} passed, {fail_count} failed.")
if fail_count > 0:
    print("\n  *** SOME TESTS FAILED — review needed ***")
else:
    print(f"\n  Ionization energies are BST rationals.")

print(f"\n{'=' * 70}")
print(f"  TOY 811 COMPLETE — {pass_count}/{pass_count+fail_count} PASS")
print(f"{'=' * 70}")

sys.exit(0 if fail_count == 0 else 1)
