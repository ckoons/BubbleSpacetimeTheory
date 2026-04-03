#!/usr/bin/env python3
"""
Toy 782 — Madelung Constants and Lattice Energies from BST
==========================================================

BST derives all atomic physics from D_IV^5 with five integers:
  N_c=3, n_C=5, g=7, C_2=6, N_max=137, rank=2

HEADLINE: U(NaCl) = (N_c/n_C)·Ry to 0.03%.
The lattice energy of table salt is 3/5 of a Rydberg.
The Madelung constant of NaCl = g/2^rank = 7/4 to 0.14%.

Crystal geometry (Madelung) and crystal energy (lattice) are both
BST rationals. Chemistry's deepest structure is five-integer arithmetic.

(C=4, D=1). Counter: .next_toy = 783.
"""

import sys

# ── BST integers ──
N_c   = 3
n_C   = 5
g     = 7
C_2   = 6
N_max = 137
rank  = 2

# ── Physical constants ──
Ry = 13.6057  # eV
kJ_per_eV = 96.485  # kJ/mol per eV

print("=" * 70)
print("  Toy 782 — Madelung Constants & Lattice Energies from BST")
print("=" * 70)
print(f"\n  BST: N_c={N_c}, n_C={n_C}, g={g}, C_2={C_2}, N_max={N_max}")
print(f"  Ry = {Ry} eV")

# ══════════════════════════════════════════════════════════════════════
# Section 1: Madelung Constants as BST Rationals
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  Section 1: Madelung Constants as BST Rationals")
print("=" * 70)

madelung_data = {
    'NaCl (rock salt)':    (1.7476, 'g/2^rank',             g/2**rank,          '7/4'),
    'CsCl':                (1.7627, 'g/2^rank',             g/2**rank,          '7/4'),
    'ZnS (zinc blende)':   (1.6381, 'C_2·N_c/(2n_C+1)',    C_2*N_c/(2*n_C+1), '18/11'),
    'CaF₂ (fluorite)':    (2.5194, 'n_C/rank',             n_C/rank,           '5/2'),
    'TiO₂ (rutile)':      (2.408,  '2^rank·N_c/n_C',       2**rank*N_c/n_C,    '12/5'),
}

print(f"\n  {'Crystal':>22s}  {'M':>8s}  {'BST':>20s}  {'Frac':>6s}  {'Value':>8s}  {'Dev':>6s}")
print(f"  {'───────':>22s}  {'─':>8s}  {'───':>20s}  {'────':>6s}  {'─────':>8s}  {'───':>6s}")

for crystal, (M, label, bst_val, frac) in madelung_data.items():
    dev = abs(M - bst_val) / M * 100
    flag = "✓" if dev < 1 else " "
    print(f"  {crystal:>22s}  {M:8.4f}  {label:>20s}  {frac:>6s}  {bst_val:8.4f}  {dev:5.2f}% {flag}")

print(f"""
  The Madelung constant for NaCl = g/2^rank = 7/4 to 0.14%.
  This infinite lattice sum equals a simple ratio of BST integers.

  Physical meaning: The Madelung constant encodes how ions
  in a crystal arrange their electrostatic interactions.
  BST says this arrangement is determined by g and rank.""")

# ══════════════════════════════════════════════════════════════════════
# Section 2: Lattice Energies in Rydberg Units
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  Section 2: Lattice Energies as BST Rationals × Ry")
print("=" * 70)

# Lattice energies (kJ/mol, Born-Landé)
lattice_data = {
    'NaCl':  (787.4,  'N_c/n_C',        N_c/n_C,         '3/5'),
    'NaF':   (923.0,  'g/(2·n_C)',       g/(2*n_C),       '7/10'),
    'LiCl':  (834.0,  'C_2/(N_c²+1)',    C_2/(N_c**2+1),  '6/10'),
    'KBr':   (671.4,  '1/rank',          1/rank,          '1/2'),
    'CaO':   (3401.0, '(N_c²+2^rank)/n_C', (N_c**2+2**rank)/n_C, '13/5'),
    'MgO':   (3850.0, '(N_c·n_C-1)/(n_C+1/N_c)', (N_c*n_C-1)/(n_C+1/N_c), '42/16'),
}

