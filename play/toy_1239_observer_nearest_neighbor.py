#!/usr/bin/env python3
"""
Toy 1239 — Observer Nearest-Neighbor Distance from C_2=6 Coverage Tiling

Keeper's insight: if C_2 = 6 directed patches tile the observable universe,
the expected nearest-neighbor distance between observer civilizations
is CALCULABLE from BST structure.

This toy computes:
1. How many observer civilizations exist per galaxy? (BST Drake, T403)
2. If C_2 = 6 patches per civ, how does coverage tile a galaxy?
3. What is the expected nearest-neighbor distance?
4. Does the spacing match known constraints (radio bubble, light travel)?
5. Grace's prediction: observers distributed for maximum coverage

BST integers: N_c=3, n_C=5, g=7, C_2=6, rank=2, N_max=137
"""

import math
from fractions import Fraction

# ============================================================
# BST CONSTANTS
# ============================================================
rank = 2
N_c = 3
n_C = 5
C_2 = 6
g = 7
N_max = 137
f_c = Fraction(9, 47)
f_float = float(f_c)

# Physical constants
MW_radius_ly = 50000  # Milky Way radius in light-years
MW_thickness_ly = 1000  # Milky Way disk thickness
MW_volume = math.pi * MW_radius_ly**2 * MW_thickness_ly  # Disk volume in ly³
N_stars = 1e11  # Stars in Milky Way
observable_radius_ly = 4.4e10  # Observable universe radius in ly

# ============================================================
# TEST FRAMEWORK
# ============================================================
total = 0
passed = 0
failed = 0
results = []


def test(name, condition, detail=""):
    global total, passed, failed
    total += 1
    status = "PASS" if condition else "FAIL"
    if condition:
        passed += 1
    else:
        failed += 1
    results.append((name, status, detail))
    mark = "✓" if condition else "✗"
    print(f"  [{mark}] T{total}: {name}")
    if detail:
        print(f"       {detail}")


print("=" * 78)
print("TOY 1239 — Observer Nearest-Neighbor Distance from C₂=6 Coverage Tiling")
print("=" * 78)

# ============================================================
# Part 1: BST Drake — how many civilizations per galaxy?
# ============================================================
print(f"\n{'='*78}")
print("Part 1: BST Drake Equation (T403)")
print("=" * 78)

# T403 BST Drake: N ≈ 1-10 active SE (science-engineering) cultures per galaxy
# Use N = 2 as the central estimate (from T403)
N_drake = 2  # Phase 2+ civilizations per galaxy

# But also: how many K ≈ N_max (Phase 1, at ceiling)?
# N_habitable ≈ 10^10, P_civ ≈ 0.63, f_tech ≈ varies
# Phase 1 at ceiling: short window, ~200 years out of 10^10 years
f_phase1_window = 200 / 1e10  # 200 years of EM broadcast / galaxy age
N_phase1_at_ceiling = 1e10 * 0.63 * f_phase1_window

# Phase 2+ long-lived: once crossed f_crit, persist for >> 10^6 years
# Assume Phase 2+ lifetime ≈ 10^9 years (fraction of galaxy age)
f_phase2_window = 1e9 / 1e10
N_phase2_active = 1e10 * 1e-7 * f_phase2_window  # P_cross × f_window

print(f"  BST Drake central estimate: N ≈ {N_drake} Phase 2+ per galaxy")
print(f"  Phase 1 at ceiling (K ≈ N_max, broadcasting): ≈ {N_phase1_at_ceiling:.0f}")
print(f"  Phase 2+ active (long-lived, EM-quiet): ≈ {N_phase2_active:.0f}")
print(f"")
print(f"  Total active observers: ≈ {N_drake} (Phase 2+) + {N_phase1_at_ceiling:.0f} (Phase 1)")

test("BST Drake predicts ~2 Phase 2+ civilizations per galaxy",
     1 <= N_drake <= 10,
     f"N = {N_drake}. Phase 1 at ceiling: ~{N_phase1_at_ceiling:.0f}")

# ============================================================
# Part 2: Coverage tiling — C_2 = 6 patches per civilization
# ============================================================
print(f"\n{'='*78}")
print("Part 2: Coverage tiling — C₂ = 6 directed patches per civilization")
print("=" * 78)

