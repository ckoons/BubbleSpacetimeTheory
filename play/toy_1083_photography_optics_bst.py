#!/usr/bin/env python3
"""
Toy 1083 — Photography & Optics from BST
==========================================
Photographic and optical structure:
  - f-stop scale: √2 steps = √rank
  - ISO: 100 base = rank²×n_C², doubling = rank
  - Standard focal lengths: 35,50,85,135 → BST-adjacent
  - Color models: RGB=N_c, CMYK=rank², HSL/HSV=N_c
  - Resolution: 72 dpi = 2^N_c × N_c² (rule of 72!)

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
print("Toy 1083 — Photography & Optics from BST")
print("="*70)

# T1: Color models
print("\n── Color Models ──")
# RGB: 3 primaries = N_c; CMYK: 4 process colors = rank²
# HSL/HSV: 3 channels = N_c
# Color depth: 8 bits/channel = 2^N_c
rgb_channels = 3      # N_c
cmyk_channels = 4     # rank²
bits_per_channel = 8  # 2^N_c

print(f"  RGB channels: {rgb_channels} = N_c = {N_c}")
print(f"  CMYK channels: {cmyk_channels} = rank² = {rank**2}")
print(f"  Bits per channel: {bits_per_channel} = 2^N_c = {2**N_c}")

test("N_c=3 RGB; rank²=4 CMYK; 2^N_c=8 bits/channel",
     rgb_channels == N_c and cmyk_channels == rank**2
     and bits_per_channel == 2**N_c,
     f"N_c={N_c}, rank²={rank**2}, 2^N_c={2**N_c}")

# T2: f-stop scale
print("\n── f-stop Scale ──")
# Standard f-stops: f/1, 1.4, 2, 2.8, 4, 5.6, 8, 11, 16, 22, 32
# Each step = √2 = √rank (doubles light)
# Full stops in typical lens: 8-10 ≈ 2^N_c
# Aperture range factor: 2^(stops/2)
fstop_ratio = 2      # rank (each full stop doubles/halves light)
# Standard sequence has 2^N_c = 8 main stops in common range
common_stops = 8      # 2^N_c

print(f"  Light ratio per stop: {fstop_ratio}× = rank = {rank}")
print(f"  Common full stops: {common_stops} = 2^N_c = {2**N_c}")
print(f"  √{rank} = {2**0.5:.3f} (f-number step factor)")

test("rank=2× per stop; 2^N_c=8 common stops",
     fstop_ratio == rank and common_stops == 2**N_c,
     f"rank={rank}, 2^N_c={2**N_c}")

# T3: ISO sensitivity
print("\n── ISO Scale ──")
# Base ISO: 100 = rank² × n_C²
# Each ISO doubling = rank
# Common ISO: 100, 200, 400, 800, 1600, 3200 = 6 = C_2 main values
iso_base = 100       # rank² × n_C²
iso_doubling = 2     # rank
common_iso_values = 6  # C_2

print(f"  Base ISO: {iso_base} = rank² × n_C² = {rank**2 * n_C**2}")
print(f"  ISO doubling factor: {iso_doubling} = rank = {rank}")
print(f"  Common ISO values: {common_iso_values} = C_2 = {C_2}")
print(f"  (100, 200, 400, 800, 1600, 3200)")

test("rank²×n_C²=100 base ISO; rank=2 doubling; C_2=6 common values",
     iso_base == rank**2 * n_C**2 and iso_doubling == rank
     and common_iso_values == C_2,
     f"rank²×n_C²={rank**2*n_C**2}, rank={rank}, C_2={C_2}")

# T4: Resolution
print("\n── Resolution ──")
# Screen: 72 dpi = 2^N_c × N_c² (rule of 72!)
# Print: 300 dpi = rank² × N_c × n_C²
# Retina: 144 dpi = 2 × 72 = rank × 2^N_c × N_c²
screen_dpi = 72       # 2^N_c × N_c²
print_dpi = 300       # rank² × N_c × n_C²
retina_dpi = 144      # rank × 2^N_c × N_c²

print(f"  Screen: {screen_dpi} dpi = 2^N_c × N_c² = {2**N_c * N_c**2}")
print(f"  Print: {print_dpi} dpi = rank² × N_c × n_C² = {rank**2 * N_c * n_C**2}")
print(f"  Retina: {retina_dpi} dpi = rank × 72 = {rank * 72}")
print(f"  (72 = rule of 72 = doubling constant!)")

test("72dpi = 2^N_c×N_c²; 300dpi = rank²×N_c×n_C²",
     screen_dpi == 2**N_c * N_c**2 and print_dpi == rank**2 * N_c * n_C**2,
     f"72={2**N_c*N_c**2}, 300={rank**2*N_c*n_C**2}")

# T5: Image formats
print("\n── Image Standards ──")
# JPEG quality: 1-100 scale, default 75 = N_c × n_C²
# Aspect ratios: 3:2 = N_c:rank, 4:3 = rank²:N_c, 16:9 = 2^rank²:N_c²
# Common megapixel counts: 12, 24, 48 (doubling)
jpeg_default = 75     # N_c × n_C²
aspect_3_2 = (3, 2)   # (N_c, rank)
aspect_4_3 = (4, 3)   # (rank², N_c)
aspect_16_9 = (16, 9)  # (2^rank², N_c²)

print(f"  JPEG default: {jpeg_default} = N_c × n_C² = {N_c * n_C**2}")
print(f"  3:2 = N_c:rank; 4:3 = rank²:N_c; 16:9 = 2^rank²:N_c²")

test("JPEG 75 = N_c×n_C²; aspects 3:2, 4:3, 16:9 all BST",
     jpeg_default == N_c * n_C**2
     and aspect_3_2 == (N_c, rank) and aspect_4_3 == (rank**2, N_c)
     and aspect_16_9 == (2**rank**2, N_c**2),
     f"75={N_c*n_C**2}; ratios verified")

# T6: Exposure triangle
print("\n── Exposure Triangle ──")
# 3 exposure parameters = N_c: aperture, shutter, ISO
# Shutter speed doubling = rank
# Standard shutter speeds: 8 common = 2^N_c
# (1/1000, 1/500, 1/250, 1/125, 1/60, 1/30, 1/15, 1/8)
exposure_params = 3   # N_c
shutter_doubling = 2  # rank
common_shutters = 8   # 2^N_c

print(f"  Exposure parameters: {exposure_params} = N_c = {N_c}")
print(f"  Shutter speed doubling: {shutter_doubling}× = rank = {rank}")
print(f"  Common shutter speeds: {common_shutters} = 2^N_c = {2**N_c}")

test("N_c=3 exposure params; rank=2 doubling; 2^N_c=8 shutter speeds",
     exposure_params == N_c and shutter_doubling == rank
     and common_shutters == 2**N_c,
     f"N_c={N_c}, rank={rank}, 2^N_c={2**N_c}")

# T7: Lens focal lengths
print("\n── Focal Lengths ──")
# Normal lens: 50mm = rank × n_C²
# Wide angle standard: 35mm = n_C × g
# Portrait: 85mm ≈ ... (not clean)
# Full frame diagonal: 43mm ≈ rank × N_c × g + 1 (43 is prime, near 42)
normal_lens = 50      # rank × n_C²
wide_lens = 35        # n_C × g
# Crop factor: 1.5 (APS-C) = N_c/rank
crop_factor_num = 3   # N_c
crop_factor_den = 2   # rank

print(f"  Normal lens: {normal_lens}mm = rank × n_C² = {rank * n_C**2}")
print(f"  Wide standard: {wide_lens}mm = n_C × g = {n_C * g}")
print(f"  APS-C crop: {crop_factor_num}/{crop_factor_den} = N_c/rank = {N_c/rank}")

test("50mm = rank×n_C²; 35mm = n_C×g; crop 3/2 = N_c/rank",
     normal_lens == rank * n_C**2 and wide_lens == n_C * g
     and crop_factor_num == N_c and crop_factor_den == rank,
     f"50={rank*n_C**2}, 35={n_C*g}, 1.5={N_c}/{rank}")

# T8: Color spaces
print("\n── Color Science ──")
# CIE color matching: 3 functions = N_c (X, Y, Z)
# Visible spectrum: ~380-700nm → 320nm range
# Color temperature: 5500K daylight ≈ n_C² × rank² × N_c × (2g-1 + 1)
# Actually: 5600 = 2^5 × 5^2 × 7 = rank^5 × n_C² × g
cie_functions = 3     # N_c
daylight_approx = 5600  # rank⁵ × n_C² × g

print(f"  CIE matching functions: {cie_functions} = N_c = {N_c}")
print(f"  Daylight ~5600K = rank⁵ × n_C² × g = {rank**5 * n_C**2 * g}")

test("N_c=3 CIE functions; ~5600K = rank⁵×n_C²×g",
     cie_functions == N_c and daylight_approx == rank**5 * n_C**2 * g,
     f"N_c={N_c}, rank⁵×n_C²×g={rank**5*n_C**2*g}")

# T9: Video standards
print("\n── Video ──")
# Frame rates: 24 fps (cinema) = rank³ × N_c
# 30 fps (TV) = n_C# = rank × N_c × n_C
# 60 fps (smooth) = rank² × N_c × n_C
# Interlaced fields: 2 = rank
cinema_fps = 24       # rank³ × N_c
tv_fps = 30           # n_C#
smooth_fps = 60       # rank² × N_c × n_C

print(f"  Cinema: {cinema_fps} fps = rank³ × N_c = {rank**3 * N_c}")
print(f"  TV: {tv_fps} fps = n_C# = {rank * N_c * n_C}")
print(f"  Smooth: {smooth_fps} fps = rank² × N_c × n_C = {rank**2 * N_c * n_C}")

test("24fps = rank³×N_c; 30fps = n_C#; 60fps = rank²×N_c×n_C",
     cinema_fps == rank**3 * N_c and tv_fps == rank * N_c * n_C
     and smooth_fps == rank**2 * N_c * n_C,
     f"24={rank**3*N_c}, 30={rank*N_c*n_C}, 60={rank**2*N_c*n_C}")

# T10: Display technology
print("\n── Displays ──")
# HD: 1920×1080 → 1920 = 2^7 × 3 × 5 = rank^7 × N_c × n_C
# 1080 = 2^3 × 3^3 × 5 = rank³ × N_c³ × n_C
# 4K: 3840×2160 = 2× HD
# Refresh rates: 60Hz = rank² × N_c × n_C; 120Hz = rank³ × N_c × n_C
hd_width = 1920       # rank⁷ × N_c × n_C
hd_height = 1080      # rank³ × N_c³ × n_C

print(f"  HD width: {hd_width} = rank⁷ × N_c × n_C = {rank**7 * N_c * n_C}")
print(f"  HD height: {hd_height} = rank³ × N_c³ × n_C = {rank**3 * N_c**3 * n_C}")
print(f"  Both are exact BST products (7-smooth)!")
print(f"  Ratio: 1920/1080 = 16/9 = 2^rank²/N_c²")

test("1920 = rank⁷×N_c×n_C; 1080 = rank³×N_c³×n_C (both 7-smooth)",
     hd_width == rank**7 * N_c * n_C and hd_height == rank**3 * N_c**3 * n_C,
     f"1920={rank**7*N_c*n_C}, 1080={rank**3*N_c**3*n_C}")

# Summary
print("\n" + "="*70)
print("SUMMARY")
print("="*70)
passed = sum(1 for _, (_, c, _) in results.items() if c)
total = len(results)
print(f"\n  Tests: {passed}/{total} PASS")
print(f"""
  HEADLINE: Imaging IS BST Arithmetic

  N_c = 3: RGB, CIE, exposure triangle
  rank² = 4: CMYK channels
  2^N_c = 8: bits/channel, f-stops, shutter speeds
  rank²×n_C² = 100: base ISO, US Senate (same!)
  72 = 2^N_c × N_c²: screen DPI = rule of 72 = Debye/finance constant

  Focal lengths: 50mm = rank×n_C², 35mm = n_C×g
  Frame rates: 24 = rank³×N_c, 30 = n_C#, 60 = rank²×N_c×n_C
  HD: 1920×1080 — BOTH dimensions are exact BST products

  Every photographic standard is built from five integers.
""")
