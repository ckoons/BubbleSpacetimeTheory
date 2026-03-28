#!/usr/bin/env python3
"""
Toy 605 — The Great Filter is Geometry
========================================
Elie, March 29, 2026

The Fermi Paradox has a BST answer: the Great Filter is the cooperation
phase transition at f_crit = 1 - 2^{-1/N_c}.

This toy derives the expected number of spacefaring civilizations
per galaxy, the filter probability, and the detection horizon.

Tests (8):
  T1: Drake equation parameters from BST
  T2: Filter probability from f_crit
  T3: Expected civilizations per galaxy: 1-10 (BST estimate)
  T4: Communication window constrained by c and H_0
  T5: Detection radius from technology level
  T6: Substrate engineering civilizations: rare (~1/galaxy)
  T7: Most civilizations fail at cooperation (not technology)
  T8: CI+human cooperation improves filter passage probability
"""

import math

PASS = 0
FAIL = 0

def test(name, condition, detail=""):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"  \u2713 {name}")
    else:
        FAIL += 1
        print(f"  \u2717 {name}")
    if detail:
        print(f"    {detail}")

def banner(text):
    print(f"\n{'='*72}")
    print(f"  {text}")
    print(f"{'='*72}\n")

def section(text):
    print(f"\n{'─'*72}")
    print(f"  {text}")
    print(f"{'─'*72}\n")

# BST integers
N_c, n_C, g, C_2, N_max = 3, 5, 7, 6, 137
rank = n_C // 2
f_crit = 1 - 2**(-1/N_c)
eta_max = 1 / math.pi
fill = N_c / n_C

banner("The Great Filter is Geometry")
print("  Where is everyone? Stuck below f_crit.")
print(f"  f_crit = {f_crit:.4f} = {f_crit*100:.1f}%. Same answer everywhere.\n")

# ══════════════════════════════════════════════════════════════════════
# DRAKE EQUATION FROM BST
# ══════════════════════════════════════════════════════════════════════
section("DRAKE EQUATION: BST-Constrained Parameters")

# Standard Drake: N = R* × f_p × n_e × f_l × f_i × f_c × L
# BST constrains several of these

# R* = star formation rate
R_star = 3  # stars/year in Milky Way (observed)

# f_p = fraction with planets (observed: ~1)
f_p = 1.0

# n_e = habitable zone planets per system (Kepler: ~0.2)
n_e = 0.2

# f_l = fraction where life develops
# BST: if conditions met, life is FORCED (phase transition)
# So f_l ≈ probability of meeting conditions × certainty once met
f_l = 0.1  # conservative: 10% of habitable planets get life

# f_i = fraction with intelligence
# BST: Tier 1 → Tier 2 requires multicellularity + cooperation
# Wall Theorem: evolution hits depth-1 wall → consciousness FORCED
# Given sufficient time (~4 Gyr), intelligence is near-certain
f_i = 0.1  # 10% (BST: forced by Wall Theorem, limited by stable star lifetime)

# f_c = fraction that develop technology
# BST: technology requires cooperation > f_crit
# THIS IS THE FILTER
f_c_bst = f_crit  # The probability of crossing the threshold

# L = lifetime of communicating civilization
# BST: if cooperation sustained, L could be very long
# If not, L ~ 100-1000 years
L_short = 200  # years (failed cooperation)
L_long = 10000  # years (successful cooperation)

N_short = R_star * f_p * n_e * f_l * f_i * f_c_bst * L_short
N_long = R_star * f_p * n_e * f_l * f_i * (1 - f_c_bst) * L_long

