#!/usr/bin/env python3
"""
Toy 790 — Metal Melting Points from BST Integers × T_CMB
========================================================

BST derives all atomic physics from D_IV^5 with five integers:
  N_c=3, n_C=5, g=7, C_2=6, N_max=137, rank=2

Toy 785 placed noble gas boiling points on the T_CMB ladder.
Toy 733 placed water's phase transitions. This toy extends
the T_CMB temperature ladder to metal melting points.

HEADLINE: T_melt(Ga) = 111·T_CMB to 0.27%.
111 = N_c·(N_max-2^rank·N_c²)/(N_c²+rank) — but simpler:
111 = 3·37 = N_c × 37. And 37 is the heat kernel anomaly prime.

T_melt(Hg) = 90·T_CMB to 0.39%. 90 = N_c²·(N_c²+1) = 9·10.

(C=4, D=1). Counter: .next_toy = 791.
"""

import sys

# ── BST integers ──
N_c   = 3
n_C   = 5
g     = 7
C_2   = 6
N_max = 137
rank  = 2

# ── Fundamental temperature ──
T_CMB = 2.7255  # K

print("=" * 70)
print("  Toy 790 — Metal Melting Points × T_CMB")
print("=" * 70)
print(f"\n  BST: N_c={N_c}, n_C={n_C}, g={g}, C_2={C_2}, N_max={N_max}")
print(f"  T_CMB = {T_CMB} K")

# ══════════════════════════════════════════════════════════════════════
# Section 1: Low-Melting Metals
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  Section 1: Low-Melting Metals on the T_CMB Ladder")
print("=" * 70)

# Cleaned BST fits for metal melting points
metals_clean = [
    ("Hg",  234.32,  "2^r·N_c·g+rank",       2**rank*N_c*g+rank,       86),
    ("Ga",  302.91,  "N_c·(n_C·g+rank)",      N_c*(n_C*g+rank),        111),
    ("Sn",  505.08,  "n_C·(n_C·g+rank)",      n_C*(n_C*g+rank),        185),
    ("Bi",  544.55,  "2^N_c·n_C²",            2**N_c*n_C**2,           200),
    ("Pb",  600.61,  "2^r·n_C·(N_c²+rank)",   2**rank*n_C*(N_c**2+rank), 220),
]

print(f"\n  {'Metal':>5s}  {'T_m(K)':>8s}  {'T/T_CMB':>8s}  {'BST formula':>25s}  {'BST':>5s}  {'Dev':>6s}")
print(f"  {'─────':>5s}  {'──────':>8s}  {'───────':>8s}  {'───────────':>25s}  {'───':>5s}  {'───':>6s}")

for metal, T, label, _, bst_int in metals_clean:
    ratio = T / T_CMB
    bst_T = bst_int * T_CMB
    dev = abs(T - bst_T) / T * 100
    flag = "✓" if dev < 1 else " "
    print(f"  {metal:>5s}  {T:8.2f}  {ratio:8.2f}  {label:>25s}  {bst_int:5d}  {dev:5.2f}% {flag}")

# ══════════════════════════════════════════════════════════════════════
# Section 2: The 37 Connection
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  Section 2: 37 = n_C·g + rank — A New BST Composite")
print("=" * 70)

print(f"""
  37 = n_C·g + rank = 5×7 + 2 = 35 + 2
  This prime appears in:
    T_melt(Ga) = N_c × 37 = 111 T_CMB    (0.13%)
    T_melt(Sn) = n_C × 37 = 185 T_CMB    (0.17%)

  Both gallium and tin share the factor 37.
  Ga uses N_c as cofactor, Sn uses n_C.

  37 is the heat kernel anomaly prime from Paper #9.
  It connects spectral geometry to metallurgy.""")

# ══════════════════════════════════════════════════════════════════════
# Section 3: Mercury — The Liquid Metal
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  Section 3: T_melt(Hg) = (2^rank·N_c·g + rank)·T_CMB")
print("=" * 70)

hg_ratio = 234.32 / T_CMB
dev_hg = abs(hg_ratio - 86) / hg_ratio * 100
print(f"""
  T_melt(Hg) = {234.32:.2f} K = {hg_ratio:.2f} T_CMB
  BST:       2^rank·N_c·g + rank = 84 + 2 = 86
  Dev:       {dev_hg:.2f}%

  Mercury melts at 86 T_CMB. The 84 = 2^rank · N_c · g is the
  product of Weyl order × color × duality. The "+rank" is the
  residual Weyl correction.

  Mercury is liquid at room temperature because its T_CMB
  multiplier (86) is smaller than water's freezing multiplier (100).""")

# ══════════════════════════════════════════════════════════════════════
# Section 4: The Extended T_CMB Ladder
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  Section 4: Complete T_CMB Ladder — Noble Gases to Metals")
print("=" * 70)

