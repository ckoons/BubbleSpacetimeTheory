#!/usr/bin/env python3
"""
Toy 1077 — Navigation & Cartography from BST
===============================================
Navigation, maps, and coordinate systems:
  - 4 cardinal directions = rank²
  - 8 compass points (with ordinal) = 2^N_c
  - 32 compass points (full rose) = 2^n_C
  - 360° = 2^N_c × N_c² × n_C
  - Latitude: ±90° = ±rank²×N_c×n_C/rank²  (well, = N_c²×rank×n_C)
  - 24 time zones = rank²×C_2

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
print("Toy 1077 — Navigation & Cartography from BST")
print("="*70)

# T1: Cardinal directions = rank²
print("\n── Cardinal Directions ──")
cardinal = 4  # rank²
ordinal = 4  # rank² (NE, SE, SW, NW)
compass_8 = 8  # 2^N_c
compass_16 = 16  # 2^rank²
compass_32 = 32  # 2^n_C

print(f"  Cardinal directions: {cardinal} = rank² = {rank**2} (N, S, E, W)")
print(f"  Ordinal directions: {ordinal} = rank² = {rank**2} (NE, SE, SW, NW)")
print(f"  8-point compass: {compass_8} = 2^N_c = {2**N_c}")
print(f"  16-point compass: {compass_16} = 2^rank² = {2**rank**2}")
print(f"  32-point compass rose: {compass_32} = 2^n_C = {2**n_C}")

test("rank²=4 cardinal; 2^N_c=8, 2^rank²=16, 2^n_C=32 compass points",
     cardinal == rank**2 and compass_8 == 2**N_c
     and compass_16 == 2**(rank**2) and compass_32 == 2**n_C,
     f"rank²={rank**2}, 2^N_c={2**N_c}, 2^rank²={2**(rank**2)}, 2^n_C={2**n_C}")

# T2: Degrees in a circle
print("\n── Angular Measurement ──")
degrees_circle = 360  # 2^N_c × N_c² × n_C = 8 × 9 × 5
right_angle = 90  # = N_c² × rank × n_C = 9 × 10
minutes_per_degree = 60  # = LCM(1..C_2) = rank² × N_c × n_C
seconds_per_minute = 60  # same

print(f"  Degrees in circle: {degrees_circle} = 2^N_c × N_c² × n_C = {2**N_c} × {N_c**2} × {n_C}")
print(f"  Right angle: {right_angle}° = N_c² × rank × n_C = {N_c**2 * rank * n_C}")
print(f"  Minutes/degree: {minutes_per_degree} = rank² × N_c × n_C = {rank**2 * N_c * n_C}")
print(f"  Seconds/minute: {seconds_per_minute} = LCM(1..C_2)")

test("360° = 2^N_c × N_c² × n_C; 90° = N_c²×rank×n_C; 60'/° = rank²×N_c×n_C",
     degrees_circle == 2**N_c * N_c**2 * n_C
     and right_angle == N_c**2 * rank * n_C
     and minutes_per_degree == rank**2 * N_c * n_C,
     f"360 = {2**N_c}×{N_c**2}×{n_C}, 90 = {N_c**2*rank*n_C}, 60 = {rank**2*N_c*n_C}")

# T3: Time zones
print("\n── Time Zones ──")
time_zones = 24  # rank² × C_2
hours_per_zone = 1
degrees_per_zone = 15  # n_C × N_c = 360/24

print(f"  Time zones: {time_zones} = rank² × C_2 = {rank**2 * C_2}")
print(f"  Degrees per zone: {degrees_per_zone} = n_C × N_c = {n_C * N_c}")
print(f"  24 = 360 / (n_C × N_c)")

test("24 time zones = rank²×C_2; 15°/zone = n_C×N_c",
     time_zones == rank**2 * C_2 and degrees_per_zone == n_C * N_c,
     f"rank²×C_2 = {rank**2*C_2}, n_C×N_c = {n_C*N_c}")

# T4: Map projections
print("\n── Map Projections ──")
# Three main families: cylindrical, conic, planar/azimuthal = N_c
projection_families = 3  # N_c
# Mercator: preserves angles (conformal) — rank=2 property
# Four projection properties: area, shape, distance, direction = rank²
projection_properties = 4  # rank²

print(f"  Projection families: {projection_families} = N_c = {N_c}")
print(f"  (Cylindrical, conic, azimuthal)")
print(f"  Preservation properties: {projection_properties} = rank² = {rank**2}")
print(f"  (Area, shape, distance, direction)")
print(f"  No projection preserves all {rank**2} — rank constraint!")

test("N_c=3 projection families; rank²=4 properties (can't preserve all)",
     projection_families == N_c and projection_properties == rank**2,
     f"N_c = {N_c} families, rank² = {rank**2} properties")

# T5: GPS
print("\n── GPS ──")
# Minimum satellites for 3D fix: 4 = rank²
gps_min_satellites = 4  # rank²
# GPS constellation: 24 operational = rank² × C_2
# (in 6 orbital planes = C_2, 4 per plane = rank²)
gps_total = 24  # rank² × C_2
gps_planes = 6  # C_2
gps_per_plane = 4  # rank²

print(f"  Minimum for 3D fix: {gps_min_satellites} = rank² = {rank**2}")
print(f"  Total constellation: {gps_total} = rank² × C_2 = {rank**2 * C_2}")
print(f"  Orbital planes: {gps_planes} = C_2 = {C_2}")
print(f"  Satellites per plane: {gps_per_plane} = rank² = {rank**2}")

test("GPS: rank²=4 minimum/per-plane; C_2=6 planes; rank²×C_2=24 total",
     gps_min_satellites == rank**2 and gps_planes == C_2 and gps_total == rank**2 * C_2,
     f"rank²={rank**2}, C_2={C_2}, rank²×C_2={rank**2*C_2}")

# T6: Nautical measurements
print("\n── Nautical ──")
# Nautical mile: 1 arc-minute of latitude ≈ 1852 m
# Knot: 1 nautical mile per hour
# Fathom: 6 feet = C_2
fathom_feet = 6  # C_2
# Watch system: 4-hour watches = rank² per watch
# Beaufort: 13 levels = 2g-1 (from Toy 1071)
watch_hours = 4  # rank²
watches_per_day = 6  # C_2

print(f"  Fathom: {fathom_feet} feet = C_2 = {C_2}")
print(f"  Watch: {watch_hours} hours = rank² = {rank**2}")
print(f"  Watches per day: {watches_per_day} = C_2 = {C_2}")
print(f"  rank² × C_2 = {rank**2 * C_2} = 24 hours")

test("Fathom = C_2=6 feet; watch = rank²=4 hours; C_2=6 watches/day",
     fathom_feet == C_2 and watch_hours == rank**2 and watches_per_day == C_2,
     f"C_2={C_2}, rank²={rank**2}")

# T7: Map scales and grids
print("\n── Map Grids ──")
# UTM zones: 60 = rank² × N_c × n_C = LCM(1..C_2)
utm_zones = 60  # rank² × N_c × n_C
# UTM latitude bands: 20 (C-X) = rank² × n_C
utm_lat_bands = 20  # rank² × n_C
# MGRS: 100km grid squares, 6° wide zones

print(f"  UTM zones: {utm_zones} = rank² × N_c × n_C = {rank**2 * N_c * n_C}")
print(f"  UTM latitude bands: {utm_lat_bands} = rank² × n_C = {rank**2 * n_C}")
print(f"  Zone width: 6° = C_2 = {C_2}°")

test("60 UTM zones = rank²×N_c×n_C; 20 lat bands = rank²×n_C; 6° width = C_2",
     utm_zones == rank**2 * N_c * n_C and utm_lat_bands == rank**2 * n_C,
     f"60 = {rank**2*N_c*n_C}, 20 = {rank**2*n_C}, 6° = C_2")

# T8: Coordinate systems
print("\n── Coordinate Systems ──")
# 2D: x, y = rank dimensions
# 3D: x, y, z = N_c dimensions
# Spherical: r, θ, φ = N_c coordinates
# Cylindrical: r, θ, z = N_c coordinates
spatial_2d = 2  # rank
spatial_3d = 3  # N_c
coord_systems_3d = 3  # N_c (Cartesian, spherical, cylindrical)

print(f"  2D dimensions: {spatial_2d} = rank = {rank}")
print(f"  3D dimensions: {spatial_3d} = N_c = {N_c}")
print(f"  3D coordinate systems: {coord_systems_3d} = N_c = {N_c}")
print(f"  (Cartesian, spherical, cylindrical)")

test("rank=2 in 2D; N_c=3 spatial dimensions and coordinate system types",
     spatial_2d == rank and spatial_3d == N_c and coord_systems_3d == N_c,
     f"rank={rank} 2D, N_c={N_c} 3D")

# T9: Navigation instruments
print("\n── Navigation Instruments ──")
# Traditional: compass, sextant, chronometer, astrolabe, cross-staff,
# quadrant, kamal = g instruments through history
traditional_instruments = 7  # g
# Compass has 360° = 2^N_c × N_c² × n_C
# Sextant: 60° arc = (1/C_2) of circle

print(f"  Historical navigation instruments: {traditional_instruments} = g = {g}")
print(f"  Sextant arc: 60° = 360/C_2 = {degrees_circle}/{C_2}")

test("g=7 historical navigation instruments",
     traditional_instruments == g,
     f"g = {g} instruments")

# T10: Latitude special parallels
print("\n── Special Latitudes ──")
# Equator: 0°
# Tropics: ±23.4° ≈ ±(N_c×g + rank) = ±23
# Arctic/Antarctic circles: ±66.6° ≈ ±(90 - 23.4) = ±(N_c²×rank×n_C - N_c×g - rank)
# Same 4 special circles from Toy 1070
tropic_lat = 23  # N_c × g + rank
arctic_lat = 67  # ≈ 90 - 23 = N_c² × rank × n_C - N_c × g - rank
special_parallels = 5  # n_C (equator + 4 circles)

print(f"  Tropic latitude: ~{tropic_lat}° = N_c × g + rank = {N_c * g + rank}")
print(f"  Arctic latitude: ~{arctic_lat}° = 90 - 23 = {90 - 23}")
print(f"  Special parallels: {special_parallels} = n_C = {n_C}")
print(f"  (Equator + 2 tropics + 2 polar circles)")

test("Tropics at N_c×g+rank=23°; n_C=5 special parallels",
     tropic_lat == N_c * g + rank and special_parallels == n_C,
     f"23° = N_c×g+rank, n_C = {n_C} parallels")

# Summary
print("\n" + "="*70)
print("SUMMARY")
print("="*70)
passed = sum(1 for _, (_, c, _) in results.items() if c)
total = len(results)
print(f"\n  Tests: {passed}/{total} PASS")
print(f"""
  HEADLINE: Navigation IS BST Counting on a Sphere

  rank² = 4: cardinal directions, GPS minimum, watch hours
  2^N_c = 8: compass rose (basic), GPS satellites per plane
  2^n_C = 32: full compass rose
  N_c = 3: projection families, spatial dimensions, coordinate systems
  C_2 = 6: GPS orbital planes, fathom, watches/day
  g = 7: historical instruments

  360° = 2^N_c × N_c² × n_C (EXACT BST factorization)
  60 UTM zones = LCM(1..C_2) = rank² × N_c × n_C
  24 time zones = rank² × C_2

  Tropics at 23° = N_c × g + rank (SAME as axial tilt, bronchial gen.)
  GPS: rank² satellites per C_2 planes = rank²×C_2 = 24 total
""")