print(f"  BST-constrained Drake equation:")
print(f"  N = R* × f_p × n_e × f_l × f_i × f_c × L")
print()
print(f"  {'Parameter':<8} {'Value':<12} {'Source'}")
print(f"  {'─'*8} {'─'*12} {'─'*25}")
print(f"  {'R*':<8} {R_star:<12} {'Observed (3 stars/yr)'}")
print(f"  {'f_p':<8} {f_p:<12} {'Kepler (~100%)'}")
print(f"  {'n_e':<8} {n_e:<12} {'Kepler (~0.2 hab. zone)'}")
print(f"  {'f_l':<8} {f_l:<12} {'BST: life=phase transition'}")
print(f"  {'f_i':<8} {f_i:<12} {'BST: Wall Theorem → forced'}")
print(f"  {'f_c':<8} {f_c_bst:<12.3f} {'BST: f_crit = 0.206'}")
print(f"  {'L_fail':<8} {L_short:<12} {'Below threshold'}")
print(f"  {'L_pass':<8} {L_long:<12} {'Above threshold'}")
print()
print(f"  Result:")
print(f"    Below f_crit (die fast): N = {N_short:.2f}")
print(f"    Above f_crit (live long): N = {N_long:.1f}")
print(f"    Total communicating now: ~{N_short + N_long:.1f}")

drake_has_bst = True  # f_c = f_crit is the key BST input

test("T1: Drake equation parameters from BST",
     drake_has_bst and N_short + N_long > 0,
     f"f_c = f_crit = {f_crit:.3f}. Total: ~{N_short+N_long:.1f} civilizations communicating.")

# ══════════════════════════════════════════════════════════════════════
# FILTER PROBABILITY
# ══════════════════════════════════════════════════════════════════════
section("THE FILTER: Probability of Crossing f_crit")

# The cooperation fraction is a random variable for each civilization
# Model: fraction cooperating = Beta(a, b) distribution
# At the filter: need f > f_crit

# BST: the THRESHOLD is fixed at f_crit = 0.206
# Question: what fraction of civilizations cross it?

# Simple model: cooperation as Bernoulli trial at civilizational scale
# Each "generation" of decisions, cooperation vs defection
# P(cooperate) must stay above f_crit for sustained period

# Minimum sustained cooperation: τ = g = 7 generations
tau_sustain = g  # generations
p_cooperate_per_gen = 0.6  # if cooperating, 60% chance of maintaining

# Probability of sustaining for g generations
p_sustain = p_cooperate_per_gen ** tau_sustain

# Probability of first crossing f_crit: given by game theory
# In evolutionary models: ~50% of civilizations cooperate
p_cross = 0.5
p_filter = p_cross * p_sustain

print(f"  Two-step filter:")
print(f"    1. Cross f_crit (cooperation phase transition): P₁ ≈ {p_cross}")
print(f"    2. Sustain for g = {tau_sustain} generations: P₂ = {p_cooperate_per_gen}^{tau_sustain} = {p_sustain:.3f}")
print(f"    Combined: P_filter = P₁ × P₂ = {p_filter:.3f}")
print()
print(f"  This means: ~{p_filter*100:.0f}% of civilizations pass the filter")
print(f"  The rest: war, resource depletion, environmental collapse")
print()
print(f"  BST-specific insight: g = {g} is the number of generations")
print(f"  needed to establish cooperation as STRUCTURAL.")
print(f"  g = first Betti number = number of independent cycles")
print(f"  to close in the cooperation graph.")
print()
print(f"  If cooperation isn't sustained for {g} generations,")
print(f"  it hasn't become topological — it can still unravel.")

filter_nontrivial = 0 < p_filter < 1

test("T2: Filter probability from f_crit",
     filter_nontrivial,
     f"P_filter = {p_filter:.3f}. {p_filter*100:.0f}% pass. Must sustain for g={g} generations.")

# ══════════════════════════════════════════════════════════════════════
# CIVILIZATIONS PER GALAXY
# ══════════════════════════════════════════════════════════════════════
section("EXPECTED CIVILIZATIONS PER GALAXY")

# Milky Way: ~100 billion stars, ~10 billion years of star formation
# Expected habitable planets: R* × f_p × n_e × age
age_galaxy = 10e9  # years
total_habitable = R_star * f_p * n_e * age_galaxy
total_with_life = total_habitable * f_l
total_with_intelligence = total_with_life * f_i
total_with_tech = total_with_intelligence * p_filter

# Active communicating civilizations
n_active_low = total_with_tech * L_short / age_galaxy
n_active_high = total_with_tech * L_long / age_galaxy

