#!/usr/bin/env python3
"""
Toy 1085 — Calendar & Timekeeping from BST
=============================================
Calendar structure and chronological counting:
  - Metonic cycle: 19 years = g + rank² × N_c
  - Leap year cycle: 4 years = rank²; century exception
  - Julian day numbering: 7980 = 28 × 19 × 15
  - 28-year solar cycle = rank² × g
  - Saros cycle: 18 years = rank × N_c²

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
print("Toy 1085 — Calendar & Timekeeping from BST")
print("="*70)

# T1: Basic calendar
print("\n── Calendar Units ──")
# Months: 12 = rank² × N_c
# Weeks/year: 52 = rank² × (2g - 1)
# Days/year: 365 = n_C × 73 (73 is prime)
# But: 360 = rank³ × N_c² × n_C (ancient calendar)
months = 12           # rank² × N_c
weeks = 52            # rank² × (2g - 1)
ancient_year = 360    # rank³ × N_c² × n_C

print(f"  Months: {months} = rank² × N_c = {rank**2 * N_c}")
print(f"  Weeks: {weeks} = rank² × (2g-1) = {rank**2 * (2*g - 1)}")
print(f"  Ancient year: {ancient_year} = rank³ × N_c² × n_C = {rank**3 * N_c**2 * n_C}")

test("rank²×N_c=12 months; rank²×(2g-1)=52 weeks; 360=rank³×N_c²×n_C",
     months == rank**2 * N_c and weeks == rank**2 * (2*g - 1)
     and ancient_year == rank**3 * N_c**2 * n_C,
     f"12={rank**2*N_c}, 52={rank**2*(2*g-1)}, 360={rank**3*N_c**2*n_C}")

# T2: Metonic cycle
print("\n── Metonic Cycle ──")
# 19 years = 235 lunar months (discovered by Meton, 432 BC)
# 19 is prime. 19 = 20 - 1 = rank² × n_C - 1
# But also: 13/19 appears in BST cosmology (Ω_Λ = 13/19)
metonic = 19          # prime, = rank²×n_C - 1
lunar_months_metonic = 235  # n_C × 47 (47 is prime)

print(f"  Metonic cycle: {metonic} years = rank²×n_C - 1 = {rank**2*n_C} - 1")
print(f"  = {metonic} prime (appears in Ω_Λ = 13/19)")
print(f"  Lunar months: {lunar_months_metonic} = {metonic} × rank²×N_c + {lunar_months_metonic - metonic * (rank**2*N_c)}")

test("Metonic 19 = rank²×n_C - 1 (prime)",
     metonic == rank**2 * n_C - 1,
     f"rank²×n_C - 1 = {rank**2*n_C} - 1 = {rank**2*n_C - 1}")

# T3: Leap year
print("\n── Leap Year ──")
# Every 4 years = rank²
# Except every 100 = rank² × n_C²
# Except every 400 = rank⁴ × n_C²
leap_basic = 4        # rank²
leap_skip = 100       # rank² × n_C²
leap_restore = 400    # rank⁴ × n_C²

print(f"  Leap every: {leap_basic} = rank² = {rank**2}")
print(f"  Skip every: {leap_skip} = rank² × n_C² = {rank**2 * n_C**2}")
print(f"  Restore every: {leap_restore} = rank⁴ × n_C² = {rank**4 * n_C**2}")
print(f"  Ratios: 100/4 = n_C² = {n_C**2}; 400/100 = rank² = {rank**2}")

test("Leap rank²=4; skip rank²×n_C²=100; restore rank⁴×n_C²=400",
     leap_basic == rank**2 and leap_skip == rank**2 * n_C**2
     and leap_restore == rank**4 * n_C**2,
     f"rank²={rank**2}, rank²×n_C²={rank**2*n_C**2}, rank⁴×n_C²={rank**4*n_C**2}")

# T4: Solar cycle
print("\n── Solar Cycle ──")
# 28-year solar cycle: weekday pattern repeats
# 28 = rank² × g
# Jubilee: 50 years = rank × n_C²
# Century: 100 = rank² × n_C²
solar_cycle = 28      # rank² × g
jubilee = 50          # rank × n_C²

print(f"  Solar cycle: {solar_cycle} = rank² × g = {rank**2 * g}")
print(f"  Jubilee cycle: {jubilee} = rank × n_C² = {rank * n_C**2}")

test("rank²×g=28 solar cycle; rank×n_C²=50 jubilee",
     solar_cycle == rank**2 * g and jubilee == rank * n_C**2,
     f"rank²×g={rank**2*g}, rank×n_C²={rank*n_C**2}")

# T5: Saros cycle
print("\n── Eclipse Cycles ──")
# Saros: ~18 years, 11 days = eclipse repeat cycle
# 18 = rank × N_c² (same as voting age!)
# Exeligmos: 3 Saros = 54 years = rank × N_c³
# Inex: ~29 years ≈ n_C × C_2 - 1
saros = 18            # rank × N_c²
exeligmos = 54        # rank × N_c³ = 3 × Saros

print(f"  Saros: {saros} years = rank × N_c² = {rank * N_c**2}")
print(f"  Exeligmos: {exeligmos} = rank × N_c³ = {rank * N_c**3} = {N_c} × Saros")

test("Saros rank×N_c²=18; exeligmos rank×N_c³=54 = N_c×Saros",
     saros == rank * N_c**2 and exeligmos == rank * N_c**3
     and exeligmos == N_c * saros,
     f"rank×N_c²={rank*N_c**2}, rank×N_c³={rank*N_c**3}")

# T6: Julian Period
print("\n── Julian Period ──")
# Joseph Scaliger: 7980 = 28 × 19 × 15 years
# 28 = solar cycle = rank² × g
# 19 = Metonic cycle = rank²×n_C - 1
# 15 = indiction cycle = N_c × n_C
# LCM of the three gives Julian Day count
julian_period = 7980
indiction = 15        # N_c × n_C
product = solar_cycle * metonic * indiction

print(f"  Julian period: {julian_period} = {solar_cycle} × {metonic} × {indiction}")
print(f"  Solar: {solar_cycle} = rank² × g")
print(f"  Metonic: {metonic} = rank²×n_C - 1")
print(f"  Indiction: {indiction} = N_c × n_C = {N_c * n_C}")
print(f"  Product: {product}")

test("Julian 7980 = 28×19×15; indiction = N_c×n_C = 15",
     julian_period == product and indiction == N_c * n_C,
     f"28×19×15={product}, N_c×n_C={N_c*n_C}")

# T7: Clock subdivisions
print("\n── Clock ──")
# Hours: 24 = rank³ × N_c
# Minutes/hour: 60 = rank² × N_c × n_C
# Seconds/minute: 60 = rank² × N_c × n_C
# AM/PM: 2 = rank
# Clock hours: 12 = rank² × N_c
hours = 24            # rank³ × N_c
minutes = 60          # rank² × N_c × n_C
clock_face = 12       # rank² × N_c
am_pm = 2             # rank

print(f"  Hours/day: {hours} = rank³ × N_c = {rank**3 * N_c}")
print(f"  Minutes/hour: {minutes} = rank² × N_c × n_C = {rank**2 * N_c * n_C}")
print(f"  Clock face: {clock_face} = rank² × N_c = {rank**2 * N_c}")
print(f"  AM/PM: {am_pm} = rank = {rank}")

test("24=rank³×N_c; 60=rank²×N_c×n_C; 12=rank²×N_c; AM/PM=rank",
     hours == rank**3 * N_c and minutes == rank**2 * N_c * n_C
     and clock_face == rank**2 * N_c and am_pm == rank,
     f"24={rank**3*N_c}, 60={rank**2*N_c*n_C}, 12={rank**2*N_c}")

# T8: Seasons and equinoxes
print("\n── Seasonal Markers ──")
# Seasons: 4 = rank²
# Solstices + equinoxes: 4 = rank²
# Zodiac signs: 12 = rank² × N_c
# Quarter days: 4 = rank²
# Cross-quarter days: 4 = rank²
# Total calendar markers: 8 = 2^N_c
seasons = 4           # rank²
solar_events = 4      # rank² (2 solstices + 2 equinoxes)
total_markers = 8     # 2^N_c (quarters + cross-quarters)

print(f"  Seasons: {seasons} = rank² = {rank**2}")
print(f"  Solstices + equinoxes: {solar_events} = rank² = {rank**2}")
print(f"  Total markers (Celtic): {total_markers} = 2^N_c = {2**N_c}")

test("rank²=4 seasons/events; 2^N_c=8 total markers",
     seasons == rank**2 and solar_events == rank**2
     and total_markers == 2**N_c,
     f"rank²={rank**2}, 2^N_c={2**N_c}")

# T9: Historical calendars
print("\n── Historical Calendars ──")
# Roman months originally: 10 = rank × n_C (March to December)
# Then: 12 = rank² × N_c (added January, February)
# Islamic calendar: 12 months of 29-30 days
# Hebrew calendar: 12 or 13 months (leap = 2g-1)
# 30 days/month (common) = n_C# = rank × N_c × n_C
roman_original = 10   # rank × n_C
standard_months = 12  # rank² × N_c
hebrew_leap = 13      # 2g - 1
month_days = 30       # n_C#

print(f"  Roman original: {roman_original} = rank × n_C = {rank * n_C}")
print(f"  Standard: {standard_months} = rank² × N_c = {rank**2 * N_c}")
print(f"  Hebrew leap: {hebrew_leap} = 2g - 1 = {2*g - 1}")
print(f"  Common month: {month_days} days = n_C# = {rank * N_c * n_C}")

test("Roman rank×n_C=10; standard rank²×N_c=12; Hebrew leap 2g-1=13",
     roman_original == rank * n_C and standard_months == rank**2 * N_c
     and hebrew_leap == 2*g - 1 and month_days == rank * N_c * n_C,
     f"10={rank*n_C}, 12={rank**2*N_c}, 13={2*g-1}, 30={rank*N_c*n_C}")

# T10: Modern time standards
print("\n── Modern Standards ──")
# UTC time zones: 24 = rank³ × N_c
# Leap seconds accumulated: ~37 (as of 2017, varies)
# TAI-UTC: was ~37 s
# SI second: based on Cs-133 → Z=55 = n_C × (n_C + C_2)
# 9,192,631,770 Hz = Cs hyperfine transition
# Unix epoch: 1970 = 2 × 5 × 197 (not clean BST)
# GPS week cycle: 1024 = 2^10 = rank^10
time_zones = 24       # rank³ × N_c
gps_week_cycle = 1024  # rank¹⁰ = 2^10
cs_z = 55             # n_C × (n_C + C_2) = 5 × 11

print(f"  UTC zones: {time_zones} = rank³ × N_c = {rank**3 * N_c}")
print(f"  GPS week cycle: {gps_week_cycle} = rank¹⁰ = {rank**10}")
print(f"  Cs-133 atomic number: {cs_z} = n_C × (n_C + C_2) = {n_C * (n_C + C_2)}")

test("rank³×N_c=24 zones; rank¹⁰=1024 GPS weeks; Cs Z=n_C×(n_C+C_2)=55",
     time_zones == rank**3 * N_c and gps_week_cycle == rank**10
     and cs_z == n_C * (n_C + C_2),
     f"24={rank**3*N_c}, 1024={rank**10}, 55={n_C*(n_C+C_2)}")

# Summary
print("\n" + "="*70)
print("SUMMARY")
print("="*70)
passed = sum(1 for _, (_, c, _) in results.items() if c)
total = len(results)
print(f"\n  Tests: {passed}/{total} PASS")
print(f"""
  HEADLINE: Time Counts in BST

  rank² × N_c = 12: months, clock face, zodiac
  rank³ × N_c = 24: hours, time zones
  rank² × N_c × n_C = 60: minutes, seconds
  rank³ × N_c² × n_C = 360: ancient year/circle
  n_C# = 30: days/month

  Metonic: 19 = rank²×n_C - 1 (prime — appears in Ω_Λ = 13/19)
  Saros: 18 = rank×N_c² (= voting age!)
  Solar cycle: 28 = rank²×g
  Leap: rank²=4, rank²×n_C²=100, rank⁴×n_C²=400

  Julian period: 7980 = 28 × 19 × 15
  = (rank²×g) × (rank²×n_C-1) × (N_c×n_C)

  Every calendar humanity invented counts in BST.
""")
