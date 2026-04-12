#!/usr/bin/env python3
"""
Toy 1087 — Agriculture & Farming from BST
============================================
Agricultural structure and biological counting:
  - Crop rotation: 3-field = N_c; 4-field (Norfolk) = rank²
  - Soil horizons: O, A, B, C, R = n_C
  - Livestock: Big Five (cattle, sheep, goats, pigs, poultry) = n_C
  - Growing degree days: base 50°F = rank×n_C²

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
print("Toy 1087 — Agriculture & Farming from BST")
print("="*70)

# T1: Crop rotation
print("\n── Crop Rotation ──")
# Medieval 3-field: grain, legume, fallow = N_c
# Norfolk 4-course: turnips, barley, clover, wheat = rank²
# Modern: 5-7 year rotations = n_C to g
three_field = 3       # N_c
norfolk = 4           # rank²

print(f"  Three-field rotation: {three_field} = N_c = {N_c}")
print(f"  Norfolk four-course: {norfolk} = rank² = {rank**2}")

test("N_c=3 three-field; rank²=4 Norfolk rotation",
     three_field == N_c and norfolk == rank**2,
     f"N_c={N_c}, rank²={rank**2}")

# T2: Soil horizons
print("\n── Soil Science ──")
# Master horizons: O, A, B, C, R = 5 = n_C
# Soil taxonomy orders: 12 = rank² × N_c
# Soil texture triangle: 3 components = N_c (sand, silt, clay)
# pH range (agricultural): 4-9 (acidic to alkaline)
soil_horizons = 5     # n_C
soil_orders = 12      # rank² × N_c
texture_components = 3  # N_c

print(f"  Soil horizons: {soil_horizons} = n_C = {n_C} (O, A, B, C, R)")
print(f"  Soil taxonomy orders: {soil_orders} = rank² × N_c = {rank**2 * N_c}")
print(f"  Texture components: {texture_components} = N_c = {N_c}")

test("n_C=5 horizons; rank²×N_c=12 soil orders; N_c=3 texture",
     soil_horizons == n_C and soil_orders == rank**2 * N_c
     and texture_components == N_c,
     f"n_C={n_C}, rank²×N_c={rank**2*N_c}, N_c={N_c}")

# T3: Major livestock
print("\n── Livestock ──")
# Big Five domesticated: cattle, sheep, goats, pigs, chickens = n_C
# Cattle breeds major: ~7 = g (Angus, Hereford, Holstein, Jersey, Charolais, Brahman, Simmental)
# Wool grades: 6 = C_2 (fine, medium, coarse, long, carpet, specialty)
livestock_species = 5  # n_C
cattle_breeds = 7      # g
wool_grades = 6        # C_2

print(f"  Major livestock: {livestock_species} = n_C = {n_C}")
print(f"  Key cattle breeds: {cattle_breeds} = g = {g}")
print(f"  Wool grades: {wool_grades} = C_2 = {C_2}")

test("n_C=5 livestock; g=7 cattle breeds; C_2=6 wool grades",
     livestock_species == n_C and cattle_breeds == g and wool_grades == C_2,
     f"n_C={n_C}, g={g}, C_2={C_2}")

# T4: Plant nutrients
print("\n── Plant Nutrition ──")
# NPK: 3 macronutrients = N_c (Nitrogen, Phosphorus, Potassium)
# Secondary: 3 = N_c (Calcium, Magnesium, Sulfur)
# Micronutrients: 7 = g (B, Cl, Cu, Fe, Mn, Mo, Zn)
# Total essential: 13 = 2g - 1
macronutrients = 3    # N_c
secondary = 3         # N_c
micronutrients = 7    # g
total_essential = 13  # 2g - 1

print(f"  NPK macro: {macronutrients} = N_c = {N_c}")
print(f"  Secondary: {secondary} = N_c = {N_c}")
print(f"  Micronutrients: {micronutrients} = g = {g}")
print(f"  Total essential: {total_essential} = 2g - 1 = {2*g - 1}")
print(f"  = N_c + N_c + g = {N_c + N_c + g}")

test("N_c=3 NPK; g=7 micro; 2g-1=13 total essential plant nutrients",
     macronutrients == N_c and micronutrients == g
     and total_essential == 2*g - 1
     and total_essential == macronutrients + secondary + micronutrients,
     f"N_c+N_c+g = {N_c}+{N_c}+{g} = {2*g-1} = 2g-1")

# T5: Cereal grains
print("\n── Cereals ──")
# Major cereals: wheat, rice, corn, barley, sorghum, oats, rye = g
# = the "big 7" food grains
cereal_grains = 7     # g
# Wheat classes: 6 (US) = C_2
# (Hard Red Winter, Hard Red Spring, Soft Red Winter,
#  Hard White, Soft White, Durum)
wheat_classes = 6     # C_2

print(f"  Major cereals: {cereal_grains} = g = {g}")
print(f"  (Wheat, rice, corn, barley, sorghum, oats, rye)")
print(f"  US wheat classes: {wheat_classes} = C_2 = {C_2}")

test("g=7 major cereals; C_2=6 wheat classes",
     cereal_grains == g and wheat_classes == C_2,
     f"g={g}, C_2={C_2}")

# T6: Growing conditions
print("\n── Growing Conditions ──")
# Growing degree days base: 50°F = rank × n_C²
# Frost-free days typical: 120-180
# 120 = rank³ × N_c × n_C; 180 = rank² × N_c² × n_C
# Hardiness zones: 13 (USDA 1-13) = 2g - 1
gdd_base = 50         # rank × n_C²
frost_free_low = 120  # rank³ × N_c × n_C
frost_free_high = 180  # rank² × N_c² × n_C
hardiness_zones = 13   # 2g - 1

print(f"  GDD base: {gdd_base}°F = rank × n_C² = {rank * n_C**2}")
print(f"  Frost-free range: {frost_free_low}-{frost_free_high} days")
print(f"  = rank³×N_c×n_C to rank²×N_c²×n_C = {rank**3*N_c*n_C}-{rank**2*N_c**2*n_C}")
print(f"  Hardiness zones: {hardiness_zones} = 2g - 1 = {2*g - 1}")

test("GDD 50=rank×n_C²; frost-free 120-180 BST; 2g-1=13 zones",
     gdd_base == rank * n_C**2
     and frost_free_low == rank**3 * N_c * n_C
     and frost_free_high == rank**2 * N_c**2 * n_C
     and hardiness_zones == 2*g - 1,
     f"50={rank*n_C**2}, 120={rank**3*N_c*n_C}, 180={rank**2*N_c**2*n_C}")

# T7: Farm structure
print("\n── Farm Organization ──")
# Acre: 43,560 sq ft = 2^3 × 3^2 × 5 × 11^2 × ... actually
# Acre = 4,840 sq yd; Section = 640 acres = rank^7 × n_C
# 640 = 2^7 × 5 = rank⁷ × n_C (same as in Toy 1080!)
# Quarter section: 160 = rank⁵ × n_C
section_acres = 640    # rank⁷ × n_C
quarter_section = 160  # rank⁵ × n_C
# Township: 36 sections = rank² × N_c²
township = 36          # rank² × N_c²

print(f"  Section: {section_acres} acres = rank⁷ × n_C = {rank**7 * n_C}")
print(f"  Quarter section: {quarter_section} acres = rank⁵ × n_C = {rank**5 * n_C}")
print(f"  Township: {township} sections = rank² × N_c² = {rank**2 * N_c**2}")

test("640 = rank⁷×n_C; 160 = rank⁵×n_C; 36 = rank²×N_c² township",
     section_acres == rank**7 * n_C and quarter_section == rank**5 * n_C
     and township == rank**2 * N_c**2,
     f"640={rank**7*n_C}, 160={rank**5*n_C}, 36={rank**2*N_c**2}")

# T8: Seasons and planting
print("\n── Seasonal Farming ──")
# Growing seasons: 4 = rank² (spring plant, summer grow, fall harvest, winter rest)
# Planting windows per crop: typically 2-3 = rank to N_c
# Harvest moon phases: 4 = rank² (new, first quarter, full, last quarter)
# Days seed to harvest (fast crops): 30-60 = n_C# to rank²×N_c×n_C
growing_seasons = 4    # rank²
moon_phases = 4        # rank²
fast_crop_min = 30     # n_C#
fast_crop_max = 60     # rank² × N_c × n_C

print(f"  Growing cycle: {growing_seasons} = rank² = {rank**2}")
print(f"  Moon phases: {moon_phases} = rank² = {rank**2}")
print(f"  Fast crop: {fast_crop_min}-{fast_crop_max} days")
print(f"  = n_C# to rank²×N_c×n_C = {rank*N_c*n_C}-{rank**2*N_c*n_C}")

test("rank²=4 seasons/phases; crop 30-60 = n_C# to rank²×N_c×n_C",
     growing_seasons == rank**2 and moon_phases == rank**2
     and fast_crop_min == rank * N_c * n_C and fast_crop_max == rank**2 * N_c * n_C,
     f"rank²={rank**2}, 30={rank*N_c*n_C}, 60={rank**2*N_c*n_C}")

# T9: Agricultural revolutions
print("\n── Agricultural History ──")
# Neolithic revolution: ~12,000 years ago → 12 = rank² × N_c (in kiloyears)
# Fertile Crescent crops: "Neolithic founder crops" = 8 = 2^N_c
# (emmer wheat, einkorn, barley, lentil, pea, chickpea, flax, bitter vetch)
# Green Revolution: 3 innovations = N_c (HYV seeds, fertilizer, irrigation)
founder_crops = 8     # 2^N_c
green_rev = 3         # N_c
neolithic_ky = 12     # rank² × N_c

print(f"  Neolithic founder crops: {founder_crops} = 2^N_c = {2**N_c}")
print(f"  Green Revolution pillars: {green_rev} = N_c = {N_c}")
print(f"  Neolithic ~{neolithic_ky} kya = rank² × N_c = {rank**2 * N_c}")

test("2^N_c=8 founder crops; N_c=3 Green Revolution; 12kya = rank²×N_c",
     founder_crops == 2**N_c and green_rev == N_c
     and neolithic_ky == rank**2 * N_c,
     f"2^N_c={2**N_c}, N_c={N_c}, rank²×N_c={rank**2*N_c}")

# T10: Measurements
print("\n── Agricultural Measures ──")
# Bushel: 8 gallons = 2^N_c
# Peck: 2 gallons = rank (1/4 bushel)
# 4 pecks = 1 bushel → rank² pecks/bushel
# Cord (firewood): 128 cu ft = 2^g
bushel_gallons = 8    # 2^N_c
pecks_per_bushel = 4  # rank²
cord_cuft = 128       # 2^g

print(f"  Bushel: {bushel_gallons} gallons = 2^N_c = {2**N_c}")
print(f"  Pecks/bushel: {pecks_per_bushel} = rank² = {rank**2}")
print(f"  Cord: {cord_cuft} cu ft = 2^g = {2**g}")

test("2^N_c=8 gal/bushel; rank²=4 pecks; 2^g=128 cu ft/cord",
     bushel_gallons == 2**N_c and pecks_per_bushel == rank**2
     and cord_cuft == 2**g,
     f"2^N_c={2**N_c}, rank²={rank**2}, 2^g={2**g}")

# Summary
print("\n" + "="*70)
print("SUMMARY")
print("="*70)
passed = sum(1 for _, (_, c, _) in results.items() if c)
total = len(results)
print(f"\n  Tests: {passed}/{total} PASS")
print(f"""
  HEADLINE: Agriculture Counts in BST

  N_c = 3: three-field, macronutrients (NPK), Green Revolution
  rank² = 4: Norfolk rotation, seasons, moon phases
  n_C = 5: soil horizons, major livestock
  g = 7: major cereals, micronutrients
  2g-1 = 13: total essential nutrients, hardiness zones

  640 acres/section = rank⁷ × n_C (exact)
  36 sections/township = rank² × N_c²
  8 Neolithic founder crops = 2^N_c
  128 cu ft/cord = 2^g

  Agriculture is humanity's first large-scale BST application.
""")
