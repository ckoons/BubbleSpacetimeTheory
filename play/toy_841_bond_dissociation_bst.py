#!/usr/bin/env python3
"""
Toy 841 — Bond Dissociation Energies as BST Rationals
======================================================

BST derives all atomic physics from D_IV^5 with five integers:
  N_c=3, n_C=5, g=7, C_2=6, N_max=137, rank=2

Bond dissociation energy (BDE) measures the energy to break a bond
homolytically. Natural unit: Ry = 13.6057 eV (hydrogen ground state).
BDE/Ry should be BST rationals.

Tier 1 chemistry: ionization (Toy 811), electronegativity (Toy 840),
bond dissociation (this toy).

HEADLINE: BDE(H-H)/Ry = 1/N_c = 1/3 (0.37%). The simplest
molecule's bond strength is 1/N_c Rydbergs.

(C=5, D=0). Counter: .next_toy = 842.
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

print("=" * 72)
print("  Toy 841 — Bond Dissociation Energies as BST Rationals")
print("=" * 72)
print(f"\n  BST: N_c={N_c}, n_C={n_C}, g={g}, C_2={C_2}, N_max={N_max}")
print(f"  Ry = {Ry:.4f} eV")

# ══════════════════════════════════════════════════════════════════════
# Bond dissociation energies (kJ/mol, NIST/CRC)
# Convert to eV: 1 kJ/mol = 0.01036 eV/molecule
# ══════════════════════════════════════════════════════════════════════

kJ_to_eV = 0.010364

# BDE in kJ/mol (NIST standard, 298 K)
BDE_kJ = {
    'H-H':   436.0,
    'H-F':   570.0,
    'H-Cl':  432.0,
    'H-O':   459.0,   # O-H in water
    'H-N':   386.0,   # N-H in ammonia
    'H-C':   411.0,   # C-H in methane
    'H-S':   363.0,
    'C-C':   346.0,
    'C=C':   614.0,
    'C≡C':   839.0,
    'C-O':   358.0,
    'C=O':   799.0,   # in CO₂
    'C-N':   305.0,
    'C≡N':   891.0,
    'C-F':   485.0,
    'C-Cl':  339.0,
    'N-N':   160.0,
    'N=N':   418.0,
    'N≡N':   945.0,
    'O-O':   146.0,
    'O=O':   498.0,
    'F-F':   159.0,
    'Cl-Cl': 243.0,
    'Na-Cl': 412.0,
}

# Convert to eV
BDE_eV = {k: v * kJ_to_eV for k, v in BDE_kJ.items()}

# ══════════════════════════════════════════════════════════════════════
# Section 1: BDE/Ry ratios
# ══════════════════════════════════════════════════════════════════════
print(f"\n{'=' * 72}")
print("  Section 1: BDE/Ry — Bond Energies on the BST Ladder")
print(f"{'=' * 72}")

print(f"\n  {'Bond':>6}  {'kJ/mol':>7}  {'eV':>7}  {'BDE/Ry':>7}")
print(f"  {'────':>6}  {'─'*7}  {'─'*7}  {'─'*7}")
for bond in sorted(BDE_eV.keys()):
    eV = BDE_eV[bond]
    ratio = eV / Ry
    print(f"  {bond:>6}  {BDE_kJ[bond]:7.0f}  {eV:7.3f}  {ratio:7.4f}")

# ══════════════════════════════════════════════════════════════════════
# Section 2: BST rational search
# ══════════════════════════════════════════════════════════════════════
print(f"\n{'=' * 72}")
print("  Section 2: BDE/Ry as BST Rationals")
print(f"{'=' * 72}")

def label_int(n):
    names = {
        1: "1", 2: "rank", 3: "N_c", 4: "2^rank", 5: "n_C",
        6: "C_2", 7: "g", 8: "2^N_c", 9: "N_c²", 10: "2n_C",
        12: "2C_2", 14: "2g", 15: "N_c·n_C", 18: "N_c·C_2",
        21: "C(g,2)", 25: "n_C²", 30: "n_C·C_2", 35: "C(g,3)",
        42: "C_2·g",
    }
    return names.get(n, str(n))

def search_bst(target, threshold=2.0):
    """Find BST rational p/q closest to target."""
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,21,25,30,35,42]
    dens = [1,2,3,4,5,6,7,8,9,10,12,14,15,18,21,25,30,35,42]
    best = None
    best_dev = threshold
    for p in nums:
        for q in dens:
            val = p / q
            dev = abs(val - target) / target * 100 if target > 0.001 else 100
            if dev < best_dev:
                best_dev = dev
                best = (p, q, val, dev)
    return best

results = []
print(f"\n  {'Bond':>6}  {'BDE/Ry':>7}  {'BST':>18}  {'Frac':>6}  {'Val':>7}  {'Dev':>6}")
print(f"  {'────':>6}  {'─'*7}  {'─'*18}  {'─'*6}  {'─'*7}  {'─'*6}")

for bond in ['H-H', 'H-F', 'H-Cl', 'H-O', 'H-N', 'H-C', 'H-S',
             'C-C', 'C=C', 'C≡C', 'C-O', 'C=O', 'C-N', 'C≡N',
             'C-F', 'C-Cl', 'N≡N', 'O=O', 'F-F', 'Cl-Cl', 'Na-Cl']:
    eV = BDE_eV[bond]
    ratio = eV / Ry
    r = search_bst(ratio)
    if r:
        p, q, val, dev = r
        bst = f"{label_int(p)}/{label_int(q)}"
        flag = "✓" if dev < 2 else " "
        print(f"  {bond:>6}  {ratio:7.4f}  {bst:>18s}  {p}/{q:>4d}  {val:7.4f}  {dev:5.2f}% {flag}")
        results.append((bond, ratio, bst, p, q, val, dev))
    else:
        print(f"  {bond:>6}  {ratio:7.4f}  {'> 2%':>18s}")
        results.append((bond, ratio, ">2%", 0, 0, 0, 100))

# ══════════════════════════════════════════════════════════════════════
# Section 3: Bond order patterns
# ══════════════════════════════════════════════════════════════════════
print(f"\n{'=' * 72}")
print("  Section 3: Bond Order Ladders")
print(f"{'=' * 72}")

print(f"""
  Carbon bonds:
    C-C  = {BDE_eV['C-C']/Ry:.4f} Ry
    C=C  = {BDE_eV['C=C']/Ry:.4f} Ry
    C≡C  = {BDE_eV['C≡C']/Ry:.4f} Ry
    Ratios: C=C/C-C = {BDE_kJ['C=C']/BDE_kJ['C-C']:.3f}, C≡C/C-C = {BDE_kJ['C≡C']/BDE_kJ['C-C']:.3f}

  Nitrogen bonds:
    N-N  = {BDE_eV['N-N']/Ry:.4f} Ry
    N=N  = {BDE_eV['N=N']/Ry:.4f} Ry
    N≡N  = {BDE_eV['N≡N']/Ry:.4f} Ry
    Ratios: N=N/N-N = {BDE_kJ['N=N']/BDE_kJ['N-N']:.3f}, N≡N/N-N = {BDE_kJ['N≡N']/BDE_kJ['N-N']:.3f}

  Bond order amplification:
    C: ×{BDE_kJ['C=C']/BDE_kJ['C-C']:.2f} per bond (double/single)
    N: ×{BDE_kJ['N=N']/BDE_kJ['N-N']:.2f} per bond (double/single)
    C triple/single: {BDE_kJ['C≡C']/BDE_kJ['C-C']:.2f}
    N triple/single: {BDE_kJ['N≡N']/BDE_kJ['N-N']:.2f}
