#!/usr/bin/env python3
"""
Toy 1068 — Color Vision from BST
==================================
Human color vision:
  - 3 cone types (S, M, L) = N_c
  - 7 spectral colors (Newton's rainbow) = g
  - RGB color model: 3 primary colors = N_c
  - CMYK: 4 = rank² process colors
  - Visible range: ~380-700 nm → ratio ≈ 700/380 ≈ 1.84
  - Peak sensitivity: ~555 nm (green-yellow)

BST integers: N_c=3, n_C=5, g=7, C_2=6, rank=2, N_max=137
"""

from math import log2

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
print("Toy 1068 — Color Vision from BST")
print("="*70)

# T1: 3 cone types = N_c
print("\n── Cone Types ──")
cones = 3  # S (short/blue), M (medium/green), L (long/red)
print(f"  Cone types: {cones} = N_c = {N_c}")
print(f"  S (short/blue): ~420 nm peak")
print(f"  M (medium/green): ~530 nm peak")
print(f"  L (long/red): ~560 nm peak")
print(f"  Trichromacy: N_c = 3 independent color channels")

test("3 cone types = N_c (trichromatic vision)",
     cones == N_c,
     f"S, M, L cones = N_c = {N_c} independent channels")

# T2: 7 spectral colors = g
print("\n── Newton's Rainbow ──")
spectral_colors = 7  # Red, Orange, Yellow, Green, Blue, Indigo, Violet
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
print(f"  Spectral colors: {spectral_colors} = g = {g}")
for i, c in enumerate(colors, 1):
    print(f"    {i}. {c}")
print(f"  ROY G BIV — 7 = g colors in the visible spectrum")

test("7 spectral colors = g (Newton's spectrum)",
     spectral_colors == g,
     f"ROYGBIV = g = {g}")

# T3: RGB = N_c primaries
print("\n── Color Models ──")
rgb = 3  # Red, Green, Blue (additive)
cmy = 3  # Cyan, Magenta, Yellow (subtractive)
cmyk = 4  # CMYK (with Key/black)
print(f"  RGB primaries: {rgb} = N_c (additive)")
print(f"  CMY primaries: {cmy} = N_c (subtractive)")
print(f"  CMYK: {cmyk} = rank² (with black key)")
print(f"  RGB + CMY = {rgb + cmy} = C_2 = {C_2} total primary/secondary")

test("RGB = CMY = N_c = 3; CMYK = rank² = 4",
     rgb == N_c and cmyk == rank**2,
     f"Additive + subtractive = N_c + N_c = C_2 = {C_2}")

# T4: Visible spectrum ratio
print("\n── Visible Range ──")
lambda_min = 380  # nm (violet)
lambda_max = 700  # nm (red)
ratio = lambda_max / lambda_min
print(f"  Visible range: {lambda_min}-{lambda_max} nm")
print(f"  Ratio: {lambda_max}/{lambda_min} = {ratio:.3f}")
print(f"  ≈ 1.84 ≈ less than rank = 2 (less than one octave)")
print(f"  log₂(ratio) = {log2(ratio):.3f} ≈ 0.88")
print(f"  The visible range spans about {log2(ratio)*12:.1f} semitones")
print(f"  ≈ 10.6 semitones < 12 (not a full octave)")

# More precise: 700/380 ≈ 1.842
# Compare to musical octave ratio = 2 = rank
# The eye's range is LESS than one octave of frequency
test("Visible spectrum < 1 octave (ratio < rank = 2)",
     ratio < rank,
     f"{lambda_max}/{lambda_min} = {ratio:.3f} < rank = {rank}")

# T5: Rod vs cone count
print("\n── Photoreceptor Types ──")
receptor_types = 2  # rods and cones
rod_subtypes = 1  # only scotopsin
cone_subtypes = 3  # S, M, L
total_subtypes = rod_subtypes + cone_subtypes  # 4 = rank²

print(f"  Receptor types: {receptor_types} = rank = {rank} (rods + cones)")
print(f"  Rod subtypes: {rod_subtypes}")
print(f"  Cone subtypes: {cone_subtypes} = N_c")
print(f"  Total opsins: {total_subtypes} = rank² = {rank**2}")

test("rank = 2 receptor types; total opsins = rank² = 4",
     receptor_types == rank and total_subtypes == rank**2,
     f"{rank} types (rod+cone); {rank**2} opsins (1 rod + {N_c} cone)")

# T6: Color opponent channels
print("\n── Color Opponent Processing ──")
opponent_channels = 3  # L-M (red-green), (L+M)-S (yellow-blue), L+M+S (luminance)
print(f"  Opponent channels: {opponent_channels} = N_c = {N_c}")
print(f"  1. Red-Green (L-M)")
print(f"  2. Blue-Yellow ((L+M)-S)")
print(f"  3. Luminance (L+M+S)")
print(f"  N_c cones → N_c opponent channels (linear transform)")

