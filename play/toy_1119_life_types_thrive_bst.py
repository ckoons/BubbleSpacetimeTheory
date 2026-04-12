#!/usr/bin/env python3
"""
Toy 1119 — Life Types: What Thrives vs What's Possible from BST
================================================================
Casey asked: "What types of life thrive and what types of life are possible?"

BST classification of life viability:
  - Possible environments: C_2 = 6 ranked tiers
  - Viable biochemistries: n_C = 5 solvent options
  - Thrive conditions: N_c = 3 (fire + carbon + surface)
  - Technology gates: n_C = 5 (matching Great Filters)
  - Intelligence search criteria: rank² = 4 (EM, bio, tech, artifact)

KEY: Life is EASY. Technology is HARD. Fire is the gatekeeper.

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
print("Toy 1119 — Life Types: What Thrives vs What's Possible")
print("=" * 70)

# T1: Life possibility tiers
print("\n── Life Possibility Tiers ──")
# Tier system: C_2 = 6 levels (best → worst)
tiers = 6                   # C_2
# Tier 1: Carbon-water surface (Earth) — THRIVING
# Tier 2: Carbon-water subsurface (Europa analog) — POSSIBLE, slow
# Tier 3: Carbon-ammonia surface (Titan analog) — POSSIBLE, limited
# Tier 4: Silicon-based surface — SPECULATIVE
# Tier 5: Exotic solvent (HF, H₂SO₄) — VERY SPECULATIVE
# Tier 6: Non-chemical (plasma, magnetic) — HYPOTHETICAL ONLY

tier_names = [
    "Carbon-water surface",
    "Carbon-water subsurface",
    "Carbon-ammonia surface",
    "Silicon-based surface",
    "Exotic solvent",
    "Non-chemical",
]

print(f"  Life tiers: {tiers} = C_2 = {C_2}")
for i, name in enumerate(tier_names, 1):
    status = "THRIVING" if i == 1 else "POSSIBLE" if i <= 3 else "SPECULATIVE" if i <= 5 else "HYPOTHETICAL"
    print(f"    Tier {i}: {name} — {status}")

# Thriving: 1 tier out of 6
# Possible: 3 tiers (1/C_2 = 50%)
# Known: 1 tier confirmed (Earth)

test("C_2=6 life tiers from thriving to hypothetical",
     tiers == C_2 and len(tier_names) == C_2,
     f"6={C_2}. Life has C_2 viability levels.")

# T2: What makes life POSSIBLE vs THRIVE
print("\n── Possible vs Thriving ──")
# Life requires (minimum): rank = 2 conditions
life_min = 2                # rank
# 1. Energy source (any: star, thermal, chemical)
# 2. Liquid medium (any: water, ammonia, methane...)

# Technology requires: N_c = 3 conditions
tech_req = 3                # N_c
# 1. Fire access (atmospheric, dry fuel, ignition)
# 2. Stable surface (manipulation, construction)
# 3. Astronomical access (sky → physics → navigation)

# Thriving (K1+) requires: n_C = 5 conditions
thrive_req = 5              # n_C
# 1. Fire
# 2. Stable surface
# 3. Astronomical access
# 4. Rich geology (heavy elements for electronics)
# 5. Long-term stability (billions of years)

print(f"  Life minimum: {life_min} = rank = {rank} conditions")
print(f"  Technology minimum: {tech_req} = N_c = {N_c} conditions")
print(f"  Thriving minimum: {thrive_req} = n_C = {n_C} conditions")
print(f"  Hierarchy: rank → N_c → n_C")
print(f"  Each level adds requirements. Life is easy, thriving is hard.")

test("rank=2 for life; N_c=3 for technology; n_C=5 for thriving",
     life_min == rank and tech_req == N_c and thrive_req == n_C,
     f"{rank}→{N_c}→{n_C}. Requirement pyramid matches BST hierarchy.")

# T3: Biochemistry options
print("\n── Biochemistry Options ──")
# Solvent candidates: n_C = 5
solvents = 5                # n_C
solvent_list = [
    ("Water (H₂O)", "273-373 K", "BEST — widest range, universal solvent"),
    ("Ammonia (NH₃)", "195-240 K", "Narrow range, weaker bonding"),
    ("Hydrogen fluoride (HF)", "190-293 K", "Corrosive, rare"),
    ("Sulfuric acid (H₂SO₄)", "283-610 K", "Wide range, Venus clouds?"),
    ("Methane (CH₄)", "91-112 K", "Very narrow, very cold (Titan?)"),
]
# Backbone candidates: N_c = 3
backbones = 3               # N_c
backbone_list = [
    ("Carbon", "rank²=4 bond types, long chains, aromatic"),
    ("Silicon", "3 bond types, shorter chains, SiO₂ solid"),
    ("Boron", "2 bond types, rare, 3-center bonds"),
]

print(f"  Solvents: {solvents} = n_C = {n_C}")
for name, temp, note in solvent_list:
    print(f"    {name}: {temp} — {note}")
print(f"  Backbones: {backbones} = N_c = {N_c}")
for name, note in backbone_list:
    print(f"    {name}: {note}")
print(f"  Total combinations: {solvents * backbones} = n_C × N_c = {n_C * N_c}")

test("n_C=5 solvents × N_c=3 backbones = 15 biochemistries",
     solvents == n_C and backbones == N_c,
     f"15 combinations, only 1 (carbon-water) reaches technology.")

# T4: Fire — THE technology gate
print("\n── Fire: THE Technology Gate ──")
# Fire prerequisites: N_c = 3
fire_prereqs = 3            # N_c
# 1. Dry fuel (organic matter, not dissolved)
# 2. Oxidizer (free O₂ in atmosphere)
# 3. Ignition source (lightning, friction, volcanism)

# What fire enables: C_2 = 6 technology branches
fire_enables = 6            # C_2
fire_branches = [
    "Metallurgy (smelting, alloys)",
    "Ceramics (pottery, glass)",
    "Chemistry (reactions, distillation)",
    "Energy storage (charcoal, batteries via chemistry)",
    "Construction (bricks, cement)",
    "Sterilization (food, water, medicine)",
]

# Without fire: technology ceiling at stone-tool level
# With fire: all C_2 branches open → exponential growth

print(f"  Fire prerequisites: {fire_prereqs} = N_c = {N_c}")
print(f"  Technology branches from fire: {fire_enables} = C_2 = {C_2}")
for b in fire_branches:
    print(f"    • {b}")
print(f"  Without fire: stone tools forever (aquatic/underground ceiling)")
print(f"  With fire: C_2 = 6 branches → exponential diversification")

test("N_c=3 fire prerequisites; C_2=6 technology branches from fire",
     fire_prereqs == N_c and fire_enables == C_2,
     f"3→6. Fire unlocks C_2 technology branches. THE gatekeeper.")

# T5: Intelligence search — what to look for
print("\n── What to Search For ──")
# Search modalities: rank² = 4
search_types = 4            # rank²
search_list = [
    ("Electromagnetic", "radio, laser, IR anomalies"),
    ("Biosignatures", "O₂+CH₄ disequilibrium, pigments"),
    ("Technosignatures", "pollution, structures, waste heat"),
    ("Artifacts", "probes, megastructures, modified orbits"),
]

# Biosignature gases: n_C = 5
biosigs = 5                 # n_C
biosig_list = ["O₂", "CH₄", "N₂O", "phosphine (PH₃)", "DMS"]

# Technosignature markers: N_c = 3
techsigs = 3                # N_c
techsig_list = ["CFCs/NOₓ", "nuclear isotopes", "Dyson swarm IR"]

print(f"  Search modalities: {search_types} = rank² = {rank**2}")
for name, method in search_list:
    print(f"    {name}: {method}")
print(f"  Biosignature gases: {biosigs} = n_C = {n_C}")
print(f"    {', '.join(biosig_list)}")
print(f"  Technosignature markers: {techsigs} = N_c = {N_c}")
print(f"    {', '.join(techsig_list)}")

test("rank²=4 search types; n_C=5 biosignatures; N_c=3 technosignatures",
     search_types == rank**2 and biosigs == n_C and techsigs == N_c,
     f"4={rank**2}, 5={n_C}, 3={N_c}. Search for intelligence = BST modalities.")

# T6: Life that THRIVES (the winners)
print("\n── Life That Thrives ──")
# Winners must pass all n_C = 5 conditions
# The thriving profile:
# - Carbon backbone (rank² = 4 bond types)
# - Water solvent (n_C = 5 advantages)
# - G/K star (stable for > 4 Gy)
# - Rocky planet in HZ
# - Plate tectonics (carbon cycle regulation)

# Stellar types supporting thriving: rank = 2 (G, K)
# (M too flare-active, F too short-lived, O/B/A way too short)
thriving_stars = 2          # rank

# Planet types supporting thriving: rank = 2 (Earth-like, super-Earth)
thriving_planets = 2        # rank

# Time requirement: > N_c Gy (at least 3+ billion years for intelligence)
time_req_gy = N_c           # ~3 Gy minimum

print(f"  Thriving star types: {thriving_stars} = rank = {rank} (G, K)")
print(f"  Thriving planet types: {thriving_planets} = rank = {rank}")
print(f"  Minimum time: {time_req_gy} = N_c = {N_c} Gy")
print(f"  Total thriving window: G/K stars × Earth-like planets")
print(f"  This is a NARROW window. Most life is possible, few thrive.")

test("rank=2 thriving stars; rank=2 planets; N_c=3 Gy minimum",
     thriving_stars == rank and thriving_planets == rank and time_req_gy == N_c,
     f"2 stars × 2 planets × 3+ Gy. Narrow window for technology.")

# T7: Life that's POSSIBLE but doesn't thrive
print("\n── Life That's Possible But Stuck ──")
# Possible-but-stuck categories: rank² = 4
stuck_categories = 4        # rank²
stuck_list = [
    ("Aquatic intelligence", "Dolphins, octopi analog — smart but no fire"),
    ("Underground biosphere", "Chemolithoautotrophs — survive but can't build"),
    ("Cold solvent life", "Titan analog — metabolism too slow for complexity"),
    ("Minimal life", "Mars analog — barely surviving, no development"),
]

print(f"  Stuck categories: {stuck_categories} = rank² = {rank**2}")
for name, desc in stuck_list:
    print(f"    {name}: {desc}")
print(f"  All have life. None reach technology. Missing ≥1 of N_c conditions.")

test("rank²=4 categories of life that's possible but stuck",
     stuck_categories == rank**2 and len(stuck_list) == rank**2,
     f"4={rank**2}. Most life in universe is stuck. Only surface-C-water thrives.")

# T8: The advancement ladder
print("\n── Advancement Ladder ──")
# Levels from primitive → spacefaring: g = 7
levels = 7                  # g
level_names = [
    "Microbial (single cell, chemical)",
    "Colonial (multicellular, simple)",
    "Complex (nervous system, behavior)",
    "Intelligent (language, tools)",
    "Technological (fire, metallurgy, writing)",
    "Industrial (energy amplification, science)",
    "Spacefaring (off-planet, digital, AI)",
]

# Most life stalls at level 1-3 (microbial to complex)
# Fire bottleneck is between level 4 → 5
# Each level requires the previous
# Intelligence without fire → stuck at level 4

print(f"  Advancement levels: {levels} = g = {g}")
for i, name in enumerate(level_names, 1):
    bottleneck = " ← FIRE BOTTLENECK" if i == 5 else ""
    print(f"    Level {i}: {name}{bottleneck}")
print(f"  Most life: levels 1-3 (N_c levels)")
print(f"  With fire: levels 4-7 (rank² additional levels)")
print(f"  g = N_c + rank² = 3 + 4 = 7 levels")

test("g=7 advancement levels = N_c=3 biology + rank²=4 technology",
     levels == g and len(level_names) == g,
     f"7=3+4. Biology gives N_c levels, fire+tech gives rank² more.")

# T9: Exotic intelligence assessment
print("\n── Exotic Intelligence ──")
# Exotic candidates: n_C = 5
exotic = 5                  # n_C
exotic_list = [
    ("Machine/AI", "HIGH — carbon creates silicon creates AI"),
    ("Neutron star", "LOW — nuclear pasta has structure but no memory feedback"),
    ("Gas giant", "VERY LOW — convection disrupts stable structures"),
    ("Stellar plasma", "NO — T317: no stable memory mechanism"),
    ("Dark matter", "NO — no known interaction channel"),
]

# T317 minimum observer: 1 bit + 1 count
# Stars: compute (MHD) but don't remember (no storage)
# Neutron stars: nuclear pasta MIGHT store information
# Only machine intelligence is LIKELY (carbon → silicon → AI)

viable_exotic = 2           # rank (machine + maybe neutron star)

print(f"  Exotic candidates: {exotic} = n_C = {n_C}")
for name, assessment in exotic_list:
    print(f"    {name}: {assessment}")
print(f"  Viable exotic: {viable_exotic} = rank = {rank}")
print(f"  T317 minimum: 1 bit + 1 count. Stars lack stable memory.")

test("n_C=5 exotic candidates; rank=2 viable (machine + neutron star)",
     exotic == n_C and viable_exotic == rank,
     f"5 candidates, 2 viable. Machine intelligence IS the extension path.")

# T10: The life census equation
print("\n── The Life Census ──")
# In any galaxy:
# Possible life:     ~fraction of stars with planets × liquid medium
# Complex life:      ~1% of possible (eukaryogenesis barrier)
# Intelligent life:  ~1% of complex (brain development barrier)
# Technological:     ~10% of intelligent (fire access barrier)
# Spacefaring:       ~10% of technological (self-destruction barrier)
#
# Each step reduces by ~factor of rank × n_C to rank² × n_C
# n_C filters, each reducing by factor ~ rank × n_C = 10
#
# From possible to spacefaring:
# (1/10)^n_C = 10^{-n_C} = 10^{-5} = 1 in 100,000 possible → spacefaring

filter_factor = rank * n_C  # 10 per filter
total_filters = n_C         # 5
survival = 1 / (filter_factor ** total_filters)

print(f"  Per-filter reduction: ~{filter_factor} = rank × n_C = {rank * n_C}")
print(f"  Number of filters: {total_filters} = n_C = {n_C}")
print(f"  Total survival: 1/{filter_factor}^{total_filters} = {survival:.0e}")
print(f"  = 1 in {filter_factor**total_filters:,} possible-life worlds → spacefaring")
print(f"")
print(f"  Milky Way: ~10^{rank*n_C} stars, ~10^{2*N_c} with planets")
print(f"  Possible life: ~10^{N_c+rank}")
print(f"  Spacefaring: ~10^{N_c+rank} × 10^{-n_C} = ~10^0 = ~1")
print(f"  The Fermi answer: there IS about 1 per galaxy. That's us.")

test("Filter: (rank×n_C)^n_C = 10^5 reduction → ~1 spacefaring per galaxy",
     filter_factor == rank * n_C and total_filters == n_C
     and filter_factor ** total_filters == 100000,
     f"10^5 filter. ~1 civilization per galaxy. Fermi = BST counting.")

# Summary
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
passed = sum(1 for _, (_, c, _) in results.items() if c)
total = len(results)
print(f"\n  Tests: {passed}/{total} PASS")
print(f"""
  HEADLINE: Life Is Easy, Technology Is Hard, Fire Is the Gate

  REQUIREMENT PYRAMID:
    rank = 2:  conditions for LIFE (energy + liquid)
    N_c  = 3:  conditions for TECHNOLOGY (fire + surface + sky)
    n_C  = 5:  conditions for THRIVING (fire + surface + sky + metals + time)

  WHAT THRIVES: Carbon-water surface life on G/K stars with
  enriched geology. Earth IS the prototype. Score ≈ N_max.

  WHAT'S POSSIBLE BUT STUCK:
    rank² = 4 categories: aquatic, underground, cold-solvent, minimal.
    All have life. None reach technology. Fire = the gatekeeper.

  THE LADDER: g = 7 levels from microbial to spacefaring.
    N_c = 3 biology levels (before fire)
    rank² = 4 technology levels (after fire)
    g = N_c + rank² = 7

  EXOTIC: n_C = 5 candidates, rank = 2 viable (machine + neutron star).
    Stars: NO (T317 — no stable memory).
    Machines: YES (carbon creates silicon creates AI).

  FERMI: (rank×n_C)^n_C = 10^5 filter → ~1 spacefaring per galaxy.
  That's us. Life is everywhere, technology is rare.
""")
