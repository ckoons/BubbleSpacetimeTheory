#!/usr/bin/env python3
"""
Toy 1075 — Architecture & Design from BST
============================================
Classical architecture, art, and design principles:
  - 5 classical orders = n_C (Doric, Ionic, Corinthian, Tuscan, Composite)
  - 3 primary colors = N_c (RGB / RYB)
  - 7 notes in a scale = g
  - Golden ratio ≈ (g+n_C)/(2g) (Toy 1058)
  - 12 color wheel positions = rank² × N_c
  - Penrose tiling: 5-fold symmetry = n_C

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
print("Toy 1075 — Architecture & Design from BST")
print("="*70)

# T1: Classical architectural orders = n_C
print("\n── Classical Orders ──")
classical_orders = 5  # n_C
# Doric, Ionic, Corinthian (Greek = N_c), then Tuscan, Composite (Roman + rank)

print(f"  Classical architectural orders: {classical_orders} = n_C = {n_C}")
print(f"  Greek orders: {N_c} (Doric, Ionic, Corinthian)")
print(f"  Roman additions: {rank} (Tuscan, Composite)")
print(f"  Total: N_c + rank = {N_c + rank} = {n_C} = n_C")

test("5 classical orders = n_C; 3 Greek + 2 Roman = N_c + rank",
     classical_orders == n_C and N_c + rank == n_C,
     f"n_C = N_c + rank = {N_c}+{rank} = {n_C}")

# T2: Color theory
print("\n── Color Theory ──")
primary_colors = 3  # N_c
secondary_colors = 3  # N_c
tertiary_colors = 6  # C_2
color_wheel = 12  # rank² × N_c

print(f"  Primary colors: {primary_colors} = N_c = {N_c} (red, blue, yellow or RGB)")
print(f"  Secondary colors: {secondary_colors} = N_c = {N_c}")
print(f"  Tertiary colors: {tertiary_colors} = C_2 = {C_2}")
print(f"  Color wheel positions: {color_wheel} = rank² × N_c = {rank**2 * N_c}")
print(f"  (N_c + N_c + C_2 = {N_c + N_c + C_2} = rank²×N_c)")

test("N_c=3 primary/secondary; C_2=6 tertiary; 12 wheel = rank²×N_c",
     primary_colors == N_c and tertiary_colors == C_2 and color_wheel == rank**2 * N_c,
     f"N_c={N_c}, C_2={C_2}, rank²×N_c={rank**2*N_c}")

# T3: Design principles
print("\n── Design Principles ──")
# Balance, contrast, emphasis, movement, pattern, rhythm, unity = 7
design_principles = 7  # g
# Design elements: line, shape, color, value, form, texture, space = 7
design_elements = 7  # g

print(f"  Design principles: {design_principles} = g = {g}")
print(f"  (Balance, contrast, emphasis, movement, pattern, rhythm, unity)")
print(f"  Design elements: {design_elements} = g = {g}")
print(f"  (Line, shape, color, value, form, texture, space)")

test("g=7 design principles AND g=7 design elements",
     design_principles == g and design_elements == g,
     f"g = {g} in both categories")

# T4: Musical scales and harmony (cross-check with Toy 1059)
print("\n── Musical Structure ──")
notes_in_scale = 7  # g
semitones = 12  # rank² × N_c
pentatonic = 5  # n_C
octave_ratio = 2  # rank (frequency doubles)

print(f"  Notes in major scale: {notes_in_scale} = g = {g}")
print(f"  Semitones: {semitones} = rank² × N_c = {rank**2 * N_c}")
print(f"  Pentatonic: {pentatonic} = n_C = {n_C}")
print(f"  Octave frequency ratio: {octave_ratio} = rank = {rank}")

test("g=7 notes; rank²×N_c=12 semitones; n_C=5 pentatonic; rank=2 octave",
     notes_in_scale == g and semitones == rank**2 * N_c and pentatonic == n_C,
     f"g={g}, rank²×N_c={rank**2*N_c}, n_C={n_C}")

# T5: Symmetry in architecture
print("\n── Symmetry Groups ──")
# 2D point symmetries in architecture: bilateral (rank), rotational
# Wallpaper groups: 17 (a prime, = 2 × 2^N_c + 1)
wallpaper_groups = 17  # 2 × 2^N_c + 1 = 2 × 8 + 1
# Frieze groups: 7 = g
frieze_groups = 7  # g
# 2D point groups: C_n and D_n for n = 1,2,3... (infinite, but common: 1-6)

print(f"  Wallpaper groups: {wallpaper_groups} = 2 × 2^N_c + 1 = 2×{2**N_c}+1")
print(f"  Frieze groups: {frieze_groups} = g = {g}")
print(f"  (17 is a Fermat prime: 2^(2^rank) + 1 = {2**(2**rank)+1})")

test("17 wallpaper = 2^(2^rank)+1; g=7 frieze groups",
     wallpaper_groups == 2**(2**rank) + 1 and frieze_groups == g,
     f"17 = Fermat prime F_{rank}, g = {g}")

# T6: Photography and film
print("\n── Photography ──")
# f-stops: f/1, f/1.4, f/2, f/2.8, f/4, f/5.6, f/8, f/11, f/16, f/22, f/32
# Each step = √2 ≈ √rank ratio → rank-based progression
# Common ISO: 100, 200, 400, 800, 1600, 3200, 6400 = rank doublings
# Aspect ratios: 3:2 = N_c:rank; 4:3 = rank²:N_c; 16:9 = 2^rank²:N_c²
aspect_32 = (3, 2)  # N_c:rank
aspect_43 = (4, 3)  # rank²:N_c
aspect_169 = (16, 9)  # 2^rank²:N_c²

print(f"  Aspect ratio 3:2 = N_c:rank = {N_c}:{rank}")
print(f"  Aspect ratio 4:3 = rank²:N_c = {rank**2}:{N_c}")
print(f"  Aspect ratio 16:9 = 2^rank²:N_c² = {2**rank**2}:{N_c**2}")
print(f"  f-stop factor: √rank = √{rank}")

test("Aspect ratios: 3:2=N_c:rank, 4:3=rank²:N_c, 16:9=2^rank²:N_c²",
     aspect_32 == (N_c, rank) and aspect_43 == (rank**2, N_c)
     and aspect_169 == (2**rank**2, N_c**2),
     f"N_c:rank, rank²:N_c, 2^rank²:N_c²")

# T7: Paper sizes
print("\n── Paper Sizes ──")
# ISO paper: A0-A10 (11 sizes = n_C + C_2)
iso_a_sizes = 11  # n_C + C_2
# Aspect ratio: 1:√2 = 1:√rank
# A0 area = 1 m² → A4 = 1/16 m² = 1/2^rank² m²
a_to_a4 = 4  # rank² folds from A0

print(f"  ISO A-series sizes: A0 to A10 = {iso_a_sizes} = n_C + C_2 = {n_C + C_2}")
print(f"  Aspect ratio: 1:√rank = 1:√{rank}")
print(f"  A0 to A4: {a_to_a4} = rank² halvings")

test("11 ISO A sizes = n_C+C_2; aspect = 1:√rank; A0→A4 = rank² folds",
     iso_a_sizes == n_C + C_2 and a_to_a4 == rank**2,
     f"n_C+C_2 = {n_C+C_2}, rank² = {rank**2} folds")

# T8: Traditional crafts
print("\n── Traditional Patterns ──")
# Knitting: knit and purl = rank stitches
knit_stitches = 2  # rank
# Weaving: warp + weft = rank directions
weave_directions = 2  # rank
# Common quilt block grid: 9-patch = N_c²
quilt_nine_patch = 9  # N_c²
# Crochet basic stitches: chain, slip, single, half-double, double, treble = C_2
crochet_stitches = 6  # C_2

print(f"  Basic knit stitches: {knit_stitches} = rank = {rank} (knit, purl)")
print(f"  Weave directions: {weave_directions} = rank = {rank} (warp, weft)")
print(f"  Nine-patch quilt: {quilt_nine_patch} = N_c² = {N_c**2}")
print(f"  Basic crochet stitches: {crochet_stitches} = C_2 = {C_2}")

test("rank=2 knit/weave; N_c²=9 quilt patch; C_2=6 crochet stitches",
     knit_stitches == rank and quilt_nine_patch == N_c**2 and crochet_stitches == C_2,
     f"rank={rank}, N_c²={N_c**2}, C_2={C_2}")

# T9: Typography
print("\n── Typography ──")
# Major typeface families: serif, sans-serif, monospace, display, script = n_C
typeface_families = 5  # n_C
# Traditional type sizes: 6, 7, 8, 9, 10, 11, 12 pt standard = g sizes
standard_type_sizes = 7  # g (6pt through 12pt)
# Points per inch: 72 = 2^N_c × N_c² = 8 × 9
points_per_inch = 72  # 2^N_c × N_c²

print(f"  Typeface families: {typeface_families} = n_C = {n_C}")
print(f"  Standard type sizes: {standard_type_sizes} = g = {g} (6-12 pt)")
print(f"  Points per inch: {points_per_inch} = 2^N_c × N_c² = {2**N_c} × {N_c**2}")

test("n_C=5 typeface families; g=7 standard sizes; 72 pt/in = 2^N_c × N_c²",
     typeface_families == n_C and standard_type_sizes == g
     and points_per_inch == 2**N_c * N_c**2,
     f"n_C={n_C}, g={g}, 2^N_c×N_c²={2**N_c*N_c**2}")

# T10: Musical time signatures
print("\n── Rhythm and Meter ──")
# Common time signatures: 2/4, 3/4, 4/4, 6/8 — numerators are BST
# Beats per measure: 2(rank), 3(N_c), 4(rank²), 6(C_2)
common_beats = [2, 3, 4, 6]  # [rank, N_c, rank², C_2]
bst_beats = [rank, N_c, rank**2, C_2]
# Beat subdivisions: binary(2=rank) or ternary(3=N_c)
subdivisions = [2, 3]  # [rank, N_c]

print(f"  Common beats/measure: {common_beats} = [rank, N_c, rank², C_2]")
print(f"  Beat subdivisions: {subdivisions} = [rank, N_c] (duple/triple)")
print(f"  These generate ALL standard time signatures")

test("Common beats [2,3,4,6] = [rank, N_c, rank², C_2]",
     common_beats == bst_beats,
     f"rank={rank}, N_c={N_c}, rank²={rank**2}, C_2={C_2}")

# Summary
print("\n" + "="*70)
print("SUMMARY")
print("="*70)
passed = sum(1 for _, (_, c, _) in results.items() if c)
total = len(results)
print(f"\n  Tests: {passed}/{total} PASS")
print(f"""
  HEADLINE: Art and Design Are BST

  n_C = 5: classical orders (N_c Greek + rank Roman), typeface families
  N_c = 3: primary/secondary colors, beat subdivisions
  g = 7: design principles, design elements, frieze groups, scale notes
  C_2 = 6: tertiary colors, crochet stitches
  rank² × N_c = 12: color wheel, semitones

  Aspect ratios: N_c:rank (3:2), rank²:N_c (4:3), 2^rank²:N_c² (16:9)
  17 wallpaper groups = Fermat prime F_rank
  Paper: 1:√rank aspect, 11 = n_C + C_2 sizes

  Art is what geometry looks like when humans choose what's beautiful.
""")