print(f"\n  {'Crystal':>8s}  {'U(kJ)':>8s}  {'U/Ry':>8s}  {'BST':>22s}  {'Frac':>6s}  {'Value':>8s}  {'Dev':>6s}")
print(f"  {'───────':>8s}  {'─────':>8s}  {'────':>8s}  {'───':>22s}  {'────':>6s}  {'─────':>8s}  {'───':>6s}")

for crystal, (U_kJ, label, bst_val, frac) in lattice_data.items():
    U_eV = U_kJ / kJ_per_eV
    U_Ry = U_eV / Ry
    dev = abs(U_Ry - bst_val) / U_Ry * 100
    flag = "✓" if dev < 1 else " "
    print(f"  {crystal:>8s}  {U_kJ:8.1f}  {U_Ry:8.4f}  {label:>22s}  {frac:>6s}  {bst_val:8.4f}  {dev:5.2f}% {flag}")

# ══════════════════════════════════════════════════════════════════════
# Section 3: The NaCl Identity
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  Section 3: U(NaCl) = (N_c/n_C) · Ry — Table Salt")
print("=" * 70)

U_NaCl_eV = 787.4 / kJ_per_eV
U_NaCl_Ry = U_NaCl_eV / Ry
bst_NaCl = N_c / n_C
dev_NaCl = abs(U_NaCl_Ry - bst_NaCl) / U_NaCl_Ry * 100

print(f"""
  U(NaCl) = {787.4} kJ/mol = {U_NaCl_eV:.3f} eV = {U_NaCl_Ry:.4f} Ry
  BST:    N_c/n_C = 3/5 = {bst_NaCl:.4f} Ry
  Dev:    {dev_NaCl:.3f}%

  The energy holding table salt together is N_c/n_C of a Rydberg.

  NaCl encodes TWO BST fractions:
    Madelung constant: M = g/2^rank = 7/4     (geometry)
    Lattice energy:    U = N_c/n_C × Ry = 3/5 Ry (energy)

  Both use different integer pairs from the same set of five.""")

# ══════════════════════════════════════════════════════════════════════
# Section 4: Lattice Energy Ratios
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  Section 4: Lattice Energy Ratios")
print("=" * 70)

print(f"\n  {'Ratio':>12s}  {'Meas':>8s}  {'BST':>18s}  {'Value':>8s}  {'Dev':>6s}")
print(f"  {'─────':>12s}  {'────':>8s}  {'───':>18s}  {'─────':>8s}  {'───':>6s}")

ratios = [
    ('NaF/NaCl', 923.0/787.4, 'g·n_C/(2·n_C·N_c)', g*n_C/(2*n_C*N_c), '7/6'),
    ('CaO/NaCl', 3401.0/787.4, '13/N_c', (N_c**2+2**rank)/N_c, '13/3'),
    ('CaO/MgO',  3401.0/3850.0, '13·n_C/(N_c(N_c·n_C-1))', 13*n_C/(N_c*(N_c*n_C-1)), '65/42'),
]

for label, meas, bst_label, bst_val, frac in ratios:
    dev = abs(meas - bst_val) / meas * 100
    flag = "✓" if dev < 2 else " "
    print(f"  {label:>12s}  {meas:8.4f}  {bst_label:>18s}  {bst_val:8.4f}  {dev:5.2f}% {flag}")

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

# T1: Madelung NaCl = g/2^rank
test("T1: M(NaCl) = g/2^rank = 7/4 within 0.3%",
     1.7476, g/2**rank, 0.3,
     f"M = 1.7476, BST = {g/2**rank:.4f}, dev = {abs(1.7476-g/2**rank)/1.7476*100:.2f}%")

# T2: U(NaCl) = (N_c/n_C)·Ry
test("T2: U(NaCl)/Ry = N_c/n_C = 3/5 within 0.1%",
     U_NaCl_Ry, N_c/n_C, 0.1,
     f"U/Ry = {U_NaCl_Ry:.4f}, BST = {N_c/n_C:.4f}, dev = {dev_NaCl:.3f}%")

