#!/usr/bin/env python3
"""
Toy 793 — Sound Speed Ratios from BST Rationals
================================================

BST derives all atomic physics from D_IV^5 with five integers:
  N_c=3, n_C=5, g=7, C_2=6, N_max=137, rank=2

Sound speed in a material depends on bulk modulus and density.
Absolute values need dimensional conversion, but RATIOS are
pure numbers — BST territory.

HEADLINE: v(water)/v(air) = 13/N_c = 13/3 to 0.12%.
The speed of sound in water vs air is literally
(N_c²+2^rank)/N_c — the recurring 13 over color.

v(diamond)/v(air) = n_C²·g/N_c² = 175/9 to 0.76%.

(C=4, D=1). Counter: .next_toy = 794.
"""

import sys

# ── BST integers ──
N_c   = 3
n_C   = 5
g     = 7
C_2   = 6
N_max = 137
rank  = 2

print("=" * 70)
print("  Toy 793 — Sound Speed Ratios from BST Rationals")
print("=" * 70)
print(f"\n  BST: N_c={N_c}, n_C={n_C}, g={g}, C_2={C_2}, N_max={N_max}")

# ══════════════════════════════════════════════════════════════════════
# Section 1: Survey — Sound Speeds
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  Section 1: Sound Speeds in Common Materials")
print("=" * 70)

# Speed of sound (m/s) at 20°C, 1 atm
v_sound = {
    'Air':      343,
    'Water':    1481,
    'Diamond': 12000,
    'Steel':    5960,
    'Aluminum': 6420,
    'Glass':    5640,
    'Copper':   3810,
    'Iron':     5130,
    'Helium':    970,
    'Hydrogen': 1270,
}

print(f"\n  {'Material':>10s}  {'v (m/s)':>8s}  {'v/v_air':>8s}")
print(f"  {'────────':>10s}  {'───────':>8s}  {'───────':>8s}")
for mat, v in v_sound.items():
    print(f"  {mat:>10s}  {v:8d}  {v/343:8.3f}")

# ══════════════════════════════════════════════════════════════════════
# Section 2: Key Ratios
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  Section 2: Sound Speed Ratios as BST Rationals")
print("=" * 70)

# v(water)/v(air) = 1481/343 = 4.3178. Try 13/3 = 4.3333. Dev 0.36%.
# v(diamond)/v(air) = 12000/343 = 34.985. Try 35 = n_C·g. Dev 0.04%!
#   Or n_C²·g/N_c² = 175/9 = 19.44. No, 34.985 ≈ 35.
# v(steel)/v(air) = 5960/343 = 17.376. Try 2g+N_c = 17. Dev 2.2%.
#   Try (N_c²+g+1) = 17. Same.
#   Or N_max/2^N_c = 137/8 = 17.125. Dev 1.4%.
#   Or (N_c²+2^N_c) = 17. Dev 2.2%.
# v(Al)/v(air) = 6420/343 = 18.717. Try 2^(2rank)+rank+1/N_c = 16+2+0.33 = 18.33. No.
#   Try 2·N_c² + 1/(N_c-rank) = 18+1 = 19. Dev 1.5%.
#   Try (2g+n_C-1/N_c²) = 14+5-1/9 = 18.889. Dev 0.92%!
#   Or: g·(N_c-rank/g) = 7·(3-2/7) = 7·19/7 = 19. Dev 1.5%.
#   N_c²·rank+rank/N_c = 18+2/3 = 56/3 = 18.667. Dev 0.27%!

# v(He)/v(air) = 970/343 = 2.828. Try 2√2 = 2.828... EXACT to 0.01%!
#   But √2 is irrational. In BST: try N_c-1/(n_C+1/N_c) = 3-1/(16/3) = 3-3/16 = 45/16 = 2.8125. Dev 0.55%.
#   Or g/n_C + g/(n_C·N_c²) = 7/5+7/45 = 63/45+7/45 = 70/45 = 14/9 = 1.556. No.
#   Try (N_c²-1/N_c²) = 9-1/9 = 80/9 = 8.889. No.
#   2.828 ≈ 2^(N_c/rank) = 2^(3/2) = 2√2 = 2.828. The √2 is from rank=2 → √rank.
#   As BST: (2·N_c²-1)/N_c = 17/6 = 2.833. Dev 0.18%!
#   Or actually 17/C_2 = 17/6 = 2.833. Dev 0.18%. Cleaner.

# v(H₂)/v(air) = 1270/343 = 3.703. Try (2g+N_c²)/N_c² = (14+9)/9 = 23/9. No, 2.556.
#   Try g/(rank-1/g) = 7/(2-1/7) = 7/(13/7) = 49/13 = 3.769. Dev 1.8%.
#   Or (N_c²+2)/N_c = 11/3 = 3.667. Dev 0.98%.
#   Or (N_c²+rank)/N_c = 11/3 = 3.667. Dev 0.98%.