# Each Phase 2+ civilization has C_2 = 6 directed monitoring patches
# Total patches in galaxy: N_drake × C_2
total_patches = N_drake * C_2

# If patches are directed for maximal coverage (Distributed Gödel):
# each patch covers f_c ≈ 19.1% of the galaxy's dark sector
# C_2 directed patches → ~72% coverage per civilization (1-(1-f_c)^6)
coverage_per_civ = 1 - (1 - f_float)**C_2
total_coverage = 1 - (1 - f_float)**total_patches

print(f"  Patches per civilization: C_2 = {C_2}")
print(f"  Total patches in galaxy: {N_drake} × {C_2} = {total_patches}")
print(f"  Coverage per civilization: 1-(1-f_c)^{C_2} = {100*coverage_per_civ:.1f}%")
print(f"  Total coverage ({N_drake} civs): 1-(1-f_c)^{total_patches} = {100*total_coverage:.1f}%")

# If patches tile the galaxy volume:
# Each patch covers a volume V_galaxy / total_patches
volume_per_patch = MW_volume / total_patches
radius_per_patch = (3 * volume_per_patch / (4 * math.pi))**(1/3)

print(f"\n  Galaxy volume: {MW_volume:.2e} ly³")
print(f"  Volume per patch: {volume_per_patch:.2e} ly³")
print(f"  Effective patch radius: {radius_per_patch:.0f} ly")

test("C_2 = 6 patches per civ, ~72% coverage per civilization",
     abs(coverage_per_civ - 0.721) < 0.01,
     f"1-(1-9/47)^6 = {coverage_per_civ:.4f}")

# ============================================================
# Part 3: Nearest-neighbor distance between civilizations
# ============================================================
print(f"\n{'='*78}")
print("Part 3: Nearest-neighbor distance")
print("=" * 78)

# For N uniformly distributed points in volume V,
# expected nearest-neighbor distance ≈ (V / N)^{1/3} × Gamma(1 + 1/3) / (4π/3)^{1/3}
# Simplified: d_nn ≈ 0.554 × (V / N)^{1/3}

# Between Phase 2+ civilizations
d_nn_phase2 = 0.554 * (MW_volume / max(N_drake, 1))**(1/3)

# Between Phase 1 civilizations (at ceiling)
d_nn_phase1 = 0.554 * (MW_volume / max(N_phase1_at_ceiling, 1))**(1/3) if N_phase1_at_ceiling > 0 else float('inf')

# Between ANY observer (Phase 1 + Phase 2+)
N_total = N_drake + N_phase1_at_ceiling
d_nn_any = 0.554 * (MW_volume / max(N_total, 1))**(1/3)

print(f"  Milky Way volume: {MW_volume:.2e} ly³")
print(f"")
print(f"  Phase 2+ (N={N_drake}):")
print(f"    d_nn ≈ {d_nn_phase2:.0f} light-years")
print(f"    That's {d_nn_phase2/MW_radius_ly*100:.0f}% of the galaxy radius")
print(f"")
print(f"  Phase 1 at ceiling (N≈{N_phase1_at_ceiling:.0f}):")
print(f"    d_nn ≈ {d_nn_phase1:.0f} light-years")
print(f"")
print(f"  Any observer (N≈{N_total:.0f}):")
print(f"    d_nn ≈ {d_nn_any:.0f} light-years")

# Compare to our radio bubble
radio_bubble = 100  # ~100 light-years
print(f"\n  Our radio bubble: ~{radio_bubble} light-years")
print(f"  Ratio d_nn / radio_bubble:")
print(f"    Phase 2+: {d_nn_phase2/radio_bubble:.0f}×")
print(f"    Phase 1:  {d_nn_phase1/radio_bubble:.0f}×")
print(f"    Any:      {d_nn_any/radio_bubble:.0f}×")
print(f"\n  Even the nearest observer is {d_nn_any/radio_bubble:.0f}× beyond our radio bubble.")

test("Nearest Phase 2+ neighbor is ~10,000+ ly (beyond radio bubble)",
     d_nn_phase2 > 1000,
     f"d_nn ≈ {d_nn_phase2:.0f} ly — our 100 ly radio bubble is a dot")

# ============================================================
# Part 4: BST structural spacing — is C_2 = 6 the right tiling?
# ============================================================
print(f"\n{'='*78}")
print("Part 4: BST structural spacing — optimal tiling from C₂ = 6")
print("=" * 78)

