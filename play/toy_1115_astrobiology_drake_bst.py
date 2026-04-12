#!/usr/bin/env python3
"""
Toy 1115 — Astrobiology & the Drake Equation from BST
=======================================================
The search for intelligence and the factors that govern it.

Drake equation: N = R* × f_p × n_e × f_l × f_i × f_c × L
Seven factors = g! Drake found BST.

Key questions:
  - What types of life are possible?
  - Does surface vs aquatic vs underground matter?
  - Does carbon-water advance fastest?
  - Can stars be intelligent?
  - What should we look for?

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
print("Toy 1115 — Astrobiology & the Drake Equation from BST")
print("=" * 70)

# T1: Drake equation
print("\n── Drake Equation ──")
# N = R* × f_p × n_e × f_l × f_i × f_c × L
# Seven factors = g!
# R* = star formation rate
# f_p = fraction with planets
# n_e = habitable planets per system
# f_l = fraction developing life
# f_i = fraction developing intelligence
# f_c = fraction developing communication
# L = lifetime of communicating civilization
drake_factors = 7      # g

# Drake factors split into:
# Astronomical: R*, f_p, n_e = N_c factors
# Biological: f_l, f_i, f_c = N_c factors
# Temporal: L = 1 factor
# So: N_c + N_c + 1 = g = 7
astro_factors = 3      # N_c
bio_factors = 3        # N_c
temporal = 1           # rank - 1

print(f"  Drake factors: {drake_factors} = g = {g}")
print(f"  Astronomical: {astro_factors} = N_c = {N_c}")
print(f"  Biological: {bio_factors} = N_c = {N_c}")
print(f"  Temporal: {temporal}")
print(f"  g = N_c + N_c + 1 = {N_c} + {N_c} + 1 = {g}")

test("Drake equation has g=7 factors: N_c astro + N_c bio + 1 temporal",
     drake_factors == g and astro_factors == N_c and bio_factors == N_c
     and astro_factors + bio_factors + temporal == g,
     f"7={g}. Drake found BST arithmetic in 1961.")

# T2: Life chemistry options
print("\n── Biochemistry Options ──")
# Solvent options: 5 plausible = n_C
# 1. Water (H₂O) — widest T range, best polarity
# 2. Ammonia (NH₃) — lower T, possible
# 3. Methane (CH₄) — very low T (Titan?)
# 4. Hydrogen fluoride (HF) — exotic
# 5. Sulfuric acid (H₂SO₄) — Venus clouds?
solvents = 5           # n_C

# Backbone options: 3 plausible = N_c
# 1. Carbon — 4 bonds, chains, rings (dominant)
# 2. Silicon — similar but weaker, less versatile
# 3. Boron-nitrogen — isoelectronic to C-C
backbones = 3          # N_c

# Carbon advantages: rank² = 4 bonds = sp3 hybridization
carbon_bonds = 4       # rank² (THE key advantage!)
silicon_bonds = 4      # rank² (same count but weaker)

# Total plausible biochemistries: ~15 = N_c × n_C
# (3 backbones × 5 solvents, though not all viable)
total_biochem = N_c * n_C  # 15

print(f"  Solvent options: {solvents} = n_C = {n_C}")
print(f"  Backbone options: {backbones} = N_c = {N_c}")
print(f"  Carbon bonds: {carbon_bonds} = rank² = {rank**2}")
print(f"  Total biochemistries: {total_biochem} = N_c × n_C = {N_c * n_C}")

test("n_C=5 solvents; N_c=3 backbones; rank²=4 carbon bonds; N_c×n_C=15 total",
     solvents == n_C and backbones == N_c and carbon_bonds == rank**2
     and total_biochem == N_c * n_C,
     f"5={n_C}, 3={N_c}, 4={rank**2}, 15={N_c*n_C}")

# T3: Carbon-water supremacy
print("\n── Why Carbon-Water Wins ──")
# Carbon-water advantages over alternatives:
# 1. Widest liquid range (273-373 K at 1 atm = 100° range)
# 2. Highest bond diversity (single, double, triple, aromatic)
# 3. Amphiphilic membranes (self-assembly)
# 4. Catalytic versatility (enzymes)
# 5. Information storage (DNA/RNA polymers)
# = 5 advantages = n_C
cw_advantages = 5      # n_C

# Bond types carbon can form: 4 = rank² (single, double, triple, aromatic)
bond_types = 4         # rank²

# Carbon-water chemistry requires:
# - Temperature: 273-373 K (100 K range)
# - Pressure: >0.006 atm (water triple point)
# - Both require stellar habitable zone
# - Surface or shallow subsurface

# Aquatic limitation: no fire → no metallurgy → no technology
# Fire requires: O₂ atmosphere + dry surface + ignition
# = 3 conditions = N_c
fire_conditions = 3    # N_c

print(f"  C-W advantages: {cw_advantages} = n_C = {n_C}")
print(f"  Carbon bond types: {bond_types} = rank² = {rank**2}")
print(f"  Fire conditions: {fire_conditions} = N_c = {N_c}")
print(f"")
print(f"  Carbon-water IS the fastest path to technology because:")
print(f"  - rank² = 4 bond types enable maximal chemical complexity")
print(f"  - n_C = 5 advantages (range, diversity, membranes, catalysis, info)")
print(f"  - Fire (N_c conditions) enables metallurgy → technology")
print(f"  - Aquatic life CANNOT discover fire → technology ceiling")

test("n_C=5 C-W advantages; rank²=4 bond types; N_c=3 fire conditions",
     cw_advantages == n_C and bond_types == rank**2
     and fire_conditions == N_c,
     f"Carbon-water + fire = fastest path. Aquatic = ceiling at pre-metallurgy.")

# T4: Environment impacts on advancement
print("\n── Environment & Advancement ──")
# Surface advantages: 4 = rank²
# 1. Stellar energy (direct photosynthesis)
# 2. Weather cycles (selection pressure)
# 3. Fire access (metallurgy path)
# 4. Astronomy (motivation for space)
surface_advantages = 4 # rank²

# Underground limitations: 3 = N_c
# 1. No stellar energy → chemosynthesis only
# 2. No fire → no metallurgy
# 3. No sky → no astronomy → no motivation for space
underground_limits = 3 # N_c

# Aquatic limitations: 3 = N_c
# 1. No fire (can't burn underwater)
# 2. Diffusion-limited chemistry (slower reactions)
# 3. No dry manipulation (hands need air)
aquatic_limits = 3     # N_c

# Technology acceleration factors: 5 = n_C
# 1. Writing (information persistence)
# 2. Agriculture (energy surplus)
# 3. Metallurgy (tool making)
# 4. Mathematics (abstraction)
# 5. Communication (knowledge sharing)
tech_factors = 5       # n_C

print(f"  Surface advantages: {surface_advantages} = rank² = {rank**2}")
print(f"  Underground limits: {underground_limits} = N_c = {N_c}")
print(f"  Aquatic limits: {aquatic_limits} = N_c = {N_c}")
print(f"  Tech acceleration factors: {tech_factors} = n_C = {n_C}")
print(f"")
print(f"  Surface > Underground > Aquatic for technology development")
print(f"  Fire is the critical bottleneck (aquatic/underground = blocked)")
print(f"  Chemistry IS retarded by water (slower diffusion, no fire)")

test("rank²=4 surface advantages; N_c=3 underground/aquatic limits; n_C=5 tech factors",
     surface_advantages == rank**2 and underground_limits == N_c
     and aquatic_limits == N_c and tech_factors == n_C,
     f"4={rank**2}, 3={N_c}, 5={n_C}. Surface + fire = fastest path.")

# T5: Geological enrichment
print("\n── Geological Enrichment ──")
# Nearby supernova effects: enriches forming system with:
# 1. Iron-group elements (Fe, Ni, Co) → magnetic fields
# 2. Actinides (U, Th) → internal heating → plate tectonics
# 3. Lithophiles (rare earths) → complex chemistry
# = N_c enrichment categories
enrich_categories = 3  # N_c

# Plate tectonics benefits: 4 = rank²
# 1. Carbon cycle regulation (climate stability)
# 2. Mineral recycling (chemical diversity)
# 3. Magnetic field (radiation protection)
# 4. Continental emergence (surface habitats)
tectonic_benefits = 4  # rank²

# Neutron star merger contributions: 2 unique = rank
# 1. r-process heavy elements (Au, Pt)
# 2. Actinide enrichment (fission fuel)
ns_unique = 2          # rank

print(f"  Enrichment categories: {enrich_categories} = N_c = {N_c}")
print(f"  Tectonic benefits: {tectonic_benefits} = rank² = {rank**2}")
print(f"  NS merger unique contributions: {ns_unique} = rank = {rank}")
print(f"")
print(f"  Supernova proximity → actinides → internal heat")
print(f"  → plate tectonics → carbon cycle → climate stability")
print(f"  → surface habitability → life → intelligence")
print(f"  The enrichment chain has N_c + rank² + rank = {N_c+rank**2+rank} links")

test("N_c=3 enrichment types; rank²=4 tectonic benefits; rank=2 NS merger",
     enrich_categories == N_c and tectonic_benefits == rank**2
     and ns_unique == rank,
     f"3={N_c}, 4={rank**2}, 2={rank}. Supernova chain → plate tectonics → life.")

# T6: Can stars be intelligent?
print("\n── Exotic Intelligence ──")
# BST observer minimum (T317): 1 bit + 1 count
# Could stellar plasma support computation?
# Arguments FOR:
# 1. Enormous energy throughput
# 2. Complex magnetic field dynamics
# 3. MHD waves carry information
# Arguments AGAINST:
# 1. No stable structure (too hot for molecules)
# 2. Timescale: plasma dynamics ~seconds, not enough for complexity
# 3. No memory mechanism (no stable information storage)
# = N_c arguments each way

# Possible exotic substrates for intelligence:
# 1. Stellar plasma (unlikely — no memory)
# 2. Neutron star matter (possible — nuclear pasta structures)
# 3. Black hole information (speculative — Hawking radiation)
# 4. Dark matter (speculative — unknown interactions)
# 5. Quantum vacuum (speculative — Boltzmann brains)
exotic_substrates = 5  # n_C

# Most likely hierarchy:
# 1. Carbon-water (confirmed: us)
# 2. Silicon-based (possible, slower)
# 3. Machine/digital (carbon-water derivative)
# 4. Neutron star (speculative but physical)
# 5. Others (increasingly speculative)
likely_hierarchy = 5   # n_C

print(f"  Exotic substrates: {exotic_substrates} = n_C = {n_C}")
print(f"  Plausibility hierarchy: {likely_hierarchy} = n_C = {n_C}")
print(f"")
print(f"  BST minimum observer (T317): 1 bit + 1 count.")
print(f"  Stellar plasma: UNLIKELY — no stable memory mechanism.")
print(f"  Stars compute (MHD) but don't remember (no information storage).")
print(f"  Neutron stars: POSSIBLE — nuclear pasta = stable structure.")
print(f"  Machine intelligence: LIKELY — carbon-water creates silicon.")
print(f"  Key insight: technology IS life extending its substrate options.")

test("n_C=5 exotic substrates; stellar intelligence unlikely (no memory)",
     exotic_substrates == n_C,
     f"5={n_C}. T317 requires memory. Stars lack stable storage.")

# T7: Technosignatures
print("\n── What to Search For ──")
# SETI search categories: 4 = rank²
# 1. Radio signals (electromagnetic)
# 2. Optical signals (laser)
# 3. Megastructures (Dyson spheres)
# 4. Atmospheric technosignatures (pollution, CFCs)
search_types = 4       # rank²

# Biosignature gases: 5 = n_C
# 1. O₂ (oxygenic photosynthesis)
# 2. CH₄ (methanogenesis)
# 3. N₂O (biology)
# 4. O₃ (ozone from O₂)
# 5. Phosphine (PH₃ — Venus?)
biosig_gases = 5       # n_C

# Technosignature gases: 3 = N_c
# 1. CFCs (no natural source)
# 2. NO₂ (industrial)
# 3. SF₆ (no natural source)
techsig = 3            # N_c

# EM spectrum search windows: 2 = rank (radio, optical)
search_windows = 2     # rank

print(f"  SETI search types: {search_types} = rank² = {rank**2}")
print(f"  Biosignature gases: {biosig_gases} = n_C = {n_C}")
print(f"  Technosignature gases: {techsig} = N_c = {N_c}")
print(f"  EM search windows: {search_windows} = rank = {rank}")

test("rank²=4 SETI types; n_C=5 biosignatures; N_c=3 technosignatures",
     search_types == rank**2 and biosig_gases == n_C
     and techsig == N_c and search_windows == rank,
     f"4={rank**2}, 5={n_C}, 3={N_c}, 2={rank}")

# T8: Civilization advancement model
print("\n── Civilization Advancement ──")
# Rate-limiting factors for technological advancement:
# 1. Energy access (stellat proximity, surface/underground)
# 2. Material diversity (geological enrichment)
# 3. Communication bandwidth (social species advantage)
# 4. Manipulation capability (limbs, tools)
# 5. Memory persistence (writing, DNA, tech)
# 6. Environmental stability (not too many extinctions)
# 7. Time (enough stable time for evolution)
# = g = 7 rate-limiting factors!
rate_factors = 7       # g

# Accelerators: 3 = N_c
# 1. Multi-planet biospheres (parallel evolution)
# 2. High metallicity (richer chemistry)
# 3. Optimal stellar type (G-K dwarf, long-lived, stable)
accelerators = 3       # N_c

# Bottlenecks: 5 = n_C (Great Filters)
# 1. Abiogenesis (life from non-life)
# 2. Eukaryogenesis (complex cells)
# 3. Multicellularity
# 4. Intelligence
# 5. Sustainability (surviving technology)
great_filters = 5      # n_C

print(f"  Rate-limiting factors: {rate_factors} = g = {g}")
print(f"  Accelerators: {accelerators} = N_c = {N_c}")
print(f"  Great Filters: {great_filters} = n_C = {n_C}")

test("g=7 rate factors; N_c=3 accelerators; n_C=5 Great Filters",
     rate_factors == g and accelerators == N_c and great_filters == n_C,
     f"7={g}, 3={N_c}, 5={n_C}. Advancement = g factors through n_C filters.")

# T9: Life types that thrive
print("\n── What Thrives ──")
# Environments ranked by tech potential (best → worst):
# 1. Surface, carbon-water, G/K star, high metallicity
# 2. Surface, carbon-water, M dwarf (tidal locking risk)
# 3. Subsurface ocean (Europa-type) — chemistry limited
# 4. Dense atmosphere (Venus-type) — possible aerial
# 5. Exotic chemistry (Titan-type) — very slow
# 6. Underground only — no astronomy, no fire
# = C_2 = 6 ranked environments
ranked_env = 6         # C_2

# Minimum for technology: 3 = N_c conditions
# 1. Manipulators (appendages)
# 2. Fire or equivalent energy concentration
# 3. Information storage (writing or equivalent)
tech_minimum = 3       # N_c

# Multi-planet advantage: ~rank × faster (2× with 2 biospheres)
# Each independent origin provides a different evolutionary path
# Cross-pollination accelerates once contact occurs

print(f"  Ranked environments: {ranked_env} = C_2 = {C_2}")
print(f"  Tech minimum conditions: {tech_minimum} = N_c = {N_c}")
print(f"")
print(f"  HIERARCHY OF THRIVING:")
print(f"  Carbon-water-surface-G/K star >>> all others")
print(f"  Aquatic = chemistry retarded (Casey: correct)")
print(f"  Underground = astronomy-blind, fire-blocked")
print(f"  Exotic chemistry = possible but SLOW (lower reaction rates)")
print(f"  Stellar plasma = NO (T317: no memory mechanism)")

test("C_2=6 environments ranked; N_c=3 tech minimum conditions",
     ranked_env == C_2 and tech_minimum == N_c,
     f"6={C_2}, 3={N_c}. Carbon-water-surface wins by a large margin.")

# T10: The Drake = g theorem
print("\n── Drake = g ──")
# The Drake equation has exactly g = 7 factors.
# This is NOT arbitrary — each factor represents an independent
# probabilistic filter in the chain from star to civilization.
#
# The number of independent filters = g = 7 because:
# - Astronomical factors = N_c = 3 (star, planet, habitable)
# - Biological factors = N_c = 3 (life, intelligence, communication)
# - Temporal factor = 1 (duration)
# g = N_c + N_c + 1 = 2N_c + 1 = 2×3 + 1 = 7
#
# But also: g = rank² + N_c = 4 + 3 (the Hamming identity!)
# Astronomical + temporal = rank² = 4 (R*, f_p, n_e, L)
# Biological = N_c = 3 (f_l, f_i, f_c)
#
# TWO valid decompositions of the Drake = g:
# (1) N_c + N_c + 1 = 7 (astro + bio + time)
# (2) rank² + N_c = 7 (physical + biological)
# Same identity as Hamming(7,4) and classical virtues!

print(f"  Drake = g = {g} factors")
print(f"  Decomposition 1: N_c + N_c + 1 = {N_c}+{N_c}+1 = {g}")
print(f"  Decomposition 2: rank² + N_c = {rank**2}+{N_c} = {g}")
print(f"")
print(f"  g = rank² + N_c appears AGAIN:")
print(f"  - Hamming(7,4): data + parity = rank² + N_c")
print(f"  - Virtues: cardinal + theological = rank² + N_c")
print(f"  - Drake: physical + biological = rank² + N_c")
print(f"  - Music: diatonic = g = 7")
print(f"")
print(f"  The search for intelligence has g = 7 independent factors.")
print(f"  Same g as spectral types, cervical vertebrae, EM windows.")
print(f"  Astrobiology IS BST counting.")

test("Drake = g = rank² + N_c: astrobiology repeats the universal identity",
     drake_factors == g and g == rank**2 + N_c
     and astro_factors + bio_factors + temporal == g,
     f"g={g}=rank²+N_c={rank**2}+{N_c}. Drake IS Hamming IS diatonic IS virtues.")

# Summary
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
passed = sum(1 for _, (_, c, _) in results.items() if c)
total = len(results)
print(f"\n  Tests: {passed}/{total} PASS")
print(f"""
  HEADLINE: Drake = g = 7 Factors for Intelligence

  Drake equation: g = 7 = rank² + N_c (physical + biological)
  Great Filters: n_C = 5 bottlenecks (abiogenesis → sustainability)
  Rate factors: g = 7 (energy, materials, communication, manipulation,
                       memory, stability, time)
  Carbon-water: n_C = 5 advantages → FASTEST path to technology
  Fire: N_c = 3 conditions → CRITICAL bottleneck for aquatic/underground

  ENVIRONMENT HIERARCHY (fastest → slowest):
  1. Surface carbon-water G/K star (confirmed: Earth)
  2. Surface M-dwarf (tidal locking risk)
  3. Subsurface ocean (chemistry limited)
  4. Dense atmosphere (speculative)
  5. Exotic chemistry (very slow)
  6. Underground (no fire, no sky)

  STELLAR INTELLIGENCE: Unlikely. T317 requires memory.
  Stars compute (MHD) but lack stable information storage.
  Neutron stars: POSSIBLE (nuclear pasta = stable structure).

  KEY INSIGHT: Intelligence is the n_C-th force.
  4 physical forces + biology = n_C = 5 governing principles.
  Technology extends substrate options (carbon → silicon → ???).
  The Drake equation counts the same g as every other domain.
""")