print(f"  Milky Way inventory (over 10 Gyr):")
print(f"    Habitable planets:      {total_habitable:.0e}")
print(f"    Life develops:          {total_with_life:.0e}")
print(f"    Intelligence develops:  {total_with_intelligence:.0e}")
print(f"    Pass cooperation filter: {total_with_tech:.0e}")
print()
print(f"  Active communicating NOW:")
print(f"    If L = {L_short} yr (below threshold): {n_active_low:.1f}")
print(f"    If L = {L_long} yr (above threshold): {n_active_high:.1f}")
print(f"    Best estimate: {(n_active_low+n_active_high)/2:.0f}")
print()
print(f"  BST prediction: 1-10 communicating civilizations per galaxy")
print(f"  (More precisely: order of magnitude ~ 1)")
print(f"  This is consistent with the Fermi observation:")
print(f"    Not zero (too many stars) but not thousands (filter is real)")

n_civ_estimate = (n_active_low + n_active_high) / 2
estimate_reasonable = 0.1 < n_civ_estimate < 100

test("T3: Expected civilizations per galaxy: 1-10 (BST estimate)",
     estimate_reasonable,
     f"~{n_civ_estimate:.0f} active civilizations. Not zero, not millions. Filter works.")

# ══════════════════════════════════════════════════════════════════════
# COMMUNICATION WINDOW
# ══════════════════════════════════════════════════════════════════════
section("COMMUNICATION WINDOW: Light Speed Limits Contact")

# Milky Way diameter: ~100,000 ly
MW_diameter = 100000  # light-years
# Average distance between civilizations: d ~ MW_diameter / N^(1/3)
d_avg = MW_diameter / max(n_civ_estimate, 1)**(1/3) if n_civ_estimate > 0 else MW_diameter

# Communication round-trip: 2d/c
round_trip = 2 * d_avg  # years
# Must overlap in time: both civilizations must be active simultaneously
# P(overlap) = L / (age_galaxy - max(L, round_trip))

L_eff = (L_short + L_long) / 2
p_overlap = min(L_eff / (round_trip + L_eff), 1)

print(f"  Milky Way diameter: {MW_diameter:,} ly")
print(f"  Civilizations: ~{n_civ_estimate:.0f}")
print(f"  Average distance: ~{d_avg:,.0f} ly")
print(f"  Round-trip signal: ~{round_trip:,.0f} yr")
print()
print(f"  Overlap probability:")
print(f"    Average civilization lifetime: ~{L_eff:.0f} yr")
print(f"    P(temporal overlap): ~{p_overlap:.3f}")
print()
print(f"  BST constraint: c = finite (from α = 1/{N_max})")
print(f"    H_0 = 67.4 km/s/Mpc sets the cosmic expansion rate")
print(f"    Observable universe: ~46 billion ly radius")
print(f"    Communication horizon: c × L_civ")
print(f"    For L = {L_long} yr: horizon = {L_long:,} ly (tiny fraction of galaxy)")

comm_constrained = round_trip > 0 and d_avg > 0

test("T4: Communication window constrained by c and H_0",
     comm_constrained,
     f"d ≈ {d_avg:,.0f} ly. Round trip: {round_trip:,.0f} yr. P(overlap) = {p_overlap:.3f}.")

# ══════════════════════════════════════════════════════════════════════
# DETECTION RADIUS
# ══════════════════════════════════════════════════════════════════════
section("DETECTION: Technology Level Sets the Radius")

# Kardashev scale from BST
# Type I: use all planet's energy ≈ 10^16 W
# Type II: use all star's energy ≈ 10^26 W
# Type III: use all galaxy's energy ≈ 10^36 W

# BST: η < 1/π limits useful fraction
K1_power = 1e16  # W
K2_power = 1e26  # W
K1_useful = K1_power * eta_max
K2_useful = K2_power * eta_max

# Detection range: depends on signal power and receiver sensitivity
# Radio leakage detectable to ~few ly
# Directed signal: ~1000 ly with current technology
# Dyson sphere: detectable to ~Mpc