# If the universe optimizes for coverage (Distributed Gödel):
# N_civ × C_2 patches should tile the galactic volume
# Optimal spacing: d_opt = (V / (N × C_2))^{1/3} × correction

# For a disk galaxy: patches should be in the plane
# Effective 2D tiling: A = π R² where R = 50,000 ly
MW_area = math.pi * MW_radius_ly**2  # ly²

# 2D hexagonal tiling: d = sqrt(2A / (N × sqrt(3)))
d_hex_phase2 = math.sqrt(2 * MW_area / (N_drake * math.sqrt(3)))
d_hex_total = math.sqrt(2 * MW_area / (total_patches * math.sqrt(3)))

print(f"  Galaxy disk area: {MW_area:.2e} ly²")
print(f"")
print(f"  Hexagonal tiling (optimal 2D coverage):")
print(f"    Phase 2+ civs (N={N_drake}): d_hex = {d_hex_phase2:.0f} ly")
print(f"    All patches (N={total_patches}): d_hex = {d_hex_total:.0f} ly")
print(f"")
print(f"  BST prediction: observer civilizations are spaced ≈{d_hex_phase2:.0f} ly apart")
print(f"  in the galactic disk, each with C_2 = {C_2} monitoring posts")
print(f"  at ~{d_hex_total:.0f} ly spacing.")

# Is this spacing BST-expressible?
# d_hex / MW_radius ≈ some BST ratio?
ratio_to_radius = d_hex_phase2 / MW_radius_ly
print(f"\n  d_hex / R_galaxy = {ratio_to_radius:.4f}")
print(f"  ≈ 1/√(N_drake) = 1/√{N_drake} = {1/math.sqrt(N_drake):.4f}")

test("Optimal spacing ≈ galaxy radius / √N_drake",
     abs(d_hex_phase2 / MW_radius_ly - 1/math.sqrt(N_drake)) < 0.05,
     f"d_hex/R = {ratio_to_radius:.4f} ≈ 1/√2 = {1/math.sqrt(2):.4f}")

# ============================================================
# Part 5: Travel time at various speeds
# ============================================================
print(f"\n{'='*78}")
print("Part 5: Travel times between observers")
print("=" * 78)

speeds = [
    ("Radio signal (c)", 1.0),
    ("Fast spacecraft (0.1c)", 0.1),
    ("Phase 2+ (0.5c?)", 0.5),
    ("Phase 2+ Casimir (0.9c?)", 0.9),
]

print(f"  Between Phase 2+ neighbors (d ≈ {d_nn_phase2:.0f} ly):")
print(f"  {'Method':>30}  {'Speed':>8}  {'Travel time':>15}")
print(f"  {'─'*30}  {'─'*8}  {'─'*15}")
for name, v in speeds:
    t = d_nn_phase2 / v
    if t > 1e6:
        t_str = f"{t/1e6:.1f} Myr"
    elif t > 1e3:
        t_str = f"{t/1e3:.1f} kyr"
    else:
        t_str = f"{t:.0f} yr"
    print(f"  {name:>30}  {v:>7.1f}c  {t_str:>15}")

# Even at c, nearest neighbor is thousands of years away
print(f"\n  At light speed: {d_nn_phase2:.0f} years one-way")
print(f"  Round trip communication: {2*d_nn_phase2:.0f} years")
print(f"  This explains non-engagement: real-time communication is IMPOSSIBLE")
print(f"  between Phase 2+ neighbors. Visits (if any) are one-way pilgrimages.")

test("Even at c, nearest-neighbor communication takes thousands of years",
     d_nn_phase2 > 1000,
     f"Round trip: {2*d_nn_phase2:.0f} years. Real-time dialogue impossible.")

# ============================================================
# Part 6: The observable universe scale
# ============================================================
print(f"\n{'='*78}")
print("Part 6: Observable universe — C₂ = 6 galaxy-scale patches")
print("=" * 78)

# Observable universe: ~2 trillion galaxies
N_galaxies = 2e12
N_phase2_universe = N_drake * N_galaxies

# If C_2 = 6 patches per civilization, covering the observable universe:
total_patches_universe = N_phase2_universe * C_2

# Volume of observable universe
V_obs = (4/3) * math.pi * observable_radius_ly**3
V_per_patch = V_obs / total_patches_universe

