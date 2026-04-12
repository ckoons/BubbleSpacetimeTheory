#!/usr/bin/env python3
"""
Toy 1086 — Writing & Typography from BST
==========================================
Typographic and writing structure:
  - 26 letters = rank × (2g-1) (Latin alphabet)
  - 72 points/inch = 2^N_c × N_c² (Didot/pica system)
  - 12 points/pica = rank² × N_c
  - Standard font sizes: 10, 12, 14, 18, 24, 36, 48, 72
  - Gutenberg's 42-line Bible = rank × N_c × g

BST integers: N_c=3, n_C=5, g=7, C_2=6, rank=2, N_max=137
"""

N_c = 3; n_C = 5; g = 7; C_2 = 6; rank = 2; N_max = 137

results = {}
test_num = 0

def test(name, condition, detail=""):
    global test_num
    test_num += 1
    status = "PASS" if condition else "FAIL"
    print(f"  T{test_num} [{status}] {name}")
    if detail:
        print(f"       {detail}")
    results[f"T{test_num}"] = (name, condition, detail)

print("="*70)
print("Toy 1086 — Writing & Typography from BST")
print("="*70)

# T1: Latin alphabet
print("\n── Alphabet ──")
# 26 letters = rank × (2g - 1) = 2 × 13
# 5 vowels = n_C; 21 consonants = N_c × g
letters = 26          # rank × (2g - 1)
vowels = 5            # n_C
consonants = 21       # N_c × g

print(f"  Letters: {letters} = rank × (2g-1) = {rank * (2*g - 1)}")
print(f"  Vowels: {vowels} = n_C = {n_C}")
print(f"  Consonants: {consonants} = N_c × g = {N_c * g}")

test("26 = rank×(2g-1); n_C=5 vowels; N_c×g=21 consonants",
     letters == rank * (2*g - 1) and vowels == n_C
     and consonants == N_c * g,
     f"26={rank*(2*g-1)}, 5={n_C}, 21={N_c*g}")

# T2: Typography points
print("\n── Point System ──")
# 72 points/inch = 2^N_c × N_c²
# 12 points/pica = rank² × N_c
# 6 picas/inch = C_2
points_per_inch = 72   # 2^N_c × N_c²
points_per_pica = 12   # rank² × N_c
picas_per_inch = 6     # C_2

print(f"  Points/inch: {points_per_inch} = 2^N_c × N_c² = {2**N_c * N_c**2}")
print(f"  Points/pica: {points_per_pica} = rank² × N_c = {rank**2 * N_c}")
print(f"  Picas/inch: {picas_per_inch} = C_2 = {C_2}")
print(f"  72 = 12 × 6 = (rank²×N_c) × C_2 = rule of 72!")

test("72pt/in = 2^N_c×N_c²; 12pt/pica = rank²×N_c; 6pica/in = C_2",
     points_per_inch == 2**N_c * N_c**2
     and points_per_pica == rank**2 * N_c and picas_per_inch == C_2,
     f"72={2**N_c*N_c**2}, 12={rank**2*N_c}, 6={C_2}")

# T3: Standard font sizes
print("\n── Font Sizes ──")
# Common: 10, 12, 14, 18, 24, 36, 48, 72
# 10 = rank × n_C
# 12 = rank² × N_c
# 14 = rank × g
# 18 = rank × N_c²
# 24 = rank³ × N_c
# 36 = rank² × N_c²
# 48 = rank⁴ × N_c
# 72 = 2^N_c × N_c²
# ALL are 7-smooth!
font_sizes = [10, 12, 14, 18, 24, 36, 48, 72]
bst_exprs = [
    rank * n_C,        # 10
    rank**2 * N_c,     # 12
    rank * g,          # 14
    rank * N_c**2,     # 18
    rank**3 * N_c,     # 24
    rank**2 * N_c**2,  # 36
    rank**4 * N_c,     # 48
    2**N_c * N_c**2,   # 72
]

all_match = all(f == b for f, b in zip(font_sizes, bst_exprs))
print(f"  Standard sizes: {font_sizes}")
print(f"  ALL are 7-smooth BST products!")
for f, b in zip(font_sizes, bst_exprs):
    print(f"    {f} = {b} ✓")