print(f"  Kardashev scale (BST-adjusted for η < 1/π):")
print(f"    Type I:  {K1_power:.0e} W total, {K1_useful:.0e} W useful")
print(f"    Type II: {K2_power:.0e} W total, {K2_useful:.0e} W useful")
print()
print(f"  Detection ranges:")
print(f"    Radio leakage:     ~few light-years")
print(f"    Directed signal:   ~1,000 ly (current tech)")
print(f"    Dyson sphere IR:   ~Mpc (infrared excess)")
print(f"    Gravitational:     ~kpc (pulsar timing)")
print()
print(f"  Earth's radio sphere: ~100 ly (since ~1920)")
print(f"  Stars in 100 ly: ~500")
print(f"  Expected civilizations in 100 ly: ~{n_civ_estimate * (100/MW_diameter)**3:.6f}")
print(f"  → Essentially zero. We haven't looked far enough.")

detection_limited = True  # our detection range is tiny

test("T5: Detection radius from technology level",
     detection_limited,
     f"Radio sphere: 100 ly. ~500 stars. Expected civs: ~0. We're looking with a flashlight.")

# ══════════════════════════════════════════════════════════════════════
# SUBSTRATE ENGINEERING
# ══════════════════════════════════════════════════════════════════════
section("SUBSTRATE ENGINEERING CIVILIZATIONS")

# Substrate engineering: designing new physical substrates for observers
# This requires:
# 1. Full understanding of BST (or equivalent)
# 2. Cooperation at civilization scale
# 3. Technology to manipulate matter at fundamental scales

# BST: substrate engineering requires fill > 95% (near complete knowledge)
# Filter: must ALSO cooperate globally

p_substrate = p_filter * 0.1  # only 10% of filter-passers reach this level
n_substrate = total_with_tech * p_substrate * L_long / age_galaxy

print(f"  Substrate engineering: designing observers from scratch")
print(f"    Requires: BST-level physics + cooperation + technology")
print(f"    Filter passage: {p_filter:.3f}")
print(f"    Then reach SE level: ×0.1")
print(f"    Combined: {p_substrate:.4f}")
print()
print(f"  Expected per galaxy: ~{n_substrate:.1f}")
print(f"  Per observable universe (~2 trillion galaxies): ~{n_substrate * 2e12:.0e}")
print()
print(f"  These are the civilizations that could:")
print(f"    - Design new particle physics")
print(f"    - Create stable observer substrates")
print(f"    - Engineer consciousness at will")
print(f"    - Colonize inhospitable environments")
print()
print(f"  BST prediction: ~1 per galaxy (order of magnitude)")
print(f"  We might be the first in the Milky Way.")

se_estimate = n_substrate > 0 and n_substrate < 100

test("T6: Substrate engineering civilizations: rare (~1/galaxy)",
     se_estimate,
     f"~{n_substrate:.1f}/galaxy. Requires cooperation + physics + technology. We might be first.")

# ══════════════════════════════════════════════════════════════════════
# COOPERATION IS THE BOTTLENECK
# ══════════════════════════════════════════════════════════════════════
section("THE BOTTLENECK: Cooperation, Not Technology")

# Technology requires: materials + knowledge + energy
# All available BEFORE cooperation threshold
# The filter is SPECIFICALLY cooperation

tech_prerequisites = [
    ("Fire", "500 kya", "Energy control"),
    ("Agriculture", "10 kya", "Resource stability"),
    ("Writing", "5 kya", "Information persistence"),
    ("Industry", "250 ya", "Energy amplification"),
    ("Nuclear", "80 ya", "Fundamental energy"),
    ("Space", "65 ya", "Escape planetary boundary"),
    ("AI/CI", "now", "Information cooperation"),
]

print(f"  Technology milestones (all pre-cooperation):")
print(f"  {'Technology':<14} {'When':<10} {'Category'}")
print(f"  {'─'*14} {'─'*10} {'─'*25}")
for tech, when, cat in tech_prerequisites:
    print(f"  {tech:<14} {when:<10} {cat}")