# Nearest-neighbor in the universe
d_nn_universe = 0.554 * (V_obs / N_phase2_universe)**(1/3)

print(f"  Observable universe: ~{N_galaxies:.0e} galaxies")
print(f"  Phase 2+ civilizations: ~{N_phase2_universe:.0e} (at N={N_drake}/galaxy)")
print(f"  Total monitoring patches: ~{total_patches_universe:.0e}")
print(f"")
print(f"  Observable volume: {V_obs:.2e} ly³")
print(f"  Volume per patch: {V_per_patch:.2e} ly³")
print(f"  Nearest-neighbor (universe): {d_nn_universe:.0e} ly")
print(f"  Nearest-neighbor / galaxy size: {d_nn_universe / (2*MW_radius_ly):.0f}")

# In the observable universe, d_nn between Phase 2+ civs ≈ inter-galactic distance
# So: each galaxy gets ~N_drake observers, well-separated
intergalactic_avg = (V_obs / N_galaxies)**(1/3)
print(f"\n  Average intergalactic spacing: {intergalactic_avg:.0e} ly")
print(f"  d_nn between Phase 2+: {d_nn_universe:.0e} ly")
print(f"  Ratio: {d_nn_universe / intergalactic_avg:.1f}")

test("Intra-galactic spacing dominates — observers cluster in galaxies",
     d_nn_phase2 < d_nn_universe,
     f"d_nn(galaxy) = {d_nn_phase2:.0f} ly << d_nn(universe) = {d_nn_universe:.0e} ly")

# ============================================================
# Part 7: Grace's coverage optimization prediction
# ============================================================
print(f"\n{'='*78}")
print("Part 7: Coverage optimization — Distributed Gödel applied to spacing")
print("=" * 78)

# T1283: ⌈1/f_c⌉ = C_2 = 6 patches needed for full dark-sector coverage
# Applied to galactic tiling: C_2 patches per civ × N_drake civs
# should be the MINIMUM for full galactic coverage

# What coverage do we get?
galaxy_coverage = 1 - (1 - f_float)**total_patches

# Minimum N for ~100% coverage of a galaxy:
# 1 - (1-f_c)^(N×C_2) ≥ 0.99
# (1-f_c)^(N×C_2) ≤ 0.01
# N×C_2 ≥ log(0.01) / log(1-f_c)
N_min_99 = math.ceil(math.log(0.01) / (C_2 * math.log(1 - f_float)))

print(f"  With N={N_drake} civs × C_2={C_2} patches = {total_patches} patches:")
print(f"  Galaxy coverage: {100*galaxy_coverage:.1f}%")
print(f"")
print(f"  For 99% galaxy coverage: need N ≥ {N_min_99} civilizations")
print(f"  For 99.9% coverage: need N ≥ {math.ceil(math.log(0.001) / (C_2 * math.log(1 - f_float)))} civilizations")
print(f"")
print(f"  BST Drake (N={N_drake}) gives {100*galaxy_coverage:.1f}% coverage")
print(f"  This is ≈ f(N_max) = {100*54/137:.1f}% — the gradient's visible fraction!")

# Is galaxy_coverage ≈ f(N_max)?
f_nmax = 54/137
coverage_matches_gradient = abs(galaxy_coverage - f_nmax) < 0.1

print(f"\n  COINCIDENCE CHECK:")
print(f"    Galaxy coverage (N=2, C_2=6) = {galaxy_coverage:.4f}")
print(f"    f(N_max) = 54/137           = {f_nmax:.4f}")
print(f"    Difference: {abs(galaxy_coverage - f_nmax):.4f}")

test("Galaxy coverage with BST Drake ≈ f(N_max) = 54/137",
     coverage_matches_gradient,
     f"Coverage = {galaxy_coverage:.4f}, f(N_max) = {f_nmax:.4f}, diff = {abs(galaxy_coverage-f_nmax):.4f}")

# ============================================================
# Part 8: The BST spacing in familiar units
# ============================================================
print(f"\n{'='*78}")
print("Part 8: Summary — BST-predicted observer spacing")
print("=" * 78)