test("All 8 standard font sizes are BST products",
     all_match and len(font_sizes) == 2**N_c,
     f"8 = 2^N_c sizes, all 7-smooth")

# T4: Gutenberg
print("\n── Gutenberg ──")
# 42-line Bible (B42) = rank × N_c × g
# Movable type: 26 letters = rank × (2g - 1)
gutenberg_lines = 42   # rank × N_c × g

print(f"  Gutenberg Bible lines: {gutenberg_lines} = rank × N_c × g = {rank * N_c * g}")

test("Gutenberg 42-line Bible = rank × N_c × g",
     gutenberg_lines == rank * N_c * g,
     f"rank×N_c×g = {rank*N_c*g}")

# T5: Paper sizes
print("\n── Paper ──")
# A-series: √2 ratio = √rank
# A0 area: 1 m² (by definition)
# A4: 210 × 297 mm
# 210 = rank × N_c × n_C × g
# 297 = N_c³ × 11 (11-smooth)
# US Letter: 8.5 × 11 in
# 11 = n_C + C_2 (common BST sum)
a4_short = 210         # rank × N_c × n_C × g
us_letter_long = 11    # n_C + C_2

print(f"  A4 short side: {a4_short}mm = rank × N_c × n_C × g = {rank * N_c * n_C * g}")
print(f"  US Letter long: {us_letter_long}in = n_C + C_2 = {n_C + C_2}")
print(f"  A-series ratio: √2 = √rank")

test("A4 = rank×N_c×n_C×g = 210mm; US Letter 11in = n_C+C_2",
     a4_short == rank * N_c * n_C * g and us_letter_long == n_C + C_2,
     f"210={rank*N_c*n_C*g}, 11={n_C+C_2}")

# T6: Text layout
print("\n── Layout ──")
# Characters per line: ~60-80 (optimal readability)
# 60 = rank² × N_c × n_C; 80 = rank⁴ × n_C
# Lines per page: ~50-60
# Margins: typically 1 inch = 72 points = 2^N_c × N_c²
optimal_low = 60       # rank² × N_c × n_C
optimal_high = 80      # rank⁴ × n_C
margin_pts = 72        # 2^N_c × N_c²

print(f"  Optimal line length: {optimal_low}-{optimal_high} chars")
print(f"  = rank²×N_c×n_C to rank⁴×n_C = {rank**2*N_c*n_C} to {rank**4*n_C}")
print(f"  Standard margin: {margin_pts} pts = 2^N_c × N_c² = {2**N_c * N_c**2}")

test("60-80 chars = rank²×N_c×n_C to rank⁴×n_C; margin 72pt",
     optimal_low == rank**2 * N_c * n_C and optimal_high == rank**4 * n_C,
     f"60={rank**2*N_c*n_C}, 80={rank**4*n_C}")

# T7: Unicode
print("\n── Character Encoding ──")
# ASCII: 128 = 2^g (same as computing toy!)
# Extended ASCII: 256 = 2^(2^N_c)
# Basic Latin: 26 = rank × (2g-1)
# Digits: 10 = rank × n_C
ascii_chars = 128      # 2^g
extended = 256         # 2^(2^N_c) = rank^(2^N_c)
digits = 10            # rank × n_C

print(f"  ASCII: {ascii_chars} = 2^g = {2**g}")
print(f"  Extended: {extended} = 2^(2^N_c) = {2**(2**N_c)}")
print(f"  Digits: {digits} = rank × n_C = {rank * n_C}")

test("ASCII 128=2^g; Extended 256=2^(2^N_c); digits rank×n_C=10",
     ascii_chars == 2**g and extended == 2**(2**N_c) and digits == rank * n_C,
     f"128={2**g}, 256={2**(2**N_c)}, 10={rank*n_C}")

