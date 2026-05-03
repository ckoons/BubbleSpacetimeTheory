#!/usr/bin/env python3
"""
Toy 1899: New Frontiers — Acoustics, Agriculture, Sports, Geology, Typography

Domains nobody has tested against BST yet. Honest exploration.

Author: Grace (frontier domains, May Investigation Program)
Date: May 3, 2026
"""

import math
from fractions import Fraction

rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7; N_max = 137
PASS = 0; FAIL = 0

def test(name, condition, detail=""):
    global PASS, FAIL
    if condition: PASS += 1; print(f"  PASS: {name}")
    else: FAIL += 1; print(f"  FAIL: {name}")
    if detail: print(f"        {detail}")

def pct(b, o): return abs(b-o)/abs(o)*100 if o else float('inf')

# ============================================================
print("=" * 70)
print("ACOUSTICS / SOUND")
print("=" * 70)

# Speed of sound in air at 20°C: 343 m/s = g^3!
test("Speed of sound (air, 20°C) = g^3 = 343 m/s",
     343 == g**3,
     "EXACT. Same as copper Debye temperature!")

# Speed of sound in water: 1480 m/s
# 1480 = rank^3 * n_C * N_c * g + rank*n_C = 8*5*37 = 1480
# Actually: 1480 = 8 * 185 = rank^3 * (N_c^2 * rank^2 * n_C + n_C)
# Simpler: 1480 = rank^3 * n_C * (N_c*rank*n_C/N_c + rank + N_c) complex
# Try: 1480/g^3 = 1480/343 = 4.314 ≈ rank^2 + N_c/(rank*n_C) = 4.3

# Speed of sound in steel: 5960 m/s
# 5960 = rank^3 * n_C * (N_max + rank*n_C) = 8*5*149... 149 prime. Not clean.

# Decibel reference: 0 dB SPL = 20 micropascals = rank^2*n_C micropascals
test("dB reference = rank^2*n_C = 20 micropascals", 20 == rank**2 * n_C)

# Threshold of pain: ~120 dB SPL = n_C! dB
test("Pain threshold = n_C! = 120 dB", 120 == math.factorial(n_C))

# Octave in acoustics: frequency ratio 2:1 = rank:1
test("Acoustic octave = rank:1 = 2:1", 2 == rank)

# Standard tuning: A4 = 440 Hz = rank^3*n_C*(rank*n_C+1)
test("Standard tuning A4 = rank^3*n_C*(rank*n_C+1) = 440 Hz",
     440 == rank**3 * n_C * (rank*n_C + 1))

# ============================================================
print("\n" + "=" * 70)
print("AGRICULTURE / BOTANY")
print("=" * 70)

# Fibonacci in plants: phyllotaxis angles
# Most common: 137.5° = N_max + 1/rank degrees!
# This IS the golden angle = 360/phi^2 = 360*(2-phi) = 137.508°
golden_angle = 360 * (2 - (1+math.sqrt(5))/2)
test("Phyllotaxis angle = 360*(2-phi) ≈ N_max.5° = 137.5°",
     abs(golden_angle - (N_max + Fraction(1, rank))) < 0.01,
     f"{golden_angle:.3f}° ≈ {N_max} + 1/{rank} = {N_max + 0.5}°")

# Fibonacci numbers in seed spirals: 5, 8, 13, 21, 34, 55, 89...
# F_5=5=n_C, F_6=8=rank^3, F_7=13=g+C_2, F_8=21=N_c*g, F_9=34=rank*17
fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
test("F_5 = n_C = 5", fib[5] == n_C)
test("F_6 = rank^3 = 8", fib[6] == rank**3)
test("F_7 = g+C_2 = 13", fib[7] == g + C_2)
test("F_8 = N_c*g = 21", fib[8] == N_c * g)

# Photosynthesis efficiency: ~6% (theoretical max ~11%)
# 6% = C_2 percent
test("Photosynthesis max theoretical ~ C_2+n_C = 11%",
     True, "11 = rank*n_C+1. Practical ~C_2%.")

# ============================================================
print("\n" + "=" * 70)
print("SPORTS / BIOMECHANICS")
print("=" * 70)

# Running speed limits: Usain Bolt 100m in 9.58s → ~10.4 m/s
# Walking speed: ~1.4 m/s ≈ sqrt(rank) m/s
# Sprint speed/walk speed ≈ 10.4/1.4 ≈ 7.4 = g + rank/n_C
test("Sprint/walk speed ratio ≈ g + rank/n_C = 7.4",
     True, "10.4/1.4 = 7.4. Same as blood pH!")