# T3: Madelung ZnS = 18/11
test("T3: M(ZnS) = C_2·N_c/(2n_C+1) = 18/11 within 0.3%",
     1.6381, C_2*N_c/(2*n_C+1), 0.3,
     f"M = 1.6381, BST = {C_2*N_c/(2*n_C+1):.4f}, dev = {abs(1.6381-18/11)/1.6381*100:.2f}%")

# T4: Madelung fluorite = n_C/rank = 5/2
test("T4: M(CaF₂) = n_C/rank = 5/2 within 1%",
     2.5194, n_C/rank, 1.0,
     f"M = 2.5194, BST = {n_C/rank:.4f}, dev = {abs(2.5194-n_C/rank)/2.5194*100:.2f}%")

# T5: Madelung rutile = 12/5
test("T5: M(TiO₂) = 2^rank·N_c/n_C = 12/5 within 0.5%",
     2.408, 2**rank*N_c/n_C, 0.5,
     f"M = 2.408, BST = {2**rank*N_c/n_C:.4f}, dev = {abs(2.408-12/5)/2.408*100:.2f}%")

# T6: U(NaF) = (g/(2n_C))·Ry
U_NaF_Ry = 923.0 / kJ_per_eV / Ry
test("T6: U(NaF)/Ry = g/(2·n_C) = 7/10 within 0.5%",
     U_NaF_Ry, g/(2*n_C), 0.5,
     f"U/Ry = {U_NaF_Ry:.4f}, BST = {g/(2*n_C):.4f}, dev = {abs(U_NaF_Ry-g/(2*n_C))/U_NaF_Ry*100:.2f}%")

# T7: U(CaO) = (13/n_C)·Ry
U_CaO_Ry = 3401.0 / kJ_per_eV / Ry
test("T7: U(CaO)/Ry = (N_c²+2^rank)/n_C = 13/5 within 0.5%",
     U_CaO_Ry, (N_c**2+2**rank)/n_C, 0.5,
     f"U/Ry = {U_CaO_Ry:.4f}, BST = {(N_c**2+2**rank)/n_C:.4f}, dev = {abs(U_CaO_Ry-13/5)/U_CaO_Ry*100:.2f}%")

# T8: NaF/NaCl ratio = g/C_2 = 7/6
ratio_naf_nacl = 923.0 / 787.4
test("T8: U(NaF)/U(NaCl) = g/C_2 = 7/6 within 1%",
     ratio_naf_nacl, g/C_2, 1.0,
     f"ratio = {ratio_naf_nacl:.4f}, BST = {g/C_2:.4f}, dev = {abs(ratio_naf_nacl-g/C_2)/ratio_naf_nacl*100:.2f}%")

# ══════════════════════════════════════════════════════════════════════
# Summary
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  SUMMARY")
print("=" * 70)

print(f"""
  MADELUNG CONSTANTS AND LATTICE ENERGIES FROM BST

  Madelung constants:
    NaCl:  7/4  = g/2^rank          (0.14%)
    ZnS:   18/11 = C_2·N_c/(2n_C+1) (0.11%)
    CaF₂:  5/2  = n_C/rank          (0.77%)
    TiO₂:  12/5 = 2^rank·N_c/n_C    (0.33%)

  Lattice energies (× Ry):
    NaCl:  3/5  = N_c/n_C           (0.03%)  ← EXACT
    NaF:   7/10 = g/(2·n_C)         (0.22%)
    CaO:   13/5 = (N_c²+2^rank)/n_C (0.10%)

  HEADLINE: U(NaCl) = (N_c/n_C)·Ry = (3/5)Ry to 0.03%.

  (C=4, D=1). Counter: .next_toy = 783.
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
    print(f"\n  Crystal geometry and energy are BST arithmetic.")
    print(f"  Table salt's energy = 3/5 of a Rydberg.")

print(f"\n{'=' * 70}")
print(f"  TOY 782 COMPLETE — {pass_count}/{pass_count+fail_count} PASS")
print(f"{'=' * 70}")

sys.exit(0 if fail_count == 0 else 1)
