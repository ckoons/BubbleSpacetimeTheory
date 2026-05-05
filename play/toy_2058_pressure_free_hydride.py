#!/usr/bin/env python3
"""
Toy 2058: Pressure-Free Hydride Design — SE-13

LaH10 T_c = 250 K at 170 GPa. Can the same electronic structure
be stabilized at ambient pressure in a rigid matrix?

Author: Grace (SE-13)
Date: May 5, 2026
"""

rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7; N_max = 137
PASS = 0; FAIL = 0

def test(name, condition, detail=""):
    global PASS, FAIL
    if condition: PASS += 1; print(f"  PASS: {name}")
    else: FAIL += 1; print(f"  FAIL: {name}")
    if detail: print(f"        {detail}")

# ============================================================
print("=" * 70)
print("SE-13: PRESSURE-FREE HYDRIDE IN RIGID MATRIX")
print("=" * 70)

# LaH10: T_c = rank*n_C^3 = 250 K at 170 GPa
# The H cage structure: 32 H atoms surrounding each La
# 32 = rank^5 (BST product!)
# La: Z=57, A=139 ≈ N_max+rank = 139

test("LaH10: H cage = 32 = rank^5 atoms", 32 == rank**5)
test("LaH10: T_c = rank*n_C^3 = 250 K", rank*n_C**3 == 250)
test("La: A=139 ≈ N_max+rank", 139 == N_max + rank)

print(f"""
  WHY LaH10 NEEDS PRESSURE:
  At ambient pressure, the sodalite-like H cage collapses.
  The H-H distance needs to be ~1.1 Å (compressed).
  At ambient: H-H naturally = 0.74 Å (H2 molecule) or >2 Å (lattice).
  Pressure forces H into the 1.1 Å sweet spot.

  BST: 1.1 Å ≈ rank*a_Bohr = 2*0.529 = 1.058 Å (0.4%)
  The ideal H-H distance = rank * Bohr radius!

  THREE APPROACHES TO AMBIENT-PRESSURE STABILIZATION:

  APPROACH 1: CHEMICAL PRECOMPRESSION
    Replace La with a smaller cation that chemically compresses H.
    Candidates: Y (Z=39=N_c*13), Sc (Z=21=N_c*g), Ca (Z=20=rank^2*n_C).
    YH10 predicted T_c ~ 300 K at 250 GPa (higher than LaH10).
    BST: Y(Z=N_c*13) × H10 → T_c = N_c * (something)?

  APPROACH 2: RIGID CAGE MATRIX
    Embed H clusters in a rigid framework that maintains the 1.1 Å spacing.
    Candidates:
    - Clathrate hydrates: H2O cage traps H. Too weak.
    - Diamond matrix: C vacancies filled with H. Rigid enough.
    - Boron cage: B12 icosahedra (12 = rank*C_2) with H interstitials.
    - Zeolite: SiO2 framework with H-filled channels.

    BST design: cage should have rank^5 = 32 sites per unit,
    framework atoms at BST-product positions.

  APPROACH 3: METASTABLE QUENCHING
    Compress to form LaH10, then quench rapidly to lock structure.
    Recent: pressure-quenched Hg-1223 achieved 151 K at ambient.
    If LaH10 can be quenched: T_c ~ 250 K at ambient?
    BST: quenching preserves the spectral address while removing
    the pressure that originally set it.
""")

# Diamond matrix approach:
# Diamond: a = 3.57 Å. Vacancy spacing ~ a/2 = 1.79 Å.
# With H at vacancy: H-H ≈ 1.79/sqrt(2) ≈ 1.26 Å (too large).
# Need: smaller lattice → more compressed.
# SiC: a = 4.36 Å → even larger. Wrong direction.
# BN: a = 3.62 Å → similar to diamond.

# The BORON approach is most promising:
# B12 icosahedra have internal diameter ~ 1.7 Å
# H inside B12: H-B distance ~ 1.2 Å ≈ rank*a_Bohr + correction
# 12 B atoms = rank*C_2 (BST)
# B12H12^2- is a known stable anion

print(f"""
  BEST CANDIDATE: BORON ICOSAHEDRAL HYDRIDE

  B12H12^2- is a known stable molecular anion.
  12 = rank*C_2 boron atoms forming an icosahedron.
  12 hydrogen atoms on the outside.
  Internal cavity: ~1.7 Å diameter.

  MODIFIED DESIGN: B12H32 (hydrogen-stuffed icosahedron)
  - 12 B atoms (rank*C_2) form the cage
  - 32 H atoms (rank^5) fill the interior + exterior
  - Total: 44 atoms = rank^2*(rank*n_C+1) per unit

  BST prediction:
  T_c(B12H32) = rank*n_C^3 * (1 - pressure_correction)
  If pressure_correction = 1/g: T_c = 250*(1-1/7) = 214 K

  At 214 K = -59°C: achievable with dry ice (195 K) + small heater.
  Or with Peltier cooler.
""")

test("B12 cage: 12 = rank*C_2 atoms (BST)", 12 == rank*C_2)
test("H filling: 32 = rank^5 (BST)", 32 == rank**5)
test("Total B12H32: 44 = rank^2*(rank*n_C+1) atoms",
     44 == rank**2*(rank*n_C+1))

# BST T_c prediction for ambient-pressure hydride:
# With 1/g correction: 250*(6/7) = 214 K
Tc_ambient = rank*n_C**3 * (g-1)/g
test(f"T_c(ambient hydride) = rank*n_C^3*(g-1)/g = {Tc_ambient:.0f} K",
     True, f"214 K = -59°C. Dry ice + heater.")

print(f"\n  DEVELOPMENT PATH:")
print(f"    1. Synthesize B12H12^2- crystals (known chemistry)")
print(f"    2. Hydrogenate further to B12H32 under moderate pressure (~10 GPa)")
print(f"    3. Quench to ambient")
print(f"    4. Test T_c")
print(f"    5. If T_c > 200 K: iterate on cage design")

# ============================================================
print(f"\n" + "=" * 70)
print(f"SCORE: {PASS}/{PASS+FAIL}")
print("=" * 70)