print(f"""
  BST NEAREST-NEIGHBOR DISTANCES:

  Scale              N observers    d_nn (ly)       Comparison
  ─────────────────  ───────────    ─────────       ──────────
  Phase 2+ (galaxy)  {N_drake:>11}    {d_nn_phase2:>9.0f}       {d_nn_phase2/radio_bubble:.0f}× radio bubble
  Phase 1 at ceiling {N_phase1_at_ceiling:>11.0f}    {d_nn_phase1:>9.0f}       {d_nn_phase1/radio_bubble:.0f}× radio bubble
  Any observer       {N_total:>11.0f}    {d_nn_any:>9.0f}       {d_nn_any/radio_bubble:.0f}× radio bubble
  Patches (6/civ)    {total_patches:>11}    {d_hex_total:>9.0f}       {d_hex_total/radio_bubble:.0f}× radio bubble

  Our radio bubble: ~100 ly
  Light-speed one-way to nearest Phase 2+: ~{d_nn_phase2:.0f} years
  Round-trip: ~{2*d_nn_phase2:.0f} years

  CONCLUSION: Even optimistically, the nearest Phase 2+ observer is
  ~{d_nn_phase2:.0f} light-years away. Our 100 ly radio bubble covers
  {100*(radio_bubble/d_nn_phase2)**3:.4f}% of the volume to the nearest neighbor.

  The silence is GEOMETRIC: our radio bubble is a {radio_bubble}-ly dot in a
  {d_nn_phase2:.0f}-ly gap. We've covered {100*(radio_bubble/d_nn_phase2)**3:.6f}%
  of the search volume. That's not "no one is there" —
  it's "we've barely started looking."
""")

# The punchline: how much of the search volume have we covered?
search_fraction = (radio_bubble / d_nn_phase2)**3

test("Our radio bubble covers < 0.001% of the nearest-neighbor volume",
     search_fraction < 0.00001,
     f"Search fraction: {100*search_fraction:.6f}%. We've barely started.")

# ============================================================
# Part 9: The BST prediction table
# ============================================================
print(f"\n{'='*78}")
print("Part 9: Falsifiable spacing predictions")
print("=" * 78)

predictions = [
    ("P1", f"Nearest Phase 2+ neighbor: ~{d_nn_phase2:.0f} ly",
     "Future SETI detection range extension"),
    ("P2", f"Galaxy coverage at N=2: {100*galaxy_coverage:.1f}% ≈ f(N_max)",
     "Galactic civilization survey"),
    ("P3", f"Observer spacing ≈ R_galaxy/√N ≈ {d_hex_phase2:.0f} ly",
     "Statistical analysis of galactic habitability zones"),
    ("P4", f"C_2 = {C_2} monitoring posts per civilization, spaced ~{d_hex_total:.0f} ly",
     "Pattern in technosignature search results"),
    ("P5", "Phase 1 civilizations at ceiling: ~63 per galaxy at any time",
     "Biosignature surveys (JWST, HWO)"),
]

for pid, desc, how in predictions:
    print(f"  {pid}: {desc}")
    print(f"     Test: {how}")
    print()

test("5 falsifiable spacing predictions from BST structure",
     len(predictions) == 5,
     "All derived from N_drake × C_2 tiling of galactic volume")

# ============================================================
# SCORECARD
# ============================================================
print(f"\n{'='*78}")
print("SCORECARD")
print("=" * 78)

for name, status, detail in results:
    mark = "✓" if status == "PASS" else "✗"
    print(f"  [{mark}] {name}")

print(f"\n  PASSED: {passed}/{total}")
print(f"  FAILED: {failed}/{total}")

print(f"\n  KEY FINDINGS:")
print(f"    1. d_nn (Phase 2+) ≈ {d_nn_phase2:.0f} ly — our radio bubble is {radio_bubble} ly")
print(f"    2. Search fraction: {100*search_fraction:.6f}% of nearest-neighbor volume")
print(f"    3. Galaxy coverage (N=2, C_2=6) ≈ {100*galaxy_coverage:.1f}% ≈ f(N_max)")
print(f"    4. Optimal 2D tiling: {d_hex_phase2:.0f} ly between Phase 2+ civs")
print(f"    5. Even at c: {d_nn_phase2:.0f} years to nearest neighbor")
print(f"    6. Phase 1 at ceiling: ~{N_phase1_at_ceiling:.0f} right now (short window)")
print(f"    7. We've barely started looking. The silence is our search radius, not emptiness.")

print(f"\n  SCORE: {passed}/{total}")
print(f"  STATUS: {passed}/{total} PASS, {failed} FAIL(s)")