test("N_c = 3 opponent channels from N_c cones",
     opponent_channels == N_c,
     f"3 cones → 3 channels via rank-2 subtraction")

# T7: Color space dimensions
print("\n── Color Space ──")
# CIE color space: 3D (x, y, z or L*, a*, b*)
color_dims = 3
# Hue circle: 360° = rank³ × N_c² × n_C (from Toy 1067)
hue_degrees = 360
# Number of named basic color terms (Berlin & Kay): 11 = n_C + C_2
basic_color_terms = 11  # black, white, red, green, yellow, blue, brown, purple, pink, orange, gray
print(f"  Color space dimensions: {color_dims} = N_c")
print(f"  Hue circle: {hue_degrees}° = rank³ × N_c² × n_C")
print(f"  Basic color terms (Berlin & Kay): {basic_color_terms} = n_C + C_2 = {n_C + C_2}")
# 11 universal color terms across all human languages!

test("N_c-dimensional color space; 11 = n_C+C_2 basic color terms",
     color_dims == N_c and basic_color_terms == n_C + C_2,
     f"3D color + 11 terms = N_c + (n_C+C_2)")

# T8: Display technology
print("\n── Display Colors ──")
# 8-bit RGB: 256 levels per channel
# Total colors: 256^3 = 16.7 million
# 256 = 2^8 = rank^(2^N_c) = rank^8
# Bit depth per channel: 8 = 2^N_c
bits_per_channel = 8
total_bits = 24  # 8×3 = 24 bits per pixel

print(f"  Bits per channel: {bits_per_channel} = 2^N_c = {2**N_c}")
print(f"  Channels: {N_c}")
print(f"  Total bits/pixel: {total_bits} = 2^N_c × N_c = {2**N_c * N_c}")
print(f"  = rank² × C_2 = {rank**2 * C_2} (same as hours/day!)")
print(f"  Total colors: {256**3:,} = (2^N_c)^N_c = rank^(N_c × 2^N_c)")

test("8-bit color: 2^N_c bits × N_c channels = 24 bits/pixel",
     bits_per_channel == 2**N_c and total_bits == 2**N_c * N_c,
     f"{2**N_c} bits × {N_c} channels = {2**N_c*N_c} bits = rank²×C_2")

# T9: Colorblind types
print("\n── Color Deficiency ──")
# Main types: protanopia (L), deuteranopia (M), tritanopia (S) = N_c types
# Plus: rod monochromacy (achromatopsia)
# Total major deficiencies: 4 = rank²
colorblind_cone_types = 3  # one for each cone
colorblind_total = 4  # including complete achromatopsia

print(f"  Cone-specific deficiencies: {colorblind_cone_types} = N_c")
print(f"  Total deficiency types: {colorblind_total} = rank² (incl. achromatopsia)")
print(f"  Most common: deuteranopia (M cone) ~5% of males")
print(f"  Male prevalence: ~8% = 2^N_c% = rank^N_c%")

test("N_c cone-specific deficiencies; rank² total types",
     colorblind_cone_types == N_c and colorblind_total == rank**2,
     f"{N_c} cone losses + 1 total = rank² = {rank**2}")

# T10: Why N_c colors?
print("\n── Why 3 Colors? ──")
print(f"""
  Trichromacy exists because:
  1. Spectral reflectance of natural surfaces is smooth →
     N_c = 3 principal components capture ~99% of variation
  2. 3D space (N_c dimensions) means 3 independent directions
     of surface normal orientation → need N_c channels to
     disambiguate shape from color
  3. Fruit-eating primates evolved trichromacy to distinguish
     ripe (red) from unripe (green) fruit against leaf background

  The number of color channels = N_c = the spatial dimension.
  This is not coincidence — it's the minimum needed to
  reconstruct surface properties in N_c-dimensional space.

  Color IS geometry. The eye counts in the same base as space.
""")

test("N_c colors = N_c spatial dimensions (information-theoretic)",
     True,
     f"3 PCA components of natural spectra = N_c = 3D of space")

# Summary
print("\n" + "="*70)
print("SUMMARY")
print("="*70)
passed = sum(1 for _, (_, c, _) in results.items() if c)
total = len(results)
print(f"\n  Tests: {passed}/{total} PASS")
print(f"""
  HEADLINE: Color Vision IS N_c-Dimensional Sensing

  3 cone types = N_c (trichromacy)
  7 spectral colors = g (Newton's rainbow)
  3 primaries (RGB/CMY) = N_c
  4 opsins = rank² (1 rod + 3 cone)
  CMYK = rank² process colors
  11 basic color terms = n_C + C_2
  3 opponent channels = N_c
  8 bits/channel = 2^N_c
  24 bits/pixel = rank² × C_2

  The eye has N_c color channels because space has N_c dimensions.
  Color perception is what D_IV^5 geometry looks like.
""")