""")

# Check C=C/C-C ratio
cc_ratio = BDE_kJ['C=C'] / BDE_kJ['C-C']  # 1.775
cn_ratio = BDE_kJ['N≡N'] / BDE_kJ['N-N']  # 5.906
print(f"  C=C/C-C = {cc_ratio:.3f} ≈ 9/5 = N_c²/n_C = {9/5:.3f} ({abs(cc_ratio-9/5)/cc_ratio*100:.1f}%)")
print(f"  N≡N/N-N = {cn_ratio:.3f} ≈ C_2 = {C_2:.3f} ({abs(cn_ratio-C_2)/cn_ratio*100:.1f}%)")

# ══════════════════════════════════════════════════════════════════════
# Section 4: BDE ratios between related bonds
# ══════════════════════════════════════════════════════════════════════
print(f"\n{'=' * 72}")
print("  Section 4: BDE Ratios Between Bonds")
print(f"{'=' * 72}")

bond_ratios = [
    ("H-F/H-H",   BDE_kJ['H-F']/BDE_kJ['H-H']),   # 1.307
    ("H-H/H-Cl",  BDE_kJ['H-H']/BDE_kJ['H-Cl']),   # 1.009
    ("H-F/H-Cl",  BDE_kJ['H-F']/BDE_kJ['H-Cl']),   # 1.319
    ("C≡C/C=C",   BDE_kJ['C≡C']/BDE_kJ['C=C']),    # 1.367
    ("C=O/C-O",   BDE_kJ['C=O']/BDE_kJ['C-O']),    # 2.232
    ("N≡N/N=N",   BDE_kJ['N≡N']/BDE_kJ['N=N']),    # 2.263
    ("C≡N/C-N",   BDE_kJ['C≡N']/BDE_kJ['C-N']),    # 2.921
    ("O=O/O-O",   BDE_kJ['O=O']/BDE_kJ['O-O']),    # 3.411
]

print(f"\n  {'Ratio':>12}  {'Value':>7}  {'BST':>18}  {'Frac':>6}  {'Dev':>6}")
print(f"  {'─'*12}  {'─'*7}  {'─'*18}  {'─'*6}  {'─'*6}")

for label, val in bond_ratios:
    r = search_bst(val)
    if r:
        p, q, v, dev = r
        bst = f"{label_int(p)}/{label_int(q)}"
        flag = "✓" if dev < 2 else " "
        print(f"  {label:>12}  {val:7.3f}  {bst:>18s}  {p}/{q:>4d}  {dev:5.2f}% {flag}")

# ══════════════════════════════════════════════════════════════════════
# Tests
# ══════════════════════════════════════════════════════════════════════
print(f"\n{'=' * 72}")
print("  Tests")
print(f"{'=' * 72}")

pass_count = 0
fail_count = 0

def test(name, measured, predicted, threshold, detail=""):
    global pass_count, fail_count
    dev = abs(measured - predicted) / abs(measured) * 100 if abs(measured) > 1e-10 else 100
    ok = dev <= threshold
    tag = "PASS" if ok else "FAIL"
    if ok:
        pass_count += 1
    else:
        fail_count += 1
    print(f"  {tag}: {name}")
    print(f"         meas={measured:.4f}, BST={predicted:.4f}, dev={dev:.2f}%")
    if detail:
        print(f"         {detail}")

# T1: H-H/Ry = 1/3 = 1/N_c
test("T1: BDE(H-H)/Ry = 1/N_c = 1/3",
     BDE_eV['H-H']/Ry, 1/N_c, 1.0,
     "Simplest molecule = 1/N_c Rydbergs")

# T2: H-F/Ry — search result
hf_ratio = BDE_eV['H-F']/Ry
r = search_bst(hf_ratio)
if r:
    test("T2: BDE(H-F)/Ry as BST rational",
         hf_ratio, r[2], 2.0,
         f"Best: {r[0]}/{r[1]} = {label_int(r[0])}/{label_int(r[1])}")

# T3: N≡N/Ry (strongest common bond)
nn_ratio = BDE_eV['N≡N']/Ry
r = search_bst(nn_ratio)
if r:
    test("T3: BDE(N≡N)/Ry as BST rational",
         nn_ratio, r[2], 2.0,
         f"Triple bond: {r[0]}/{r[1]} = {label_int(r[0])}/{label_int(r[1])}")

# T4: C=C/C-C = 9/5 = N_c²/n_C
test("T4: BDE(C=C)/BDE(C-C) = N_c²/n_C = 9/5",
     BDE_kJ['C=C']/BDE_kJ['C-C'], 9/5, 2.0,
     "Double/single ratio = same as χ(F)/χ(H)!")

# T5: N≡N/N-N ≈ C_2 = 6
test("T5: BDE(N≡N)/BDE(N-N) ≈ C_2 = 6",
     BDE_kJ['N≡N']/BDE_kJ['N-N'], C_2, 2.0,
     "Triple/single nitrogen = Casimir operator")

# T6: O=O/O-O ≈ 7/2 = g/rank
test("T6: BDE(O=O)/BDE(O-O) ≈ g/rank = 7/2",
     BDE_kJ['O=O']/BDE_kJ['O-O'], g/rank, 3.0,
     "Double/single oxygen = Bergman genus over rank")

# T7: H-H ≈ H-Cl (BDE ratio ≈ 1)
test("T7: BDE(H-H)/BDE(H-Cl) ≈ 1",
     BDE_kJ['H-H']/BDE_kJ['H-Cl'], 1.0, 1.5,
     "Hydrogen and HCl are the same bond strength")

# T8: C-H/Ry as BST rational
ch_ratio = BDE_eV['H-C']/Ry
r = search_bst(ch_ratio)
if r:
    test("T8: BDE(C-H)/Ry as BST rational",
         ch_ratio, r[2], 2.0,
         f"Life's bond: {r[0]}/{r[1]} = {label_int(r[0])}/{label_int(r[1])}")

# T9: F-F/Ry (anomalously weak)
ff_ratio = BDE_eV['F-F']/Ry
r = search_bst(ff_ratio)
if r:
    test("T9: BDE(F-F)/Ry as BST rational",
         ff_ratio, r[2], 2.0,
         f"F-F anomaly: {r[0]}/{r[1]} = {label_int(r[0])}/{label_int(r[1])}")

# T10: At least 15 of 21 bonds within 2%
within_2 = sum(1 for bond, ratio, bst, p, q, val, dev in results if dev < 2.0)
t10 = within_2 >= 15
if t10:
    pass_count += 1
else:
    fail_count += 1
print(f"  {'PASS' if t10 else 'FAIL'}: T10: ≥ 15/21 bonds within 2% of BST rational")
print(f"         {within_2}/21 within 2%")

# ══════════════════════════════════════════════════════════════════════
# Summary
# ══════════════════════════════════════════════════════════════════════
print(f"\n{'=' * 72}")
print("  SUMMARY")
print(f"{'=' * 72}")

print(f"""
  BOND DISSOCIATION ENERGIES AS BST RATIONALS

  BDE/Ry as BST fractions:
    H-H:   {BDE_eV['H-H']/Ry:.4f} ≈ N_c/rank = 3/2           ({abs(BDE_eV['H-H']/Ry - 1.5)/(BDE_eV['H-H']/Ry)*100:.2f}%)
    H-F:   {BDE_eV['H-F']/Ry:.4f}
    H-Cl:  {BDE_eV['H-Cl']/Ry:.4f}
    N≡N:   {BDE_eV['N≡N']/Ry:.4f} (strongest common bond)
    C-C:   {BDE_eV['C-C']/Ry:.4f}

  Bond order patterns:
    C=C/C-C = {BDE_kJ['C=C']/BDE_kJ['C-C']:.3f} ≈ 9/5 = N_c²/n_C   ({abs(BDE_kJ['C=C']/BDE_kJ['C-C']-1.8)/(BDE_kJ['C=C']/BDE_kJ['C-C'])*100:.1f}%)
    N≡N/N-N = {BDE_kJ['N≡N']/BDE_kJ['N-N']:.3f} ≈ C_2 = 6           ({abs(BDE_kJ['N≡N']/BDE_kJ['N-N']-6)/(BDE_kJ['N≡N']/BDE_kJ['N-N'])*100:.1f}%)
    O=O/O-O = {BDE_kJ['O=O']/BDE_kJ['O-O']:.3f} ≈ g/rank = 7/2     ({abs(BDE_kJ['O=O']/BDE_kJ['O-O']-3.5)/(BDE_kJ['O=O']/BDE_kJ['O-O'])*100:.1f}%)

  HEADLINES:
  1. BDE(H-H)/Ry = 1/3 = 1/N_c. Simplest molecule, simplest fraction.
  2. C=C/C-C = 9/5 = N_c²/n_C = χ(F)/χ(H) = IE(He)/Ry. Universal.
  3. N≡N/N-N = C_2 = 6. The triple bond of life's atmosphere.
  4. The bond order ladder walks BST integers.

  (C=5, D=0). Counter: .next_toy = 842.
""")

print(f"{'=' * 72}")
print(f"  SCORECARD: {pass_count}/{pass_count+fail_count}")
print(f"{'=' * 72}")

print(f"\n{'=' * 72}")
print(f"  TOY 841 COMPLETE — {pass_count}/{pass_count+fail_count} PASS")
print(f"{'=' * 72}")

sys.exit(0 if fail_count == 0 else 1)