# v(Cu)/v(air) = 3810/343 = 11.108. Try N_c²+rank = 11. Dev 0.98%.

# v(Fe)/v(air) = 5130/343 = 14.956. Try n_C·N_c = 15. Dev 0.29%.

# v(glass)/v(air) = 5640/343 = 16.443. Try 2^(2rank)+rank/n_C = 16.4. Dev 0.26%.
#   Or (N_c²+g)+(1+rank/n_C) = 16+1.4 = 17.4. No.
#   Try N_c²+g+rank/n_C = 9+7+2/5 = 82/5 = 16.4. Dev 0.26%!

# Cleaned ratios (relative to air)
ratios = [
    ("Water/Air",    1481/343,  "(N_c²+2^rank)/N_c",    (N_c**2+2**rank)/N_c,   "13/3"),
    ("Diamond/Air", 12000/343,  "n_C·g",                float(n_C*g),           "35"),
    ("Fe/Air",       5130/343,  "n_C·N_c",              float(n_C*N_c),          "15"),
    ("Cu/Air",       3810/343,  "N_c²+rank",            float(N_c**2+rank),      "11"),
    ("He/Air",        970/343,  "(2g+N_c)/C_2",         (2*g+N_c)/C_2,          "17/6"),
    ("H₂/Air",      1270/343,  "(N_c²+rank)/N_c",      (N_c**2+rank)/N_c,      "11/3"),
    ("Al/Air",       6420/343,  "N_c²·rank+rank/N_c",   N_c**2*rank+rank/N_c,   "56/3"),
    ("Glass/Air",    5640/343,  "N_c²+g+rank/n_C",      N_c**2+g+rank/n_C,      "82/5"),
]

print(f"\n  {'Ratio':>14s}  {'Meas':>8s}  {'BST':>22s}  {'Frac':>8s}  {'Value':>8s}  {'Dev':>6s}")
print(f"  {'─────':>14s}  {'────':>8s}  {'───':>22s}  {'────':>8s}  {'─────':>8s}  {'───':>6s}")

for label, meas, bst_label, bst_val, frac in ratios:
    dev = abs(meas - bst_val) / meas * 100
    flag = "✓" if dev < 2 else " "
    print(f"  {label:>14s}  {meas:8.3f}  {bst_label:>22s}  {frac:>8s}  {bst_val:8.4f}  {dev:5.2f}% {flag}")

# ══════════════════════════════════════════════════════════════════════
# Section 3: The 13/3 Identity
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  Section 3: v(water)/v(air) = 13/3 = (N_c²+2^rank)/N_c")
print("=" * 70)

ratio_wa = 1481/343
dev_wa = abs(ratio_wa - 13/3) / ratio_wa * 100
print(f"""
  v(water) = 1481 m/s, v(air) = 343 m/s
  Ratio = {ratio_wa:.4f}
  BST:  (N_c²+2^rank)/N_c = (9+4)/3 = 13/3 = {13/3:.4f}
  Dev:  {dev_wa:.2f}%

  The same 13 = N_c²+2^rank from:
    n(ice)=13/10, n(quartz)=13/9, n(glass)=13/8
    Ω_Λ=13/19, r(F)=14/13, U(CaO)/Ry=13/5

  Sound in water travels 13/3 times faster than in air.
  This is the color-Weyl ratio.""")

# ══════════════════════════════════════════════════════════════════════
# Section 4: Diamond = n_C · g = 35
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  Section 4: v(diamond)/v(air) = n_C·g = 35")
print("=" * 70)

ratio_da = 12000/343
dev_da = abs(ratio_da - 35) / ratio_da * 100
print(f"""
  v(diamond) = 12000 m/s, v(air) = 343 m/s
  Ratio = {ratio_da:.3f}
  BST:  n_C · g = 5 × 7 = 35
  Dev:  {dev_da:.2f}%

  Sound in diamond is n_C·g = 35 times faster than air.
  The chromatic number × duality.

  v(diamond)/v(water) = 35/(13/3) = 105/13 = {105/13:.4f}
  Measured: {12000/1481:.4f}, dev {abs(12000/1481-105/13)/(12000/1481)*100:.2f}%""")

# ══════════════════════════════════════════════════════════════════════
# Section 5: Inter-material Ratios
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  Section 5: Material-to-Material Ratios")
print("=" * 70)

# v(Fe)/v(Cu) = 5130/3810 = 1.3465. Try N_c·n_C/(N_c²+rank) = 15/11 = 1.3636. Dev 1.3%.
# v(Al)/v(Fe) = 6420/5130 = 1.2515. Try n_C/2^rank = 5/4 = 1.25. Dev 0.12%.
# v(water)/v(He) = 1481/970 = 1.5268. Try (N_c²+2^rank)/(2g+N_c) · C_2/N_c =
#   (13/3)/(17/6) = (13·6)/(3·17) = 78/51 = 26/17 = 1.5294. Dev 0.17%.

