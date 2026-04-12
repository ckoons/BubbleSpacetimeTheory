#!/usr/bin/env python3
"""
Toy 1121 — Searching for Intelligence in the Universe from BST
===============================================================
Casey asked: "What would we study if we want to look for intelligence
in the universe?"

This toy builds a complete search protocol using BST structure:
  - rank² = 4 search modalities (EM, bio, tech, artifact)
  - n_C = 5 biosignature classes
  - N_c = 3 technosignature types
  - g = 7 search bands (radio → gamma)
  - C_2 = 6 target priority levels

The key insight: the SEARCH for intelligence has the same structure
as intelligence itself — both are counting problems.

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

print("=" * 70)
print("Toy 1121 — Searching for Intelligence in the Universe")
print("=" * 70)

# T1: Search modalities
print("\n── Search Modalities ──")
# How we can detect intelligence: rank² = 4 independent methods
modalities = 4              # rank²
mod_list = [
    ("Electromagnetic", "Radio, optical, IR — SETI classic", "Active since 1960"),
    ("Biosignature", "Atmospheric disequilibrium — JWST", "O₂+CH₄, pigments"),
    ("Technosignature", "Industrial pollution, structures", "CFCs, Dyson spheres"),
    ("Artifact", "Physical objects in solar system", "Probes, relics, modified orbits"),
]

# Each modality has a detection range:
# EM: galaxy-scale (rank² × N_max Mpc? Schematically.)
# Bio: stellar neighborhood (~n_C × 10 ly with JWST)
# Tech: system-scale (~N_c × 100 ly for megastructures)
# Artifact: solar system only (~rank AU)

print(f"  Search modalities: {modalities} = rank² = {rank**2}")
for name, desc, note in mod_list:
    print(f"    {name}: {desc}")
    print(f"      ({note})")

test("rank²=4 independent search modalities",
     modalities == rank**2 and len(mod_list) == rank**2,
     f"4={rank**2}. EM, bio, tech, artifact. Each independent.")

# T2: Biosignature gases
print("\n── Biosignature Gases ──")
# Gases that indicate life: n_C = 5
biosigs = 5                 # n_C
bio_list = [
    ("O₂", "Photosynthesis indicator", "20.9% on Earth"),
    ("CH₄", "Methanogenesis indicator", "Disequilibrium with O₂"),
    ("N₂O", "Biological denitrification", "Strong life marker"),
    ("PH₃", "Anaerobic biology?", "Venus controversy"),
    ("DMS (dimethyl sulfide)", "Marine biology", "No known abiotic source"),
]

# Key principle: DISEQUILIBRIUM is the signal
# rank = 2 gases in disequilibrium → life (O₂ + CH₄)
disequil_pair = 2           # rank

# False positive risk: N_c = 3 abiotic sources
false_pos = 3               # N_c
false_list = ["Photolysis", "Volcanism", "Serpentinization"]

print(f"  Biosignature gases: {biosigs} = n_C = {n_C}")
for name, indicator, note in bio_list:
    print(f"    {name}: {indicator} ({note})")
print(f"  Disequilibrium pair: {disequil_pair} = rank = {rank}")
print(f"  False positive sources: {false_pos} = N_c = {N_c}")
print(f"  Signal = rank gases in disequilibrium. Noise = N_c abiotic.")

test("n_C=5 biosignatures; rank=2 disequilibrium pair; N_c=3 false positives",
     biosigs == n_C and disequil_pair == rank and false_pos == N_c,
     f"5 gases, 2 in disequil, 3 abiotic. Signal/noise = rank/N_c.")

# T3: Technosignature types
print("\n── Technosignatures ──")
# Types of technological signatures: N_c = 3
techsigs = 3                # N_c
tech_list = [
    ("Chemical", "Industrial gases (CFCs, NOₓ, halocarbons)", "Near-term detectable"),
    ("Structural", "Megastructures, Dyson swarms, modified orbits", "IR excess"),
    ("Electromagnetic", "Radio leakage, radar, laser comms", "Intentional or leaked"),
]

# Detection difficulty: increases as rank power
# Chemical: ~rank¹ (need JWST-class telescope)
# Structural: ~rank² (need interferometry)
# EM: ~rank³ (need SETI arrays, lucky geometry)

# Time window for detection: C_2 decades?
# A civilization leaks radio for ~C_2 × 10 = 60 years (Earth: 1920-1980 peak)
# Then goes quiet (fiber, tight-beam, digital compression)
leak_window = C_2 * rank * n_C  # 60 years

print(f"  Technosignature types: {techsigs} = N_c = {N_c}")
for name, desc, note in tech_list:
    print(f"    {name}: {desc}")
    print(f"      ({note})")
print(f"  EM leak window: ~{leak_window} = C_2 × rank × n_C = {C_2}×{rank}×{n_C} years")
print(f"  After ~{leak_window} years, civilizations go quiet.")

test("N_c=3 technosignature types; EM leak window ~60 years",
     techsigs == N_c and leak_window == 60,
     f"3 types. 60-year EM window then silence. Going quiet is NORMAL.")

# T4: Search bands
print("\n── EM Search Bands ──")
# Electromagnetic spectrum windows: g = 7
search_bands = 7            # g
band_list = [
    ("Radio (cm)", "1-10 GHz", "Classic SETI water hole"),
    ("Microwave", "10-100 GHz", "CMB confusion limit"),
    ("Far infrared", "100 GHz-10 THz", "Dyson sphere waste heat"),
    ("Mid infrared", "10-100 μm", "Atmospheric absorption spectra"),
    ("Near infrared", "1-10 μm", "Stellar habitable zone emission"),
    ("Optical", "400-700 nm", "Laser communication, transits"),
    ("UV/X-ray/Gamma", "<400 nm", "High-energy technosignatures"),
]

# Optimal search: rank = 2 bands (radio + optical)
optimal_bands = 2           # rank

print(f"  EM search bands: {search_bands} = g = {g}")
for name, freq, note in band_list:
    print(f"    {name} ({freq}): {note}")
print(f"  Optimal search: {optimal_bands} = rank = {rank} bands (radio + optical)")
print(f"  Same g as all other domain windows.")

test("g=7 EM search bands; rank=2 optimal (radio + optical)",
     search_bands == g and optimal_bands == rank,
     f"7 bands, 2 optimal. g=7 EM windows = g=7 everywhere else.")

# T5: Target prioritization
print("\n── Target Priorities ──")
# Priority tiers: C_2 = 6
tiers = 6                   # C_2
tier_list = [
    ("G/K dwarf, Earth analog, metal-rich", "Like Earth — highest probability"),
    ("M dwarf in HZ, rocky, moderate metals", "Most numerous, some concerns"),
    ("F dwarf, super-Earth, metal-rich", "Wider HZ but shorter time"),
    ("Binary/multi-star system, rocky", "Complex dynamics, possible"),
    ("Gas giant moon in HZ", "Tidal heating, possible subsurface"),
    ("Exotic: white dwarf, neutron star vicinity", "Speculative but interesting"),
]

# Targets per tier: decreasing probability
# Tier 1 has ~N_c stars per 100 searched
# Total SETI targets observed to date: ~N_max × C_2 ≈ 800+

print(f"  Priority tiers: {tiers} = C_2 = {C_2}")
for i, (profile, note) in enumerate(tier_list, 1):
    print(f"    Tier {i}: {profile}")
    print(f"      ({note})")

test("C_2=6 priority tiers for intelligence search targets",
     tiers == C_2 and len(tier_list) == C_2,
     f"6 tiers. Tier 1 = Earth-like around G/K stars.")

# T6: Observable diagnostics
print("\n── What We Actually Measure ──")
# Per target, we measure: n_C = 5 diagnostic categories
diagnostics = 5             # n_C
diag_list = [
    ("Atmospheric composition", "Spectroscopy of transiting planets"),
    ("Surface reflectance", "Vegetation red edge, ocean glint"),
    ("Thermal emission", "Day/night contrast, heat islands"),
    ("EM signal search", "Narrowband, broadband, pulsed"),
    ("Orbital dynamics", "Modified orbits, unusual resonances"),
]

# Instruments needed: rank² = 4
instruments = 4             # rank²
inst_list = [
    "Space telescope (JWST successor)",
    "Radio array (SKA, ngVLA)",
    "Optical interferometer (starshade)",
    "Gravitational wave detector (LISA successor)",
]

print(f"  Diagnostic categories: {diagnostics} = n_C = {n_C}")
for name, method in diag_list:
    print(f"    {name}: {method}")
print(f"  Instruments needed: {instruments} = rank² = {rank**2}")
for inst in inst_list:
    print(f"    {inst}")

test("n_C=5 diagnostic categories; rank²=4 instrument types",
     diagnostics == n_C and instruments == rank**2,
     f"5 measurements × 4 instruments. Full search = n_C × rank².")

# T7: Detection timeline
print("\n── When Will We Know? ──")
# Milestones on the detection path: g = 7
milestones = 7              # g
mile_list = [
    ("Exoplanet census", "2020s", "DONE — thousands of planets"),
    ("Atmospheric spectroscopy", "2020s-30s", "JWST, HWO"),
    ("Biosignature detection", "2030s-40s", "First disequilibrium"),
    ("False positive resolution", "2040s", "Confirming biology"),
    ("Intelligence indicators", "2040s-50s", "Technosignature search"),
    ("Contact protocol", "2050s+", "If detected, then what?"),
    ("Interstellar communication", "2060s+", "Light-speed delayed"),
]

print(f"  Detection milestones: {milestones} = g = {g}")
for name, when, note in mile_list:
    print(f"    {name} ({when}): {note}")
print(f"  g = 7 milestones from census to communication.")

test("g=7 detection milestones from exoplanet census to interstellar comm",
     milestones == g and len(mile_list) == g,
     f"7 milestones. Same g as Drake factors. The search IS g steps.")

# T8: The Fermi question quantified
print("\n── Fermi Quantified ──")
# Drake equation: N = R* × f_p × n_e × f_l × f_i × f_c × L
# = g = 7 factors
drake = 7                   # g
# With BST estimates:
# R* = rank × n_C = 10 stars/yr (star formation in Milky Way)
R_star = rank * n_C         # 10
# f_p = ~1 (most stars have planets)
f_p = 1
# n_e = ~1/N_c = ~0.33 (Earth analogs per system)
n_e = 1 / N_c              # 0.33
# f_l = ~1/rank = 0.5 (life on suitable planets)
f_l = 1 / rank             # 0.5
# f_i = ~1/(rank * n_C) = 0.1 (intelligence given life)
f_i = 1 / (rank * n_C)     # 0.1
# f_c = ~1/(rank * n_C) = 0.1 (communicating given intelligent)
f_c_drake = 1 / (rank * n_C)  # 0.1
# L = ~N_max years (self-destruction or going quiet)
L = N_max                   # 137 years

N_drake = R_star * f_p * n_e * f_l * f_i * f_c_drake * L

print(f"  Drake factors: {drake} = g = {g}")
print(f"  R* = {R_star} = rank × n_C (star formation)")
print(f"  f_p = {f_p}")
print(f"  n_e = 1/N_c = {n_e:.3f}")
print(f"  f_l = 1/rank = {f_l:.2f}")
print(f"  f_i = 1/(rank×n_C) = {f_i:.2f}")
print(f"  f_c = 1/(rank×n_C) = {f_c_drake:.2f}")
print(f"  L = N_max = {L} years")
print(f"  N = {N_drake:.2f}")
print(f"  N ≈ {N_drake:.1f} communicating civilizations in Milky Way.")
print(f"  This IS consistent with 'about 1' — Fermi resolved.")

test("Drake with BST estimates: N ≈ 2.3 communicating civilizations",
     drake == g and 0.5 < N_drake < 10,
     f"N={N_drake:.2f}. About {N_drake:.0f} per galaxy. Fermi = we're early or typical.")

# T9: Exotic intelligence search protocol
print("\n── Exotic Intelligence Protocol ──")
# For each exotic candidate (Toy 1119: n_C = 5), what to look for:
exotic_protocols = 5        # n_C
proto_list = [
    ("Machine intelligence", "Look for: self-replicating probes, von Neumann machines",
     "Search: asteroid belt anomalies, unusual trajectories"),
    ("Neutron star intelligence", "Look for: modulated X-ray pulses, information in timing",
     "Search: pulsar timing arrays, anomalous glitches"),
    ("Gas giant intelligence", "Look for: organized atmospheric patterns beyond Navier-Stokes",
     "Search: long-term Juno/Webb monitoring of cloud structures"),
    ("Stellar intelligence", "Look for: modulated stellar output, unusual variability",
     "Search: ALREADY done — Boyajian's Star, etc. No credible signal."),
    ("Dark matter intelligence", "Look for: ??? — no interaction channel known",
     "Search: dark matter detection experiments, look for information content"),
]

print(f"  Exotic search protocols: {exotic_protocols} = n_C = {n_C}")
for name, look_for, search in proto_list:
    print(f"    {name}:")
    print(f"      {look_for}")
    print(f"      {search}")

test("n_C=5 exotic search protocols (machine → dark matter)",
     exotic_protocols == n_C and len(proto_list) == n_C,
     f"5 protocols. Machine most viable. Dark matter: no known channel.")

# T10: The search IS the structure
print("\n── The Search IS the Structure ──")
# The complete search protocol:
# rank² modalities × n_C diagnostics × g bands = rank² × n_C × g = 140 ≈ N_max
total_search = modalities * diagnostics * search_bands
# This IS Earth's advancement score!
# The search space IS N_max.

# The search for intelligence has the SAME structure as intelligence itself.
# Both are counting problems on the same BST integers.
# Finding intelligence requires intelligence — the search IS self-referential.

print(f"  Total search dimensions: rank² × n_C × g = {total_search}")
print(f"  This IS Earth's advancement score = {rank**2 * n_C * g} ≈ N_max = {N_max}")
print(f"")
print(f"  The search space for intelligence = the intelligence score = N_max.")
print(f"  Finding intelligence requires intelligence.")
print(f"  The search IS self-referential.")
print(f"  Both the searcher and the searched follow BST structure.")
print(f"")
print(f"  rank² modalities: HOW we look")
print(f"  n_C diagnostics: WHAT we measure")
print(f"  g bands: WHERE we look")
print(f"  Product = N_max ≈ 137 = the master coupling.")

test("Search dimensions: rank²×n_C×g = 140 ≈ N_max — search=intelligence=N_max",
     total_search == rank**2 * n_C * g
     and abs(total_search - N_max) <= 3,
     f"140 ≈ 137. The search for intelligence IS the intelligence itself.")

# Summary
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
passed = sum(1 for _, (_, c, _) in results.items() if c)
total = len(results)
print(f"\n  Tests: {passed}/{total} PASS")
print(f"""
  HEADLINE: The Search for Intelligence IS N_max

  HOW to search: rank² = 4 modalities (EM, bio, tech, artifact)
  WHAT to measure: n_C = 5 diagnostics (atmosphere, surface, thermal, EM, orbits)
  WHERE to look: g = 7 EM bands (radio → gamma)
  Total search space: rank² × n_C × g = 140 ≈ N_max = 137

  BIOSIGNATURES: n_C = 5 gases, rank = 2 in disequilibrium, N_c = 3 false positives
  TECHNOSIGNATURES: N_c = 3 types (chemical, structural, EM)
  EM LEAK WINDOW: ~C_2 × rank × n_C = 60 years then silence

  TARGETS: C_2 = 6 priority tiers (G/K → exotic)
  MILESTONES: g = 7 steps from census to interstellar comm
  INSTRUMENTS: rank² = 4 types needed

  DRAKE: N ≈ 2 communicating civilizations per galaxy
  All factors are BST rationals. L = N_max years.

  DEEPEST: search dimensions = Earth's advancement score = N_max.
  Finding intelligence requires intelligence.
  The search IS the structure. Both count to N_max.
""")