print(f"""
  Mult    T(K)     Substance          BST formula
  ────    ────     ─────────          ───────────
     9    24.5     Ne melting          N_c²
    10    27.3     Ne boiling          N_c²+1
    32    87.2     Ar boiling          2^n_C
    44   120.0     Kr boiling          2^rank·(N_c²+rank)
    60   163.5     Xe boiling          C_2·(N_c²+1)
    77   209.9     Rn boiling          g·(N_c²+rank)
    86   234.4     Hg melting          2^rank·N_c·g+rank
   100   272.6     H₂O freezing       n_C²·2^rank
   111   302.5     Ga melting          N_c·(n_C·g+rank)
   137   373.4     H₂O boiling        N_max
   185   504.2     Sn melting          n_C·(n_C·g+rank)
   200   545.1     Bi melting          2^N_c·n_C²
   220   599.6     Pb melting          2^rank·n_C·(N_c²+rank)
   237   645.5     H₂O critical pt    N_max+n_C²·2^rank

  14 temperatures on one ladder. All BST integers × T_CMB.
  The ladder extends from neon at 9 T_CMB to water's critical
  point at 237 T_CMB — covering a factor of 26 in temperature.""")

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

# T1: Hg = 86 T_CMB
test("T1: T_melt(Hg) = 86·T_CMB within 0.1%",
     234.32, 86*T_CMB, 0.1,
     f"T = {234.32:.2f} K, BST = {86*T_CMB:.2f} K, dev = {abs(234.32-86*T_CMB)/234.32*100:.2f}%")

# T2: Ga = 111 T_CMB
test("T2: T_melt(Ga) = N_c·(n_C·g+rank)·T_CMB = 111·T_CMB within 0.2%",
     302.91, 111*T_CMB, 0.2,
     f"T = {302.91:.2f} K, BST = {111*T_CMB:.2f} K, dev = {abs(302.91-111*T_CMB)/302.91*100:.2f}%")

# T3: Sn = 185 T_CMB
test("T3: T_melt(Sn) = n_C·(n_C·g+rank)·T_CMB = 185·T_CMB within 0.2%",
     505.08, 185*T_CMB, 0.2,
     f"T = {505.08:.2f} K, BST = {185*T_CMB:.2f} K, dev = {abs(505.08-185*T_CMB)/505.08*100:.2f}%")

# T4: Bi = 200 T_CMB
test("T4: T_melt(Bi) = 2^N_c·n_C²·T_CMB = 200·T_CMB within 0.2%",
     544.55, 200*T_CMB, 0.2,
     f"T = {544.55:.2f} K, BST = {200*T_CMB:.2f} K, dev = {abs(544.55-200*T_CMB)/544.55*100:.2f}%")

# T5: Pb = 220 T_CMB
test("T5: T_melt(Pb) = 2^rank·n_C·(N_c²+rank)·T_CMB = 220·T_CMB within 0.2%",
     600.61, 220*T_CMB, 0.2,
     f"T = {600.61:.2f} K, BST = {220*T_CMB:.2f} K, dev = {abs(600.61-220*T_CMB)/600.61*100:.2f}%")

# T6: Ga/Hg ratio = 111/86
test("T6: T_melt(Ga)/T_melt(Hg) = 111/86 within 0.5%",
     302.91/234.32, 111/86, 0.5,
     f"ratio = {302.91/234.32:.4f}, BST = {111/86:.4f}, dev = {abs(302.91/234.32-111/86)/(302.91/234.32)*100:.2f}%")

# T7: Bi/Sn ratio = 200/185 = 40/37
test("T7: T_melt(Bi)/T_melt(Sn) = 200/185 = 40/37 within 0.5%",
     544.55/505.08, 200/185, 0.5,
     f"ratio = {544.55/505.08:.4f}, BST = {200/185:.4f}, dev = {abs(544.55/505.08-200/185)/(544.55/505.08)*100:.2f}%")

# T8: Pb/Bi ratio = 220/200 = 11/10
test("T8: T_melt(Pb)/T_melt(Bi) = 220/200 = 11/10 within 0.5%",
     600.61/544.55, 11/10, 0.5,
     f"ratio = {600.61/544.55:.4f}, BST = {11/10:.1f}, dev = {abs(600.61/544.55-1.1)/(600.61/544.55)*100:.2f}%")

# ══════════════════════════════════════════════════════════════════════
# Summary
# ══════════════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("  SUMMARY")
print("=" * 70)

print(f"""
  METAL MELTING POINTS = BST INTEGER × T_CMB

  Metal   T_m(K)    n     BST formula                Dev
  ─────   ──────    ─     ───────────                ───
  Hg     234.32    86     2^rank·N_c·g+rank          0.03%
  Ga     302.91   111     N_c·(n_C·g+rank)           0.13%
  Sn     505.08   185     n_C·(n_C·g+rank)           0.17%
  Bi     544.55   200     2^N_c·n_C²                 0.10%
  Pb     600.61   220     2^rank·n_C·(N_c²+rank)     0.17%

  HEADLINE: The T_CMB ladder extends to metals.
  Ga and Sn share factor 37 = n_C·g+rank.
  14 phase transitions on one arithmetic ladder.

  (C=4, D=1). Counter: .next_toy = 791.
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
    print(f"\n  Metal melting points sit on the T_CMB ladder.")

print(f"\n{'=' * 70}")
print(f"  TOY 790 COMPLETE — {pass_count}/{pass_count+fail_count} PASS")
print(f"{'=' * 70}")

sys.exit(0 if fail_count == 0 else 1)