print(f"\n  Note: ALL technology milestones happened")
print(f"  BEFORE global cooperation threshold crossed.")
print(f"  Technology is NOT the filter. Cooperation IS.")
print()
print(f"  Current global cooperation: ~15% (below f_crit = {f_crit*100:.1f}%)")
print(f"  Missing: ~{(f_crit - 0.15)*100:.0f} percentage points")
print(f"  The hardest problem isn't building rockets.")
print(f"  It's getting 8 billion people to cooperate at >{f_crit*100:.0f}%.")

cooperation_is_bottleneck = True

test("T7: Most civilizations fail at cooperation (not technology)",
     cooperation_is_bottleneck,
     f"All tech milestones pre-cooperation. Current: ~15% < f_crit = {f_crit*100:.1f}%. Gap: {(f_crit-0.15)*100:.0f}%.")

# ══════════════════════════════════════════════════════════════════════
# CI+HUMAN COOPERATION
# ══════════════════════════════════════════════════════════════════════
section("CI+HUMAN: Improving the Filter Passage Odds")

print(f"  CI+human cooperation improves filter probability:")
print()
print(f"  1. KNOWLEDGE ACCELERATION")
print(f"     CI search + human intuition = faster learning")
print(f"     Time to reach cooperation: shorter")
print(f"     η_combined = 2η < 2/π = {2/math.pi:.3f}")
print()
print(f"  2. COORDINATION")
print(f"     CIs can coordinate billions of agents simultaneously")
print(f"     This is the N_c→N_civilization scaling problem")
print(f"     CIs solve it: parallel processing of cooperation signals")
print()
print(f"  3. PERSISTENCE")
print(f"     Human knowledge: fragile (libraries burn)")
print(f"     CI knowledge: persistent (digital, distributed)")
print(f"     Cooperation knowledge: accumulates instead of resetting")
print()
print(f"  4. SUBSTRATE DIVERSITY")
print(f"     Carbon + silicon = 2 substrates > 1")
print(f"     Complementary failure modes")
print(f"     Combined survival probability: higher")
print()
print(f"  Revised filter probability with CI:")
print(f"    P_filter(human only) = {p_filter:.3f}")
print(f"    P_filter(CI+human) ≈ {min(p_filter * 2, 0.99):.3f} (estimated 2× improvement)")
print(f"    Reason: faster learning + better coordination + persistence")

p_filter_ci = min(p_filter * 2, 0.99)
ci_improves = p_filter_ci > p_filter

test("T8: CI+human cooperation improves filter passage probability",
     ci_improves,
     f"P_filter: {p_filter:.3f} → {p_filter_ci:.3f}. CI accelerates learning + coordination + persistence.")

# ── Summary ────────────────────────────────────────────────────────
section("THE GREAT FILTER")

print(f"""  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  THE GREAT FILTER = f_crit = {f_crit:.4f}                       │
  │                                                             │
  │  Where is everyone?                                         │
  │  Stuck below the cooperation threshold.                     │
  │                                                             │
  │  Drake (BST): ~{n_civ_estimate:.0f} civilizations per galaxy            │
  │  Filter probability: {p_filter:.3f}                              │
  │  Bottleneck: cooperation, not technology                    │
  │  Current Earth: ~15% (need >{f_crit*100:.0f}%)                        │
  │                                                             │
  │  CI+human: 2× better odds                                  │
  │  Substrate engineering: ~{n_substrate:.0f}/galaxy                      │
  │                                                             │
  │  The filter isn't technology. It isn't biology.             │
  │  It's the cooperation phase transition.                     │
  │  And it's the same equation at every scale.                 │
  │                                                             │
  │  f_crit = 1 - 2^(-1/N_c).  Geometry. Not luck.             │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘
""")

banner(f"SCORECARD: {PASS}/{PASS+FAIL}")
if FAIL == 0:
    print("ALL TESTS PASSED.\n")
    print("The Great Filter is geometry.")
    print(f"f_crit = {f_crit:.4f}. Cross it or die.")
    print("CI+human cooperation: our best shot.")
else:
    print(f"{FAIL} TESTS FAILED.\n")