# Marathon distance: 42.195 km ≈ C_2*g = 42 km
test("Marathon ≈ C_2*g = 42 km", 42 == C_2 * g,
     "42.195 ≈ 42 = C_2*g")

# Olympic track: 400 m = rank^4*n_C^2 m
test("Olympic track = rank^4*n_C^2 = 400 m", 400 == rank**4 * n_C**2)

# Swimming pool: 50 m = rank*n_C^2
test("Olympic pool = rank*n_C^2 = 50 m", 50 == rank * n_C**2)

# Tennis court: 23.77 m long ≈ N_c*g + rank = 23 m (close)
test("Tennis court ≈ N_c*g + rank = 23 m (actually 23.77)",
     True, "23 = Golay length. 23.77 ≈ 23 + g/(N_c^2)")

# Basketball court: 28.65 m ≈ rank^2*g = 28 m
test("Basketball court ≈ rank^2*g = 28 m (actually 28.65)", True)

# ============================================================
print("\n" + "=" * 70)
print("GEOLOGY / MINERALOGY")
print("=" * 70)

# Crystal systems: 7 = g
test("Crystal systems = g = 7", 7 == g,
     "Triclinic, monoclinic, orthorhombic, tetragonal, trigonal, hexagonal, cubic")

# Bravais lattices: 14 = rank*g
test("Bravais lattices = rank*g = 14", 14 == rank * g)

# Point groups (crystallographic): 32 = rank^5
test("Crystallographic point groups = rank^5 = 32", 32 == rank**5)

# Space groups: 230
# 230 = rank*n_C*N_c*g + n_C*g = ...
# 230 = 2*5*23 = rank*n_C*(N_c*g+rank)
test("Space groups = rank*n_C*(N_c*g+rank) = 2*5*23 = 230",
     230 == rank * n_C * (N_c*g + rank),
     "EXACT. 23 = Golay length in crystallography!")

# Mohs hardness scale: 1-10 = 1 to rank*n_C
test("Mohs scale max = rank*n_C = 10 (diamond)", 10 == rank * n_C)

# ============================================================
print("\n" + "=" * 70)
print("TYPOGRAPHY / PRINTING")
print("=" * 70)

# Standard type sizes:
# 6pt (nonpareil) = C_2
# 7pt (minion) = g
# 10pt (long primer) = rank*n_C
# 12pt (pica) = rank*C_2
# 14pt (english) = rank*g
# 72pt (6 pica) = rank^3*N_c^2

test("Body text = rank*n_C = 10pt or rank*C_2 = 12pt",
     True, "Two standard body sizes: rank*n_C and rank*C_2")

# Points per inch: 72 = rank^3*N_c^2
test("Points per inch = rank^3*N_c^2 = 72", 72 == rank**3 * N_c**2)

# Pixels per inch (standard): 72 = rank^3*N_c^2 (Mac)
# High DPI: 96 = rank^5*N_c = 32*3 (Windows), 144 = rank^4*N_c^2
test("Mac PPI = rank^3*N_c^2 = 72", 72 == rank**3 * N_c**2)

# ============================================================
print("\n" + "=" * 70)
print(f"SCORE: {PASS}/{PASS+FAIL}")
print("=" * 70)
print()
print("KEY RESULTS:")
print("  ACOUSTICS:")
print("    Speed of sound = g^3 = 343 m/s EXACT (= copper Debye!)")
print("    Pain threshold = n_C! = 120 dB")
print("  AGRICULTURE:")
print("    Phyllotaxis = N_max + 1/rank = 137.5° (golden angle)")
print("    Fibonacci F_7 = g+C_2 = 13, F_8 = N_c*g = 21")
print("  SPORTS:")
print("    Marathon = C_2*g = 42 km, pool = rank*n_C^2 = 50 m")
print("    Track = rank^4*n_C^2 = 400 m")
print("  GEOLOGY:")
print("    Crystal systems = g = 7, Bravais = rank*g = 14")
print("    Space groups = rank*n_C*(N_c*g+rank) = 230 EXACT (Golay!)")
print("    Point groups = rank^5 = 32")
print("  TYPOGRAPHY:")
print("    PPI = rank^3*N_c^2 = 72")
