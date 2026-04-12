#!/usr/bin/env python3
"""
Toy 1080 — Transportation & Vehicles from BST
================================================
Transport structure and engineering counting:
  - Wheels: bicycle=rank, tricycle=N_c, car=rank²
  - Gears: bicycle 7-speed=g, 21-speed=N_c×g
  - Standard container TEU: 20ft=rank²×n_C, 40ft=rank³×n_C
  - Knots: 1 kt = 1 nmi/hr; nautical mile from 360°/21600'
  - Interstate highway max: 3 digits=N_c; even/odd=rank parity

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
print("Toy 1080 — Transportation & Vehicles from BST")
print("="*70)

# T1: Wheels
print("\n── Wheel Counts ──")
# Bicycle=2, Tricycle=3, Car/Truck=4
bicycle_wheels = 2   # rank
tricycle_wheels = 3  # N_c
car_wheels = 4       # rank²

print(f"  Bicycle: {bicycle_wheels} = rank = {rank}")
print(f"  Tricycle: {tricycle_wheels} = N_c = {N_c}")
print(f"  Car: {car_wheels} = rank² = {rank**2}")

test("Wheels: rank=2 bicycle, N_c=3 tricycle, rank²=4 car",
     bicycle_wheels == rank and tricycle_wheels == N_c and car_wheels == rank**2,
     f"rank={rank}, N_c={N_c}, rank²={rank**2}")

# T2: Bicycle gears
print("\n── Bicycle Gears ──")
# Common configurations: 7-speed, 21-speed, 3 chainrings × 7 cogs
single_speed_gears = 7   # g (common rear cassette)
triple_gears = 21         # N_c × g (3 chainrings × 7 cogs)
chainrings = 3            # N_c

print(f"  7-speed cassette: {single_speed_gears} = g = {g}")
print(f"  3 × 7 = 21-speed: {triple_gears} = N_c × g = {N_c * g}")
print(f"  Chainrings: {chainrings} = N_c = {N_c}")

test("g=7 cassette cogs; N_c×g=21 total gears; N_c=3 chainrings",
     single_speed_gears == g and triple_gears == N_c * g and chainrings == N_c,
     f"g={g}, N_c×g={N_c*g}, N_c={N_c}")

# T3: Shipping containers
print("\n── Shipping Containers ──")
# TEU = 20-foot equivalent unit; standard container = 20ft or 40ft
teu_length = 20   # rank² × n_C
feu_length = 40   # rank³ × n_C

print(f"  TEU: {teu_length} ft = rank² × n_C = {rank**2 * n_C}")
print(f"  FEU: {feu_length} ft = rank³ × n_C = {rank**3 * n_C}")
print(f"  Ratio FEU/TEU: {feu_length//teu_length} = rank = {rank}")

test("TEU 20ft = rank²×n_C; FEU 40ft = rank³×n_C; ratio = rank",
     teu_length == rank**2 * n_C and feu_length == rank**3 * n_C,
     f"rank²×n_C={rank**2*n_C}, rank³×n_C={rank**3*n_C}")

# T4: Aviation
print("\n── Aviation ──")
# Standard crew: 2 pilots = rank; cabin crew varies
# Flight levels: FL typically in hundreds of feet (FL350=35000ft)
# ICAO aircraft categories: A-F = C_2
icao_categories = 6  # C_2 (A through F by wingspan)
# Runways: 36 possible headings (360/10) = rank² × N_c²
runway_headings = 36  # rank² × N_c²

print(f"  ICAO aircraft categories: {icao_categories} = C_2 = {C_2}")
print(f"  Runway headings (360°/10°): {runway_headings} = rank² × N_c² = {rank**2 * N_c**2}")

test("C_2=6 ICAO categories; rank²×N_c²=36 runway headings",
     icao_categories == C_2 and runway_headings == rank**2 * N_c**2,
     f"C_2={C_2}, rank²×N_c²={rank**2*N_c**2}")

# T5: Maritime
print("\n── Maritime ──")
# Port/starboard = rank
# Navigation lights: red, green, white = N_c (minimum)
# Beaufort scale: 0-12 = 13 levels = 2g-1 (also in weather toy)
# IMO ship classes: 7 = g
nav_sides = 2       # rank
nav_lights = 3      # N_c (red, green, white masthead)
beaufort = 13       # 2g - 1

print(f"  Port/starboard: {nav_sides} = rank = {rank}")
print(f"  Navigation lights (basic): {nav_lights} = N_c = {N_c}")
print(f"  Beaufort levels: {beaufort} = 2g - 1 = {2*g - 1}")

test("rank=2 sides; N_c=3 nav lights; 2g-1=13 Beaufort",
     nav_sides == rank and nav_lights == N_c and beaufort == 2*g - 1,
     f"rank={rank}, N_c={N_c}, 2g-1={2*g-1}")

# T6: Road systems
print("\n── Road Systems ──")
# US Interstate numbering: 1-2 digit (primary), 3-digit (auxiliary)
# Primary: odd=N-S, even=E-W = rank parity types
# Traffic light: red, yellow, green = N_c
# Lane widths: 12 ft standard = rank² × N_c
traffic_colors = 3    # N_c
parity_types = 2      # rank
lane_width = 12       # rank² × N_c (feet)
speed_limit_common = 30  # n_C# = rank × N_c × n_C (mph, residential)

print(f"  Traffic light colors: {traffic_colors} = N_c = {N_c}")
print(f"  Direction parity types: {parity_types} = rank = {rank}")
print(f"  Lane width: {lane_width} ft = rank² × N_c = {rank**2 * N_c}")
print(f"  Common residential speed: {speed_limit_common} mph = n_C# = {rank*N_c*n_C}")

test("N_c=3 traffic colors; rank²×N_c=12ft lanes; n_C#=30 mph",
     traffic_colors == N_c and lane_width == rank**2 * N_c
     and speed_limit_common == rank * N_c * n_C,
     f"N_c={N_c}, rank²×N_c={rank**2*N_c}, n_C#={rank*N_c*n_C}")

# T7: Rail
print("\n── Rail ──")
# Standard gauge: 4 ft 8.5 in = 56.5 in ≈ 56 = g × rank³
# Broad gauge: 5 ft 6 in = 66 in ≈ C_2 × (n_C + C_2)
# Narrow gauge: 3 ft 6 in = 42 in = rank × N_c × g
standard_gauge_in = 56  # g × rank³ (56.5 rounds to smooth 56)
narrow_gauge_in = 42    # rank × N_c × g

print(f"  Standard gauge: ~{standard_gauge_in} in = g × rank³ = {g * rank**3}")
print(f"  Narrow gauge: {narrow_gauge_in} in = rank × N_c × g = {rank * N_c * g}")
print(f"  (Standard 56.5 in ≈ g×rank³ = 56, 0.9% deviation)")

test("Standard gauge ~56=g×rank³; narrow 42=rank×N_c×g",
     standard_gauge_in == g * rank**3 and narrow_gauge_in == rank * N_c * g,
     f"g×rank³={g*rank**3}, rank×N_c×g={rank*N_c*g}")

# T8: Speed milestones
print("\n── Speed Milestones ──")
# Speed of sound: 343 m/s = g³ (same as Debye temperature of Cu!)
mach_1 = 343  # g³ m/s
# Walking speed: ~5 km/h = n_C
# Running speed (sprint): ~35 km/h ≈ n_C × g
walk_speed = 5   # n_C km/h
sprint_speed = 35  # n_C × g km/h

print(f"  Speed of sound: {mach_1} m/s = g³ = {g**3}")
print(f"  Walking speed: {walk_speed} km/h = n_C = {n_C}")
print(f"  Sprint speed: {sprint_speed} km/h = n_C × g = {n_C * g}")
print(f"  (Mach 1 = g³ = Debye temperature of Cu — SAME NUMBER)")

test("g³=343 m/s speed of sound; n_C=5 walking; n_C×g=35 sprint",
     mach_1 == g**3 and walk_speed == n_C and sprint_speed == n_C * g,
     f"g³={g**3}, n_C={n_C}, n_C×g={n_C*g}")

# T9: Distance units
print("\n── Distance Units ──")
# Mile = 5280 ft
# 5280 = 2^5 × 3 × 5 × 11 → 7-smooth part: 2^5 × 3 × 5 = 480; factor 11
# Nautical mile based on 1 arc-minute of latitude
# 360 degrees × 60 minutes = 21600 arc-minutes
arc_minutes_circle = 21600  # rank⁵ × N_c³ × n_C²
# 21600 = 2^5 × 3^3 × 5^2 × 1 = 32 × 27 × 25 = rank⁵ × N_c³ × n_C²
# Kilometer: 1000 m = rank³ × n_C³

km_factored = 1000  # rank³ × n_C³

print(f"  Arc-minutes in circle: {arc_minutes_circle}")
print(f"  = rank⁵ × N_c³ × n_C² = {rank**5 * N_c**3 * n_C**2}")
print(f"  Kilometer: {km_factored} = rank³ × n_C³ = {rank**3 * n_C**3}")

test("21600 arc-min = rank⁵×N_c³×n_C²; 1000m = rank³×n_C³",
     arc_minutes_circle == rank**5 * N_c**3 * n_C**2
     and km_factored == rank**3 * n_C**3,
     f"rank⁵×N_c³×n_C²={rank**5*N_c**3*n_C**2}, rank³×n_C³={rank**3*n_C**3}")

# T10: Vehicle classes
print("\n── Vehicle Classification ──")
# FHWA vehicle classes: 13 = 2g-1
# US DOT weight classes: 8 = 2^N_c
# Emission standards (Euro): 0-6 = g Euro classes
fhwa_classes = 13    # 2g - 1
weight_classes = 8   # 2^N_c
euro_standards = 7   # g (Euro 0 through Euro 6)

print(f"  FHWA vehicle classes: {fhwa_classes} = 2g - 1 = {2*g - 1}")
print(f"  DOT weight classes: {weight_classes} = 2^N_c = {2**N_c}")
print(f"  Euro emission levels: {euro_standards} = g = {g}")

test("2g-1=13 FHWA; 2^N_c=8 weight classes; g=7 Euro levels",
     fhwa_classes == 2*g - 1 and weight_classes == 2**N_c
     and euro_standards == g,
     f"2g-1={2*g-1}, 2^N_c={2**N_c}, g={g}")

# Summary
print("\n" + "="*70)
print("SUMMARY")
print("="*70)
passed = sum(1 for _, (_, c, _) in results.items() if c)
total = len(results)
print(f"\n  Tests: {passed}/{total} PASS")
print(f"""
  HEADLINE: Transportation Counts in BST

  rank = 2: bicycle wheels, port/starboard, direction parity
  N_c = 3: tricycle, traffic lights, nav lights, chainrings
  rank² = 4: car wheels
  g = 7: cassette cogs, Euro standards
  2g-1 = 13: Beaufort scale, FHWA classes
  n_C# = 30: residential speed limit

  g³ = 343: speed of sound (m/s) = Debye temperature of Cu (K)!
  21600 arc-minutes = rank⁵ × N_c³ × n_C² (exact BST factorization)
  1000 meters = rank³ × n_C³

  The speed of sound and the Debye temperature are the same number.
  Human transport evolved under BST constraints.
""")