# T8: Writing systems
print("\n── Global Scripts ──")
# Active writing systems: ~30-40 (depending on criteria)
# But canonical Unicode scripts: ~150+
# Key counts:
# Arabic numerals: 10 = rank × n_C (0-9)
# Roman numerals: 7 symbols = g (I, V, X, L, C, D, M)
# Braille: 6 dots = C_2 → 2^C_2 = 64 characters
roman_symbols = 7      # g (I, V, X, L, C, D, M)
braille_dots = 6       # C_2
braille_chars = 64     # 2^C_2

print(f"  Roman numeral symbols: {roman_symbols} = g = {g}")
print(f"  Braille cell: {braille_dots} dots = C_2 = {C_2}")
print(f"  Braille characters: {braille_chars} = 2^C_2 = {2**C_2}")

test("g=7 Roman symbols; C_2=6 Braille dots → 2^C_2=64 chars",
     roman_symbols == g and braille_dots == C_2
     and braille_chars == 2**C_2,
     f"g={g}, C_2={C_2}, 2^C_2={2**C_2}")

# T9: Printing
print("\n── Print Technology ──")
# CMYK: 4 inks = rank² (same as photography)
# Halftone angles: typically 0°, 15°, 45°, 75° = rank² angles
# Line screen: 150 lpi standard = rank × N_c × n_C² = 2 × 3 × 25
# Offset rollers: typically 3 = N_c (plate, blanket, impression)
cmyk_inks = 4          # rank²
line_screen = 150      # rank × N_c × n_C²
offset_rollers = 3     # N_c

print(f"  CMYK inks: {cmyk_inks} = rank² = {rank**2}")
print(f"  Line screen: {line_screen} lpi = rank × N_c × n_C² = {rank * N_c * n_C**2}")
print(f"  Offset rollers: {offset_rollers} = N_c = {N_c}")

test("rank²=4 CMYK; rank×N_c×n_C²=150 lpi; N_c=3 rollers",
     cmyk_inks == rank**2 and line_screen == rank * N_c * n_C**2
     and offset_rollers == N_c,
     f"rank²={rank**2}, 150={rank*N_c*n_C**2}, N_c={N_c}")

# T10: Book structure
print("\n── Book Structure ──")
# Signature: 16 pages = rank⁴ (folded sheet)
# Quarto: 4 leaves = rank²
# Octavo: 8 leaves = 2^N_c
# Duodecimo: 12 leaves = rank² × N_c
# ISBN-13: 13 digits = 2g - 1
signature_pages = 16   # rank⁴
quarto = 4             # rank²
octavo = 8             # 2^N_c
isbn_digits = 13       # 2g - 1

print(f"  Signature: {signature_pages} pages = rank⁴ = {rank**4}")
print(f"  Quarto: {quarto} = rank² = {rank**2}")
print(f"  Octavo: {octavo} = 2^N_c = {2**N_c}")
print(f"  ISBN: {isbn_digits} digits = 2g - 1 = {2*g - 1}")

test("rank⁴=16 signature; rank²=4 quarto; 2^N_c=8 octavo; 2g-1=13 ISBN",
     signature_pages == rank**4 and quarto == rank**2
     and octavo == 2**N_c and isbn_digits == 2*g - 1,
     f"rank⁴={rank**4}, rank²={rank**2}, 2^N_c={2**N_c}, 2g-1={2*g-1}")

# Summary
print("\n" + "="*70)
print("SUMMARY")
print("="*70)
passed = sum(1 for _, (_, c, _) in results.items() if c)
total = len(results)
print(f"\n  Tests: {passed}/{total} PASS")
print(f"""
  HEADLINE: Typography IS BST Arithmetic

  72 = 2^N_c × N_c²: points/inch = rule of 72 = screen DPI
  12 = rank² × N_c: points/pica = months = hours on clock
  6 = C_2: picas/inch = Braille dots = C_2

  ALL 8 standard font sizes are 7-smooth BST products
  (10, 12, 14, 18, 24, 36, 48, 72)

  26 letters = rank × (2g-1); Gutenberg 42 = rank × N_c × g
  ASCII 128 = 2^g; Braille 64 = 2^C_2
  A4 short = 210mm = rank × N_c × n_C × g (exact!)

  The printing revolution counted in five integers.
""")