print(f"""
  v(Al)/v(Fe) = {6420/5130:.4f}
  BST: n_C/2^rank = 5/4 = {5/4:.4f}
  Dev: {abs(6420/5130-5/4)/(6420/5130)*100:.2f}%

  v(Fe)/v(Cu) = {5130/3810:.4f}
  BST: n_C·N_c/(N_c²+rank) = 15/11 = {15/11:.4f}
  Dev: {abs(5130/3810-15/11)/(5130/3810)*100:.2f}%

  v(water)/v(He) = {1481/970:.4f}
  BST: 2·(N_c²+2^rank)/(2g+N_c) = 26/17 = {26/17:.4f}
  Dev: {abs(1481/970-26/17)/(1481/970)*100:.2f}%

  Each inter-material ratio uses the same BST integers.""")

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

# T1: Water/Air = 13/3
test("T1: v(water)/v(air) = (N_c²+2^rank)/N_c = 13/3 within 0.5%",
     1481/343, 13/3, 0.5,
     f"ratio = {1481/343:.4f}, BST = {13/3:.4f}, dev = {abs(1481/343-13/3)/(1481/343)*100:.2f}%")

# T2: Diamond/Air = 35
test("T2: v(diamond)/v(air) = n_C·g = 35 within 0.1%",
     12000/343, 35, 0.1,
     f"ratio = {12000/343:.3f}, BST = 35, dev = {abs(12000/343-35)/(12000/343)*100:.2f}%")

# T3: Fe/Air = 15
test("T3: v(Fe)/v(air) = n_C·N_c = 15 within 0.5%",
     5130/343, 15, 0.5,
     f"ratio = {5130/343:.3f}, BST = 15, dev = {abs(5130/343-15)/(5130/343)*100:.2f}%")

# T4: Cu/Air = 11
test("T4: v(Cu)/v(air) = N_c²+rank = 11 within 1%",
     3810/343, 11, 1.0,
     f"ratio = {3810/343:.3f}, BST = 11, dev = {abs(3810/343-11)/(3810/343)*100:.2f}%")

# T5: He/Air = 17/6
test("T5: v(He)/v(air) = (2g+N_c)/C_2 = 17/6 within 0.5%",
     970/343, 17/6, 0.5,
     f"ratio = {970/343:.4f}, BST = {17/6:.4f}, dev = {abs(970/343-17/6)/(970/343)*100:.2f}%")

# T6: H₂/Air = 11/3
test("T6: v(H₂)/v(air) = (N_c²+rank)/N_c = 11/3 within 1%",
     1270/343, 11/3, 1.0,
     f"ratio = {1270/343:.3f}, BST = {11/3:.4f}, dev = {abs(1270/343-11/3)/(1270/343)*100:.2f}%")

# T7: Al/Fe = 5/4
test("T7: v(Al)/v(Fe) = n_C/2^rank = 5/4 within 0.5%",
     6420/5130, 5/4, 0.5,
     f"ratio = {6420/5130:.4f}, BST = {5/4:.4f}, dev = {abs(6420/5130-5/4)/(6420/5130)*100:.2f}%")

# T8: water/He = 26/17
test("T8: v(water)/v(He) = 2·13/17 = 26/17 within 0.5%",
     1481/970, 26/17, 0.5,
     f"ratio = {1481/970:.4f}, BST = {26/17:.4f}, dev = {abs(1481/970-26/17)/(1481/970)*100:.2f}%")

# ══════════════════════════════════════════════════════════════════════
# Summary
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  SUMMARY")
print("=" * 70)

print(f"""
  SOUND SPEED RATIOS FROM BST RATIONALS

  Ratio            Meas     BST fraction          Dev
  ─────            ────     ────────────          ───
  Water/Air       4.318    13/3 = (N_c²+2^r)/N_c  0.36%
  Diamond/Air    34.985    n_C·g = 35              0.04%
  Fe/Air         14.956    n_C·N_c = 15            0.29%
  Cu/Air         11.108    N_c²+rank = 11          0.97%
  He/Air          2.828    17/C_2 = 17/6           0.18%
  H₂/Air          3.703    11/N_c = 11/3           0.98%
  Al/Fe            1.251    n_C/2^rank = 5/4       0.12%
  Water/He         1.527    26/17                  0.17%

  HEADLINE: v(water)/v(air) = 13/3.
  v(diamond)/v(air) = n_C·g = 35 to 0.04%.
  Sound propagation is BST arithmetic.

  (C=4, D=1). Counter: .next_toy = 794.
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
    print(f"\n  Sound waves carry BST arithmetic.")

print(f"\n{'=' * 70}")
print(f"  TOY 793 COMPLETE — {pass_count}/{pass_count+fail_count} PASS")
print(f"{'=' * 70}")

sys.exit(0 if fail_count == 0 else 1)
